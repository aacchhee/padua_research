"""J3 audit: data-only extraction of essential-receipt JSON members from the pinned old return.
Reads regular members only, never extracts paths, never executes anything from the archive.
Usage: python3 -I extract.py ARCHIVE OUTDIR DEGREES(comma list)"""
import hashlib, json, re, sys, tarfile
from pathlib import Path
PIN = 'b00fd57f85ce6d96a6c1fa01e2307abd815088bb8fcb28b1587657ef142b109a'
src, outdir, degs = sys.argv[1], Path(sys.argv[2]), set(map(int, sys.argv[3].split(',')))
h = hashlib.sha256()
with open(src, 'rb') as f:
    for b in iter(lambda: f.read(1 << 20), b''): h.update(b)
assert h.hexdigest() == PIN, 'archive pin'
outdir.mkdir(parents=True, exist_ok=False)
rows = {}; inventory = set()
with tarfile.open(src, 'r:gz') as tf:
    for m in tf:
        mt = re.fullmatch(r'outputs/all/jobs/(\d+)/(produce|verify)/essential-receipt.json', m.name)
        if not mt: continue
        assert m.isfile() and 0 < m.size < 100000, ('unsafe member', m.name)
        key = (int(mt[1]), mt[2]); assert key not in inventory, 'duplicate'; inventory.add(key)
        if key[0] in degs:
            b = tf.extractfile(m).read(); d = json.loads(b); assert d['n'] == key[0]
            name = 'n%d-%s.json' % key; (outdir / name).write_bytes(b)
            rows[name] = {'member': m.name, 'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}
assert inventory == {(n, p) for n in [*range(41, 320), 511] for p in ('produce', 'verify')}, 'inventory'
assert len(rows) == 2 * len(degs), 'requested members'
print(json.dumps({'archive_sha256': PIN, 'inventory_pairs': len(inventory), 'extracted': rows}, indent=1, sort_keys=True))
