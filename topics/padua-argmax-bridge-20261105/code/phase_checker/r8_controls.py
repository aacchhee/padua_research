#!/usr/bin/env python3
"""Bounded r8 parser/premise/geometry controls; synthetic bounds are not a proof run."""
import copy, ctypes, hashlib, json, math, pathlib, resource, shutil, subprocess, sys, time
import check_r8 as c


def main():
    resource.setrlimit(resource.RLIMIT_CPU,(110,115))
    start=time.process_time();wall_start=time.monotonic();child_start=resource.getrusage(resource.RUSAGE_CHILDREN);count=0
    def test(ok,label):
        nonlocal count
        if not ok:raise AssertionError(label)
        count+=1
    def rejects(fn,label):
        try:fn()
        except (c.Invalid,ValueError,TypeError,KeyError):test(True,label)
        else:raise AssertionError('accepted malformed control: '+label)
    read=lambda p:(c.ROOT/p).read_bytes()
    raw=(c.ROOT/c.ENERGY_PATH).read_bytes();d=c.strict_json(raw)
    c.published_bootstrap_premise();test(True,'published receipt/code closure')
    for key,val in [('accepted',1),('independent_execution',False),('degree_count',126),
                    ('degree_count',True),('degree_last',129),('normalized_threshold','1'),
                    ('predicate','energy <= threshold'),('producer_endpoints_imported',True),
                    ('runner_sha256','0'*64),('raw_execution_manifest_sha256','0'*64),
                    ('worst_normalized_energy_upper','4/5')]:
        bad=copy.deepcopy(d);bad[key]=val
        rejects(lambda:c._validate_bootstrap_contents(bad,read),key)
    for key in ('both_enclosed','nonzero_cardinals','zero_cardinals_omitted'):
        bad=copy.deepcopy(d);bad['n2_control'][key]=1 if key=='both_enclosed' else True
        rejects(lambda:c._validate_bootstrap_contents(bad,read),'n2 exact type '+key)
    rejects(lambda:c._validate_bootstrap_snapshot(raw+b' ',read),'receipt byte mismatch')
    rejects(lambda:c._validate_bootstrap_contents(d,lambda p:b'wrong'),'code byte mismatch')
    for x in [b'{"n":2,"n":3}',b'{"n":NaN}',b'{"n":1e999}',b'[]']:
        rejects(lambda:c.strict_json(x),'strict JSON')
    inside=[0.,.25,0.,.25]
    test(c.bootstrap_range(32,inside),'diamond exact boundary')
    test(c.bootstrap_range(32,[-.25,0.,-.25,0.]),'opposite inward corner')
    test(c.bootstrap_range(2,[0.,.5,0.,0.]),'n2 boundary')
    test(c.bootstrap_range(128,[0.,math.nextafter(.5,0.),0.,0.]),'below binary boundary')
    for n,b in [(32,[0.,math.nextafter(.5,math.inf),0.,0.]),(32,[0.,.3,0.,.3]),
                (1,inside),(129,inside),(True,inside),(32,[.1,0.,0.,.1]),
                (32,[0.,math.inf,0.,0.]),(32,[0.,math.nan,0.,0.]),
                (32,[False,.25,0.,.25]),(32,['0',.25,0.,.25]),(32,[0.,.5,0.])]:
        test(not c.bootstrap_range(n,b),'malformed/outside geometry')
    # Exact partition exercising the new semantic branch without doing arithmetic.
    class Fake:
        strict=True
        def bounds(self,n,b):return [2. if self.strict else 3.,4.,0.,3.,3.,3.125,3.25]
    roots=[[-3.25,0.,-3.25,0.],[-3.25,0.,0.,3.25],[0.,3.25,-3.25,0.],[0.,3.25,0.,3.25]]
    leaves=[]
    for root in range(4):
        def walk(path,depth):
            b=c.box_for(roots,root,path)
            if c.bootstrap_range(32,b):leaves.append(dict(root=root,path=path,kind='maximum-exclusion-plus-defect'))
            elif depth==8:leaves.append(dict(root=root,path=path,kind='far'))
            else:
                walk(path+'0',depth+1);walk(path+'1',depth+1)
        walk('',0)
    data=dict(format='n3-phase-maximum-bootstrap-v2',mode='global-maximum-bootstrap',
              bootstrap_premise=c.bootstrap_descriptor(),n=32,constants=[3.125,3.25,3.,3.],
              roots=roots,leaves=leaves,pending=[],complete=True)
    result=c.check(data,Fake());test(result['accepted'],'complete synthetic partition')
    test(any(x['kind']=='maximum-exclusion-plus-defect' for x in leaves),'new kind exercised')
    fake=Fake();fake.strict=False
    test(not c.check(data,fake)['accepted'],'bootstrap cannot discharge missing strict noncorner comparison')
    for key,val in [('format','n3-phase-candidate-v1'),('mode','pointwise'),
                    ('bootstrap_premise',{'accepted':True}),('n',129),('n',True),
                    ('leaves',[None]),('complete',False)]:
        bad=copy.deepcopy(data);bad[key]=val
        rejects(lambda:c.check(bad,Fake()),'candidate '+key)
    rejects(lambda:c.check(data,Fake(),-1),'negative leaf cap')
    for mutation in ['duplicate','gap','overlap','unknown','oversize-bootstrap']:
        bad=copy.deepcopy(data)
        if mutation=='duplicate':bad['leaves'].append(copy.deepcopy(bad['leaves'][0]))
        elif mutation=='gap':bad['leaves'].pop()
        elif mutation=='overlap':bad['leaves'].append(dict(root=0,path='',kind='far'))
        elif mutation=='unknown':bad['leaves'][0]['kind']='bootstrap'
        else:
            far=next(x for x in bad['leaves'] if x['kind']=='far');far['kind']='maximum-exclusion-plus-defect'
            test(not c.check(bad,Fake())['accepted'],mutation);continue
        rejects(lambda:c.check(bad,Fake()),mutation)
    # Separate native backend smoke controls, never fake arithmetic acceptance.
    kernel=c.Kernel('round5');bounds=[]
    for b in [[0.,0.,0.,0.],[0.,.25,0.,.25],[0.,math.nextafter(.5,math.inf),0.,0.]]:
        out=kernel.bounds(2,b);test(len(out)==7 and all(math.isfinite(v) for v in out),'independent Arb finite smoke')
        bounds.append(dict(box=b,bounds=out))
    # Fresh unchanged MPFR backend: the explicit flag requests calculation,
    # and never supplies a mathematical pointwise premise.
    sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
    import n3_bootstrap_r8 as producer
    work=c.ROOT/'local-output/argmax-bridge-20261105/bootstrap-r8/controls-mpfr-v2'
    work.mkdir(exist_ok=False)
    source=pathlib.Path(producer.__file__).parent
    originals=[source/'n3_outward.c',source/'n3_outward_interval.h',c.ROOT/'local-output/argmax-bridge-20261105/N3/runtime/extracted/usr/include/mpfr.h']
    for path in originals:shutil.copyfile(path,work/path.name)
    binary=work/'bounds.so'
    argv=['cc','-O3','-std=c11','-shared','-fPIC','-I'+str(work),str(work/'n3_outward.c'),'/lib/x86_64-linux-gnu/libmpfr.so.6','-lm','-o',str(binary)]
    before=resource.getrusage(resource.RUSAGE_CHILDREN)
    subprocess.run(argv,check=True)
    lib=ctypes.CDLL(str(binary));ptr=ctypes.POINTER(ctypes.c_double)
    lib.n3_box.argtypes=[ctypes.c_int,*([ctypes.c_double]*6),ctypes.c_int,ptr];lib.n3_box.restype=ctypes.c_int
    lib.n3_constants.argtypes=[ctypes.c_int,ptr]
    constants=(ctypes.c_double*6)();lib.n3_constants(32,constants)
    b=[0.,.25,0.,.25]
    test(c.bootstrap_range(32,b) and not producer.local_range(32,b),'real bootstrap box outside old local patch')
    skipped=producer.producer_bounds(lib,32,b,constants[2],False)
    computed=producer.producer_bounds(lib,32,b,constants[2],True)
    test(skipped[:2]==computed[:2],'flag leaves S/corner bounds unchanged')
    test(skipped[2]==0. and computed[2]>0.,'explicit request computes previously skipped defect')
    after=resource.getrusage(resource.RUSAGE_CHILDREN)
    mpfr=dict(n=32,box=b,early_exit_bounds=skipped,always_compute_defect_bounds=computed,
              compile_argv=argv,sources=[producer.identity(path) for path in originals],
              binary=producer.identity(binary),compiler_child_cpu_seconds=(after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime))
    child_end=resource.getrusage(resource.RUSAGE_CHILDREN)
    report=dict(format='bootstrap-r8-controls-v2',wall_seconds=time.monotonic()-wall_start,
                total_child_cpu_seconds=child_end.ru_utime+child_end.ru_stime-child_start.ru_utime-child_start.ru_stime,
                status='PASS',controls=count,full_degree_cover_executed=False,
                synthetic_kernel_scope='parser/partition/branch controls only; not numerical proof',
                native_smoke=dict(n=2,boxes=bounds,provenance=kernel.provenance),mpfr_flag_control=mpfr,
                own_cpu_seconds=time.process_time()-start)
    target=c.ROOT/'local-output/argmax-bridge-20261105/bootstrap-r8/controls-v2.json'
    target.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k not in ('native_smoke','mpfr_flag_control')}))

if __name__=='__main__':main()
