#!/usr/bin/env python3
"""Frozen degree-block runner/inventory; the unchanged producer never approves."""
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

ROOT = Path(__file__).resolve().parents[3]
TOPIC = Path(__file__).resolve().parents[1]
OUT = ROOT / 'local-output/argmax-bridge-20261105/native-37-40'
DRIVER = ROOT / 'topics/padua-argmax-effective-20261103/code/native_producer/run.py'
DEGREES = (37, 38, 39, 40)


def identity(path):
    payload = path.read_bytes()
    return dict(path=str(path.relative_to(ROOT)), bytes=len(payload),
                sha256=hashlib.sha256(payload).hexdigest())


def group_cpu(pgid):
    """Live process CPU plus reaped child CPU; no double counting live children."""
    ticks = 0
    for entry in Path('/proc').iterdir():
        if not entry.name.isdecimal():
            continue
        try:
            fields = (entry/'stat').read_text().rsplit(')', 1)[1].split()
            if int(fields[2]) == pgid:
                ticks += sum(int(fields[i]) for i in (11, 12, 13, 14))
        except (FileNotFoundError, ProcessLookupError):
            pass
    return ticks / os.sysconf('SC_CLK_TCK')


def main():
    os.chdir(ROOT)
    prereg = json.loads((OUT/'preregistered-inputs.json').read_text())
    for item in prereg['sources']:
        assert identity(ROOT/item['path']) == item, item['path']
    assert not os.environ.get('PADUA_DUMP_INITIAL'), 'bulk dump forbidden'
    receipt = dict(status='Producer inventory only; independent acceptance is separate',
                   rules_input='bda45a4c1392bea87de0841b6b23e5c35b2a694b',
                   source_revision='bda45a4c1392bea87de0841b6b23e5c35b2a694b',
                   developer='Codex delegated producer; serving model/effort metadata unexposed',
                   cwd=str(ROOT), python=sys.version, platform=platform.platform(),
                   compiler=subprocess.check_output(['gcc','--version'],text=True).splitlines()[0],
                   gmp_version=subprocess.check_output(['pkg-config','--modversion','gmp'],text=True).strip(),
                   source_identities=prereg['sources'], degrees=[],
                   limits='n37–40 only; 1700 search CPU seconds, 1800 total CPU seconds per degree; no rerun',
                   independent_replay='PENDING: separate checker owns acceptance',
                   storage='Bulk local working output only; no archival destination selected')
    for n in DEGREES:
        output = OUT/f'n{n}.json.gz'
        work = OUT/f'native{n}'
        assert not output.exists() and not work.exists(), 'No overwrites or adaptive reruns'
        argv = [sys.executable, str(DRIVER), '--n', str(n), '--seconds', '1700',
                '--boxes', '200000', '--depth', '48', '--output', str(output), '--work', str(work)]
        before = resource.getrusage(resource.RUSAGE_CHILDREN)
        started = time.monotonic()
        with (OUT/f'n{n}-stdout.txt').open('w') as stdout, (OUT/f'n{n}-stderr.txt').open('w') as stderr:
            proc = subprocess.Popen(argv, stdout=stdout, stderr=stderr, start_new_session=True)
            stopped = False
            while proc.poll() is None:
                if group_cpu(proc.pid) >= 1795:
                    os.killpg(proc.pid, signal.SIGKILL)
                    stopped = True
                    break
                time.sleep(0.25)
            returncode = proc.wait()
        after = resource.getrusage(resource.RUSAGE_CHILDREN)
        record = dict(n=n, argv=argv, returncode=returncode, cpu_watchdog_stopped=stopped,
                      elapsed_wall_seconds=time.monotonic()-started,
                      child_user_cpu_seconds=after.ru_utime-before.ru_utime,
                      child_system_cpu_seconds=after.ru_stime-before.ru_stime)
        if output.exists():
            d = json.loads(gzip.decompress(output.read_bytes()))
            record.update(certificate=identity(output), complete=d['complete'],
                          producer_accepted=d['accepted'], pending=len(d['pending']),
                          leaves=len(d['leaves']), statistics=d['statistics'],
                          seconds={k:d[k] for k in ('setup_seconds','search_seconds','total_seconds')},
                          producer_provenance=d['producer_provenance'],
                          artifacts=[identity(work/p) for p in
                                     (f'n{n}-input.txt','producer-build.c','native-producer',f'n{n}-native.txt')])
            assert d['accepted'] is False
        receipt['degrees'].append(record)
        payload = json.dumps(receipt, indent=2)+'\n'
        assert len(payload.encode()) < 16384
        (TOPIC/'evidence/native-37-40-producer.json').write_text(payload)
        print(json.dumps(record), flush=True)
        if returncode or stopped or not record.get('complete'):
            print('BLOCK FROZEN: failed/incomplete degree; no adaptive rerun', flush=True)
            break


if __name__ == '__main__':
    main()
