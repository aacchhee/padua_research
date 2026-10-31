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
