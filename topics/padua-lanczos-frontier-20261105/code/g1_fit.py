"""Frozen G1 fit producer. Real inputs require all152 accepted exact rows.
No actual G1 execution is implied by implementation or synthetic self-tests.
"""
import argparse, copy, hashlib, json, math, pathlib, platform, sys, time
from fractions import Fraction as F
sys.set_int_max_str_digits(0)
DEGREES=tuple(range(2,21)); RULES=('bj','mirror','alt','pivot'); GRIDS=('triangle','rotated')
METRIC='PD-T137 aggregate all-source spectral normal output'
SOURCE='19ce7b774e5a6fa56108eebca3b2ef81f5237328e518d95225adf9f8835e060f'
FIELDS=('Knode_squared','KHS_squared','Urow_squared','upper_squared')
class GuardError(ValueError):pass
def require(ok,msg):
 if not ok:raise GuardError(msg)
def sha(p):return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def ident(p):
 p=pathlib.Path(p);return {'path':str(p.resolve()),'sha256':sha(p),'bytes':p.stat().st_size}
def pinned(a):
 p=pathlib.Path(a['path']);require(p.stat().st_size==a['bytes'] and sha(p)==a['sha256'],'artifact hash/size mismatch');return p
def rows(p):
 s=p.read_text()
 try:r=json.loads(s);return r['runs']
 except json.JSONDecodeError:return [json.loads(x) for x in s.splitlines() if x.strip()]
def strings(x):
 if isinstance(x,dict):return [z for v in x.values() for z in strings(v)]
 if isinstance(x,list):return [z for v in x for z in strings(v)]
 return [x]
def validrow(r,g,rule):
 n=r['degree'];k=(n+1)*(n+2)//2;m={'triangle':325,'rotated':625}[g]
 require(r['set']==g and r['rule']==rule and n in DEGREES,'row identity')
 require(r['sources']=='all' and r['source_count']==k-1 and r['basis_count']==k and r['point_count']==m,'source/node coverage')
 require(F(r['normal_trace_exact'])==m-k,'trace')
 c=r['pivot_choices'];require(len(c)==k-1 and set(c)<=set('XY'),'choices coverage')
 for t in range(1,n+1):
  for j in range(t+1):
   axis=c[t*(t+1)//2+j-1]
   want='X' if ((rule=='bj' and j==0) or (rule=='mirror' and j!=t) or (rule=='alt' and 2*j<t)) else 'Y'
   require((rule=='pivot' and (0<j<t or axis==('X' if j==0 else 'Y'))) or (rule!='pivot' and axis==want),'illegal creator choice')
 ties=r['pivot_ties'];require(len(ties)==len({tuple(z) for z in ties}),'duplicate ties')
 require(rule=='pivot' or ties==[],'nonpivot ties')
 if n<=12:require(ties==([[2,1]] if g=='rotated' and rule=='pivot' else []),'frozen overlap ties')
 for t,j in ties:require(1<=t<=n and 0<j<t and c[t*(t+1)//2+j-1]=='X','X tie convention')
 if 'exact_gram_pairs_checked' in r:require(r['exact_gram_pairs_checked']>=k*(k-1)//2,'Gram coverage')
 L,H,R,U=[F(r[f]['exact']) for f in FIELDS]
 require(0<L<=U and U==min(H,R),'endpoint positivity/minimum')
 return (L,H,R,U)
def load_manifest(path):
 manifest=json.loads(pathlib.Path(path).read_text())
 require(manifest.get('schema')=='g1-fit-input-v1' and manifest.get('source_metric')==METRIC and manifest.get('tie_convention')=='X wins exact ties' and manifest.get('frozen_source_sha256')==SOURCE,'manifest scientific identity')
 cases=manifest['cases'];require(len(cases)==8,'eight complete cases required');data={};pins=[]
 for c in cases:
  g,rule=c['grid'],c['rule'];require((g,rule) in [(g,r) for g in GRIDS for r in RULES] and (g,rule) not in data,'duplicate/invalid case')
  pp,ip,rp=[pinned(c[k]) for k in ['endpoints','independent_endpoints','acceptance_receipt']]
  receipt=json.loads(rp.read_text());vals=strings(receipt)
  require(str(receipt.get('status','')).startswith('PASS') and c['endpoints']['sha256'] in vals and c['independent_endpoints']['sha256'] in vals,'independent acceptance receipt')
  a,b=rows(pp),rows(ip);require([r['degree'] for r in a]==list(DEGREES) and [r['degree'] for r in b]==list(DEGREES),'full19degree coverage required before logs')
  out=[]
  for p,q in zip(a,b):
   pv,qv=validrow(p,g,rule),validrow(q,g,rule);require(pv==qv,'independent endpoints differ')
   for key in ['pivot_choices','pivot_ties']:require(p[key]==q[key],'independent metadata differs')
   if out:
    prev=a[len(out)-1];require(p['pivot_choices'][:len(prev['pivot_choices'])]==prev['pivot_choices'] and [z for z in p['pivot_ties'] if z[0]<=prev['degree']]==prev['pivot_ties'],'prefix consistency')
   out.append(pv)
  data[g,rule]=out;pins.append(c)
 require(sum(map(len,data.values()))==152,'152rows required')
 return data,manifest

def down(x,p):return F((x.numerator<<p)//x.denominator,1<<p)
def up(x,p):return -down(-x,p)
class I:
 p=128
 def __init__(self,a,b=None):
  if isinstance(a,I):self.a,self.b=a.a,a.b;return
  self.a,self.b=F(a),F(a if b is None else b);require(self.a<=self.b,'reversed interval')
 def __add__(self,y):
  y=I(y);return I(down(self.a+y.a,self.p),up(self.b+y.b,self.p))
 __radd__=__add__
 def __neg__(self):return I(-self.b,-self.a)
 def __sub__(self,y):return self+-I(y)
 def __rsub__(self,y):return I(y)+-self
 def __mul__(self,y):
  y=I(y);v=[a*b for a in [self.a,self.b] for b in [y.a,y.b]];return I(down(min(v),self.p),up(max(v),self.p))
 __rmul__=__mul__
 def __truediv__(self,y):
  y=I(y);require(y.a>0 or y.b<0,'interval denominator contains zero');return self*I(down(1/y.b,self.p),up(1/y.a,self.p))
 def square(self):return I(down(0 if self.a<=0<=self.b else min(self.a*self.a,self.b*self.b),self.p),up(max(self.a*self.a,self.b*self.b),self.p))
 def absmax(self):return max(abs(self.a),abs(self.b))
 def json(self):return [str(self.a),str(self.b)]
def series(v,m):
 z=(v-1)/(v+1);z2=z*z;term=z;s=F(0)
 for j in range(m):s+=2*term/F(2*j+1);term*=z2
 return s,s+2*term/F((2*m+1)*(1-z2))
def logq(q,p):
 q=F(q);require(q>0,'positive rational logarithm required')
 if q==1:return I(0)
 k=q.numerator.bit_length()-q.denominator.bit_length();two=F(2)**k
 if q<two:k-=1;two/=2
 t=q/two;require(1<=t<2,'mantissa reduction');work=p+16+abs(k).bit_length()
 while True:
  lo,hi=down(t,work),up(t,work);m=work//3+8
  sl,_=series(lo,m);_,su=series(hi,m);l2,u2=series(F(2),m)
  a=sl+k*(l2 if k>=0 else u2);b=su+k*(u2 if k>=0 else l2)
  a,b=down(a,p+4),up(b,p+4)
  if b-a<=F(1,1<<p):return I(a,b)
  work+=16

def predictors(ds,kind,p):return [I(d) if kind=='E' else logq(F(d+1),p+8) for d in ds]
def ols(x,y):
 n=len(x);xb=sum(x,I(0))/n;yb=sum(y,I(0))/n;D=sum(((a-xb).square() for a in x),I(0));require(D.a>0,'OLS denominator guard')
 slope=sum(((a-xb)*b for a,b in zip(x,y)),I(0))/D
 return yb-slope*xb,slope
def weights(p,kind):
 x=predictors(tuple(range(2,15)),kind,p);h=predictors(tuple(range(15,21)),kind,p);xb=sum(x,I(0))/13;D=sum(((a-xb).square() for a in x),I(0));require(D.a>0,'OLS weight denominator guard')
 return [[I(F(1,13))+(z-xb)*(v-xb)/D for v in x] for z in h]
def residual_matrix(w):
 return [[-v for v in row]+[I(int(i==j)) for j in range(6)] for i,row in enumerate(w)]
def quadratic(p):
 E,P=[residual_matrix(weights(p,k)) for k in ['E','P']];Q=[[None]*19 for _ in DEGREES]
 for i in range(19):
  for j in range(i,19):
   Q[i][j]=Q[j][i]=2*sum((r[i]*r[j] for r in P),I(0))-sum((r[i]*r[j] for r in E),I(0))
 return Q
def qeval(Q,y):
 return sum((Q[i][i]*y[i].square() for i in range(19)),I(0))+2*sum((Q[i][j]*y[i]*y[j] for i in range(19) for j in range(i+1,19)),I(0))
def image(A,B,tau):return [(1-t)*a+t*b for a,b,t in zip(A,B,tau)]
def corner(coeff,minimum):return [F(1,2) if c==0 else F(int((c<0) if minimum else (c>0))) for c in coeff]
EARLY=[F(s-6,60) if s<=10 else F(0) for s in DEGREES]
LATE=[F(2*s-31,165) if s>=11 else F(0) for s in DEGREES]
G=[l-e/2 for l,e in zip(LATE,EARLY)]
def slope_test(coeff,D,minimum,A,B,qa,qb):
 tau=corner(coeff,minimum);v=sum((c*y for c,y in zip(coeff,image(A,B,tau))),I(0));recipe=[]
 for c,t,a,b in zip(coeff,tau,qa,qb):
  if c:recipe.append({'q':str(a if t==0 else b),'exponent':int(D*c)})
 sign=1 if v.a>0 else -1 if v.b<0 else None;via='outward logarithm sign'
 if sign is None:
  product=F(1)
  for r in recipe:product*=F(r['q'])**r['exponent']
  sign=(product>1)-(product<1);via='exact rational product'
 passed=sign>0 if minimum else sign<=0
 return {'passed':passed,'sign':sign,'via':via,'interval':v.json(),'D':D,'product_recipe':recipe,'tau':[str(t) for t in tau]}
def upper_bound(Q,Y):
 m=[(z.a+z.b)/2 for z in Y];r=[(z.b-z.a)/2 for z in Y];qm=[sum((Q[i][j]*m[j] for j in range(19)),I(0)) for i in range(19)]
 center=sum((m[i]*qm[i] for i in range(19)),I(0))
 ub=center.b+2*sum(qm[i].absmax()*r[i] for i in range(19))+sum(max(F(0),Q[i][i].b)*r[i]*r[i] for i in range(19))+2*sum(Q[i][j].absmax()*r[i]*r[j] for i in range(19) for j in range(i+1,19))
 return min(ub,qeval(Q,Y).b)
def cover(Q,A,B,p,out,cap=4096):
 # IDs allocated before processing; a successful tree contains every child.
 stack=[(0,None,[(F(0),F(1)) for _ in DEGREES])];nxt=1;processed=0
 path=out/f'cover-{p}.jsonl'
 with path.open('w') as f:
  while stack and processed<cap:
   node,parent,tau=stack.pop();processed+=1
   Y=[I(image([a],[b],[lo])[0].a,image([a],[b],[hi])[0].b) for a,b,(lo,hi) in zip(A,B,tau)];ub=upper_bound(Q,Y)
   event={'id':node,'parent':parent,'precision':p,'tau_box':[[str(a),str(b)] for a,b in tau],'upper_bound':str(ub)}
   if ub<=0:event['action']='certified'
   else:
    mid=[(lo+hi)/2 for lo,hi in tau];val=qeval(Q,image(A,B,mid))
    if val.a>0:
     event['action']='counterchoice';f.write(json.dumps(event)+'\n');f.flush();return {'status':'INCONCLUSIVE, certified counterchoice','violated_clause':'SSE','witness_tau':[str(t) for t in mid],'signed_interval':val.json(),'processed_boxes':processed,'tree_artifact':ident(path)}
    widths=[(b.b-a.a)*(hi-lo) for a,b,(lo,hi) in zip(A,B,tau)];axis=max(range(19),key=lambda i:(widths[i],-i));lo,hi=tau[axis];md=(lo+hi)/2;l=tau.copy();r=tau.copy();l[axis]=(lo,md);r[axis]=(md,hi);children=[nxt,nxt+1];nxt+=2
    event.update(action='split',axis=axis,children=children);stack.extend([(children[1],node,r),(children[0],node,l)])
   f.write(json.dumps(event)+'\n')
 return {'status':'KILL, certified universal' if not stack else 'INCONCLUSIVE, not certified within budget','processed_boxes':processed,'pending_boxes':len(stack),'tree_artifact':ident(path)}
def descriptive(y,p):
 ans={}
 for kind in ['E','P']:
  a,b=ols(predictors(DEGREES,kind,p),y);w=weights(p,kind);sse=sum(((y[13+h]-sum((v*z for v,z in zip(row,y[:13])),I(0))).square() for h,row in enumerate(w)),I(0))
  traina,trainb=ols(predictors(tuple(range(2,15)),kind,p),y[:13])
  ans[kind]={'all_degree_intercept':a.json(),'all_degree_slope':b.json(),'training_2_14_intercept':traina.json(),'training_2_14_slope':trainb.json(),'holdout_15_20_SSE':sse.json()}
 ans['early_slope']=sum((c*v for c,v in zip(EARLY,y)),I(0)).json();ans['late_slope']=sum((c*v for c,v in zip(LATE,y)),I(0)).json()
 return ans
def run_grid(data,g,out):
 out.mkdir();qa=[];qb=[];recipes=[]
 for i,s in enumerate(DEGREES):
  comps={r:data[g,r][i] for r in RULES[1:]};mu=min(v[3] for v in comps.values());ml=min(v[0] for v in comps.values());lo=data[g,'bj'][i][0]/mu;hi=data[g,'bj'][i][3]/ml;require(lo<=hi,'ratio endpoint order');qa.append(lo);qb.append(hi)
  recipes.append({'degree':s,'lower_q':str(lo),'upper_q':str(hi),'lower_min_rules':[r for r,v in comps.items() if v[3]==mu],'upper_min_rules':[r for r,v in comps.items() if v[0]==ml]})
 history=[];desc=None;rulefits=None
 for p in [128,256,512]:
  I.p=p
  try:
   A=[logq(q,p+8)/2 for q in qa];B=[logq(q,p+8)/2 for q in qb]
   rulefits={}
   for rule in RULES:
    L=[logq(v[0],p+8)/2 for v in data[g,rule]];U=[logq(v[3],p+8)/2 for v in data[g,rule]]
    rulefits[rule]={name:{kind:{'intercept':a.json(),'slope':b.json()} for kind in ['E','P'] for a,b in [ols(predictors(DEGREES,kind,p),curve)]} for name,curve in [('lower',L),('upper',U),('midpoint',[(a+b)/2 for a,b in zip(L,U)])]}
   desc={name:descriptive(curve,p) for name,curve in [('lower',A),('upper',B),('midpoint',[(a+b)/2 for a,b in zip(A,B)])]}
   early=slope_test(EARLY,60,True,A,B,qa,qb);late=slope_test(G,1320,False,A,B,qa,qb);clauses={'early_positive':early,'late_minus_half_early':late,'SSE':'NOT_NEEDED_AFTER_SLOPE_COUNTERCHOICE'}
   if not early['passed'] or not late['passed']:
    bad=early if not early['passed'] else late;result={'status':'INCONCLUSIVE, certified counterchoice','violated_clause':'early_positive' if bad is early else 'late_minus_half_early','witness_tau':bad['tau'],'signed_interval':bad['interval']};break
   Q=quadratic(p);fixed=[[F(0)]*19,[F(1,2)]*19,[F(1)]*19,[F(x) for x in early['tau']],[F(x) for x in late['tau']]];result=None
   for tau in fixed:
    val=qeval(Q,image(A,B,tau))
    if val.a>0:result={'status':'INCONCLUSIVE, certified counterchoice','violated_clause':'SSE','witness_tau':[str(x) for x in tau],'signed_interval':val.json()};break
   if result is None:result=cover(Q,A,B,p,out)
   clauses['SSE']=result['status'];history.append({'precision':p,**result})
   if result['status']!='INCONCLUSIVE, not certified within budget':break
  except GuardError as exc:
   history.append({'precision':p,'arithmetic_guard':str(exc)});result={'status':'INCONCLUSIVE, not certified within budget','arithmetic_guard':str(exc)};clauses={'arithmetic':'unresolved guard'}
 return {'ratio_recipes':recipes,'log_endpoint_enclosures':{'lower':[v.json() for v in A],'upper':[v.json() for v in B]},'ordinate_width_upper_bounds':[str(b.b-a.a) for a,b in zip(A,B)],'rule_descriptive_fits':rulefits,'ratio_descriptive_diagnostics':desc,'universal':{'precision':p,'clauses':clauses,'precision_history':history,**result}}

def run(path,out):
 data,manifest=load_manifest(path) # All152 guards precede log/fit calls.
 out.mkdir(parents=True,exist_ok=False);t=time.monotonic()
 meta={'schema':'g1-fit-output-v1','status':'MEASURED finite endpoint fits and frozen operational interval verdicts; no trueK/asymptotic claim','input_manifest':ident(path),'producer':ident(__file__),'specification':ident(pathlib.Path(__file__).resolve().parents[1]/'g1-fit-spec.md'),'runtime':{'python':platform.python_version(),'arithmetic':'stdlib Fraction exact rational/dyadic outward','precision_schedule':[128,256,512],'max_processed_boxes_per_grid_precision':4096},'accepted_rows':152}
 (out/'pre-fit.json').write_text(json.dumps(meta,indent=1)+'\n')
 report={**meta,'grids':{g:run_grid(data,g,out/g) for g in GRIDS}};report['elapsed_seconds']=time.monotonic()-t
 (out/'report.json').write_text(json.dumps(report,indent=1)+'\n')
 receipt={**meta,'report':ident(out/'report.json'),'elapsed_seconds':report['elapsed_seconds'],'grid_verdicts':{g:report['grids'][g]['universal']['status'] for g in GRIDS}}
 (out/'receipt.json').write_text(json.dumps(receipt,indent=1)+'\n');return receipt

def synthetic_fixture(directory):
 directory.mkdir(parents=True,exist_ok=False);cases=[]
 for g in GRIDS:
  for rule in RULES:
   rr=[]
   for n in DEGREES:
    choices=[]
    for t in range(1,n+1):
     for j in range(t+1):choices.append('X' if (rule=='pivot' and j<t) or (rule=='bj' and j==0) or (rule=='mirror' and j!=t) or (rule=='alt' and 2*j<t) else 'Y')
    k=(n+1)*(n+2)//2;m={'triangle':325,'rotated':625}[g]
    rr.append({'set':g,'rule':rule,'degree':n,'sources':'all','source_count':k-1,'basis_count':k,'point_count':m,'pivot_choices':choices,'pivot_ties':[[2,1]] if rule=='pivot' and g=='rotated' else [],'normal_trace_exact':str(m-k),**{field:{'exact':value} for field,value in zip(FIELDS,['1','4','9','4'])}})
   stem=directory/f'{g}-{rule}';pp=stem.with_suffix('.json');ip=directory/(stem.name+'-independent.jsonl');rp=directory/(stem.name+'-acceptance.json')
   pp.write_text(json.dumps({'runs':rr}));ip.write_text('\n'.join(json.dumps(r) for r in rr)+'\n');rp.write_text(json.dumps({'status':'PASS SYNTHETIC FIXTURE ONLY','producer_endpoints':ident(pp),'native_endpoints':ident(ip)}))
   cases.append({'grid':g,'rule':rule,'endpoints':ident(pp),'independent_endpoints':ident(ip),'acceptance_receipt':ident(rp)})
 manifest={'schema':'g1-fit-input-v1','source_metric':METRIC,'tie_convention':'X wins exact ties','frozen_source_sha256':SOURCE,'cases':cases,'synthetic_only':True}
 path=directory/'manifest.json';path.write_text(json.dumps(manifest));return path

def self_test(out):
 out.mkdir(parents=True,exist_ok=False);t=time.monotonic();tests=[];I.p=128
 def test(ok,name):
  require(ok,'synthetic test failed: '+name);tests.append(name)
 test(logq(1,128).json()==['0','0'],'log1 exact')
 for prec in [128,256,512]:
  z=logq(F(3,2),prec);lo,hi=series(F(3,2),512);test(z.a<=lo<=hi<=z.b and z.b-z.a<=F(1,1<<prec),'log enclosure precision '+str(prec))
 for k in [-10000,-1,1,10000]:
  z=logq(F(2)**k,128);lo,hi=series(F(2),160);a,b=(k*lo,k*hi) if k>0 else (k*hi,k*lo)
  test(z.a<=a<=b<=z.b and z.b-z.a<=F(1,1<<128),'signed large-scale log2 exponent '+str(k))
 for q in [F(3,2),F(3,4),F(1,3),F((1<<200)+1,1<<199)]:
  a,b=logq(q,128),logq(1/q,128);test(a.a<=-b.a and a.b>=-b.b and a.b-a.a<=F(1,1<<128),'reciprocal log enclosure '+str(q))
 test(I(-2,3).square().json()==['0','9'],'zero-straddling square')
 test(I(-3,-2).square().json()==['4','9'],'negative interval square')
 a,b=ols([I(n) for n in DEGREES],[I(2+3*n) for n in DEGREES]);test(a.a<=2<=a.b and b.a<=3<=b.b,'affine exact-predictor OLS')
 for kind in ['E','P']:
  x=predictors(DEGREES,kind,128);a,b=ols(x,[2+3*z for z in x]);test(a.a<=2<=a.b and b.a<=3<=b.b,'affine '+kind+' predictor OLS')
  w=weights(128,kind);xt=predictors(tuple(range(2,15)),kind,128);xh=predictors(tuple(range(15,21)),kind,128)
  test(all(sum(row,I(0)).a<=1<=sum(row,I(0)).b and sum((u*v for u,v in zip(row,xt)),I(0)).a<=h.b and sum((u*v for u,v in zip(row,xt)),I(0)).b>=h.a for row,h in zip(w,xh)),'holdout affine exactness '+kind)
 A=[I(0)]*19;B=[I(0)]*19;ones=[F(1)]*19
 e=slope_test(EARLY,60,True,A,B,ones,ones);l=slope_test(G,1320,False,A,B,ones,ones)
 test(not e['passed'] and e['sign']==0 and l['passed'] and l['sign']==0,'strict early equality fails; late equality passes')
 neg=[[I(-int(i==j)) for j in range(19)] for i in range(19)];pos=[[-z for z in row] for row in neg]
 test(qeval(pos,[I(F(1,2))]*19).a>0,'strict SSE quadratic counterchoice')
 negative_dir=out/'negative-cover';negative_dir.mkdir();c=cover(neg,[I(0)]*19,[I(1)]*19,128,negative_dir,2);test(c['status']=='KILL, certified universal' and c['processed_boxes']==1,'negative quadratic full root cover')
 tangent=[[I(0) for _ in range(19)] for _ in range(19)];tangent[0][0]=tangent[1][1]=I(-1);tangent[0][1]=tangent[1][0]=I(1)
 budget_dir=out/'tangency-budget';budget_dir.mkdir();budget=cover(tangent,[I(0)]*19,[I(1)]*19,128,budget_dir,3)
 test(budget['status']=='INCONCLUSIVE, not certified within budget' and budget['processed_boxes']==3,'tangency never becomes kill on budget exhaustion')
 events=[json.loads(z) for z in pathlib.Path(budget['tree_artifact']['path']).read_text().splitlines()];first=events[0];test(first['action']=='split' and first['axis']==0 and first['children']==[1,2],'deterministic split coordinate and ids')
 # Exact squared ratio min/half-log regression primitive, with different minima winners.
 low=F(9)/min(F(16),F(25),F(36));high=F(100)/min(F(4),F(1),F(9));test(low==F(9,16) and high==100 and (logq(low,128)/2).b<0,'separate squared comparator minima and half-log')
 fixture=synthetic_fixture(out/'valid-fixture');data,m=load_manifest(fixture);test(len(data)==8 and sum(map(len,data.values()))==152,'full synthetic coverage guard accepts')
 # Every malformed test calls only the entry guard: no logarithm or fit.
 original=globals()['logq']
 def forbidden(*args):raise AssertionError('logarithm reached before coverage gate')
 globals()['logq']=forbidden
 try:
  for name,mutate in [('missingcase',lambda x:x['cases'].pop()),('duplicatecase',lambda x:x['cases'].__setitem__(1,x['cases'][0])),('wrongmetric',lambda x:x.update(source_metric='scalar')),('wrongsourcepin',lambda x:x.update(frozen_source_sha256='0'*64)),('badartifacthash',lambda x:x['cases'][0]['endpoints'].update(sha256='0'*64))]:
   bad=copy.deepcopy(m);mutate(bad);bp=out/f'{name}.json';bp.write_text(json.dumps(bad))
   try:load_manifest(bp)
   except GuardError:test(True,'prelog rejection '+name)
   else:raise AssertionError('malformed fixture accepted '+name)
  base=rows(pathlib.Path(m['cases'][0]['endpoints']['path']))
  edits=[('missingdegree',lambda r:r.pop()),('duplicatedegree',lambda r:r.__setitem__(1,r[0])),('partialsource',lambda r:r[-1].update(source_count=1)),('badupper',lambda r:r[-1]['upper_squared'].update(exact='5')),('negativeL',lambda r:r[-1]['Knode_squared'].update(exact='-1')),('badchoice',lambda r:r[-1]['pivot_choices'].__setitem__(0,'Y')),('badtie',lambda r:r[-1].update(pivot_ties=[[2,1]])),('wrongnodes',lambda r:r[-1].update(point_count=624)),('wrongtrace',lambda r:r[-1].update(normal_trace_exact='0'))]
  for name,edit in edits:
   rr=copy.deepcopy(base);edit(rr);bad=copy.deepcopy(m);pp=out/f'{name}-endpoints.json';pp.write_text(json.dumps({'runs':rr}));bad['cases'][0]['endpoints']=ident(pp);rp=out/f'{name}-acceptance.json';rp.write_text(json.dumps({'status':'PASS SYNTHETIC ONLY','producer_endpoints':ident(pp),'native_endpoints':bad['cases'][0]['independent_endpoints']}));bad['cases'][0]['acceptance_receipt']=ident(rp);bp=out/f'{name}.json';bp.write_text(json.dumps(bad))
   try:load_manifest(bp)
   except GuardError:test(True,'prelog rejection '+name)
   else:raise AssertionError('malformed fixture accepted '+name)
 finally:globals()['logq']=original
 receipt={'status':'PASS SYNTHETIC ARITHMETIC AND GUARD TESTS ONLY; REAL G1 FIT NOT RUN','producer':ident(__file__),'command':sys.argv,'python':platform.python_version(),'precision':128,'elapsed_seconds':time.monotonic()-t,'tests':tests,'synthetic_fixture':ident(fixture),'limits':'Not independent approval; no real G1 endpoint rows loaded, no trueK or trend measured.'}
 (out/'synthetic-receipt.json').write_text(json.dumps(receipt,indent=1)+'\n');return receipt

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--manifest');ap.add_argument('--output-dir',required=True);ap.add_argument('--self-test',action='store_true');a=ap.parse_args()
 require(a.self_test or a.manifest,'manifest required outside synthetic self-test')
 receipt=self_test(pathlib.Path(a.output_dir)) if a.self_test else run(a.manifest,pathlib.Path(a.output_dir));print(json.dumps(receipt,indent=1))
if __name__=='__main__':main()
