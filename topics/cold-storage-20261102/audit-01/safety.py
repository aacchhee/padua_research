import contextlib, hashlib, importlib.util, io, json, pathlib, subprocess, tempfile, types
from unittest.mock import patch
# Run from a repository root containing the candidate tools/cold_storage.py.
P=pathlib.Path; spec=importlib.util.spec_from_file_location('cs',P.cwd()/'tools/cold_storage.py'); cs=importlib.util.module_from_spec(spec);spec.loader.exec_module(cs)
with tempfile.TemporaryDirectory(prefix='padua-cold-audit-') as td:
 r=P(td); cs.ROOT=r
 def git(*a,input=None): return subprocess.check_output(['git','-C',str(r),*a],input=input,stderr=subprocess.DEVNULL)
 git('init','-q'); data=b'archived data\n'; blob=git('hash-object','-w','--stdin',input=data).decode().strip()
 e={'path':'topics/sample/data.json','git_blob':blob,'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)}
 m={'source_commit':'test fixture','entries':[e]}; path=r/e['path'];path.parent.mkdir(parents=True)
 (path.parent/'cold-storage.json').write_text(json.dumps(m))
 def call(fn,**kw):
  buf=io.StringIO()
  with contextlib.redirect_stdout(buf): fn(types.SimpleNamespace(slug='sample',**kw))
  return json.loads(buf.getvalue())
 checks={}
 path.write_bytes(b'new user results\n');call(cs.cmd_clean);checks['clean_preserves_differing_copy']=path.read_bytes()==b'new user results\n'
 call(cs.cmd_restore,dest=None);checks['restore_overwrites_differing_copy']=path.read_bytes()==data
 git('add','--',e['path']);call(cs.cmd_clean);checks['clean_preserves_tracked_copy']=path.exists()
 path.write_bytes(b'local changes to tracked file\n');call(cs.cmd_restore,dest=None);checks['restore_overwrites_tracked_modification']=path.read_bytes()==data
 git('rm','--cached','--',e['path']);call(cs.cmd_clean);checks['clean_removes_matching_untracked_copy']=not path.exists()
 original=P.write_bytes
 def corrupt(target,contents):
  result=original(target,contents)
  if 'export-bad' in str(target): original(target,b'bad disk contents\n')
  return result
 with patch.object(P,'write_bytes',corrupt): receipt=call(cs.cmd_export,dest=str(r/'export-bad'))
 exported=r/'export-bad'/'sample'/e['path']; checks['export_reports_match_with_corrupt_destination']=receipt['all_hashes_match_manifest'] and hashlib.sha256(exported.read_bytes()).hexdigest()!=e['sha256']
 good=call(cs.cmd_export,dest=str(r/'export-good'));checks['ordinary_export_matches']= (r/'export-good'/'sample'/e['path']).read_bytes()==data
 result={'fixture':'isolated temporary Git repository; no real repository files modified','checks':checks,'all_expected_behaviors_reproduced':all(checks.values())}
 P('/tmp/cold-audit-safety.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2));assert all(checks.values())
