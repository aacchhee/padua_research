"""Audit-06 I1 (data-only): classify identity rows of the original return's sampled passes.
Usage: python3 -I -B ident6.py RETURN_TAR_GZ PADUA30_ZIP REPORT
Reads members into memory (tarfile/zipfile), parses JSON only; extracts and executes nothing."""
import json, sys, tarfile, zipfile
from collections import Counter
from pathlib import PurePosixPath as P

ret, pkg, report = sys.argv[1], sys.argv[2], sys.argv[3]
NAMES = ('raw-evidence.json', 'summary.json', 'final-accounting.json', 'preregistration.json', 'essential-receipt.json')


def identities(v):
    if isinstance(v, dict):
        if {'path', 'bytes', 'sha256'} <= set(v): yield {k: v[k] for k in ('path', 'bytes', 'sha256')}
        for c in v.values(): yield from identities(c)
    elif isinstance(v, list):
        for c in v: yield from identities(c)


with zipfile.ZipFile(pkg) as z:
    trusted = set(json.loads(z.read('padua30/runtime_manifest.json'))['files'])
docs = {}
with tarfile.open(ret, 'r:gz') as t:
    for m in t:
        if not m.isfile(): continue
        parts = m.name.split('/')
        if m.name == 'outputs/all/run.json' or (len(parts) == 6 and parts[2] == 'jobs' and parts[3] in ('199', '238')
                                                and parts[4] in ('produce', 'verify') and parts[5] in NAMES):
            docs[m.name] = json.loads(t.extractfile(m).read())
run = docs.pop('outputs/all/run.json')
root = P(run['package_root']) if 'package_root' in run else None
rows = []; cls = Counter(); other = set(); outside = set(); under_prefix = set()
for name, doc in sorted(docs.items()):
    for r in identities(doc):
        p = P(r['path'])
        if root is not None and p.is_relative_to(root):
            rel = p.relative_to(root).as_posix()
            if rel.startswith('outputs/all/'): k = 'under_output_prefix'; under_prefix.add(rel)
            elif rel in trusted: k = 'trusted_manifest'
            else: k = 'other_under_root'; other.add(rel)
        else:
            k = 'outside_root'; outside.add(r['sha256'])
        cls[k] += 1
out = {'run_keys': sorted(run)[:40], 'package_root': str(root), 'docs_read': sorted(docs), 'row_classes': dict(cls),
       'distinct_other_under_root': sorted(other), 'distinct_outside_root_sha': len(outside),
       'distinct_under_prefix': len(under_prefix), 'under_prefix_examples': sorted(under_prefix)[:12]}
open(report, 'x').write(json.dumps(out, indent=1) + '\n')
print(json.dumps({k: out[k] for k in ('package_root', 'row_classes', 'distinct_outside_root_sha', 'distinct_under_prefix')}))
print('other_under_root:', out['distinct_other_under_root'][:20])
