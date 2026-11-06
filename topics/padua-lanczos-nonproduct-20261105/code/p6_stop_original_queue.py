#!/usr/bin/env python3
"""Preserve original producer caps, then cancel queued scalar600s cases.

Coordinator authorized this prospective resource change before scalar cases
started. Only the identified disk scan process and its checker children are
stopped; completed output is preserved for the separate3600s successor.
"""
import argparse
import hashlib
import json
import os
import signal
import sys
import time
from pathlib import Path


def identity(path):
    data = Path(path).read_bytes()
    return {'path': str(path), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def processes():
    result = {}
    for proc in Path('/proc').iterdir():
        if not proc.name.isdigit():
            continue
        try:
            argv = (proc/'cmdline').read_bytes().split(b'\0')
            result[int(proc.name)] = [x.decode() for x in argv if x]
        except (OSError, UnicodeError):
            pass
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--original-receipt', type=Path, required=True)
    parser.add_argument('--work-dir', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    started = time.monotonic()
    while True:
        try:
            original = json.loads(args.original_receipt.read_text())
            producer = [r for r in original['runs'] if r['backend'] == 'producer']
        except (ValueError, OSError):
            time.sleep(.25)
            continue
        if len(producer) == 4:
            break
        assert time.monotonic()-started < 1800, 'original producer outcomes did not complete within monitoring cap'
        time.sleep(.25)
    found = []
    for pid, argv in processes().items():
        if (any(x.endswith('/p6_scan.py') for x in argv) and
                '--work-dir' in argv and argv[argv.index('--work-dir')+1] == str(args.work_dir)):
            found.append((pid, argv))
    assert len(found) <= 1
    stopped = []
    # Freeze the queue before enumerating children, then terminate it. No
    # producer is left running: all four producer outcomes were persisted.
    if found:
        pid, argv = found[0]
        os.kill(pid, signal.SIGSTOP)
        children = [(p, a) for p, a in processes().items()
                    if a and a[0] == str(args.work_dir/'checker')]
        os.kill(pid, signal.SIGKILL)
        stopped.append({'pid': pid, 'command': argv, 'action': 'killed original wrapper after all producer outcomes'})
        for child, command in children:
            try:
                os.kill(child, signal.SIGTERM)
                stopped.append({'pid': child, 'command': command, 'action': 'cancelled automatically started scalar600s case'})
            except ProcessLookupError:
                pass
    scalar = []
    for rule in ('bj', 'mirror', 'alt', 'pivot'):
        output, log = [args.work_dir/('checker-'+rule+ext) for ext in ('.jsonl', '.log')]
        attempted = output.exists() or log.exists()
        row = {'backend': 'checker', 'rule': rule,
               'status': 'CANCELLED_PARTIAL' if attempted else 'UNSTARTED_DEFERRED_TO_SUCCESSOR',
               'completed_degree_rows': []}
        if output.exists():
            row['output'] = identity(output)
            row['completed_degree_rows'] = [json.loads(x)['degree'] for x in output.read_text().splitlines()]
        if log.exists():
            row['log'] = identity(log)
            row['last_log_line'] = log.read_text().splitlines()[-1:] or []
        scalar.append(row)
    result = {'status': 'CLOSED original600s attempt; successor resource plan required',
              'reason': 'Prospective coordinator authorization to avoid predicted600s scalar timeout and use3600s directly',
              'original_receipt': identity(args.original_receipt), 'producer_outcomes': producer,
              'scalar_dispositions': scalar, 'stopped_processes': stopped,
              'monitor_seconds': time.monotonic()-started, 'code': identity(__file__),
              'command': [sys.executable, '-B', *sys.argv]}
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': result['status'], 'scalar_dispositions': scalar}), flush=True)


if __name__ == '__main__':
    main()
