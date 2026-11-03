"""Independent re-audit fixtures; run from the candidate repository root."""
import contextlib, hashlib, importlib.util, io, json, os
from pathlib import Path
import shutil, subprocess, sys, tempfile, types

tool = Path.cwd() / 'tools/cold_storage.py'
spec = importlib.util.spec_from_file_location('audit_cs', tool)
cs = importlib.util.module_from_spec(spec); spec.loader.exec_module(cs)
results = {}

with tempfile.TemporaryDirectory(prefix='padua-audit02-faults-') as temp:
    base = Path(temp); repo = base / 'fixture'; repo.mkdir(); cs.ROOT = repo
    def git(*args):
        return subprocess.check_output(['git', '-C', str(repo), *args], stderr=subprocess.DEVNULL).decode().strip()
    git('init', '-q'); git('config', 'user.name', 'Audit fixture')
    git('config', 'user.email', 'audit@example.invalid'); git('config', 'commit.gpgsign', 'false')
    payloads = {'topics/demo/a.bin': b'A'*32, 'topics/demo/b.bin': b'B'*64}
    for name, data in payloads.items():
        p = repo / name; p.parent.mkdir(parents=True, exist_ok=True); p.write_bytes(data)
    git('add', '--all'); git('commit', '-qm', 'fixture source'); source = git('rev-parse', 'HEAD')
    entries = [{'path': p, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
                'git_blob': git('rev-parse', source+':'+p)} for p, data in payloads.items()]
    manifest = {'format': 'padua-cold-storage-v1', 'source_commit': source,
                'entries': entries, 'total_bytes': 96}
    mp = repo / 'topics/demo/cold-storage.json'; mp.write_text(json.dumps(manifest))
    for name in payloads: (repo/name).unlink()
    git('add', '--all'); git('commit', '-qm', 'fixture archive')
    def call(fn, expected=True, **kwargs):
        output = io.StringIO(); error = None
        try:
            with contextlib.redirect_stdout(output): fn(types.SimpleNamespace(**kwargs))
        except (Exception, SystemExit) as exc: error = type(exc).__name__+': '+str(exc)
        assert (error is None) == expected, (fn.__name__, output.getvalue(), error)
        return output.getvalue(), error
    def export(dest, expected=True):
        return call(cs.cmd_export, expected, slug='demo', dest=str(dest))
    def verify(root, expected=True, manifest_path=mp):
        return call(cs.cmd_verify_archive, expected, dir=str(root), manifest=str(manifest_path) if manifest_path else None)
    original_write = cs.SafeTree.write_new
    def corrupt_payload(tree, name, data):
        original_write(tree, name, data)
        if name.endswith('b.bin'):
            # The injected failure occurs after the tool's complete write.
            (tree.root / name).write_bytes(b'X' * len(data))
    cs.SafeTree.write_new = corrupt_payload
    damaged = base / 'damaged'; _, err = export(damaged, False)
    assert 'readback failed' in err and not (damaged/'demo'/cs.RECEIPT).exists()
    results['corruption_after_payload_write_rejected_without_receipt'] = True
    cs.SafeTree.write_new = original_write
    good = base / 'good'; export(good); archive = good/'demo'; verify(archive)
    receipt_bytes = (archive/cs.RECEIPT).read_bytes()
    (archive/'topics/demo/b.bin').unlink()
    cs.SafeTree.write_new = corrupt_payload
    export(good, False); cs.SafeTree.write_new = original_write
    assert (archive/cs.RECEIPT).read_bytes() == receipt_bytes
    verify(archive, False)
    results['stale_success_receipt_cannot_pass_current_verification_after_failed_reexport'] = True
    (archive/'topics/demo/b.bin').write_bytes(payloads['topics/demo/b.bin'])
    export(good); verify(archive)
    transferred = base / 'transferred'; shutil.copytree(archive, transferred)
    standalone = base / 'standalone/tools/cold_storage.py'; standalone.parent.mkdir(parents=True)
    shutil.copyfile(tool, standalone)
    def offline(root, expected=True, with_manifest=True):
        args = [sys.executable, '-B', str(standalone), 'verify-archive', str(root)]
        if with_manifest: args += ['--manifest', str(mp)]
        proc = subprocess.run(args, cwd=standalone.parent, env={**os.environ, 'GIT_DIR': str(base/'absent-git')}, capture_output=True, text=True)
        assert (proc.returncode == 0) == expected, proc.stdout+proc.stderr
        return proc.stdout
    offline(transferred); offline(transferred, with_manifest=False)
    results['transferred_archive_verifies_without_git'] = True
    target = transferred/'topics/demo/a.bin'; target.write_bytes(b'A')
    offline(transferred, False); target.write_bytes(payloads['topics/demo/a.bin'])
    results['transferred_truncated_payload_rejected'] = True
    target.unlink(); offline(transferred, False); target.write_bytes(payloads['topics/demo/a.bin'])
    results['transferred_missing_payload_rejected'] = True
    exact_manifest = mp.read_bytes(); mp.write_bytes(exact_manifest+b'\n')
    offline(transferred, False); mp.write_bytes(exact_manifest)
    results['semantically_equal_but_changed_manifest_bytes_rejected_v2'] = True
    v1 = json.loads(receipt_bytes); v1['format'] = 'padua-cold-storage-export-v1'
    v1.pop('manifest_sha256'); v1.pop('destination_readback_matched'); v1.pop('meaning')
    v1['all_hashes_match_manifest'] = True
    (transferred/cs.RECEIPT).write_text(json.dumps(v1))
    report = json.loads(offline(transferred)); assert 'without destination readback' in report['note']
    target.write_bytes(b'Z'*32); offline(transferred, False)
    results['v1_receipt_checked_currently_and_damage_rejected'] = True
    colliding = base/'collision'; p=colliding/'topics/demo/b.bin'; p.parent.mkdir(parents=True);p.write_bytes(b'new result')
    call(cs.cmd_restore, False, slug='demo', dest=str(colliding))
    assert not (colliding/'topics/demo/a.bin').exists() and p.read_bytes()==b'new result'
    results['late_collision_does_not_overwrite_or_partially_restore'] = True

report = {'candidate_tool_sha256': hashlib.sha256(tool.read_bytes()).hexdigest(),
          'controls': results, 'passed': all(results.values()), 'count': len(results)}
print(json.dumps(report, indent=2)); assert report['passed']
