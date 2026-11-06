import sys; sys.path.insert(0, '.')
import mpmath as mp
from fractions import Fraction as Fr
from indep_nn import *
mp.mp.dps = 60
for (p1, p2) in [(Fr(2,5), Fr(1,2)), (Fr(1,5), Fr(2,5)), (Fr(3,5), Fr(4,5))]:
    for N in (3, 4, 5, 6, 7):
        M = N-1
        q = inputs(N, 'krawtchouk', p1, p2)
        out, P = nn_map(*q)
        # support polynomial check
        err_supp = mp.mpf(0)
        for n in range(N+1):
            poly = P[(n, N-n)]
            for xl in q[0]:
                err_supp = max(err_supp, abs(sum(c*xl**j for j, c in enumerate(poly))))
        err = mp.mpf(0)
        q1, q2 = p1*(1-p1), p2*(1-p2)
        for t in range(M+1):
            for n in range(t+1):
                m = t-n
                for j, pj in ((1, p1), (2, p2)):
                    B = pj*(M-t)+(1-p1)*n+(1-p2)*m
                    err = max(err, abs(out[('b%d'%j, (n,m))] - (mp.mpf(2*B.numerator)/B.denominator/M - 1)))
                if n >= 1:
                    A1 = n*q1*(M-t+1)*Fr(4, M*M)
                    err = max(err, abs(out[('a1',(n,m))] - mp.mpf(A1.numerator)/A1.denominator))
                if m >= 1:
                    A2 = m*q2*(M-t+1)*Fr(4, M*M)
                    err = max(err, abs(out[('a2',(n,m))] - mp.mpf(A2.numerator)/A2.denominator))
        print(str(p1), str(p2), N, 'coef-formula err', mp.nstr(err, 3), 'support err', mp.nstr(err_supp, 3),
              'resid', mp.nstr(out['_resid'], 3), 'a-consistency', mp.nstr(out.get('_aconsist', 0), 3))
