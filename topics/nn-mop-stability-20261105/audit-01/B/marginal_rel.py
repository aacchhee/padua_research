# Auditor B: componentwise relative marginal errors (alpha_k, k>=1; beta_k where nonzero)
import sys, mpmath as mp
sys.path.insert(0,'/home/user/padua_research/topics/nn-mop-stability-20261105/code')
import stage_isolation as si
base=si.base
mp.mp.dps=220
for fam in ('krawtchouk','hahn'):
    for N in (4,8,12,16,24,32):
        x,w=base.inputs(N,fam)
        xx=[base.convert(v,float) for v in x]; ww=[[base.convert(v,float) for v in r] for r in w]
        rx=list(map(mp.mpf,xx)); rw=[list(map(mp.mpf,r)) for r in ww]
        res={}
        for name in ('stieltjes','lanczos'):
            worst_a=worst_b=mp.mpf(0); worst_abs=mp.mpf(0)
            for row,rrow in zip(ww,rw):
                hb,ha=base.marginal(rx,rrow)
                if name=='lanczos': (b,a),_=si.lanczos(xx,row)
                else: b,a=base.marginal(xx,row)
                for k in range(1,N): worst_a=max(worst_a,abs(mp.mpf(a[k])-ha[k])/abs(ha[k]))
                for k in range(N):
                    if abs(hb[k])>mp.mpf(10)**-100: worst_b=max(worst_b,abs(mp.mpf(b[k])-hb[k])/abs(hb[k]))
                    worst_abs=max(worst_abs,abs(mp.mpf(b[k])-hb[k]))
            res[name]='rel_alpha/u=%.3g rel_beta(nonzero)/u=%.3g abs_beta/u=%.3g'%(float(worst_a/2**-53),float(worst_b/2**-53),float(worst_abs/2**-53))
        print(fam,N,res)
