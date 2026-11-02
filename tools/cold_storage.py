#!/usr/bin/env python3
"""Cold-storage manifests for large generated outputs.

Large, regenerable generated outputs are not kept at the branch head. Each topic
that moved files lists them in ``topics/<slug>/cold-storage.json`` (machine
manifest) and ``topics/<slug>/COLD_STORAGE.md`` (human manifest, templates/
COLD_STORAGE.md layout). Every entry pins the exact bytes by SHA-256 and by the
Git blob id at a pushed source commit, so the files stay retrievable from
repository history even before they are copied to AC's Padua cold storage.

Commands (run from the repository root; standard library only):

  plan    <path> [--threshold N]   list generated data files >= N bytes under <path>
  verify  <slug>                   check manifest entries against Git objects and the worktree
  restore <slug> [--dest DIR]      write the moved files back (default: their repository paths)
  clean   <slug>                   delete restored copies that still match the manifest
  export  <slug> --dest ROOT       copy files to ROOT/<slug>/<path> and write a receipt there

Typical replay of an old topic checker:

  python tools/cold_storage.py restore <slug>
  <run the topic's recorded checker command>
  python tools/cold_storage.py clean <slug>

Retrieval needs the source commit's objects locally (a full clone, or
``git fetch origin <source_commit>`` in a shallow clone).
"""
import argparse, hashlib, json, os, subprocess, sys, time
from pathlib import Path

# Extensions treated as records or code, never moved: written by hand, not generated.
RECORD_EXT = {'md', 'py', 'sh', 'tex', 'bib', 'svg', 'gitignore'}
# The cold-storage manifest itself always stays committed.
def is_manifest(path):
    return path.rsplit('/', 1)[-1].lower() == 'cold-storage.json'

ROOT = Path(__file__).resolve().parent.parent


def git(*args, binary=False):
    out = subprocess.run(['git', '-C', str(ROOT), *args], check=True, capture_output=True)
    return out.stdout if binary else out.stdout.decode()


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def manifest_path(slug):
    return ROOT / 'topics' / slug / 'cold-storage.json'


def load(slug):
    return json.loads(manifest_path(slug).read_text())


def blob_bytes(entry):
    data = git('cat-file', 'blob', entry['git_blob'], binary=True)
    if sha256(data) != entry['sha256'] or len(data) != entry['bytes']:
        raise SystemExit(f"hash/size mismatch for Git blob of {entry['path']}")
    return data


def cmd_plan(a):
    rows = []
    for rec in git('ls-tree', '-r', '-l', '-z', 'HEAD', '--', a.path, binary=True).split(b'\0'):
        if not rec:
            continue
        meta, path = rec.split(b'\t', 1)
        size, path = int(meta.split()[3]), path.decode()
        name = path.rsplit('/', 1)[-1]
        ext = name.rsplit('.', 1)[-1].lower() if '.' in name else ''
        if ext in RECORD_EXT or is_manifest(path) or size < a.threshold:
            continue
        rows.append({'path': path, 'bytes': size, 'git_blob': meta.split()[2].decode()})
    rows.sort(key=lambda r: r['path'])
    print(json.dumps({'threshold': a.threshold, 'files': len(rows),
                      'bytes': sum(r['bytes'] for r in rows), 'entries': rows}, indent=1))


def cmd_verify(a):
    m = load(a.slug)
    problems, present = [], 0
    for e in m['entries']:
        try:
            blob_bytes(e)
        except subprocess.CalledProcessError:
            problems.append(f"missing Git object {e['git_blob']} for {e['path']} (fetch {m['source_commit']})")
            continue
        except SystemExit as exc:
            problems.append(str(exc))
            continue
        tracked = git('ls-files', '--', e['path']).strip()
        if tracked:
            problems.append(f"still tracked at the branch head: {e['path']}")
        p = ROOT / e['path']
        if p.exists():
            present += 1
            if sha256(p.read_bytes()) != e['sha256']:
                problems.append(f"worktree copy differs from manifest: {e['path']}")
    result = {'slug': a.slug, 'entries': len(m['entries']), 'bytes': sum(e['bytes'] for e in m['entries']),
              'restored_copies_present': present, 'accepted': not problems, 'problems': problems}
    print(json.dumps(result, indent=1))
    sys.exit(0 if not problems else 1)


def write_entries(m, dest_root):
    written = []
    for e in m['entries']:
        data = blob_bytes(e)
        target = dest_root / e['path']
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        written.append({'path': e['path'], 'bytes': len(data), 'sha256': sha256(data)})
    return written


def cmd_restore(a):
    m = load(a.slug)
    dest = Path(a.dest) if a.dest else ROOT
    written = write_entries(m, dest)
    print(json.dumps({'slug': a.slug, 'restored': len(written), 'dest': str(dest)}, indent=1))


def cmd_clean(a):
    m = load(a.slug)
    removed = 0
    for e in m['entries']:
        p = ROOT / e['path']
        if p.exists() and not git('ls-files', '--', e['path']).strip() and sha256(p.read_bytes()) == e['sha256']:
            p.unlink()
            removed += 1
    print(json.dumps({'slug': a.slug, 'removed_restored_copies': removed}, indent=1))


def cmd_export(a):
    m = load(a.slug)
    dest = Path(a.dest) / a.slug
    written = write_entries(m, dest)
    receipt = {'slug': a.slug, 'source_commit': m['source_commit'], 'exported_at': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
               'files': written, 'bytes': sum(w['bytes'] for w in written), 'all_hashes_match_manifest': True}
    (dest / 'cold-storage-export-receipt.json').write_text(json.dumps(receipt, indent=1) + '\n')
    print(json.dumps({k: v for k, v in receipt.items() if k != 'files'}, indent=1))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='cmd', required=True)
    p = sub.add_parser('plan'); p.add_argument('path'); p.add_argument('--threshold', type=int, default=16384)
    for name in ('verify', 'restore', 'clean', 'export'):
        p = sub.add_parser(name); p.add_argument('slug')
        if name == 'restore':
            p.add_argument('--dest')
        if name == 'export':
            p.add_argument('--dest', required=True)
    a = ap.parse_args()
    {'plan': cmd_plan, 'verify': cmd_verify, 'restore': cmd_restore, 'clean': cmd_clean, 'export': cmd_export}[a.cmd](a)


if __name__ == '__main__':
    main()
