# Audit05 sub-report A: response04 (G1–G7 and returned items) plus section F provenance, budget and storage

- **Auditor:** Claude, Opus 5.5 (`claude-opus-5-5`), xhigh. Independent protocol/technical subagent. It made no Git or repository change.
- **Rules:** read at `acf0fbc`. They are unchanged since `04ef28b`; the last rules change is `be9a831`.
- **Inputs:**
  - Candidate `ec5c089f35fa2002a2ed2b293a41034364380170`. Head `acf0fbc` changes only the status line of handoff 19 and adds handoff 20.
  - `git ls-remote`: main is `f70a260`; the branch is at `acf0fbc`.
- **Execution:** only in `git archive ec5c089` copies under `scratchpad/a5-A/`, with the venv Python 3.13.18. Nothing ran in rerun5.
- **Novelty scope:** none, so the full read of `state/IDEAS.md` was omitted. The G6 review covered comparison wording only.

## Executions

1. `artifact_manifest.py --verify` passes: 362 artifacts, 2,281,441 bytes.
2. Mutation controls, each on a fresh copy:
   - The control copy exits 0.
   - Each of the following exits 1: a bit flip in `code/fd3_certify.py`; a bit flip in `evidence/fd3-certificate.json`; a bit flip in the inherited `tracks/lattice-unisolvence/code/c3_rank.py`; an added `evidence/zz-extra.json`; an added `code/notes.txt`; a deleted `evidence/fd4-lee.json`.
3. Regenerating the master gives a byte-identical file: 18,976 bytes, SHA256 `a297095a…7040`.
4. `pdpr_manifest_check.py --output <scratch>` passes 44 controls; the historical receipt had 45 (see N5).
5. The retired command `r08_hygiene.py pins` still fails with `AssertionError: code/artifact_manifest.py`. That is consistent with its retirement; no pass is claimed anywhere.
6. G1, checked with my own exact script:
   - The x3 map u→240−u carries the (1,17,212) node set exactly onto (1,17,28) (L=480, 120 nodes).
   - All 8 orbit labels are hyperoctahedral images of that set, and (1,17,28) is their lexicographic minimum.
7. G5: `evidence/u3-f.json` has exactly 2 positives over n3..8, both at n5 with tie_count 2. The tie set is therefore the same under any tolerance. `u3_constructions.py:158` (absolute `<=1e-9`) is unchanged.
8. P5: the counts 45/48 at n6 and 100/100 at n8 match the results table and audit04 D.
9. Storage, from `git ls-tree -r -l ec5c089` over json/txt/out/gz/stdout/csv/jsonl:
   - Repository: 8,672,675 bytes in 1,760 files, within 10 MB.
   - Topic: 1,676,496 bytes in 283 files. For comparison, 04ef28b had 8,338,560 and main has 6,996,179.
   - The largest generated topic file is 29,229 bytes. Seven new evidence files lie between 16 and 32 KiB: fd4-qr-n13/14/15/16-nodes, fd4-qr, fd2-exact and fdq-qr-replay. The master is 18,976 bytes.
   - Only prose and code exceed 32 KiB: LOG, pruning-protocol and pdpr_run.py.
10. Provenance sweep over the 52 new code and evidence files:
    - Every code hash in a receipt equals the committed code.
    - `fd2-optimize-failed` matches the pre-repair hash 754a9c4c.
    - The repair hash 7b844e2c was published in gates.md at 3bea991, before the results commit.
    - Exceptions are M7–M9.
11. Links: all 789 local links and anchors in the 94 changed Markdown files resolve, except the link to handoff 20, which exists only at acf0fbc.
12. `git diff --check 04ef28b ec5c089` reports a blank line at EOF in `final-d1/gate.md` and `final-d1/protocol.md` (introduced in f9ab1c6).

## Verdicts on handoff 20, section A

- **A1/G1 — verified.**
  - Exact reflection and the full orbit are confirmed.
  - No evidence JSON was modified, so the old bytes are preserved.
  - No score or maximality claim is made; non-maximality is stated and the log 3 gap is recorded.
  - Missed location from audit04 A2: `report-round08.md:84` (M1).
- **A2/G2 — verified.**
  - The original 176-step, 120.7177 s failure is preserved.
  - The current disposition is retained, hardware-dependent MEASURED evidence, with no hardware-independent rejection.
  - Missed location from audit04 B2: `continuation-results.md:28` (M2).
- **A3/G3 — verified.** The retirement note is dated, both pins JSON files are byte-unchanged and no fabricated pass exists.
- **A4/G4 — verified for every parent that audit04 listed, and for R08-minima → D4-minima.**
  - All 26 aliases map to IDs that carry the agent component and are used in canonical records.
  - Malformed strings remain only in the alias table and the frozen `audit-04/novelty.md`.
  - No final allocation was made.
  - Residues: M3 and M4.
- **A5/G5 — verified.** The disclosure is correct, the historical code is untouched and the invariance argument holds (execution 7).
- **A6/G6 — verified.**
  - The comparison distinguishes CATCH moment compression, L2 frame sparsification (Christoffel, MSS), physical unweighted OLS, integer repeats and sampled sup-norm goals.
  - dim Π₃₂ = 6545 > 1377 is correctly stated not to decide compressibility.
  - Source gaps remain explicit.
  - The Gunzburger–Teckentrup values and U2's 3.15587/5.54401 match their sources.
  - Residue: M12.
- **A7/G7 — verified.**
  - Nine IDEA records with every template field, plus a disposition table.
  - H is deferred with a resume condition; FORCE-N is abandoned without a PD-N.
  - next-01, next-02 and next-03 are each disposed.
  - Pruning is 5/15 used, with 10 rounds frozen.
  - The P5 record is in THEORY form: MEASURED, REJECTED: failed for the first-pair goal only.
  - Residues: M11 and N8.
- **Returned items and AC decisions.**
  - A1-W1, NV-F1 and NV-F3 are done. NV-F6 is only partly done (M15).
  - Both deviation records end with exactly "Accepted by AC 2026-11-08 (see LOG)."
  - E4, storage, deviations and the lattice boundary are presented as settled in response04, the LOG, the final report, the PR body and handoff 20.
  - Exception: older sections of the results file (M5), plus one Open-items line (M6).
  - The E4 application arithmetic was spot-checked and holds: 38n³/27; 19n³/108; f(109) = −9809 and f(110) = 2312; D_k ≤ (k+1)²; s = 8.
- **Protected bodies.** `git diff 04ef28b ec5c089` shows nothing under audit-0*, the fixes, frontier-assessment, frontier-2026-11-08 or handoffs. acf0fbc changes only the handoff 19 status and adds handoff 20.
- **Budgets.**
  - D1 4/6 (rounds 5–6 not run), D2 3/3, D3 1/1, D4 2/2, D5 3/3 RECORD. These match rounds.md, the LOG increments, the item ledgers and the PR.
  - The D2 repair counts inside R3: the original attempt plus 499 new ones stays within the 500-attempt budget.
  - Replays and repairs count zero rounds. T/U/P counts are unchanged and frozen.
- **Trailers.** All 11 commits carry `Agent: Codex` and `Model:` (see N1).

## Changes to pre-existing theory records

All are dated or labelled; none is silent.

1. Half-shift n7 label → (1,17,28); the values are unchanged.
2. u2c disposition: REJECTED: failed → retained, hardware-dependent. Status remains MEASURED.
3. Packing-source header status wording harmonized (N6).
4. Finite-complement split wording.
5. P5 rebuilt in THEORY form with a new provisional PD-N ID; the claim is unchanged.
6. prune-next-02: retained → deferred.
7. Split headers.
8. 26 ID re-keys.
9. Dated settled-E4 sections.

## Findings

**BLOCKING: none. MAJOR: none.** Every finding below is MINOR and eligible for an exact OLD → NEW fix.

- **M1** `report-round08.md:84`
  - Old: `|7|(1,17,212)|136.690399705|loses QR and Leja|`
  - New: `|7|(1,17,212); current label (1,17,28) by exact x3-reflection ([audit04 G1](attempts/T8-round08.md#audit04-g1--n7-exact-tie-label-correction-2026-11-12))|136.690399705|loses QR and Leja|`
- **M2** `continuation-results.md:28`
  - Old: `Park the frozen120-second extension.`
  - New: `Park the frozen120-second extension (revised 2026-11-12: retained as hardware-dependent MEASURED evidence; [audit04 G2](u2-continuation.md#audit04-g2--hardware-dependent-c1-disposition-revision-2026-11-12)).`
- **M3** `theory/t7-finite-reduction.md:4`. Audit04 missed this nonreciprocal pair: the child PD-N T7-09 says "Split from … T7-03", and line 145 already maps it.
  - Old: `Split from: none. Split into: none. Supports the OPEN T7 target.`
  - New: `Split from: none. Split into: PD-N?padua-3d-20261106-codex-T7-09 ([t7-one-phase-refutation.md](t7-one-phase-refutation.md)), the refuted one-phase-per-stratum inference already mapped below. Supports the OPEN T7 target.`
- **M4** The n4..7 split should use full IDs in both files.
  - `final-d4/finite-minima.md:4`
    - Old: `Split from: R08-minima, its n4..7 cases with the same exact statement.`
    - New: `Split from: PD-T?padua-3d-20261106-codex-R08-minima ([r08-lattice-minima.md](../theory/r08-lattice-minima.md)), its n4..7 cases with the same exact statement.`
  - `theory/r08-lattice-minima.md:4`
    - Old: `Split into: [D4-minima, packing-free n4..7 cases](../final-d4/finite-minima.md).`
    - New: `Split into: PD-T?padua-3d-20261106-codex-D4-minima ([finite-minima.md](../final-d4/finite-minima.md)), packing-free n4..7 cases.`
- **M5** `results/padua-3d-20261106.md` (orchestrator-owned; feeds RESULTS.md) still presents settled decisions as pending.
  - (a) Lines 152–153.
    - Old: `the sharp log³ corollary is proposed as **PROVED with explicit LITERATURE` / `  dependency** under the uniform E4 convention for AC.`
    - New: `the sharp log³ corollary is **PROVED with explicit LITERATURE` / `  dependency** under the E4 convention AC approved on 2026-11-08 ([E4 checks](../topics/padua-3d-20261106/final-d5/e4-verification.md)).`
  - (b) Line 179.
    - Old: `reading/provenance limits for AC.`
    - New: `reading/provenance limits, accepted by AC on 2026-11-08 as disclosed.`
  - (c) Lines 234–235.
    - Old: `Original timing/scope deviations remain` / `for AC in [the canonical disclosure]`
    - New: `Original timing/scope deviations were accepted` / `by AC on 2026-11-08 as disclosed in [the canonical disclosure]`
  - (d) Lines 36–37.
    - Old: `Formal Claude audit remains` / `pending, with explicit uncovered prior/source-verification work.`
    - New: `Claude audit04 (2026-11-08) later` / `accepted the mathematics; uncovered prior/source-verification work stays explicit.`
  - (e) Bold labels.
    - Old: `**PROVED with an explicit imported packing theorem:**`
    - New: `**PROVED with explicit LITERATURE dependency (packing theorem):**`
    - Old: `**Verified known construction, PROVED transfer with LITERATURE premise:**`
    - New: `**Verified known construction; transfer PROVED with explicit LITERATURE dependency:**`
- **M6** `theory/r08-negative-t9-unshifted-minimal-cubature.md:68`. The Open-items line contradicts the appended settled section.
  - Old: `E4's exact source-dependent label is pending AC’s convention decision;`
  - New: `E4's exact source-dependent label was settled by AC on 2026-11-08 (dated E4 section below);`
- **M7** `evidence/fd4-manifest.json` pins nine `final-d4/*.md` prose files. WORKFLOW says new checkers must not pin prose. Two of the pins (lebesgue-intervals.md and results.md) already mismatched at first publication. No checker reads the file, but `final-d4/results.md:77-78` says it "identifies all worker artifacts".
  - Old: `artifacts and generated bytes; raw scratch remains regenerate-only.`
  - New: `artifacts and generated bytes; raw scratch remains regenerate-only. Dated note 2026-11-12: its nine final-d4 prose rows are a historical return snapshot, not verification pins (lebesgue-intervals.md and results.md changed before publication); current code/data integrity is the master manifest's --verify.`
- **M8** The PROVED status of D4-minima depends on `audit-04/code/A1/aud_enum.cpp`, which `fd4_lee.py:11` compiles. The master manifest does not cover that file; only the fd4-lee/fdq-lee receipts pin it. The g++ version is not recorded, and the "independent" replay used byte-identical binaries.
  - File: `final-d4/finite-minima.md`.
  - Old: `endpoint, not assumed optimal. No catalogue optimality label is used.`
  - New: `endpoint, not assumed optimal. No catalogue optimality label is used. Verification limitation: the second enumerator source audit-04/code/A1/aud_enum.cpp (10,115 bytes, SHA256 d39563b9340bb0e8384031dac36e2050efb0ab6953c64e165e4006eaca9be503) is outside the master manifest's code/evidence scope and is pinned by fd4-lee.json and fdq-lee-replay.json; the g++ version was not recorded, and both executions used identical binaries.`
  - Adding the file to the master `inherited_inputs` instead would be a material change, so that choice belongs to the developer.
- **M9** `evidence/fdr-d2-quality-replay.json` has no command and no code identity, and the root SVD script is uncommitted.
  - File: `final-root-checks.md`.
  - Old: `[Receipt](evidence/fdr-d2-quality-replay.json) pins the actual input and environment.`
  - New: `[Receipt](evidence/fdr-d2-quality-replay.json) pins the actual input and environment; it records no command or code identity, and the replay script is not committed (the next paragraph is the reproduction specification).`
  - Committing the script would be better, at the developer's option.
- **M10** `pruning-manifest.md`. Append at the end: `Dated note 2026-11-12: under AC's approved 32 KiB allowance (LOG 2026-11-08, 2026-11-12) artifact_manifest.py and pdpr_manifest_check.py use 32,768-byte limits; the committed receipt above records the earlier 16 KiB checker (SHA256 165d444a…4968). Current-checker runs are regenerate-only; at 32 KiB the plus-40 fixture fits (20,764 bytes), so the oversize-rejection control no longer fires.`
- **M11** `pruning-next-questions.md:264`
  - Old: `next-02 is deferred.`
  - New: `next-02 is deferred (its earlier disposition read “equal-order comparison retained; richer pool deferred pending positive support evidence or a specific coverage need.”).`
- **M12** `gate-addendum-audit04.md:20`
  - Old: `so that generic bound alone guarantees no useful reduction here.`
  - New: `so that generic bound alone does not guarantee any reduction here.`
- **M13** Remove the trailing empty line at EOF in `final-d1/gate.md` and `final-d1/protocol.md`.
- **M14** Stale "pending" process text, to replace with a link to audit-05 when it is recorded:
  - `final-d4/finite-minima.md:32`;
  - `final-d4/lebesgue-intervals.md:92`;
  - `final-d4/results.md:71-72`;
  - "Formal focused Claude audit is next" in the results top section. Keep process text out of RESULTS.md.
- **M15** Spacing in the results top section:
  - `certified20-node` → `certified 20-node`
  - `sampledLambda30.0121` → `sampled Lambda 30.0121`
  - `numerical4.05benchmark` → `numerical 4.05 benchmark`
  - `whole-cubeLambda` → `whole-cube Lambda`
  - `minima92/178/304/486` → `minima 92/178/304/486`
  - `dimPi_(n−1)` → `dim Pi_(n−1)`

  The new LOG and report text repeats the pattern.

## Notes (no action)

- **N1** `Agent:` is separated from `Model:` by a blank line, so git parses only Model as a trailer. Earlier Claude commits did the same. Do not rewrite history.
- **N2** The new receipts have no execution UTC except fd4-input-inventory (09:20:44, after the D4 prereg at 09:13:43). The commits span 09:06–09:44, so the claim that each protocol was published before its run rests on commit order and attestation. `fd2-runtime.json` records `recorded_after_R1_R2: true`.
- **N3** 1.33 MB of headroom remains under 10 MB, and main alone exceeds the 5 MB baseline. This goes to PR discussion, as the PR body already records.
- **N4** The "362 producer artifacts" include supplemental receipts.
- **N5** The 32 KiB guard in `render_manifest` is now covered only by inspection.
- **N6** The t9-r06-packing-source status line was reworded in place with no semantic change.
- **N7** The U3-01/02 children name their parents by title, not ID; the parents list them.
- **N8** The pruning IDEA records share boilerplate fields. "Retained" is not one of the template dispositions.
- **N9** `t8-r08-halfshift-measurements.md:12-14` says the executed scans "yield" the tabled sets, but the n7 label in the table is now transferred. History clarifies this.
- **N10** The PR #33 body states the allowance use, the settled decisions and audit05 PENDING correctly.

## Residual uncertainty

- Run chronology rests on attestation (N2).
- The D4 C++ toolchain is unrecorded (M8).
- The root D2 quality replay cannot be rerun from committed code (M9).
- Sections B–E are outside this sub-report.
