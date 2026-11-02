import hashlib, json, os, shutil, subprocess, sys, tempfile
from pathlib import Path
TOOL = Path('/home/user/padua_research/tools/cold_storage.py')
BASE = Path(sys.argv[1]); results = []
def sh(*a, cwd=None, check=True):
    return subprocess.run(list(a), cwd=cwd, check=check, capture_output=True, text=True)
def h(b): return hashlib.sha256(b).hexdigest()
def mkrepo(name):
    repo = BASE / name
    if repo.exists(): shutil.rmtree(repo)
    repo.mkdir(parents=True)
    g = lambda *a: sh('git', '-C', str(repo), *a).stdout
    g('init', '-q'); g('config', 'user.name', 'F'); g('config', 'user.email', 'f@x.invalid'); g('config','commit.gpgsign','false')
    (repo/'tools').mkdir(); shutil.copyfile(TOOL, repo/'tools/cold_storage.py')
    pay = {'topics/demo/out/a.json': b'A\n', 'topics/demo/out/sub/b.json': b'BB\n', 'topics/demo/c.bin': b'CCC\n'}
    for n, d in pay.items():
        p = repo/n; p.parent.mkdir(parents=True, exist_ok=True); p.write_bytes(d)
    (repo/'topics/demo/other.json').write_bytes(b'OTHER\n')
    os.symlink('out/a.json', repo/'topics/demo/link.json')
    g('add', '-A'); g('commit', '-qm', 's'); src = g('rev-parse', 'HEAD').strip()
    ents = [{'path': n, 'bytes': len(d), 'sha256': h(d), 'git_blob': g('rev-parse', f'{src}:{n}').strip()} for n, d in pay.items()]
    for n in pay: (repo/n).unlink()
    m = {'format': 'padua-cold-storage-v1', 'slug': 'demo', 'source_commit': src, 'entries': ents, 'total_bytes': sum(e['bytes'] for e in ents)}
    (repo/'topics/demo/cold-storage.json').write_text(json.dumps(m))
    g('add', '-A'); g('commit', '-qm', 'arch')
    return repo, m, pay, g
def cli(repo, *a):
    r = subprocess.run([sys.executable, '-B', str(repo/'tools/cold_storage.py'), *map(str, a)], cwd=repo, capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr).strip().splitlines()[-1] if (r.stdout + r.stderr).strip() else ''
def rec(name, ok, detail=''):
    results.append((name, ok, detail)); print(('PASS' if ok else 'FAIL'), name, '|', detail)
def snap(root):
    return {str(p.relative_to(root)): (p.read_bytes() if p.is_file() and not p.is_symlink() else 'L') for p in root.rglob('*') if (p.is_file() or p.is_symlink()) and '.git' not in p.parts}

# 1 restore -> git init + add at dest -> clean refuses, nothing deleted
repo, m, pay, g = mkrepo('r1'); d = BASE/'d1'; shutil.rmtree(d, ignore_errors=True)
rc, _ = cli(repo, 'restore', 'demo', '--dest', d); assert rc == 0
sh('git', 'init', '-q', str(d)); sh('git', '-C', str(d), 'add', '-A')
before = snap(d); rc, out = cli(repo, 'clean', 'demo', '--dest', d)
rec('1 foreign init+add at dest -> clean refuses', rc != 0 and snap(d) == before and len(before) == 3, out)
rc, out = cli(repo, 'verify', 'demo', '--dest', d); rec('1b verify of foreign-repo dest still read-only accepted', rc == 0, out)
# 1c foreign init (no add, only HEAD/config) -> clean refuses too (nonempty .git)
d = BASE/'d1c'; shutil.rmtree(d, ignore_errors=True); cli(repo, 'restore', 'demo', '--dest', d); sh('git', 'init', '-q', str(d)); b = snap(d)
rc, out = cli(repo, 'clean', 'demo', '--dest', d); rec('1c foreign init (unstaged) -> clean refuses', rc != 0 and snap(d) == b, out)
# 2 nested foreign repo at payload parent dir (dest/topics/demo/out) after restore
d = BASE/'d2'; shutil.rmtree(d, ignore_errors=True); cli(repo, 'restore', 'demo', '--dest', d)
sh('git', 'init', '-q', str(d/'topics/demo/out/sub')); b = snap(d)
rc, out = cli(repo, 'clean', 'demo', '--dest', d); rec('2 nested deep .git dir at payload parent -> clean refuses, zero deletions (preflight)', rc != 0 and snap(d) == b, out)
# 3 .git FILE at ancestor of dest
anc = BASE/'anc3'; shutil.rmtree(anc, ignore_errors=True); anc.mkdir(); (anc/'.git').write_text('gitdir: /nowhere\n')
rc, out = cli(repo, 'restore', 'demo', '--dest', anc/'x/y'); rec('3 .git file at ancestor -> restore refuses, no dir created', rc != 0 and not (anc/'x').exists(), out)
rc, out = cli(repo, 'export', 'demo', '--dest', anc); rec('3b export under .git-file ancestor refuses', rc != 0 and not (anc/'demo').exists(), out)
# 4 .git symlink nested inside dest (payload parent) before restore
d = BASE/'d4'; shutil.rmtree(d, ignore_errors=True); (d/'topics/demo').mkdir(parents=True); os.symlink('/nonexistent', d/'topics/demo/.git')
rc, out = cli(repo, 'restore', 'demo', '--dest', d); rec('4 nested .git symlink -> restore refuses, no payload', rc != 0 and not (d/'topics/demo/c.bin').exists() and not (d/'topics/demo/out').exists(), out)
# 4b dangling .git symlink at dest root -> clean refuses
d = BASE/'d4b'; shutil.rmtree(d, ignore_errors=True); cli(repo, 'restore', 'demo', '--dest', d); os.symlink(str(repo/'.git'), d/'.git'); b = snap(d)
rc, out = cli(repo, 'clean', 'demo', '--dest', d); rec('4b .git symlink to source .git at dest -> clean refuses', rc != 0 and snap(d) == b, out)
# 5 empty .git dir ignored
d = BASE/'d5'; shutil.rmtree(d, ignore_errors=True); (d/'topics').mkdir(parents=True); (d/'topics/.git').mkdir()
rc, out = cli(repo, 'restore', 'demo', '--dest', d); rc2, out2 = cli(repo, 'clean', 'demo', '--dest', d)
rec('5 empty .git dir ignored (restore+clean ok)', rc == 0 and rc2 == 0 and not (d/'topics/demo/c.bin').exists(), out2)
# 6 export nesting: export twice, then export into a dest that is inside the first export; export into source repo untracked area
e = BASE/'e6'; shutil.rmtree(e, ignore_errors=True)
rc, _ = cli(repo, 'export', 'demo', '--dest', e); r1 = (e/'demo/cold-storage-export-receipt.json').read_bytes()
rc2, _ = cli(repo, 'export', 'demo', '--dest', e); rec('6a export idempotent receipt', rc == 0 and rc2 == 0 and r1 == (e/'demo/cold-storage-export-receipt.json').read_bytes())
rc, out = cli(repo, 'export', 'demo', '--dest', e/'demo'); rec('6b nested export inside prior export dir -> ok (non-git)', rc == 0 and (e/'demo/demo/topics/demo/c.bin').exists(), out)
sh('git', 'init', '-q', str(e)); rc, out = cli(repo, 'export', 'demo', '--dest', e/'demo'/'n2'); rec('6c export below foreign repo -> refuse', rc != 0 and not (e/'demo/n2').exists(), out)
rc, out = cli(repo, 'export', 'demo', '--dest', repo/'scratch-exp'); exists = (repo/'scratch-exp/demo/c.bin').exists() or (repo/'scratch-exp/demo/topics/demo/c.bin').exists()
rec('6d export into source repo untracked subdir (allowed; not tracked)', rc == 0 and exists, out); shutil.rmtree(repo/'scratch-exp', ignore_errors=True)
# 6e export --dest such that DEST/demo maps onto tracked source path topics -> tracked collision
rc, out = cli(repo, 'export', 'demo', '--dest', repo/'topics'); rec('6e export --dest repo/topics (DEST/demo == tracked topics/demo prefix) -> refuse', rc != 0, out)
# 7 receipt collision: differing receipt present -> refuse before payload writes
e = BASE/'e7'; shutil.rmtree(e, ignore_errors=True); (e/'demo').mkdir(parents=True); (e/'demo/cold-storage-export-receipt.json').write_text('{"stale":1}')
rc, out = cli(repo, 'export', 'demo', '--dest', e); rec('7 stale differing receipt -> refuse, no payload', rc != 0 and not (e/'demo/topics').exists(), out)
# 7b matching receipt but payload deleted/tampered: export detects differing payload
e = BASE/'e7b'; shutil.rmtree(e, ignore_errors=True); cli(repo, 'export', 'demo', '--dest', e); (e/'demo/topics/demo/c.bin').write_bytes(b'tamper')
rc, out = cli(repo, 'export', 'demo', '--dest', e); rc2, out2 = cli(repo, 'verify', 'demo', '--dest', e/'demo')
rec('7b tampered export: re-export refuses and verify rejects', rc != 0 and rc2 != 0 and (e/'demo/topics/demo/c.bin').read_bytes() == b'tamper', out2)
# 8 root symlink / ancestor symlink in dest path
os.makedirs(BASE/'real8', exist_ok=True); 
if not (BASE/'lnk8').exists(): os.symlink(BASE/'real8', BASE/'lnk8')
rc, out = cli(repo, 'restore', 'demo', '--dest', BASE/'lnk8'); rc2, out2 = cli(repo, 'restore', 'demo', '--dest', BASE/'lnk8/sub')
rec('8 dest root symlink and symlinked ancestor -> refuse', rc != 0 and rc2 != 0 and not any((BASE/'real8').iterdir()), out2)
# 9 source forgeries / malformed
def mut(f, label, cmd='verify'):
    mm = json.loads(json.dumps(m)); f(mm); (repo/'topics/demo/cold-storage.json').write_text(json.dumps(mm) if not isinstance(mm, str) else mm)
    rc, out = cli(repo, cmd, 'demo', '--dest', BASE/'d9'); rec('9 '+label, rc != 0 and not (BASE/'d9').exists(), out)
tree = g('rev-parse', m['source_commit'] + '^{tree}').strip()
mut(lambda x: x.update(source_commit='0'*40), 'zero source commit')
mut(lambda x: x.update(source_commit=tree), 'source_commit is a tree', 'restore')
mut(lambda x: x.update(source_commit=x['source_commit'].upper()), 'uppercase source sha')
def swap(x): x['entries'][0]['path'] = 'topics/demo/other.json'
mut(swap, 'path/blob mismatch (blob exists at other path)', 'restore')
def symlinkentry(x):
    blob = g('rev-parse', m['source_commit']+':topics/demo/link.json').strip(); d = b'out/a.json'
    x['entries'].append({'path': 'topics/demo/link.json', 'bytes': len(d), 'sha256': h(d), 'git_blob': blob}); x['total_bytes'] += len(d)
mut(symlinkentry, 'symlink (mode 120000) source entry', 'restore')
mut(lambda x: x['entries'][0].update(bytes=True), 'bool bytes')
mut(lambda x: x['entries'][0].update(path='topics/demo/../x'), 'dotdot path', 'restore')
mut(lambda x: x['entries'].append(dict(x['entries'][0], path=x['entries'][0]['path'].upper())), 'casefold dup', 'restore')
mut(lambda x: x['entries'][1].update(path='topics/demo/out/a.json/b'), 'file/dir prefix collision', 'restore')
mut(lambda x: x.update(total_bytes=1), 'total mismatch')
mut(lambda x: x['entries'][0].update(worktree_role='active'), 'unknown role')
mut(lambda x: x['entries'][0].update(path='/abs/x'), 'absolute path', 'restore')
(repo/'topics/demo/cold-storage.json').write_text('{"format":"padua-cold-storage-v1","format":"x"}'); rc,out=cli(repo,'verify','demo'); rec('9 duplicate JSON key', rc!=0, out)
(repo/'topics/demo/cold-storage.json').write_text(json.dumps(m))
# 10 indexed-but-absent destination in source + differing untracked preservation
g('checkout', '--', '.') ; rc, out = cli(repo, 'restore', 'demo'); rec('10a in-place restore into source (untracked, absent) ok', rc == 0, out)
(repo/'topics/demo/c.bin').write_bytes(b'LOCAL-REGEN\n'); rc, out = cli(repo, 'clean', 'demo')
rec('10b clean in source preserves differing local file, removes matching', rc == 0 and (repo/'topics/demo/c.bin').read_bytes() == b'LOCAL-REGEN\n' and not (repo/'topics/demo/out/a.json').exists(), out)
rc, out = cli(repo, 'restore', 'demo'); rec('10c restore refuses differing file and writes nothing', rc != 0 and not (repo/'topics/demo/out/a.json').exists(), out)
(repo/'topics/demo/c.bin').unlink(); cli(repo,'restore','demo'); g('add', 'topics/demo/out/a.json'); (repo/'topics/demo/out/a.json').unlink()
rc, out = cli(repo, 'restore', 'demo'); rec('10d indexed-but-absent path -> restore refuses', rc != 0 and not (repo/'topics/demo/out/a.json').exists(), out)
g('reset', '-q'); cli(repo, 'clean', 'demo')
# 11 FIFO at dest
d = BASE/'d11'; shutil.rmtree(d, ignore_errors=True); (d/'topics/demo').mkdir(parents=True); os.mkfifo(d/'topics/demo/c.bin')
rc, out = cli(repo, 'restore', 'demo', '--dest', d); rec('11 FIFO destination refused (no hang)', rc != 0 and not (d/'topics/demo/out').exists(), out)
# 12 dest inside source .git refused; dest inside nested foreign repo inside source refused
rc, out = cli(repo, 'restore', 'demo', '--dest', repo/'.git/x'); rec('12a dest inside .git refused', rc != 0 and not (repo/'.git/x').exists(), out)
sh('git', 'init', '-q', str(repo/'nested')); rc, out = cli(repo, 'restore', 'demo', '--dest', repo/'nested/d'); rec('12b dest in nested repo inside source refused', rc != 0 and not (repo/'nested/d').exists(), out)
# 13 case: interior hardlink of an outside file in dest; clean unlinks only dest name
d = BASE/'d13'; shutil.rmtree(d, ignore_errors=True); cli(repo, 'restore', 'demo', '--dest', d); outside = BASE/'outside13.bin'; outside.write_bytes(b'CCC\n')
(d/'topics/demo/c.bin').unlink(); os.link(outside, d/'topics/demo/c.bin'); rc, out = cli(repo, 'clean', 'demo', '--dest', d)
rec('13 hardlink: clean unlinks dest name only; outside file intact', rc == 0 and outside.read_bytes() == b'CCC\n', out)
print(json.dumps({'passed': sum(r[1] for r in results), 'total': len(results)}))
