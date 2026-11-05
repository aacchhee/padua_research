"""Bounded, fresh native producer/checker replay; no Git operations.

Run from any directory. All generated bulk output goes below --work.
Only --summary is intended as a small committed evidence artifact.
"""
import argparse
import datetime
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

REPO = Path(__file__).resolve().parents[3]
PHASE1 = REPO / 'topics/padua-argmax-effective-20261103'
PHASE2 = REPO / 'topics/padua-argmax-effective-2-20261105'
OMIT = {'setup_seconds', 'search_seconds', 'total_seconds', 'producer_provenance'}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical(data):
    return json.dumps(data, sort_keys=True, separators=(',', ':')).encode()


def load(path):
    return json.loads(gzip.decompress(path.read_bytes()))


def run(command, name, work, records):
    if globals().get('REUSE_NATIVE', False) and name != 'pilot-n32':
        assert (work / (name + '.stdout')).exists()
        assert (work / (name + '.stderr')).exists()
        records.append(dict(name=name, command=command, returncode=0, resumed_native_from_prior_execution=True, timing='not retained after preflight failure; checker own seconds retained in acceptance receipts'))
        return
    before = resource.getrusage(resource.RUSAGE_CHILDREN)
    started = time.monotonic()
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', OPENBLAS_NUM_THREADS='1', PYTHONPATH=str(PHASE2 / 'code'))
    with (work / (name + '.stdout')).open('w') as out, (work / (name + '.stderr')).open('w') as err:
        proc = subprocess.Popen(command, cwd=REPO, env=env, stdout=out, stderr=err, start_new_session=True)
        try:
            status = proc.wait(timeout=900)
        except subprocess.TimeoutExpired:
            os.killpg(proc.pid, signal.SIGKILL)
            proc.wait()
            raise RuntimeError('900-second process-group cap: ' + name)
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    records.append(dict(name=name, command=command, returncode=status,
                        wall_seconds=time.monotonic()-started,
                        user_seconds=after.ru_utime-before.ru_utime,
                        system_seconds=after.ru_stime-before.ru_stime))
    if status:
        raise RuntimeError('failed command: ' + name)


def replay_pilot(work, records, frozen_inputs=None):
    """Run unchanged predicates/validation/queue at n32; relocate every write.

    Literal replacements are asserted so inherited driver drift fails closed.
    The adapted source is retained in bulk output, separately hashed.
    """
    previous = json.loads((PHASE2 / 'evidence/box-pilot.json').read_text())
    for item in previous['sources']:
        assert sha(REPO / item['path']) == item['sha256'], item['path']
    input_rows = []
    for item in previous['mathematical_inputs']:
        pinned = (frozen_inputs / item['path']) if frozen_inputs else (REPO / item['path'])
        assert sha(pinned) == item['sha256'], str(pinned)
        input_rows.append(dict(path=item['path'], historical_sha256=item['sha256'], current_sha256=sha(REPO / item['path'])))
    original = PHASE2 / 'code/box_pilot.py'
    source = original.read_text()
    replacements = {
        "OUT=ROOT/'local-output/argmax-effective-2-20261105/phase-probe'": "OUT=Path(" + repr(str(work / 'pilot')) + ")",
        'for n in [17,32,64,128,256]:': 'for n in [32]:',
        "dest=TOPIC/'evidence/box-pilot.json'": "dest=OUT/'box-pilot.json'",
    }
    for old, new in replacements.items():
        assert source.count(old) == 1, old
        source = source.replace(old, new)
    source = '__file__ = ' + repr(str(original)) + '\n' + source
    adapted = work / 'pilot_n32.py'
    adapted.write_text(source)
    run([sys.executable, str(adapted)], 'pilot-n32', work, records)
    receipt = work / 'pilot/box-pilot.json'
    current = json.loads(receipt.read_text())
    new = current['degrees'][0]
    old = next(r for r in previous['degrees'] if r['n'] == 32)
    omit = {'wall_seconds', 'cpu_seconds'}
    deterministic_equal = {k:v for k,v in new.items() if k not in omit} == {k:v for k,v in old.items() if k not in omit}
    assert deterministic_equal, (new, old)
    assert new['visited'] == 2000 and current['validation'] == previous['validation']
    return dict(result=new, deterministic_fields_equal=True,
                ignored_fields=sorted(omit), validation=current['validation'],
                receipt_sha256=sha(receipt), adapted_driver_sha256=sha(adapted),
                raw=current['raw'], source_pins_verified=True, mathematical_input_pins=input_rows,
                comparison_scope='All committed n32 degree fields except CPU/wall timing; validation fields equal. Committed frontier bulk is not available, so frontier count/width fields compared; new ordered frontier retained locally.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--work', type=Path, required=True)
    parser.add_argument('--summary', type=Path, required=True)
    parser.add_argument('--reuse-native', action='store_true', help='Resume after a pilot preflight stop; revalidate existing native outputs without rerunning.')
    parser.add_argument('--frozen-inputs', type=Path, help='Frozen historical pilot input tree matching committed receipt pins.')
    args = parser.parse_args()
    work = args.work.resolve()
    work.mkdir(parents=True, exist_ok=args.reuse_native)
    binary = work / 'checker'
    records = []
    global REUSE_NATIVE
    REUSE_NATIVE = args.reuse_native
    sources = [Path(__file__).resolve()]
    sources += sorted((PHASE1 / 'code/native_producer').glob('*.py'))
    sources += [PHASE1 / 'code/native_producer/producer.c', PHASE1 / 'code/native_checker/check.py', PHASE1 / 'code/native_checker/kernel.cpp']
    sources += sorted((REPO / 'topics/padua-argmax-alln-20261101/code/part3').glob('finite*.py'))
    versions = {name: subprocess.check_output(cmd, text=True).splitlines()[0]
                for name, cmd in {'gcc': ['gcc', '--version'], 'g++': ['g++', '--version'],
                                  'gmp': ['pkg-config', '--modversion', 'gmp'],
                                  'gmpxx': ['pkg-config', '--modversion', 'gmpxx']}.items()}
    versions.update(python=sys.version, platform=platform.platform(),
                    cpu=next((line.split(':',1)[1].strip() for line in Path('/proc/cpuinfo').read_text().splitlines() if line.startswith('model name')), 'unavailable'))
    run(['g++', '-O3', '-std=c++17', str(PHASE1 / 'code/native_checker/kernel.cpp'), '-lgmpxx', '-lgmp', '-o', str(binary)], 'build-checker', work, records)
    rows = []
    producer_summary = json.loads((PHASE1 / 'evidence/native-producer-summary.json').read_text())
    checker_summary = json.loads((PHASE1 / 'evidence/native-checker-summary.json').read_text())
    for n in (24,):
        certificate = work / f'n{n}.json.gz'
        committed = PHASE1 / f'evidence/n{n}.json.gz'
        run([sys.executable, str(PHASE1 / 'code/native_producer/run.py'), '--n', str(n), '--output', str(certificate), '--work', str(work / f'build-n{n}')], f'produce-n{n}', work, records)
        accepted = {}
        for label, path in [('regenerated', certificate), ('committed', committed)]:
            receipt = work / f'n{n}-{label}-check.json'
            run([sys.executable, str(PHASE1 / 'code/native_checker/check.py'), str(path), '--binary', str(binary), '--output', str(receipt)], f'check-n{n}-{label}', work, records)
            accepted[label] = dict(receipt_sha256=sha(receipt), **json.loads(receipt.read_text()))
        new, old = load(certificate), load(committed)
        mathematical = {k: v for k, v in new.items() if k not in OMIT}
        previous = {k: v for k, v in old.items() if k not in OMIT}
        previous_producer = next(r for r in producer_summary['rows'] if r['n'] == n)
        previous_checker = next(r for r in checker_summary['final_rows'] if r[0] == n)
        math_sha = hashlib.sha256(canonical(mathematical)).hexdigest()
        row = dict(n=n, regenerated_certificate_sha256=sha(certificate), committed_certificate_sha256=sha(committed),
                   regenerated_input_sha256=new['producer_provenance']['input_sha256'],
                   producer_binary_sha256=new['producer_provenance']['binary_sha256'],
                   leaves=len(new['leaves']), statistics=new['statistics'], threshold_interval=new['threshold_interval'],
                   complete=new['complete'], mathematical_sha256=math_sha,
                   mathematical_fields_equal=mathematical == previous,
                   frontier_and_bounds_equal=new['leaves'] == old['leaves'],
                   previous_producer_math_hash_matches=math_sha == previous_producer['mathematical_sha256'],
                   previous_receipt_certificate_hash_matches=sha(committed) == previous_checker[1] == previous_producer['certificate_sha256'],
                   accepted=accepted)
        if not all(row[k] for k in ('complete', 'mathematical_fields_equal', 'frontier_and_bounds_equal', 'previous_producer_math_hash_matches', 'previous_receipt_certificate_hash_matches')) or not all(r['accepted'] for r in accepted.values()):
            raise RuntimeError('comparison/acceptance failed')
        rows.append(row)
    pilot = replay_pilot(work, records, args.frozen_inputs)
    sources += [PHASE2 / 'code' / name for name in ('box_pilot.py', 'box_pilot.c', 'phase_probe.py', 'phase_probe.c')]
    sources += [PHASE2 / 'evidence/box-pilot.json', PHASE1 / 'evidence/native-producer-summary.json', PHASE1 / 'evidence/native-checker-summary.json', PHASE1 / 'evidence/n24.json.gz']
    summary = dict(pilot=pilot, format='padua-bridge-b0-replay-v1', status='MEASURED independent bounded replay',
                   input_head='274630887938c573a041cacb306d59c6c0cb2e18',
                   identity='Codex independent replay subagent; requested gpt-6.1-sol medium; runtime model metadata unavailable',
                   utc=datetime.datetime.now(datetime.timezone.utc).isoformat(), versions=versions,
                   source_sha256={str(p.relative_to(REPO)): sha(p) for p in sources},
                   checker_binary_sha256=sha(binary), commands=records, rows=rows,
                   excluded_comparison_fields=sorted(OMIT), process_group_wall_cap_seconds=900,
                   limitations=['Only native n=24 and floating pilot n=32; no new scientific claim.',
                                'No fresh corruption-control or reference-Python replay; uses frozen independent C++ checker.',
                                'Bulk outputs local and pending archival; no historical environment inferred from current versions.'])
    args.summary.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(summary, indent=2, sort_keys=True)+'\n'
    assert len(payload.encode()) < 16384
    args.summary.write_text(payload)
    print(json.dumps(dict(summary=str(args.summary), accepted_degrees=[r['n'] for r in rows])))


if __name__ == '__main__':
    main()
