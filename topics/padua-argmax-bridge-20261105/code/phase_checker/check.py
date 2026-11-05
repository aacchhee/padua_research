#!/usr/bin/env python3
"""Independent Arb replay of N3 candidate leaves. No producer imports.

Certificate numbers S_upper/corner_upper/defect_lower are diagnostic only.
Acceptance is recomputed with this backend's bounds, not supplied numbers.
"""
import argparse, ctypes, hashlib, json, math, pathlib, time
from fractions import Fraction as F

ROOT=pathlib.Path(__file__).resolve().parents[4]
LIB=ROOT/'local-output/argmax-bridge-20261105/phase-checker/libphase_checker.so'
class Invalid(ValueError): pass

def rational(x):
    if type(x) not in (int,float) or not math.isfinite(x): raise Invalid('nonfinite or nonnumeric endpoint')
    return F(x)

class Kernel:
    def __init__(self):
        self.lib=ctypes.CDLL(str(LIB)); self.fn=self.lib.phase_bounds
        self.fn.argtypes=[ctypes.c_int]+[ctypes.c_double]*4+[ctypes.POINTER(ctypes.c_double)]
        self.fn.restype=ctypes.c_int
    def bounds(self,n,b):
        out=(ctypes.c_double*7)()
        if self.fn(n,*b,out): raise Invalid('kernel rejected inputs')
        return list(out)

def tree_partition(items):
    groups=[set() for _ in range(4)]
    for item in items:
        r,p=item.get('root'),item.get('path')
        if type(r) is not int or not 0<=r<4 or not isinstance(p,str) or len(p)>1024 or set(p)-{'0','1'}:
            raise Invalid('invalid root/path')
        if p in groups[r]: raise Invalid('duplicate tree leaf')
        groups[r].add(p)
    for g in groups:
        # Prefix-free is essential; a Kraft sum alone does not imply coverage.
        for p in g:
            if any(p[:i] in g for i in range(len(p))): raise Invalid('overlapping ancestor/descendant leaves')
        while any(g):
            deepest=max(map(len,g),default=0)
            if deepest==0: break
            p=next(p for p in g if len(p)==deepest)
            sibling=p[:-1]+('1' if p[-1]=='0' else '0')
            if sibling not in g: raise Invalid('tree partition has a gap')
            g.remove(p);g.remove(sibling);g.add(p[:-1])
        if g!={''}: raise Invalid('missing root')

def box_for(roots,r,p):
    b=list(roots[r])
    for bit in p:
        # Exact replay of producer's declared IEEE binary64 operation order.
        i=0 if b[1]-b[0]>=b[3]-b[2] else 2
        mid=b[i]+(b[i+1]-b[i])/2
        if not b[i]<mid<b[i+1]: raise Invalid('degenerate or stagnant split')
        b[i+1 if bit=='0' else i]=mid
    return b

def minabs(lo,hi): return F(0) if lo<=0<=hi else min(abs(F(lo)),abs(F(hi)))
def maxabs(lo,hi): return max(abs(F(lo)),abs(F(hi)))
def local_inherited(n,b):
    # 1-cos(t)<=t²/2 for every real t; exact rational arithmetic.
    a=maxabs(*b[:2]);beta=maxabs(*b[2:]);N=n*(n+1)
    H=a*a/(2*n*n)+beta*beta/(2*(n+1)**2)
    return H<=max(F(1,2*N**3),F(1,10**11*n*n))

def check(data,kernel,max_leaves=None):
    if data.get('format')!='n3-phase-candidate-v1': raise Invalid('unknown format')
    n=data.get('n')
    if type(n) is not int or not 2<=n<=512: raise Invalid('invalid degree')
    c=data.get('constants')
    if not isinstance(c,list) or len(c)!=4: raise Invalid('bad constants')
    for v in c:rational(v)
    own=kernel.bounds(n,[0.,0.,0.,0.]);lc=F(own[3]);pu=F(own[6])
    if F(c[0])>F(own[5]) or F(c[1])<pu: raise Invalid('pi constants do not outward-enclose independent pi')
    if F(c[2])>lc or F(c[3])<F(own[4]): raise Invalid('corner constants fail independent enclosure check')
    p=c[1];expected=[[-p,0.,-p,0.],[-p,0.,0.,p],[0.,p,-p,0.],[0.,p,0.,p]]
    if data.get('roots')!=expected: raise Invalid('root geometry mismatch')
    leaves=data.get('leaves');pending=data.get('pending')
    if not isinstance(leaves,list) or not isinstance(pending,list):raise Invalid('bad leaf lists')
    tree_partition(leaves+pending)
    if type(data.get('complete')) is not bool or data['complete'] != (not pending):raise Invalid('false completion flag')
    checked=[];failed=[]
    for item in leaves[:max_leaves]:
        b=box_for(expected,item['root'],item['path']);kind=item.get('kind')
        if kind=='outside':
            ok=minabs(*b[:2])+minabs(*b[2:])>pu;bounds=None
        elif kind in ('far','local-corner-plus-defect','corner-orbit-plus-defect'):
            bounds=kernel.bounds(n,b);su,cu,dl=map(F,bounds[:3])
            # T366 applies only on the full box's |a|+|b|<=1/10 region.
            if n>=48 and maxabs(*b[:2])+maxabs(*b[2:])<=F(1,10):dl=max(dl,F(1,8192))
            if kind=='far':ok=su<lc
            elif kind=='local-corner-plus-defect':ok=local_inherited(n,b) and su-dl<lc
            else:ok=cu<lc and su-dl<lc
        else:raise Invalid('unknown leaf predicate')
        result={'root':item['root'],'path':item['path'],'kind':kind,'valid':bool(ok),'bounds':bounds}
        checked.append(result)
        if not ok:failed.append(result)
    all_checked=len(checked)==len(leaves)
    return {'accepted':not pending and all_checked and not failed,'complete':not pending,
            'n':n,'checked_leaves':len(checked),'total_leaves':len(leaves),'pending':len(pending),
            'failed_leaves':failed,'replay':checked,'independent_constants':own[3:],
            'arithmetic':'FLINT 3.1.3 Arb 160-bit balls; exact rational acceptance/geometry',
            'supplied_numeric_leaf_bounds':'ignored; predicates recomputed independently',
            'local_patch':'inherited T251/T369 only; no new kappa accepted'}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('candidate',type=pathlib.Path);ap.add_argument('--output',type=pathlib.Path)
    ap.add_argument('--max-leaves',type=int);args=ap.parse_args();t=time.process_time()
    try:report=check(json.loads(args.candidate.read_text()),Kernel(),args.max_leaves)
    except (Invalid,ValueError,KeyError,TypeError) as e:report={'accepted':False,'error':str(e)}
    report['candidate_sha256']=hashlib.sha256(args.candidate.read_bytes()).hexdigest()
    report['cpu_seconds']=time.process_time()-t
    text=json.dumps(report,indent=2)
    if args.output:args.output.write_text(text+'\n')
    print(text)
    return 0 if report.get('accepted') else 1
if __name__=='__main__':raise SystemExit(main())
