#!/usr/bin/env python3
"""Same frozen BJ node-sign witness, all output columns, exact rational readout.
No new sign search, comparator-envelope regeneration, status or ID assignment.
"""
import argparse,gzip,hashlib,json,math,pathlib,platform,sys,time
import numpy as np
import flint
from flint import fmpq as Q,fmpq_mat as Mat
ROOT=pathlib.Path(__file__).resolve().parents[3]
PINS={'e1_exact.py':'19ce7b774e5a6fa56108eebca3b2ef81f5237328e518d95225adf9f8835e060f','e1_cgs2.py':'426630eb916e13bb14409f6f7b8ea310eaeb1bf7949de10866d163aad31c7b4b'}
LOWER_PIN='fae9c8743c78230ef0aa82c185d1efe0eee37be066982a37d39d920af95719f0'
UPPER=13462956266
UPPER_CODE='0da27e69ddd3cff5ca23e3fcac764f53891ad164ffab20324540fd67d2faf901'
def sha(p):
 h=hashlib.sha256()
 with open(p,'rb') as f:
  for x in iter(lambda:f.read(1048576),b''):h.update(x)
 return h.hexdigest()
def ident(p):return {'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)}
def event(**x):print(json.dumps(x),flush=True)
def sign(x):return 1 if x>0 else -1 if x<0 else 0
def normal(v,b,d,ex):
 r=v
 for row,dk in zip(b,d):r=r-ex.dot(row,v)/dk*row
 return r

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--frozen-evidence',required=True);ap.add_argument('--upper-receipt',required=True);ap.add_argument('--output-dir',required=True);ap.add_argument('--receipt',required=True);a=ap.parse_args()
 start=time.monotonic();out=pathlib.Path(a.output_dir);out.mkdir(parents=True,exist_ok=False)
 src=ROOT/'tracks/bivariate-lanczos/code/drift'
 for f,h in PINS.items():assert sha(src/f)==h
 lowerpath=pathlib.Path(a.frozen_evidence)/'e1-multinode-certificates.json';assert sha(lowerpath)==LOWER_PIN
 lower=json.loads(lowerpath.read_text());old=next(x for x in lower['witnesses'] if x['set']=='rotated' and x['rule']=='bj')
 assert old['degree']==12 and old['target_column']==90
 s=old['node_signs'];assert len(s)==625 and set(s)<={-1,1}
 G=Q(old['explicit_greedy_sign_lower_squared']['exact'])
 upper=json.loads(pathlib.Path(a.upper_receipt).read_text());assert upper['code_sha256']==UPPER_CODE and upper['new_upper_integer']==UPPER and upper['old_frobenius_exactly_reproduced']
 assert any(x['U_integer_upper']==UPPER and x['step']==3 for x in upper['candidates'])
 sys.path.insert(0,str(src));import e1_exact as ex
 coords,b,d,rec,metadata=ex.build(ex.points('rotated'),12,'bj');M,N=len(coords[0]),len(b)
 assert (M,N)==(625,91) and all(x>0 for x in d)
 V=[Mat(1,M) for _ in range(N)];seen=[]
 for h in range(1,N):
  axis,parent,alpha,_=rec[h];u=ex.multiply(b[parent],coords[axis]);rho=[]
  for i in range(M):
   products=Q(0);sums=Q(0);partial=Q(0)
   for l,c in enumerate(alpha):
    term=c*b[l][0,i];products+=abs(term);partial+=term
    if l>=1:sums+=abs(partial)
   rho.append(abs(u[0,i])+products+sums+3*abs(b[h][0,i]))
  g=[None]*N;g[h]=Mat([[1]*M])
  for k in range(h+1,N):
   axis,parent,alpha,_=rec[k];v=ex.multiply(g[parent],coords[axis]) if parent>=h else Mat(1,M)
   for l in range(h,k):
    if alpha[l]:v=v-alpha[l]*g[l]
   g[k]=v
  f=[s[i]*sign(g[90][0,i])*rho[i] for i in range(M)]
  assert all(abs(fi)<=ri for fi,ri in zip(f,rho))
  for k in range(h,N):V[k]=V[k]+ex.multiply(g[k],f)
  seen.append(h);event(event='full_witness_source',source=h)
 assert seen==list(range(1,91)) and V[0]==Mat(1,625)
 projected=normal(V[90],b,d,ex);control=ex.dot(projected,projected)/d[90];assert control==G
 event(event='old_target_exactly_reproduced',elapsed=time.monotonic()-start)
 raw=out/'full-witness.jsonl.gz'
 with gzip.open(raw,'wt') as f:
  f.write(json.dumps({'schema':'full-old-witness-v1','M':625,'N':91,'sources':seen,'d':[str(x) for x in d],'node_signs':s,'target':90})+'\n')
  for k in range(N):f.write(json.dumps({'k':k,'b':[str(b[k][0,i]) for i in range(M)],'V':[str(V[k][0,i]) for i in range(M)]})+'\n')
 Bf=np.array([[float(v[0,i])/math.sqrt(float(dk)) for i in range(M)] for v,dk in zip(b,d)]).T
 W=np.array([[float(v[0,i])/math.sqrt(float(dk)) for i in range(M)] for v,dk in zip(V,d)]).T
 W=W-Bf@(Bf.T@W)
 _,sigma,right=np.linalg.svd(W,full_matrices=False)
 x=right[0]/np.sqrt(np.array([float(z) for z in d]));x[0]=0;x/=max(abs(x))
 assert np.all(np.isfinite(x)) and max(abs(x))==1
 trials=[];passed=False
 for scale in [10**6,10**9,10**12]:
  t=[int(round(float(z)*scale)) for z in x];assert t[0]==0 and any(t[1:])
  v=Mat(1,625)
  for tk,Vk in zip(t,V):
   if tk:v=v+tk*Vk
  rv=normal(v,b,d,ex);num=ex.dot(rv,rv);den=sum((dk*tk*tk for dk,tk in zip(d,t)),Q(0));assert num>=0 and den>0
  lowergain=num/den;L=int(lowergain.numerator)//int(lowergain.denominator);assert L<=lowergain<L+1
  passed=lowergain>100*UPPER
  record={'scale':scale,'monic_coefficients':t,'lower_exact':str(lowergain),'lower_integer_floor':L,'denominator_exact':str(den),'pass_exact':bool(passed),'pass_integer_floor':bool(L>100*UPPER)}
  cp=out/('readout-%d.json'%scale);cp.write_text(json.dumps(record,indent=2)+'\n')
  trials.append({'scale':scale,'lower_float_display':float(lowergain),'lower_integer_floor':L,'pass_exact':bool(passed),'pass_integer_floor':bool(L>100*UPPER),'artifact':ident(cp)})
  event(event='readout',scale=scale,lower_integer_floor=L,passes=bool(passed))
  if passed:break
 receipt={'result':'FULL_OUTPUT_READOUT_PASSES' if passed else 'INCONCLUSIVE_FULL_OUTPUT_READOUT','scope':{'set':'rotated Q24','degree':12,'rule':'bj','sources':90,'outputs':90,'target_signs':90,'node_signs':'identical inherited625signs','local_error':'s_i sign(g90,h(i)) rho_hi; same frozen formal cube witness'},'rules_head':'684849d7d19ac2604213ae3d4f499d3436f58b3d','source_sha256':PINS,'lower_input':ident(lowerpath),'upper_input':ident(pathlib.Path(a.upper_receipt)),'code_sha256':sha(__file__),'old_target_projection_exactly_reproduced':True,'fixed_comparator_upper_integer':UPPER,'required_lower_strict_threshold':100*UPPER,'float_proposal_only':{'largest_singular_value_display':float(sigma[0]),'normalization':'monicx=a/sqrt(d), maxabs=1','quantizations':[10**6,10**9,10**12]},'readouts':trials,'raw_full_witness':ident(raw),'command':[sys.executable,'-B',str(pathlib.Path(__file__).resolve()),*sys.argv[1:]],'runtime':{'python':platform.python_version(),'python_flint':flint.__version__,'numpy':np.__version__,'elapsed_seconds':time.monotonic()-start},'retention':'Temporary external working artifacts; archive/delivery pending orchestrator cold-storage process. Reproduce with a new output directory.','limits':['Same formal relative-error witness; no new node/source sign search.','Failure of this readout gives no upper on BJ capacity and does not kill true factor-ten target.','No actual IEEE lower, finite-epsilon or all-degree conclusion.','Developer computation; independent regeneration/check remains separate.']}
 pathlib.Path(a.receipt).write_text(json.dumps(receipt,indent=2)+'\n');event(event='complete',result=receipt['result'],elapsed=time.monotonic()-start)
if __name__=='__main__':main()
