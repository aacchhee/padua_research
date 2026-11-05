# Audit-03 family report — APP (literal application, durable consistency, application refresh)

The subagent auditor was Claude Opus 5.5 at effort high, working under the Claude audit-03 orchestrator. The orchestrator saved this report from the subagent's returned text in condensed form; every finding is kept. Scripts ran only in a scratch clone at `0299fcf`. The real repository was left untouched, and its working tree was clean.

**Verdict:** checks 5, 6 and 7 all PASS. There are no BLOCKING or MAJOR findings.

## Scope

- **Input:** `0299fcf` against the integrated base `a3f03be`. That base's registries are byte-identical to main `b4d292e`.
- **Later commits:** `0299fcf..1fb21c1` changes only handoff10's status and adds handoff11.
- **Hashes at `0299fcf`:**
  - proposal `aeb09ac1`, final-id-map `65fcfbcc`, application-receipt `75892f5e`;
  - scripts: apply_registration `a43d75fd`, check_registration `047a5ffc`, finalize_metadata `74bf7ade`;
  - registries: PROOF_STATUS `a696f9f6`, IDEAS `a3405f6e`, CURRENT `b8995375`, ID_CROSSWALK `ec3cb89f`, RESULTS `b4ef6482`;
  - batch ALLOCATIONS `71556c0c`;
  - inherited theory files: e1-05 `21706657`, e1-06 `f3ba5850`, e3-11 `85138f08`.

## Check 5 — literal application and preservation: PASS

**Which shared files changed.** Relative to `a3f03be`, exactly nine shared files changed: the five registries, one additive dated section in the batch ledger, and three inherited theory files that were only appended to.

**PROOF_STATUS — 7 rows changed.**
- The rows are PD-T055, T056, T075, T140 (target part), T141, T143 and T146.
- In every one the statement cell and status cell are unchanged, except the PD-T140 target part, which goes from PARTIAL to PROVED. All other edits are appended text.
- The PD-T140 experiment row is byte-identical: MEASURED, with an INCONCLUSIVE sufficient test.
- PD-T055 (OPEN), PD-T056 (OPEN), PD-T075 (PARTIAL, U2 OPEN), PD-T143 (PROVED) and PD-T146 (MEASURED) keep both their status and their statement.

**IDEAS — 15 rows changed, each equal to its literal NEW block cell for cell.**
- The rows are 158, 160, 162, 168, 248, 250, 251, 253, 255 and 262–267.
- The six homes 248, 250, 251, 262, 266 and 267 only append to their alias and disposition columns.
- IDEA-168, the extra parent, matches its receipt `extra_parent_updates` exactly and changes additively.

**Other registries.**
- CURRENT changes in one paragraph, and the crosswalk in one paragraph. All other bytes, including other topics' rows and sections, are identical.
- RESULTS.md is a pure append. The new section equals the topic results file, with its header demoted and `../` links rewritten.

**Proposal file since `29a78ec`.**
- All 28 OLD blocks and their titles are byte-identical.
- Only the NEW parts of seven pairs changed: R2-1 non-inclusion wording, AC acceptance, the N2 and N3 wording, and audit-stage attribution. No mathematical statement changed.

**Transformations `build()` makes beyond literal replacement.** Each was reproduced and is documented:
- final-ID substitution;
- 8 continuations folded into 7 rows;
- "(alias PD-Txxx)" dropped from new first cells;
- companion links added on T324/T325;
- the crosswalk header rewritten;
- the RESULTS section taken from the topic results file.

**P3 attribution.** It now cites the merged path `topics/padua-literature-20261103/p3-comparison.md`, blob `4741c38943f37ae05ba525552ceafc3f32ac5537`, which is identical at `b4d292e`. The coverage limits are unchanged, and no added shared line says "unmerged".

## Check 6 — durable source consistency: PASS

- **IDs and statuses.** For all 19 records, the final ID and status agree across PROOF_STATUS, the map, the theory title, the "Final registration" line and the primary "Overall status". IDEA-414–424, PD-T324–339 and PD-N116–118 each appear exactly once, and no gap ID appears in any registry.
- **Frozen files.** These are identical at `29a78ec`, `a3f03be`, `0299fcf` and `1fb21c1`:
  - L1 `f27a22c4…`
  - L2-01 `44498c62…`
  - n1 contract `9d857e30…`

  They match the pins in the checkers. T324 and T325 link their companions.
- **Science files.** No code or evidence file changed. evidence-manifest.json changes only its inventory and rules metadata.
- **Changed theory, method and response files (26).** All fenced blocks and every Proof section are preserved. The only removed theory line is the title, where the alias becomes the final ID.
- **Inherited files.** e1-05, e1-06 and e3-11 keep their full base bytes as a prefix. Each appended tail equals its fenced block in inherited-target-updates.md or pd-t143-cross-reference.md. e3-11 cites corollary (9), which exists, scoped to model (1).
- **Links and whitespace.** All 120 links on added shared lines resolve from each file's own location. `git diff --check` is clean.

## Check 7 — application refresh: PASS

- **Reconstruction.** The five outputs are reconstructed byte-identically from the `a3f03be` blobs, the proposal and the map.
- **Receipt.** The receipt's `after` hashes equal the committed blobs, and its `before` hashes equal the base. Its 28 operations equal a fresh build. A fresh rehearse-mode receipt equals the committed one minus `previous_receipt`.
- **Guard.** The `--update-applied` guard asserts the same base, that the prior `before` hashes equal the base, and that the current files equal the prior `after`. It writes the prior receipt with exclusive create.
- **Prior receipt.** `6deaa2de…` sits at a `/tmp` path that is absent here and was never committed, so it is attested only.
- **Peer branches.** Shared files did not change between `e5fbd85` and `0299fcf`. Neither PR27 `3dda890` nor PR28 `d879256` touches the five registries, the batch ledger or tracks/.

## Executions (all in scratch, run with `python3 -B`)

1. `check_registration.py --receipt …` on a pristine `0299fcf` clone: exit 0, PASS in applied mode, 28 literal pairs.
2. Own `recon.py`, which imports `build()` and writes to scratch: exit 0. All five files are byte-identical under `cmp`, and the receipt and operations are equal.
3. Restored the clone's registries to `a3f03be`, then ran `apply_registration.py --base a3f03be --receipt <scratch>`: exit 0, REHEARSED, 28 pairs. `check_registration.py --rehearse` then passed. The clone was restored afterwards.
4. `finalize_metadata.py` in the clone: exit 0 ("19 claims and 19 candidate records"); `git status` stayed empty, so it is idempotent.
5. Negative test: appended one line to the clone's results file. The checker raised `AssertionError: Application operations changed`. The file was restored.
6. An independent naive literal applier gives CURRENT identical. The other four files differ only by the documented transformations.

## Findings

| ID | Severity | Location | Finding | Remedy |
|---|---|---|---|---|
| P3-APP-1 | MINOR | Applied registries, batch ledger, e1-05 addendum | Stage text goes stale at readiness ("preparation audit pending" in 19 PROOF rows; "awaits preparation audit"; "PR24 stays draft"), and the receipt locks it. | Amend the NEW blocks and the results file, re-apply with `--update-applied`, and append dated lines to the ledger and e1-05. |
| P3-APP-2 | MINOR | handoff11 check 7 and record.md | "Reconstructs from pinned base/proposal/map" omits a fourth input: `build()` also reads the live `results/padua-lanczos-frontier-20261105.md`, which the receipt does not hash. | State that input. |
| P3-APP-3 | NOTE | ID_CROSSWALK L5-02/L5-03 rows | Each row lists the other candidate's alias, though the two remain distinct candidates. | Optional. |
| P3-APP-4 | NOTE | Applied text | Cosmetic wording: "failed IDEA IDEA-420 subroute"; "historical audit-03 PARTIAL" means the inherited Codex audit-03; the e1-05 addendum repeats a sentence; the crosswalk header rewrite is not mentioned in the amendment. | Optional. |
| P3-APP-5 | NOTE | `previous_receipt` | The prior receipt `6deaa2de…` is unavailable, a disclosed retention limit. | None. |
| P3-APP-6 | NOTE | LOG at `0299fcf` | Forward link to handoff11, which resolves at HEAD. | None. |

## Orchestrator dispositions

| Finding | Disposition |
|---|---|
| P3-APP-1 | FIXED. NEW-block amendment plus a guarded `--update-applied` re-application. The results file was updated, and dated lines were appended to the batch ledger and e1-05. See audit-03.md. |
| P3-APP-2 | FIXED. Stated in audit-03.md and preparation/record.md. |
| P3-APP-3 | Recorded as cosmetic; the candidates remain distinct. |
| P3-APP-4 | "historical Codex audit-03" FIXED. The rest is recorded as cosmetic. |
| P3-APP-5 | For this refresh, the prior receipt `75892f5e…` is now committed at preparation/application-receipt-before-audit03.json. |
| P3-APP-6 | No action. |
