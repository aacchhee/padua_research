"""Independent publication controls; fake checker exercises no math predicate."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import tempfile

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--driver',required=True)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    path=Path(args.driver).resolve()
    sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
    before=sha(path)
    spec=importlib.util.spec_from_file_location('reviewed_driver',path)
    driver=importlib.util.module_from_spec(spec);spec.loader.exec_module(driver)
    driver.cached.install=lambda:None
    checks=[]
    with tempfile.TemporaryDirectory(prefix='t1-independent-wrapper-') as folder:
        folder=Path(folder)
        for case in ('success','checker_reject','checker_exception','post_guard_failure',
                     'input_changed','wrapper_changed','receipt_wrong_input'):
            input_path=folder/(case+'.input');input_path.write_bytes(b'fixture input')
            output_path=folder/(case+'.json')
            original_digest=driver.digest
            calls=0
            def guard():
                nonlocal calls
                calls+=1
                if case=='post_guard_failure' and calls==2:raise RuntimeError('injected source guard')
            driver.cached.guard_entry=guard
            def fake_checker():
                if case=='checker_exception':raise RuntimeError('injected checker exception')
                data={'certificate_sha256':sha(input_path),
                      'accepted':case!='checker_reject','count_certified':case!='checker_reject'}
                if case=='receipt_wrong_input':data['certificate_sha256']='0'*64
                Path(sys.argv[sys.argv.index('--output')+1]).write_text(json.dumps(data))
                if case=='input_changed':input_path.write_bytes(b'changed fixture')
                if case=='wrapper_changed':
                    driver.digest=lambda p:'0'*64 if Path(p).resolve()==path else original_digest(p)
                return int(case=='checker_reject')
            driver.cached.check.main=fake_checker
            arguments=sys.argv[:]
            sys.argv[:]=[str(path),str(input_path),'--output',str(output_path)]
            try:
                try:
                    rc=driver.main();error=None
                except (RuntimeError,AssertionError) as e:
                    rc=None;error=str(e)
                if case in ('success','checker_reject'):
                    data=json.loads(output_path.read_text())
                    assert rc==int(case=='checker_reject')
                    assert data['accepted']==(case=='success')
                    assert data['count_certified']==(case=='success')
                    assert data['input_unchanged'] and data['execution_entry_source_unchanged']
                else:
                    assert error is not None and not output_path.exists()
                assert not list(folder.glob('*.unpublished'))
                checks.append({'case':case,'passed':True,'published':output_path.exists(),
                               'returncode':rc,'error':error})
            finally:
                driver.digest=original_digest;sys.argv[:]=arguments
    assert sha(path)==before
    result={'scope':'publication structure using fake checker; no mathematical certificate accepted',
            'all_controls_passed':True,'driver_sha256':before,'driver_sha256_after':sha(path),
            'control_sha256':sha(__file__),'controls':checks}
    Path(args.output).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,sort_keys=True))
if __name__=='__main__':main()
