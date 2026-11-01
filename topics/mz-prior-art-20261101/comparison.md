# Source-by-claim comparison — CC / Padua MZ manuscript

Claude (Opus 5.5), 2026-11-01, rules `9739a0c` (unchanged at `64c3c79`). Revised in response-01 to audit-01 (F1–F4, N1–N4). Literature verdicts only. **No PD status changes** (AGENTS.md / WORKFLOW: literature verdicts never change a PD status). Translations are proved in [translation.md](translation.md) (T1: λ_−(N,n)=1/‖L_N‖_n² for the CC-weighted nodal ℓ²→L²(dx) norm; T3: ½Δ_N(x_k)≤w_k≤5Δ_N(x_k); T4: Mastroianni–Totik at CC nodes, no stronger than exactness; T5: Lubinsky's excluded borderline; T6: Mastroianni–Milovanović–Notarangelo at CC nodes).

Admissible verdicts: SUBSUMES (with written translation) · IMPLIES PART (which part) · RELATED, DIFFERENT SETTING (mismatch) · *no matching result found in the documented search* (the only admissible negative).

## Our claims (abbreviated; exact statements in tracks/mz-constants/theory)

| Claim | Statement in comparison form |
|---|---|
| PD-T017 | ∫p²≤K_N Q_N(p²), p∈Π_N, K_N≍(1+log N)²; equivalently ‖L_N‖_N=O(1+log N) for ℓ²(w^CC)→L²(dx) at the N+1 Lobatto nodes. |
| PD-T018 | λ_−(N,N−1)≤128000/(log N)²; equivalently ‖L_N‖_{N−1}≳log N on data of degree ≤N−1 (witness in Π_{N−1}). |
| PD-T022 | λ_+(N,n)≤1+max(2n/N−1,0)²; endpoint λ_+(N,N−1)≤2−4/N+4/N²<2. |
| PD-T023/PD-T024 | For every θ<1 and n≤θN: spectrum ⊂[(1−θ)²/C_*, 1+max(2θ−1,0)²], explicit C_*. |
| PD-T025 | Positive-rule hyperinterpolation bound from an upper Gram bound only; CC constant (1+√2)√2. |
| PD-N004 | η_512>3/4 at m=513 points, n=511 (An–Wu's assumed η=3/4 fails there). |

## Comparison rows

| Source (LIT) | Our claim | Nodes | Weights | Nodal norm | Continuous norm | Degree range | Constant / rate | Verdict |
|---|---|---|---|---|---|---|---|---|
| Nevai III, TAMS 282 (1984) Thms 1, 2, 6, 7 (LIT-063) | PD-T017/018 | zeros of generalized Jacobi p_n(w); Thm 6 quasi-Lagrange adds ±1 (w=(1−x²)^{1/2}, r=s=1 is Lobatto/CC) | none (interpolation) | ‖f‖_∞ (uniform) | weighted L^p(u) | Π_{n−1} (Π_{n+r+s−1} for Thm 6) | sup_n bounded iff weight conditions; Thm 7: divergence via a log n lower bound for uniform input | RELATED, DIFFERENT SETTING: uniform input, not ℓ²(w) nodal data. Uniform C→L² boundedness at CC is consistent with ℓ²(w)→L² growth (ℓ²(w) is the weaker data norm). |
| Nevai III, property (g) eq. (24) (LIT-063) | PD-T023/024 | Gauss zeros | Christoffel λ_kn | ℓ^p(λ v) | L^p(vw) | degree ≤cn | constant C(c) | RELATED: forward direction (discrete ≤ continuous), Gauss nodes. |
| Mastroianni–Russo 1999, Thm 2.7 (LIT-293, new) | PD-T017/018 | zeros of p_m(w), w∈GDT | λ_m(v;x) or λ_m(σ^p;x) | weighted ℓ^p | L^p(σ^p) | P∈Π_{m−1} | iff σ/√(wϕ)∈L^p (and √(wϕ)/σ∈L^{p′}) | RELATED, DIFFERENT SETTING. At the interior CC nodes (zeros of U_{N−1}, w=(1−x²)^{1/2}), σ≡1, p=2 the condition requires (1−x²)^{−1/2}∈L², which fails (log divergence). This is a Gauss-node statement (interior nodes only, no endpoint terms) on Π_{m−1}. It gives no rate, no CC endpoint terms and no degree-(N−1) Lobatto witness. Its necessity proof (p. 275, read by the developer; not independently accessible to audit-01) passes through ‖p_m(w)σ‖_p≲‖L_m(w)‖_{L∞→L^p_σ}. It is an analogous classical borderline, not a proof of the CC statement (audit-01 F4); see T6 for the Lobatto-node source. |
| König–Nielsen 1994 / arXiv math/9208201 Thm 1 (LIT-294, new) | PD-T017/018 | zeros of p_{n+1}^{(α,β)} (Gauss) | Christoffel numbers of the same weight | ℓ^p(λ) | L^p(w_{αβ}) (same weight) | Π_n | iff p in (μ,M), with the upper endpoint determined by a=max(α,β): M=4(a+1)/(2a+1) when a>−1/2 (corrected per audit-01 F3; the α-only form assumes α≥β). At p=M, test norms grow like (log n)^{1/p}. | RELATED, DIFFERENT SETTING: nodes, weights and measure all come from one Jacobi weight. For the U-nodes (α=β=1/2) the critical exponent is p=3 with continuous weight √(1−x²); at p=2 the same-weight Gaussian form is exact. Our case mixes nodes from (1−x²)^{1/2} with Lebesgue measure. |
| Lubinsky 1999, Thms 1.1–1.7 (LIT-064) | PD-T017 | arbitrary ordered nodes incl. endpoints | local cardinal integrals + δ_jω(t_j)^p/[δ_j|π′(t_j)|]^p | weighted ℓ^p | L^p(ν^p) | Π_{n−1} | constant C(σ,…), σ in the open range (−1/p,1−1/p) | RELATED, DIFFERENT SETTING: the CC/Lebesgue case is the excluded endpoint σ=1/2 (translation.md T5). |
| Lubinsky 1999 (LIT-064) | PD-T018 | — | — | — | — | — | upper-type inequality only | RELATED (gives no lower bound on the norm). |
| Mastroianni–Totik 2000, §7 algebraic Marcinkiewicz inequality (LIT-051) | PD-T023/PD-T024 (lower) | any x_j=cos ξ_j with ±1, absolute angular gaps ≤1/(Mn) | Δ_n(x_j)w_n(x_j), with 1≤w_n≤2 for w≡1 | weighted ℓ^p | L^p(w), doubling w | Π_n with n≤N/(πM) at CC, admissible M≥1 | unspecified M, C_src | RELATED (**downgraded** from IMPLIES PART, audit-01 F1): λ_−(N,n)≥1/(16π²M²C_src) for n≤N/(πM), N≥2πM (translation.md T4). The window n≤N/π lies inside half-exactness, where exactness alone gives λ_±=1, so nothing beyond exactness follows unless the source allowed M<2/π (unspecified). |
| Mastroianni–Totik 2000 (LIT-051) | PD-T022 | same | same | — | — | n≤cN | converse with C_M, no value | RELATED: no upper constant <2, and for n≤N/2 exactness already gives 1. |
| Mastroianni–Totik 2000 (LIT-051) | PD-T017/018 | — | — | — | — | n≍N excluded | — | RELATED, DIFFERENT SETTING (degree ≤εn only; cf. Lubinsky 1999 p. 578). |
| Lubinsky–Máté–Nevai 1987, Thm 5 (LIT-050) | PD-T014/PD-T022/PD-T024 (upper) | arbitrary cos θ_j incl. ±1, min gap δ | Christoffel λ_n(w,y_j) | ℓ^p(λ) | L^p(w) | degree ≤ ln | C{1+(nδ)^{−1}}, unspecified; C may depend on l | RELATED: **forward** inequality; for each fixed l, at CC it gives λ_+(N,n)≤C_l (unspecified) for n≤lN. That is uniform boundedness only, not the threshold 2, not 1+ρ, not 2−4/N+4/N². Consistent with PD-T016. |
| Lubinsky–Máté–Nevai 1987 (LIT-050) | PD-T017/018/023 (lower) | — | — | — | — | — | — | RELATED (no converse inequality). |
| Askey 1972 journal (LIT-062) | PD-T017/018 | Gauss zeros of Jacobi | — | ‖f‖_∞ | L^p Jacobi | Π_{n−1} | p<4(α+1)/(2α+1) | RELATED, DIFFERENT SETTING. |
| Smith 1986 (LIT-065) | PD-T017/018 | zeros of (1−x²)Q_n (Lobatto); CC for ρ=(1−x²)^{1/2} | — | ‖f‖_∞ | L²(ρ/(1−x²)) = Chebyshev weight at CC | Π_{n+1} | uniformly bounded C→L² | RELATED, DIFFERENT SETTING (uniform input, Chebyshev measure). |
| Erdős–Feldheim 1936 (LIT-061) | PD-T017/018 | Chebyshev abscissae | — | ‖f‖_∞ | L^p Chebyshev measure | — | convergence | RELATED, DIFFERENT SETTING. The preceding note is identified as Feldheim alone, C. R. 203 (1936) 650–652 (unread, low priority). |
| Sloan–Smith 1978 (LIT-047) | PD-T017/018/022/024 | cos(iπ/n) | product weights (CC for k≡1) | C[−1,1] functional (Σ|w|) | — | Π_n | lim Σ|w_ni|=∫|k| | RELATED, DIFFERENT SETTING (no quadratic form). |
| Sloan–Smith 1980 (LIT-048) | all | same | same | — | — | — | error estimates for smooth f | RELATED, DIFFERENT SETTING. Complete text keyword- and section-screened in response-01: §§1–5 (formulas, implementation, heuristic error estimates "rather than rigorous error bounds", numerical tables); no theorem statement at all. |
| Lubinsky 1998 survey (LIT-052) | PD-T017/018 | Gauss (Freud, generalized Jacobi) | Christoffel | ℓ^p | L^p | Π_{n−1} | conditions only | RELATED, DIFFERENT SETTING: a genuine nodal-norm (converse quadrature-sum) result, Thm 3.3, but at Gauss nodes and weights (audit-01 F2). Points to Xu II (read: LIT-296). |
| Xu 1994 II, Thms 3.2/3.4 (LIT-296), Xu 1993 I | PD-T017/018 | Gauss zeros of generalized Jacobi p_n(dα) | λ_kn(dα)u_n | weighted ℓ^p | L^p(dβ) | Π_{n−1} | sufficient conditions; sharpness open (Remark 3.1) | RELATED, DIFFERENT SETTING: (3.2c) fails for U-nodes with Lebesgue measure at p=2 (same borderline as LIT-293). |
| Nevai 1990 letter (LIT-063 addendum) | PD-T017/018 | — | — | — | — | — | — | RELATED: justifies a step of Nevai III (Widom's proof); no change to its theorems. |
| Sloan–Smith 1982, Thms 5–7 (LIT-297); Smith–Sloan 1980 (LIT-298) | all | general / Jacobi zeros | product weights | C[−1,1] | L^q | — | equivalence with uniform-input mean convergence | RELATED, DIFFERENT SETTING. |
| Mastroianni–Milovanović 2008 ch. 2/4/5 (LIT-049) | PD-T017/018 | various | — | uniform | uniform | — | Lebesgue constant ≍log n | RELATED, DIFFERENT SETTING (uniform-norm operator). |
| Widom 1966 (LIT-053) | PD-T017/018 | — | — | ℓ² coefficients | — | infinite/finite Hankel | largest eigenvalues, counting | RELATED, DIFFERENT SETTING. |
| Widom–Wilf 1966 (LIT-054) | PD-T017/018 | — | — | monomial coefficients | moments of α | H_N | exponentially small, three regimes (exponent change in a boundary case; erratum unread) | RELATED, DIFFERENT SETTING (standard eigenproblem for monomial moments, not a basis-invariant Gram pencil). |
| Don–Gottlieb ICASE 93-40 (LIT-058) | PD-T017 | Chebyshev–Lobatto data, Legendre–Gauss–Lobatto ghost points | GLL weights | nodal quadratic form H = pullback of the **discrete GLL energy** (audit-01 N3) | GLL quadrature, exact only through degree 2N−1, so not ∫p² for every p∈Π_N | Π_N | identity, no constants | RELATED, DIFFERENT SETTING. |
| Niu–Liao–Ma–Wu 2021, Mathematics 9, 3271, Lemma 1 (LIT-295, new) | PD-T017 | CGL x_j=cos(jπ/N) | — | H¹ / H^σ input | L²(dx) | Π_N | C N^{−σ}, no log | RELATED, DIFFERENT SETTING (Sobolev input). |
| An–Sommariva–Vianello, arXiv v1 and published MCS 252 (LIT-045) | PD-T014/017/018/022/024/T028 | CC, Padua | rule weights | — | L²(μ) | finite n≤30, m≤20 | numerical η; Thm 2.1: Gaussian rules η≥1 for n≥k | RELATED: numerical predecessor. The published version (p. 738) says the CC behaviour beyond half-exactness is, to the authors' knowledge, "not known" and "could deserve further study". |
| ASV eq. (7) (LIT-045) | PD-T025 | general | positive | — | L²(μ) | — | factor 1+√(1+η) | RELATED: generic upper-Gram mechanism already in ASV (as recorded before); our CC constant is an application. |
| An–Wu 2022 published (LIT-046) | PD-N004 | m-point CC, n+2≤m≤2n+1 | CC | — | L²(dx) | Π_n | assumes η=3/4 | Unchanged: conditional corollary; PD-N004 refutes the assumption at m=n+2=513 and does not refute the implication. |
| Mastroianni–Milovanović–Notarangelo 2012, Cor. 2.2 / Thm 2.3 (LIT-299, new; audit-01 lead) | PD-T017/018/019 | zeros of p_m(v^α) **plus ±1** (r=1: Lagrange at Jacobi zeros and ±1; α=1/2 gives the CC nodes, N=m+1) | Δx_k or Christoffel λ_m(v^{γp},x_k) + endpoint term σ_m(P)/m^{2γ+2/p} | weighted ℓ^p incl. endpoint values | L^p(v^{γp}) | P∈P_{m+2r−1}=Π_N for r=1 | iff −1/p<r+γ−α/2−1/4<1/q; no rate | **RELATED, closest classical statement.** At α=1/2, γ=0, r=1, p=2 the middle term equals 1/q, the excluded endpoint. By translation.md T6, inf_N λ_−(N,N)=0 at CC nodes is classical (conditional on the source's necessity part). This is a weaker, qualitative full-space consequence of PD-T018/PD-T019. It gives no rate, no limit along every N, and nothing on Π_{N−1}. |
| Forward citations 2010–2026 (group-C screen; Wu arXiv 2606.23409; An–Hu–Yuan arXiv 2608.00525; An–Ran–Wu arXiv 2510.04904) | all | — | — | — | — | — | — | *no matching result found in the documented search* (abstract-level screen; Wu, Appl. Math. Lett. 182 (2026) 110033 unread). |

## PD-T019 note (not in the original target list; rewritten per audit-01 F4)

Separate assertions:
1. **Classical, exact CC/Lobatto setting, qualitative, full space.** Mastroianni–Milovanović–Notarangelo 2012 Cor. 2.2 (necessity part; LIT-299) implies inf_N λ_−(N,N)=0 at the CC nodes on Π_N (translation.md T6). This is failure of a uniform bound (an unbounded subsequence of ‖L_N‖_N), not a limit, rate or degree-(N−1) statement.
2. **Classical, analogous settings.**
   - Mastroianni–Russo Thm 2.7 (LIT-293) and Xu (LIT-296): Gauss nodes without endpoint terms, mixed weights.
   - König–Nielsen (LIT-294): same-weight Jacobi; for U-nodes the borderline is p=3 with weight √(1−x²), giving (log n)^{1/3} test growth.
   These show the same kind of borderline failure but do not by themselves establish the CC statement.
3. **Ours (exact CC evaluation).** PD-T019 evaluates U_{N−1} exactly. Its interior nodal values vanish, so Q_N(U_{N−1}²)=O(1) while ∫U_{N−1}²≍log N. This gives λ_−(N,N−1)≲1/log N for every N, and PD-T018 sharpens it to (log N)^{−2}.
   - The growth ∫U_m²dx≍log m is an elementary computation.
   - Its use as the CC witness and the degree-(N−1), every-N conclusions are attributed to the manuscript, not to the cited sources.

## Answer to the priority question: is the endpoint log rate classical?

- **Qualitative full-space failure at CC nodes: classical** (assertion 1 above), conditional on the source's necessity part, which was not proof-audited.
- **Every-N limit on Π_{N−1}, the 1/log N witness rate and the two-sided (1+log N)^{−2} order: no matching result found in the documented search.**
  - Read: Nevai III (+1990 letter), Askey, Lubinsky 1999, Mastroianni–Russo 1999, Mastroianni–Totik, König–Nielsen, Smith, Lubinsky survey, Mastroianni–Milovanović book (ch. 2/4/5), Xu I/II, Lubinsky–Máté–Nevai, Sloan–Smith 1978/80/82, Smith–Sloan 1980, Mastroianni–Milovanović–Notarangelo 2012, published ASV, and the forward-citation screen.
  - The published ASV states that the CC behaviour beyond half-exactness is not known theoretically.
- **Fixed ratio:** Mastroianni–Totik gives nothing beyond exactness in its documented form (T4). No explicit beyond-half-exactness constants were found.
- **Upper side:** Lubinsky–Máté–Nevai gives classical boundedness λ_+≤C_l. No threshold below 2 was found.
- **Still unread:** Mastroianni–Russo 2000 (Hadronic Press), Della Vecchia–Mastroianni–Vértesi 1995, Wu AML 2026, Feldheim C. R. 203 p. 650. Mastroianni–Russo 2000 is the most likely remaining place for a quantitative borderline statement.
