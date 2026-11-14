#!/usr/bin/env python3
"""Compile one frozen checker; strict retained-input replay at degrees 2 and 17."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import resource
import shutil
import signal
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
TOPIC = ROOT / 'topics/padua-argmax-bridge-20261105'
SMALL = TOPIC / 'code/small_degree_unification'
OUTPUT = ROOT / 'local-output/argmax-bridge-20261105/polynomial-regeneration-20261114'

def need(value, message):
    if not value:
        raise RuntimeError(message)

def identity(path):
    path = Path(path)
    return {'path': str(path), 'bytes': path.stat().st_size,
            'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}

def save(path, value):
    with Path(path).open('x') as stream:
        json.dump(value, stream, indent=2, sort_keys=True)
        stream.write('\n')

def check_inputs(freeze):
    for row in freeze['inputs']:
        actual = identity(ROOT / row['path'])
        need(actual['bytes'] == row['bytes'] and actual['sha256'] == row['sha256'],
             'changed input: ' + row['path'])

def interrupted(number, frame):
    raise RuntimeError('supervisor signal ' + str(number))

def run_stage(base, label, command, cpu, wall):
    """Record direct owned wait4 status; kill whole isolated group on timeout/error."""
    need(signal.getsignal(signal.SIGCHLD) == signal.SIG_DFL, 'nondefault SIGCHLD')
    started = time.monotonic()
    observation = {'label': label, 'command': command, 'CPU_limit_per_process': cpu,
                   'wall_limit_seconds': wall, 'cleanup': False}
    def limits():
        resource.setrlimit(resource.RLIMIT_CPU, (cpu, cpu))
        resource.setrlimit(resource.RLIMIT_AS, (2 * 1024**3, 2 * 1024**3))
        resource.setrlimit(resource.RLIMIT_CORE, (0, 0))
        os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
    proc = None
    status = None
    problem = None
    with (base / (label + '.stdout')).open('x') as stdout, (base / (label + '.stderr')).open('x') as stderr:
        try:
            proc = subprocess.Popen(command, cwd=ROOT, stdout=stdout, stderr=stderr,
                                    start_new_session=True, preexec_fn=limits,
                                    env={'PATH': os.environ['PATH'], 'LC_ALL': 'C',
                                         'OPENBLAS_NUM_THREADS': '1', 'OMP_NUM_THREADS': '1'})
            observation['pid'] = proc.pid
            while True:
                pid, status, usage = os.wait4(proc.pid, os.WNOHANG)
                if pid:
                    need(pid == proc.pid, 'wrong owned child')
                    break
                status = None
                need(time.monotonic() - started <= wall, 'wall cap')
                time.sleep(.05)
        except BaseException as error:
            problem = repr(error)
        finally:
            if proc is not None and status is None:
                observation['cleanup'] = True
                # Kill the entire owned group, including compiler/native descendants.
                try:
                    os.killpg(proc.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
                try:
                    pid, status, usage = os.wait4(proc.pid, 0)
                    need(pid == proc.pid, 'wrong cleanup child')
                except ChildProcessError as error:
                    problem = (problem or '') + '; missing actual child status: ' + repr(error)
            if proc is not None:
                proc.returncode = os.waitstatus_to_exitcode(status) if status is not None else 255
            observation.update(wall_seconds=time.monotonic()-started, problem=problem)
            if status is not None:
                observation.update(wait_status=status, returncode=os.waitstatus_to_exitcode(status),
                                   CPU_seconds=usage.ru_utime+usage.ru_stime,
                                   maximum_RSS_KiB=usage.ru_maxrss)
            save(base / (label + '.observation.json'), observation)
    need(not problem and not observation['cleanup'] and observation.get('returncode') == 0,
         label + ' did not complete cleanly')
    return observation

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--execute', action='store_true', help='only after committed preregistration and reviewer clearance')
    args = parser.parse_args()
    need(args.execute, 'execution requires explicit --execute')
    need(signal.getsignal(signal.SIGCHLD) == signal.SIG_DFL, 'nondefault SIGCHLD at startup')
    for number in (signal.SIGTERM, signal.SIGHUP, signal.SIGINT):
        signal.signal(number, interrupted)
    freeze = json.loads((HERE / 'frozen-inputs.json').read_text())
    check_inputs(freeze)
    OUTPUT.mkdir(parents=True, exist_ok=False)
    observations = []
    tool_paths = [Path(sys.executable).resolve()]
    for tool in ('g++', 'as', 'ld', 'ldd'):
        path = shutil.which(tool)
        need(path is not None, 'missing ' + tool)
        tool_paths.append(Path(path).resolve())
    tool_paths += list(Path('/usr/lib/gcc').glob('*/*/cc1plus'))
    tool_paths += [Path('/usr/include/gmpxx.h'), Path('/usr/include/x86_64-linux-gnu/gmp.h')]
    save(OUTPUT / 'environment.json', {'python': sys.version, 'platform': platform.platform(),
         'tools_and_GMP_headers': [identity(p) for p in tool_paths],
         'input_freeze': identity(HERE / 'frozen-inputs.json'),
         'historical_binary_recovered': False, 'new_build': True})
    binary = OUTPUT / 'kernel'
    compiler = str(Path(shutil.which('g++')).resolve())
    observations.append(run_stage(OUTPUT, 'compile', [compiler, '-v', '-O3', '-std=c++17',
        str(SMALL / 'metadata_kernel.cpp'), '-lgmpxx', '-lgmp', '-o', str(binary)], 60, 300))
    binary_identity = identity(binary)
    observations.append(run_stage(OUTPUT, 'linked-libraries', [str(Path(shutil.which('ldd')).resolve()), str(binary)], 5, 30))
    dependencies = sorted(set(re.findall(r'(/[^\s()]+)', (OUTPUT / 'linked-libraries.stdout').read_text())))
    need(dependencies and all(Path(p).is_file() for p in dependencies), 'unresolved linked library')
    save(OUTPUT / 'runtime-closure.json', {'binary': binary_identity,
         'libraries': [identity(p) for p in dependencies]})
    receipts = []
    index = json.loads((SMALL / 'common-witness-index.json').read_text())
    for n, cpu, wall in [(2, 15, 120), (17, 60, 300)]:
        check_inputs(freeze)
        need(identity(binary) == binary_identity, 'binary changed')
        certificate = ROOT / freeze['certificates'][str(n)]
        receipt = OUTPUT / ('n' + str(n) + '-check.json')
        observations.append(run_stage(OUTPUT, 'n' + str(n), [sys.executable, '-E', '-S', '-B',
            str(SMALL / 'check.py'), str(certificate), '--binary', str(binary), '--output', str(receipt)], cpu, wall))
        result = json.loads(receipt.read_text())
        row = next(row for row in index['rows'] if row[0] == n)
        need(result['n'] == n and all(result[k] is True for k in
             ['accepted', 'complete_partition', 'all_supplied_bounds_verified']), 'nonacceptance')
        need(result['counts']['bound'] == row[3] and result['counts']['corner'] == 2,
             'unexpected leaf counts')
        need(result['binary_sha256'] == binary_identity['sha256'] and
             result['certificate_sha256'] == identity(certificate)['sha256'], 'receipt identities')
        receipts.append(identity(receipt))
    check_inputs(freeze)
    need(identity(binary) == binary_identity, 'final binary changed')
    save(OUTPUT / 'summary.json', {'scope': 'fresh checker build and targeted strict retained-input replay',
         'replayed_degrees': [2, 17], 'full_39_replay': False, 'historical_binary_recovered': False,
         'binary': binary_identity, 'receipts': receipts, 'observations': observations,
         'input_inventory_checked': 39, 'all_frozen_inputs_unchanged': True})
    print('New checker built; strict n2 and n17 accepted. Full 39-degree replay not performed.', flush=True)

if __name__ == '__main__':
    main()
