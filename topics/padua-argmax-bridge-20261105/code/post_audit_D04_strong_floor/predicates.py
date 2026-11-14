"""Exact consumer predicates on stored binary64 endpoint rationals.
No numerical kernel, transcendental approximation or physical extrapolation.
"""
from fractions import Fraction as F
import math

def radius(box):
 assert len(box)==4 and all(math.isfinite(x) for x in box)
 al,ah,bl,bh=map(F.from_float,box)
 assert al<=ah and bl<=bh
 return max(abs(al),abs(ah))+max(abs(bl),abs(bh))

def floor_tier(n,box):
 if not isinstance(n,int) or not 2<=n<=512:raise ValueError('native degree cap')
 return F(1,32) if n>=160 and radius(box)<=F(1,2) else F(1,64) if n>=64 and radius(box)<=F(1,2) else F(0)

def center_scope(n,j,k,box):
 if not all(type(x) is int for x in (n,j,k)):return 'invalid-index'
 if not 2<=n<=512 or not 0<=j<=n or not 0<=k<=n+1 or (j+k)%2!=1:return 'invalid-index'
 al,ah,bl,bh=map(F.from_float,box);r=radius(box)
 if r>F(1,2):return 'outside-whole-box-floor-domain'
 # Since r<=.5<pi, all interior centers are physical throughout.
 # Endpoint centers have exact physical half-box cuts on their phase sign.
 possible_a=(ah>=0 if j==0 else al<=0 if j==n else True)
 possible_b=(bh>=0 if k==0 else bl<=0 if k==n+1 else True)
 if not possible_a or not possible_b:return 'no-physical-point'
 if j in (0,n) and k in (0,n+1):return 'actual-corner-separate'
 entire_a=(al>=0 if j==0 else ah<=0 if j==n else True)
 entire_b=(bl>=0 if k==0 else bh<=0 if k==n+1 else True)
 return 'noncorner-entire-box' if entire_a and entire_b else 'noncorner-physical-subset'

def h3_guard(n,box):
 a=max(abs(F.from_float(x)) for x in box[:2]);b=max(abs(F.from_float(x)) for x in box[2:])
 return a*a/(2*n*n)+b*b/(2*(n+1)**2)<=F(1,10**11*n*n)

def margins(outputs,lc,eps,local):
 # Counterfactual old-C08 analytic floor uses the SAME measured S/cu,
 # not old-N3 numerical values and not another native call.
 su,cu,defect,flag,*_=outputs;t=F.from_float(lc)-F.from_float(eps)
 s=F.from_float(su);c=F.from_float(cu);d=F.from_float(defect)
 return dict(far=float(t-s),corner=float(t-c),noncorner=float(t-s+d),
  complete_predicate=bool(s<t or ((local or c<t) and s-d<t)))
