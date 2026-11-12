# Audit 05 — auditor MINOR fixes (dated companion note), 2026-11-12

Auditor: Claude, claude-opus-5-5 xhigh audit; edits applied by a mechanical subagent from the audit-05 sub-reports ([A](audit-05/A.md), [D1a](audit-05/D1a.md), [D1b](audit-05/D1b.md), [D2](audit-05/D2.md), [D3](audit-05/D3.md), [D4](audit-05/D4.md), [D5](audit-05/D5.md)).

These are the auditor in-place fixes allowed by `agents/WORKFLOW.md`, "Proportionate audit and records". They are limited to wording and formatting, links, stale process text and recording an already documented decision. They are committed separately from the audit report. No claim, status, ID, disposition, `Split from/into` header, threshold, code, input or evidence JSON is changed. Hash-pinned prose is not edited; its corrections are in this companion note ("companion" below). Pin check: `grep -l <path> evidence/*.json evidence-manifest.json` before each edit. Pinned prose in this round: the nine `final-d4/*.md` rows of `evidence/fd4-manifest.json` (`candidates.md`, `certificate-reduction.md`, `finite-minima.md`, `lebesgue-intervals.md`, `results.md`, and others); no other file edited here is pinned. Line numbers are approximate post-edit positions.

## Applied fixes (direct)

| ID | File:line | Kind | Summary |
|---|---|---|---|
| A-M1 | `report-round08.md:84` | direct | n7 row now reads "(1,17,212); current label (1,17,28) by exact x3-reflection" with link to [audit04 G1](attempts/T8-round08.md#audit04-g1--n7-exact-tie-label-correction-2026-11-12). |
| A-M2 | `continuation-results.md:28` | direct | "Park the frozen120-second extension" gains "(revised 2026-11-12: retained as hardware-dependent MEASURED evidence; audit04 G2 link)". |
| A-M6 | `theory/r08-negative-t9-unshifted-minimal-cubature.md:68` | direct | "is pending AC's convention decision" becomes "was settled by AC on 2026-11-08 (dated E4 section below)". |
| A-M9 | `final-root-checks.md:10` | direct | Receipt sentence now also says it records no command or code identity and the replay script is not committed (next paragraph is the reproduction specification). Dated (audit-05 note). Code and evidence untouched. |
| A-M10 | `pruning-manifest.md` (end) | direct | Dated note: 32 KiB allowance, current checkers use 32,768-byte limits, committed receipt records the 16 KiB checker (SHA256 `165d444a…4968`), the plus-40 fixture (20,764 B) now fits so the oversize control no longer fires; current-checker runs are regenerate-only. |
| A-M11 | `pruning-next-questions.md:264` | direct | "next-02 is deferred" gains its earlier disposition text in parentheses. |
| A-M12 | `gate-addendum-audit04.md:20` | direct | "alone guarantees no useful reduction here" becomes "alone does not guarantee any reduction here". |
| A-M13 | `final-d1/gate.md`, `final-d1/protocol.md` (EOF) | direct | Trailing blank line removed (`git diff --check`). |
| D1a-F2 | `final-d1/finite-frame.md:5,52`; `final-d1/stationary-limit.md:89,93`; `final-d1/spectral-obstruction.md:56` | direct | Dated "Superseded 2026-11-12 (audit-05)" pointer appended after each stale in-progress sentence (completed in D1-03/D1-04 and the R4 [reconstruction](final-d1/reconstruction.md); current status in the [D1 README](final-d1/README.md)); round history kept. |
| D1b-3 | `final-d1/reconstruction.md:45` | direct | "AMO's remark allows an orthogonal nonbasis family" becomes "AMO's remark (p16) extends AMO's obstruction to an orthogonal nonbasis family ... (the p15 sphere/tight-design remark is also AMO's; see the supplemental audit)". |
| D1b-5 | `paper-note-draft.md:33` | direct | "positive rules with N=N_n do not exist for all sufficiently large n" becomes "for every sufficiently large n, no positive rule with N=N_n exists" (the proved quantifier of `final-d1/spectral-obstruction.md`). |
| D2-m1 | `final-d2/outcome.md:43` | direct | RREF-basis scope sentence added after "versus 12/20/30 total.": 10/14/18 nonzeros are basis-dependent (other orders give 9/13/17 or more). |
| D2-m2 | `final-narrowed-report.md:21`; `paper-note-draft.md:81` | direct | "independently replayed" / "after independent replay" now state root replayed the frozen producer code (quality check with a different basis/SVD) and audit-05 independently reimplemented the exact checks. |
| D2-m4 | `final-d2/candidate.md:47`; `final-d2/outcome.md:50` | direct | "an established absence of exploitable 2D structure" becomes "that the 2D calibration shows no exploitable structure (handoff 18 wording)"; outcome gains: D2 did not construct or test a 3D analogue of the Padua Hilbert–Burch shape, so the exploitability conjunct is undetermined. |
| D3-m1 | `final-d3/theory.md:166`; `final-d3/runs.md:81`; `final-d3/candidate.md:46` | direct | Stale "formal audit remains" lines replaced by links to [audit-05](audit-05.md) (and the [supplemental](final-check/d3-audit.md) review). |
| D3-m2 | `final-narrowed-report.md:17` | direct | "rounded-center searchedLambda30.0121" becomes "rounded-center sampled Lambda 30.0121". |
| D3-m3 | `final-d3/theory.md:101` | direct | Proof prose: "two fixed rational coordinates a,b (distinct from the torus shift in the Statement, written a0 below)". Statement text unchanged. |
| D4-m2 (mirror) | `final-d5/source-records.md:77` | direct | Audit05 note: 2311.18656v1 states Lemma 1 without proof, citing Piazzon–Vianello, Optim. Lett. 12 (2018) 63–71, following Bos (DRNA 10, 2017); Prop. 1 proof pp3–4; Lemma 1 proof not locally verified. |
| D5-F2 | `paper-note-draft.md:50` | direct | Kuperberg §6/§7 added to the named predecessors, with gate link. |
| D5-F3 | `paper-note-draft.md:70` | direct | 18/19 packing density attributed to Minkowski 1904 as credited and tabulated by Betke–Henk. |
| D5-F4 | `paper-note-draft.md:74` | direct | "double-Lee-sphere anticode bound", Horak–AlBdaiwi context, locally proved, attains 2,12,38 at n1..3. |
| D5-F5 | `paper-note-draft.md:76` | direct | Octahedral Dirichlet-kernel order credited to Belinsky/Travaglini lead and Dencker–Erb–Kolomoitsev–Lomako Thm 2.3. |
| D5-F6 | `paper-note-draft.md:81` | direct | Hilbert–Burch classical (Gaeta; Eisenbud); IDEA-199 derived and measured the recurrence-residual pencils. |
| D5-F7 | `paper-note-draft.md:91` | direct | "separate later-round review coverage" becomes "transfer covered by the supplemental R4 review only". |
| D5-F8 | `final-d5/novelty-gate.md:21`; `paper-note-draft.md:104`; `final-d5/outcome.md:30` | direct | LIT-381 partial Cools–Poppe reading (§3.2, Table 2, §6) recorded; fulltext gap stated as "beyond" it. |
| D5-F9 | `final-d5/outcome.md:22` | direct | "pending independent replay" replaced by link to [final-root-checks](final-root-checks.md). |
| D5-F10 | `final-d5/e4-verification.md:3` | direct | Later Greenfeld–Lev 1.1 and Białas-Cież et al. mesh imports are pointed to their checking records. |
| D5-F12 | `final-d5/novelty-gate.md:33`; `final-d5/source-records.md:96` | direct | "R2 follow-through" relabelled "post-R2 follow-through (committed after the R3 preregistration ...)". |
| D5-F14 | `final-d2/candidate.md:70` | direct | Resume only under the recorded freeze conditions, with links. |

## Companion corrections (pinned prose, not edited)

The following files are pinned in `evidence/fd4-manifest.json`; their corrections are recorded here. Read each as a dated note to the named lines.

- **A-M8** (`final-d4/finite-minima.md`, after "No catalogue optimality label is used."): Verification limitation: the second enumerator source `audit-04/code/A1/aud_enum.cpp` (10,115 bytes, SHA256 `d39563b9340bb0e8384031dac36e2050efb0ab6953c64e165e4006eaca9be503`) is outside the master manifest's code/evidence scope and is pinned by `fd4-lee.json` and `fdq-lee-replay.json`; the g++ version was not recorded, and both executions used identical binaries. Adding the file to the master `inherited_inputs` is a developer choice (returned below).
- **D4-m1** (`final-d4/certificate-reduction.md:141–144`): replace "7.7% should not be used" by: The source's m3 factor is 2/sqrt(3)≈1.15470054 relative to the mesh maximum. The source's eq.(6) midpoint estimate has relative error at most (c_m−1)/2≈7.7% of ||L_n|| at m3 (the scout's figure); the interval half-width relative to its midpoint is (c_m−1)/(c_m+1)≈7.18%. Neither percentage is used: the certificate applies the factor c_m itself.
- **D4-m2** (`final-d4/certificate-reduction.md` after line 41; `final-d4/lebesgue-intervals.md:51–53`): 2311.18656v1 states Lemma 1 without proof, citing Piazzon–Vianello, Optim. Lett. 12 (2018) 63–71, following Bos (DRNA 10, 2017); Proposition 1's proof is pp3–4. Lemma 1's proof is therefore located in that cited source, not locally verified. (Mirror applied directly at `final-d5/source-records.md:77`.)
- **D4-m3** (`evidence/fd4-manifest.json`, note for `final-d4/results.md` "Storage and integration"): 2026-11-12 audit05 note: `evidence/fd4-manifest.json` is the D4 worker's return-time snapshot. Its prose identities for lebesgue-intervals.md and results.md predate the root's post-check status edits, and its `status_at_return` is historical. Prose is not hash-pinned for verification; current code/data integrity is `evidence-manifest.json` (verify PASS, 362 artifacts). This also records A-M7 as a dated disclosure; the JSON itself is unchanged.
- **D4-m4** (stale "audit pending" lines, to be read as superseded by [audit-05](audit-05.md)): `final-d4/finite-minima.md:32`: Formal Claude audit05 independently re-enumerated all four windows with a fresh dual-form enumerator (identical per-q counts, minimizer HNFs and folds); see audit-05. `final-d4/lebesgue-intervals.md:48,92`, `final-d4/results.md:40,71–72`: Formal Claude audit05 independently recomputed all 13 QR and both optimized-n12 enclosures (exact rational V, exact cos(kθ) mesh rows, own π/cos enclosures, int128); each lies inside the stated interval; see audit-05. `final-d4/candidates.md` last bullets stay as dated history.
- **D5-F11** (`final-d4/candidates.md:16`): "Final independent m3 replay was pending when this worker returned" has since passed: dated 2026-11-12 note, see [D4 audit](final-check-d4/audit.md).
- **A-M14** (same stale process text, no exact replacement given): `final-d4/finite-minima.md:32`, `final-d4/lebesgue-intervals.md:92`, `final-d4/results.md:71-72` are covered by D4-m4 above.

## Returned to developer or orchestrator

- **MAJOR findings** (all sub-reports): developer, as dispositioned in the audit report.
- **D1a-F1** (exterior nodes, adds a hypothesis to theorem statements): material; developer.
- **D1b-1** (effective fixed-excess sphere/disk literature omitted), **D1b-2** (Li–Sun–Xu question framing), **D1b-4** (reconstruction.md:47 reasoning): developer.
- **A-M3, A-M4** (`Split from/into` headers in `theory/t7-finite-reduction.md`, `final-d4/finite-minima.md`, `theory/r08-lattice-minima.md`): split headers, developer.
- **A-M5, A-M15** (`results/padua-3d-20261106.md` status wording and spacing): orchestrator.
- **A-M7** (`evidence/fd4-manifest.json` prose pins): evidence JSON; only the dated companion note above. **A-M8, A-M9:** a developer option to add `aud_enum.cpp` to the master `inherited_inputs` and to commit the SVD replay script.
- **D2-m3** (LOG correction about the R3 baseline failure; `gates.md` is a preregistration record): orchestrator LOG note: "Correction (audit-05): the original R3 children failed in the first proposal's batched Newton solve, after the single baseline objective (receipt evaluations=1), not during the baseline evaluation. gates.md is unchanged as a preregistration record."
- **D5-F1, D5-F13** (summary wording that adds hypotheses/quantifier scope "exact on Π_(2n−1)"/"exact through degree 2n−1", and a certified-rule scope sentence): excluded as changes to a claim's statement/hypotheses; developer or AC.
- **D5 M1–M4** and the two developer-returned MINORs (paper manuscript/process restructuring and bibliography; D3 candidate disposition-reason field): developer.
- **Optional NOTEs** in all sub-reports: no action.
