"""Independent once-only D07 actual-point result check; see PREEXEC.md."""
import ctypes, hashlib, importlib.util, json, math, os, pathlib, resource
import signal, subprocess, sys, time

HERE=pathlib.Path(__file__).resolve().parent
ROOT=HERE.parents[3]
AUTHOR=HERE.parent/'post_audit_D07_fourcopy_point'
OUT=ROOT/'local-output/argmax-bridge-20261105/post-audit-D07/result-review'
EVIDENCE=ROOT/'topics/padua-argmax-bridge-20261105/evidence/d07-fourcopy-point.json'
PINS={'point.cpp':'03dc79bbbc7563ba9066137c0a52467624c810a758f865f9931511c82985ff6f',
      'controls.cpp':'5db13088e9fff85a134c95851337750ca03ea62be2f5d3ecf07e1f6e7d49c3fa',
      'controller.py':'af8d357badba85786fec088c735cc988f0950587d112e2e63a8d5b39cc14a9a5',
      'FREEZE.json':'c8b8e49e5c5af5ff520f00f8b7bac655a6c31cc132a5cb06cd87397c36fa33fb',
      'build.py':'13efba942b47be6ccacd4f13f81ce387bb268ff4f7ef77c2e648357a135c9ef8',
      'CASES.json':'fbfad19f2b6b00dd094b728716a3bcd7371ba0573321fd71c978dd5c06025d01'}
RECEIPT='f6e574e8e9ce3523d2dfc257c9597e80b62973dd4b4d9f419a686dfd4b07206b'

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
    actual=identity(ROOT/row['path'])
    assert actual['bytes']==row['bytes'] and actual['sha256']==row['sha256'],row['path']
def verify_tree(obj):
    count=0
    if isinstance(obj,dict):
        if {'path','bytes','sha256'} <= obj.keys():verify_row(obj);count+=1
        for value in obj.values():count+=verify_tree(value)
    elif isinstance(obj,list):
        for value in obj:count+=verify_tree(value)
    return count
def verify_inputs():
    for name,digest in PINS.items():assert identity(AUTHOR/name)['sha256']==digest,name
    assert identity(EVIDENCE)['sha256']==RECEIPT
    freeze=json.loads((AUTHOR/'FREEZE.json').read_text())
    for row in freeze['files']:verify_row(row)
    for row in json.loads((AUTHOR/'SOURCES.json').read_text())['frozen_ancestors']:verify_row(row)
    return json.loads(EVIDENCE.read_text())
def load_builder():
    spec=importlib.util.spec_from_file_location('review_frozen_builder',AUTHOR/'build.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    module.LOCAL=OUT/'build';return module
def group_cpu(group):
    total=0.
    for path in pathlib.Path('/proc').glob('[0-9]*/stat'):
        try:
            data=path.read_text();v=data[data.rfind(')')+2:].split()
            if int(v[2])==group:total+=sum(int(v[k]) for k in (11,12,13,14))/os.sysconf('SC_CLK_TCK')
        except (OSError,ValueError,IndexError):pass
    return total
def supervisor_cpu():
    data=pathlib.Path('/proc/'+str(os.getppid())+'/stat').read_text()
    v=data[data.rfind(')')+2:].split()
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

def worker():
    resource.setrlimit(resource.RLIMIT_CPU,(114,115))
    registration=json.loads((OUT/'registration.json').read_text())
    assert registration['driver']==identity(__file__)
    with (OUT/'worker-entry.json').open('x') as f:json.dump(dict(pid=os.getpid(),driver=identity(__file__)),f)
    expected=verify_inputs();state=dict(status='VERIFYING',active=None,completed=[])
    save('progress.json',state)
    count=verify_tree(expected)
    author_manifest=json.loads(pathlib.Path(next(x['path'] for x in expected['raw_files'] if x['path'].endswith('build-manifest.json'))).read_text())
    count+=verify_tree(author_manifest)
    for filename in ('runtime-before.json','runtime-after.json'):
        path=next(x['path'] for x in expected['raw_files'] if x['path'].endswith('/'+filename))
        count+=verify_tree(json.loads(pathlib.Path(path).read_text()))
    state['verified_author_identity_records']=count;state['status']='BUILDING';save('progress.json',state)
    build=load_builder();binary,manifest=build.build();save('build-manifest.json',manifest)
    lib=ctypes.CDLL(str(binary))
    assert ctypes.sizeof(ctypes.c_long)==8 and ctypes.sizeof(ctypes.c_double)==8
    signature=[ctypes.c_long,ctypes.c_char_p,ctypes.c_char_p,ctypes.POINTER(ctypes.c_double),ctypes.POINTER(ctypes.c_long)]
    for name in ('d07_point','d07_compare','c07_point'):
        fn=getattr(lib,name);fn.argtypes=signature;fn.restype=ctypes.c_int
    loaded=build.loaded_closure(manifest)
    save('runtime-before.json',dict(loaded=loaded,python=sys.version))
    (OUT/'loaded-before.maps').write_text(pathlib.Path('/proc/self/maps').read_text())
    state['status']='RUNNING';points=[];invalids=[]
    def call(label,fn):
        assert cpu()+supervisor_cpu()<90,'CPU reserve stop'
        state['active']=dict(label=label,cpu_start=cpu());save('progress.json',state)
        started=cpu()
        try:result=fn()
        except BaseException as error:
            state['first_failure']=dict(label=label,error=repr(error),CPU=cpu()-started)
            save('progress.json',state);raise
        record=dict(label=label,CPU=cpu()-started,result=result)
        state['completed'].append(record);state['active']=None;save('progress.json',state)
        assert record['CPU']<=20,'completed-call cost stop'
        return record
    for n,x,z in [(1,'0','0'),(2049,'0','0'),(2,'-1/8','0'),(2,'0','9/8'),(2,'bad','0'),(2,'0/0','0')]:
        def reject(n=n,x=x,z=z):
            out=(ctypes.c_double*3)();counts=(ctypes.c_long*13)()
            status=lib.d07_point(n,x.encode(),z.encode(),out,counts)
            state['raw_output']=repr((status,list(out),list(counts)));save('progress.json',state)
            assert status!=0 and all(math.isnan(value) for value in out)
            return dict(status=status,NaN_outputs=True)
        invalids.append(call('invalid-'+str(n)+'-'+x+'-'+z,reject))
    cases=json.loads((AUTHOR/'CASES.json').read_text())
    assert len(cases['cases'])==13 and sum(x['reference'] for x in cases['cases'])==10
    assert [x['case'] for x in expected['point_cases']]==cases['cases']
    for case,baseline in zip(cases['cases'],expected['point_cases']):
        def evaluate(case=case,baseline=baseline):
            reference=case['reference'];out=(ctypes.c_double*(9 if reference else 3))();counts=(ctypes.c_long*13)()
            fn=lib.d07_compare if reference else lib.d07_point
            status=fn(case['n'],case['xi_pi'].encode(),case['zeta_pi'].encode(),out,counts)
            state['raw_output']=repr((status,list(out),list(counts)));save('progress.json',state)
            assert status==0 and all(math.isfinite(value) for value in out)
            value=list(out[3:6] if reference else out)
            assert value[0]<=value[1] and value[2]>=0
            assert value==baseline['enclosure'] and list(counts)==baseline['counts'],'author result/count mismatch'
            result=dict(case=case,enclosure=value,counts=list(counts),matches_author=True)
            if reference:
                assert out[0] and (out[1] or (counts[10]==1 and out[2])),'reference containment failed'
                assert list(out[6:9])==baseline['reference_enclosure']
                assert bool(out[1])==baseline['contains_complete_reference']
                assert bool(out[2])==baseline['reference_contains_exact_shortcut']
                result.update(reference_enclosure=list(out[6:9]),contains_reference=bool(out[1]),reference_contains_shortcut=bool(out[2]))
            if case['kind']=='node':assert value[:2]==[1.,1.]
            return result
        record=call('point-'+str(case['n'])+'-'+case['kind'],evaluate);points.append(record)
    context=cases['large_S_context']
    def common_s():
        out=(ctypes.c_double*3)();counts=(ctypes.c_long*6)()
        status=lib.c07_point(context['n'],context['af_pi'].encode(),context['bf_pi'].encode(),out,counts)
        state['raw_output']=repr((status,list(out),list(counts)));save('progress.json',state)
        assert status==0 and all(math.isfinite(value) for value in out)
        assert list(out)==expected['common_S_context']['result']['enclosure']
        assert list(counts)==expected['common_S_context']['result']['counts']
        return dict(enclosure=list(out),counts=list(counts),scope='common-S context only')
    context_result=call('common-S-context',common_s)
    after=build.loaded_closure(manifest);assert loaded==after
    for key in ('toolchain','toolchain_dependency_closure','headers','linked_dependency_closure'):
        for row in manifest[key]:verify_row(row)
    verify_row(manifest['checker_binary']);verify_row(manifest['preprocessed_translation_unit'])
    verify_inputs();assert registration['driver']==identity(__file__)
    save('runtime-after.json',dict(loaded=after));(OUT/'loaded-after.maps').write_text(pathlib.Path('/proc/self/maps').read_text())
    generic=next(x for x in points if x['result']['case']['n']==512 and x['result']['case']['kind']=='generic')
    summary=dict(status='PASS finite independent point rerun',points=points,invalids=invalids,context=context_result,
        verified_author_identity_records=count,generic_n512_CPU=generic['CPU'],performance_gate=generic['CPU']<=10,
        driver=identity(__file__),binary=identity(binary),worker_CPU=cpu())
    save('worker-result.json',summary)
    assert summary['performance_gate'],'finite generic n512 performance gate failed'
    state['status']='PASS';save('progress.json',state)

def main():
    if len(sys.argv)>1:
        assert sys.argv[1:]==['--worker']
        worker();return
    resource.setrlimit(resource.RLIMIT_CPU,(119,120));subreaper();verify_inputs()
    OUT.mkdir(parents=True,exist_ok=True)
    with (OUT/'registration.json').open('x') as f:
        json.dump(dict(driver=identity(__file__),preregistration=identity(HERE/'PREEXEC.md'),inputs=PINS,
            author_receipt=identity(EVIDENCE),CPU_cap=120,safety=110,wall=240),f,indent=2)
    start=time.monotonic();stop=None
    with (OUT/'worker.stdout').open('xb') as stdout,(OUT/'worker.stderr').open('xb') as stderr:
        child=subprocess.Popen([sys.executable,__file__,'--worker'],stdout=stdout,stderr=stderr,
            stdin=subprocess.DEVNULL,start_new_session=True)
        while child.poll() is None:
            live=group_cpu(child.pid)
            if cpu()+live>=110:stop='aggregate CPU safety'
            if time.monotonic()-start>=240:stop='wall cap'
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
        inclusive_CPU_before_summary=cpu(),CPU_cap=120,wall=time.monotonic()-start,
        driver=identity(__file__),stdout=identity(OUT/'worker.stdout'),stderr=identity(OUT/'worker.stderr'))
    result['status']='PASS' if child.returncode==0 and stop is None and descendants['complete'] and cpu()<120 else 'FIRST_FAILURE_OR_STOP'
    save('supervisor.json',result)
    save('final-accounting.json',dict(complete=descendants['complete'],CPU_through_summary=cpu(),
        scope='self plus all waited descendants; sample precedes final tiny write/print'))
    print(json.dumps(result),flush=True)
    sys.exit(0 if result['status']=='PASS' else 1)
if __name__=='__main__':main()
