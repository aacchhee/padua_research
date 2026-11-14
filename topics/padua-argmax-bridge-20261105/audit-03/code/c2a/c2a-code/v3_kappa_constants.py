# C2A audit: kappa series (uc:kappa-series), coarse input, origin identity, scalar constants
import mpmath as mp
from fractions import Fraction as Fr
mp.mp.dps = 40
pi = mp.pi; g_ = mp.euler; z = mp.zeta
K = 64
a = [mp.mpf(1)] + [1-2*mp.fsum(z(2*r)/4**r for r in range(1, p+1)) for p in range(1, K+1)]
b = [7*z(3)/8] + [(1-mp.mpf(2)**(-2*q-3))*z(2*q+3)-(1-mp.mpf(2)**(-2*q-1))*z(2*q+1) for q in range(1, K+1)]
c = [mp.fsum(a[p]*b[k-p] for p in range(k+1)) for k in range(K+1)]
kap_series = 8/pi**2*mp.fsum(c[k]/(k+1) for k in range(K+1))
tail = mp.mpf(8)/(3*(K+2)*4**(K+1))
oddsum = lambda t: mp.nsum(lambda j: 1/((2*j+1)*((2*j+1)**2-t**2)), [0, mp.inf])
mp.mp.dps = 25
kap_int = 8/pi*mp.quad(lambda t: t**2*mp.cot(pi*t/2)*oddsum(t), [0, 0.5, 1])
mp.mp.dps = 40
print('kappa series K=64:', mp.nstr(kap_series, 25), ' tail radius', mp.nstr(tail, 5))
print('kappa integral   :', mp.nstr(kap_int, 20))
print('a_p checks 0<a_p<=4^-p:', all(0 < a[p] <= mp.mpf(4)**(-p) for p in range(K+1)), ' b0<10/9', b[0] < mp.mpf(10)/9, ' |b_q|<9^-q:', all(abs(b[q]) < mp.mpf(9)**(-q) for q in range(1, K+1)), ' |c_k|<2*4^-k:', all(abs(c[k]) < 2*mp.mpf(4)**(-k) for k in range(K+1)))
# actual tail magnitude
cfull = None
kap = kap_series
G = g_+mp.log(8/pi)
Cstar = 4*G**2/pi**2 + kap
print('9/10<kappa<23/25:', 0.9 < kap < 0.92, ' C*=', mp.nstr(Cstar, 15), ' <1847/1000:', Cstar < mp.mpf(1847)/1000)
k0 = 2*g_+4*mp.log(2)-2*mp.log(pi)
H0_id = kap/2 + 2*k0/pi**2*mp.log(2/pi)
print('H0 from origin identity:', mp.nstr(H0_id, 15), ' (direct finite-part computation in v2: 0.310002264407)')
C0 = 2*g_+4*mp.log(2); bst = C0-mp.mpf(7)/2; B = C0**2/pi**2; d0 = C0*bst/pi**2; v0 = 7*bst/(2*pi**2)
g0 = 4*(mp.log(pi)**2-mp.log(2)**2)/pi**2; j = H0_id+d0-g0; t0 = 2*mp.log(2)/pi
print('C*=B-g0+2H0 check:', mp.nstr(B-g0+2*H0_id-Cstar, 5))
for name, val, lo, hi in [('H0', H0_id, Fr(7, 25), Fr(1633, 5125)), ('d0', d0, Fr(39, 250), None), ('g0', g0, None, Fr(43, 125)), ('j', j, Fr(23, 250), None), ('t0', t0, 0, Fr(221, 500)), ('b*', bst, Fr(2, 5), None), ('C0', C0, Fr(39, 10), None), ('k0', k0, Fr(161, 100), Fr(9, 5)), ('v0', v0, None, None)]:
    ok = (lo is None or val > mp.mpf(lo.numerator)/lo.denominator) and (hi is None or val < mp.mpf(hi.numerator)/hi.denominator)
    print('%-3s = %s  in claimed range: %s' % (name, mp.nstr(val, 12), ok))
print('H0+v0 =', mp.nstr(H0_id+v0, 10))
# rational arithmetic of the companion's displayed steps
print('9/20-828/4925 =', Fr(9, 20)-Fr(828, 4925), float(Fr(9, 20)-Fr(828, 4925)), '> 7/25:', Fr(9, 20)-Fr(828, 4925) > Fr(7, 25))
print('(18/5)(23/50)(20/197) =', Fr(18, 5)*Fr(23, 50)*Fr(20, 197))
print('23/50 - (2*161/100)(18/41)/10 =', Fr(23, 50)-Fr(2*161, 100)*Fr(18, 41)/10)
print('g0 bound (80/197)((23/20)^2-(69/100)^2) =', float(Fr(80, 197)*(Fr(23, 20)**2-Fr(69, 100)**2)), ' 43/125=', 43/125)
print('j lower 7/25+39/250-43/125 =', Fr(7, 25)+Fr(39, 250)-Fr(43, 125))
print('t0 bound 2*0.6932/(157/50) =', float(2*Fr(6932, 10000)/Fr(157, 50)), ' 221/500=', 221/500)
dl = Fr(9, 4)-Fr(1847, 1000)
print('delta=', dl, ' delta^2+delta*j_lo - (221/500)^2 =', float(dl**2+dl*Fr(23, 250)-Fr(221, 500)**2))
print('C_inf global bound C*-j/2+sqrt(j^2/4+t0^2) (actual constants) =', mp.nstr(Cstar-j/2+mp.sqrt(j**2/4+t0**2), 10))
# elementary log bounds used
print('log(25/16)=', mp.nstr(mp.log(mp.mpf(25)/16), 8), '>18/41=', 18/41, '; 2atanh(9/41) first term =', 18/41)
print('log(pi/2)=', mp.nstr(mp.log(pi/2), 8), ' <23/50')
print('2atanh(17/39) two terms', float(2*(Fr(17, 39)+Fr(17, 39)**3/3)), '> 37/40=0.925; log(28/11)=', mp.nstr(mp.log(mp.mpf(28)/11), 8))
print('2atanh(1/3) three terms', float(2*(Fr(1, 3)+Fr(1, 81)+Fr(1, 1215))), '>0.69')
print('gamma+log(8/pi)=', mp.nstr(G, 10), ' log(8/3)=', mp.nstr(mp.log(mp.mpf(8)/3), 8))
print('b_c=8G/pi^2=', mp.nstr(8*G/pi**2, 10), ' 79/(5pi^2)=', mp.nstr(mp.mpf(79)/(5*pi**2), 10))
print('zeta(3)<=1+1/8+1/27+1/18 =', float(1+Fr(1, 8)+Fr(1, 27)+Fr(1, 18)))
print('sum_{l>=3 odd} 1/(l(l^2-1)) =', mp.nstr(mp.nsum(lambda j: 1/((2*j+1)*((2*j+1)**2-1)), [1, mp.inf]), 12), ' 3/4-log2=', mp.nstr(mp.mpf(3)/4-mp.log(2), 12))
print('(32/pi^2)(7/4-log2)=', mp.nstr(32/pi**2*(mp.mpf(7)/4-mp.log(2)), 10))
print('I4=', mp.nstr(mp.quad(lambda t: mp.sqrt(1-t**4), [0, 1]), 10), ' 319/360=', 319/360)
print('coefficients 4I4/(pi^2 sqrt a): rho<=1/2 ->', float(4*Fr(319, 360)*Fr(20, 197)*Fr(30, 29)), ' rho<=1 ->', float(4*Fr(319, 360)*Fr(20, 197)*Fr(8, 7)))
print('1679/8000 check', Fr(23, 24)*(Fr(69, 100)+Fr(3, 2))/10)
