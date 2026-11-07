#!/usr/bin/env python3
"""Bounded rerun of the unchanged native producer, small-degree stages only."""
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import platform
import resource
import signal
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
OUT = ROOT / 'local-output/argmax-bridge-20261105/small-degree-unification'
DRIVER = ROOT / 'topics/padua-argmax-effective-20261103/code/native_producer/run.py'
STAGES = {'pilot': (2, 8), 'rest': (3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16)}


def identity(path):
    raw = path.read_bytes()
    return {'path': str(path.relative_to(ROOT)), 'bytes': len(raw),
            'sha256': hashlib.sha256(raw).hexdigest()}


def group_cpu(pgid):
    # Same process-group accounting as native_37_40.py: live CPU plus each
    # process's reaped descendants, counted only while that process is live.
    ticks = 0
    for entry in Path('/proc').iterdir():
        if not entry.name.isdecimal():
            continue
        try:
            fields = (entry / 'stat').read_text().rsplit(')', 1)[1].split()
            if int(fields[2]) == pgid:
                ticks += sum(int(fields[i]) for i in (11, 12, 13, 14))
        except (FileNotFoundError, ProcessLookupError):
            pass
    return ticks / os.sysconf('SC_CLK_TCK')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('stage', choices=STAGES)
    args = parser.parse_args()
    os.chdir(ROOT)
    frozen = json.loads((HERE / 'FREEZE.json').read_text())
    for row in frozen['sources']:
        if identity(ROOT / row['path']) != row:
            raise RuntimeError('Frozen source mismatch: ' + row['path'])
    if os.environ.get('PADUA_DUMP_INITIAL'):
        raise RuntimeError('Bulk dumps forbidden')
    if args.stage == 'rest':
        pilot = json.loads((OUT / 'pilot-receipt.json').read_text())
        if not all(r['returncode'] == 0 and r['complete'] for r in pilot['runs']):
            raise RuntimeError('Pilot did not complete')
    receipt_path = OUT / (args.stage + '-receipt.json')
    if receipt_path.exists():
        raise RuntimeError('No stage overwrite or rerun')
    OUT.mkdir(parents=True, exist_ok=True)
    receipt = {'rules_source_head': frozen['rules_source_head'],
               'freeze_sha256': identity(HERE / 'FREEZE.json')['sha256'],
               'purpose': 'Same accepted scheme at old degrees; no new degree theorem',
               'stage': args.stage, 'python': sys.version,
               'platform': platform.platform(), 'runs': []}
    for n in STAGES[args.stage]:
        output = OUT / f'n{n}.json.gz'
        work = OUT / f'native{n}'
        if output.exists() or work.exists():
            raise RuntimeError('No output overwrite or adaptive rerun')
        argv = ['prlimit', '--as=4294967296', '--fsize=1048576', '--',
                sys.executable, '-E', '-S', '-B', str(DRIVER), '--n', str(n),
                '--seconds', '100', '--boxes', '200000', '--depth', '48',
                '--output', str(output), '--work', str(work)]
        before = resource.getrusage(resource.RUSAGE_CHILDREN)
        started = time.monotonic()
        stopped = None
        with (OUT / f'n{n}-stdout.txt').open('x') as stdout, \
                (OUT / f'n{n}-stderr.txt').open('x') as stderr:
            proc = subprocess.Popen(argv, stdout=stdout, stderr=stderr,
                                    start_new_session=True)
            while proc.poll() is None:
                if group_cpu(proc.pid) >= 115:
                    stopped = 'CPU stop before120s'
                elif time.monotonic() - started >= 175:
                    stopped = 'wall stop before180s'
                if stopped:
                    os.killpg(proc.pid, signal.SIGKILL)
                    break
                time.sleep(0.1)
            returncode = proc.wait()
        after = resource.getrusage(resource.RUSAGE_CHILDREN)
        row = {'n': n, 'argv': argv, 'returncode': returncode,
               'stopped': stopped, 'wall_seconds': time.monotonic() - started,
               'child_user_cpu_seconds': after.ru_utime - before.ru_utime,
               'child_system_cpu_seconds': after.ru_stime - before.ru_stime}
        if output.exists():
            data = json.loads(gzip.decompress(output.read_bytes()))
            row.update(certificate=identity(output), complete=data['complete'],
                       producer_accepted=data['accepted'], pending=len(data['pending']),
                       statistics=data['statistics'],
                       producer_provenance=data['producer_provenance'])
        receipt['runs'].append(row)
        receipt_path.write_text(json.dumps(receipt, indent=2) + '\n')
        print(json.dumps(row), flush=True)
        if returncode or stopped or not row.get('complete') or row.get('producer_accepted') is not False:
            raise RuntimeError('Stage stopped: first failed/incomplete candidate; no rescue')


if __name__ == '__main__':
    main()
