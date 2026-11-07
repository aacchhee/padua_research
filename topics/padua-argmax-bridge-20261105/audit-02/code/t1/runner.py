import json,resource,subprocess,sys,time
# usage: runner.py LOGJSON -- cmd...
log=sys.argv[1];cmd=sys.argv[3:]
t0=time.monotonic();start=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())
with open(log+'.stdout','wb') as o,open(log+'.stderr','wb') as e:
    p=subprocess.run(cmd,stdout=o,stderr=e)
ru=resource.getrusage(resource.RUSAGE_CHILDREN)
rec={'cmd':cmd,'start_utc':start,'wall_s':time.monotonic()-t0,'exit_code':p.returncode,'children_user_s':ru.ru_utime,'children_sys_s':ru.ru_stime,'children_cpu_s':ru.ru_utime+ru.ru_stime,'maxrss_kB':ru.ru_maxrss}
open(log,'w').write(json.dumps(rec,indent=1)+'\n');print(json.dumps(rec))
