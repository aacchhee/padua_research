# L3 independent adversarial reconstruction 02 (rounds R04–R06)

## Header

- **Auditor.** Claude Opus 5.5, effort xhigh, as assigned (the runtime does not expose effort). Role: independent adversarial reconstructor for direction L3. I did not develop this work. I changed no Git state; I used only read-only `git log/show/diff/ls-files`.
- **Files written.** This file; scripts in `tracks/bivariate-lanczos/code/review_L3b/`; logs in `topics/bivariate-lanczos-20261031/reviews/logs_L3b/` (52 KB in total).
- **Rules read** at branch `claude/bivariate-lanczos-20261031`: `AGENTS.md`, `agents/WORKFLOW.md`, `agents/claude/CLAUDE_ROLES.md` (§Independent audit).
- **Audited head.** `ae991c128b5b7613d0bc0c6864bd2e6d4cc9409d` at audit start. The head advanced while I worked, to `05e0f52` and then `4406ac0`. `git diff ae991c1 HEAD` touches only L5 files: no L3 theory, round, candidate or code file changed.
- **sha256 of the audited files** (`tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-*`):

| File | sha256 |
|---|---|
| 310 | `2c934c863f46aa8fcc48eb35b84734a072df5be6cc3f1a44f63802f9dd1ae75b` |
| 311 | `53df46cf0bbea541a35abb118e0e6c6c5417a35659c7e2009dbc8059b3d6925b` |
| 312 | `80f59ddd11542339832392bd331ae0c5ec57811ae337e2b12303a81dcfdc394d` |
| 313 | `8293be74080873b7bf3bd78364c99cdff6e8ff4c15612b42a14ec27248d2a196` |
| 314 | `05d29b9b67504a219acbb501bef56147c8b6c07c98e59e1d6a890770465d5bc7` |
| 315 | `92518c2a895ad910863a0eee3f34e0c969ad23ee7c1bbd3faaf952a9ffb47d22` |
| 306 | `f2ee769d486b7a2f69585c1648ac1cd3d717a9288421c15c1a27293eb2e4a2ac` |
| N301 | `d49c9cb7b0b09ce9132c1df59a0e5239a69005d8d15c9a8ef01ef918d68c1653` |
| N302 | `abbe3b4385b8b935640bce9838177ed609936384f6e8510f5c8f4a105082c7a1` |
| N303 | `59ff30b96511754cb8239a65952bc51a22d958193ed31d8696c049a4c424eac7` |
| N304 | `73774e9b616744d1a53638195a339fa70caf15227610939cb5bb7b0c219009f9` |
| N305 | `e3e0c2d37a0a5ac4f6a1010d327203398a104564a3854991028e60d465c92792` |
| N306 | `beed786a72cb229ba882b2d61d3eab5cf925eca1bb25064a1f8d1b963d843af2` |

  Dependency hashes: 300 `6e1f225e69909dfa195949c33deb6b8969a9347b9fd136d1059ee2c61dea7cda`; 301 `ee3c600065b62557ae130e29eddcd18008cf0d51f7e77e329be7f5e9807f005b`; 303 `94a2065ff4dea04344a94fdf110fdc327884ef3978645e543bc337977346f76e`; 308 `59be05e16c06d18efd37475849449fa33e6999c976a9d5e3275329512ae5cc38`.

  Round records (`directions/L3/`): R04 `df404f42900026181eacf0af2dd6fd8fd6db328f873bfe12c31e7e59d1955eb4`; R05 `43ab136214214e910d520d1eaeb0a7876af88c398c1059419f5790b10c73e3d9`; R06 `a7ba225256ea0ad936ecc0d0b8b3772cf9ecee21bd3544d482f44f2f876ff6fa`; candidates `f18aa9c682743b1648904528a1ecea13feb7ae913243c36cc743074714e888f0`; SUMMARY `22b6eda2e76b8eab749826728a32f17012834816862c3e2e80a4f3522fdd853c`; STATUS `347d235ecc1238e4533d168337ce83ac6a1c84df82789aba4c0023debe33ad05`; response-recon-01 `85e60e478923e9739ed8b8e85fd6d6247729c485b0f1d09d901f857a96c9284a`.

  Other: plan.md `e88d2396c6b09a5f62d27b9056433b5eb4184e9349c33579125d2f16c306576f`; state/IDEAS.md `12ba5f8eccfc943faebee07b83ea37b995f0b89244fa3b9b81a6f88051ad931d`; review 01 `f1586072e5faf422309aa3193f47e0cb59ecc654e217a6359a66f239202ee871`.

- **Developer code.** All 17 L3 scripts and the L1 `l1_recurrence.py` match `directions/L3/logs/code_sha256*.txt` (`sha256sum -c`: all OK).
- **Read coverage, in full:** AGENTS.md; WORKFLOW.md; CLAUDE_ROLES.md; plan.md (L3-Q1, ledger, History including the M1 correction); **state/IDEAS.md complete** (144 lines: 48 seed rows, OBST-01..15, the disposition table); review 01; response-recon-01; R04, R05, R06, SUMMARY, STATUS and candidates.md (all L3 records); theory 310–315, N303–N306, 306, N301, 301, 303, 308, and the History sections of 300–309 and N302; L1's 102 and 104 (statements and proofs, needed for 314); developer scripts `r05_boundary_proof.py`, `r06_consistency.py`, `r06_weight_fit.py`, `l1_recurrence.py`, and the header of `exact_checkerboard.py` (only the node family and normalisation; nothing was imported); all R04–R06 logs.
- **Read in part:** the 300 status table and literature note; the 302/303/306/307/N301 diffs `0b7b396..ae991c1`; LOG.md (L3 entries).
- **Literature.** None needed. No R04–R06 claim rests on a new source. Padua unisolvence remains the one LITERATURE dependency (record `bos-dmv-xu-2007`); I did not re-verify it beyond review 01's exact check for n ≤ 4.
- **Environment.** Python 3.13.18, numpy 2.5.3, scipy 1.18.1, sympy 1.13.3, mpmath 1.3.0, x86-64 with 80-bit long double, 2 cores. No SDP package was used by my checkers.

## 1. PD-T?…-313 / PD-N?…-303: Padua obstruction for all n ≥ 4 (task 1)

**Reconstructed statement.** Let n ≥ 4 and g_m = T_{n−m}(x)T_m(y) − T_m(x)T_{n+1−m}(y). Then P_n = 9(g₁² − ½g₀g₂) + (g₂² − g₁g₃) satisfies three properties:

- deg P_n ≤ 2n+1;
- P_n = 0 and ∇P_n = 0 at all Padua points (cos jπ/n, cos kπ/(n+1)) with j+k even;
- Hess P_n ≻ 0 at all of them.

Consequently, by 303(e), for any positive weights on Π_n-unisolvent Padua points and every ε ∈ (0, ε₁], no positive measure on K_δ with δ ≤ δ₀(n) has the sections Φ(L_μ+E) whenever E(P_n) < 0.

**Hand check (all n).**

- *Degree.* For 1 ≤ m ≤ n the top form of g_m is −2^{n−1}x^m y^{n+1−m}, and that of g₀ is −2^n y^{n+1}. Hence the degree-(2n+2) parts of g₁² − ½g₀g₂ and of g₂² − g₁g₃ cancel exactly. This needs n+1−3 ≥ 1, which holds.
- *Double zeros.* At a node, T_{n−m}(cos θ) = (−1)^j cos mθ and T_{n+1−m}(cos φ) = (−1)^k cos mφ, so g_m = cos mθ cos mφ((−1)^j − (−1)^k) = 0. Products of such functions have double zeros.
- *Boundary gradient formulas.* I re-derived all of them from T_k(±1), T_k′(±1) and the node identities: E1, E2, E3, E4, and the corners (1,1), (1,−1) (n odd) and (−1,1) (n even). All agree with 313. The parity argument (Q contains only w_jw_k with j+k even, so the sign factors cancel) is correct.
- *Closed forms.* I expanded all three by hand and they agree with 313:
  - E1: A = n²(32t⁴ + (16 + 16n − 2n²)t² + 11n² − 52n + 32)/20, X = n(n+1)t(9n−40)/10, B = (n+1)².
  - E3: A = n², X = n(n+1)t(9n−31)/10, B = (n+1)²(32t⁴ + (30 + 12n − 2n²)t² + 11n² − 30n − 9)/20.
  - C11: A = n²(9n² − 36n + 80)/20, B = (n+1)²(9n² − 18n + 53)/20, X = −n(n+1)(9n² − 27n + 62)/10. Writing u = 9n² − 27n + 62 gives 4AB − X² = n²(n+1)²[9u − 81(n−1)(n−2)]/100 = 99n²(n+1)²/25.
  - In s = 1 − t²: the E1 expression is (32/5)s² + n(121n − 1040)s/100 + 99n²/100, and the E3 expression is (32/5)s² + (n+1)(121n − 919)s/100 + 99(n+1)²/100.
- *Positivity.* Drop the s² term. For E3 the endpoint values are 99(n+1)²/100 and (n+1)(11n − 41)/5, both > 0 for n ≥ 4. For E1 they are 99n²/100 and n(11n − 52)/5, both > 0 for n ≥ 5. For n = 4 the E1/E2 nodes have k ∈ {2, 4}, where the exact values are (247 ∓ 89√5)/50 = 0.960 and 8.920.

**Independent machine checks** (own code, no developer import):

- *Exact checks* (`padua_turan_check.py`, own integer Chebyshev and bivariate-polynomial arithmetic).
  - Degree: verified exactly.
  - Double zeros: verified exactly. Interior nodes of parity class r are the common zero grid of hx_r = gcd(T_n − (−1)^r, U_{n−1}) and hy_r = gcd(T_{n+1} − (−1)^r, U_n). I checked that P_n, P_x and P_y have normal form 0 modulo this Gröbner pair, and handled edge and corner nodes by exact substitution.
  - Boundary gradient formulas: verified exactly for m = 0..3.
  - PD: decided by **rigorous rational interval arithmetic** (Fraction endpoints, outward dyadic rounding at 2^−256; node enclosures of half-width 1e−45, certified by exact sign changes of U_{n−1} and U_n).
  - **Result: PASS for every n = 4..16.**
  - Minimum λ_min(Hess P_n) over nodes: 3.0587, 1.4923, 0.7990, 0.4622, 0.2846, 0.1843, 0.1244, 0.08693, 0.06253, 0.04610, 0.03473, 0.02665, 0.02079 for n = 4..16. It is always attained at the interior node (j,k) = (1,1).
  - These agree with the developer to 4 digits for n ≤ 12. The developer's floating values drift from n = 13 (3.4387e-2 against my 3.4726e-2 at n = 14), a monomial-cancellation effect.
  - Negative control: n = 3 FAILS at (j,k) = (0,2), i.e. (1,0), with λ = −225, as the developer reports. Further self-tests reject P_n + x, reject −P_n and reject g₁ on the wrong parity grid, and confirm that the interval enclosure contains the 50-digit value.
- *Symbolic checks* (`turan_symbolic.py`, n symbolic). The three closed forms and the n = 4 values reproduce exactly from my own gradient formulas.

**Nonnegativity and δ₀(n).** The route needs P_n ≥ 0 on K_{δ₀} = ∪ B̄(z_i, δ₀), not merely PD Hessians. 303(e) proves that such a δ₀ exists by Taylor's theorem, which is all N303 claims. Explicit values are new (reviewer computation). `padua_delta0.py` encloses the exact Taylor expansion at every node by intervals and certifies P_n > 0 on punctured discs of radius δ₀(n):

| n | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|
| certified δ₀(n) ≥ | 5.63e-4 | 1.02e-4 | 2.36e-5 | 6.61e-6 | 2.15e-6 | 7.87e-7 | 3.18e-7 | 1.40e-7 | 6.55e-8 |
| first sampled negative radius (MEASURED) | 3.4e-2 | 1.4e-2 | 6.6e-3 | 3.5e-3 | 2.1e-3 | 1.1e-3 | 7.5e-4 | 7.2e-4 | 3.5e-4 |

The binding node is interior (1,1) in every case. The obstruction radius therefore shrinks with n, roughly like n⁻³ in the sampled column: the obstruction holds per n, with no radius uniform in n.

**Verdicts.**

- **312: CONFIRMED** (see §2).
- **313: CONFIRMED for all n ≥ 4.** The written proof is complete. Its only open obligation, the hand check of the three expansions, is discharged here, and an independent exact rerun covers n = 4..16. **Eligible CONDITIONAL → PROVED** (developer to record, citing this review).
- **N303: CONFIRMED** for n ≥ 4 with any positive weights and ε ≤ ε₁. It holds under the explicit assumption of Padua Π_n-unisolvence (LITERATURE), which is needed so that the sections exist. Eligible for "PROVED under the stated assumption" once 313 is upgraded. Corrections L6 and L7 apply.

## 2. PD-T?…-312: interior lemma (task 2)

**Reconstructed statement.** At an interior node (0 < j < n, 0 < k < n+1), with S = sin²θ and T = sin²φ, Hess p_c ≻ 0 ⟺ 0 < cST < 1/4.

**Check.**

- *Interior gradients.* I re-derived ∂_u g_m = s[a sin mθ cos mφ + b cos mθ sin mφ] with a = −nu₁/sin θ and b = (n+1)u₂/sin φ; the factor s = (−1)^j comes from sin(jπ − mθ) and sin(kπ − mφ). At interior nodes ∂_u g₀ = 0.
- *Quadratic form.* I re-derived the AB coefficient, 2S cos 4φ − 2T cos 4θ = 2(S−T)(1 − 8ST), and the identity sin α sin β = S − T. `turan_symbolic.py` confirms the whole interior identity exactly, as Laurent polynomials in e^{iθ}, e^{iφ}.
- *Non-degeneracy.* sin α and sin β ≠ 0 because n | j would be forced, and gcd(n, n+1) = 1.
- *The equivalence holds for every real c,* not only 0 < c < 1, since the identity is polynomial in c.
- *Rigorous test of the ⟺* (both sides decided by intervals, n = 3..16, c ∈ {1/10, 1/5, 3/10, 1/2, 9/10}): agreement at **every** interior node. For c ≥ 3/10 there are genuine non-PD interior nodes, so the test is not vacuous.
- *Boundary and corner nodes* are outside 312's statement and are covered by 313 (§1).

**Verdict: CONFIRMED (PROVED).**

**Corollary (informational; strengthens R05 §5).** R05 §5 says "the κ-family cannot certify n = 3", tested at c = 0.1 and 0.2 only. It is true for every real c. At (1,0), A = 9(5c−3)/2 and 4AB − X² = 288(5c−3), so PD needs c > 3/5; but the interior node (j,k) = (1,2) needs c·(3/4) < 1/4. At n = 2 no c works either, consistent with (H) holding there (306). Log: `kappa_family_n3.log`.

## 3. PD-T?…-310 / 311: equispaced checkerboards (task 3)

**Reconstructed statement (310).** For S₀(n) = {(−1 + 2i/n, −1 + 2j/(n+1)) : i + j even} and n ≤ 7, two things hold: dim S₁ = n(n+1)/2 with the Hessian map injective, and there exist rational A_i ≻ 0 annihilating 𝓗(S₁). Hence (H) holds (303(f)) and δ* ≍ √ε (303(c),(d)), for any positive weights.

**Independent exact rerun.** My checker `equi_H_cert.py` is independent of the developer's in three respects:

- *Basis.* Chebyshev products T_a(x)T_b(y) (the developer uses monomials).
- *Exact linear algebra.* My own Fraction RREF for the jet nullspace, the Hessian-map rank and an exact basis V of null(G).
- *Proposer.* My own log-barrier method in mpmath at 40 and 60 digits (the developer uses cvxpy/CLARABEL in double).

Acceptance is exact. The certificate v = Vθ (θ rational) satisfies Gv = 0 by construction; this is asserted exactly, followed by an exact 2×2 PD test of every block.

| n | 1 | 2 | 3 | 4 | 5 | 6 | 7 | **8** |
|---|---|---|---|---|---|---|---|---|
| dim S₁ / rank 𝓗 | 1/1 | 3/3 | 6/6 | 10/10 | 15/15 | 21/21 | 28/28 | 36/36 |
| t_D (high precision; Σ tr A_i = 1) | 8.5740e-2 | 2.00489e-2 | 1.82825e-3 | 1.32648e-4 | 4.84696e-6 | 4.61511e-8 | **6.78339e-11** | **4.12459e-15** |
| exact min det/tr | 4.287e-2 | 1.002e-2 | 9.141e-4 | 6.632e-5 | 2.424e-6 | 2.308e-8 | 3.392e-11 | 2.062e-15 |
| verdict | (H) | (H) | (H) | (H) | (H) | (H) | (H) | **(H)** |

- **n = 1..7: PASS, matching the developer.**
- **n = 8 is resolved: (H) CERTIFIED** (`equi_H_cert_n8.log`). The developer's floating optimum (−1.3e-12) had the wrong sign; they correctly left n = 8 unresolved. This is a reviewer computation, not self-approved: before PROVED status for n = 8 it needs a developer record and an independent rerun of this certificate.
- **Negative control** (`equi_H_cert_negative_control.log`). For random rational square sets, the same code certifies **robust failure** of (H) at n = 4 for seeds 2 and 3. Strong duality is visible: t_D = −5.8036e-6 against λ_P = 5.8026e-6. The checker can therefore reject.

**Verdicts.**

- **310: CONFIRMED for n = 1..7.** The computer-proof rule is now met (proved reduction 303(f), exact arithmetic, committed developer checker and log, independent rerun; this review's scripts and logs must be committed). **Eligible CONDITIONAL → PROVED.**
- **311 (MEASURED): CONFIRMED WITH CORRECTIONS (L4).**
  - The double-precision t_D at n = 7 (4.5e-11) underestimates the optimum, which is 6.78e-11.
  - The decay ratios are 4.28, 10.97, 13.78, 27.4, 105, **680** and **16 400** for n = 1→8; super-geometric decay is confirmed on 8 values.
  - The "certified margin" min det/tr is ≈ t_D/2 by construction (for A ≈ tI, det/tr = t/2), so it is not a separate observation.
  - n = 8 is no longer "unresolved".

## 4. PD-T?…-314 / 315: reading (G) (task 4)

### PD-T?…-314

**Reconstructed statement.** Take run data (T_F, τ) with positive pivots, and L1's implicit completion Ĥ_J (PD-T?…-104 part 2). Then:

- (a) [Ĥ_F, Ĥ_J]e_c = 0 for deg c ≤ n−1, as an identity on the computed numbers.
- (b) (Ĥ_F, Ĥ_J) ∈ 𝒞_n ⟺ both matrices are symmetric.
- (c) The max-entry distance from (Ĥ_F, Ĥ_J) to 𝒞_n is ≥ ½·asymmetry.

**Quantifiers.** "Sections of a **functional** L̂ on Π_{2n+1} with M_n(L̂) ≻ 0", not of a positive measure. 314, the R06 table and SUMMARY item 7 state this correctly; positivity and support are a separate question (302/303).

**Proof check.**

- *(a)* is a tautology of the completion's definition: β_k Ĥ_J e_k + Σ h_l Ĥ_J e_l = T_F Ĥ_J e_p. The truncation argument is correct (Ĥ_J e_p and T_F e_p have degree ≤ n).
- *(c)* is routine.
- *(b) has a skipped step* (finding L1). "If both are symmetric, the pair is structured" is asserted without argument, and it is not automatic in floating point:
  - The completion recursion lets column (t,j) of Ĥ_J spill into rows of degree ≤ t−3, because T_F and the window terms reach one block lower each step. So Ĥ_J need not be block tridiagonal.
  - Its degree-(t+1) echelon pattern is not given by construction.
  - The step is true. Symmetry plus the upper band (rows ≤ deg c+1) gives block tridiagonality, and it also kills the block-window extras, so the "exact window" hypothesis can be dropped. 301(b)'s proof uses only block tridiagonality, symmetry, the F echelon pattern with positive pivots, and the injected (t,0)-column pattern and pivots. The J echelon pattern then follows a posteriori from 301(a) applied to L̂.

**Verdict: CONFIRMED WITH CORRECTIONS** (L1, and wording L2: R06's "dist_max(data, 𝒞_n)" concerns the completed pair, not the raw data (T_F, τ); 314(c) says it correctly).

### PD-T?…-315 (MEASURED)

**Reruns.**

1. *Developer's script.* `r06_consistency.py rot03 26` reproduces the committed log bit for bit in loss, asym_F, asym_J and comm. Only fwd_F at n ≤ 17 changes, by up to ≈ 20%, because the reference QR was edited after the log was made (disclosed in R06 §5). That change already shows fwd_F sits at the reference floor there.
2. *Own re-implementation* (`consistency_recheck.py`): own BJ recurrence, own completion, own weight Jacobian, the same node set. It adds two references: B, a full double reorthogonalisation; and **C, an 80-bit long-double CGS2 reference**. It also splits off the block-window "extra" coefficients, which are structural zeros of every consistent pair and therefore force ρ ≥ ‖e_extra‖/‖e‖.

**Results** (rotated square, my rounding realisation):

| n | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| loss | 2.8e-13 | 1.0e-12 | 3.7e-12 | 1.6e-11 | 6.0e-11 | 2.8e-10 | 1.4e-9 | 7.6e-9 | 4.6e-8 | 3.3e-7 | 2.5e-6 |
| ‖e_C‖/‖e_A‖ | 0.44 | 0.57 | 0.73 | 0.78 | 0.88 | 0.97 | 1.01 | 0.99 | 1.00 | 1.00 | 1.00 |
| ρ (reference A, as R06) | 0.79 | 0.74 | 0.68 | 0.61 | 0.50 | 0.53 | 0.60 | 0.62 | 0.55 | 0.42 | 0.37 |
| max\|η\|/w_min (A) | 1e-12 | 5e-12 | 3e-11 | 7e-11 | **2.7** | **11** | **23** | **96** | **500** | 2e3 | 2e4 |
| ρ (reference C) | 0.79 | 0.70 | 0.62 | 0.56 | 0.45 | 0.55 | **0.65** | **0.71** | **0.74** | 0.60 | 0.42 |
| max\|η\|/w_min (C) | 5e-13 | 4e-12 | 7e-11 | 8e-10 | **3e-9** | **7e-8** | **4e-6** | **1e-4** | **4e-3** | 1e4 | 5e4 |
| ‖e_extra‖/‖e‖ (C) | 0.07 | 0.07 | 0.02 | 0.03 | 0.02 | 0.01 | 0.02 | 0.03 | 0.03 | 0.04 | 0.06 |

**Interpretation of the table.**

- *The extras are not the cause.* ρ without the extras equals ρ within 0.02 under reference C.
- *The double-precision reference is inadequate.* At n ≤ 15, 22–56% of the developer-style ‖e‖ is the reference's own error. With an accurate reference the least-squares minimiser stays in the linear regime **up to n = 20**. The developer's statement "for n ≥ 16 the minimiser leaves the linear regime (max|η|/w_min = 1.8 … 1.8e7) — not an achievable fit" is, for n = 16..20, **an artefact of the reference** (finding M1).
- *The conclusion survives and is strengthened.* No first-order consistent fit removes more than ≈ 55% of the forward error, and K15 is killed in the linear regime at n = 18, 19 and 20 (ρ = 0.65–0.74 with loss ≥ 1e-9), where the developer's kill (n = 19) used a minimiser with |η|/w_min = 377.
- *Other 315 items reproduced qualitatively.* asym_J = fwd_J to printed digits; asym_F ≪ loss; comm ≤ 5.4u (K12).
- *Ranges are mis-stated against the developer's own log* (finding L3). On the rotated square, asym_J/loss = 2.2–10.2 for n = 10..26 (stated "4–10") and asym_F/loss = 0.005–0.09 (stated "0.03–0.06").

**Random square** (developer's log; finding M2). The raw F data are inaccurate (fwd_F ≈ 0.09·loss at n = 36–40) but **nearly symmetric** (asym_F/fwd_F ≈ 1.5e-3–2.4e-3). asym_J ≈ fwd_J is a property of the completion, as R06 §3a itself warns, and the only fit (n = 22..27) is at the reference floor. 315's sentence "the computed coefficients are as inconsistent as they are inaccurate", and "no Greenbaum regime seen" in 300, SUMMARY and R06, are therefore supported only on the rotated square. On the random square the near-symmetry of inaccurate F data is, if anything, a Greenbaum-like counter-indication and should be recorded as such.

**Verdict: CONFIRMED WITH CORRECTIONS as MEASURED** (M1, M2, L3). The scope is the rotated square, M = 1681, BJ/CGS, linear regime for n ≤ 20.

## 5. N304–N306 and the 306/N301 upgrades (task 5)

All three new PD-N files are genuine under the L5 rule: each is a scoped negative mathematical statement about a failed or refuted mechanism, with evidence, and none is an administrative record.

- **N304 (compression ⇏ exact section): CONFIRMED (PROVED)** via 308 and N301, as a failed route (ii). Correction L5: 308's ρ(δ) bounds ‖Ĥ − H‖ in a matrix norm, whereas ‖E‖ is the functional norm. The combination needs ε < min(ρ(δ)/L_Φ, ε₁), with L_Φ the local Lipschitz constant of Φ (301(c)), not ε < min(ρ(δ), ε₁).
- **N305 (C1 fails, n = 2..12): CONFIRMED as MEASURED.** It is a legitimate failed-candidate PD-N; I did not rerun it. The n = 2 entry is automatic, because (H) holds at n = 2 (306), so no failure certificate of any kind can exist there.
- **N306 ((H) not decided by the count): CONFIRMED.** The refutation of IDEA 311's hypothesis now rests on an exact equispaced n = 3 certificate with two independent checkers (§3), so the **negative statement can be PROVED**. The survey parts (graded checkerboards, sorted-uniform sets) stay MEASURED. Label the parts separately or split.
- **306 and N301 (CONDITIONAL → PROVED at 23:54): rule-compliant.** The proved reductions are 303(f) and 303(e). Arithmetic is exact. The developer's checker and log are committed. Review 01's independent rerun scripts and logs were committed at `fefeaa1` (23:40:30), before the upgrade. The L1 quantifier fix (ε ∈ (0, ε₁] with M_n(L_μ+E) ≻ 0) is correctly applied in 303(e), N301, N303 and N304. Gaps: the trusted dependencies are not listed (L10), and stale text remains (L9).

## 6. Response quality (task 6)

Every finding of review 01 has a row in response-recon-01. I checked each claimed fix in the files.

**Applied with History lines:** M1, M2, L1–L7, L11–L13, 304(a) and N302. I found no silent narrowing. No status was upgraded without an independent rerun.

**No backdating detected.**

- Nine History stamps read exactly 23:54:00. They look rounded rather than `date -Iseconds` output, but they fall between the review commit (23:40:30) and the commits that contain them (23:57:24, 23:58:40).
- M3 is answered honestly: R01–R03 are disclosed as not pre-registered.
- For R04, pre-registration *is* evidenced: the criteria were committed at 23:09:09 and the log at 23:12:48.
- For R05 and R06, the criteria were committed **together with** their deciding logs, so "written before the runs" rests on self-reported file times.
- R06 §5 omits the first, partial weight-fit run (rows n = 14–18, committed with K15 at 23:29:33) (L12).

**Residuals.**

- *Original wording not kept.* The History lines in 302 (M1, M2) give the change and the reason but not the original wording (L11).
- *Stale text after the upgrades* (L9). Not updated:
  - 306 Checks ("registry status stays CONDITIONAL until an independent rerun");
  - N301 "Not covered: n ≥ 4 (MEASURED only)";
  - IDEA 307 disposition ("CONDITIONAL on independent rerun", "MEASURED failure n = 4..7");
  - 300's overdetermined row still says "Π_{2n+1}-unisolvent" (an L11 residual);
  - 307 item 6 "equispaced … n = 6 unresolved": R04's pending correction was never applied, although 307 was edited at 23:54;
  - plan.md ledger row R01 "Literal reading trivial" (the orchestrator's file; an M1 residual).
- *L10 recurs.* The R06 hypotheses A (K13, killed), B (K14) and C (K15, killed) have no IDEA records, and the two refuted ones have no PD-N (L8).

## 7. Independent reruns

All commands are run from `tracks/bivariate-lanczos/code/review_L3b/`. Logs are in `topics/bivariate-lanczos-20261031/reviews/logs_L3b/`.

| Command | Log (sha256 prefix) | Result |
|---|---|---|
| `python3 -I -B padua_turan_check.py 3 16` (37 s) | `padua_turan_check.log` (974b306e) | P_n: degree, exact double zeros, exact boundary gradients, rigorous PD all PASS for n = 4..16; n = 3 FAIL (−225); 312 ⟺ agrees at all interior nodes |
| `python3 -I -B turan_symbolic.py` | `turan_symbolic.log` (e1170b52) | 312 identity exact; 313 E1/E3/C11 closed forms equal the developer's (n symbolic) |
| `python3 -I -B padua_delta0.py 4 12` (75 s) | `padua_delta0.log` (885c063a) | rigorous δ₀(n) table of §1 |
| `python3 -I -B kappa_family_n3.py` | `kappa_family_n3.log` (14f6dbed) | no c certifies n = 2, 3 |
| `python3 -I -B equi_H_cert.py 1 7 40` (12 min) | `equi_H_cert_n1_7.log` (60ad0a14) | (H) certified exactly n = 1..7 |
| `python3 -I -B equi_H_cert.py 8 8 60` (16 min) | `equi_H_cert_n8.log` (ae2467e5) | (H) certified exactly n = 8 (new) |
| `python3 -I -B equi_H_cert.py 3 4 30 randrat 1,2,3,4` | `equi_H_cert_negative_control.log` (9194f7af) | robust failure certified (seeds 2, 3, n = 4) |
| `cd ../L3 && python3 -B r06_consistency.py rot03 26` (developer code) | `dev_r06_consistency_rot03_rerun.log` (7c9fa7e5) | bit-identical except reference-dependent fwd_F |
| `python3 -I -B consistency_recheck.py rot03 12 19`, then `… 20 22` | `consistency_recheck_rot03.log` (98d62813), `consistency_recheck_rot03_n20_22.log` (bcac5a9d) | §4 table (an earlier n = 10..20 run without reference C was overwritten; its ρ_all and extras columns agreed) |

**Script sha256.**

| Script | sha256 |
|---|---|
| `rigorous.py` | `de764cc6b955aa7e68bf6838f5c4e715bfbe1d8a5cf384879ecf3a321ae2085a` |
| `padua_turan_check.py` | `c1896577dcf9683b75e1ffa6ea481f1c498107ce482df97381e8462c0fe108ff` |
| `turan_symbolic.py` | `495ae2f488daf835d9f24f18aabcd7671dd5c01dc743b83d5adac200db89fd5d` |
| `padua_delta0.py` | `f096ea84d13475b6389628fca7880132e391ad5f6a31f0a393e6e93486ec215b` |
| `kappa_family_n3.py` | `30826747a3085c9965aed90009368333f2116e710e5180581c8cfb3f3d1e4aa1` |
| `equi_H_cert.py` | `324ddfa83348f6ee90af8847e84587b4d654eff9977383b1a8c9cfcbda9f4d33` |
| `consistency_recheck.py` | `635766a9a1448ea9bb529b805144368fe09eef3055420d46cd08173cdcae4bbb` |

Note on versions: the n = 1..7 and n = 8 runs used `equi_H_cert.py` before the `randrat` option was added; that edit only added the option and changed nothing on the equispaced path. `consistency_recheck.py` is the final version, with reference C.

**Trusted dependencies:** Python `fractions`/ints (all exact checks), sympy (symbolic checks only), mpmath (the proposer only; acceptance is exact), numpy (MEASURED parts only).

## 8. Findings by severity

**High: none.** No claim was refuted.

**Medium**

- **M1 (315 item 4; R06 §4; 300 (G) row).** In the rotated-square weight fit the double-precision reference error is comparable to the forward error at n ≤ 15. The "minimiser leaves the linear regime for n ≥ 16" narrative is therefore an artefact: with an 80-bit reference the minimiser is linear up to n = 20, with ρ = 0.45–0.79. Fix: use an extended-precision reference, restate item 4, and record K15 as killed in the linear regime. The conclusion is unchanged and stronger.
- **M2 (315 Statement; SUMMARY §1; 300).** "As inconsistent as they are inaccurate" and "no Greenbaum regime seen" overreach on the random square, where the inaccurate F data are nearly symmetric and the fit is inconclusive. Restrict the claim to the rotated square and record the counter-indication.

**Low**

- **L1.** 314(b) proof: justify "symmetric ⇒ structured" (spill, J echelon pattern, extras); see §4.
- **L2.** R06 "dist_max(data, 𝒞_n)" should read "(Ĥ_F, Ĥ_J)".
- **L3.** 315 ranges (2.2–10.2; 0.005–0.09).
- **L4.** 311 values: t_D(7) = 6.78e-11; ratio 680; margin ≈ t_D/2; n = 8 resolved.
- **L5.** N304: ε < ρ(δ)/L_Φ.
- **L6.** N301/N303 example "E = −ε ev_ζ" needs normalisation (‖E‖ = ε‖ev_ζ‖), as in 303(e).
- **L7.** N303/313: state that δ₀(n) → 0 with n (reviewer bounds for n ≤ 12 can be cited as a reviewer computation).
- **L8.** Missing IDEA/PD-N records for the R06 hypotheses A and C (and B): L10 of review 01 recurs.
- **L9.** Stale text after the upgrades (§6 list).
- **L10.** 306/N301 do not state their trusted dependencies.
- **L11.** History lines do not preserve the original wording (302).
- **L12.** R05/R06 pre-registration rests only on self-reported times; R06 §5 run record incomplete.
- **L13.** 313 Checks "No independent rerun yet" and N305's "n = 2" entry: update or annotate.

**Informational (positive).**

- 312 holds for all real c.
- 313 is hand-verified (every expansion and gradient formula) and exactly verified for n = 4..16.
- Rigorous explicit δ₀(n) bounds for n ≤ 12.
- 310 is independently certified for n ≤ 7, and **equispaced n = 8 is now certified**.
- The κ-family's failure at n ≤ 3 is proved for every c.
- The developer's R06 script reproduces its log bit for bit.

## 9. Remaining uncertainty

- **Trusted code.** My exact checks trust Python big-integer and Fraction arithmetic and my own interval and RREF code. Self-tests and negative controls passed, but no second person has run these scripts. The equispaced n = 8 certificate and the δ₀(n) bounds are reviewer computations and need an independent rerun before they are cited as PROVED.
- **Unisolvence.** Padua unisolvence for all n is LITERATURE and was not re-verified here. N303's content depends on it.
- **315 scope.** My replicate uses a different rounding realisation from the developer's run (loss differs by a factor of 1.5–4 at equal n), so it supports the qualitative picture, not their digits. HL/ORTH, O(1) loss and larger M remain untested. Reading (G) is OPEN.
- **Hand checks.** Statements checked by hand rather than machine (312's trig derivation, 313's boundary gradient formulas for general n, and 314's argument) carry the usual "no gap found ≠ guarantee" caveat.

## 10. Requested dispositions (orchestrator or AC; the reviewer approves nothing beyond this scope)

- **313: CONDITIONAL → PROVED; N303 → PROVED under the stated Padua-unisolvence assumption.** The developer records the History line, cites this review, and applies L6/L7.
- **310: CONDITIONAL → PROVED for n ≤ 7**, once this review's scripts and logs are committed. Equispaced n = 8 may be cited as a reviewer computation pending an independent rerun.
- **N306:** the refutation part → PROVED; the survey parts stay MEASURED.
- **314:** stays PROVED after the L1 proof addition.
- **311, 315:** stay MEASURED with the corrections L4, M1, M2 and L3.
- **N304:** stays PROVED with L5.
- **N305:** stays MEASURED.
