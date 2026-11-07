#!/usr/bin/env python3
"""Supplementary r8 adversarial controls. Synthetic verdicts are wiring only."""
import copy, ctypes, hashlib, json, math, pathlib, resource, shutil, subprocess, sys, tempfile, time
import check_r8 as c


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (110,115))
    start=time.process_time(); checks=[]
    def test(ok,label):
        if not ok: raise AssertionError(label)
        checks.append(label)
    def reject(fn,label):
        try: fn()
        except (c.Invalid,ValueError,TypeError,KeyError,OverflowError): checks.append(label)
        else: raise AssertionError('accepted '+label)
    def read(p):
        test(p in c.ENERGY_PINS,'premise read restricted to fixed code')
        return (c.ROOT/p).read_bytes()
    raw=(c.ROOT/c.ENERGY_PATH).read_bytes(); d=c.strict_json(raw)
    c._validate_bootstrap_snapshot(raw,read)
    for key in ['accepted','independent_execution','every_integer_degree_checked','all_native_exit_statuses_zero','all_new_predicates_passed','all_masks_cardinal_counts_and_positive_denominators_verified']:
        for value in [False,1,None]:
            bad=copy.deepcopy(d); bad[key]=value
            reject(lambda:c._validate_bootstrap_contents(bad,read),'receipt '+key+' '+repr(value))
    for key,value in [('degree_first',3),('degree_last',129),('degree_count',127.),('source_sha256','0'*64),('raw_execution_manifest_bytes',111213),('worst_normalized_energy_upper','751/1000'),('worst_normalized_energy_degree',True),('normalized_threshold','0.75')]:
        bad=copy.deepcopy(d);bad[key]=value
        reject(lambda:c._validate_bootstrap_contents(bad,read),'receipt '+key)
    reject(lambda:c._validate_bootstrap_snapshot(raw+b'\n',read),'fixed receipt bytes')
    reject(lambda:c._validate_bootstrap_contents(d,lambda p:(c.ROOT/p).read_bytes()+b'\n'),'fixed code bytes')
    for n in [2,3,32,127,128]:
        for sa in [-1,1]:
            for sb in [-1,1]:
                box=sorted([0.,sa*.25])+sorted([0.,sb*.25])
                test(c.bootstrap_range(n,box),'closed signed diamond '+repr((n,sa,sb)))
    for endpoint in [.5,math.nextafter(.5,0.)]:test(c.bootstrap_range(32,[0.,endpoint,0.,0.]),'axis boundary '+repr(endpoint))
    for box in [[0.,math.nextafter(.5,math.inf),0.,0.],[0.,.25,0.,math.nextafter(.25,math.inf)],[0.,.3,0.,.3],[1.,0.,0.,0.],[0.,0.,False,0.],[0.,float('nan'),0.,0.]]:
        test(not c.bootstrap_range(32,box),'outside/malformed diamond '+repr(box))
    for n in [True,False,1,129,32.,'32']:test(not c.bootstrap_range(n,[0.,0.,0.,0.]),'degree '+repr(n))
    for raw_bad in [b'{"a":1,"a":2}',b'{"a":NaN}',b'{"a":Infinity}',b'{"a":1e999}',b'[]']:
        reject(lambda:c.strict_json(raw_bad),'parser '+repr(raw_bad))
    roots=[[-4.,0.,-4.,0.],[-4.,0.,0.,4.],[0.,4.,-4.,0.],[0.,4.,0.,4.]]
    leaves=[]
    for r in range(4):
        path=''
        while not c.bootstrap_range(32,c.box_for(roots,r,path)):
            a=c.box_for(roots,r,path+'0'); choose='0' if a[0]<=0<=a[1] and a[2]<=0<=a[3] else '1'
            leaves.append(dict(root=r,path=path+('1' if choose=='0' else '0'),kind='far'));path+=choose
        leaves.append(dict(root=r,path=path,kind='maximum-exclusion-plus-defect'))
    class Synthetic:
        delta=3.
        def bounds(self,n,b):
            if b==[0.,0.,0.,0.]:return [3.,3.,0.,3.,3.,3.,4.]
            return ([5.,100.,self.delta] if c.bootstrap_range(n,b) else [2.,100.,0.])+[3.,3.,3.,4.]
    data=dict(format='n3-phase-maximum-bootstrap-v2',mode='global-maximum-bootstrap',bootstrap_premise=c.bootstrap_descriptor(),n=32,constants=[3.,4.,3.,3.],roots=roots,leaves=leaves,pending=[],complete=True)
    test(c.check(data,Synthetic())['accepted'],'synthetic complete bootstrap branch')
    equality=Synthetic();equality.delta=2.
    test(not c.check(data,equality)['accepted'],'strict noncorner equality rejected')
    slight=Synthetic();slight.delta=math.nextafter(2.,0.)
    test(not c.check(data,slight)['accepted'],'exact subtraction above equality rejected')
    old=copy.deepcopy(data)
    for leaf in old['leaves']:
        if leaf['kind']=='maximum-exclusion-plus-defect':leaf['kind']='local-corner-plus-defect'
    test(not c.check(old,Synthetic())['accepted'],'old local predicate not enlarged')
    for mut in ['gap','overlap','duplicate','missing-root','unknown-kind','wrong-mode','old-schema','caller-premise','false-complete','bool-root','bad-path']:
        bad=copy.deepcopy(data)
        if mut=='gap':bad['leaves'].pop()
        elif mut=='overlap':bad['leaves'].append(dict(root=0,path='',kind='far'))
        elif mut=='duplicate':bad['leaves'].append(bad['leaves'][0].copy())
        elif mut=='missing-root':bad['leaves']=[v for v in bad['leaves'] if v['root']!=3]
        elif mut=='unknown-kind':bad['leaves'][0]['kind']='maximum'
        elif mut=='wrong-mode':bad['mode']='pointwise'
        elif mut=='old-schema':bad['format']='n3-phase-candidate-v1'
        elif mut=='caller-premise':bad['bootstrap_premise']={'accepted':True}
        elif mut=='false-complete':bad['complete']=False
        elif mut=='bool-root':bad['leaves'][0]['root']=False
        else:bad['leaves'][0]['path']='x'
        reject(lambda:c.check(bad,Synthetic()),'certificate '+mut)
    partial=copy.deepcopy(data);partial['pending']=[partial['leaves'].pop()];partial['complete']=False
    test(not c.check(partial,Synthetic())['accepted'],'pending forbids acceptance')
    test(not c.check(data,Synthetic(),1)['accepted'],'bounded replay forbids acceptance')
    for cap in [-1,True,1.5]:reject(lambda:c.check(data,Synthetic(),cap),'bad leaf cap '+repr(cap))
    # Real independent Arb integration, including closed boundary, all inward signs,
    # and the physical-center zero-phase distinction. This is no cover proof.
    kernel=c.Kernel('round5');native=[]
    for box in [[0.,0.,0.,0.],[0.,.25,0.,.25],[-.25,0.,-.25,0.],[-.25,0.,0.,.25],[0.,.25,-.25,0.],[.5,.5,0.,0.]]:
        bounds=kernel.bounds(2,box);native.append(dict(box=box,bounds=bounds))
        test(all(math.isfinite(v) for v in bounds),'native finite '+repr(box))
    origin=native[0]['bounds'];test(origin[3]<=3<=origin[4] and origin[0]-origin[2]<origin[3],'n2 origin noncorner strict while corner equality')
    # Separate producer execution control: no MPFR result enters Arb acceptance.
    sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
    import n3_bootstrap_r8 as producer
    work=pathlib.Path(tempfile.mkdtemp(prefix='r8-independent-mpfr-',dir='/tmp'))
    source=pathlib.Path(producer.__file__).parent
    originals=[source/'n3_outward.c',source/'n3_outward_interval.h',c.ROOT/'local-output/argmax-bridge-20261105/N3/runtime/extracted/usr/include/mpfr.h']
    for path in originals:shutil.copyfile(path,work/path.name)
    binary=work/'bounds.so'
    argv=['cc','-O3','-std=c11','-shared','-fPIC','-I'+str(work),str(work/'n3_outward.c'),'/lib/x86_64-linux-gnu/libmpfr.so.6','-lm','-o',str(binary)]
    subprocess.run(argv,check=True)
    lib=ctypes.CDLL(str(binary));ptr=ctypes.POINTER(ctypes.c_double)
    lib.n3_box.argtypes=[ctypes.c_int,*([ctypes.c_double]*6),ctypes.c_int,ptr];lib.n3_box.restype=ctypes.c_int
    lib.n3_constants.argtypes=[ctypes.c_int,ptr]
    constants=(ctypes.c_double*6)();lib.n3_constants(32,constants)
    # A signed axis boundary differs from the developer's broad square control.
    box=[-.25,0.,0.,.25]
    test(c.bootstrap_range(32,box) and not producer.local_range(32,box),'real mixed-sign bootstrap box outside old local')
    off=producer.producer_bounds(lib,32,box,constants[2],False)
    on=producer.producer_bounds(lib,32,box,constants[2],True)
    test(off[:2]==on[:2],'MPFR request preserves S and corner bounds')
    test(off[2]==0 and off[3]==0 and on[2]>0 and on[3]==1,'MPFR request computes defect without local premise')
    producer_control=dict(n=32,box=box,off=off,on=on,compile_argv=argv,binary=producer.identity(binary),sources=[producer.identity(p) for p in originals])
    paths=[pathlib.Path(producer.__file__),pathlib.Path(__file__),pathlib.Path(c.__file__),pathlib.Path(c.legacy.__file__),pathlib.Path(c.build_snapshot.__file__),pathlib.Path(c.__file__).with_name('hybrid_kernel_v2.cpp')]
    report=dict(format='bootstrap-r8-independent-controls-v1',status='PASS',full_cover_executed=False,synthetic_scope='parser, partition and semantic branch only; no mathematical acceptance',checks=len(checks),check_labels=checks,native_n2=native,producer_calculation_control=producer_control,source_sha256={str(p.relative_to(c.ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},own_cpu_seconds=time.process_time()-start,children_cpu_seconds=sum((getattr(resource.getrusage(resource.RUSAGE_CHILDREN),k) for k in ['ru_utime','ru_stime'])),kernel_source_sha256=hashlib.sha256(pathlib.Path(c.__file__).with_name('hybrid_kernel_v2.cpp').read_bytes()).hexdigest())
    target=c.ROOT/'topics/padua-argmax-bridge-20261105/evidence/bootstrap-r8-review.json'
    target.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ['check_labels','native_n2','producer_calculation_control']}))
if __name__=='__main__':main()
