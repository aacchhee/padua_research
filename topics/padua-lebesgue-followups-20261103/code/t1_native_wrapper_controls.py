"""Publication-only controls: fake solve never runs a scientific predicate."""
if not __debug__:
    raise RuntimeError('T1 native wrapper controls refuse optimized Python')
import argparse,hashlib,json,subprocess,sys
from pathlib import Path

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--native-build-receipt',required=True);ap.add_argument('--output',required=True);a=ap.parse_args()
    program=r'''
import sys,json
from pathlib import Path
sys.path.insert(0,sys.argv[1])
import t1_native_produce as runner
import a5_n8_boxes as module
mode=sys.argv[3]
records=[]
def fake_write(out,path):records.append(out)
def fake_solve(args):
    if mode=='source-fault':
        original=runner.digest
        runner.digest=lambda p: 'changed' if Path(p).name=='t1_native.c' else original(p)
    if mode=='runtime-fault':module.evaluate=lambda *a:None
    module.write_artifact({'metadata':{}},args.output)
module.write_artifact=fake_write
module.solve=fake_solve
sys.argv=['t1_native_produce.py','--native-build-receipt',sys.argv[2],'--output','unused.fake']
try:runner.main()
except AssertionError:
    assert mode!='success' and not records
else:
    assert mode=='success' and len(records)==1
    execution=records[0]['metadata']['execution']
    assert execution['frozen_sources_unchanged']
    assert len(execution['native_sources_and_binary_sha256'])==6
    assert execution['native_build']['source_sha256']==runner.digest(Path(runner.__file__).with_name('t1_native.c'))
print(json.dumps({'mode':mode,'passed':True,'scientific_solve_executed':False}))
'''
    rows=[]
    for mode in ('success','source-fault','runtime-fault'):
        r=subprocess.run([sys.executable,'-B','-c',program,str(Path(__file__).parent),str(Path(a.native_build_receipt).resolve()),mode],text=True,capture_output=True,check=True)
        rows.append(json.loads(r.stdout))
    result={'all_controls_passed':True,'count_certified':False,'rows':rows,'wrapper_sha256':hashlib.sha256(Path(__file__).with_name('t1_native_produce.py').read_bytes()).hexdigest()}
    Path(a.output).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps(result))
if __name__=='__main__':main()
