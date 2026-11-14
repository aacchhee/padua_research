# Independent checks X1 — Xu Lebesgue constant records X1-01 … X1-07 (X1-08 skimmed)

Checker: Claude Opus 5.5 (independent checker subagent, launched by the orchestrator; standard effort). Date 2026-11-14. I did not develop this work and did not run git or edit any existing file. This record supplements the Codex audit required by `agents/WORKFLOW.md`; it is not a substitute for it.

## 1. Scope and files read

Developer: Claude Fable 5.2 (xhigh), round X1-2. Conventions: `literature-xu-mp.md` §1 and `lit-notes/X1-sources.md` §8. Every proof step of X1-01 to X1-07 was reconstructed by hand. X1-08 is MEASURED only and was skimmed; I re-derived its edge identity (1).

| File | SHA-256 |
|---|---|
| theory/X1-01-tensor-lift.md | 830dac482b452962e216c6e9568af2e539f6e88339d7ec2d96fafbae6c0751be |
| theory/X1-02-trig-lebesgue-function.md | a46b2c9a8131e9492de69042f09a7f5c0441ae380ebd16f04911e9e3a18da551 |
| theory/X1-03-vertex-value.md | 71ca9f4d54d154daea4552475d8b873794fe279a6cecd3835fd8cfb72550aa66 |
| theory/X1-04-exact-lebesgue-constant.md | 821355268ea3ea83fe50f7948b78d781ee7f7f4fa311faf25b02799cd99d2b4c |
| theory/X1-05-argmax-set.md | 47fdd0b01f3d35c7d3243185ed1c8e8e6f8a33815ca7cd9b05db3d24d530b3d9 |
| theory/X1-06-chebyshev-constant-expansion.md | e2d830ba361b25852c1cd3a4b9fd2acbf4c683cec827ea83357adb1fe5073227 |
| theory/X1-07-expansion-and-conjecture-17.md | 080bf20d57ffe6ef646559f7ef5d1e39a4f67660ee8f927b7d091860d43564cc |
| theory/X1-08-edge-deficit-measured.md (skimmed) | 49dc4c24c8f93ea53a292ecc706d95456a39234ed1701f143b91ef8701591318 |
| literature-xu-mp.md | fdd907d488d944762c43c3197f7d48bd76ed45165da9c6fa92bdd652998f2350 |
| lit-notes/X1-sources.md (§8, plus grep for Harris / Dencker–Erb / Lissajous) | 9f20c7c0c63ff4c606bcc09691daf955365f5cb67545085263c7dcd56b55251f |
| ../padua-lebesgue-followups-20261103/theory/t4-01-corner-defect-limit.md (PD-T269: statement, eq. (9), (1), (2)) | a40f61a44d787201ecfe82f08eccb9e57de02a9d3a18161741be7f2f8cde4b46 |
| ../padua-lebesgue-followups-20261103/theory/t4-02-one-dimensional-remainder.md (PD-T270 eq. (2)) | ead57816c2b33e250462514e25bcd4e709902523b33bd4cf1a17c007a6ec2e28 |

PROOF_STATUS.md was consulted only to confirm that PD-T159, PD-T269, PD-T270 and PD-T271 are registered PROVED on main.

## 2. Independent recomputation

All code is my own, written from the definitions in `literature-xu-mp.md` §1. None of it imports or copies the developer's scripts (`xu_kernel.py`, `xu_exact.py`, `research/x1_*`), and no kernel formula of Xu or BCDMV is used. Scratch copies are in `/tmp/ic-x1/`. Committable copies are in `code/xu/independent/`:

| Script | SHA-256 |
|---|---|
| ic_x1_a_vandermonde.py | 3b043b91db2afe4daf2182aafbfe078fe0af9a8ab1d589698df4add7dcce538c |
| ic_x1_b_grid.py | 15ab31c2b362052839303370a6a029765314949a7da6d40dd78de15dd94ddefa |
| ic_x1_c_1d.py | 18f4a3ad93c0387b81f02b4673f2a8957bdf43f15e7b838f88949455075abdd5 |
| ic_x1_d_enclosure.py | 319a872e2e6b699ff7d0d2ec607daa00823b5589d795d4447eb1949da940c9a0 |
| ic_x1_e_signs.py | af90c87f5b52be47b3f8603ea7101a1048d9ef2bdde93170aee891ac2d4b8e4d |

Environment: Python 3.13.18, mpmath 1.4.1, numpy 2.5.3, scipy 1.18.1. Every run used `python3 -I`.

**(a) Direct Lagrange basis at 50 digits.** `python3 -I /tmp/ic-x1/a_vandermonde.py 10 500` (17 s; log `/tmp/ic-x1/a_log.txt`, json `a_out.json`).
- Method: mpmath at dps = 50. The basis is T_i(x)T_j(y) for i + j ≤ n−1 plus the E_j. The Vandermonde matrix at X_n is inverted with `mp.inverse`.
- Range: n = 2..10.
- Results:
  - The matrix is square for every n, which confirms dim count = |X_n|. Inverse residual ≤ 2.5e−53.
  - Vertices: |λ_n(v) − L_n²| ≤ 6.4e−50 for v ∈ V*. At the node vertices (odd n), λ_n = 1 to 2.2e−50.
  - X1-03 (1), node by node, at every non-node vertex: max error 1.9e−50.
  - 500 seeded uniform random points per n: **0 violations of λ_n ≤ L_n²**. The largest ratio λ/L_n² is 0.97 (n = 2), 0.94 (n = 3) and 0.76–0.79 for n ≥ 4.
  - Lift formula X1-01 (1), with my own d_n and a brute-force fiber enumeration, at 15 random (u, v) ∈ [−4, 4]² per n: max error 3.7e−50.
  - The fiber image equals X_n, and every |F(ξ)| = 2^{3−β}.
  - At the same 15 points per n, λ ≤ ω(u)ω(v) ≤ L_n² held with 0 violations.

**(b) Maximizer set, n = 2..16, float64.** `python3 -I /tmp/ic-x1/b_grid.py 16` (68 s; log `b_log.txt`).
- Method: float64 Vandermonde Lagrange basis on the angle grid θ_i = kπ/(12n), k = 0..12n. This grid contains every complementary point (aπ/n, bπ/n).
- Grid results:
  - For every n = 2..16, the set of grid points within 1e−9 of the grid maximum is exactly V*.
  - |grid max − L_n²| ≤ 1.2e−14.
- Local search: Nelder–Mead in the angles, started from the 30 best non-vertex grid points and from 200 random starts.
  - The best non-vertex local values λ/L_n², for n = 2..16, are 0.5000, 0.7757, 0.7929, 0.8002, 0.7997, 0.8243, 0.8385, 0.8465, 0.8512, 0.8614, 0.8678, 0.8720, 0.8746, 0.8798, 0.8833. All lie on an edge for n ≥ 3.
  - No non-vertex point approaches L_n².

**(c) One-dimensional claim, n = 1..30.** `python3 -I /tmp/ic-x1/c_1d.py` (20 s; log `c_log.txt`).
- Method: ω_n^C was evaluated for both parity classes on a full period with step π/(800n). Midpoints lie on this grid exactly.
- Results:
  - max(ω − L_n) = 1.6e−14, which is rounding.
  - For n ≥ 2, ω = L_n at every midpoint to 1e−12, and ω < L_n at every other grid point. The minimal relative gap, 1.9e−6, is the expected quadratic dip next to a midpoint.
  - For n = 1, ω ≡ 1.
- X1-02 (d): the Lagrange Lebesgue function of the n zeros of T_n has maximum L_n, attained at ±1, to 1e−11 for every n ≤ 30.

**(d) X1-06 / X1-07 at 50 digits.** `python3 -I /tmp/ic-x1/d_enclosure.py` (106 s; log `d_log.txt`).
- X1-06 (2) holds for every n = 1..200. n⁴(A_n + π/(72n²) − L_n) runs from 0.0061561 (n = 1) to 0.0087922 (n = 200), below 7/(240π) = 0.0092840 and approaching 49π³/172800 = 0.0087923.
- Series (1), with G computed by direct quadrature of φ₀ (not through the digamma identity), for n = 1, 2, 3, 7, 20: |L_n − A_n − (4/π)Σ(−1)^{j−1}G(nj)| ≤ 3e−31 at dps 30. G(n) = ψ(n+½) − log n holds to 1e−31.
- X1-07:
  - (a) 0 < R_n < πA_n/(36n²) + π²/(5184n⁴) < (log n + 1.55)/(18n²), for n = 1..200;
  - (b) the two-sided bound on E_n, n = 1..200;
  - (c) L_n² < ((2/π)log n + 1)² for 2 ≤ n ≤ 200, with equality at n = 1;
  - (d) L_n² > ((2/π)log(n+1))² for every n ≤ 200.
- Constants: c₁ = 0.96252282676071300779813206836…, b = 1.2255221257420120939668889992720…, c = 0.92645019203543354466032051215757…. These agree with the record's digits (the record truncates).
- Margins: πc₁/36 + π²/5184 = 0.085900 < 1.55/18 = 0.086111; c₁ + π/288 = 0.97343 < 1; (2/π)log 2 = 0.44127 < c₁.
- The PD-T159/PD-T269 definition (2/n)Σ_{r odd} d_r csc(rπ/(2n)) equals (1/n)Σ cot((2k−1)π/(4n)) to 1e−50 for n = 2..80.
- L_n² = 10.288129, 11.744499, 12.887738, 13.835133 for n = 34, 48, 62, 76, matching X1-04's Checks.

**(e) Sign identities and the X1-05 cancellation, computed directly from d_n values.** `python3 -I /tmp/ic-x1/e_signs.py` (4 s; log `e_log.txt`).
- For n = 2..40, three things were checked:
  - the (χ) identities of X1-02 (b);
  - the formula χ(m) = (−1)^{(m₀−1)/2};
  - X1-05 Step 2, χ(e+1)χ(e−1) = −1 for every even e ≢ 0 (mod 2n) in [−6n, 6n].
- For n = 2..24, Δ_n > 0 was checked from the fiber sums at all 2696 non-vertex complementary grid points.
- 0 failures.

## 3. Line-by-line proof check (summary of what was verified)

- **X1-01.**
  - §0: the Dirichlet identity sin((n−½)t) + cos(nt)sin(t/2) = sin(nt)cos(t/2), cardinality on C_n, and the top-frequency decomposition (2).
  - §1: r₀, s₀ are well defined mod 2n. The map C_n² → {(r₀, s₀)} is exactly 2-to-1, the generators act as τ: id, s: (r₀, −s₀), c: (−r₀, s₀), and |F| = 2·2^{2−β}. Surjectivity follows from the "Conversely" construction.
  - §2: Γ-invariance, the relation s*c* h = h(−u, −v), and 𝒜s* = 𝒜.
  - §3: every product-to-sum identity in (i)–(iii), re-derived:
    - k ± l ↔ m₁, m₂ and the identifications nu ± mv, nv ± mu ↔ k, l;
    - for even n, 𝒮(sin nu · e^{imv}) = (i/2)(T_l(x)T_k(y) − T_k(x)T_l(y)) = (i/2)E_k or −(i/2)E_l, and sin nu sin nv = −½E₀ with σ = +1;
    - for odd n, ½E_{min(k,l)} and ½E₀ with σ = −1, and 1 ≤ min(k, l) ≤ (n−1)/2 < ⌈n/2⌉.

    The symmetrization kills exactly the τ-odd modes, and the surviving degree-n modes land in the correct E_j with the correct σ. Both parities are fine.
  - §4: the descent argument (Im P vanishes on Q, hence identically) is correct.
  - §5: surjectivity together with #spanning functions = |X_n| gives a bijection; linear independence is not needed. The counts n(n+1)/2 + ⌈n/2⌉ = n(n+2)/2 (n even) and (n+1)²/2 (n odd) are correct.
- **X1-02.**
  - (a) and (b) are correct: χ is even and 4n-periodic, χ(m+2n) = −(−1)^nχ(m), and the midpoint sum equals L_n.
  - (c) is a real proof, not an appeal to folklore. On [0, π/(2n)) all 2n terms of ω^odd have the sign ε_p, which I checked with the signs of sin(n(u ∓ u_p)) and cot((u ∓ u_p)/2). Then ω^odd = P(cos u), with P = Σ(−1)^{k−1}ℓ_k of degree n−1. P has n−1 zeros in (t_n, t₁) and a > 0, so it is strictly increasing on [t₁, ∞), and cos u ∈ [t₁, 1]. The reduction to [0, π/(2n)] and the "mapped to 0 iff midpoint" claim are correct. For n = 1, ω ≡ 1.
  - (d) is correct; the step ℓ_k(cos u) = c_k(u) holds for all u.
- **X1-03.**
  - §1: the shift to odd residues, and that {±r − a_v} = {±r′} mod 2n for a_v ∈ {0, n}. Also r′ + s′ ≡ p′ is odd, and (p₀, q₀) = (r′+s′, r′−s′) lies in F′.
  - §2: the orbit-sum formula holds even when the action is not faithful. Four group elements give t(p₀, q₀) and four give t(p₀+2n, q₀+2n). Also checked: the ranges of α and β̃; sin(p₀π/2)sin(q₀π/2) = −(−1)^{r′}; cot α cot β̃ + tan α tan β̃ = 2(2 + z_{r′} + z_{s′})/(z_{s′} − z_{r′}); and |F′|/(4n²) = 2^{1−β}/n². This agrees with 1/K*_n(ξ, ξ) of the conventions.
  - §3: all terms in a fiber share a sign, so λ_n(v) = ω(u_i)ω(u_j) = L_n².
- **X1-04.** λ = ω(u)ω(v) − Δ with Δ ≥ 0 follows from the partition of C_n² into fibers and the triangle inequality applied fiber by fiber. The identity holds for all real (θ₁, θ₂), and Φ covers Q, so the bound holds on all of Q. Attainment at V* comes from X1-03.
- **X1-05.**
  - Step 1: equality forces ω(u) = ω(v) = L_n, because L_n > 0 and each factor is ≤ L_n. Then u, v are midpoints (this is where n ≥ 2 enters), which gives a = (i+j)/2 and b = (i−j)/2 in [0, n] with a + b ≡ n.
  - Step 2: correct, including the case e₀ > 2n.
  - Step 3: both witness pairs, (i+1, j+1) with its s-image and (i+1, j−1) with its c-image, are in C_n², lie in one fiber, and have nonzero terms of opposite sign. No d_n term vanishes at midpoints (X1-02 (b)), so no degenerate cases arise.
  - Edge cases:
    - n = 2: the complementary non-vertex point is the centre, where a = b = 1.
    - Odd n: Step 4 correctly leaves only (0, n) and (n, 0).
    - n = 1: the remark is correct, with V₁ = span{1, x+y} and ℓ = ½ ± (x+y)/4 ≥ 0.
- **X1-06.**
  - §1: the partial fractions match PD-T269 eq. (9), which is proved locally there; the block bookkeeping is correct.
  - §2, kernel inequalities: (K2) has coefficients [1 − 2k(2k+1)/6]; (K3) has coefficients that are 0 at m = 2, 4 and positive for m ≥ 6, since 140 > 60. The bounds G < 1/(24x²) and H ≤ 7/(960x⁴) follow.
  - §3: the summation formula (5).
  - §4: the blocks (6), and (7) via 2H_{2K} − H_K → log K + γ + 2 log 2.
  - §5: the telescoping 2Σ(−1)^{j−1}G_j − G₁ + G_{2M+1}, Wallis' product (or the PD-T270 variant), and the final constant log(8/π).
  - §6: the alternating-series enclosure of S_H and the constant 7/(240π).
- **X1-07.**
  - Algebra: R_n = (ε − η)(2A_n + ε − η), and both bounds in (a) and (b).
  - (c) and the literal-inequality argument in (d).
  - Dependencies: PD-T269 (1), (2) (statement read; its definitions use n ≥ 2) and PD-T270 eq. (2) (identity of the L_n definitions, also checked numerically).

## 4. Findings

| # | Severity | Locator | Finding |
|---|---|---|---|
| F1 | MINOR | X1-05 §Checks, first bullet (and the LOG or PR text if it quotes the same list) | The list "largest non-vertex ratio λ_n/L_n² per n: 0.5, 0.76, 0.7929, 0.7978, 0.7944, …" is a maximum over the **complementary grid points** only. Off-grid non-vertex local maxima are larger for some n: n = 3: 0.7757; n = 5: 0.8002; n = 6: 0.7997 (my check (b)). The bullet should say "over complementary grid points" so that it is not read as the global second maximum. This is a MEASURED item only; the proof does not use it. X1-08 Scope already notes the off-grid issue for n ≢ 0 (mod 4). |
| F2 | MINOR | X1-07 Statement (d), first sentence; any headline "settles Conjecture (17)" | "Both parts hold for every even n ≥ 2" mixes an asymptotic statement with an every-n statement. Suggested wording: "the first part holds as Λ/((2/π)log(n+1))² → 1, while the literal inequality fails for every n; the second part holds for every even n ≥ 2". The verdict "settles (17)" is correct under the reading of "≲" as an asymptotic upper bound fixed in `literature-xu-mp.md` §4. Headlines should keep that qualifier together with the fact that the literal inequality fails for every n. |
| F3 | NOTE | X1-07 §1 and §2 (the "certified inequalities") | The two inequalities the proof uses can be checked by hand, so the arb script is not needed for them. Since πc₁/36 = (γ + log(8/π))/18, the first is γ + log(8/π) + π²/288 < 1.55; its value is 1.54620. The second is c₁ + π/288 = 0.97343 < 1. Four-digit bounds on γ, log 2 and log π suffice. Optional: state this so that the PROVED parts (a) and (c) carry no computer step. |
| F4 | NOTE | X1-07 Statement header, (e) | The header says "Let n ≥ 1", but Λ_c(n) in PD-T269 is defined for n ≥ 2. The limit and the n ≥ 32 bound are unaffected. |
| F5 | NOTE | X1-06 §Depends on | Σ(−1)^{j−1}j^{−2} = π²/12 and Wallis' product are used at textbook status, following the PD-T159 precedent, and the Wallis-free route through PD-T270 is valid. The dependency on PD-T269 eq. (9) was checked: that record proves it locally. |
| F6 | NOTE | X1-01 §Sources; X1-04 / X1-05 / X1-07 novelty wording | This is not a mathematical finding; it is for the novelty gate. Harris, "Bivariate Lagrange interpolation at the Chebyshev nodes", Proc. AMS 138 (2010) 4447–4453 ([AMS](https://www.ams.org/proc/2010-138-12/S0002-9939-2010-10581-6/)), builds on Xu's Lagrange formula and does not appear in `lit-notes/X1-sources.md`. Its abstract does not mention Lebesgue constants. Li–Sun–Xu 2009 is read at digest level only, as the developer already flags. Both should be read in fulltext before any priority wording. A quick web search on 2026-11-14 found no statement of Λ^Xu_n = L_n². This includes Białas-Cież–De Marchi–Suder, arXiv 2605.23299, whose digest does not mention Xu points. The search is not exhaustive. |
| F7 | NOTE | X1-01 §1 | The 2-to-1 claim states injectivity modulo τ explicitly, but surjectivity onto {r₀ + s₀ ≡ n+1} only implicitly, through the "Conversely" construction. This is harmless. |

There are **no BLOCKING or MAJOR findings.**

**Status discipline.**
- Each PROVED record states its definitions, assumptions, dependencies and a complete proof. The dependency lists are accurate:
  - X1-03 uses X1-01 (a) and (1) and X1-02 (b).
  - X1-04 uses X1-01, X1-02 (c) and X1-03 (b).
  - X1-05 uses X1-01, X1-02 (b), (χ) and (c), X1-03 and X1-04.
  - X1-06 uses PD-T269 eq. (9), which is merged.
  - X1-07 uses X1-03 to X1-06, PD-T269 and PD-T270, all merged.
- Nothing depends on the unmerged PR #27; the only mentions of it are disclaimers or history.
- Numerical runs are labelled MEASURED, for verification only, and no constant is fitted.
- X1-08 is correctly MEASURED, and its integral formula (M3) is marked OPEN.
- I re-derived the edge identity X1-08 (1): the eight Γ-images on θ₂ = 0 pair up as stated.

## 5. Verdict per record

| Record | Verdict |
|---|---|
| X1-01 tensor lift, fibers, unisolvence | **confirmed** (F7 is a note) |
| X1-02 1D factor, ω_n ≤ L_n, equality iff midpoint (n ≥ 2), Chebyshev interpretation | **confirmed** |
| X1-03 λ_n(v) = L_n² on V*, nodewise formula (1) | **confirmed** |
| X1-04 λ_n = ω(u)ω(v) − Δ_n, Λ^Xu_n = L_n² | **confirmed** |
| X1-05 argmax = V* for every n ≥ 2 | **confirmed with minor issues** (F1, Checks wording only) |
| X1-06 series and n⁻⁴ enclosure | **confirmed** (F5 note) |
| X1-07 expansion, constants, remainder, verdict on Conjecture (17) | **confirmed with minor issues** (F2 wording; F3, F4 notes) |
| X1-08 (skimmed) | MEASURED status appropriate; identity (1) re-derived |

Headline check: Λ^Xu_n = L_n² for every n ≥ 1, with L_n = (1/n)Σ_{k=1}^n cot((2k−1)π/(4n)), and the argmax is exactly the non-node vertices for every n ≥ 2. Both are confirmed by my reconstruction of the proofs and by independent 50-digit Vandermonde computations (n ≤ 10) and float64 grid and local search (n ≤ 16). Consequently both parts of BCDMV Conjecture (17) hold for even n, with "≲" read as an asymptotic bound. The first part holds in the sharp form Λ ~ ((2/π)log(n+1))²; the literal inequality fails for every n.
