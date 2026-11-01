"""E6 MEASURED: unmodified external polyrat functions, compared with own L2 CGS2.
Third party files stay outside repository. No novelty or computer-proof claim.
Run with OPENBLAS_NUM_THREADS=1; external checkout pinned in e6-provenance.json.
"""
import argparse, hashlib, importlib, json, os, pathlib, platform, sys, types
import numpy as np
from scipy.linalg import svd, qr, solve_triangular
ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'L2'))
import l2_core as L2


def load_upstream(directory):
    # Namespace package adapter loads real, unchanged source modules, bypassing
    # unrelated rational solver imports in __init__ (cvxopt/cvxpy/iterprinter).
    # basis.py and index.py themselves are unmodified; actual dependency installed.
    sys.path.insert(0, str(pathlib.Path(directory).parent / 'deps'))
    package = types.ModuleType('polyrat'); package.__path__ = [str(pathlib.Path(directory) / 'polyrat')]
    sys.modules['polyrat'] = package
    return importlib.import_module('polyrat.arnoldi')


def reference(P, w, n, name, test):
    # Product Chebyshev in inverse-rotated frame, or Dubiner on triangle.
    from scipy.special import eval_jacobi
    A, B = P.copy(), test.copy()
    theta = {'rot0.3': .3, 'rotpi4': np.pi/4}.get(name, 0)
    if theta:
        A = L2.L1.rotate(A, -theta); B = L2.L1.rotate(B, -theta)
    if name == 'Q24':
        rot = np.array([[3/5, -4/5], [4/5, 3/5]])
        A = A @ rot; B = B @ rot
    if name in ('triangle','T24'):
        def make(Z):
            xi, et = (Z[:,0]+1)/2, (Z[:,1]+1)/2
            om=1-et; arg=(2*xi-om)/np.where(om>0,om,1)
            return np.column_stack([eval_jacobi(t-j,0,0,arg)*om**(t-j)*eval_jacobi(j,2*(t-j)+1,0,2*et-1) for t in range(n+1) for j in range(t+1)])
        V, Vt=make(A),make(B)
    else:
        mid=(A.max(axis=0)+A.min(axis=0))/2; rad=(A.max(axis=0)-A.min(axis=0))/2
        def make(Z):
            x,y=((Z-mid)/rad).T
            vx=np.polynomial.chebyshev.chebvander(x,n);vy=np.polynomial.chebyshev.chebvander(y,n)
            return np.column_stack([vx[:,t-j]*vy[:,j] for t in range(n+1) for j in range(t+1)])
        V,Vt=make(A),make(B)
    V*=np.sqrt(w)[:,None]
    norm=np.linalg.norm(V,axis=0); V/=norm;Vt/=norm
    U,R=qr(V,mode='economic'); s=svd(V,compute_uv=False)
    return U,R,Vt,float(s[0]/s[-1]),float(s[-1]),int(np.sum(s>s[0]*max(V.shape)*np.finfo(float).eps))


def selection_check(up,n):
    idx=up.total_degree_index(2,n)
    assert np.array_equal(idx,np.array([(j,t-j) for t in range(n+1) for j in range(t+1)]))
    for k in range(1,len(idx)):
        i,p=up._update_rule(idx,idx[k]);t=sum(idx[k]);j=int(idx[k,0])
        expected=L2.rule_sel('dev',t,j)
        # input reversed: first upstream coordinate is campaign y, second is x
        assert ('Y' if i==0 else 'X') == expected[0]
        assert tuple((sum(idx[p]),idx[p,0])) == expected[1]
        mirror=L2.rule_sel('mirror',t,int(idx[k,1]))
        assert ('X' if i==0 else 'Y') == mirror[0]
        assert (sum(idx[p]),idx[p,1]) == mirror[1]
    return {'n':n,'columns':len(idx),'all_parents_checked':True,'input_xy':'mirror with reverse within-degree order','input_yx':'dev in campaign within-degree order'}


def metrics(Q,U):
    W=qr(Q,mode='economic')[0]
    D=U-W@(W.T@U)
    _,s,vt=svd(D,full_matrices=False)
    return {'gap':float(s[0]),'orth_max':float(np.max(abs(Q.T@Q-np.eye(Q.shape[1]))))},W,vt[0]


def run_case(up,name,P,w,n):
    test=(P[:128]+P[-128:])/2
    U,R,Vtest,kap,smin,rank=reference(P,w,n,name,test)
    ans={'name':name,'n':n,'M':len(P),'N':L2.Nof(n),'input_sha256':hashlib.sha256(P.tobytes()+w.tobytes()).hexdigest(),
         'reference':{'kind':'Dubiner' if name in ('triangle','T24') else 'frame Chebyshev','kappa':kap,'u_kappa':2**-53*kap,'smin':smin,'rank_tolerance_rule':'s0*max(M,N)*eps','numerical_rank':rank,'full_rank':rank==len(R),'trusted':kap<1e8 and rank==len(R)},'methods':{}}
    bases={}; extras={}
    for label,order in [('upstream_xy',[0,1]),('upstream_yx',[1,0])]:
        Q,H,idx=up.vandermonde_arnoldi_CGS(P[:,order],n,weight=np.sqrt(w))
        bases[label]=Q;extras[label]=(H,idx,order)
    for sel in ['dev','mirror','alt','adapt']:
        bases[sel]=L2.run_sel(P[:,0],P[:,1],w,n,sel=sel,reorth='fullcgs2')[0]
    # Exhaustively checked selection does not imply bitwise same arithmetic.
    ans['upstream_yx_vs_dev_entry_max']=float(np.max(abs(bases['upstream_yx']-bases['dev'])))
    ans['upstream_yx_vs_dev_span_gap']=float(np.linalg.norm(bases['upstream_yx']-bases['dev']@(bases['dev'].T@bases['upstream_yx']),2))
    # Common adversarial target: exact-span unit polynomial nearest the missing
    # direction of upstream yx. Target selection is post-hoc and disclosed.
    _,_,v=metrics(bases['upstream_yx'],U);f=U@v
    ans['target']={'selection':'post-hoc largest right singular vector of (I-P_upstream_yx) Uref','qr_coefficients':v.tolist()}
    trusted=ans['reference']['trusted']
    ftest=Vtest@solve_triangular(R,v) if trusted else None
    for label,Q in bases.items():
        m,W,_=metrics(Q,U)
        residual=f-W@(W.T@f)
        m['adversarial_fit_relative_residual']=float(np.linalg.norm(residual))
        m['projection_using_Q_relative_residual']=float(np.linalg.norm(f-Q@(Q.T@f)))
        # Terminal closure bound is for max(theta[n-1], theta[n]), not theta[n].
        Nm=L2.Nof(n-1); cols=slice(L2.Nof(n-2),Nm)
        for axis in range(2):
            A=P[:,axis,None]*W[:,cols]
            m['terminal_defect_'+str(axis)]=float(np.linalg.norm(A-W@(W.T@A),2))
        if label in extras and trusted:
            H,idx,order=extras[label]
            E=up.vandermonde_arnoldi_eval(test[:,order],H,idx)
            c=np.linalg.lstsq(Q,f,rcond=None)[0]
            pred=E@c
            m['adversarial_test_relative_error']=float(np.linalg.norm(pred-ftest)/np.linalg.norm(ftest))
        ans['methods'][label]=m
    return ans


def main():
    p=argparse.ArgumentParser();p.add_argument('--external',default='/workspace/padua-drift-external/polyrat');p.add_argument('--output',required=True);p.add_argument('--grid-degree',type=int,default=12);p.add_argument('--sets',nargs='*',default=L2.BENCH);a=p.parse_args()
    up=load_upstream(a.external)
    result={'status':'MEASURED','python':platform.python_version(),'numpy':np.__version__,'blas_threads':os.getenv('OPENBLAS_NUM_THREADS'),'selection_check':selection_check(up,47),'cases':[]}
    for name in a.sets:
        if name in ('T24','Q24'):
            # Frozen E1 rational grids, round each rational coordinate once.
            from fractions import Fraction as F
            if name == 'T24':
                pts=[(F(i,12)-1,F(j,12)-1) for i in range(25) for j in range(25-i)]
            else:
                pts=[((3*(F(i,12)-1)-4*(F(j,12)-1))/5,(4*(F(i,12)-1)+3*(F(j,12)-1))/5) for i in range(25) for j in range(25)]
            P=np.array(pts,dtype=float);w=np.ones(len(P));n=a.grid_degree
        else:
            P,w,n=L2.benchmark(name)
        r=run_case(up,name,P,w,n);result['cases'].append(r)
        pathlib.Path(a.output).write_text(json.dumps(result,indent=2)+'\n')
        print(name,n,'kappa',r['reference']['kappa'],{k:round(m['gap'],12) for k,m in r['methods'].items()},flush=True)
if __name__=='__main__':main()
