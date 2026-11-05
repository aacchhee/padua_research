#!/usr/bin/env python3
"""Distinct n4 G3 certificate checker: Sympy algebraic field/domain matrices.
No producer code or arithmetic imports. All acceptance is exact in QQ(sqrt(2),sqrt(5)).
"""
import argparse,copy,hashlib,json,math,pathlib,re,resource,signal,sys,time
import sympy as sp
from sympy.polys.matrices import DomainMatrix as DM
sys.set_int_max_str_digits(1000000)
F=sp.QQ.algebraic_field(sp.sqrt(2),sp.sqrt(5));ZERO=F.zero;ONE=F.one
RAD=[F.from_sympy(v) for v in (sp.Integer(1),sp.sqrt(5),sp.sqrt(2),sp.sqrt(10))]
def power_coeff(z):
 c=list(reversed(z.to_list()));return c+[sp.QQ.zero]*(4-len(c))
COORD=sp.Matrix.hstack(*[sp.Matrix(power_coeff(z)) for z in RAD]).inv()
COORD=[[sp.QQ.from_sympy(COORD[i,j]) for j in range(4)] for i in range(4)]
MON=[(a,t-a) for t in range(10) for a in range(t+1)]
def need(ok,msg):
 if not ok:raise ValueError(msg)
def identity(p):
 p=pathlib.Path(p);b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def rat(s):
 need(isinstance(s,str) and re.fullmatch(r'[+-]?\d+(?:/[1-9]\d*)?',s) is not None,'invalid rational string')
 return sp.QQ.from_sympy(sp.Rational(s))
def decode(v):
 need(isinstance(v,list) and len(v)==4,'invalid quartic-field encoding')
 return sum((F.convert(rat(c))*r for c,r in zip(v,RAD)),ZERO)
def pair(z):
 c=power_coeff(z)
 return tuple(sum((COORD[i][j]*c[j] for j in range(4)),sp.QQ.zero) for i in range(4))
def encode(z):return [str(t) for t in pair(z)]
def qsign(a,b):
 if b==0:return (a>0)-(a<0)
 if a==0:return (b>0)-(b<0)
 if (a>0)==(b>0):return 1 if a>0 else -1
 delta=a*a-5*b*b
 need(delta!=0,'impossible sqrt5 rational equality')
 return (1 if delta>0 else -1)*(1 if a>0 else -1)
def sign(z):
 a,b,c,d=pair(z);u=qsign(a,b);v=qsign(c,d)
 if not u:return v
 if not v:return u
 if u==v:return u
 delta=qsign(a*a+5*b*b-2*c*c-10*d*d,2*a*b-4*c*d)
 need(delta!=0,'impossible sqrt2 over Qsqrt5 equality')
 return delta*u
def absolute(z):return z if sign(z)>=0 else -z
def nodes():
 r2,r5=RAD[2],RAD[1]
 xx=[ONE,r2/2,ZERO,-r2/2,-ONE]
 yy=[ONE,(ONE+r5)/4,(r5-ONE)/4,(ONE-r5)/4,-(ONE+r5)/4,-ONE]
 need(r2*r2==F.convert(2) and r5*r5==F.convert(5) and sign(r2)>0 and sign(r5)>0,'positive radical embedding')
 for seq,degree in [(xx,3),(yy,4)]:
  need(seq[0]==ONE and seq[-1]==-ONE and all(sign(a-b)>0 for a,b in zip(seq,seq[1:])),'node order/endpoints')
  for x in seq[1:-1]:
   prev,cur=ONE,2*x
   for k in range(2,degree+1):prev,cur=cur,2*x*cur-prev
   need(cur==ZERO,'Chebyshev U interior node identity')
 out=[(x,y) for j,x in enumerate(xx) for k,y in enumerate(yy) if (j+k)%2==0]
 need(len(out)==15 and len(set(out))==15,'node cardinality/uniqueness')
 for z,want in [(r5-2,1),(2-r5,-1),(r2-r5,-1),(r5-r2,1),(r2*r5-3,1),(3-r2*r5,-1)]:need(sign(z)==want,'embedding sign control')
 return out
def jet_and_kernel(z):
 need(len(MON)==55 and len(set(MON))==55 and max(a+b for a,b in MON)==9,'full monomial space')
 rows=[]
 for x,y in z:
  rows.append([x**a*y**b for a,b in MON])
  rows.append([F.convert(a)*x**(a-1)*y**b if a else ZERO for a,b in MON])
  rows.append([F.convert(b)*x**a*y**(b-1) if b else ZERO for a,b in MON])
 J=DM(rows,(45,55),F);rank=J.rank();B=J.nullspace();validate_kernel(J,B,rank)
 return J,B,rank
def validate_kernel(J,B,rank):
 d=55-rank;need(J.shape==(45,55) and B.shape==(d,55),'incomplete first-jet kernel dimension')
 need(B.rank()==d,'kernel rank failure');need(J.matmul(B.transpose()).is_zero_matrix,'kernel annihilation failure')
def baseline():
 x,y=sp.symbols('x y')
 def T(k,v):
  if k==0:return sp.Integer(1)
  prev,cur=sp.Integer(1),v
  for j in range(1,k):prev,cur=cur,sp.expand(2*v*cur-prev)
  return cur
 g=[T(4-m,x)*T(m,y)-T(m,x)*T(5-m,y) for m in range(4)]
 p=sp.Poly(sp.expand(9*(g[1]**2-g[0]*g[2]/2)+g[2]**2-g[1]*g[3]),x,y)
 need(p.total_degree()<=9 and not p.is_zero,'actual P4 degree/nonzero')
 return {mon:F.from_sympy(c) for mon,c in p.terms()}
def lower_check(cert,z,original):
 L=rat(cert['L']);need(L>0,'nonpositive lower radius');p={}
 for term in cert['polynomial']:
  need(isinstance(term,list) and len(term)==3,'polynomial term schema');a,b,c=term;need(type(a)is int and type(b)is int and a>=0 and b>=0 and a+b<=9,'polynomial degree/indices');need((a,b)not in p,'duplicate polynomial term');p[a,b]=decode(c)
 p={k:v for k,v in p.items() if v!=ZERO};need(p and p==original,'polynomial is not the actual rational P4')
 LK=F.convert(L);records=[];jet_zeros=0
 for node,(x,y) in enumerate(z):
  t={}
  for r,s in MON:
   v=ZERO
   for (a,b),c in p.items():
    if a>=r and b>=s:v+=c*F.convert(math.comb(a,r)*math.comb(b,s))*x**(a-r)*y**(b-s)
   t[r,s]=v
  need(t[0,0]==ZERO and t[1,0]==ZERO and t[0,1]==ZERO,'lower first-jet failure');jet_zeros+=3
  hxx=2*t[2,0];hxy=t[1,1];hyy=2*t[0,2];det=hxx*hyy-hxy*hxy;trace=hxx+hyy
  need(sign(hxx)>0 and sign(det)>0 and sign(trace)>0,'lower Hessian not positive definite');mu=det/trace;need(sign(mu)>0,'nonpositive eigenvalue lower bound')
  sums={k:sum((absolute(t[a,b]) for a,b in MON if a+b==k),ZERO) for k in range(3,10)}
  remainder=sum((sums[k]*LK**(k-2) for k in range(3,10)),ZERO);margin=mu/2-remainder;need(sign(margin)>=0,'lower Taylor full-ball inequality failure')
  records.append({'node':node,'mu':encode(mu),'Taylor_margin':encode(margin)})
 return {'L':str(L),'nonzero_terms':len(p),'degree':max(a+b for a,b in p),'exact_jet_zeros':jet_zeros,'node_certificates':records,'whole_ball_criterion':'PASS all15 exact finite Taylor inequalities'}
def upper_check(cert,z,B):
 U=rat(cert['U']);need(U>0,'nonpositive upper radius');q=cert['q'];need(type(q)is int and q in (2,4,8),'unregistered proposer q')
 points=cert['points'];weights=cert['weights'];need(isinstance(points,list) and len(points)==len(weights) and points,'upper point/weight cardinality');rows=[];lam=[];seen=set();outside=0
 for point,weight in zip(points,weights):
  need(isinstance(point,list) and len(point)==3,'point schema');i,hx,hy=point;need(type(i)is int and 0<=i<len(z),'invalid node index');hx,hy=rat(hx),rat(hy)
  need(hx*hx+hy*hy<=U*U,'point outside full Euclidean node ball');need((hx*q/U).denominator==1 and (hy*q/U).denominator==1,'point not on registered rational offset grid')
  w=(z[i][0]+F.convert(hx),z[i][1]+F.convert(hy));need(w not in seen,'duplicate exact point');seen.add(w)
  outside+=int(sign(absolute(w[0])-ONE)>0 or sign(absolute(w[1])-ONE)>0)
  rows.append([w[0]**a*w[1]**b for a,b in MON]);v=decode(weight);need(sign(v)>0,'nonpositive retained weight');lam.append([v])
 W=DM(rows,(len(rows),55),F);A=W.matmul(B.transpose());d=B.shape[0];need(A.rank()==d,'upper evaluation rank does not span full kernel')
 need(A.transpose().matmul(DM(lam,(len(lam),1),F)).is_zero_matrix,'upper positive dependence failure')
 return {'U':str(U),'q':q,'retained_points':len(points),'strict_positive_weights':len(weights),'full_kernel_evaluation_rank':d,'exact_balance_coordinates':d,'ball_membership':'PASS every point in its full R2 ball','points_outside_square':outside}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--lower',required=True);ap.add_argument('--upper');ap.add_argument('--out',required=True);ap.add_argument('--receipt',required=True);a=ap.parse_args();start=time.monotonic();out=pathlib.Path(a.out);out.mkdir(parents=True,exist_ok=False)
 resource.setrlimit(resource.RLIMIT_AS,(2*1024**3,2*1024**3))
 def expired(*_):raise TimeoutError('580-second internal checker cap')
 signal.signal(signal.SIGALRM,expired);signal.alarm(580)
 receipt={'status':'INCOMPLETE','rules_sha':'9825d184517db81d0aad8542fbd6639f2164b803','code':identity(__file__),'command':[sys.executable,'-B',str(pathlib.Path(__file__).resolve()),*sys.argv[1:]],'runtime':{'python':sys.version.split()[0],'sympy':sp.__version__},'inputs':[identity(p) for p in [a.lower,a.upper] if p],'trusted_dependencies':'Sympy exact QQ(sqrt2,sqrt5) domain arithmetic/elimination; Python rational/integer comparison; independently implemented positive-radical nested-square sign tests','scope':'n4 only; D9/full55monomials/15nodes/fullR2balls; no n5-8/G3trend/U2 status'}
 try:
  lower=json.loads(pathlib.Path(a.lower).read_text());poly=baseline();z=nodes();J,B,rank=jet_and_kernel(z)
  receipt.update(jet_matrix_shape=[45,55],jet_rank=rank,full_kernel_dimension=B.shape[0],kernel_identity='J*B^T=0 and full exact ranks checked')
  lo=lower_check(lower,z,poly);accepted=[]
  for j in range(21):
   c=copy.deepcopy(lower);c['L']=str(sp.Rational(1,2**j))
   try:lower_check(c,z,poly)
   except ValueError as e:
    need('Taylor full-ball inequality failure' in str(e),'unexpected radius-check failure: '+str(e))
   else:accepted.append(c['L'])
  need(accepted and lower['L']==accepted[0],'producer lower is not largest accepted saved radius')
  receipt.update(lower=lo,saved_radius_list_accepted=accepted)
  if a.upper:receipt['upper']=upper_check(json.loads(pathlib.Path(a.upper).read_text()),z,B)
  basis={'monomials':MON,'nodes':[[encode(x),encode(y)]for x,y in z],'J_shape':J.shape,'J_rank':rank,'kernel_rows':[[encode(x)for x in row]for row in B.to_list()]};bp=out/'independent-kernel.json';bp.write_text(json.dumps(basis,separators=(',',':'))+'\n')
  receipt.update(status='PASS independent exact n4 lower/full-kernel upper checks' if a.upper else 'PASS independent exact n4 lower/full-kernel checks; upper pending',kernel_artifact=identity(bp))
 except Exception as e:receipt.update(status='INCOMPLETE_OR_REJECTED',error=repr(e))
 finally:
  signal.alarm(0);receipt['elapsed_seconds']=time.monotonic()-start;receipt['peak_rss_KiB']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss;pathlib.Path(a.receipt).write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt,indent=2))
 return 0 if receipt['status'].startswith('PASS') else 1
if __name__=='__main__':sys.exit(main())
