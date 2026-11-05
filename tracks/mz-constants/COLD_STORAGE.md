# Cold-storage manifest — tracks/mz-constants

## Repository cleanup 2026-11-02 — large regenerable outputs moved off the branch head

AC (2026-11-02): "I do not think that we have to store large outputs that can be regenerated. Make sure that all needed code is in the repo, some short summaries are stored and expunge the large data files (cold storage)"; "18 mb per repo is too much."

Every generated data file of 16 KiB or more in this directory left the branch head: 5 files, 141,753 bytes. Machine manifest: [`cold-storage.json`](cold-storage.json). Tool: `tools/cold_storage.py`.

These files have **not been delivered to AC's Padua cold storage yet** (PENDING). Until then, the only stored copy is Git history, pinned by blob id at the pushed main commit `2b52b432fe59c9a50aef9deebe5152c5d6874465`. Each file's SHA-256 is recorded alongside, so the bytes can be verified.

Code, records, and small receipts and summaries stay. reproduction.json and astra-reproduction.json are MEASURED outputs of tracks/mz-constants/code/reproduce.py (1.25 s run; numbers deterministic, JSON bytes carry timestamps); the other three are auditor manifests/checks, only protocol-check.py has a committed generator. They are mutually hash-pinned (reproduction-manifest.json, astra-manifest.json, protocol-check.json, audit-targets.json, response-01-targets.json) and read at runtime by protocol-check.py and astra-final-check.py, so those scripts break unless the files are retrieved from history. Small committed counterparts remain: reproduction-manifest.json, astra-replay-comparison.json, astra-*-check.json, claude-audit-01-check.json, theory/reproduced-spectra.md (PD-T026). No proof dependency: all MEASURED/hygiene evidence. Abbreviations in commands: T/ = topics/padua-proof-attempts-2-20261101/, O/ = T/outputs/, C/ = T/code/, K/ = tracks/mz-constants/evidence/, M/ = topics/mz-constants/, E = 'PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=<python-flint deps> python -B', E0 = 'PYTHONDONTWRITEBYTECODE=1 python -B'.

Files of 16 KiB or more kept on purpose (not generated output):
- none

| File | Actual storage path | Bytes | SHA-256 | Source commit | Frozen generating command | Script blob IDs | Checker command / result |
|---|---|---|---|---|---|---|---|
| `evidence/astra-allocation-check.json` | Git blob `6ec9dbcb6e95` at `2b52b432fe59`; AC cold storage PENDING | 17,094 | `cba0804375a9d5703ccc64a757d23b9d4bda3e96835dfaf41c16ef847238e63c` | `2b52b432fe59` | none recorded | committed at source commit | Summary: M/independent-astra-01.md:495-504 (all 21 theory files and 35/37 files match preallocation SHA-256; two expected exceptions). Auditor-produced check; pinned in astra-manifest.json, protocol-check.json, audit-targets/response-01-targets. Cost: unknown (seconds-scale hashing). |
| `evidence/astra-manifest.json` | Git blob `ff7ee7ab22a0` at `2b52b432fe59`; AC cold storage PENDING | 29,075 | `623c181d19a29b24a35e9d88f20fb65f4964ae20b081716e7df836bdb80c01d1` | `2b52b432fe59` | none recorded | committed at source commit | Summary: M/independent-astra-01.md:463-470. Historical mixed-time identities; pins final-id-map.json, astra-allocation-check.json, astra-reproduction.json. Checker: python K/protocol-check.py (re-hashes its audited_inputs and auditor_artifacts, protocol-check.py:35) Receipt: K/protocol-check.json (manifest_checks) Cost: n/a. |
| `evidence/astra-reproduction.json` | Git blob `e9be9ac7a3f7` at `2b52b432fe59`; AC cold storage PENDING | 29,187 | `1511bfeb982f3e12b904acf151d9a586e6a65ee776dc464a12789a955ead4976` | `2b52b432fe59` | OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python tracks/mz-constants/code/reproduce.py --suite all --max-N 1280 --output /tmp/mz-audit-reproduction.json > /tmp/mz-astra-reproduction-stdout.txt (independent-astra-01.md:166; copied to this path; JSON embeds the /tmp command) | committed at source commit | Summary: tracks/mz-constants/theory/reproduced-spectra.md:23-33 (PD-T026 MEASURED); M/independent-astra-01.md:210-214; reproduction.md:30-38. MEASURED float64 replay; no proof dependency. Input bundle M/sources/padua_mz_inputs (committed). Checker: comparison with developer output: K/astra-replay-comparison.json (committed small: 637 numeric values, max abs difference 0); astra-final-check.py uses it for the manuscript tables Receipt: K/astra-replay-comparison.json; K/astra-manuscript-check.json Cost: ~1.26 s (elapsed_seconds in the JSON). |
| `evidence/protocol-check.json` | Git blob `9364041f476d` at `2b52b432fe59`; AC cold storage PENDING | 37,195 | `90d28fcedab0582ea76fee993be44834fe428775ca2b4247c83b50719fbe672d` | `2b52b432fe59` | python K/protocol-check.py > K/protocol-check.json (independent-protocol-01.md:13; recorded head 39f4785d48de7e77ff99e209bda954d632c61956) | committed at source commit | Summary: M/independent-protocol-01.md:13-38. Protocol-hygiene review snapshot (not scientific). Pins final-id-map.json, reproduction*.json, batch-registry-resolution.patch hashes. Checker: is itself the checker output (read-only git queries, header/registry-status checks, input hashes, manifest classification, local link existence, public-size accounting) Receipt: M/independent-protocol-01.md:38 (PASS) Cost: seconds. |
| `evidence/reproduction.json` | Git blob `a6c19e29ced5` at `2b52b432fe59`; AC cold storage PENDING | 29,202 | `b85b06fa9b3317d6ce84f9d354626b74edad4e8f9885341ecad39166d4fd6d40` | `2b52b432fe59` | OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python tracks/mz-constants/code/reproduce.py --suite all --max-N 1280 --output K/reproduction.json (M/reproduction.md:8; cold-storage.md Command R) | committed at source commit | Summary: tracks/mz-constants/theory/reproduced-spectra.md:23-33 (PD-T026, MEASURED); M/reproduction.md:30-38; M/cold-storage.md. Supports MEASURED claim PD-T026 and the manuscript tables; cold-storage.md already asks to preserve the archived JSON for byte-for-byte retrieval. Source of the paper README link. Checker: identity check inline in M/cold-storage.md (PASS: two staged files, all manifest artifacts, embedded runner identity); numeric replay by Astra Receipt: M/cold-storage.md (checker result); K/astra-replay-comparison.json; K/reproduction-manifest.json (2084 B, pins sha b85b06fa...) Cost: ~1.25 s (elapsed_seconds; Python 3.12, NumPy 2.3.5, SciPy 1.17.0). |

`<out>`, `<work>`, `<deps>` and `<flint>` stand for scratch paths. Never write regenerated output over committed files.

**Retrieval**

```sh
python tools/cold_storage.py verify  tracks/mz-constants   # every entry against its Git object
python tools/cold_storage.py restore tracks/mz-constants   # put the files back in place, then run the recorded checkers
python tools/cold_storage.py clean   tracks/mz-constants   # remove the restored copies again
python tools/cold_storage.py export  tracks/mz-constants --dest C:\Users\andreyac\Downloads\padua\cold_storage
```

These commands need a full clone. In a shallow clone, first run `git fetch origin 2b52b432fe59c9a50aef9deebe5152c5d6874465`.

**Retention**

Permanent, with AC as custodian. The Git history copy lasts as long as history is not rewritten. The AC copy is created by `export`; commit its receipt hash here when that is done.

### Corrections 2026-11-02: complete commands and readers (response to the Codex cold-storage audit, F3/F4)

These values replace the clipped or inaccurate ones in the tables above. The machine manifest [`cold-storage.json`](cold-storage.json) carries the same values.
- No identity field changed (path, bytes, SHA-256, Git blob).
- Commands are quoted verbatim from the cited records. Where a record gives no command, the row says so explicitly.
- A "working-tree reader" reads the checked-out file and needs `restore` first. A "historical Git reader" reads pinned Git objects and does not.
- Restoring files does not mean that point-in-time validators accept a later head.

- `evidence/protocol-check.json`, **generating_command** (F3): python tracks/mz-constants/evidence/protocol-check.py > tracks/mz-constants/evidence/protocol-check.json (topics/mz-constants/independent-protocol-01.md:13; recorded head 39f4785d48de7e77ff99e209bda954d632c61956)
- `evidence/reproduction.json`, **generating_command** (F3): OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python tracks/mz-constants/code/reproduce.py --suite all --max-N 1280 --output tracks/mz-constants/evidence/reproduction.json (topics/mz-constants/reproduction.md:10; topics/mz-constants/cold-storage.md:17)
- `evidence/reproduction.json`, **notes** (F3): Supports MEASURED claim PD-T026 and the manuscript tables; topics/mz-constants/cold-storage.md already asks to preserve the archived JSON for byte-for-byte retrieval. Source of the paper README link. Checker: identity check inline in topics/mz-constants/cold-storage.md (PASS: two staged files, all manifest artifacts, embedded runner identity); numeric replay by Astra Receipt: topics/mz-constants/cold-storage.md (checker result); tracks/mz-constants/evidence/astra-replay-comparison.json; tracks/mz-constants/evidence/reproduction-manifest.json (2084 B, pins SHA-256 b85b06fa9b3317d6ce84f9d354626b74edad4e8f9885341ecad39166d4fd6d40) Cost: ~1.25 s (elapsed_seconds; Python 3.12, NumPy 2.3.5, SciPy 1.17.0).
- **Topic note** (F3): reproduction.json and astra-reproduction.json are MEASURED outputs of tracks/mz-constants/code/reproduce.py (1.25 s run; numbers deterministic, JSON bytes carry timestamps); the other three are auditor manifests/checks, only protocol-check.py has a committed generator. They are mutually hash-pinned (reproduction-manifest.json, astra-manifest.json, protocol-check.json, audit-targets.json, response-01-targets.json) and read at runtime by protocol-check.py and astra-final-check.py, so those scripts break unless the files are retrieved from history. Small committed counterparts remain: reproduction-manifest.json, astra-replay-comparison.json, astra-*-check.json, claude-audit-01-check.json, theory/reproduced-spectra.md (PD-T026). No proof dependency: all MEASURED/hygiene evidence. Abbreviations used in entries: K/ = tracks/mz-constants/evidence/, M/ = topics/mz-constants/.

After any export, check the archive with `python tools/cold_storage.py verify-archive <DIR>/tracks_mz-constants --manifest tracks/mz-constants/cold-storage.json`, and run it again immediately before relying on the archive (for delivery acceptance, or before a history purge). The export receipt alone is not proof that the files are still present.

## 2026-11-05 raw-output archival addendum

AC directed generated outputs to cold storage. Additional raw transcripts and
analysis captures from this topic are now pinned at source40347d1 in separate
component manifests; all older manifests/identities above are unchanged. See
[the migration index](../../topics/padua-lebesgue-followups-20261103/preparation/cold-storage-migration.md)
for exact file counts, manifest paths, verified export/restore commands and
receipt hashes. Small essential proof receipts, summaries and code remain in Git.
Physical delivery to AC remains pending; staging is not a delivery claim.
