# A7 (informational, MEASURED): mean-permutation determinant lower quantity [S A - log D(pi)]/(N n) for A and L orders at large n,
# plus direct check of n^-4 log D_M limit.
import numpy as np, math, mpmath as mp
def logD(n,o):
    h=np.cos(np.pi*np.arange(n+1)/n); z=h[o]; s=0.0
    for j in range(1,n+1):
        s+=math.comb(n-j+2,2)*np.sum(np.log(np.abs(z[j]-z[:j])))
    return s
def Aord(n):
    o=[]
    for j in range((n+2)//2):
        o.append(j)
        if n-j!=j: o.append(n-j)
    return o
def Lord(n):
    h=np.cos(np.pi*np.arange(n+1)/n); used=[0]; logp=np.log(np.abs(h-h[0])+0.0); mask=np.ones(n+1,bool); mask[0]=False
    lp=np.where(mask,np.log(np.abs(h-h[0])),-np.inf)
    while mask.any():
        cand=np.where(mask)[0]; v=lp[cand]; b=v.max(); w=cand[np.where(v>=b-1e-9)[0][0]]
        used.append(int(w)); mask[w]=False
        with np.errstate(divide='ignore'): lp=lp+np.log(np.abs(h-h[w]))
    return used
lim=-math.log(2)/24-float(mp.zeta(3))/(4*math.pi**2)
for n in [50,100,200,400,800]:
    S=math.comb(n+3,4); N=math.comb(n+3,3); A=((n+1)*math.log(n)+(3-n*n)*math.log(2))/(n*(n+1))
    out=[]
    for name,o in [('M',list(range(n+1))),('A',Aord(n)),('L',Lord(n))]:
        out.append('%s:%.5f'%(name,(S*A-logD(n,o))/N/n))
    print(n,' '.join(out),' n^-4 logD_M=%.6f (limit %.6f)'%(logD(n,list(range(n+1)))/n**4,lim))
