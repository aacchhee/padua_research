#!/usr/bin/env python3
"""Inventory frozen exact producer outputs; never self-approve certificates."""
import gzip
import hashlib
import json
from pathlib import Path
import platform
import subprocess

ROOT = Path(__file__).resolve().parents[3]
TOPIC = Path(__file__).resolve().parents[1]
OUT = ROOT/'local-output/argmax-bridge-20261105/N3'
NATIVE = ROOT/'topics/padua-argmax-effective-20261103/code/native_producer'

def identity(path):
    data = path.read_bytes()
    return {'path': str(path.relative_to(ROOT)), 'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest()}

def main():
    records = []
    for path in sorted(OUT.glob('n*.json.gz')):
        d = json.loads(gzip.decompress(path.read_bytes()))
        n = d['n']
        work = OUT/f'native{n}'
        records.append({
            'n': n, 'certificate': identity(path),
            'complete': d['complete'], 'producer_accepted': d['accepted'],
            'independent_replay': 'PENDING (separate agent owns acceptance)',
            'statistics': d['statistics'], 'pending': len(d['pending']),
            'leaves': len(d['leaves']),
            'seconds': {k: d[k] for k in ['setup_seconds','search_seconds','total_seconds']},
            'provenance': d['producer_provenance'],
            'inputs': [identity(work/f'n{n}-input.txt'), identity(work/'producer-build.c'),
                       identity(work/'native-producer')],
            'command': f'python topics/padua-argmax-effective-20261103/code/native_producer/run.py --n {n} --seconds 900 --output local-output/argmax-bridge-20261105/N3/n{n}.json.gz --work local-output/argmax-bridge-20261105/N3/native{n}',
        })
    receipt = {
        'status': 'Exact producer inventory only; no developer self-approval',
        'rules_input': '98d6c00d8a474cf97602c9cfdea631a837191ac0',
        'source_revision': '98d6c00d8a474cf97602c9cfdea631a837191ac0 (producer sources unmodified)',
        'developer': 'Codex; requested Sol medium; serving metadata not exposed',
        'python': platform.python_version(), 'platform': platform.platform(),
        'compiler': subprocess.check_output(['gcc','--version'],text=True).splitlines()[0],
        'gmp_version': subprocess.check_output(['pkg-config','--modversion','gmp'],text=True).strip(),
        'sources': [identity(NATIVE/'producer.c'),identity(NATIVE/'run.py'),identity(Path(__file__).resolve())],
        'degrees': records,
        'limits': ['PD-T210 unchanged; complete producer output is not checker acceptance.',
                   'Generated raw artifacts retained locally; archival transfer pending.',
                   'No larger degree or all-degree statement follows from this inventory.']}
    text = json.dumps(receipt,indent=2)+'\n'
    assert len(text.encode()) < 16384
    (TOPIC/'evidence/n3-native-producer.json').write_text(text)
    print(json.dumps({'degrees':[x['n'] for x in records],'bytes':len(text.encode())}))

if __name__ == '__main__':
    main()
