"""End-to-end storage safety controls in exclusively owned temporary repos.

No shared repository index/ref is changed. All data and commits are fixtures;
the test driver records a small summary on stdout, never over proof evidence.
"""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

TOOL = Path(__file__).with_name('cold_storage.py')


@unittest.skipUnless(os.name == 'posix', 'mutating safety backend requires POSIX')
class StorageControls(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='padua-storage-control-')
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.repo = self.base / 'repo'
        self.repo.mkdir()
        self.git('init', '-q')
        self.git('config', 'user.name', 'Storage Fixture')
        self.git('config', 'user.email', 'fixture@example.invalid')
        self.git('config', 'commit.gpgsign', 'false')
        self.git('config', 'core.autocrlf', 'false')
        self.tool = self.repo / 'tools/cold_storage.py'
        self.tool.parent.mkdir()
        shutil.copyfile(TOOL, self.tool)
        self.payloads = {
            'topics/demo/out/a.json': b'{"artifact":"a"}\n',
            'topics/demo/out/b.json': b'{"artifact":"b-longer"}\n',
            'topics/demo/evidence-manifest.json': b'{"historical":true}\n',
        }
        for name, data in self.payloads.items():
            p = self.repo / name
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(data)
        self.git('add', '--all')
        self.git('commit', '-qm', 'fixture source')
        self.source = self.git('rev-parse', 'HEAD').strip()
        entries = []
        for name, data in self.payloads.items():
            entry = {'path': name, 'bytes': len(data),
                     'sha256': hashlib.sha256(data).hexdigest(),
                     'git_blob': self.git('rev-parse', self.source + ':' + name).strip()}
            if name.endswith('evidence-manifest.json'):
                entry['worktree_role'] = 'historical-version'
            entries.append(entry)
            (self.repo / name).unlink()
        self.manifest = {'format': 'padua-cold-storage-v1', 'slug': 'demo',
                         'source_commit': self.source, 'entries': entries,
                         'total_bytes': sum(x['bytes'] for x in entries)}
        self.manifest_path = self.repo / 'topics/demo/cold-storage.json'
        self.save_manifest()
        self.active = self.repo / 'topics/demo/evidence-manifest.json'
        self.active.write_bytes(b'{"current":true}\n')
        self.git('add', '--all')
        self.git('commit', '-qm', 'fixture archive and active metadata')

    def git(self, *args):
        return subprocess.run(['git', '-C', str(self.repo), *args], check=True,
                              capture_output=True, text=True).stdout

    def save_manifest(self):
        self.manifest_path.write_text(json.dumps(self.manifest, indent=2) + '\n')

    def cli(self, *args, accepted=True):
        result = subprocess.run([sys.executable, '-B', str(self.tool), *map(str, args)],
                                cwd=self.repo, capture_output=True, text=True)
        if accepted:
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        else:
            self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        return result

    def put(self, root, name, data):
        p = root / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(data)
        return p

    def test_verify_active_version_and_directory_address(self):
        before = self.active.read_bytes()
        self.cli('verify', 'demo')
        self.cli('verify', 'topics/demo')
        self.assertEqual(self.active.read_bytes(), before)

    def test_restore_tracked_active_refuses_before_any_payload(self):
        before = self.active.read_bytes()
        self.cli('restore', 'demo', accepted=False)
        self.assertFalse((self.repo / 'topics/demo/out/a.json').exists())
        self.assertFalse((self.repo / 'topics/demo/out/b.json').exists())
        self.assertEqual(self.active.read_bytes(), before)

    def test_restore_verify_clean_scratch_roundtrip(self):
        dest = self.base / 'restored'
        self.cli('restore', 'demo', '--dest', dest)
        for name, data in self.payloads.items():
            self.assertEqual((dest / name).read_bytes(), data)
        before = {name: (dest / name).stat().st_mtime_ns for name in self.payloads}
        self.cli('restore', 'demo', '--dest', dest)
        self.assertEqual(before, {name: (dest / name).stat().st_mtime_ns for name in self.payloads})
        self.cli('verify', 'demo', '--dest', dest)
        keep = self.put(dest, 'unrelated.txt', b'keep')
        self.cli('clean', 'demo', '--dest', dest)
        self.assertTrue(all(not (dest / name).exists() for name in self.payloads))
        self.assertEqual(keep.read_bytes(), b'keep')
        self.cli('verify', 'demo', '--dest', dest)

    def test_restore_late_collision_preserves_existing_and_writes_nothing(self):
        dest = self.base / 'collision'
        conflict = self.put(dest, 'topics/demo/out/b.json', b'new user data')
        self.cli('restore', 'demo', '--dest', dest, accepted=False)
        self.assertEqual(conflict.read_bytes(), b'new user data')
        self.assertFalse((dest / 'topics/demo/out/a.json').exists())

    def test_export_is_idempotent(self):
        dest = self.base / 'export'
        self.cli('export', 'demo', '--dest', dest)
        root = dest / 'demo'
        receipt = root / 'cold-storage-export-receipt.json'
        before = receipt.read_bytes(), receipt.stat().st_mtime_ns
        self.cli('export', 'demo', '--dest', dest)
        self.assertEqual(before, (receipt.read_bytes(), receipt.stat().st_mtime_ns))
        for name, data in self.payloads.items():
            self.assertEqual((root / name).read_bytes(), data)

    def test_export_receipt_collision_preflights_before_payloads(self):
        dest = self.base / 'export-collision'
        receipt = self.put(dest / 'demo', 'cold-storage-export-receipt.json', b'keep receipt')
        self.cli('export', 'demo', '--dest', dest, accepted=False)
        self.assertEqual(receipt.read_bytes(), b'keep receipt')
        self.assertFalse((dest / 'demo/topics/demo/out/a.json').exists())

    def test_restore_rejects_parent_symlink(self):
        dest = self.base / 'parent-link'
        outside = self.base / 'outside'
        outside.mkdir()
        marker = self.put(outside, 'a.json', b'outside data')
        (dest / 'topics/demo').mkdir(parents=True)
        (dest / 'topics/demo/out').symlink_to(outside, target_is_directory=True)
        self.cli('restore', 'demo', '--dest', dest, accepted=False)
        self.assertEqual(marker.read_bytes(), b'outside data')
        self.assertFalse((outside / 'b.json').exists())

    def test_restore_rejects_final_symlink_even_when_matching(self):
        dest = self.base / 'final-link'
        outside = self.put(self.base, 'outside.json', self.payloads['topics/demo/out/a.json'])
        p = dest / 'topics/demo/out/a.json'
        p.parent.mkdir(parents=True)
        p.symlink_to(outside)
        before = outside.read_bytes(), outside.stat().st_mtime_ns
        self.cli('restore', 'demo', '--dest', dest, accepted=False)
        self.assertEqual(before, (outside.read_bytes(), outside.stat().st_mtime_ns))
        self.assertTrue(p.is_symlink())

    def test_clean_rejects_parent_symlink_and_preserves_outside(self):
        dest = self.base / 'clean-parent'
        outside = self.base / 'clean-outside'
        marker = self.put(outside, 'a.json', self.payloads['topics/demo/out/a.json'])
        (dest / 'topics/demo').mkdir(parents=True)
        (dest / 'topics/demo/out').symlink_to(outside, target_is_directory=True)
        self.cli('clean', 'demo', '--dest', dest, accepted=False)
        self.assertEqual(marker.read_bytes(), self.payloads['topics/demo/out/a.json'])

    def test_clean_late_final_symlink_refuses_before_any_deletion(self):
        dest = self.base / 'clean-final'
        first = self.put(dest, 'topics/demo/out/a.json', self.payloads['topics/demo/out/a.json'])
        outside = self.put(self.base, 'outside-b.json', self.payloads['topics/demo/out/b.json'])
        (dest / 'topics/demo/out/b.json').symlink_to(outside)
        self.cli('clean', 'demo', '--dest', dest, accepted=False)
        self.assertTrue(first.exists())
        self.assertEqual(outside.read_bytes(), self.payloads['topics/demo/out/b.json'])

    def test_clean_preserves_tracked_and_differing_files(self):
        first = self.put(self.repo, 'topics/demo/out/a.json', self.payloads['topics/demo/out/a.json'])
        second = self.put(self.repo, 'topics/demo/out/b.json', b'new local data')
        self.git('add', 'topics/demo/out/a.json')
        self.git('commit', '-qm', 'fixture tracked destination')
        active = self.active.read_bytes()
        self.cli('clean', 'demo')
        self.assertEqual(first.read_bytes(), self.payloads['topics/demo/out/a.json'])
        self.assertEqual(second.read_bytes(), b'new local data')
        self.assertEqual(self.active.read_bytes(), active)

    def test_verify_refuses_unexpected_tracked_payload(self):
        self.put(self.repo, 'topics/demo/out/a.json', self.payloads['topics/demo/out/a.json'])
        self.git('add', 'topics/demo/out/a.json')
        self.git('commit', '-qm', 'fixture unexpected tracked archive')
        self.cli('verify', 'demo', accepted=False)

    def test_clean_rejects_foreign_checkout_without_deleting_tracked_files(self):
        dest = self.base / 'foreign'
        self.cli('restore', 'demo', '--dest', dest)
        subprocess.run(['git', '-C', str(dest), 'init', '-q'], check=True)
        subprocess.run(['git', '-C', str(dest), 'add', '--all'], check=True)
        self.cli('clean', 'demo', '--dest', dest, accepted=False)
        for name, data in self.payloads.items():
            self.assertEqual((dest / name).read_bytes(), data)

    def test_restore_and_export_reject_foreign_checkout_ancestor(self):
        foreign = self.base / 'foreign-ancestor'
        foreign.mkdir()
        subprocess.run(['git', '-C', str(foreign), 'init', '-q'], check=True)
        dest = foreign / 'missing/subdir'
        self.cli('restore', 'demo', '--dest', dest, accepted=False)
        self.cli('export', 'demo', '--dest', dest, accepted=False)
        self.assertFalse(dest.exists())

    def test_nested_worktree_marker_preflights_before_writes_or_deletes(self):
        for marker_type in ('directory', 'file'):
            with self.subTest(marker_type=marker_type):
                dest = self.base / ('nested-' + marker_type)
                first = self.put(dest, 'topics/demo/out/a.json',
                                 self.payloads['topics/demo/out/a.json'])
                # The final historical manifest traverses demo; the marker
                # also guards earlier entries, before any operation occurs.
                marker = dest / 'topics/demo/.git'
                if marker_type == 'directory':
                    marker.mkdir()
                    (marker / 'HEAD').write_text('ref: refs/heads/fixture\n')
                else:
                    marker.write_text('gitdir: /unavailable/fixture\n')
                self.cli('clean', 'demo', '--dest', dest, accepted=False)
                self.assertEqual(first.read_bytes(), self.payloads['topics/demo/out/a.json'])
                self.cli('restore', 'demo', '--dest', dest, accepted=False)
                self.assertFalse((dest / 'topics/demo/out/b.json').exists())

    def test_manifest_paths_and_roles_are_validated(self):
        original = json.loads(json.dumps(self.manifest))
        for path in ('../escape.json', '/tmp/escape.json', 'C:/escape.json',
                     'topics/demo/../escape.json', 'topics\\demo\\escape.json', '.git/config'):
            with self.subTest(path=path):
                self.manifest = json.loads(json.dumps(original))
                self.manifest['entries'][0]['path'] = path
                self.save_manifest()
                self.cli('verify', 'demo', accepted=False)
        self.manifest = json.loads(json.dumps(original))
        self.manifest['entries'][0]['worktree_role'] = 'unknown'
        self.save_manifest()
        self.cli('verify', 'demo', accepted=False)

    def test_duplicate_entries_are_rejected(self):
        self.manifest['entries'].append(self.manifest['entries'][0].copy())
        self.manifest['total_bytes'] += self.manifest['entries'][0]['bytes']
        self.save_manifest()
        self.cli('restore', 'demo', '--dest', self.base / 'duplicate', accepted=False)
        self.assertFalse((self.base / 'duplicate/topics/demo/out/a.json').exists())

    def test_forged_source_association_is_rejected(self):
        first, second = self.manifest['entries'][:2]
        for key in ('git_blob', 'sha256', 'bytes'):
            first[key] = second[key]
        self.manifest['total_bytes'] = sum(e['bytes'] for e in self.manifest['entries'])
        self.save_manifest()
        result = self.cli('verify', 'demo', accepted=False)
        self.assertTrue('source' in (result.stdout + result.stderr).lower()
                        or 'blob' in (result.stdout + result.stderr).lower())

    def test_plan_threshold_and_metadata_names(self):
        self.put(self.repo, 'topics/demo/out/large.json', b'x' * 16384)
        self.put(self.repo, 'topics/demo/cold-storage-extra.json', b'x' * 16384)
        self.git('add', '--all')
        self.git('commit', '-qm', 'fixture size policy')
        result = json.loads(self.cli('plan', 'topics/demo', '--threshold', 16384).stdout)
        names = [e['path'] for e in result['entries']]
        self.assertIn('topics/demo/out/large.json', names)
        self.assertNotIn('topics/demo/cold-storage-extra.json', names)


if __name__ == '__main__':
    unittest.main(verbosity=2)
