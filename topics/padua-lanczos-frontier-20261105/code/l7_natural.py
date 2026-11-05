"""Preregistered natural-fit study; full suite NOT EXECUTED.
Bounded primitive validation is recorded separately under G4.
Third-party sources remain external. G4 review precedes any suite execution.
"""
import argparse, hashlib, json, os, pathlib, platform, sys, time
import numpy as np
import scipy
from scipy.linalg import qr, svdvals, solve_triangular
ROOT=pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'tracks/bivariate-lanczos/code/drift'))
from e6_benchmark import load_upstream, L2
LD=np.longdouble
DEGREES=(8,16,24)
DOMAINS=('disk','lshape','triangle','sector')
SEEDS=(2026110501,2026110502)

def digest(x): return hashlib.sha256(x).hexdigest()
def filehash(p): return digest(pathlib.Path(p).read_bytes())
def inside(P,d):
 x,y=P.T;r=np.hypot(x,y)
 if d=='disk': return r<=1
 if d=='triangle': return (x+y<=0)
 if d=='lshape': return ~((x>0)&(y>0))
 t=np.mod(np.arctan2(y,x),2*np.pi)
 return (r>=.4)&(r<=1)&(t<=1.5*np.pi)
def boundary_distance(P,d):
 x,y=P.T;r=np.hypot(x,y)
 if d=='disk': return 1-r
 if d=='triangle':return np.minimum.reduce([x+1,y+1,-(x+y)/np.sqrt(2)])
 if d=='lshape':
  # distances to reentrant segments [0,1]x{0} and {0}x[0,1]
  a=np.hypot(x-np.clip(x,0,1),y);b=np.hypot(x,y-np.clip(y,0,1))
  return np.minimum.reduce([x+1,y+1,1-x,1-y,a,b])
 # radial segments (.4,0)..(1,0) and (0,-.4)..(0,-1)
 a=np.hypot(x-np.clip(x,.4,1),y);b=np.hypot(x,y-np.clip(y,-1,-.4))
 return np.minimum.reduce([r-.4,1-r,a,b])
def samples(d,seed,m,band=False):
 rng=np.random.default_rng(seed);chunks=[];count=0
 while count<m:
  P=rng.uniform(-1,1,(max(4096,2*m),2));keep=inside(P,d)
  if band: keep&=boundary_distance(P,d)<=.05
  P=P[keep];chunks.append(P);count+=len(P)
 return np.concatenate(chunks)[:m]
def targets(P):
 x,y=P.T
 return {'rational':1/(1+25*(x*x+y*y)),'tanh':np.tanh(10*(x+y-.3)), 'absolute':abs(x-y),'entire':np.exp(x)*np.cos(2*y)+np.sin(3*x*y)}
def jacobi(k,a,b,x):
 if k==0:return np.ones_like(x)
 p0=np.ones_like(x);p1=((a-b)+(a+b+2)*x)/2
 for n in range(2,k+1):
  h=LD(2*n+a+b)
  p2=((h-1)*(h*(h-2)*x+a*a-b*b)*p1-2*(n+a-1)*(n+b-1)*h*p0)/(2*n*(n+a+b)*(h-2))
  p0,p1=p1,p2
 return p1
def vander(P,d,n):
 x,y=np.asarray(P,dtype=LD).T
 if d=='triangle':
  xi=(x+1)/2;eta=(y+1)/2;om=1-eta;arg=(2*xi-om)/np.where(om>0,om,1)
  return np.column_stack([jacobi(t-j,0,0,arg)*om**(t-j)*jacobi(j,2*(t-j)+1,0,2*eta-1) for t in range(n+1) for j in range(t+1)])
 def cheb(z):
  a=[np.ones_like(z),z]
  for k in range(2,n+1):a.append(2*z*a[-1]-a[-2])
  return a
 cx,cy=cheb(x),cheb(y)
 return np.column_stack([cx[t-j]*cy[j] for t in range(n+1) for j in range(t+1)])
def ldqr(V):
 m,n=V.shape;Q=np.zeros((m,n),dtype=LD,order='F');R=np.zeros((n,n),dtype=LD)
 for k in range(n):
  v=V[:,k].copy()
  for _ in range(2):
   h=Q[:,:k].T@v;R[:k,k]+=h;v-=Q[:,:k]@h
  R[k,k]=np.sqrt(v@v);Q[:,k]=v/R[k,k]
 return Q,R
def ldsolve(R,c):
 x=np.array(c,dtype=LD,copy=True)
 for k in range(len(R)-1,-1,-1):x[k]=(x[k]-R[k,k+1:]@x[k+1:])/R[k,k]
 return x
def own(P,n,selection,full):
 idx=[(t,j) for t in range(n+1) for j in range(t+1)];pos={a:i for i,a in enumerate(idx)}
 Q=np.zeros((len(P),len(idx)));Q[:,0]=1/np.sqrt(len(P));rec=[None]
 for k,(t,j) in enumerate(idx[1:],1):
  W=np.arange(k) if full else np.arange(L2.Nof(t-3) if t>=2 else 0,k)
  options=L2.candidates_sel(t,j) if selection=='adapt' else [L2.rule_sel(selection,t,j)]
  best=None
  for op,par in options:
   p=pos[par];axis=0 if op=='X' else 1;a=P[:,axis]*Q[:,p];na=np.sqrt(a@a)
   Qw=Q[:,:k] if full else Q[:,W]
   h=Qw.T@a;r=a-Qw@h
   if full:
    h2=Qw.T@r;r=r-Qw@h2;h=h+h2
   score=np.sqrt(r@r)/na
   if best is None or score>best[0]:best=(score,axis,p,r,h)
  _,axis,p,r,h=best
  if not full:
   h2=Qw.T@r;r=r-Qw@h2;h=h+h2
  beta=np.sqrt(r@r);Q[:,k]=r/beta;rec.append((axis,p,W,h,beta))
 return Q,rec

def evaluate(P,rec,M):
 E=np.zeros((len(P),len(rec)));E[:,0]=1/np.sqrt(M)
 for k,(axis,p,W,h,beta) in enumerate(rec[1:],1):E[:,k]=(P[:,axis]*E[:,p]-E[:,W]@h)/beta
 return E

def errors(pred,f):
 return {'rel_l2':float(np.linalg.norm(pred-f)/np.linalg.norm(f)), 'rel_max':float(np.max(abs(pred-f))/np.max(abs(f)))}

def run(up,d,seed,outdir):
 t0=time.time();P=samples(d,seed,1600);S=[samples(d,seed+100,2000),samples(d,seed+200,2000,True)];T=np.vstack(S);allP=np.vstack([P,T]);N=L2.Nof(24)
 ftrain=targets(P);truth=targets(T)
 V=vander(P,d,24);sc=np.sqrt(np.sum(V*V,axis=0));V/=sc
 Eref=vander(T,d,24)/sc;UL,RL=ldqr(V);U=np.asarray(UL,float)
 bases={};checks={}
 for label,order in [('upstream_xy',[0,1]),('upstream_yx',[1,0])]:
  Q,H,idx=up.vandermonde_arnoldi_CGS(P[:,order],24,weight=np.ones(len(P)))
  Eall=up.vandermonde_arnoldi_eval(allP[:,order],H,idx);bases[label]=(Q,Eall[len(P):],None)
  checks[label]={'training_replay_max':float(np.max(abs(Eall[:len(P)]-Q)))}
 for sel in ['dev','mirror','alt','adapt']:
  for full in [True,False]:
   label=sel+('_full' if full else '_window');Q,rec=own(P,24,sel,full);Eall=evaluate(allP,rec,len(P));bases[label]=(Q,Eall[len(P):],rec)
   old,info,_=L2.run_sel(P[:,0],P[:,1],np.ones(len(P)),24,sel=sel,reorth='fullcgs2' if full else 'none')
   diff=float(np.max(abs(old-Q)));assert diff==0,(label,diff)
   checks[label]={'old_Q_entry_max':diff,'training_replay_max':float(np.max(abs(Eall[:len(P)]-Q))), 'parent_path_sha256':digest(json.dumps(info).encode())}
 checks['upstream_yx_vs_dev_entry_max']=float(np.max(abs(bases['upstream_yx'][0]-bases['dev_full'][0])))
 ans={'domain':d,'seed':seed,'M':len(P),'test_sizes':[len(z) for z in S], 'input_sha256':digest(P.tobytes()),'test_sha256':[digest(z.tobytes()) for z in S],'checks':checks,'cases':[]}
 for n in DEGREES:
  k=L2.Nof(n);Vn=V[:,:k];Un=U[:,:k];R=RL[:k,:k];Er=Eref[:,:k];s=svdvals(np.asarray(Vn,float));kap=float(s[0]/s[-1]);rank=int(np.sum(s>s[0]*max(Vn.shape)*np.finfo(float).eps));Ud=qr(np.asarray(Vn,float),mode='economic')[0];dis=float(svdvals(Un-Ud@(Ud.T@Un))[0]);lg=float(np.max(abs(UL[:,:k].T@UL[:,:k]-np.eye(k,dtype=LD))))
  trusted=rank==k and kap<1e8 and lg<1e-12 and dis<1e-7 and np.finfo(LD).nmant>np.finfo(float).nmant
  case={'n':n,'N':k,'reference':{'kappa':kap,'rank':rank,'longdouble_gram_max':lg,'double_ld_span_gap':dis,'trusted':bool(trusted)},'methods':{},'targets':{}}
  refs={}
  for tn,f in ftrain.items():
   c=UL[:,:k].T@np.asarray(f,LD);a=ldsolve(R,c);pred=np.asarray(Er@a,float);refs[tn]=pred
   case['targets'][tn]={'reference':{'train':errors(Un@np.asarray(c,float),f),'coefficient_l2':float(np.linalg.norm(np.asarray(c,float))), 'uniform':errors(pred[:2000],truth[tn][:2000]),'boundary':errors(pred[2000:],truth[tn][2000:])},'methods':{}}
  for label,(Qa,Ea,rec) in bases.items():
   Q=Qa[:,:k];E=Ea[:,:k];G=Q.T@Q-np.eye(k);W=qr(Q,mode='economic')[0];gap=float(svdvals(Un-W@(W.T@Un))[0]);sq=svdvals(Q)
   case['methods'][label]={'gap_raw':gap,'gram_2':float(svdvals(G)[0]),'gram_max':float(np.max(abs(G))),'Q_kappa':float(sq[0]/sq[-1]),'Q_rank':int(np.sum(sq>sq[0]*max(Q.shape)*np.finfo(float).eps))}
   F=np.column_stack(list(ftrain.values()));C,res,rnk,sv=np.linalg.lstsq(Q,F,rcond=max(Q.shape)*np.finfo(float).eps);preds=E@C
   for j,(tn,f) in enumerate(ftrain.items()):
    pred=preds[:,j];row={'coefficient_l2':float(np.linalg.norm(C[:,j])),'fit_rank':int(rnk),'train':errors(Q@C[:,j],f)}
    for name,sl in [('uniform',slice(0,2000)),('boundary',slice(2000,4000))]:
     row[name]=errors(pred[sl],truth[tn][sl]);diff=float(np.linalg.norm(pred[sl]-refs[tn][sl])/np.linalg.norm(truth[tn][sl]));row[name]['difference_vs_reference']=diff
     referr=case['targets'][tn]['reference'][name]['rel_l2'];row[name]['resolved_loss']=bool(trusted and row[name]['rel_l2']>2*referr and diff>max(1e-10,100*np.finfo(float).eps*kap))
    case['targets'][tn]['methods'][label]=row
  ans['cases'].append(case)
 ans['elapsed_seconds']=time.time()-t0
 path=outdir/f'{d}-{seed}.json';path.write_text(json.dumps(ans,indent=1)+'\n');print(d,seed,'seconds',round(ans['elapsed_seconds'],1),'trusted',[c['reference']['trusted'] for c in ans['cases']],flush=True)
 return ans

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--external',required=True);ap.add_argument('--output-dir',required=True);ap.add_argument('--domains',nargs='+',default=DOMAINS);ap.add_argument('--seeds',nargs='+',type=int,default=SEEDS);a=ap.parse_args();out=pathlib.Path(a.output_dir);out.mkdir(parents=True,exist_ok=True);up=load_upstream(a.external)
 meta={'command':sys.argv,'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'longdouble_nmant':np.finfo(LD).nmant,'blas_threads':os.getenv('OPENBLAS_NUM_THREADS'),'code_sha256':filehash(__file__),'prereg_sha256':filehash(pathlib.Path(__file__).parents[1]/'l7-preregistration.md'),'source_sha256':{p.name:filehash(p) for p in (pathlib.Path(a.external)/'polyrat').glob('*.py') if p.name in ('arnoldi.py','index.py','basis.py','version.py')}}
 (out/'metadata.json').write_text(json.dumps(meta,indent=1)+'\n')
 for d in a.domains:
  for seed in a.seeds:run(up,d,seed,out)
if __name__=='__main__':main()
