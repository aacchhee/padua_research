"""Supplementary finite O-Lt audit; no imports from developer modules."""
import gzip, hashlib, json, math
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
p=ROOT/'topics/padua-argmax-alln-20261101'
base=ROOT/'topics/padua-proof-attempts-2-20261101/outputs'
e=json.loads((p/'outputs/part3/pairing_screens.json').read_text())['certified_list']
c=json.loads(gzip.decompress((base/'a5_n4_certificate.json.gz').read_bytes()))
g=json.loads((base/'a5_n4_global.json').read_text())
assert c['summary']['complete'] is True and g['complete'] is True
assert len(c['interior_roots'])==13
# 24 terms instead of the developer checker's 30.
def atan_bounds(q):
 s=sum((F(1,(2*k+1)*q**(2*k+1)) if k%2==0 else -F(1,(2*k+1)*q**(2*k+1))) for k in range(24))
 return s,s+F(1,49*q**49)
u,v=atan_bounds(5); w,z=atan_bounds(239)
plo,phi=16*u-4*z,16*v-4*w
assert 3<plo<phi<F(22,7)
# Taylor degree 48, with degree-49 coefficient zero and remainder order 50.
def cos_bounds(t):
 assert 0<t<plo
 s=sum((-1)**k*t**(2*k)/math.factorial(2*k) for k in range(25))
 r=t**50/math.factorial(50)
 return s-r,s+r
roots={r['id']:r for r in c['interior_roots']}
vals={r['id']:tuple(map(F,r['enclosure'])) for r in g['interior_values']}
centers=[(j,k) for j in range(5) for k in range(6) if (j+k)%2]
groups={}; margins={}
assert {r['id'] for r in e['rows']}==set(roots)
for r in e['rows']:
 box=[tuple(map(F,a)) for a in r['qbox']]
 for axis,m in enumerate((4,5)):
  lo,hi=box[axis];xlo,xhi=map(F,roots[r['id']]['R'][axis])
  assert cos_bounds(lo*phi/m)[0]>xhi
  assert cos_bounds(hi*plo/m)[1]<xlo
 claimed=tuple(r['cell'])
 # Enumerate all 15 possible centers; demonstrate membership and exclusion.
 inside=[]
 for a in centers:
  maximum=sum(max(abs(lo-t),abs(hi-t)) for (lo,hi),t in zip(box,a))
  minimum=sum(max(lo-t,t-hi,F(0)) for (lo,hi),t in zip(box,a))
  if maximum<1:
   inside.append(a);margins[str(r['id'])]=str(1-maximum)
  else: assert minimum>1
 assert inside==[claimed]
 groups.setdefault(claimed,[]).append(r['id'])
a,b,corner=(3,2),(2,1),(4,5)
assert groups[a]==[5] and groups[b]==[6,7,11]
upper=max(vals[i][1] for i in groups[a]); lower=max(vals[i][0] for i in groups[b])
assert lower-upper>F(3161,50000) # 0.06322, exact
# Reconstruct all directed list comparisons with/without ties.
C=[(0,5),(4,5)]
def d(a,c): return sum((x-y)**2 for x,y in zip(a,c))
unique=[];ties=[]
for aa in groups:
 for bb in groups:
  if tuple(abs(x-y) for x,y in zip(aa,bb))!=(1,1):continue
  for cc in C:
   if d(bb,cc)<=d(aa,cc):continue
   if all(d(aa,cc)<=d(aa,z) and d(bb,cc)<=d(bb,z) for z in C):
    ties.append((aa,bb,cc))
    if all(z==cc or (d(aa,cc)<d(aa,z) and d(bb,cc)<d(bb,z)) for z in C):unique.append((aa,bb,cc))
assert not unique and (a,b,corner) in ties
out={'status':'PASS','method':'independent rational reconstruction,24 arctan terms,degree48 cosine Taylor','groups':{str(k):v for k,v in groups.items()},'strict_cell_margins':margins,'upper_a':str(upper),'lower_b':str(lower),'positive_reversal':str(lower-upper),'unique_closest_comparisons':len(unique),'tie_inclusive_comparisons':len(ties),'full_inherited_n4_proof_replayed':False}
print(json.dumps(out,sort_keys=True))
(p/'outputs/part3/pairing_independent_reconstruction.json').write_text(json.dumps(out,sort_keys=True)+'\n')
