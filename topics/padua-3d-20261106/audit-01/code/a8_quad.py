# A8: direct quadrature of I=(1/2)int_0^1 (1-t)^2 int_0^t log(cos(pi s)-cos(pi t)) ds dt, vs -log2/24-zeta(3)/(4pi^2);
# and J(t) closed form vs direct inner integral at sample t.
import mpmath as mp
mp.mp.dps=30
f=lambda s,t: mp.log(mp.cos(mp.pi*s)-mp.cos(mp.pi*t))
Jdir=lambda t: mp.quad(lambda s: f(s,t),[0,t])
Jser=lambda t: -t*mp.log(2)-mp.nsum(lambda r: mp.sin(2*mp.pi*r*t)/r**2,[1,mp.inf])/mp.pi
for t in [mp.mpf('0.1'),mp.mpf('0.5'),mp.mpf('0.77'),mp.mpf(1)]:
    print('t=',t,' Jdirect-Jseries=',mp.nstr(Jdir(t)-Jser(t),5))
Jcl=lambda t: t*mp.log(2)+2*mp.quad(lambda v: mp.log(mp.sin(mp.pi*v)),[0,t])
I=mp.quad(lambda t: (1-t)**2*Jcl(t),[0,mp.mpf(1)/2,1])/2
tgt=-mp.log(2)/24-mp.zeta(3)/(4*mp.pi**2)
print('I=',mp.nstr(I,20),' target=',mp.nstr(tgt,20),' diff=',mp.nstr(I-tgt,3))
print('rate 6*(-log2/24 - I)=',mp.nstr(6*(-mp.log(2)/24-I),20),' 3zeta3/2pi^2=',mp.nstr(3*mp.zeta(3)/(2*mp.pi**2),20))
