"""Independent one-shot D09 replay. Never imports the author controller."""
import ctypes,hashlib,importlib.util,json,math,os,pathlib,resource
import signal,subprocess,sys,time
from fractions import Fraction as Q
from arithmetic import endpoints,loss_test,covers_half_diamond

HERE=pathlib.Path(__file__).resolve().parent;ROOT=HERE.parents[3]
AUTHOR=HERE.parent/'post_audit_D09_threepoint'
D07=HERE.parent/'post_audit_D07_fourcopy_point'
OUT=ROOT/'local-output/argmax-bridge-20261105/post-audit-D09/result-review'
AUTHOR_OUT=OUT.parent/'threepoint'
PINS={'controller.py':'5642ad6fdf2c28165fc8d17ce8e62330ed695e7b64bb1242c13312d53d47fd73',
 'SOURCES.json':'f7d2bd992d93ec631000e98a657e119ade3d24f843e4280cb1d27f0a0069794a',
 'FREEZE.md':'6cd130544e02b9734bba710de27d9cba62bfe49a67e0fffbb031782234685d60'}

def identity(path):
    p=pathlib.Path(path).resolve();raw=p.read_bytes()
    return dict(path=str(p),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
def cpu():
    return sum(resource.getrusage(k).ru_utime+resource.getrusage(k).ru_stime
               for k in (resource.RUSAGE_SELF,resource.RUSAGE_CHILDREN))
def save(name,data):
    path=OUT/name;tmp=path.with_name(path.name+'.tmp')
    tmp.write_text(json.dumps(data,indent=2,allow_nan=False)+'\n');tmp.replace(path)
def verify_row(row):
    got=identity(ROOT/row['path'])
    assert got['bytes']==row['bytes'] and got['sha256']==row['sha256'],row['path']
def verify_tree(obj):
    count=0
    if isinstance(obj,dict):
        if {'path','bytes','sha256'}<=obj.keys():verify_row(obj);count+=1
        for value in obj.values():count+=verify_tree(value)
    elif isinstance(obj,list):
        for value in obj:count+=verify_tree(value)
    return count
def verify_inputs():
    for name,digest in PINS.items():assert identity(AUTHOR/name)['sha256']==digest,name
    for row in json.loads((AUTHOR/'FREEZE.md').read_text())['files']:verify_row(row)
    sources=json.loads((AUTHOR/'SOURCES.json').read_text())
    for row in sources['frozen_ancestors']:verify_row(row)
    assert sources['native_n']==512 and sources['norms']['512']['upper']=='34'
    assert sources['primary']==dict(a_turn='1/4',b_turn='3/16')
    assert sources['fallback']==dict(a_turn='1/6',b_turn='5/31')
    assert sources['pi_upper']=='22/7' and sources['pi_lower']=='157/50'
    release=json.loads((OUT/'release.json').read_text())
    assert release['root_released'] is True
    assert release['fallback_authorized'] is False,'root released primary-only replay'
    count=verify_tree(release)
    for name in ('build-manifest.json','runtime-before.json','runtime-after.json'):
        count+=verify_tree(json.loads((AUTHOR_OUT/name).read_text()))
    baseline=json.loads((AUTHOR_OUT/'checkpoint.json').read_text())
    supervisor=json.loads((AUTHOR_OUT/'supervisor.json').read_text())
    accounting=json.loads((AUTHOR_OUT/'final-accounting.json').read_text())
    summary=json.loads((AUTHOR_OUT/'worker-summary.json').read_text())
    assert supervisor['result']=='COMPLETED' and supervisor['accounting_complete']
    assert accounting['accounting_complete'] and accounting['total_cpu_seconds_through_supervisor_serialization']<59
    assert baseline['status']=='COMPLETED' and baseline['active_call'] is None and not baseline['pending_points']
    assert list(baseline['rectangles'])==['primary'] and summary['passed']
    assert baseline['rectangles']['primary']['criterion']['passes']
    assert len(baseline['completed_calls'])==5
    assert summary['corner']==baseline['corner'] and summary['rectangles']==baseline['rectangles']
    return baseline,count
def group_cpu(group):
    total=0.
    for path in pathlib.Path('/proc').glob('[0-9]*/stat'):
        try:
            data=path.read_text();v=data[data.rfind(')')+2:].split()
            if int(v[2])==group:total+=sum(int(v[k]) for k in (11,12,13,14))/os.sysconf('SC_CLK_TCK')
        except (OSError,ValueError,IndexError):pass
    return total
def supervisor_cpu():
    data=pathlib.Path('/proc/'+str(os.getppid())+'/stat').read_text();v=data[data.rfind(')')+2:].split()
    return sum(int(v[k]) for k in (11,12,13,14))/os.sysconf('SC_CLK_TCK')
def subreaper():
    libc=ctypes.CDLL(None,use_errno=True);fn=libc.prctl
    fn.argtypes=[ctypes.c_int]+[ctypes.c_ulong]*4;fn.restype=ctypes.c_int
    assert fn(36,1,0,0,0)==0
    flag=ctypes.c_int();assert fn(37,ctypes.addressof(flag),0,0,0)==0 and flag.value==1
def cleanup(group):
    deadline=time.monotonic()+5;records=[]
    while True:
        try:os.killpg(group,signal.SIGKILL)
        except ProcessLookupError:pass
        try:pid,status,usage=os.wait4(-1,os.WNOHANG)
        except ChildProcessError:return dict(complete=True,records=records)
        if pid:records.append(dict(pid=pid,status=status,CPU=usage.ru_utime+usage.ru_stime));continue
        if time.monotonic()>deadline:return dict(complete=False,records=records)
        time.sleep(.01)
def own_code():return [identity(HERE/name) for name in ('run.py','arithmetic.py','summarize.py')]

def worker():
    resource.setrlimit(resource.RLIMIT_CPU,(54,55))
    registration=json.loads((OUT/'registration.json').read_text())
    assert registration['review_code']==own_code()
    with (OUT/'worker-entry.json').open('x') as f:json.dump(dict(pid=os.getpid(),code=own_code()),f)
    baseline,count=verify_inputs();state=dict(status='BUILDING',active=None,completed=[])
    save('progress.json',state)
    spec=importlib.util.spec_from_file_location('unchanged_d07_builder_review',D07/'build.py')
    build=importlib.util.module_from_spec(spec);spec.loader.exec_module(build);build.LOCAL=OUT/'build'
    binary,manifest=build.build();save('build-manifest.json',manifest)
    lib=ctypes.CDLL(str(binary));assert ctypes.sizeof(ctypes.c_long)==8 and ctypes.sizeof(ctypes.c_double)==8
    signature=[ctypes.c_long,ctypes.c_char_p,ctypes.c_char_p,ctypes.POINTER(ctypes.c_double),ctypes.POINTER(ctypes.c_long)]
    for name in ('d07_point','d07_compare','c07_point'):
        fn=getattr(lib,name);fn.argtypes=signature;fn.restype=ctypes.c_int
    loaded=build.loaded_closure(manifest);save('runtime-before.json',dict(loaded=loaded,python=sys.version))
    (OUT/'loaded-before.maps').write_text(pathlib.Path('/proc/self/maps').read_text())
    state['status']='RUNNING'
    def call(label,api,n,x,z,expected):
        assert cpu()+supervisor_cpu()<42,'CPU reserve stop'
        state['active']=dict(label=label,cpu_start=cpu());save('progress.json',state)
        start=cpu()
        try:
            reference=api=='d07_compare';values=(ctypes.c_double*(9 if reference else 3))()
            counts=(ctypes.c_long*(6 if api=='c07_point' else 13))()
            status=getattr(lib,api)(n,str(x).encode(),str(z).encode(),values,counts)
            state['raw_output']=repr(dict(status=status,outputs=list(values),counts=list(counts)));save('progress.json',state)
            assert status==0 and all(math.isfinite(v) for v in values),'native status/nonfinite failure'
            if reference:
                assert values[0]==1 and values[1]==1,'complete finite reference containment failed'
                result=dict(point=endpoints(list(values[3:6])),reference=endpoints(list(values[6:9])),
                    contains_reference=True,counts=list(counts),api=api)
            else:result=dict(point=endpoints(list(values)),counts=list(counts),api=api,n=n,xi_pi=str(x),zeta_pi=str(z))
            assert result==expected,'author interval/count/input mismatch'
        except BaseException as error:
            state['first_failure']=dict(label=label,error=repr(error),CPU=cpu()-start);save('progress.json',state);raise
        record=dict(label=label,CPU=cpu()-start,result=result,matches_author=True)
        if reference:record['native_reference_verdicts']=list(values[:3])
        state['completed'].append(record);state['active']=None;save('progress.json',state)
        assert record['CPU']<=20,'completed-call cost stop'
        return result
    control=call('control-n32','d07_compare',32,Q(1,512),Q(1,1056),baseline['control'])
    corner=call('corner-n512-C11-S0','c07_point',512,Q(0),Q(0),baseline['corner'])
    rectangle=baseline['rectangles']['primary'];a,b=Q(1,4),Q(3,16)
    assert covers_half_diamond(a,b)
    assert rectangle['geometry']==dict(a_turn=str(a),b_turn=str(b),xi_pi=str(a/512),zeta_pi=str(b/513))
    vertices=[]
    for key,x,z in [('x',a/512,Q(0)),('y',Q(0),b/513),('xy',a/512,b/513)]:
        vertices.append(call('primary-'+key,'d07_point',512,x,z,rectangle['vertices'][key]))
    criterion=loss_test(512,a,b,corner['point'],[row['point'] for row in vertices])
    assert criterion==rectangle['criterion'],'independent exact loss criterion mismatch'
    assert criterion['passes'],'released primary truth predicate mismatch; no fallback authorized'
    after=build.loaded_closure(manifest);assert loaded==after
    count+=verify_tree(manifest)
    verify_inputs();assert registration['review_code']==own_code()
    save('runtime-after.json',dict(loaded=after));(OUT/'loaded-after.maps').write_text(pathlib.Path('/proc/self/maps').read_text())
    save('worker-result.json',dict(status='PASS independent finite point and exact criterion replay',
        completed=state['completed'],criterion=criterion,coverage=True,verified_identity_records=count,
        review_code=own_code(),binary=identity(binary),worker_CPU=cpu()))
    state['status']='PASS';save('progress.json',state)

def main():
    if sys.argv[1:]==['--worker']:
        try:worker()
        except BaseException as error:
            save('worker-first-error.json',dict(error=repr(error),CPU=cpu()));raise
        return
    assert sys.argv[1:]==['--released-once'],'explicit root release and --released-once required'
    resource.setrlimit(resource.RLIMIT_CPU,(57,58));subreaper();verify_inputs()
    OUT.mkdir(parents=True,exist_ok=True)
    with (OUT/'registration.json').open('x') as f:
        json.dump(dict(review_code=own_code(),preregistration=identity(HERE/'PREEXEC.md'),
            release=identity(OUT/'release.json'),inputs=PINS,run_CPU_cap=58,total_review_CPU_cap=60,
            pure_and_summary_reserved_CPU=2,safety=52,wall=180),f,indent=2)
    start=time.monotonic();stop=None
    with (OUT/'worker.stdout').open('xb') as stdout,(OUT/'worker.stderr').open('xb') as stderr:
        child=subprocess.Popen([sys.executable,__file__,'--worker'],stdout=stdout,stderr=stderr,
            stdin=subprocess.DEVNULL,start_new_session=True)
        while child.poll() is None:
            live=group_cpu(child.pid)
            if cpu()+live>=52:stop='aggregate CPU safety'
            if time.monotonic()-start>=180:stop='wall cap'
            try:active=json.loads((OUT/'progress.json').read_text()).get('active')
            except (OSError,ValueError):active=None
            if active and live-active['cpu_start']>=25:stop='unfinished call hard stop'
            if stop:
                try:os.killpg(child.pid,signal.SIGKILL)
                except ProcessLookupError:pass
                break
            time.sleep(.05)
        child.wait()
    descendants=cleanup(child.pid);save('descendants.json',descendants)
    result=dict(returncode=child.returncode,stop=stop,accounting_complete=descendants['complete'],
        inclusive_CPU_before_summary=cpu(),run_CPU_cap=58,wall=time.monotonic()-start,
        review_code=own_code(),stdout=identity(OUT/'worker.stdout'),stderr=identity(OUT/'worker.stderr'))
    result['status']='PASS' if child.returncode==0 and stop is None and descendants['complete'] and cpu()<58 else 'FIRST_FAILURE_OR_STOP'
    save('supervisor.json',result)
    save('final-accounting.json',dict(complete=descendants['complete'],CPU_through_summary=cpu(),
        scope='self plus all waited descendants; sample precedes final tiny write/print bounded by parent58 CPU'))
    print(json.dumps(result),flush=True);sys.exit(0 if result['status']=='PASS' else 1)
if __name__=='__main__':main()
