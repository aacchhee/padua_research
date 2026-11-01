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
- Statement (Theorem 1): for Jacobi weight w_{αβ} with n+1 nodes at the zeros of p_{n+1}^{(α,β)} and Christoffel numbers λ_j, the converse inequality (∫‖q‖^p w_{αβ})^{1/p}≤c(Σλ_j‖q(t_j)‖^p)^{1/p} on Π_n(X) holds iff X is UMD and μ(α,β)<p<M(α,β). The upper endpoint is set by a=max(α,β): M=4(a+1)/(2a+1) when a>−1/2. The α-only form used in the necessity proof (p. 15) assumes α≥β; for example α=0, β=1 gives M=8/3, not 4. Corrected 2026-11-01 per audit-01 F3, which checked the primary pp. 3–4, 15. At p=M, test norms grow like (log n)^{1/p} while the discrete side stays bounded (eqs. (18)–(19)).
- Relation: nodes, weights and continuous measure come from the same Jacobi weight. For U-nodes (α=β=1/2) the critical exponent is p=M=3 with weight √(1−x²); at p=2 the same-weight Gaussian quadratic form is exact. Our CC problem mixes nodes of (1−x²)^{1/2} with Lebesgue measure. **RELATED, DIFFERENT SETTING**, an analogous borderline mechanism only (audit-01 F4).

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

2026-11-01: created for topic mz-prior-art-20261101; LIT-293–295 allocated through the batch ledger; LIT-296 added after AC supplied Xu I/II (LIT-297–298 live in the Sloan–Smith record).

### LIT-296 — Xu 1994 (Part II), converse MZ inequality at generalized Jacobi zeros; with Part I context

Reader: Claude, Opus 5.5. Access: PDF supplied by AC in Downloads\\padua\\papers (2026-11-01, NTNU access), staged to the session; text via pdftotext, or tesseract OCR for image-only scans (Xu I/II). Read in the session only; nothing stored in Git. Rules `9739a0c`.

- Citations: Y. Xu, *Mean convergence of generalized Jacobi series and interpolating polynomials, II*, J. Approx. Theory 76 (1994) 77–92, DOI 10.1006/jath.1994.1006; Part I, J. Approx. Theory 72 (1993) 237–251, DOI 10.1006/jath.1993.1019.
- Coverage: Part II pp. 77–87 read via OCR (§§1–3 complete, start of §4), §4 theorem statements screened. Part I keyword-screened via OCR (Theorem 4.1, Remark 4.1, Lemma 3.6).
- Statement (Part II, Theorem 3.2, p. 82): for P∈Π_{n−1}, 1<p<∞, generalized Jacobi distributions dα, dβ and u∈GJ with (3.2a)–(3.2c), ‖P‖_{dβ,p}≤c(Σ_k|P(x_kn(dα))|^p u_n(x_kn)λ_kn(dα))^{1/p} at the **Gauss** zeros of p_n(dα). The decisive condition (3.2c) is (α′√(1−x²))^{−p/2}β′∈L¹. Theorem 3.4 (pp. 85–86) reduces the conditions to (3.12) by choosing u. Remark 3.1 (p. 87): sharpness of the conditions is not clear. Part I Theorem 4.1: weighted partial-sum bounds (necessity of (4.4) from Máté–Nevai–Totik). Part I Lemma 3.6 contains a log T factor in an auxiliary Hardy-type estimate, not an interpolation-norm rate.
- Relation: with α′=(1−x²)^{1/2} (interior CC nodes), β′≡1 and p=2, (3.2c) requires (1−x²)^{−1}∈L¹, which fails. These are sufficient conditions at Gauss nodes; the same borderline as LIT-293. **Verdict: RELATED, DIFFERENT SETTING** for PD-T017/018.

### LIT-299 — Mastroianni–Milovanović–Notarangelo 2012, Lagrange–Hermite interpolation at Jacobi zeros plus ±1 (added in response-01; audit-01 lead)

- Citation: G. Mastroianni, G. V. Milovanović, I. Notarangelo, *On an interpolation process of Lagrange–Hermite type*, Publ. Inst. Math. (Beograd) (N.S.) 91(105) (2012) 163–175, DOI <https://doi.org/10.2298/PIM1205163M>; author PDF <https://www.mi.sanu.ac.rs/~gvm/radovi/n105p163.pdf>.
- Coverage: Claude, Opus 5.5, 2026-11-01. Author PDF loaded in AC's built-in browser and its text layer read for pp. 163–167, covering the definition, (2.1)–(2.11), Theorems 2.1–2.3, Proposition 2.1, Corollaries 2.1–2.2 and the Christoffel remark; the reference list was keyword-checked. The page image of p. 164 was viewed: it shows "r ⩾ 1" and "γ ⩾ 0", which the text layer renders as ">". Proofs (§3) were not audited.
- Statements:
  - Process: L_{m,r}(v^α,f) interpolates at the zeros of p_m(v^α), v^α=(1−x²)^α, α>−1, and matches f^{(j)}(±1) for j<r, with r⩾1 an integer (p. 163–164). For r=1 it is Lagrange interpolation at the zeros together with ±1.
  - Theorem 2.3 (p. 166): for 1<p<∞, γ⩾0, ‖L_{m,r}(v^α,f)v^γ‖_p≤C{(Σ_kΔx_k|fv^γ|^p(x_k))^{1/p}+σ_m(f)/m^{2γ+2/p}} iff −1/p<γ+r−α/2−1/4<1/q.
  - Corollary 2.2 (p. 167): for P∈P_{m+2r−1}, ‖Pv^γ‖_p∼(Σ_kΔx_k|Pv^γ|^p(x_k))^{1/p}+σ_m(P)/m^{2γ+2/p}, with constants independent of m and P, iff the same strict two-sided condition holds.
  - Supporting remarks (p. 167): the reverse direction (nodal ≲ continuous) holds for all α>−1, γ⩾0, r⩾1, 1≤p<∞, citing Nevai III p. 675 together with Markov, Schur and Nikol'skiĭ. The Δx_k sum may be replaced by Christoffel weights λ_m(v^{γp},x)∼v^{γp}(x)√(1−x²)/m.
  - Theorem 2.1 (p. 165) is the uniform-norm analogue, with a log m factor.
- Relation: specialized in topics/mz-prior-art-20261101/translation.md T6 (α=1/2, r=1, γ=0, p=2, where the middle term equals 1/q). The necessity part then gives inf_N λ_−(N,N)=0 at the CC nodes on the full space Π_N. That is qualitative (an unbounded subsequence), with no rate and nothing on Π_{N−1}. It is the closest classical statement found. **Verdict: RELATED** to PD-T017/018/019: it implies only a weaker qualitative consequence of PD-T018/PD-T019. It is conditional on the source's unaudited necessity proof.
