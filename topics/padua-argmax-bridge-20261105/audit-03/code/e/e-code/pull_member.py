"""Copy named regular members (data only) from the untrusted tar into an output dir
under flat sanitized names; never extracts paths, never runs anything."""
import hashlib, sys, tarfile
from pathlib import Path, PurePosixPath
src, outdir, *names = sys.argv[1:]
outdir = Path(outdir); outdir.mkdir(parents=True, exist_ok=True)
want = set(names); got = {}
with tarfile.open(src, 'r|gz') as tar:
    for m in tar:
        if m.isfile(): got[m.name] = tar.extractfile(m).read() if m.name in want else None
        elif m.islnk() and m.name in want: got[m.name] = ('LINK', m.linkname)
for name in names:
    data = got.get(name)
    if isinstance(data, tuple):
        print(name, 'hardlink->', data[1]); continue
    if data is None: print(name, 'MISSING'); continue
    flat = name.replace('/', '__')
    (outdir / flat).write_bytes(data)
    print(name, len(data), hashlib.sha256(data).hexdigest(), '->', flat)
