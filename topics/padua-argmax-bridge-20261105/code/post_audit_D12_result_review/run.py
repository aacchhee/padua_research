"""One frozen independent fixed-certificate replay; no author controller import."""
import ctypes, hashlib, importlib.util, json, math, os, pathlib, resource
import signal, subprocess, sys, time
from verify import strict_json, geometry, endpoints, corner, predicates
HERE=pathlib.Path(__file__).resolve().parent; ROOT=HERE.parents[3]
TOPIC=HERE.parents[1]; EVIDENCE=TOPIC/'evidence'
OUT=ROOT/'local-output/argmax-bridge-20261105/post-audit-D12/result-review'
PRIMARY=ROOT/'local-output/argmax-bridge-20261105/post-audit-D11/point-cover'
SOURCE=HERE.parent/'post_audit_D11_point_cover'
CERT=EVIDENCE/'d12-point-cover-tree.json'

def ident(path):
    p=pathlib.Path(path).resolve(); b=p.read_bytes()
    return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def cpu():
    return sum(resource.getrusage(k).ru_utime+resource.getrusage(k).ru_stime for k in (resource.RUSAGE_SELF,resource.RUSAGE_CHILDREN))
def save(path, obj):
    temporary=path.with_suffix(path.suffix+'.tmp')
    temporary.write_text(json.dumps(obj,sort_keys=True,separators=(',',':'),allow_nan=False)+'\n');temporary.replace(path)
def check_row(row):
    p=pathlib.Path(row['path']);p=p if p.is_absolute() else ROOT/p
    actual=ident(p);assert (actual['bytes'],actual['sha256'])==(row['bytes'],row['sha256']),str(p)
def verify_inputs():
    f=strict_json(HERE/'FREEZE.json')
    for row in f['files']:check_row(row)
    assert ident(SOURCE/'FREEZE.json')['sha256']=='3c361e44db34babd168cdca0c785fe101abb80c5441cbf9e1c7314e52c73c8c1'
    a=strict_json(SOURCE/'FREEZE.json'); s=strict_json(SOURCE/'SOURCES.json')
    for row in a['code_data']+s['immutable_code_data_dependencies']:check_row(row)
    return f
def mapped():
    paths=set(); raw=pathlib.Path('/proc/self/maps').read_text()
    for line in raw.splitlines():
        parts=line.split(maxsplit=5)
        if len(parts)==6 and parts[5].startswith('/'):
            assert not parts[5].endswith(' (deleted)')
            paths.add(pathlib.Path(parts[5]).resolve())
    return [ident(p) for p in sorted(paths)],raw
def load_build():
    p=HERE.parent/'post_audit_D07_fourcopy_point/build.py'
    spec=importlib.util.spec_from_file_location('unchanged_d07_builder',p)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    module.LOCAL=OUT
    assert module.INC.is_dir() and module.FLINT.is_file(), 'fixed bootstrap prerequisite missing; no recovery'
    return module
def worker():
    resource.setrlimit(resource.RLIMIT_CPU,(116,117));verify_inputs()
    assert strict_json(OUT/'registration.json')['freeze']==ident(HERE/'FREEZE.json')
    state=dict(status='BUILDING',completed=[],active_call=None)
    def checkpoint():save(OUT/'checkpoint.json',state)
    checkpoint()
    try:
        lower,witness=corner(strict_json(EVIDENCE/'d09-threepoint.json'))
        leaves,points,depth=geometry(strict_json(CERT))
        assert (len(points),len(leaves),depth)==(53,42,12)
        build=load_build();binary,manifest=build.build();save(OUT/'build.json',manifest)
        assert ctypes.sizeof(ctypes.c_long)==8 and ctypes.sizeof(ctypes.c_double)==8
        lib=ctypes.CDLL(str(binary));fn=lib.c07_point
        fn.argtypes=[ctypes.c_long,ctypes.c_char_p,ctypes.c_char_p,ctypes.POINTER(ctypes.c_double),ctypes.POINTER(ctypes.c_long)];fn.restype=ctypes.c_int
        linked=build.loaded_closure(manifest);before,raw=mapped()
        save(OUT/'runtime-before.json',dict(mapped=before,linked=linked,python=sys.version));(OUT/'before.maps').write_text(raw)
        state['status']='RUNNING';checkpoint()
        for a,b in points:
            assert cpu()<107, 'before-call reserve'
            assert a>=0 and b>=0 and a+b<=1 and max(len(str(a)),len(str(b)))<=256
            started=cpu();state['active_call']=dict(turns=[str(a),str(b)],cpu_start=started);checkpoint()
            values=(ctypes.c_double*3)();counts=(ctypes.c_long*6)()
            rc=fn(512,str(a).encode(),str(b).encode(),values,counts)
            duration=cpu()-started
            row=[str(a),str(b),[x.hex() for x in values],list(counts)]
            state['completed'].append(dict(row=row,returncode=rc,cpu=duration));state['active_call']=None;checkpoint()
            assert duration<=20, 'completed call cost stop'
            assert rc==0;endpoints(row[2]);assert all(c>=0 for c in counts)
        rows=[entry['row'] for entry in state['completed']]
        summary,details=predicates(leaves,rows,lower)
        assert summary['leaf_counts']=={'NEAR':8,'FAR':31,'OUTSIDE':3}
        save(OUT/'leaves.json',details)
        # Optional local comparison is not a clean-clone proof dependency.
        baseline=PRIMARY/'checker-checkpoint.json';comparison='primary local raw absent'
        if baseline.exists():
            assert ident(baseline)['sha256']=='b1747afae4b6cbd6f53eb4604e214056b8aa128ffbbbf2033a39b714e7658bb8'
            original=json.loads(baseline.read_text());assert original['status']=='COMPLETE' and original['active_call'] is None
            old={e['key']:(e['native']['raw_hex'],e['native']['counts'],e['native']['returncode']) for e in original['completed_calls']}
            assert len(old)==53
            for row in rows:assert old[row[0]+','+row[1]]==(row[2],row[3],0)
            comparison='all 53 endpoint/radius hex triples and six-counter vectors exactly equal'
        after,raw=mapped();assert before==after
        assert linked==build.loaded_closure(manifest)
        save(OUT/'runtime-after.json',dict(mapped=after,linked=linked));(OUT/'after.maps').write_text(raw)
        for key in ['source_snapshot','preprocessed_translation_unit','checker_binary']:check_row(manifest[key])
        for key in ['toolchain','toolchain_dependency_closure','headers','dependency_inputs','linked_dependency_closure']:
            for row in manifest[key]:check_row(row)
        verify_inputs()
        state.update(status='COMPLETE',summary=summary,witness=witness,lower=str(lower),nodes=len(strict_json(CERT)['preorder']),
                     max_depth=depth,author_comparison=comparison,worker_inclusive_cpu=cpu())
        checkpoint()
    except BaseException as error:
        state.update(status='FIRST_FAILURE',first_failure=repr(error));checkpoint();raise

def group_cpu(group):
    total=0
    for p in pathlib.Path('/proc').glob('[0-9]*/stat'):
        try:
            raw=p.read_text();v=raw[raw.rfind(')')+2:].split()
            if int(v[2])==group:total+=sum(int(v[k]) for k in (11,12,13,14))
        except (OSError,ValueError,IndexError):pass
    return total/os.sysconf('SC_CLK_TCK')
def subreaper():
    lib=ctypes.CDLL(None,use_errno=True);fn=lib.prctl
    fn.argtypes=[ctypes.c_int,ctypes.c_ulong,ctypes.c_ulong,ctypes.c_ulong,ctypes.c_ulong];fn.restype=ctypes.c_int
    assert fn(36,1,0,0,0)==0
    value=ctypes.c_int();assert fn(37,ctypes.addressof(value),0,0,0)==0 and value.value==1
    return value.value
def supervise():
    resource.setrlimit(resource.RLIMIT_CPU,(118,119))
    OUT.mkdir(parents=True,exist_ok=False);verify_inputs();enabled=subreaper()
    save(OUT/'registration.json',dict(freeze=ident(HERE/'FREEZE.json'),subreaper=enabled,cap_cpu=120,
         safety_cpu=114,completed_call=20,unfinished_call=25,wall_cap=600,root_release='parent task plus post-PREEXEC release',no_retry=True))
    started=time.monotonic();stop=None;reaped=[];complete=False
    with (OUT/'stdout').open('xb') as stdout,(OUT/'stderr').open('xb') as stderr:
        p=subprocess.Popen([sys.executable,str(HERE/'run.py'),'--worker'],stdin=subprocess.DEVNULL,stdout=stdout,stderr=stderr,start_new_session=True)
        try:
            while p.poll() is None:
                live=group_cpu(p.pid)
                if cpu()+live>=114:stop='inclusive CPU safety stop'
                if time.monotonic()-started>=600:stop='wall stop'
                try:active=json.loads((OUT/'checkpoint.json').read_text()).get('active_call')
                except (OSError,ValueError):active=None
                if active and live-active['cpu_start']>=25:stop='unfinished call stop'
                if stop:break
                time.sleep(.05)
        except BaseException as error:stop=repr(error)
        finally:
            if stop:
                try:os.killpg(p.pid,signal.SIGKILL)
                except ProcessLookupError:pass
            p.wait()
            try:os.killpg(p.pid,signal.SIGKILL)
            except ProcessLookupError:pass
            deadline=time.monotonic()+5
            while time.monotonic()<deadline:
                try:pid,status,usage=os.wait4(-1,os.WNOHANG)
                except ChildProcessError:complete=True;break
                if pid:reaped.append(dict(pid=pid,status=status,cpu=usage.ru_utime+usage.ru_stime))
                else:time.sleep(.01)
    state=json.loads((OUT/'checkpoint.json').read_text())
    passed=stop is None and p.returncode==0 and complete and cpu()<118 and state['status']=='COMPLETE'
    ledger=dict(passed=passed,first_failure=stop or state.get('first_failure'),returncode=p.returncode,accounting_complete=complete,
                reaped_descendants=reaped,inclusive_cpu_through_sample=cpu(),wall_seconds=time.monotonic()-started,
                scope='supervisor plus waited descendants, final serialization excluded; hard limits and 2CPU metadata reserve within120')
    save(OUT/'final-accounting.json',ledger)
    print(json.dumps(ledger),flush=True)
    if not passed:raise SystemExit(1)

if __name__=='__main__':
    if sys.argv[1:]==['--released-once']:supervise()
    elif sys.argv[1:]==['--worker']:worker()
    else:raise SystemExit('explicit release required')
