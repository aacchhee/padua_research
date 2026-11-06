#!/usr/bin/env python3
"""Measured external/native comparisons after M4/M2; no stability theorem.

External NN errors include the H+d0 moment lift at 140/220 dps.
The d0 anchor uses binary64 arithmetic on that run's actual input weights.
Native data are read from C3's pinned raw run, never recomputed here.
"""
import argparse,csv,hashlib,json,platform,sys,time,struct
from pathlib import Path
import numpy as np
import mpmath as mp
from c4_normalization import ROOT,load,monic_hessenberg,affine_monic
from c4_lift import lift

BASE=ROOT/'topics/nn-mop-iep-20261103/code/c4_float_baseline.py'
b=load('comparison_base',BASE)
FIELDS=('a1','a2','b1','b2')
METHODS=('C4','A-LU','A-QR','B-nodeqr','CORE','KRYL','REORTH')


def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def mp_matrix(H):return [[mp.mpf(x) for x in row] for row in H]


def frombits(bits):
    return [struct.unpack('>d',bytes.fromhex(bits[k:k+16]))[0] for k in range(0,len(bits),16)]


def bitmatrix(bits,N):
    values=frombits(bits)
    if len(values)!=N*N:raise ValueError('matrix bit count')
    return [[mp.mpf(values[i+N*j]) for j in range(N)] for i in range(N)]


def distance(A,B):
    # Subtract in high precision before the binary64 spectral-norm evaluation.
    delta=np.array([[float(a-b) for a,b in zip(r,s)] for r,s in zip(A,B)])
    return float(np.linalg.norm(delta,2)/np.linalg.norm(np.array(B,float),2))


def normed_error(got,ref):
    fields={k:mp.fdiv(max(abs(got[nu][k]-r[k]) for nu,r in ref.items()),
                       max(abs(r[k]) for r in ref.values())) for k in FIELDS}
    return float(max(fields.values())),{k:float(v) for k,v in fields.items()}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--external',type=Path,required=True)
    ap.add_argument('--native',type=Path,required=True);ap.add_argument('--raw',type=Path,required=True)
    ap.add_argument('--evidence',type=Path,required=True);a=ap.parse_args()
    ext=json.loads(a.external.read_text());native=json.loads(a.native.read_text())['cases']
    native={(r['family'],r['N']):r for r in native}
    rows=[];started=time.time();input_matches=[]
    with mp.workdps(220):
        refs={}
        for f in ('krawtchouk','hahn'):
            for N in range(4,33):
                ref,_=b.compute(N,f,220);refs[f,N]=ref
        for inp in ext:
            N,f,kind=inp['N'],inp['family'],inp['input_kind'];s=mp.mpf(N-1)/2
            ref=refs[f,N];Href=affine_monic(monic_hessenberg(ref,N),s,s)
            if kind=='shared_normalized':
                xq,wq=b.inputs(N,f)
                expected=dict(nodes=list(map(str,xq)),weights=[list(map(str,r)) for r in wq])
                input_sha=hashlib.sha256(json.dumps(expected,sort_keys=True).encode()).hexdigest()
                if input_sha!=native[f,N]['measurement']['input_sha256']:
                    raise ValueError('C3 rational input identity mismatch')
                observed=[float(v).hex() for key in ('nodes_bits','weights1_bits','weights2_bits') for v in frombits(inp[key])]
                desired=[float(v).hex() for v in xq]+[float(v).hex() for r in wq for v in r]
                if observed!=desired:raise ValueError('Octave/C3 binary64 input mismatch')
                input_matches.append(dict(family=f,N=N,input_sha256=input_sha,
                    binary64_hex_sha256=hashlib.sha256(json.dumps(observed).encode()).hexdigest()))
            # The exact desired family is the same rational data used in C3.
            row=dict(N=N,family=f,input_kind=kind,methods={})
            if kind=='shared_normalized':
                for method in METHODS[:4]:
                    co={tuple(nu):{k:mp.mpf(v) for k,v in r.items()}
                        for nu,r in native[f,N][method]['coefficients']}
                    E,fields=normed_error(co,ref)
                    row['methods'][method]=dict(status='ok',E_NN=E,fields=fields,
                        H_integer=distance(affine_monic(monic_hessenberg(co,N),s,s),Href),
                        output='native full NN',input_sha256=native[f,N]['measurement']['input_sha256'])
            z=np.array(frombits(inp['nodes_bits']),dtype=float);w=np.array([frombits(inp['weights1_bits']),frombits(inp['weights2_bits'])],dtype=float)
            # Actual input, not a reference NN coefficient or exact oracle anchor.
            d0=float(np.dot(z,w[1])/np.sum(w[1])-np.dot(z,w[0])/np.sum(w[0]))
            row['d0_binary64']=d0
            for method,r in inp['algorithms'].items():
                if r['status']!='ok':row['methods'][method]=r;continue
                H=bitmatrix(r['H_bits'],N)
                Hint=H if kind=='archive_integer' else affine_monic(H,s,s)
                Hz=affine_monic(H,1/s,-1) if kind=='archive_integer' else H
                anchor=mp.mpf(d0)/s if kind=='archive_integer' else mp.mpf(d0)
                result=dict(status='ok',H_integer=distance(Hint,Href),bior=r['bior'],
                    output='external monic H plus input-anchor high-precision functional lift')
                if inp['exact']:
                    result['source_generator_H_error']=distance(H,bitmatrix(inp['exact_bits'],N))
                lifts=[]
                try:
                    for dps in (140,220):
                        with mp.workdps(dps):
                            got,_=lift(Hz,anchor,b.layers)
                            lifts.append(got)
                    E,fields=normed_error(lifts[-1],ref)
                    precision,_=normed_error(lifts[0],lifts[-1])
                    result.update(E_NN=E,fields=fields,lift_precision_agreement=precision)
                    if precision>1e-50:result['status']='precision_unresolved'
                except (ArithmeticError,ZeroDivisionError,ValueError) as e:
                    result.update(status='lift_failed',lift_message=str(e))
                row['methods'][method]=result
            rows.append(row)
            print(f'{f} N{N} {kind} complete',file=sys.stderr,flush=True)
    raw=dict(cases=rows,platform=dict(python=platform.python_version(),numpy=np.__version__,mpmath=mp.__version__),
        binary64_input_matches=input_matches,files={str(p):digest(p) for p in (a.external,a.native,Path(__file__),Path(__file__).with_name('c4_lift.py'),Path(__file__).with_name('c4_normalization.py'),BASE)},wall_seconds=time.time()-started)
    a.raw.write_text(json.dumps(raw,indent=2,sort_keys=True)+'\n');a.evidence.mkdir(exist_ok=True,parents=True)
    for f in ('krawtchouk','hahn'):
        for method in METHODS:
            path=a.evidence/f'{f}-{method}.csv'
            with path.open('w') as stream:
                wr=csv.writer(stream);wr.writerow(['N','input_kind','status','a1','a2','b1','b2','E_NN','H_integer','lift_precision_agreement'])
                for row in rows:
                    if row['family']!=f or method not in row['methods']:continue
                    r=row['methods'][method]
                    vals=[r.get('fields',{}).get(k) for k in FIELDS]+[r.get('E_NN'),r.get('H_integer'),r.get('lift_precision_agreement')]
                    wr.writerow([row['N'],row['input_kind'],r['status']]+['' if v is None else f'{v:.9e}' for v in vals])
    failures=[dict(N=r['N'],family=r['family'],input_kind=r['input_kind'],method=k,status=v['status'])
              for r in rows for k,v in r['methods'].items() if v['status']!='ok']
    summary=dict(status='MEASURED',M4='PASS',M2='PASS',case_count=len(rows),failures=failures,
        binary64_input_equality_cases=len(input_matches),max_lift_precision_agreement=max(v.get('lift_precision_agreement',0) for r in rows for v in r['methods'].values()),
        platform=raw['platform'],raw=dict(path=str(a.raw),bytes=a.raw.stat().st_size,sha256=digest(a.raw)),
        input_files=raw['files'],tables={p.name:dict(bytes=p.stat().st_size,sha256=digest(p)) for p in sorted(a.evidence.glob('*.csv'))})
    (a.evidence.parent/'c4-comparison-receipt.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')


if __name__=='__main__':main()
