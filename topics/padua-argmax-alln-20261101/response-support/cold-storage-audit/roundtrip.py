"""Read pinned tool via git show; exercise it without replacing working source.
Run from repository root, before refreshing evidence-manifest.json.
Writes only restored manifest paths (then cleans), /tmp, and its JSON receipt.
"""
import hashlib,json,pathlib,subprocess,sys
ROOT=pathlib.Path.cwd(); TOP='topics/padua-argmax-alln-20261101'; SLUG=TOP.split('/')[-1]
SOURCE='1cecd68ac0a64b01ed7b2d262b6263a955a7d4d7'
REVS=['6fae535df28303b27ca1d533d9afa229660a3a20','b8fbb5c5be374bf658d2970681c7cac0fb40d737']
def git(*args):return subprocess.check_output(['git',*args])
def digest(data):return hashlib.sha256(data).hexdigest()
m=json.loads(git('show',REVS[0]+':'+TOP+'/cold-storage.json'))
assert (ROOT/TOP/'cold-storage.json').read_bytes()==git('show',REVS[0]+':'+TOP+'/cold-storage.json')
assert len({e['path'] for e in m['entries']})==36
assert all(not (ROOT/e['path']).exists() for e in m['entries']), 'Refuse existing destinations'
changes=git('diff','--name-status',SOURCE,REVS[0]).decode().splitlines()
deleted={x[2:] for x in changes if x.startswith('D\t')}
assert deleted=={e['path'] for e in m['entries']}
receipt={'source':SOURCE,'initial':REVS[0],'latest':REVS[1],'entries':len(m['entries']),'bytes':sum(e['bytes'] for e in m['entries']),'deleted_equals_manifest':True,'changes':changes,'runs':[]}
for e in m['entries']:
 d=git('show',SOURCE+':'+e['path'])
 assert git('rev-parse',SOURCE+':'+e['path']).decode().strip()==e['git_blob']
 assert digest(d)==e['sha256'] and len(d)==e['bytes']
receipt['all_source_path_blob_sha256_size_identities_match']=True
wrapper="import subprocess,sys; from pathlib import Path; src=subprocess.check_output(['git','show',sys.argv[1]+':tools/cold_storage.py']); sys.argv=['tools/cold_storage.py']+sys.argv[2:]; exec(compile(src,'tools/cold_storage.py','exec'),{'__name__':'__main__','__file__':str(Path.cwd()/'tools/cold_storage.py')})"
for rev in REVS:
 run={'revision':rev,'tool_blob':git('rev-parse',rev+':tools/cold_storage.py').decode().strip(),'tool_sha256':digest(git('show',rev+':tools/cold_storage.py')),'commands':[]}
 for command in ['verify','restore','verify','clean','verify']:
  if command=='clean':
   for e in m['entries']:assert (ROOT/e['path']).read_bytes()==git('show',SOURCE+':'+e['path'])
   run['restored_bytes_equal_git_show_all_36']=True
  p=subprocess.run([sys.executable,'-B','-c',wrapper,rev,command,SLUG],capture_output=True,text=True)
  run['commands'].append({'command':command,'returncode':p.returncode,'stdout':json.loads(p.stdout) if p.stdout else '', 'stderr':p.stderr})
  assert p.returncode==0,p.stderr
 assert all(not (ROOT/e['path']).exists() for e in m['entries'])
 run['all_restored_copies_absent_after_clean']=True
 receipt['runs'].append(run)
# Export current revision to an empty scratch destination; never AC's machine.
export_root=pathlib.Path('/tmp/padua-cold-audit/export');assert not export_root.exists()
p=subprocess.run([sys.executable,'-B','-c',wrapper,REVS[1],'export',SLUG,'--dest',str(export_root)],capture_output=True,text=True)
assert p.returncode==0,p.stderr
for e in m['entries']:assert (export_root/SLUG/e['path']).read_bytes()==git('show',SOURCE+':'+e['path'])
receipt['scratch_export']={'returncode':p.returncode,'stdout':json.loads(p.stdout),'all_36_bytes_equal_source':True,'delivery_to_AC':'NOT PERFORMED'}
out=ROOT/TOP/'response-support/cold-storage-audit/roundtrip.json';out.write_text(json.dumps(receipt,indent=1)+'\n');assert out.stat().st_size<16384
print(json.dumps({'roundtrip_both_revisions':'PASS','identities_36':'PASS','export_36':'PASS','receipt_bytes':out.stat().st_size}))
