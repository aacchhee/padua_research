"""E8 negative controls on disposable copies of the delivered ZIP package (integrity paths only)."""
import hashlib, json, shutil, subprocess, sys, importlib.util
from pathlib import Path

SRC = Path(sys.argv[1]); WORK = Path(sys.argv[2])
sha = lambda b: hashlib.sha256(b).hexdigest()

def fresh(name):
    d = WORK / name
    if d.exists(): shutil.rmtree(d)
    shutil.copytree(SRC, d)
    for p in d.rglob('*'):
        if p.is_file(): p.chmod(0o644)
    return d

def refresh(d, manifest_too=True, skip=()):
    if manifest_too:
        m = json.loads((d/'MANIFEST.json').read_bytes())
        for row in m['payload']:
            if row['path'] in skip: continue
            p = d/row['path']
            if p.exists():
                b = p.read_bytes(); row['bytes'] = len(b); row['sha256'] = sha(b)
        (d/'MANIFEST.json').write_bytes((json.dumps(m, indent=2, sort_keys=True)+'\n').encode())
    files = sorted(p for p in d.rglob('*') if p.is_file() and p.name != 'SHA256SUMS' or (p.is_file() and p.relative_to(d).as_posix() != 'SHA256SUMS' and p.name == 'SHA256SUMS'))
    s = ''.join(sha(p.read_bytes())+'  '+p.relative_to(d).as_posix()+'\n' for p in files if p.relative_to(d).as_posix() != 'SHA256SUMS')
    (d/'SHA256SUMS').write_text(s)

def run(d, label, extra=()):
    r = subprocess.run([sys.executable, *extra, '-E', '-B', str(d/'verify.py')], cwd=WORK, capture_output=True, text=True, timeout=300)
    last = (r.stderr.strip().splitlines() or [''])[-1]
    print(json.dumps(dict(control=label, rc=r.returncode, stdout=r.stdout.strip().splitlines()[-1:] , stderr_last=last)))
    return r

def edit_expected(d, fn):
    p = d/'phase/expected-results.jsonl'; lines = p.read_text().splitlines(); lines[0] = fn(lines[0]); p.write_text('\n'.join(lines)+'\n')

# C0 baseline
d = fresh('c0'); run(d, 'C0 baseline integrity, unmodified copy')
# C0b baseline after our refresh routine (refresh must be a no-op)
d = fresh('c0b'); refresh(d); run(d, 'C0b refresh-only (should PASS)')
# C1 duplicate key in expected results
d = fresh('c1'); edit_expected(d, lambda s: s[:-1]+', "n": '+str(json.loads(s)['n'])+'}'); refresh(d); run(d, 'C1 duplicate key expected-results line 1 (same value)')
# C2 NaN literal
d = fresh('c2'); edit_expected(d, lambda s: s[:-1]+', "zz": NaN}'); refresh(d); run(d, 'C2 NaN literal in expected-results')
# C3 overflowing float
d = fresh('c3'); edit_expected(d, lambda s: s[:-1]+', "zz": 1e999}'); refresh(d); run(d, 'C3 1e999 in expected-results')
# C4 extra file in SHA256SUMS but not in manifest payload
d = fresh('c4'); (d/'phase/extra.txt').write_text('x\n'); refresh(d, manifest_too=False); run(d, 'C4 extra file listed in SHA256SUMS only')
# C5 manifest payload hash mismatch (README.txt row), SHA256SUMS refreshed
d = fresh('c5'); m = json.loads((d/'MANIFEST.json').read_bytes())
for row in m['payload']:
    if row['path'] == 'README.txt': row['sha256'] = '0'*64
(d/'MANIFEST.json').write_bytes((json.dumps(m, indent=2, sort_keys=True)+'\n').encode()); refresh(d, manifest_too=False); run(d, 'C5 manifest payload sha mismatch README.txt')
# C6 stored polynomial certificate hash mismatch n33
d = fresh('c6'); p = d/'polynomial/receipts/n0033.json'; r = json.loads(p.read_bytes()); r['certificate_sha256'] = '0'*64
p.write_text(json.dumps(r, indent=2)+'\n'); refresh(d); run(d, 'C6 stored n33 certificate_sha256 tampered')
# C7 tampered n2 stored counts: integrity expected PASS (counts compared only at replay)
d = fresh('c7'); p = d/'polynomial/receipts/degrees-2-16.json'; r = json.loads(p.read_bytes()); r['accepted_rows'][0]['bound_leaves'] += 1
p.write_text(json.dumps(r, indent=2)+'\n'); refresh(d); run(d, 'C7 tampered n2 stored bound_leaves, integrity only')
# C7b comparison logic with stubbed subprocess (no compile, no numerical replay)
spec = importlib.util.spec_from_file_location('v_c7', d/'verify.py'); v = importlib.util.module_from_spec(spec); spec.loader.exec_module(v)
orig = json.loads((SRC/'polynomial/receipts/degrees-2-16.json').read_bytes())['accepted_rows'][0]
def stub(cmd, **kw):
    if cmd[0] == 'g++': return None
    out = Path(cmd[cmd.index('--output')+1])
    out.write_text(json.dumps(dict(n=2, accepted=True, complete_partition=True, all_supplied_bounds_verified=True, certificate_sha256=orig['certificate_sha256'], counts=dict(bound=orig['bound_leaves'], corner=orig['corner_leaves'], splits=orig['splits']))))
v.subprocess.run = stub
m = v.load(d/'MANIFEST.json')
for label, root in (('C7b stub receipt with true counts vs tampered stored', d), ('C7c stub receipt with true counts vs unmodified stored', fresh('c7c'))):
    v.ROOT = root
    try: v.polynomial([2], v.load(root/'MANIFEST.json')); print(json.dumps(dict(control=label, result='PASS')))
    except Exception as e: print(json.dumps(dict(control=label, result='REJECT', error=repr(e))))
# C7d stub receipt with an extra counts key (format sensitivity)
v.ROOT = WORK/'c7c'
def stub2(cmd, **kw):
    if cmd[0] == 'g++': return None
    out = Path(cmd[cmd.index('--output')+1])
    out.write_text(json.dumps(dict(n=2, accepted=True, complete_partition=True, all_supplied_bounds_verified=True, certificate_sha256=orig['certificate_sha256'], counts=dict(bound=orig['bound_leaves'], corner=orig['corner_leaves'], splits=orig['splits'], extra=0))))
v.subprocess.run = stub2
try: v.polynomial([2], v.load(v.ROOT/'MANIFEST.json')); print(json.dumps(dict(control='C7d extra counts key', result='PASS')))
except Exception as e: print(json.dumps(dict(control='C7d extra counts key', result='REJECT', error=repr(e))))
# C8 -O refusal
d = WORK/'c0'; run(d, 'C8 python -O', extra=('-O',))
