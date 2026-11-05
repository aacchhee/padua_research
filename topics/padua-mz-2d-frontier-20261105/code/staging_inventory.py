#!/usr/bin/env python3
"""Describe actual regenerable scratch staging; never asserts archive delivery."""
import hashlib,json,shlex,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parents[1]
paths=[Path('/tmp/padua-g0')/s for s in ('exact.json','spectra.json','independent.json')]
paths += [Path('/tmp/g1-frontier')/s for s in ('validation.json','scaling.json','localization.json','screen.json','minimum-only.json','carrier.json','corner-trial.json','fejer.json','minimum-only-vectors/m1600-n1599-min.npy')]
rows=[]
for p in paths:
    if not p.is_file():continue
    sha=hashlib.sha256()
    with p.open('rb') as f:
        for block in iter(lambda:f.read(1048576),b''):sha.update(block)
    command=None
    if p.suffix=='.json':
        d=json.loads(p.read_text());command=d.get('command',d.get('argv'))
    rows.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha.hexdigest(),'generating_command':command,'retention':'ephemeral local staging, regenerable; no external delivery or durable retrieval established'})
manifest={'format':'padua-cold-storage-v1','slug':ROOT.name,'source_commit':subprocess.check_output(['git','rev-parse','f745e6d'],cwd=REPO,text=True).strip(),'entries':[],'total_bytes':0,
 'policy':'AC: do not store large regenerable outputs. No bulk output was committed or exported. Empty entries means tools/cold_storage.py has no Git-backed payload to retrieve. Scratch inventory is distinct and not an archive.',
 'destination':'Downloads\\padua\\cold_storage\\padua-mz-2d-frontier-20261105\\','delivery':'PENDING; no access to AC destination or archival receipt',
 'local_staging':rows,'regeneration_records':['numerical-results.md','independent-checks-g0.md','certifier-results.md','independent-checks-cert.md'],'native_bulk':'Pencil/transform identities and commands are in cert-m60/m80 and independent-cert receipts. Some contiguous-batch bulk was pruned after checks and is regenerable; it is not listed as present staging.'}
(ROOT/'cold-storage.json').write_text(json.dumps(manifest,separators=(',',':'))+'\n')
print('Inventoried',len(rows),'present staged files;',sum(r['bytes'] for r in rows),'bytes; external delivery pending')
