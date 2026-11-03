"""Strict three-pair wrapper around inherited exact E-C checker; shared kernel."""
import argparse,copy,json,sys,time
from pathlib import Path
SOURCE=Path(__file__).resolve().parents[3]/'padua-argmax-alln-20261101'/'code'/'gated'
sys.path.insert(0,str(SOURCE))
import d3_edge_common as c
from d3_edge_check import check_pair
EXPECTED=[(13,0,9,7),(17,0,11,9),(24,24,11,13)]
c.DEGREES=(13,17,24)

def check(data):
    assert data['format']=='padua-effective-g6-spots-v1'
    assert data['inherited_source_sha256']==c.source_hashes()
    assert data['producer_sha256']==c.digest(Path(__file__).with_name('g6_exact_spots.py'))
    assert data['precision']==c.g.PRECISION and data['scale']==c.g.S
    assert [tuple(r['identity']) for r in data['rows']]==EXPECTED
    assert c.arithmetic_controls()
    return [check_pair(r['certificate'],identity) for r,identity in zip(data['rows'],EXPECTED)]

def controls(data):
    def missing_row(d):d['rows'].pop()
    def missing_leaf(d):d['rows'][0]['certificate']['leaves'].pop()
    def duplicate_leaf(d):d['rows'][0]['certificate']['leaves'].append(copy.deepcopy(d['rows'][0]['certificate']['leaves'][0]))
    cases={'missing_row':missing_row,'missing_leaf':missing_leaf,'duplicate_leaf':duplicate_leaf,
    'nonedge_j':lambda d:d['rows'][0]['certificate'].update(j=1),
    'wrong_target':lambda d:d['rows'][0]['certificate'].update(target=2),
    'bad_path':lambda d:d['rows'][0]['certificate']['leaves'][0].update(path='X'),
    'forged_bound':lambda d:d['rows'][0]['certificate']['leaves'][0].update(upper=0),
    'forged_target':lambda d:d['rows'][0]['certificate'].update(target_lower=0),
    'forged_source_hash':lambda d:d['inherited_source_sha256'].update({'code/gated/d3_edge_common.py':'0'*64}),
    'forged_scale':lambda d:d.update(scale=1),
    'pending_leaf':lambda d:d['rows'][0]['certificate'].update(pending=['0'])}
    rejected=[]
    for label,mutate in cases.items():
        changed=copy.deepcopy(data);mutate(changed)
        try:check(changed)
        except (AssertionError,KeyError,ValueError,TypeError):rejected.append(label)
        else:raise AssertionError('malformed certificate accepted: '+label)
    return rejected

def main():
    p=argparse.ArgumentParser();p.add_argument('certificate');p.add_argument('--output',required=True);p.add_argument('--controls',action='store_true');a=p.parse_args();start=time.process_time()
    data=json.loads(Path(a.certificate).read_text());pairs=check(data)
    out={'accepted':True,'pairs':pairs,'certificate_sha256':c.digest(a.certificate),'checker_sha256':c.digest(__file__),'inherited_source_sha256':c.source_hashes(),'shared_arithmetic_kernel':True}
    if a.controls:out['malformed_controls_rejected']=controls(data)
    out['cpu_seconds']=time.process_time()-start;Path(a.output).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
