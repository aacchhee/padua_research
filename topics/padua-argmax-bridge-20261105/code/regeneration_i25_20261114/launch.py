"""Bounded four-process orchestration; no numerical or certificate logic."""
import argparse, hashlib, json, os, resource, signal, subprocess, sys, time
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'compact_pack'))
from process_guard import normalize_startup

def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def interrupted(number, frame): raise RuntimeError('supervisor signal '+str(number))
def kill_group(pid, number):
    try: os.killpg(pid,number)
    except ProcessLookupError: pass

def main():
    normalize_startup()
    parser=argparse.ArgumentParser(); parser.add_argument('--freeze',required=True); parser.add_argument('--output',required=True); args=parser.parse_args()
    freeze=json.loads(Path(args.freeze).read_bytes())
    for name,sha in freeze['sources'].items():
        if digest(Path(name))!=sha: raise ValueError('source pin: '+name)
    if digest(Path(freeze['inventory']))!=freeze['inventory_sha256']: raise ValueError('inventory pin')
    base=Path(args.output); base.mkdir(parents=True,exist_ok=False); resource.setrlimit(resource.RLIMIT_CPU,(80,10800))
    source=Path(__file__).parent
    archive='local-output/argmax-bridge-20261105/actual-return-20261107/return.tar.gz'
    started=time.monotonic(); cpu=time.process_time(); before=resource.getrusage(resource.RUSAGE_CHILDREN)
    jobs=[]; files=[]; pending={}; stop=None
    def observe(pid, flags):
        job=pending[pid]
        observed,status,usage=os.wait4(pid,flags)
        if not observed: return
        if observed!=pid: raise RuntimeError('wrong wait4 child')
        job.update(wait_status=status,returncode=os.waitstatus_to_exitcode(status),
                   CPU_seconds=usage.ru_utime+usage.ru_stime,maximum_RSS_KiB=usage.ru_maxrss)
        job['process'].returncode=job['returncode']; del pending[pid]
    for number in [signal.SIGTERM,signal.SIGHUP,signal.SIGINT]: signal.signal(number,interrupted)
    try:
        for j in range(4):
            degrees=list(range(41+j,512,4))
            cmd=['timeout','--signal=TERM','--kill-after=5s','7200s','env','OPENBLAS_NUM_THREADS=1',
                 'OMP_NUM_THREADS=1',sys.executable,'-E','-B',str(source/'worker.py'),'--archive',archive,
                 '--freeze',args.freeze,'--additional-dir',freeze['additional_dir'],'--inventory-sha',freeze['inventory_sha256'],
                 *(['--controls'] if 199 in degrees else []),'--degrees',','.join(map(str,degrees)),
                 '--cpu-limit','2670','--output',str(base/('worker-'+str(j)))]
            out=(base/('worker-'+str(j)+'.stdout')).open('x'); files.append(out)
            err=(base/('worker-'+str(j)+'.stderr')).open('x'); files.append(err)
            normalize_startup(); proc=subprocess.Popen(cmd,stdout=out,stderr=err,start_new_session=True)
            job={'worker':j,'degrees':degrees,'command':cmd,'process':proc,'pid':proc.pid}
            jobs.append(job); pending[proc.pid]=job
        while pending:
            for pid in list(pending): observe(pid,os.WNOHANG)
            if any(job.get('returncode',0) for job in jobs): raise RuntimeError('worker failure')
            if time.monotonic()-started>7250: raise RuntimeError('outer wall cap')
            if pending: time.sleep(.2)
    except BaseException as error:
        stop=repr(error)
    finally:
        for number in [signal.SIGTERM,signal.SIGHUP,signal.SIGINT]: signal.signal(number,signal.SIG_IGN)
        for pid in pending: kill_group(pid,signal.SIGTERM)
        deadline=time.monotonic()+2
        while pending and time.monotonic()<deadline:
            for pid in list(pending):
                try: observe(pid,os.WNOHANG)
                except ChildProcessError as error:
                    pending[pid]['wait_error']=repr(error); pending[pid]['process'].returncode=255
                    del pending[pid]; stop=stop or 'missing owned child status'
            if pending: time.sleep(.02)
        for pid in pending: kill_group(pid,signal.SIGKILL)
        for pid in list(pending):
            try: observe(pid,0)
            except ChildProcessError as error:
                pending[pid]['wait_error']=repr(error); pending[pid]['process'].returncode=255
                del pending[pid]; stop=stop or 'missing owned child status'
        for job in jobs: del job['process']
        for f in files: f.close()
    after=resource.getrusage(resource.RUSAGE_CHILDREN)
    totalcpu=time.process_time()-cpu+after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime
    observations={'jobs':jobs,'stop':stop,'wall_seconds':time.monotonic()-started,'CPU_seconds_inclusive':totalcpu,
                  'maximum_child_RSS_KiB':after.ru_maxrss,'source_hashes':freeze['sources'],'freeze_sha256':digest(Path(args.freeze))}
    (base/'outer-observation.json').write_text(json.dumps(observations,indent=2)+'\n')
    if stop or len(jobs)!=4 or any(j.get('returncode')!=0 for j in jobs) or totalcpu>10800: raise SystemExit(1)
    summaries=[json.loads((base/('worker-'+str(j))/'summary.json').read_bytes()) for j in range(4)]
    if any(s['arithmetic_controls']!=31 for s in summaries) or sum(s['corruption_controls'] for s in summaries)!=27: raise SystemExit('control count mismatch')
    rows=[]
    for j in range(4): rows.extend(json.loads(line) for line in (base/('worker-'+str(j))/'observations.jsonl').read_text().splitlines())
    expected={(n,p) for n in range(41,512) for p in ['produce','verify']}
    if len(rows)!=942 or {(r['n'],r['pass']) for r in rows}!=expected or not all(r['accepted'] for r in rows): raise SystemExit(1)
    artifacts=[]
    for p in sorted(base.rglob('*')):
        if p.is_file(): artifacts.append({'path':str(p),'bytes':p.stat().st_size,'sha256':digest(p)})
    summary={'accepted':942,'degrees':471,'CPU_seconds_inclusive':totalcpu,'wall_seconds':observations['wall_seconds'],
             'scope':'independent substituted-bound recertification','all_native_endpoints_validated':False,'artifact_manifest':artifacts}
    (base/'full-summary.json').write_text(json.dumps(summary,indent=2)+'\n'); print(json.dumps(summary),flush=True)
if __name__=='__main__': main()
