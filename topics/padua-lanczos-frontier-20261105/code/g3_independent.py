#!/usr/bin/env python3
"""Distinct n3 G3 certificate checker: Sympy algebraic field/domain matrices.
No producer code or arithmetic imports. All acceptance is exact in QQ(sqrt(2)).
"""
import argparse,copy,hashlib,json,math,pathlib,re,resource,signal,sys,time
import sympy as sp
from sympy.polys.matrices import DomainMatrix as DM
sys.set_int_max_str_digits(1000000)
F=sp.QQ.algebraic_field(sp.sqrt(2));ZERO=F.zero;ONE=F.one
BASE_SHA='287e8dd0bdaa60d93d728045fcd47c5c75832813657f4849081fe4b1e0629e8b'
MON=[(a,t-a) for t in range(8) for a in range(t+1)]
def need(ok,msg):
 if not ok:raise ValueError(msg)
def identity(p):
 p=pathlib.Path(p);b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def rat(s):
 need(isinstance(s,str) and re.fullmatch(r'[+-]?\d+(?:/[1-9]\d*)?',s) is not None,'invalid rational string')
 return sp.QQ.from_sympy(sp.Rational(s))
def decode(v):
 need(isinstance(v,list) and len(v)==2,'invalid quadratic-field encoding')
 return F.convert(rat(v[0]))+F.convert(rat(v[1]))*F.from_sympy(sp.sqrt(2))
def pair(z):
 c=list(z.to_list());need(len(c)<=2,'unexpected algebraic degree')
 if len(c)==0:return sp.QQ.zero,sp.QQ.zero
 if len(c)==1:return c[0],sp.QQ.zero
 return c[1],c[0]
def encode(z):return [str(t) for t in pair(z)]
def sign(z):
 a,b=pair(z)
 if b==0:return (a>0)-(a<0)
 if a==0:return (b>0)-(b<0)
 if (a>0)==(b>0):return 1 if a>0 else -1
 c=a*a-2*b*b
 need(c!=0,'impossible rational sqrt2 equality for nonzero coefficients')
 return (1 if c>0 else -1)*(1 if a>0 else -1)
def absolute(z):return z if sign(z)>=0 else -z
def nodes():
 out=[]
 for j in range(4):
  for k in range(5):
   if (j+k)%2==0:out.append((F.from_sympy(sp.cos(sp.pi*j/3)),F.from_sympy(sp.cos(sp.pi*k/4))))
 need(len(out)==10 and len(set(out))==10,'node cardinality/uniqueness')
 r=F.from_sympy(sp.sqrt(2));need(r*r==F.convert(2) and sign(r)>0 and sign(r-ONE)>0 and sign(F.convert(2)-r)>0,'positive real embedding')
 for text,expected in [(['3','-2'],1),(['-3','2'],-1),(['1','-1'],-1),(['-1','1'],1)]:need(sign(decode(text))==expected,'exact embedding sign control')
 return out
def jet_and_kernel(z):
 need(len(MON)==36 and len(set(MON))==36 and max(a+b for a,b in MON)==7,'full monomial space')
 rows=[]
 for x,y in z:
  rows.append([x**a*y**b for a,b in MON])
  rows.append([F.convert(a)*x**(a-1)*y**b if a else ZERO for a,b in MON])
  rows.append([F.convert(b)*x**a*y**(b-1) if b else ZERO for a,b in MON])
 J=DM(rows,(30,36),F);rank=J.rank();B=J.nullspace();validate_kernel(J,B,rank)
 return J,B,rank
def validate_kernel(J,B,rank):
 d=36-rank;need(J.shape==(30,36) and B.shape==(d,36),'incomplete first-jet kernel dimension')
 need(B.rank()==d,'kernel rank failure');need(J.matmul(B.transpose()).is_zero_matrix,'kernel annihilation failure')
def baseline(p):
 ident=identity(p);need(ident['bytes']==3963 and ident['sha256']==BASE_SHA,'baseline source hash/size')
 text=pathlib.Path(p).read_text();block=text.split('p* monomial coefficients',1)[1].split('    node ',1)[0];poly={}
 for aa,bb,body in re.findall(r'x\^(\d+) y\^(\d+): \(([^()]*)r2\)',block):
  m=re.fullmatch(r'(.+)\+([^+]+)',body);need(m is not None,'baseline coefficient syntax');key=(int(aa),int(bb));need(key not in poly,'duplicate baseline monomial');poly[key]=decode([m[1],m[2]])
 need(len(poly)==20 and all(a+b<=7 for a,b in poly) and any(v!=ZERO for v in poly.values()),'baseline polynomial extraction')
 return poly,ident
def lower_check(cert,z,original):
 L=rat(cert['L']);need(L>0,'nonpositive lower radius');p={}
 for term in cert['polynomial']:
  need(isinstance(term,list) and len(term)==3,'polynomial term schema');a,b,c=term;need(type(a)is int and type(b)is int and a>=0 and b>=0 and a+b<=7,'polynomial degree/indices');need((a,b)not in p,'duplicate polynomial term');p[a,b]=decode(c)
 p={k:v for k,v in p.items() if v!=ZERO};need(p and p==original,'polynomial is not the actual recovered pstar')
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
  sums={k:sum((absolute(t[a,b]) for a,b in MON if a+b==k),ZERO) for k in range(3,8)}
  remainder=sum((sums[k]*LK**(k-2) for k in range(3,8)),ZERO);margin=mu/2-remainder;need(sign(margin)>=0,'lower Taylor full-ball inequality failure')
  records.append({'node':node,'mu':encode(mu),'Taylor_margin':encode(margin)})
 return {'L':str(L),'nonzero_terms':len(p),'degree':max(a+b for a,b in p),'exact_jet_zeros':jet_zeros,'node_certificates':records,'whole_ball_criterion':'PASS all10 exact finite Taylor inequalities'}
def upper_check(cert,z,B):
 U=rat(cert['U']);need(U>0,'nonpositive upper radius');q=cert['q'];need(type(q)is int and q in (2,4,8),'unregistered proposer q')
 points=cert['points'];weights=cert['weights'];need(isinstance(points,list) and len(points)==len(weights) and points,'upper point/weight cardinality');rows=[];lam=[];seen=set();outside=0
 for point,weight in zip(points,weights):
  need(isinstance(point,list) and len(point)==3,'point schema');i,hx,hy=point;need(type(i)is int and 0<=i<len(z),'invalid node index');hx,hy=rat(hx),rat(hy)
  need(hx*hx+hy*hy<=U*U,'point outside full Euclidean node ball');need((hx*q/U).denominator==1 and (hy*q/U).denominator==1,'point not on registered rational offset grid')
  w=(z[i][0]+F.convert(hx),z[i][1]+F.convert(hy));need(w not in seen,'duplicate exact point');seen.add(w)
  outside+=int(sign(absolute(w[0])-ONE)>0 or sign(absolute(w[1])-ONE)>0)
  rows.append([w[0]**a*w[1]**b for a,b in MON]);v=decode(weight);need(sign(v)>0,'nonpositive retained weight');lam.append([v])
 W=DM(rows,(len(rows),36),F);A=W.matmul(B.transpose());d=B.shape[0];need(A.rank()==d,'upper evaluation rank does not span full kernel')
 need(A.transpose().matmul(DM(lam,(len(lam),1),F)).is_zero_matrix,'upper positive dependence failure')
 return {'U':str(U),'q':q,'retained_points':len(points),'strict_positive_weights':len(weights),'full_kernel_evaluation_rank':d,'exact_balance_coordinates':d,'ball_membership':'PASS every point in its full R2 ball','points_outside_square':outside}
def controls(lower,upper,z,poly,J,B,rank):
 results=[]
 def reject(label,fn):
  try:fn()
  except (ValueError,KeyError,TypeError,IndexError) as e:results.append({'control':label,'rejected':True,'reason':str(e)});return
  raise ValueError('malformed control accepted: '+label)
 c=copy.deepcopy(lower);c['polynomial'][0][2][0]=str(rat(c['polynomial'][0][2][0])+1);reject('changed actual polynomial',lambda:lower_check(c,z,poly))
 c=copy.deepcopy(lower);c['L']='1';reject('oversized lower radius violates Taylor bound',lambda:lower_check(c,z,poly))
 c=copy.deepcopy(upper);c['weights'][0]=['-1','0'];reject('negative retained weight',lambda:upper_check(c,z,B))
 c=copy.deepcopy(upper);c['weights'][0][0]=str(rat(c['weights'][0][0])+1);reject('positive but unbalanced weights',lambda:upper_check(c,z,B))
 c=copy.deepcopy(upper);c['points'][0][1]='10';reject('off-ball point',lambda:upper_check(c,z,B))
 c=copy.deepcopy(upper);c['points']=c['points'][:1];c['weights']=c['weights'][:1];reject('rank-deficient point set',lambda:upper_check(c,z,B))
 c=copy.deepcopy(upper);c['points'][0][0]=10;reject('invalid node index',lambda:upper_check(c,z,B))
 c=copy.deepcopy(upper);c['weights'][0]=['1','0','0'];reject('invalid field encoding',lambda:upper_check(c,z,B))
 smaller=DM(B.to_list()[:-1],(B.shape[0]-1,36),F);reject('proper kernel subspace',lambda:validate_kernel(J,smaller,rank))
 lower_check(lower,z,poly);upper_check(upper,z,B)
 return results

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--lower',required=True);ap.add_argument('--upper',required=True);ap.add_argument('--baseline',required=True);ap.add_argument('--out',required=True);ap.add_argument('--receipt',required=True);a=ap.parse_args();start=time.monotonic();out=pathlib.Path(a.out);out.mkdir(parents=True,exist_ok=False)
 resource.setrlimit(resource.RLIMIT_AS,(2*1024**3,2*1024**3))
 def expired(*_):raise TimeoutError('580-second internal prototype cap')
 signal.signal(signal.SIGALRM,expired);signal.alarm(580)
 receipt={'status':'INCOMPLETE','rules_sha':'12879b5666a93f2ca88d89c3deaa7a152f883cc3','code':identity(__file__),'command':[sys.executable,'-B',str(pathlib.Path(__file__).resolve()),*sys.argv[1:]],'runtime':{'python':sys.version.split()[0],'sympy':sp.__version__},'inputs':[identity(a.lower),identity(a.upper),identity(a.baseline)],'trusted_dependencies':'Sympy QQ(sqrt2) exact domain arithmetic/elimination; Python exact rational/integer comparison; positive sqrt2 embedding independently sign-checked','scope':'n3 only; D7/full36monomials/10nodes/fullR2balls; no n4-8/G3trend/U2 status'}
 try:
  lower=json.loads(pathlib.Path(a.lower).read_text());upper=json.loads(pathlib.Path(a.upper).read_text());poly,base=baseline(a.baseline);z=nodes();J,B,rank=jet_and_kernel(z)
  need(rank+B.shape[0]==36,'rank-nullity failure');lo=lower_check(lower,z,poly);up=upper_check(upper,z,B);bad=controls(lower,upper,z,poly,J,B,rank)
  basis={'monomials':MON,'nodes':[[encode(x),encode(y)]for x,y in z],'J_shape':J.shape,'J_rank':rank,'kernel_rows':[[encode(x)for x in row]for row in B.to_list()]};bp=out/'independent-kernel.json';bp.write_text(json.dumps(basis,separators=(',',':'))+'\n')
  receipt.update(status='PASS independent exact n3 lower/full-kernel upper checks',jet_matrix_shape=[30,36],jet_rank=rank,full_kernel_dimension=B.shape[0],kernel_identity='J*B^T=0 and rank(B)=36-rank(J), exact',kernel_artifact=identity(bp),lower=lo,upper=up,malformed_controls=bad,positive_control_after_mutations='PASS original lower and upper rechecked')
 except Exception as e:receipt.update(status='INCOMPLETE_OR_REJECTED',error=repr(e))
 finally:
  signal.alarm(0);receipt['elapsed_seconds']=time.monotonic()-start;pathlib.Path(a.receipt).write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt,indent=2))
 return 0 if receipt['status'].startswith('PASS') else 1
if __name__=='__main__':sys.exit(main())
