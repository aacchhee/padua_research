# Cold-storage manifest — mz-constants reproduction

Status: **locally staged only** in this Padua workspace. No delivery to Windows cold storage or durable remote storage is claimed. These are the actual existing files, not a historical receipt. The reproduction worker is Codex `gpt-6.1-sol`, medium (explicit orchestration assignment).

| File | Actual storage path | Bytes | SHA-256 | Source base | Frozen generating command | Script content identity | Checker result |
|---|---|---:|---|---|---|---|---|
| Reproduction JSON | `/workspace/padua_research/tracks/mz-constants/evidence/reproduction.json` | 29202 | `b85b06fa9b3317d6ce84f9d354626b74edad4e8f9885341ecad39166d4fd6d40` | `d36722823441dc40c6e19d69a174459348dd309c` | Command R below | Runner SHA256 `fe88a16d2ac08df96dc5e18a224ac1b0d46d5cec4310cc86fff0f7fda1aa44ac` | SHA256 and size matched; embedded runner hash matched current code |
| Reproduction manifest | `/workspace/padua_research/tracks/mz-constants/evidence/reproduction-manifest.json` | 1521 | `740a7afb0167b44f2206c5050ce9b88b87e08bc59daf06c7a58e84810a36867f` | `d36722823441dc40c6e19d69a174459348dd309c` | Command M below | Administrative inline Python; source below; numerical producer identified by runner SHA256 above | SHA256 and size matched; all four referenced artifact identities matched |

Source base is the rule/input starting revision, **not** a claim that the newly developed runner already existed at that commit. The runner's SHA256 pins its actual bytes; no Git blob ID is claimed by this worker. The input bundle manifest SHA256 is `c12ee67df3efc0a17791930da47332e6f7e8532f2006938a3608a6fd93ada19b`; all 21 listed files were checked against it.

## Frozen commands

Command R, from `/workspace/padua_research`:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python tracks/mz-constants/code/reproduce.py --suite all --max-N 1280 --output tracks/mz-constants/evidence/reproduction.json
```

The actual run redirected console output to `local-output/mz-constants/reproduction-console.txt`. Re-execution creates new UTC timestamps and elapsed times; it is expected to change the JSON hash. Preserve the archived JSON if byte-for-byte retrieval is required.

Command M is the actual administrative manifest refresh after the two prose model-provenance corrections; it did not rerun numerical code:

```sh
python - <<'PY'
import hashlib,json
from pathlib import Path
p=Path('tracks/mz-constants/evidence/reproduction-manifest.json')
m=json.loads(p.read_text())
for a in m['artifacts']:
    q=Path(a['path'])
    a['sha256']=hashlib.sha256(q.read_bytes()).hexdigest()
    a['bytes']=q.stat().st_size
p.write_text(json.dumps(m,indent=2)+'\n')
PY
```

The original manifest was assembled with Python `hashlib` and `json` from the four artifact paths, the bundle manifest, and the exact command R; its complete content is in the staged file. Command M reproduces the final refresh from that manifest. It does not recreate a missing manifest without its prior content.

## Committed checker output

This worker does not perform Git operations; commitment is the orchestrator's step. The following checker was actually executed against the staged bytes on 2026-10-31 and printed `PASS: two staged files, all manifest artifacts, embedded runner identity`. Its result is recorded here for commitment with the manifest:

```sh
python - <<'PY'
import hashlib,json
from pathlib import Path
expected={
 'tracks/mz-constants/evidence/reproduction.json':(29202,'b85b06fa9b3317d6ce84f9d354626b74edad4e8f9885341ecad39166d4fd6d40'),
 'tracks/mz-constants/evidence/reproduction-manifest.json':(1521,'740a7afb0167b44f2206c5050ce9b88b87e08bc59daf06c7a58e84810a36867f')}
for n,(size,h) in expected.items():
    p=Path(n)
    assert p.stat().st_size==size and hashlib.sha256(p.read_bytes()).hexdigest()==h,n
m=json.loads(Path('tracks/mz-constants/evidence/reproduction-manifest.json').read_text())
for a in m['artifacts']:
    p=Path(a['path'])
    assert p.stat().st_size==a['bytes'] and hashlib.sha256(p.read_bytes()).hexdigest()==a['sha256'],a['path']
r=json.loads(Path('tracks/mz-constants/evidence/reproduction.json').read_text())
assert r['runner_sha256']==hashlib.sha256(Path('tracks/mz-constants/code/reproduce.py').read_bytes()).hexdigest()
print('PASS: two staged files, all manifest artifacts, embedded runner identity')
PY
```

This is an artifact identity check, not an independent numerical replay. Separate auditor execution must be recorded in the audit record.

## Regeneration and handoff

The generating environment is Python 3.12, NumPy 2.3.5, SciPy 1.17.0 on Linux; exact versions/platform and thread settings are embedded in JSON. Preserve the pinned input bundle and runner, then use command R for numerical regeneration. The JSON includes source hashes and exact finite scope. None of these results certifies an unbounded theorem or imported N20480 output.

Transfer of the two staged JSON files and this manifest to AC's requested Windows destination is **pending**. This workspace has no accessible Windows destination or transfer receipt. No alternative durable destination was invented. On delivery, add the actual destination paths, delivery date and independent retrieval/checker result without overwriting this staging record.

## Retention

Keep the small essential reproduction JSON and manifest as repository commit candidates and preserve this local staging until the orchestrator/AC completes archival. No deletion or expiry was authorized. The ignored console duplicate is not essential evidence. Long-term custody and retention at the requested Windows destination remain for AC's handoff.

## Retrieval

While this workspace exists, retrieve the two files from the absolute paths in the table and run the checker above from `/workspace/padua_research`. The table hashes identify the exact bytes. A future clone retrieves committed candidates only after the orchestrator commits them; no commit receipt is claimed here. Windows retrieval remains pending until an actual delivery locator and verification receipt exist.
