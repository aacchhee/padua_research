#!/usr/bin/env python3
"""Scalar what-if onsets for the three C13 cases (binary64; planning only).
Uses C13's displayed formulas (23),(25),(18),p(L); 'true' margin uses the
MEASURED sampled fit 0.0126L^2+0.06 of Lambda_c-M_far at rho=1/2 diagonal."""
import math
PI=math.pi
def parts(n):
    L=math.log(n)
    inv=((763*L+86237)+((449/2)*L+1762)+(62+8*L)/3+(3002*L+32803)+4*(L+1))/n
    inv2=(7082790000+((101124/8)*(L+13)+.5)+6+(10+(20/3)*(L+1))+(2/63))/n**2
    const=(2/63)+7/50
    return inv,inv2,const
def far_margin_proof(n):
    L=math.log(n); u=191/6144; d=((16/25)*n-28000)/(n+1)
    return u*(4*L*L-3*L)/10+9/10+d-1/1000-8821/3000
def far_margin_true(n):
    L=math.log(n); return 0.0126*L*L+0.06
def onset(ok,lo=41,hi=10**9):
    # smallest N in [lo,hi] such that ok(n) holds for all sampled n>=N (geometric scan + bisection on last failure)
    ns=sorted(set([int(lo*1.01**i) for i in range(0,3000) if lo*1.01**i<=hi]))
    last_fail=None
    for n in ns:
        if not ok(n): last_fail=n
    return lo if last_fail is None else (None if last_fail==ns[-1] else ns[ns.index(last_fail)+1])
print('A current proof far onset:',onset(lambda n: far_margin_proof(n)>sum(parts(n))))
print('B proof margin, all 1/n,1/n^2 terms -> 0, constants kept:',onset(lambda n: far_margin_proof(n)>parts(n)[2]))
print('B2 proof margin, every E_far term -> 0:',onset(lambda n: far_margin_proof(n)>0))
for s1,sc in [(1,1),(1e-1,1),(1e-2,1),(1e-3,1),(1e-1,.1),(1e-2,.1),(1e-3,.1),(1e-4,.1)]:
    f=lambda n: far_margin_true(n)>s1*(parts(n)[0]+parts(n)[1])+sc*parts(n)[2]
    print(f'C true-model margin, 1/n-scale {s1:g}, const-scale {sc:g}: far onset',onset(f))
# measured true model error ~0.4 L/n: what constant c in c(L+1)/n would give onset N?
for N in [41,100,1000,10**4]:
    L=math.log(N); print(f'D far: allowed c in c(L+1)/n+0.02 at N={N}:',(far_margin_true(N)-0.02)*N/(L+1))
# near: S-Lambda_c < floor(n) with C13 (18) form
def floor(n): return 1/16 if n>=4096 else (1/32 if n>=160 else (1/64 if n>=64 else 0))
for s in [1,1e-1,1e-2,1e-3]:
    print(f'E near onset, (18) 1/n-constants scaled {s:g}:',onset(lambda n: 2/1000+1/10000+s*(11270+200*(math.log(n)+1))/n<floor(n),lo=64))
for N in [64,160,1000,4096,10**4]:
    L=math.log(N); print(f'F near: allowed K in K/n at N={N} (floor {floor(N):.4g}):',(floor(N)-0.0021)*N)
for N in [41,100,1000,10**4,10**5]:
    L=math.log(N); print(f'G corner: allowed constant K0 (now 16) at N={N}:',(47/192)*((2/5)*(L+1.5)**2-1/1000)-(L+1)/3)
