#!/usr/bin/env python3
"""Record cancellation of selected native cases after reviewed method supersession."""
import argparse
import hashlib
import json
import os
import signal
import sys
import time
from pathlib import Path


def identity(path):
    data = path.read_bytes()
    return {'path': str(path), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--work-dir', type=Path, required=True)
    parser.add_argument('--rules', nargs='+', choices=('bj', 'mirror', 'alt', 'pivot'), required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    records = []
    for proc in Path('/proc').iterdir():
        if not proc.name.isdigit():
            continue
        try:
            argv = [x.decode() for x in (proc/'cmdline').read_bytes().split(b'\0') if x]
            if len(argv) != 5 or argv[0] != str(args.work_dir/'checker') or argv[3] not in args.rules:
                continue
            stat = (proc/'stat').read_text().split()
            ticks = os.sysconf('SC_CLK_TCK')
            elapsed = float(Path('/proc/uptime').read_text().split()[0])-int(stat[21])/ticks
            cpu = (int(stat[13])+int(stat[14]))/ticks
            os.kill(int(proc.name), signal.SIGTERM)
            records.append({'pid': int(proc.name), 'rule': argv[3], 'command': argv,
                            'observed_wall_seconds': elapsed, 'observed_cpu_seconds': cpu,
                            'status': 'CANCELLED_PARTIAL for reviewed method supersession'})
        except (OSError, ProcessLookupError):
            continue
    time.sleep(.1)
    for row in records:
        output = args.work_dir/('checker-'+row['rule']+'.jsonl')
        log = output.with_suffix('.log')
        row.update(output=identity(output), log=identity(log),
                   completed_degrees=[json.loads(x)['degree'] for x in output.read_text().splitlines()],
                   last_log_lines=log.read_text().splitlines()[-3:])
    result = {'status': 'Recorded actual selected-case cancellations; not a scientific failure',
              'reason': 'Coordinator authorized alt/pivot cancellation only after exact reflection proof, pilots and distinct code review accepted; full-node model and source set unchanged',
              'records': records, 'requested_rules': args.rules, 'code': identity(Path(__file__)),
              'command': [sys.executable, '-B', *sys.argv]}
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
