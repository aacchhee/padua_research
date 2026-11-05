#!/usr/bin/env python3
"""Full frozen scalar-CGS2 envelope certificate, rotQ24/alt, degree twelve.
No theorem/status assignment. Default regenerates every source exactly.
"""
import argparse, gzip, hashlib, importlib.util, json, math, os, pathlib
import platform, sys, time
import numpy as np
import flint
from flint import fmpq as Q, fmpq_mat as Mat
ROOT=pathlib.Path(__file__).resolve().parents[3]
SOURCE_PINS={'e1_exact.py':'19ce7b774e5a6fa56108eebca3b2ef81f5237328e518d95225adf9f8835e060f',
             'e1_cgs2.py':'426630eb916e13bb14409f6f7b8ea310eaeb1bf7949de10866d163aad31c7b4b'}
EVIDENCE_PINS={'e1-scalar-cgs2.json':'e215556a01f9e169163b228dfe1b984d28e0cebd7f78e0d858f9a61a0de878c8',
               'e1-multinode-certificates.json':'fae9c8743c78230ef0aa82c185d1efe0eee37be066982a37d39d920af95719f0'}
def sha(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
    return h.hexdigest()
def ident(p):return {'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)}
def event(**v):print(json.dumps(v),flush=True)
def ceilq(x):return (int(x.numerator)+int(x.denominator)-1)//int(x.denominator)
def save_envelope(p,S,d):
    with gzip.open(p,'wt') as f:
        f.write(json.dumps({'schema':'full-envelope-v1','rows':91,'nodes':625,'sources':list(range(1,91)),'d':[str(x) for x in d]})+'\n')
        for k,row in enumerate(S):f.write(json.dumps({'k':k,'values':[str(x) for x in row]})+'\n')
def regenerate(ex):
    coords,b,d,rec,_=ex.build(ex.points('rotated'),12,'alt');M,N=len(coords[0]),len(b)
    assert (M,N)==(625,91) and len(rec)==91 and all(x>0 for x in d)
    S=[[Q(0)]*M for _ in range(N)];seen=[]
    # Exact frozen e1_cgs2.py run body; retain its otherwise discarded absolute.
    for source in range(1,N):
        axis,parent,alpha,_=rec[source];u=ex.multiply(b[parent],coords[axis]);rho=[]
        assert len(alpha)==source and parent<source
        for i in range(M):
            products=Q(0);sums=Q(0);partial=Q(0)
            for l,c in enumerate(alpha):
                term=c*b[l][0,i];products+=abs(term);partial+=term
                if l>=1:sums+=abs(partial)
            rho.append(abs(u[0,i])+products+sums+3*abs(b[source][0,i]))
        assert len(rho)==M and min(rho)>=0
        g=[None]*N;g[source]=Mat([[1]*M])
        for i in range(M):S[source][i]+=rho[i]
        for k in range(source+1,N):
            a,p,coefficients,_=rec[k]
            v=ex.multiply(g[p],coords[a]) if p>=source else Mat(1,M)
            for l in range(source,k):
                if coefficients[l]:v=v-coefficients[l]*g[l]
            g[k]=v
            for i in range(M):S[k][i]+=abs(v[0,i])*rho[i]
        seen.append(source);event(event='graph_source',source=source)
    assert seen==list(range(1,91)) and S[0]==[Q(0)]*625
    assert all(x>=0 for row in S for x in row)
    return S,d

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--frozen-evidence',required=True);ap.add_argument('--output-dir',required=True);ap.add_argument('--receipt',required=True);a=ap.parse_args()
    start=time.monotonic();out=pathlib.Path(a.output_dir);out.mkdir(parents=True,exist_ok=False)
    producer=ROOT/'tracks/bivariate-lanczos/code/drift'
    for f,h in SOURCE_PINS.items():assert sha(producer/f)==h
    ev=pathlib.Path(a.frozen_evidence)
    for f,h in EVIDENCE_PINS.items():assert sha(ev/f)==h
    sys.path.insert(0,str(producer));import e1_exact as ex
    old=json.loads((ev/'e1-scalar-cgs2.json').read_text());lower=json.loads((ev/'e1-multinode-certificates.json').read_text())
    oldrow=next(x for x in old['full_graph_upper_runs'] if x['set']=='rotated' and x['rule']=='alt')
    lowerrow=next(x for x in lower['witnesses'] if x['set']=='rotated' and x['rule']=='bj')
    assert oldrow['degree']==lowerrow['degree']==12 and oldrow['source_count']==90
    assert lowerrow['target_column']==90 and len(lowerrow['node_signs'])==625 and set(lowerrow['node_signs'])<={-1,1}
    Uold=Q(oldrow['upper_squared']['exact']);G=Q(lowerrow['explicit_greedy_sign_lower_squared']['exact'])
    S,d=regenerate(ex)
    old_reproduced=sum((sum((x*x for x in S[k]),Q(0))/d[k] for k in range(1,91)),Q(0))
    assert old_reproduced==Uold and G/Uold<100
    save_envelope(out/'full-envelope.jsonl.gz',S,d)
    event(event='old_frobenius_reproduced',elapsed=time.monotonic()-start)
    SM=Mat(S);ST=SM.transpose();Tf=np.array([[float(x)/math.sqrt(float(dk)) for x in row] for row,dk in zip(S,d)])
    vf=np.ones(625);records=[];passed=False
    for step in range(9):
        if step==0:v=[1]*625
        else:
            vf=Tf.T@(Tf@vf);vf/=max(vf)
            assert np.all(np.isfinite(vf)) and min(vf)>=0
            v=[max(1,int(round(float(x)*10**9))) for x in vf]
        assert len(v)==625 and min(v)>0
        w=SM*Mat([[x] for x in v]);z=ST*Mat([[w[k,0]/d[k]] for k in range(91)])
        ratios=[z[i,0]/v[i] for i in range(625)];U=max(ratios);imax=ratios.index(U)
        assert U>0 and all(z[i,0]<=U*v[i] for i in range(625))
        # A compact integer outward bound avoids embedding 10k-digit rationals.
        B=ceilq(U);assert U<=B and U> B-1
        passed=100*B<G
        cert={'step':step,'proposal':'ones' if step==0 else 'float power step, normalize max=1, round times1e9, floor1','v':v,'U_exact':str(U),'U_integer_upper':B,'maximizing_node':imax,'all_exact_inequalities':True,'pass_100_integer_upper_lt_G':bool(passed)}
        cp=out/('candidate-%02d.json'%step);cp.write_text(json.dumps(cert,indent=2)+'\n')
        records.append({'step':step,'proposal':cert['proposal'],'U_integer_upper':B,'U_float_display':float(U),'maximizing_node':imax,'pass_exact_100U_lt_G':bool(100*U<G),'pass_100_integer_upper_lt_G':bool(passed),'candidate':ident(cp)})
        event(event='candidate',step=step,upper=B,pass_factor_ten=bool(passed))
        if passed:break
    receipt={'scope':{'set':'rotated Q24','degree':12,'rule':'alt','M':625,'N':91,'all_source_columns':90,'source_range':[1,90],'row_zero':'identically zero','rho':'coordinate product + all first matvec products + all partial sums l>=1 + 3abs(bk)','model':'PD-T138 full formal relative-error scalar-CGS2 graph'},'result':'EXACT_CERTIFICATE_PASSES' if passed else 'INCONCLUSIVE_CERTIFICATE','rules_head':'684849d7d19ac2604213ae3d4f499d3436f58b3d','source_sha256':SOURCE_PINS,'frozen_evidence_sha256':EVIDENCE_PINS,'code_sha256':sha(__file__),'old_frobenius_exactly_reproduced':True,'old_ratio_G_over_U_display':float(G/Uold),'old_factor_ten':'INCONCLUSIVE original endpoints; unchanged','new_upper_integer':min(x['U_integer_upper'] for x in records),'strict_exact_comparison':'100 * new_upper_integer < frozen G_R' if passed else 'No tested upper passes; no conclusion about true capacity ratio','candidates':records,'envelope':ident(out/'full-envelope.jsonl.gz'),'command':[sys.executable,'-B',str(pathlib.Path(__file__).resolve()),*sys.argv[1:]],'runtime':{'python':platform.python_version(),'python_flint':flint.__version__,'numpy':np.__version__,'platform':platform.platform(),'elapsed_seconds':time.monotonic()-start},'retention':'Temporary external working artifacts; cold-storage archival/delivery pending. Regenerate with recorded command and new output directory.','limits':['Formal first-order scalar relative-error capacity only; no actual IEEE lower or finite-epsilon conclusion.','No all-degree claim, theorem status, ID assignment, or kill of target on certificate failure.','Developer execution; independent checker/rerun remains separate.']}
    pathlib.Path(a.receipt).write_text(json.dumps(receipt,indent=2)+'\n');event(event='complete',result=receipt['result'],elapsed=time.monotonic()-start)
if __name__=='__main__':main()
