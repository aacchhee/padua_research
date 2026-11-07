# LP: minimal norm projection C([-1,1]^d)->Pi_1 with functionals supported on a grid G (upper bound on minimal projection constant).
import numpy as np, itertools as it
from scipy.optimize import linprog
from scipy.sparse import lil_matrix, csr_matrix
def run(d,q):
    g=np.linspace(-1,1,q); G=np.array(list(it.product(g,repeat=d))); m=len(G)
    W=np.array(list(it.product([-1,1],repeat=d))); nv=len(W)
    # variables: L (d+1)*m (free), for each vertex v: u_v (m) >=0 with u_v>=|M_v|, then t
    nL=(d+1)*m; nu=nv*m; nvar=nL+nu+1
    A=lil_matrix((2*nv*m+nv,nvar)); b=np.zeros(2*nv*m+nv); r=0
    for vi,v in enumerate(W):
        coef=np.concatenate([[1],v])
        for i in range(m):
            for j in range(d+1): A[r,j*m+i]=coef[j]
            A[r,nL+vi*m+i]=-1; r+=1
            for j in range(d+1): A[r,j*m+i]=-coef[j]
            A[r,nL+vi*m+i]=-1; r+=1
        A[r,nL+vi*m:nL+(vi+1)*m]=1; A[r,-1]=-1; r+=1
    Ph=np.hstack([np.ones((m,1)),G])  # basis values at grid
    Aeq=lil_matrix(((d+1)**2,nvar)); beq=np.zeros((d+1)**2)
    for j in range(d+1):
        for i in range(d+1):
            Aeq[j*(d+1)+i,j*m:(j+1)*m]=Ph[:,i]; beq[j*(d+1)+i]=float(i==j)
    c=np.zeros(nvar); c[-1]=1
    bounds=[(None,None)]*nL+[(0,None)]*nu+[(0,None)]
    res=linprog(c,A_ub=csr_matrix(A),b_ub=b,A_eq=csr_matrix(Aeq),b_eq=beq,bounds=bounds,method='highs')
    return res.fun
for d,q in ((2,3),(2,9),(2,17),(3,3),(3,5),(3,9)):
    print('d',d,'grid',q,'min ||P|| (grid-supported projections onto Pi_1) =',run(d,q))
print('theorem lower bounds: d2 ||K_1||_1=1.17508, d3 ||K_1||_1=1.28842 ; box bounds 1.13662, 1.22746')
