"""New join wrapper controls with synthetic, nonmathematical fixtures."""
import argparse
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--driver',required=True)
    parser.add_argument('--output',required=True);args=parser.parse_args()
    driver=Path(args.driver).resolve();topic=driver.parent.parent
    frozen=topic.parent/'padua-proof-attempts-2-20261101'/'code'
    sys.path.insert(0,str(frozen))
    import a5_n8_join_axis_controls as controls
    base=controls.m
    sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
    before=sha(driver)
    interior,boundary=controls.fixtures()
    interior['metadata']['source_sha256']=sha(frozen/'a5_n8_boxes.py')
    boundary['metadata']={'source_sha256':sha(driver.with_name('t1_boundary.py')),
                          'frozen_boundary_sha256':sha(frozen/'a5_n8_boundary.py')}
    cases=[('valid',None,None),
           ('pending_interior',lambda a:a['pending_paths'].append('0'),None),
           ('missing_leaf_subtree',lambda a:a['leaves'][0].update(path='0'),None),
           ('false_leaf_accounting',lambda a:a['summary'].update(all_gradient_leaves=2),None),
           ('counterfeit_interior_source',lambda a:a['metadata'].update(source_sha256='0'*64),None),
           ('missing_edge',None,lambda a:a['edges'].pop()),
           ('missing_corner',None,lambda a:a['corners'].pop()),
           ('unresolved_boundary',None,lambda a:a['unresolved'].append({'fixture':True})),
           ('counterfeit_boundary_wrapper',None,lambda a:a['metadata'].update(source_sha256='0'*64)),
           ('counterfeit_boundary_frozen_ancestry',None,lambda a:a['metadata'].update(frozen_boundary_sha256='0'*64)),
           ('wrong_raw_interior_hash',None,None),('wrong_raw_boundary_hash',None,None),
           ('existing_output_preserved',None,None)]
    results=[]
    with tempfile.TemporaryDirectory(prefix='t1-independent-join-')as directory:
        folder=Path(directory)
        for name,change_i,change_b in cases:
            i,b=copy.deepcopy(interior),copy.deepcopy(boundary)
            if change_i:change_i(i)
            if change_b:change_b(b)
            ip=folder/(name+'.interior.json');bp=folder/(name+'.boundary.json')
            op=folder/(name+'.joined.gz');rp=folder/(name+'.receipt.json')
            ip.write_bytes(base.canonical(i));bp.write_bytes(base.canonical(b))
            if name=='existing_output_preserved':op.write_bytes(b'preserve existing')
            command=[sys.executable,'-B',str(driver),str(ip),str(bp),'--interior-sha256',
                     '0'*64 if name=='wrong_raw_interior_hash'else sha(ip),
                     '--boundary-sha256','0'*64 if name=='wrong_raw_boundary_hash'else sha(bp),
                     '--output',str(op),'--receipt',str(rp)]
            run=subprocess.run(command,capture_output=True,text=True)
            if name=='valid':
                assert run.returncode==0,run.stderr
                output=base.decode(op.read_bytes());receipt=json.loads(rp.read_text())
                assert receipt['count_certified']is False and receipt['structural_complete']is True
                for key in i:
                    if key not in ('summary','metadata'):assert base.canonical(output[key])==base.canonical(i[key])
                assert base.canonical({'edges':output['edges'],'corners':output['corners'],
                                       'summary':output['boundary_summary']})==base.canonical(base.components(b))
                assert receipt['output_sha256']==sha(op)
            else:
                assert run.returncode!=0 and not rp.exists(),(name,run.stdout,run.stderr)
                if name=='existing_output_preserved':assert op.read_bytes()==b'preserve existing'
                else:assert not op.exists(),name
            assert ip.read_bytes()==base.canonical(i)and bp.read_bytes()==base.canonical(b)
            results.append({'case':name,'passed':True,'returncode':run.returncode,
                            'failure':run.stderr.splitlines()[-1]if run.stderr else None})
    assert sha(driver)==before
    result={'all_controls_passed':True,'count_certified':False,
            'scope':'synthetic structural fixtures; no mathematical certificate accepted',
            'driver_sha256':before,'driver_sha256_after':sha(driver),
            'control_sha256':sha(__file__),'controls':results}
    Path(args.output).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,sort_keys=True))
if __name__=='__main__':main()
