#!/usr/bin/env python3
"""Verify the blocked-checkpoint inventory. No claim-level computation."""
import hashlib,json
from pathlib import Path
root=Path(__file__).resolve().parents[3]
topic=Path(__file__).resolve().parents[1]
data=json.loads((topic/'evidence-manifest.json').read_text())
for row in data['files']:
    b=(root/row['path']).read_bytes()
    assert len(b)==row['bytes'],row['path']
    assert hashlib.sha256(b).hexdigest()==row['sha256'],row['path']
print(f"PASS: {len(data['files'])} pinned checkpoint files")
