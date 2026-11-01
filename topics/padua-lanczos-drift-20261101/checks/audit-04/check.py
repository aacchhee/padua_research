"""Independent bounded audit04 rerun; raw regeneration remains outside Git."""
import argparse
import concurrent.futures
import datetime
import hashlib
import json
import os
import platform
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

sys.set_int_max_str_digits(0)
CODE = Path('tracks/bivariate-lanczos/code/drift')
TOPIC = Path('topics/padua-lanczos-drift-20261101')
FILES = ['cgs2-triangle-n12-pivot.json', 'reproduce-triangle.json',
         'cgs2-rotated-n12-alt.json', 'reproduce-rotated.json']

def pin(path):
    p = Path(path)
    data = p.read_bytes()
    return {'path': str(p), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--work', required=True)
    ap.add_argument('--output', required=True)
    ap.add_argument('--regenerate', action='store_true')
    args = ap.parse_args()
    work = Path(args.work).resolve()
    work.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ, OPENBLAS_NUM_THREADS='1', PYTHONDONTWRITEBYTECODE='1')
    out = {'auditor': 'Codex; requested gpt-6-astra high; resolved runtime metadata unexposed',
           'rules_head': '39b3c5d8690566ce461e6e3a0a628e772a695dbc',
           'candidate': '02bd97b892ed409ec64e9b281130c71a85e914e9',
           'started_utc': utc(), 'python': platform.python_version(),
           'command': [sys.executable, *sys.argv], 'working_directory': str(Path.cwd()),
           'environment': {'PYTHONPATH': env.get('PYTHONPATH'), 'OPENBLAS_NUM_THREADS': '1'},
           'inputs': [pin(p) for p in [__file__, CODE/'e1_scalar_finite_check.py',
               CODE/'e1_cgs2.py', CODE/'e1_reproduce.py', CODE/'e1_cgs2_multinode.py',
               CODE/'e1_sign_check.py', CODE/'e1_cgs2_witness.py', CODE/'e1_exact.py',
               TOPIC/'evidence/response-03-e1-regeneration-check.json',
               TOPIC/'evidence/response-02-e1-scalar-finite.json']]}

    def check(label, directory, expected, missing):
        path = work / (label + '.json')
        cmd = [sys.executable, '-B', str(CODE/'e1_scalar_finite_check.py'), '--output', str(path)]
        if directory is not None:
            cmd += ['--regenerated', str(directory)]
        run = subprocess.run(cmd, capture_output=True, text=True, env=env)
        d = json.loads(path.read_text())
        regen = d.get('new_regeneration')
        record = {'case': label, 'command': cmd, 'exit_status': run.returncode,
                  'all_pass': d['all_pass'], 'sets_pass': {r['set']: r['pass'] for r in d['sets']},
                  'raw_output': pin(path)}
        assert run.returncode == (0 if expected else 1), record
        assert d['all_pass'] is expected and all(record['sets_pass'].values()), record
        if regen is not None:
            assert regen['pass'] is expected and set(regen['missing_required']) == set(missing), regen
            record['regeneration'] = regen
        print(json.dumps({'case': label, 'expected_result_verified': True}), flush=True)
        return record

    out['cases'] = [check('none', None, True, [])]
    with tempfile.TemporaryDirectory(dir=work) as temp:
        absent = Path(temp)/'absent'
        out['cases'].append(check('absent', absent, False, FILES))

    def produce(spec):
        filename, script, extra = spec
        cmd = [sys.executable, '-B', str(CODE/script), *extra, '--output', str(work/filename)]
        started, t = utc(), time.monotonic()
        run = subprocess.run(cmd, capture_output=True, text=True, env=env)
        assert run.returncode == 0, (cmd, run.stderr[-2000:])
        record = {'command': cmd, 'started_utc': started, 'finished_utc': utc(),
                  'wall_seconds': time.monotonic()-t, 'exit_status': run.returncode,
                  'output': pin(work/filename)}
        print(json.dumps({'producer_completed': filename, 'wall_seconds': record['wall_seconds']}), flush=True)
        return record

    specs = [(FILES[2], 'e1_cgs2.py', ['--set','rotated','--degree','12','--rule','alt']),
             (FILES[3], 'e1_reproduce.py', ['--set','rotated']),
             (FILES[0], 'e1_cgs2.py', ['--set','triangle','--degree','12','--rule','pivot']),
             (FILES[1], 'e1_reproduce.py', ['--set','triangle'])]
    if args.regenerate:
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
            out['fresh_regeneration'] = list(pool.map(produce, specs))
        (work/'regeneration-runs.json').write_text(json.dumps(out['fresh_regeneration'], indent=1)+'\n')
    else:
        out['fresh_regeneration'] = json.loads((work/'regeneration-runs.json').read_text())
        out['regeneration_reuse_note'] = 'Own actual separate audit04 executions from the preceding --regenerate invocation.'

    out['cases'].append(check('complete', work, True, []))
    for index, omitted in enumerate(FILES):
        with tempfile.TemporaryDirectory(dir=work) as temp:
            directory = Path(temp)
            for name in FILES:
                if name != omitted:
                    shutil.copyfile(work/name, directory/name)
            out['cases'].append(check('partial-'+str(index), directory, False, [omitted]))
    prior = json.loads((TOPIC/'evidence/response-03-e1-regeneration-check.json').read_text())
    out['comparison_to_developer'] = {
        'checker_pin_equal': prior['checker_sha256_now'] == pin(CODE/'e1_scalar_finite_check.py')['sha256'],
        'none_absent_complete_exit_and_flag_equal': all(
            r['exit_status'] == prior['cases'][r['case']]['cli_exit_status'] and
            r['all_pass'] == prior['cases'][r['case']]['all_pass']
            for r in out['cases'] if r['case'] in ('none', 'absent', 'complete')),
        'partial_reproduce_rotated_exit_and_flag_equal':
            out['cases'][-1]['exit_status'] == prior['cases']['partial']['cli_exit_status'] and
            out['cases'][-1]['all_pass'] == prior['cases']['partial']['all_pass'],
        'raw_byte_identity_expected': False,
        'reason': 'Fresh paths/timings/Python differ; positive checker compares exact uppers and producer/certificate pins.',
    }
    assert all(out['comparison_to_developer'][k] for k in
               ['checker_pin_equal','none_absent_complete_exit_and_flag_equal','partial_reproduce_rotated_exit_and_flag_equal'])
    out['finished_utc'] = utc()
    out['result'] = 'PASS'
    out['limits'] = 'Independent execution of inspected producers/checker, not a new independent mathematical implementation; no campaign-wide replay or IEEE claim. Raw files regenerable outside Git.'
    Path(args.output).write_text(json.dumps(out, indent=1)+'\n')
    print(json.dumps({'result': out['result'], 'cases': len(out['cases'])}), flush=True)

if __name__ == '__main__':
    main()
