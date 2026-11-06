#!/usr/bin/env python3
"""Response regression checks; run artifacts stay outside Git in /tmp.

No theorem is inferred from these finite checks. Source tables are read only.
"""
import ast
import csv
import hashlib
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import numpy
import mpmath
import sympy

TOPIC=Path(__file__).resolve().parents[1]
WORK=Path('/tmp/nn-mop-response-code-checks')
EXTERNAL=Path('/tmp/c4-external-grid-bits.json')
NATIVE=Path('/tmp/nn-mop-c3-grid-raw.json')
BASELINE=Path('/tmp/c4-comparison-bits-raw.json')
MATRIX=Path('/tmp/nn-mop-conditioning-20261106/c1-matrix-all.json')

def pin(p):
    return dict(path=str(p),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest())

def run_compare(external,native,destination):
    destination.mkdir(parents=True,exist_ok=True)
    command=[sys.executable,str(TOPIC/'code/c4_compare.py'),'--external',str(external),
             '--native',str(native),'--raw',str(destination/'raw.json'),
             '--evidence',str(destination/'tables')]
    with (destination/'run.log').open('w') as stream:
        subprocess.run(command,check=True,stdout=stream,stderr=subprocess.STDOUT,
                       env={**os.environ,'OPENBLAS_NUM_THREADS':'1'})
    return command,json.loads((destination/'raw.json').read_text())

def main():
    WORK.mkdir(parents=True,exist_ok=True)
    receipt=json.loads((TOPIC/'c4-comparison-receipt.json').read_text())
    assert pin(BASELINE)['sha256']==receipt['raw']['sha256']
    baseline=json.loads(BASELINE.read_text())
    command,healthy=run_compare(EXTERNAL,NATIVE,WORK/'healthy')
    assert healthy['cases']==baseline['cases']
    assert healthy['binary64_input_matches']==baseline['binary64_input_matches']
    assert len(healthy['cases'])==116 and len(healthy['binary64_input_matches'])==58
    tables={}
    for path in sorted((TOPIC/'c4-tables').glob('*.csv')):
        assert path.read_bytes()==(WORK/'healthy/tables'/path.name).read_bytes(),path.name
        tables[path.name]=pin(path)
    # Use the real producer's breakdown shape, with three other missing-data cases.
    native=json.loads(NATIVE.read_text())
    target=native['cases'][0]
    target.pop('C4')
    target['measurement']['C4']=dict(status='breakdown',reason='synthetic C3 breakdown')
    target.pop('A-LU')
    target['A-QR']=dict(status='completed')
    target['B-nodeqr']=dict(status='completed',coefficients=[])
    broken_native=WORK/'broken-native.json'
    broken_native.write_text(json.dumps(native))
    selected=[r for r in json.loads(EXTERNAL.read_text())
              if r['input_kind']=='shared_normalized' and r['N']==target['N'] and r['family']==target['family']]
    assert len(selected)==1
    broken_external=WORK/'single-external.json'
    broken_external.write_text(json.dumps(selected))
    broken_command,broken=run_compare(broken_external,broken_native,WORK/'broken')
    methods=broken['cases'][0]['methods']
    expected={'C4':'breakdown','A-LU':'missing','A-QR':'missing_coefficients','B-nodeqr':'invalid_coefficients'}
    for method,status in expected.items():
        assert methods[method]['status']==status
        rows=list(csv.DictReader((WORK/'broken/tables'/f"{target['family']}-{method}.csv").open()))
        assert len(rows)==1 and rows[0]['status']==status
        assert all(rows[0][k]=='' for k in ('a1','a2','b1','b2','E_NN','H_integer','lift_precision_agreement'))
    original=next(r for r in baseline['cases'] if r['family']==target['family'] and r['N']==target['N'] and r['input_kind']=='shared_normalized')
    for method in ('CORE','KRYL','REORTH'):
        assert methods[method]==original['methods'][method]
    failures=json.loads((WORK/'broken/c4-comparison-receipt.json').read_text())['failures']
    assert {r['method']:r['status'] for r in failures}==expected
    hard=TOPIC/'code/c2_hard_check.py'
    assert pin(hard)['sha256']=='452d72d73b7116068a6b7b2f7fabebdb2eb77e5e51d83ae25507173014fecb66'
    hard_command=[sys.executable,str(hard)]
    hard_result=ast.literal_eval(subprocess.check_output(hard_command,text=True))
    assert hard_result['result']=='PASS'
    assert hard_result['checks']==dict(polynomials=50,jet_coordinates=735,a_rows=1050,support_coordinates=330)
    diagnostic=TOPIC/'c1-error-comparison.json'
    previous=json.loads(diagnostic.read_text())
    c1_command=[sys.executable,str(TOPIC/'code/c1_error_diagnostic.py')]
    subprocess.run(c1_command,check=True)
    current=json.loads(diagnostic.read_text())
    assert previous['cases']==current['cases']
    assert current['input_sha256'][str(TOPIC/'c4-comparison-receipt.json')]==pin(TOPIC/'c4-comparison-receipt.json')['sha256']
    out=dict(status='PASS; finite code regression checks, not a theorem',
             source_commit='3d5b29d7aa8c1274793139d7040695035e1bda22',platform=dict(python=platform.python_version(),numpy=numpy.__version__,mpmath=mpmath.__version__,sympy=sympy.__version__),
             commands=[command,broken_command,hard_command,c1_command],
             healthy=dict(cases=116,binary64_input_matches=58,scientific_payload_unchanged=True,tables_byte_identical=len(tables),tables=tables),
             failure_path=dict(statuses=expected,csv_metrics_blank=True,external_payload_unchanged=True,failures_recorded=failures),
             c2_hard=hard_result,c1=dict(cases_unchanged=True,case_summaries=len(current['cases']),error_rows=348,receipt_pin_current=True),
             inputs=[pin(p) for p in (EXTERNAL,NATIVE,BASELINE,MATRIX,TOPIC/'c4-comparison-receipt.json')],
             code=[pin(p) for p in (Path(__file__),TOPIC/'code/c4_compare.py',hard,TOPIC/'code/c1_error_diagnostic.py')],
             outputs=[pin(p) for p in (WORK/'healthy/raw.json',WORK/'broken/raw.json',diagnostic)])
    (TOPIC/'response-code-checks.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(dict(status='PASS',output=str(TOPIC/'response-code-checks.json'))))

if __name__=='__main__':main()
