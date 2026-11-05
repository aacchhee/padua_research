"""Bounded replay after GMP canonical-operand fix; preserves prior receipts."""
if not __debug__:
    raise RuntimeError('Scientific verification requires assertions; do not use -O.')

import hashlib
import json
from pathlib import Path
import resource
import subprocess
import sys
import time

REPO = Path(__file__).resolve().parents[4]
CHECK = REPO / 'topics/padua-argmax-effective-20261103/code/native_checker'
OUT = Path('/workspace/padua-work/independent')
EXPECTED = 'b0c871e7711219edfe3ce01480d8d1de3503a20d9b59f82b63a00eff248bc6e0'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def limits():
    resource.setrlimit(resource.RLIMIT_CORE, (0, 0))
    resource.setrlimit(resource.RLIMIT_CPU, (600, 610))
    resource.setrlimit(resource.RLIMIT_AS, (6 << 30, 6 << 30))


def main():
    n = int(sys.argv[1])
    assert n in (32, 40)
    source = CHECK/'kernel.cpp'
    assert digest(source) == EXPECTED
    binary = OUT/'checker-kernel-canonical'
    build = json.loads((OUT/'canonical-build.json').read_text())
    assert build['kernel_sha256'] == EXPECTED and build['binary_sha256'] == digest(binary)
    cert = Path(f'/workspace/padua-work/producer/final/n{n}.json.gz')
    receipt = OUT/f'canonical-check-n{n}.json'
    assert not receipt.exists(), 'preserve existing corrected receipts'
    metrics = OUT/f'canonical-check-n{n}-resources.json'
    command = [sys.executable, str(CHECK/'check.py'), str(cert), '--binary', str(binary), '--output', str(receipt)]
    begin = time.monotonic()
    before = resource.getrusage(resource.RUSAGE_CHILDREN)
    process = subprocess.run(command, text=True, capture_output=True, preexec_fn=limits, timeout=1800)
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    usage = dict(wall_seconds=time.monotonic()-begin,
                 user_cpu_seconds=after.ru_utime-before.ru_utime,
                 system_cpu_seconds=after.ru_stime-before.ru_stime,
                 max_rss_kib=after.ru_maxrss, source='getrusage(RUSAGE_CHILDREN) after one waited driver')
    metrics.write_text(json.dumps(usage, indent=2, sort_keys=True)+'\n')
    (OUT/f'canonical-check-n{n}.stdout').write_text(process.stdout)
    (OUT/f'canonical-check-n{n}.stderr').write_text(process.stderr)
    result = dict(n=n, command=command, returncode=process.returncode, elapsed_seconds=time.monotonic()-begin,
                  kernel_sha256=EXPECTED, binary_sha256=digest(binary), certificate_sha256=digest(cert),
                  cpu_limit_seconds=600, address_space_limit_bytes=6 << 30)
    assert digest(source) == EXPECTED, 'source changed during corrected replay'
    if process.returncode == 0:
        accepted = json.loads(receipt.read_text())
        assert accepted['accepted'] and accepted['certificate_sha256'] == digest(cert)
        result.update(accepted=True, counts=accepted['counts'], checker_receipt_sha256=digest(receipt),
                      resources=json.loads(metrics.read_text()))
    else:
        result.update(accepted=False, failure=process.stderr[-2000:])
    record = OUT/f'canonical-check-n{n}-run.json'
    record.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    print(json.dumps(result), flush=True)
    assert process.returncode == 0, 'corrected replay did not complete successfully'


if __name__ == '__main__':
    main()
