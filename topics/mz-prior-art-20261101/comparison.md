# Source-by-claim comparison — CC / Padua MZ manuscript

Claude (Opus 5.5), 2026-11-01, rules `9739a0c`. Literature verdicts only. **No PD status changes** (AGENTS.md / WORKFLOW: literature verdicts never change a PD status). Translations are proved in [translation.md](translation.md) (T1: λ_−(N,n)=1/‖L_N‖_n² for the CC-weighted nodal ℓ²→L²(dx) norm; T3: ½Δ_N(x_k)≤w_k≤5Δ_N(x_k); T4: Mastroianni–Totik at CC nodes; T5: Lubinsky's excluded borderline).

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
| Mastroianni–Russo 1999, Thm 2.7 (LIT-293, new) | PD-T017/018 | zeros of p_m(w), w∈GDT | λ_m(v;x) or λ_m(σ^p;x) | weighted ℓ^p | L^p(σ^p) | P∈Π_{m−1} | iff σ/√(wϕ)∈L^p (and √(wϕ)/σ∈L^{p′}) | RELATED, DIFFERENT SETTING. At the interior CC nodes (zeros of U_{N−1}, w=(1−x²)^{1/2}), σ≡1, p=2 the condition requires (1−x²)^{−1/2}∈L², which fails (log divergence). It yields failure of a uniform converse inequality on Π_{N−2} without endpoint nodes. It gives no rate, no CC endpoint terms, no degree-(N−1) Lobatto witness. Its necessity proof uses ‖p_m(w)σ‖_p≲‖L_m‖, the classical U-polynomial mechanism (see the PD-T019 note below). |
| König–Nielsen 1994 / arXiv math/9208201 Thm 1 (LIT-294, new) | PD-T017/018 | zeros of p_{n+1}^{(α,β)} (Gauss) | Christoffel numbers of the same weight | ℓ^p(λ) | L^p(w_{αβ}) (same weight) | Π_n | iff p in (μ,M); at p=M test norms grow like (log n)^{1/p} | RELATED, DIFFERENT SETTING: nodes, weights and measure all from one Jacobi weight. Our case mixes nodes from (1−x²)^{1/2} with Lebesgue measure. |
| Lubinsky 1999, Thms 1.1–1.7 (LIT-064) | PD-T017 | arbitrary ordered nodes incl. endpoints | local cardinal integrals + δ_jω(t_j)^p/[δ_j|π′(t_j)|]^p | weighted ℓ^p | L^p(ν^p) | Π_{n−1} | constant C(σ,…), σ in the open range (−1/p,1−1/p) | RELATED, DIFFERENT SETTING: the CC/Lebesgue case is the excluded endpoint σ=1/2 (translation.md T5). |
| Lubinsky 1999 (LIT-064) | PD-T018 | — | — | — | — | — | upper-type inequality only | RELATED (gives no lower bound on the norm). |
| Mastroianni–Totik 2000, §7 algebraic Marcinkiewicz inequality (LIT-051) | PD-T023/PD-T024 (lower) | any x_j=cos ξ_j with ±1, gaps ≤1/(Mn) | Δ_n(x_j)w_n(x_j) | weighted ℓ^p | L^p(w), doubling w | Π_n with n≤N/(πM) at CC | unspecified M, C | **IMPLIES PART**: λ_−(N,n)≥1/(8π²M²C) for n≤N/(πM), N≥2πM (translation.md T4). Not every θ<1, not explicit. |
| Mastroianni–Totik 2000 (LIT-051) | PD-T022 | same | same | — | — | n≤cN | converse with C_M, no value | RELATED: no upper constant <2, and for n≤N/2 exactness already gives 1. |
| Mastroianni–Totik 2000 (LIT-051) | PD-T017/018 | — | — | — | — | n≍N excluded | — | RELATED, DIFFERENT SETTING (degree ≤εn only; cf. Lubinsky 1999 p. 578). |
| Lubinsky–Máté–Nevai 1987 (LIT-050) | PD-T023/024, PD-T017 | — | — | — | — | — | — | **FULLTEXT UNVERIFIED** (on AC's missing list). |
| Askey 1972 journal (LIT-062) | PD-T017/018 | Gauss zeros of Jacobi | — | ‖f‖_∞ | L^p Jacobi | Π_{n−1} | p<4(α+1)/(2α+1) | RELATED, DIFFERENT SETTING. |
| Smith 1986 (LIT-065) | PD-T017/018 | zeros of (1−x²)Q_n (Lobatto); CC for ρ=(1−x²)^{1/2} | — | ‖f‖_∞ | L²(ρ/(1−x²)) = Chebyshev weight at CC | Π_{n+1} | uniformly bounded C→L² | RELATED, DIFFERENT SETTING (uniform input, Chebyshev measure). |
| Erdős–Feldheim 1936 (LIT-061) | PD-T017/018 | Chebyshev abscissae | — | ‖f‖_∞ | L^p Chebyshev measure | — | convergence | RELATED, DIFFERENT SETTING. The preceding note is identified as Feldheim alone, C. R. 203 (1936) 650–652 (unread, low priority). |
| Sloan–Smith 1978 (LIT-047) | PD-T017/018/022/024 | cos(iπ/n) | product weights (CC for k≡1) | C[−1,1] functional (Σ|w|) | — | Π_n | lim Σ|w_ni|=∫|k| | RELATED, DIFFERENT SETTING (no quadratic form). |
| Sloan–Smith 1980 (LIT-048) | all | same | same | — | — | — | error estimates for smooth f | RELATED, DIFFERENT SETTING (pp. 389–401 unread). |
| Lubinsky 1998 survey (LIT-052) | PD-T017/018 | Gauss (Freud, generalized Jacobi) | Christoffel | ℓ^p | L^p | Π_{n−1} | conditions only | RELATED; points to Xu II (pp. 82–83), unread. |
| Mastroianni–Milovanović 2008 ch. 2/4/5 (LIT-049) | PD-T017/018 | various | — | uniform | uniform | — | Lebesgue constant ≍log n | RELATED, DIFFERENT SETTING (uniform-norm operator). |
| Widom 1966 (LIT-053) | PD-T017/018 | — | — | ℓ² coefficients | — | infinite/finite Hankel | largest eigenvalues, counting | RELATED, DIFFERENT SETTING. |
| Widom–Wilf 1966 (LIT-054) | PD-T017/018 | — | — | monomial coefficients | moments of α | H_N | λ_N ≍ N^{1/2}σ^{−2N} | RELATED, DIFFERENT SETTING (standard eigenproblem in a non-orthogonal basis). |
| Don–Gottlieb ICASE 93-40 (LIT-058) | PD-T017 | Chebyshev–Lobatto data, Legendre–Gauss–Lobatto ghost points | GLL weights | nodal quadratic form H | L²(dx) via GLL exactness | Π_N | identity, no constants | RELATED, DIFFERENT SETTING. |
| Niu–Liao–Ma–Wu 2021, Mathematics 9, 3271, Lemma 1 (LIT-295, new) | PD-T017 | CGL x_j=cos(jπ/N) | — | H¹ / H^σ input | L²(dx) | Π_N | C N^{−σ}, no log | RELATED, DIFFERENT SETTING (Sobolev input). |
| An–Sommariva–Vianello arXiv v1 (LIT-045) | PD-T022/024/T028 | CC, Padua | rule weights | — | L²(μ) | finite n≤30, m≤20 | numerical η | RELATED (numerical predecessor; known since the MZ campaign). Published MCS version **FULLTEXT UNVERIFIED** (on AC's list). |
| ASV eq. (7) (LIT-045) | PD-T025 | general | positive | — | L²(μ) | — | factor 1+√(1+η) | RELATED: generic upper-Gram mechanism already in ASV (as recorded before); our CC constant is an application. |
| An–Wu 2022 published (LIT-046) | PD-N004 | m-point CC, n+2≤m≤2n+1 | CC | — | L²(dx) | Π_n | assumes η=3/4 | Unchanged: conditional corollary; PD-N004 refutes the assumption at m=n+2=513 and does not refute the implication. |
| Forward citations 2010–2026 (group-C screen; Wu arXiv 2606.23409; An–Hu–Yuan arXiv 2608.00525; An–Ran–Wu arXiv 2510.04904) | all | — | — | — | — | — | — | *no matching result found in the documented search* (abstract-level screen; Wu, Appl. Math. Lett. 182 (2026) 110033 unread). |

## PD-T019 note (not in the original target list)

The classical U-polynomial mechanism, ‖U_m‖²_{L²(dx)}=∫_0^π sin²((m+1)θ)/sinθ dθ ≍ log m, drives the necessity half of Mastroianni–Russo Thm 2.7 (via ‖p_m(w)σ‖_p≲‖L_m(w)‖) and the borderline examples of König–Nielsen and Nevai III. PD-T019's exact U witness (reciprocal-log quotient) is therefore a known mechanism. The manuscript should present it as a classical ingredient and claim only the exact CC evaluation.

## Answer to the priority question: is the endpoint log rate classical?

- **Qualitative part: classical.** Failure of a uniform converse (nodal-ℓ²→L²) inequality at Chebyshev/Lobatto-type nodes with Lebesgue measure follows from Mastroianni–Russo 1999 Thm 2.7 (and König–Nielsen-type borderline examples), via the √(log)-growth of U-polynomials. This gives λ_−→0 in the corresponding Gauss-node setting, but not literally with CC endpoint weights.
- **Order law: no matching result found in the documented search.** Read so far: Nevai III, Askey, Lubinsky 1999, Mastroianni–Russo 1999, Mastroianni–Totik, König–Nielsen, Smith, the Lubinsky survey, the Mastroianni–Milovanović book (ch. 2/4/5) and the forward-citation screen. None gives the two-sided order λ_−(N,N−1)≍(1+log N)^{−2} with CC weights and Lebesgue measure. None gives the PD-T018 log² witness inside Π_{N−1}.
- **Still unread** (AC's missing list): Xu I/II, Nevai 1990, Lubinsky–Máté–Nevai 1987, Mastroianni–Russo 2000 (Hadronic), Della Vecchia–Mastroianni–Vértesi 1995. Xu II and Mastroianni–Russo 2000 are the most likely places for a quantitative borderline statement.
