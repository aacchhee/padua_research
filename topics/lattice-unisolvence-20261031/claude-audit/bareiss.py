from sympy.polys.rings import ring
from sympy import ZZ
def bareiss(M):
    M=[r[:] for r in M]; n=len(M); sign=1; prev=M[0][0].ring.one
    for k in range(n-1):
        if M[k][k]==0:
            sw=next((i for i in range(k+1,n) if M[i][k]!=0),None)
            if sw is None: return M[0][0].ring.zero
            M[k],M[sw]=M[sw],M[k]; sign=-sign
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=M[i][j]*M[k][k]-M[i][k]*M[k][j]
                q,r=num.div(prev); assert r==0
                M[i][j]=q
        prev=M[k][k]
    return sign*M[n-1][n-1]
