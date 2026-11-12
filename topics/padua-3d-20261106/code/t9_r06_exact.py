#!/usr/bin/env python3
"""Exact arithmetic checks accompanying hand proofs; not a density proof."""
import argparse,hashlib,itertools as it,json,math,platform,sys
from fractions import Fraction as F
from pathlib import Path
import sympy as s

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args()
 B=s.Matrix([[2,-1,-3],[3,-2,1],[1,3,-2]])/3
 n=s.symbols('n',integer=True);f=n**3-108*n**2-198*n-108
 threshold={'109':int(f.subs(n,109)),'110':int(f.subs(n,110)),'difference':str(s.expand(f.subs(n,n+1)-f))}
 sums=[]
 for q in range(17):
  left=sum((i+1)**2*(j+1)**2*(k+1)**2 for i in range(q+1) for j in range(q-i+1) for k in range(q-i-j+1))
  right=sum(math.comb(3,j)*math.comb(q-j+9,9) for j in range(min(3,q)+1));assert left==right
  sums.append([q,left])
 eps=[e for e in it.product((-1,1),repeat=3) if math.prod(e)==1];tetra=[]
 for t in [F(1),F(1,2),F(1,3),F(1,4),F(1,100)]:
  maximum=max(sum(abs((1+e[0]*F(x)/t+e[1]*y+e[2]*z)/4) for e in eps) for x,y,z in it.product((-1,1),repeat=3))
  assert maximum==max(1/t,(1/t+3)/2);tetra.append({'t':str(t),'Lambda':str(maximum)})
 # Reflection invariance of the sign-orbit factor multiset for all support sizes.
 for d in (1,2,3):
  canon=lambda e:e if e[0]==1 else tuple(-v for v in e)
  reps={canon(e) for e in it.product((-1,1),repeat=d)}
  for j in range(d):assert {canon(tuple(-v if i==j else v for i,v in enumerate(e))) for e in reps}==reps
 # The relevant Padua annihilator degree is above interpolation/exactness cutoffs.
 padua=[{'n':q,'shortest_dual_l1':2*q,'minimum_annihilator_degree':2*q,'mixed_dual_l1':2*q+1,'mixed_annihilator_degree':2*(2*q+1)} for q in range(1,17)]
 z=s.symbols('z');witnesses=[]
 for q,g,k in [(6,[1,2,3],[1,1,1]),(20,[1,2,5],[3,1,-1]),(21,[1,4,7],[3,1,-1])]:
  assert sum(a*b for a,b in zip(g,k))%q==0
  modes=sorted([(abs(a),b) for a,b in zip(k,g)],reverse=True)
  u,v,w=[(z**((a*b)%q)+z**((-a*b)%q))/2 for a,b in modes]
  remainder=s.rem(s.Poly(s.expand(1-v*v-w*w+2*u*v*w-u*u),z),s.Poly(s.cyclotomic_poly(q,z),z))
  assert remainder.is_zero
  r=sum(map(abs,k));assert max(2*modes[1][0],2*modes[2][0],r)==r
  witnesses.append({'q':q,'g':g,'k':k,'witness_degree':r,'cyclotomic_remainder_zero':True,'integral':'0','identity_value':'1'})
 out={'status':'EXACT arithmetic checks; hand proofs and imported density are separate','command':sys.argv,'versions':{'python':platform.python_version(),'sympy':s.__version__},'seed':0,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'critical_basis_signed_det':str(B.det()),'critical_basis_covolume':str(abs(B.det())),'density':str(F(4,3)/F(abs(B.det()))),'threshold':threshold,'rleja_sum':sums,'tetrahedron':tetra,'sign_orbit_reflection_checked_supports':[1,2,3],'Padua_compatibility':padua,'positive_weight_witnesses':witnesses}
 a.output.write_text(json.dumps(out,separators=(',',':'))+'\n')
if __name__=='__main__':main()
