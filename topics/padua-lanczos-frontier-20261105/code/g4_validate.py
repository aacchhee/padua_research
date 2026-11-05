"""Bounded basis/reference primitives; no natural-target experiment."""
import argparse,hashlib,json,pathlib,platform
import numpy as np,scipy
from scipy.special import eval_jacobi
import l7_natural as l

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',type=pathlib.Path,required=True);a=p.parse_args()
 P=np.random.default_rng(9107).uniform(-1,1,(80,2));rows=[]
 for sel in ['dev','mirror','alt','adapt']:
  for full in [True,False]:
   q,rec=l.own(P,6,sel,full);old,info,_=l.L2.run_sel(P[:,0],P[:,1],np.ones(len(P)),6,sel=sel,reorth='fullcgs2' if full else 'none')
   delta=float(np.max(abs(q-old)));assert delta==0,(sel,full,delta)
   path=[None]+[('X' if r[0]==0 else 'Y',r[1]) for r in rec[1:]];assert path==info
   replay=float(np.max(abs(l.evaluate(P,rec,len(P))-q)))
   rows.append({'selection':sel,'full':full,'old_Q_entry_max':delta,'parent_path_equal':True,'training_replay_max':replay})
 x=np.linspace(-1,1,97,dtype=np.longdouble);errors=[]
 for aa in range(0,14,2):
  for k in range(8):
   err=float(np.max(abs(l.jacobi(k,aa,0,x)-eval_jacobi(k,aa,0,np.asarray(x,float)))));errors.append(err)
 assert max(errors)<1e-9
 refs=[]
 for d in l.DOMAINS:
  points=l.samples(d,9108,80);v=l.vander(points,d,6);norm=np.sqrt(np.sum(v*v,axis=0));v/=norm;u,r=l.ldqr(v)
  c=np.arange(1,v.shape[1]+1,dtype=l.LD)/v.shape[1];rhs=r@c;sol=l.ldsolve(r,rhs)
  gram=float(np.max(abs(u.T@u-np.eye(len(r),dtype=l.LD))));res=float(np.max(abs(u@r-v)));solve=float(np.max(abs(sol-c)))
  assert gram<1e-15 and res<1e-15 and solve<1e-12
  refs.append({'domain':d,'degree':6,'longdouble_gram_max':gram,'QR_residual_max':res,'known_coeff_solve_max':solve})
 ans={'scope':'primitive validation only, seed9107/9108, degree6, M80; no natural targets','python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'longdouble_nmant':np.finfo(l.LD).nmant,'l7_sha256':l.filehash(l.__file__),'validator_sha256':l.filehash(__file__),'own':rows,'Jacobi_max_difference_vs_scipy':max(errors),'references':refs,'status':'PASS_BOUNDED_PRIMITIVES'}
 a.output.write_text(json.dumps(ans,indent=2)+'\n');print(json.dumps(ans,indent=2))
if __name__=='__main__':main()
