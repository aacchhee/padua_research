"""Operational continuation of a source-pinned incomplete N8 V3 tree.

Every mathematical helper and the traversal body equal the frozen producer.
The final certificate contains all prior and new evidence and is checked anew.
"""
import argparse,json,time,sys,gzip,os,tempfile
from collections import Counter
from functools import lru_cache
from math import lcm
from a5_n8_field import *

def encbox(Q):return[[str(F(v,S))for v in Z]for Z in Q]
def write_artifact(out,path):
 data=json.dumps(out,separators=(',',':'),sort_keys=True).encode()
 payload=gzip.compress(data,mtime=0)if path.endswith('.gz')else data
 directory=os.path.dirname(os.path.abspath(path));temporary=None
 try:
  with tempfile.NamedTemporaryFile(mode='wb',dir=directory,prefix=os.path.basename(path)+'.',suffix='.tmp',delete=False)as f:
   temporary=f.name;f.write(payload);f.flush();os.fsync(f.fileno())
  os.replace(temporary,path);temporary=None
 finally:
  if temporary is not None:
   try:os.unlink(temporary)
   except FileNotFoundError:pass
def hull(Q,R):return[(min(Q[i][0],R[i][0]),max(Q[i][1],R[i][1]))for i in range(2)]
def precondition(Hxx,Hxy,Hyy,Q):
 c=[(Z[0]+Z[1])//2 for Z in Q];X=(c[0],c[0]);Y=(c[1],c[1])
 vals=[evaluate(p,X,Y)for p in(Hxx,Hxy,Hyy)];xx,xy,yy=[F(v[0]+v[1],2*S)for v in vals];d=xx*yy-xy*xy
 if not d:return None
 return[[yy/d,-xy/d],[-xy/d,xx/d]]
def inject(Hxx,Hxy,Hyy,C,Q):
 xx,xy,yy=[evaluate(p,*Q)for p in(Hxx,Hxy,Hyy)];H=[[xx,xy],[xy,yy]]
 E=[[add((S if i==j else 0,)*2,neg(asum(mul(rat(C[i][k]),H[k][j])for k in range(2))))for j in range(2)]for i in range(2)]
 norm=max(sum(max(abs(v)for v in E[i][j])for j in range(2))for i in range(2))
 return norm<S,E
def encC(C):return[[str(q)for q in row]for row in C]
def krawczyk(A,B,Hxx,Hxy,Hyy,C,R):
 ok,E=inject(Hxx,Hxy,Hyy,C,R)
 if not ok:return False
 c=[(Z[0]+Z[1])//2 for Z in R];fc=[evaluate(p,(c[0],c[0]),(c[1],c[1]))for p in(A,B)]
 KR=[add(add((c[i],c[i]),neg(asum(mul(rat(C[i][k]),fc[k])for k in range(2)))),asum(mul(E[i][j],(R[j][0]-c[j],R[j][1]-c[j]))for j in range(2)))for i in range(2)]
 return all(R[i][0]<KR[i][0]<=KR[i][1]<R[i][1]for i in range(2))


# This operational extension is pinned to the original V3 source.  Every
# mathematical helper and the classification/subdivision loop is unchanged.
import hashlib,ast
from pathlib import Path
FROZEN_SOURCES={
 'a5_n8_field.py':'764a7d7e50718c04f076ab3bbc86270adad1c47bc902d0b8d4eecf32ebbd2ec2',
 'a5_n8_nodes.py':'c59018d0f17e6d5b9c803e0344cc878e6b067fe8ba457cd4a623bc649b65056b',
 'a5_n8_boxes.py':'e9d763d409dab8568e4b6c3452ac51283e36b708d8aa733e3f4ac3dda923f958',
 'a5_n8_boundary.py':'6088db34cce2952332bd22e560c8b02e90446236f994dc2bac79b33717e769cb',
 'a5_n8_global.py':'f730b4cc3db102e8615326c60c6a26f28ff4d4ab4815e28aca88c55e05c08c7a',
 'a5_n8_schema.md':'1ca5289329359833859960d216b103284457495d6326d35463e18a761d43ed24'}
def frozen_guards():
 folder=Path(__file__).resolve().parent
 for name,digest in FROZEN_SOURCES.items():
  assert hashlib.sha256((folder/name).read_bytes()).hexdigest()==digest,'frozen source changed: '+name
 original=ast.parse((folder/'a5_n8_boxes.py').read_text());continued=ast.parse(Path(__file__).read_text())
 def functions(tree):return{n.name:n for n in ast.walk(tree)if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef))}
 first,second=functions(original),functions(continued)
 for name,node in first.items():
  if name!='solve':assert ast.dump(node,include_attributes=False)==ast.dump(second[name],include_attributes=False),'changed mathematical helper: '+name
 before=[n for n in first['solve'].body if isinstance(n,ast.While)]
 after=[n for n in second['solve'].body if isinstance(n,ast.While)]
 assert len(before)==len(after)==1
 assert ast.dump(before[0],include_attributes=False)==ast.dump(after[0],include_attributes=False),'changed classification/subdivision loop'
 return dict(FROZEN_SOURCES)
def require(condition,message):
 if not condition:raise ValueError(message)
def exact_int(value,label):
 require(type(value)is int and value>=0,label+' must be a nonnegative integer');return value
def dyadic(value):
 require(type(value)is str,'root coordinate must be an exact rational string')
 scaled=F(value)*S;require(scaled.denominator==1,'root coordinate is not on the precision160 dyadic grid');return scaled.numerator
def pathbox(path):
 Q=[(-S,S),(-S,S)]
 for bit in path:
  axis=0 if Q[0][1]-Q[0][0]>=Q[1][1]-Q[1][0]else 1
  lo,hi=Q[axis];mid=(lo+hi)//2;Q[axis]=(lo,mid)if bit=='0'else(mid,hi)
 return Q
def prefix_partition(paths):
 trie={}
 for path in paths:
  require(type(path)is str and set(path)<=set('01'),'path must be a binary string')
  require(len(path)<=44,'path exceeds frozen depth44')
  node=trie
  for bit in path:
   require('_end'not in node,'a path extends a terminal prefix');node=node.setdefault(bit,{})
  require(not node,'duplicate path or terminal path contains another path');node['_end']=True
 def complete(node):
  if '_end'in node:return set(node)=={'_end'}
  return set(node)=={'0','1'} and complete(node['0'])and complete(node['1'])
 require(complete(trie),'paths do not form a complete finite prefix partition')
def restore_roots(records):
 require(type(records)is list,'root records must be a list');out=[]
 for i,record in enumerate(records):
  require(type(record)is dict and set(record)=={'id','mask','R','C'},'malformed exact root record')
  require(type(record['id'])is int and record['id']==i,'root ids must be consecutive exact integers')
  mask=exact_int(record['mask'],'mask');require(mask<1<<45,'mask exceeds45bits')
  require(type(record['R'])is list and len(record['R'])==2,'root box dimension')
  R=[]
  for interval in record['R']:
   require(type(interval)is list and len(interval)==2,'root interval dimension');lo,hi=map(dyadic,interval)
   require(-S<lo<hi<S,'root box must lie strictly inside the square');R.append((lo,hi))
  require(type(record['C'])is list and len(record['C'])==2,'preconditioner dimension')
  C=[]
  for row in record['C']:
   require(type(row)is list and len(row)==2 and all(type(v)is str for v in row),'preconditioner needs exact rational strings');C.append([F(v)for v in row])
  require(C[0][0]*C[1][1]-C[0][1]*C[1][0]!=0,'singular preconditioner')
  restored=dict(record);restored['_R']=R;restored['_C']=C;out.append(restored)
 return out
def validate_partial(data):
 require(type(data)is dict and data.get('format')=='a5-n8-spatial-v1','wrong certificate format')
 require(type(data.get('n'))is int and data['n']==8 and type(data.get('precision'))is int and data['precision']==PREC,'wrong degree or precision')
 require(data.get('pattern_order')=='compatible-mask','wrong pattern order')
 require(data.get('field_embedding')==embedding_record(),'wrong exact field embedding')
 require(data.get('metadata',{}).get('source_sha256')==FROZEN_SOURCES['a5_n8_boxes.py'],'partial input is not the frozen V3 producer')
 require(not any(k in data for k in('edges','corners','boundary_summary')),'boundary-bearing input is outside this continuation protocol')
 require(data.get('unresolved')==[],'unresolved leaves are outside this continuation protocol')
 summary=data['summary'];require(summary.get('complete')is False and summary.get('interior_complete')is False,'input must be an incomplete interior cap result')
 for key in('unresolved','pending','interior','node_leaves','all_gradient_leaves','leaf_pattern_records','depth','maximum_ambiguity'):exact_int(summary[key],key)
 require(type(summary.get('leaf_counts'))is dict and all(type(k)is str and type(v)is int and v>=0 for k,v in summary['leaf_counts'].items()),'malformed leaf-count table')
 require(summary.get('unresolved')==0,'summary reports unresolved leaves')
 leaves=data['leaves'];pending=data['pending_paths'];require(type(leaves)is list and type(pending)is list and pending,'retained pending paths required')
 counts=Counter()
 for leaf in leaves:
  require(type(leaf)is dict and set(leaf)in({'path','patterns'},{'path','node_cone'},{'path','all_gradient'}),'malformed disposed leaf')
  if 'node_cone'in leaf:
   index=exact_int(leaf['node_cone'],'node index');require(index<45,'node index range');counts['node_cone']+=1
  elif 'all_gradient'in leaf:
   require(type(leaf['all_gradient'])is int and leaf['all_gradient']in(0,1),'invalid universal-gradient axis');counts['all_gradient']+=1
  else:
   require(type(leaf['patterns'])is list and leaf['patterns'],'ordinary patterns must be a nonempty list')
   for record in leaf['patterns']:
    require(type(record)is dict and record.get('code')in('flat','gradient','hessian','regular_point','factor','root'),'malformed ordinary disposition');counts[record['code']]+=1
    if record['code']=='root':
     reference=exact_int(record.get('id'),'root reference');require(reference<len(data['interior_roots']),'root reference is absent')
 prefix_partition([r['path']for r in leaves]+pending)
 stats=summary['stats'];require(type(stats)is dict,'stats must be a dictionary')
 for key,value in stats.items():require(type(key)is str and type(value)is int and value>=0,'malformed profiling statistic')
 require(stats.get('depth_limit',0)==0,'depth-limit record cannot be resumed by this protocol')
 require(stats.get('visited')==2*len(leaves)+len(pending)-1 and stats.get('discard')==len(leaves),'inconsistent partial tree accounting')
 require(summary.get('pending')==len(pending),'pending count mismatch')
 require(dict(counts)==summary.get('leaf_counts'),'disposed-leaf counts mismatch')
 require(summary.get('leaf_pattern_records')==sum(v for k,v in counts.items()if k not in('node_cone','all_gradient')),'ordinary pattern count mismatch')
 require(summary.get('node_leaves')==counts['node_cone'] and summary.get('all_gradient_leaves')==counts['all_gradient'],'direct leaf count mismatch')
 require(stats.get('node_cone',0)==counts['node_cone'] and stats.get('all_gradient',0)==counts['all_gradient'],'direct profiling count mismatch')
 depth=exact_int(summary['depth'],'depth');require(depth<=44 and all(len(p)<=depth+1 for p in pending),'invalid prior depth')
 ambiguity=exact_int(summary['maximum_ambiguity'],'maximum ambiguity');require(ambiguity<=45,'invalid prior ambiguity')
 require(type(data['node_cones'])is list and len(data['node_cones'])==45,'all45node records required')
 require(all(type(row)is dict and type(row.get('index'))is int and row['index']==i and row.get('status')=='accepted'for i,row in enumerate(data['node_cones'])),'node records must be index-ordered and accepted')
 restored=restore_roots(data['interior_roots']);require(summary.get('interior')==len(restored),'root count mismatch')
 return restored,counts

def load_partial(path):
 raw=Path(path).read_bytes();payload=gzip.decompress(raw)if raw.startswith(b'\x1f\x8b')else raw
 def unique(pairs):
  result={}
  for key,value in pairs:
   require(key not in result,'duplicate JSON key');result[key]=value
  return result
 data=json.loads(payload,object_pairs_hook=unique);restored,counts=validate_partial(data)
 return data,restored,counts,hashlib.sha256(raw).hexdigest(),len(raw)

def solve(args):
 t0=time.time();frozen_guards();prior,restored,prior_counts,input_sha,input_bytes=load_partial(args.resume);nodes,L=construct();LT=list(map(terms,L));LX=[terms(q.diff(x))for q in L];LY=[terms(q.diff(y))for q in L]
 mons=[(i,d-i)for d in range(9)for i in range(d,-1,-1)]
 fieldcoeffs=[[kparts(q.rep.to_dict().get((i,j),K.zero))for i,j in mons]for q in L]
 den=lcm(*(v.denominator for rows in fieldcoeffs for row in rows for v in row))
 LC=[[[int(v*den)for v in row]for row in rows]for rows in fieldcoeffs]
 def dterms(pc,dx,dy):
  out=[]
  for j,(a,b)in enumerate(mons):
   if a<dx or b<dy or not any(pc[j]):continue
   fac=1
   for z in range(dx):fac*=a-z
   for z in range(dy):fac*=b-z
   out.append((a-dx,b-dy,cparts(tuple(F(v*fac,den)for v in pc[j]))))
  return out
 def psym(pc):
  return s.Poly.from_dict({(a,b):decode([F(v,den)for v in pc[j]])for j,(a,b)in enumerate(mons)if any(pc[j])},(x,y),domain=K)
 @lru_cache(maxsize=args.cache_masks)
 def pdata(mask):
  selected=[i for i in range(45)if mask>>i&1]
  pc=tuple(tuple(2*sum(LC[i][j][k]for i in selected)-(den if j==0 and k==0 else 0)for k in range(12))for j in range(45))
  return pc,dterms(pc,1,0),dterms(pc,0,1),dterms(pc,2,0),dterms(pc,1,1),dterms(pc,0,2)
 @lru_cache(maxsize=args.cache_masks)
 def fixed_gradient(fixed,ambiguous):
  positive=[i for i in range(45)if fixed>>i&1];amb=[i for i in range(45)if ambiguous>>i&1]
  # Partition of unity: forced background =2sum_positive Li+sum_amb Li−1.
  pc=tuple(tuple(2*sum(LC[i][j][k]for i in positive)+sum(LC[i][j][k]for i in amb)-(den if j==0 and k==0 else 0)for k in range(12))for j in range(45))
  return dterms(pc,1,0),dterms(pc,0,1),dterms(pc,2,0),dterms(pc,1,1),dterms(pc,0,2)
 roots=restored;special_cache={};factor_cache={}
 special=[]
 Xlist=list(dict.fromkeys(z[0]for z in nodes));Ylist=list(dict.fromkeys(z[1]for z in nodes))
 if K.zero not in Ylist:Ylist.append(K.zero)
 deriv=[(q.rep.to_dict(),q.diff(x).rep.to_dict(),q.diff(y).rep.to_dict())for q in L]
 for u in Xlist:
  for v in Ylist:
   up=[u**i for i in range(9)];vp=[v**i for i in range(9)]
   values=[tuple(sum((c*up[i]*vp[j]for(i,j),c in row.items()),K.zero)for row in triple)for triple in deriv]
   vals=[z[0]for z in values];gx=[z[1]for z in values];gy=[z[2]for z in values]
   regular=any(vals[i]==K.zero and(gx[i]!=K.zero or gy[i]!=K.zero)for i in range(45));node=vals.count(K.one)==1 and vals.count(K.zero)==44
   if regular or node:
    gfields=[[kparts(v)for v in g]for g in(gx,gy)]
    gd=lcm(*(v.denominator for g in gfields for z in g for v in z))
    ints=[[[int(v*gd)for v in z]for z in g]for g in gfields]
    special.append(((u,v),(kfield(u),kfield(v)),*ints))
 def atspecial(mask,j):
  key=(mask,j)
  if key not in special_cache:
   _,_,gx,gy=special[j];special_cache[key]=all(sum((1 if mask>>i&1 else -1)*g[i][k]for i in range(45))==0 for g in(gx,gy)for k in range(12))
  return special_cache[key]
 def exceptional(mask,Q,data):
  P,A,B,Hxx,Hxy,Hyy=data
  for j,(point,R,gx,gy)in enumerate(special):
   if any(R[i][1]<Q[i][0]-S//100 or R[i][0]>Q[i][1]+S//100 for i in range(2)):continue
   if not atspecial(mask,j):continue
   U=hull(Q,R);C=precondition(Hxx,Hxy,Hyy,U)
   if C and inject(Hxx,Hxy,Hyy,C,U)[0]:return {'code':'regular_point','point':[encfield(v)for v in point],'C':encC(C),'U':encbox(U)}
  return None
 def smoothroot(mask,Q,data):
  P,A,B,Hxx,Hxy,Hyy=data
  for rr in roots:
   if rr['mask']!=mask:continue
   R=rr['_R'];U=hull(Q,R);C=rr['_C']
   if inject(Hxx,Hxy,Hyy,C,U)[0]:return {'code':'root','id':rr['id'],'U':encbox(U)}
  c=[(Z[0]+Z[1])//2 for Z in Q]
  for it in range(5):
   point=[(v,v)for v in c];C=precondition(Hxx,Hxy,Hyy,point)
   if not C:return None
   fc=[evaluate(p,*point)for p in(A,B)];step=[neg(asum(mul(rat(C[i][k]),fc[k])for k in range(2)))for i in range(2)]
   c=[c[i]+(step[i][0]+step[i][1])//2 for i in range(2)]
  r=S>>30;R=[(v-r,v+r)for v in c]
  if any(Z[0]<=-S or Z[1]>=S for Z in R):return None
  C=precondition(Hxx,Hxy,Hyy,R)
  if not C or not krawczyk(A,B,Hxx,Hxy,Hyy,C,R):return None
  xx,xy,yy=[evaluate(p,*R)for p in(Hxx,Hxy,Hyy)]
  if xx[1]>=0 or add(mul(xx,yy),neg(power(xy,2)))[0]<=0:return None
  if any(scale(evaluate(LT[i],*R),1 if mask>>i&1 else -1)[0]<=0 for i in range(45)):return None
  U=hull(Q,R)
  if not inject(Hxx,Hxy,Hyy,C,U)[0]:return None
  if any(all(R[i][0]<=v['_R'][i][1]and v['_R'][i][0]<=R[i][1]for i in range(2))for v in roots):return None
  rr={'id':len(roots),'mask':mask,'R':encbox(R),'C':encC(C),'_R':R,'_C':C};roots.append(rr)
  return {'code':'root','id':rr['id'],'U':encbox(U)}
 def factor(mask,Q,data):
  if mask not in factor_cache:
   P=psym(data[0]);A=P.diff(x);B=P.diff(y);G=s.gcd(A,B)
   if G.total_degree()==0:factor_cache[mask]=None
   else:
    g=G.sqf_part();factor_cache[mask]=(terms(A.exquo(G)),terms(B.exquo(G)),terms(g.diff(x)),terms(g.diff(y)),str(G.as_expr()))
  v=factor_cache[mask]
  if v and(sign(evaluate(v[0],*Q))or sign(evaluate(v[1],*Q)))and(sign(evaluate(v[2],*Q))or sign(evaluate(v[3],*Q))):return {'code':'factor'}
  return None
 from a5_n8_nodes import build_node_certificates,cubes
 node_cones=prior['node_cones']
 accepted_cones=[(r['index'],tuple(tuple(int(F(z)*S)for z in a)for a in r['B']))for r in node_cones if r['status']=='accepted']
 print(json.dumps({'node_cones':len(accepted_cones),'node_gap_positive':sum(F(r['gap_lower'])>0 for r in node_cones),'seconds':time.time()-t0}),flush=True)
 stats=Counter(prior['summary']['stats']);leafstats=Counter(prior_counts);pending=[(*pathbox(path),len(path),path)for path in prior['pending_paths']];unresolved=[];leaves=list(prior['leaves']);deepest=prior['summary']['depth'];maxamb=prior['summary']['maximum_ambiguity']
 print(json.dumps({'construction_seconds':time.time()-t0,'precision':PREC}),flush=True)
 while pending and stats['visited']<args.boxes and time.time()-t0<args.seconds:
  X,Y,d,path=pending.pop();stats['visited']+=1;deepest=max(deepest,d)
  containing=next((index for index,B in accepted_cones if all(B[a][0]<(X,Y)[a][0] and (X,Y)[a][1]<B[a][1]for a in range(2))),None)
  if containing is not None:
   stats['discard']+=1;stats['node_cone']+=1;leafstats['node_cone']+=1
   if args.certificate:leaves.append({'path':path,'node_cone':containing})
   continue
  lv=[centered(p,LX[i],LY[i],X,Y)for i,p in enumerate(LT)];sg=[sign(v)for v in lv];amb=[i for i,z in enumerate(sg)if not z];maxamb=max(maxamb,len(amb))
  fixed=sum(1<<i for i,z in enumerate(sg)if z>0)
  background=fixed_gradient(fixed,sum(1<<i for i in amb));all_axis=None
  for axis,derivatives in enumerate((LX,LY)):
   G=evaluate(background[axis],X,Y)
   radius=sum(max(abs(z)for z in evaluate(derivatives[i],X,Y))for i in amb)
   if not sign((G[0]-radius,G[1]+radius)):
    G=centered(background[0],background[2],background[3],X,Y)if axis==0 else centered(background[1],background[3],background[4],X,Y)
   if sign((G[0]-radius,G[1]+radius)):
    all_axis=axis;break
  if all_axis is not None:
   stats['discard']+=1;stats['all_gradient']+=1;leafstats['all_gradient']+=1
   if args.certificate:leaves.append({'path':path,'all_gradient':all_axis})
   continue
  codes=[];ok=False
  if len(amb)<=args.ambiguity or d>=args.full_depth:
   ok=True
   for bits in range(1<<len(amb)):
    mask=fixed+sum(1<<i for j,i in enumerate(amb)if bits>>j&1)
    data=pdata(mask);P,A,B,Hxx,Hxy,Hyy=data
    if not A or not B:code='flat'
    elif sign(evaluate(A,X,Y))or sign(evaluate(B,X,Y)):code='gradient'
    else:
     xx=evaluate(Hxx,X,Y);yy=evaluate(Hyy,X,Y);xy=evaluate(Hxy,X,Y)
     det=add(mul(xx,yy),neg(mul(xy,xy)))
     if xx[0]>0 or yy[0]>0 or det[1]<0:code='hessian'
     else:
      rec=None
      if d>=args.root_depth:rec=smoothroot(mask,(X,Y),data) or exceptional(mask,(X,Y),data) or factor(mask,(X,Y),data)
      if rec is None:ok=False;stats['failedmask']+=1;break
      code=rec
    if isinstance(code,str):code={'code':code}
    codes.append(code);stats[code['code']]+=1;stats['mask_checks']+=1
  if ok:
   stats['discard']+=1
   leafstats.update(row['code']for row in codes)
   if args.certificate:leaves.append({'path':path,'patterns':codes})
   continue
  if d>=args.depth:
   unresolved.append({'path':path,'X':[str(F(v,S))for v in X],'Y':[str(F(v,S))for v in Y],'ambiguity':len(amb),'mask':mask if len(amb)<=args.ambiguity else None});stats['depth_limit']+=1;continue
  axis=0 if X[1]-X[0]>=Y[1]-Y[0]else 1
  Z=(X,Y)[axis];m=(Z[0]+Z[1])//2
  if m in Z:raise AssertionError('precision exhausted')
  q1=[X,Y];q2=[X,Y];q1[axis]=(Z[0],m);q2[axis]=(m,Z[1]);pending.extend([(*q2,d+1,path+'1'),(*q1,d+1,path+'0')])
  if stats['visited']%1000==0:print(json.dumps({'seconds':time.time()-t0,'stats':dict(stats),'pending':len(pending),'depth':deepest,'unresolved':len(unresolved),'Pcache':pdata.cache_info().currsize}),flush=True)
 summary={'seconds':time.time()-t0,'stats':dict(stats),'pending':len(pending),'depth':deepest,'unresolved':len(unresolved),'Pcache':pdata.cache_info().currsize,'interior':len(roots),'leaf_counts':dict(leafstats),'leaf_pattern_records':sum(v for k,v in leafstats.items()if k not in('node_cone','all_gradient')),'node_leaves':leafstats['node_cone'],'all_gradient_leaves':leafstats['all_gradient'],'maximum_ambiguity':maxamb,'interior_complete':not pending and not unresolved,'complete':False}
 for rr in roots:rr.pop('_R');rr.pop('_C')
 out={'field_embedding':embedding_record(),'pattern_order':'compatible-mask','interior_roots':roots,'format':'a5-n8-spatial-v1','n':8,'precision':PREC,'node_cones':node_cones,'summary':summary,'unresolved':unresolved,'pending_paths':[v[-1]for v in pending],'leaves':leaves}
 out['metadata']={'python':sys.version,'sympy':s.__version__,'backend':str(s.external.gmpy.GROUND_TYPES),'source_sha256':__import__('hashlib').sha256(open(__file__,'rb').read()).hexdigest(),'seed':None,'mathematical_run_deterministic':True}
 out['metadata']['continuation']={'input_sha256':input_sha,'input_bytes':input_bytes,'prior_source_sha256':prior['metadata']['source_sha256'],'prior_summary_seconds':prior['summary']['seconds'],'frozen_sources':dict(FROZEN_SOURCES),'scope':'self-contained full old/new tree; old input is provenance only'}
 if args.boundary and summary['interior_complete']:
  # Persist the complete interior proof with closed-square complete still false.
  # A boundary interruption must not erase the expensive tree and node evidence.
  write_artifact(out,args.output)
  print(json.dumps({'interior_checkpoint':args.output,'interior_complete':True,'complete':False}),flush=True)
  from a5_n8_boundary import boundaries
  e,c,bs,bu=boundaries(nodes,L);out['edges']=e;out['corners']=c;out['boundary_summary']=bs;out['unresolved'].extend(bu);out['summary'].update(edge=bs['edge'],corner=bs['corner'],total=len(roots)+bs['edge']+bs['corner'],complete=not bu)
 write_artifact(out,args.output)
 print(json.dumps(summary),flush=True)

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--resume',required=True);ap.add_argument('--boxes',type=int,default=200000);ap.add_argument('--seconds',type=int,default=3600);ap.add_argument('--depth',type=int,default=44);ap.add_argument('--ambiguity',type=int,default=8);ap.add_argument('--output',required=True);ap.add_argument('--certificate',action='store_true');ap.add_argument('--boundary',action='store_true');ap.add_argument('--full-depth',type=int,default=44);ap.add_argument('--root-depth',type=int,default=12);ap.add_argument('--cache-masks',type=int,default=8000);ap.add_argument('--validate-only',action='store_true');args=ap.parse_args()
 frozen_guards();require(args.certificate,'self-contained certificate output is required');require(args.depth==44 and args.full_depth==44 and args.ambiguity==8 and args.root_depth==12,'continuation must preserve frozen search parameters');require(args.seconds>0 and args.boxes>0 and args.cache_masks>0,'positive run bounds required')
 if args.validate_only:
  prior,restored,counts,digest,size=load_partial(args.resume);print(json.dumps({'structurally_valid':True,'search_advanced':False,'input_sha256':digest,'input_bytes':size,'pending':len(prior['pending_paths']),'disposed_leaves':len(prior['leaves']),'restored_roots':len(restored),'mathematical_certificate_accepted':False}),flush=True)
 else:solve(args)
