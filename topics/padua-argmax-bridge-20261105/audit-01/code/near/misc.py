from fractions import Fraction as F
import math
n=F(500000); m=n+1
# log10 > 23/10 via 3*2atanh(1/3)+2atanh(1/9) partial sums (lower bounds)
log2_lo=2*(F(1,3)+F(1,81)+F(1,1215)+F(1,15309)); log54_lo=F(2,9)
print('log10_lo',float(3*log2_lo+log54_lo), 3*log2_lo+log54_lo>F(23,10))
# log2<7/10: exp(7/10) partial series through deg 4 > 2
s=sum(F(7,10)**k/math.factorial(k) for k in range(5)); print('exp(.7) lo',float(s), s>2)
print('logn0 lo', 6*F(23,10)-F(7,10))
# log n0 < 14 : e>27/10, (27/10)^14 > 500000
print('(2.7)^14',float(F(27,10)**14), F(27,10)**14>n)
# X bounds with pi in (311/99? ) use pi<22/7, pi>333/106
pi_lo=F(333,106); pi_hi=F(22,7)
X_lo=m/(1000*pi_hi); print('X>=',float(X_lo), X_lo>159, X_lo-F(1,2)>158)
print('128pi/m<delta', 128*pi_hi/m<F(1,1000))
print('h/2', float(pi_hi/(2*m)), F(1,1000)-pi_hi/(2*m)>F(249,250000))
print('delta+h<126/125000', F(1,1000)+pi_hi/m<F(126,125000), 'and <101/100000',F(1,1000)+pi_hi/(2*m)<F(101,100000))
G=F(101,108)*F(126,125000)**2; print('G',float(G),G<F(1,10**6))
# log(1/x)<9 for x=delta: 1000<e^9
print('e^9>1000', F(27,10)**9>1000)
print('log(2/ell0)<8: 2/ell0=',float(2/F(249,250000)),'e^8>',float(F(27,10)**8), F(27,10)**8>2/F(249,250000))
print('log158<6', F(27,10)**6>158)
# eA and elog
L=F(14)
print('eA', float(L*(F(1,1000)+pi_hi/(2*m))/(6*m)), L*(F(1,1000)+pi_hi/(2*m))/(6*m)<F(1,10**8))
print('elog',F(1,3060)/n<F(1,10**9))
# C05 (11): l^2/(6pi)*L/n^2 with l<516/n
print('516^2/18',F(516**2,18)<15000)
# (14) vs 5(L+1) at L>=3
for Lv in [F(3),F(131,10),F(14)]:
    print('L',Lv, F(18)+F(3,1000)+F(109,300)*Lv < 5*(Lv+1), 4*(Lv+6)+F(2,3)*(Lv+1) < 10*(Lv+1), 8*(Lv+5)+1<50*(Lv+1))
# exp checks
print('alpha small', 15/32*math.exp(-12)+32/9*math.exp(-16), 'beta', math.exp(-144)/(18*math.e))
# sharpness margins
print('eta0 margin', 1e-3-0.00033874681)
print('(18) margin to 1/32', float(F(1,32)-F(383,12500)), ' final lambda margin', float(F(1,16)-F(383,12500)-F(1,32)))
