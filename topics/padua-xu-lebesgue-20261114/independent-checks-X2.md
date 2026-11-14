# Independent checks — round X2-2 corner-value records (Morrow–Patterson points)

Checker: Claude Opus 5.5 (claude-opus-5-5), independent subagent; I did not develop this work (developer: Claude Fable 5.2 xhigh). Date 2026-11-14.
Role: independent mathematical checker (supplements, does not replace, the cross-agent audit required by `agents/WORKFLOW.md`). No Git operations were run, as instructed, so no commit SHA is recorded. Rule files and records are identified by the SHA-256 hashes below. No existing file was edited. Concurrent X2-3* records were ignored.

Scope: theory/X2-21, -22, -23, -24, -25, -26, X2-N29, X2-N30 in full; X2-27 (MEASURED) and X2-28 (OPEN) skimmed for honest labelling only. No novelty content is in scope (the novelty gate X2 was not re-run), so `state/IDEAS.md` was not read.

## 1. Files read (SHA-256)

| File | SHA-256 |
|---|---|
| theory/X2-21-corner-kernel.md | 67106d7e9d4c4772e6cb19f629a357c2fcd1be60f8630cecc113e71bcf766032 |
| theory/X2-22-lower-vertices.md | 2e2b9b9fc34ed343313ce0f7ca5dea6420c4703550e54a996bfe23dcccd67568 |
| theory/X2-23-upper-vertex-closed-form.md | 06925042e4cbc4e9249f40d5047cbc128dc1bfc6444452584dc5cda782b0becb |
| theory/X2-24-upper-exceeds-lower.md | 0dd0d75ce2790478bfb2339f3de3bd3bd7f2a05e3e2e83cc7a5be522899db216 |
| theory/X2-25-upper-vertex-asymptotics.md | ce47a5a4dbe7e267d06c0e47813a77ba5791073ff6ea9d8b5a0b0789e6b25167 |
| theory/X2-26-explicit-lower-bound.md | c811552621cece787002ae77f3c27f665f48aef21374c48e8c38025bf3657c0d |
| theory/X2-27-vertex-remainder-measured.md (skim) | 3e5314035ba4fa2fc6a430ed998c486585f81b2238fe163c517dbb299fb80109 |
| theory/X2-28-argmax-open.md (first ~80 lines) | 8f1aa4e8093ebb81747b763c9a11b311062e257818cfccd263a30fa577a179e1 |
| theory/X2-N29-no-central-symmetry.md | f77b04de929f8954df39133ae0e3e87a169bfceece62a024bb4ef2237cfe5eb4 |
| theory/X2-N30-vertex-value-not-dimension.md | 7ecd43dc6dd28f1a71b90322c166d07f216eac8fa230377152cf27507af74b17 |
| literature-xu-mp.md (§§1–5) | fdd907d488d944762c43c3197f7d48bd76ed45165da9c6fa92bdd652998f2350 |
| lit-notes/X2-sources.md (§§0–1b, grep of §6–7) | a019db2e5860e5d93f948e18f1b2e5f27fc04f5ea72957ba5b67179d5e0fc202 |
| code/mp/research/x2_corner_checks.py (first 80 lines read; run in full) | cf3a6199bc627847b968d6d41ff6b5ede99d64650e5b411a2f88bea5dfe3de65 |
| code/mp/research/x2_corner_arb.py (read in full) | 20417025731ecc2adad0fb93be9efefadcfb0f50cdfacad51c65222d4a89e924 |
| AGENTS.md | c44a76f138fce01f02c06753b22fbc83fd5c1ee701785d49ba17cef5f8eee05b |
| agents/WORKFLOW.md (grep for status/split/severity rules) | 65e6b7268f4df4c97a3271ead27199381747b940ebba5cce2796a0bf7b8b9209 |
| agents/claude/CLAUDE_ROLES.md (grep) | 35c6146f23712d7bfa7305ee03345f8e55457fc9bc7b0ff2132e5872b09703d2 |

I did not open these primary sources: BBDM (Constr. Approx. 63 (2026)), Beberok (JAT 311 (2025)) and Washington. Literature statements below are taken from the lit-notes, as the records also take them.

## 2. Files written by this checker

| File | SHA-256 | Purpose |
|---|---|---|
| code/mp/independent/ic_x2_vandermonde.py | afc612aad46e2e3605ef7e05581c15438f46c538870a32f5f81f911418b7f678 | Lagrange values at the 4 vertices from a Chebyshev-T Vandermonde solve (mpmath, 60 digits), even n ≤ 20; no kernel or closed form used for ℓ |
| code/mp/independent/ic_x2_cstar.py | 4898890cc9cc9a6b7fc36853107d55fe74ed044a97b0d74098fcefffaf14508d | c* by direct integration of ĥ: mpmath quad (non-rigorous) and acb.integral (rigorous), plus constant arithmetic of X2-25 |
| code/mp/independent/ic_x2_arb_finite.py | 2785a35d6d3b4eccf851aec806ace787f9737acc64c14ea658d6f932942292bd | own arb implementation of X2-23(a) in the original (p,q) indexing; finite ranges of X2-24/26/N30, bracket of X2-25, thresholds |
| code/mp/independent/ic_x2_bracket.py | c8b29d061ecd0c33c85e95a25652a366a6b89c24746ac97542bd0223daba02a3 | float64 Σ|A| over all nodes, 248 even n ≤ 5000, two-sided bracket of X2-25 |
| code/mp/independent/ic_x2_stepB.py | ad43d47b6532e83819ff398a2882e171a049ff38a0583eed910b16975e684513 | float64 node-wise check of (B6) with majorants (B2), (B5), and the Step C block totals |

Outputs (scratch, not committed): `/tmp/ic-x2/*.json`, `/tmp/ic-x2/*.log`.
Environment: Python 3.13.18, mpmath 1.4.1, numpy 2.5.3, python-flint 0.9.0, 2 cores.

## 3. Commands run and output summaries

All commands were run from `code/mp/research` (developer) or `code/mp/independent` (checker).

1. `python3 x2_corner_checks.py --out /tmp/ic-x2/dev_checks.json`: 27 s, all sections.
   - ident: orthonormality max err 5.99e−41; corner-kernel rel. err 1.46e−37; closed forms 7.46e−38; `agrees_with_pathA_certificate_to_1e-33: true`.
   - Per n ∈ {2,…,12,16,20,24,30}: `sign_pattern_ok: True`, band sizes 3,5,7,9,11,13,18,22,27,34, and the band/one-sum/hyperbolic differences ≤ 2e−36.
   - cstar: series J=60 gives 0.51695365331673; nsum gives 0.516953653366806272706422282045; max|Φ'+h̃| = 2.6e−41; max|h̃''| on [0.05,60] = 2.892 (bound 4.533).
   - decomp: `all=True` for every M ∈ {4,…,1202}.
   - table: R_n from −1.623 (n=2) to −20.420 (n=6400).
   - Every number quoted in the records' Checks was reproduced.
2. `python3 x2_corner_arb.py --nmax 60 --out /tmp/ic-x2/dev_arb.json`: 0.4 s.
   - c* ∈ [0.51695365336638144…, 0.51695365336768164…], `roots_certified: true`.
   - All seven flags are true for even n ≤ 60.
   - f(42) = −0.891764, f(44) > 0, g(18) = −0.241886, g(20) > 0.
   - λ values are identical to those quoted in X2-23 and X2-N30.
3. `python3 ic_x2_vandermonde.py --nmax 20 --dps 60`: 226 s. For every even n ≤ 20:
   - Vandermonde Lagrange values agree with the four closed forms of X2-21 part 3 *node by node*, max error 5.9e−57.
   - λ_n(±1,−1) − (n+1) = O(1e−58); λ_n(−1,1) − λ_n(1,1) = O(1e−58).
   - λ_n(1,1) equals the developer's values (e.g. 5.84555923316812696768990194691, 236.900953275273810960675988079).
   - sign rule (−1)^{m+1} at (±1,−1): ok; band sign rule of X2-23(b) at (1,1): ok (both from the Vandermonde values); U_n(x_m) = (−1)^{m+1}: ok.
4. `python3 ic_x2_cstar.py --J 800 --JR 300`: 4 s.
   - mpmath quad over 801 bumps, sign structure checked for j ≤ 50: partial sum 0.5169536533668045881755589, proved tail ≤ 5.1e−15; with a fitted j⁻⁵ tail, 0.516953653366806271651805. This agrees with the developer's 0.516953653366806272706 to 1e−18, i.e. ≥ 15 digits.
   - c₀ by quadrature equals the Si formula to 30 digits.
   - **Rigorous** (acb.integral of h̃ over each bump, roots enclosed by certified sign changes, [0, 2⁻³⁰] bounded by (4/3)τ², proved tail): **c* ∈ [0.51695365336672179537, 0.51695365336697862536]**. This lies inside the developer's interval [0.5169536533663, 0.5169536533677] and is about 5× narrower.
   - Bump integral × j⁵/(2/π⁵) is 0.048 (j=1), 0.26 (10), 0.332 (800), so the proved bound 2/(jπ)⁵ holds with ratio → about 1/3.
   - Constants: sup sin²x/x = 0.7246114 (at 1.16556); ∫x²(1−x)|2x−1| = 1/32 exactly (numerically); T₂ arithmetic = 9.0120537; Σe₁ bound 2.011365; ΣL_s bound 4.277729; 2·1.4494/π = 0.9227167; log P offset 1.5963126; 3.6280725; 1.1118923; miss-tail coefficients 0.112337, 0.27376. All are consistent with the rounded constants in X2-25.
5. `python3 ic_x2_arb_finite.py --nmax 60 --extra 100,200,400,1000`: 4 s, 200 bits, using my own c* enclosure.
   - All flags are true for every even n ≤ 60: X2-26 λ > c*n²; X2-N30 λ < d for n = 2, 4 and λ > d for 6 ≤ n ≤ 60; X2-24 λ > n+1.
   - The flags also hold for n ∈ {100, 200, 400, 1000}: X2-23(f) no term's ball contains 0; X2-23(c) ΣA ∋ −(n+1); X2-25 bracket.
   - Smallest margins: λ_6 − d_6 = 0.025027606 ± 3e−12; λ_2 − d_2 = −0.15444077; λ_4 − d_4 = −0.15916453.
   - g(20) = 2.36194, g'(20) = 1.31417, f(44) = 1.77693, f'(44) = 1.37103.
   - g > 0 for even M ∈ [20, 4000] and f > 0 for M ∈ [44, 4000] (sanity check only; the analytic monotonicity was checked by hand, §4).
6. `python3 ic_x2_bracket.py`: 100 s, float64, 248 values: all even n ≤ 300, n = 300…5000 step 50, and 1024, 2048, 4096, 4998.
   - `all_inside: true`.
   - min upper margin 7.66 − R_n = 9.28; min lower margin 19.11.
   - R_5000 = −19.418; max |ΣA + (n+1)| = 9.8e−5 (accuracy proxy). Float agrees with arb at n = 1000 to 1.3e−7.
7. `python3 ic_x2_stepB.py`: float64, M ∈ {4,6,8,10,20,50,100,200,400}.
   - (B6) holds at every node of 𝒩₊ with the explicit majorants.
   - Block totals: Σe₁ ≤ 0.814 (bound 2.012); ΣL_s ≤ 2.374 (bound 4.28); ΣL_c ≤ 6.34 at M = 400 (bound 14.34). `all_ok True`.

## 4. Proof reconstruction (what I re-derived by hand)

- **X2-21.**
  - Lemma 0: the even extension to 𝒯, the parity count 4Σ_𝒩, the character sums, and the range analysis (|a₋|,|b₋| ≤ M−2; 2 ≤ a₊,b₊ ≤ 2M−2; a₊ = M and b₊ = M+1 cannot hold together because a₊+b₊ ≤ 2M) are all correct. Square AᵀA = I gives AAᵀ = I and hence the Lagrange property. The count (M−1)M/2 = dim Π_n is correct.
  - Lemma 1: the coefficient analysis c(a,b) (four cases) is correct, and the grouping c₀ = ½ is correct.
  - ∂x∂y P_M = G_n, and the derivative of Q is correct.
  - Lemma 2: the lattice values are correct, including U_{M−1}(y_q) = −(−1)^q.
  - Proposition: both parity cases and x ≠ y (M | p impossible) are correct.
  - Part 3: the reflections −x_p = x_{M−p} (same parity, M even) and −y_q = y_{M+1−q} (parity flips) are correct, and the signs of all four vertex formulas match.
  - Part 4 is correct. Equivalence with Beberok (2) as transcribed in lit-notes §1b: (2+x+y)/(2(y−x)³) = −(2+x+y)/(2(x−y)³). It matches.
- **X2-22.**
  - U_n(x_p) = sin(pπ − w)/sin w = −(−1)^p = (−1)^{p+1} is exact for every 1 ≤ p ≤ M−1.
  - ω > 0 and x_p ± y_q ≠ 0, so sgn ℓ(±1,−1) = (−1)^{p+1} at every node with no exception.
  - Reproduction of U_n(x) ∈ Π_n gives n+1 at (1,−1) and U_n(−1) = n+1 at (−1,−1) (n even).
  - The closed sum (n+1)(n+2)(n+3)/2 is correct.
- **X2-23.**
  - (a): the algebra (2M+1)(X−Y) − 2(X+Y) = (2M−1)X − (2M+3)Y and the prefactor 16/N are correct.
  - (b): the signs are correct, and so is the translation to (2n+3)x − (2n+7)y − 4.
  - (c): |A| = A + 2[−A]_+ and |A| = −A + 2[A]_+ are correct.
  - (d): |𝓡| = 2N − 4M = 4|𝒩'|; the CRT representatives r₁, r₂ and their four-fold distinctness; X_r − Y_r = sin(πr(2M+1)/(2N)) sin(πr/(2N)) with gcd(2M+1, 2N) = 1; and the folding to 1..N−1 are all correct (NOTE n1).
  - (e): (M−½)e^u − (M+3/2)e^{−u} = (2M+1) sinh u − 2 cosh u is correct.
  - (f): 2+2x_p ∈ ℤ ∩ (0,4), and κ ∈ {3/2, 2, 3} forces M ∈ {9/2, 5/2, 3/2}. Correct (NOTE n3).
- **X2-24.** The node (M−1, 2) is in 𝒩 and has x_p < 0 < y_q, so it lies outside B with A > 0. Correct.
- **X2-25.** Every step was re-derived.
  - Lemma C:
    - (i) the sign structure, and b_j − a_j < 1/(jπ) via cot ε = a_j;
    - (ii) ĥ ≤ 4(b_j−τ)/τ³ and the bump integral < 2/(jπ)⁵;
    - (iii) Φ' = −h̃ (also checked numerically by the developer, 2.6e−41), Φ(0+) = Φ(∞) = 0;
    - (iv) the series, the tail 2/(π⁶J⁴), ∫h̃ = 0, Φ(a_j) at tan a = a, and Φ(b_j);
    - (v) P − Q decomposition with integral remainders, h̃'' kernel, 68/15, and the 8τ⁻² + 20τ⁻³ + 30τ⁻⁴ + 15.6τ⁻⁵ bound;
    - (vi) one-sided derivatives at a_j, b_j;
    - (vii) T₂ ≤ 9.01205 < 9.0121.
  - Lemma R: the kernel K, the telescoping and the jump terms are correct. (R1) follows (NOTE n2).
  - Step A: X > Y ⟺ q' ≤ p'; b = πr/(2N); τ̃ = (M+½)b = ηr = jπ + μ (checked term by term); the bijection onto R₊; and (A3) ĥ(τ̃) = 4cos⁴μ ζ₊(V̂) are all correct.
  - Step B:
    - the product formulas and sinh u = sin b cot μ/(1−ε_s);
    - (B1), including tan(b/2)/(b/2) ≥ 1;
    - −A = 4c_M cos²t cos²θ (cosh u − S)/S³;
    - S < cosh u ⟺ S < S*;
    - (B2) via cosh u − 1 ≤ ½sinh²u;
    - (B3);
    - convexity of ζ₊ (ζ'' = 6V⁻⁵(2−V), kink −1 → 0) and the tangent bound.
    - (B4): I checked the case 1 − 2ε_c < 0 separately; it is covered because ζ₊ ≥ 0.
    - (B5): ε_s < M²/(2M+1)² < ¼ on V̂ < 1, using cos μ > cos t ≥ sin(π/2M) ≥ 1/M.
  - Step C:
    - counting ≤ 1/(yη) + 1 with 1/η < (2M+1)/π (because 4N < (2M+1)²);
    - S* < 1.02565;
    - block constants 0.00518 and 0.00554, so Σe₁ ≤ 2.01137;
    - ΣL_s ≤ 4.2777;
    - block-0 L_c via sup sin²x/x < 0.7247 and Σcot ≤ (2M/π)(1+log M);
    - blocks j ≥ 1 via the decreasing φ(s) = (1 + log(P/s))/s comparison, which gives 1 + 2 log P + ½log²P;
    - log P = log M − 1.5963126, giving 0.202642L² + 0.163608L − 0.372262. This is ≥ 0 at M = 4, the only even M with P < 1.
  - Step D:
    - 2Mη = π − 2ς, ηM = π/2 − ς, η − ς = π/(4M);
    - r ≤ M below π/2;
    - the block-separation claims for 1 ≤ i ≤ M/2 − 1 (they need (i+1)·2ς ≤ π/2, which holds);
    - ρ ≤ 2i gives ηr < iπ + π/4 < a_i;
    - ρ = M+k gives k ≤ i and Σ(2i+1−2k)ς = (i+1)²ς, then (i+1)²/i³ ≤ 4/i;
    - i ≥ M/2 tails 108/π⁶ and 80/(3π⁴).
  - Step E: 2c_M/η = 4(M+½)²/π; 2c_Mη = π(1+1/(4N))² < 3.2207; 2c_M/(M+1) ≤ 2; c_M ≤ M+0.6; and the assembly of 7.653 < 7.66 and of 0.405284/2.983256/15.8189 all check.
  - Corollaries (25c*/4 − 1 = 2.23096; the rate inequality) are correct.
- **X2-26.**
  - (M+½)² − (M−2)² = 5M − 15/4 is correct, and so is monotonicity in c.
  - (0.8106 log M + 2.9833)/M is decreasing for M ≥ 1, since its derivative has numerator −0.8106 log M − 2.1727 < 0. So g' > 0 on [20, ∞), and g(20) = 2.362 > 0.
  - sup{c : λ_n ≥ cn² for all n} = inf λ_n/n² = c* follows from strict inequality plus the limit.
- **X2-N30.**
  - The algebra (c* − ½)M² + (c* − ½)M + c*/4 + 1 − ℓ is correct.
  - f' is increasing (linear term increasing, subtracted term decreasing), f'(44) = 1.371 and f(44) = 1.777, so the analytic range n ≥ 42 is correct.
  - (iii): (n+5/2)² = (n+1)(n+2) + 2(n+1) + 9/4 is correct.
- **X2-N29.**
  - (i) and (ii) follow from X2-22 and X2-24 exactly as stated.
  - "Attained at each corner" is refuted because λ_n(±1,−1) = n+1 < λ_n(1,1) ≤ Λ_n.
  - The "not refuted" list (x-symmetry; attainment at (±1,1)) is scoped correctly.

## 5. Findings

| ID | Severity | Locator | Finding | Suggested disposition |
|---|---|---|---|---|
| — | BLOCKING | — | None. Every PROVED status in scope is supported by a proof I could reconstruct step by step. Every computer-assisted finite range (X2-25 enclosure, X2-26 n ≤ 16, X2-N30 n ≤ 40) was reproduced by my own independent rigorous code. | — |
| M1 | MAJOR (process) | X2-25 Checks and status row "Enclosure … PROVED, computer-assisted"; X2-26 status/Checks; X2-N30 status/Checks; X2-23/X2-24 Checks | The computer-assisted parts cite outputs in `/tmp/x2r2/` "not committed". CLAUDE_ROLES item 4 and WORKFLOW require a committed checker **and committed evidence records** (with manifest/hash) for a computer proof. The checker script is in the tree; the evidence JSON is not. The mathematics is confirmed independently (§3 items 4–5), so this is not BLOCKING, but it must be fixed before PR. | Commit the small `x2_corner_arb.py` JSON output (≈ tens of KB; `rows` can be kept) under `evidence/` with hash and environment, and cite it plus this independent rerun in the three records' Checks ("Independent rerun: pending" → done, this file). |
| m1 | MINOR | code/mp/research/x2_corner_arb.py lines 2, 5 (docstring) | Stale identifiers: it says the script serves "X2-N31, X2-N32" and cites "X2-23, Theorem 1(c)". The records are X2-N29/X2-N30 and X2-23 part (a)/(c). | Fix the docstring (non-result-bearing). |
| m2 | MINOR | LOG.md l. 58 ("c* … in closed form"); rounds.md l. 12 ("with c* in closed form") | c* is defined by an integral and evaluated by a convergent series over the roots of tan τ = τ. It is not a closed form. X2-25 itself words this correctly ("convergent series"). | Reword to "c* given by an explicit integral / convergent Si-series". |
| m3 | MINOR | X2-26 Statement ¶ "the constant readable from his final display is about 7.5·10⁻⁴ (n ≥ 8)"; literature-xu-mp.md §3.1 | This comparison constant rests on the orchestrator's transcription of Beberok's final display. lit-notes/X2-sources.md §1b flags that transcription for re-check (odd denominator "(n/2+n+2)"); literature-xu-mp §3.1 silently writes "(3n/2+2)²". The value 7.5·10⁻⁴ is right for the latter form. The attribution of Thm 0.1 (existential c) and the re-derivation of eq. (2) (X2-21, labelled "LITERATURE, not used as a lemma") are handled correctly. | Mark "(as transcribed; display not re-checked against the source)" or re-check the display. |
| m4 | MINOR | X2-28 status table (rows "First variation … MEASURED", "Scaling limits … MEASURED agreement", "Lemma K PROVED (minor)") | Outside core scope (skim). The OPEN label of the target is honest, and the PARTIAL ban is respected. However, the distinct measured claim D_x, D_y > 0 (n ≤ 80) has no durable home of its own (WORKFLOW: "A distinct measured claim gets its own durable registered home"). Classifying Lemma K as minor is acceptable, since nothing PROVED depends on it. | Move the measured first-variation claim into a MEASURED record, or reference it as evidence only. |
| n1 | NOTE | X2-23 (d) proof, "Let a_r be the r-th summand of (d)" | The identity a_r = (N/16)|A| holds for the summand *without* the prefactor 8/N. With the prefactor it would be |A|/2. The final formula is correct (developer and checker numerics agree). | Optional wording fix. |
| n2 | NOTE | X2-25 Lemma R "Consequence": "ĥ(τ) ≤ 4/τ⁴ for τ ≥ π" | This is true, but not by Lemma C(ii) as cited: (ii) gives 4/(jπ)⁴. Use instead that on the support tan μ ≥ τ, so cos μ < 1/τ, and ĥ ≤ 4 sin³μ cos μ/τ³ < 4/τ⁴. It is used only for integrability, so there is no effect. | Optional. |
| n3 | NOTE | X2-23 Assumptions/(f): "Washington … Prop. 2.4" | I did not check the locator. The fact ℚ(ζ_a) ∩ ℚ(ζ_b) = ℚ(ζ_gcd) is standard. Nothing depends on (f). Its conclusion is confirmed in ball arithmetic: no term contains 0 for every even n ≤ 60 and for n = 100, 200, 400, 1000. | None. |
| n4 | NOTE | X2-N29 Assumptions, "the negative statements hold for it [−MP_n] verbatim" | What holds verbatim for −MP_n is the refutation of the two BBDM statements. Items (i)/(ii) as written hold with the upper and lower vertices exchanged. | Optional wording. |
| n5 | NOTE | X2-25 Lemma C(vii), Step C, Step E | Some rounded constants have thin but valid margins: T₂ = 9.012054 vs 9.0121; sup sin²x/x = 0.724611 vs 0.7247; Σe₁ 2.011365 vs 2.012; 2c_MηT₂/8 3.628073 vs 3.629; 1.111892 vs 1.1119. All are verified (§3 item 4). | None. |
| n6 | NOTE | X2-N29/N30 Sources; X2-21/25/26 Sources | BBDM §7 p. 63 / §7.1 p. 64 and Beberok's content are LITERATURE via the lit-notes (orchestrator/reader readings), and I did not read the primary sources. The mathematical negative statements do not depend on them; only the phrase "negative answer to BBDM §7.1" does. The labels are correct, and no source claim is promoted into a proof. | None. |
| n7 | NOTE | X2-27, X2-28 | Labelling is honest. X2-27 is MEASURED, with the log² coefficient 2/π² explicitly OPEN. My float values of R_n (n ≤ 5000) agree with its table (R_1000 = −13.522, R_2000 = −15.928, …). X2-28 is OPEN, with measured support labelled MEASURED. | None. |
| n8 | NOTE | computer-assisted parts | "Exact arithmetic" is met in the sense of rigorous outward-rounded ball arithmetic (arb). The finite reduction (analytic ranges n ≥ 18 and n ≥ 42) is proved, and the checker is independent (this file). | None. |

## 6. Status / split discipline

- X2-21 bundles Lemma 0, the kernel and the vertex formulas. All are PROVED, with a per-part table, so this is acceptable.
- X2-24 is a separate corollary ID. X2-25 separates the measured remainder (X2-27) and the consequences (X2-26, N30).
- The computer-assisted enclosure inside X2-25 is labelled individually.
- PD-N records carry the status of the negative statement (PROVED) and the disposition REJECTED: refuted, with the scope (every even n ≥ 2, BBDM's node set, Π_n) stated exactly. The negative scope is neither over- nor under-stated.
- Literature attribution:
  - Beberok's eq. (2) is re-derived (X2-21 Lemmas 1–2 + Proposition), not inherited.
  - BBDM Thm 2 (cubature) is replaced by the self-contained Lemma 0.
  - X2-26 correctly presents itself as a strengthening of Beberok's Thm 0.1, not as a new theorem type.

## 7. Verdicts per record

| Record | Claimed | Verdict |
|---|---|---|
| X2-21 | PROVED | **Confirmed.** Proof reconstructed; node-by-node agreement with an independent Vandermonde solve at 60 digits, n ≤ 20. |
| X2-22 | PROVED | **Confirmed.** Sign identity exact at all nodes; λ(±1,−1) = n+1 reproduced independently. |
| X2-23 | PROVED | **Confirmed** (NOTEs n1, n3). Sign band rule verified from Vandermonde values; (f) confirmed in arb for n ≤ 60 and n ∈ {100, 200, 400, 1000}. |
| X2-24 | PROVED | **Confirmed.** |
| X2-25 | PROVED (enclosure computer-assisted) | **Confirmed.** All Steps A–E and their constants re-derived. Independent rigorous c* ∈ [0.516953653366722, 0.516953653366979] lies inside the claimed enclosure. The bracket holds for 248 even n ≤ 5000 (float) and in arb for n ≤ 60 and n ∈ {100, 200, 400, 1000}. Evidence-commit fix M1 is required. |
| X2-26 | PROVED (analytic n ≥ 18; computer-assisted n ≤ 16) | **Confirmed.** The finite range was checked independently in arb up to n = 60 (MINOR m3; M1). |
| X2-N29 | PROVED / REJECTED: refuted | **Confirmed**; scope exact (NOTE n4). |
| X2-N30 | PROVED (analytic n ≥ 42; computer-assisted n ≤ 40) / REJECTED: refuted | **Confirmed.** The finite range was checked independently in arb up to n = 60; smallest margin λ_6 − d_6 = 0.0250276 (M1). |
| X2-27 | MEASURED | Label honest. |
| X2-28 | OPEN | Label honest (MINOR m4). |

Remaining uncertainty: primary-source locators (BBDM, Beberok, Washington) were not checked by me. The float64 part of the bracket check (n > 1000) is MEASURED, but it is not needed because X2-25 is analytic. Proof checking is by hand reading; the per-node inequalities of Step B and the block bounds of Step C were also confirmed numerically by my own code for M ≤ 400.
