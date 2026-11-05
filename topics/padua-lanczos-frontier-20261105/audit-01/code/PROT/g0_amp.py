import json, math, sys
R='/home/user/padua_research/topics/padua-lanczos-frontier-20261105/evidence/'
a=json.load(open(R+'g0-attribution.json'))
ind=json.load(open(R+'g0-independent.json'))
probes=json.load(open(R+'g0-kernel-probes.json'))
u=2.0**-53
hist={m:v['historical_gap'] for m,v in ind['runs']['baseline']['methods'].items()}
# certified T24 n12 squared capacity endpoints (PD-T139 / e1-summary.md, rounded)
cap={'yx':(2.0493879359e14,1.0859728745e16),'alt':(1.9412657630e10,3.3992362099e11)}
print('u=',u)
for k in ('Haswell','Nehalem'):
    for m in ('xy','yx','alt'):
        c=a['cases'][k][m]
        rel=c['normalized_source_fro']; fro=c['local_residual_fro']; ne=c['normal_error']
        hk={'xy':'upstream_xy','yx':'upstream_yx','alt':'alt'}[m]
        line=f"{k:8s} {m:4s} maxres/u={c['max_local_residual']/u:.3f} |F|_F={fro:.3e} rel={rel:.3e} gap={ne:.4e} amp_rel={ne/rel:.4e} amp_fro={ne/fro:.4e} hist={hist[hk]:.4e} need_rel={hist[hk]/rel:.4e}"
        if m in cap:
            Kl=math.sqrt(cap[m][0]); Ku=math.sqrt(cap[m][1])
            line+=f" Kcert=[{Kl:.3e},{Ku:.3e}] need/Klow={hist[hk]/rel/Kl:.3e} realized/Klow={ne/rel/Kl:.3e} Klow*rel={Kl*rel:.3e}"
        print(line)
# differences
print('dev hist-current', hist['dev']-2.7558694937e-10, (2.7558694937e-10-hist['dev'])/hist['dev'])
print('alt hist-current', hist['alt']-1.3027152070e-12)
print(json.dumps(probes,indent=0)[:2500])
