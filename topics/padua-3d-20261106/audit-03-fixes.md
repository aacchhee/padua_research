# Audit 03 — auditor MINOR fixes (dated companion note), 2026-11-06

These are third-round auditor fixes (Claude, claude-opus-5-5 xhigh audit; applied by a mechanical subagent) under WORKFLOW "Proportionate audit and records". They are wording, link, stale-text and already-documented-decision repairs only, and are committed separately from the audit report. No claim statement, status, ID, disposition, threshold, code, input or evidence changed.

Hash-pinned prose (`evidence/independent-r06-pins.json`, and `evidence/t9-r06-run-manifest.json` for `literature-round06/t9-betke-henk.md`) is not edited. For those files the correction is recorded here as a dated companion note: read the replacement text where the old text stands. Source IDs: PA = Part A (response-02, manifest, metadata); T7/T8/T9/T10 = per-direction audit; NV = protocol/novelty sub-report. Where two reports proposed the same fix it is listed once with both IDs.

## A. Direct edits to unpinned files (20 IDs)

Each carries an inline dated note or exact replacement; verified to match the old text before replacing.

| ID | File (location) | Edit |
|---|---|---|
| PA-F1 | response-02.md:36-37 | "Requested original-location text is in the integration notes" replaced by "The dated withdrawals are in rounds.md, attempts/T7–T9.md and report-continuation-04.md". |
| PA-F2 | response-02.md:81 | "Full namespaced mapping ... integration notes for the route worker." replaced by "The C4 mapping and aliases are in the table above, theory/t7-rank-two.md and theory/t7-one-phase-refutation.md; attempts/T7.md's bare labels are history, decoded by its dated route-map note." |
| PA-F11 | response-02.md:22 and :107-110 | "Manifest refresh accompanies the evolving new batch." -> "The manifest v2 at 696bca5 pins these code/data files."; the "Excluded-file integration ... eventual next handoff." sentence -> "Root integration followed in 7f773eb; the focused Claude review is handoff07 (audit-03)." |
| PA-F3 | attempts/T7.md (after "## Route map") | Dated audit-03 label note decoding ID-suffix vs theory-ID suffixes (T7-03, T7-04 = PD-N T7-08, T7-09 split). |
| PA-F4 | rounds.md | "Final handoff06 stopping record" block moved unchanged to directly after the historical-counts intro; "the preceding direction-wide stops" -> "the direction-wide stops recorded below under "Handoff04 final boundaries""; withdrawal pointer added under "Handoff04 final boundaries". |
| PA-F6a | attempts/T9.md:24-30 | `padua-3d-codex-` -> `padua-3d-20261106-codex-` in all 7 IDs. |
| PA-F7 | novelty-gate-T9.md (end) | Appended attribution paragraph (audit-02 n5) under the audit-03 heading. |
| T7-M2 | report-round06.md (Unequal noncyclic n6 union row) | "Escapes the common-subgroup trace obstruction, still poor" -> "Avoids the equal-common-H n6 screen failure (0/128, MEASURED), still poor". |
| T7-M3 | attempts/T7-round06.md (Phi row, status cell) | Appended "; no degree-uniform H_n was proposed or prospectively saved (only n3/n5 have nonempty rank>=2 no-fold classes in n3..6)". |
| T7-M4 | attempts/T7-round06.md (U row, status cell) | Appended "; only generic no-fold phases were screened — folded special-phase unions and unequal/mixed cyclic unions were not screened by T7". |
| T7-M5d | theory/t7-finite-reduction.md (after the "Next unresolved step" paragraph) | Dated note: the enumeration and symmetry quotients are implemented and the n2 census completed in t7-r06-n2-census.md; n3 remains OPEN. |
| T8-F1 | attempts/T8-round06.md:23-25 | Publication sentence now reads "...made after these initial runs (its Phi3b append already reports their outcomes) and before this first counted research boundary. Pre-run existence of the initial protocol is developer attestation, not established by publication order." |
| T8-F2 | attempts/T8-round06.md:88 | "is impossible since 3 does not divide 85" -> "finds no count-permitted stratum, since 3 does not divide 85". |
| T9-F1 | report-round06.md (Strict-positivity sentence) | "Strict positivity at every node is essential." -> "Nonnegative weights with positive identity mass suffice for the witness; strict positivity on all of X makes the node count |X|." |
| T9-F5 / NV-F2 | theory/t9-packing-conditional.md (end) | Two forward pointers to t9-r06-packing-source.md (density premise now imported at primary-statement level; n>=110 consequence for strictly positive full-support unshifted weights with Betke–Henk as LITERATURE dependency). Statement and CONDITIONAL status unchanged. |
| NV-F3 | theory/t9-lower-set-transfer.md (end) | Pointer to t9-r06-explicit-rleja.md (PD-T T9-r06-05); lines 26 and 34 describe the earlier state. |
| NV-F6 | attempts/T8-round06.md after :61-62 and :103-104 | Appended "2026-11-06 audit-03: independent reruns are recorded in evidence/independent-r06-t8-*.json and independent-checks-round06.md; no status change here." |
| NV-F7 | attempts/T10.md:14 | After "every eligible extraction" inserted the audit-03 note on "every nonsingular extracted set" (preregistration-T10.md item 3). |
| NV-F8 | report-round06.md (after intro paragraph) | Added provenance line: T10 and ranked routes proposed in Claude's handoff06; M=N=20 orbit, Betke–Henk and Chkifa leads from Claude's audit-02 (the latter two from recollection). |
| NV-F9 | independent-checks-round06.md:3 | After "check06" inserted ", assigned gpt-6-astra high (696bca5 trailer; runtime unexposed)". |

(Count: PA 7, T7 4, T8 2, T9 2 with NV-F2 merged into T9-F5, NV 5 further = 20.)

## B. Companion corrections for hash-pinned files (16)

Format: for FILE:LINE, read REPLACEMENT instead of OLD. The pinned files are unchanged.

- **PA-F6b / NV-F1.** For theory/t8-r06-parity-admissibility.md:31, read "PD-N?padua-3d-20261106-codex-T8-02 (old alias PD-N?padua-3d-codex-T8-02)" instead of "PD-N?padua-3d-codex-T8-02".
- **T7-M1.** For theory/t7-r06-n2-census.md after line 21, add: "These are labelled (H,a) classes, not distinct node sets: torus negations t_j→−t_j fix c, so the four order16 groups give one and the same 10-node set, and the 32 order19 groups give 8 distinct node sets (2 up to coordinate permutation)." For theory/t7-r06-n2-census.md:121 and theory/t7-r06-quality.md:105, append "(only these two values occur)".
- **T7-M5a.** For theory/t7-r06-census-reductions.md:102-103, read "The n2 general census was subsequently completed with every quotient stratum decided exactly (n2 census: `t7-r06-n2-census.md`, relative to theory/); the n3 census remains OPEN." instead of "The n2 general census remains OPEN until every quotient stratum is decided exactly."
- **T7-M5b / NV-F4.** For theory/t7-r06-torsion-obstruction.md:83-84, read "Independent review completed in `independent-checks-round06.md` (link `../independent-checks-round06.md` from theory/). Broad T7 target remains OPEN." instead of "Independent mathematical review requested from root's checker; no claim that a replay has already occurred." (T7-M5b's equivalent wording: "Independent check06 reviewed this argument as a valid necessary condition (`independent checks` (link `../independent-checks-round06.md` from theory/)).")
- **T8-F3.** For theory/t8-r06-phase-strata.md:42-43, read "sample proves a symbolic full-size minor is not identically zero on the containing stratum (full rank then holds off a proper algebraic subset);" instead of "sample proves a symbolic full-size minor is nonzero on the containing stratum;".
- **T8-F4.** For theory/t8-r06-unit-coordinate-folds.md after line 90, read in addition: "Addendum 2026-11-06 (audit03): that checker now exists; see t8-r06-near-order-measurements.md." (the word "future" at lines 89-90 is history).
- **T8-F5.** For theory/t8-r06-certification.md after line 53, read in addition: "Addendum 2026-11-06 (audit03): executed checks are in ../independent-checks-round06.md (supplementary) and ../audit-03.md." (the "arranged by root" text is history).
- **T9-F2.** For theory/t9-r06-packing-source.md:9, read "and the densest packing lattice Λ*(O) (a critical lattice of the difference body O−O=2O) with basis" instead of "and the critical lattice with basis".
- **T9-F3.** For theory/t9-r06-packing-source.md:35, read "the comparison packing lattice is **n Bcrit**" instead of "the critical comparison lattice is **n Bcrit**", and "multiply the difference 19n^3/108−binom(n+3,3) by 108" instead of "multiply the difference by 648".
- **T9-F4.** For literature-round06/t9-betke-henk.md:15 (pinned in evidence/t9-r06-run-manifest.json), read "The displayed densest packing lattice Λ*(P_o) (a critical lattice of P_o−P_o, source Algorithm 4.2) is twice" instead of "The displayed critical lattice is twice".
- **T9-F7.** For theory/t9-r06-phase-weight-boundaries.md:70, read "Closed-form values through16 are tabulated (not enumerated) in `evidence/t9-r06-exact.json`;" instead of "Exact arithmetic controls through16 are in `evidence/t9-r06-exact.json`;".
- **T10-m5.** For theory/t10-quality.md:15, read "(conditions about5e16–1e19)" instead of "(conditions around1e17–1e19)" (receipt shows 4.77e16–9.96e18).
- **NV-F5.** At theory/t8-r06-parity-admissibility.md:76-77, t8-r06-phase-strata.md:44,59, t8-r06-union-parity.md:22,50, t8-r06-unit-coordinate-folds.md:81 and t8-r06-near-order-measurements.md:13,20, read in addition: "2026-11-06 audit-03: independent reruns are recorded in evidence/independent-r06-t8-*.json and independent-checks-round06.md; no status change here."
- **NV-F11.** For theory/t10-census.md:25, read "Independent replay: evidence/independent-r06-t10-global.json reproduces 2/12/38 (n1..3)." instead of "Independent replay was requested … arrives." For theory/t10-neighborhood-search.md:15, read "4941-box replay: independent-checks-round06.md." instead of "Independent replay remains required …".
- **NV-F12.** For theory/t8-r06-measurements.md:46, read after "audit control": " (Claude audit-02 lead; audit-02/T8.md, audit-02/code/m20_check.py)".
- **NV-F13.** For theory/t9-r06-explicit-rleja.md:3, add "Lead: Claude audit-02.md:168 (recollection), handoff06 T9.U."; for theory/t9-r06-packing-source.md:3, add "Betke–Henk lead: Claude audit-02/T9.md:160 (recollection)."

## C. Recommendation only (not applied)

- **PA-F9 (response-deviations-02.md:66-67).** Auditor recommends that the developer replace "an unrelated Lanczos registration range641–690" with "state/IDEAS.md lines 641–690 (Lanczos registrations IDEA-081–IDEA-128, including IDEA-109 and IDEA-120; IDEA-120 was already treated by the inherited T7 gate)". Marked optional-dispute by the report; if the developer disputes the range meaning, AC decides.

## D. Returned to developer / orchestrator (not auditor-fixable)

- Root `results/padua-3d-20261106.md` (orchestrator-owned, outside the topic): PA-F5 (line 56 stopping-rule withdrawal), T7-M1 results line 13, T7-M5c (line 69), T8-F7 (list the four PROVED T8 records), T9-F6 (line 93 superseded pointer).
- LOG.md (recorded by the orchestrator): PA-F8, NV-F10 (header base SHA, report links, round-06 heading attributions), and the LOG pointer at :337-338.
- Disposition-reason edit: T8-F6 (insert ": failed" after REJECTED at t8-r06-near-order-measurements.md:100 and novelty-gate-T8-round06.md:79, 81, 88, 92).
- Optional, header-semantic: PA-F10 (theory/t7-rank-two.md:4 "Split from:") not applied; T7-N3 optional measured text for attempts/T7-round06.md not applied.
- Material or developer findings (not edited): PA A3-4 beyond slug, T7 NOTEs, T8 N2 lead and MINOR-4/5 notes, T9 M1 (status convention), M2 (complement feasibility), m2–m5, n3 LIT status line; T10 m1–m4; NV MJ1–MJ4, m1–m8.
