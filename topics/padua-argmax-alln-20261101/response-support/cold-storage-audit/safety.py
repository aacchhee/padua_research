"""Isolated safety probes of exact pinned tool code; no Git mutations.
ROOT/load redirected to disposable fixtures. Git reads use actual audit repository;
blob_bytes and all command logic are the unmodified audited implementation.
"""
import contextlib,hashlib,io,json,pathlib,subprocess,tempfile,types
ROOT=pathlib.Path.cwd();TOP='topics/padua-argmax-alln-20261101'
REVS=['6fae535df28303b27ca1d533d9afa229660a3a20','b8fbb5c5be374bf658d2970681c7cac0fb40d737']
def git(*args,binary=False):
 d=subprocess.check_output(['git','-C',str(ROOT),*args],stderr=subprocess.PIPE);return d if binary else d.decode()
m=json.loads(git('show',REVS[0]+':'+TOP+'/cold-storage.json'));entry=m['entries'][0];data=git('cat-file','blob',entry['git_blob'],binary=True)
results=[]
for rev in REVS:
 ns={'__name__':'cold_audit','__file__':str(ROOT/'tools/cold_storage.py')};src=git('show',rev+':tools/cold_storage.py',binary=True);exec(compile(src,'tools/cold_storage.py','exec'),ns);ns['git']=git
 record={'revision':rev,'source_sha256':hashlib.sha256(src).hexdigest(),'cases':[]}
 def case(name,operation,setup,path='file.json',source_commit=m['source_commit']):
  with tempfile.TemporaryDirectory(prefix='cold-safety-') as temp:
   root=pathlib.Path(temp)/'repo';root.mkdir(); outside=pathlib.Path(temp)/'outside';outside.mkdir()
   e=dict(entry,path=path);manifest=dict(m,source_commit=source_commit,entries=[e]);ns['ROOT']=root;ns['load']=lambda slug:manifest
   target,check=setup(root,outside,e);out=io.StringIO();rc=0
   with contextlib.redirect_stdout(out):
    try:ns['cmd_'+operation](types.SimpleNamespace(slug='fixture',dest=None))
    except SystemExit as ex:rc=ex.code
    except subprocess.CalledProcessError as ex:rc=ex.returncode;print(ex.stderr.decode().strip())
   record['cases'].append({'name':name,'operation':operation,'returncode':rc,'observed':check(target),'stdout':out.getvalue().strip()})
 def regular(initial):
  def setup(root,outside,e):
   p=root/e['path'];p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(initial)
   return p,lambda x:{'exists':x.exists(),'equals_manifest':x.exists() and x.read_bytes()==data,'original_preserved':x.exists() and x.read_bytes()==initial}
  return setup
 case('restore overwrites different untracked bytes','restore',regular(b'unique user work'))
 case('restore overwrites tracked path','restore',regular(b'unique user work'),path='tools/cold_storage.py')
 case('clean preserves different untracked bytes','clean',regular(b'unique user work'))
 case('clean preserves tracked matching bytes','clean',regular(data),path='tools/cold_storage.py')
 case('clean removes matching untracked regular file','clean',regular(data))
 def leaf(root,outside,e):
  p=outside/'valuable';p.write_bytes(b'unique user work');(root/e['path']).symlink_to(p)
  return p,lambda x:{'outside_bytes_overwritten':x.read_bytes()==data}
 case('restore follows final symlink','restore',leaf)
 def parent(root,outside,e):
  (root/'link').symlink_to(outside,target_is_directory=True);p=outside/'file.json';p.write_bytes(data)
  return p,lambda x:{'outside_file_deleted':not x.exists()}
 case('clean follows parent symlink outside root','clean',parent,path='link/file.json')
 def traversal(root,outside,e):
  p=outside/'file.json';p.write_bytes(data);return p,lambda x:{'outside_file_deleted':not x.exists()}
 case('clean rejects parent traversal via Git error','clean',traversal,path='../outside/file.json')
 def missing(root,outside,e):return root/'absent',lambda x:{'missing_remains_missing':not x.exists()}
 case('verify does not validate source commit/path association','verify',missing,source_commit='0'*40)
 results.append(record)
out=ROOT/TOP/'response-support/cold-storage-audit/safety.json';out.write_text(json.dumps({'fixture_method':__doc__,'results':results},indent=1)+'\n');assert out.stat().st_size<16384
print(json.dumps({'revisions':len(results),'cases_each':len(results[0]['cases']),'receipt_bytes':out.stat().st_size}))
