#!/usr/bin/env python3
"""Frozen actual binary64 n1 scalar contract; pre-execution review required."""
import argparse,base64,hashlib,itertools,json,math,pathlib,platform,resource,signal,struct,sys,time,zlib
from fractions import Fraction as F

TRACE={'primitives':[],'states':[]}
def word(x):return struct.pack('>d',x).hex()
def bits(x):return int(word(x),16)
def frac(x):return F(*x.as_integer_ratio())
def enc(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,list):return [enc(v)for v in x]
 if isinstance(x,dict):return {str(k):enc(v)for k,v in x.items()}
 return x
def state(label,x):
 def words(v):return [words(t)for t in v]if isinstance(v,list)else word(v)
 TRACE['states'].append({'label':label,'words':words(x)})
def zero_sign(op,args,target):
 if target:return target<0
 neg=lambda v:bool(bits(v)>>63)
 if op=='sqrt':return neg(args[0])
 if op in ('mul','div'):return neg(args[0])!=neg(args[1])
 if args[0]==0 and args[1]==0:
  return neg(args[0]) and (neg(args[1])if op=='add'else not neg(args[1]))
 return False

def rounded(op,*args):
 # Every host expression contains exactly one requested primitive operation.
 if op=='add':out=args[0]+args[1];target=frac(args[0])+frac(args[1])
 elif op=='sub':out=args[0]-args[1];target=frac(args[0])-frac(args[1])
 elif op=='mul':out=args[0]*args[1];target=frac(args[0])*frac(args[1])
 elif op=='div':out=args[0]/args[1];target=frac(args[0])/frac(args[1])
 elif op=='sqrt':out=math.sqrt(args[0]);target=frac(args[0])
 else:raise ValueError('unknown primitive')
 assert math.isfinite(out) and all(math.isfinite(x)for x in args)
 even=(bits(out)&1)==0
 prev,nxt=math.nextafter(out,-math.inf),math.nextafter(out,math.inf)
 assert math.isfinite(prev) and math.isfinite(nxt)
 midlo=(frac(prev)+frac(out))/2;midhi=(frac(out)+frac(nxt))/2
 if op=='sqrt':
  assert target>=0 and out>=0
  assert midlo<0 or target>midlo*midlo or (even and target==midlo*midlo)
  assert target<midhi*midhi or (even and target==midhi*midhi)
 else:
  assert target>midlo or (even and target==midlo)
  assert target<midhi or (even and target==midhi)
 if out==0:assert bool(bits(out)>>63)==zero_sign(op,args,target)
 TRACE['primitives'].append({'seq':len(TRACE['primitives']),'op':op,'args':[word(x)for x in args],'out':word(out),'exact':str(target),'RN':True,'subnormal':((bits(out)>>52)&2047)==0 and bool(bits(out)&((1<<52)-1))})
 return out

def dot(v,w):
 s=0.0
 for r in range(3):
  p=rounded('mul',v[r],w[r]);s=rounded('add',s,p)
 return s

def prod(diag,q,label):
 v=[rounded('mul',diag[r],q[r])for r in range(3)];state(label,v);return v

def cgs(v,qs,label):
 state(label+'.input',v);passes=[]
 for ipass in range(2):
  b=[dot(q,v)for q in qs] # all dots use same unchanged v
  w=[]
  for r in range(3):
   s=0.0
   for i in range(len(qs)):
    p=rounded('mul',qs[i][r],b[i]);s=rounded('add',s,p)
   w.append(rounded('sub',v[r],s))
  state(label+'.b'+str(ipass+1),b);state(label+'.w'+str(ipass+1),w)
  passes.append(b);v=w
 h=[rounded('add',passes[0][i],passes[1][i])for i in range(len(qs))]
 state(label+'.h',h);return v,h

def normalize(v,label):
 beta=rounded('sqrt',dot(v,v));assert math.isfinite(beta)and beta>0
 q=[rounded('div',x,beta)for x in v];state(label+'.beta',beta);state(label+'.q',q)
 return q,beta

def transpose(a):return [list(row)for row in zip(*a)]
def mm(a,b):return [[sum((x*y for x,y in zip(row,col)),F(0))for col in zip(*b)]for row in a]
def sub(a,b):return [[x-y for x,y in zip(ar,br)]for ar,br in zip(a,b)]
def mv(a,v):return [sum((x*y for x,y in zip(row,v)),F(0))for row in a]
def det(a):
 return a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])-a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])+a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0])
def sqrtenclose(q):
 assert q>=0
 scale=1<<192;n=math.isqrt(q.numerator*scale*scale//q.denominator);lo=F(n,scale)
 hi=lo if lo*lo==q else F(n+1,scale)
 assert lo*lo<=q<=hi*hi
 return [lo,hi]
def normbounds(a):
 col=[sqrtenclose(sum((x*x for x in c),F(0)))for c in zip(*a)]
 upper=sqrtenclose(sum((x*x for row in a for x in row),F(0)))[1]
 return {'spectral':[max(v[0]for v in col),upper],'column_euclidean':col,'upper_method':'Frobenius; lower=max column Euclidean lower bound'}
def consistency(hx,hy,beta1,beta2):
 witness=[]
 for label,h in [('Hx',hx),('Hy',hy)]:
  for i in range(3):
   for j in range(i+1,3):
    if h[i][j]!=h[j][i]:witness.append({'matrix':label,'i':i,'j':j,'exact_difference':h[i][j]-h[j][i]})
 comm=sub(mm(hx,hy),mm(hy,hx))
 pattern=(beta1>0 and beta2>0 and hy[2][0]==0 and hy[1][0]>0 and hx[2][0]>0)
 interior=all(comm[0][i]==0 and comm[i][0]==0 for i in range(3))
 out={'symmetry':not witness,'asymmetry_witnesses':witness,'positive_pivots_and_n1_pattern':pattern,'interior_commutator_row_col0_zero':interior,'commutator':comm}
 if witness or not pattern or not interior:
  out['status']='INCONSISTENT raw exact data; STOP';return out
 moments={}
 for degree in range(4):
  for letters in itertools.product('xy',repeat=degree):
   v=[F(1),F(0),F(0)]
   for letter in reversed(letters):v=mv(hx if letter=='x'else hy,v)
   key=(letters.count('x'),letters.count('y'))
   if key in moments:assert moments[key]==v[0]
   moments[key]=v[0]
 assert len(moments)==10 and moments[0,0]==1
 mon=[(0,0),(0,1),(1,0)]
 momentmatrix=lambda dx,dy:[[moments[a+c+dx,b+d+dy]for c,d in mon]for a,b in mon]
 M=momentmatrix(0,0);minors=[M[0][0],M[0][0]*M[1][1]-M[0][1]*M[1][0],det(M)]
 assert all(x>0 for x in minors)
 V=transpose([[F(1),F(0),F(0)],[hy[i][0]for i in range(3)],[hx[i][0]for i in range(3)]])
 assert mm(transpose(V),V)==M
 assert mm(mm(transpose(V),hx),V)==momentmatrix(1,0)
 assert mm(mm(transpose(V),hy),V)==momentmatrix(0,1)
 out.update(status='CONSISTENT exact mass-one section data',moments={str(k):v for k,v in moments.items()},moment_leading_minors=minors)
 return out

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--out',required=True);a=ap.parse_args()
 out=pathlib.Path(a.out);out.mkdir(parents=True,exist_ok=False);start=time.monotonic()
 resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2))
 def expire(*_):raise TimeoutError('55s internal cap')
 signal.signal(signal.SIGALRM,expire);signal.alarm(55)
 receipt={'status':'RUNNING','source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),'command':[sys.executable,*sys.argv],'runtime':{'python':sys.version,'platform':platform.platform(),'float_info':str(sys.float_info),'float_rounds':sys.float_info.rounds},'scope':'one frozen n1 binary64 mirror(1,y,x); no correction/model search or general G claim'}
 try:
  assert sys.float_info.radix==2 and sys.float_info.mant_dig==53 and sys.float_info.max_exp==1024 and sys.float_info.rounds==1
  X=[0.0,1.0,0.0];Y=[0.0,0.0,1.0];state('Xdiag',X);state('Ydiag',Y)
  s=rounded('sqrt',3.0);a0=rounded('div',1.0,s);q0=[a0,a0,a0];state('startup.s',s);state('q0',q0)
  v,g=cgs(prod(Y,q0,'Yq0'),[q0],'q1.cgs');q1,beta1=normalize(v,'q1');g0=g[0]
  v,h=cgs(prod(X,q0,'Xq0'),[q0,q1],'q2.cgs');q2,beta2=normalize(v,'q2');h0,h1=h
  qs=[q0,q1,q2];columns=[[h0,h1,beta2]];terminals={}
  for j in [1,2]:
   terminal,coeff=cgs(prod(X,qs[j],'Xq'+str(j)),qs,'Xcol'+str(j));columns.append(coeff);terminals['X'+str(j)]=terminal
  terminal,j1=cgs(prod(Y,q1,'Yq1'),qs,'Ycol1');terminals['Y1']=terminal
  j0=[g0,beta1,0.0];Hx=transpose(columns);Q=transpose(qs)
  state('Q',Q);state('Hx',Hx);state('j0',j0);state('j1',j1)
  receipt['raw_words']={'Q':[[word(v)for v in row]for row in Q],'Hx':[[word(v)for v in row]for row in Hx],'j0':[word(v)for v in j0],'j1':[word(v)for v in j1],'terminals':{k:[word(v)for v in val]for k,val in terminals.items()},'stored_D_scalars':14}
  qr=[[frac(v)for v in row]for row in Q];hx=[[frac(v)for v in row]for row in Hx];j0r=list(map(frac,j0));j1r=list(map(frac,j1));h0r,h1r,b2=map(frac,[h0,h1,beta2])
  temp=mv(hx,j0r);j2=[(temp[i]-h0r*j0r[i]-h1r*j1r[i])/b2 for i in range(3)];hy=transpose([j0r,j1r,j2])
  ident=[[F(int(i==j))for j in range(3)]for i in range(3)];gram=sub(mm(transpose(qr),qr),ident);detq=det(qr);assert detq
  fx=sub([[F(int(i==1))*v for v in row]for i,row in enumerate(qr)],mm(qr,hx));fy=sub([[F(int(i==2))*v for v in row]for i,row in enumerate(qr)],mm(qr,hy))
  gn=normbounds(gram);xn=normbounds(fx);yn=normbounds(fy);eta=gn['spectral'][1];assert eta<1
  qnorm=[sqrtenclose(1-eta)[0],sqrtenclose(1+eta)[1]];sigma=[sqrtenclose(1-eta)[0],sqrtenclose(1+eta)[1]]
  budget=F(64,2**53)
  def gate(norm):
   return 'PASS'if norm[1]<=budget*qnorm[0]else('FAIL'if norm[0]>budget*qnorm[1]else'UNRESOLVED')
  checks=consistency(hx,hy,frac(beta1),b2)
  analysis={'Q':qr,'raw_Hx':hx,'raw_j0':j0r,'raw_j1':j1r,'C1_j2':j2,'completed_Hy':hy,'Gram_loss':gram,'detQ':detq,'Fx':fx,'Fy':fy,'omitted_Y_column':[row[2]for row in fy],'consistency':checks}
  (out/'analysis.json').write_text(json.dumps(enc(analysis),indent=2)+'\n')
  receipt.update(status='FROZEN n1 actual run completed; independent verification PENDING',norm_bounds=enc({'Gram_loss':gn,'Q_spectral':qnorm,'sigma_min_Q':sigma,'Fx':xn,'Fy':yn,'omitted_Y_column':yn['column_euclidean'][2]}),budget_gates={'Gram_loss_le_half':'PASS'if eta<=F(1,2)else'UNRESOLVED','Fx_le_64u_normQ':gate(xn['spectral']),'Fy_le_64u_normQ':gate(yn['spectral'])},invertibility='PASS exact nonzero detQ',consistency_status=checks['status'],symmetry_witnesses=enc(checks['asymmetry_witnesses']),C1_j2=enc(j2),completed_Hy=enc(hy))
 except Exception as e:receipt.update(status='INVALID_OR_CAP',error=repr(e))
 finally:
  signal.alarm(0);raw=json.dumps(TRACE,separators=(',',':')).encode();(out/'trace.json').write_bytes(raw)
  packed={'encoding':'zlib-compressed UTF8 JSON, base64','uncompressed_sha256':hashlib.sha256(raw).hexdigest(),'uncompressed_bytes':len(raw),'data':base64.b64encode(zlib.compress(raw,9)).decode()};(out/'trace-packed.json').write_text(json.dumps(packed,separators=(',',':'))+'\n')
  receipt['trace']={'primitive_count':len(TRACE['primitives']),'state_count':len(TRACE['states']),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw)}
  receipt['elapsed_seconds']=time.monotonic()-start;receipt['peak_rss_KiB']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
  (out/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt,indent=2))
if __name__=='__main__':main()
