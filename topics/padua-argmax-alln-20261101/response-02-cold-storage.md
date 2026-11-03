# Response02 — cold-storage protocol repair

2026-11-02, Codex gpt-6.1-sol high (requested/configured; serving metadata not exposed). Developer response under handoff09, not an independent approval. Source/rules input `93169ab6e193fbbef91af16914cd1191e7564420`, administrative redirection commit `863c319b13170a7625647e03ea5dc8f2687ebdc3`; base main `2b52b432fe59c9a50aef9deebe5152c5d6874465`. Remote access/publication uses the GitHub connector. The [complete materialized source-path inventory](response-support/storage-repair/input-files.json.gz) records the pinned selected-file snapshot; its paths' source identities resolve at the exact input tree. AC explicitly selected Codex for this continuation; the independent Claude review previously requested by08 remains pending for response-01 and this repair.

## Findings and developer dispositions

| Finding | Implemented response | Evidence / remaining gate |
|---|---|---|
| CS1 MAJOR: restore/export overwrite user or tracked data, including receipts | Validate all source identities and preflight every destination before creating directories/payloads. Refuse tracked/prefix collisions, symlinks, nonregular and differing files. Reuse byte-identical regular files without rewriting. Use exclusive no-follow creation and a deterministic receipt, checking its collision before any payload. |19fixture controls and real36-byte comparisons/idempotence; independent Claude acceptance pending. |
| CS2 MAJOR: cleanup follows parent symlinks outside destination | Walk directories with pinned no-follow descriptors, preflight every traversal before the first deletion, preserve tracked/differing files, recheck bytes/identity/index immediately before descriptor-relative unlink. Unsupported descriptor platforms fail closed. |Parent/final/root symlink tests and supplementary FIFO/marker probes; no adversarial-concurrency guarantee. |
| CS3 MINOR: generic/incomplete regeneration commands | Correct all rows against pinned interfaces; full producer/dependency blob IDs, complete historical source bootstrap, scratch A and D relocation, explicit historical T1 T2/T3/T4 prerequisites. Distinguish equivalent scientific invocations from unknown original shell wrappers/timing and retrieval-only snapshots. |All36identity tuples and19unique script/blob pairs checked; commands syntax-checked; distinct Astra fresh short D3 regeneration. Long A/D/T1 scans were not rerun here. |
| Active versus archived manifest | Only the archived evidence-manifest row has historical-version role. Verify reports a regular tracked active version separately, while checking every historical source identity. Restore refuses the tracked active path before writing anything; scratch copies must match the old bytes. |Default restore refusal and active bytes preserved in developer and distinct checks. Active contents are validated by current integrity checker, not by the historical-role exception. |
| Supplementary foreign-checkout finding | A separate probe showed source-index-only cleanup could delete matching files tracked in another checkout. Added explicit mutation refusal for foreign Git metadata at destination ancestors and traversed payload directories. |Regression recreates restore→foreign git init/add→clean and confirms refusal with all bytes preserved. Additional ancestor/nested markers tested. |

The original [audit-02-cold-storage](audit-02-cold-storage.md) and its support remain immutable; these are developer dispositions awaiting independent Claude protocol review. The distinct [Astra storage check](response-support/storage-repair-check.md) supplements that review and does not replace it. No response-review-01 acceptance is authored by Codex.

## Implementation and operational contract

`tools/cold_storage.py` validates format, unique JSON keys, integer sizes, full Git object IDs, source commit type, exact literal source path/blob association, SHA-256 and byte size, safe relative paths, roles, casefold duplicates and path-prefix collisions. It checks source identities before writing. Source-index tracking guards include absent indexed paths and ancestor/descendant collisions. No assertion-based safety predicates are used.

Restore/export/clean refuse foreign `.git` files, symlinks, other nondirectory markers and nonempty `.git` directories encountered at ancestors or along payload parent traversal. Own source-root metadata is allowed with its own index checks; a containing outer repository is shadowed by the source checkout, while nested foreign markers are refused. Empty `.git` directories contain no index and are ignored (the environment has such immutable sentinel directories). The destination/index must stay quiescent, including no concurrent Git initialization. Read-only verify safely traverses and compares foreign scratch copies without applying the mutation-only foreign marker restriction. Use fresh non-worktree storage.

**Supported backend: POSIX with dir_fd, O_DIRECTORY and O_NOFOLLOW. Native Windows fails closed**, including manifest load/verify; use an appropriate supported POSIX/WSL filesystem and AC's actual authorized mounted path. No native-Windows or actual AC-machine test is claimed. Manifest-loading traversal has the same no-follow checks.

This is not transactional or safe against a hostile concurrent filesystem actor. Pinned handles cannot prevent moving directories, changing mounts, editing open files or swapping a final entry after its final stat; POSIX has no atomic compare-and-unlink. An I/O failure/interruption may leave a partial newly created file; inspect/remove that partial file manually before retrying. Completed matching files can be reused. No rollback deletes existing files; cleanup leaves directories and export receipts intact. Ordinary static differing/tracked/symlink collisions are refused before writes/deletions.

## Exact developer executions

From the selected-file workspace `/workspace/padua-storage-fix-20261102`:

```text
python -B tools/test_cold_storage.py
python -B topics/padua-argmax-alln-20261101/response-support/storage-repair/validate.py
```

The first completed **19/19 tests**, 3.136s on Python3.12.14/Linux, with fixture Git repositories exclusively in newly owned temporary directories. [Compact controls receipt](response-support/storage-repair/developer-controls.json) pins driver/helper/stdout/stderr. It tests normal and refused operations, receipt conflicts, traversal and role errors, source substitution, indexed destinations, idempotence and the foreign-checkout regression.

The second uses the actual36archived objects, source `1cecd68ac0a64b01ed7b2d262b6263a955a7d4d7`: verifies all original identity tuples unchanged; verifies the default source; confirms in-place refusal and unchanged active manifest; restores all36to fresh scratch; compares every byte to source; verifies/repeats without payload mtime changes; cleans matching files while preserving an unrelated file; exports/repeats without receipt byte/mtime changes. [Actual command arguments/result hashes](response-support/storage-repair/developer-validation.json) and the committed runner make this reproducible. No historical payload was written to the source worktree. Scratch locations in receipts are ephemeral; rerun the script for a fresh owned destination.

Distinct Astra independently executes its own controls/real36workflow and checks all metadata/source pins. Its separate report/receipt distinguish original checks from the later foreign-marker repair. A fresh historical D3 E-P screen reproduces24,993B, SHA256`3215523e1a768ce7e81c76283ac18bf476f8162bdcd84e579a7b93388707d14c`; this is a short provenance check, not a new scientific claim or proof review.

The integrity-only checker now includes the safety-test driver and records input93169ab. It is refreshed after covered files freeze, followed by a plain read-only check. The explicit packaging receipt reports actual counts/hashes. It preserves the one current integrity-manifest size exception and cold-manifest metadata exception; every other generated head file stays strictly below16KiB. Generic `plan` may still list the explicitly excepted active integrity manifest; no zero-candidate promise is made. Old audits/support and scientific proof/checker/certificate bytes remain unchanged.

## Candidate identities

| File | SHA-256 |
|---|---|
| `tools/cold_storage.py` | `d12fc95dc1fe6145ad0f82b225104cee568bab5586bcd247fe445c671f123bd5` |
| `tools/test_cold_storage.py` | `0aac0194efcd551a6ebe97216d2bf22992d9f3e86c8b0aa77e584285cf5fc3fe` |
| `topics/padua-argmax-alln-20261101/cold-storage.json` | `88871c2064aa300bcdbcfae93e7b9de528daf3d60241d608454d8ea420216908` |
| `topics/padua-argmax-alln-20261101/COLD_STORAGE.md` | `4ea56e5d2548a75e1ef1752c79e59a40d274c6efb7be07da3f01f0c482c34ce9` |
| `topics/padua-argmax-alln-20261101/response-support/storage-repair/validate.py` | `18a20d44cca256ef0545f134d93b77454ae4bcf7d3edfbf87012cce175256875` |

These are exact development file identities; the output commit will pin them. No archival tuple/path/blob/SHA/size/source changed:36files,2,526,191B. The complete historical T1 reconstruction and response-01 identities are unchanged.

## Remaining work and integration

Stage **AUDIT**, PR17 stays draft. Independent Claude Opus5.5 high must review both Codex responses, check the scoped findings, execute appropriate storage controls/real36checks and verify packaging. Only after that gate may audited preparation apply shared rows/final IDs; scientific assertion-optimization hardening remains a separately scoped pending preparation task. Mathematical acceptance remains audit-01's scope: finite2–16 and eventual exact two-corner argmax with non-effective threshold; PD-T099 stays **OPEN**. No new gated round was run.

Delivery/export to AC's Padua cold storage remains **PENDING**; all exports here are scratch. History is preserved, so existing clone object stores have not shrunk. No future purge/force-push authority is inferred.

PR18 (`claude/cold-storage-20261102`, observed head`1d90af5d58fca87f240a04c18c427e8f59e2d6b8`) is integration context only. This topic's repaired shared helper now diverges; later integration must preserve these guards and check other manifests against their stricter validation. PR18 is not audited, edited or merged by this repair. The recorded recommendation remains PR18 first subject to AC, then reconcile updated main here without discarding storage safety. Only AC merges.
