import math
import platform
import sympy as s

u,x=s.symbols('u x')
checks={'polynomials':0,'jet_coordinates':0,'a_rows':0,'support_coordinates':0}
for N in range(2,7):
    M=N-1
    p=(s.Rational(2,5),s.Rational(1,2))
    w=[[s.binomial(M,k)*ps**k*(1-ps)**(M-k) for k in range(N)] for ps in p]
    def B(f):
        return s.Poly(sum(s.binomial(M,k)*f[k]*u**k*(1-u)**(M-k) for k in range(N)),u)
    def mono(k,j):
        return s.Integer(k)**j
    def mom(ws,j):
        return sum(ws[k]*mono(k,j) for k in range(N))
    mus=[[mom(ws,j) for j in range(2*N+1)] for ws in w]
    polys={(0,0):s.Poly(1,x)}
    derivs={(0,0):[s.Poly(0,x) for _ in range(3*N)]}
    for t in range(1,N+1):
        for n in range(t+1):
            nm=(n,t-n)
            rows=[(a,j) for a in range(2) for j in range(nm[a])]
            A=s.Matrix([[mus[a][j+r] for r in range(t)] for a,j in rows])
            Ai=A.inv()
            coef=-Ai*s.Matrix([mus[a][j+t] for a,j in rows])
            P=s.Poly(x**t+sum(coef[r]*x**r for r in range(t)),x)
            polys[nm]=P
            pv=[P.eval(k) for k in range(N)]
            pp=[P.diff().eval(k) for k in range(N)]
            dp=[]
            for h in range(3*N):
                k=h%N
                if h<N:
                    rhs=[w[a][k]*(pp[k]*mono(k,j)+(pv[k]*j*mono(k,j-1) if j else 0)) for a,j in rows]
                else:
                    aa=h//N-1
                    rhs=[w[a][k]*pv[k]*mono(k,j) if a==aa else 0 for a,j in rows]
                dc=-Ai*s.Matrix(rhs)
                dP=s.Poly(sum(dc[r]*x**r for r in range(t)),x)
                dp.append(dP)
                if t==N:
                    expected=-s.prod(x-j for j in range(N) if j!=k) if h<N else 0
                    assert dP==s.Poly(expected,x)
                    checks['support_coordinates']+=1
                else:
                    R=B([dP.eval(j) for j in range(N)])
                    f=B([pv[j] if j==k else 0 for j in range(N)])
                    g=B([pp[j] if j==k else 0 for j in range(N)])
                    for a in range(2):
                        ps=p[a]
                        for r in range(nm[a]):
                            val=R.diff((u,r)).eval(ps)
                            if h<N:
                                val+=g.diff((u,r)).eval(ps)
                                for l in range(1,r+1):
                                    lj=s.factorial(l-1)*((-1)**(l-1)/ps**l+1/(1-ps)**l)
                                    val+=s.binomial(r,l)*f.diff((u,r-l)).eval(ps)*lj
                            elif h//N-1==a:
                                val+=f.diff((u,r)).eval(ps)
                            assert s.cancel(val)==0,(N,nm,h,a,r,val)
                    checks['jet_coordinates']+=1
            derivs[nm]=dp
            if t<=M:
                assert B(pv)==s.Poly(s.factorial(M)/s.factorial(M-t)*(u-p[0])**n*(u-p[1])**(t-n),u)
                checks['polynomials']+=1
    def c(nm,j):
        t=sum(nm)
        return polys[nm].nth(t-j) if j<=t else s.Integer(0)
    def dc(nm,j,h):
        t=sum(nm)
        return derivs[nm][h].nth(t-j) if j<=t else s.Integer(0)
    def hn(nm,a):
        return sum(w[a][k]*polys[nm].eval(k)*mono(k,nm[a]) for k in range(N))
    def dh(nm,a,h):
        P=polys[nm]; dP=derivs[nm][h]; j=nm[a]; k=h%N
        val=sum(w[a][l]*dP.eval(l)*mono(l,j) for l in range(N))
        if h<N:
            val+=w[a][k]*(P.diff().eval(k)*mono(k,j)+(P.eval(k)*j*mono(k,j-1) if j else 0))
        elif h//N-1==a:
            val+=w[a][k]*P.eval(k)*mono(k,j)
        return val
    for t in range(1,M+1):
        for n in range(t+1):
            nm=(n,t-n); up=(n+1,t-n)
            be=c(nm,1)-c(up,1)
            S=c(nm,2)-c(up,2)-be*c(nm,1)
            T=c(nm,3)-c(up,3)-be*c(nm,2)
            active=[a for a in range(2) if nm[a]]
            pred={a:tuple(nm[j]-(j==a) for j in range(2)) for a in active}
            av={a:hn(nm,a)/hn(pred[a],a) for a in active}
            assert S==sum(av.values())
            assert T==sum(av[a]*c(pred[a],1) for a in active)
            for h in range(3*N):
                db=dc(nm,1,h)-dc(up,1,h)
                ds=dc(nm,2,h)-dc(up,2,h)-db*c(nm,1)-be*dc(nm,1,h)
                dt=dc(nm,3,h)-dc(up,3,h)-db*c(nm,2)-be*dc(nm,2,h)
                da={a:(dh(nm,a,h)-av[a]*dh(pred[a],a,h))/hn(pred[a],a) for a in active}
                if len(active)==1:
                    assert ds==da[active[0]]
                else:
                    gap=c(pred[0],1)-c(pred[1],1)
                    assert gap==-s.Rational(M-t+2,10)
                    a1=(dt-ds*c(pred[1],1)-S*dc(pred[1],1,h)-av[0]*(dc(pred[0],1,h)-dc(pred[1],1,h)))/gap
                    assert s.cancel(a1-da[0])==0
                    assert s.cancel(ds-a1-da[1])==0
                checks['a_rows']+=len(active)
print({'result':'PASS','N':list(range(2,7)),'arithmetic':'SymPy exact rationals','python':platform.python_version(),'sympy':s.__version__,'checks':checks})
