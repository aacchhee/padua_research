# L1 (+L4) — independent adversarial reconstruction 02 (response to reconstruction 01, R04–R07, SUMMARY)

## Header

- **Reconstructor:** Claude Opus 5.5 (`claude-opus-5-5`), effort xhigh. Same role as reconstruction 01: a separate agent from the L1 developer, no Git state changes.
- **What I wrote:** only this file, the scripts in `tracks/bivariate-lanczos/code/review_L1b/`, and the logs in `reviews/logs_L1b/` (60 KB). The scripts also import my own recon-01 module `review_L1/rv_core.py` (unchanged, sha256 `b2360c4c…2b00`). No developer code was imported or read for the reruns.
- **Date:** 2026-10-31 23:16–23:33 UTC (2026-11-01 00:16–00:33 CET).
- **Branch:** `claude/bivariate-lanczos-20261031`. Head as given: `c8ccce05baf2fa0c127b499b27fb646eef651ab6`; head during the reruns: `7f5d57b626248a115698bf0601cd956b7a72d1c5`.
  - Every audited file is identical between the two heads (`git diff c8ccce0 7f5d57b` over the L1 theory, direction, plan and code paths is empty).
  - The rule files (`AGENTS.md`, `agents/WORKFLOW.md`, `agents/claude/CLAUDE_ROLES.md`) and `state/IDEAS.md` are unchanged since `1063469` (empty `git diff`), so `state/IDEAS.md` was not re-read, as instructed.
- **Read coverage (full unless noted):**
  - `directions/L1/response-recon-01.md`, `R04.md`–`R07.md`, `SUMMARY.md`, `STATUS.md`;
  - the correction sections appended to `R01.md`–`R03.md`;
  - `candidates.md`: IDEA-101…111 corrections, PC-1…PC-12, IDEA-112…120, C01;
  - the `plan.md` diff since `b84af76`;
  - the ten theory files in scope plus the two new PD-N files, and the `git diff b84af76 HEAD` of every file audited in recon-01;
  - developer logs `r04_*`, `r05_*`, `r06_*`, `r07_*`, `c01_*` (outputs only).
- **Literature:** nothing new read. Barrio–Peña–Sauer (BPS) 2010 was read in recon-01.
- **Memory:** none used.
- **Timezone note:** the container clock is CET (UTC+1). File mtimes are quoted in UTC.

| File | SHA-256 |
|---|---|
| theory/selection-and-truncation-both-matter-measured.md (PD-N?…-105) | `ebca2453cceca650231fa1aa0a31b7b8e98d976e830174bb4fd42295e8b6ec0e` |
| theory/support-shape-does-not-classify-loss-regime.md (PD-N?…-106) | `b5b84d154066296156aac44d4379b9fa4dd9a293d2814ed4d90f9bfa30bfc265` |
| theory/near-product-transfer-perturbation-bound.md (110) | `5bec5e40a79bafa6bb2ed50e7540ad521dd1dcaea2e62280d21a40c4b092f338` |
| theory/moment-matching-product-factorization-checkerboards.md (111) | `19b908c7e8e422d5c5ec8dd552fbbcf95c2eb4600b516407211d9cc9b78637b4` |
| theory/checkerboard-and-near-product-measurements.md (112) | `6ca1657b7fcc57c3344405b91821841c9782eb69ecb165c86b990498843582e7` |
| theory/exact-certificate-propagator-growth-triangle.md (113) | `65ee3071da86eb302b8c750cdc653d1dad7d1b4aff58b2667d6a7e56939c783d` |
| theory/first-order-coefficient-channel-gains-product-type.md (114) | `dd265ef7297c914e8875c91c6870748502aee134c409e92db736c810dd6cc8d8` |
| theory/closed-loop-dot-product-rounding-carries-coefficient-channel.md (115) | `5a972f1cdce03e2eefcb943857e715c95fdf7d52afed02f8cd8228366c13918e` |
| theory/r04-failed-scaling-and-predictor-hypotheses.md (N103) | `88f93a1c484436a9856ab817f8999869959094eabb7749070d1adeeeba05dcbb` |
| theory/open-loop-coefficient-noise-estimates-fail.md (N104) | `cbb0f81e5bd1ee58cbd5ca8151f4f151bb93e7846e7e9ba95a6495f085cedf3c` |
| theory 101 / 102 / 103 / 104 (corrected) | `f5110d68…8f99` / `13fd2f50…8735` / `a2707434…589e` / `0c618867…6023` |
| theory 105 / 106 / 107 / 108 (corrected) | `b304e439…72f3` / `b9b984de…aa9` / `dae0bf50…db73` / `75c3ea0e…7ecd` |
| theory 109 / 401 / N101 / N102 (corrected) | `8decf8da…6544` / `54bf537b…749d` / `5388763d…27b3` / `47cd4f5b…a1f5` |
| directions/L1/response-recon-01.md | `d9fb5fee6d221c624a5998a51c0132e9df9ca75b4659d13f38c57f9152e5c6bf` |
| R04 / R05 / R06 / R07 | `1ad5abbc…b352` / `b9e67527…73cb` / `57d81495…27da` / `edd2d475…8c71` |
| R01.md (with corrections) | `db0cf3aa9d01e788158c65317248f4106771d9953cd59cf473f3e72576660fe6` |
| R02.md (with corrections) | `72acc598f090e5ddb209c47eb5bb65ad726fc94e2e1e7e44c81ee08f6df30037` |
| R03.md (with corrections) | `324e9621e498a10f70a7af78b507f888aeec693100c97a33008fdc9ae67404d5` |
| SUMMARY.md | `4fb6bb955692690ced8b3e7e20844d463ab0d397c06a5e0b2b25f68d6eebeddb` |
| STATUS.md | `60d077af301c5feacfc0f24a82e7f4585dfaf19066c37f865b6036c9d8947db5` |
| candidates.md | `c842418cd967ab26b34316050a90f2f4657db3e7bd8cec1492ff105bd581c70d` |
| plan.md | `65f29146c195fdbc956e431b3d45783f15f866261e03459a6e75f8b46e3a8d47` |

## Verdict summary

| Item | Verdict |
|---|---|
| Response to recon-01 (B1, B2, majors, minors) | **Faithful.** No silent narrowing found. Refuted claims are marked REJECTED: refuted with scoped PD-N links. History/Correction lines are present. No backdating relative to review 01. Minor documentation gaps (m3–m5). |
| PD-N?…-105 (selection and truncation both matter) | **CONFIRMED.** The selection dependence also holds on a product-type measure, with set-dependent winners (M1) |
| PD-N?…-106 (support does not classify the regime) | **CONFIRMED WITH CORRECTIONS** (minor m2) |
| 110 near-product transfer bound | **CONFIRMED** (proof re-derived; informativeness numbers not rerun) |
| 111 moment matching, checkerboards | **CONFIRMED** (re-derived; exact rational check, sharp at degree 2m+1; ordering hypothesis necessary) |
| 112 checkerboard measurements | (a), (b), (d) **CONFIRMED** by an independent rerun; (c), (e), (f) not rerun |
| 113 certificate | Part 1 **CONFIRMED**. Part 2 **CONFIRMED by an independent exact rerun.** The computer-proof obligations are now met, so I recommend **CONDITIONAL → PROVED** with two wording corrections (M2). Part 3: T_40 and rotated Q_24 reproduced exactly; Q_40 not rerun. |
| 114 coefficient-channel gains | Parts 1–4 **CONFIRMED** (re-derived). Part 5: the IDEA-117 on/off split is reproduced independently; the gain magnitudes are not rerun |
| 115 closed-loop dot-product rounding | **CONFIRMED in a convention-free form**, stronger than its corrected text: actual double dot products alone reproduce L within 0.56–1.86 on all six sets (M3) |
| N103 | (c) **CONFIRMED**; (a), (b) not rerun |
| N104 | (c) trend **CONFIRMED convention-free**; with actual rounding the kill is **inconclusive**, matching the developer's correction; (a), (b) not rerun |
| SUMMARY.md ranking | **Faithful to statuses.** Corrections needed in item 3, item 5 and §5 (M1, M2, M3) |

**Blocking findings: none.**

## 1. Response to reconstruction 01: faithfulness

| Recon-01 finding | Developer disposition | My check |
|---|---|---|
| B1 (109 Consequence) | REJECTED: refuted, new PD-N?…-105. 109's title narrowed with the original kept. IDEA-111 REJECTED: refuted. R03 F8 withdrawn. STATUS R03 annotated. | Faithful. The rerun numbers (C01-2/3) agree with mine at different seeds. Example at n = 24: rotation 0.3 dev 5.8e-6 (mine 4.7e-6), adapt 2.9e-12 (mine 1.3e-12); full single-pass CGS on rotation π/4 1.9e-14 (mine 3.8e-14). The dependence check (113 restated as a dev-rule statement; 110/111/114/115 independent of B1) is correct. |
| B2 (K1, tensor n = 40) | K1 inconclusive; N101(b) withdrawn as evidence. The Consequences line is narrowed with the original kept. IDEA-101/-102 rejection reasons narrowed. STATUS R01 annotated. The plan ledger was corrected by the orchestrator. | Faithful. The developer also applied the u-convention lesson to R07 without being asked (C01-6), which is good practice; §2 below decides those verdicts convention-free. |
| 107 support classifier | New PD-N?…-106; corrections block in 107 | Faithful. The developer disclosed a discrepancy with my exp(4xy) run (see m2). |
| 109(b) two-relation scope | Heading narrowed with the original kept | Faithful |
| 105 scope | Scope rewritten with the original kept | Faithful |
| 108 attribution | Sources section (Xu / Dunkl–Xu, BPS, Liu–Narayan, OTV) with the separation | Faithful. The separation (monic vs coupled graded basis) matches what I found in BPS. |
| Minor fixes in 102, 103, 105, 106, 401, N102 | Corrections in place, originals kept | Verified line by line in `git diff b84af76 HEAD`. My own T-401 extensions are recorded as mine and unaudited, which is correct. |

**Timestamps and backdating.**
- Review 01's final mtime is 22:57:54Z. Every correction stamp in the L1 files is ≥ 23:00Z (stamp census: 23:05Z ×29, 23:10–23:14Z otherwise).
- The C01 criteria (23:02:34Z) precede the first C01 log (23:03:11Z). C01-6 (23:09:22Z) precedes `c01_u53_rerun.log` (23:09:47Z).
- No stamp predates the review, so there is no backdating.
- The disclosed guessed stamps cannot be checked precisely, because all R01–R07/STATUS/candidates files share one batch-edit mtime (23:14:26Z). Their ordering relative to the review is correct (m5).

**Pre-registration of R04–R07, against the git WIP snapshots.**
- Positively verified for IDEA-112/-113. Their K1–K3 and C1–C2 criteria are in snapshot `e038ed3` (22:01:46Z), before `r04_near_product.log` (22:02:34Z) and `r04_checkerboard.log` (22:03:18Z).
- Positively verified for IDEA-120. Its criterion is in `3d6c0da` (22:40:47Z), before the stated run start (22:40:51Z; log 22:41:15Z).
- IDEA-114–119 and -116 are *consistent with but not verifiable from* the snapshots: the first snapshot containing each record postdates its log (for example, IDEA-116 first appears in `d1e8150` at 22:15:45Z, after the certificate logs at 22:15:17Z and 22:15:30Z; the earlier `ec7fb5b` at 22:12:48Z lacks it).
- No contradiction found.

## 2. R04–R07 claims

### PD-T?…-113 — exact certificate (the computer-proof decision)

**Independent exact rerun** (`rv2_certificate.py`), from the statement only. It does not use the developer's checker or their window tables.
- **A.** The monic graded basis by *full* exact Gram–Schmidt of the dev products against all previous vectors. Off-window coefficients are checked to be exactly 0.
- **B.** The same basis independently from an exact LDLᵀ factorisation of the monomial moment matrix (ψ = L⁻¹m). Node values and every D_k agree with A exactly (T_24, Q_24).
- **C.** Exact orthogonality: 0 nonzero inner products among 4095 pairs (T_24, Q_24), 11628 pairs (T_40) and 7140 pairs (rotated Q_24, n ≤ 14).
- **D.** The entries via the impulse identity in integer coordinates, rescaled by (m/2)². The rescaling was also verified directly: a run in rescaled rational coordinates reproduces the developer's values *and their exact numerator/denominator bit counts* (9/8 … 116/65).
- **E.** Part 1 (the identity) checked by building the orthonormal L*(z) in mpmath at 60 digits from the exact data and inverting it at 3 nodes per set: maximum relative deviation 1.9e-56 (T_24) and 6.1e-60 (Q_24).

**Results** (log10 G(n), n = 2…12):

| Set | Mine | Developer |
|---|---|---|
| T_24 | 0.446, 2.445, 3.874, 5.224, 6.525, 7.931, 9.360, 10.768, 12.172, 13.696, 15.211 | identical to 3 decimals, with the same maximising (s, k) at every n |
| Q_24 | −∞, 1.102, 1.544, 1.836, 2.014, 2.166, 2.286, 2.379, 2.471, 2.591, 2.809 | identical |

- Criterion decided **in exact rational arithmetic** (the ratio is scale-free): T_24 has G(12) ≥ 10⁶·G(6) (TRUE; increment 8.686), and Q_24 has G(12) ≤ 10²·G(6) (TRUE; 0.795).
- Part 3:
  - T_40, n ≤ 16: 0.464 … 20.896, matching the developer's two-decimal values; increments 1.38–1.50 per degree.
  - Rotated Q_24, n ≤ 14: −0.431 … 13.951, all matching once my own sign slip in the 5×-scale conversion was fixed (log retained).
  - Q_40: not rerun.

**Status.** The reduction (part 1, re-derived and numerically confirmed), exact arithmetic, the committed checker and logs, and an independent rerun are all present. Part 2 therefore meets the workflow's computer-proof rule.

**M2 (major, wording before the upgrade).**
- (i) The Statement defines G(n) over "columns k of degree n". With k = s included, G(2) on Q_24 would be max_s 1/β_s² > 0, not "exactly 0". The computed quantity uses **k > s**, and the definition must say so.
- (ii) The PROVED statement should be the exact finite one, for the dev rule, degree-2 impulses, rescaled coordinates and n ≤ 12: the listed values, G(12) ≥ 10⁶G(6) on T_24 and G(12) ≤ 10²G(6) on Q_24. The title's "grows exponentially" stays a descriptive finite-range gloss with no asymptotic claim, as the History already says.
- Trusted dependencies of my rerun: CPython `fractions` and big-integer arithmetic; `math.log10` is used for reporting only; mpmath is used only for the part-1 cross-check.

### PD-T?…-110 — near-product bound: CONFIRMED

- I re-derived the transfer form (rows of degree t involve only degrees t, t−1, t−2 for the block or exact window). The telescoping identity and discrete Gronwall induction are correct: x_b ≤ K + KΣε_r x_{r−1} ≤ y_b.
- K(z) covers every sub-product, as the lemma needs.
- Minor m7: "the diagonal block is −D_t⁻¹" is the block of the map Φ ↦ P = −L*⁻¹Φ; the block of L*⁻¹ itself is +D_t⁻¹. Norms are unaffected.
- The informativeness numbers (112 (f)) were not rerun.

### PD-T?…-111 — moment matching and checkerboards: CONFIRMED

- Part 1: inner products of degree-≤-n polynomials and every window coefficient creating degree ≤ n are integrals of degree ≤ 2n. Re-derived.
- Part 2: the signs (−1)^{m−i} and (−1)^{m+1−j}, the parity indicator, the vanishing divided differences for x^a y^b with a + b ≤ 2m, and |S_e| = N_m are all re-derived.
- Exact rational check (`exact_checkerboard.log`; m = 4; equispaced e = 0/1, cubic s³, an irregular ordered set):
  - 0 moment mismatches for a + b ≤ 2m;
  - the first failure is exactly x⁴y⁵ (a = m, b = m+1, as the proof predicts);
  - 0 coefficients outside the product (chain) pattern up to degree m.
- With unordered labels Y = (0, 1, 3, 2) the identity fails (6 mismatches) and the pattern breaks, consistent with AC's ordered-nodes correction.

### PD-T?…-112 — checkerboard measurements: (a), (b), (d) CONFIRMED

Independent implementation (`rv2_checkerboard.py`, `checkerboard.log`, `checkerboard_ritz.log`): m = 30, e = 0, M = 496, x = s³; factor weights 1.7e-33…0.49; bivariate weights 1.8e-67…0.47, confirming PC-12.

- **(a)** BJ loss at n = 8/12/16/20/24:

  | Family | Loss |
  |---|---|
  | Lobatto | flat at 3.6e-15 |
  | equispaced | mild, 2.9e-14 |
  | cubic | 7.2e-16 / 3.0e-14 / 1.7e-11 / 5.3e-9 / 1.0e-6 (developer 7e-16 … 7e-7) |

  - Long double cubic: 5.3e-15 at n = 16 (ratio 3.2·10³ against an ε-ratio of 2048), so the growth scales with u.
  - Univariate Lanczos on the factors stays ≤ 6e-16 to step 20.
  - HL/ORTH (7.0e-6) and block CGS2 (1.0e-5) at n = 24 also lose, and by more than BJ.
  - It is not Ritz-type: u/ρ_Z ≤ 2.1e-14 and u/ρ_{X,Y} ≤ 2.1e-11 at u = 2^-53.
- **(b)** Exact split: the Gram defect of Ξ̄ = Ξ(c_BJ) equals L to the printed digit, while |Φ̃| = max|Ξ̄ − Q̂| ≤ 1.1e-15 up to n = 20. That is the coefficient channel. Independently reproduced IDEA-117 table, D(·) at n = 8…24:
  - D(c*) ≤ 1.3e-18;
  - D(c_BJ on-pattern only) ≤ 2.1e-15 to n = 20 (3.0e-12 at n = 24);
  - D(c* + c_BJ off-pattern) = L.

  So H_off is confirmed. Minor m10: my on-pattern deviation including β is 3.0e-13 over degrees ≤ 24 (PC-11 quotes 1.6e-14); harmless either way, given the on-pattern-only D.
- **(d)** The two-relation control fails: 1.1e-5 (n = 12), 0.29 (n = 20), 0.61 (n = 24). Confirmed.

### PD-T?…-114 — coefficient-channel gains: parts 1–4 CONFIRMED

I re-derived each part:
- the variation ∂ξ_k = −ξ*_l/β*_k with R propagated by the c* recurrence;
- tree propagation (with product-type c*, a forcing at (t, j ≥ 1) stays on the y-chain of x-degree i as ψ_l G^{y,[j]}; at (t, 0) it moves along the x-chain and then multiplies by r_r on each y-chain based at (i′ ≥ t, 0));
- the Gram derivative: integrand degree ≤ 2n, so moment matching plus Fubini gives the stated univariate factors;
- the on/off split (on-pattern ⟺ i_l = i for j ≥ 1, j_l = 0 for j = 0).

Minor m8: "(A β_k-perturbation is the case l := k with weight β*_k)". The β-derivative is −ξ*_k/β*_k, i.e. R^{(k,k)} with no extra weight; the parenthesis is unclear. Part 5: the decisive split is reproduced (112 (b) above); the gain magnitudes (on ≤ 5e3, off ≤ 1.3e14) were not rerun.

### PD-T?…-115 and PD-N?…-104 — convention-free decisions (M3)

The noise-model verdicts were labelled convention-sensitive. I replaced the model by **actual IEEE-double dot products**, so no u-convention is involved:

- **Closed loop** (`rv2_closed_loop.py` / `rv2_closed_loop_sets.py`; everything in long double except the window inner products, computed by a float64 BLAS product). C/L on the six IDEA-120 sets, n = 12/16/20/24:

  | Set | C/L |
  |---|---|
  | cubic m = 30 | 1.05 / 0.63 / 0.87 / 0.70 |
  | equispaced | 0.74 / 0.67 / 1.00 / 0.93 |
  | quadratic | 0.80 / 0.73 / 0.81 / 0.76 |
  | quartic | 0.77 / 0.66 / 0.87 / 0.87 |
  | cubic m = 36 | 1.86 / 0.56 / 0.84 / 0.85 |
  | Lobatto | 1.07 / 1.03 / 0.96 / 0.96 |

  **IDEA-120's rule gives "survives" on all six**, and PD-T?…-115's title claim holds. The term-wise N(0,1) model underestimates the actual rounding: on cubic m = 30 at n = 16, C/L = 0.16 at σ = u/√3 (the "physical" calibration the developer proposed), 0.28 at σ = u = 2^-53 and 0.57 at σ = 2u. The per-term model misses the summation rounding.
- **Open loop** (`rv2_open_loop.py`; c* plus the actual double rounding of the dot products of the exact vectors, off-pattern entries, as in IDEA-119). E/L at n = 16/20:

  | Set | E/L |
  |---|---|
  | quadratic | 1.13 / 0.53 |
  | cubic m = 30 | 5.13 / 4.70 |
  | quartic | 21.6 / 12.9 |
  | cubic m = 36 | 16.4 / 21.1 |
  | Lobatto | flat |

  - IDEA-119's rule gives **inconclusive**, not killed. This matches the developer's 2^-53 correction ("no longer REJECTED").
  - IDEA-118 H_term (cubic m = 30, within 10×) gives **survives**.
  - The over-estimate grows with clustering. The feedback damping (open/closed) is ≈ 1.5 (quadratic), 8 (cubic m = 30), 30 (quartic, cubic m = 36) at n = 16. N104 (c)'s trend is confirmed.
- **Recommendation:** replace the convention-sensitive labels with these convention-free verdicts, citing these logs, or rerun the developer's scripts with actual reduced-precision dot products.
- **m1:** two texts are stale after the correction: 115's title ("the closed-loop model reproduces the loss") and N104 §Scope ("the closed-loop model … succeeds on the same sets"). Both are true for actual rounding (above) but not for the developer's noise model at 2^-53.

### PD-N?…-103: (c) CONFIRMED

See 112 (d). (a) H_lin and (b) the predictor failures were not rerun.

### PD-N?…-105 and the selection dependence on a product-type measure (M1, major)

`checkerboard.log`, block window, one CGS pass, n = 24:

| Set | dev | mirror | alt | adapt | two-relation |
|---|---|---|---|---|---|
| cubic checkerboard | 1.0e-6 | 2.7e-7 | **3.1e-13** | **9.3e-6** | 0.61 |
| equispaced | 2.9e-14 | 1.8e-14 | 1.4e-15 | 4.1e-14 | — |
| Lobatto | 3.6e-15 | 2.6e-15 | 2.0e-14 | 1.1e-13 | — |

- So the selection effect is not confined to non-product sets: on the clustered product-type checkerboard the coefficient-channel loss changes by 3·10⁶ between dev and alt.
- The pivot-adaptive rule, which was the best rule on rotation 0.3 and the triangle, is **9× worse than dev** here.
- Consequences:
  - SUMMARY §5 ("The alt and adapt rules reduce the loss by 10³–10⁸") and the open item "a selection principle" must carry this counterexample. Adapt is not a remedy to hand to L2 unqualified.
  - The 112/114/115 statements are dev-rule statements. 112's History says so. SUMMARY item 5 does not, and should.
  - PD-N?…-105 itself is correct within its stated scope. Its "Not covered: other parent rules" could add the product-type checkerboard as an extension, with the reversed ranking of adapt.

### PD-N?…-106: CONFIRMED WITH CORRECTIONS

- Minor m2: the u/ρ predictions omit the scale ‖A‖ (Paige's prediction is u‖A‖/ρ). The standard-normal cloud of (b) has ‖X‖ ≈ 3–4, so "2.4·10³×" overstates by about that factor; the conclusion is unchanged.
- Correction to my own recon-01 wording: I called exp(4xy) "stable", but my `extra.log` (ii) shows 4.3e-13 against u/ρ_Z = 9.4e-14 (4.6×) at n = 24. The developer's 32× is a quantitative, seed-level difference, not a contradiction.

## 3. SUMMARY.md ranking

- The ranking matches the claim statuses. Item 1 rests on K2, as required. Withdrawn and refuted items are listed in §2. Attributions to recon-01 are kept in the theory files.
- Item 3: 113 part 2 can move to PROVED, with the M2 wording.
- Item 5: add "dev rule" and the convention-free closed-loop result (M3). Optionally rank it below the Paige identities: it is shown only on extreme-weight checkerboards (weights down to 1e-67).
- §5 L2 hand-off: add the adapt counterexample (M1).
- §6: "Certificate rerun" is done.

**Other documentation items:**
- m3: STATUS R02 is not annotated. Its "predicts loss within 1–5x in both regimes" is superseded by PC-3 and PD-N?…-106. STATUS R05 still says CONDITIONAL.
- m4 (orchestrator-owned): in the plan ledger, the R03 row lacks the B1 correction; the note sits on the R02 row.

## 4. Reruns (actual executions)

**Environment:** Python 3.13.18, NumPy 2.5.3, mpmath 1.3.0, SymPy 1.13.3 (not used), x87 long double, 2 cores.

Commands are run from `tracks/bivariate-lanczos/code/review_L1b/`; `L` = `topics/bivariate-lanczos-20261031/reviews/logs_L1b/`.

| Command | Output |
|---|---|
| `python3 -I -u rv2_certificate.py triangle 24 12 integer mp` | `L/cert_T24.log` (27 s) |
| `python3 -I -u rv2_certificate.py square 24 12 integer mp` | `L/cert_Q24.log` (37 s) |
| `python3 -I -u rv2_certificate.py triangle 24 12 rescaled` | `L/cert_T24_rescaled.log` |
| `python3 -I -u rv2_certificate.py triangle 40 16 integer` | `L/cert_T40.log` (79 s) |
| `python3 -I -u rv2_certificate.py rotsquare 24 14 integer` | `L/cert_rotQ24.log` (199 s; after the rotation-scale fix) |
| `python3 -I -u rv2_certificate.py {triangle,square} 24 12 integer` | `L/cert_{T24,Q24}_exactcmp.log` (exact criterion comparisons) |
| `python3 -I -u rv2_exact_checkerboard.py` | `L/exact_checkerboard.log` |
| `python3 -I -u rv2_checkerboard.py` | `L/checkerboard.log` |
| `python3 -I -u rv2_checkerboard_ritz.py` | `L/checkerboard_ritz.log` |
| `python3 -I -u rv2_closed_loop.py` | `L/closed_loop.log` |
| `python3 -I -u rv2_closed_loop_sets.py` | `L/closed_loop_sets.log` |
| `python3 -I -u rv2_open_loop.py` | `L/open_loop.log` |

The first four certificate logs come from the script version before the rotation-scale and exact-comparison edit; the edit affects neither the triangle nor the square values.

- **Seeds:** the noise model uses `default_rng(0..2)`. Everything else is deterministic.
- **Script SHA-256:**

  | Script | SHA-256 |
  |---|---|
  | rv2_certificate | `b817545b…9501` |
  | rv2_checkerboard | `d29ed806…02a2` |
  | rv2_checkerboard_ritz | `870fa766…bdf` |
  | rv2_closed_loop | `2f3fe373…bc76` |
  | rv2_closed_loop_sets | `6ab077f6…ff42` |
  | rv2_exact_checkerboard | `be0a8dd4…f462` |
  | rv2_open_loop | `2a41103f…b3da` |

## 5. Remaining uncertainty

- **Not rerun:**
  - 110/112 (e)(f) (rotation sweep, informativeness);
  - N103 (a)(b);
  - 114's gain magnitudes and formula check;
  - IDEA-118's φ/ρ anatomy;
  - the C01 numbers beyond overlap with my recon-01 runs;
  - Q_40.
- **Scope:** one seed per random set, and checkerboards only at m = 30/36.
- **What the certificate covers:** it is exact but finite (n ≤ 12, two grids, dev rule). No asymptotic statement is supported.
- **Calibration:** "actual double dot product" means NumPy/OpenBLAS summation on this machine. Another BLAS could shift C/L by small factors.
- **Selection dependence:** the product-type finding (M1) is one measure and four rules.
