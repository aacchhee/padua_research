import numpy as np
exec(open('tangent_dim.py').read().split('for n in')[0])
for n in [3,4,5,6]:
    N=(n+1)*(n+2)//2
    rng=np.random.default_rng(n)
    x=rng.uniform(-1,1,N); y=rng.uniform(-1,1,N); w=rng.uniform(0.5,1.5,N)
    Hx,Hy=sections(x,y,w,n)
    patx=np.abs(Hx)>1e-10; paty=np.abs(Hy)>1e-10   # actual generalized-Hessenberg patterns
    def cols_for(pat,left):
        pairs=[(i,j) for i in range(N) for j in range(i,N) if pat[i,j]]
        out=[]
        for (i,j) in pairs:
            E=np.zeros((N,N)); E[i,j]=1; E[j,i]=1
            out.append(((E@Hy-Hy@E) if left else (Hx@E-E@Hx)).ravel())
        return out,len(pairs)
    cx,mx=cols_for(patx,True); cy,my=cols_for(paty,False)
    A=np.array(cx+cy).T; sv=np.linalg.svd(A,compute_uv=False); rank=(sv>1e-9*sv[0]).sum()
    print(f"n={n} N={N}: nnz-sym entries Hx={mx}, Hy={my}, tangent dim (gen-Hessenberg pattern)={mx+my-rank}, 3N-1={3*N-1}, C(n+2,3)={(n+2)*(n+1)*n//6}")
