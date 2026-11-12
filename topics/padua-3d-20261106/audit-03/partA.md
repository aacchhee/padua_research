# Audit 03 Part A: response-02, manifest v2 and metadata repairs

- Auditor: Claude Opus 5.5 (`claude-opus-5-5`), xhigh. Audit only: no Git state changed, no repository file edited.
- Candidate: `696bca5fe8842b8b99ec298381c948206be79548`. Head `54d554a` only changes handoff-06's status line and adds handoff 07.
- Base for diffs: `7afa6a5`.
- Executions: only in a `git archive` copy under `.../scratchpad/a3-partA/`, with TMPDIR inside it.
- Environment: Python 3.13.18, numpy 2.3.5, scipy 1.17.0, sympy 1.14.0, mpmath 1.3.0, one BLAS/OMP thread, no `-O`.

## Verdict

**Part A accepted. No BLOCKING, MAJOR or material finding.**
- C1–C4 and n1–n6 are each fixed or explicitly limited, as response-02 states.
- No accepted statement, proof or status changed. Protected audit and handoff bodies are intact.
- Manifest v2 verifies, and every requested mutation class fails it.
- The T8 pin repair reproduces the D0 and n2 science and the raw hash.
- The T9 companion reproduces and invents nothing.

Seven MINOR hygiene items (A3-1..7) can all be fixed in place. Five NOTEs follow them.

## Per-finding review

| Item | Verdict | Evidence |
|---|---|---|
| C1 | **Fixed.** Old wording is kept as history under dated withdrawals. Counters were 0/25 at the Part A commit 7f773eb. | rounds.md:28-32; attempts/T7.md:3-12; T8.md:3-12,147-155; T9.md:3-13; report-continuation-04.md:3-12; report.md:240-249. Structure issues: A3-2, A3-3. |
| C2 | **Fixed, labelled retrospective.** All required items present: search terms; IDEA-027/029/044/047/109/120/209 (+049); LIT-010/192/307/374/378/389/413 (+387); OBST-11; Subbotin Cor. 1. States "not a new prospective gate" and "cannot be backdated". The T10 gate first appears in 7f773eb, before T10 attempts and evidence (26434e7). | novelty-gate-T9.md:46-96. Every cited IDEAS/INDEX row exists and matches its summary. |
| C3 | **Fixed, one canonical record.** `git diff 51c031a e80e000` confirms exactly the disclosed edits: the IDEA-203–205 label replaced in two rows; LOCALIZED "Screened, deferred" → "Equivalent…". No PD-N invented; AC acceptance not presumed. | response-deviations-02.md:9-25; novelty-gate-T9.md:46-56 |
| C4 | **Fixed, provisional.** Mappings: PD-T T7-04 → PD-N T7-08 (header/kind and alias history only). New PD-N T7-09 (t7-one-phase-refutation.md) restates the accepted counterexample (same H, phases, determinant). PD-T T7-03 keeps the positive reduction. | t7-rank-two.md:1-5,66-76; t7-finite-reduction.md:105-113,137-144 |
| n1 | **Fixed in the old files.** All 21 stale m5 sentences replaced (0 remain). T3 label, deviation pointers and response-01 "integration notes" repaired; m11 withdrawn in deviations-01. **Regression:** response-02 itself cites nonexistent "integration notes" (A3-1). LOG.md:186 stays as history, but its pointer at LOG.md:337-338 names the wrong file (A3-6). | `git grep "integration note"` hits only response-02.md:37,81 and the audit-02 quotations |
| n2 | **Partly fixed.** Provenance limit is honest (preregistration-T7 dated note; deviations-02:27-35); results:71 now says "Computer-assisted". But the claimed "full namespaced mapping and per-candidate aliases" sit in nonexistent integration notes. attempts/T7.md:69-80 still mixes IDEA and theory suffixes, now colliding with PD-N T7-08/09 (A3-1). | |
| n3 | **Fixed.** Retrospective, not backdated, E row; PD-N T8-02 pointer; rerun wording; pins (§5). | gates.md:169-175; t8-phase-obstructions.md:103-113 |
| n4 | **Fixed.** 2420 vs 4592 explained; Minkowski 1904 named; normalization dropped (linear invariance); unions added to escapes. Status stays CONDITIONAL. | t9-squarewave-lower.md:86-93; t9-packing-conditional.md:21,35-42 |
| n5 | **Fixed** in theory, attempt and literature records. The T9 gate table still credits only the T1 sketch (A3-5). | t8-cyclic-reduction.md:115-116; t9-haar-packing-reduction.md:98-104; attempts/T9.md:10-13 |
| n6 | **Mostly fixed.** Ten T9 IDEA records; pointers; T5-04 made single-canonical; allocation deviation made canonical (deviations-02:45-53); companion and inventory added. 8 old-slug IDs remain (A3-4). The PR body must still name the Sol-high T8 proofs at PR preparation. | |

## Checks (2)–(7)

**(2) Accepted mathematics unchanged.** I read every removed line of the modified T1–T9 theory files (`git diff -U0`). Each is one of:
- a slug change, stale process sentence or rerun/pointer wording;
- the C4 header/kind change;
- a requested scope clarification (t9-packing-conditional: unions excluded, "normalization" removed).

No statement, proof or epistemic status changed.

**(3) Protected bodies.** `git diff 7afa6a5 696bca5` is empty for `audit-0*` and for `handoffs/0[1-6]*`. `54d554a` changes only handoff-06 line 3.

**(4) Manifest v2.**
- `--verify` → PASS: 154 artifacts (54 code, 100 evidence), 728,307 bytes; the manifest is 15,648 bytes.
- The format is lossless: one map, `{code, evidence}` × filename stem → `[bytes, sha256]`, with fixed `.py`/`.json` suffixes. Inherited inputs are full `{path, bytes, sha256}` rows for c3_lebesgue.py and c3_rank.py.
- Removing v1's `recorded_commands` loses nothing: those strings are the `command` fields of unchanged, hash-pinned receipts.

Mutations, each on a fresh copy:
- **FAIL (exit 1):** code byte (appended, or same length); evidence byte; c3_rank or c3_lebesgue byte; c3_rank deleted (FileNotFoundError); added `code/extra.py` or `evidence/extra.json`; file deleted, renamed or swapped; `inherited_inputs` removed.
- **PASS (outside scope, N1):** `code/extra.txt`, `code/sub/extra.py`, `evidence/extra.txt`, `evidence/sub/extra.json`; edits to manifest prose or `schema`.

Verify has no silent fallback; the compact-JSON branch is generation-only.

**(5) T8 pins.**
- preregistration-T8.md hashes: f089f36d… at 1c75e1f and 51c031a; 8cad326a… from e80e000 on. These match the historical receipts: f089 for controls/census/odd/phases, 8cad for even-family.
- I ran `t8_cyclic.py controls --scratch-dir S` and `census --n 2 --scratch-dir S`, then compared with the committed receipts.
  - Differences: only `seconds`, `source_sha256` (5077782… old vs 9615fd7f… new), `status`, `versions` and n2's `raw_path`.
  - All science fields match, and the `preregistration_sha256` f089 pin is reproduced.
  - Raw n2 file: 962,991 B, sha 0fe94978…b61f, identical (15,733 classes / 95 sets / 2 full-rank).
- `check_response02_t8.py` → PASS. Historical receipts keep their executed old-source hash.

**(6) legacy_t9_metadata.py** → PASS under 3.13.18.
- Science is equal, excluding `seconds`.
- All 26 raw arrays are identical by bytes and sha to the committed companion.
- t9-checks.json and t9-maxima.json are byte-unchanged.
- `historical_commands` match handoffs/05-audit.md:170-171 and attempts/T9.md:81-83.
- The new versions are labelled as new execution metadata. Nothing is invented.

**(7) T7 qualifications.**
- The reading qualification is canonical in deviations-02:62-71. It is linked from novelty-gate-T7-round06.md:32 and attempts/T7-round06.md:132, with no claim that later reading cures it.
- The D0 snapshot gap is disclosed at attempts/T7-round06.md:193-201 and in LOG. No commit holds a t7_r06_search.py with sha da4c5339…; the only version (26434e7) is a3960922…, which is what the frozen replay pins.
- Neither is overstated. A wording issue in the qualification is A3-7.

## New findings

- **A3-1 MINOR (n1 regression, n2 partial).**
  - response-02.md:36-37 and :81 cite nonexistent "integration notes".
  - attempts/T7.md:69-80 keeps bare suffixes that mix IDEA and theory IDs. IDEA T7-08/09 now collide with PD-N T7-08/09.
- **A3-2 MINOR (rounds.md structure).**
  - The handoff-06 final stopping record (lines 34-44) sits under "## Historical handoffs01/04 counts".
  - Line 28 says "preceding" for stops that appear below it.
  - The "Handoff04 final boundaries" section (107-122) has no adjacent withdrawal pointer.
- **A3-3 MINOR.** results/padua-3d-20261106.md:56: the handoff-04 report "collects … stopping rules", with no C1 withdrawal.
- **A3-4 MINOR.** Old-slug IDs remain: attempts/T9.md:24-30 (7) and theory/t8-r06-parity-admissibility.md:31 (1).
- **A3-5 MINOR.** novelty-gate-T9.md:28 credits only the "T1 open-class packing sketch" for T9-HAAR/PACK. The n5 correction is absent from the gate.
- **A3-6 MINOR.** LOG.md:337-338 says the model attribution is withdrawn "by that dated record" (deviations-02). The withdrawal is in deviations-01 m11.
- **A3-7 MINOR.** deviations-02:66-67 calls "Lanczos registration range641–690" "unrelated".
  - IDEA IDs stop at 611, so these are state/IDEAS.md lines 641–690: rows IDEA-081..128.
  - That range includes IDEA-109 (cubature as joint eigenvalues) and IDEA-120 (3D Padua via joint spectra). Both are shortlisted in the T9 and T10 gates.
  - Mitigation: the inherited T7 gate already treats IDEA-120 (novelty-gate-T7-round06.md:19). Still, "unrelated" overstates it.
- **N1 NOTE (pre-existing v1 scope; no current exposure).**
  - The guard pins only non-recursive `code/*.py` and `evidence/*.json`. Other suffixes or subdirectories would be silently unpinned; none exist now.
  - Only the c3_lebesgue/c3_rank helpers are pinned. replay.py's c0_catalogue.py is pinned only via evidence/replay.json.
  - So handoff 07's "rejects add-file changes" holds only for those suffixes. Hardening it is a code change for the developer.
- **N2 NOTE.**
  - t8_cyclic.py:24-25 calls `tempfile.mkdtemp` at import. Each import, including with `--scratch-dir` or from t8_phases, t8_even_family or the checker, leaves an empty TMPDIR directory; I observed one per invocation.
  - :138 hard-codes a status citing audit-02 reruns into every future receipt.
  - Fix at the developer's next touch of the code.
- **N3 NOTE.** check_response02_t8.py compares only the n2 receipt with history. Controls are asserted but not receipt-compared; my comparison of them shows a scientific match.
- **N4 NOTE.** cold-storage.json `source_commit` was repointed from 7407e13 to 7afa6a5. The old value moved to `historical_source_commit`, so nothing is lost, but the field's meaning shifted.
- **N5 NOTE.** t7-rank-two.md:4 uses "Split from:" for a whole-record re-kinding. Under templates/THEORY.md:5, a split names the exact original claim. Optional fix F10.

## Proposed in-place MINOR fixes (separate commit)

- **F1** response-02.md:36-37
  - Old: `not exhaust a direction. Requested original-location text is in the` / `integration notes; no retroactive approval of the old stops is asserted.`
  - New: `not exhaust a direction. The dated withdrawals are in rounds.md,` / `attempts/T7–T9.md and report-continuation-04.md; no retroactive approval of the old stops is asserted.`
- **F2** response-02.md:81
  - Old: `Full namespaced mapping and per-candidate aliases supplied in integration notes for the route worker.`
  - New: `The C4 mapping and aliases are in the table above, theory/t7-rank-two.md and theory/t7-one-phase-refutation.md; attempts/T7.md's bare labels are history, decoded by its dated route-map note.`
- **F3** attempts/T7.md: insert after line 69 (`## Route map (full dispositions below)`):

  `Dated audit-03 label note (2026-11-06): the ID-suffix column names IDEA?padua-3d-20261106-codex-T7-NN candidates. Disposition-column suffixes are theory IDs: T7-03 = PD-T?padua-3d-20261106-codex-T7-03 (its refuted one-phase inference is now PD-N?padua-3d-20261106-codex-T7-09); T7-04 = historical PD-T?…T7-04 = PD-N?padua-3d-20261106-codex-T7-08; T7-05/T7-06 = PD-T?padua-3d-20261106-codex-T7-05/06; T7-07 = PD-N?padua-3d-20261106-codex-T7-07. See [response-02](../response-02.md), C4.`
- **F4** rounds.md
  - Line 28: `the preceding direction-wide stops` → `the direction-wide stops recorded below under "Handoff04 final boundaries"`.
  - Move lines 34-44 (`Final handoff06 stopping record: …`) unchanged to directly after line 24.
  - After line 107, insert: `Withdrawn as direction-wide stops under audit-02 C1 (2026-11-06); see "Historical handoffs01/04 counts" above. Preserved as history.`
- **F5** results/padua-3d-20261106.md:56
  - Old: `collects the new scopes, evidence and stopping rules. No historical novelty`
  - New: `collects the new scopes and evidence; its direction-wide stops are withdrawn under audit-02 C1 (see the topic rounds.md). No historical novelty`
- **F6** Slug normalization
  - attempts/T9.md:24-30: every `padua-3d-codex-` → `padua-3d-20261106-codex-`.
  - theory/t8-r06-parity-admissibility.md:31: `PD-N?padua-3d-codex-T8-02` → `PD-N?padua-3d-20261106-codex-T8-02`.
- **F7** novelty-gate-T9.md: append after line 96:

  `Attribution (audit-02 n5, recorded 2026-11-06): the T9-HAAR/PACK packing sketch, fold bound, 2-D check, 19n^3/108, threshold 110 and escape list were supplied by Claude's [handoff04](handoffs/04-work.md); the "T1 open-class packing sketch" in the table above is an additional lead. See [T9-HAAR](theory/t9-haar-packing-reduction.md).`
- **F8** LOG. Keep it append-only and do not edit lines 337-338. Add to the audit-03 LOG entry:

  `Correction to the 2026-11-06 PartA entry: the unsupported AC model-attribution is withdrawn in response-deviations-01.md (m11 addendum); deviations02 withdraws the stronger T9 gate-timing claim.`
- **F9** response-deviations-02.md:66-67
  - Old: `supplemented before mechanisms, but an unrelated Lanczos registration` / `range641–690 was reread after initial runs as an additional completeness`
  - New: `supplemented before mechanisms, but state/IDEAS.md lines 641–690 (Lanczos registrations IDEA-081–IDEA-128, including IDEA-109 and IDEA-120; IDEA-120 was already treated by the inherited T7 gate) were reread after initial runs as an additional completeness`
  - This is a more conservative disclosure. If the developer disputes the range meaning, return it to them; AC decides disputes.
- **F10** (optional) t7-rank-two.md:4
  - Old: `Split from: historical PD-T?padua-3d-20261106-codex-T7-04.`
  - New: `Split from: none; whole record reclassified, historical alias PD-T?padua-3d-20261106-codex-T7-04.`
- **F11** (optional, stale process text) response-02.md
  - Line 22: `Manifest refresh accompanies the evolving new batch.` → `The manifest v2 at 696bca5 pins these code/data files.`
  - Lines 107-110, from `Excluded-file` to `next handoff.` → `Root integration followed in 7f773eb; the focused Claude review is handoff07 (audit-03).`

**Material items for the developer: none.** N1 and N2 are optional code hardening. They are NOTEs, not defects, because no stated claim is false.

## Commands executed (archive copy, TMPDIR in scratch)

1. `artifact_manifest.py --verify` → PASS 154/728307; 18 mutation runs on fresh copies (§4).
2. `t8_cyclic.py controls|census --n 2 --scratch-dir S`, compared key by key with preserved receipts; raw sha 0fe94978…b61f.
3. `legacy_t9_metadata.py --output …` → PASS (12.7 s), 26/26 arrays equal, T9 receipts unchanged (`cmp`).
4. `check_response02_t8.py --output …` → PASS.
5. Git checks: prereg-T8, t8_cyclic and t7_r06_search hashes across history; the 51c031a→e80e000 T9 gate diff; all brief diffs and protected bodies.
6. Link check: the only miss is LOG.md:4 → handoffs/07 (it resolves at 54d554a). All JSON parses; every receipt is < 16 KiB.

## Residual uncertainty

Commit order is not execution order. The T9-timing, T7-pilot and E-gate statements remain attestations, disclosed for AC. No primary sources were re-read; IDEAS rows were spot-checked only.
