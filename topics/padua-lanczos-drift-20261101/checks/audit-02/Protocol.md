# Audit 02 — bounded protocol and original-artifact verification

Rules and audited head: `7a6dd1f7f8f10d0f9c2568e89d693b7d04cd571b`.
Current main: `28aaa20861d08074b77efc74eaef75cdcb36234d`.
Scientific response candidate: `cef79d66321a93d93d53e53efcb7e6744c387481`.
Original scientific snapshot: `b09e1dbe0baafd666cf0d779a671a40f55de2d75`.
Original base: `806cc7b4509fd93bae652f9545d32d95529f8281`.

Auditor: independent Codex protocol subagent, assigned under handoff 06's
`gpt-6-astra` xhigh audit allocation. The subagent interface does not separately
expose the actual runtime model variant/effort. Scope: artifact integrity,
manifest provenance, administrative dispositions P-F1–P-F8, literal proposal
anchors, results-summary accuracy and repository boundaries. Mathematical
acceptance and novelty comparison belong to the E1/E3–E4/E5/E6 reviewers; the
orchestrator owns the current remote union scan and integration rehearsal.
This review introduces no ideas or novelty claims, so it does not repeat the
full IDEAS read. P-F6/P-F7 below verify the requested disclosures, not a new
independent priority search.

**Outcome:** original ZIP and all manifested original run-artifact references
verified locally. Windows delivery remains pending. No high or medium protocol
finding; one low administrative cleanup is identified below. There is one
explicit limitation concerning an earlier, uncommitted theory-input hash.

## Executed checks and identities

The committed scripts use only Python's standard library and read-only Git
commands. Neither changes Git state, invokes branch/PR tools, modifies a
developer file, nor writes to Windows. Run from the repository root:

```sh
python topics/padua-lanczos-drift-20261101/checks/audit-02/Protocol/check_artifacts.py --output topics/padua-lanczos-drift-20261101/evidence/audit-02-protocol-artifacts.json
python topics/padua-lanczos-drift-20261101/checks/audit-02/Protocol/check_text.py --output topics/padua-lanczos-drift-20261101/evidence/audit-02-protocol-text.json
```

Both executed successfully. Evidence:
[artifact receipt](../../evidence/audit-02-protocol-artifacts.json) and
[text/anchor receipt](../../evidence/audit-02-protocol-text.json).
The latter records hashes for the rules, handoff, original audit, response and
developer reports, administrative files and selected source files read.
Additional inspection used `rg`, `git show`, `git diff`, `git ls-tree`, and
`git rev-list`; no scientific checker execution is claimed by this reviewer.
An initial checker attempt incorrectly treated final-validation's later list
as the ZIP list and stopped on absent `archive-receipt.json`. The final checker
uses the actual pinned source tree and records the two receipts separately.

### Original ZIP

`/workspace/exports/padua-lanczos-drift-b09e1db.zip` is **799,968 bytes**,
SHA-256
`27476b624d424f082a71779618b9e1f9b06d6fba7db6b662755cf886637dd3a4`.
`zipfile.testzip()` returned `None` (CRC PASS). There are 82 unique entries:
exactly the 81 own topic/code/theory files in source `b09e1dbe…`, plus
`SNAPSHOT.txt`. Every one of those 81 entries is byte-for-byte equal to
`git show b09e1dbe…:<path>`; the receipt records each SHA-256 and Git blob ID.
The snapshot note names that source and explicitly disclaims Windows delivery.
No third-party source payload or large raw capacity output is in this ZIP.

The ZIP is not a copy of the later final-validation list. Its file set contains
handoff 01, while final-validation instead includes the subsequently created
archive receipt. Of their 80 common paths, 76 are identical; COLD_STORAGE,
LOG, plan and report carry later metadata in final-validation. The source-tree
comparison, not an assumed equality between these two historical receipts,
establishes the archive identity. This does not alter either frozen receipt.

### Original run outputs and the historical “46” count

The requested development capacity file exists at
`/workspace/padua-drift-runs/e1/cgs2-multinode-rotated-n12-bj.json`:
3,626,111 bytes, SHA-256
`ffd035eef09d39be2ab862a6c12abbe58c455cd9131615ee89b4eefba14d1d8e`.
The original root E6 output also exists:
`/workspace/padua-drift-runs/root-independent-e6.json`, 25,154 bytes, SHA-256
`3cc34860ead3b2bc4d07441e9e10a8adc7e0acc0be1c643c6a9287e2a18056c4`.
Both match the committed identities exactly.

A broader sweep of every original topic JSON content-ID reference to
`/workspace/padua-drift-runs/` verifies **160 reference occurrences covering
147 unique paths**, all present with matching sizes and SHA-256. This includes
the full-sweep and degree-two records as well as the originally requested
scalar and independent outputs. These are checks of the existing original
bytes; no replacement artifact was generated for this integrity test.

Audit-01's “46 off-repo artifacts” is an overcount of off-repository files:

| Original manifest selection | Manifest rows | Actual off-repo rows | Unique off-repo paths | Absolute repository inputs |
|---|---:|---:|---:|---:|
| e1-scalar-manifest, working_artifacts | 10 | 10 | 10 | 0 |
| independent-scalar-01, all SHA/path rows | 36 | 11 | 9 | 25 |

Thus those 46 rows describe 19 unique off-repository paths, 25 repository
inputs, and two repeated capacity references. All 19 original output paths
match. This corrects the count for this audit without rewriting audit-01.

**Earlier input-pin limitation:** 14 of the 25 repository-input files have
changed since the independent scalar receipt. Thirteen original hashes are
recoverable exactly from source `b09e1dbe…`. The remaining record-05 input pin
is 8,373 bytes, SHA-256
`ae35d20a999f265945dbd74ac494e049bdafc5201707c4f4f43fc0f8d63bf22e`.
It is not the current file or the 9,348-byte source-snapshot file, and no
matching version was found in that path's reachable Git history (all-ref
check: two distinct file-changing commits). The existing final-validation
metadata already discloses the later receipt/status-only addition; the source
file explicitly calls it a post-checker metadata update. Accordingly, **45 of
the 46 historical manifest rows have retrievable matching content IDs**, while
all actual off-repository outputs do. This audit does not manufacture the
missing working-byte version or claim to have compared its mathematics.
Current record 05 is independently re-audited by the E1 reviewer.

### Reproduction versus delivery

Inspection of `e1_reproduce.py` confirms that it reads the committed compact
scalar and certificate JSON, checks producer/source hashes, reconstructs
capacities in a temporary directory, and checks explicit projection. It does
not require the 3.6 MB raw development file as input. This is source inspection
here; audit-01's executed reproductions and the current scientific reviewers'
executions remain separately attributed.

No Windows bridge is available in this session, and no Windows copy/readback
was performed. **P-F1 artifact-integrity uncertainty is resolved; original
development Windows archival delivery remains pending.** Verification can
continue from committed compact evidence plus regeneration under the current
repository-only rule. Local workspace existence is not permanent custody.
The audit-01 Windows ZIP delivery/readback in LOG:90 is a historical Claude
receipt (269,978 bytes, SHA-256
`29c177218d0d08dcfb1299c1cdc2cc333c40f6da3208abd6f12f1e089150f9ff`), not
a delivery newly observed by this reviewer.

## P-F1–P-F8 dispositions

| Finding | Protocol disposition |
|---|---|
| P-F1 | Original ZIP, capacity, root E6 and all original run-output references verified above. Windows archival delivery remains pending; compact evidence/regeneration is the explicit verification path. Preserve the earlier theory-input-pin limitation. |
| P-F2 | RESOLVED by disclosure. Against current main, ID_CROSSWALK adds only the reservation link/provenance section; ALLOCATIONS changes only that reservation's link/provenance line. Neither allocates final IDs. The old empty receipt field stays historical. |
| P-F3 | Text correction accepted with a provenance qualification: the current task brief supplies AC's exact instructions “Campaign mode adventurous and less gated” and “Relaxed novelty gate at start and before each new mechanism.” Audit-01 lacked that prompt. Its “no recorded instruction” conclusion was limited to its available record, not evidence that AC never gave the instruction. Removing “relaxed” does not change the executed gate, which audit-01 found to meet the normal minimum. No new gate execution is invented. |
| P-F4 | RESOLVED: LOG links handoff 02 and the numbered 01–06 chain. |
| P-F5 | The response's e0d9e3d/PR12/PR16 check is historical. Current union-scan and integration acceptance belong to the root's separately recorded run against current main/open heads; this report does not substitute the old receipt for that run. Repeat at final-ID assignment/readiness. |
| P-F6 | Requested PD-T042/043, IDEA-139/141–144 disclosures and span-normal-versus-Gram/error-model separations are present in ideas-e1 and record 03. Mathematical adequacy is cross-referenced to the E1 review. |
| P-F7 | Requested E1 IDEA-087/088, E5 PD-T061/IDEA-157 and PD-N021/IDEA-161, and E6 IDEA-086/116 predecessor disclosures are present. No independent literature-priority verdict is added here. |
| P-F8 | Active “independent reproduction pending” wording is reconciled; old wording survives as explicitly historical quotations/snapshots. Whether record 05's exact inequalities must be split is the E1 mathematical finding, not decided by this protocol review. |

## Repository boundaries, proposals and results

At pinned head, all **131 new own campaign files** relative to current main
total **3,119,781 bytes**, conservatively including prose/code as well as
generated evidence. JSON totals 2,230,158 bytes. The largest file is
`e1-full-sweep.json`, 616,693 bytes. Thus every new own file is below 1 MB and
even the all-file total is below 5 MB. Imported MZ/main material and raw files
outside Git are excluded. Audit-02 additions require the root's final size
check when all workers finish; this is a pinned pre-audit-additions count.
No vendored third-party payload was found in the own-file inventory or the
inspected source/provenance. This is an inventory/content review, not a claim
of an exhaustive originality test.

All **77 pre-existing bivariate theory files** are byte-identical to both
original base and current main. There are no head-versus-current-main changes
under `.github`, `state`, `literature`, `agents`, or in AGENTS, PROOF_STATUS,
PAPER_MAP or root RESULTS. Scientific code/theory and response evidence are
unchanged from candidate `cef79d66…`. Audit-01 and its checker directory are
unchanged. All ten response-manifest identities match current bytes.

All **15 literal OLD blocks plus the optional History anchor** occur exactly
once in their intended targets at both current main and audited head. A
sequential in-memory replacement also leaves every later anchor unique.
Nothing was applied. Final IDs, the E5 split/crosswalk text, removal of withdrawn
record 14, and the root RESULTS section remain preparation actions.

The topic results file contains original summaries, record/evidence links and
bounded statuses; no third-party fulltext or private material was found.
The scalar factor-ten result remains INCONCLUSIVE, the raw-source/polynomial
scope is retained, U2/G remain OPEN, and response changes are explicitly
marked as awaiting re-audit. The record-15 row describes its valid ten-node
instance and mentions the pending generalization; record 14 is explicitly
said to become an IDEA disposition. After this audit the orchestrator should
synchronize those rows and the next-step/status text to the actual outcome.
The original constant and the pending sharper constant are distinguished.
This summary check does not replace the four mathematical reviews.

## Low administrative finding: P02-F1

`proposed-record-changes.md:143` still directs a Windows results write and
mentions the old shared-RESULTS modification-time guard. `plan.md:35` and
`report.md:164` still include Windows **results** delivery among pending work.
These are active preparation/frontier sentences, unlike immutable historical
handoffs and the dated audit-01 delivery receipt. The current WORKFLOW and the
root's new LOG entry supersede them: topic results live in the repository,
and only this topic's root RESULTS section changes at PR preparation. No
Windows results write is needed or authorized by these stale sentences.

Required administrative disposition: explicitly carry the supersession into
the next handoff and synchronize the current frontier during the authorized
administrative update; preserve historical receipts and handoff bodies. Also
replace the results file's old “PR16 still draft/once merged” timing with the
current main state when its audit status is updated. No scientific change,
new allocation or early root RESULTS edit follows from this finding. These
developer documents were not changed by this reviewer.

Residual limits: no Windows readback, no claim that workspace retention is
permanent, no newly executed mathematical regeneration by this worker, one
unretrieved earlier theory working-byte pin, and dependence on the root's
current remote/integration checks and the scientific reviewers' conclusions.
