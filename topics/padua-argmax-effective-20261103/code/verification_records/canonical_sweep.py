from pathlib import Path
import hashlib,json,resource,subprocess,sys,time
repo=Path('/workspace/padua_research');work=Path('/workspace/padua-work/checker')
start,end=map(int,sys.argv[1:]);rows=[]
for n in range(start,end+1):
 cert=Path(f'/workspace/padua-work/producer/final/n{n}.json.gz');output=work/f'n{n}-canonical-final-producer.json'
 before=resource.getrusage(resource.RUSAGE_CHILDREN);started=time.monotonic()
 subprocess.run(['python',str(repo/'topics/padua-argmax-effective-20261103/code/native_checker/check.py'),str(cert),'--binary',str(work/'kernel'),'--output',str(output)],check=True)
 after=resource.getrusage(resource.RUSAGE_CHILDREN)
 row=dict(n=n,cpu_user_seconds=after.ru_utime-before.ru_utime,cpu_system_seconds=after.ru_stime-before.ru_stime,wall_seconds=time.monotonic()-started,receipt_sha256=hashlib.sha256(output.read_bytes()).hexdigest(),receipt=json.loads(output.read_text()))
 rows.append(row)
 (work/f'cpu-canonical-sweep-{start}-{end}.json').write_text(json.dumps(dict(format='padua-canonical-checker-cpu-sweep-v1',method='resource.getrusage(RUSAGE_CHILDREN) differences around each sequential fresh Python-driver/native-child replay; includes driver and child CPU',rows=rows),indent=2,sort_keys=True)+'\n')
 if n in (17,24):
  selected=[r for r in rows if r['n'] in (17,24)]
  (work/'cpu-bench-canonical.json').write_text(json.dumps(dict(format='padua-native-checker-cpu-benchmark-v1',method='resource.getrusage(RUSAGE_CHILDREN) differences around sequential fresh Python-driver/native-child replay; includes both driver and child CPU',rows=selected),indent=2,sort_keys=True)+'\n')
