"""Bounded four-process orchestration; no numerical or certificate logic."""
import hashlib, json, os, resource, subprocess, sys, time
from pathlib import Path

def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def main():
    base=Path(sys.argv[1]); base.mkdir(parents=True,exist_ok=False); resource.setrlimit(resource.RLIMIT_CPU,(80,10800))
    source=Path(__file__).parent
    archive='local-output/argmax-bridge-20261105/actual-return-20261107/return.tar.gz'
    additional='local-output/argmax-bridge-20261105/onset512-local-20261108-essential'
    started=time.monotonic(); cpu=time.process_time(); before=resource.getrusage(resource.RUSAGE_CHILDREN)
    jobs=[]; files=[]; stop=None
    for j in range(4):
        degree_list=list(range(41+j,512,4))
        cmd=['timeout','--signal=TERM','--kill-after=5s','7200s','env','OPENBLAS_NUM_THREADS=1',
             'OMP_NUM_THREADS=1',sys.executable,str(source/'run.py'),'--archive',archive,
             '--additional-dir',additional,'--degrees',','.join(map(str,degree_list)),
             '--cpu-limit','2670','--output',str(base/('worker-'+str(j)))]
        out=(base/('worker-'+str(j)+'.stdout')).open('x'); err=(base/('worker-'+str(j)+'.stderr')).open('x')
        files.extend([out,err]); proc=subprocess.Popen(cmd,stdout=out,stderr=err,start_new_session=True)
        jobs.append({'worker':j,'degrees':degree_list,'command':cmd,'process':proc})
    while any(job['process'].poll() is None for job in jobs):
        failed=[job for job in jobs if job['process'].poll() not in (None,0)]
        if failed or time.monotonic()-started>7250:
            stop='worker failure' if failed else 'outer wall cap'
            for job in jobs:
                if job['process'].poll() is None: os.killpg(job['process'].pid,15)
            break
        time.sleep(.2)
    for job in jobs:
        try: job['returncode']=job['process'].wait(timeout=10)
        except subprocess.TimeoutExpired:
            os.killpg(job['process'].pid,9); job['returncode']=job['process'].wait(); stop='termination timeout'
        del job['process']
    for f in files: f.close()
    after=resource.getrusage(resource.RUSAGE_CHILDREN)
    totalcpu=time.process_time()-cpu+after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime
    observations={'jobs':jobs,'stop':stop,'wall_seconds':time.monotonic()-started,'CPU_seconds_inclusive':totalcpu,
                  'maximum_child_RSS_KiB':after.ru_maxrss,'source_hashes':{p.name:digest(p) for p in source.glob('*.py')}}
    (base/'outer-observation.json').write_text(json.dumps(observations,indent=2)+'\n')
    if stop or any(j['returncode'] for j in jobs) or totalcpu>10800: raise SystemExit(1)
    rows=[]
    for j in range(4): rows.extend(json.loads(line) for line in (base/('worker-'+str(j))/'observations.jsonl').read_text().splitlines())
    expected={(n,p) for n in range(41,512) for p in ['produce','verify']}
    if len(rows)!=942 or {(r['n'],r['pass']) for r in rows}!=expected or not all(r['accepted'] for r in rows): raise SystemExit(1)
    artifacts=[]
    for p in sorted(base.rglob('*')):
        if p.is_file(): artifacts.append({'path':str(p),'bytes':p.stat().st_size,'sha256':digest(p)})
    summary={'accepted':942,'degrees':471,'CPU_seconds_inclusive':totalcpu,'wall_seconds':observations['wall_seconds'],
             'scope':'independent substituted-bound recertification','all_native_endpoints_validated':False,
             'artifact_manifest':artifacts}
    (base/'full-summary.json').write_text(json.dumps(summary,indent=2)+'\n'); print(json.dumps(summary),flush=True)
if __name__=='__main__': main()
