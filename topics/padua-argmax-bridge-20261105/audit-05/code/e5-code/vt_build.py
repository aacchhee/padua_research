"""R12 transport part: build mutated tar.gz copies of the OLD return (data only; never extracted to disk).
Usage: python3 -I -S -B vt_build.py TREE RETURN OUTDIR"""
import io, json, sys, tarfile
from pathlib import Path

tree, ret, outdir = Path(sys.argv[1]), sys.argv[2], Path(sys.argv[3])
sys.path.insert(0, str(tree / 'topics/padua-argmax-bridge-20261105/compact_pack'))
from common import digest, encoded
outdir.mkdir(parents=True, exist_ok=False)
members = []  # (TarInfo, bytes or None)
with tarfile.open(ret, 'r|gz') as t:
    for m in t:
        members.append((m, t.extractfile(m).read() if m.isfile() else None))
BIG = 'preserved-sha256/840b332fb62ec6f694ac77d91fe69ef7f80b0d69512ed89374af0ee7a506255d'
big = next(m for m, _ in members if m.name == BIG)
if big.size != 32675168:
    raise SystemExit('unexpected big member')


def link(name, target, kind=tarfile.LNKTYPE):
    i = tarfile.TarInfo(name); i.type = kind; i.linkname = target; i.size = 0; i.mtime = 0; return (i, None)


def write(label, rows):
    path = outdir / (label + '.tar.gz')
    with tarfile.open(path, 'x:gz', format=tarfile.PAX_FORMAT) as out:
        for info, data in rows:
            out.addfile(info, io.BytesIO(data) if data is not None else None)
    return path


def reinventory(rows, extra):
    rows = list(rows)
    for k, (info, data) in enumerate(rows):
        if info.name == 'COMPACT.json':
            rec = json.loads(data)
            for name, d in extra.items():
                rec['files'][name] = {'bytes': len(d), 'sha256': digest(d)}
            new = encoded(rec); ni = tarfile.TarInfo('COMPACT.json'); ni.size = len(new); ni.mtime = info.mtime
            rows[k] = (ni, new)
    return rows


made = {}
made['VT-1'] = write('VT-1-alias-uninventoried', members + [link('alias.bin', BIG)])
made['VT-2'] = write('VT-2-alias-before-target', [link('alias.bin', BIG)] + members)
made['VT-3'] = write('VT-3-symlink', members[:5] + [link('evil', '/etc/passwd', tarfile.SYMTYPE)] + members[5:])
d = tarfile.TarInfo('outputs/extra-dir'); d.type = tarfile.DIRTYPE; d.mtime = 0
made['VT-4'] = write('VT-4-directory', members[:5] + [(d, None)] + members[5:])
made['VT-5'] = write('VT-5-800-aliases', members + [link('alias-%04d.bin' % k, BIG) for k in range(800)])
job = b'{}'
ji = tarfile.TarInfo('outputs/all/jobs/999/attempt.json'); ji.size = len(job); ji.mtime = 0
made['VT-6'] = write('VT-6-job999', reinventory(members, {'outputs/all/jobs/999/attempt.json': job}) + [(ji, job)])
report = {k: {'path': str(p), 'bytes': p.stat().st_size, 'sha256': digest(p.read_bytes())} for k, p in made.items()}
report['_source_members'] = len(members)
(outdir / 'vt-build.json').write_text(json.dumps(report, indent=1) + '\n'); print(json.dumps(report))
