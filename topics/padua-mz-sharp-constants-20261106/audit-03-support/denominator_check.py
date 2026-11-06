# Claude audit-03: floating mpmath cross-check of P4-denominator-closed-form.md closed forms
# against direct quadrature of C_ij = int_0^inf t F_i F_j dt, F_j = 2(-1)^j a_j^2 sin t/[t(t^2-a_j^2)], a_j = pi j.
# MEASURED corroboration only; quadrature truncated at T = 399 pi, crude tail estimate printed.
import mpmath as mp
mp.mp.dps=30
def F(j,t):
    a=mp.pi*j; s=(-1)**j
    return 2*s*a**2*mp.sin(t)/(t*(t**2-a**2))
def Cin(x): return mp.euler+mp.log(x)-mp.ci(x)
def closed(i,j):
    a,b=mp.pi*i,mp.pi*j; si,sj=(-1)**i,(-1)**j
    if i==j: return 2*(a*mp.si(2*a)+Cin(2*a))
    return 2*si*sj*(a**2*Cin(2*b)-b**2*Cin(2*a))/(a**2-b**2)
def quadC(i,j):
    pts=[0]+[mp.pi*k for k in range(1,400)]
    v=mp.quad(lambda t: t*F(i,t)*F(j,t),pts)
    return v,(mp.pi*i)**2*(mp.pi*j)**2/pts[-1]**4*2
for i,j in [(1,1),(1,2),(2,3),(3,3),(1,5),(4,7)]:
    q,tb=quadC(i,j); c=closed(i,j)
    print(i,j,mp.nstr(c,15),mp.nstr(q,15),mp.nstr(abs(c-q),3),'tail<~',mp.nstr(tb,3))
