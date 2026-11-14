#!/usr/bin/env python3
"""Round6 independent Arb replay with the published n2..128 range premise.
No producer imports; reviewed arithmetic and old check.py remain unchanged.

Certificate numbers S_upper/corner_upper/defect_lower are diagnostic only.
Acceptance is recomputed with this backend's bounds, not supplied numbers.
"""
import argparse, ctypes, hashlib, json, math, pathlib, time, sys
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
import build_snapshot
from fractions import Fraction as F

ROOT=pathlib.Path(__file__).resolve().parents[4]
class Invalid(ValueError): pass

def rational(x):
    if type(x) not in (int,float) or not math.isfinite(x): raise Invalid('nonfinite or nonnumeric endpoint')
    return F(x)

class Kernel:
    def __init__(self,kernel_variant="baseline"):
        binary,self.provenance=build_snapshot.build(kernel_variant)
        self.lib=ctypes.CDLL(str(binary)); self.fn=self.lib.phase_bounds
        self.provenance['loaded_dependency_closure']=build_snapshot.loaded_closure(self.provenance)
        self.fn.argtypes=[ctypes.c_int]+[ctypes.c_double]*4+[ctypes.POINTER(ctypes.c_double)]
        self.fn.restype=ctypes.c_int
    def bounds(self,n,b):
        out=(ctypes.c_double*7)()
        if self.fn(n,*b,out): raise Invalid('kernel rejected inputs')
        return list(out)

RANGE_RECEIPT_SHA='e685674c028bc99e42d547e8b84a2ce5a7e7e67c3cc69f6c29a55ecbcffd23c0'
RANGE_RECEIPT_PATH='topics/padua-argmax-bridge-20261105/evidence/independent-corner-range.json'
# Only executable code and certificate/evidence data are validation pins.
# Legacy prose references embedded in the published evidence are not guards.
CODE_DATA_PINS={
 'topics/padua-argmax-bridge-20261105/code/check_corner_exact.cpp':('3646f4e8b6b16957b9e1114f95ad2f0a7c18eec4687b49d5e6f1947a25eea6e3',5725),
 'topics/padua-argmax-bridge-20261105/code/check_corner_range.py':('66fc2d9583260572125bd6c70a943577f94f1dd1ce2755a2c47ad96fffa9a982',7416),
 'topics/padua-argmax-bridge-20261105/evidence/n3-corner-batch.json':('97e20cc877ad5afd0c9dfe96c1e399a42d820b38c18626e2b69bfa54f6acfc88',3601),
 'topics/padua-argmax-bridge-20261105/evidence/independent-corner-replay.json':('573afc5d5ae229b0fa1d47df9b6bf334e47e0e437288a3543826838e5403cb4b',7892),
}

def _validate_range_contents(receipt,read_code_data):
    # Private semantic validator for the fixed published receipt; unit tests
    # may exercise failures directly. Production always checks SHA first.
    if receipt.get('schema')!='independent-corner-range-v1' or receipt.get('status')!='PASS':raise Invalid('range receipt schema/status mismatch')
    degrees=receipt.get('input_degrees')
    if not isinstance(degrees,list) or any(type(n) is not int for n in degrees) or degrees!=list(range(2,129)):raise Invalid('range receipt degree coverage mismatch')
    if receipt.get('common_kappa')!='1/16000' or receipt.get('scaled_phase_square_radius')!='1/128':raise Invalid('range receipt constants mismatch')
    counters=receipt.get('counters')
    if not isinstance(counters,dict):raise Invalid('range counters missing')
    for name,value in {'requested':127,'attempted':127,'completed':127,'passed':127,'failed':0,'unrun':0}.items():
        if type(counters.get(name)) is not int or counters[name]!=value:raise Invalid('range counter mismatch: '+name)
    if receipt.get('all_integer_inputs_ran_and_passed') is not True or receipt.get('failure') is not None:raise Invalid('range execution/pass premise missing')
    references=receipt.get('frozen_reference_identities')
    if not isinstance(references,list):raise Invalid('range reference identities missing')
    entries=[receipt.get('source'),receipt.get('wrapper')]+[r for r in references if isinstance(r,dict) and r.get('path') in CODE_DATA_PINS]
    pinned={}
    for entry in entries:
        if not isinstance(entry,dict) or entry.get('path') not in CODE_DATA_PINS:raise Invalid('range code/data reference mismatch')
        path=entry['path'];sha,size=CODE_DATA_PINS[path]
        if path in pinned or entry.get('sha256')!=sha or type(entry.get('bytes')) is not int or entry['bytes']!=size:raise Invalid('range code/data identity mismatch: '+path)
        raw=read_code_data(path)
        if len(raw)!=size or hashlib.sha256(raw).hexdigest()!=sha:raise Invalid('range code/data bytes mismatch: '+path)
        pinned[path]={'path':path,'sha256':sha,'bytes':size}
    if set(pinned)!=set(CODE_DATA_PINS):raise Invalid('range code/data identity coverage mismatch')
    return list(pinned.values())

def _validate_range_snapshot(raw,read_code_data):
    if hashlib.sha256(raw).hexdigest()!=RANGE_RECEIPT_SHA:raise Invalid('published range receipt identity mismatch')
    return _validate_range_contents(strict_json(raw),read_code_data)

def published_corner_premise():
    # No candidate field, alternate path or caller boolean supplies proof.
    # One immutable evidence snapshot supplies both identity and contents.
    raw=(ROOT/RANGE_RECEIPT_PATH).read_bytes()
    pins=_validate_range_snapshot(raw,lambda path:(ROOT/path).read_bytes())
    return {'receipt_sha256':RANGE_RECEIPT_SHA,'degrees':list(range(2,129)),
            'kappa':'1/16000','phase_square':'1/128','code_data_pins':pins,
            'dependency_scope':'fixed published all-integer finite range theorem; no prose validation pins or caller assertion'}

def local_range(n,b):
    # Called only after the fixed published range premise has been verified.
    if type(n) is not int or not 2<=n<=128:return False
    a=maxabs(*b[:2]);beta=maxabs(*b[2:])
    if max(a,beta)>F(1,128):return False
    return a*a/2+F(n*n,(n+1)**2)*beta*beta/2<=F(1,16000)

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
    if type(n) is not int or not 2<=n<=128: raise Invalid('invalid degree outside published range')
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
    premise=published_corner_premise()
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
            elif kind=='local-corner-plus-defect':ok=(local_inherited(n,b) or (premise is not None and local_range(n,b))) and su-dl<lc
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
            'local_patch':'T251/T369; fixed published kappa=1/16000 integer n2..128 and phase-square 1/128',
            'fixed_corner_premise':premise}

def strict_json(raw):
    def pairs(items):
        result={}
        for key,value in items:
            if key in result:raise Invalid('duplicate JSON key: '+key)
            result[key]=value
        return result
    def bad(value):raise Invalid('nonfinite JSON constant: '+value)
    data=json.loads(raw,object_pairs_hook=pairs,parse_constant=bad)
    def validate(value):
        if isinstance(value,float) and not math.isfinite(value):raise Invalid('nonfinite JSON number')
        if isinstance(value,dict):
            for item in value.values():validate(item)
        elif isinstance(value,list):
            for item in value:validate(item)
    validate(data)
    if not isinstance(data,dict):raise Invalid('top-level JSON must be an object')
    return data

def main():
    ap=argparse.ArgumentParser();ap.add_argument('candidate',type=pathlib.Path);ap.add_argument('--output',type=pathlib.Path)
    ap.add_argument('--max-leaves',type=int)
    ap.add_argument('--kernel',choices=('round5',),default='round5')
    args=ap.parse_args();t=time.process_time()
    # One byte snapshot supplies both the checked object and its identity.
    raw=args.candidate.read_bytes();candidate_sha=hashlib.sha256(raw).hexdigest()
    provenance=None
    python_paths=[pathlib.Path(__file__),pathlib.Path(build_snapshot.__file__)]
    python_sources=[build_snapshot.identity(p) for p in python_paths]
    try:
        data=strict_json(raw);kernel=Kernel(args.kernel);provenance=kernel.provenance
        report=check(data,kernel,args.max_leaves)
        if python_sources!=[build_snapshot.identity(p) for p in python_paths]:raise Invalid('checker Python source changed during replay')
        if build_snapshot.identity(pathlib.Path(provenance['checker_binary']['path']))!=provenance['checker_binary']:raise Invalid('checker binary changed during replay')
    except (Invalid,ValueError,KeyError,TypeError,RuntimeError) as e:report={'accepted':False,'error':str(e)}
    report['candidate_sha256']=candidate_sha;report['candidate_bytes']=len(raw)
    report['build_provenance']=provenance
    report['checker_python_sources']=python_sources
    report['cpu_seconds']=time.process_time()-t
    text=json.dumps(report,indent=2)
    if args.output:args.output.write_text(text+'\n')
    print(text)
    return 0 if report.get('accepted') else 1
if __name__=='__main__':raise SystemExit(main())
