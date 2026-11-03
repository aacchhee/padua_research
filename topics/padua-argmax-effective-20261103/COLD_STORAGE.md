# Gate and comparison scratch evidence inventory

Status2026-11-03: **local archive staged and verified; external durable delivery and AC Windows delivery PENDING**. No Windows destination has been selected. No remote transfer, Windows destination verification, historical-tool export receipt or external delivery is claimed.

[cold-storage.json](cold-storage.json) inventories16 regenerable files,695346 bytes, currently under `/workspace/padua-work/gates/` and `/workspace/padua-work/comparison/`. Every entry gives its current path, relative archive path, byte count, SHA256 and generator identifier. Generator records give commands and source paths; source hashes and environment are pinned separately. The two small exact proof artifacts `g6-exact.json` and `g6-exact-independent.json` are excluded because root owns copying their essential bytes into committed `evidence/`. Their verbose logs remain inventoried. Root owns `evidence-manifest.json`; it was not edited here.

## Verified local staging archive

[Download the locally staged raw evidence archive](/workspace/padua-work/export/padua-argmax-effective-20261103-raw.tar.gz).

- Absolute path: `/workspace/padua-work/export/padua-argmax-effective-20261103-raw.tar.gz`.
- Bytes:87815.
- SHA256:`7aafe2207be329528e39015fa233e96011050869efd00f1ebbd41cfbf4db2ae9`.
- Contents: the16 inventoried payload files plus the exact `cold-storage.json` bytes,17 regular-file members total. No code, certificate excluded from the inventory, or unlisted scratch file is included.
- Executed verification: opened the completed gzip tar with Python `tarfile`; checked the exact member-name set, regular-file types, manifest byte identity, and every payload's byte count and SHA256 against that manifest. Verification read the member bytes without extracting them.

This is **custom local staging**, not `tools/cold_storage.py export`, a remote upload or AC Windows delivery. The archive remains in the execution workspace; its local link permits app retrieval but does not establish that a durable external copy has been received. After retrieval, verify the archive SHA256 and the member inventory at the destination.

The embedded/current inventory predates staging and deliberately retains its original `export_performed=false` and `archive_verified=false` fields: those fields describe the inventory's creation checkpoint, not this subsequently executed custom staging step. The archive's own identity and verification are recorded only here to avoid a manifest/archive self-hash cycle. No manifest bytes were changed during staging.

## Retrieval contract and tool limitation

This inventory has format `padua-scratch-inventory-v1`, deliberately **not** `padua-cold-storage-v1`. The existing `tools/cold_storage.py` restores/exports historical committed Git blobs and requires valid source-commit/blob identities. These raw files were never committed. They therefore have no historical blob to restore through that tool, and no source identity has been invented. Do not invoke its restore/export commands on this inventory or treat this file as its export receipt.

Exact bytes can currently be recovered by copying the surviving local files and verifying the copied bytes against this inventory. If the workspace disappears before an external archive is delivered, exact original timings/log/provenance bytes may be lost. Reexecuting the generators reproduces a scientific measurement, **not guaranteed byte-identical files**: elapsed times, invocation strings, source paths and logs can change. The compact committed measurement receipts and exact proof artifacts are separate evidence, not an archive of every raw sample.

## Contents and regeneration

Run commands from `/workspace/padua_research`, using `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1`. The JSON's `generators` section supplies the full commands and redirections. No regeneration was executed as part of this inventory task.

- G2/G3 pilot replay stdout: unchanged pilot scripts. The existing outputs match the prior committed pilot outputs byte for byte. `replay-receipt.json` was made by an inline subprocess timing wrapper not retained as a source file; rerunning the listed pilots and recording actual elapsed times is its regeneration procedure, without a promise to restore its old bytes.
- `g2.json`, `g3.json`, `g4.json` and logs: `code/gates/screens.py` with the named gate and output path. These contain both-corner G2 samples, the1861-point G3 phase grids' summaries, and G4 center/offset class extrema and minimizing locations. The generator does not retain every individual point value; rerun it if those values are needed. G2/G3/G4 sample-scope limitations remain in [the attempt](attempts/gates-g2-g5.md) and [the durable MEASURED record](theory/argmax-effective-codex-02-gate-measurements.md).
- `stability.json`: `code/gates/validate.py`; finite dense-evaluator comparisons and longdouble diagnostics only.
- `g6.json` and log: `code/comparison/g6_screen.py` default run, containing all1536 E-C comparisons and182 representative I-B0 rectangles with their numerical phases and optimizer outcomes. This is577726 bytes and is the largest item.
- `g6-independent-ec.json` and log: same frozen script, `--degrees 13 17 24 60 --ib-degrees`; different-agent96-comparison replay. It does not independently replay I-B0 or all48 degrees.
- Exact producer/checker stdout logs: generated by the listed spot producer and checker commands. Their essential small certificate and acceptance JSON files are handled by root separately. The checker uses inherited arithmetic; its shared-kernel limitation is recorded in the exact theory record.

Producer/native-checker bulk certificates and logs are outside this narrowly assigned inventory. Their owners' attempts and root's final manifests govern their retrieval; this document makes no availability assertion for them.

## Prospective local copy and verification

The following is an **unexecuted template**, not a delivery record. AC/root must choose a durable destination first. Set the task-specific variable `PADUA_ARCHIVE_DIR` to that absolute destination; it is intentionally unspecified here. Existing matching files are reused and differing files cause refusal. Use a new non-Git archive directory and keep it quiescent during the copy. This template is for trusted local paths; it is not a hardened hostile-filesystem copier.

```sh
python3 - "$PADUA_ARCHIVE_DIR" <<'PY'
import hashlib, json, shutil, sys
from pathlib import Path
manifest = Path('topics/padua-argmax-effective-20261103/cold-storage.json')
data = json.loads(manifest.read_text())
dest = Path(sys.argv[1])
assert dest.is_absolute(), 'select an absolute archive destination'
def valid(path, entry):
    raw = path.read_bytes()
    return len(raw) == entry['bytes'] and hashlib.sha256(raw).hexdigest() == entry['sha256']
for entry in data['entries']:
    source = Path(entry['current_local_path'])
    assert source.is_file() and not source.is_symlink() and valid(source, entry), source
    target = dest / entry['path']
    assert not target.is_symlink(), target
    if target.exists():
        assert target.is_file() and valid(target, entry), target
for entry in data['entries']:
    target = dest / entry['path']
    target.parent.mkdir(parents=True, exist_ok=True)
    if not target.exists():
        shutil.copyfile(entry['current_local_path'], target)
    assert valid(target, entry), target
print('Verified copied payload:', len(data['entries']), 'files,', data['total_bytes'], 'bytes')
PY
```

After a transfer to AC's Windows machine, independently read every delivered file and compare bytes/SHA256 to the inventory **at that destination**. A previous local verification cannot establish that the Windows copy exists or is intact. Preserve the inventory alongside the payload and record the actual destination, copy date, resulting manifest hash and destination verification before claiming delivery. No existing `tools/cold_storage.py verify-archive` compatibility is implied by this scratch format.

## History

2026-11-03, Codex gates worker, gpt-6.1-sol medium: created this local inventory by reading and hashing existing files only; no numerical run, external delivery or Git operation. Subsequently, at root’s explicit instruction, staged the listed local tar.gz and verified all17 members using `tarfile`; no remote upload occurred. Root requested the separate scratch format because the historical cold-storage tool cannot source never-committed scratch artifacts.
