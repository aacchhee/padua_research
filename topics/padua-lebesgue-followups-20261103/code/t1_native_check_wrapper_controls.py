"""Fault-test native checker publication without invoking the scientific checker."""
if not __debug__:
    raise RuntimeError('T1 native checker wrapper controls refuse optimized Python')
import argparse,json,subprocess,sys
from pathlib import Path

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--native-build-receipt',required=True);ap.add_argument('--output',required=True);options=ap.parse_args()
    program=r'''
import sys,json,tempfile,hashlib
from pathlib import Path
sys.path.insert(0,sys.argv[1])
import t1_native_check as runner
mode=sys.argv[3]
receipt=sys.argv[2]
with tempfile.TemporaryDirectory(prefix='t1-native-check-test-')as tmp:
    tmp=Path(tmp);source=tmp/'input';source.write_bytes(b'fake-control-only');output=tmp/'receipt';output.write_bytes(b'existing')
    expected=runner.digest(source)
    def fake_main():
        if mode=='exception':raise RuntimeError('injected failure')
        value={'certificate_sha256':expected if mode!='binding-fault' else'0'*64,'test_mock_only':True,'count_certified':False}
        Path(sys.argv[sys.argv.index('--output')+1]).write_text(json.dumps(value))
        if mode=='input-fault':source.write_bytes(b'changed')
        if mode=='runtime-fault':runner.check.evaluate=lambda *a:None
        if mode=='source-fault':
            original=runner.digest
            runner.digest=lambda p:'changed' if Path(p).resolve()==Path(runner.__file__).resolve() else original(p)
        return 0
    runner.check.main=fake_main
    original_evaluator=runner.check.evaluate
    sys.argv=['t1_native_check.py',str(source),'--output',str(output),'--native-build-receipt',receipt]
    arguments=sys.argv[:]
    try:runner.main()
    except (runner.check.Rejected,RuntimeError):
        assert mode!='success' and output.read_bytes()==b'existing'
    else:
        assert mode=='success';value=json.loads(output.read_text())
        assert value['test_mock_only'] and value['input_unchanged'] and value['count_only_scope'] and not value['count_certified']
    assert sys.argv==arguments and runner.check.evaluate is original_evaluator
    assert not list(tmp.glob('*.unpublished'))
print(json.dumps({'mode':mode,'passed':True,'scientific_checker_executed':False}))
'''
    rows=[]
    for mode in('success','source-fault','runtime-fault','input-fault','binding-fault','exception'):
        r=subprocess.run([sys.executable,'-B','-c',program,str(Path(__file__).parent),str(Path(options.native_build_receipt).resolve()),mode],text=True,capture_output=True,check=True);rows.append(json.loads(r.stdout))
    result={'all_controls_passed':True,'count_certified':False,'rows':rows}
    Path(options.output).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps(result))
if __name__=='__main__':main()
