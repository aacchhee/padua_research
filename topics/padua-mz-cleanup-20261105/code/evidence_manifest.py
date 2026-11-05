#!/usr/bin/env python3
"""Create/verify the small current development inventory (no bulk artifacts)."""
import argparse
import hashlib
import json
from pathlib import Path


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--write',action='store_true')
    args=ap.parse_args()
    topic=Path(__file__).resolve().parents[1]
    root=topic.parents[1]
    target=topic/'evidence-manifest.json'
    if args.write:
        # Handoff statuses and the work log change in the subsequent
        # orchestration commit. The immutable outputs below do not.
        files=[p for p in topic.rglob('*') if p.is_file()
               and '__pycache__' not in p.parts and 'handoffs' not in p.parts
               and p.name not in ['LOG.md','evidence-manifest.json']]
        files += [root/'results/padua-mz-cleanup-20261105.md',
                  root/'tracks/mz-constants/paper/manuscript.tex',
                  root/'tracks/mz-constants/paper/refs.bib',
                  root/'tracks/mz-constants/paper/README.md',
                  root/'topics/mz-constants/directions/M7/manuscript-record.md']
        rows=[[str(p.relative_to(root)),p.stat().st_size,digest(p)]
              for p in sorted(set(files))]
        out=dict(format='padua-mz-cleanup-small-inventory-v1',
            columns=['repository_path','bytes','sha256'],files=rows,
            bulk='Large witnesses/norms/vectors and raw runs are separately manifested in cold-storage.json. No delivery is claimed.',
            excludes='LOG and numbered handoffs are orchestration metadata; no scientific file is excluded on size grounds.')
        target.write_text(json.dumps(out,separators=(',',':'))+'\n')
    data=json.loads(target.read_text())
    for name,size,expected in data['files']:
        path=root/name
        if not path.is_file() or path.stat().st_size!=size or digest(path)!=expected:
            raise ValueError(f'inventory mismatch: {name}')
    # Scientific receipts must pin the actual producer/checker source.
    for receipt in (topic/'evidence').glob('witness-*.json'):
        r=json.loads(receipt.read_text())
        code=topic/'code'/('rigorous_witness.py' if 'producer' in receipt.name else 'independent_witness.py')
        if r['code_sha256']!=digest(code):
            raise ValueError(f'receipt source mismatch: {receipt}')
    print(f"Verified {len(data['files'])} small file identities and all witness source hashes")


if __name__=='__main__':main()
