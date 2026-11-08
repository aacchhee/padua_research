# P4 audit: numerical spot checks of Section 3 identities (cu:square, cu:exact, cu:deform). MEASURED.
import mpmath as mp
mp.mp.dps=30
pi=mp.pi
def f(u,v): return (1+mp.cos(v))/abs(mp.cos(u)-mp.cos(v))
for n in [5,6,11,30]:
    m=n+1
    eps=lambda j: mp.mpf(1)/2 if j in (0,n) else 1
    sq=4*sum(eps(j)*eps(k)*f(pi*j/n,pi*k/n) for j in range(n+1) for k in range(n+1) if (j+k)%2==1)/n**2
    Ln=2*sum((mp.mpf(1)/2 if r==n else 1)/mp.sin(r*pi/(2*n)) for r in range(1,n+1,2))/n
    eta=lambda k: mp.mpf(1)/2 if k in (0,m) else 1
    Lc=4*sum(eps(j)*eta(k)*f(pi*j/n,pi*k/m) for j in range(n+1) for k in range(n+1) if (j+k)%2==1)/(n*m)+mp.mpf(1)/m
    w=lambda x: mp.cot(pi*x/2)
    B=lambda x: mp.cot(pi*x)-1/(pi*x)+1/(pi*(1-x))
    Tn=lambda r: sum(mp.cot(pi*(l+(1-mp.mpf(r)/m)/2)/n) for l in range(r))
    ex1=1-mp.mpf(2*n)/m+4*sum(w(mp.mpf(r)/m)*Tn(r) for r in range(1,m))/(n*m)
    al=lambda r:(1-mp.mpf(r)/m)/2
    D=lambda r: mp.digamma(r+al(r))+mp.digamma(m-r-al(r))-mp.digamma(m-al(r))-mp.digamma(al(r))
    Hm=4*sum(w(mp.mpf(r)/m)*D(r) for r in range(1,m))/(pi*m)
    V=sum(w(mp.mpf(r)/m)*sum(B((l+al(r))/n) for l in range(r)) for r in range(1,m))
    ex2=-1+mp.mpf(2)/m+Hm+4*V/(n*m)
    # deform bound
    worst=0
    for j in range(n+1):
        for k in range(n+1):
            if (j+k)%2==1:
                l=abs(j-k)
                d=abs(f(pi*j/n,pi*k/m)-f(pi*j/n,pi*k/n)) if not (k==0 or j==n) else 0
                worst=max(worst, d/(pi**2*n/(2*l**2)))
    print(n,'square-Ln^2',mp.nstr(sq-Ln**2,5),' Lc-ex1',mp.nstr(Lc-ex1,5),' Lc-ex2',mp.nstr(Lc-ex2,5),' max deform ratio',mp.nstr(worst,5))
