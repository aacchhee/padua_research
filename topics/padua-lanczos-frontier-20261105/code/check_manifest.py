#!/usr/bin/env python3
"""Verify pinned file identities; no scientific computation."""
import hashlib,json
from pathlib import Path
root=Path(__file__).resolve().parents[3]
topic=Path(__file__).resolve().parents[1]
data=json.loads((topic/'evidence-manifest.json').read_text())
files=data['files']
if isinstance(files,dict):
    rows=[{'path':p,'bytes':v[0],'sha256':v[1]} for p,v in files.items()]
    for r in rows:
        p=r['path'];r['path']=str((root/p[1:]) if p.startswith('@') else topic/p)
else:
    rows=files
    for r in rows:r['path']=str(root/data.get('path_roots',{}).get(r.get('root'),'')/r['path'])
for row in rows:
    b=Path(row['path']).read_bytes()
    assert len(b)==row['bytes'],row['path']
    assert hashlib.sha256(b).hexdigest()==row['sha256'],row['path']
print(f"PASS: {len(rows)} pinned checkpoint files")
