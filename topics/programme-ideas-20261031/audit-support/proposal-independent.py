"""Independent cardinal construction by solving the Chebyshev Vandermonde.
No developer evaluator imported. Finite float64 validation, not certification.
Source snapshot: 614709d4a60fb0c2593b05764e8d5aceda1be381.
"""
import pathlib,json,platform
import numpy as np
import scipy
root=pathlib.Path(__file__).resolve().parents[1]
data=json.loads((root/'checks/code/decisive/gen4-2/t3_maxima.json').read_text())
rows=[]
for ns, dat in data.items():
    n=int(ns)
    nodes=np.array([(j*np.pi/n,k*np.pi/(n+1)) for j in range(n+1) for k in range(n+2) if (j+k)%2==0])
    idx=np.array([(i,j) for i in range(n+1) for j in range(n+1-i)])
    ii,jj=idx.T
    V=np.cos(nodes[:,0,None]*ii)*np.cos(nodes[:,1,None]*jj)
    coeff=np.linalg.inv(V)
    def ev(t,p):
        t=np.atleast_1d(t)[:,None]; p=np.atleast_1d(p)[:,None]
        ct,st=np.cos(t*ii),np.sin(t*ii)
        cp,sp=np.cos(p*jj),np.sin(p*jj)
        return dict(L=(ct*cp)@coeff,Lt=(-ii*st*cp)@coeff,Lp=(-jj*ct*sp)@coeff,
                    Ltt=(-ii**2*ct*cp)@coeff,Lpp=(-jj**2*ct*cp)@coeff,Ltp=(ii*jj*st*sp)@coeff)
    pts=np.array(dat['interior']+dat['edge']+dat['corner'])
    d=ev(pts[:,0],pts[:,1]); s=np.sign(d['L'])
    grad=np.c_[np.sum(s*d['Lt'],1),np.sum(s*d['Lp'],1)]
    rings=[]
    a=np.arange(64)*np.pi/32
    for rad in (1e-3,1e-4,1e-5):
        worst=-np.inf; fails=0
        for t,p,v in pts:
            vals=np.sum(np.abs(ev(t+rad*np.cos(a),p+rad*np.sin(a))['L']),axis=1)
            val=np.sum(np.abs(ev(t,p)['L']))
            delta=float(max(vals)-val)
            worst=max(worst,delta); fails+=int(delta>1e-12)
        rings.append(dict(radius=rad,failures=fails,worst_delta=worst))
    rows.append(dict(n=n,total=len(pts),interior=len(dat['interior']),edge=len(dat['edge']),corner=len(dat['corner']),
                     max_lambda_difference=float(max(abs(np.sum(abs(d['L']),1)-pts[:,2]))),
                     max_gradient_norm=float(max(np.linalg.norm(grad,axis=1))),rings=rings,
                     vandermonde_condition=float(np.linalg.cond(V))))
    print(rows[-1],flush=True)
(root/'audit-support/proposal-independent.json').write_text(json.dumps(dict(
    method='independent Chebyshev Vandermonde inverse, float64',python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__,rows=rows),indent=2))
