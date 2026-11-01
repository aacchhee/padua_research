"""Independent audit checks: rational Padua n=2 dual and mass normalization.

No developer/reviewer module imported. The published dual certificate is data.
Python/SymPy exact rationals are the trusted arithmetic dependencies.
"""
from pathlib import Path
import hashlib
import re
import random
import sympy as s

ROOT = Path(__file__).resolve().parents[4]
LOG = ROOT / 'topics/bivariate-lanczos-20261031/directions/L3/logs/exact_certificates.log'
x, y = s.symbols('x y')

def monomials(d):
    return [x**a * y**(t-a) for t in range(d+1) for a in range(t+1)]

def at(p, z):
    return p.subs({x:z[0], y:z[1]})

def padua2():
    text = LOG.read_text()
    section = text.split('Padua n=2:')[1].split('=> (H)')[0]
    rows = re.findall(r'A = \[\[(.*?)\]\]', section)
    cert = []
    for row in rows:
        pairs = re.findall(r'\((-?\d+(?:/\d+)?)\+(-?\d+(?:/\d+)?)r2\)', row)
        assert len(pairs) == 4 and all(s.Rational(b) == 0 for _, b in pairs)
        A = s.Matrix(2, 2, [s.Rational(a) for a, _ in pairs])
        assert A == A.T and A[0,0] > 0 and A.det() > 0
        cert.append(A)
    nodes = [(1,1),(1,-s.Rational(1,2)),(0,s.Rational(1,2)),(0,-1),(-1,1),(-1,-s.Rational(1,2))]
    assert len(cert) == len(nodes)
    mons = monomials(5)
    jet = s.Matrix([[at(s.diff(m,x,dx,y,dy),z) for m in mons]
                    for z in nodes for dx,dy in [(0,0),(1,0),(0,1)]])
    basis = [sum(c*m for c,m in zip(v,mons)) for v in jet.nullspace()]
    H = [s.hessian(p,(x,y)) for p in basis]
    hmap = s.Matrix([[at(h[r,c],z) for h in H] for z in nodes for r,c in [(0,0),(0,1),(1,1)]])
    assert jet.rank()==18 and len(basis)==3 and hmap.rank()==3
    annihilation = [sum(s.trace(A*s.Matrix([[at(v,z) for v in h.row(r)] for r in range(2)]))
                       for z,A in zip(nodes,cert)) for h in H]
    assert annihilation == [0,0,0]
    vand = s.Matrix([[at(m,z) for m in monomials(2)] for z in nodes])
    assert vand.det() != 0
    print('PADUA2 PASS rank jet=18 dim S1=3 rank Hessian=3; all six dual blocks PD; all annihilations zero; Pi2 determinant=',vand.det())
    print('S1 basis=',[s.factor(p) for p in basis])
    print('certificate source sha256=',hashlib.sha256(LOG.read_bytes()).hexdigest())

def normalization_counterexample():
    # Degree n=1 sections; V=Pi3. The ten evaluation vectors form a basis.
    nodes=[(a,t-a) for t in range(4) for a in range(t+1)]
    V=s.Matrix([[at(m,z) for m in monomials(3)] for z in nodes])
    assert V.det()!=0
    target=nodes.index((1,1))
    alpha=s.Rational(1,1000)
    weights=[(1-alpha)/9]*10
    weights[target]=alpha
    eps=2*alpha-alpha**2
    theta=s.Rational(1,2)
    perturbed=weights.copy()
    perturbed[target]-=eps
    # Norm ||sum_i c_i ev_zi|| = ||c||_2, so cone C(K0)=R_+^10,
    # r(0)=min_i weights_i=alpha. Normalization divides by 1-eps.
    G=s.zeros(3)
    for z,w in zip(nodes,perturbed):
        v=s.Matrix([1,z[1],z[0]])
        G+=w*v*v.T
    minors=[G[:k,:k].det() for k in [1,2,3]]
    assert all(d>0 for d in minors)
    r=min(weights)
    threshold=(1-theta)*eps
    dist=(eps-alpha)/(1-eps)
    assert r>threshold and dist>theta*eps
    print('NORMALIZATION COUNTEREXAMPLE: n=1 M=10, determining Pi3 Vandermonde determinant=',V.det())
    print('weights min=',alpha,'epsilon=',eps,'theta=',theta,'r(0)=',r,'(1-theta)epsilon=',threshold)
    print('M1(Lmu+E) Sylvester minors=',minors)
    print('normalized Lhat mass=1; exact distance to C(K0)=',dist,'>',theta*eps,'=theta epsilon')
    print('Unnormalized distance=',eps-alpha,'satisfies full-cone claim; normalized residual version does not.')

def completion_checks():
    rng=random.Random(314)
    for n in range(1,5):
        idx=[(t,j) for t in range(n+2) for j in range(t+1)]
        pos={v:k for k,v in enumerate(idx)}
        N=len(idx)
        F=s.zeros(N)
        J=s.zeros(N)
        rec={}
        for k,(t,j) in enumerate(idx[1:],1):
            parent=pos[(t-1,max(0,j-1))]
            window=list(range(max(0,t-2)*(max(0,t-2)+1)//2,k))
            h=s.Matrix([s.Rational(rng.randint(-3,3),7) for _ in window])
            beta=s.Rational(rng.randint(1,5),3)
            dest=J if j==0 else F
            for l,a in zip(window,h):
                dest[l,parent]=a
            dest[k,parent]=beta
            rec[k]=(parent,window,h,beta)
        for k,(t,j) in enumerate(idx[1:],1):
            if j==0 or t>n:
                continue
            p,W,h,beta=rec[k]
            J[:,k]=(F*J[:,p]-J[:,W]*h)/beta
        count=(n+1)*(n+2)//2
        low=n*(n+1)//2
        Fn=F[:count,:count]
        Jn=J[:count,:count]
        residual=(Fn*Jn-Jn*Fn)[:,:low]
        assert residual==s.zeros(count,low)
        assert Fn!=Fn.T or Jn!=Jn.T
        print('COMPLETION PASS n=',n,'all commutator columns degree<n exactly zero; input pair asymmetric (nonvacuous)')

if __name__=='__main__':
    padua2()
    normalization_counterexample()
    completion_checks()
