# Compare independent binary64 evaluator against every committed native outward upper/lower
# in the sampled compact-return certificates (MEASURED comparison, not a proof).
import json, time, sys
from fractions import Fraction as F
from indep_S import S_n, lambda_phys
E='/home/user/padua_research/topics/padua-argmax-bridge-20261105/evidence/compact-return/'
out=[]
for name in ['primary-n199','fresh-n199','primary-n238','fresh-n238']:
    d=json.load(open(E+name+'.json'))
    if 'S_upper_rows' not in d:
        print(name,'keys',list(d.keys())[:20]); continue
    n=d['n']; t0=time.process_time(); worst_gap=1e9; worst_excess=-1e9
    for a,b,h in d['S_upper_rows']:
        up=float.fromhex(h); v=S_n(n,F(a),F(b))
        worst_gap=min(worst_gap, up-v); worst_excess=max(worst_excess, v-up)
    lam=[]
    for x,z,h in d['lambda_upper_rows']:
        up=float.fromhex(h); v=lambda_phys(n,F(x),F(z)); lam.append(up-v)
    lo=float.fromhex(d['origin_lower_hex']); c=S_n(n,0,0)
    dt=time.process_time()-t0
    print(f"{name}: n={n} #S={len(d['S_upper_rows'])} min(upper-indep)={worst_gap:.3e} max(indep-upper)={worst_excess:.3e} "
          f"lambda upper-indep={[f'{g:.2e}' for g in lam]} indep corner - native lower={c-lo:.3e} CPU={dt:.2f}s")
