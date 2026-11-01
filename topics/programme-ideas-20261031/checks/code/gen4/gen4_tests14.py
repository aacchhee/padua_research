import numpy as np
from numpy.polynomial import legendre as Lg
# Sections of the block Jacobi pair (multiplication by x,y in orthonormal product basis) on Pi_{m}, for product Chebyshev and product Legendre on the square.
def jac1d(kind, m):
    # 1D Jacobi matrix (m+1)x(m+1) for orthonormal basis
    if kind=='cheb':
        J=np.zeros((m+1,m+1)); 
        for i in range(m):
            J[i,i+1]=J[i+1,i]= (1/np.sqrt(2) if i==0 else 0.5)
        return J
    else:
        J=np.zeros((m+1,m+1))
        for i in range(m):
            b=(i+1)/np.sqrt((2*i+1)*(2*i+3)); J[i,i+1]=J[i+1,i]=b
        return J
def sections(kind,m):
    idx=[(i,j) for d in range(m+1) for i in range(d+1) for j in [d-i]]
    pos={p:q for q,p in enumerate(idx)}
    J=jac1d(kind,m+1)
    Hx=np.zeros((len(idx),)*2); Hy=np.zeros_like(Hx)
    for (i,j),q in pos.items():
        for i2 in range(m+2):
            if J[i,i2]!=0 and (i2,j) in pos: Hx[pos[(i2,j)],q]=J[i,i2]
        for j2 in range(m+2):
            if J[j,j2]!=0 and (i,j2) in pos: Hy[pos[(i,j2)],q]=J[j,j2]
    return Hx,Hy,len(idx)
def moller(n):  # degree 2n-1 rule, centrally symmetric weight: N >= dim Pi_{n-1} + floor(n/2)
    return n*(n+1)//2 + n//2
if __name__=='__main__':
  for kind in ('cheb','leg'):
    for n in range(2,11):
        Hx,Hy,N=sections(kind,n-1)   # sections on Pi_{n-1}; a degree-(2n-1) rule with M nodes gives a commuting extension of size M
        C=Hx@Hy-Hy@Hx; r=np.linalg.matrix_rank(C,tol=1e-10)
        print(kind,'n',n,'dim Pi_{n-1}',N,'rank[Hx,Hy]',r,'DST bound M >= dim+rank/2 =',N+int(np.ceil(r/2)),'Moller',moller(n),'Padua dim Pi_n',(n+1)*(n+2)//2)
