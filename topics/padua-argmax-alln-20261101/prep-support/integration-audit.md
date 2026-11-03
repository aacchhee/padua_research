# Final preparation integration audit — actual merged main

2026-11-03. **PASS within the preparation/integration scope below.** Distinct requested/configured `gpt-6-astra` high reviewer, in the same finalization pass under AC's instruction to finalize without further Claude rounds. Serving metadata is not independently exposed. No new mathematics or novelty assessment.

This addendum addresses AC's merge of PR18 into main `1acebf7af47885654dfd1ffe0b9c8cda19c8f2a6` after the [original final audit](final-audit.md) froze. The original report and [receipt](final-audit.json) remain byte-identical: SHA256 `bb2010970704c80d2520b5ae87438ccf4848cf8362961b8bd8866e2190091f3f` and `34cb36cf04b0b8dd09f42db01e79534bb7a8ba9e2472ce63c5d935a9f1a7ef04`. Their old-main/unmerged-PR18 statements describe that earlier boundary and are superseded here for current integration. No retrospective change to an audit verdict or execution identity was made.

## Input and preserved integration

Read [PR18 audit-02](../../cold-storage-20261102/audit-02.md) and the updated WORKFLOW independently at pinned new main, then checked their materialized bytes. AGENTS/CODEX are unchanged from old main. PR18 final head is `367c3167199bb3599e96c161136dfbdb72acb57b`; topic parent is `0441756471436253b70f2a37be1bb644351f8bc4`. The selected local HEAD remains genuine source `cdb12257af24ea2542de707b9730f8278d69a168`; it is not relabeled as a completed publication. The [integration resolution record](main-integration.json) distinguishes actual main from this local head.

The candidate keeps all 176 PR18 deletions absent from its index. Comparing complete old/new-main trees and the candidate index finds all 87 incoming changed paths preserved exactly except the five intentional shared-file combinations. There are no unmerged index entries. All 31 checked materialized incoming nonshared/rule files equal pinned main bytes. The partial object store does not contain every deleted historical blob; a failing whole-repository Git status/diff is not treated as a content test. No full-clone or fsck certification is claimed.

- `RESULTS.md`, `state/CURRENT.md` and the batch allocation ledger preserve complete incoming main as byte prefixes, followed by PR17's own section.
- `PROOF_STATUS.md` and `ID_CROSSWALK.md` equal the frozen audited preparation with exactly main's one/three archive-link changes applied. No unrelated scientific row or reservation is lost or rewritten.
- 72 of the original 84 covered files remain exact. The 12 changed files are the audited storage tool/tests, five shared integration files, own results, FINALIZATION/LOG/report and the integrity checker's base-main metadata. Inspected changes add accepted integration status, archive links and PR18 history; scientific predicates and claims are unchanged.
- Revalidated all 37 scientific and 20 candidate records, unique IDs, aliases, canonical paths and statuses, original candidate byte prefixes and unrelated registry rows. PD-T181 remains reused PROVED; PD-T099 remains OPEN across the unknown finite-to-eventual bridge. The earlier four measured homes and three measured negatives retain their exact scopes.

## Storage validation actually executed

Exact accepted PR18/main SHA256:

| File | SHA256 |
|---|---|
| `tools/cold_storage.py` | `287153916a35f4360fde2f689cdd624b14f050f7329a323d95d8a8764c455c62` |
| `tools/test_cold_storage.py` | `f5047aab7ea6434e344b38bcc1cd85738d3329ec65cf745faa59cb403f062991` |

Inspected the complete tool delta against the earlier accepted helper: all filesystem/tracked-file/preflight guards remain, with destination readback, deterministic v2 receipts and offline archive verification added. Independently executed:

```sh
python -B tools/test_cold_storage.py
python -B topics/cold-storage-20261102/audit-02/faults.py
python -B tools/cold_storage.py verify padua-argmax-alln-20261101
python -B tools/cold_storage.py restore padua-argmax-alln-20261101 --dest <fresh-scratch>
python -B tools/cold_storage.py verify padua-argmax-alln-20261101 --dest <fresh-scratch>
python -B tools/cold_storage.py export padua-argmax-alln-20261101 --dest <fresh-export>
python -B tools/cold_storage.py verify-archive <fresh-export>/padua-argmax-alln-20261101 --manifest topics/padua-argmax-alln-20261101/cold-storage.json
```

**23/23 regression tests and 8/8 inherited independently authored fault controls pass.** The real 36-entry archive (2,526,191 bytes) verifies; each restored payload independently equals its exact Git source bytes, size and SHA256. A second restore preserves payload mtimes. The exported receipt is v2 with destination-readback true. A transferred archive and standalone copied tool verify both with and without a trusted manifest while `GIT_DIR` and `PATH` point to nonexistent scratch paths; Python is invoked absolutely, so Git cannot supply the bytes.

Additional independently constructed controls reject same-size payload corruption, a missing payload despite the surviving receipt, and a trusted manifest with only an extra newline. Restoring original scratch bytes returns verification to PASS. These are scratch mutations only. Protected scientific sources, frozen reports and the original cold manifest remain unchanged. The cold manifest SHA256 stays `88871c2064aa300bcdbcfae93e7b9de528daf3d60241d608454d8ea420216908` at source `1cecd68ac0a64b01ed7b2d262b6263a955a7d4d7`.

S1's implementation issue is resolved by the accepted merged tool. A receipt describes export-time verification; current verification against the trusted manifest remains necessary at the actual destination before reliance. Receipt-only verification establishes self-consistency, not external authenticity. Physical AC delivery is still PENDING and no purge is authorized or performed by this audit.

## Scientific replay after archival relocation

Inspected the new [scratch-only integration adapter](integration-checker-replay.py), SHA256 `ddcd27334d9a08ea53107a8909c9a771438bdc7b0b1efedd18f8cd745b4b2fad`, and independently executed it:

```sh
python -B topics/padua-argmax-alln-20261101/prep-support/integration-checker-replay.py > <fresh-scratch>/independent-integration.json
```

The accepted n4 pairing certificate is the only newly cold direct dependency needed by these checks. Source `2b52b432fe59c9a50aef9deebe5152c5d6874465`, blob `d768d04857c580459547f090a1256fd4ed8bed58`, 64,360 bytes, SHA256 `14a69a131b3c20416fd5521bd971efdadd4e3741f70546d0fc5f0d9f25a2cf61` are verified against an actual commit/tree association before scratch restoration and readback. The other 22 inherited archived entries are omitted. The adapter passes exact current sources to the frozen checker runner through isolated mirrors; read-only Git alternates provide real pinned objects without invented commits or shared Git changes. Independently matched 75 materialized inherited code/theory files against new-main blob identities, including the unchanged PD-T101 dependency pin.

**All 40 invocations pass with unchanged semantic summary and source hashes:** standalone n2; ten field/general certificates; 14 general, five field, four independent-general and 17 D3 malformed controls; exact pairing and independent rational reconstruction; D3 ten whole-cell pairs/eight witnesses; the two forged n2 source-pin rejections; and 21 refusals covering -O/-OO/PYTHONOPTIMIZE across seven proof entry points. All 242 inner scientific input hashes and 17 outer watched files remain unchanged. The cold n4 file remains absent from the source worktree. The original frozen runner, reports, receipts and enumerated historical-source adapters remain unchanged.

This replays the prior scoped checks after relocation. It does not reprove inherited n4 completeness/counts, rerun every historical numerical scan or establish any degree>=17 global certificate.

## Integrity boundary and remaining limits

Reviewed current local links: 3,092 references, no broken targets; 452 unmaterialized historical targets exist in the candidate index. The only temporarily absent target was this report before creation. Before this addendum, the active checker inventories 506 paths and 808,045 ordinary generated bytes, with largest ordinary artifact 16,344 bytes; the new JSON is also strictly below 16,384 bytes. No archived measurement payload is split or recommitted. The original 36 archive identities independently verify read-only. The parent's [complete-tree budget](repository-budget.json) conservatively counts 4,317,198 data bytes (4,012,640 ordinary) across 1,128 data files before this addendum/final refresh, below 5,000,000. Its method combines complete remote main-tree sizes with actual branch deltas; this reviewer inspected the receipt, while the final remote-tree budget remains a parent publication check.

The parent must now update only final acceptance metadata and refresh the manifest/packaging receipt after this report freezes. The independent reviewer then performs stdout-only normal and -O plain integrity checks, verifies before/after hashes and assesses those final metadata deltas without rewriting this report. This frozen report does not preclaim that subsequent result. A successful final plain check and publication of the checked bytes complete the preparation boundary; only AC merges PR17.

Environment: Python 3.12.14, SymPy 1.14.0, Linux 6.18.57 x86_64, glibc 2.41. Native Windows, actual WSL/drvfs and hostile concurrent mutation are untested. Supported POSIX primitives and quiescent destinations/indexes remain required. There is no AC delivery, history purge, force-push, clone-shrink or new scientific claim. [Machine receipt](integration-audit.json) pins inspected bytes and actual execution outputs; raw scratch logs stay outside the repository.
