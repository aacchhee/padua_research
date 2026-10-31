# L5 candidate records (provisional IDs `IDEA?bivariate-lanczos-claude-5nn`)

Developer: Claude Sonnet 5.5, high. Rules read at `d36722823441dc40c6e19d69a174459348dd309c` (plan.md header). Format: `templates/IDEA.md`. Kill criteria below were written **before** any of my own R01 experiment ran (only a timing run of the C Givens port and a bitwise-identity check against the unchanged input `givens()` had been done).

## Novelty gate (scope, terms, shortlist)

Scope read: `state/IDEAS.md` headings and alias lines of all rows, the full obstruction table (OBST 01-15) and disposition table rows 011-017, 035; `literature/INDEX.md` header and rows 001-020; `topics/.../baseline-candidates.md` seeds 011-016; `plan.md` (L5-Q1 and History); `sources/.../notes/adv_F1_F6_F3.md` section 2 (unaudited); VB-C 2010 fulltext pp. 391-401 (pdftotext, scratchpad only). Terms searched in `state/IDEAS.md`: pivot, Givens, rotation, deflat, unisolv. Shortlist read in full: IDEA 011, 013, 015, 016, 017, 035; OBST 08.
No theory file exists yet in `tracks/bivariate-lanczos/theory/`. No novelty claim is made: L5 measures and, in later rounds, derives routine Higham-style bounds; the 'largest' negative is recorded as MEASURED scope only (COMMON_RULES: no novelty claims).
Limitation: `literature/INDEX.md` was read to row 020 only; I did not search the rest for Givens-updating priority, and make no priority claim.

---

## IDEA?bivariate-lanczos-claude-501 — Rotation counting explains the Givens accuracy deficit

Aliases: Givens deficit; rotation counting; error ~ M vs ~ sqrt(M); registry seed IDEA 015.

- Question / scope: plan L5-Q1 first clause. Is the relative error of (H_x, H_y) from point-by-point Givens updating (VB-C 2010 Algorithm 1, real nodes) growing like M^1 while HL, CGS2, Householder grow like M^(1/2)?
- Mechanism and hypotheses: each entry of the final H is hit by O(M) rotations in the chase (one chase of length i-1 per added point i). [FP] floating point; Padua (cubature, random, uniform weights) and uniform random nodes; 'scheme' pivot rule.
- Closest registry entries: IDEA 015 (same claim, supplier data M = 66-496), IDEA 017 (settled-background, normwise backward stability textbook). Closest literature: `higham-2002` (ASNA ch. 18-19), `vanbarel-chesnokov-2010` Tables 1-2 (p. 400-401).
- Separation criterion vs closest entry: none claimed (this is the registry-seed test over a larger M range, not a new mechanism). Falsified by the kill criterion below.
- Literature baseline and search limitations: see novelty gate.
- Applicable obstructions: none (OBST 17-type ill-posedness concerns commutation of computed H, not this question).
- Novelty gate verdict: duplicate of seed 015 (test of that seed, no new mechanism).
- Cheapest decisive test: R01 `exp_r01.py` with M = 66..2016, 5 orders/seeds per size.
- **Kill criterion written before testing** (identical to plan L5-Q1; operational reading fixed here): slopes are OLS slopes of log(error) on log(M) over all (order, seed) replicates of a family and weight type. The explanation is **killed for a family** if the Givens-scheme slope is <= 0.7, or if the HL slope or the CGS2 slope is >= 0.9, on the full range M = 66..2016 or on the upper range M >= 496. Verdict is reported family by family and the explanation is called not killed overall only if no family triggers it. Because plan L5-Q1 does not name the family, I additionally report which families trigger.
- Test discriminability: slopes ~1 vs ~0.5 differ by 0.5 in the exponent; over a factor ~30 in M this is a factor ~5.5 in error ratio, far above the replicate scatter seen in the inputs (factor ~2). Confounds recorded: intrinsic conditioning growth with M (random nodes), which affects all methods.
- Actual test results: R01.md.
- Disposition: R01.md.
- Canonical theory ID: none (MEASURED; a worst-case bound is candidate 503).

## IDEA?bivariate-lanczos-claude-502 — Prefix mechanism for the 'largest redundant pivot' catastrophe

Aliases: redundant-pivot catastrophe; prefix mechanism; registry seed IDEA 016; OBST 08.

- Question / scope: plan L5-Q1 second clause. Is the 'largest' pivot rule catastrophe present only on node orders with at least one non-unisolvent intermediate prefix (first K nodes vs first K monomials of the graded order, K <= M)?
- Mechanism and hypotheses: if the K-prefix is not unisolvent for the K-monomial prefix, the two pivots of a doubly-parented monomial are not equivalent and both are at rounding level in exact-structure terms; choosing the larger builds a rotation from rounding noise. [FP]; Padua M = N = 66..2016 (cubature weights are irrelevant to unisolvence; weights only affect values).
- Closest registry entries: IDEA 016 (same), IDEA 013, OBST 08 ('random nodes do not show it'). Closest literature: `vanbarel-humet-sorber-2014` section 4 p. 133 (max-norm pivot heuristic, as reported), `vanbarel-chesnokov-2010` p. 395 (pivot remark; plan History: p. 395, not 392).
- Separation criterion: a measured catastrophe (error >= 1e3 times the 'scheme' error on the same data) on an order all of whose K-prefixes (K = 1..M) have sigma_min(prefix block) above the stated tolerance falsifies 'only on non-unisolvent prefixes'.
- Novelty gate verdict: duplicate of seed 016 (test of that seed).
- Cheapest decisive test: exact/high-precision unisolvence test of every prefix for given/sortx/random orders plus orders constructed to have all prefixes well-conditioned (greedy maximal Schur pivot), then compare 'largest' error.
- **Kill criterion written before testing** (plan L5-Q1): a catastrophe on an order whose prefixes are all unisolvent kills the prefix mechanism. Operational: 'catastrophe' = error(largest) >= 1e3 x error(scheme) and >= 1e-10 absolute; 'all prefixes unisolvent' = min over K of sigma_min(Q_c[:K,:K]) >= 1e-8 where Q_c is the (orthogonal) weighted product-Chebyshev matrix in the order, with a high-precision cross-check at M = 66, 136 and 231. The converse (no catastrophe on any order with a non-unisolvent prefix) is **not** part of the kill test but is reported as the second direction of the correlation.
- Test discriminability: the tolerance 1e-8 is 8 orders above double roundoff; I record the whole distribution of min sigma_min per order so a different tolerance can be read off.
- Resources: prefix tests O(M^3)-O(M^4); heavy sizes are screened by a bordered-inverse chain (see R01).
- Actual test results: R01.md. Disposition: R01.md.
- Canonical theory ID: PD-N?bivariate-lanczos-claude-506 only if R03 finds the evidence supports a scoped MEASURED negative statement for 'largest'.

## IDEA?bivariate-lanczos-claude-503 — Worst-case rotation-count backward-error bound for point-by-point Givens updating

Aliases: Higham-style rotation bound; planned R02.

- Question / scope: for the VB-C Algorithm 1 (fixed rotation sequence, real nodes) in floating point, a bound of the form || [w|X|Y]-transformed - exact || <= c M^p u ... for the accumulated transformation, derived from Higham ASNA Lemma 19.7/Thm 19.10-type rotation analysis.
- Closest: IDEA 017 (settled-background, normwise backward stability textbook), IDEA 015. Literature: `higham-2002` ch. 19 (pending record read at R02).
- Kill criterion written before testing: the claim 'worst-case bound distinguishes M from sqrt(M) growth' is **not** asserted. The candidate is killed (as an explanation) if the proved bound has the same M-exponent for Givens and for the Householder/Krylov comparators, i.e. no separation. Any PROVED statement is a routine instance; the separation M vs sqrt(M) is statistical and stays MEASURED/OPEN.
- Disposition: R02.

## IDEA?bivariate-lanczos-claude-504 — Safe pivot / deflation rules (fixed scheme, rank-revealing, prefix-aware deferral)

Aliases: registry seeds 013, 016; planned R03.

- Question / scope: a pivot rule that is node-order independent in accuracy, with a proof that the fixed 'scheme' rule gives a well-defined rotation sequence.
- Sub-candidates: (a) fixed 'scheme' rule; (b) rank-revealing choice (pivot of larger magnitude but only among pivots that are not at rounding level relative to a prefix scale); (c) prefix-aware deferral (postpone a node whose prefix would be non-unisolvent). Kill test per sub-candidate to be written at R03 start, before running it.
- Disposition: R03.

### 504 — kill tests written before the R03 experiments (`exp_r03.py`; written after R01 data and the pivot-vs-sigma diagnostic, before any R03 rule comparison was run)

Test set: Padua n = 20, 30 (and 40, 50 for the C-only rules if time allows), cubature and random weights, orders given, sortx, rand1-3, gepp (the unisolvent-prefix order). Error = relative Frobenius error of (H_x, H_y), as R01. Baseline = rule `scheme` on the same stream.
- (a) fixed `scheme`: **killed as a 'safe, order-independent' rule** if on any tested order its error exceeds 10 x its error on the `given` stream of the same n and weights, or exceeds 1e-11 (this is falsified/confirmed by R01 data already; recorded in R03 as the baseline verdict, not a new test).
- (b1) `pivk{10,100}` (alternative pivot used only if kappa times larger) and (b2) `pairnorm{1,100}` (alternative pair used only if its norm is kappa times larger): each **killed** if on any tested (n, weights, order) its error exceeds 3 x the `scheme` error on the same stream and is above 1e-13, or if it exceeds 1e-11 anywhere. A rule that is never worse than 3 x scheme but also never better is recorded as 'equivalent to scheme' (not an improvement).
- (c) `defer` (prefix-aware deferral with the online detector min_j |pivot_j| < 1e-8): **killed** if on any tested stream its error exceeds 3 x the `scheme` error on the `gepp` stream of the same n and weights (the target is order-independence at the level of the best order), or if it needs forced insertions (a stalled buffer) on a unisolvent set.
- Detector claim (R03, from `diag_pivot_vs_sigma.py`): "prefix K is numerically singular iff min_{j<=K} |pivot_j| < 1e-10" is **killed** if a single prefix at n = 10, 14, 20 violates it in either direction (n = 10, 14 already show 0 violations in both directions before the kill test was written).

#### 504c' — `defer` with a larger threshold (post-hoc variant, kill test written before it is run)

Reason: the pre-registered `defer` (tau = 1e-8) was seen at n = 20 to accept prefixes whose min-pivot is only just above 1e-8 and to give errors 3e-9..1.5e-8 on the structured streams (forced insertions 0-3). New variant `defer3` with tau = 1e-3 (still only the online min-pivot detector; no knowledge of Q). **Killed** if on any tested stream (n = 20, 30, both weights) its error exceeds 3 x the `scheme` error on the `gepp` stream of the same n and weights, or it needs more forced insertions than 5% of M. Run by: `L5_TAUS=1e-3 python3 -I exp_r03.py ... ` (see R03.md).

#### 504c'' — windowed best-pivot deferral `deferbestW` (post-hoc variant, kill test written before it is run)

Reason: FIFO threshold deferral (tau = 1e-8 and 1e-3) fails on structured streams (errors 1e-9..1e-5) because it accepts the first admissible node, not a well-conditioned one. Variant: keep a window of the first W pending nodes (W = 8, 32); at each step tentatively insert all of them and commit the one with the largest min_j |pivot_j| (ties: oldest); the window is refilled from the stream. **Killed** if on any tested stream (n = 20, 30; both weights; given, sortx, rand1, gepp) its error exceeds 3 x the `scheme` error on the `gepp` stream of the same n and weights. Cost note: O(W) tentative insertions per step, each O(K^2); not claimed practical.

---

## Results and dispositions (written at the end of R03; the kill criteria above are unchanged)

### IDEA 501 (rotation counting explains the Givens deficit)

Result (R01; size-level re-analysis `logs/analysis_r01c.txt`, after reconstruction finding M2/M3): **the pre-registered kill criterion FIRED as written in the uniform-density random-node family** (CGS2 slope 1.57 [1.01, 2.13] and HL 2.28 [1.66, 2.89] >= 0.9, full range and M >= 496). By the operational rule fixed above ('called not killed overall only if no family triggers it'), the verdict is **KILLED (in that family)**. The statement 'not killed in the other four families' (Padua with cubature 1.40 [1.01, 1.79], U(0.1,1) 1.55 [1.03, 2.06], unit weights 1.08 [0.81, 1.34]; arcsine random nodes 1.28 [0.96, 1.60]; HL 0.71-0.79, CGS2 0.38-0.53 there) is a **post-hoc reading**, resting on excluding the uniform family as confounded (cond ~ M^2.96, Householder slope 2.11; no exclusion rule was pre-registered) and on adding the arcsine family after runs had started (it reaches only M = 1326). Secondary, post-hoc, disclosed: Householder-normalised slopes (per instance log10(err/err_hh)): Givens 0.76 [0.06, 1.46] vs HL 0.16 [-0.04, 0.37], CGS2 -0.54 in the uniform family; Givens 1.0-1.2 vs HL 0.35-0.43, CGS2 0.10-0.15 in the Padua and arcsine families. Qualified by curvature: Givens-scheme is convex in log-log on pooled and random orders (quad +0.7..+1.5, t about 3.5); only the structured-order slope 0.93 [0.88, 0.99] is a clean power law; upper-range (M >= 496) slopes are not statistically supported (df 2). 'HL ~ sqrt(M)' is not supported (0.69-0.81). Rotation counting as a mechanism remains OPEN (worst-case count gives M^{3/2}; no model predicts the observed). Disposition: REJECTED: failed as pre-registered, scoped to the uniform-density random family (the criterion fired); the post-hoc reading does not overturn it. Theory: PD-T?bivariate-lanczos-claude-502 (MEASURED).

### IDEA 502 (prefix mechanism for 'largest')

Result (R01, `logs/analysis_r01b.txt`): catastrophe (ratio >= 1e3 and error >= 1e-10) occurs on 16 of 54 all-prefix-unisolvent cases (n >= 20), including gepp/rpiv1-3 at n = 50 with min prefix sigma_min >= 4.7e-4 (8 cases, independent of any tolerance); also 13 of 18 non-unisolvent cases. The kill rests on the **operational catastrophe threshold**, not on the seed's 7e-4 magnitude (finding M4): on well-conditioned unisolvent orders 'largest' stays <= 3.1e-9 up to n = 50; >= 1e-4 occurs only on non-unisolvent or near-singular (REPRO, sigma_min 9.7e-10) orders. Under the pre-registered tolerance (all prefixes sigma_min >= 1e-8) 14 of the 16 remain (finding L5). Confirmed by the reconstruction with independent code and two further unisolvent orders (finding on 3b: CONFIRMED). Disposition: the claim 'only on non-unisolvent prefixes' is **REJECTED: refuted** (negation established in scope, MEASURED; wording corrected after finding L8); the mechanism 'larger redundant pivot as stabiliser' is REJECTED: failed. Canonical record: PD-N?bivariate-lanczos-claude-506 (MEASURED negative, scoped n <= 62 natural/sorted orders, n <= 50 constructed orders); with PD-T?bivariate-lanczos-claude-503 (prefix statistics) and PD-T?bivariate-lanczos-claude-505 (PROVED existence of all-prefix-unisolvent orders).

### IDEA 503 (worst-case rotation-count bound)

Result (R02): Theorem A PROVED (PD-T?bivariate-lanczos-claude-501): backward error <= 16.5 u nu M(M-1), relative O(u M^{3/2}); holds for any pivot choice. **Correction (findings M1, L1):** it is not an IEP backward-stability statement (met by doing nothing; constrains neither the first column nor the zero pattern) and says nothing that distinguishes 'scheme' from 'largest'. Pre-registered kill criterion was 'same M-exponent as the comparators'. That literal criterion did **not** fire: if the comparator is the Householder QR bound (Higham ASNA Thm 19.4, UNVERIFIED by me), it is M^2 u versus M^{3/2} u here; Givens QR (ASNA 19.6) is linear in m+n (UNVERIFIED). The worst-case bounds rank Givens better than Householder, the opposite of the measured order, and the quantities are not like for like (two-sided similarity versus QR of the Chebyshev-Vandermonde matrix; no HL/CGS2 bound cited). Disposition: REJECTED: failed as an *explanation* of the measured deficit (the worst-case bound points the wrong way and is not comparable), **not** by the pre-registered criterion; Theorem A kept as a positive routine result. No PD-N (the comparator statements are unverified). Open: stage structure (2M-3 stages) may allow M u; probabilistic analyses (Higham-Mary; Connolly-Higham 2022) are the natural frame (not read in detail by me).

### IDEA 504 (safe pivot/deflation rules)

Results (R03, `logs/r03_rules.*`, `r03_defer3.*`, `r03_deferbest*.*`, `r03_detector.log`):
- (a) fixed 'scheme': **killed as an order-independent rule** by the pre-registered 10x clause: n = 50 rand3 error 1.6e-12 (cubature) and 3.4e-12 (U) versus 6.0e-14 and 6.6e-14 on the given order (27x, 52x); the absolute 1e-11 clause is not triggered at n <= 50 (max 3.4e-12) but is at n = 60 (random permutation s = 3: 2.0e-11; the other random orders 5.1e-13, 1.6e-12, 2.0e-12 [REPRO], gepp 2.0e-13; `logs/r03_x60_controls.jsonl`). Scheme is accurate (<= 3.4e-12) on every order tested up to n = 50; the failure is a growth of the order-spread, correlated with the minimum prefix sigma_min (Spearman -0.51 over 40 cases).
- (b1) pivk10, pivk100: **killed** (n = 30 given cubature: 8.6e-9 and 5.9e-12 versus scheme 2.3e-14; random weights 4.3e-3 for both); on all-unisolvent streams they equal scheme.
- (b2) pairnorm1: **killed** (equals 'largest' within 15% on rand1-3/gepp, 2.0e-12 at n = 30 rand1 versus scheme 4.7e-14); pairnorm100: never worse than 2.4x scheme (n = 30 random-weight given: 5.9e-14 versus 2.4e-14) and never better -> **equivalent to scheme** (not an improvement).
- (c) defer (tau = 1e-8): **killed** (n = 20 given 3.1e-9 and sortx 1.5e-8 versus gepp-scheme 1.9e-14; forced insertions 0-3).
- 504c' defer3 (tau = 1e-3): **killed** (n = 20 given 5.5e-10, sortx 2.0e-9; n = 30 sortx 0.13, cubature given 1.5e-3; forced insertions up to 10 at n = 30).
- 504c'' deferbestW (W = 8, 32): **not killed** at n = 20 and 30 (24 stream/parameter rows, errors 1.1e-14..6.8e-14, all <= 1.62x the gepp-scheme error of the same n/weights; the window cannot avoid singular prefixes on given/sortx -- min over the run of the min pivot is 0 -- yet the error stays at scheme level) and at n = 50 rand1 (cubature: 2.7e-13 versus scheme 1.5e-13 on that stream and 1.1e-13 on gepp, 2.4x). **No gain over scheme anywhere tested** (scheme is already as accurate on those streams). The case where a gain is possible (n = 50 rand2/rand3, and n = 60 REPRO order) was not completed (background run lost): Runs needed. Cost O(W) tentative insertions per step; not practical.
- Online detector 'prefix K singular <=> min over j <= K of |primary pivot_j| < 1e-10': **survives** 20 order/size cases (n = 10, 14, 20; no violation in either direction). Exactness in exact arithmetic: OPEN (non-routine; escalated).
Disposition: no tested modification of the pivot rule improves on 'scheme'. (b1), (b2: pairnorm1): REJECTED: failed, recorded as PD-N?bivariate-lanczos-claude-507 (MEASURED negative, scoped n = 20, 30; this includes the VB-C p. 395 'orders of magnitude' rule, finding L7); pairnorm100: equivalent (IDEA disposition, no PD-N). (c), 504c': REJECTED: failed, recorded as PD-N?bivariate-lanczos-claude-508 (finding L9). 504c'' windowed best-pivot deferral: not killed, no gain (IDEA disposition, no PD-N; n = 50 rand2/rand3 not completed). (a) scheme retained as the recommended rule with the order-spread caveat. REPRO n = 60: the 'typical draw' wording is withdrawn; the REPRO value lies within the range of four random draws (finding L6).

### ID crosswalk (finding L10; the digit blocks are separate namespaces, this table is the map)

| IDEA (candidate) | theory record(s) | note |
|---|---|---|
| IDEA 501 (rotation counting explains the deficit) | PD-T?bivariate-lanczos-claude-502 (slopes, MEASURED) | kill criterion fired as written (uniform family) |
| IDEA 502 (prefix mechanism for 'largest') | PD-N?bivariate-lanczos-claude-506; PD-T?...-503 (prefix statistics, MEASURED); PD-T?...-505 (existence lemma, PROVED) | claim refuted in scope |
| IDEA 503 (worst-case rotation bound) | PD-T?bivariate-lanczos-claude-501 (Theorem A, PROVED routine) | rejected as an explanation |
| IDEA 504 (safe pivot/deflation rules) | PD-N?...-507 (magnitude thresholds), PD-N?...-508 (FIFO deferral); PD-T?...-505 | (a) scheme retained |

Digit 506 was chosen for PD-N only to keep it distinct from PD-T 501 in human reading; the namespaces are separate and the choice is cosmetic.

## History

- 2026-10-31T23:01Z: results and dispositions revised in response to L5 reconstruction 01 (findings M2, M3, M4, L1, L5, L6, L7, L8, L9, L10): IDEA 501 headline now 'kill fired as written'; IDEA 502 'refuted' wording; IDEA 503 reason corrected; IDEA 504 (b)/(c) given PD-N 507/508; crosswalk added. The kill criteria above (written before testing, self-attested; all L5 files arrived in one commit, finding P1) were not changed.
