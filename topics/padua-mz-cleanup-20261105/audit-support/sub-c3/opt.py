from mpmath import mp, mpf, log, findroot, diff
mp.dps = 30
def xl(x):
    x = abs(x); return mpf(0) if x == 0 else x**2*log(x)
def C(q): return 3*xl(q)-2*xl(q+1)-2*xl(q-1)+(xl(q+2)+xl(q-2))/2
A = 4*log(2)
Jm = lambda a: (A + C(1/a))/2
Jp = lambda a: (A - C(1/a) - C(2) + (C(1/a+2)+C(1/a-2))/2)/4
fm = lambda a: 16*a*(mpf(1)/2-a)/(9*A*Jm(a))
fp = lambda a: 8*a*(mpf(1)/2-2*a)/(9*A*Jp(a))
import itertools
best = max(((fm(mpf(k)/1000), k) for k in range(1,500)))
print('neg family: value at a=1/4', fm(mpf(1)/4), ' grid best', best)
best = max(((fp(mpf(k)/1000), k) for k in range(1,250)))
print('pos family: value at a=1/8', fp(mpf(1)/8), ' grid best', best)
for a in [mpf('0.1'), mpf('0.2'), mpf('0.25'), mpf('0.3'), mpf('0.4')]:
    print('a',a,'Jm',Jm(a))
for a in [mpf('0.05'), mpf('0.1'), mpf('0.125'), mpf('0.15'), mpf('0.2')]:
    print('a',a,'Jp',Jp(a))
from mpmath import findroot, diff
am = findroot(lambda a: diff(fm, a), mpf('0.257')); print('neg argmax a', am, fm(am))
for a in [mpf('0.124'), mpf('0.1245'), mpf('0.125'), mpf('0.1255'), mpf('0.126')]:
    print('pos', a, fp(a))
ap = findroot(lambda a: diff(fp, a), mpf('0.125')); print('pos argmax a', ap, fp(ap))
