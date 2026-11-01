#!/usr/bin/env python3
"""Bounded float64 reproduction. Imports supplied function definitions only via AST.
No imported .out is used. Run BLAS single-threaded; see --help for finite scope.
"""
import argparse, ast, contextlib, datetime, hashlib, io, json, os, platform, subprocess, sys, time
from pathlib import Path
import numpy as np
import scipy
from scipy.linalg import eigh

ROOT = Path(__file__).resolve().parents[3]
SRC = ROOT / 'topics/mz-constants/sources/padua_mz_inputs/code'
sys.path.insert(0, str(SRC))

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def functions(name):
    """Execute imports and function definitions, never source's top-level runs."""
    path = SRC / name
    tree = ast.parse(path.read_text(), filename=str(path))
    tree.body = [n for n in tree.body if isinstance(n, (ast.Import, ast.ImportFrom, ast.FunctionDef))]
    ns = {'__file__': str(path), '__name__': 'bounded_functions'}
    exec(compile(tree, str(path), 'exec'), ns)
    return ns

def limits(cc, N, n):
    r = [cc['extremes'](N, n, p) for p in (0, 1) if p <= n]
    lo, hi = min(v[0] for v in r), max(v[1] for v in r)
    return dict(N=N, n=n, lmin=float(lo), lmax=float(hi), eta=float(max(1-lo, hi-1)), parity=r)

def direct(N,n):
    # Independent from supplied recurrence/weight routine: Cheb interpolation
    # moments determine CC weights; numpy Legendre Vandermonde determines B.
    x=np.cos(np.pi*np.arange(N+1)/N)
    V=np.polynomial.chebyshev.chebvander(x,N)
    k=np.arange(N+1); h=np.zeros(N+1); h[::2]=2/(1-k[::2].astype(float)**2)
    w=np.linalg.solve(V.T,h)
    B=np.polynomial.legendre.legvander(x,n)*np.sqrt((2*np.arange(n+1)+1)/2)
    ev=np.linalg.eigvalsh(B.T@(w[:,None]*B))
    return float(ev[0]),float(ev[-1])

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--suite', choices=['all','hankel','cc','direct','ratio','padua','marginal','schur','hss'],default='all')
    ap.add_argument('--output', type=Path, required=True)
    ap.add_argument('--max-N',type=int,default=640)
    args=ap.parse_args()
    selected=lambda s:args.suite in ('all',s)
    report={'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'MEASURED','rules_sha':'d36722823441dc40c6e19d69a174459348dd309c','command':sys.argv,'python':sys.version,'platform':platform.platform(),'numpy':np.__version__,'scipy':scipy.__version__,'threads':{k:os.environ.get(k) for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']},'runner_sha256':digest(Path(__file__)),'source_sha256':{p.name:digest(p) for p in sorted(SRC.glob('*.py'))},'independent_rerun':'not performed by this developer runner','results':{}}
    cc=functions('cc_mz_large.py')
    started=time.monotonic()
    def save():
        report['elapsed_seconds']=time.monotonic()-started
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(report,indent=2,allow_nan=False,default=lambda x:x.item() if isinstance(x,np.generic) else x)+'\n')
    def result(name, value):
        report['results'][name]=value;save(); print(name,json.dumps(value,default=lambda x:x.item() if isinstance(x,np.generic) else x),flush=True)
    if selected('hankel'):
        p=subprocess.run([sys.executable,str(SRC/'hankel_check.py')],capture_output=True,text=True,timeout=60,check=True)
        result('hankel_original_N60',{'stdout':p.stdout,'stderr':p.stderr,'command':[sys.executable,str(SRC/'hankel_check.py')]})
    if selected('cc'):
        rows=[]
        for N in [40,80,160,320,640,1280]:
            if N>args.max_N:continue
            r=limits(cc,N,N-1);r['u_ratio']=float(cc['u_ratio'](N));rows.append(r)
        result('cc_Nminus1',rows)
        p=subprocess.run([sys.executable,str(SRC/'cc_mz_large.py'),*[str(n) for n in [40,80,160,320,640,1280] if n<=args.max_N]],capture_output=True,text=True,timeout=120,check=True)
        result('cc_original_stdout',{'stdout':p.stdout,'stderr':p.stderr})
    if selected('direct'):
        rows=[]
        for N in [3,4,5,9,10,21,40,81]:
            for n in sorted(set([N//2,N-1,N])):
                r=limits(cc,N,n);lo,hi=direct(N,n);r.update(direct_lmin=lo,direct_lmax=hi,max_error=max(abs(lo-r['lmin']),abs(hi-r['lmax'])));rows.append(r)
        result('direct_vs_generalized',rows)
    if selected('ratio'):
        result('fixed_ratios',[dict(limits(cc,N,int(r*N)),ratio=r) for r in [.6,.75,.9,.95] for N in [40,80,160,320,640] if N<=args.max_N])
    if selected('padua'):
        fn=functions('padua_mz_large.py')['run']
        result('padua',[dict(m=m,out=fn(m,(m-1,))) for m in [10,20,30,40]])
    if selected('marginal'):
        fn=functions('mz_padua_cc_check.py');rows=[]
        for m in [10,20,31]:
            P,_=fn['padua'](m);idx=fn['total_degree'](m)
            V=np.column_stack([fn['cheb_hat'](a,P[:,0])*fn['cheb_hat'](b,P[:,1]) for a,b in idx])
            moment=lambda k:0. if k%2 else 2/(1-k*k)
            mom=np.array([moment(a)*moment(b)*(1 if a==0 else np.sqrt(2))*(1 if b==0 else np.sqrt(2)) for a,b in idx])
            w=np.linalg.solve(V.T,mom);x=np.cos(np.pi*np.arange(m+1)/m)
            wx=np.array([w[np.abs(P[:,0]-z)<1e-12].sum() for z in x])
            wc=np.linalg.solve(np.polynomial.chebyshev.chebvander(x,m).T,np.array([moment(k) for k in range(m+1)]))
            rows.append(dict(m=m,max_abs_wx_minus_2wcc=float(np.max(np.abs(wx-2*wc))),max_abs_wx_minus_wcc=float(np.max(np.abs(wx-wc))),sum_wx=float(wx.sum()),sum_wcc=float(wc.sum())))
        result('true_marginal',rows)
    if selected('schur'):
        fn=functions('bttbmap_b2_cc_schur.py')['run'];out=io.StringIO()
        with contextlib.redirect_stdout(out):
            for N in [40,80,160,320,640]:
                if N<=args.max_N:fn(N)
        result('schur_original_function',{'stdout':out.getvalue(),'degree':'n=N (full nodal polynomial space), not n=N-1'})
    if selected('hss'):
        fn=functions('bttbmap_p_cc_hss_nodes.py');rows=[]
        for N in [256,512]:
            A=fn['mats'](N); rows.append(dict(N=N,ranks_1e12=fn['offrank'](A,1e-12),ranks_1e8=fn['offrank'](A,1e-8)))
        result('node_hss_ranks',rows)
    save()

if __name__=='__main__':main()
