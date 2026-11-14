import numpy as np, mpmath as mp
mp.mp.dps=30
# (1) d^2/ds^2 f(sqrt(2s)) = int int t^2 f''''(r t sqrt(2s)) dr dt for even f
for f,f4 in ((lambda A: mp.cos(3*A)+0.3*mp.cos(A), lambda A: 81*mp.cos(3*A)+0.3*mp.cos(A)),
             (lambda A: mp.cos(0.7*A)**2, lambda A: mp.diff(lambda t: mp.cos(0.7*t)**2, A, 4))):
    for s in (mp.mpf('0.05'), mp.mpf('0.8'), mp.mpf('2.0')):
        lhs=mp.diff(lambda w: f(mp.sqrt(2*w)), s, 2)
        rhs=mp.quad(lambda t: t**2*mp.quad(lambda r: f4(r*t*mp.sqrt(2*s)),[0,1]),[0,1])
        assert abs(lhs-rhs)<1e-15, (s,lhs,rhs)
print("squared-variable second-derivative identity verified (two even test functions, three s values); weight mass int t^2 = 1/3")
# (2) h_uu = (A p_AA - p_A)/A^3
p=lambda A: mp.cos(2*A)*mp.cos(0.4*A)
for A0 in (mp.mpf('0.3'),mp.mpf('1.1')):
    u0=A0**2/2
    lhs=mp.diff(lambda u: p(mp.sqrt(2*u)), u0, 2)
    rhs=(A0*mp.diff(p,A0,2)-mp.diff(p,A0,1))/A0**3
    assert abs(lhs-rhs)<1e-15
print("h_uu=(A p_AA - p_A)/A^3 verified")
# (3) small-degree maximizer sanity (MEASURED, grid) via direct cardinals
def lam(n,X,Y):
    m=n+1; N=n*m; th=np.arccos(np.clip(X,-1,1)); ph=np.arccos(np.clip(Y,-1,1))
    tot=np.zeros_like(X)
    nu=lambda p: 1.0 if p==0 else 2.0
    for j in range(n+1):
        for k in range(m+1):
            if (j+k)%2: continue
            e=0.5 if j in (0,n) else 1.0; f=0.5 if k in (0,m) else 1.0
            w=2*e*f/N; a=j*np.pi/n; b=k*np.pi/m
            K=np.zeros_like(X)
            for pp in range(n+1):
                cp=np.cos(pp*th)*np.cos(pp*a)
                for q in range(n+1-pp):
                    K+=nu(pp)*nu(q)*cp*np.cos(q*ph)*np.cos(q*b)
            K-=np.cos(n*th)*np.cos(n*a)
            tot+=np.abs(w*K)
    return tot
g=np.linspace(-1,1,241); X,Y=np.meshgrid(g,g)
for n in range(2,9):
    L=lam(n,X,Y); mx=L.max(); pts=[(round(X[i,j],3),round(Y[i,j],3)) for i,j in np.argwhere(L>mx-1e-9)]
    print(f"n={n}: grid max {mx:.10f} at {pts}; second-largest gap {mx-np.sort(L.ravel())[-3]:.3e}")
