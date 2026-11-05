# Claude audit: independent check of frontier weight formula (3) against solved Padua weights.
import numpy as np, sys
from fractions import Fraction
def nodes(m):
    J,K=[],[]
    for j in range(m+1):
        for k in range(m+2):
            if (j+k)%2==0: J.append(j);K.append(k)
    return np.array(J),np.array(K)
def h(r): return 0.0 if r%2 else 2.0/(1-r*r)
def solved(m):
    J,K=nodes(m); th=J*np.pi/m; ph=K*np.pi/(m+1)
    rows=[];rhs=[]
    for d in range(m+1):
        for a in range(d,-1,-1):
            b=d-a; rows.append(np.cos(a*th)*np.cos(b*ph)); rhs.append(h(a)*h(b))
    V=np.array(rows); return J,K,np.linalg.solve(V,np.array(rhs))
def formula(m,exc=2.0):
    R=m//2; J,K=nodes(m); th=J*np.pi/m; ph=K*np.pi/(m+1)
    t=np.array([2.0]+[-4.0/(4*a*a-1) for a in range(1,R+1)])
    S=np.zeros(len(J))
    for a in range(R+1):
        b=np.arange(0,R-a+1)
        S+=t[a]*np.cos(2*a*th)*(np.cos(np.outer(ph,2*b))@t[b])
    eps=np.where((J==0)|(J==m),.5,1.); eta=np.where((K==0)|(K==m+1),.5,1.)
    return 2*eps*eta/(m*(m+1))*(S-exc*h(m)*np.cos(m*th))
for m in [2,4,6,8,10,12,20,30]:
    J,K,w=solved(m); f2=formula(m,2.0); f4=formula(m,4.0)
    print(m, "sum", round(w.sum(),12), "max|w-f(2h)|=%.2e"%abs(w-f2).max(), "max|w-f(4h)|=%.2e"%abs(w-f4).max(),
          "bound2 ok", bool(np.all(np.abs(w)<=4096/m**4*((1+J)*(1+K)+np.log(m+1)))) if m>=4 else '')
