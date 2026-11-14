from pathlib import Path
import sys,json,time,resource
sys.path.insert(0,'topics/padua-argmax-bridge-20261105/code/regeneration_20261114')
import campaign as C
from evidence import validate_pass
R=C.R;reg=C.checked();access=R.LocalAccess(R.ROOT,str(R.ROOT));manifest=R.read(R.RELEASE/'runtime_manifest.json')
target=C.OUTPUT.with_name(C.OUTPUT.name+'-direct-essentials');target.mkdir(exist_ok=False)
rows=[];start=time.monotonic()
for n in reg['degrees']:
 for mode in ('produce','verify'):
  directory=C.OUTPUT/'jobs'/str(n)/mode
  data=validate_pass(access,directory.relative_to(R.ROOT).as_posix(),n,mode,manifest)
  original=directory/'essential-receipt.json';identity=R.identity(original)
  local=R.read(directory/'local-validation.json')
  R.require(local['receipt']==identity and original.read_bytes()==data,'unchanged native validated essential bytes')
  name=f'n{n}-{mode}.json'
  with (target/name).open('xb') as stream: stream.write(data)
  rows.append({'name':name,'bytes':identity['bytes'],'sha256':identity['sha256'],'origin':str(original)})
 if (n-319)%20==0: print(json.dumps({'validated_pairs':n-319}),flush=True)
inventory=target.with_name(target.name+'-inventory.json');R.save(inventory,{'files':rows})
usage=resource.getrusage(resource.RUSAGE_SELF)
R.save(target.with_name(target.name+'-staging-receipt.json'),{'inventory':R.identity(inventory),'preregistration':R.identity(C.OUTPUT/'preregistration.json'),'pairs':191,'proofs':382,'method':'unchanged full validate_pass plus native local-validation receipt identity; exact JSON bytes only','wall_seconds':time.monotonic()-start,'self_user_CPU_seconds':usage.ru_utime,'self_system_CPU_seconds':usage.ru_stime,'maxrss_kib':usage.ru_maxrss})
print(json.dumps({'inventory':R.identity(inventory)}),flush=True)
