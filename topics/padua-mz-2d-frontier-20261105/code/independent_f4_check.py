#!/usr/bin/env python3
"""Independent F4 regressions: direct moment solve, rational tails, sign enumeration.
Float checks are MEASURED and are not premises of the analytic theorem.
"""
import hashlib, importlib.util, json, math, platform, sys, time
from fractions import Fraction as F
from pathlib import Path
import numpy as np
import scipy
from scipy.linalg import eigvalsh

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
TOP=HERE.parent

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def h(a): return 2/(1-a*a) if a%2==0 else 0.
def indices(n): return [(a,b) for a in range(n+1) for b in range(n+1-a)]
def check(m, developer):
    nodes=[(j,k) for j in range(m+1) for k in range(m+2) if (j+k)%2==0]
    js,ks=np.array(nodes).T
    x=np.cos(np.pi*js/m);y=np.cos(np.pi*ks/(m+1))
    ix=indices(m)
    tx=np.polynomial.chebyshev.chebvander(x,m)
    ty=np.polynomial.chebyshev.chebvander(y,m)
    V=np.column_stack([tx[:,a]*ty[:,b] for a,b in ix])
    moments=np.array([h(a)*h(b) for a,b in ix])
    w=np.linalg.solve(V.T,moments)
    rho=2/(m*(m+1))*np.where((js==0)|(js==m),.5,1.)*np.where((ks==0)|(ks==m+1),.5,1.)
    c=lambda a:1 if a==0 else 2
    d=V@np.array([c(a)*h(a)*c(b)*h(b) for a,b in ix])-2*h(m)*tx[:,m]
    g=np.pi**2*np.sqrt(np.maximum(0,1-x*x))*np.sqrt(np.maximum(0,1-y*y))
    ixn=indices(m-1)
    lx=np.polynomial.legendre.legvander(x,m-1)*np.sqrt((2*np.arange(m)+1)/2)
    ly=np.polynomial.legendre.legvander(y,m-1)*np.sqrt((2*np.arange(m)+1)/2)
    B=np.column_stack([lx[:,a]*ly[:,b] for a,b in ixn])
    raw=B.T@(rho[:,None]*B)
    main=B.T@((rho*g)[:,None]*B)
    row={'m':m,'nodes':len(nodes),'moment_solve_residual':float(np.max(abs(V.T@w-moments))),
         'density_weight_max_error':float(np.max(abs(w-rho*d))),
         'g1_dct_weight_max_error':float(np.max(abs(w-developer.weights_dct(m)[js,ks]))),
         'density_error_times_m_nodes':float(m*np.max(abs(d-g))),
         'main_mass':float(rho@g),'main_mass_formula_error':float(abs(rho@g-np.pi**2/(m*(m+1))/np.tan(np.pi/(2*m))/np.tan(np.pi/(2*(m+1))))),
         'raw_gram_max_over_m2':float(eigvalsh(raw)[-1]/m**2),
         'main_gram_max':float(eigvalsh(main)[-1])}
    C=np.column_stack([tx[:,a]*ty[:,b] for a,b in ixn])
    expected=np.diag([1/c(a)/c(b) for a,b in ixn])
    row['chebyshev_discrete_gram_max_error']=float(np.max(abs(C.T@(rho[:,None]*C)-expected)))
    row['signed_eigenvalues']=[float(z) for z in eigvalsh(B.T@(w[:,None]*B))[[0,-1]]]
    if m<=4:
        # The convex quadratic achieves its maximum on a sign vertex.
        # Evaluate every vertex with the first sign fixed, by global symmetry.
        best=0.
        for start in range(0,2**(len(nodes)-1),1024):
            bits=np.arange(start,min(start+1024,2**(len(nodes)-1)))[:,None]
            signs=np.column_stack([np.ones(len(bits)),2*((bits>>np.arange(len(nodes)-1))&1)-1])
            outputs=(signs*w)@B
            best=max(best,float(np.max(np.sum(outputs**2,axis=1))))
        row['enumerated_sign_vertices']=2**(len(nodes)-1)
        row['float_operator_norm_all_signs']=math.sqrt(best)
    assert row['moment_solve_residual']<1e-11
    assert row['density_weight_max_error']<1e-11
    assert row['g1_dct_weight_max_error']<1e-11
    assert row['density_error_times_m_nodes']<=68/3+1e-10
    assert row['main_mass']<=4+1e-10
    assert row['main_mass_formula_error']<1e-10
    assert row['raw_gram_max_over_m2']<=(.5+1/np.pi)**2+1e-10
    assert row['main_gram_max']<=8*np.pi**2/(np.pi-4/3)**2+1e-10
    assert row['chebyshev_discrete_gram_max_error']<1e-11
    return row

def main():
    tick=time.monotonic()
    source=HERE/'g1_spectral.py'
    spec=importlib.util.spec_from_file_location('dev_g1',source)
    developer=importlib.util.module_from_spec(spec);spec.loader.exec_module(developer)
    for R in range(1,101):
        t=[F(2)]+[F(-4,4*r*r-1) for r in range(1,R+1)]
        A=sum(t[r]*t[s] for r in range(R+1) for s in range(R+1-r))
        N=2*R+1;S=sum(F(1,2*i-1) for i in range(1,R+1))
        assert A==F(8,N*(N+1))-16*S/(N*N-1)
        absolute=sum(abs(t[r]*t[s]) for r in range(R+1) for s in range(R+1-r))
        tail=16-absolute
        assert tail==F(16,N)-A and tail<=F(20,N)
    files=[Path(__file__),source,ROOT/'tracks/mz-constants/code/mz2d_spectra.py',
           ROOT/'topics/padua-mz-2d-20261101/definitions.md',
           TOP/'theory/f4-uniform-density-bound.md']
    out={'status':'MEASURED float checks; exact rational finite tail regression',
         'proof_dependency':False,'rules_input_sha':'83cf6f1ee244f2e72057332a7ec04ee74db1f0de',
         'command':sys.argv,'python':sys.version,'numpy':np.__version__,'scipy':scipy.__version__,
         'platform':platform.platform(),'seed':None,'inputs':{str(p.relative_to(ROOT)):sha(p) for p in files},
         'rational_tail_R_range':[1,100], 'rows':[check(m,developer) for m in [2,3,4,5,6,9,10,15,20]],
         'constant':4*np.sqrt(2)*np.pi/(np.pi-4/3)+(68/3)*(.5+1/np.pi)}
    out['seconds']=time.monotonic()-tick
    Path(sys.argv[1]).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'pass':True,'rows':len(out['rows']),'seconds':out['seconds'],'constant':out['constant']}))
if __name__=='__main__':main()
