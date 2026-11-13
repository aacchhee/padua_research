# A2: extrapolate the limit of L(n)/n by least squares c + (a log n + b)/n + (d log n + e)/n^2
import mpmath as mp, math, numpy as np
mp.mp.dps=30
def r(n):
    h=[mp.cos(mp.pi*j/n) for j in range(n+1)]
    logD=mp.fsum(math.comb(n-j+2,2)*mp.fsum(mp.log(h[i]-h[j]) for i in range(j)) for j in range(n+1))
    S=math.comb(n+3,4); N=math.comb(n+3,3)
    A=((n+1)*mp.log(n)+(3-n*n)*mp.log(2))/(n*(n+1))
    return (S*A-logD)/N/n
ns=[200,300,400,600,800,1000,1200,1500]
vals=[r(n) for n in ns]
M=mp.matrix([[1,mp.log(n)/n,mp.mpf(1)/n,mp.log(n)/n**2,mp.mpf(1)/n**2] for n in ns])
y=mp.matrix(vals)
sol=mp.lu_solve(M.T*M,M.T*y)
print("extrapolated c =",mp.nstr(sol[0],10),"target",mp.nstr(3*mp.zeta(3)/(2*mp.pi**2),10),"coefs",[mp.nstr(s,6) for s in sol[1:]])
