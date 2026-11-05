#!/usr/bin/env python3
"""Exact all-source PD-T137 prefix scan; no fits, gate verdict or asymptotics.
Frozen source/build controls and degree2--12 overlap precede higher interpretation.
"""
import argparse,gzip,hashlib,json,pathlib,platform,signal,sys,time
import flint
from flint import fmpq as Q,fmpq_mat as Mat
ROOT=pathlib.Path(__file__).resolve().parents[3]
PIN='19ce7b774e5a6fa56108eebca3b2ef81f5237328e518d95225adf9f8835e060f'
OLD_PIN='0d9c236fe879879b7f546596c554d213b7b8c408d31dec08dd79146c7d629344'
FIELDS=['Knode_squared','KHS_squared','Urow_squared','upper_squared']
def sha(p):return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def event(**v):print(json.dumps(v),flush=True)
def ident(p):return {'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)}
def N(n):return (n+1)*(n+2)//2
def build(ex,xy,n,rule):
 coords=[[p[a] for p in xy] for a in (0,1)];b=[Mat([[1]*len(xy)])];d=[Q(len(xy))];rec=[None];meta=[(0,0)];pos={(0,0):0};ties=[]
 for t in range(1,n+1):
  for j in range(t+1):
   axes=[a for a in (0,1) if (a==0 and j<t) or (a==1 and j>0)]
   if rule!='pivot':
    wanted=0 if ((rule=='bj' and j==0) or (rule=='mirror' and j!=t) or (rule=='alt' and 2*j<t)) else 1
    axes=[wanted if wanted in axes else axes[0]]
   candidates=[]
   for axis in axes:
    p=pos[t-1,j-(axis==1)];u=ex.multiply(b[p],coords[axis]);sigma=ex.dot(u,u)
    alpha=[ex.dot(v,u)/dv for v,dv in zip(b,d)];r=u
    for c,v in zip(alpha,b):
     if c:r=r-c*v
    dk=ex.dot(r,r);assert dk>0 and sigma>0
    candidates.append((dk/sigma,axis,p,alpha,sigma,r,dk))
   if len(candidates)==2 and candidates[0][0]==candidates[1][0]:ties.append([t,j])
   _,axis,p,alpha,sigma,r,dk=max(candidates,key=lambda c:(c[0],-c[1]))
   pos[t,j]=len(b);b.append(r);d.append(dk);rec.append((axis,p,alpha,sigma));meta.append((t,j))
  event(event='basis_degree',degree=t,rule=rule)
 return coords,b,d,rec,meta,ties

def run(a,out,state):
 src=ROOT/'tracks/bivariate-lanczos/code/drift/e1_exact.py';assert sha(src)==PIN
 assert sha(a.old_sweep)==OLD_PIN
 sys.path.insert(0,str(src.parent));import e1_exact as ex
 old=json.loads(pathlib.Path(a.old_sweep).read_text())['runs']
 old={(x['set'],x['rule'],x['degree']):x for x in old}
 if a.max_degree>12:
  assert a.overlap_receipt,'Higher degree requires a completed degree12 overlap receipt'
  ov=json.loads(pathlib.Path(a.overlap_receipt).read_text())
  assert ov['result']=='EXACT_OVERLAP_PASS' and ov['set']==a.set and ov['rule']==a.rule and ov['max_degree']==12 and ov['frozen_source_sha256']==PIN
 xy=ex.points(a.set);M=len(xy);assert M in (325,625) and M>N(a.max_degree)
 coords,b,d,rec,meta,ties=build(ex,xy,a.max_degree,a.rule);state['basis_degree_completed']=a.max_degree
 assert len(b)==N(a.max_degree)
 controls=[]
 # Independently constructed degree-by-degree bases/bounds, never slices of b.
 for n in [2,3,4]:
  if n>a.max_degree:continue
  cb=ex.build(xy,n,a.rule)
  assert cb[0]==coords and cb[1]==b[:N(n)] and cb[2]==d[:N(n)] and cb[3]==rec[:N(n)] and cb[4]==meta[:N(n)]
  r=ex.bounds(xy,n,a.rule,'all');o=old[a.set,a.rule,n]
  assert all(r[f]['exact']==o[f]['exact'] for f in FIELDS) and r['pivot_choices']==o['pivot_choices']
  controls.append(n)
 event(event='independent_degree_controls_pass',degrees=controls)
 raw=out/'basis-recurrence.jsonl.gz'
 with gzip.open(raw,'wt') as f:
  f.write(json.dumps({'set':a.set,'rule':a.rule,'max_degree':a.max_degree,'M':M,'N':len(b),'coordinates':[[str(x) for x in c] for c in coords],'pivot_ties':ties})+'\n')
  for k in range(len(b)):
   rr=None if k==0 else [rec[k][0],rec[k][1],[str(x) for x in rec[k][2]],str(rec[k][3])]
   f.write(json.dumps({'k':k,'meta':meta[k],'b':[str(b[k][0,i]) for i in range(M)],'d':str(d[k]),'rec':rr})+'\n')
 stages=list(range(2,a.max_degree+1));normal={};pdiag=[Q(0)]*M
 for k in range(len(b)):
  for i in range(M):pdiag[i]+=b[k][0,i]**2/d[k]
  n=meta[k][0]
  if n in stages and k==N(n)-1:
   normal[n]=[1-z for z in pdiag];assert min(normal[n])>=0 and sum(normal[n])==M-N(n)
 rows={n:[Q(0)]*M for n in stages};peaks={n:[Q(0)]*M for n in stages};which={n:[0]*M for n in stages};records=[]
 ends={N(n)-1:n for n in stages}
 def collect(n,h,energy):
  sigma=rec[h][3]
  for i,en in enumerate(energy):
   v=sigma*en;rows[n][i]+=v
   if v>peaks[n][i]:peaks[n][i]=v;which[n][i]=h
 def finish(n):
  vals=[normal[n][i]*peaks[n][i] for i in range(M)];L=max(vals);idx=min((which[n][i],i) for i,v in enumerate(vals) if v==L)
  H=sum((x*y for x,y in zip(normal[n],rows[n])),Q(0));R=max(rows[n]);U=min(H,R)
  r={'set':a.set,'rule':a.rule,'degree':n,'sources':'all','source_count':N(n)-1,'point_count':M,'basis_count':N(n),'Knode_squared':{'exact':str(L),'float':float(L)},'KHS_squared':{'exact':str(H),'float':float(H)},'Urow_squared':{'exact':str(R),'float':float(R)},'upper_squared':{'exact':str(U),'float':float(U)},'pivot_choices':['XY'[r[0]] for r in rec[1:N(n)]],'pivot_ties':[t for t in ties if t[0]<=n],'normal_trace_exact':str(sum(normal[n])),'witness':{'source':idx[0],'node':idx[1],'source_degree_index':meta[idx[0]],'point':[str(coords[axis][idx[1]]) for axis in (0,1)]}}
  assert 0<L<=U and H>=U and R>=U
  if n<=12:
   o=old[a.set,a.rule,n]
   assert all(r[f]['exact']==o[f]['exact'] for f in FIELDS) and r['pivot_choices']==o['pivot_choices'] and r['source_count']==o['source_count']
  if a.rule=='pivot':
   assert ([2,1] in r['pivot_ties'])==(a.set=='rotated')
   if a.set=='triangle' and n<=12:assert not r['pivot_ties']
  records.append(r);(out/'endpoints.json').write_text(json.dumps({'runs':records},indent=2)+'\n')
  state['completed_degrees']=[r['degree'] for r in records];event(event='stage_complete',degree=n,overlap_pass=n<=12)
 for h in range(1,len(b)):
  g=[None]*len(b);g[h]=Mat([[1]*M]);energy=[Q(1)/d[h]]*M
  if h in ends:collect(ends[h],h,energy)
  for k in range(h+1,len(b)):
   axis,p,alpha,_=rec[k];v=ex.multiply(g[p],coords[axis]) if p>=h else Mat(1,M)
   for l in range(h,k):
    if alpha[l]:v=v-alpha[l]*g[l]
   g[k]=v
   for i in range(M):energy[i]+=v[0,i]**2/d[k]
   if k in ends:collect(ends[k],h,energy)
  state['last_source_completed']=h
  if h in ends:finish(ends[h])
  event(event='source',source=h,total=len(b)-1)
 assert len(records)==a.max_degree-1 and state['completed_degrees']==stages
 receipt={'result':'EXACT_OVERLAP_PASS' if a.max_degree==12 else 'EXACT_PREFIX_SCAN_COMPLETED','rules_head':'0e493be7f9883e00e6260cf6b081c607a230177f','set':a.set,'rule':a.rule,'max_degree':a.max_degree,'frozen_source_sha256':PIN,'old_sweep':ident(pathlib.Path(a.old_sweep)),'independent_degree_controls':controls,'all_2_through_12_overlap_pass':a.max_degree>=12,'pivot_ties':ties,'source_class':'all','completed_degrees':stages,'endpoint_file':ident(out/'endpoints.json'),'basis_recurrence':ident(raw),'code_sha256':sha(__file__),'command':[sys.executable,'-B',str(pathlib.Path(__file__).resolve()),*sys.argv[1:]],'runtime':{'python':platform.python_version(),'python_flint':flint.__version__,'elapsed_seconds':time.monotonic()-state['start']},'endpoint_displays':[{'degree':r['degree'],**{f:r[f]['float'] for f in FIELDS}} for r in records],'limits':['Exact finite PD-T137 endpoints only; no fits or scientific gate verdict.','Independent checker/port remains separate.','Temporary external artifacts: archival/delivery pending.']}
 return receipt

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--set',choices=['triangle','rotated'],required=True);ap.add_argument('--rule',choices=['bj','mirror','alt','pivot'],required=True);ap.add_argument('--max-degree',type=int,required=True);ap.add_argument('--old-sweep',required=True);ap.add_argument('--overlap-receipt');ap.add_argument('--output-dir',required=True);ap.add_argument('--receipt',required=True);ap.add_argument('--case-seconds',type=int,default=1800);a=ap.parse_args();assert 4<=a.max_degree<=20 and 0<a.case_seconds<=1800
 out=pathlib.Path(a.output_dir);out.mkdir(parents=True,exist_ok=False);state={'start':time.monotonic(),'completed_degrees':[],'last_source_completed':0}
 def expired(*_):raise TimeoutError('Per-case deadline; switch to native producer/port before continuing this case')
 signal.signal(signal.SIGALRM,expired);signal.alarm(a.case_seconds)
 try:r=run(a,out,state)
 except TimeoutError as e:
  r={'result':'COST_LIMIT_PENDING_NATIVE','set':a.set,'rule':a.rule,'max_degree':a.max_degree,'state':{k:v for k,v in state.items() if k!='start'},'elapsed_seconds':time.monotonic()-state['start'],'reason':str(e),'code_sha256':sha(__file__),'command':[sys.executable,'-B',str(pathlib.Path(__file__).resolve()),*sys.argv[1:]]}
 signal.alarm(0);pathlib.Path(a.receipt).write_text(json.dumps(r,indent=2)+'\n');event(event='complete',result=r['result'])
if __name__=='__main__':main()
