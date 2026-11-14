# MEASURED: discrete sums A1,A2,A3 and sum (g-1/6)^-2 over C07's new R, versus C07 (8),(16).
import numpy as np, math
for n in (1000,4000):
    m=n+1; A1=A2=A3=G2=0.0
    for j in range(n+1):
        r=np.arange(m+1); keep=((j+r)%2==1)&~((r==j+1)&(j>=n/2))
        r=r[keep]; S=j+r; g=np.abs(j-r+j/n)
        Sq=S-1/6; gq=g-1/6
        A1+=np.sum(1/(Sq*gq**3)); A2+=np.sum(1/(Sq**3*gq)); A3+=np.sum(1/(Sq**2*gq**2)); G2+=np.sum(gq**-2.0)
    L=math.log(m)
    print(n,"A1=%.4f bound=%.4f  A2=%.4f<6  A3=%.4f<7  sum(g-1/6)^-2/m=%.4f<4.5"%(A1,7581/4000*L+21,A2,A3,G2/m))
