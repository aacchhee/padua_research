# L2 candidate records

Direction L2 (provable partial/selective reorthogonalization) of topic `bivariate-lanczos-20261031`. Developer: Claude Opus 5.5, effort xhigh. Template `templates/IDEA.md`. Provisional IDs `IDEA?bivariate-lanczos-claude-2nn`; final IDs only at PR preparation. No novelty claims (the adversarial reconstruction is a separate agent).

## Conventions (fixed before any L2 run)

- **u := 2^-53** (unit roundoff, as plan.md and PD-T?…-102 define it; the L1 reconstruction showed that L1's u := 2^-52 flips a frozen verdict). √u = 1.05e-8, u^{3/4} = 1.11e-12, 10³u = 1.11e-13.
- Recurrence: BJ ordering of PD-T?…-101 (column (t,0) = X·(t−1,0) "J", column (t,j≥1) = Y·(t−1,j−1) "F"), block window (degrees t−2..t), CGS, unless a record states otherwise. HL mirror = same code with (x, y) exchanged.
- L(n) := max|Q̂_nᵀQ̂_n − I| over columns of degree ≤ n (diagonal included), Gram in double.
- Benchmarks (the L1 set): random square, square rotated 0.3 and π/4, disk, triangle (M = 1681, the rng(11) construction of `code/L1/l1_node_propagator.py`); random L-shape and annulus (M = 3000, `l1_recurrence.nodes_lshape_random(3000,1)`, `nodes_annulus_random(3000,2)`); tensor Chebyshev 41²; Padua n = 48 with cubature weights; ordered Harris–Simanek checkerboards m = 30 (Chebyshev–Lobatto, equispaced, cubic-clustered; weights |1/ω′_X||1/ω′_Y|, `code/L1/l1_r04_checkerboard.py`).
- Dependencies on L1 results are CONDITIONAL inputs (developer results under review): PD-T?…-101, -102, -104, -106 (identities; reconstruction 01: CONFIRMED), -108, -114, -115.

Novelty-gate scope (2026-11-01, before R01): `state/IDEAS.md` read in full in bounded chunks (seed rows 001–048, OBST-01..15, disposition table); `baseline-candidates.md` rows 003, 008 (the L2 seeds), 036, 040; `literature/INDEX.md` all rows (abridged view) and the records simon-1984-mathcomp (LIT-008/009/210–213), simon-1984-laa (010/214), larsen-1998 (011), jia-li-2021 (012), bai-day-ye-1999 (013), paige-1971/1976/1980-lanczos (201–206), zhu-nakatsukasa-2026 (024/025), carson-et-al-2025 (022/023), liu-narayan-2023, barrio-pena-sauer-2010 (301–303), zaccaron-2014; `reviews/L1-prior-art-01.md` (its (d): the ω-recurrence template is Simon's; no two-operator / commutator form found in that search) and `reviews/L1-reconstruction-01.md` (selection rule decides; single-pass untruncated CGS unstable on some sets). Terms searched across ideas, theory, logs, literature: reorthogonal, semi-orthogonal, semiorthogonal, omega, ω-recurrence, partial, selective, twice is enough, CGS2, commutator residual, implicit section. Closest entries: IDEA?…-003 (partial/selective reorthogonalization, "near-transcription of Simon/PROPACK/Jia–Li"), -008 (commutator-defect ω-recurrence remark), OBST?…-03 (H_y only partly formed), OBST?…-07 (BCGS2 results cover full, not truncated, orthogonalization), -036 (sketched alternative, deferred). Limitation: Simon LAA 61, Larsen 1998 and the Jia–Li fulltext are not read (records are abstract/secondary); the 1D semi-orthogonality theorem is known only through Simon Math. Comp. Thm 2 (proof deferred there) and secondary accounts.

---

## IDEA?bivariate-lanczos-claude-201 — ω-recurrence estimate, rounding-only sources (Simon transcription with the implicit J-section)

Aliases: E1 (random sources), E1D (sign-matched sources); "2D Simon ω-estimate"; L2-Q1(a) primary estimator.

- Question / scope: does the estimate track L(n) on the benchmark set (frozen L2-Q1, first clause)?
- Mechanism and hypotheses: run the exact ω-recurrence of PD-T?…-106 online with the run's computed coefficients: for column k (operator A, parent p, window W, coefficients h, β), out-of-window l: β ω̃_{lk} = Σ_r (T_A)_{rl} ω̃_{rp} − Σ_{l′∈W} h_{l′} ω̃_{ll′} + θ_{lk}; in-window l: β ω̃_{lk} = −Σ_{l′∈W, l′≠l} h_{l′} ω̃_{ll′} + θ_{lk} (the CGS in-window identity, PD-T?…-106 with h_l = q̂_lᵀAq̂_p + rounding); T_F = computed F-coefficients, T_J = Ĥ_J (implicit J-section from computed coefficients, PD-T?…-104 part 2), built online from data of lower degree only. Sources: θ_{lk} = ε_{lk} · u · (‖(h, β)‖₂ + ‖T_A e_l‖₂) out of window and ε_{lk} · u · ‖(h, β)‖₂ in window; E1: ε_{lk} iid N(0, 1) (Simon-type), estimate = median over 5 seeds; E1D: ε = sign of the propagation term (Larsen-type conservative). Diagonal fixed at u. No commutator term: J-steps use Ĥ_J as if the J-relation had only rounding error.
- Closest registry entries: IDEA?…-003, -008; LIT?…-210, -212 (Simon's random-source ω-estimate).
- Separation criterion vs closest entry: Simon's recurrence is tridiagonal with two neighbours; here the propagation uses the 2D window and the implicit section Ĥ_J, and the in-window CGS cascade (2t+1 neighbours) is propagated rather than set to a rounding constant. Falsified as a distinct object if the in-window and J-terms are numerically irrelevant (estimate unchanged when they are replaced by Simon's constants).
- Literature baseline: Simon 1984 §5 (random sources; overestimates initially, tracks near √u), as digested.
- Applicable obstructions: OBST-03 (J-section implicit) — handled by Ĥ_J; the commutator residual is ignored here (that is -202's difference).
- Novelty gate verdict: variant with difference of IDEA?…-003/-008 (within documented search).
- Cheapest decisive test: the frozen comparison on the 13 benchmarks.
- **Kill criterion written before testing (frozen L2-Q1 operationalised).** Per benchmark: E(n) = max off-diagonal |ω̃_{lk}| over deg k ≤ n (median over 5 seeds for E1); informative degrees D = {n : L(n) ≥ 10³u or E(n) ≥ 10³u}; U = max_{n∈D} L(n)/E(n). The estimate is **killed** if U > 10 on any benchmark. Tracking (reported, no kill): O = max_{n∈D} E(n)/L(n); "tracks within factor c" if max(U, O) ≤ c on every benchmark. Degrees: all n up to the benchmark's nmax (listed in R01); no exclusion of saturated degrees.
- Test discriminability: the estimate shares the propagation operator with the true Gram recursion, so an underestimate can only come from source magnitudes, the J-step (commutator), or the in-window model; the checkerboard sets isolate the coefficient channel, the rotated/triangle sets the vector channel.
- Actual test results: see R01.md.
- Disposition: pending.

## IDEA?bivariate-lanczos-claude-202 — ω-estimate with the commutator channel measured on the J-columns ("J-measured hybrid")

Aliases: E2; commutator-exact J-steps; "measure the n injected columns, estimate the N − n others".

- Mechanism: as E1 for F-columns; for each J-column k = (t,0) the row ω_{·k} is measured exactly (one inner-product pass Q̂_{<k}ᵀq̂_k). By PD-T?…-106 this equals using the exact commutator source (C_res e_l)ᵀq̂_p = q̂_lᵀ(Jq̂_p) − Σ_r (Ĥ_J)_{rl}ω_{rp} with exact ω. Cost of the measurement: Σ_t M N_{t−1} ≈ M n³/6 flops-pairs, i.e. ≈ 1/4 of the CGS window cost, same order O(M N^{3/2}).
- Closest entries: -201, IDEA?…-008. Separation: differs from -201 exactly by the commutator source of the J-steps; falsified as distinct if E2 ≈ E1 on all benchmarks.
- **Kill criterion (before testing):** identical to -201 (U > 10 on any benchmark kills).
- Disposition: pending.

## IDEA?bivariate-lanczos-claude-203 — 2D Simon theorem: semi-orthogonality implies accurate sections

Aliases: L2-Q1(b); "semi-orthogonality ⇒ sections = WᵀXW, WᵀYW + O(u)"; F-part / formed-J-part / implicit-J-part.

- Question: if ‖Q̂ᵀQ̂ − I‖ ≤ √u, are the computed sections equal to W_nᵀ(F, J)W_{n−1} for the orthonormal basis W = Q̂R⁻¹ (R = chol(Q̂ᵀQ̂), nested spans) up to O(u)‖(X, Y)‖?
- Mechanism (intended proof route, before testing): exact identity W_nᵀAW_{n−1} − T_A = (R T̃_A R′⁻¹ − T_A) + R⁻ᵀQ̂ᵀE_AR′⁻¹; profile preservation of R T̃ R′⁻¹ (generalised Hessenberg); symmetry of the square part; first-order terms reduce to products (coefficient × local Gram entry) for pairs inside a common window; second-order terms O(‖Ω‖²). For J the "local error" E_J is the commutator residual C_res, which is not a rounding quantity.
- Closest entries: LIT?…-211/-214 (Simon Thm 2 / LAA Thm 5, single operator), -003. Separation: two operators, growing blocks, injected J-columns, implicit Ĥ_J, window cascade; falsified as distinct if the 1D proof applies verbatim.
- Applicable obstructions: OBST-03 (J implicit), OBST-07 (no truncated BCGS2 theory).
- **Kill criterion (frozen L2-Q1 second clause, operationalised before testing).** Section errors, relative to ‖(X, Y)‖ := max(max|x_i|, max|y_i|): e_F(n) = max|W_nᵀFW_{n−1} − T_F|; e_τ(n) = max over formed J-columns (t, 0), t ≤ n−1, of |W_nᵀJW_{n−1}e_{(t,0)} − Ĥ_Je_{(t,0)}|; e_H(n) = max over all columns of degree ≤ n−1 of |W_nᵀJW_{n−1} − Ĥ_J|. A run is semi-orthogonal at n iff L(n) ≤ √u. "Section error ≫ u" := e > u^{3/4} (= 10⁴u). The criterion "semi-orthogonality guarantees O(u) sections" is **killed for a section type** if some benchmark has a semi-orthogonal (n, run) with that e > u^{3/4}. Runs: plain BJ (its semi-orthogonal degrees), BJ with full CGS2 reorthogonalization against all previous vectors (V+A-type), BJ with oracle partial reorthogonalization at √u. Evaluation floor check: the same quantities on a product set with full reorthogonalization must be ≤ 10²u, otherwise the evaluation is not discriminating.
- Disposition: pending.

## IDEA?bivariate-lanczos-claude-204 — full reorthogonalization keeps the computed graded spaces close to S_n (H_drift)

Aliases: "reorthogonalization cures the non-product instability"; span-drift test; V+A-type CGS2 with the BJ selection.

- Question: on non-product benchmarks, with full CGS2 reorthogonalization (Q̂ orthonormal to O(u)), is span(Q̂_n) close to the exact graded space S_n = {p(X,Y)√w : deg p ≤ n}?
- Mechanism (hypothesis to be tested): reorthogonalization removes in-span error components; out-of-span components (the J-defect of PD-T?…-102 part 4) are propagated by the F-marching (defect recursion) and might not be removed.
- Reference: U_ref = Householder QR (double) of the product-Chebyshev Vandermonde [T_a(x̃)T_b(ỹ)√w]_{a+b≤n} on the bounding-box-scaled coordinates; reference accuracy bound ρ_ref(n) := u·κ₂(V_n).
- Drift d(n) := ‖(I − U_refU_refᵀ)W_n‖₂ (sine of the largest principal angle).
- **Kill criterion (before testing):** H_drift is killed if, on some benchmark, d(n) > √u at a degree where ρ_ref(n) < 10⁻¹¹. It survives if d(n) ≤ 10³·max(ρ_ref(n), u√N_n) at all tested degrees of all benchmarks; otherwise inconclusive.
- Test discriminability: the reference error bound is computed per degree, so a drift above √u with ρ_ref < 1e-11 cannot be a reference artefact.
- Disposition: pending.

## Diagnostic (no kill test): one-step source audit

For the plain BJ run, compute in long double the actual source s_{lk} := β_kω_{lk} − [propagation − window terms with the exact ω] and compare |s_{lk}| with the model scale σ_{lk} of IDEA?…-201, per degree (max and median of |s|/σ), separately for F-steps (out of window), J-steps (out of window; contains the commutator source) and in-window entries.

---

## Post-hoc additions (written 2026-11-01T00:12:00+01:00, AFTER the R01 E1/E2 run and the rotπ/4 section smoke test; disclosed)

### IDEA?bivariate-lanczos-claude-205 — componentwise in-window sources (E3)

Aliases: E3; "abs-dot scale"; coefficient-channel-aware ω-estimate.

- Motivation (seen before writing): E1 overestimates the cubic-clustered checkerboard by 2.4·10⁵ (coefficient channel; PD-T?…-115 reports dot-product terms ≈ 10⁻⁶u at the high-gain entries).
- Mechanism: E1 with the in-window source scale replaced by u·(|q̂_l|ᵀ|Aq̂_p|) for l ∈ W_k (one extra matvec with absolute values per column, same cost as the window coefficients); out-of-window scale unchanged.
- Kill criterion (written before running E3): the frozen rule (U > 10 on any benchmark kills). Improvement criterion: E3 counts as a tracking improvement only if O(cb_cubic) drops by ≥ 100× and O does not rise by > 3× on any other benchmark.
- Disposition: pending.

### Amendment to IDEA?…-204 (drift), disclosed post hoc

The smoke test on rotπ/4 showed the box-scaled Chebyshev reference has u·κ ≈ the measured drift at every degree (not discriminating there). Added after seeing it: (i) a reference-free certificate, the proved inequality max(θ_s, θ_{s+1}) ≥ δ_J(s)/(2‖J‖) where δ_J(s) = max column norm of (I − Π̂_{s+1})J Ŵ_s (J-defect of the computed spans) and θ_s the largest principal angle between Ŝ_s and S_s; (ii) for the rotated squares, a second reference in the unrotated frame (S_n is rotation invariant). H_drift is also counted as killed if δ_J(s)/(2‖J‖) > √u for a fully reorthogonalized run. The pre-registered rule is reported unchanged alongside.

### IDEA?bivariate-lanczos-claude-206 — two-pass window (CGS2 restricted to the window)

Written 2026-11-01T00:16:00+01:00, AFTER the R01 section suite showed that the semi-orthogonal F-section failures (rot0.3, triangle, annulus) coincide with growth of the local level μ (in-window Gram entries), and BEFORE any two-pass-window run.

Aliases: "two-pass window"; CGS2-window; local-orthogonality repair; task item "two-pass window".

- Mechanism: second CGS pass against the same window W_k (coefficients added to h). Proposition L (to be proved in R01): β_k|Ω_{W_k,k}| ≤ ‖Ω_{W_k}‖²‖h⁽¹⁾‖ + c·u‖Aq̂_p‖, so global semi-orthogonality implies local orthogonality without induction; single-pass CGS only gives β_k|Ω_{W,k}| ≤ ‖Ω_W‖‖h‖ + c·u‖Aq̂_p‖.
- Closest entries: HL ORTH (MGS + conditional second pass, LIT?…-110/-118), Kahan–Parlett twice-is-enough (as reported in LIT?…-110), Carson et al. 2025 BCGS2 (abstract). Separation: applied to the truncated window only, as the hypothesis-supplier of the 2D Simon theorem; falsified as distinct if it is identical to HL ORTH's effect (HL ORTH's second pass is conditional).
- Predictions / kill criteria (before running): (P1) with the two-pass window and no other reorthogonalization, μ(n) ≤ 10³u at every degree where L(n) ≤ √u on every benchmark — killed if violated; (P2) with the two-pass window plus oracle partial reorthogonalization at √u, e_F(n) ≤ u^{3/4} at every semi-orthogonal degree on every benchmark — killed if violated; (P3, J-part, expected to FAIL by the commutator obstruction) e_H(n) ≤ u^{3/4} at semi-orthogonal degrees — recorded, its failure supports the obstruction.
- Disposition: pending.

---

## R01 results and dispositions (appended 2026-11-01 after the runs; the pre-registered text above is unchanged)

| ID | Result (verdict file `logs/r01_verdicts.txt`) | Disposition | Canonical record |
|---|---|---|---|
| IDEA?…-201 (E1, E1D) | frozen kill test not fired: max U = 1.08 (E1), 3.85 (E1D); tracks within max(U,O) ≤ 7.1 off the checkerboards; overestimates cubic checkerboard 2.4e5 | survives (as an estimate of loss of orthogonality; not a bound) | PD-T?…-203 |
| IDEA?…-202 (E2, E2D) | not fired: max U = 1.22 / 1.15; verdicts as E1 (commutator sources measured exactly change little) | survives; not separated from -201 in tracking quality (separation criterion "E2 ≈ E1": met → equivalent in effect within scope) | PD-T?…-203 |
| IDEA?…-205 (E3) | not fired (U ≤ 1.44) but improvement criterion fails (cubic O 1.8e5 vs 2.4e5, needed ≥ 100× drop) | REJECTED: failed (aim: repair the coefficient-channel overestimate; scope R01 benchmarks) | PD-T?…-203 (b) |
| IDEA?…-203 F-part | killed for one-pass windows on rot0.3, triangle, annulus (local level μ ≥ 1.2e-11); not fired for fullcgs2 or two-pass windows; Theorem A PROVED explains the pattern | survives in the corrected form "semi-orthogonality + local orthogonality ⇒ O(u) F-section" (PD-T?…-201); the unconditional one-pass form is REJECTED: failed | PD-T?…-201, -204 |
| IDEA?…-203 J-part (τ, Ĥ_J) | killed on 8–9 benchmarks for every run type including fullcgs2 (Ĥ_J) and partial/two-pass (τ) | REJECTED: failed (BJ selection, scope of PD-N?…-201) | PD-N?…-201, PD-T?…-202 |
| IDEA?…-204 (H_drift) | pre-registered rule inconclusive (reference too ill-conditioned); post-hoc reference-free bound and unrotated reference kill it on 5 non-product sets | REJECTED: failed (kill rests on criteria added after the smoke test, disclosed) | PD-N?…-201 |
| IDEA?…-206 (two-pass window) | P1, P2 survive on all 12 benchmarks; P3 fails as expected | survives | PD-T?…-201 (Prop. L, Cor. A′), -204 |

---

## R02 pre-registration (written 2026-11-01T00:24:54+01:00, before any R02 run)

Origin of the selection candidates: reconstruction 01 (`reviews/L1-reconstruction-01.md`, PD-T?…-109 section: the selection rule changes loss by 10⁴–10⁸; rules 'mirror', 'alt' (X for 2j < t, else Y), 'adapt' (per column the candidate with larger β/‖Aq̂_p‖)); BPS 2010 Remark 9 / §5 (LIT?…-302) for the point-dependent variable choice. Own implementation (not the reviewer's code).

### IDEA?bivariate-lanczos-claude-207 — a selection rule whose spans stay J- and Y-closed under reorthogonalization

Aliases: "selection repairs the space channel"; adaptive/balanced selection + reorthogonalization; reviewer-origin candidate.

- Mechanism: PD-T?…-202 generalises to any one-relation selection: for each operator the unformed products are fixed by commutativity and their residuals follow a clamped recursion; the selection changes the propagator (reconstruction 01, a priori). Hypothesis: for 'adapt' (and possibly 'alt'), the defects δ_X, δ_Y and the drift stay at rounding level.
- Closest entries: PD-N?…-201 (BJ), PD-T?…-108/-109 (L1), IDEA?…-117–120 (L1 coefficient channel), Liu–Narayan two-relation (LIT, as reported). Separation: one relation per column (cost of the window recurrence) vs two-relation block completion.
- Test: selections dev, mirror, alt, adapt, each with fullcgs2 (spans only) and with a two-pass window and no reorthogonalization (loss); controls: two-relation block recurrence with 2 passes. Benchmarks: rot0.3, rotπ/4, disk, triangle, L-shape, annulus (non-product), square, tensor 41², cubic checkerboard (controls). Quantities: L(n), μ(n), δ_X, δ_Y, θ_LB := max(δ_X/(2‖X‖), δ_Y/(2‖Y‖)) (reference-free, PD-T?…-202 part 5 for both operators), drift against the unrotated-frame reference (rotated squares) and against a Koornwinder–Dubiner reference (triangle), with reference bound u·κ.
- **Kill criterion (before testing), per selection rule S:** "S keeps the spans near S_n under fullcgs2" is killed if θ_LB > √u at some n on some non-product benchmark, or a reference drift > √u where u·κ < 1e-11. It **survives** if θ_LB ≤ 10³u√N_n and reference drift ≤ 10³·max(u·κ, u√N_n) at every tested degree of every benchmark; otherwise inconclusive.
- Secondary (reported, no kill): plain loss of S with a two-pass window and no reorthogonalization.

### IDEA?bivariate-lanczos-claude-208 — PRO-2D: two-pass window + ω-triggered partial reorthogonalization (BJ ordering)

Aliases: 2D partial reorthogonalization; Simon-type PRO for the window recurrence; strategy of L2 R02.

- Mechanism: two-pass window (local orthogonality, Prop. L); after it, the E1 estimate (IDEA?…-201, sign-matched variant E1D for the trigger, which never underestimated by more than 3.9×) predicts the out-of-window row; if its max exceeds √u, reorthogonalize (two CGS passes) against {l : |ω̃_l| > u^{3/4}} plus the window, reset those estimates to rounding level, and treat the next column likewise (Simon's "next step" rule).
- Closest entries: Simon 1984 PRO (LIT?…-212), IDEA?…-003. Separation: 2D window, implicit Ĥ_J in the estimate, two-pass window as the local-orthogonality supplier.
- **Kill criteria (before testing):** killed if on any benchmark of R01 L(n) > 10√u at some degree (fails to keep semi-orthogonality), or e_F(n) > u^{3/4} at a degree with L(n) ≤ √u. Cost success criterion (reported): reorthogonalization dot products ≤ 30% of fullcgs2's on every benchmark.
- Known limitation stated before testing: with the BJ selection it cannot repair the J-section or the drift (PD-N?…-201); it is the strategy for loss of orthogonality only.

### Cost comparison protocol (before testing)

Dot-product counts (exact, from the run) and wall time for BJ one-pass, two-pass window, PRO-2D, adapt + two-pass window, fullcgs2 (≡ V+A-type CGS2 against all previous columns), at M ∈ {1681, 10⁴, 10⁵} on rotπ/4 (n = 24) and the triangle (n = 20); model counts: window passes ≈ Σ_k |W_k| ≈ (4/3)n³·(M flops-pairs), fullcgs2 ≈ N²·M. M = 10⁶ goes to Runs needed with an exact driver.

### IDEA?bivariate-lanczos-claude-209 — PRO-2D-J: PRO-2D with the J-rows measured (commutator channel exact in the trigger)

Written 2026-11-01T00:26:57+01:00, AFTER the PRO-2D (IDEA?…-208) smoke test on rotπ/4 and the triangle failed its kill rule (L(24) = 5.0e-7 and L(20) = 2.4e-6 > 10√u) and BEFORE any PRO-2D-J run (disclosed post-hoc candidate).

- Mechanism: as -208, but at J-steps the provisional out-of-window row is measured exactly (one inner-product pass, n per degree → O(M N^{3/2}) total, cf. -202) and the stored J-rows are exact; F-steps use the sign-matched estimate. Motivation: after reorthogonalization removes the propagated loss, the J-step commutator sources (R01 audit: up to 10⁸–10¹⁰ × the rounding scale on non-product sets) are no longer subdominant; -208's estimate ignores them.
- Kill criteria (before running): identical to -208 (L(n) > 10√u at some degree of some R01 benchmark, or e_F > u^{3/4} at a semi-orthogonal degree). Cost criterion reported: (reorthogonalization + measurement dot products) / fullcgs2.

---

## R02 results and dispositions (appended after the runs; pre-registered text unchanged)

| ID | Result (`logs/r02_verdicts.txt`, `logs/r02_cost.jsonl`) | Disposition | Canonical record |
|---|---|---|---|
| IDEA?…-207 dev / mirror / alt / adapt | killed for every rule (dev 5 sets, mirror 4, alt 4, adapt only rotπ/4: θ_LB 2.1e-7); adapt below √u on the other five non-product sets (7–10 decades below BJ); two-relation control below 5e-13 on all six non-product sets but fails on the cubic checkerboard | each rule REJECTED: failed (uniform safety); adapt retained as the best one-relation rule (deferred: resume with an rotπ/4-type fix or a hybrid with two relations) | PD-T?…-206, PD-N?…-203 |
| IDEA?…-208 PRO-2D (E1D trigger) | killed on rotπ/4, triangle, L-shape, annulus, cubic checkerboard | REJECTED: failed | PD-N?…-202 |
| IDEA?…-209 PRO-2D-J | survives on 11 of 12; killed on the cubic checkerboard at n = 29 (L = 2.0e-7); cost 0.16–0.71 of CGS2-against-all; secondary ≤ 30% criterion fails on 4 hard sets | REJECTED: failed on the cubic checkerboard (scope: that set, last degree); otherwise the measured strategy for loss of orthogonality; does not repair the drift | PD-T?…-207 |

---

## R03 pre-registration (written 2026-11-01T00:44:13+01:00, before any R03 run)

### IDEA?bivariate-lanczos-claude-210 — correctly rounded (or extended-precision) window dot products against the coefficient channel

Aliases: exact window dots; compensated dots; L1 hand-off "compensated/extra-precision window dot products"; ρ-removal.

- Origin: L1 SUMMARY §5 and PD-T?…-115 (closed-loop dot-product rounding ρ drives the clustered-checkerboard loss through off-pattern gains).
- Mechanism: in the BJ block-window CGS step compute each window coefficient as the correctly rounded value of q̂_lᵀa (Dekker splitting of the products + math.fsum), everything else in double ('exact'); variant 'ld': the whole step (product, dots, update, normalisation) in x87 long double, vectors stored in double.
- Sets: Harris–Simanek checkerboards m = 30 with grading s|s| (quadratic), s|s|² (cubic), s|s|³ (quartic), and cubic with m = 36 (the PD-T?…-115 sets, our construction), Chebyshev–Lobatto (control); rotπ/4, triangle, tensor 41² (vector/space-channel controls).
- **Kill criteria (before running).** P1 (main): on each of the four clustered checkerboards, 'exact' reduces L(n) at n = 20 and at n = 24 by ≥ 100× relative to the double run; the candidate is killed if on some clustered set the reduction is < 10× at both n = 20 and n = 24. P2 (channel separation): on rotπ/4 and the triangle the 'exact' reduction of L at n = 20 (triangle 16) and 24 (triangle 20) is < 10×; the separation claim is killed if the reduction is ≥ 10× at both degrees on either set. P3: θ_LB on rotπ/4 and the triangle changes by < 10× under 'exact' (killed otherwise).
- Reported, no kill: 'ld' on the same sets; PRO-2D-J with 'exact' dots on the cubic checkerboard (its R02 failure).
