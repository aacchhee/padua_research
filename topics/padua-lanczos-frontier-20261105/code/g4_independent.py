"""Independent G4 arithmetic attribution on frozen Q/H; no algorithm/suite rerun.
Arb monomial projection checks the reference; independent long-double recurrence
checks actual normal errors. Final norms are floating diagnostics, not proofs.
"""
import argparse, hashlib, json, os, pathlib, sys, time
import numpy as np
from scipy.linalg import svdvals
from flint import arb, arb_mat, ctx
ROOT=pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'tracks/bivariate-lanczos/code/drift'))
import e6_benchmark as e6
LD=np.longdouble

def sha(p): return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def norm(a): return float(svdvals(np.asarray(a,float))[0])
def aa(x):
 p,q=float(x).as_integer_ratio();return arb(p)/q

def reference_check(P,w,n,U):
 assert np.all(w==1), 'This diagnostic explicitly covers the uniform frozen inputs.'
 ctx.prec=384
 V=arb_mat([[x**(t-j)*y**j for t in range(n+1) for j in range(t+1)] for x,y in [[aa(v) for v in row] for row in P]])
 T=V.transpose(); B=arb_mat([[aa(v) for v in row] for row in U])
 E=B-V*(T*V).solve(T*B)
 A=np.array([[float(E[i,j].mid()) for j in range(E.ncols())] for i in range(E.nrows())])
 radius=max(float(E[i,j].rad()) for i in range(E.nrows()) for j in range(E.ncols()))
 assert np.isfinite(A).all() and np.isfinite(radius)
 return {'arb_bits':ctx.prec,'reference_outside_monomial_span_norm':norm(A),'max_arb_entry_radius':radius,'reference_orthogonality_norm':norm(U.T@U-np.eye(U.shape[1]))}

def parents_for(z,method):
 if 'parents' in z:return z['parents']
 idx=z['idx'];out=[[-1,-1]]
 for k in range(1,len(idx)):
  candidates=[]
  for p in range(k):
   d=idx[k]-idx[p]
   if tuple(d) in [(1,0),(0,1)]: candidates.append((p,int(np.argmax(d))))
  p,axis=min(candidates);out.append([1-axis,p]) # yx stored coordinates
 return np.array(out)

def check(P,Q,H,parents,U):
 Q=np.asarray(Q,LD);H=np.asarray(H,LD);P=np.asarray(P,LD);U=np.asarray(U,LD)
 assert np.all(Q[:,0]==Q[0,0]) and np.all(np.diag(H)[1:]>0)
 N=Q.shape[1];error=np.zeros_like(Q);local=[];scaled=[]
 # d_k is the directly measured normalized recurrence defect. This is an
 # independently written form of the triangular frozen polynomial identity.
 for k in range(1,N):
  axis,p=map(int,parents[k]);assert axis in (0,1) and 0<=p<k
  raw=P[:,axis]*Q[:,p];projection=np.sum(Q[:,:k]*H[:k,k],axis=1);beta=H[k,k]
  residual=beta*Q[:,k]-raw+projection
  error[:,k]=(residual+P[:,axis]*error[:,p]-np.sum(error[:,:k]*H[:k,k],axis=1))/beta
  size=np.sqrt(np.sum(residual*residual));local.append(size)
  scaled.append(size/(LD(2)**-53*(np.sqrt(raw@raw)+np.sqrt(projection@projection)+beta*np.sqrt(Q[:,k]@Q[:,k]))))
 normal=lambda A:A-U@(U.T@A)
 nq=normal(Q);ne=normal(error)
 return {'normal_Q':norm(nq),'normal_propagated':norm(ne),'reconstruction_defect':norm(nq-ne),'max_local_residual':float(max(local)),'local_residual_fro':float(np.sqrt(np.sum(np.array(local)**2))),'max_local_over_u_operation_sum':float(max(scaled))},nq

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--raw-root',type=pathlib.Path,required=True);ap.add_argument('--receipt',type=pathlib.Path,required=True);a=ap.parse_args();start=time.time()
 baseline=json.loads((ROOT/'topics/padua-lanczos-frontier-20261105/evidence/g4-replay.json').read_text())
 for p,h in baseline['source_sha256'].items():assert sha(ROOT/p)==h
 result={'status':'MEASURED_INDEPENDENT_DIAGNOSTICS','checker_sha256':sha(__file__),'command':[sys.executable,'-B',*sys.argv],'source_pins':baseline['source_sha256'],'longdouble_nmant':np.finfo(LD).nmant,'cases':[],'limitations':['Stored producer Q/H are reused; this is new independent reference/residual arithmetic, not a fresh algorithm rerun.','Historical Q/H and runtime remain unavailable; no historical reconstruction or kernel enclosure.','Final norms use binary64 SVD; no certified theorem or automatic gate decision.']}
 for name in ['rotpi4','triangle']:
  f=np.load(a.raw_root/'attribution'/f'{name}-input.npz');P,w,n=f['P'],f['w'],int(f['n']);ih=hashlib.sha256(P.tobytes()+w.tobytes()).hexdigest()
  saved=json.loads((a.raw_root/'g4'/f'{name}.json').read_text());saved=saved['cases'][0] if 'cases' in saved else saved
  assert ih==saved['input_sha256']
  U=e6.reference(P,w,n,name,P[:128])[0];ref=reference_check(P,w,n,U);print(name,'reference',ref,flush=True)
  row={'name':name,'n':n,'M':len(P),'input_sha256':ih,'reference':ref,'methods':[]};result['cases'].append(row)
  for method in ['upstream_yx','upstream_xy','mirror','alt','adapt']:
   vals=[];normals=[];paths=[]
   for core in ['Haswell','Nehalem']:
    path=a.raw_root/('attribution' if method=='upstream_yx' else 'classes')/(f'{name}-{core}-double.npz' if method=='upstream_yx' else f'{name}-{method}-{core}-double.npz')
    z=np.load(path);assert np.array_equal(P,z['P']) and np.array_equal(w,z['w']);parents=parents_for(z,method)
    val,nq=check(P,z['Q'],z['H'],parents,U);val.update(core=core,raw_sha256=sha(path),raw_path=str(path));vals.append(val);normals.append(nq);paths.append(parents)
   change=norm(normals[0]-normals[1]);ratios=[v['reconstruction_defect']/min(v['normal_Q'],change) for v in vals]
   rr=ref['reference_outside_monomial_span_norm']/min(change,*[v['normal_Q'] for v in vals])
   row['methods'].append({'method':method,'controls':vals,'kernel_normal_difference':change,'kernel_parent_path_equal':bool(np.array_equal(*paths)),'reconstruction_quality_ratios':ratios,'reference_quality_ratio':rr,'prospective_one_percent_quality_pass':max(*ratios,rr)<.01})
   result['elapsed_seconds']=time.time()-start;a.receipt.write_text(json.dumps(result,indent=2)+'\n');print(name,method,ratios,rr,flush=True)
 print('complete',time.time()-start,flush=True)
if __name__=='__main__':main()
