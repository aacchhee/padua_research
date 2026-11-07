import sys,json,time,resource,hashlib
from pathlib import Path
root=Path('/workspace/p02'); archive=Path('/workspace/d278941b28f0-padua-local-20261107T071625.609373Z.zip')
start=time.monotonic(); before=resource.getrusage(resource.RUSAGE_SELF)
manifest=(root/'runtime_manifest.json').read_bytes(); expected='583435701282d0f22aa8d2d9429e735ed8c125b9cf285c3f6ac57983157c2eb4'
assert hashlib.sha256(manifest).hexdigest()==expected
for name,row in json.loads(manifest)['files'].items():
 data=(root/name).read_bytes(); assert len(data)==row['bytes'] and hashlib.sha256(data).hexdigest()==row['sha256']
sys.path.insert(0,str(root))
import verify_return
result=verify_return.verify(archive,root,expected,partial=True)
assert result['completed_subset']==[41,511] and result['failed_or_interrupted']==[] and result['never_started']==[] and result['complete280'] is False
hashvalue=hashlib.sha256()
with archive.open('rb') as f:
 while block:=f.read(1048576):hashvalue.update(block)
after=resource.getrusage(resource.RUSAGE_SELF)
print(json.dumps({'archive':str(archive),'bytes':archive.stat().st_size,'sha256':hashvalue.hexdigest(),'result':result,'review_CPU':after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,'review_wall':time.monotonic()-start,'native_executions':0},indent=2))
