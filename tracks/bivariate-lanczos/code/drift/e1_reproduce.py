#!/usr/bin/env python3
"""Regenerate a compact many-node certificate and check explicit projection.

No external capacity artifact is needed: the committed scalar-source record
supplies the prior target selection, and the committed generator reconstructs
all capacities. This uses the same producer, followed by a distinct final
projection formula. An independent-agent invocation is still required for
independent-rerun status.
"""
import argparse
import hashlib
import json
import tempfile
from pathlib import Path
from e1_cgs2_multinode import run
from e1_sign_check import check


if __name__=='__main__':
    root=Path(__file__).resolve().parents[4]
    evidence=root/'topics/padua-lanczos-drift-20261101/evidence'
    p=argparse.ArgumentParser();p.add_argument('--set',choices=['triangle','rotated'],required=True);p.add_argument('--certificates',default=str(evidence/'e1-multinode-certificates.json'));p.add_argument('--source-record',default=str(evidence/'e1-scalar-cgs2.json'));p.add_argument('--output',required=True);a=p.parse_args()
    certificate=json.loads(Path(a.certificates).read_text())
    expected=next(r for r in certificate['witnesses'] if r['set']==a.set)
    assert hashlib.sha256(Path(a.source_record).read_bytes()).hexdigest()==certificate['source_record_sha256']
    prior=next(r for r in json.loads(Path(a.source_record).read_text())['full_graph_sign_witness_runs'] if r['set']==a.set)
    generator=Path(__file__).with_name('e1_cgs2_multinode.py')
    assert hashlib.sha256(generator.read_bytes()).hexdigest()==expected['code_sha256']
    assert hashlib.sha256(Path(__file__).with_name('e1_exact.py').read_bytes()).hexdigest()==expected['aggregate_code_sha256']
    assert hashlib.sha256((json.dumps(prior,indent=2)+'\n').encode()).hexdigest()==expected['prior_witness_sha256']
    with tempfile.TemporaryDirectory(prefix='e1-reproduce-') as temporary:
        priorpath=Path(temporary)/'prior.json';priorpath.write_text(json.dumps(prior))
        generated=run(priorpath)
        for key in ['target_column','node_signs','expected_random_sign_lower_squared','explicit_greedy_sign_lower_squared']:
            assert generated[key]==expected[key],key
        resultpath=Path(temporary)/'generated.json';resultpath.write_text(json.dumps(generated))
        finalcheck=check(resultpath)
    result={'set':a.set,'result':'PASS','regenerated_target_capacities_and_signs':'matched compact certificate','explicit_projection_check':finalcheck,'generator_sha256':expected['code_sha256'],'certificate_sha256':hashlib.sha256(Path(a.certificates).read_bytes()).hexdigest(),'source_record_sha256':hashlib.sha256(Path(a.source_record).read_bytes()).hexdigest()}
    Path(a.output).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'set':a.set,'result':'PASS'}))
