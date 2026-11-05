#!/usr/bin/env python3
"""Inventory campaign sources and compact evidence; exclude mutable log/handoffs."""
import argparse,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parents[1]
MANIFEST=ROOT/'evidence-manifest.json'
def inventory():
    paths=[p for p in ROOT.rglob('*') if p.is_file() and p!=MANIFEST and p.name!='LOG.md' and 'handoffs' not in p.parts and '__pycache__' not in p.parts and p.suffix!='.pyc']
    paths.append(REPO/'results'/f'{ROOT.name}.md')
    return [{'path':str(p.relative_to(ROOT)) if p.is_relative_to(ROOT) else '../../'+str(p.relative_to(REPO)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(paths)]
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
    rows=inventory()
    if args.write:
        MANIFEST.write_text(json.dumps({'root':str(ROOT.relative_to(REPO)),'scope':'Sources, proofs, compact evidence and dedicated results; LOG and numbered handoffs excluded as mutable orchestration metadata. No bulk-output retention is established by this inventory.','files':rows},separators=(',',':'))+'\n')
        print(f'Wrote {len(rows)} identities')
    else:
        old=json.loads(MANIFEST.read_text())['files']
        if old!=rows:
            before={r['path']:r for r in old};after={r['path']:r for r in rows}
            changed=[p for p in sorted(before.keys()|after.keys()) if before.get(p)!=after.get(p)]
            raise SystemExit('Inventory differs: '+', '.join(changed))
        print(f'Verified {len(rows)} identities')
if __name__=='__main__':main()
