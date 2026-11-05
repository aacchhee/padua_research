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
  den=Z(den);assert den
  if den<0:row=-row;den=-den
  if row.is_zero():den=Z(1)
  elif den!=1:
   g=den
   for z in row.entries():
    g=g.gcd(z)
    if g==1:break
   if g!=1:row=IM([[z//g for z in row.entries()]]);den//=g
  self.z=row;self.D=den;self.a=tuple(row.entries())
 @classmethod
 def const(cls,M,n):return cls(IM([[n]*M]))
 @classmethod
 def qs(cls,qs):
  D=Z(1)
  for q in qs:D=D.lcm(q.denominator)
  return cls(IM([[q.numerator*(D//q.denominator) for q in qs]]),D)
 def scale(self,c):
  c=Q(c)
  if not c:return V.const(len(self.a),0)
  return V(self.z*c.numerator,self.D*c.denominator)
 def __add__(self,o):
  D=self.D.lcm(o.D);return V(self.z*(D//self.D)+o.z*(D//o.D),D)
 def __sub__(self,o):
  D=self.D.lcm(o.D);return V(self.z*(D//self.D)-o.z*(D//o.D),D)
 def mul(self,o):return V(IM([[x*y for x,y in zip(self.a,o.a)]]),self.D*o.D)
 def square(self):return V(IM([[x*x for x in self.a]]),self.D*self.D)
 def dot(self,o):return Q((self.z*o.z.transpose())[0,0],self.D*o.D)
 def eq(self,other):return self.z*other.D==other.z*self.D
 def asq(self):return [Q(z,self.D) for z in self.a]
 def maxwith(self,o,previous,h):
  D=self.D.lcm(o.D);a=self.z*(D//self.D);b=o.z*(D//o.D);aa=a.entries();bb=b.entries();vals=[];who=[]
  for x,y,old in zip(aa,bb,previous):
   if y>x:vals.append(y);who.append(h)
   else:vals.append(x);who.append(old)
  return V(IM([vals]),D),who

def arithmetic_controls():
 x=[Q(-2,3),Q(0),Q(4,9),Q(7,12),Q(-10,21),Q(2,3)];y=[Q(1,5),Q(-3,7),Q(0),Q(9,2),Q(-1,4),Q(2,3)];a=V.qs(x);b=V.qs(y)
 assert (a+b).asq()==[u+v for u,v in zip(x,y)]
 assert (a-b).asq()==[u-v for u,v in zip(x,y)]
 assert a.scale(Q(-7,11)).asq()==[u*Q(-7,11) for u in x]
 assert a.mul(b).asq()==[u*v for u,v in zip(x,y)]
 assert a.square().asq()==[u*u for u in x]
 assert a.dot(b)==sum((u*v for u,v in zip(x,y)),Q(0))
 p,w=a.maxwith(b,[2]*6,5);assert p.asq()==[max(u,v) for u,v in zip(x,y)] and w[-1]==2
 assert (a-a).D==1 and (a-a).z.is_zero()
 assert V(IM([[6,-9,0]]),-15).asq()==[Q(-2,5),Q(3,5),Q(0)]
 return {'signed_zero_common_content_add_mul_dot_square_max_controls':True,'control_vector_length':6}

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
    p=pos[t-1,j-(axis==1)];u=coords[axis].mul(b[p]);sigma=u.dot(u);alpha=[v.dot(u)/dk for v,dk in zip(b,d)];r=u
    for c,v in zip(alpha,b):
     if c:r=r-v.scale(c)
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
 sums={n:V.const(M,0) for n in stages};peaks={n:V.const(M,0) for n in stages};which={n:[0]*M for n in stages};records=[]
 def collect(n,h,energy):
  val=energy.scale(rec[h][3]);sums[n]=sums[n]+val;peaks[n],which[n]=peaks[n].maxwith(val,which[n],h)
 def finish(n):
  values=[x*y for x,y in zip(normal[n].a,peaks[n].a)];m=max(values);L=Q(m,normal[n].D*peaks[n].D);w=min((which[n][i],i) for i,v in enumerate(values) if v==m)
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
   for l in range(h,k):
    if alpha[l]:v=v-g[l].scale(alpha[l])
   g[k]=v;energy=energy+v.square().scale(1/d[k])
   if k in ends:collect(ends[k],h,energy)
  state['last_source']=h
  if h in ends:finish(ends[h])
  event(event='source',source=h,total=len(b)-1)
 assert len(records)==a.degree-1
 comparison=None
 if a.compare:
  other={r['degree']:r for r in json.loads(pathlib.Path(a.compare).read_text())['runs']}
  for r in records:
   if r['degree'] in other:
    o=other[r['degree']];assert all(r[f]['exact']==o[f]['exact'] for f in FIELDS) and r['pivot_choices']==o['pivot_choices'] and r['pivot_ties']==o['pivot_ties']
  comparison=ident(pathlib.Path(a.compare))
 return {'result':'EXACT_CASE_COMPLETED','set':a.set,'rule':a.rule,'max_degree':a.degree,'code_sha256':sha(__file__),'frozen_source_sha256':PIN,'old_sweep':ident(pathlib.Path(a.old_sweep)),'controls':{**controls,'fresh_scalar_basis_degrees':fresh,'every_new_column_exact_Gram_pairings':True,'every_old_endpoint_and_choice_matched':a.degree<=12,'X_tie_break_and_recording':True},'normal_trace_role':'consistency only; full exact Gram pairings are separately checked','all_original_nodes':M,'all_source_columns':len(b)-1,'complete_degrees':stages,'endpoint_file':ident(out/'endpoints.json'),'baseline':ident(raw),'additional_exact_comparison':comparison,'timing':{'wall_seconds':time.monotonic()-t0,'process_cpu_seconds':time.process_time()-c0,'basis_wall_seconds':tb-t0,'basis_cpu_seconds':cb-c0},'runtime':{'python':platform.python_version(),'python_flint':flint.__version__},'limits':['Exact vector representation optimization only; no nodes/source/gauge change.','No fits, operational verdict or asymptotic claim.','Independent implementation/check remains separate.','Bulk outputs temporary outside Git; no archive delivery claimed.']}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--set',choices=['triangle','rotated'],required=True);ap.add_argument('--rule',choices=['bj','mirror','alt','pivot'],required=True);ap.add_argument('--degree',type=int,required=True);ap.add_argument('--old-sweep',required=True);ap.add_argument('--output-dir',required=True);ap.add_argument('--receipt',required=True);ap.add_argument('--seconds',type=int,default=120);ap.add_argument('--compare');a=ap.parse_args();assert 4<=a.degree<=14 and 0<a.seconds<=180
 out=pathlib.Path(a.output_dir);out.mkdir(parents=True,exist_ok=False);state={'basis_degree':0,'last_source':0,'completed_degrees':[]};start=time.monotonic();cpu=time.process_time()
 def expire(*_):raise TimeoutError('Prospective bounded case cap')
 signal.signal(signal.SIGALRM,expire);signal.alarm(a.seconds)
 try:r=run(a,out,state)
 except TimeoutError:r={'result':'INCOMPLETE_COST_CAP','set':a.set,'rule':a.rule,'max_degree':a.degree,'code_sha256':sha(__file__),'state':state,'wall_seconds':time.monotonic()-start,'process_cpu_seconds':time.process_time()-cpu,'limits':'No missing-source endpoint or completed-case claim.'}
 signal.alarm(0);r['rules_head']='02a465b';r['command']=[sys.executable,'-B',str(pathlib.Path(__file__).resolve()),*sys.argv[1:]];pathlib.Path(a.receipt).write_text(json.dumps(r,indent=2)+'\n');event(event='complete',result=r['result'])
if __name__=='__main__':main()
