# L1 (+L4) R01–R03 — independent adversarial reconstruction 01

## Header

- **Reconstructor:** Claude Opus 5.5 (`claude-opus-5-5`), effort **xhigh** — the WORKFLOW table's level for an adversarial audit of a novel mechanism. I am a separate agent from the L1 developer and made no Git state changes. I wrote only this file, the scripts in `tracks/bivariate-lanczos/code/review_L1/` and the logs in `reviews/logs_L1/` (≈ 140 KB in total).
- **Date:** 2026-10-31. **Branch:** `claude/bivariate-lanczos-20261031`. **Head when I started (rules read here):** `1063469a0ccff27823459e6f9c613eb26def8e10`. **Head during the reruns:** `f9bb09990f7c039388320cd9d0cb92ddd2863b03`. **Head when I finished writing:** `246d494e511c2733d4004d2430f737cba0f75d17`. The intervening orchestrator commits add L1 R04–R05, the BPS 2010 record, other directions, and a WIP checkpoint that captured an intermediate version of this report. This file is the final version.
- **Audited content:** every theory file below and `R01.md`–`R03.md` are byte-identical to the developer commit `b84af76` (checked read-only with `git show b84af76:<path> | sha256sum`). The current `candidates.md` (sha256 `27ba43dd…`) differs from `b84af76` (`bb5f6d8b…`) only by appended R04 sections. Records IDEA?…-101…-111, which I audited, are unchanged. R04–R05 are outside this audit.
- **Rules read:** `AGENTS.md`, `agents/WORKFLOW.md`, `agents/claude/CLAUDE_ROLES.md` §Independent audit, `topics/…/plan.md` (notation, frozen L1-Q1/L4-Q1, History).
- **Read coverage:** `state/IDEAS.md` read in full (144 lines; seed table 001–048, OBST-01…15, disposition table). Also read in full: `directions/L1/BRIEF.md`, `STATUS.md`, `R01.md`, `R02.md`, `R03.md`, `candidates.md` (records 101–111), `directions/COMMON_RULES.md`, the 12 theory files below, the developer code `code/L1/l1_recurrence.py` and `l1_kill_test.py` (read so I could reproduce the setup, never imported), and all developer logs in `directions/L1/logs/` except the `.raw` bodies. The `.raw` JSON records were parsed by `rv_rule_sensitivity.py`. The developer's analysis scripts were not reused.
- **Literature I read:**
  - Barrio–Peña–Sauer, J. Approx. Theory 162 (2010) 407–420, pp. 410–419 (§3–§5, eqs. (2)–(20), Thm 8, Remark 9). Source: AC's PDF via pdftotext into the scratchpad only, as directed by the coordinator. A web search did not find an open copy.
  - HL SIMAX 2002, Algorithm 1 listing pp. 1079–1080 (AC's PDF, pdftotext, scratchpad).
  - Liu–Narayan, arXiv 2202.04843, through a WebFetch *summary*, which is not verbatim, so its locators need re-checking.
  - The coordinator relayed AC's authorization (2026-10-31 23:00) to read related literature on the net. No fulltext entered the repository.
- **Memory:** none used.

| Theory file (`tracks/bivariate-lanczos/theory/`) | ID | SHA-256 |
|---|---|---|
| window-coefficient-pattern-exact.md | PD-T?…-101 | `3da66a24636eef451b101febcfe5900c8764f3c092edd799279ac1f23fcaa222` |
| fp-local-relations-window-recurrence.md | PD-T?…-102 | `b3c1edfc6357095e62b799c1a9665a35f43078c072e31e887fcabbd70dc6520c` |
| full-operator-paige-identity-growing-blocks.md | PD-T?…-103 | `965c788fedfe263803143228770be6eb977c1287fda31495d246e8b8757db95d` |
| node-row-representation-and-commutator-residual.md | PD-T?…-104 | `505c99571896cfc9b823a58c09f1ad7ef8590a4713fed73cd22497a795aad4c1` |
| product-measure-propagator-factorization.md | PD-T?…-105 | `02aa86228edd915e2f51ee41eb656f271029bf586cb8d83b22f856b0e047b14f` |
| exact-omega-recurrence-window.md | PD-T?…-106 | `9effae71e4e7e4bebae24e40325772bf18fddbe83e4b189b5752854a632c1286` |
| loss-regimes-node-propagator-measured.md | PD-T?…-107 | `0e3953c4b54c265f2893f5d167343e7fa0df32c06d9cdac6bede43bfce358bbd` |
| window-recurrence-row-selection-of-jacobi-pencil.md | PD-T?…-108 | `9b98459b1f680300d27c18491aee50e33a0ae470f4ec9c6f2a8f70b4b1d9187e` |
| non-product-amplification-is-a-priori-measured.md | PD-T?…-109 | `ff7d69259efd7a5380fdcedfb139e15213df2695e8c37c26e9569b92fc583b93` |
| l4-band-krylov-obstruction.md | PD-T?…-401 | `4880cd58036595e33fdf3e0f58e5a741eae970456816e62b725221053d449717` |
| ritz-residual-governance-fails-off-product-supports.md | PD-N?…-101 | `c925f46d90beed38d2e8582bbd9c03f73146d65afc51b2c520978c1604d5f58e` |
| hl-simax-windowed-complex-recurrence-instability.md | PD-N?…-102 | `aa5d2526f2ab6c19b1f85d8702d1c70a55698aa862aae1dd02f09a859eb2fb0a` |

Direction records: `R01.md` `88ab1ebe…602a`, `R02.md` `547d7656…75ba`, `R03.md` `5aa0b066…b0eb` (full hashes in the Reruns section).

## Verdict summary

| Claim | Developer status | Verdict | Scope of the verdict |
|---|---|---|---|
| PD-T?…-101 coefficient pattern | PROVED | **CONFIRMED** | Exact rational checks: generic nodes, M = N square case, repeated x-coordinates (breakdown exactly when U fails) |
| PD-T?…-102 [FP] local relations | PROVED, first order | **CONFIRMED** (honestly scoped; minor slips) | Bound respected in measurement by a factor ≥ 16 |
| PD-T?…-103 growing-block Paige identity | PROVED | **CONFIRMED** | Exact rational real and complex-symmetric instances; bandwidth hypothesis shown necessary |
| PD-T?…-104 node rows / commutator residual | PROVED | **CONFIRMED** | Exact rational simulated "computed" run with injected errors |
| PD-T?…-105 product factorisation | PROVED (idealised), FP CONDITIONAL | **CONFIRMED WITH CORRECTIONS** (minor) | Idealisation labelled, FP transfer genuinely CONDITIONAL; scope sentence overreaches |
| PD-T?…-106 exact ω-recurrence | PROVED | **CONFIRMED** (one inequality in the reading is wrong for the exact window) | Exact rational check, 155 (l,k) pairs |
| PD-T?…-108 row selection of the Jacobi pencil | PROVED | **CONFIRMED** as mathematics; **not new** in its framing | Must cite BPS 2010 and Xu's left-inverse recurrence |
| PD-T?…-401 L4 obstruction | PROVED | **CONFIRMED** (minor corrections) | U(2m+1) and the commutant restriction are both needed; non-band schemes are not covered |
| PD-N?…-101 Ritz governance fails | MEASURED | (a) **CONFIRMED**; (b) **NOT CONFIRMED as evidence against single sections** | (b) is a chain-completion artifact at n = 40 |
| PD-N?…-102 windowed (N, N*) instability | MEASURED | **CONFIRMED** | Independent implementation of the published listing |
| PD-T?…-107 regimes / predictor | MEASURED | **CONFIRMED WITH CORRECTIONS** | (b) confirmed (u-scaling, M-independence up to n ≈ 18); the support-based regime split fails as a classifier |
| PD-T?…-109 a priori / two-relation | MEASURED | (a), (b) **CONFIRMED WITH CORRECTIONS**; the "Consequence" sentence **REFUTED as stated** | The instability depends on *which* one-relation selection is used, and on single-pass CGS/truncation |
| Kill test K1 as reported ("fires") | — | **NOT CONFIRMED** | Flips with the factor-2 u convention; the single-section falsifier is the completion degree |
| Kill test K2 ("fires") | — | **CONFIRMED** | Non-product sets, every object fails |

**Blocking findings:**
- **B1:** PD-T?…-109 "Consequence", R03 §3 B / F8, the R03 STATUS line and the IDEA?…-111 disposition say the growth "is caused by the triangular one-relation-per-column selection … not by the truncation". This is refuted as stated.
- **B2:** "K1 fires", "single sections are falsified by tensor grids" (R01 §3, STATUS R01, the plan round ledger, PD-N?…-101 (b) consequence line) and the IDEA?…-101 rejection reason are unsupported.

The developer's final answer to L1-Q1 ("neither single nor joint Ritz pairs govern loss in general") survives, but only through K2.

## Per-claim reconstruction

### PD-T?…-101 — exact coefficient pattern (PROVED → CONFIRMED)

**Reconstructed statement.**
- Assumptions: [EXACT], distinct nodes, w > 0, U(n+1), graded order with j ascending inside each degree.
- The graded basis q_{t,j} is the Gram–Schmidt basis of the monomials x^{t−j}y^j in that order. It does not depend on which product generates each column; my long-double check gives the same basis for four different parent rules, to 1e-18.
- Supports:
  - Y-column (t,j): rows {(t−1,i≥j−1)} ∪ block t ∪ {(t+1,r≤j+1)}.
  - X-column (t,j): rows {(t−1,i≥j)} ∪ block t ∪ {(t+1,r≤j)}.
- Window sizes 2t−1, 2t, 2t+1. Only the J-columns (t,0) are formed. The implicit J-columns follow from commutativity.
- Z is unitarily similar to the square part of N_k.

**Proof check.** I re-derived each step: the induction in part 1, the symmetric-operator vanishing argument in parts 2–3, the counts in part 4, part 5 (JF = FJ), and part 6 (two orthonormal bases of the same complex subspace). All steps are correct.

**Counterexample search.**
- `exact_checks.log`, exact rationals, unnormalised weighted Gram–Schmidt:
  - 385 entries outside the derived support (M = 30 generic, random integer weights, n = 4): **0 nonzero**.
  - M = N_4 = 15 (square case), n = 3: 164 outside, **0 nonzero**.
  - Nodes on 4 distinct x-values: the recurrence breaks down at (4,0), exactly where U(4) fails. At n = 2, where U(3) holds, 55 outside, 0 nonzero.
- Long double: the full-reorthogonalisation run has coefficients outside my independently derived exact window of size ≤ 7.7e-20. The exact-window runs equal the full run to 9e-19 for the parent rules dev, mirror, alt and adapt.

**Findings.**
- Minor: part 5 is an immediate consequence of commutativity (correctly called routine).

### PD-T?…-102 — [FP] local relations (PROVED, first order → CONFIRMED)

**Reconstructed statement.**
- Under the standard model and to first order in u: β_k q̂_k = A_k q̂_{p(k)} − Q̂_W h_k − f_k, with the stated BJ and HL constants.
- The matrix relations for F, the J relation for the columns (t,0), and the defect recursion are *exact* identities once f_k is defined as the residual.
- Only part 1's constants are first-order. The file says so explicitly in the Statement ("to first order in u"), in Assumptions ("O(u²) terms dropped") and in Status. That labelling is honest; no rigorous γ-form bound is claimed.

**Proof check.** BJ: δ_a, δ_r ≤ γ_{w+1}(|a| + |Q̂_W||h|), βδ_q, and the collection into (w+2)(1 + κ√w μ) + 1 are correct. The defect recursion is re-derived correctly.

**Findings (minor).**
- `fp-local-relations…md` Proof 1(BJ): "‖h‖ ≤ (1+γ_M)κ‖a‖" is not a valid inequality; the correct bound is κ‖a‖ + γ_M√wμ‖a‖. It enters only at O(u²), so it is harmless at first order.
- 1(HL): the accounting omits the rounding of the coefficient sum h = c + c′. That term is ≲ uκ²‖a‖, so it is absorbed by the κ² slack. "‖r‖ nonincreasing up to O(u) factors bounded by κ²" is muddled: MGS steps are nonincreasing whenever ‖q̂_l‖ ≤ √2.
- Part 4: "propagated by the same computed recurrence" should say "by the same coefficients, interleaved with the projectors (I − Π_{t+1})".

**Measurement.** `extra.log` (iii): local errors f_k evaluated in long double from double BJ runs. max ‖f_k‖/(u‖A‖μ) = 0.96 (square), 1.00 (square rotated π/4), 31 (triangle). In every case ‖f_k‖/bound ≤ 0.061, so the bound holds with margin.

### PD-T?…-103 — growing-block Paige identity (PROVED → CONFIRMED)

**Reconstructed statement.** For any diagonal (complex) A and any matrices with AQ̂ = Q̂T + Q̂_+B + E, where B vanishes outside its last r columns and S = (T+Tᵀ)/2 has bandwidth b: sᵀcBs = sᵀΩs − sᵀ(R−Rᵀ)ρ for all s ∈ Cᵐ and θ, plus the norm bound and the corollary.

**Proof check.** Steps 1–7 are re-derived. The antisymmetry of every term of (1), the locality argument (indices l − k ≤ l − j ≤ b) and the bilinear step sᵀXs = sᵀ(R−Rᵀ)ρ are correct.

**Exact checks (`exact_checks.log`).**
- 5 random rational real instances (M = 14, m = 9, q = 4, r = 3, b = 2): |lhs − rhs| = 0.
- One complex-symmetric instance in SymPy: 0.
- Control with the bandwidth hypothesis deliberately violated: the residual is nonzero (10249579529/8587340257). So the check discriminates, and the bandwidth hypothesis is necessary.

**Findings (minor).**
- `Specialisations, F`: "All terms of Ω are local" is descriptive. With BJ's block window, K also contains the asymmetry produced by off-pattern computed coefficients (T_{lp} ≠ 0 with T_{pl} = 0).
- The identity controls one bilinear combination per Ritz pair, as the Scope says. R02's measured 0–47% confirms this is not a loss bound.

### PD-T?…-104 — node rows and commutator residual (PROVED → CONFIRMED)

**Exact check.** I simulated a "computed" run in rationals: exact-window dev recurrence, coefficients rounded to a 1e-8 grid, injected random rational local errors f_k, M = 24, run to degree 5.
- Part 1 (node rows at all nodes): 0 mismatches.
- Part 3 (commutator-residual recursion, with Ĥ_J built from the computed coefficients by definition 2): 0 mismatches.

These identities hold as exact algebra on arbitrary computed data, as claimed. No findings.

### PD-T?…-105 — product factorisation (PROVED idealised; FP CONDITIONAL → CONFIRMED WITH CORRECTIONS)

**Exact and high-precision checks.**
- Part 1 on a 5×5 rational tensor grid with product weights: 0 within-degree couplings and 0 off-chain coefficients.
- Controls: the sheared grid has 10 nonzero within-degree couplings; the product grid with weights (2 + xy) has 20.
- Impulse formula ρ^{[s]} = b_s(r_{s−1}σ − σ_{s−1}r), checked in mpmath at 50 digits on a 6-point measure: maximum error 2.7e-51.

**Idealisation and conditional status.** The idealisation is labelled ([IDEALIZED: exact coefficients]). 2′ is genuinely CONDITIONAL: it names the hypothesis (computed = exact + O(δ)), there is no proof that δ stays small, and tensor 41² supplies only a measured δ ≤ 7e-15.

**Findings.**
- Minor: the normalisation of μ_x, μ_y as probability measures is implicit but needed (W_0 = −1 uses σ_1 = μ(1)/b_1; so does |r_l(η_b)| ≤ 1/√v_b).
- Minor: A′_t is defined with 1 ≤ r ≤ j, which excludes the coupling to (t,0), yet part 3's "equivalently" clause includes it.
- Minor: the factor (n+1)² can be (n+1).
- Minor: part 3 is a true but nearly vacuous reading.
- Minor 2′: first-order validity also needs ‖L⁻¹‖·δ ≪ 1, which is not stated.
- Major (scope): §Scope says the result "Explains why the recurrence shows no amplification … consistent with the flat loss". The propagator → loss link is OPEN (PD-T?…-104 open item), so the statement explains the idealised propagator, not the loss.
- My checks also show that non-diagonal within-degree coupling does **not** imply growth: weights exp(xy) and exp(4xy) on the square are stable (`sweep_alt.log` C).

### PD-T?…-106 — exact ω-recurrence (PROVED → CONFIRMED)

**Exact check.** On the simulated rational run, 155 pairs (l, k) were checked, using T_F/E_F for F-products and Ĥ_J/C_res for J-products: 0 mismatches.

**Finding.**
- Minor, `Statement` 2nd paragraph: "for l outside W_k … r of degree ≤ deg(l)+1 ≤ deg(k) − 2" is false for the **exact** window (HL). There, l = (t−2, i < j−2) lies outside W_k and has deg(l)+1 = t−1. The conclusion (a recursion on older Gram entries) still holds, because those ω_{rp} have r, p of degree t−1 < t. For the block window (BJ) the inequality is correct.

### PD-T?…-108 — row selection of the Jacobi pencil (PROVED → CONFIRMED; novelty: known framing)

**Reconstructed statement.** At z, row k of L*(z) is −ℛ^{A_k}_{p(k)}(z). p(z) satisfies all 2N_{n−1} pencil relations (a polynomial identity under U(n), via injectivity of evaluation). Any triangular selection is a left inverse. The two-relation block step spans S_n, and its truncation to blocks n−2, n−1 is exact. All three parts are correct.

**Attribution (major).** The developer cites no predecessor; candidates.md IDEA?…-111 lists xu-siam-1994 and liu-narayan-2023 "as reported".
- In block form, the window recurrence is Xu's recurrence formula with the particular left inverse D_n^T = L_n^{-1}·Sel of the stacked A_{n−1} = [A_{n−1,1}; A_{n−1,2}]. The left-inverse/pseudo-inverse form is textbook: BPS p. 412 cite Dunkl–Xu [8, Thm 3.2.5]. I verified BPS's text, not Dunkl–Xu itself.
- BPS 2010 give:
  - the explicit one-variable-per-polynomial recurrence, eq. (5), with free choice j ∈ s(α);
  - its assembled form (14)–(15) and the all-relations average (6)/Thm 8;
  - Remark 9: the choice of variable affects numerical behaviour;
  - two point-dependent selection strategies (§5, p. 416);
  - Clenshaw as a block triangular substitution, with forward bound (20) in the comparison-matrix inverse.

**Separation that remains.**
- BPS work with **monic** OPs: A_{n,j} is a 0/1 shift there, so their selected system has no within-degree coupling. The window recurrence uses the strongly orthogonal graded-lex basis (BPS's t_α, p. 410), whose selected block L_n is lower triangular with coupling.
- The setting is discrete-measure Lanczos vectors with window truncation, linked to orthogonality loss.
- BPS report no experiments (no tables or figures in the paper).

My selection-rule measurements (below) are a quantitative instance of exactly BPS's Remark 9.

### PD-T?…-401 — L4 obstruction (PROVED → CONFIRMED with minor corrections)

**Reconstructed statement.** For distinct nodes, w > 0, U(2m+1) and real A with AX = XA and AY = YA (that is, A diagonal): no V ∈ R^{M×m} has both S_m and S_{m+1} in the band Krylov chain B_{j,i}. Corollary 1 extends this to every n ≥ m+1 (padding argument, U(2n−1)). Corollary 2: affine A needs m ≥ n+1 for S_n.

**Proof check.** Lemma 1 (B = span V + A B_{j−1,i}), Lemma 2, Lemma 3 (chain), Lemma 4 (top form of g·xⁿ has degree d + n ≤ 2n+1), Lemma 5 (codim = n+1 via U(n+1) and injectivity) and the Theorem's dimension step (dim B_{j+1,i} ≤ N_m + m < N_{m+1} ⇒ A S_m ⊂ S_{m+1}) are all correct.

**Exact checks (`exact_checks.log`).**
- Lemma 5 by exact rank, M = 40 generic rational nodes, n = 1…4: codim = n+1 for X and for 0.6X+0.8Y+0.3, and 2n+1 for X²+Y. This agrees with the developer's numerical check.
- **The hypothesis U(2m+1) is needed, not artificial.** For nodes on two vertical lines (U(2) fails), S_n = B_{n,1}(Y, [q_0, Xq_0]) for every n = 1…5 (exact ranks equal). Nodes on k lines, tensor grids included, admit band descriptions with k fixed starts for all n.
- **The commutant restriction is needed:** the Remark's A = QTQᵀ is correct.

**Do non-commuting or non-band schemes escape?**
- Non-commuting A that is built without the output is not covered. The file's "L4-Q1 has computational content only inside the commutant" is an assertion, not a proved statement (minor).
- I checked one natural extension: A = (commutant) + rank r. By the same top-degree count, (X + L)S_n + S_n has dimension ≥ N_n + n + 1 − r, so a fixed rank r with fixed m cannot pass all degrees. This is my own short argument and has not been audited.
- Non-band Krylov-type processes (each new vector = A × any vector of the current space, no injection) are outside the Theorem. For **affine** A they are excluded by a strengthening I verified: under U(n+2), every continuation vector c with Ac ∈ S_{n+1} lies in S_n, so S_{n+1} ⊂ S_n + AS_n, whose dimension is N_n + n + 1 < N_{n+1} (exact dimension check in `exact_checks.log`). Hence, for affine A, *any* such process needs at least one injected vector per degree, regardless of m. For non-affine commutant A with arbitrary continuation the question is open.

**Findings (minor).**
- `Checks` says "1681 random nodes, n ≤ 10", but the log `r01_l4_codim_check.log` has n ≤ 8 and R01 says M = 400.
- Corollary 2 "lower bound attained by the recurrence": the staggered-start description Σ_a K_{n−a+1}(F, v_a) is not a member of the B_{j,i} class the Statement defines. The bound still applies, because Lemma 1 holds for any S = span V + A B′ with B′ ⊂ S. This should be said.
- Transfer item 3: "the injected vectors … are not in any band Krylov space of F with a start block fixed in advance" overstates. They are in such spaces up to a degree; the Theorem says no fixed-size block works for all degrees.
- The statement covers real A only. Complex commutant elements such as N = X + iY are not literally covered, although the proof transfers verbatim over C.

### PD-N?…-101 — Ritz governance fails (MEASURED)

**(a) Non-product supports: CONFIRMED** (my seeds and node generators; `sweep_ritz.log`).
- On rotation pairs of the same 1681 points, u/ρ_Z is identical to all printed digits (3.7e-14 at n = 24 for the square, the 0.3 rotation and the π/4 rotation). The BJ loss is 2.3e-14, 4.7e-6 and 1.0e-2 respectively.
- On the disk and the triangle, u/ρ_{X,Y,Z} ≤ 6e-14 at n ≤ 24 while the loss reaches 7.5e-9 and 1.
- Single and joint residuals agree within a factor ≈ 6 everywhere (≤ 3 on the squares), while the loss misses them by 10³–10¹². They never separate.

**(b) Tensor over-prediction: the measurement reproduces, but it does not support the use made of it.**
- My tensor_cheb 41² data, n = 33…40 at every degree: u/ρ_X = 2.0e-14 … **2.5e-14 at n = 39**, consistent with the loss of 2.0e-14. At **n = 40**, u/ρ_X jumps to 8.7e-2.
- n = 40 is the completion degree of both one-coordinate chains on 41 abscissae: the next J-product x⁴¹ breaks down, and S_40 contains every function of x. The one-coordinate subspaces become exactly invariant, so Bs = 0 in PD-T?…-103, and Paige-type theory predicts nothing there.
- This is the same degeneracy the developer excluded post hoc for Padua (N = M: "every Ritz pair is exact and no next vector exists"), but it was not excluded here.
- Excluding it, the tensor grid is uninformative for every object, and **no run falsifies single sections relative to Z** (`rule_sensitivity.log`).

**Finding (blocking, B2).** The PD-N?…-101 "Consequences" line ("IDEA?…-101 fails on (a) and (b)") and IDEA?…-101's rejection reason ("tensor over-prediction; non-product supports") must drop (b). IDEA?…-101 and -102 fail together on (a) and only there.

### PD-N?…-102 — windowed (N, N*) recurrence (MEASURED → CONFIRMED)

**Implementation.** I implemented HL SIMAX Algorithm 1 independently. I re-derived the window indices from the listing on pp. 1079–1080: k0 : k2−1 for the N*-product; l−k+1 : k+l for the N-product, i.e. cycle k−2 from index s−1, cycle k−1, cycle k up to s−1. These match the developer's description.

**Results** (`extra.log` (i), loss at n = 8/16/24):

| Set | ORTH | CGS | Full orthogonalisation |
|---|---|---|---|
| square | 6.1e-15 / 4.3e-11 / 6.5e-6 | 1.7e-14 / 3.0e-10 / 5.9e-5 | 1.6e-15 |
| tensor 41² | 2.2e-14 / 5.2e-10 / 3.6e-5 | 1.3e-13 / 7.1e-9 / 2.9e-3 | 2.0e-15 |

The square rotated by 0.3 and the disk behave similarly. The rate is ≈ 3–5 per degree from n ≈ 8 (ORTH).

**Structural explanation.** I re-derived that the window start s−1 in block k−2 rests on ⟨q_p, N*q_l⟩ = 0. That is an *implicit* N*-relation, because N* products are formed only for first vectors. This supports the developer's CONDITIONAL reasoning.

**Finding.** Minor: "from degree ≈ 6" fits CGS, but onset is n ≈ 8–10 for ORTH in my runs.

### PD-T?…-107 — regimes and predictor (MEASURED → CONFIRMED WITH CORRECTIONS)

**(b) Non-product growth: CONFIRMED** on every non-product set I tried (square rotated 0.3 and π/4, disk, two triangles, annulus, tensor rotated 0.3). It starts at n ≈ 8–12 and is present for both BJ and HL. HL is 3–10× lower on the rotated squares, disk and annulus, and 10²–10⁴× lower on the triangles and the rotated tensor grid, but it still grows there. The following hold:
- **Scales with u:** BJ float32/float64 loss ratios before saturation are 1.6e8–8e8 against u₃₂/u₆₄ = 5.4e8 (`sweep_loss.log`).
- **M-independent for n ≤ 18:** square rotated π/4, n = 16: 1.2e-9 / 1.3e-9 / 1.0e-9 at M = 1681 / 6724 / 26896; disk 2.8e-12 / 2.1e-12 / 1.5e-12. At n = 22, M = 1681 is 10–20× above the larger M, a finite-M acceleration (`sweep_M.log`). This partly discharges the developer's Runs-needed item, up to M = 26896 rather than 10⁵–10⁶.
- **Correction (minor, matters for R04's targets):** log-loss is **convex** in n on n ≤ 24. Quadratic fits cut the rms 2–7× against linear fits. The per-degree factor rises from ≈ 3–4 at n ≈ 10 to ≈ 8–12 at n ≈ 22 (square rotated π/4: increments 0.59 → 0.91 decades/degree; tensor rotated 0.3: 0.57 → 1.1). "Exponential" understates this; an a priori lower-bound target should not presuppose a fixed rate.

**(a) Product-aligned regime: CONFIRMED for the listed set types** (random square stable to n ≈ 22, then Ritz-type with loss/(u/ρ) = 0.2–0.8 for n = 24–32; tensor grid flat). **Refuted as a support-based classifier (major):**
- **Product support, non-product weights:** weights exp(8xy) on the square give BJ loss 1.8e-12 already at n = 8 and 4.0e-7 at n = 24. That is ≈ 10³ above u/ρ_Z. The two-relation recurrence is at ≈ u/ρ (`extra.log` (ii)). exp(xy) and exp(4xy) are stable.
- **Sampled product density:** the Gaussian cloud (unrotated) has BJ loss 3.6e-5 at n = 24, against u/ρ_Z = 5.8e-7. BJ exceeds u/ρ by 6–370× at n = 16–28. Here the two-relation recurrence is **Ritz-governed** (loss/(u/ρ_Z) = 0.5–1.2). The rotated cloud behaves the same.
- So the regime is set by the (empirical) measure's coefficients, with a quantitative threshold, not by the support. R02/R03's phrasing "product-aligned supports vs non-product supports" should be restated accordingly.

**(c) Predictor.** I did not rerun the developer's iid-forcing predictor. My independent a priori analogue is u·median_i and u·max_i of ‖L*(z_i)⁻¹‖₂ with exact coefficients (`prop.log`). On six of the seven sets it **brackets** the loss: the median is 1–2000× below, the maximum 3–100× above. The six are the square, the rotations by 0.3 and π/4, the disk, the tensor grid and the rotated Gaussian. On the triangle the loss exceeds u·max at n = 12 and 16 (by 1.3× and 54×), and u·max ≈ the loss at n = 20. This parallels the developer's own predictor failure on the triangle.

**(d)** Not rerun.

**(e) Couplings: consistent.** My exact within-degree coupling max_{r<j}|h_{(t,r)}|/β at t = 4…20 is:
- square 0.05–0.14;
- rotated 0.3: 0.78–2.1; rotated π/4: 0.64–0.93;
- disk 0.62–1.0; triangle 1.2–1.8;
- tensor ≤ 5e-16.

**(f)** Not rerun.

### PD-T?…-109 — a priori and two-relation (MEASURED → (a), (b) CONFIRMED WITH CORRECTIONS; Consequence REFUTED as stated)

**(a) A priori growth: CONFIRMED in substance, by a different construction.** I compute ‖L*(z_i)⁻¹‖ directly with exact coefficients, validated at 3 nodes per set in mpmath at 30 digits (relative difference ≤ 1e-10, except 1e-4 at one triangle node with norm 6e11). max_i ‖L*⁻¹‖ at n = 20:

| Set | max_i ‖L*⁻¹‖ |
|---|---|
| square | 2.0e3 |
| tensor | 6.5e2 |
| rotated 0.3 | 7.6e9 |
| rotated π/4 | 1.7e12 |
| disk | 2.7e7 |
| triangle | 1.0e16 |

I did not reproduce "P* = P to the printed digit", because I did not form the computed-coefficient propagator.

**(b) Two-relation control: CONFIRMED** on the square rotated 0.3 and π/4, the disk, the annulus and the tensor grid rotated 0.3 (≤ 2.6e-13 at n = 24, one CGS pass). **Corrections (major):**
- Triangles: reduced, not removed, with one pass (1.0e-10 and 8.5e-12 at n = 24, still growing ≈ 0.2 decades/degree). Removed with two passes (4.3e-12; 6.9e-15 on the rotated squares and the disk).
- Gaussian cloud: not removed (3.3e-7 at n = 24). The loss there is Ritz-type.
- Tensor grid: the two-relation recurrence is **worse** than BJ (1.1e-12 vs 1.9e-14 at n = 24; float32 1.3e-4 vs 7.0e-6).

**Consequence sentence — REFUTED as stated (blocking, B1).** The text reads: "the growth … is caused by the triangular one-relation-per-column selection of the Jacobi pencil (PD-T?…-108), not by the truncation of the window". Two independent facts contradict it.

1. **The selection rule decides, not one-relation-ness.** All runs use the same graded basis, block window, CGS and double precision (`sweep_alt.log` A). Loss at n = 24:

   | Set | dev (developer's) | mirror (HL BIT) | alt (balanced) | adapt (max β/‖Aq‖ per column) |
   |---|---|---|---|---|
   | square rotated 0.3 | 4.7e-6 | 1.7e-8 | 3.4e-9 | **1.3e-12** |
   | square rotated π/4 | 1.0e-2 | 4.5e-1 | **1.8e-8** | 1.6e-8 |
   | disk | 7.5e-9 | 8.2e-12 | 9.1e-12 | 1.1e-11 |
   | triangle | 1 | 1 | 4.9e-5 | **9.2e-8** |

   The exact-coefficient propagator itself is selection-dependent a priori (`prop_selection.log`; exact coefficients for each selection; the disk rows were not computed because I stopped the run). u·max_i‖L*(z_i)⁻¹‖ at n = 20:

   | Set | dev | mirror | alt | adapt |
   |---|---|---|---|---|
   | square rotated π/4 | 1.9e-4 | 1.9e-1 | 9.1e-9 | 6.8e-8 |
   | square rotated 0.3 | 8.5e-7 | 2.7e-8 | 2.9e-9 | 4.5e-12 |
   | triangle | 1.2 | 1.5e-4 | 2.5e-5 | 3.4e-8 |

   The median moves in the same way, e.g. triangle 1.3e-7 (dev) → 1.3e-14 (adapt).

   So the a priori amplification is a property of (measure, coordinates, **selection rule**). Some one-relation selections are 10⁴–10⁸ more stable than the developer's at n = 24, although none tested is as stable as the two-relation recurrence with two passes.

2. **Truncation is necessary on some sets and not on others.** Same dev selection, no truncation, single CGS pass against *all* previous columns (`sweep_loss.log`, `fullcgs_f64`):
   - square rotated π/4: 3.8e-14 (stable); disk: 6.9e-15 (stable). Removing the truncation removes the growth on these sets.
   - triangle: 1 at n = 20, identical to BJ; square rotated 0.3: 2.6e-6; tensor rotated 0.3: 1.6e-2; annulus: 2.8e-7; Gaussian: 2.2e-5. Here single-pass CGS loses orthogonality without any truncation.

   The developer's test (two relations, same truncation, stable) shows truncation is not *sufficient*. It does not show truncation is not a cause.

**Required restatement.** The growth requires the selection, together with either truncation or single-pass Gram–Schmidt on the selected products. The magnitude is selection-dependent and is cut by orders of magnitude by a pivot-aware or balanced selection (BPS Remark 9 / §5 territory).

**(c)** I did not rerun the 12-angle orientation scan. My two triangles (right and equilateral) differ by a factor ≈ 10⁵ at n = 16, which is consistent.

## Protocol

### P1. Frozen kill test as applied (K1) — blocking (B2)

The operationalisation in candidates.md was written before the runs. That is good. But:

- **(i) Convention sensitivity.** The rule uses u := 2^-52 ("the input's convention"), while plan.md and PD-T?…-102 define u as the unit roundoff, 2^-53. I re-applied the rule independently to the developer's raw JSON (`rule_sensitivity.log`):
  - u = 2^-52: K1 fires. This reproduces the developer.
  - u = 2^-53: K1 **does not fire**. Z then predicts on random6724 bj and on random1681_s0/s7 **hl**. On random1681_s0 hl both single sections *fail* (Z ratios 0.35–1.1, X 0.20–0.66, Y 0.19–0.61). By the pre-registered rule, that is the falsifier of single-section governance. On random1681_s7 hl, X fails and Y predicts.
  - Conversely, at u = 2^-53, Z *fails* on random1681_s0/s7 **bj** while single sections predict: the reverse "separation".

  A factor-2 convention therefore flips the outcome in both directions. The frozen factor-3 band cannot separate objects whose residuals agree within 2×, which is the case on every informative product-type run. The correct report is "K1 inconclusive (no separation)", not "K1 fires".
- **(ii) Declining the K1 consequence.** The developer declined the K1 consequence ("L1 reduces to per-operator Paige theory") citing M2, the tensor over-prediction. M2 rests solely on the completion degree n = 40 (PD-N?…-101 (b) above). With that degree excluded under the developer's own N = M rationale, no single-section falsifier remains.
- The valid reason to reject *both* consequences is K2/M3, which I confirm.
- Required corrections: STATUS R01, the plan round ledger, R01 §3, PD-N?…-101 (b) and the IDEA?…-101 rejection reason.

### P2. Post-hoc changes

- The R01 N = M exclusion: harmless for Padua, which is uninformative anyway, but applied **asymmetrically**. Its rationale also covers tensor n = 40, and that asymmetry produced the only single-section falsifier. Major.
- The "tracks" ≥ 2 degrees change relabels random6724 hl only. Minor.
- The IDEA?…-106/-107 criteria were written after the runs and carry no pre-registration weight (disclosed).
  - IDEA?…-106's conclusion "intrinsic amplification" is also not tested against the selection: the mixed-precision test only localises the error source between F- and J-products.
  - IDEA?…-107's triangle failure is honestly recorded.
- The R03 criteria were pre-registered. But IDEA?…-111's criterion can only show that truncation is not sufficient, so the recorded inference "the selection, not the truncation" exceeds what the test can establish (B1).
- IDEA?…-110/-111 lack a "Novelty gate verdict" line, which the template requires.

### P3. Literature reliance

- T-103 cites Paige and Sinha "as reported / not inspected", explicitly not as dependencies. Correct.
- T-401's transfer list is labelled LITERATURE-as-reported at abstract level. Correct.
- T-101 is cross-checked against the HL BIT fulltext. The SIMAX listing is read in fulltext; I confirmed the window indices.
- Missed predecessors:
  - BPS 2010 and the Xu/Dunkl–Xu left-inverse recurrence for T-108, IDEA-110 and IDEA-111. Major.
  - Liu–Narayan 2023 for the two-relation block Stieltjes (listed only as "as reported").
  - Zaccaron 2014's geometry dependence for IDEA?…-106 (found by the prior-art agent; self-corrected in R04 PC-5; I did not verify Zaccaron).

### P4. Scope overreach

The tested scope is M = 1681 (≤ 6724 by the developer, ≤ 26896 by me), n ≤ 24–32 (48 for Padua), one seed per shape and uniform weights. Several statements generalise beyond it:
- "a priori property of (measure, ordering, coordinates)": the selection is missing from that list.
- "caused by the selection, not truncation": B1.
- "product-aligned supports": refuted as a classifier by exp(8xy) and the Gaussian cloud.
- "two relations remove it": scope is the listed sets only.
- "exponential": the growth is convex in n.

Separately, the R04 self-corrections PC-1/PC-2 (square rotated 0.05: borderline, onset n ≈ 18) agree with my runs (1.5e-13 at n = 24, onset ≈ n = 17).

### P5. Status labels and split rules

These are appropriate:
- PROVED files contain only exact algebra or labelled first-order results.
- MEASURED results have their own files.
- 105-2′ is a properly split CONDITIONAL part.
- The PD-N files carry MEASURED negative statements with ranges.
- One mixed sentence, the PD-T?…-109 "Consequence", is an inference presented as a conclusion; the developer labels it "inference … within its scope".

## Alternative explanations of the non-product growth (task item 4)

| Alternative | Test | Outcome |
|---|---|---|
| Ill-conditioning of the measure / Christoffel function on the support | Rotation pairs: S_n, the Christoffel function and ρ_Z are rotation-covariant; loss is not (10⁸–10¹² differences); full CGS2 is orthonormal on every set | **Excluded** as a cause of loss. The coordinate-dependent conditioning of the graded-lex basis is not excluded; it is effectively the selection-dependent propagator |
| Near-degenerate pivots | min β/‖A q_p‖ per degree (`sweep_alt.log` D): square 0.65–0.68, rotated 0.3 0.66→0.29, rotated π/4 0.48–0.63, disk 0.49–0.63, triangle 0.21–0.29, tensor 0.58 | **Excluded as "near-degenerate"** (all ≥ 0.2). Pivot size still matters: the triangle's small pivots match the instability of full single-pass CGS, and the pivot-maximising selection (adapt) nearly removes the growth on the 0.3 rotation |
| Ordering within degree / parent operator per column | dev / mirror / alt / adapt | **Not excluded by the developer; decisive.** 10⁴–10⁸ effect at n = 24; a priori in the exact propagator |
| Truncation depth / local reorthogonalisation | Window depth 2→10; window CGS2 | Modest: rotated π/4 1e-2 → 9.3e-6 (depth 10), 2.6e-3 (CGS2); triangle unaffected by depth, 7.7e-2 with CGS2 |
| Classical single-pass CGS (κ²) loss | Full window, one CGS pass | Present on the triangle, rotated 0.3, tensor rotated, annulus and Gaussian at BJ's level; absent on rotated π/4 and disk |
| Known Stieltjes/recurrence instability | BPS 2010 Remark 9 and §5 (choice of variable affects rounding error); Liu–Narayan (larger errors on some domains, attributed to the conditioning of T_n, from the summary only) | The selection dependence is anticipated qualitatively by BPS. No source in my reading quantifies growth with degree |

## Reruns (actual executions)

**Environment.** Python 3.13.18, NumPy 2.5.3 (OpenBLAS), SymPy 1.13.3, mpmath 1.3.0, x87 80-bit long double, 2 cores.

**Seeds.**
- `rv_core.node_set(..., seed=20261031)`, with +1 disk, +2 annulus, +3 right triangle, +4 equilateral triangle, +5 Gaussian, +6 anisotropic Gaussian.
- Rotations reuse the same points.
- Exact checks: `random.seed(31102026)`.

**Commands.** Run from `tracks/bivariate-lanczos/code/review_L1/`; `L` = `topics/bivariate-lanczos-20261031/reviews/logs_L1/`:

| Command | Output |
|---|---|
| `python3 -I -u rv_exact_checks.py > L/exact_checks.log` | T-101, -103, -104, -105, -106, -401 exact checks, all as reported above |
| `python3 -I -u rv_sweep.py loss > L/sweep_loss.log 2> L/sweep_loss.json` | Loss at every degree n ≤ 24; 12 sets × {BJ, HL, two-relation} × {f64, f32}, plus full single-pass CGS; growth fits |
| `python3 -I -u rv_sweep.py alt > L/sweep_alt.log` | Selection rules, window depth, window CGS2, two-relation with 2 passes, weights exp(cxy), Gaussian clouds, pivots and couplings |
| `python3 -I -u rv_sweep.py M > L/sweep_M.log` | M = 1681 / 6724 / 26896 |
| `python3 -I -u rv_sweep.py ritz > L/sweep_ritz.log` | u/ρ_{X,Y,Z} on the computed and exact spans; tensor n = 33…40 at every degree |
| `OPENBLAS_NUM_THREADS=1 python3 -I -u rv_prop.py > L/prop.log` | Exact-coefficient ‖L*(z_i)⁻¹‖ at all nodes; mpmath validation |
| `python3 -I -u rv_extra.py > L/extra.log` | (N, N*) recurrence; Ritz on Gaussian and exp(8xy); T-102 bound check |
| `python3 -I rv_rule_sensitivity.py <developer logs>/r01_{input3,rotation,swap,padua,irregular}.raw > L/rule_sensitivity.log` | Protocol re-application of the pre-registered rule to the developer's raw output (not a rerun) |
| `OPENBLAS_NUM_THREADS=2 python3 -I -u rv_prop_selection.py > L/prop_selection.log` | Selection dependence of the exact propagator; stopped after the triangle rows, so the disk rows were not computed |

**Script SHA-256.**
- rv_core `b2360c4c…2b00`
- rv_exact_checks `be0cbd8a…cfa63f`
- rv_sweep `9a641998…8e34`
- rv_prop `1b2073d1…48d7`
- rv_extra `62484956…7da7ab`
- rv_rule_sensitivity `c92a16aa…d3cf`
- rv_prop_selection `45595ee5…0f33`

**Direction record SHA-256.**
- R01 `88ab1ebe389d96c0ed2a533fbbaea4688711504f9cfed351163d20d56939602a`
- R02 `547d7656d3aa35e1e29bd0ae0a4b6420254823acda412302419e7bf3594175ba`
- R03 `5aa0b06672a8f6c8705b35899bfa45aff0cb0556b9b6014d5b56fad6cc6cb0eb`

**Representative output** (BJ, f64, n = 16 / 20 / 24, my seed):

| Set | BJ loss | u/ρ_Z | Full single-pass CGS | Two-relation |
|---|---|---|---|---|
| square | 6.9e-15 / 6.9e-15 / 2.3e-14 | 2.7e-15 / 8.2e-15 / 3.7e-14 | 6.9e-15 at n = 24 | 5.9e-14 at n = 24 |
| rotated π/4 | 1.2e-9 / 2.1e-6 / 1.0e-2 | identical to the square | 3.8e-14 | 5.8e-14 |
| triangle | 3.7e-3 / 1.0 / 1.0 | 4.2e-15 / 9.5e-15 / 5.2e-14 | 1 | 1.0e-10 |

Agreement with the developer's numbers at matching degrees is within factors 2–5, with different seeds and generators. Example: rotated π/4 at n = 20: mine 2.1e-6, developer 2e-6.

## Remaining uncertainty

- One seed per shape; M mostly 1681 (≤ 26896 for the M scan); n ≤ 24 (≤ 32 for Ritz). Padua and the developer's L-shape sets were not rerun.
- The developer's iid-forcing predictor (T-107 (c)), mixed-precision split (d), block-identity fractions (f), "P* = P" and the 12-angle triangle scan were **not** rerun. I used independent analogues instead (direct exact-propagator norms).
- The selection-rule result is MEASURED on 5 sets. I have no theory for which selection is optimal, and "adapt" is a heuristic.
- The super-exponential shape is measured over a short range only.
- Liu–Narayan was read only through a WebFetch summary, and Dunkl–Xu Thm 3.2.5 only as cited by BPS. Neither is verified.
- My (N, N*) implementation follows the published listing with ORTH added. HL's own code was not available.
- The rank-r non-commutant argument and the affine continuation-scheme strengthening for T-401 are my own short arguments. They should be audited before anyone relies on them.
