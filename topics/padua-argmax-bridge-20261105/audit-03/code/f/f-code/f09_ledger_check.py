#!/usr/bin/env python3
"""[E] F09 checks: (i) coefficient identity -A+q(2t-1)+2d=-2p and the endpoint ledger of g
(both cases, sympy); (ii) assembly of Gamma_T's q/d coefficients from the four log
constants and B endpoints (sympy); (iii) exact finite products Q_tau[log z], Q_tau[log(pi-z)]
versus [(3/2+/-tau)log m + Alog/Dlog]/m, worst m^2*error over tau grid, m=33..4000;
(iv) Stirling remainder 0<r(x)<1/(12x) spot checks; (v) final aggregate arithmetic.
Usage: PYTHONPATH=<pylib> python3 f09_ledger_check.py
"""
import sympy as sp
from mpmath import mp, mpf, log, loggamma, pi as mpi, nstr, fabs, quad

p, q, t = sp.symbols('p q t', real=True)
# case p>=q: d=0 ; case p<q: d=q-p
for case, d, pmq_plus, mx in (('p>=q', 0, p - q, p), ('p<q', q - p, 0, q)):
    A = (sp.Rational(3, 2) - t)*pmq_plus + (sp.Rational(1, 2) + t)*(p + q + d)
    ledger = (sp.Rational(3, 2) + t)*q + (sp.Rational(3, 2) - t)*mx + (sp.Rational(5, 2) - t)*(-q) + (sp.Rational(1, 2) + t)*mx
    print(case, ": E-ledger of g == A:", sp.simplify(ledger - A) == 0, "; -A+q(2t-1)+2d == -2p:", sp.simplify(-A + q*(2*t - 1) + 2*d + 2*p) == 0)

# Gamma_T constant assembly
lg = sp.Function('lG'); lpi = sp.log(sp.pi); dd, H, w, Pc = sp.symbols('d H w Pc')
Alog = lambda tau: sp.log(2*sp.pi)/2 - lg(2 + tau) - 3*lpi
Dlog = lambda tau: sp.log(2*sp.pi)/2 - lg(2 - tau) - 3*lpi
EB = -4*dd*lpi + 2*H + (2*t - 1)*q*lpi
const = -(2*t - 1)*w - 2*Pc - EB/sp.pi + (q/sp.pi)*(Alog(t) - Alog(1 - t)) + (dd/sp.pi)*(Dlog(t) + Dlog(1 - t))
GammaT = -(2*t - 1)*w - 2*Pc + (1/sp.pi)*(-2*H + q*(lg(3 - t) - lg(2 + t) - (2*t - 1)*lpi) + dd*(sp.log(2/sp.pi) - lg(2 - t) - lg(1 + t)))
print("Gamma_T (G) equals ledger constant:", sp.simplify(sp.expand_log(sp.expand(const - GammaT), force=True)) == 0)

mp.dps = 25
def Qlog(m, tau, right=False):
    h = mpi/m
    if not right:
        s = (m - 3)*log(h) + loggamma(m - 1 + tau) - loggamma(2 + tau)
    else:
        s = (m - 3)*log(h) + loggamma(m - 1 - tau) - loggamma(2 - tau)
    return s/m - (log(mpi) - 1)

# direct sum sanity at one point
m, tau = 40, mpf('0.3'); h = mpi/m
direct = sum(log(h*(k + tau)) for k in range(2, m - 1))/m - (log(mpi) - 1)
print("finite product identity check (m=40,tau=.3):", nstr(direct - Qlog(m, tau), 5))
worst = [0, 0]
for m in list(range(33, 200)) + [250, 500, 1000, 2000, 4000]:
    for k in range(0, 21):
        tau = mpf(k)/20
        e1 = Qlog(m, tau) - ((mpf(3)/2 + tau)*log(m) + log(2*mpi)/2 - loggamma(2 + tau) - 3*log(mpi))/m
        e2 = Qlog(m, tau, True) - ((mpf(3)/2 - tau)*log(m) + log(2*mpi)/2 - loggamma(2 - tau) - 3*log(mpi))/m
        worst[0] = max(worst[0], fabs(e1)*m**2); worst[1] = max(worst[1], fabs(e2)*m**2)
print("max m^2|Q_tau[log z]-pred| =", nstr(worst[0], 6), "; max m^2|Q_tau[log(pi-z)]-pred| =", nstr(worst[1], 6), "(claimed <=10)")

for x in (mpf(1), mpf(3), mpf(31), mpf(1000)):
    r = loggamma(x) - ((x - mpf(1)/2)*log(x) - x + log(2*mpi)/2)
    print(f"  Stirling r({x}) = {nstr(r, 8)} ; 1/(12x) = {nstr(1/(12*x), 8)} ; 0<r<1/(12x): {0 < r < 1/(12*x)}")

# final aggregate: [40000(1+l)+81 l+443] <= 41000(1+l) for l>=log 33
l = sp.symbols('l', positive=True)
print("aggregate slack 41000(1+l)-[40000(1+l)+81l+443] = ", sp.simplify(41000*(1 + l) - (40000*(1 + l) + 81*l + 443)), "(>0 for l>0)")
print("120000/pi < 40000:", 120000/mpi < 40000, "; 7175*pi*(1+log(24/pi)) vs 120000:", nstr(7175*mpi*(1 + log(24/mpi)), 8))
# hole lengths sum of squares
tt = sp.symbols('tt')
ss = sp.expand((sp.Rational(3, 2) + tt)**2 + (sp.Rational(3, 2) - tt)**2 + (sp.Rational(5, 2) - tt)**2 + (sp.Rational(1, 2) + tt)**2)
print("sum of four hole lengths^2 / h^2 =", ss, "; max on [0,1] =", max(ss.subs(tt, 0), ss.subs(tt, 1), ss.subs(tt, sp.Rational(1, 2))), "(<=13 used in (H), <=25 used in (B))")
