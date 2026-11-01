"""Independent replay harness; scripts and mathematics remain unchanged."""
from pathlib import Path
import concurrent.futures,datetime,hashlib,json,os,subprocess,time
OUT=Path(__file__).resolve().parent
CODE=OUT.parent.parent/'code'
RUNS=[['check.py'],['cell.py','3','4','5','6','7','8','9','10','12','15','20','30','40'],['interior.py','8','12','16','24','32','48'],['edgeprofile.py','12','24','48','96'],['strips.py','24','48'],['n2_edges.py']]
def run(args):
    name=Path(args[0]).stem
    start=datetime.datetime.now(datetime.timezone.utc).isoformat(); t=time.perf_counter()
    env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1')
    with (OUT/(name+'.out')).open('w') as out, (OUT/(name+'.err')).open('w') as err:
        p=subprocess.run(['python3',*args],cwd=CODE,env=env,stdout=out,stderr=err)
    rec={'command':['python3',*args],'cwd':str(CODE),'started_utc':start,'finished_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'wall_seconds':time.perf_counter()-t,'returncode':p.returncode,'environment_overrides':{k:env[k] for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','PYTHONDONTWRITEBYTECODE']},'output':name+'.out','output_sha256':hashlib.sha256((OUT/(name+'.out')).read_bytes()).hexdigest()}
    (OUT/(name+'.run.json')).write_text(json.dumps(rec,indent=2)+'\n')
    print(name,rec['wall_seconds'],p.returncode,flush=True)
    return rec
if __name__=='__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        records=list(pool.map(run,RUNS))
    (OUT/'runs.json').write_text(json.dumps(records,indent=2)+'\n')
