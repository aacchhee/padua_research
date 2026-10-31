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
- Canonical theory ID: PD-N?bivariate-lanczos-claude-501 only if R03 finds the evidence supports a scoped MEASURED negative statement for 'largest'.

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
