# mz-prior-art-2026-additions — converse-MZ and forward-citation sources added by topic mz-prior-art-20261101

- Access/reading date: 2026-11-01. Reader: Claude, Opus 5.5 (orchestrator). Rules `9739a0c`.
- No PDF or fulltext extract is stored in the repository. Comparison and translations: [comparison.md](../../topics/mz-prior-art-20261101/comparison.md), [translation.md](../../topics/mz-prior-art-20261101/translation.md).

## Extracted published statements

### LIT-293 — Mastroianni–Russo 1999, inverse Marcinkiewicz inequalities at zeros

- Citation: G. Mastroianni, M. G. Russo, *Lagrange interpolation in weighted Besov spaces*, Constr. Approx. 15 (1999) 257–289, DOI <https://doi.org/10.1007/s003659900107>.
- Coverage: publisher PDF (33 pp., text layer) via AC's NTNU access in the built-in browser. Pp. 257–264 read in full (introduction, §2.1 GDT weights, Lemma 2.5, §2.5 Theorems 2.6–2.7, start of §3, Theorem 3.1). The rest was keyword-screened, including the proof of Theorem 2.7 necessity (pp. 275–276) and the reference list.
- Statement (Theorem 2.7, p. 263): let w, σ, v∈GDT, σ∈L^p, 1<p<∞, v:=max{σ_−^p, √(wϕ)_−}, ϕ=√(1−x²). Then ‖Pσ‖_p^p≤C Σ_{i=1}^m λ_m(v;x_{m,i}(w))|P(x_{m,i}(w))|^p for all P∈Π_{m−1}, m≥1, iff σ/√(wϕ)∈L^p (2.22). Moreover, ‖Pσ‖_p^p≤C Σ λ_m(σ^p;x_{m,i}(w))|P(x_{m,i}(w))|^p iff (2.22) and √(wϕ)/σ∈L^{p′} (2.24). The nodes are the zeros of p_m(w) (Gauss); C is independent of m and P. The authors note that Xu (1994, [37]) gave sufficient conditions, and that for Jacobi w and σ=w^{1/p} the equivalence is due to König–Nielsen [15]. Theorem 2.6 (p. 262) is the direct inequality at general points y_k=cos ϑ_k including ±1.
- Necessity mechanism (p. 275): (2.23) ⇒ ‖L_m(w)‖_{L∞→L^p_σ}<∞ ⇒ ‖p_m(w)σ‖_p≤C, via Shi / Mastroianni–Vértesi / Nevai III Thm 6.
- Relation: see comparison.md. At the zeros of U_{N−1} (interior CC nodes), with σ≡1 and p=2, (2.22) fails because ∫(1−x²)^{−1}dx=∞. This gives qualitative failure of a uniform converse inequality on Π_{N−2} without endpoint nodes, with no rate. **RELATED, DIFFERENT SETTING** for PD-T017/018. It is the closest classical statement found.

### LIT-294 — König–Nielsen, Jacobi-node MZ characterization

- Citation: H. König, N. J. Nielsen, *Vector-valued L_p-convergence of orthogonal series and Lagrange interpolation*, Forum Math. 6 (1994) 183–207 (citation as given in Mastroianni–Russo 1999, ref. [15]; DOI not verified here). Preprint: arXiv:math/9208201v1 (13 Aug 1992), <https://arxiv.org/abs/math/9208201>.
- Coverage: arXiv v1 read through WebFetch extraction (paraphrase-level; inequality signs partly garbled). Journal version not compared.
- Statement (Theorem 1): for Jacobi weight w_{αβ} with n+1 nodes at the zeros of p_{n+1}^{(α,β)} and Christoffel numbers λ_j, the converse inequality (∫‖q‖^p w_{αβ})^{1/p}≤c(Σλ_j‖q(t_j)‖^p)^{1/p} on Π_n(X) holds iff X is UMD and μ(α,β)<p<M(α,β), with M=4(α+1)/(2α+1) for α>−1/2. At p=M, test norms grow like (log n)^{1/p} while the discrete side stays bounded (eqs. (18)–(19)).
- Relation: nodes, weights and continuous measure come from the same Jacobi weight. Our CC problem mixes nodes of (1−x²)^{1/2} with Lebesgue measure. **RELATED, DIFFERENT SETTING.**

### LIT-295 — Niu–Liao–Ma–Wu 2021, CGL interpolation in the Legendre norm

- Citation: Niu, Liao, Ma, Wu, *Approximation properties of Chebyshev polynomials in the Legendre norm*, Mathematics 9(24) (2021) 3271, DOI <https://doi.org/10.3390/math9243271> (open access, CC BY).
- Coverage: article page read through WebFetch extraction (paraphrase-level).
- Statement: Lemma 1, eqs. (2)–(3), attributed to Ma (SINUM 1998) and Wu–Ma–Li (NMPDE 2009): for Chebyshev–Gauss–Lobatto interpolation at cos(jπ/N), N‖I_Nu−u‖+‖∂_xI_Nu‖≤C‖∂_xu‖ (u∈H¹) and ‖I_Nu−u‖_{H^l}≤CN^{l−σ}‖u‖_{H^σ}, σ>1/2, in unweighted norms. Lemma 2 is CC quadrature error. No log factors; no discrete ℓ² inequality.
- Relation: Sobolev-input interpolation bounds. **RELATED, DIFFERENT SETTING** for PD-T017/018 (a forward-citation hit, abstract-ranked first by the group-C worker).

## Search and attribution notes

- Forward-citation screen (group-C worker, Sonnet 5.5 high, 2026-11-01): Semantic Scholar citing lists for An–Wu (24), Sloan–Smith 1978 (67, 25 from 2010 on), Nevai III (first three pages of 244), ASV (0; also 0 in Crossref/OpenAlex). OpenAlex list endpoint failed. Hits were screened at abstract level. No 2010–2026 paper proving all-N CC/Lobatto Gram, MZ or ℓ²→L² bounds was found.
- Ranked leads:
  - Niu et al. (LIT-295);
  - An–Hu–Yuan arXiv:2608.00525 (sphere);
  - Wu arXiv:2606.23409 (sup-norm Lebesgue constants of perturbed Chebyshev–Lobatto nodes, abstract read);
  - Wu, Appl. Math. Lett. 182 (2026) 110033, DOI 10.1016/j.aml.2026.110033 (unread, on AC's list);
  - An–Ran–Wu survey arXiv:2510.04904.
- Literal queries are in scratchpad worker reports, summarized in the topic LOG.
- Not exhaustive.

## History

2026-11-01: created for topic mz-prior-art-20261101; LIT-293–295 allocated through the batch ledger.
