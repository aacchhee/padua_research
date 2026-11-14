# C1: companion Sections 1–3, reader assessment and verification

Part of the substantive Claude audit (handoff 28), §3 of `claude-audit-brief-20261108.md`.

- **Auditor:** Claude Opus 5.5, xhigh effort. Independent subagent auditor. I made no repository edits and ran no state-changing git command.
- **Rules:** I read `AGENTS.md`, `agents/WORKFLOW.md`, `agents/claude/CLAUDE_ROLES.md`, the brief, and the companion's `README.md`, `BUILD.md`, `review.md` and `main.tex`.
- **Revision:** branch `codex/padua-argmax-bridge-20261105`, head `f366535e1fa4ede566cb83bdc554220c12b307cf`. The tree was clean.
- **Audited sources:** these match the frozen identities in `review.md` (SHA-256):
  - `main.tex`: `2c3350b7…`
  - `sections/introduction.tex` (496 lines): `8f3174fe…`
  - `sections/preliminaries.tex` (641 lines): `0667719e…`
  - `sections/corner-unified.tex` (1795 lines): `6d68c3f8…`
- **Reading coverage:** I read every line of those three companion files, the matching paper sections (`paper/sections/introduction.tex`, `preliminaries.tex` and `corner-unified.tex`), and the companion's `main.tex`.
- **PDF used for page references:** agent X's fresh build at `$A/build/companion/main.pdf`.
  - 162 pages, 1153282 bytes, SHA-256 `dec7c44c…`. It is not byte-identical to the recorded PDF; that is expected.
  - My page numbers come from `pdftotext -layout` and the fresh `.aux` file. Section 1 is pp. 1–9, Section 2 pp. 9–19, Section 3 pp. 19–46.
  - The fresh `.aux` gives Lemma 2.1 on p. 12, eq. (8) on p. 20, (12) on p. 24, (13) on p. 26, (14) on p. 29, (15) on p. 32, Lemma 3.1 on p. 34, Prop 3.2 on p. 37 and (23) on p. 44.
- **No novelty content.** The companion is expository, so the full IDEAS gate does not apply. I made no literature or novelty judgments.
- **Evidence labels:** [D] derived or checked by hand, [E] executed computation, [I] inspection or judgment.

## Verdicts

**Mathematics of the added explanations: no error found.**
- I re-derived every added identity, inequality, worked example and intermediate calculation in Sections 1–3 by hand [D]. I also checked them with mpmath, sympy and numpy at 25–40 digits [E].
- No sign, constant, index-range or hypothesis error was found. All numerical examples recompute exactly.
- The equality of the original numbered blocks was confirmed separately by X. My checks are of the added prose and displays.

**Pedagogy: largely meets the depth standard; ACCEPT AFTER REVISION.**
- Two MAJOR clarity items remain:
  - C1-01: the central exact corner formula cannot be reconstructed from the text.
  - C1-02: symbol overloading, including collisions that the companion itself introduced.
- There are also eleven MINOR or NOTE items.
- The depth is otherwise good. In particular, the linear algebra of Lemma 2.1, the endpoint and quadrature machinery, the limit interchange and the coefficient ledger can be reconstructed by a reader with university analysis.

**Agreement with the paper: consistent.**
- Theorem 1.1 and 1.2 hypotheses, the constants in (3) and (4), the node convention (2), the equality sets, the uniform remainder for n≥2 and all label numbers agree.
- No discrepancy was found (see §6).

## 1. Subsection map: purpose, needs, definitions before use, gaps [I]

| Unit (PDF pages) | Purpose / reader needs | Terms defined before use? | Gaps |
|---|---|---|---|
| §1 "Problem in ordinary terms", (1) and its proof (pp. 2–3) | Interpolation operator, operator norm, Lebesgue inequality, perturbation reading. Needs: linear maps, sup norm. | Yes: Π_n, total degree, C(Q), ‖·‖∞, I_n, ‖I_n‖. | none |
| Padua points (2), n=2 example, count, corner parity, Fig. 1 (pp. 3–4) | Concrete node set and why the corners are non-nodes. | Yes: mesh, checkerboard. | Fig. 1 dots are tiny, and there is no index-array picture (C1-11). |
| Cardinal L_B, λ_n, worst-case sign data (pp. 4–5) | Lebesgue function, λ_n≥1, attainment of the bound. | Yes: cardinal polynomial, sgn. | none |
| Thm 1.1, strength of location claim, symmetry, certificates and enclosures (pp. 5–6) | Statement and proof architecture. | Yes: enclosure, certificate. | Repetition (C1-09). |
| (3), (4), "Reading the constants", κ convergence (pp. 6–7) | Constants and finiteness of κ. | Yes: γ, natural log. | "Near the other endpoint" comes before either endpoint is named (C1-09). |
| Thm 1.2, error term, N-scale (pp. 7–8) | Meaning of the uniform O and of N. | Yes. | Misleading parity sentence (C1-07). |
| Literature and route (pp. 8–9) | Global proof vocabulary. | Yes: envelope, reflection defect, completed model, positive interpolation, quadratic descent. | Orphan sentence "The onset 320…" (C1-09). |
| §2 Existence/uniqueness, operator norm (pp. 9–10) | Unisolvence as bijectivity, plus a hat-function extremal input. | Unisolvent: yes. Kronecker δ is used at l.30 but defined at l.41. | C1-08 |
| Chebyshev basis, weights, checkerboard scalar product (pp. 10–11) | Basis of Π_n; bilinear, symmetric, positive semidefinite form. | Mode index, bilinear, positive definite: yes. Trapezoidal rule is not defined (p. 11). | C1-08 |
| K_n, reproducing kernel, continuous orthogonality, R_n (pp. 11–12) | Why the coefficients ν are 1 and 2, and why one is corrected. | Yes: kernel, reproducing kernel, cardinal kernel. | "changes the highest available frequency" is imprecise (C1-08). R_n name collides with the intro (C1-02). |
| Lemma 2.1 proof: geometric sum, Q_M, Gram, alternating part, positivity, matrix form, reproduction, F=I (pp. 12–16) | Complete, reconstructible linear algebra. | Yes: Gram matrix, tensor part, indicator, diag, transpose. | none (excellent) |
| n=1 example (pp. 16–17) | Full small case: weights, Gram, cardinals, λ_1, maximizers. | Yes. | Could note that it shows the odd-parity pattern of Thm 1.1, with Λ_c(1)=2 (C1-10). |
| Angles, G_n (7), reflected copies, cancellation loss (pp. 17–18) | Bridge to the trigonometric proofs. | Yes: angular kernel, trigonometric polynomial. | §3 never connects D_n to G_n (C1-01). |
| Symmetry, quotient convention, Remark (pp. 18–19) | Equal values at the two corners; collisions. | Yes: collision. "Removable singularity" is defined only on p. 22. | Heading "surviving reflections" (C1-08). |
| §3 opening (pp. 19–20) | Three-stage roadmap; pole, Cauchy sum, O, uniformity, endpoint weights. | Yes. | none |
| §3.1 exact row formula, (8)–(12) (pp. 20–26) | Corner value as a positive Cauchy sum, then the row and digamma form. Needs product-to-sum identities, geometric progressions, coprimality, the sine product and the ψ recurrence. | D_n, analytic, w, B, ψ, logarithmic derivative: yes. ψ is never named as the digamma function. | C1-01, C1-03, C1-04 |
| §3.2 square reference, (13)–(15) (pp. 26–33) | Leading square L_n², mesh-defect bound, κ limit with an explicit ε/3 interchange. | Yes: H_k, Riemann sum (assumed known). | H_k expansion is used before it is proved (C1-05). |
| §3.3 Lemma 3.1, ψ estimates, Prop 3.2 and proofs (pp. 33–46) | Quadrature with log endpoints, digamma estimates, endpoint sequences, M_m, smooth part, cancellation, half step. | Quadrature, local uniform convergence: yes. The termwise-differentiation theorem is never stated. | C1-05, C1-06, C1-12 |

## 2. Independent verification of the added derivations

Every item below was checked; nothing failed. Scripts and outputs are in `$A/c1-code/`: `check_exact.py` and `check_exact.out` (25.8 s), `check_asym.py` and `check_asym.out` (4.6 s), `example_table.py`/`.out`, and `prose_diff.py`/`.out`.

**Introduction**
- [D] The dimension formula and the n=2 node and index list. [E] The six nodes recomputed.
- [D] The counting argument, the corner index parities, the reflection symmetries, the proof of (1) and the extremal sign argument.
- [D] The square identity a²log²N+b log N+c=(a log N+c_1)²+κ.
- [D] The bound ℓ²−t²≥(8/9)ℓ² for ℓ≥3, and Σ_{ℓ≥L}ℓ⁻³≤L⁻³+1/(2L²).
- [D][E] lim_{t↑1} t²cot(πt/2)/(1−t²)=π/4: 0.785398163397447 at 1−10⁻¹⁵.
- [E] sympy confirms log²(n+½)=log²n+(log n)/n+O(log n/n²).
- [E] The κ integrand tends to 2 at t=1 and is about 1.7×10⁻⁸ at t=10⁻⁸. κ=0.91971011838849…>0, consistent with the positivity claim on p. 33.

**Preliminaries**
- [D] The hat-function extension, the Chebyshev recurrence and basis argument, and the continuous orthogonality integrals.
- [D] The geometric sum (1−σz)/(1−z)−(1+σ)/2=(1−σ)(1+z)/(2(1−z)), and (1+e^{iα})/(1−e^{iα})=i cot(α/2).
- [D] Q_M values and h_p^{(M)}; the identity cos((M−p)t_j)=(−1)^j cos(pt_j); the alternating-part contradiction 2n+1>2n.
- [D] The inverse Gram coefficients, (E^TWE)=D, F=ED⁻¹E^TW, FE=E, and hence F=I.
- [D] The reflected-copies identity for R_n, including the −cos(nθ)cos(nα) correction.
- [D] The sum-of-exponentials quotient with its limit M; the reflection maps and their parity.
- **n=1 example** [E]:
  - weights 1/4, 1/4, 1/2 and the exact Gram matrix diag(1,1,½) (Fractions);
  - the cardinal matrix is the identity and the cardinals sum to 1 (sympy);
  - |a+b|+|a−b|=2max(|a|,|b|) [D];
  - λ_1=max(1,|y|+(1−x)/2) with maximum 2 exactly at (−1,±1) [D], with a grid check [E].
- [E] For n=1..8: L_B(A)=δ_AB to 10⁻⁴⁰ from formula (6); Σ_B L_B=1; node corners have λ=1; the two non-node corners are equal.

**§3.1**
- [E] Λ_c(n) from Lemma 2.1 agrees with (8) and with both forms of (12) for n=2..8 to 15 digits. Λ_c(2)=3 exactly.
- [E][D] The diamond closed form for D_n.
- [D] |p|+|q|=max(|A|,|B|) and pu+qv=AS+BT; progression lengths n+1 and n; Σe^{i(−M+2h)z}=sin((M+1)z)/sin z.
- [E] D_n(θ_j,φ_k)=(−1)^j(2+cos θ_j+cos φ_k)/(cos θ_j−cos φ_k) and |D_n−(−1)^j|=2f, for all odd-checkerboard pairs with n≤7.
- [E] sin(mθ_j)=(−1)^j sin θ_j, sin(nφ_k)=(−1)^{k+1}sin φ_k, and D_n(π,π)=(−1)^n(2n+1).
- [D] The collision weight 1/(2nm) and its contribution 1/m; coprimality leaves only the collisions (0,0) and (n,m); B(0)=1/π and B(1)=−1/π; the series of w at both ends; 0<w≤a/x; and w≤π(1−x) on [½,1) [E] (maximum ratio 0.637).
- [E] The F_r cotangent form; Σcot(z+ℓπ/n)=n cot(nz); the csc² identity; Σ_{ℓ<n}csc²((ℓ+½)π/n)=n²; the signed row sum equals n (n≤11, every r).
- [D] The plus-sum argument n z=π/2−v/2, and the minus sum differing by rπ.
- [E] The positive indices are exactly {−r+1,…,r−1}; P_r=wT_{n,r}; the absolute row equals 2P_r−n.
- [D] The folding identity; F_0=−csc²(u/2); the n=2 csc² example (4=n²).
- [D] The assembly 1/m+n/m−2(m−1)/m=1−2n/m (with m−1=n).
- [E] The two-pole decomposition and both ψ telescopings (to 10⁻⁴⁰).

**§3.2**
- [E] For n=2..40: equation (13); the unnormalized e-form and its square; L_n=(1/n)Σcot y_r. Maximum deviation 10⁻³⁶.
- [D] The diagonal and cross-term bookkeeping (r=s↔k=0, r=2n−s↔j=n, the ec_n²/4 term). [E] The n=2 check L_2=√2 and the four terms totalling 2.
- [D] (1/n)Σ1/y_r=a(2H_{2n}−H_n). [E] ∫(cot y−1/y)=log(2/π). [D] 2H_{2n}−H_n=log n+γ+2log2+O(n⁻²) and L_n²−A(n)²=O(log n/n²).
- [D] The (14) chain:
  - the order of u and v_i, including nk−mj=n(ℓ−1)+(n−j);
  - the common-denominator numerator (1+c)(c_1−c_0) [E, sympy];
  - the half-angle factors and sin S_i≥cos(u/2)sin(v_i/2);
  - cot(v_0/2)≤π(n−k)/(2k) and cot(v_1/2)≤π(m−k)/(2k);
  - sin(δ/2)≤πk/(2nm), sin Q_i≥|u−v_i|/π, and both cases k<j and k>j;
  - (ℓ−1)h≤(ℓ−1)n.
  - [E] The maximum of |difference|/(π²n/(2ℓ²)) over all pairs (n≤59 and n=101, 160, 257) is 0.203, so the bound holds.
- [D] Λ_c−L_n²=Δ_n+(1−L_n²)/m; the k=n reference row is 0; φ_k−θ_j=π(σℓ−t)/m; the local limit h_{σ,ℓ}; and (4n/m)·Riemann sum.
- [D] The endpoint-strip count ≤2δn+2; the ε/3 order of limits; and the orientation pairing 2t²/(ℓ(ℓ²−t²)).

**§3.3**
- [D] The Peano kernel K: K'(u)=h/2, K''=−1, max K=h²/8, ∫K=h³/6. [D] The midpoint bound M_2h³/24 and the endpoint-cell estimate. [E] For x log x, m²·err/log m≈0.11–0.19, which is bounded.
- [D] Σ(z+k)⁻³≤z⁻³+1/(2z²) gives |ψ''|≤z⁻²+2z⁻³. [E] (16) is uniform for z≥1.
- [D] The csc² limit to ψ′(½)=π²/2, with the middle-block tail bound (1/2)Σ_{j≥J}(j+½)⁻², and S=π²/6. [E] ψ(½)=−γ−2log2 and ψ′(½)=π²/2.
- [D] (19): α=s/(2m), the three shifts, the lower arguments ≥r, 3s/4, 3m/4, and the r-term bound 3/(4m²). [E] max m²·|error| = 0.456 over m≤301.
- [D] The midpoint cell error ≤1/(4(r+k)⁴), the sum ≤1/(3r³), e_r=O(r⁻²) and u_r=O(r⁻²). [E] r²e_r→1/24 and r²u_r→−1/12.
- [E] The recurrence identity for Σψ′(r+½) holds exactly (R=1, 2, 7). [D] So does its R−1→R difference.
- [E] S_u=1+2log2−π²/4=−0.0811067… and q_0+S_u=2log2.
- [D] (20): every term, including the cancelling ±1/(2m). [E] max |Q|/(s⁻²+(ms)⁻¹+m⁻²)=0.14.
- [D] The split of the weighted remainder sum, the e_r/u_r tail and v contributions, and the endpoint regularity of w/(1−x)−a/x and xw.
- [D] (21): the full assembly.
- [D][E] J(0)=d_0, J′(0)=q_0, R(0)=aq_0 and R(1)=π−ad_0.
  - The factorizations R=aq_0+xA_0+xv_1 log x and R(1−y)=A_1+yb log y hold.
  - The second-derivative formula holds.
  - A_1(0)=π−ad_0.
- [D] The cutoff integral of v gives (22) with the cancellation of a/(2m).
- [D] The cell identity for log t/t: f″=(2log t−3)/t³, the outer correction −log m/(2m), and the tail C(1+log m)/m². [E] C_K≈−0.072816.
- [D] The three singular pieces of M_m and their L/m cancellation. The L coefficient is a(c_v+d_0)=ad and the 1/m coefficient is −(π+aq_0)/2.
- [D] β_H via aπ=2. [E] A fit of H_m over m=400..3000 gives β_H=−3.551278 against −3.551275 claimed.
- [D] The smooth part: cell endpoints −t/(2n) and t+t/(2n), the extension integrals, F_B(0)=a²/2, G_B(0)=a², F_B(1)=G_B(1)=0, −a²/m−a²/(nm)=−a²/n, and β_B.
  - [E] A fit gives C_B=0.3378987115 against 0.3378987117 and β_B=−0.061485 against −0.061486.
  - [E] max n|row error|/t=0.027.
- [D][E] (23): 2I_B−aI_1=−0.41169568858130270 on both sides. [D] The integrand identity and the three boundary terms a², −a²log(2/π) and −1.
- [D][E] 2+β_H+β_B=−1−a²d=−1.6127610628710. [D] |β_B/n−β_B/m|≤3|β_B|/(2m²).
- [D] A(m)²−A(n)², P′ and P″ [E, sympy], and the Taylor step to N=m−½.
- [E] **Theorem 1.2 end to end.** Λ_c(n) was computed from (8) for n up to 3001.
  - N(Λ_c−A(N)²−κ) = −0.773 (n=2), −0.961 (n=10), −1.000607 (n=200) and −1.000215 (n=3000), tending to −1 in both parities.
  - R_nN²/log N stays within [−0.081, 0.62].
  - −1+C_H+C_B=0.9197101186 against κ=0.9197101184.
  - This is a numerical consistency check of an analytic proof, not evidence for it.

## 3. Passages that still hide work [I]

1. **The corner kernel evaluation** (corner-unified.tex:77–79 and 87–94; p. 21). See C1-01.
   - The text says "Grouping signs identifies this with the product Chebyshev sum at a corner".
   - Missing: K_n((−1,−1),B)=D_n(π−θ_j,π−φ_k), with D_n=G_n+cos(nu) and T_n(−1)T_n(cos θ_j)=(−1)^{n−j}.
2. **The numerator reduction** (l.138–143; pp. 21–22). See C1-01.
   - The text says "these identities reduce the numerator". The quoted sin(mθ_j) and sin(nφ_k) identities do not do this.
   - Missing: product to sum on each numerator term, and the four cosine values at mesh angles.
3. **The F_r cotangent form** (l.265–266; p. 24). The text says "follows by putting the two cotangents over a common denominator". Missing: cot A+cot B=sin(A+B)/(sin A sin B), 2 sin A sin B=cos u−cos v, and cot(v/2)sin v=1+cos v.
4. **The sine product** (l.274–276). The text says "the product then factors e^{2inz}−1 into its n roots". Missing: with X=e^{2iz} and ω=e^{2πi/n}, ∏_ℓ(1−Xω^ℓ)=1−X^n, so ∏_ℓ sin(z+ℓπ/n)=2^{1−n}sin(nz).
5. **The minus sum** (l.300–302). Missing: {−ℓπ/n} equals {ℓπ/n} modulo π, so the identity applies after reindexing.
6. **H_k** (l.500–504, p. 27; and l.992 "This also proves the harmonic estimate used above", p. 35). Missing: ψ(k+1)=H_k−γ by telescoping, and log(k+1)−1/(2(k+1))=log k+1/(2k)+O(k⁻²). See C1-05.
7. **ψ(1/2) and ψ(m)** (l.993–994; l.1515 "follows directly from ψ(m)=H_{m−1}−γ"). These are claimed before they are derived (the derivation is at l.1057–1063), and ψ(m)=H_{m−1}−γ is never shown. See C1-05.
8. **Analyticity, termwise differentiation and power-series summation** (l.208–211, 959–967, 1400–1406). See C1-06.
9. **"Successive elimination by degree"** (prelims:84–85). This is acceptable, but one sentence would complete it: the transition matrix between the two bases is triangular with respect to total degree.

All other "directly", "follows" and "summing" occurrences in the three files (54 hits, l-numbers in my notes) are followed by the actual calculation, or are trivial.

## 4. Standard tools [I]

**Well handled:**
- Geometric sums (proved).
- Product-to-sum identities (stated where used, except for C1-01).
- The trapezoid rule with its Peano kernel (derived as the integration-by-parts identity, though not named "Peano").
- The midpoint rule (derived) and the logarithmic-endpoint quadrature lemma (complete).
- The Weierstrass-type uniform bound for the κ series, integration of uniform limits, and the dominated-convergence step for the csc² limit and the κ interchange (both done by hand with explicit ε/3 or tail arguments).
- Partial fractions, which are replaced by finite cotangent sums.
- Taylor's formula with integral remainder (stated).

**Insufficient:**
- (a) The termwise-differentiation theorem: if Σf_k converges at one point and Σf_k' converges uniformly on an interval, the sum is C¹ there with derivative Σf_k'. It is used at l.959–967 without a statement.
- (b) The power-series facts behind "analytic across [0,1]" (l.190–211, 1400–1406). These need Laurent or power series of cot or complex analysis, which is beyond the declared prerequisite. Only C²–C⁴ smoothness with bounded derivatives is ever used.
- (c) ψ is never named as the digamma function Γ′/Γ. This is harmless, but a reader consulting references needs the name.
- The Gamma function and Euler–Maclaurin are not needed and are correctly avoided.

## 5. Pacing, examples, figures [I]

**Strengths:**
- Every major step has a local motivation: the §3 opening, the 3.2 lead, the Prop 3.2 preamble, the half-step "forced" paragraph and the explicit ε/3 choice.
- The linear algebra on pp. 12–16 is model exposition.

**Weaknesses:**
- Preserving the article text while interleaving explanations produces repeated passages and lost antecedents (C1-03, C1-09).
- §3.1 opens with a 15-sentence paragraph on p. 21 mixing the change of variables and four reflections.
- The 9-page proof of Prop 3.2 has no step list and no final ledger (C1-12).
- Symbol overloading is heavy (C1-02).
- There is no worked example of an actual corner value and only one small figure (C1-10, C1-11).

## 6. Agreement with the paper [I][E]

- **Statements and numbering.** Theorems 1.1/1.2, Lemma 2.1, Lemma 3.1 and Prop 3.2 are identical. In the fresh `.aux`, the numbers 1.1, 1.2, 2.1, 3.1, 3.2 and equations (1)–(23) match the paper's numbering. X's block diff reports 0 missing paper displays for these sections.
- **Prose.** `prose_diff.py` finds that the only paper prose in these sections absent from the companion is re-segmented sentences, plus one replacement. The paper's "classical paired partial fraction … cosine series of cos(zs)" derivation of ψ′(½) (paper corner-unified.tex:257–266) is replaced by the finite csc² limit (p. 36). The proved value and its use are unchanged.
- **No discrepancy** in hypotheses (n≥2; the uniform C), the constants a, d, c_1, b, c, κ, the node orientation (2), the exceptional coefficient one, the equality sets, or the statement that the corner proof is analytic while Λ_n uses Thm 1.1.
- **Paper premises exposed by the longer text** (for the paper assessment; coordinate with C1-01):
  - (i) paper/introduction.tex:5–9 uses Π_n and I_n in (1) before they are defined (prelims l.2–6).
  - (ii) paper corner-unified.tex:25–46 has the same two gaps as C1-01: no D_n↔G_n link and no cosine mesh values in the "product to sum" step. The remedy is the same two displayed lines in both texts.

## 7. Findings

**C1-01 — MAJOR (clarity; theorem sound). The exact corner formula (8) cannot be reconstructed.**
- *Location:* corner-unified.tex:77–160 (pp. 20–22).
- *Reason:*
  - (a) The step from Lemma 2.1 to "|D_n(θ_j,φ_k)−(−1)^j|" is described only in words. G_n of (7), which §2 says "gives the exact signed row sums", never reappears; a new D_n is used instead.
  - (b) The numerator reduction cites sin(mθ_j)=(−1)^j sin θ_j and sin(nφ_k)=(−1)^{k+1}sin φ_k. A reader cannot get the formula from these. The working identities are the cosine values.
  - (c) The text never says why one sign change per row is enough. On the odd checkerboard, j≡r+1 (mod 2) is fixed along row k=r, so (−1)^j is constant there.
- *Impact:* this is the foundation of all of §3, and the intended reader cannot verify it.
- *Fix:* insert the following display after l.94.
  - "At z=(−1,−1), T_p(−1)=(−1)^p gives K_n((−1,−1),B)=Σν_pν_q cos(p(π−α))cos(q(π−β))=D_n(π−α,π−β), where D_n(u,v)=Σ_{p,q≥0,p+q≤n}ν_pν_q cos(pu)cos(qv)=G_n(u,v)+cos(nu)."
  - "With (j′,k′)=(n−j,m−k), π−θ_j=θ_{j′}, π−φ_k=φ_{k′} and T_n(−1)T_n(cos θ_j)=(−1)^{j′}=cos(nθ_{j′}), we get L_{jk}(−1,−1)=w_{jk}[D_n(θ_{j′},φ_{k′})−(−1)^{j′}]=w_{jk}G_n(θ_{j′},φ_{k′})."
  - Then replace l.138–143 with: "Since S−T=u and S+T=v, sin(aS)sin(aT)=½[cos(au)−cos(av)] and sin S sin T=½(cos u−cos v). At u=θ_j and v=φ_k, cos(nθ_j)=(−1)^j, cos(mθ_j)=(−1)^j cos θ_j, cos(mφ_k)=(−1)^k and cos(nφ_k)=(−1)^k cos φ_k. So the numerator is ½[(−1)^j cos u−(−1)^k+(−1)^j−(−1)^k cos v]=½(−1)^j(2+cos u+cos v), because (−1)^k=−(−1)^j."
  - Add one sentence on the constancy of (−1)^j along a row.
  - Split the paragraph at l.104–137 into three: change of variables, reflections, corner entry.

**C1-02 — MAJOR (collective clarity). Symbol overloading, including collisions the companion introduced.**
- *Locations:*
  - R_n is the remainder at intro:369 (p. 7) and the corrected kernel at prelims:180 (p. 12).
  - A and B are integer indices at corner:105 (p. 21), while A(z) is in force and B means a node or the function B(x).
  - c and c_i are cosines at corner:571 (p. 29), clashing with the main constants c and c_1 of (3).
  - Q is the "magnitude of the negative sum" at corner:354 (p. 25), alongside Q the square, Q_M, Q_i and Q_{m,r}.
  - e is the odd-n indicator at corner:468 (p. 27), alongside e_r, e_pq and e_B.
  - M is the offset cutoff at corner:758 and 771 (p. 32), alongside Q_M, the progression length M, M_m and M_2.
  - S=Σk⁻² at corner:1033 (p. 36), alongside S, S_i, S_e and S_u.
  - L=log m at corner:1519 (p. 42), alongside L_n, L(y) and L_B.
  - Inherited from the paper: D_n versus D_{m,r}; T versus T_p and T_{n,r}; h as the cell width, n−j, h_p^{(M)} and h_{σ,ℓ}.
- *Impact:* a reader without specialist background repeatedly holds two live meanings at once. The c_1 and R_n clashes are the most confusing.
- *Fix:* rename the symbols the companion introduced. These are unnumbered additions, so no paper block changes. Suggested renamings:
  - intro remainder R_n → ρ_n;
  - (A,B) → (μ_1,μ_2);
  - (c,c_0,c_1) → (x,y_0,y_1), consistent with x_j and y_k at l.59;
  - negative sum Q → N_r;
  - e → 𝟙_{n odd};
  - offset cutoff M → L_0;
  - S → ζ(2) or Σ_2;
  - L=log m → λ_m or ℓ_m.
- Add an unnumbered "Notation used in Section 3" table on p. 20 giving the scope of each inherited overloaded symbol (h, S, T, D, Q), and note that the sans-serif 𝖭=nm of §4 is distinct from N=n+½.

**C1-03 — MINOR. §3.1 bookkeeping order and lost antecedent.**
- *Location:* corner:257–399 (pp. 24–26).
- *Reason:*
  - The row derivation is told three times (l.257–304, the article paragraph at 306–324, then 326–399).
  - "Here is the endpoint bookkeeping behind them" (l.306) now follows the cotangent sums rather than (12).
  - The renaming of the row index k of (8) to r, and f(θ_j,φ_r)=|F_r(θ_j)|, are never stated.
- *Fix:* order the material as (12), then the article paragraph as a summary, then "Details" in the existing order. State "row k of (8) is written r; its entries are |F_r(θ_j)|" and give the row's contribution (4/(nm))η_r·½(2P_r−n).

**C1-04 — MINOR. Hidden trigonometric steps.** At corner:265–266, 274–276 and 300–302 (p. 24), add the three missing lines given in §3, items 3–5.

**C1-05 — MINOR. Digamma and harmonic facts are used before they are derived.**
- *Location:* corner:500–504 (p. 27), 990–994 (p. 35), 1057–1063 (p. 37) and 1515 (p. 42).
- *Fix:*
  - Add a forward reference at l.503.
  - Gather a "Facts about ψ" block at the start of §3.3:
    - (i) ψ(z+1)−ψ(z)=1/z;
    - (ii) ψ(k+1)=H_k−γ, by telescoping;
    - (iii) ψ(R+½)=ψ(½)+2H_{2R}−H_R;
    - (iv) estimate (16), followed by the one-line derivation of H_k=log k+γ+1/(2k)+O(k⁻²);
    - (v) the half-integer values.
  - Name ψ as the digamma function Γ′/Γ, used here only through its series.

**C1-06 — MINOR. Standard tools without a usable statement, and a prerequisite beyond the stated background.**
- *Location:* corner:190–211 (p. 22), 959–967 (p. 35) and 1400–1406 (p. 41).
- *Reason:*
  - The termwise-differentiation theorem is never stated.
  - "The same convergent power series give the asserted analytic extensions" assumes power series of cot, which is beyond some university analysis.
  - "The reciprocal-series bounds justify summing these local power series" omits the necessary separation of the p=0 term before the double series converges absolutely.
- *Fix:*
  - State the termwise-differentiation theorem.
  - Replace "analytic" by "C^∞ with bounded derivatives on the closed interval". Prove it for B and w by L'Hôpital or by the elementary representation cot(πx)−1/(πx)=(πx cos πx−sin πx)/(πx sin πx).
  - Obtain J_2 and v_1 from Taylor's formula with integral remainder: J_2(x)=∫_0^1(1−s)J″(sx)ds. This needs ψ∈C⁴ near ½, which follows from the termwise theorem.

**C1-07 — MINOR. Misleading motivation in the intro.**
- *Location:* intro:390–393 (p. 8) says "The midpoint scale N brings the two parities into the same formula". This is false as a contrast: in n or m the expansion is equally parity-free, Λ_c=A(m)²+κ−(a²log m+1+a²d)/m+O. The scale N absorbs −a²(log m+d)/m, as l.1741–1751 explain.
- *Location:* intro:376–378 says "resolved at a finer scale than the error", which is garbled.
- *Fix:*
  - Replace the first with: "The scale N absorbs the logarithmic reciprocal term, leaving the pure −1/N; both parities share one formula at any of these scales."
  - Replace the second with: "the error is smaller than the reciprocal term, so −1/N is genuinely determined."

**C1-08 — MINOR. Definition order and wording in §2.**
- δ_AB is used at prelims:30 but defined at l.41 (p. 10).
- "trapezoidal rule" at l.97 (p. 11) is not defined until corner:864. Give the formula h[g_0/2+g_1+…+g_{M−1}+g_M/2] at first use.
- "initially positive semidefinite" (l.119): drop "initially".
- "changes the highest available frequency in the first coordinate" (l.169–171): replace with "doubles the squared norm of the highest first-coordinate mode p=n (h_n^{(n)}=1 instead of ½); the second grid's corresponding mode q=n+1 is not admissible".
- "We use the Chebyshev polynomials" (l.89) comes after they have already been used.
- The heading "Why the surviving reflections preserve interpolation" (l.584, p. 18) is unclear and followed by blank lines. Suggested: "Symmetry of the node set and equal corner values".
- The unisolvence count (l.15) should cite the count on p. 4 and the distinctness of the points (cos is injective on [0,π]).

**C1-09 — MINOR/EDITORIAL. Repetition caused by interleaving.**
- *Repeated material:*
  - the certified-enclosure remarks three times (intro:264–291, pp. 5–6);
  - the κ integrand convergence at intro:325–354 and again at corner:816–857 (add a cross-reference);
  - corner:593–619 repeated by 621–631;
  - 753–768 repeated by 770–802;
  - 984–992 repeated by 1038–1055;
  - 993–994 repeated by 1057–1071;
  - the ledger display at 1700–1709 repeated by 1716–1721.
- Orphan sentences: intro:461 "The onset 320 is sufficient…" (also in paper:173); intro:341 "Near the other endpoint" comes before either endpoint is named.
- *Fix:* typeset preserved article passages as visibly marked summaries (for example, a left rule or "Article text:") and place the details after them; merge the duplicated estimates.

**C1-10 — MINOR (recommended addition). Worked examples are missing.**
- *Location:* add after (8) on p. 22, or after (12) on p. 26.
- *n=2 corner value from (8)* [E, hand-checkable]. Pairs (0,1), (1,0), (1,2), (2,1) give weighted terms 3/2, 1, 1, 1/2. Then (4/6)·4+1/3=3=Λ_c(2). Both forms of (12) also give 3.
- *A table of Λ_c(n) against the four-term expansion,* labelled as an illustration, not evidence:

  | n | Λ_c(n) | four-term expansion | difference |
  |---|---|---|---|
  | 2 | 3 | 2.90937 | 0.0906 |
  | 3 | 3.77614 | 3.73179 | 0.0444 |
  | 10 | 6.87710 | 6.87339 | 0.0037 |
  | 50 | 12.86692 | 12.86686 | 5.5e−5 |
  | 200 | 19.725381 | 19.725384 | −3.0e−6 |

- κ≈0.919710118388.
- The n=1 example could note Λ_c(1)=2 and the odd-parity pattern.

**C1-11 — MINOR (recommended). Figures.**
- Enlarge Fig. 1 (p. 4).
- Add:
  - (F1) the (j,k) index array for n=2 or 3, with the retained cells, the weights ε_jη_k, the non-node corner (n,m), and the reflected odd checkerboard of §3.1;
  - (F2) the diamond-to-square map (p,q)→(A,B) with its two parity lattices (p. 21);
  - (F3) the corner row: F_r on (−π,π] with the samples j≡1−r, the positive block |u|<φ_r, and the folding to [0,π] with half weights (p. 25);
  - (F4) the (r,s) triangle and its reflection into the square (Σd_rc_r)² (p. 27);
  - (F5) a plot of N(Λ_c−A(N)²−κ) tending to −1 (an illustration).

**C1-12 — MINOR. The proof of Prop 3.2 needs a roadmap and a ledger.**
- *Location:* pp. 37–44.
- *Fix:*
  - Open the proof with a step list: centering (19), endpoint sequences e_r and u_r, row expansion (20), weighted remainder, reduction to M_m (21), the M_m endpoints, and the smooth part.
  - Close §3 with a 1/m ledger table:
    - exact scalar +2;
    - from H_m: −aπ=−2 (from R(0)+R(1) and −ad_0), −a²q_0, −a²γ−aI_1 (row term −1/(2m(1−x))), −aI_2−a²S_u (row term −(x+u_r)/(2m)), using q_0+S_u=2log2, so that these sum to β_H;
    - β_B=−a²+2I_B+aI_2;
    - (23) gives a total of −1−a²d;
    - the half step removes −a²(log m+d)/m and leaves −1/N.

**C1-13 — NOTE.** κ>0 is shown on p. 33. The intro's "As usual … absorbed by increasing a finite constant" (l.397–399) is consistent, but §3 already proves the constants uniform for n≥2; one clause could say so.

**C1-14 — NOTE (agreement).** The replaced partial-fraction paragraph (§6) is acceptable and changes no claim. The paper premises (i) and (ii) in §6 are passed to the paper assessment.

## 8. Prioritized fix list for Sections 1–3

1. C1-01: displayed corner-kernel evaluation, D_n=G_n+cos(nu), cosine mesh values, constant row sign. Apply the same two lines to the paper.
2. C1-02: rename the symbols the companion introduced (ρ_n, μ_i, x/y_i, N_r, 𝟙, L_0, Σ_2, λ_m) and add a notation table for §3.
3. C1-10 and C1-11: the n=2 corner value example, the expansion table, κ≈0.9197, and figures F1–F3 (F4–F5 optional).
4. C1-05 and C1-06: a ψ facts block, the termwise-differentiation statement, and smoothness in place of analyticity.
5. C1-03, C1-12 and C1-09: reorder and mark the article text, add the Prop 3.2 roadmap and ledger, merge the duplicates.
6. C1-04, C1-07 and C1-08: line-level fixes as given.

## 9. Commands actually run (all outputs under `$A/c1-code/`)

- `sha256sum` of the four sources. `git rev-parse HEAD` and `git status --short` (clean). Both are read-only.
- `pdfinfo`, `pdftotext -layout main.pdf companion.txt`, and `pdftoppm -f 4 -l 4` and `-f 21 -l 21` (pages inspected visually) on X's fresh build. I did not build anything.
- `PYLIB=$A/pylib python3 -I check_exact.py` (mpmath 1.3.0, sympy 1.14.0), 25.8 s.
- `PYLIB=$A/pylib python3 -I check_asym.py` (adds numpy 2.5.3 and scipy 1.18.1), 4.6 s, after a one-line fix of a B(0) evaluation in my own script.
- `python3 -I prose_diff.py` and `PYLIB=… python3 -I example_table.py`.
- Total CPU is under 1 minute, against the 25-minute cap.

**Limits:** the numerical checks are consistency checks of analytic statements, and I claim no proved status from them. I did not assess Sections 4–5. I relied on X for the build and the block correspondence.
