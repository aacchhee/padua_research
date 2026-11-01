"""Draft-2 entry point 2 (quick form): given H_x (full pattern) and the first column of H_y,
how many entries of H_y are left free by commutativity + symmetric pattern? Then the same
with the pivot columns of H_y that Algorithm 1 forms (one per degree, the y-pivot column)."""
import numpy as np
exec(open('tangent_dim.py').read().split('for n in')[0])
for n in [3,4,5,6,8]:
    N=(n+1)*(n+2)//2; rng=np.random.default_rng(n)
    x=rng.uniform(-1,1,N); y=rng.uniform(-1,1,N); w=rng.uniform(0.5,1.5,N)
    Hx,Hy=sections(x,y,w,n)
    paty=np.abs(Hy)>1e-10
    pairs=[(i,j) for i in range(N) for j in range(i,N) if paty[i,j]]
    cols=[]
    for (i,j) in pairs:
        E=np.zeros((N,N)); E[i,j]=1; E[j,i]=1; cols.append((Hx@E-E@Hx).ravel())
    A=np.array(cols).T
    sv=np.linalg.svd(A,compute_uv=False); free=len(pairs)-(sv>1e-9*sv[0]).sum()
    # entries of Hy in the known "pivot" columns: take the column k of Hy whose below-pattern pivot is a y-step
    # simple proxy: first column (degree 0 -> 1) and all entries in columns whose pattern has an entry below the x-pattern
    patx=np.abs(Hx)>1e-10
    ycols=[k for k in range(N) if any(paty[i,k] and not patx[i,k] for i in range(N))]
    known=[(i,j) for (i,j) in pairs if j in ycols or i in ycols]
    # constrain known entries: add rows fixing them
    Afix=np.zeros((len(known),len(pairs)))
    for r,(i,j) in enumerate(known): Afix[r,pairs.index((i,j))]=1
    A2=np.vstack([A,Afix]); sv2=np.linalg.svd(A2,compute_uv=False); free2=len(pairs)-(sv2>1e-9*sv2[0]).sum()
    print(f"n={n} N={N}: Hy pattern entries={len(pairs)}; free given Hx only (commutant)={free}; "
          f"y-pivot columns={len(ycols)} (entries {len(known)}); free given Hx + those columns={free2}")
