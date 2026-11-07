# Audit check A1: lower-bound quantity L(n)=[S_n A_n - log D_M]/N, its /n, and constant
import mpmath as mp, math, numpy as np
mp.mp.dps=40
c=3*mp.zeta(3)/(2*mp.pi**2)
print("3zeta3/(2pi^2) =",c)
def Lval(n, dps=30):
    with mp.workdps(dps):
        h=[mp.cos(mp.pi*j/n) for j in range(n+1)]
        logD=mp.mpf(0)
        for j in range(n+1):
            Nj=math.comb(n-j+2,2)
            s=mp.fsum(mp.log(h[i]-h[j]) for i in range(j))
            logD+=Nj*s
        S=math.comb(n+3,4); N=math.comb(n+3,3)
        A=((n+1)*mp.log(n)+(3-n*n)*mp.log(2))/(n*(n+1))
        # check A against direct mean
        return (S*A-logD)/N, logD, A
# check A_n against direct mean for a few n
for n in [1,2,3,7,20]:
    with mp.workdps(40):
        h=[mp.cos(mp.pi*j/n) for j in range(n+1)]
        direct=mp.fsum(mp.log(abs(h[a]-h[b])) for a in range(n+1) for b in range(a+1,n+1))/math.comb(n+1,2)
        A=((n+1)*mp.log(n)+(3-n*n)*mp.log(2))/(n*(n+1))
        print("n",n,"A_n formula-direct",mp.nstr(A-direct,5), " sum jN_j==C(n+3,4):", sum(j*math.comb(n-j+2,2) for j in range(n+1))==math.comb(n+3,4))
prev=None
rows=[]
for n in [1,2,3,4,5,6,7,8,10,12,16,20,32,50,64,100,128,200,256,400,512,800,1024,1600,2048]:
    L,logD,A=Lval(n, 25)
    r=L/n
    rows.append((n,r))
    print("n=%5d  L(n)=%.6f  L/n=%.6f  gap=%.6f  gap*n/log n=%s"%(n,float(L),float(r),float(c-r), mp.nstr((c-r)*n/mp.log(n),6) if n>1 else '-'))
