#!/usr/bin/env python3
"""Independent exact-rational pair oracle and three frozen failed-box controls."""
import ctypes,hashlib,itertools,json,math,pathlib,resource,sys,time
from fractions import Fraction as F
import check_r9 as r9
ROOT=r9.ROOT;TOPIC=ROOT/'topics/padua-argmax-bridge-20261105'


def main():
    resource.setrlimit(resource.RLIMIT_CPU,(110,115));started=time.process_time()
    sources=r9.python_sources()+[r9.build.identity(pathlib.Path(r9.__file__).with_name('hybrid_kernel_v3.cpp')),r9.build.identity(__file__)]
    kernel=r9.Kernel('round9');fn=kernel.lib.phase_pair_defect
    fn.argtypes=[ctypes.c_double]*4+[ctypes.POINTER(ctypes.c_double)];fn.restype=ctypes.c_int
    counts={};case_records=[]
    def check(ok,label):
        if not ok:raise AssertionError(label)
        counts[label]=counts.get(label,0)+1
    def oracle(b):
        # Direct endpoint evaluation of d, independent of implementation's
        # sign dispatch. The hand proof establishes rectangle extrema occur
        # at these corners, including mixed and zero-touch intervals.
        vals=[abs(F(x))+abs(F(y))-abs(F(x)+F(y)) for x in b[:2] for y in b[2:]]
        return min(vals),max(vals)
    def pair(b,record=False):
        out=(ctypes.c_double*5)();code=fn(*b,out)
        check(code==0,'finite pair returned success')
        vals=list(out);lo,hi=oracle(b)
        check(all(math.isfinite(x) for x in vals),'pair outputs finite')
        check(0<=F(vals[0])<=lo,'positive lower safe')
        check(F(vals[2])<=lo and F(vals[3])>=hi,'old natural enclosure safe')
        check(max(F(0),F(vals[0]),F(vals[2]))==F(vals[4])<=lo,'maximum lower safe')
        check(vals[0]<=vals[1],'lower-point output ordered')
        if lo==0:check(vals[0]==0 and vals[4]==0,'zero/mixed rectangle exact zero floor')
        if b==[1.,1.,-1.,-1.]:check(vals[0]==2 and vals[4]==2,'opposite singleton exact two')
        if record:case_records.append(dict(box=b,true_infimum=str(lo),true_supremum=str(hi),outputs=vals))
    endpoints=[-3.,-1.,0.,1.,3.]
    intervals=[(x,y) for i,x in enumerate(endpoints) for y in endpoints[i:]]
    for x,y in itertools.product(intervals,repeat=2):pair([*x,*y])
    tiny=math.ulp(0.0)
    special=[
        [1.,1.,-1.,-1.],[1.,4.,-9.,-2.],[-9.,-2.,1.,4.],
        [0.,1.,-2.,-1.],[-0.,0.,-1.,1.],[-1.,1.,2.,3.],
        [1.,math.nextafter(1.,math.inf),-2.,-1.],
        [tiny,tiny,-tiny,-tiny],[tiny,2*tiny,-4*tiny,-3*tiny],
        [2.**500,2.**501,-2.**502,-2.**501],
        [2.**-500,2.**-499,-2.**-498,-2.**-499],
        [2.**1022,2.**1022,-2.**1022,-2.**1022],
    ]
    for b in special:pair(b,True)
    for b in [[2.,1.,0.,1.],[0.,1.,2.,1.],[math.nan,1.,0.,1.],[0.,math.inf,0.,1.],[0.,1.,-math.inf,0.]]:
        out=(ctypes.c_double*5)();check(fn(*b,out)!=0,'malformed pair rejected')
    large=sys.float_info.max;out=(ctypes.c_double*5)()
    check(fn(large,large,-large,-large,out)!=0,'unrepresentable doubled output rejected')
    candidate=ROOT/'local-output/argmax-bridge-20261105/bootstrap-r8/n32/n32-phase-compact.json'
    old=ROOT/'local-output/argmax-bridge-20261105/bootstrap-r8/checker-n32/checker-report.json'
    cident=r9.build.identity(candidate);oident=r9.build.identity(old)
    check(cident['sha256']=='97c339181652d37e7e3c34522959f1b7157b8ea26d3f0ab83c0ebc1c3901528e','original candidate identity')
    check(oident['sha256']=='b7801039c828a200f46aa44787cca370e6fcc09c1e300f196d160b76877107a1','frozen failed receipt identity')
    data=r9.acceptance.strict_json(candidate.read_bytes());prior=r9.acceptance.strict_json(old.read_bytes())
    failed={(v['root'],v['path']):v for v in prior['failed_leaves']}
    selected=[]
    for root,path in [(0,'111111111'),(0,'111111011'),(0,'1111111001')]:
        previous=failed[(root,path)];b=r9.acceptance.box_for(data['roots'],root,path)
        bounds=kernel.bounds(32,b);su,cu,dl,lc=map(F,bounds[:4])
        check(r9.acceptance.bootstrap_range(32,b),'selected box unchanged bootstrap geometry')
        check(all(bounds[k]==previous['bounds'][k] for k in [0,1,3,4,5,6]),'unchanged nondefect numerical outputs')
        check(dl>=F(previous['bounds'][2]),'selected defect never weakened')
        check(dl>0,'selected defect positive')
        check(su-dl<lc,'selected strict comparison passes')
        selected.append(dict(root=root,path=path,box=b,previous_bounds=previous['bounds'],new_bounds=bounds,exact_strict_excess=str(su-dl-lc)))
    r9.verify(sources)
    check(r9.build.identity(candidate)==cident and r9.build.identity(old)==oident,'original input and failed report unchanged')
    local=ROOT/'local-output/argmax-bridge-20261105/phase-r9/independent-controls';local.mkdir(exist_ok=False)
    raw=local/'build-provenance.json';raw.write_text(json.dumps(kernel.provenance,indent=2)+'\n')
    report=dict(format='phase-r9-independent-controls-v1',status='PASS',pair_rectangles=225+len(special),control_assertions=sum(counts.values()),counts=counts,
                special_pair_cases=case_records,selected_failed_boxes=selected,full_cover_executed=False,new_candidate_or_tree=False,
                independent_oracle='exact Fraction evaluation of d at all four rectangle corners; no producer import or arithmetic',
                candidate=cident,prior_failed_receipt=oident,sources=sources,build_provenance=r9.build.identity(raw),
                kernel_binary=kernel.provenance['checker_binary'],own_cpu_seconds=time.process_time()-started,
                compiler_build_helper_cpu_seconds=sum(getattr(resource.getrusage(resource.RUSAGE_CHILDREN),k) for k in ['ru_utime','ru_stime']))
    text=json.dumps(report,indent=2)+'\n'
    if len(text.encode())>=16384:raise RuntimeError('essential receipt exceeds16KiB')
    (TOPIC/'evidence/phase-r9-review.json').write_text(text)
    print(json.dumps({k:report[k] for k in ['status','pair_rectangles','control_assertions','own_cpu_seconds','compiler_build_helper_cpu_seconds']}))
if __name__=='__main__':main()
