#!/usr/bin/env python3
"""Exact PD-T137 vectors as integer FLINT rows/common positive denominators.
All original nodes/sources; no compression, interval arithmetic, fits or G1 verdict.
"""
import argparse,gzip,hashlib,json,pathlib,platform,signal,sys,time
import flint
from flint import fmpq as Q,fmpz as Z,fmpz_mat as IM
ROOT=pathlib.Path(__file__).resolve().parents[3]
PIN='19ce7b774e5a6fa56108eebca3b2ef81f5237328e518d95225adf9f8835e060f'
OLD='0d9c236fe879879b7f546596c554d213b7b8c408d31dec08dd79146c7d629344'
FIELDS=['Knode_squared','KHS_squared','Urow_squared','upper_squared']
def N(n):return (n+1)*(n+2)//2
def sha(p):return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def ident(p):return {'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)}
def event(**v):print(json.dumps(v),flush=True)
class V:
 def __init__(self,row,den=1):
  den=Z(den);assert den and row.nrows()==1 and row.ncols()>0
  if den<0:row=-row;den=-den
  if row.is_zero():den=Z(1)
  elif den!=1:
   g=den
   for j in range(row.ncols()):
    g=g.gcd(row[0,j])
    if g==1:break
   if g!=1:row=IM([[z//g for z in row.entries()]]);den//=g
  self.z=row;self.D=den;self._a=None
 @property
 def a(self):
  if self._a is None:self._a=tuple(self.z.entries())
  return self._a
 @classmethod
 def const(cls,M,n):return cls(IM([[n]*M]))
 @classmethod
 def qs(cls,qs):
  D=Z(1)
  for q in qs:D=D.lcm(q.denominator)
  return cls(IM([[q.numerator*(D//q.denominator) for q in qs]]),D)
 @classmethod
 def linear_combination(cls,M,terms):
  """Exact integer lcm-weighted sum, canonicalized only after all terms."""
  assert M>0
  weighted=[];D=Z(1)
  for c,v in terms:
   assert v.z.nrows()==1 and v.z.ncols()==M
   c=Q(c)
   if c:
    den=v.D*c.denominator;D=D.lcm(den)
    weighted.append((c.numerator,den,v.z))
  row=IM(1,M)
  for num,den,z in weighted:row=row+z*(num*(D//den))
  return cls(row,D)
 def scale(self,c):
  c=Q(c)
  if not c:return V.const(len(self.a),0)
  return V(self.z*c.numerator,self.D*c.denominator)
 def __add__(self,o):
  D=self.D.lcm(o.D);return V(self.z*(D//self.D)+o.z*(D//o.D),D)
 def __sub__(self,o):
  D=self.D.lcm(o.D);return V(self.z*(D//self.D)-o.z*(D//o.D),D)
 def mul(self,o):
  assert self.z.ncols()==o.z.ncols()
  return V(IM([[x*y for x,y in zip(self.a,o.a)]]),self.D*o.D)
 def add_square_scaled(self,g,c):
  """Return self+c*g^2 with one final common-content normalization."""
  assert self.z.ncols()==g.z.ncols()
  c=Q(c);den=g.D*g.D*c.denominator;D=self.D.lcm(den)
  row=self.z*(D//self.D)
  if c:row=row+IM([[x*x for x in g.a]])*(c.numerator*(D//den))
  return V(row,D)
 def square(self):return V(IM([[x*x for x in self.a]]),self.D*self.D)
 def dot(self,o):
  assert self.z.ncols()==o.z.ncols()
  return Q((self.z*o.z.transpose())[0,0],self.D*o.D)
 def eq(self,other):return self.z*other.D==other.z*self.D
 def asq(self):return [Q(z,self.D) for z in self.a]

class Peaks:
 """One unreduced positive-denominator pair per ORIGINAL node; strict ties."""
 def __init__(self,M):
  assert M>0
  self.num=[Z(0)]*M;self.den=[Z(1)]*M;self.who=[0]*M
 def add(self,nums,den,h):
  den=Z(den);assert den>0 and h>0 and len(nums)==len(self.num)
  for i,x in enumerate(nums):
   if x*self.den[i]>self.num[i]*den:self.num[i]=x;self.den[i]=den;self.who[i]=h
 def best(self,normal):
  assert len(normal.a)==len(self.num) and min(normal.a)>=0
  num=Z(0);den=Z(1);witness=(0,0)
  for i,(z,x,D,h) in enumerate(zip(normal.a,self.num,self.den,self.who)):
   nn=z*x;dd=normal.D*D;left=nn*den;right=num*dd
   if left>right or (left==right and (h,i)<witness):num,den,witness=nn,dd,(h,i)
  return Q(num,den),witness

def arithmetic_controls():
 x=[Q(-2,3),Q(0),Q(4,9),Q(7,12),Q(-10,21),Q(2,3)];y=[Q(1,5),Q(-3,7),Q(0),Q(9,2),Q(-1,4),Q(2,3)];a=V.qs(x);b=V.qs(y)
 assert (a+b).asq()==[u+v for u,v in zip(x,y)]
 assert (a-b).asq()==[u-v for u,v in zip(x,y)]
 assert a.scale(Q(-7,11)).asq()==[u*Q(-7,11) for u in x]
 assert a.mul(b).asq()==[u*v for u,v in zip(x,y)]
 assert a.square().asq()==[u*u for u in x]
 assert a.dot(b)==sum((u*v for u,v in zip(x,y)),Q(0))
 for terms in [[],[(Q(0),a)],[(Q(1),a),(Q(-1),a)],[(Q(-7,11),a),(Q(5,13),b),(Q(2,9),a)],[(Q(3,2),a),(Q(-6,4),a),(Q(0),b)]]:
  got=V.linear_combination(6,terms)
  assert got.asq()==[sum((c*v.asq()[i] for c,v in terms),Q(0)) for i in range(6)]
  if not any(got.a):assert got.D==1
 for base,g,c in [(a,b,Q(-7,11)),(b,a,Q(0)),(a,a,Q(13,21)),(a.square().scale(-1),a,Q(1)),(V.const(6,0),b,Q(5,17))]:
  fused=base.add_square_scaled(g,c)
  assert fused.asq()==[u+c*v*v for u,v in zip(base.asq(),g.asq())]
  if not any(fused.a):assert fused.D==1
 peaks=Peaks(6);peaks.add(a.a,a.D,2);peaks.add(b.a,b.D,5)
 assert [Q(n,d) for n,d in zip(peaks.num,peaks.den)]==[max(Q(0),u,v) for u,v in zip(x,y)] and peaks.who[-1]==2
 peaks.add([2*z for z in b.a],2*b.D,9);assert peaks.who[-1]==2
 gain,witness=peaks.best(V.qs([Q(i) for i in range(1,7)]));assert gain==18 and witness==(5,3)
 assert (a-a).D==1 and (a-a).z.is_zero()
 assert V(IM([[6,-9,0]]),-15).asq()==[Q(-2,5),Q(3,5),Q(0)]
 bad=[lambda:a.add_square_scaled(V.const(5,1),0),lambda:V.linear_combination(0,[]),lambda:V.linear_combination(6,[(0,V.const(5,1))]),lambda:V(IM([[1]]),0),lambda:V(IM([[1,2],[3,4]])),lambda:a.mul(V.const(5,1)),lambda:a.dot(V.const(5,1)),lambda:Peaks(0),lambda:peaks.add([Z(1)]*6,0,1),lambda:peaks.add([Z(1)]*6,-1,1),lambda:peaks.add([Z(1)]*5,1,1),lambda:peaks.add([Z(1)]*6,1,0)]
 for fn in bad:
  try:fn()
  except AssertionError:continue
  raise AssertionError('Malformed primitive was accepted')
 return {'fused_energy_signed_zero_cancellation_controls':True,'batched_signed_zero_repeated_terms_and_cancellation_controls':True,'signed_zero_common_content_add_mul_dot_square_max_controls':True,'control_vector_length':6,'unreduced_peak_pairs_and_strict_ties':True,'malformed_primitive_controls_rejected':len(bad)}

def build(coords,n,rule,state):
 M=len(coords[0].a);b=[V.const(M,1)];d=[Q(M)];rec=[None];meta=[(0,0)];pos={(0,0):0};ties=[]
 for t in range(1,n+1):
  for j in range(t+1):
   axes=[a for a in (0,1) if (a==0 and j<t) or(a==1 and j>0)]
   if rule!='pivot':
    wanted=0 if ((rule=='bj' and j==0) or(rule=='mirror' and j!=t) or(rule=='alt' and 2*j<t)) else 1
    axes=[wanted if wanted in axes else axes[0]]
   candidates=[]
   for axis in axes:
    p=pos[t-1,j-(axis==1)];u=coords[axis].mul(b[p]);sigma=u.dot(u);alpha=[v.dot(u)/dk for v,dk in zip(b,d)]
    r=V.linear_combination(M,[(1,u)]+[(-c,v) for c,v in zip(alpha,b)])
    dk=r.dot(r);assert dk>0 and sigma>0
    candidates.append((dk/sigma,axis,p,alpha,sigma,r,dk))
   if len(candidates)==2 and candidates[0][0]==candidates[1][0]:ties.append([t,j])
   _,axis,p,alpha,sigma,r,dk=max(candidates,key=lambda c:(c[0],-c[1]))
   assert all(not old.dot(r) for old in b)
   pos[t,j]=len(b);b.append(r);d.append(dk);rec.append((axis,p,alpha,sigma));meta.append((t,j))
  state['basis_degree']=t;event(event='basis_degree',degree=t)
 return b,d,rec,meta,ties

def rawdump(p,coords,b,d,rec,meta,ties):
 with gzip.open(p,'wt') as f:
  f.write(json.dumps({'representation':'integer row/common positive denominator','coordinates':[[str(z) for z in c.a] for c in coords],'coordinate_denominators':[str(c.D) for c in coords],'M':len(coords[0].a),'N':len(b),'ties':ties})+'\n')
  for k,v in enumerate(b):f.write(json.dumps({'k':k,'meta':meta[k],'num':[str(z) for z in v.a],'D':str(v.D),'d':str(d[k]),'rec':None if k==0 else [rec[k][0],rec[k][1],[str(q) for q in rec[k][2]],str(rec[k][3])]})+'\n')

def run(a,out,state):
 t0=time.monotonic();c0=time.process_time();controls=arithmetic_controls();src=ROOT/'tracks/bivariate-lanczos/code/drift/e1_exact.py';assert sha(src)==PIN and sha(a.old_sweep)==OLD
 sys.path.insert(0,str(src.parent));import e1_exact as ex
 old={(x['set'],x['rule'],x['degree']):x for x in json.loads(pathlib.Path(a.old_sweep).read_text())['runs']}
 xy=ex.points(a.set);M=len(xy);coords=[V.qs([p[axis] for p in xy]) for axis in(0,1)];assert M in(325,625) and M>N(a.degree)
 b,d,rec,meta,ties=build(coords,a.degree,a.rule,state);tb=time.monotonic();cb=time.process_time()
 fresh=[]
 for n in [2,3,4]:
  if n>a.degree:continue
  cc,bb,dd,rr,mm=ex.build(xy,n,a.rule)
  assert dd==d[:N(n)] and rr==rec[:N(n)] and mm==meta[:N(n)]
  assert all(b[k].asq()==[bb[k][0,i] for i in range(M)] for k in range(N(n)))
  fresh.append(n)
 raw=out/'baseline.jsonl.gz';rawdump(raw,coords,b,d,rec,meta,ties)
 stages=list(range(2,a.degree+1));ends={N(n)-1:n for n in stages};normal={};pdiag=V.const(M,0)
 for k,bk in enumerate(b):
  pdiag=pdiag+bk.square().scale(1/d[k])
  if k in ends:
   norm=V.const(M,1)-pdiag;assert min(norm.a)>=0 and norm.dot(V.const(M,1))==M-k-1;normal[ends[k]]=norm
 sums={n:V.const(M,0) for n in stages};peaks={n:Peaks(M) for n in stages};records=[]
 def collect(n,h,energy):
  val=energy.scale(rec[h][3]);sums[n]=sums[n]+val;peaks[n].add(val.a,val.D,h)
 def finish(n):
  L,w=peaks[n].best(normal[n])
  H=normal[n].dot(sums[n]);R=Q(max(sums[n].a),sums[n].D);U=min(H,R);assert 0<L<=U
  r={'set':a.set,'rule':a.rule,'degree':n,'sources':'all','source_count':N(n)-1,'point_count':M,'basis_count':N(n),'Knode_squared':{'exact':str(L),'float':float(L)},'KHS_squared':{'exact':str(H),'float':float(H)},'Urow_squared':{'exact':str(R),'float':float(R)},'upper_squared':{'exact':str(U),'float':float(U)},'pivot_choices':['XY'[v[0]] for v in rec[1:N(n)]],'pivot_ties':[v for v in ties if v[0]<=n],'normal_trace_exact':str(M-N(n)),'witness':{'source':w[0],'node':w[1]}}
  if n<=12:
   prior=old[a.set,a.rule,n];assert all(r[f]['exact']==prior[f]['exact'] for f in FIELDS) and r['pivot_choices']==prior['pivot_choices']
  if a.rule=='pivot' and n<=12:assert r['pivot_ties']==([] if a.set=='triangle' else [[2,1]])
  records.append(r);(out/'endpoints.json').write_text(json.dumps({'runs':records},indent=2)+'\n');state['completed_degrees']=[r['degree'] for r in records];event(event='endpoint',degree=n)
 for h in range(1,len(b)):
  g=[None]*len(b);g[h]=V.const(M,1);energy=V.const(M,1).scale(1/d[h])
  if h in ends:collect(ends[h],h,energy)
  for k in range(h+1,len(b)):
   axis,p,alpha,_=rec[k];v=coords[axis].mul(g[p]) if p>=h else V.const(M,0)
   v=V.linear_combination(M,[(1,v)]+[(-alpha[l],g[l]) for l in range(h,k)])
   g[k]=v;energy=energy.add_square_scaled(v,1/d[k])
   if k in ends:collect(ends[k],h,energy)
  state['last_source']=h
  if h in ends:finish(ends[h])
  event(event='source',source=h,total=len(b)-1)
 assert len(records)==a.degree-1
 comparison=None;compared=[]
 if a.compare:
  text=pathlib.Path(a.compare).read_text()
  try:otherrows=json.loads(text)['runs']
  except json.JSONDecodeError:otherrows=[json.loads(line) for line in text.splitlines() if line.strip()]
  other={r['degree']:r for r in otherrows}
  for r in records:
   if r['degree'] in other:
    o=other[r['degree']];compared.append(r['degree']);assert all(r[f]['exact']==o[f]['exact'] for f in FIELDS) and r['pivot_choices']==o['pivot_choices'] and r['pivot_ties']==o['pivot_ties']
  comparison=ident(pathlib.Path(a.compare))
  assert compared
  if a.degree==14:assert {13,14}<=set(compared)
  if a.degree==20:assert compared==list(range(2,21))
 return {'result':'EXACT_CASE_COMPLETED','set':a.set,'rule':a.rule,'max_degree':a.degree,'code_sha256':sha(__file__),'frozen_source_sha256':PIN,'old_sweep':ident(pathlib.Path(a.old_sweep)),'controls':{**controls,'fresh_scalar_basis_degrees':fresh,'every_new_column_exact_Gram_pairings':True,'every_old_endpoint_and_choice_matched':a.degree<=12,'X_tie_break_and_recording':True},'normal_trace_role':'consistency only; full exact Gram pairings are separately checked','all_original_nodes':M,'all_source_columns':len(b)-1,'complete_degrees':stages,'endpoint_file':ident(out/'endpoints.json'),'baseline':ident(raw),'additional_exact_comparison':comparison,'additional_exact_comparison_degrees':compared,'timing':{'wall_seconds':time.monotonic()-t0,'process_cpu_seconds':time.process_time()-c0,'basis_wall_seconds':tb-t0,'basis_cpu_seconds':cb-c0},'runtime':{'python':platform.python_version(),'python_flint':flint.__version__},'limits':['Exact vector representation optimization only; no nodes/source/gauge change.','No fits, operational verdict or asymptotic claim.','Independent implementation/check remains separate.','Bulk outputs temporary outside Git; no archive delivery claimed.']}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--set',choices=['triangle','rotated'],required=True);ap.add_argument('--rule',choices=['bj','mirror','alt','pivot'],required=True);ap.add_argument('--degree',type=int,required=True);ap.add_argument('--old-sweep',required=True);ap.add_argument('--output-dir',required=True);ap.add_argument('--receipt',required=True);ap.add_argument('--seconds',type=int,default=120);ap.add_argument('--compare');ap.add_argument('--high20-approved-benchmark');a=ap.parse_args();assert (4<=a.degree<=14 or a.degree==20) and a.seconds>0
 if a.degree<=12:assert a.seconds<=120
 elif a.degree<=14:assert a.seconds<=180
 else:
  assert a.set=='rotated' and a.rule=='bj' and a.seconds<=600 and a.compare and a.high20_approved_benchmark
  guard=json.loads(pathlib.Path(a.high20_approved_benchmark).read_text())
  assert guard['result']=='EXACT_CASE_COMPLETED' and guard['max_degree']==14 and guard['set']=='rotated' and guard['rule']=='bj'
  assert guard['code_sha256']==sha(__file__) and guard['timing']['wall_seconds']<=60 and {13,14}<=set(guard['additional_exact_comparison_degrees'])
 out=pathlib.Path(a.output_dir);out.mkdir(parents=True,exist_ok=False);state={'basis_degree':0,'last_source':0,'completed_degrees':[]};start=time.monotonic();cpu=time.process_time()
 def expire(*_):raise TimeoutError('Prospective bounded case cap')
 signal.signal(signal.SIGALRM,expire);signal.alarm(a.seconds)
 try:r=run(a,out,state)
 except TimeoutError:r={'result':'INCOMPLETE_COST_CAP','set':a.set,'rule':a.rule,'max_degree':a.degree,'code_sha256':sha(__file__),'state':state,'wall_seconds':time.monotonic()-start,'process_cpu_seconds':time.process_time()-cpu,'limits':'No missing-source endpoint or completed-case claim.'}
 signal.alarm(0);r['rules_head']='9825d184517db81d0aad8542fbd6639f2164b803';r['command']=[sys.executable,'-B',str(pathlib.Path(__file__).resolve()),*sys.argv[1:]];pathlib.Path(a.receipt).write_text(json.dumps(r,indent=2)+'\n');event(event='complete',result=r['result'])
if __name__=='__main__':main()
