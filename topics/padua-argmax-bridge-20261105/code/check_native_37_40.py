"""Separate-process bounded replay of the frozen native checker, degrees 37–40.

No producer module is imported. Run --build once, then one --degree per process.
"""
import argparse
import datetime
import gzip
import hashlib
import json
from pathlib import Path
import platform
import resource
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / 'topics/padua-argmax-bridge-20261105'
LOCAL = ROOT / 'local-output/argmax-bridge-20261105/check-native-37-40'
SOURCE = ROOT / 'topics/padua-argmax-effective-20261103/code/native_checker'
HEAD = 'bda45a4c1392bea87de0841b6b23e5c35b2a694b'
PINS = {'check.py': 'b6c7320db2f7cfebf27fe33aa38ffdd45ff719870e3d23e15f845b6e8026eb2e',
        'kernel.cpp': 'b0c871e7711219edfe3ce01480d8d1de3503a20d9b59f82b63a00eff248bc6e0'}


def need(ok, message):
    if not ok:
        raise RuntimeError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pinned():
    for name, expected in PINS.items():
        need(sha(SOURCE / name) == expected, 'changed checker source: ' + name)
        historical = subprocess.check_output(['git', 'show', f'{HEAD}:{(SOURCE / name).relative_to(ROOT)}'], cwd=ROOT)
        need(hashlib.sha256(historical).hexdigest() == expected, 'input commit source mismatch')


def write(path, value):
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + '\n')


def timed(argv, stem, limit=False):
    def cpu_limit():
        # Inherited by the driver and native child; reserve headroom below 1800.
        resource.setrlimit(resource.RLIMIT_CPU, (1790, 1790))
    before = resource.getrusage(resource.RUSAGE_CHILDREN)
    started = time.monotonic()
    utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with (LOCAL / (stem + '.stdout')).open('w') as out, (LOCAL / (stem + '.stderr')).open('w') as err:
        proc = subprocess.run(argv, cwd=ROOT, stdout=out, stderr=err,
                              preexec_fn=cpu_limit if limit else None)
    wall = time.monotonic() - started
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    return dict(argv=argv, cwd=str(ROOT), started_utc=utc, exit_status=proc.returncode,
                wall_seconds=wall, child_user_seconds=after.ru_utime-before.ru_utime,
                child_system_seconds=after.ru_stime-before.ru_stime,
                cpu_seconds=(after.ru_utime-before.ru_utime)+(after.ru_stime-before.ru_stime))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument('--build', action='store_true')
    action.add_argument('--degree', type=int, choices=range(37, 41))
    args = parser.parse_args()
    LOCAL.mkdir(parents=True, exist_ok=True)
    pinned()
    binary = LOCAL / 'kernel'
    if args.build:
        need(not binary.exists(), 'fresh binary destination required')
        result = timed(['g++', '-O3', '-std=c++17', str(SOURCE / 'kernel.cpp'),
                        '-lgmpxx', '-lgmp', '-o', str(binary)], 'compile')
        need(result['exit_status'] == 0, 'compile failed')
        pinned()
        result.update(binary_sha256=sha(binary), source_sha256=PINS, input_head=HEAD,
                      python=platform.python_version(), compiler=subprocess.check_output(['g++', '--version'], text=True).splitlines()[0],
                      gmp_package=subprocess.check_output(['dpkg-query', '-W', '-f=${Version}', 'libgmp-dev'], text=True))
        write(LOCAL / 'build.json', result)
        print(json.dumps(result, sort_keys=True))
        return
    n = args.degree
    build = json.loads((LOCAL / 'build.json').read_text())
    need(sha(binary) == build['binary_sha256'], 'binary changed since fresh build')
    cert = ROOT / f'local-output/argmax-bridge-20261105/native-37-40/n{n}.json.gz'
    identity = sha(cert)
    data = json.loads(gzip.decompress(cert.read_bytes()))
    need(data['n'] == n and data['accepted'] is False and data['complete'] is True and data['pending'] == [], 'candidate is not complete/non-approved')
    raw = LOCAL / f'replay-n{n}.json'
    receipt = TOPIC / f'evidence/independent-n{n}.json'
    need(not raw.exists() and not receipt.exists(), 'refuse to overwrite completed replay')
    argv = [sys.executable, str(SOURCE / 'check.py'), str(cert), '--binary', str(binary), '--output', str(raw)]
    execution = timed(argv, f'n{n}', limit=True)
    write(LOCAL / f'execution-n{n}.json', execution)
    need(execution['exit_status'] == 0, 'checker failed; preserved execution and stderr')
    need(execution['cpu_seconds'] < 1800, 'CPU allowance exceeded')
    pinned()
    need(sha(cert) == identity and sha(binary) == build['binary_sha256'], 'input/binary changed during replay')
    result = json.loads(raw.read_text())
    for key in ('accepted', 'complete_partition', 'all_supplied_bounds_verified'):
        need(result[key] is True, 'incomplete verdict: ' + key)
    need(result['n'] == n and result['certificate_sha256'] == identity, 'receipt input identity')
    need(result['checker_sha256'] == PINS['check.py'] and result['kernel_sha256'] == PINS['kernel.cpp']
         and result['binary_sha256'] == build['binary_sha256'], 'receipt checker identity')
    result.update(execution=execution, input_head=HEAD, certificate_bytes=cert.stat().st_size,
                  producer_accepted=False, source_hashes_checked_before_and_after=True,
                  runner_sha256=sha(Path(__file__)), cpu_limit_per_process_seconds=1790,
                  cpu_accounting='RUSAGE_CHILDREN user+system delta for driver and its waited-for native child',
                  independent_execution=True, no_arithmetic_cache=True,
                  native_exit_status=0, native_exit_status_basis='unchanged driver subprocess.run(check=True) completed',
                  build=build, raw_receipt_sha256=sha(raw))
    write(receipt, result)
    print(json.dumps({'n': n, 'accepted': True, 'counts': result['counts'], 'execution': execution, 'receipt': str(receipt)}, sort_keys=True))


if __name__ == '__main__':
    main()
