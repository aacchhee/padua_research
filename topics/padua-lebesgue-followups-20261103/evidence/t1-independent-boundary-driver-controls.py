"""Publication-only fake boundary controls; no scientific method is executed."""
if not __debug__:raise RuntimeError('independent controls refuse optimized Python')
import argparse,hashlib,json,subprocess,sys
from pathlib import Path

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--driver',required=True)
    ap.add_argument('--output',required=True);a=ap.parse_args()
    driver=Path(a.driver).resolve();before=hashlib.sha256(driver.read_bytes()).hexdigest()
    program=r'''
import contextlib,hashlib,importlib.util,io,json,sys,tempfile
from pathlib import Path
from types import SimpleNamespace
path=Path(sys.argv[1]);mode=sys.argv[2]
spec=importlib.util.spec_from_file_location('boundary_driver',path)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
with tempfile.TemporaryDirectory(prefix='t1-independent-boundary-')as folder:
 folder=Path(folder);fp=folder/'field.json';bp=folder/'boundary.json';op=folder/'out.json'
 fp.write_text('{"field_embedding":{}}')
 boundary={'edges':[],'corners':[],'summary':{'complete':True,'unresolved':0,'edge':0,'corner':0,'counts':{}},'unresolved':[]}
 if mode=='summary_fault':boundary['summary']['edge']=1
 if mode=='unresolved':boundary['unresolved']=[{'fake':True}]
 bp.write_text(json.dumps(boundary));entry=path.read_bytes()
 if mode=='existing_output':op.write_bytes(b'preserve existing')
 result={'verified_edge_maxima_enclosures':0,'verified_corner_maxima':0,'verified_edge_patterns':0,'edge_dispositions':{},'corner_active_patterns':0,'edge_roots':[],'corner_roots':[]}
 class Fake:
  def __init__(self,embedding):self.edge_flat_values=[];self.embedding_result={'fake':True}
  def boundaries(self,edges,corners):
   if mode=='exception':raise RuntimeError('injected method failure')
   if mode=='input_fault':bp.write_bytes(b'changed')
   if mode=='source_fault':
    saved=m.sha;m.sha=lambda raw:'0'*64 if raw==entry else saved(raw)
   if mode=='method_fault':Fake.boundaries=lambda *a:None
   return result
 m.check.Verifier=Fake;m.ORIGINAL_VERIFIER=Fake;m.ORIGINAL_BOUNDARY=Fake.boundaries
 args=SimpleNamespace(field_certificate=str(fp),field_certificate_sha256=m.sha(fp.read_bytes()),boundary=str(bp),boundary_sha256=m.sha(bp.read_bytes()),output=str(op))
 if mode=='raw_hash_fault':args.boundary_sha256='0'*64
 if mode=='field_hash_fault':args.field_certificate_sha256='0'*64
 try:
  with contextlib.redirect_stdout(io.StringIO()):m.replay(args)
 except (m.check.Rejected,RuntimeError):
  assert mode!='success'
  if mode=='existing_output':assert op.read_bytes()==b'preserve existing'
  else:assert not op.exists()
 else:
  assert mode=='success';data=json.loads(op.read_text())
  assert data['boundary_verified']and data['all_boundary_predicates_replayed']
  assert not data['interior_verified']and not data['count_certified']and not data['complete_closed_count']
  assert data['boundary_method_ast_sha256']==m.frozen_boundary_ast()
 print(json.dumps({'mode':mode,'passed':True,'scientific_method_executed':False}))
'''
    rows=[]
    for mode in ('success','summary_fault','unresolved','exception','input_fault','source_fault','method_fault','existing_output','raw_hash_fault','field_hash_fault'):
        run=subprocess.run([sys.executable,'-B','-c',program,str(driver),mode],capture_output=True,text=True)
        assert run.returncode==0,(mode,run.stdout,run.stderr)
        rows.append(json.loads(run.stdout))
    refusals=[]
    for flag in('-O','-OO'):
        run=subprocess.run([sys.executable,flag,str(driver)],capture_output=True,text=True)
        assert run.returncode and 'refuse'in run.stderr;refusals.append(flag)
    assert hashlib.sha256(driver.read_bytes()).hexdigest()==before
    result={'all_controls_passed':True,'count_certified':False,'scope':'mock boundary method publication only',
            'driver_sha256':before,'driver_sha256_after':before,'rows':rows,'optimized_refusals':refusals,
            'control_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(a.output).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps(result))
if __name__=='__main__':main()
