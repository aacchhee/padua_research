# Independent reference/flag check for triangle cases: own Dubiner construction via scipy eval_jacobi,
# double Householder QR (LAPACK), own least squares; method predictions re-evaluated from stored raw recurrences.
import sys; sys.path.insert(0,'/tmp/claude-0/-home-user-padua-research/4e9db0f4-c32d-5606-95a7-0413431483a5/scratchpad/L7G1/deps312')
import sys, json, pathlib, numpy as np
from scipy.special import eval_jacobi
from scipy.linalg import qr, solve_triangular
run=pathlib.Path(sys.argv[1]); ext=sys.argv[2]
sys.path.insert(0,str(pathlib.Path(ext).parent/'deps'))
import types, importlib
pkg=types.ModuleType('polyrat'); pkg.__path__=[str(pathlib.Path(ext)/'polyrat')]; sys.modules['polyrat']=pkg
up=importlib.import_module('polyrat.arnoldi')
def dub(Z,n):
    xi,et=(Z[:,0]+1)/2,(Z[:,1]+1)/2; om=1-et; arg=(2*xi-om)/np.where(om>0,om,1)
    return np.column_stack([eval_jacobi(t-j,0,0,arg)*om**(t-j)*eval_jacobi(j,2*(t-j)+1,0,2*et-1) for t in range(n+1) for j in range(t+1)])
def tg(P):
    x,y=P.T; return {'rational':1/(1+25*(x*x+y*y)),'tanh':np.tanh(10*(x+y-.3)),'absolute':abs(x-y),'entire':np.exp(x)*np.cos(2*y)+np.sin(3*x*y)}
eps=np.finfo(float).eps; out=[]
for js in sorted(run.glob('*/triangle-*0[12].json')):
    r=json.loads(js.read_text()); seed=r['seed']
    inp=np.load(js.parent/f'triangle-{seed}-inputs.npz'); raw=np.load(js.parent/f'triangle-{seed}-raw.npz')
    P=inp['training']; T=np.vstack([inp['uniform'],inp['boundary']])
    assert np.array_equal(P,raw['P']) and np.array_equal(T,raw['T'])
    V=dub(P,24); sc=np.linalg.norm(V,axis=0); V/=sc; Vt=dub(T,24)/sc
    f=tg(P); tr=tg(T)
    # method test predictions from stored recurrences
    preds={}
    for lab in ['upstream_xy','upstream_yx','dev_full','mirror_full','alt_full','adapt_full','dev_window','mirror_window','alt_window','adapt_window']:
        Q=raw[lab+'_Q']
        if lab.startswith('upstream'):
            o=[0,1] if lab.endswith('xy') else [1,0]; E=up.vandermonde_arnoldi_eval(T[:,o],raw[lab+'_H'],raw[lab+'_index'])
        else:
            hc,par,beta=raw[lab+'_coeff'],raw[lab+'_parents'],raw[lab+'_beta']
            E=np.zeros((len(T),Q.shape[1])); E[:,0]=1/np.sqrt(len(P))
            for k in range(1,Q.shape[1]):
                ax,p,w0=par[k]; W=np.arange(w0,k); E[:,k]=(T[:,ax]*E[:,p]-E[:,W]@hc[W,k])/beta[k]
        preds[lab]=(Q,E)
    for c in r['cases']:
        n=c['n']; k=(n+1)*(n+2)//2; Vn=V[:,:k]
        s=np.linalg.svd(Vn,compute_uv=False); kap=s[0]/s[-1]
        Qh,Rh=qr(Vn,mode='economic')
        maxrel=0; flags={}
        for tn in f:
            a=solve_triangular(Rh,Qh.T@f[tn]); rp=Vt[:,:k]@a
            for name,sl in [('uniform',slice(0,2000)),('boundary',slice(2000,4000))]:
                re=np.linalg.norm(rp[sl]-tr[tn][sl])/np.linalg.norm(tr[tn][sl]); st=c['targets'][tn]['reference'][name]['rel_l2']
                maxrel=max(maxrel,abs(re-st)/st)
            for lab,(Q,E) in preds.items():
                C=np.linalg.lstsq(Q[:,:k],f[tn],rcond=max(Q[:,:k].shape)*eps)[0]; pm=E[:,:k]@C
                for name,sl in [('uniform',slice(0,2000)),('boundary',slice(2000,4000))]:
                    re=np.linalg.norm(rp[sl]-tr[tn][sl])/np.linalg.norm(tr[tn][sl]); me=np.linalg.norm(pm[sl]-tr[tn][sl])/np.linalg.norm(tr[tn][sl])
                    df=np.linalg.norm(pm[sl]-rp[sl])/np.linalg.norm(tr[tn][sl])
                    fl=bool(c['reference']['trusted'] and me>2*re and df>max(1e-10,100*eps*kap))
                    flags[(tn,lab,name)]=(fl,me/(2*re),c['targets'][tn]['methods'][lab][name]['resolved_loss'],abs(me-c['targets'][tn]['methods'][lab][name]['rel_l2'])/c['targets'][tn]['methods'][lab][name]['rel_l2'])
        nl=sum(v[0] for v in flags.values()); mism=[k_ for k_,v in flags.items() if v[0]!=v[2]]
        near=sorted((abs(v[1]-1),k_,round(v[1],4)) for k_,v in flags.items())[:3]
        print(seed,n,'kappa %.4g (json %.4g)'%(kap,c['reference']['kappa']),'max rel diff of my double-QR reference errors vs stored LD reference errors %.2e'%maxrel,
              '| my losses',nl,'| flag mismatches',len(mism),mism[:4],'| max method-error reproduction rel diff %.1e'%max(v[3] for v in flags.values()),'| nearest 2x-margins',near)
