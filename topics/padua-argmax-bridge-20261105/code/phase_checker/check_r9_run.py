#!/usr/bin/env python3
"""One round9 replay of original n32 bytes; independent CPU limits and no retry."""
import collections, hashlib, json, os, pathlib, resource, runpy, signal, subprocess, sys, time
ROOT=pathlib.Path(__file__).resolve().parents[4]
TOPIC=ROOT/'topics/padua-argmax-bridge-20261105'
WORK=ROOT/'local-output/argmax-bridge-20261105/phase-r9/n32'
CANDIDATE=ROOT/'local-output/argmax-bridge-20261105/bootstrap-r8/n32/n32-phase-compact.json'
CHECKER=pathlib.Path(__file__).with_name('check_r9.py')
REPORT=WORK/'checker-report.json'
PINS={
 'code/phase_checker/check_r9.py':'1161ad5c7d4ced9736bffcbf633df349189c842314b04664ff6b465e50f2c01e',
 'code/phase_checker/check_r8.py':'3c71ada8e49829cb897ee1c064fcdc70d08c846afcb1fb067c6c84673e205bb9',
 'code/phase_checker/build_snapshot_r9.py':'6e29f5990515d50829aa7978ebeeb97dcb49e8f62716d62d37fc8ddc69e82bfa',
 'code/phase_checker/hybrid_kernel_v3.cpp':'f52d1a9da3c86212663f7ac22e9475b76811d7be4bbc4916779fd32a59d95bf0',
 'code/phase_checker/check_r6.py':'437378a5d0fe21d4d0ef30b1c9843274d2cb98fc9f408e9bad5683ec9f1e73dc',
 'code/phase_checker/build_snapshot.py':'19a5a7c2296768853b94672b9b5dc4cf16c9ae87c37abbcde073ffaf89246bfb',
 'code/phase_checker/hybrid_kernel_v2.cpp':'17fea91d4fa02e4183823e5d70b44705e96da7acfd26b04a0f3ed1cac443d9a2',
}
CANDIDATE_SHA='97c339181652d37e7e3c34522959f1b7157b8ea26d3f0ab83c0ebc1c3901528e'

def identity(path):
    path=pathlib.Path(path).resolve();raw=path.read_bytes()
    try:name=str(path.relative_to(ROOT))
    except ValueError:name=str(path)
    return dict(path=name,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())

def child_cpu():
    r=resource.getrusage(resource.RUSAGE_CHILDREN);return r.ru_utime+r.ru_stime

def group_cpu(group):
    ticks=0
    for p in pathlib.Path('/proc').iterdir():
        if not p.name.isdecimal():continue
        try:
            fields=(p/'stat').read_text().rsplit(')',1)[1].split()
            if int(fields[2])==group:ticks+=sum(int(fields[i]) for i in (11,12,13,14))
        except (FileNotFoundError,ProcessLookupError):pass
    return ticks/os.sysconf('SC_CLK_TCK')

def inputs():
    for rel,sha in PINS.items():
        if identity(TOPIC/rel)['sha256']!=sha:raise RuntimeError('source mismatch: '+rel)
    candidate=identity(CANDIDATE)
    if candidate['sha256']!=CANDIDATE_SHA or candidate['bytes']!=21338:raise RuntimeError('candidate mismatch')
    return candidate,[identity(TOPIC/p) for p in PINS]

def worker():
    resource.setrlimit(resource.RLIMIT_CPU,(1190,1191))
    inputs();start=time.process_time();before=child_cpu()
    # runpy preserves the exact frozen checker source and CLI sys.argv while
    # allowing an external accounting sidecar after its SystemExit. No bound,
    # parser or acceptance function is wrapped or modified.
    command=[str(CHECKER),str(CANDIDATE),'--kernel','round9','--output',str(REPORT)]
    sys.argv=command
    code=1
    try:
        runpy.run_path(str(CHECKER),run_name='__main__');code=0
    except SystemExit as e:
        code=e.code if isinstance(e.code,int) else 1
    finally:
        (WORK/'worker-accounting.json').write_text(json.dumps(dict(
            checker_argv=[sys.executable,*command],exit_status=code,
            checker_process_cpu_seconds=time.process_time()-start,
            compiler_build_helper_cpu_seconds=child_cpu()-before,
            process_rlimit_cpu=[1190,1191]),indent=2)+'\n')
    return code

def main():
    os.chdir(ROOT)
    if sys.argv[1:]==['--worker']:return worker()
    if len(sys.argv)!=4 or sys.argv[1:3]!=['--run-once','--source-commit']:raise RuntimeError('explicit --run-once --source-commit SHA required')
    publication_commit=sys.argv[3]
    if len(publication_commit)!=40 or set(publication_commit)-set('0123456789abcdef'):raise RuntimeError('full publication commit SHA required')
    candidate,sources=inputs();wrapper=identity(__file__)
    WORK.mkdir(exist_ok=False)
    stdout=WORK/'stdout.txt';stderr=WORK/'stderr.txt'
    command=[sys.executable,str(pathlib.Path(__file__).resolve()),'--worker']
    start=time.monotonic();before=child_cpu();peak=0.;stopped=False
    utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())
    with stdout.open('w') as out,stderr.open('w') as err:
        p=subprocess.Popen(command,stdout=out,stderr=err,start_new_session=True)
        while p.poll() is None:
            peak=max(peak,group_cpu(p.pid))
            if peak>=1188:
                os.killpg(p.pid,signal.SIGKILL);stopped=True;break
            time.sleep(.2)
        code=p.wait()
    total=child_cpu()-before;wall=time.monotonic()-start
    stable=inputs()==(candidate,sources) and identity(__file__)==wrapper
    report=json.loads(REPORT.read_text()) if REPORT.exists() else {}
    accounting_path=WORK/'worker-accounting.json'
    accounting=json.loads(accounting_path.read_text()) if accounting_path.exists() else {}
    passed=(code==0 and not stopped and stable and total<=1200 and report.get('accepted') is True and report.get('complete') is True and report.get('n')==32 and report.get('checked_leaves')==364 and report.get('total_leaves')==364 and report.get('pending')==0 and report.get('failed_leaves')==[] and report.get('candidate_sha256')==CANDIDATE_SHA and report.get('candidate_bytes')==21338)
    closure=report.get('build_provenance',{}) or {}
    closure_entries=[]
    for key in ['source_snapshot','preprocessed_translation_unit','checker_binary']:
        if key in closure:closure_entries.append(closure[key])
    for key in ['toolchain','toolchain_dependency_closure','headers','dependency_inputs','linked_dependency_closure','loaded_dependency_closure']:
        closure_entries.extend(closure.get(key,[]))
    closure_ok=bool(closure_entries) and all(identity(e['path'])['sha256']==e['sha256'] and identity(e['path'])['bytes']==e['bytes'] for e in closure_entries)
    passed=passed and closure_ok
    receipt=dict(format='independent-phase-r9-n32-v1',status='PASS' if passed else 'FAIL',accepted=bool(passed),
        scope='one round9 replay of unchanged previously failed n32 candidate; no degree extension',source_commit=publication_commit,
        candidate=candidate,checker_sources=sources,supervisor=wrapper,
        supervisor_argv=[sys.executable,str(pathlib.Path(__file__).resolve()),'--run-once','--source-commit',publication_commit],worker_argv=command,
        checker_execution='runpy.run_path of unchanged checker with exact CLI sys.argv; accounting only surrounds execution',
        execution_started_utc=utc,execution_finished_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),
        process_exit_status=code,watchdog_stopped=stopped,total_subprocess_cpu_seconds=total,elapsed_wall_seconds=wall,
        total_cpu_limit_seconds=1200,aggregate_watchdog_trigger_cpu_seconds=1188,aggregate_observed_peak_seconds=peak,
        accounting=accounting,source_input_supervisor_unchanged_after=stable,
        checked_leaves=report.get('checked_leaves'),total_leaves=report.get('total_leaves'),pending=report.get('pending'),
        failed_leaves_count=len(report.get('failed_leaves',[])),complete=report.get('complete'),
        kind_counts=dict(collections.Counter(x['kind'] for x in report.get('replay',[]))),
        checker_report=identity(REPORT) if REPORT.exists() else None,stdout=identity(stdout),stderr=identity(stderr),
        worker_accounting=identity(accounting_path) if accounting_path.exists() else None,
        full_build_runtime_closure_in_raw_report=True,closure_entries_rehashed_after=len(closure_entries),closure_unchanged_after=closure_ok,
        kernel_variant=closure.get('kernel_variant'),kernel_source=closure.get('source_snapshot'),checker_binary=closure.get('checker_binary'),
        no_max_leaves=True,retries=0,other_degrees_executed=[],arithmetic=report.get('arithmetic'))
    text=json.dumps(receipt,indent=2)+'\n'
    if len(text.encode())>=16384:raise RuntimeError('essential receipt too large')
    (TOPIC/'evidence/phase-r9-n32.json').write_text(text)
    print(text)
    return 0 if passed else 1
if __name__=='__main__':raise SystemExit(main())
