#!/usr/bin/env python3
"""Stage and finalize the per-paper Zenodo evidence packs for MZ-CC and MZ-SP.

  stage     python tools/zenodo_pack.py stage --pack mz-cc|mz-sp --rev REV --data DATA --out OUT
  finalize  python tools/zenodo_pack.py finalize --dir OUT/<pack-name>

`stage` writes OUT/<pack-name>/ with
  repository/   `git archive REV` of the repository paths the paper's statement names,
                together with every file those programs read or hash;
  data/         files that are not in Git (DATA must hold them, see DATA_FILES);
  tools/        compare_receipts.py;
  verify.sh, requirements.txt, README.md (template with the commit filled in).
`finalize` writes MANIFEST-SHA256.txt (all files except itself) and a
deterministic <pack-name>.tar.gz (sorted members, fixed mtime/owner, gzip -n)
next to the directory, then prints its size and SHA-256.

Run from the repository root. Only the orchestrator runs it; it changes no Git state.
"""
import argparse, gzip, hashlib, io, os, shutil, subprocess, sys, tarfile
from pathlib import Path

TOPIC = Path('topics/padua-mz-paper-20261113')
ZEN = TOPIC / 'zenodo'

REPO_PATHS = {
    'mz-cc': [
        'topics/padua-mz-sharp-constants-20261106',
        'topics/mz-constants/sources/padua_mz_inputs',
        'tracks/mz-constants/code',
        'tracks/mz-constants/evidence',
        'tracks/mz-constants/paper',
    ],
    'mz-sp': [
        'topics/padua-mz-cleanup-20261105',
        'topics/padua-mz-2d-frontier-20261105',
        'topics/padua-mz-sharp-constants-20261106',
        'topics/padua-mz-2d-20261101',
        'topics/mz-constants/sources/padua_mz_inputs',
        'tracks/mz-constants/code',
        'tracks/mz-constants/evidence',
        'tracks/mz-constants/paper-sp',
    ],
}
# pack-relative destination  <-  path relative to DATA
DATA_FILES = {
    'mz-cc': {
        'data/table1/reproduction.json': 'table1/reproduction.json',
        'data/table1/reproduction-historical-2b52b432.json': 'table1/reproduction-historical-2b52b432.json',
        'data/protocol-history/attempts-P4-d03e74dc.md': 'protocol-history/attempts-P4-d03e74dc.md',
    },
    'mz-sp': {
        **{f'data/witnesses/cert-m{m}/{f}': f'witnesses/cert-m{m}/{f}'
           for m in (1101, 1240, 1600) for f in ('witness.json.gz', 'exact-norm.txt')},
        'data/witnesses/PAYLOAD-SHA256.txt': 'witnesses/PAYLOAD-SHA256.txt',
        **{f'data/source-vectors/m{m}-n{m-1}-min.npy': f'source-vectors/m{m}-n{m-1}-min.npy'
           for m in (1101, 1240, 1600)},
        **{f'data/regeneration-receipts/{f}': f'regeneration-receipts/{f}'
           for f in ('scan-m1101.json', 'scan-m1240-1600.json',
                     'producer-m1101.json', 'producer-m1240.json', 'producer-m1600.json',
                     'independent-m1101.json', 'independent-m1240.json', 'independent-m1600.json')},
        'data/measurements/reproduction-padua.json': 'measurements/reproduction-padua.json',
        'data/measurements/reproduction-marginal.json': 'measurements/reproduction-marginal.json',
        'data/protocol-history/ideas-P1-numeric-protocol-c1e6e59d.md': 'protocol-history/ideas-P1-numeric-protocol-c1e6e59d.md',
        'data/protocol-history/theory-P1-rectangle-certificate-c1e6e59d.md': 'protocol-history/theory-P1-rectangle-certificate-c1e6e59d.md',
    },
}
NAME = {'mz-cc': 'padua-mz-cc-evidence', 'mz-sp': 'padua-mz-sp-evidence'}


def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def stage(a):
    rev = subprocess.run(['git', 'rev-parse', a.rev], check=True, capture_output=True, text=True).stdout.strip()
    root = Path(a.out) / NAME[a.pack]
    if root.exists():
        shutil.rmtree(root)
    (root / 'repository').mkdir(parents=True)
    tar = subprocess.run(['git', 'archive', '--format=tar', rev, *REPO_PATHS[a.pack]], check=True, capture_output=True).stdout
    with tarfile.open(fileobj=io.BytesIO(tar)) as t:
        t.extractall(root / 'repository', filter='data')
    for dst, src in DATA_FILES[a.pack].items():
        s = Path(a.data) / src
        if not s.is_file():
            sys.exit(f'missing data file {s}')
        (root / dst).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(s, root / dst)
    (root / 'tools').mkdir()
    shutil.copyfile(ZEN / 'compare_receipts.py', root / 'tools/compare_receipts.py')
    shutil.copyfile(ZEN / f'verify-{a.pack}.sh', root / 'verify.sh')
    shutil.copyfile(ZEN / 'requirements.txt', root / 'requirements.txt')
    readme = (ZEN / f'README-{a.pack}.md').read_text().replace('{COMMIT}', rev)
    (root / 'README.md').write_text(readme)
    print(root, rev)


def finalize(a):
    root = Path(a.dir).resolve()
    files = sorted(p for p in root.rglob('*') if p.is_file() and p.name != 'MANIFEST-SHA256.txt')
    lines = [f'{sha(p)}  {p.relative_to(root).as_posix()}' for p in files]
    (root / 'MANIFEST-SHA256.txt').write_text('\n'.join(lines) + '\n')
    out = root.parent / f'{root.name}.tar.gz'
    members = sorted([root] + [p for p in root.rglob('*')], key=lambda p: p.relative_to(root.parent).as_posix())
    raw = io.BytesIO()
    with tarfile.open(fileobj=raw, mode='w', format=tarfile.PAX_FORMAT) as t:
        for p in members:
            ti = t.gettarinfo(str(p), arcname=p.relative_to(root.parent).as_posix())
            ti.mtime = 1794614400  # 2026-11-14T00:00:00Z, fixed
            ti.uid = ti.gid = 0
            ti.uname = ti.gname = ''
            ti.mode = 0o755 if (p.is_dir() or p.suffix == '.sh') else 0o644
            if p.is_file():
                with open(p, 'rb') as f:
                    t.addfile(ti, f)
            else:
                t.addfile(ti)
    with open(out, 'wb') as f, gzip.GzipFile(fileobj=f, mode='wb', mtime=0, filename='') as g:
        g.write(raw.getvalue())
    print(out, out.stat().st_size, sha(out), f'{len(files) + 1} files')


def main():
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest='cmd', required=True)
    s = sp.add_parser('stage'); s.add_argument('--pack', choices=list(NAME), required=True)
    s.add_argument('--rev', default='HEAD'); s.add_argument('--data', required=True); s.add_argument('--out', required=True)
    f = sp.add_parser('finalize'); f.add_argument('--dir', required=True)
    a = ap.parse_args()
    stage(a) if a.cmd == 'stage' else finalize(a)


if __name__ == '__main__':
    main()
