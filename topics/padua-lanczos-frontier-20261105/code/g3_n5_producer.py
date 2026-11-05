#!/usr/bin/env python3
"""Bounded n5 G3 proposer; exact acceptance, floating LP proposals only.

See ../g3-n5-methods.md. No result exists until this script actually executes.
Independent verifier must not import this implementation.
"""
import argparse
from fractions import Fraction as F
from math import comb, sqrt
import hashlib
import json
import os
from pathlib import Path
import re
import resource
import platform
import sys
import importlib.metadata
import subprocess
import time


class S:
    """a+b sqrt(5), positive-root embedding, rational exact sign."""
    __slots__ = ('a', 'b')
    def __init__(self, a=0, b=0):
        if isinstance(a, S): self.a, self.b = a.a, a.b
        else: self.a, self.b = F(a), F(b)
    def __add__(self, v):
        v=S(v); return S(self.a+v.a,self.b+v.b)
    __radd__=__add__
    def __neg__(self): return S(-self.a,-self.b)
    def __sub__(self,v): return self+-S(v)
    def __rsub__(self,v): return S(v)+-self
    def __mul__(self,v):
        v=S(v); return S(self.a*v.a+5*self.b*v.b,self.a*v.b+self.b*v.a)
    __rmul__=__mul__
    def __truediv__(self,v):
        v=S(v); den=v.a*v.a-5*v.b*v.b
        if not den: raise ZeroDivisionError
        return self*S(v.a/den,-v.b/den)
    def __pow__(self,k):
        ans=S(1)
        for _ in range(k): ans=ans*self
        return ans
    def __bool__(self): return bool(self.a or self.b)
    def __eq__(self,v):
        v=S(v); return self.a==v.a and self.b==v.b
    def sign(self):
        if not self.a: return (self.b>0)-(self.b<0)
        if not self.b: return (self.a>0)-(self.a<0)
        if (self.a>0)==(self.b>0): return 1 if self.a>0 else -1
        diff=self.a*self.a-5*self.b*self.b
        return ((diff>0)-(diff<0))*(1 if self.a>0 else -1)
    def __abs__(self): return self if self.sign()>=0 else -self
    def __float__(self): return float(self.a)+float(self.b)*sqrt(5)
    def data(self): return [str(self.a),str(self.b)]


class Q:
    """u+v sqrt3 over Q(sqrt5), positive radicals, exact nested signs."""
    __slots__=('u','v')
    def __init__(self,a=0,b=0,c=0,d=0):
        if isinstance(a,Q): self.u,self.v=a.u,a.v
        else: self.u,self.v=S(a,b),S(c,d)
    @classmethod
    def pair(cls,u,v):
        z=cls(); z.u,z.v=S(u),S(v); return z
    def __add__(self,o):
        o=Q(o); return Q.pair(self.u+o.u,self.v+o.v)
    __radd__=__add__
    def __neg__(self): return Q.pair(-self.u,-self.v)
    def __sub__(self,o): return self+-Q(o)
    def __rsub__(self,o): return Q(o)+-self
    def __mul__(self,o):
        o=Q(o); return Q.pair(self.u*o.u+3*self.v*o.v,self.u*o.v+self.v*o.u)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=Q(o); norm=o.u*o.u-3*o.v*o.v
        if not norm: raise ZeroDivisionError
        z=self*Q.pair(o.u,-o.v); return Q.pair(z.u/norm,z.v/norm)
    def __pow__(self,k):
        ans=Q(1)
        for _ in range(k): ans=ans*self
        return ans
    def __bool__(self): return bool(self.u or self.v)
    def __eq__(self,o):
        o=Q(o); return self.u==o.u and self.v==o.v
    def sign(self):
        su,sv=self.u.sign(),self.v.sign()
        if not su: return sv
        if not sv or su==sv: return su
        return (self.u*self.u-3*self.v*self.v).sign()*su
    def __abs__(self): return self if self.sign()>=0 else -self
    def __float__(self): return float(self.u)+float(self.v)*sqrt(3)
    def data(self): return self.u.data()+self.v.data()


class Cap(Exception): pass
DEADLINE=float('inf')
GLOBAL_DEADLINE=float('inf')
def checkcap():
    if time.monotonic()>min(DEADLINE,GLOBAL_DEADLINE): raise Cap('stage wall cap')


def rref(rows):
    a=[[Q(x) for x in row] for row in rows]
    if not a: return a,[]
    piv=[]; r=0
    for c in range(len(a[0])):
        checkcap()
        p=next((i for i in range(r,len(a)) if a[i][c]),None)
        if p is None: continue
        a[r],a[p]=a[p],a[r]
        v=a[r][c]; a[r]=[x/v for x in a[r]]
        for i in range(len(a)):
            if i!=r and a[i][c]:
                v=a[i][c]; a[i]=[x-v*y for x,y in zip(a[i],a[r])]
        piv.append(c); r+=1
        if r==len(a): break
    return a,piv


def kernel(rows):
    a,piv=rref(rows); free=[j for j in range(len(rows[0])) if j not in piv]
    out=[]
    for j in free:
        v=[Q() for _ in rows[0]]; v[j]=Q(1)
        for i,c in enumerate(piv): v[c]=-a[i][j]
        out.append(v)
    return out,piv


def dot(a,b): return sum((x*y for x,y in zip(a,b) if x and y),Q())
MON=[(a,k-a) for k in range(12) for a in range(k+1)]
X=[Q(1),Q(F(1,4),F(1,4)),Q(F(-1,4),F(1,4)),
   Q(F(1,4),F(-1,4)),Q(F(-1,4),F(-1,4)),Q(-1)]
Y=[Q(1),Q(0,0,F(1,2)),Q(F(1,2)),Q(0),Q(F(-1,2)),Q(0,0,F(-1,2)),Q(-1)]
NODES=[(j,k,X[j],Y[k]) for j in range(6) for k in range(7) if (j+k)%2==0]


def node_identities():
    def cheb_u(k,z):
        a,b=Q(1),2*z
        if k==0: return a
        for _ in range(k-1): a,b=b,2*z*b-a
        return b
    for axis,N in [(X,5),(Y,6)]:
        assert axis[0]==1 and axis[-1]==-1
        assert all((a-b).sign()>0 for a,b in zip(axis,axis[1:]))
        assert all(not cheb_u(N-1,z) for z in axis[1:-1])
    assert len(NODES)==21 and len(MON)==78


def values(x,y,dx=0,dy=0):
    xp=[Q(1)]; yp=[Q(1)]
    for _ in range(11): xp.append(xp[-1]*x); yp.append(yp[-1]*y)
    return [Q(0) if a<dx or b<dy else
            comb(a,dx)*comb(b,dy)*xp[a-dx]*yp[b-dy]
            for a,b in MON]


def recover():
    # Actual P5 from PD-T069/144, reconstructed with rational coefficients.
    def add(*ps):
        out={}
        for poly in ps:
            for m,c in poly.items(): out[m]=out.get(m,F(0))+c
        return {m:c for m,c in out.items() if c}
    def scale(c,p): return {m:c*v for m,v in p.items() if c*v}
    def mul(p,q):
        out={}
        for (a,b),c in p.items():
            for (u,v),w in q.items(): out[a+u,b+v]=out.get((a+u,b+v),F(0))+c*w
        return {m:c for m,c in out.items() if c}
    def cheb(k):
        a,b={0:F(1)},{1:F(1)}
        if k==0:return a
        for _ in range(k-1):
            c={i+1:2*v for i,v in b.items()}
            for i,v in a.items(): c[i]=c.get(i,F(0))-v
            a,b=b,{i:v for i,v in c.items() if v}
        return b
    def outer(p,q): return {(i,j):a*b for i,a in p.items() for j,b in q.items()}
    g=[add(outer(cheb(5-m),cheb(m)),scale(-1,outer(cheb(m),cheb(6-m)))) for m in range(4)]
    p=add(scale(9,mul(g[1],g[1])),scale(F(-9,2),mul(g[0],g[2])),mul(g[2],g[2]),scale(-1,mul(g[1],g[3])))
    return {m:Q(c) for m,c in p.items()},{'formula':'P5=9(g1^2-g0*g2/2)+g2^2-g1*g3; g_m=T_(5-m)(x)T_m(y)-T_m(x)T_(6-m)(y)',
        'coefficient_domain':'QQ','construction':'integer Chebyshev recurrence; exact rational polynomial operations'}


def lower(p):
    assert p and any(p.values()) and max(a+b for a,b in p)<=11
    pernode=[]
    for j,k,x,y in NODES:
        checkcap()
        tc={(u,v):sum((c*comb(a,u)*comb(b,v)*x**(a-u)*y**(b-v)
                       for (a,b),c in p.items() if a>=u and b>=v),Q()) for u,v in MON}
        assert all(not tc[g] for g in [(0,0),(1,0),(0,1)])
        hxx=2*tc[2,0]; hxy=tc[1,1]; hyy=2*tc[0,2]
        det=hxx*hyy-hxy*hxy; tr=hxx+hyy
        assert hxx.sign()>0 and det.sign()>0 and tr.sign()>0
        mu=det/tr
        sums={d:sum((abs(tc[a,b]) for a,b in MON if a+b==d),Q()) for d in range(3,12)}
        pernode.append((mu,sums))
    for j in range(21):
        checkcap()
        radius=F(1,2**j)
        margins=[mu/2-sum((s[d]*radius**(d-2) for d in range(3,12)),Q()) for mu,s in pernode]
        if all(v.sign()>=0 for v in margins):
            checkcap()
            return {'L':str(radius),'polynomial':[[a,b,c.data()] for (a,b),c in sorted(p.items())],
                    'node_margins':[v.data() for v in margins]}
    return None


def independent_rows(rows):
    # Row independence is column independence of the transpose.
    return rref(list(map(list,zip(*rows))))[1]


def reconstruct(rows, weights, basis):
    support=[i for i,w in enumerate(weights) if w>1e-9]
    if not all(i in support for i in basis): return None
    sr=[rows[i] for i in support]
    piv=independent_rows(sr)
    d=len(rows[0])
    if len(piv)!=d: return None
    free=[i for i in range(len(sr)) if i not in piv]
    for scale in [10**6,10**9,10**12]:
        lamb=[Q() for _ in sr]
        for i in free: lamb[i]=Q(F(float(weights[support[i]])).limit_denominator(scale))
        rhs=[-sum((lamb[i]*sr[i][j] for i in free),Q()) for j in range(d)]
        aug=[[sr[i][j] for i in piv]+[rhs[j]] for j in range(d)]
        solved,cols=rref(aug)
        if cols[:d]!=list(range(d)): continue
        for j,i in enumerate(piv): lamb[i]=solved[j][-1]
        if all(x.sign()>0 for x in lamb) and all(not sum((lamb[i]*sr[i][j] for i in range(len(sr))),Q()) for j in range(d)):
            return support,lamb
    return None


def upper_grid(q,B,on_accept,records):
    import numpy as np
    from scipy.optimize import linprog
    best=None
    offsets=[(a,b) for a in range(-q,q+1) for b in range(-q,q+1) if 0<a*a+b*b<=q*q]
    for j in range(21):
        checkcap(); U=F(1,2**j); rows=[]; pts=[]; seen=set()
        for node,(_,_,x,y) in enumerate(NODES):
            for a,b in offsets:
                checkcap(); xx=x+U*F(a,q); yy=y+U*F(b,q)
                key=tuple(xx.data()+yy.data())
                if key in seen: continue
                seen.add(key); v=values(xx,yy); ev=[dot(v,col) for col in B]
                if any(ev): rows.append(ev); pts.append([node,str(U*F(a,q)),str(U*F(b,q))])
        basis=independent_rows(rows); d=len(B)
        if len(basis)!=d:
            records.append({'j':j,'rows':len(rows),'status':'INCONCLUSIVE rank'}); continue
        A=np.asarray([[float(z) for z in row] for row in rows]).T
        norm=np.max(np.abs(A),axis=1); A=A/norm[:,None]
        bounds=[(1,None) if i in basis else (0,None) for i in range(len(rows))]
        lp=linprog(np.ones(len(rows)),A_eq=A,b_eq=np.zeros(d),bounds=bounds,
                   method='highs',options={'time_limit':5.0})
        rec={'j':j,'rows':len(rows),'lp_status':int(lp.status),'status':'INCONCLUSIVE'}
        if lp.success:
            exact=reconstruct(rows,lp.x,basis)
            if exact:
                support,lamb=exact
                cert={'U':str(U),'q':q,'points':[pts[i] for i in support],
                      'weights':[x.data() for x in lamb]}
                # Recheck all acceptance conditions independently of LP return status.
                assert len(independent_rows([rows[i] for i in support]))==d
                assert all(F(pts[i][1])**2+F(pts[i][2])**2<=U*U for i in support)
                assert all(x.sign()>0 for x in lamb)
                assert all(not sum((lamb[t]*rows[i][c] for t,i in enumerate(support)),Q()) for c in range(d))
                checkcap()
                rec['status']='EXACT ACCEPTED'; best=cert
                on_accept(cert)
        records.append(rec)
        print(json.dumps({'q':q,**rec}),flush=True)
    return best,records


def main():
    global DEADLINE, GLOBAL_DEADLINE
    ap=argparse.ArgumentParser(); ap.add_argument('--out',required=True); args=ap.parse_args()
    os.environ['OPENBLAS_NUM_THREADS']='1'
    os.environ['OMP_NUM_THREADS']='1'
    resource.setrlimit(resource.RLIMIT_AS,(2*1024**3,2*1024**3))
    out=Path(args.out); out.mkdir(parents=True,exist_ok=False)
    start=time.monotonic(); GLOBAL_DEADLINE=start+890; receipt={'n':5,'D':11,'scientific_status':'RUNNING',
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'command':[sys.executable]+sys.argv,'cwd':os.getcwd(),
        'git_head':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),
        'environment':{'python':sys.version,'platform':platform.platform(),
                       'numpy':importlib.metadata.version('numpy'),
                       'scipy':importlib.metadata.version('scipy')}}
    try:
        DEADLINE=time.monotonic()+10; p,source=recover(); receipt['input']=source
        node_identities()
        assert Q(0,1).sign()==1 and Q(-2,1).sign()==1 and Q(-3,1).sign()==-1
        assert Q(0,0,1).sign()==1 and Q(-1,0,1).sign()==1 and Q(-2,0,1).sign()==-1
        checkcap()
        DEADLINE=time.monotonic()+150
        J=[values(x,y,dx,dy) for _,_,x,y in NODES for dx,dy in [(0,0),(1,0),(0,1)]]
        B,piv=kernel(J)
        assert all(not dot(row,col) for row in J for col in B)
        assert len(rref(B)[1])==len(B)==78-len(piv)
        checkcap()
        receipt['kernel']={'shape_J':[63,78],'field_basis':['1','sqrt5','sqrt3','sqrt15'],'rank_J':len(piv),'dimension':len(B),'rank_B':len(B),'pivots_J':piv,'elapsed':time.monotonic()-start}
        print(json.dumps({'kernel':receipt['kernel']}),flush=True)
        DEADLINE=time.monotonic()+60; lower_start=time.monotonic(); lo=lower(p)
        checkcap()
        receipt['lower_elapsed_seconds']=time.monotonic()-lower_start
        if lo:
            lower_raw=json.dumps(lo,indent=2)+'\n'
            if len(lower_raw.encode())>=16384: raise Cap('lower certificate exceeds16KiB')
            (out/'lower.json').write_text(lower_raw)
        receipt['lower']='EXACT ACCEPTED' if lo else 'INCONCLUSIVE'
        if lo is None: raise Cap('no accepted lower on saved grid; upper STOP')
        print(json.dumps({'lower':receipt['lower'],'L':lo['L'] if lo else None,'elapsed':time.monotonic()-start}),flush=True)
        receipt['grids']=[]; best=None
        def save_upper(cert):
            nonlocal best
            if best is None or F(cert['U'])<F(best['U']):
                raw=json.dumps(cert,indent=2)+'\n'
                if len(raw.encode())>=16384: raise Cap('certificate exceeds16KiB')
                best=cert
                (out/'upper.json').write_text(raw)
        for q in [2,4,8]:
            DEADLINE=time.monotonic()+210
            grid={'q':q,'records':[],'status':'RUNNING'}; grid_start=time.monotonic()
            receipt['grids'].append(grid)
            try:
                cert,records=upper_grid(q,B,save_upper,grid['records'])
                grid['status']='COMPLETED'
                if cert and (best is None or F(cert['U'])<F(best['U'])): best=cert
            except Cap as exc:
                grid['status']='CAP'; grid['reason']=str(exc)
            grid['elapsed_seconds']=time.monotonic()-grid_start
            if best:
                raw=json.dumps(best,indent=2)+'\n'
                if len(raw.encode())>=16384: raise Cap('certificate exceeds16KiB')
                (out/'upper.json').write_text(raw)
        receipt['upper']='EXACT ACCEPTED' if best else 'INCONCLUSIVE'
        receipt['scientific_status']='n5 finite certificates; independent verification PENDING'
    except (Cap,AssertionError) as exc:
        receipt['scientific_status']='INCONCLUSIVE'; receipt['error']=repr(exc)
    finally:
        receipt['elapsed_seconds']=time.monotonic()-start
        receipt['peak_rss_KiB']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        (out/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
        print(json.dumps(receipt),flush=True)


if __name__=='__main__': main()
