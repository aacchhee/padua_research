"""Supplementary final-native replay with per-file source and output identity."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

REPO = Path(__file__).resolve().parents[4]
CHECK = REPO / 'topics/padua-argmax-effective-20261103/code/native_checker'
OUT = Path('/workspace/padua-work/independent')
BINARY = OUT / 'checker-kernel-final'


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    pins = {str(p): digest(p) for p in (CHECK/'check.py', CHECK/'kernel.cpp', BINARY)}
    records = []
    for name in sys.argv[1:]:
        cert = Path(name).resolve()
        receipt = OUT / ('native-final-check-' + cert.parent.name + '-' + cert.name.replace('.gz', ''))
        before = time.monotonic()
        argv = [sys.executable, str(CHECK/'check.py'), str(cert), '--binary', str(BINARY), '--output', str(receipt)]
        result = subprocess.run(argv, capture_output=True, text=True, timeout=600)
        if result.returncode:
            raise RuntimeError(result.stderr)
        data = json.loads(receipt.read_text())
        assert data['accepted']
        assert pins == {p: digest(Path(p)) for p in pins}, 'sources changed during replay'
        records.append({'certificate': str(cert), 'certificate_sha256': digest(cert),
                        'receipt': str(receipt), 'receipt_sha256': digest(receipt),
                        'n': data['n'], 'seconds': data['seconds'], 'counts': data['counts'],
                        'command': argv, 'wall_seconds': time.monotonic()-before})
        print(json.dumps(records[-1]), flush=True)
    output = OUT / ('native-final-batch-' + str(time.time_ns()) + '.json')
    output.write_text(json.dumps({'pins': pins, 'records': records}, indent=2)+'\n')
    print(str(output), flush=True)


if __name__ == '__main__':
    main()
