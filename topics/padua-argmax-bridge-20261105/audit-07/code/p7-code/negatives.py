"""P7 negative controls on disposable copies. Usage: python3 -I negatives.py <pristine_pkg> <workdir>"""
import hashlib, json, os, shutil, subprocess, sys, time, resource
from pathlib import Path
src, work = Path(sys.argv[1]), Path(sys.argv[2]); work.mkdir(exist_ok=False)
H = lambda b: hashlib.sha256(b).hexdigest()
results = []

def fresh(name):
    d = work / name; shutil.copytree(src, d);
    for p in d.rglob('*'): os.chmod(p, 0o700 if p.is_dir() else 0o600)
    return d
def refresh_sums(d):
    s = ''.join(H(p.read_bytes()) + '  ' + p.relative_to(d).as_posix() + '\n' for p in sorted(d.rglob('*')) if p.is_file() and p.name != 'SHA256SUMS' or (p.is_file() and p.relative_to(d).as_posix() != 'SHA256SUMS' and False))
    (d / 'SHA256SUMS').write_text(s)
def refresh_manifest(d):
    m = json.loads((d / 'MANIFEST.json').read_text())
    for key in ('phase_inputs', 'polynomial_inputs', 'payload'):
        for r in m[key]:
            p = d / r['path']
            if p.exists(): b = p.read_bytes(); r['bytes'] = len(b); r['sha256'] = H(b)
    (d / 'MANIFEST.json').write_text(json.dumps(m, indent=2, sort_keys=True) + '\n')
def refresh(d): refresh_manifest(d); refresh_sums(d)
def lim():
    resource.setrlimit(resource.RLIMIT_AS, (4_000_000_000,) * 2); resource.setrlimit(resource.RLIMIT_CPU, (600, 600)); resource.setrlimit(resource.RLIMIT_CORE, (0, 0))
def run(name, d, args, expect):
    t = time.monotonic()
    p = subprocess.run(['/usr/bin/python3', '-E', '-B', 'verify.py'] + args, cwd=d, capture_output=True, text=True, preexec_fn=lim, timeout=900,
                       env={'PATH': '/usr/bin:/bin', 'OPENBLAS_NUM_THREADS': '1', 'OMP_NUM_THREADS': '1'})
    last = (p.stdout.strip().splitlines() or [''])[-1]
    err = (p.stderr.strip().splitlines() or [''])[-1]
    outcome = 'accept' if p.returncode == 0 else 'reject'
    r = dict(name=name, args=args, returncode=p.returncode, outcome=outcome, expected=expect, as_expected=outcome == expect,
             passed_integrity='PASS integrity' in p.stdout, last_stdout=last, last_stderr=err, wall=round(time.monotonic() - t, 2))
    results.append(r); print(json.dumps(r), flush=True)
def edit_json(path, fn):
    d = json.loads(path.read_text()); fn(d); path.write_text(json.dumps(d))

# N01 changed byte, no refresh
d = fresh('N01'); p = d / 'phase/inputs/n0100-produce.json'; b = bytearray(p.read_bytes()); b[-2] ^= 1; p.write_bytes(bytes(b)); run('N01 changed byte in input, no refresh', d, [], 'reject')
# N02 missing input
d = fresh('N02'); (d / 'polynomial/inputs/n0010.json.gz').unlink(); run('N02 missing polynomial input', d, [], 'reject')
# N03 extra unlisted file
d = fresh('N03'); (d / 'notes.txt').write_text('x'); run('N03 extra unlisted file', d, [], 'reject')
# N04 extra file listed with refreshed SHA256SUMS (non-input location)
d = fresh('N04'); (d / 'notes.txt').write_text('arbitrary extra'); refresh_sums(d); run('N04 extra file with refreshed SHA256SUMS', d, [], 'reject')
# N05 extra phase input with refreshed sums
d = fresh('N05'); shutil.copy(d / 'phase/inputs/n0100-produce.json', d / 'phase/inputs/n0100-produce-copy.json'); refresh_sums(d); run('N05 extra phase input file, refreshed sums', d, [], 'reject')
# N06 duplicate input (n41 bytes in n42 slot), refreshed sums+manifest
d = fresh('N06'); shutil.copy(d / 'phase/inputs/n0041-produce.json', d / 'phase/inputs/n0042-produce.json'); refresh(d); run('N06 duplicate input bytes into other degree, refreshed', d, [], 'reject')
# N07 swap produce/verify n300, refreshed SHA256SUMS only
d = fresh('N07'); a, v = d / 'phase/inputs/n0300-produce.json', d / 'phase/inputs/n0300-verify.json'; ab, vb = a.read_bytes(), v.read_bytes(); a.write_bytes(vb); v.write_bytes(ab); refresh_sums(d); run('N07 swap produce/verify n300, sums refreshed, manifest not', d, [], 'reject')
# N08 swap produce/verify n300, refreshed sums+manifest, then replay
d = fresh('N08'); a, v = d / 'phase/inputs/n0300-produce.json', d / 'phase/inputs/n0300-verify.json'; ab, vb = a.read_bytes(), v.read_bytes(); a.write_bytes(vb); v.write_bytes(ab); refresh(d); run('N08 swap produce/verify n300, fully refreshed, replay 300', d, ['--degrees', '300'], 'reject')
# N09 lowered S upper endpoint below independent lower (n100), refreshed: integrity only, then replay
d = fresh('N09'); edit_json(d / 'phase/inputs/n0100-produce.json', lambda j: j['S_upper_rows'][0].__setitem__(2, '0x1p-4')); refresh(d)
run('N09a lowered S endpoint n100 produce, refreshed, integrity only', d, [], 'accept')
run('N09b same, replay 100', d, ['--degrees', '100'], 'reject')
# N10 raised (contained) S upper endpoint (+1.0): substituted bound - replay cannot see it unless containment count changes
def raise_contained(j):
    r = j['S_upper_rows'][5]; r[2] = (float.fromhex(r[2]) + 1.0).hex()
d = fresh('N10'); edit_json(d / 'phase/inputs/n0100-produce.json', raise_contained); refresh(d); run('N10 raised S endpoint n100 produce (+1.0), refreshed, replay 100', d, ['--degrees', '100'], 'reject')
# N11 expected-row tamper on n100 both records, refreshed: integrity passes; replay 100 rejects; replay 101 passes
def tamper_expected(d, n, key, val):
    p = d / 'phase/expected-results.jsonl'; rows = [json.loads(s) for s in p.read_text().splitlines()]
    for r in rows:
        if r['n'] == n: r[key] = val
    p.write_text(''.join(json.dumps(r, sort_keys=True, separators=(',', ':')) + '\n' for r in rows))
d = fresh('N11'); tamper_expected(d, 100, 'near_min', '1/1000'); refresh(d)
run('N11a expected near_min n100 tampered, refreshed, integrity', d, [], 'accept')
run('N11b same, replay 100', d, ['--degrees', '100'], 'reject')
# N12 duplicate JSON key in expected-results (same value), refreshed
d = fresh('N12'); p = d / 'phase/expected-results.jsonl'; t = p.read_text().splitlines(); t = [s[:-1] + ',"n":%d}' % json.loads(s)['n'] for s in t]; p.write_text('\n'.join(t) + '\n'); refresh(d)
run('N12 duplicate key in every expected row, refreshed', d, [], 'reject')
# N13 duplicate key in phase input, refreshed
d = fresh('N13'); p = d / 'phase/inputs/n0100-produce.json'; s = p.read_text().rstrip(); p.write_text(s[:-1] + ',"n":100}'); refresh(d); run('N13 duplicate key in phase input, refreshed', d, [], 'reject')
# N14 NaN in phase input field, refreshed
d = fresh('N14'); p = d / 'phase/inputs/n0100-produce.json'; s = p.read_text().rstrip(); p.write_text(s[:-1] + ',"extra":NaN}'); refresh(d); run('N14 NaN in phase input, refreshed', d, [], 'reject')
# N15 path traversal and duplicate lines in SHA256SUMS
d = fresh('N15'); (d / 'SHA256SUMS').write_text((d / 'SHA256SUMS').read_text() + H(b'') + '  ../outside\n'); run('N15 traversal line in SHA256SUMS', d, [], 'reject')
d = fresh('N16'); s = (d / 'SHA256SUMS').read_text(); (d / 'SHA256SUMS').write_text(s + s.splitlines()[0] + '\n'); run('N16 duplicate line in SHA256SUMS', d, [], 'reject')
# N17 symlinked input file
d = fresh('N17'); p = d / 'phase/inputs/n0100-produce.json'; tgt = work / 'outside-n0100.json'; shutil.copy(p, tgt); p.unlink(); p.symlink_to(tgt); run('N17 symlinked input', d, [], 'reject')
# N18 symlinked directory (phase/inputs -> outside copy)
d = fresh('N18'); out = work / 'outside-inputs'; shutil.move(str(d / 'phase/inputs'), out); (d / 'phase/inputs').symlink_to(out); run('N18 symlinked inputs directory', d, [], 'reject')
# N19 bad degree selections
d = fresh('N19')
run('N19a --degrees 40', d, ['--degrees', '40'], 'reject')
run('N19b --degrees 41,41', d, ['--degrees', '41,41'], 'reject')
run('N19c --polynomial-degrees 41', d, ['--polynomial-degrees', '41'], 'reject')
# N20 forged-consistent package: change n100 tree-independent field that affects result (pi bracket untouched) -> mutate expected + input consistently
# Lower origin_lower_hex for n100 both records to 0 (substitution, accepted) and change native_lower_contained only if needed: shows input bytes changed but full pass
def zero_origin(j): j['origin_lower_hex'] = '0x0p+0'
d = fresh('N20'); [edit_json(d / f'phase/inputs/n0100-{m}.json', zero_origin) for m in ('produce', 'verify')]; refresh(d)
run('N20 origin_lower zeroed in both n100 records, refreshed, replay 100', d, ['--degrees', '100'], 'reject')
# N21 checksum file CRLF
d = fresh('N21'); s = (d / 'SHA256SUMS').read_text(); (d / 'SHA256SUMS').write_text(s.replace('\n', '\r\n')); run('N21 CRLF SHA256SUMS', d, [], 'reject')
json.dump(results, open(work / 'negatives.json', 'w'), indent=1)
print('SUMMARY', sum(r['as_expected'] for r in results), '/', len(results), 'as pre-stated expectation')
