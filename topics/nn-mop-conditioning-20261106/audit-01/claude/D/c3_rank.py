# Independent exact check of the C3 residual-dimension statement (monomial basis).
import sympy as sp, math, sys
from fractions import Fraction as Q
def run(N, fam):
    M_=N-1
    x0=[sp.Rational(2*k,M_)-1 for k in range(N)]
    if fam=='krawtchouk':
        w0=[[sp.binomial(M_,k)*p**k*(1-p)**(M_-k) for k in range(N)] for p in (sp.Rational(2,5),sp.Rational(1,2))]
    else:
        w0=[[sp.rf(b+1,k)/sp.factorial(k)*sp.rf(2,M_-k)/sp.factorial(M_-k) for k in range(N)] for b in (sp.Integer(1),sp.Rational(3,2))]
    X=sp.symbols('x0:%d'%N); W=[sp.symbols('w%d_0:%d'%(s,N)) for s in range(2)]
    p=list(X)+list(W[0])+list(W[1]); p0=x0+w0[0]+w0[1]; sub=dict(zip(p,p0))
    eqs=[]; csyms=[]; dc=0
    for s in range(1,N):
        for n in range(s+1):
            m=s-n; c=sp.symbols('c_%d_%d_0:%d'%(n,m,s)); csyms.append(c); dc+=s
            P=lambda t: t**s+sum(c[j]*t**j for j in range(s))
            for (k,src) in [(k,0) for k in range(n)]+[(k,1) for k in range(m)]:
                eqs.append(sum(W[src][l]*X[l]**k*P(X[l]) for l in range(N)))
    allc=[v for c in csyms for v in c]
    # exact c at base point: solve linear systems
    E0=[e.subs(sub) for e in eqs]
    sol=sp.solve(E0,allc,dict=True)[0]
    Mmat=sp.Matrix(E0).jacobian(allc)
    H=sp.Matrix(eqs).jacobian(p).subs(sub).subs(sol)
    nullv=[sp.Matrix([0]*N+list(w0[0])+[0]*N), sp.Matrix([0]*(2*N)+list(w0[1]))]
    return dc, N*(N-1)*(N+1)//3, Mmat.rank(), H.shape, H.rank(), 3*N-2, [ (H*v).norm()==0 for v in nullv]
for N in (3,4,5):
    for fam in ('krawtchouk','hahn'):
        print(N,fam,run(N,fam)); sys.stdout.flush()
