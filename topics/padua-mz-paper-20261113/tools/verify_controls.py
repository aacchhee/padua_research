#!/usr/bin/env python3
"""Outcome controls for the evidence-pack verifiers (verify.sh of both Zenodo packs).

These controls run the *real* verify.sh shell logic end to end on a copy of a staged
pack, but replace the numerical programs it calls by small stubs. Each stub writes the
committed receipt (or archived file) that the real program is expected to reproduce,
optionally altered to simulate a specific disagreement. They test the verifier's
outcome logic, exit status and final wording; they are not certificate runs.

Usage:
  python verify_controls.py --pack-dir STAGED_PACK_DIR --pack mz-cc|mz-sp --out OUT.json [--python PY]

Each scenario copies the pack, installs the stubs, creates `venv/bin/python` in the pack
root as a symlink to the given interpreter, and runs `PY=venv/bin/python bash verify.sh ...`
from the pack root, exactly as the README documents. It records exit status, the
summary lines and whether they match the expectation.
"""
import argparse, json, os, shutil, subprocess, sys, tempfile
from pathlib import Path

C = 'topics/padua-mz-cleanup-20261105'
F = 'topics/padua-mz-2d-frontier-20261105'
S = 'topics/padua-mz-sharp-constants-20261106'
T = S

STUB_COMMON = r'''#!/usr/bin/env python3
# CONTROL STUB (verify_controls.py): not the real program.
import gzip, json, os, shutil, sys
from pathlib import Path
MODE = os.environ.get('CONTROL_MODE', 'agree')
PACK = Path(os.environ['CONTROL_PACK'])
REPO = PACK / 'repository'
def arg(name, default=None):
    a = sys.argv
    return a[a.index(name) + 1] if name in a else default
def args_after(name):
    a = sys.argv; i = a.index(name) + 1; out = []
    while i < len(a) and not a[i].startswith('--'):
        out.append(a[i]); i += 1
    return out
def copy_json(src, dst, edit=None):
    d = json.loads(Path(src).read_text())
    if edit: edit(d)
    Path(dst).parent.mkdir(parents=True, exist_ok=True)
    Path(dst).write_text(json.dumps(d))
'''

STUBS = {
    f'{C}/code/rigorous_witness.py': r'''
m = int(arg('--m'))
ref = REPO / 'topics/padua-mz-cleanup-20261105/evidence' / f'witness-producer-m{m}.json'
if arg('--witness'):
    if MODE == 'producer_crash':
        sys.exit(3)
    def e(d): d['witness']['source_vector_sha256'] = None
    copy_json(ref, arg('--output'), e)
else:   # --vector: regenerate witness from the given vector
    scratch = Path(arg('--scratch')); scratch.mkdir(parents=True, exist_ok=True)
    arch = PACK / 'data/witnesses' / f'cert-m{m}'
    payload = gzip.decompress((arch / 'witness.json.gz').read_bytes())
    if MODE == 'payload_differs':
        payload = payload.replace(b'1', b'2', 1)
    (scratch / 'witness.json.gz').write_bytes(gzip.compress(payload))
    shutil.copyfile(arch / 'exact-norm.txt', scratch / 'exact-norm.txt')
    copy_json(ref, arg('--output'))
''',
    f'{C}/code/independent_witness.py': r'''
w = arg('--witness'); m = int(Path(w).parent.name.split('m')[-1])
ref = REPO / 'topics/padua-mz-cleanup-20261105/evidence' / f'witness-independent-m{m}.json'
def e(d):
    if MODE == 'required_fails' and m == 1240:
        d['accepted'] = False
copy_json(ref, arg('--output'), e)
''',
    f'{C}/code/g1_minimum.py': r'''
vd = Path(arg('--vector-dir')); vd.mkdir(parents=True, exist_ok=True)
for m in args_after('--m'):
    m = int(m); name = f'm{m}-n{m-1}-min.npy'
    b = (PACK / 'data/source-vectors' / name).read_bytes()
    if MODE in ('vector_differs', 'payload_differs'):
        b = b[:-1] + bytes([b[-1] ^ 1])
    (vd / name).write_bytes(b)
Path(arg('--output')).parent.mkdir(parents=True, exist_ok=True)
Path(arg('--output')).write_text('{}')
''',
    f'{F}/code/cert_native.py': r'''
od = Path(arg('--output-dir')); od.mkdir(parents=True, exist_ok=True)
for m in args_after('--m'):
    shutil.copyfile(REPO / 'topics/padua-mz-2d-frontier-20261105/evidence' / f'cert-m{m}.json', od / f'cert-m{m}.json')
''',
    f'{F}/code/independent_cert.py': r'''
m = Path(arg('--producer-receipt')).stem.split('-m')[-1]
copy_json(REPO / 'topics/padua-mz-2d-frontier-20261105/evidence' / f'independent-cert-m{m}.json', arg('--output'))
''',
    f'{S}/code/P1_rectangle.py': r'''
n = arg('--N')
copy_json(REPO / 'topics/padua-mz-sharp-constants-20261106/evidence' / f'P1-rectangle-N{n}.json', arg('--output'))
''',
    'tracks/mz-constants/code/reproduce.py': r'''
suite = arg('--suite', 'all')
src = PACK / ('data/table1/reproduction.json' if suite == 'all' else f'data/measurements/reproduction-{suite}.json')
shutil.copyfile(src, arg('--output'))
''',
    f'{T}/code/P4_rayleigh.py': r'''
def e(d):
    d['protocol_sha256'] = 'not-compared'
    if MODE == 'required_fails':
        d['finite_threshold_pass'] = False
copy_json(REPO / 'topics/padua-mz-sharp-constants-20261106/evidence/P4-rayleigh.json', arg('--output'), e)
''',
    f'{T}/code/P4_check_grouped.py': r'''
copy_json(REPO / 'topics/padua-mz-sharp-constants-20261106/evidence/P4-grouped-check.json', arg('--output'))
''',
}

# scenario: (CONTROL_MODE, extra verify.sh args, expected exit, expected summary lines)
SCENARIOS = {
    'mz-sp': [
        ('agree', [], 0, ['ALL REQUIRED CHECKS AGREE']),
        ('agree', ['--regenerate'], 0, ['ALL REQUIRED CHECKS AGREE', 'OPTIONAL REGENERATION REPRODUCED THE ARCHIVED WITNESSES (0 source-vector difference(s) noted)']),
        ('vector_differs', ['--regenerate'], 0, ['ALL REQUIRED CHECKS AGREE', 'OPTIONAL REGENERATION REPRODUCED THE ARCHIVED WITNESSES (3 source-vector difference(s) noted)']),
        ('payload_differs', ['--regenerate'], 2, ['ALL REQUIRED CHECKS AGREE', 'OPTIONAL REGENERATION DID NOT REPRODUCE THE ARCHIVED WITNESSES (see above; the archived certificates are unaffected)']),
        ('required_fails', ['--regenerate'], 1, ['REQUIRED CHECKS FAILED (see DIFFER/FAILED lines above)', 'OPTIONAL REGENERATION REPRODUCED THE ARCHIVED WITNESSES (0 source-vector difference(s) noted)']),
        ('producer_crash', [], 1, ['REQUIRED CHECKS FAILED (see DIFFER/FAILED lines above)']),
    ],
    'mz-cc': [
        ('agree', [], 0, ['ALL REQUIRED CHECKS AGREE']),
        ('required_fails', [], 1, ['REQUIRED CHECKS FAILED (see DIFFER/FAILED lines above)']),
    ],
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--pack-dir', required=True); ap.add_argument('--pack', choices=list(SCENARIOS), required=True)
    ap.add_argument('--out', required=True); ap.add_argument('--python', default=sys.executable)
    a = ap.parse_args()
    results = []
    for mode, extra, want_exit, want_lines in SCENARIOS[a.pack]:
        with tempfile.TemporaryDirectory(prefix='mz-verify-control-') as tmp:
            pack = Path(tmp) / Path(a.pack_dir).name
            shutil.copytree(a.pack_dir, pack, symlinks=True)
            for rel, body in STUBS.items():
                p = pack / 'repository' / rel
                if p.exists():
                    p.write_text(STUB_COMMON + body)
            (pack / 'venv/bin').mkdir(parents=True)
            os.symlink(a.python, pack / 'venv/bin/python')
            env = dict(os.environ, CONTROL_MODE=mode, CONTROL_PACK=str(pack), PY='venv/bin/python')
            r = subprocess.run(['bash', 'verify.sh', 'out', *extra], cwd=pack, env=env, capture_output=True, text=True)
            lines = r.stdout.strip().splitlines()
            summary = lines[lines.index('== Summary') + 1:] if '== Summary' in lines else lines[-3:]
            ok = (r.returncode == want_exit) and (summary == want_lines)
            results.append(dict(pack=a.pack, mode=mode, args=['out', *extra], exit=r.returncode, expected_exit=want_exit,
                                summary=summary, expected_summary=want_lines, pass_=ok,
                                differ_lines=[l for l in lines if l.startswith(('DIFFER', 'FAILED', 'NOTE'))],
                                stderr_tail=r.stderr[-400:]))
            print(('PASS ' if ok else 'FAIL ') + f'{a.pack} {mode} {" ".join(extra)} exit={r.returncode} {summary}')
    Path(a.out).write_text(json.dumps(dict(scope='verifier outcome controls with stubbed numerical programs; not certificate runs',
                                           interpreter_invocation='PY=venv/bin/python bash verify.sh ... from the pack root',
                                           results=results), indent=1) + '\n')
    sys.exit(0 if all(r['pass_'] for r in results) else 1)


if __name__ == '__main__':
    main()
