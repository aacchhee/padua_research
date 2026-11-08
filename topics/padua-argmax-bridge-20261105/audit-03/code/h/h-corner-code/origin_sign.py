# MEASURED side observation: F03's E_n(0)=Lambda_c-A_n^2-kappa (A_n with log n) at sampled n.
import sys, mpmath as mp
from analyze import parse, A, kap, a, d
data={}
for fn in sys.argv[1:]:
    for n,v in parse(fn).items(): data.setdefault(n,v)
for n in sorted(data):
    if n in (2,10,40,64,100,101,200,201,1600,1601,204800,204801):
        L=data[n][0][0]; E=L-A(n)**2-kap
        print(n, mp.nstr(E,10), " n*E=",mp.nstr(n*E,8), " a^2(log n+d)-1=", mp.nstr(a**2*(mp.log(n)+d)-1,8))
