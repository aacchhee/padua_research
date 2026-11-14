"""P8 negative controls on disposable copies. Usage: python3 -I negatives.py <pristine_pkg> <workdir>"""
import gzip, hashlib, json, os, shutil, subprocess, sys, time, resource
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
src, work = Path(sys.argv[1]), Path(sys.argv[2]); work.mkdir(exist_ok=False)
H = lambda b: hashlib.sha256(b).hexdigest()
results = []

def fresh(name):
    d = work / name; shutil.copytree(src, d)
    for p in d.rglob('*'): os.chmod(p, 0o700 if p.is_dir() else 0o600)
    return d
def refresh_sums(d):
    s = ''.join(H(p.read_bytes()) + '  ' + p.relative_to(d).as_posix() + '\n'
                for p in sorted(d.rglob('*'), key=lambda q: q.relative_to(d).as_posix()) if p.is_file() and p.relative_to(d).as_posix() != 'SHA256SUMS')
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
jobs = []
def run(name, d, args, expect, opt=False):
    jobs.append((name, d, args, expect, opt))
def execute(job):
    name, d, args, expect, opt = job
    t = time.monotonic()
    p = subprocess.run(['/usr/bin/python3'] + (['-O'] if opt else []) + ['-E', '-B', 'verify.py'] + args, cwd=d, capture_output=True, text=True, preexec_fn=lim, timeout=900,
                       env={'PATH': '/usr/bin:/bin', 'OPENBLAS_NUM_THREADS': '1', 'OMP_NUM_THREADS': '1'})
    last = (p.stdout.strip().splitlines() or [''])[-1]
    err = (p.stderr.strip().splitlines() or [''])[-1]
    outcome = 'accept' if p.returncode == 0 else 'reject'
    return dict(name=name, args=args, returncode=p.returncode, outcome=outcome, expected=expect, as_expected=outcome == expect,
                passed_integrity='PASS integrity' in p.stdout, last_stdout=last, last_stderr=err[:300], wall=round(time.monotonic() - t, 2))
def edit_json(path, fn):
    d = json.loads(path.read_text()); fn(d); path.write_text(json.dumps(d))
def tamper_expected(d, n, fn):
    p = d / 'phase/expected-results.jsonl'; lines = p.read_text().splitlines(); out = []
    for s in lines:
        r = json.loads(s)
        out.append(fn(s) if r['n'] == n else s)
    p.write_text('\n'.join(out) + '\n')

# ---- previous audit-07 cases (N-numbers kept) ----
d = fresh('N01'); p = d / 'phase/inputs/n0100-produce.json'; b = bytearray(p.read_bytes()); b[-2] ^= 1; p.write_bytes(bytes(b)); run('N01 changed byte in input, no refresh', d, [], 'reject')
d = fresh('N02'); (d / 'polynomial/inputs/n0010.json.gz').unlink(); run('N02 missing polynomial input', d, [], 'reject')
d = fresh('N03'); (d / 'notes.txt').write_text('x'); run('N03 extra unlisted file', d, [], 'reject')
d = fresh('N04'); (d / 'notes.txt').write_text('arbitrary extra'); refresh_sums(d); run('N04 extra file, SHA256SUMS refreshed, MANIFEST not', d, [], 'reject')
d = fresh('N05'); shutil.copy(d / 'phase/inputs/n0100-produce.json', d / 'phase/inputs/n0100-produce-copy.json'); refresh_sums(d); run('N05 extra phase input file, sums refreshed', d, [], 'reject')
d = fresh('N06'); shutil.copy(d / 'phase/inputs/n0041-produce.json', d / 'phase/inputs/n0042-produce.json'); refresh(d); run('N06 n41 bytes into n42 slot, fully refreshed', d, [], 'reject')
d = fresh('N07'); a, v = d / 'phase/inputs/n0300-produce.json', d / 'phase/inputs/n0300-verify.json'; ab, vb = a.read_bytes(), v.read_bytes(); a.write_bytes(vb); v.write_bytes(ab); refresh_sums(d); run('N07 swap produce/verify n300, sums refreshed, manifest not', d, [], 'reject')
d = fresh('N08'); a, v = d / 'phase/inputs/n0300-produce.json', d / 'phase/inputs/n0300-verify.json'; ab, vb = a.read_bytes(), v.read_bytes(); a.write_bytes(vb); v.write_bytes(ab); refresh(d); run('N08 swap produce/verify n300, fully refreshed, replay 300', d, ['--degrees', '300'], 'accept')
d = fresh('N09'); edit_json(d / 'phase/inputs/n0100-produce.json', lambda j: j['S_upper_rows'][0].__setitem__(2, '0x1p-4')); refresh(d)
run('N09a lowered S endpoint n100 produce only, refreshed, integrity', d, [], 'reject')
def tamper_near(s):
    r = json.loads(s); r['near_min'] = '1/1000'; return json.dumps(r, sort_keys=True, separators=(',', ':'))
d = fresh('N11'); tamper_expected(d, 100, tamper_near); refresh(d)
run('N11a expected near_min n100 tampered, refreshed, integrity', d, [], 'accept')
run('N11b same, replay 100', d, ['--degrees', '100'], 'reject')
d = fresh('N12'); p = d / 'phase/expected-results.jsonl'; t = p.read_text().splitlines(); t = [s[:-1] + ',"n":%d}' % json.loads(s)['n'] for s in t]; p.write_text('\n'.join(t) + '\n'); refresh(d)
run('N12 duplicate key (same value) in every expected row, refreshed', d, [], 'reject')
d = fresh('N13'); p = d / 'phase/inputs/n0100-produce.json'; s = p.read_text().rstrip(); p.write_text(s[:-1] + ',"n":100}'); refresh(d); run('N13 duplicate key in phase input, refreshed', d, [], 'reject')
d = fresh('N14'); p = d / 'phase/inputs/n0100-produce.json'; s = p.read_text().rstrip(); p.write_text(s[:-1] + ',"extra":NaN}'); refresh(d); run('N14 NaN in phase input, refreshed', d, [], 'reject')
d = fresh('N15'); (d / 'SHA256SUMS').write_text((d / 'SHA256SUMS').read_text() + H(b'') + '  ../outside\n'); run('N15 traversal line in SHA256SUMS', d, [], 'reject')
d = fresh('N16'); s = (d / 'SHA256SUMS').read_text(); (d / 'SHA256SUMS').write_text(s + s.splitlines()[0] + '\n'); run('N16 duplicate line in SHA256SUMS', d, [], 'reject')
d = fresh('N17'); p = d / 'phase/inputs/n0100-produce.json'; tgt = work / 'outside-n0100.json'; shutil.copy(p, tgt); p.unlink(); p.symlink_to(tgt); run('N17 symlinked input', d, [], 'reject')
d = fresh('N18'); out = work / 'outside-inputs'; shutil.move(str(d / 'phase/inputs'), out); (d / 'phase/inputs').symlink_to(out); run('N18 symlinked inputs directory', d, [], 'reject')
d = fresh('N19')
for a_ in (['--degrees', '40'], ['--degrees', '512'], ['--degrees', '41,41'], ['--degrees', 'all,41'], ['--degrees', ''], ['--degrees', '41,'], ['--degrees', ' 41'],
           ['--polynomial-degrees', '41'], ['--polynomial-degrees', '1'], ['--polynomial-degrees', ''], ['--polynomial-degrees', 'x'], ['--degree', '41']):
    run('N19 selection ' + repr(a_), d, a_, 'reject')
def zero_origin(j): j['origin_lower_hex'] = '0x0p+0'
d = fresh('N20'); [edit_json(d / f'phase/inputs/n0100-{m}.json', zero_origin) for m in ('produce', 'verify')]; refresh(d)
run('N20 origin_lower zeroed both n100 records, refreshed, replay 100', d, ['--degrees', '100'], 'accept')
d = fresh('N21'); s = (d / 'SHA256SUMS').read_text(); (d / 'SHA256SUMS').write_text(s.replace('\n', '\r\n')); run('N21 CRLF SHA256SUMS', d, [], 'accept')
def lower(j): j['S_upper_rows'][0][2] = '0x1p-4'
def raise_c(j): r = j['S_upper_rows'][5]; r[2] = (float.fromhex(r[2]) + 1.0).hex()
def lam_low(j): j['lambda_upper_rows'][0][2] = '0x1p-4'
for tag, fn, deg, exp_replay in [('N22 lowered S endpoint both n100 records', lower, 100, 'reject'), ('N23 raised contained S endpoint +1.0 both n100', raise_c, 100, 'accept'),
                                 ('N24 lowered actual-lambda endpoint both n100', lam_low, 100, 'reject'), ('N22x lowered S endpoint both n410 records', lower, 410, 'reject')]:
    d = fresh(tag.split()[0])
    for mm in ('produce', 'verify'): edit_json(d / f'phase/inputs/n{deg:04d}-{mm}.json', fn)
    refresh(d)
    run(tag + ', refreshed, integrity', d, [], 'accept')
    run(tag + ', refreshed, replay', d, ['--degrees', str(deg)], exp_replay)
d = fresh('N25'); run('N25 -O', d, [], 'reject', opt=True)

# ---- new P8 cases for the response-07 checks ----
def dupkey(s): return s[:-1] + ',"n":100}'
d = fresh('M01'); tamper_expected(d, 100, dupkey); refresh(d); run('M01 duplicate key in one expected row (n100), refreshed', d, [], 'reject')
def nan_field(s): return s[:-1] + ',"extra":NaN}'
d = fresh('M02'); tamper_expected(d, 100, nan_field); refresh(d); run('M02 NaN constant in expected row n100 (both), refreshed', d, [], 'reject')
def inf_field(s): return s[:-1] + ',"extra":1e999}'
d = fresh('M03'); tamper_expected(d, 100, inf_field); refresh(d); run('M03 overflow 1e999 in expected rows n100, refreshed', d, [], 'reject')
def infinity(s): return s[:-1] + ',"extra":Infinity}'
d = fresh('M04'); tamper_expected(d, 100, infinity); refresh(d); run('M04 Infinity constant in expected rows n100, refreshed', d, [], 'reject')
def extra_key(s): return s[:-1] + ',"extra":1}'
d = fresh('M05'); tamper_expected(d, 100, extra_key); refresh(d)
run('M05 extra key in both n100 expected rows, refreshed, integrity', d, [], 'accept'); run('M05b same, replay 100', d, ['--degrees', '100'], 'reject')
d = fresh('M06'); (d / 'analytic/receipt.json').unlink(); refresh_sums(d); run('M06 missing payload file, SHA256SUMS refreshed, MANIFEST not', d, [], 'reject')
d = fresh('M07'); (d / 'notes.txt').write_text('arbitrary extra'); m = json.loads((d / 'MANIFEST.json').read_text())
m['payload'].append(dict(path='notes.txt', bytes=15, sha256=H(b'arbitrary extra'), source={})); (d / 'MANIFEST.json').write_text(json.dumps(m, indent=2)); refresh_sums(d)
run('M07 extra file added to both SHA256SUMS and MANIFEST payload', d, [], 'accept')
d = fresh('M08'); p = d / 'README.txt'; p.write_text(p.read_text() + 'tampered\n'); refresh_sums(d); run('M08 payload changed (README.txt), SHA256SUMS refreshed, MANIFEST not', d, [], 'reject')
d = fresh('M09'); m = json.loads((d / 'MANIFEST.json').read_text()); [r.__setitem__('bytes', r['bytes'] + 1) for r in m['payload'] if r['path'] == 'verify.py']; (d / 'MANIFEST.json').write_text(json.dumps(m, indent=2)); refresh_sums(d)
run('M09 MANIFEST payload byte count wrong (hash right), sums refreshed', d, [], 'reject')
d = fresh('M10'); m = json.loads((d / 'MANIFEST.json').read_text()); m['payload'] = [r for r in m['payload'] if r['path'] != 'README.md'] + [r for r in m['payload'] if r['path'] == 'README.txt']; (d / 'MANIFEST.json').write_text(json.dumps(m)); refresh_sums(d)
run('M10 duplicate payload path replacing another, sums refreshed', d, [], 'reject')
a, b = d.parent / 'x', None
d = fresh('M11'); a, b = d / 'polynomial/inputs/n0005.json.gz', d / 'polynomial/inputs/n0006.json.gz'; ab, bb = a.read_bytes(), b.read_bytes(); a.write_bytes(bb); b.write_bytes(ab); refresh(d)
run('M11 swap polynomial inputs n5/n6, sums+manifest refreshed', d, [], 'reject')
def regzip(p, fn=None):
    raw = gzip.decompress(p.read_bytes())
    if fn: o = json.loads(raw); fn(o); raw = json.dumps(o).encode()
    p.write_bytes(gzip.compress(raw, compresslevel=1, mtime=0))
def set_receipt_sha(d, n):
    sha = H((d / f'polynomial/inputs/n{n:04d}.json.gz').read_bytes())
    name = 'degrees-2-16.json' if n <= 16 else 'degrees-17-32.json'
    edit_json(d / 'polynomial/receipts' / name, lambda j: [r.__setitem__('certificate_sha256', sha) for r in j['accepted_rows'] if r['n'] == n])
d = fresh('M12'); regzip(d / 'polynomial/inputs/n0005.json.gz'); refresh(d); run('M12 n5 re-gzipped (same JSON), sums+manifest refreshed, receipts not', d, [], 'reject')
d = fresh('M13'); regzip(d / 'polynomial/inputs/n0005.json.gz'); set_receipt_sha(d, 5); refresh(d)
run('M13 n5 re-gzipped, receipt sha + sums + manifest refreshed, integrity', d, [], 'accept'); run('M13b same, replay 5', d, ['--polynomial-degrees', '5'], 'accept')
d = fresh('M14'); regzip(d / 'polynomial/inputs/n0005.json.gz', lambda o: o.__setitem__('leaves', o['leaves'][1:])); set_receipt_sha(d, 5); refresh(d)
run('M14 n5 first leaf deleted, receipt sha + sums + manifest refreshed, integrity', d, [], 'accept'); run('M14b same, replay 5', d, ['--polynomial-degrees', '5'], 'reject')
d = fresh('M15'); edit_json(d / 'polynomial/receipts/degrees-2-16.json', lambda j: [r.__setitem__('splits', r['splits'] + 1) for r in j['accepted_rows'] if r['n'] == 5]); refresh(d)
run('M15 stored n5 split count +1, refreshed, integrity', d, [], 'accept'); run('M15b same, replay 5', d, ['--polynomial-degrees', '5'], 'reject')
d = fresh('M16'); edit_json(d / 'polynomial/receipts/degrees-17-32.json', lambda j: [r.__setitem__('bound', r['bound'] - 1) for r in j['accepted_rows'] if r['n'] == 21]); refresh(d)
run('M16 stored n21 bound count -1, refreshed, replay 21', d, ['--polynomial-degrees', '21'], 'reject')
d = fresh('M17'); edit_json(d / 'polynomial/receipts/n0037.json', lambda j: j.__setitem__('accepted', False)); refresh(d); run('M17 stored n37 receipt accepted=false, refreshed', d, [], 'reject')
d = fresh('M18'); edit_json(d / 'polynomial/receipts/degrees-2-16.json', lambda j: [r.__setitem__('actual_returncode', 1) for r in j['accepted_rows'] if r['n'] == 3]); refresh(d); run('M18 stored n3 returncode 1, refreshed', d, [], 'reject')
d = fresh('M19'); edit_json(d / 'polynomial/receipts/degrees-17-32.json', lambda j: j.__setitem__('accepted_rows', [r for r in j['accepted_rows'] if r['n'] != 30])); refresh(d); run('M19 stored row n30 removed, refreshed', d, [], 'reject')
d = fresh('M20'); p = d / 'analytic/tables/paper.tex'; t = p.read_text(); import re
mm = re.search(r'(\d+\.\d{6})', t[t.find('\\begin{tabular'):]); assert mm; old = mm.group(1); new = old[:-1] + str((int(old[-1]) + 1) % 10)
i = t.find(old, t.find('\\begin{tabular')); p.write_text(t[:i] + new + t[i + len(old):]); refresh(d)
run(f'M20 paper table entry {old}->{new}, refreshed, integrity', d, [], 'accept'); run('M20b same, --analytic', d, ['--analytic'], 'reject')
d = fresh('M21'); p = d / 'phase/expected-results.jsonl'; p.write_text(p.read_text() + '\n'); refresh(d); run('M21 trailing blank line in expected-results, refreshed', d, [], 'reject')
d = fresh('M22'); (d / 'phase/inputs/sub').mkdir(); run('M22 empty extra directory in phase/inputs', d, [], 'reject')
d = fresh('M23'); (d / 'emptydir').mkdir(); run('M23 empty extra directory at root', d, [], 'accept')

with ThreadPoolExecutor(3) as ex:
    results = list(ex.map(execute, jobs))
for r in results: print(json.dumps(r))
json.dump(results, open(work / 'negatives.json', 'w'), indent=1)
print('SUMMARY', sum(r['as_expected'] for r in results), '/', len(results), 'as pre-stated expectation')
print('leftover tmp', [p.name for p in Path('/tmp').glob('padua-public-*')])
