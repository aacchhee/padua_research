# L3 independent adversarial reconstruction 01

## Header

- Auditor: Claude Opus 5.5, effort xhigh (as assigned; the runtime does not expose effort). Role: independent adversarial reconstructor for direction L3. I did not develop this work. I changed no Git state; I wrote only this file, `tracks/bivariate-lanczos/code/review_L3/*` and `topics/bivariate-lanczos-20261031/reviews/logs_L3/*` (48 KB).
- Rules read: `AGENTS.md`, `agents/WORKFLOW.md`, `agents/claude/CLAUDE_ROLES.md` (§Independent audit), at branch `claude/bivariate-lanczos-20261031`.
- Audited candidate: branch head at audit start **`0b7b396b9021804074f6e1fd36bc342026dbd1b7`**. The head advanced while I worked (to `f9bb09990f7c039388320cd9d0cb92ddd2863b03` at the time of writing) with new L3 work: R04–R06, PD-T?…-310–313, PD-N?…-303, and the `exact_checkerboard.py` / `r05_*` / `r06_*` scripts. That work is **not audited here**. `git diff 0b7b396..f9bb099` shows that none of the audited theory files, R01–R03, `lit_reading.md` or the audited L3 scripts changed. `candidates.md` and `plan.md` only gained appended material (IDEA 312/313, a "Pending corrections" list, ledger rows, ID-range text). I audited both at `0b7b396`.
- sha256 of the audited theory files (`tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-*.md`): 300 `83e0d4407a07893df81353659335f3ca68b130c5d3709f6e09f2c0115d4342c4`; 301 `d20e1d2fc1b19084654cbacb725c2bb6ed74d5aa177d06d48f63c330eb47c480`; 302 `9b2263ad1c4f151caf03eab4d11d39b191a9045191cd1af52bff41fe59027c9f`; 303 `cc6f979cff17614a4233d45927f4c52617ad9d757f2b27ff1d74d7bccd923c59`; 304 `0b50c6aefd3e60b45cc836ad51868a9b19edee4ede55941cd4228098cc52d704`; 305 `52f5ddda0bad49b102da6637a6b58428a881c0be2eb2863ca7cbf8682cd9ce48`; 306 `970d41f182fe11d848d042f16894f55b1db0d0173aae00004659e0f5d6f3c007`; 307 `9367e3be3a19d5bc937f06906c6f9acf254de2e5eabb45c5eaf6fbd96b859701`; 308 `59be05e16c06d18efd37475849449fa33e6999c976a9d5e3275329512ae5cc38`; 309 `db55c7bf9ae72e7650603fa1cbab94aa31e1cdec9bac1b8ac804035e5d7fb47d`; N301 `bd8fc3991df5c2b524aeb21a7ad53e968dc85a7e97865cec8a4e3cedf99581c1`; N302 `b5b26d4e326d1c6a5d787e8180d9c7c03cf710979c17d230d324f182332b7925`.
- Developer code: all ten L3 scripts match `directions/L3/logs/code_sha256.txt` (`sha256sum -c`: all OK). `exact_certificates.py` = `752188b6f537f38b7dfba2fb4f5cf37cf39661b7fbc4fc924c3968347fcee6c5`. The certificate log `exact_certificates.log` = `287e8dd0bdaa60d93d728045fcd47c5c75832813657f4849081fe4b1e0629e8b`.
- Read coverage, in full: AGENTS.md; WORKFLOW.md; CLAUDE_ROLES.md; plan.md (notation, frozen L3-Q1, ledger, History); directions/COMMON_RULES.md; L3 BRIEF, STATUS, R01, R02, R03, candidates.md, lit_reading.md; **state/IDEAS.md complete** (144 lines in three chunks: 48 seed rows, OBST-01..15, the disposition table); theory 300–309, N301, N302; all ten L3 scripts (`exact_certificates.py`, `l3lib.py`, `hess_condition.py`, `hs_checkerboard_condition.py` and `lp_rate.py` line by line; the others skimmed); all L3 logs relevant to the claims.
- Read in part: LOG.md (the L3 entries); the L1 theory file `window-coefficient-pattern-exact.md` (part 4); `literature/INDEX.md` (the rows for Greenbaum, Kachkovskiy–Safarov, Koiran, Curto–Fialkow and Šimonová–Tichý).
- Not read: baseline-candidates.md in full; the literature record files; any post-`0b7b396` L3 material.
- Environment: Python 3.13.18, numpy 2.5.3, scipy 1.18.1 (HiGHS), sympy 1.13.3, cvxpy 1.6.0 (CLARABEL), 2 cores. arxiv.org is blocked for curl by the session proxy (policy 403, not retried), so the literature was read through WebFetch.

## 1. Scope decision (task 1)

**Is the literal L3-Q1 trivial?** Only under an added hypothesis. The frozen hypothesis is: "computed sections that satisfy the exact structural zero pattern and the recurrence relations up to O(ε)". It does not say that Ĥ is close to Φ(μ). That leaves three readings:

- **(i) Relations on the sections alone.** If "recurrence relations" means relations on the sections alone (the only ones that can be stated without Q̂, i.e. interior commutativity), the hypothesis does not tie Ĥ to the nodes. The literal question is then trivially **negative**: Ĥ = Φ(ν) for any positive measure ν far from the nodes satisfies every relation exactly, and no μ′ near the nodes has sections within O(ε) of it.
- **(ii) Forward accuracy.** If forward accuracy is added (‖Ĥ − Φ(μ)‖ = O(ε)), the literal question is trivially **positive** with μ′ = μ. This is 302(c), and it is correct.
- **(iii) Local relations with the computed basis.** If the relations are the local relations X Q̂ = Q̂ Ĥ_x + … + F with the computed Q̂, the question is the Greenbaum regime (G). That is the content the words "Greenbaum-type backward interpretation" point to, since Greenbaum's theorem is about computed tridiagonals that are *not* forward accurate.

So "read literally, L3-Q1 is trivial" (plan History; R01 §3; LOG line 70, "Scope decision: literal L3-Q1 trivial") is an **overstatement**. Only the forward-accurate sub-reading is trivial.

**Is the exact reading (E) faithful?** It is an openly recorded **substitution**, not a weakening and not the frozen question. It strengthens the conclusion (exact representation, or residual < θε with θ < 1, instead of "up to O(ε)"). It narrows the hypothesis to forward-accurate, exactly consistent data. Its positive results (overdetermined δ = 0; square case δ ≍ √ε under (H)) imply the trivial literal answer. Its obstruction (N301) answers only the strengthened question; under literal "up to O(ε)" with constant ≥ 1, μ itself works. The theory files say this correctly (N301 "Not covered: residuals as large as the perturbation"). The [IDEALIZED: perturbations given as data] tag and the plan's kill-test wording ("admitting no representing measure") support (E) as a legitimate, non-trivial companion reading. One point in its favour: for the worst-case direction E* (the norming functional of p*/‖p*‖_*), dist(L_μ + E*, C(K_δ)) = ε exactly for δ ≤ δ_0. Nothing then beats the trivial representation, so "residual strictly smaller than the perturbation" is the right threshold for (E).

**Is (G) correctly left OPEN?** Yes. PD-T?…-300 is OPEN (not PARTIAL), (G) is listed as OPEN in every round record and next-question list, and nothing in the R01–R03 material silently drops it. Because (G) is the regime the frozen question is really about, the topic-level summary must not present L3-Q1 as "answered" or "made precise" without the qualifier "in reading (E)". STATUS R01 ("L3-Q1 made precise") and the plan History both need that qualifier (finding M1).

## 2. Per-claim reconstruction and verdicts

### PD-T?…-301 (truncated Favard): CONFIRMED for (a)–(c); CONFIRMED WITH CORRECTIONS for (d)

**Reconstructed statement.** Fix the graded order (degree, then x-exponent ascending; this is a monomial order). Structured symmetric pairs (block tridiagonal, echelon off-diagonal blocks with positive pivots) whose commutator vanishes outside block (n,n) are in bijection with functionals L on Π_{2n+1} with L(1) = 1 and M_n(L) ≻ 0. The inverse is the words formula. 𝒞_n is an analytic submanifold of dimension (n+1)(2n+3) − 1.

**Proof check.** I re-derived the proof line by line.

- (a): the echelon pivots equal c_{(k,s)}/c_{(k+1,s+1)}. The commutator rows with deg a ≤ n−1 vanish because x p_a, y p_a ∈ Π_n and the products have degree ≤ 2n+1.
- (b): for a transposition inside a word of length ≤ 2n+1, |U| + |V| ≤ 2n−1, so one of the two sides has degree ≤ n−1. π is well defined because |V| ≤ n−2. Triangularity uses the H_x pivots for s ≥ 1 and the H_y pivot for s = 0. For uniqueness, every monomial of degree ≤ 2n+1 has the form x^α x^β or x^α·(x or y)·x^β with |α|, |β| ≤ n.
- (c): Φ⁻¹ is polynomial and Φ⁻¹∘Φ = id, so Φ is an injective immersion with a continuous inverse, i.e. an embedding.

**Numerical check.** In a Legendre basis (`indep_measured.py favard 4`), for n = 1..4, for a measure and for a signed functional: low commutator rows ≤ 9.3e-16 while the last block is O(10⁻¹); words-formula relative error ≤ 3.3e-16; echelon pattern and pivots as stated.

**Count (d).** The counts e_n = 1, 6, 17, 36, 65, 106, 161, 232, 321, 430 reproduce independently. Correction L4: the count assumes that B_{n,x} and column (n,0) of H_y are formed, i.e. that the products of the degree-n vectors are computed (half of the step to degree n+1). L1's PD-T?…-101(4) states that a degree-n run forms only the F-columns of S_{n−1}. Under that convention the formed entries determine L only on Π_{2n}, and the excess differs (by my count e′_1 = 0, e′_2 = 2). The convention should be stated in 301(d).

### PD-T?…-302 (reduction): CONFIRMED WITH CORRECTIONS

**Reconstructed statement.** (a) For Ĥ ∈ 𝒞_n: exact sections of a positive measure on K_δ = ∪ B̄(z_i, δ) ⟺ L̂ ∈ C(K_δ) ⟺ L̂ ≥ 0 on Pos(K_δ) ⟺ a positive cubature of degree 2n+1 with nodes in K_δ. At most dim Π_{2n+1} atoms are needed. (b) B(L_μ, ε) ⊂ C(K_δ) ⟺ r(δ) ≥ ε. (c) The literal reading is trivial under forward accuracy.

**Proof check.**

- Closedness: {ev_z : z ∈ K_δ} is compact and misses 0 because ev_z(1) = 1. Carathéodory for cones gives the atom bound. Bipolar duality gives (ii)⇔(iii). For (i)⇒(ii) with a non-atomic μ′, duality plus closedness suffices; Tchakaloff is not needed and is not cited.
- (b): ‖·‖_* is the predual norm. A norming functional exists by Hahn–Banach. The bound dist ≥ ε − r(δ) is correct. Monotonicity of r and the δ* threshold are correct.

**Corrections.**

- **M2. The residual definition is wrong as written.** The Definitions say "up to residual θε = ‖L_{μ′} − cL̂‖ ≤ θε for some c > 0". With c free this is always satisfiable: take μ′ = cμ, so the residual is c‖E‖ → 0. The residual clause of (b), and the "residual ≤ θε" scope text in N301/N302, are therefore vacuous or false as written. The intended statement holds with c = 1, or with normalised functionals, and the proofs use c = 1. Fix the definition.
- **M1.** Part (c) and the History wording "literal reading is trivial" need the forward-accuracy hypothesis stated (see §1).
- Part (d) is fine (routine).

### PD-T?…-303 (rate theorem): CONFIRMED (minor corrections)

**Reconstructed statement.** Let S_0 be the polynomials in Π_{2n+1} vanishing at the nodes, and S_1 those also with vanishing gradient. Let (H) be: no nonzero p ∈ S_1 has PSD Hessians at all nodes.

- (a) S_0 = {0} ⇒ r(0) ≥ w_min σ_1.
- (b) S_0 ≠ {0} = S_1 ⇒ r ≍ δ.
- (c) S_1 ≠ {0} ⇒ r ≤ Cδ².
- (d) (H) ⇒ r ≍ δ².
- (e) A p* ∈ S_1 with PD Hessians at all nodes ⇒ r = 0 on [0, δ_0].
- (f) (H) ⟺ the Hessian map is injective on S_1 and there are PD A_i annihilating S_1.

All constants depend on (z, w, n, ‖·‖).

**Proof check.** I re-derived every step:

- (I) 0 ≤ p(z_i) ≤ η/w_min.
- (II) |∇p(z_i)| ≤ p(z_i)/δ + C_2δ/2.
- (III) The even Taylor expansion gives uᵀHu ≥ −2p(z_i)/δ² − C_4δ²/12.
- (d): ‖p_W‖ ≤ C″δ, with C″ bounded for c ≤ 1. Then κ(1 − C″δ) ≤ 2c/w_min + O(δ), a contradiction for c < κw_min/4. κ > 0 by compactness of the unit sphere of S_1. The case p_S = 0 is excluded for small δ.
- (e): p*(z+h) ≥ ½λ|h|² − (C_3/6)|h|³.
- (f): separation of the subspace U^⊥ from int PSD^M.

The degenerate PSD-singular subcase is correctly excluded and listed as open.

**Small corrections.**

- L1: in (e) and N301, "for every ε > 0" should be restricted to E with M_n(L_μ + E) ≻ 0 (automatic for small ε); otherwise Φ(L_μ + E) is undefined.
- L11: "Π_{2n+1}-unisolvent" for M > dim Π_{2n+1} means "determining" (S_0 = {0}).
- L13: "Within δ" means supp μ′ ⊂ K_δ, not Hausdorff distance. The obstructions are therefore stated under the weaker requirement, which makes them stronger. For the existence results, Hausdorff ≤ δ also follows for small ε (mass ≈ w_i near each node, via the Π_n Lagrange basis); this is worth one sentence.
- L12: the frozen question asks for an "explicit δ(ε)". In the square case only the rate is explicit; c and C come from compactness (303 Open item 2).

### PD-T?…-304: (a), (b) CONFIRMED; (c) CONFIRMED WITH CORRECTIONS

**(a)** The barycentre surrogate is a valid construction. The first-order Taylor terms cancel, giving ‖L_{μ′} − L_{μ̃}‖ ≤ Cμ′(K)δ². One step needs adding: the hypothesis "Φ(μ′) close to H" forces the cluster masses W_i ≈ w_i > 0 (Lagrange-basis argument). That makes μ̃ an N_n-point Π_n-unisolvent measure with κ = 0; otherwise μ̃ could have missing atoms. With that, a Lipschitz bound on normalised functionals applies.

**(b)** Bauer–Fike for normal N; cyclicity of e_0 from π(Π_n) = ℝ^N; Gram–Schmidt in the eigenbasis returns Vᵀe_a. Correct.

**(c), finding L3.** The proof shows only that d(κ∘Φ) vanishes on T (so it factors through V*/T ≅ S_1*). It does not show that the induced map is an isomorphism, which is what "κ is, to first order, the S_1*-component" asserts. Measured (`indep_measured.py dkappa 2|3`): rank n(n+1)/2 for Padua n = 2 (singular values 4.94, 3.33, 3.12) and n = 3 (9.41 … 2.11). Along T, |dκ| ≤ 4.2e-11. Label the isomorphism part MEASURED, or prove it.

### PD-T?…-305 (n = 1): CONFIRMED

The Bézout argument checks line by line. For abᵀ + baᵀ with a, b independent, the eigenvalues a·b ± |a||b| have opposite signs. Exact check for Padua n = 1: S_1 = span(ℓ12ℓ13ℓ23), and det Hess < 0 at all three nodes (`indep_exact_check.py`).

### PD-T?…-306 (Padua n = 2, √ε): CONFIRMED; eligible to move CONDITIONAL → PROVED

The finite reduction (303(f), then 303(c),(d)) is proved. My independent exact rerun, using sympy QQ<√2> plus my own sign test with a rational-enclosure cross-check, recomputes S_1 exactly: rank J = 18, dim S_1 = 3, rank of the Hessian map 3. It verifies Σ_i⟨A_i, Hess p(z_i)⟩ = 0 for every basis element of S_1, with the developer's six rational A_i read as data from the log, and A_i ≻ 0 exactly, with min λ_min(A_i) ≥ 0.015199 (**PASS**). Cross-check with 309(b): Σ_i G_iA_iG_iᵀ is exactly Hankel (`hankel_crosscheck.py`).

All four workflow requirements are now met: a proved finite reduction, exact arithmetic, a committed checker and log, and an independent rerun.

### PD-T?…-307 (MEASURED): CONFIRMED as MEASURED within scope, with wording corrections (L5)

**Independent reruns.** These use a different basis (Legendre), a different primal normalisation (Σ tr Hess = 1) and different LP grids.

| Family | Reviewer result | Developer result |
|---|---|---|
| Padua | (H) holds for n = 1, 2 (t_D = 0.0857, 0.0152); robust failure for n = 3..7 (λ_P > 0, t_D ≤ −6.9e-4) | identical t_D |
| Equispaced checkerboard | t_D = 0.0201, 1.83e-3, 1.33e-4, 4.85e-6 for n = 2..5; n = 6 unresolved | same |
| Graded checkerboard | (H) for n ≤ 4; n = 5 unresolved | same |
| Random, seed 1 (same RNG stream) | (H) for n = 1, 2; failure for n = 3..6 | same |
| LP, Padua n = 2 | δ_min/√ε = 0.054, 0.050, 0.049 (ε = 1e-2..1e-4) | 0.054 |
| LP, Padua n = 1 | 0.214, 0.195, 0.192 | 0.191 |
| Grid residual, Padua n = 3 | residual/ε ≈ 0.011–0.015 (Legendre ℓ1) for δ ∈ {0.003, 0.02, 0.04, 0.1} | 0.023–0.035 (Chebyshev ℓ1; the norm differs) |

**Exact upgrade.** S_1 = {p_C : C ⊥ Hankel} holds *exactly* for Padua n = 1, 2, 3 (rank of C ↦ p_C equals dim S_1; `indep_generator_cert.py`). This upgrades 307 item 5 for n ≤ 3.

**Wording corrections (L5).**

- Item 2 says "n = 4..6: fails for all seeds", yet two of the nine cases are marginal (seed 3 n = 4: λ_P = 8.2e-7; seed 2 n = 5: t_D = −3.1e-7). The R01 table ("fails n ≥ 4 (3 seeds)") overstates this.
- Item 6 labels sorted-uniform draw 1 at n = 6 a robust failure with λ_P = 2.1e-6, which sits at the 1e-6 threshold.
- Item 4: "n = 3 residual never 0" is a grid statement. The grid minimum is an *upper* bound on the true minimal residual over K_δ, so for δ beyond the certified positivity radius (now 0.04) a nonzero grid residual is not evidence of non-representability.

### PD-T?…-308 (compression model): CONFIRMED

The trace-pairing interior-point argument checks: an affine φ_i that is ≥ 0 on a ball and 0 at its centre vanishes identically, so F(z)r_i = 0, and three affinely independent points give F r_i = 0. The rows r_i span ℝ^N because Q is square orthogonal. The Naimark dilation step is correct.

### PD-T?…-309 (generator form): (a), (c) CONFIRMED; (b) CONFIRMED WITH CORRECTIONS

- (a): the top form vanishes when the anti-diagonal sums are zero; Hess p_C = 2G_iᵀCG_i; dim = (n+2)(n+3)/2 − (2n+3) = n(n+1)/2.
- (c): checked by hand (sin nθ = sin(n+1)φ = 0, cos nθ = cos(n+1)φ = s) and exactly for n = 1, 2, 3: the generators vanish, the top forms are right, and the interior-gradient formula holds at the 0, 1 and 3 interior nodes (`indep_generator_cert.py`). Padua unisolvence, the LITERATURE dependency, was verified exactly for n ≤ 4 (`unisolvence_check.py`).
- **L6.** In (b), "(H) ⟺ ∃A_i ≻ 0 with ΣG_iA_iG_iᵀ Hankel (and the Hessian map is injective)": injectivity must be a conjunct on the right-hand side, not a parenthetical consequence.
- **L7.** The status "PROVED with LITERATURE dependency" should read "PROVED under the stated assumption (Padua unisolvence)". It is not load-bearing for N301.

### PD-N?…-301 (Padua n = 3 obstruction): CONFIRMED; eligible to move CONDITIONAL → PROVED; δ_0 can be improved

**Reduction, line by line.**

- p* ∈ Π_7 = Π_{2n+1}.
- p* ≥ 0 on K_{δ_0}, so L_{μ′}(p*) ≥ 0 for every positive μ′ on K_δ with δ ≤ δ_0.
- (L_μ + E)(p*) = E(p*) < 0.
- If Φ(μ′) = Φ(L_μ + E), then 301 uniqueness forces L_{μ′} = c(L_μ + E) with c > 0, a contradiction.
- The distance bound follows from 302(b).

The reduction depends only on p*'s properties, so it holds for any positive weights. It needs M_3(L_μ + E) ≻ 0, hence the quantifier fix L1.

**Exact rerun (independent code).** p* (read as data from the log) has 20 rational monomials, total degree 7 and is even in y. p*(z_i) = 0 and ∇p*(z_i) = 0 exactly at all 10 nodes. Hess p*(z_i) is PD exactly at all 10 nodes, with min λ_min ≥ 0.112782. Exact S_1: rank J = 30, dim S_1 = 6, rank of the Hessian map 6.

**Rigour of δ_0.** I read the developer's bound and it is valid: λ_min ≥ det/tr, rational enclosures of √2, and a third-derivative coefficient bound on |x|, |y| ≤ 1.1 that contains the balls. My own bounds:

1. A full exact Taylor expansion with a coefficient-sum bound on each homogeneous part certifies radius 0.00235 ≥ 3.89e-4. Hence the developer's δ_0 = 30117029139000/77370908310949543 is confirmed.
2. Rigorous rational interval arithmetic on q(r,s) = p*(z + r v)/r² over the boundary of the direction square proves **p* > 0 on punctured discs of radius 0.04 at all 10 nodes**.

The interval code was validated by required failures: it rejects −p*, and it rejects radius ≥ 0.06 at the nodes (−1, ±√2/2), where sampling gives min p* = −2.5e-5 at radius 0.06 and +1.2e-5 at 0.05.

**Second, independently derived certificate.** Built from the 309 generator form, it uses a rational C ⊥ Hankel (in the log), has G_iᵀCG_i ≻ 0 exactly at all 10 nodes with min λ ≥ 0.199, p_C ∈ S_1, degree 7, and is positive on punctured discs of radius 0.02. **PASS.**

**Developer rerun.** `python3 -B exact_certificates.py` gives output byte-identical to the committed log (sha256 `287e8dd0…`).

### PD-N?…-302 (no δ = O(ε) in the square case): CONFIRMED

S_1 ≠ {0} because dim Π_{2n+1} − 3N_n = n(n+1)/2. With δ_ε = (ε/C)^{1/2}/2, r(δ_ε) ≤ ε/4 < ε. The norming functional of the minimiser then gives a consistent perturbation (M_n ≻ 0 for small ε) with no representing measure supported in K_{δ_ε}. "Atom" should read "support point" for non-atomic measures.

### PD-T?…-300 (target): status OPEN CONFIRMED

The mixed parts (PROVED, CONDITIONAL, MEASURED, OPEN) correctly prevent PARTIAL. The framing corrections are M1 (§1) and L9 below.

## 3. Independent reruns (commands and outputs)

All commands run from the repository root unless noted. The scripts are in `tracks/bivariate-lanczos/code/review_L3/`; the logs are in `topics/bivariate-lanczos-20261031/reviews/logs_L3/`. No developer module is imported; developer certificates are read as data from the log.

| Command | Log (sha256 prefix) | Result |
|---|---|---|
| `python3 -I tracks/bivariate-lanczos/code/review_L3/indep_exact_check.py topics/bivariate-lanczos-20261031/directions/L3/logs/exact_certificates.log` (80 s) | `indep_exact_check.log` (2c2aded4) | n = 1, 2 dual certificates PASS; n = 3 p* PASS; radii as in §2 |
| `cd tracks/bivariate-lanczos/code/L3 && python3 -B exact_certificates.py` | `dev_exact_certificates_rerun.log` (287e8dd0, identical to the developer log) | byte-identical |
| `cd …/review_L3 && python3 -I -B indep_generator_cert.py` (36 s) | `indep_generator_cert.log` (cbedab3c) | 309(a)–(c) exact for n ≤ 3; second n = 3 certificate PASS |
| `python3 -I -B hankel_crosscheck.py <dev log>` | `hankel_crosscheck.log` (ba4d8303) | Σ G_iA_iG_iᵀ is Hankel for n = 1, 2 |
| `python3 -I -B unisolvence_check.py` | `unisolvence_check.log` (a1e21ecb) | Padua n = 1..4 unisolvent (exact Vandermonde rank) |
| `python3 -I -B indep_measured.py favard 4` | `indep_favard.log` (a3c0394a) | 301 numeric; e_n counts |
| `python3 -I -B indep_measured.py dkappa 2`, `… dkappa 3` | `indep_dkappa.log` (83f8ea74) | dκ rank n(n+1)/2; zero along T |
| `python3 -I -B indep_measured.py H padua 7 0`; `H equi 6 0`; `H random 6 1`; `H graded 5 0` | `indep_H.log` (925e8040) | as in §2 (307) |
| `python3 -I -B indep_measured.py lp 2 1e-2,1e-3,1e-4 0.03`; `lp 1 1e-2,1e-3,1e-4 0.3`; `resid 3 1e-3 0.003,0.02,0.04,0.1 0.03` | `indep_lp.log` (81beed39) | √ε laws; n = 3 grid residual > 0 |
| `python3 -I -B padua_n4_generator_cert.py` (4 s; beyond the audited scope) | `padua_n4_generator_cert.log` (0b8df797) | **Padua n = 4: exact obstruction certificate.** Rational C ⊥ Hankel (6×6; in the log) with G_iᵀCG_i ≻ 0 exactly in Q(√2)(√5) at all 15 nodes (float min λ 0.0743); p_C of degree 9 with exact double zeros. By 303(e) there is no δ(ε) → 0 at Padua n = 4. This is a reviewer computation, not self-approved; it independently supports the post-audit PD-N?…-303 case n = 4. |

Script hashes: `indep_exact_check.py` 989ed4e1…; `indep_generator_cert.py` d5483c0c…; `indep_measured.py` 39a6e445… (the `favard`, `H` and `lp` logs were produced by this final version; `dkappa` ran under an earlier revision whose dkappa path is unchanged); `hankel_crosscheck.py` 7bd58fdc…; `unisolvence_check.py` 6b31e106…; `padua_n4_generator_cert.py` 2089430c…. Trusted dependencies: sympy (QQ<√2> ANP arithmetic, DomainMatrix rank/nullspace, Chebyshev polynomials), Python Fraction. cvxpy only proposes candidates.

## 4. Literature (task 5)

All readings were through WebFetch, i.e. a summarising model, not page images, as for the developer.

- **Kachkovskiy–Safarov, arXiv:1403.2021: CONFIRMED.** Introduction eq. (1.3): ‖X − X′‖ + ‖Y − Y′‖ ≤ C‖[X,Y]‖^{1/2}, for *commuting Hermitian* X′, Y′, with "C does not depend on X, Y and the dimension". It is a consequence of Thm 1.1 (real rank zero C*-algebras, (1.1)/(1.2)); Remark 1.3 gives d_1 = 0 for matrices. Matches lit_reading and INDEX LIT?…-221.
- **Koiran, arXiv:2401.01302: CONFIRMED.** §1.4: "At the moment, this problem is wide open" (two matrices). Also: "it is easier to compute commuting extensions for three or more matrices than for two"; size-2n extensions always exist (§2); Kimsey–Woerdeman Thm 4.1 (size 2n − 1 for invertible pairs); real symmetric r = n+1 studied in [6] Thm 4.2. Nothing on approximate extensions or positivity.
- **Di Dio–Schmüdgen, arXiv:1703.01497.** Prop. 27(i)/(ii) (locally compact X, no compactness needed): boundary ⟺ N_+(s) ≠ {0}, inner ⟺ N_+(s) = {0}. Thm 40 and Cor. 41 restate this for X = ℝ^n, E ⊂ C¹. Consistent with 302's context citation, and no proof is imported. The paper does not state closedness of the cone; 302 proves it directly by compactness, correctly.
- **Šimonová–Tichý, arXiv:2507.16484 (html v1) §1.** "the proof is given for intervals of size √ε‖A‖"; "experiments indicate … ε‖A‖"; block case "remains open". So the developer's *secondary* report is accurate. However, **INDEX LIT?…-209 (online pass) records mutually inconsistent secondary accounts**: Chen arXiv 2608.21268 gives a fourth-root dependence, and Meurant–Strakoš Thm 4.9 gives a polynomial factor times max{ε‖A‖, f_j}. Two further sources I checked give no exponent. Hence finding L9: the remark in 300, R03 §3 and lit_reading that Greenbaum's width is "the same order as the square-case (H) rate" is contested. It also compares two different ε's (unit roundoff versus functional perturbation size). It is non-load-bearing and should be marked as unresolved per LIT?…-209.
- **Degani–Schiff–Tannor.** Abstract-level only (as the developer says); not re-read.
- **Curto–Fialkow.** Not used by L3, correctly: the flat-extension theorem (INDEX LIT?…-225) concerns even-degree moment matrices and representing measures without support localisation, whereas L3 needs odd degree 2n+1 and support in K_δ.
- **Tchakaloff.** Not needed: Carathéodory plus duality on compact K_δ suffices, as written.
- **Positive cubature existence.** Correctly reduced to 302(a)(iv). No external theorem is used.

## 5. Protocol and record-keeping (task 6)

- **M3. Kill criteria are not demonstrably written before the tests.** K1–K4 first appear in commit `4474064` (22:57:04, where candidates.md and R01.md are created). The log that decides K1 (`lp_rate_n2_r0.03.log`) was already committed in `53fd00b` (22:34:35); at that checkpoint `directions/L3/` contained only BRIEF.md and the four lp logs, although the checkpoint swept in other directions' R01 files. The code deciding K2 (`exact_certificates.py`) was committed at 22:14:14. K5/K6 (R02) and the IDEA 311 criterion (R03) arrive in the same commits as their deciding logs. The claim "kill criteria were written … before the corresponding test was run" (candidates.md header) is therefore unverifiable, and the commit order is against it for K1. This does not affect the mathematics, because the decisive tests are exact or robust, but the protocol requirement is not evidenced.
- **L8. STATUS timestamps.** The orchestrator's note flags R02/R03 (23:20/23:40) as future estimates. **The R01 line "23:05:00" was already present in commit `4474064` at 22:57:04**, so it is also an estimate, and no STATUS line records an observed time. R03 was triggered by the 23:00 authorisation and committed at 23:05:40, so it took at most about 6 minutes for four web readings plus the survey run. That is plausible, but the window should be recorded. The post-audit "Pending corrections" in candidates.md mention only R02/R03.
- **L10. PD-N dispositions.** IDEA 303 (compression route: the evidenced negative statement "compression existence ⇏ section existence", witnessed by 308 + N301), IDEA 310 (closed form C1, MEASURED failure for n = 2..12) and IDEA 311 (MEASURED refutation) are REJECTED without a PD-N. WORKFLOW says "A separate evidenced mechanism failure still gets its own PD-N". This is a classification for the orchestrator or AC.
- **Status labels and splits** are otherwise correct. 300 is OPEN rather than PARTIAL. 303 has six PROVED parts in one file with no status mixing. 306/N301 are CONDITIONAL only pending the rerun, now done. 307 is MEASURED. 309 should carry the explicit assumption (L7). `lp_rate.py` changed after the R01 bisect runs only by an added `resid` mode (verified by `git diff 53fd00b 4474064`), as R02 discloses. All code hashes verify. The log total is 140 KB, under the limit.

## 6. Findings by severity

**High: none.** No PROVED claim was refuted; no counterexample was found.

**Medium**

- **M1.** Overstated scope framing (plan History; R01 §3/§5; STATUS R01; LOG line 70). "The literal L3-Q1 is trivial" holds only with an added forward-accuracy hypothesis. As frozen, the question is either trivially negative (relations on the sections alone) or the OPEN Greenbaum regime (G). Reading (E) is a recorded substitution with a stronger conclusion. Fix: reword, and qualify every "L3-Q1 answered/made precise" as "in reading (E)".
- **M2.** 302 Definitions: residual "for some c > 0" is trivially satisfiable. Fix c = 1 (or normalise); propagate to 302(b) and the N301/N302 scope text.
- **M3.** Pre-registration of kill criteria is not evidenced and is contradicted by commit order for K1 (§5).

**Low**

- **L1.** The quantifier "for every ε > 0" in 303(e)/N301 needs M_n(L_μ + E) ≻ 0.
- **L2.** δ_0 is valid but 100× conservative; rigorous 0.04 is available.
- **L3.** 304(c): the isomorphism part is unproved (measured rank full for n = 2, 3).
- **L4.** 301(d): the formed-entries convention conflicts with L1 PD-T?…-101(4) unless stated.
- **L5.** 307 wording: marginal cases are counted as failures; the grid residual is an upper bound.
- **L6.** 309(b): injectivity must be a conjunct.
- **L7.** 309: state Padua unisolvence as an assumption.
- **L8.** STATUS R01 timestamp is also not observed.
- **L9.** The Greenbaum-width "same order" remark is contested (LIT?…-209) and compares different ε's.
- **L10.** PD-N classification of IDEA 303/310/311.
- **L11.** "Unisolvent" should read "determining" in 303(a).
- **L12.** "Explicit δ(ε)" is met only as a rate.
- **L13.** State support-inclusion versus Hausdorff explicitly (the existence results also give Hausdorff for small ε).
- **304(a).** Add the W_i > 0 step.
- **N302.** "Atom" should read "support point".

**Informational (positive)**

- Independent exact reruns pass for 305, 306 and N301.
- The developer rerun is byte-identical.
- A second, independently derived n = 3 certificate exists.
- An exact n = 4 obstruction certificate exists (beyond scope).
- S_1 = {p_C} exactly for n ≤ 3.
- 309(c) is exact for n ≤ 3.
- Padua unisolvence is exact for n ≤ 4.

## 7. Remaining uncertainty

- **Trusted dependencies.** My exact checks trust sympy's QQ<√2> arithmetic and DomainMatrix nullspace/rank, plus my own sign test. The latter is cross-checked against rational enclosures of √2 (assertions passed). The Q(√2)(√5) tower class in the n = 4 probe is my own code and has not been independently re-run.
- **Shared method.** Both my LP/SDP reruns and the developer's use CLARABEL/HiGHS, so they are not solver-independent; only the exact results are solver-free.
- **Literature reading method.** The literature confirmations are WebFetch summaries, not page images. Greenbaum 1989 remains unread by anyone, and its exponent is unresolved.
- **Hand-checked proofs.** 301–305, 308 and N302 have no machine-checked proof. I found no gap beyond those listed, but "no gap found" is not a guarantee.
- **Out of scope.** Reading (G) is OPEN, and nothing here bears on it. Post-`0b7b396` L3 material (R04–R06, 310–313, N303) is unaudited.

## 8. Requested dispositions (for the orchestrator or AC; the reviewer approves nothing beyond this scope)

- **PD-T?…-306 and PD-N?…-301.** All computer-assisted-proof obligations are met once this review's checker and logs are committed: proved finite reduction, exact arithmetic, a committed developer checker and log, and an independent rerun (this review). They may move CONDITIONAL → PROVED after the developer answers L1 (quantifier). Optionally restate δ_0, citing this review's rigorous interval certificate, which would need a developer record.
- **PROVED claims.** 301–305, 308, 309 and N302 stand as PROVED after the M2/L-level wording fixes. M1 is required before any topic-level statement that L3-Q1 is answered.
- **307** stays MEASURED with the L5 wording fixes. The reviewer's exact S_1 = {p_C} for n ≤ 3 may be cited as an independent check.
