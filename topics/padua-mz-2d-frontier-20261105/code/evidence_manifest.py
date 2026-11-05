#!/usr/bin/env python3
"""Derived inventory (v2 compact tuples); reads the historical v1 row format."""
import argparse,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parents[1]
MANIFEST=ROOT/'evidence-manifest.json'
def inventory():
    paths=[p for p in ROOT.rglob('*') if p.is_file() and p!=MANIFEST and p.name!='LOG.md' and 'handoffs' not in p.parts and '__pycache__' not in p.parts and p.suffix!='.pyc']
    paths.append(REPO/'results'/f'{ROOT.name}.md')
    return [[str(p.relative_to(ROOT)) if p.is_relative_to(ROOT) else '../../'+str(p.relative_to(REPO)),p.stat().st_size,hashlib.sha256(p.read_bytes()).hexdigest()] for p in sorted(paths)]
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
    rows=inventory()
    if args.write:
        MANIFEST.write_text(json.dumps({'format':'padua-inventory-v2','root':str(ROOT.relative_to(REPO)),'columns':['path','bytes','sha256'],'scope':'Whole topic and dedicated results, excluding this manifest, mutable LOG, numbered handoffs and bytecode. Compact tuples avoid duplicated keys; no archival durability asserted. Original 84-entry audited v1 is retained at dee638408505c9977f3febd98fdd42c9bc512c92.','files':rows},separators=(',',':'))+'\n')
        print(f'Wrote {len(rows)} identities')
    else:
        old=json.loads(MANIFEST.read_text())['files']
        if old and isinstance(old[0],dict):old=[[x['path'],x['bytes'],x['sha256']] for x in old]
        if old!=rows:
            before={x[0]:x for x in old};after={x[0]:x for x in rows}
            raise SystemExit('Inventory differs: '+', '.join(p for p in sorted(before.keys()|after.keys()) if before.get(p)!=after.get(p)))
        print(f'Verified {len(rows)} identities')
if __name__=='__main__':main()
