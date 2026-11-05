#!/usr/bin/env python3
"""Independent targeted diagnostics; all-degree claim rests on analytic review."""
from pathlib import Path
from fractions import Fraction as Q
import hashlib, json, platform, time
import mpmath as mp
ROOT=Path(__file__).resolve().parents[3]
TOPIC=Path(__file__).resolve().parents[1]
PINS={
 'theory/N5-all-edge-defect.md':'1c1492b50b9ab89b9a94d88a01caccc889d4547df677210152b91521a2df6fda',
 'code/n5_all_edge_defect.py':'81ebfb554c297fd444ca2bfa8e6c50459538a3e81949fa32543532a220922381',
 'evidence/n5-all-edge-defect.json':'5a3697a540fda6dd096d3e971714f70bddbae9078ebb9de8d219a902e72ac471'}
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def pins():
 for p,h in PINS.items(): assert sha(TOPIC/p)==h

def divided_polynomial(x,y,n):
 # [T_(n+1)(y)+T_n(y)-T_(n+1)(x)-T_n(x)]/(y-x),
 # computed as a finite recurrence with NO division, valid also at x=y.
 # d_(k+1)=2*y*d_k+2*T_k(x)-d_(k-1).
 tx0,tx1=mp.mpf(1),x
 d0,d1=mp.mpf(0),mp.mpf(1)
 for k in range(1,n+1):
  d2=2*y*d1+2*tx1-d0
  tx0,tx1=tx1,2*x*tx1-tx0
  d0,d1=d1,d2
 return d0+d1

def case(n,ep,q,s):
 m=n+1;J=0 if ep==1 else n;s=mp.mpf(s);phi=(q*mp.pi+s)/m
 assert ep**n*(-1)**q==-1 and 1<=q<=m-1
 a=min(q,m-q);pairs=[];gamma=min(phi,mp.pi-phi)
 if a<=4:
  top=q>m/2;eta=a%2 if top else 1-a%2
  pairs=[(n-l if top else l,l+eta) for l in range(1,n) if Q(3*n,8)<=l<=Q(n,2)]
  assert len(pairs)>=Q(n,16)
  category='near';floor=mp.mpf(1)/864;numfloor=mp.mpf(1)/8
 else:
  assert gamma>4*mp.pi/n
  # Compare before division to identify the EXACT transition at q=m/6,s=0.
  distance_numerator=min(q*mp.pi+s,(m-q)*mp.pi-s)
  small=(distance_numerator<=m*mp.pi/6)
  category='small' if small else 'middle';numfloor=mp.mpf(7)/32
  floor=7/(768*mp.pi) if small else mp.mpf(7)/6144
  counts=[]
  for k in range(1,m):
   bp=(k if phi<=mp.pi/2 else m-k)*mp.pi/m
   if not ((mp.pi/3<=bp<=mp.pi/2) if small else (mp.pi/12<=bp<=mp.pi/6)): continue
   low,high=(bp-gamma/2,bp+gamma/2) if small else (gamma-bp/2,gamma+bp/2)
   row=[(r,k) for r in range(1,n) if (r+k-J)%2==0 and low<=r*mp.pi/n<=high]
   assert len(row)>= (n*gamma/(4*mp.pi) if small else mp.mpf(n)/48)
   counts.append(len(row));pairs+=row
  assert len(counts)>= (mp.mpf(m)/12 if small else mp.mpf(m)/16)
 total=mp.mpf(0);error=mp.mpf(0);minnum=mp.inf
 for r,k in pairs:
  j=r if ep==1 else n-r
  assert (j+k)%2==0 and 0<j<n and 0<k<m
  x=mp.cos(r*mp.pi/n);halves=[];denoms=[]
  for sign in [-1,1]:
   v=phi+sign*k*mp.pi/m;y=mp.cos(v)
   numerator=mp.cos(s/2)**2*(1+y)+mp.sin(s)*mp.sin(v)/2
   denom=x-y;assert abs(denom)>mp.mpf('1e-80')
   h=(((-1)**r)*divided_polynomial(x,y,n)-1)/2
   assert numerator>=numfloor-mp.mpf('1e-80')
   error=max(error,abs(h-numerator/denom));minnum=min(minnum,numerator)
   halves.append(h);denoms.append(denom)
  assert denoms[0]*denoms[1]<0 and halves[0]*halves[1]<0
  total+=2/(mp.mpf(n)*m)*(abs(halves[0])+abs(halves[1])-abs(sum(halves)))
 assert total>=floor and error<mp.mpf('1e-75')
 return dict(n=n,endpoint=ep,q=q,s=str(s),category=category,selected_pairs=len(pairs),selected_defect=mp.nstr(total,30),case_floor=mp.nstr(floor,30),ratio=mp.nstr(total/floor,30),minimum_numerator=mp.nstr(minnum,30),polynomial_quotient_error=mp.nstr(error,10))

def main():
 pins();started=time.process_time();mp.mp.dps=100
 assert Q(3*64,40)-Q(43,10)==Q(1,2)
 assert Q(64,10)-Q(22,5)==2
 assert Q(3,8)*3>Q(1,2) and 8*Q(22,7)+1<27
 assert Q(11,5)**2<5 and Q(7,20)<Q(9,25)
 assert Q(15,16)*Q(2,5)-Q(1,4)==Q(1,8)
 assert Q(15,32)-Q(1,4)==Q(7,32)
 assert Q(1,864)>Q(1,1024) and Q(7,768*4)>Q(1,1024) and Q(7,6144)>Q(1,1024)
 assert Q(7,576)+Q(112,225)==Q(66087,129600)<1
 inputs=[(n,e,q,s) for n,e,q in [(64,1,1),(64,-1,63),(65,1,1),(65,1,65),(65,-1,2),(65,-1,64),(65,-1,4),(65,1,5)] for s in ['-0.5','0.5']]
 inputs += [(65,1,q,s) for q in [11,55] for s in ['-0.5','0','0.5']]+[(65,1,33,'0')]
 rows=[case(*args) for args in inputs]
 pins()
 result=dict(status='PASS analytic constants and targeted MEASURED diagnostics; not interval proof',precision_decimal_digits=100,independent_formula='Finite divided-Chebyshev recurrence, no developer imports; selected physical points only',cases=len(rows),rows=rows,category_counts={s:sum(r['category']==s for r in rows) for s in ['near','small','middle']},minimum_ratio=min((r['ratio'] for r in rows),key=mp.mpf),maximum_polynomial_quotient_error=max((r['polynomial_quotient_error'] for r in rows),key=mp.mpf),pins=PINS,checker_sha256=sha(Path(__file__)),command='python topics/padua-argmax-bridge-20261105/code/check_n5_all_edge.py',python=platform.python_version(),mpmath=mp.__version__,cpu_seconds_diagnostic=time.process_time()-started,scope='Independent supplement, not required Claude audit; no global maximum, E-C or model-maximum claim')
 target=TOPIC/'evidence/independent-n5-all-edge.json';target.write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({k:result[k] for k in ['status','cases','category_counts','minimum_ratio','maximum_polynomial_quotient_error']},indent=2));print('receipt_sha256',sha(target))
if __name__=='__main__': main()
