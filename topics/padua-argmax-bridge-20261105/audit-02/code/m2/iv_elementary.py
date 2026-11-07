"""mpmath interval-arithmetic (iv) check of elementary scalar constants used by E06/E07/E10.
Trusted base: mpmath 1.3.0 iv outward rounding."""
from mpmath import iv
iv.dps = 30
pi = iv.pi; g = iv.euler; l2 = iv.log(2); lp = iv.log(pi)
def lt(a, b): return (a - b).b < 0  # upper endpoint of a-b negative
C0 = 2*g + 4*l2
k0 = C0 - 2*lp
lam0 = (2/pi)*iv.log(4/pi)
J = 2*(lp - g)/pi
t0 = 2*l2/pi
B = C0**2/pi**2; d0 = C0*(C0-iv.mpf(7)/2)/pi**2; v0 = 7*(C0-iv.mpf(7)/2)/(2*pi**2); g0 = (4/pi**2)*(lp**2-l2**2)
kap_lo, kap_hi = iv.mpf('0.919710118388492535099518225790'), iv.mpf('0.919710118388492535099518225791')
H0 = iv.mpf([kap_lo.a, kap_hi.b])/2 + (2*k0/pi**2)*iv.log(2/pi)
j = H0 + d0 - g0
checks = {
 "log pi > 11/10": lt(iv.mpf(11)/10, lp), "gamma < 3/5": lt(g, iv.mpf(3)/5), "C0 < 4": lt(C0, 4),
 "0<lambda0<1/(2pi)": lt(0, lam0) and lt(lam0, 1/(2*pi)), "J > 1/pi": lt(1/pi, J),
 "161/100 < k0 < 9/5": lt(iv.mpf(161)/100, k0) and lt(k0, iv.mpf(9)/5), "f0=k0/pi<72/125": lt(k0/pi, iv.mpf(72)/125),
 "t0 < 221/500": lt(t0, iv.mpf(221)/500), "g0 < 43/125": lt(g0, iv.mpf(43)/125), "d0 > 39/250": lt(iv.mpf(39)/250, d0),
 "v0 > 0": lt(0, v0), "7/25 < H0 < 8/25 (PD-T271 kappa)": lt(iv.mpf(7)/25, H0) and lt(H0, iv.mpf(8)/25),
 "j > 23/250 (PD-T271 kappa)": lt(iv.mpf(23)/250, j), "H0+v0>0": lt(0, H0+v0),
}
for k_, v_ in checks.items(): print(("PASS " if v_ else "FAIL ")+k_)
print("H0 interval:", H0, " j interval:", j, " d0:", d0, " g0:", g0)
print("SUMMARY", sum(checks.values()), "/", len(checks))
