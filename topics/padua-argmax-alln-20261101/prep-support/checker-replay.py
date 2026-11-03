"""Replay guarded proof checkers in a fresh scratch mirror; JSON goes to stdout.

The mirror preserves repository-relative paths and source bytes. Frozen evidence
and source-repository outputs are never overwritten. Large scratch is ephemeral.
"""
import ast
import copy
import gzip
import hashlib
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import tempfile
import time

TOPIC = Path(__file__).resolve().parents[1]
ROOT = TOPIC.parents[1]
REL = str(TOPIC.relative_to(ROOT))
ENTRIES = (
    'code/part3/finite_n2_exact.py',
    'code/part3/finite_bernstein_check.py',
    'code/part3/finite_general_check.py',
    'code/part3/finite_general_controls.py',
    'code/part3/pairing_exact_check.py',
    'code/part3/pairing_independent_reconstruction.py',
    'code/gated/d3_edge_check.py',
)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def run():
    started = time.monotonic()
    input_roots = (REL + '/code', REL + '/outputs',
                   'topics/padua-proof-attempts-2-20261101/code',
                   'topics/padua-proof-attempts-2-20261101/outputs',
                   'topics/padua-proof-attempts-20261101/theory')
    # Other workers update theory/registry records concurrently. Monitor only
    # scientific source/evidence inputs; packaging metadata belongs to parent.
    excluded = {REL + '/code/part3/check_evidence.py',
                REL + '/outputs/part3/packaging-validation.json'}
    monitored = sorted(p for relative in input_roots for p in (ROOT / relative).rglob('*')
                       if p.is_file() and '__pycache__' not in p.parts
                       and str(p.relative_to(ROOT)) not in excluded)
    before = {str(p.relative_to(ROOT)): digest(p.read_bytes()) for p in monitored}
    commands = []
    with tempfile.TemporaryDirectory(prefix='padua-checker-replay-') as folder:
        scratch = Path(folder)
        mirror = scratch / 'repo'
        for relative in input_roots:
            shutil.copytree(ROOT / relative, mirror / relative,
                            ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
        topic = mirror / REL
        historical_pairing = REL + '/outputs/part3/pairing_screens.json'
        pairing_bytes = subprocess.check_output(
            ['git', '-C', str(ROOT), 'show',
             '1cecd68ac0a64b01ed7b2d262b6263a955a7d4d7:' + historical_pairing])
        cold = json.loads((TOPIC / 'cold-storage.json').read_text())
        entry = next(e for e in cold['entries'] if e['path'] == historical_pairing)
        if digest(pairing_bytes) != entry['sha256'] or len(pairing_bytes) != entry['bytes']:
            raise ValueError('historical pairing source identity mismatch')
        (mirror / historical_pairing).write_bytes(pairing_bytes)
        out = scratch / 'out'
        out.mkdir()

        def execute(label, arguments, want=0, env=None):
            command = [sys.executable, '-B', *map(str, arguments)]
            result = subprocess.run(command, cwd=mirror, capture_output=True, env=env)
            (out / (label + '.stdout')).write_bytes(result.stdout)
            (out / (label + '.stderr')).write_bytes(result.stderr)
            if (want == 0 and result.returncode != 0) or (want != 0 and result.returncode == 0):
                raise RuntimeError(label + ': ' + result.stderr.decode(errors='replace'))
            commands.append({'case': label, 'argv': [a.replace(str(mirror), '<repo>').replace(str(scratch), '<scratch>').replace(sys.executable, '<python>') for a in command],
                             'returncode': result.returncode,
                             'stdout_sha256': digest(result.stdout),
                             'stderr_sha256': digest(result.stderr)})
            return result

        for index, name in enumerate(ENTRIES):
            script = topic / name
            for option in ('-O', '-OO'):
                result = execute('optimized_' + str(index) + option[1:], [option, script], want=1)
                if b'Scientific verification requires Python assertions' not in result.stderr:
                    raise ValueError('did not reach explicit refusal: ' + name)
            env = dict(os.environ)
            env['PYTHONOPTIMIZE'] = '1'
            result = execute('environment_optimized_' + str(index), [script], want=1, env=env)
            if b'Scientific verification requires Python assertions' not in result.stderr:
                raise ValueError('environment optimization not explicitly refused: ' + name)

        execute('n2', [topic / ENTRIES[0], '--output', out / 'n2.json'])
        n2 = json.loads((out / 'n2.json').read_text())
        if not n2['accepted'] or n2['global_maximum'] != '3':
            raise ValueError('n2 claim changed')
        execute('n8_field', [topic / ENTRIES[1], topic / 'outputs/part3/finite_n8_pilot.json.gz',
                             '--output', out / 'n8-field.json'])
        for n in range(8, 17):
            name = 'finite_n12_pilot.json.gz' if n == 12 else 'finite_n' + str(n) + '_general.json.gz'
            execute('n' + str(n) + '_general', [topic / ENTRIES[2], topic / 'outputs/part3' / name,
                                               '--output', out / ('n' + str(n) + '.json')])
        execute('general_controls', [topic / ENTRIES[3], topic / 'outputs/part3/finite_n12_pilot.json.gz',
                                      '--output', out / 'general-controls.json'])
        execute('n8_field_controls', [topic / 'outputs/part3/independent_n8_controls.py'])
        execute('n12_independent_controls', [topic / 'outputs/part3/independent_general_controls.py'])
        execute('pairing', [topic / ENTRIES[4], topic / 'outputs/part3/pairing_screens.json',
                             '--output', out / 'pairing.json'])
        execute('pairing_reconstruction', [topic / ENTRIES[5]])
        execute('d3_controls', [topic / ENTRIES[6], topic / 'outputs/gated/d3_edge_certificate.json',
                                '--output', out / 'd3.json', '--controls'])
        accepted = [json.loads((out / file).read_text()) for file in
                    ['n8-field.json'] + ['n' + str(n) + '.json' for n in range(8, 17)]]
        if not all(d['accepted'] and d['complete_partition'] and d['all_supplied_bounds_verified'] for d in accepted):
            raise ValueError('finite replay changed')
        controls = json.loads((out / 'general-controls.json').read_text())
        d3 = json.loads((out / 'd3.json').read_text())
        if controls['negative_count'] != 14 or d3['malformed_controls']['count'] != 17:
            raise ValueError('corruption control scope changed')
        # A forged n2 source pin must not bypass either historical adapter.
        for label, checker_path, certificate in (
            ('forged_general_n2_pin', topic / ENTRIES[2], topic / 'outputs/part3/finite_n12_pilot.json.gz'),
            ('forged_d3_n2_pin', topic / ENTRIES[6], topic / 'outputs/gated/d3_edge_certificate.json')):
            raw = certificate.read_bytes()
            data = json.loads(gzip.decompress(raw) if certificate.suffix == '.gz' else raw)
            key = 'finite_n2_exact.py' if label.startswith('forged_general') else 'code/part3/finite_n2_exact.py'
            data['source_sha256'][key] = '0' * 64
            path = out / (label + '.json')
            path.write_text(json.dumps(data))
            execute(label, [checker_path, path, '--output', out / (label + '-receipt.json')], want=1)
        # Record semantic outcomes, not platform timings or fresh proof evidence.
        semantic = {'n2': n2['accepted'], 'finite_certificates_replayed': len(accepted),
                    'general_malformed_rejected': controls['negative_count'],
                    'field_malformed_rejected': 5, 'independent_general_malformed_rejected': 4,
                    'd3_malformed_rejected': d3['malformed_controls']['count'],
                    'pairing': json.loads((out / 'pairing.json').read_text())['check'],
                    'd3_pairs': len(d3['pairs']), 'd3_witnesses': len(d3['exact_EP_reversal_witnesses'])}
    after = {str(p.relative_to(ROOT)): digest(p.read_bytes()) for p in monitored}
    if before != after:
        raise ValueError('source topic file set or bytes changed during scratch replay')
    return {'accepted': True, 'input_head': 'cdb12257af24ea2542de707b9730f8278d69a168',
            'python': sys.version, 'python_executable': sys.executable, 'platform': platform.platform(),
            'guarded_entry_points': list(ENTRIES), 'optimization_refusals': 3 * len(ENTRIES),
            'semantics': semantic, 'monitored_scientific_inputs_unchanged': len(before),
            'sources': {name: digest((TOPIC / name).read_bytes()) for name in
                        [*ENTRIES, 'code/part3/proof_runtime.py']},
            'commands': commands, 'seconds': time.monotonic() - started,
            'scope': 'All writes in fresh scratch mirror; frozen certificates and receipts preserved. No new research.'}


if __name__ == '__main__':
    print(json.dumps(run(), separators=(',', ':')))
