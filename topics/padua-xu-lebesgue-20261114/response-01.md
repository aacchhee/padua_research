# Response 01 — padua-xu-lebesgue-20261114 — MINOR-only response to audit-01

- **Responder:** topic orchestrator (Claude Opus 5.5). The mechanical fixes of handoff 03, Task step 2, were applied by a Claude Sonnet 5.5 (high) subagent working from the orchestrator's fix list; no git command was run by it (one `git status` was attempted by mistake and was refused by the permission system; it had no effect).
- **Audited SHA:** `971beb79b8edb93835b20d1b9148e93d4ba3aba4` (audit-01 head inspected: `46dcd9227aa24fa88ab657b4e15318062219d73f`). Handoff 03 input head: `278926731b35fc03384eeb1eb5212d62537af0cd`. Date: 2026-11-14.
- **Scope:** MINOR, non-material fixes only (handoff 03, Task step 2 and Scope limits). Every correction is a dated addendum or one of the in-place edits that step 2 allows (stale process text, the word PARTIAL, the X2-33 summary, a "superseded by X2-32" annotation).
- **Not changed:** any Statement, quantifier, hypothesis, constant, status word, dependency direction of a proof, `audit-01.md`, `independent-checks-*.md`, `handoffs/*`, any `evidence/*.json`, any `code/**` file.
- **Not taken (material; AC's choice):** registering P1 as its own PARTIAL target (A-m4, alternative option) and upgrading X2-N35 from MEASURED to PROVED at M = 62, 102, 202 (n2). Either would be a status change and would return the topic to a focused re-audit.
- **Disagreements with audit-01:** none. Every finding was accepted.

## A. Findings A-m1 … A-m9

| ID | Disposition | Files and sections changed |
|---|---|---|
| A-m1 | **fixed** (retroactive record; no pre-registration is claimed) | `novelty-gate-X2.md`: new section "Round X2-3 addendum" with four rows (far-field localization X2-33; averaged shifted-lattice bound and W-programme X2-34; zero-shift maximality X2-N35 as the MP variant of IDEA-316, REJECTED: failed, MEASURED scope, PD-N079 not transferred; first-variation band certificate X2-31/32) and the closest entries IDEA-316/PD-N079, IDEA-333, IDEA-206, IDEA-326–328, IDEA-330/PD-T227, PD-T215–T228. Dated "closest entries" sentences in Sources of `theory/X2-33`, `theory/X2-34`, `theory/X2-N35`. The scan is stated at the level of the registry rows read (the full records of PD-T215–T228 were not re-read). |
| A-m2 | **fixed** | `results/padua-xu-lebesgue-20261114.md`, X2-33 bullet, reworded in place to the true scope (sin θ₁, sin θ₂ ≤ ϑ_n for every even n ≥ 2; non-trivial only for n ≥ 1030, where ϑ_n ≤ 21.5 log²(n+2)/n; maximizers in the four vertex boxes). `LOG.md`: old line untouched; dated correction appended at the end. `report.md` states the corrected scope. The PR #36 body remains to be worded the same way at PR preparation. |
| A-m3 | **fixed** | `report.md`: header (audit-01 confirmed all claims; which items had independent subagent checks), §2 (round X2-3 results, no longer "in progress"; independent-check bullet), §4 (argmax OPEN after round X2-3; P1-tail, W1–W3), §5 (conditional sentence). Results file: header line and the X2-32 bullet ("independent rerun done in audit-01 §2.1"); a closing dated line replaces the stale "or the audit now" reading. |
| A-m4 | **fixed (non-material option)** | `theory/X2-28`: "PARTIAL in the sense of the workflow" replaced in place by "plan progress (not a registered target)"; the MEASURED first-variation row annotated "superseded by X2-32" (MEASURED word kept); dated addendum at the end. `theory/X2-32`: dated note that "Split from: X2-28 plan item P1" names a plan item. Registering P1 as a PARTIAL target is **not** done. |
| A-m5 | **fixed** (status unchanged: MEASURED) | `theory/X2-N35`, Checks: dated note on the float64 cancellation near x = y (M = 102: recorded ratio 1.0752491 against the certified 1.0752352 ± 2.6e−8; cause per audit-01: node (43,44)); the missing M = 62 and 102 values from `evidence/mp-x2r3_checks_b.json`; certified ratios 1.0698576 ± 3.9e−8 (M = 62), 1.0752352 ± 2.6e−8 (M = 102), 1.0796015 ± 4.8e−8 (M = 202) from `evidence/audit-x2-separate-path.json`, section `xi_certificate`. |
| A-m6 | **fixed** | `theory/X2-32`, Checks: dated note that the pinned sha256 of `evidence/mp-x2r3-first-variation.json` covers the non-deterministic `wall_seconds` (105.7) and that a rerun matches after substitution (audit-01 §2.1 R5); no timing-free hash was added and the pinned evidence was not rewritten. Evidence files now referenced from records: `mp-fv_full_2_24.json` (X2-31, X2-32; its missing command and version fields are stated in the note), `mp-x2r3_checks_t.json` (X2-33, X2-34), `mp-x2r3_checks_c.json` (X2-33, X2-28 W2), `mp-x2r3_checks_b.json` (X2-N35, X2-28), `mp-corner-values.json` (X2-27, X2-N30), `mp-cmp-identify.json` (X2-22, X2-N29). `gates.md`: new "Evidence index" listing all 18 evidence files and the records they support. |
| A-m7 | **fixed as a qualification; locator still pending** | `theory/X2-26` (dated note at the end) and `literature-xu-mp.md` §3 item 1 (dated sub-bullet): "(as transcribed by the orchestrator from the ScienceDirect HTML; display not re-checked; page/equation locator pending)", and the "(n/2+n+2)²" → "(3n/2+2)²" normalisation is disclosed. Beberok's page was **not** re-checked here. |
| A-m8 | **fixed** | In place: every "Independent rerun: pending" line in `theory/X2-21 … X2-N35` (15 records) replaced by "Independent rerun: done in audit-01 §2.1 (R1–R8). Per-record verdict: audit-01 §6." (X2-32 and X2-N35 with record-specific pointers). Dated addenda (status lines left as written): `theory/X1-01 … X1-07`, `X2-25`, `X2-26`, `X2-N30`, `X2-32`, `X2-28`. `gates.md`: dated addendum under the Verdicts. `LOG.md` header line 6 edited in place ("Claims: see results file and audit-01 §6"). `attempts/X2-round3.md`: dated note. |
| A-m9 | **fixed; the exact fact proved** | `theory/X2-23`, dated addendum at the end: (1) dependency statement corrected (X2-34 (c), X2-31 (b), X2-28 remark all use (f); the Assumptions sentence and the "not used elsewhere" cell are stale); (2) self-contained proof of ℚ(ζ_a) ∩ ℚ(ζ_b) = ℚ(ζ_gcd(a,b)) (compositum = ℚ(ζ_lcm) by Bézout; φ(a)φ(b) = φ(lcm)φ(gcd); degree bound via restriction to the intersection; ℚ(ζ_gcd) ⊆ intersection), specialised to the exact fact used in (f): a = 2M, b = 2M+2, gcd = 2, intersection ℚ. The only quoted input is [ℚ(ζ_m):ℚ] = φ(m) (textbook, locator not verified). X2-23 (f) was already listed in X2-34's Depends; `theory/X2-34` got a dated note confirming it is used for every even n ≥ 2. Whether (f) needs its own ID is left to PR preparation. |

## B. NOTEs

| ID | Disposition | Where |
|---|---|---|
| n1 | superseded by the proof in A-m9; the Washington Prop. 2.4 locator is still unverified and is flagged as such | `theory/X2-23` addendum |
| n2 | **not taken** (status change; material) | — |
| n3 | done as an optional remark | `theory/X2-N30` (dated note at the end) |
| n4 | done | `literature-xu-mp.md` §2 (dated sub-bullet: "Lemma 1 (p. 45; cited as Lemma 15 in their §7.1)"); the same lemma is meant in gates.md, X2-31 |
| n5 | AC's decision (no LICENSE file); not touched | — |
| n6 | acknowledged; the "not found in the documented search" wording is kept | `novelty-gate-X2.md` addendum (scope paragraph) |
| n7, n8 | no action (confirmations) | — |
| n9 | carried into the new gate addendum; to be kept in `state/IDEAS.md` at PR preparation | `novelty-gate-X2.md`, Notes (ii) |

## C. Unresolved or open after this response

- A-m7: the page and equation locator of Beberok's final display, and a re-check of the display itself, remain open; any manuscript or LIT record must do this first.
- A-m6: no timing-free hash of the 758 KB output was added (it would need a rerun and a new evidence field); the substitution rule is documented instead.
- A-m9: the cyclotomic input [ℚ(ζ_m):ℚ] = φ(m) is quoted as textbook without a verified locator; the decision on a separate ID for (f) is deferred to PR preparation.
- A-m1: the closest-entries comparison used registry rows and the PD-N079 / IDEA-316 records; the full PD-T215–T228 theory records were not re-read.
- All items under "Not taken" above (P1 registration, X2-N35 upgrade) stay as AC's decision; if taken they go to a focused re-audit.

## D. Check performed

No file under `evidence/`, `code/`, `handoffs/`, `audit-01.md` or `independent-checks-*.md` was modified (modification times unchanged). The edited files are: `novelty-gate-X2.md`, `gates.md`, `LOG.md`, `report.md`, `literature-xu-mp.md`, `attempts/X2-round3.md`, `theory/X1-01 … X1-07`, `theory/X2-21 … X2-28`, `theory/X2-31 … X2-34`, `theory/X2-N29`, `X2-N30`, `X2-N35`, and `results/padua-xu-lebesgue-20261114.md`. The φ-identity used in A-m9 was also checked numerically for all 1 ≤ a, b ≤ 60.
