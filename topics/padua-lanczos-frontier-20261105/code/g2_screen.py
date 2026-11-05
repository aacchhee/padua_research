#!/usr/bin/env python3
"""Exact LOWER-only G2 W screens: fixed s11, sources6,4,3,5, all nodes.
No source-subset upper/expectation, span substitution, or all-degree claim.
"""
import argparse,gzip,hashlib,json,pathlib,platform,sys,time
import flint
from flint import fmpq as Q,fmpq_mat as Mat
ROOT=pathlib.Path(__file__).resolve().parents[3]
PIN='19ce7b774e5a6fa56108eebca3b2ef81f5237328e518d95225adf9f8835e060f'
REDUCTION_PIN='44498c6230d0a59bbd0cfc4bc96600f0b401eb92ba9302b5c1d54cc569c8d5f9'
def sha(p):return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def ident(p):return {'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)}
def event(**x):print(json.dumps(x),flush=True)
def N(s):return (s+1)*(s+2)//2
def rows(v,M):return Mat([[r[0,i] for i in range(M)] for r in v])
def diagonal(v):return Mat([[v[i] if i==j else 0 for j in range(len(v))] for i in range(len(v))])
def gram_and_cx(ex,coords,b,d,n):
 M=len(coords[0]);B=rows(b,M);G=B*B.transpose()
 assert all(G[i,j]==(d[i] if i==j else 0) for i in range(len(b)) for j in range(len(b)))
 xb=[ex.multiply(v,coords[0]) for v in b[:N(n-1)]];GX=B*rows(xb,M).transpose();C=Mat(len(b),len(xb));sparse=[]
 for j in range(len(xb)):
  terms=[];v=Mat(1,M);deg=next(t for t in range(n) if j<N(t))
  for l in range(len(b)):
   c=GX[l,j]/d[l];C[l,j]=c
   if c:terms.append((l,c));v=v+c*b[l]
   if l>=N(deg+1):assert c==0
  assert v==xb[j];sparse.append(terms)
 return C,sparse

def responses(ex,coords,rec,h):
 g=[None]*len(rec);g[h]=Mat([[1]*len(coords[0])])
 for k in range(h+1,len(rec)):
  axis,p,alpha,_=rec[k];v=ex.multiply(g[p],coords[axis]) if p>=h else Mat(1,len(coords[0]))
  for l in range(h,k):
   if alpha[l]:v=v-alpha[l]*g[l]
  g[k]=v
 return g

def omega(ex,coords,g,h,sparse,count):
 ans=[];M=len(coords[0])
 for j in range(count):
  v=ex.multiply(g[j],coords[0]) if j>=h else Mat(1,M)
  for l,c in sparse[j]:
   if l>=h:v=v-c*g[l]
  ans.append(v)
 return ans

def small_projector_control(ex):
 # Exact independent differentiation of full rational projector matrices.
 xy=[(Q(i,12)-1,Q(j,12)-1) for i in range(4) for j in range(4-i)]
 coords,b,d,rec,_=ex.build(xy,2,'bj');M=len(xy);C,sparse=gram_and_cx(ex,coords,b,d,2);B=rows(b,M).transpose();X=diagonal(coords[0]);I=diagonal([Q(1)]*M);checks=0
 def span(k):
  BB=Mat([[B[i,j] for j in range(k)] for i in range(M)]);D=diagonal([1/z for z in d[:k]]);P=BB*D*BB.transpose();return BB,D,P,I-P
 for h,node in [(1,0),(4,M-1)]:
  g=responses(ex,coords,rec,h);V=[Mat(1,M) for _ in b]
  for k in range(h,len(b)):V[k][0,node]=g[k][0,node]
  # Alternative coefficient and beta derivatives give arbitrary polynomial
  # forcing at every column, then propagate through the full recurrence.
  W=[Mat(1,M)]
  for k in range(1,len(b)):
   axis,p,alpha,_=rec[k];v=ex.multiply(W[p],coords[axis])+((k+1)*b[0]-(k+2)*b[k])
   for l,c in enumerate(alpha):
    if c:v=v-c*W[l]
   if k==h:v[0,node]+=1
   W.append(v)
  for s in [0,1]:
   Bs,Ds,Ps,Rs=span(N(s));Bt,Dt,Pt,Rt=span(N(s+1))
   def pdot(Z,k,BB,D,R):
    ZM=rows(Z[:k],M).transpose();return R*ZM*D*BB.transpose()+BB*D*ZM.transpose()*R
   actual=-(pdot(W,N(s+1),Bt,Dt,Rt)*X*Ps)+Rt*X*pdot(W,N(s),Bs,Ds,Rs)
   Vs=rows(V[:N(s)],M).transpose();Vt=rows(V[:N(s+1)],M).transpose();CC=Mat([[C[l,j] for j in range(N(s))] for l in range(N(s+1))])
   predicted=Rt*(X*Vs-Vt*CC)*Ds*Bs.transpose();assert actual==predicted
   plain=-(pdot(V,N(s+1),Bt,Dt,Rt)*X*Ps)+Rt*X*pdot(V,N(s),Bs,Ds,Rs);assert plain==actual
   checks+=1
 return {'generic_rational_nodes':M,'degree':2,'stage_source_controls':checks,'full_projector_derivative_agrees':True,'alternative_coefficient_and_beta_derivatives_agree':True}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--set',choices=['triangle','rotated'],required=True);ap.add_argument('--output-dir',required=True);ap.add_argument('--receipt',required=True);a=ap.parse_args();start=time.monotonic();out=pathlib.Path(a.output_dir);out.mkdir(parents=True,exist_ok=False)
 src=ROOT/'tracks/bivariate-lanczos/code/drift/e1_exact.py';assert sha(src)==PIN
 reduction=pathlib.Path(__file__).resolve().parents[1]/'theory/l2-smooth-rule-closure-reduction.md';assert sha(reduction)==REDUCTION_PIN
 sys.path.insert(0,str(src.parent));import e1_exact as ex
 controls=small_projector_control(ex);coords,b,d,rec,metadata=ex.build(ex.points(a.set),12,'bj');M=len(coords[0]);assert len(b)==91 and M in(325,625) and min(d)>0 and all(rec[k][3]>0 for k in range(1,91))
 C,sparse=gram_and_cx(ex,coords,b,d,12);normal=[1-sum((bk[0,i]**2/dk for bk,dk in zip(b,d)),Q(0)) for i in range(M)]
 assert min(normal)>=0 and max(normal)<=1 and sum(normal)==M-91
 X2=max(x*x for x in coords[0]);assert X2==(Q(1) if a.set=='triangle' else Q(49,25))
 baseline=out/'baseline.jsonl.gz'
 with gzip.open(baseline,'wt') as f:
  f.write(json.dumps({'set':a.set,'rule':'bj','M':M,'N':91,'coordinates':[[str(x) for x in c] for c in coords],'d':[str(x) for x in d],'Xnorm_squared':str(X2),'source_range':[1,90]})+'\n')
  for k in range(91):f.write(json.dumps({'k':k,'meta':metadata[k],'b':[str(b[k][0,i]) for i in range(M)],'rec':None if k==0 else [rec[k][0],rec[k][1],[str(x) for x in rec[k][2]],str(rec[k][3])]})+'\n')
 trials=[];passed=False
 for h in [6,4,3,5]:
  g=responses(ex,coords,rec,h);om=omega(ex,coords,g,h,sparse,78)
  # X-formed pure-power child relation, including source/top-degree sign.
  for t in range(12):
   j=N(t-1) if t else 0;child=N(t)
   assert all(om[j][0,i]==(-1 if h==child else 0) for i in range(M))
  energies=[sum((v[0,i]**2/dj for v,dj in zip(om,d[:78])),Q(0)) for i in range(M)]
  ell=[rec[h][3]*normal[i]*energies[i] for i in range(M)];value=max(ell);node=ell.index(value);normalized=value/X2;floor=int(normalized.numerator)//int(normalized.denominator);assert floor<=normalized<floor+1
  # Independently form and project the actual monic impulse closure matrix.
  raw=Mat(M,78)
  for j in range(78):
   raw[node,j]=(coords[0][node]*g[j][0,node] if j>=h else 0)-sum((C[l,j]*g[l][0,node] for l in range(h,91)),Q(0))
  BM=rows(b,M);Dinv=diagonal([1/z for z in d]);projected=raw-BM.transpose()*Dinv*(BM*raw)
  direct=rec[h][3]*sum((sum((projected[i,j]**2 for i in range(M)),Q(0))/d[j] for j in range(78)),Q(0));assert direct==value
  passed=normalized>=65536
  rp=out/f'impulse-h{h}.json';rp.write_text(json.dumps({'stage':11,'source':h,'source_degree_index':metadata[h],'maximizing_node':node,'point':[str(c[node]) for c in coords],'ell_exact':str(value),'normalized_squared_lower_exact':str(normalized),'tau_squared':str(rec[h][3]),'Xnorm_squared':str(X2),'normal_diag_at_node':str(normal[node]),'direct_projected_pulse_exactly_agrees':True,'all_node_ell':[str(v) for v in ell]},indent=2)+'\n')
  trials.append({'stage':11,'source':h,'node':node,'point':[str(c[node]) for c in coords],'normalized_squared_lower_floor':floor,'normalized_squared_lower_display':float(normalized),'passes_saved_W_threshold':bool(passed),'direct_projected_pulse_exactly_agrees':True,'artifact':ident(rp)})
  event(event='W_lower_screen',source=h,normalized_squared_lower_floor=floor,passes=bool(passed))
  if passed:break
 receipt={'result':'W_LOWER_SCREEN_PASSES' if passed else 'W_SCREEN_INCONCLUSIVE','scope':{'set':a.set,'degree':12,'rule':'bj','global_source_count':90,'global_source_range':[1,90],'stage':11,'screen_source_order':[6,4,3,5],'screen_source_role':'subset LOWER only; no screened-source upper or R expectation','node_coverage':M,'saved_W_threshold':256,'squared_W_threshold':65536,'saved_R_threshold':16,'R_status':'NOT_RUN'},'rules_head':'0e493be7f9883e00e6260cf6b081c607a230177f','frozen_source_sha256':PIN,'analytic_reduction_sha256':REDUCTION_PIN,'code_sha256':sha(__file__),'controls':{**controls,'full_degree12_Gram_diagonal':True,'full_X_expansion_with_top_degree':True,'positive_d_and_tau_squared':True,'normal_diag_in_unit_interval':True,'normal_trace_exact':str(sum(normal)),'X_formed_child_omega_sign_identity':True},'baseline':ident(baseline),'screens':trials,'command':[sys.executable,'-B',str(pathlib.Path(__file__).resolve()),*sys.argv[1:]],'runtime':{'python':platform.python_version(),'python_flint':flint.__version__,'elapsed_seconds':time.monotonic()-start},'limits':['Formal first-order smooth exact-base rule class only; original working-precision PD-T055 remains distinct.','No span-condition substitution, actual IEEE or all-degree conclusion.','A failed lower screen is inconclusive, not W FAIL. R requires all sources/stages and is not computed here.','Developer result; independent checker/execution remains separate.','Bulk arrays are external temporary working evidence; archive/delivery pending.']}
 pathlib.Path(a.receipt).write_text(json.dumps(receipt,indent=2)+'\n');event(event='complete',result=receipt['result'],elapsed=time.monotonic()-start)
if __name__=='__main__':main()
