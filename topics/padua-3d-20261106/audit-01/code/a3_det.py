# A3: (i) Lobatto discriminant formula; (ii) det V(X_pi) / D(pi) constant across ALL permutations (mpmath 50 dps, n<=4);
# (iii) exhaustive max over permutations of log D vs mean, n<=8.
import mpmath as mp, math, itertools as it
mp.mp.dps=50
def padua(m):
    if m==0: return [(mp.mpf(1),mp.mpf(1))]
    return [(mp.cos(i*mp.pi/m),mp.cos(j*mp.pi/(m+1))) for i in range(m+1) for j in range(m+2) if (i+j)%2==0]
def expo(n):
    return [(a,b,c) for d in range(n+1) for a in range(d+1) for b in range(d-a+1) for c in [d-a-b]]
def logD(n,z):
    return mp.fsum(math.comb(n-j+2,2)*mp.log(abs(z[j]-z[i])) for j in range(n+1) for i in range(j))
for n in range(1,9):
    h=[mp.cos(mp.pi*j/n) for j in range(n+1)]
    lhs=mp.fprod((h[a]-h[b])**2 for a in range(n+1) for b in range(a+1,n+1))
    rhs=mp.mpf(n)**(n+1)*mp.mpf(2)**(3-n*n)
    print("disc n=%d rel.err %s"%(n,mp.nstr(lhs/rhs-1,3)))
for n in range(1,5):
    h=[mp.cos(mp.pi*j/n) for j in range(n+1)]
    E=expo(n); consts=set(); signs=set()
    for perm in it.permutations(range(n+1)):
        z=[h[p] for p in perm]
        pts=[(x,y,z[k]) for k in range(n+1) for (x,y) in padua(n-k)]
        V=mp.matrix([[x**a*y**b*zz**c for (a,b,c) in E] for (x,y,zz) in pts])
        d=mp.det(V)
        # signed height factor prod_{i<j}(z_j-z_i)^{N_j}
        sf=mp.fprod((z[j]-z[i])**math.comb(n-j+2,2) for j in range(n+1) for i in range(j))
        consts.add(mp.nstr(d/sf,25))
    print("n=%d perms=%d distinct det/heightfactor values: %s"%(n,math.factorial(n+1),consts))
for n in range(1,9):
    h=[mp.cos(mp.pi*j/n) for j in range(n+1)]
    mp.mp.dps=20
    vals=[]
    for perm in it.permutations(range(n+1)):
        vals.append(logD(n,[h[p] for p in perm]))
    mp.mp.dps=50
    N=math.comb(n+3,3); S=math.comb(n+3,4)
    A=((n+1)*mp.log(n)+(3-n*n)*mp.log(2))/(n*(n+1))
    mean=mp.fsum(vals)/len(vals)
    lM=logD(n,h)
    print("n=%d mean-S*A=%s  mean-bound=%.4f  max-bound=%.4f (log Lambda_M >=)  argmax-count=%d"%(n,mp.nstr(mean-S*A,3),float((mean-lM)/N),float((max(vals)-lM)/N),sum(1 for v in vals if v>max(vals)-1e-12)))
