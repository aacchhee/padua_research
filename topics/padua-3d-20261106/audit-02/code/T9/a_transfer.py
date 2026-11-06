# Numeric sanity checks of T9-04 (lower-set transfer) and T9-05 (correction lemma). MEASURED only.
import numpy as np, itertools as it, math
from numpy.polynomial import chebyshev as C
fine=np.cos(np.linspace(0,np.pi,4001))
# fixed nested Leja-type sequence on [-1,1] (discrete on fine grid), independent of n
seq=[1.0]
while len(seq)<12:
    p=np.prod([np.abs(fine-s) for s in seq],axis=0); seq.append(fine[np.argmax(p)])
seq=np.array(seq)
def lam1(m):  # univariate Lebesgue const of first m+1 nodes on fine grid (lower sample)
    x=seq[:m+1]; V=C.chebvander(x,m); Vf=C.chebvander(fine,m)
    return np.abs(np.linalg.solve(V.T,Vf.T)).sum(0).max()
lam=[lam1(m) for m in range(12)]
print('univariate prefix Lebesgue samples',np.round(lam,3).tolist())
d=3
for n in (3,4,5,6):
    A=[a for a in it.product(range(n+1),repeat=d) if sum(a)<=n]
    X=np.array([[seq[a] for a in al] for al in A])
    E=A
    def basis(P):
        T=[C.chebvander(P[:,j],n) for j in range(d)]
        return np.stack([T[0][:,a]*T[1][:,b]*T[2][:,c] for a,b,c in E],1)
    V=basis(X); print('n',n,'N',len(A),'cond',np.linalg.cond(V))
    g=np.cos(np.linspace(0,np.pi,31)); M=np.array(list(it.product(g,repeat=3)))
    Lam=np.abs(basis(M)@np.linalg.inv(V)).sum(1).max()
    lp=lambda m: lam[m]+(lam[m-1] if m>0 else 0)
    bound=sum(np.prod([lp(a) for a in al]) for al in A)
    # hierarchical formula check: S_A f == I_A f for random f at random points
    rng=np.random.default_rng(n); f=lambda P: np.exp(P[:,0]-0.5*P[:,1])*np.cos(2*P[:,2])+P[:,0]*P[:,1]
    Z=rng.uniform(-1,1,(200,3))
    IA=basis(Z)@np.linalg.solve(V,f(X))
    def Iuni(m,vals_fn):  # 1D interpolation operator on first m+1 nodes, returns Lagrange basis at z
        x=seq[:m+1]
        def L(z):
            out=np.ones((len(z),m+1))
            for i in range(m+1):
                for j in range(m+1):
                    if i!=j: out[:,i]*= (z-x[j])/(x[i]-x[j])
            return out
        return L
    def Delta_weights(m,z):  # weights over nodes 0..m of Delta_m evaluated at z
        w=np.zeros((len(z),m+1)); w[:,:m+1]+=Iuni(m,None)(z)
        if m>0: w[:,:m]-=Iuni(m-1,None)(z)
        return w
    SA=np.zeros(len(Z))
    for al in A:
        W=[Delta_weights(al[j],Z[:,j]) for j in range(3)]
        for idx in it.product(*[range(a+1) for a in al]):
            SA+=W[0][:,idx[0]]*W[1][:,idx[1]]*W[2][:,idx[2]]*f(np.array([[seq[idx[0]],seq[idx[1]],seq[idx[2]]]]))[0]
    print('   mesh31 Lambda',round(Lam,4),'<= transfer bound',round(bound,2),Lam<=bound,' |S_A f - I_A f|max',np.abs(SA-IA).max())
# T9-05: d=2, V=Pi_n^2, H = hyperinterpolation on tensor Gauss-Chebyshev (exact deg 2n+1 product) grid Y
for n in (3,5,8):
    E=[(a,b) for a in range(n+1) for b in range(n+1-a)]
    k=n+1; th=(np.arange(k)+0.5)*np.pi/k; g1=np.cos(th)
    Y=np.array(list(it.product(g1,g1))); w=np.full(len(Y),1/len(Y))
    nrm=lambda a: 1.0 if a==0 else math.sqrt(2)
    def B2(P):
        T=[C.chebvander(P[:,j],n) for j in range(2)]
        return np.stack([nrm(a)*nrm(b)*T[0][:,a]*T[1][:,b] for a,b in E],1)
    BY=B2(Y)
    print('n',n,'Gram err',np.abs(BY.T@(w[:,None]*BY)-np.eye(len(E))).max())
    g=np.cos(np.linspace(0,np.pi,201)); M=np.array(list(it.product(g,g)))
    h=lambda Z: (B2(Z)@BY.T)*w[None,:]   # h_y(z), columns y
    Hn=np.abs(h(M)).sum(1).max()
    # choose X subset of Y by pivoted QR on Vandermonde rows
    import scipy.linalg as sl
    piv=sl.qr(BY.T,pivoting=True,mode='economic')[2][:len(E)]
    X=Y[piv]; Cm=h(X)[:,piv]  # C_ij = h_{x_j}(x_i)
    Ci=np.linalg.inv(Cm); ci=np.abs(Ci).sum(1).max()
    ell=h(M)[:,piv]@Ci
    VX=B2(X); ell2=B2(M)@np.linalg.inv(VX)
    print('   ||H||~',round(Hn,3),' ||C^-1||_inf',round(ci,3),' Lambda(I_X)~',round(np.abs(ell).sum(1).max(),3),'<= product',round(Hn*ci,3),'; formula==direct interp',np.abs(ell-ell2).max()<1e-8)
