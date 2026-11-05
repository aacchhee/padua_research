#!/usr/bin/env python3
"""Fast repository-only certificate check; no producer import, raw data, or fitting.

Each entry encloses the exact logarithm of an original rational squared endpoint,
scaled by 1/2. Interval minima therefore enclose the exact comparator minimum.
An exact endpoint-defined corner is admissible even when its enclosure spills
outside the original box. Its strictly positive late-half-early enclosure proves
that the universal predicate fails. Input authenticity rests on source pins and
archival provenance; this does not regenerate the original rational endpoints.
"""
import hashlib,json,pathlib
from fractions import Fraction as F

class Interval:
    def __init__(self,a,b=None):
        self.a,self.b=F(a),F(a if b is None else b)
        assert self.a<=self.b
    def __add__(self,y):
        if not isinstance(y,Interval):y=Interval(y)
        return Interval(self.a+y.a,self.b+y.b)
    __radd__=__add__
    def __neg__(self):return Interval(-self.b,-self.a)
    def __sub__(self,y):return self+-y
    def __mul__(self,c):
        c=F(c);return Interval(min(self.a*c,self.b*c),max(self.a*c,self.b*c))
    __rmul__=__mul__
    def json(self):return [str(self.a),str(self.b)]

def minimum(xs):return Interval(min(x.a for x in xs),min(x.b for x in xs))
def check(path):
    b=path.read_bytes();o=json.loads(b);assert len(b)<16384
    assert o['schema']=='g1-compact-log-endpoints-v1' and o['scale']==10**15
    assert o['source_manifest']['sha256']=='8bd04bb6502762a61d53d5633f6737786315d743b6e408e689d647ac7998c144'
    assert o['source_report']['sha256']=='5211917f379060bfa5f477354bbe0cf29066dba76d85d428d43de34a6190176b'
    assert o['frozen_log_code']['sha256']=='18eea30277a3d2d58aab8ece2f15b33e83a1178d5b03e96180229b41a247aeac'
    assert [(r[0],r[1]) for r in o['rows']]==[(n,r) for n in range(2,21) for r in ['bj','mirror','alt','pivot']]
    assert {c['rule'] for c in o['source_cases']}=={'bj','mirror','alt','pivot'}
    scale=o['scale'];rows={}
    for n,r,ll,lh,ul,uh in o['rows']:
        assert all(type(v) is int for v in [ll,lh,ul,uh])
        assert 0<=lh-ll<=1 and 0<=uh-ul<=1 and ll<=uh
        rows[n,r]=(Interval(F(ll,scale),F(lh,scale)),Interval(F(ul,scale),F(uh,scale)))
    A=[];B=[]
    for n in range(2,21):
        l,u=rows[n,'bj'];comps=[rows[n,r] for r in ['mirror','alt','pivot']]
        A.append(l-minimum([x[1] for x in comps]));B.append(u-minimum([x[0] for x in comps]))
        assert A[-1].b<=B[-1].a
    # OLS slope on 2..10: (n-6)/60. On 11..20: (2n-31)/165.
    early=[F(n-6,60) if n<=10 else F(0) for n in range(2,21)]
    late=[F(2*n-31,165) if n>=11 else F(0) for n in range(2,21)]
    coeff=[l-e/2 for e,l in zip(early,late)]
    tau=[F(1) if c>0 else F(0) if c<0 else F(1,2) for c in coeff]
    Y=[a*(1-t)+b*t for a,b,t in zip(A,B,tau)]
    margin=sum((y*c for y,c in zip(Y,coeff)),Interval(0))
    emin=sum(((a if c>=0 else b)*c for a,b,c in zip(A,B,early)),Interval(0))
    midpoint_margin=sum((((a+b)*F(1,2))*c for a,b,c in zip(A,B,coeff)),Interval(0))
    assert margin.a>0 and emin.a>0 and midpoint_margin.a>0
    return dict(grid=o['grid'],table_sha256=hashlib.sha256(b).hexdigest(),rows=76,status='INCONCLUSIVE, certified counterchoice',tau=[str(t) for t in tau],late_minus_half_early=margin.json(),early_minimum=emin.json(),midpoint_late_minus_half_early=midpoint_margin.json(),source_scope='Rounded outward original per-rule endpoint logs; comparator minima independently reconstructed')

def main():
    root=pathlib.Path(__file__).resolve().parents[1]
    out=[check(root/'evidence'/f'g1-compact-{g}.json') for g in ['triangle','rotated']]
    assert [x['grid'] for x in out]==['triangle','rotated']
    print(json.dumps(dict(status='PASS compact finite G1 certificates; both INCONCLUSIVE',checks=out),indent=1))
if __name__=='__main__':main()
