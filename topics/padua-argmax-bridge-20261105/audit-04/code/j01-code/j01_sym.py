"""Audit-04 J01: symbolic identities (2) and (4), Cauchy-Schwarz bracket, (T+A4)' bound."""
import sympy as sp
l1,l2,d1,d2,rho,x=sp.symbols('l1 l2 d1 d2 rho x',positive=True)
S0=d1+d2; e=d1*d2/S0; f=(d2*l1+d1*l2)/S0; g=(l1-l2)**2/(4*S0)
xs=(d2*rho+(l1-l2)/2)/S0
lhs=l1*x+l2*(rho-x)-d1*x**2-d2*(rho-x)**2
rhs=g+f*rho-e*rho**2-S0*(x-xs)**2
print('square completion (2):',sp.simplify(lhs-rhs)==0)
print('max identity (4):',sp.simplify(g+f**2/(4*e)-(l1**2/(4*d1)+l2**2/(4*d2)))==0)
print('vertex identity (4):',sp.simplify(f/(2*e)-(l1/(2*d1)+l2/(2*d2)))==0)
print('ystar at rho=1/2:',sp.simplify((sp.Rational(1,2)-xs.subs(rho,sp.Rational(1,2)))-(d1/2-(l1-l2)/2)/S0)==0)
h,dl,Th,t,KD=sp.symbols('h delta Theta t K_D',real=True)
X,Y=h+dl,h-dl
u=1-(sp.cos(X)+sp.cos(Y))/2
expr=u*Th-t*sp.sin(X)-KD*(sp.sin(X)+sp.sin(Y))
C=t+2*KD; A=Th*sp.cos(h)+C*sp.sin(h); B=t*sp.cos(h)
print('gate bracket identity (6):',sp.simplify(sp.expand_trig(expr-(Th-(A*sp.cos(dl)+B*sp.sin(dl)))))==0)
n=sp.symbols('n',positive=True); L=sp.log(n)
T=(4*L**2-3*L)/sp.pi**2; A4=4/n+40*(1+L)/(sp.pi*n**2)
dT=sp.diff(T+A4,n)
# exact derivative vs claimed lower bound (L/n^3)(n^2/2-4n-40), checked at sample reals as a sanity check only
for nv in [32,40,100,512,10**4,10**8]:
    v=dT.subs(n,nv).evalf(30); b=(sp.log(nv)/nv**3*(sp.Rational(nv**2,2)-4*nv-40)).evalf(30)
    print('n',nv,'(T+A4)\'',sp.N(v,8),'claimed lower',sp.N(b,8),'ok',v>b)
