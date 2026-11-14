#!/usr/bin/env python3
"""Collect existing bounded outward calibration outputs without rerunning."""
import json
from pathlib import Path
from n3_native_receipt import identity

ROOT=Path(__file__).resolve().parents[3]
TOPIC=Path(__file__).resolve().parents[1]
OUT=ROOT/'local-output/argmax-bridge-20261105/N3'

def main():
    runs=[]
    for n in [17,24,32]:
        path=OUT/f'outward-calibration-v1/n{n}-phase.json';data=json.loads(path.read_text())
        assert data['complete'] is False and data['accepted'] is False
        runs.append({'n':n,'complete':False,'accepted':False,'statistics':data['statistics'],
                     'pending':len(data['pending']),'leaves':len(data['leaves']),'output':identity(path)})
    canceled_dir=OUT/'float-v3'
    canceled={'status':'Terminated by coordinator instruction before any completed degree; no result used',
              'command':'OPENBLAS_NUM_THREADS=1 python topics/padua-argmax-bridge-20261105/code/n3_float_v3.py --degrees 33 64 128 --seconds 600 --corner-replay topics/padua-argmax-bridge-20261105/evidence/independent-corner-replay.json',
              'reason':'Duplicate campaign solely for premise metadata was unnecessary; separate input-impact check used.',
              'raw':[identity(p) for p in sorted(canceled_dir.glob('*.json*'))],
              'completed_degrees':[]}
    data={'status':'MEASURED bounded outward calibration; no complete phase cover or independent acceptance',
          'command':'python topics/padua-argmax-bridge-20261105/code/n3_outward_run.py --degrees 17 24 32 --seconds 30 --boxes 32 --work local-output/argmax-bridge-20261105/N3/outward-calibration-v1 --execute',
          'collector_command':'python topics/padua-argmax-bridge-20261105/code/n3_outward_receipt.py',
          'collector_source':identity(Path(__file__).resolve()),'runs':runs,
          'sample_leaf_receipt':identity(TOPIC/'evidence/n3-phase-samples.json'),
          'canceled_duplicate':canceled,
          'notes':['First outward invocation failed before mathematical execution because a relative work path could not be recorded relative to repository root; driver now resolves work path.',
                   'Each calibration has only one outside leaf; narrow far/defect/local leaves are separate explicit partial prefix trees.',
                   'Every calibration preserves pending paths and producer accepted=false; independent phase checker owns acceptance.']}
    text=json.dumps(data,indent=2)+'\n';assert len(text.encode())<16384
    (TOPIC/'evidence/n3-outward-bounded.json').write_text(text)
    print(json.dumps({'degrees':[r['n'] for r in runs],'cpu_seconds':[r['statistics']['cpu_seconds'] for r in runs],'bytes':len(text)}))

if __name__=='__main__':main()
