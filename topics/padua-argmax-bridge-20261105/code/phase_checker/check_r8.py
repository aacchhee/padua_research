#!/usr/bin/env python3
"""Explicit r8 global-maximum certificate. MPFR producer arithmetic is never imported.
The old pointwise corner predicates are unchanged; bootstrap is a separate kind.
"""
import argparse, ctypes, hashlib, json, math, pathlib, sys, time
from fractions import Fraction as F
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
import check_r6 as legacy
import build_snapshot
from check_r6 import (Invalid, rational, tree_partition, box_for, minabs, maxabs,
                      local_inherited, local_range, published_corner_premise, strict_json, Kernel)
ROOT=pathlib.Path(__file__).resolve().parents[4]
ENERGY_PATH='topics/padua-argmax-bridge-20261105/evidence/independent-bootstrap-energy.json'
ENERGY_SHA='f0c48ea7f55e3a926b36537ebe46724b4305cacb9f1254c6417b2abd9676425b'
ENERGY_PINS={
 'topics/padua-argmax-bridge-20261105/code/check_corner_exact.cpp':'3646f4e8b6b16957b9e1114f95ad2f0a7c18eec4687b49d5e6f1947a25eea6e3',
 'topics/padua-argmax-bridge-20261105/code/check_bootstrap_energy.py':'915c6c7c40e8c9e0c748cf50c2fe278f6760d79a9e725939aed1553269030972',
}

def require(ok,message):
    if not ok:raise Invalid(message)

def bootstrap_descriptor():
    return dict(receipt_sha256=ENERGY_SHA,degree_first=2,degree_last=128,
                normalized_threshold='3/4',phase_diamond_radius='1/2')

def bootstrap_range(n,b):
    # Exact rational endpoint predicate. No bool degree, nonfinite, reversed,
    # string endpoint, or arbitrary caller-supplied premise is admissible.
    if type(n) is not int or not 2<=n<=128:return False
    if not isinstance(b,(list,tuple)) or len(b)!=4:return False
    try:
        q=[rational(x) for x in b]
    except (Invalid,OverflowError,ValueError):return False
    return q[0]<=q[1] and q[2]<=q[3] and max(abs(q[0]),abs(q[1]))+max(abs(q[2]),abs(q[3]))<=F(1,2)

def _validate_bootstrap_contents(d,read):
    require(isinstance(d,dict),'bootstrap receipt object required')
    require(d.get('format')=='padua-independent-bootstrap-energy-v1','bootstrap schema')
    for key in ('accepted','independent_execution','every_integer_degree_checked',
                'all_native_exit_statuses_zero','all_new_predicates_passed',
                'all_masks_cardinal_counts_and_positive_denominators_verified'):
        require(d.get(key) is True,'bootstrap receipt flag: '+key)
    require(d.get('producer_endpoints_imported') is False,'bootstrap independence')
    for key,value in [('degree_first',2),('degree_last',128),('degree_count',127)]:
        require(type(d.get(key)) is int and d[key]==value,'bootstrap degree coverage: '+key)
    require(d.get('normalized_threshold')=='3/4' and d.get('predicate')=='4*energy_upper <= 3*n^4*corner_lower','bootstrap exact threshold')
    source,runner=ENERGY_PINS.values()
    require(d.get('source_sha256')==source and d.get('runner_sha256')==runner,'bootstrap code references')
    require(isinstance(d.get('build'),dict) and d['build'].get('source_sha256')==source and type(d['build'].get('exit_status')) is int and d['build']['exit_status']==0,'bootstrap successful source build')
    pins=[]
    for path,sha in ENERGY_PINS.items():
        raw=read(path);require(hashlib.sha256(raw).hexdigest()==sha,'bootstrap code bytes: '+path)
        pins.append(dict(path=path,sha256=sha,bytes=len(raw)))
    # The fixed independent receipt is the accepted finite theorem evidence.
    # Its frozen execution-manifest identity is checked as data identity here;
    # bulk raw endpoints are regenerable and are not proof inputs to this cover.
    require(d.get('raw_execution_manifest')=='local-output/argmax-bridge-20261105/check-bootstrap/executions.json' and d.get('raw_execution_manifest_sha256')=='a0e8a38fa7d2f9d341bdf43d3555c1851a31e540e8d982116bb02441b63a874a' and type(d.get('raw_execution_manifest_bytes')) is int and d['raw_execution_manifest_bytes']==111214,'bootstrap execution evidence identity')
    n2=d.get('n2_control')
    require(isinstance(n2,dict) and n2==dict(both_enclosed=True,corner_exact='3',energy_exact='331/18',nonzero_cardinals=5,zero_cardinals_omitted=1),'bootstrap n2 control')
    require(n2['both_enclosed'] is True and type(n2['nonzero_cardinals']) is int and type(n2['zero_cardinals_omitted']) is int,'bootstrap n2 control exact types')
    worst=F(d['worst_normalized_energy_upper'])
    require(0<worst<=F(3,4) and type(d.get('worst_normalized_energy_degree')) is int and 2<=d['worst_normalized_energy_degree']<=128,'bootstrap worst ratio')
    return pins

def _validate_bootstrap_snapshot(raw,read):
    require(hashlib.sha256(raw).hexdigest()==ENERGY_SHA,'fixed independent bootstrap receipt identity')
    return _validate_bootstrap_contents(strict_json(raw),read)

def published_bootstrap_premise():
    raw=(ROOT/ENERGY_PATH).read_bytes()
    pins=_validate_bootstrap_snapshot(raw,lambda p:(ROOT/p).read_bytes())
    return dict(**bootstrap_descriptor(),receipt_path=ENERGY_PATH,code_data_pins=pins,
                scope='fixed independent finite energy theorem n2..128; no caller premise or prose pins')

def check(data,kernel,max_leaves=None):
    if not isinstance(data,dict):raise Invalid('certificate object required')
    if max_leaves is not None and (type(max_leaves) is not int or max_leaves<0):raise Invalid('invalid leaf cap')
    if data.get('format')!='n3-phase-maximum-bootstrap-v2': raise Invalid('unknown format')
    if data.get('mode')!='global-maximum-bootstrap':raise Invalid('unknown certificate mode')
    if data.get('bootstrap_premise')!=bootstrap_descriptor():raise Invalid('candidate bootstrap premise mismatch')
    bootstrap=published_bootstrap_premise()
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
    if any(not isinstance(item,dict) for item in leaves+pending):raise Invalid('leaf objects required')
    tree_partition(leaves+pending)
    if type(data.get('complete')) is not bool or data['complete'] != (not pending):raise Invalid('false completion flag')
    premise=published_corner_premise()
    checked=[];failed=[]
    for item in leaves[:max_leaves]:
        b=box_for(expected,item['root'],item['path']);kind=item.get('kind')
        if kind=='outside':
            ok=minabs(*b[:2])+minabs(*b[2:])>pu;bounds=None
        elif kind in ('far','local-corner-plus-defect','corner-orbit-plus-defect','maximum-exclusion-plus-defect'):
            bounds=kernel.bounds(n,b);su,cu,dl=map(F,bounds[:3])
            # T366 applies only on the full box's |a|+|b|<=1/10 region.
            if n>=48 and maxabs(*b[:2])+maxabs(*b[2:])<=F(1,10):dl=max(dl,F(1,8192))
            if kind=='far':ok=su<lc
            elif kind=='local-corner-plus-defect':ok=(local_inherited(n,b) or (premise is not None and local_range(n,b))) and su-dl<lc
            elif kind=='maximum-exclusion-plus-defect':ok=bootstrap_range(n,b) and su-dl<lc
            else:ok=cu<lc and su-dl<lc
        else:raise Invalid('unknown leaf predicate')
        result={'root':item['root'],'path':item['path'],'kind':kind,'valid':bool(ok),'bounds':bounds}
        checked.append(result)
        if not ok:failed.append(result)
    if published_bootstrap_premise()!=bootstrap or published_corner_premise()!=premise:raise Invalid('premise closure changed during replay')
    all_checked=len(checked)==len(leaves)
    return {'accepted':not pending and all_checked and not failed,'complete':not pending,
            'n':n,'checked_leaves':len(checked),'total_leaves':len(leaves),'pending':len(pending),
            'failed_leaves':failed,'replay':checked,'independent_constants':own[3:],
            'arithmetic':'FLINT 3.1.3 Arb 160-bit balls; exact rational acceptance/geometry',
            'supplied_numeric_leaf_bounds':'ignored; predicates recomputed independently',
            'local_patch':'T251/T369; fixed published kappa=1/16000 integer n2..128 and phase-square 1/128',
            'fixed_corner_premise':premise,'fixed_bootstrap_premise':bootstrap,
            'conclusion':'global maximum equals corner value with exactly two nonnode corner maximizers',
            'bootstrap_leaf_scope':'maximum exclusion only for actual corner classes; strict defect bound for all noncorner classes'}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('candidate',type=pathlib.Path);ap.add_argument('--output',type=pathlib.Path)
    ap.add_argument('--max-leaves',type=int)
    ap.add_argument('--kernel',choices=('round5',),default='round5')
    args=ap.parse_args();t=time.process_time()
    # One byte snapshot supplies both the checked object and its identity.
    raw=args.candidate.read_bytes();candidate_sha=hashlib.sha256(raw).hexdigest()
    provenance=None
    python_paths=[pathlib.Path(__file__),pathlib.Path(build_snapshot.__file__),pathlib.Path(legacy.__file__)]
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
