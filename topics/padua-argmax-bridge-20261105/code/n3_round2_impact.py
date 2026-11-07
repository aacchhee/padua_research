#!/usr/bin/env python3
"""Verify the accepted corner premise against the frozen conditional float run.

No mathematical kernels or search runs are executed by this input-impact check.
"""
import hashlib
import json
from pathlib import Path
from n3_native_receipt import identity

ROOT=Path(__file__).resolve().parents[3]
TOPIC=Path(__file__).resolve().parents[1]

def verify(record):
    path=ROOT/record['path'];b=path.read_bytes()
    assert len(b)==record['bytes'] and hashlib.sha256(b).hexdigest()==record['sha256'],record['path']

def main():
    float_path=TOPIC/'evidence/n3-float-v2.json'
    corner_path=TOPIC/'evidence/independent-corner-replay.json'
    run=json.loads(float_path.read_text());corner=json.loads(corner_path.read_text())
    assert run['corner_premise'].startswith('CONDITIONAL')
    assert corner['schema']=='independent-corner-replay-v2' and corner['status'].startswith('PASS ')
    checker_sources=[x for x in corner['sources'] if x['path'].endswith('/check_corner_exact.cpp')]
    assert len(checker_sources)==1
    assert checker_sources[0]['sha256']!='84cbbe858b52711c99713b05f6b538eb352efb73aa41c2c1eac715288362bfa6', 'Initial checker superseded for current use'
    verified=[]
    for item in run['sources']+run['mathematical_inputs']+run['raw']:
        verify(item);verified.append(item['path'])
    for item in corner['sources']:
        verify(item)
    for row in corner['rows']:
        verify(row['raw'])
    rows={r['degree']:r for r in corner['rows']}
    degrees={r['n']:r for r in run['degrees']}
    assert set(degrees)=={33,64,128}
    for n in degrees:
        row=rows[n]
        assert row['exact_assembly_pass'] is True
        assert all(value is True for value in row['own_interval_inside_producer'].values())
        assert row['certified_common_kappa']=='1/12500' and row['certified_scaled_phase_box']=='1/128'
        assert degrees[n]['complete_float_cover'] is True and degrees[n]['unresolved_frontier']==0
    assert degrees[64]['cpu_seconds']<600
    assert degrees[33]['visited']>=degrees[64]['visited']>=degrees[128]['visited']
    source=(TOPIC/'code/n3_float_v2.py').read_text()
    expected='n in [33,64,128] and aa<=1/128 and bb<=1/128'
    assert expected in source
    result={'status':'PASS input-impact verification only; no new mathematical execution',
            'rules_input':'3dda890275a7599caa707b0fb8c0b6e6f6a80643',
            'command':'python topics/padua-argmax-bridge-20261105/code/n3_round2_impact.py',
            'source':identity(Path(__file__).resolve()),'float_receipt':identity(float_path),
            'corner_independent_receipt':identity(corner_path),'verified_float_file_identities':verified,
            'patch_interface':{'degrees':[33,64,128],'phase_square':'1/128','common_kappa':'1/12500'},
            'completed_float_counts':{str(n):degrees[n]['visited'] for n in sorted(degrees)},
            'cpu_seconds':{str(n):degrees[n]['cpu_seconds'] for n in sorted(degrees)},
            'interpretation':'Frozen v2 conditional corner premise is now independently verified; original execution status and timings are unchanged.',
            'superseded_guard':'n3-round2-impact-initial.json refers only to the initial checker, before its rational-canonicalization fix.',
            'limits':['This guard trusts the named different-agent corner acceptance; it does not replay that arithmetic.',
                      'B2 float timing and finite count criteria hold at the three named degrees; no universal count law is proved.',
                      'Floating phase leaves are not outward certificates. No full-phase checker or global argmax extension follows.',
                      'An unnecessary v3 repeat was terminated before any degree completion; it supplies no evidence.']}
    (TOPIC/'evidence/n3-round2-impact.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'counts':result['completed_float_counts'],'cpu_seconds':result['cpu_seconds']}))

if __name__=='__main__':main()
