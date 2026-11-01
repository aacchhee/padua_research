# L5 — response to independent reconstruction 01 (`reviews/L5-reconstruction-01.md`)

Developer: Claude Sonnet 5.5, high. Written 2026-10-31T23:02Z. I read the review in full and did not edit it. No new rounds were run; one re-analysis script was added (`code/L5/analyze_r01c.py`, output `logs/analysis_r01c.txt`) and nothing else was recomputed. Items cited as REVIEWER-MEASURED (structure defect, Q-accumulated residuals, geppR1/geppR2 runs, stage structure) were **not** rerun by me. Verdicts of the reviewer: Claim 1 (PD-T 501) CONFIRMED WITH CORRECTIONS, Claim 2 (PD-T 505) CONFIRMED, Claim 3 (502/503/506) slopes CONFIRMED WITH CORRECTIONS, prefix kill CONFIRMED, REPRO numbers CONFIRMED. Each finding below ends with FIX, REJECT (evidence-based) or UNRESOLVED.

## Medium findings

**M1 — PD-T 501 is not an IEP backward-stability statement; the Remark overreaches.** Accepted. Doing nothing (Q̃ = I) satisfies Theorem A, so it constrains neither ŵ ≈ ‖v‖e₁ nor the zero pattern. My inference that 'largest' fails by a Q̃ with the wrong first column is withdrawn: the reviewer's Q-accumulated measurement shows the same backward and first-column residuals for 'scheme' and 'largest' and a structure defect that tracks the forward error (n = 50 gepp: 8.4e-10 vs 6.8e-14). **FIX:** Scope and Remark of `givens-updating-rotation-count-backward-bound.md` restated (History line names M1); R02 §3 reworded and the inference withdrawn; PD-N 506 gets N6 (REVIEWER-MEASURED) stating that the zero pattern, not the backward error, is lost. Theorem A and its proof unchanged.

**M2 — slope uncertainty understated; single power law misspecified.** Accepted after checking: my size-level fit of the same logs reproduces the reviewer (Padua cubature Givens 1.40 [1.01, 1.79], U 1.55 [1.03, 2.06]; the earlier [1.09, 1.70] came from OLS over 35 replicate points and a within-size bootstrap). Quadratic terms (log10 convention): +0.73 (t = 3.7) cubature, +0.93 U, +1.2..+1.5 random orders; structured orders 0.93 [0.88, 0.99] with no significant curvature. Upper-range (M >= 496) intervals have df 2: 2.15 [0.60, 3.71], 2.50 [0.31, 4.70]; the arcsine family has df 1 there. **FIX:** new primary table in `givens-deficit-slopes-measured.md` and R01 §3.1 (size-level intervals, curvature, per-class statements, upper range declared unsupported); `analysis_r01.txt` kept as the original output and superseded. **UNRESOLVED (needs runs):** more sizes in the upper range (Runs needed 2).

**M3 — the frozen kill test fires as written in the uniform-random family.** Accepted; this is the correct headline. The criterion I pre-registered says 'not killed overall only if no family triggers it'; the uniform family triggers it (CGS2 1.57, HL 2.28). **FIX:** R01 §3.1, the 502 theory file, candidates.md (IDEA 501) and STATUS.md now state 'killed as written (in that family)' first; 'not killed in the other four families' is labelled a post-hoc reading (exclusion of a confounded family without a pre-registered rule; arcsine family added after runs started, reaching only M = 1326); the Householder-normalised analysis is disclosed as secondary and post-hoc (my `analyze_r01c.py` agrees with the reviewer: Givens 0.76 [0.06, 1.46], HL 0.16 [-0.04, 0.37], CGS2 -0.54). Disposition of IDEA 501: REJECTED: failed, scoped to the uniform-density family.

**M4 — the prefix kill rests on the operational threshold.** Accepted as a scope statement; the kill itself stands (the reviewer reproduced it with independent code and two further unisolvent orders). **FIX:** PD-N 506 N2 gets a scope paragraph: on well-conditioned unisolvent orders 'largest' stays <= 3.1e-9 up to n = 50; >= 1e-4 occurs only on non-unisolvent or near-singular (sigma_min 9.7e-10) orders; the surviving statement is graded ('x15-50 per Delta n = 10 on every order; >= 1e-6 only on singular or near-singular sequences in the tested range'), described as a reading of the data, not tested by the kill; the fragility of the binary classification (n = 40 rand2, K = 2 prefix with equal x) is noted in 506 and 503. The same wording is in R01 §3.2 and candidates.md.

**M5 — scope contradicts statement (catastrophe at n = 15).** Accepted; checked: given order, U(0.1,1) weights, n = 15: 1.1e-2, ratio 1.6e12. **FIX:** 506 scope now reads 'no catastrophe at n <= 10' (ratios 0.8-1.3 on all 9 orders, both weights) and nothing stronger.

## Low findings

**L1 — comparator citation and the kill criterion.** Accepted. Exponents differ (M^{3/2}u here vs M^2 u for Householder, Givens QR linear in m+n): the worst-case bounds favour Givens, the opposite of the measured order; not like for like. The pre-registered 'same exponent' criterion therefore did **not** fire, and IDEA 503's rejection rests on a different ground. **FIX:** theory 501 Scope (ii), R02, candidates.md (IDEA 503: REJECTED: failed as an explanation, stated not to be by the pre-registered criterion). The Higham statements remain LITERATURE, UNVERIFIED (I did not read ASNA; I rely on the reviewer's check against Connolly-Higham 2022).

**L2 — stage structure and sharpness.** Accepted. **FIX:** noted in theory 501 Scope (iv) and R02, with 'worst case, not claimed attained'. **UNRESOLVED:** whether M u is provable in the two-sided setting (OPEN).

**L3 — floating-point GEPP order.** Accepted. **FIX:** scope note in `unisolvent-prefix-extension-lemma.md`: measured claims use the numerical certificate (mine and the reviewer's), not the lemma. The M > N remark is added to the same file.

**L4 — the frozen test cannot detect too-steep growth.** Accepted as a remark on the frozen design (plan unchanged). **FIX:** recorded in the 502 file and R01 §3.1; no change to the test.

**L5 — classification tolerance 1e-11 vs pre-registered 1e-8.** Accepted; already disclosed. **FIX:** restated prominently (14 of 16 pass the pre-registered rule; the 8 gepp/rpiv n = 50 cases are tolerance-independent) in 503, 506, R01 and candidates.md.

**L6 — 'typical draw' overstated.** Accepted. **FIX:** wording changed to 'within the range of four random draws' in R03, 503, STATUS.md, candidates.md. I also found that R03 said the gepp order at n = 60 had large prefix sigma_min; that order was not scanned at n = 60. Corrected.

**L7 — p. 395 is the kappa-pivot rule, not 'largest'.** Accepted (checked against my own reading of p. 395: 'if two pivots differ in some orders of magnitude'). **FIX:** 506 disposition no longer rejects the p. 395 suggestion on 'largest' data; the rejection of the kappa rule (kappa = 10, 100) now stands in PD-N 507 on its own evidence.

**L8 — IDEA 502 disposition wording.** Accepted. **FIX:** claim 'only on non-unisolvent prefixes': REJECTED: refuted; mechanism 'larger pivot as stabiliser': REJECTED: failed (506, candidates.md, R01).

**L9 — 504(b)/(c) and PD-N bundling.** Accepted under AC's L5 decision (a separate evidenced mechanism failure gets its own PD-N). **FIX:** new files `magnitude-threshold-pivot-rules-failure.md` (PD-N?bivariate-lanczos-claude-507: pivk10/100, pairnorm1; scoped n = 20, 30) and `fifo-threshold-deferral-failure.md` (PD-N?bivariate-lanczos-claude-508: FIFO threshold deferral, tau 1e-8 and 1e-3); N4 removed from 506 and replaced by a pointer. Not given a PD-N, by the same decision: pairnorm100 (equivalent to 'scheme'), windowed best-pivot deferral 504c'' (not killed, no gain): IDEA dispositions only. Both new records carry ranges n = 20, 30 only.

**L10 — ID choice and crosswalk.** Accepted. **FIX:** crosswalk table added to candidates.md; the cosmetic 'digit clash' justification is dropped. (The LOG.md sentence the reviewer cites is not in my files; I did not write LOG.md.)

## Informational and protocol

**I1** (HL not sqrt(M)): agreed, stated in 502/R01. **P1** (kill criteria only self-attested; one commit): agreed; cannot be improved retroactively; recorded in the candidates.md History. **UNRESOLVED.** **P2** (post-hoc items): all are listed as post-hoc in the records. **P3**: agreed.

## Remaining uncertainty and Runs needed

Added to the existing lists (R01 §7, R03 §7): the reviewer's four runs (slopes to M >= 2000 with the reviewer's code; all-unisolvent orders at n = 62, 70; full SVD prefix scan of the REPRO order and of the three other n = 60 random orders; uniform-family M = 861..2016 with the Householder-ratio analysis). Not independently checked by me: the reviewer's Q-accumulated residuals and stage-structure check.

## Files changed

R01.md, R02.md, R03.md, candidates.md, STATUS.md; theory: givens-updating-rotation-count-backward-bound.md, givens-deficit-slopes-measured.md, prefix-unisolvence-order-statistics-measured.md, unisolvent-prefix-extension-lemma.md, largest-redundant-pivot-degradation.md; new: magnitude-threshold-pivot-rules-failure.md, fifo-threshold-deferral-failure.md; code: analyze_r01c.py; logs: analysis_r01c.txt. Each theory file has a dated History line naming the findings.
