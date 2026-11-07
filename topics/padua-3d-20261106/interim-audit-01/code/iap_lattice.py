#!/usr/bin/env python3
"""Supplementary interim audit, pinned 5440555; exact lattice reruns.

Uses the frozen producer enumerator, with an independently written monomial
quotient/Fraction rank reducer. Alternate window/control mode explicitly
reuses the earlier independent checker; it is a fresh run, not new code.
"""
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import importlib.util
import itertools
import json
import math
from pathlib import Path
import platform
import subprocess
import sys
import time

PIN = '5440555cf326afdbd66b75bed195802013901c2d'
TOPIC = Path(__file__).resolve().parents[2]

def identity(path):
    path = Path(path)
    data = path.read_bytes()
    return {'path': str(path), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

def quotient(k, h):
    a,b,c,d,e,f = h
    u,r = divmod(k[0],a)
    v,s = divmod(k[1]-b*u,d)
    return r,s,(k[2]-c*u-e*v)%f

def rank(h,n):
    """Monomial Fourier columns, sparse Gaussian elimination over Q."""
    piv = {}
    for i in range(n+1):
        for j in range(n-i+1):
            for k in range(n-i-j+1):
                alpha=(i,j,k)
                col=Counter()
                for beta in itertools.product(*(range(t+1) for t in alpha)):
                    freq=tuple(t-2*s for t,s in zip(alpha,beta))
                    col[quotient(freq,h)]+=math.prod(math.comb(t,s) for t,s in zip(alpha,beta))
                col={x:Fraction(y) for x,y in col.items()}
                while col:
                    key=min(col)
                    val=col[key]
                    if key not in piv:
                        piv[key]={x:y/val for x,y in col.items()}
                        break
                    for x,y in piv[key].items():
                        z=col.get(x,0)-val*y
                        if z: col[x]=z
                        else: col.pop(x,None)
    return len(piv)

def folds(h):
    a,b,c,d,e,f=h
    q=a*d*f
    pts=[]
    for t in range(f):
        z=Fraction(t,f)
        for s in range(d):
            y=(s-e*z)/d
            for r in range(a):
                x=(r-b*y-c*z)/a
                pts.append(tuple(int(v*q)%q for v in (x,y,z)))
    assert len(set(pts))==q
    folded=Counter(tuple(min(v,q-v) for v in p) for p in pts)
    assert all(count<=8 for count in folded.values())
    return q,len(folded),max(folded.values())

def load_old():
    path=TOPIC/'code/r08_lattice_check.py'
    spec=importlib.util.spec_from_file_location('frozen_alternate_lattice',path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('mode',choices=['enumeration','alternate'])
    parser.add_argument('--scratch',type=Path,required=True)
    parser.add_argument('--receipt',type=Path,required=True)
    args=parser.parse_args()
    args.scratch.mkdir(parents=True,exist_ok=True)
    start=time.monotonic()
    result={'audit_pin':PIN,'model':'gpt-6-astra xhigh (assigned; runtime metadata unexposed)',
            'command':sys.argv,'python':platform.python_version(),'platform':platform.platform(),
            'source_identity':identity(__file__),'mode':args.mode,'rows':[]}
    if args.mode=='enumeration':
        source=TOPIC/'code/r08_lattice_enum.cpp'
        binary=args.scratch/'enum'
        compile_cmd=['g++','-O3','-std=c++17','-Wall','-Wextra',str(source),'-o',str(binary)]
        subprocess.run(compile_cmd,check=True)
        result.update(producer_source=identity(source),binary=identity(binary),compile_command=compile_cmd,
                      compiler=subprocess.check_output(['g++','--version'],text=True).splitlines()[0])
        cases=[(3,184,23,24,[(16,15,1),(20,17,20),(20,18,3),(22,18,68)]),
               (4,352,44,45,[(35,30,1),(39,33,3),(43,32,24)]),
               (5,592,74,75,[(54,48,1),(63,53,3),(72,53,3)]),
               (6,672,84,None,[]),(7,960,120,None,[])]
        for n,hi,cap,target,expected in cases:
            raw=args.scratch/f'full-n{n}.jsonl'
            assert not raw.exists()
            cmd=[str(binary),'complement',str(n),'1',str(hi),str(cap),str(raw)]
            subprocess.run(cmd,check=True)
            qs=[]; small=[]; summary=None
            for line in raw.read_text().splitlines():
                row=json.loads(line)
                if row['type']=='q': qs.append(row)
                elif row['type']=='small': small.append(row)
                elif row['type']=='summary': summary=row
            assert [r['q'] for r in qs]==list(range(1,hi+1)) and summary is not None
            hist=Counter()
            for row in small:
                q,m,fiber=folds(row['hnf'])
                assert q==row['q'] and m==row['fold']
                hist[m,rank(row['hnf'],n)]+=1
            observed=sorted((m,r,c) for (m,r),c in hist.items())
            assert observed==expected,(n,observed)
            assert sum(r['hnf_total'] for r in qs)==summary['hnf_total']
            assert sum(r['admissible'] for r in qs)==summary['admissible']
            record={'n':n,'complete_interval':[1,hi],'fold_cap':cap,'command':cmd,
                    'raw':identity(raw),'summary':summary,'independent_rank_histogram':observed,
                    'small_cases_recounted':len(small),'global_full_rank_target':target}
            if target:
                assert hi==8*(target-1)
                witness={3:(1,3,3,6,0,10),4:(4,0,5,5,5,10),5:(5,0,6,6,6,12)}[n]
                q,m,fiber=folds(witness)
                rw=rank(witness,n)
                assert m==target and rw==math.comb(n+3,3)
                record['attaining_witness']={'hnf':witness,'q':q,'fold':m,'rank':rw,'max_fiber':fiber}
            result['rows'].append(record)
            args.receipt.write_text(json.dumps(result,separators=(',',':'))+'\n')
            print(json.dumps({'n':n,'complete':True,'summary':summary,'histogram':observed}),flush=True)
    else:
        module=load_old()
        result['reused_alternate_source']=identity(TOPIC/'code/r08_lattice_check.py')
        result['versions']={'numpy':module.np.__version__,'sympy':module.sympy.__version__}
        result['controls']=module.controls()
        result['fold_controls']={'q_range':[1,16],'all_hnfs':0,'max_fiber':0}
        for q in range(1,17):
            for a,d,f in module.triples(q):
                for b,c,e in itertools.product(range(d),range(f),range(f)):
                    h=(a,b,c,d,e,f)
                    aq,m,fiber=folds(h)
                    oq,of=module.folding(h)
                    assert aq==oq==q and m==len(of) and q<=8*m
                    result['fold_controls']['all_hnfs']+=1
                    result['fold_controls']['max_fiber']=max(result['fold_controls']['max_fiber'],fiber)
        for q in range((38*16**3+26)//27,5793):
            good=list(module.forbidden_enumerator(16,q))
            result['rows'].append({'n':16,'q':q,'admissible':len(good),
                                   'hnf_total':module.hnf_number(q)})
            print(json.dumps(result['rows'][-1]),flush=True)
            if good:
                assert q==5772 and len(good)==24
                histogram=Counter(folds(h)[1] for h in good)
                assert histogram=={2887:24}
                raw=args.scratch/'alternate-n16-minimizers.json'
                raw.write_text(json.dumps(good,separators=(',',':'))+'\n')
                result['minimizers']={'raw':identity(raw),'fold_histogram':dict(histogram)}
                break
        assert result['rows'][-1]['q']==5772
    result['elapsed_seconds']=time.monotonic()-start
    result['final_source_identity']=identity(__file__)
    assert result['source_identity']==result['final_source_identity']
    encoded=json.dumps(result,separators=(',',':'))+'\n'
    assert len(encoded.encode())<16384
    args.receipt.write_text(encoded)
    print(json.dumps({'receipt':identity(args.receipt),'elapsed_seconds':result['elapsed_seconds']}),flush=True)

if __name__=='__main__':main()
