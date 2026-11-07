"""Exactly two authorized verify-only native engine invocations; never retry."""
import os,sys,json,signal,time,pathlib,hashlib,resource
OUT=pathlib.Path(__file__).resolve().parent
PACKAGE=OUT.parent/'compact-release-aea62883/padua30'
sys.path.insert(0,str(PACKAGE))
from process_guard import Popen,normalize_startup
from ownership import subreaper,cleanup
from common import manifest
ENGINE=PACKAGE/'topics/padua-argmax-bridge-20261105/code/final_hybrid_engine/engine.py'
LIB=PACKAGE/'local-output/argmax-bridge-20261105/phase-checker/runtime/extracted/usr/lib/x86_64-linux-gnu'
normalize_startup();subreaper();manifest(PACKAGE)
reg=json.loads((OUT/'PREREGISTRATION.json').read_text())
for row in reg['calls']:
 n=row['n']; cert=OUT/('primary-n'+str(n)+'.json')
 data=cert.read_bytes()
 assert len(data)==row['input_bytes'] and hashlib.sha256(data).hexdigest()==row['input_sha256']
 assert row['command']==[sys.executable,'-E','-S','-B',str(ENGINE),'--mode','verify','--n',str(n),'--output',str(OUT/('verify-n'+str(n))),'--run-once','--certificate',str(cert)]
 assert not (OUT/('verify-n'+str(n))).exists()
 env=dict(os.environ,LD_LIBRARY_PATH=str(LIB));env.pop('PYTHONPATH',None);env.pop('PYTHONHOME',None)
 started=time.monotonic()
 with (OUT/('verify-n'+str(n)+'.stdout')).open('xb') as out,(OUT/('verify-n'+str(n)+'.stderr')).open('xb') as err:
  child=Popen(row['command'],cwd=PACKAGE,env=env,stdin=-3,stdout=out,stderr=err,start_new_session=True)
  try:rc=child.wait(timeout=1050)
  except BaseException:
   os.killpg(child.pid,signal.SIGKILL);child.wait();raise
 killed=cleanup()
 record={'n':n,'command':row['command'],'observed_returncode':rc,'SIGCHLD':'SIG_DFL','ECHILD':True,'cleanup_killed':killed,'wall_seconds':time.monotonic()-started,'first_failure':None if rc==0 and not killed else 'observed nonzero return or cleanup descendants'}
 with (OUT/('verify-n'+str(n)+'-exit.json')).open('x') as stream:json.dump(record,stream,indent=2);stream.write('\n')
 print(json.dumps(record),flush=True)
manifest(PACKAGE)
