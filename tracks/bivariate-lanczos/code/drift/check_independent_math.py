#!/usr/bin/env python3
"""Supplementary independent checks, not a computer proof or rounding theorem.

Own Fraction implementation, monomial Gram-Schmidt, and differentiation of
every coefficient. Imports no development implementation for these checks.
E5 high-precision evaluation corroborates the separately reconstructed proof.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
import platform
from pathlib import Path


def dot(u, v):
    return sum((a*b for a, b in zip(u, v)), Q(0))


def add(u, v, a=Q(1)):
    return [x+a*y for x, y in zip(u, v)]


def product(u, v):
    return [a*b for a, b in zip(u, v)]


def project_normal(v, basis, norms):
    out = list(v)
    for b, d in zip(basis, norms):
        out = add(out, b, -dot(v, b)/d)
    return out


def check_e1(rule):
    # A square unrotated grid would hide some coefficient paths; a triangle
    # with 15 points keeps degree-2 output codimension positive.
    pts = [(Q(i, 2)-1, Q(j, 2)-1) for i in range(5) for j in range(5-i)]
    M, degree = len(pts), 2
    meta = [(t, j) for t in range(degree+1) for j in range(t+1)]
    coords = [[p[a] for p in pts] for a in (0, 1)]
    index = {ij:k for k,ij in enumerate(meta)}
    # Independent canonical construction from monomials, not selected parents.
    basis, norms = [], []
    for t, j in meta:
        m = [x**(t-j)*y**j for x,y in pts]
        b = project_normal(m, basis, norms)
        d = dot(b,b)
        assert d > 0
        basis.append(b)
        norms.append(d)
    N = len(basis)
    assert all(dot(basis[i],basis[j]) == (norms[i] if i==j else 0)
               for i in range(N) for j in range(N))
    rec = [None]
    for k,(t,j) in enumerate(meta[1:],1):
        allowed = ([0] if j==0 else [1] if j==t else [0,1])
        if rule != 'pivot':
            desired = (0 if j==0 else 1) if rule=='bj' else (
                (1 if j==t else 0) if rule=='mirror' else (0 if 2*j<t else 1))
            allowed = [desired]
        candidates=[]
        for a in allowed:
            p=index[(t-1,j-a)]
            u=product(coords[a],basis[p])
            alpha=[dot(u,b)/d for b,d in zip(basis[:k],norms[:k])]
            res=project_normal(u,basis[:k],norms[:k])
            assert res==basis[k]
            sigma=dot(u,u)
            candidates.append((norms[k]/sigma,-a,a,p,alpha,sigma))
        _,_,a,p,alpha,sigma=max(candidates)
        rec.append((a,p,alpha,sigma))
    rdiag=[1-sum((b[i]*b[i]/d for b,d in zip(basis,norms)),Q(0)) for i in range(M)]
    assert sum(rdiag)==M-N
    lower,total=Q(0),Q(0)
    row_total=[Q(0)]*M
    equalities=0
    for h in range(1,N):
        # Distinct propagation implementation: one scalar recurrence per node.
        g=[[Q(0)]*N for _ in range(M)]
        for i in range(M):
            g[i][h]=Q(1)
            for k in range(h+1,N):
                a,p,alpha,_=rec[k]
                g[i][k]=coords[a][i]*g[i][p]-sum(
                    (alpha[l]*g[i][l] for l in range(k)),Q(0))
        for i in range(M):
            # Differentiate complete Gram-Schmidt coefficient and norm map.
            db=[[Q(0)]*M]
            for k in range(1,N):
                a,p,alpha,_=rec[k]
                u=product(coords[a],basis[p])
                du=product(coords[a],db[p])
                if k==h:
                    du[i]+=1
                out=list(du)
                for l in range(k):
                    da=(dot(du,basis[l])+dot(u,db[l])
                        -2*alpha[l]*dot(basis[l],db[l]))/norms[l]
                    out=add(add(out,basis[l],-da),db[l],-alpha[l])
                db.append(out)
            impulse=[Q(int(z==i)) for z in range(M)]
            ri=project_normal(impulse,basis,norms)
            energy=Q(0)
            for k in range(N):
                normal=project_normal(db[k],basis,norms)
                assert normal==[g[i][k]*z for z in ri]
                energy+=dot(normal,normal)/norms[k]
                equalities+=1
            sigma=rec[h][3]
            expected=sigma*rdiag[i]*sum((z*z/d for z,d in zip(g[i],norms)),Q(0))
            assert sigma*energy==expected
            lower=max(lower,expected)
            total+=expected
            row_total[i]+=sigma*sum((z*z/d for z,d in zip(g[i],norms)),Q(0))
    return {'rule':rule,'point_count':M,'degree':degree,
            'all_input_coordinate_normal_equalities':equalities,
            'Knode_squared':str(lower),'KHS_squared':str(total),
            'Urow_squared':str(max(row_total)),'result':'PASS'}


def check_e5():
    import mpmath as mp
    mp.mp.dps=100
    a=20*mp.pi**3/9
    limit=-6400*mp.pi**12/729
    distance_limit=20*mp.sqrt(2)*mp.pi**4/9
    def f(n,m,t):
        x=mp.pi/n+t
        y=mp.pi/(n+1)+t
        return mp.cos((n-m)*x)*mp.cos(m*y)-mp.cos(m*x)*mp.cos((n+1-m)*y)
    errors=[]
    for n in (4,9,25):
        th,ph=mp.pi/n,mp.pi/(n+1)
        for m in range(4):
            d1=(mp.sin((2*n+1)*m*(th-ph))-(2*n+1)*mp.sin(m*(th-ph)))/2
            d2=-(2*n+1-2*m)*mp.cos(m*th)*mp.cos(m*ph)-2*m*mp.sin(m*th)*mp.sin(m*ph)
            errors.extend([abs(mp.diff(lambda t:f(n,m,t),0)-d1),
                           abs(mp.diff(lambda t:f(n,m,t),0,2)-d2)])
    rows=[]
    for n in (10,20,50,100,300,1000,3000):
        t=a/n**4
        g=[f(n,m,t) for m in range(4)]
        p=9*(g[1]**2-g[0]*g[2]/2)+g[2]**2-g[1]*g[3]
        distance=mp.sqrt((mp.cos(mp.pi/n+t)-mp.cos(mp.pi/n))**2+
                         (mp.cos(mp.pi/(n+1)+t)-mp.cos(mp.pi/(n+1)))**2)
        rows.append({'n':n,'n14P_over_claimed_limit':mp.nstr(n**14*p/limit,30),
                     'n5distance_over_claimed_limit':mp.nstr(n**5*distance/distance_limit,30),
                     'negative':bool(p<0)})
    assert max(errors)<mp.mpf('1e-85')
    return {'status':'MEASURED corroboration of analytic proof; not certified signs',
            'mpmath_version':mp.__version__,'precision_decimal_digits':mp.mp.dps,
            'max_derivative_identity_error':mp.nstr(max(errors),10),'rows':rows}


def check_e4():
    pts=[(i,j) for i in range(4) for j in range(4-i)]
    w=[Q(11*x*x+26*x*y-39*x+6*y*y-26*y+18,23) for x,y in pts]
    r=[Q(y**3)-Q(30,7)*y*y+Q(29,7)*y-Q(6,35) for x,y in pts]
    V=[[Q(1)]*10,[Q(x) for x,y in pts],[Q(y) for x,y in pts],
       [Q(x*x) for x,y in pts],[Q(x*y+2*y*y) for x,y in pts]]
    S2=V+[[Q(x*y) for x,y in pts],[Q(y*y) for x,y in pts]]
    assert all(dot(w,v)==0 for v in V)
    assert all(dot(r,v)==0 for v in S2)
    assert dot(w,w)/10==Q(28,115)
    assert dot(r,r)/10==Q(72,175)
    assert sum(Q(y*y*(x-1)**2) for x,y in pts)/10==Q(3,2)
    for (x,y),wi in zip(pts,w):
        assert x*y-y-wi==(-Q(11,23)*x*x-Q(3,23)*(x*y+2*y*y)
                          +Q(39,23)*x+Q(3,23)*y-Q(18,23))
        # Multiply the Jq_y decomposition by sqrt(3).
        assert x*(x+2*y-3)==2*y*(x-1)+(x*x-3*x+2*y)
    b2=Q(28,115)
    u2=Q(1,16)
    assert Q(345)/(56+345*u2)>=4
    assert 2*b2/(b2+Q(3,2)*u2)>=1
    return {'result':'PASS','points':pts,'w_squared_norm':str(b2),
            'r_squared_norm':str(dot(r,r)/10),
            'v21_squared_norm':'3/2','all_projection_moments_exact_zero':True,
            'relative_budget_inequalities_at_max_u':'PASS'}


def check_e5_family():
    import sympy as sp
    t=sp.Symbol('t',real=True)
    atoms=[(t,t,sp.Rational(1,6)),(-t,-t,sp.Rational(1,6)),
           (sp.Integer(1),sp.Integer(0),sp.Rational(1,3)),
           (sp.Integer(0),sp.Integer(1),sp.Rational(1,3))]
    def moment(a,b):
        return sp.expand(sum(w*x**a*y**b for x,y,w in atoms))
    for k in range(4):
        for a in range(k+1):
            b=k-a
            original=(sp.Rational(int(a==0)+int(b==0),3)
                      +sp.Rational(int(k==0),3))
            assert sp.expand(moment(a,b)-original)==(t*t/3 if k==2 else 0)
    basis=[(0,0),(1,0),(0,1)]
    def gram(a,b):
        return sp.Matrix([[moment(i+k+a,j+l+b) for k,l in basis] for i,j in basis])
    M,X,Y=gram(0,0),gram(1,0),gram(0,1)
    assert sp.simplify(M.det()-(1+6*t*t)/27)==0
    comm=M.inv()*X*M.inv()*Y-M.inv()*Y*M.inv()*X
    expected=t*t*(4*t*t-1)/(1+6*t*t)**2
    assert sp.simplify(comm[0,1]-expected)==0
    x,y=sp.symbols('x y')
    p=x*y*(1-x-y)
    assert all(g.subs({x:xx,y:yy})==0 for xx,yy in [(0,0),(1,0),(0,1)]
               for g in [p,sp.diff(p,x),sp.diff(p,y)])
    assert moment(1,1)-moment(2,1)-moment(1,2)==t*t/3
    return {'result':'PASS','sympy_version':sp.__version__,
            'moment_matrices_built_from_four_atoms':True,
            'determinant':str(sp.factor(M.det())),
            'commutator_01':str(sp.factor(comm[0,1])),
            'double_zero_cubic_jets':'exact zero'}


if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--output',required=True)
    args=p.parse_args()
    result={'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'python':platform.python_version(),
            'E1':[check_e1(r) for r in ('bj','mirror','alt','pivot')],
            'E4':check_e4(),
            'E5':check_e5(),'E5_square_family':check_e5_family()}
    Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
