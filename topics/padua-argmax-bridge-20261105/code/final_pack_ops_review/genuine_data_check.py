"""DATA_ONLY_NO_NATIVE: four fixed saved passes, no child/compiler/network/oracle."""
import hashlib
import importlib
import json
from pathlib import Path
import resource
import signal
import sys
import time
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
TOPIC = 'topics/padua-argmax-bridge-20261105/'
ENGINE = TOPIC + 'code/final_hybrid_engine'
OPS = TOPIC + 'syvert2_pack'
BASE = 'local-output/argmax-bridge-20261105/final-hybrid-validation/'
BOX = ROOT / 'local-output/argmax-bridge-20261105/final-ops-genuine-data-01'

def digest(data): return hashlib.sha256(data).hexdigest()
def main():
    resource.setrlimit(resource.RLIMIT_AS, (1024**3, 1024**3))
    resource.setrlimit(resource.RLIMIT_CPU, (20, 20))
    signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('60s data-only cap')))
    signal.alarm(60); started = time.monotonic()
    pins = json.loads((HERE / 'genuine_data_pins.json').read_bytes())
    for name, expected in pins.items():
        if digest((ROOT / name).read_bytes()) != expected: raise ValueError('registered input changed: ' + name)
    BOX.mkdir(parents=True, exist_ok=False)
    source = BOX / ENGINE / 'checker.py'; source.parent.mkdir(parents=True)
    source.write_bytes((ROOT / ENGINE / 'checker.py').read_bytes())
    sys.path.insert(0, str(ROOT / OPS))
    evidence = importlib.import_module('evidence')
    def read_bytes(name):
        evidence.safe(name)
        return ((BOX if name.startswith('preserved-sha256/') else ROOT) / name).read_bytes()
    access = evidence.Access(BOX, str(ROOT), read_bytes=read_bytes, capture=True)
    freeze = json.loads((ROOT / ENGINE / 'FREEZE.json').read_bytes())
    manifest = {'files': {r['path']: {'bytes': r['bytes'], 'sha256': r['sha256']} for r in freeze['code_data']}}
    results = []; failure = None
    try:
        for suffix, n, mode in [('primary-n41', 41, 'produce'), ('verify-n41', 41, 'verify'),
                                ('primary-n511', 511, 'produce'), ('verify-n511', 511, 'verify')]:
            receipt = evidence.validate_pass(access, BASE + suffix, n, mode, manifest)
            results.append({'input': BASE + suffix, 'n': n, 'mode': mode, 'receipt_sha256': digest(receipt)})
        for name, expected in pins.items():
            if digest((ROOT / name).read_bytes()) != expected: raise ValueError('registered input changed during checking: ' + name)
    except BaseException as error: failure = repr(error); raise
    finally:
        signal.alarm(0)
        total = sum(p.stat().st_size for p in BOX.rglob('*') if p.is_file())
        record = {'scope': 'DATA_ONLY_NO_NATIVE', 'results': results, 'failure': failure,
                  'wall_seconds': time.monotonic() - started, 'self_cpu': resource.getrusage(resource.RUSAGE_SELF).ru_utime + resource.getrusage(resource.RUSAGE_SELF).ru_stime,
                  'captured_bytes_before_receipt': total, 'reservation_bytes': 256 * 1024**2,
                  'reservation_scope': 'prospective staging reservation with post-check, not aggregate hard quota',
                  'original_inputs': pins}
        (BOX / 'receipt.json').write_text(json.dumps(record, indent=2) + '\n')
        if total > 256 * 1024**2: raise RuntimeError('data-only staging reservation exceeded')
    print('FOUR_SAVED_PASSES_DATA_ONLY_NO_NATIVE', flush=True)
if __name__ == '__main__': main()
