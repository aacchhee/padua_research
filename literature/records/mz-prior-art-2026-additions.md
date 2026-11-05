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

- Citation: H. König, N. J. Nielsen, *Vector-valued L_p-convergence of orthogonal series and Lagrange interpolation*, Forum Math. 6 (1994) 183–207 DOI 10.1515/form.1994.6.183 verified via Crossref (p2-links) and the publisher page (2026-11-03); pages 183–207 confirmed on the publisher page.. Preprint: arXiv:math/9208201v1 (13 Aug 1992), <https://arxiv.org/abs/math/9208201>.
- Coverage: arXiv v1 pp. 1–4, 13–17 read directly from the PDF text layer (2026-11-03, Claude Opus 5.5 high); earlier WebFetch extraction superseded for these items. Journal version: only the publisher preview of p. 183 was readable (matches arXiv pp. 1–2); journal body not accessible (De Gruyter 'Unlicensed'), so journal-vs-arXiv comparison of Theorem 1 and eqs. (18)–(19) remains open.
- Statement (Theorem 1): for Jacobi weight w_{αβ} with n+1 nodes at the zeros of p_{n+1}^{(α,β)} and Christoffel numbers λ_j, the converse inequality (∫‖q‖^p w_{αβ})^{1/p}≤c(Σλ_j‖q(t_j)‖^p)^{1/p} on Π_n(X) holds iff X is UMD and μ(α,β)<p<M(α,β). The upper endpoint is set by a=max(α,β): M = 4(a+1)/(2a+1) when a = max(α,β) > −1/2, and M = ∞ when a ≤ −1/2; the lower endpoint is μ = 4(a+1)/(2a+5) when a > 1/2 and μ = 1 otherwise (arXiv p. 3). The α-only form used in the necessity proof (p. 15) assumes α≥β; for example α=0, β=1 gives M=8/3, not 4. Corrected 2026-11-01 per audit-01 F3, which checked the primary pp. 3–4, 15. At p=M, test norms grow like (log n)^{1/p} while the discrete side stays bounded (eqs. (18)–(19)).
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
  - Supporting remarks (p. 167): the reverse direction (nodal ≲ continuous) holds for all α>−1, γ⩾0, r⩾1, 1≤p<∞, citing Nevai III p. 675 together with Markov, Schur and Nikol'skiĭ. The Δx_k sum may be replaced by Christoffel weights λ_m(v^{γp},x_k)∼v^{γp}(x_k)√(1−x_k²)/m, an estimate at the interior zeros x_k only (not at ±1, where λ_m(1,±1)≍m^{−2}; corrected per audit-02 E1).
  - Theorem 2.1 (p. 165) is the uniform-norm analogue, with a log m factor.
- Relation: specialized in topics/mz-prior-art-20261101/translation.md T6 (α=1/2, r=1, γ=0, p=2, where the middle term equals 1/q). The necessity part then gives inf_N λ_−(N,N)=0 at the CC nodes on the full space Π_N. That is qualitative (an unbounded subsequence), with no rate and nothing on Π_{N−1}. It is the closest classical statement found. **Verdict: RELATED** to PD-T017/018/019: it implies only a weaker qualitative consequence of PD-T018/PD-T019. It is conditional on the source's unaudited necessity proof.

## 2026-11-03 primary arXiv re-reading and journal access — padua-literature-20261103

# Addendum to mz-prior-art-2026-additions, LIT-294 (König–Nielsen) — journal access attempt and primary arXiv re-reading

H. König, N. J. Nielsen, *Vector-valued L_p-convergence of orthogonal series and Lagrange interpolation*, Forum Math. 6 (1994) 183–207, DOI <https://doi.org/10.1515/form.1994.6.183>; journal page <https://www.degruyter.com/document/doi/10.1515/form.1994.6.183/html> (redirects to degruyterbrill.com); preprint arXiv:math/9208201v1 (13 Aug 1992), <https://arxiv.org/abs/math/9208201>.

- Access and reading date: 2026-11-03. Reader: Claude, Opus 5.5, high. Rules `af1ac9fde6b23cb9cd826a33d5611680566c52cb`.
- **Journal body: NOT read.** The De Gruyter Brill article page reported the item as "Unlicensed" in AC's built-in browser; the PDF request was redirected to an unauthorized-download page. No institutional login was attempted (credential entry is outside the reader's permissions). The journal body therefore remains a gap; the item is for AC's download list (journal page above).
- What the journal page did show: the publisher's preview of journal p. 183 (title, authors, communicating editor, abstract, MSC 46E40/42C15, the first paragraph of §1 defining UMD spaces, and the two grant footnotes). This preview matches arXiv v1 pp. 1–2 in all inspected wording and footnote grant numbers. Pages 183–207 are confirmed by the publisher page ("Forum Math. 6 (1994), 183-207"); the arXiv abstract page carries the same journal reference. The publisher title is written "Vector-valued Lp-convergence" with a hyphen (matching the repo's citation); the arXiv listing title has no hyphen, the arXiv PDF title has one.
- arXiv v1 re-read directly (publisher-independent primary text, full PDF text layer via pdf.js in the browser, 33 pp.): pp. 1–4 (introduction, Theorem 1, Theorem 2 statement), pp. 13–17 (necessity proof of Theorem 1(b) including eqs. (15)–(20), Remarks (1)–(2), Proposition 9). Earlier repo coverage was WebFetch extraction; this reading replaces it for the items below.

## LIT-294 — corrected and confirmed statement (arXiv v1 locators; journal locators unknown)

- Theorem 1 (arXiv pp. 3–4). Setting: Banach space X, Jacobi weight w_{αβ}(t) = (1−t)^α(1+t)^β with α, β > −1, nodes t_j = zeros of the orthonormal Jacobi polynomial p_{n+1}^{(α,β)}, Gaussian weights λ_j.
  - (a) Forward inequality on Π_{2n}(X) for all 1 ≤ p ≤ ∞, constant independent of n and p.
  - (b) Define μ(α,β) = max(1, 4(α+1)/(2α+5), 4(β+1)/(2β+5)) and m(α,β) = max(1, 4(α+1)/(2α+3), 4(β+1)/(2β+3)), and let M(α,β) be the conjugate exponent of m(α,β). The converse inequality (7) on Π_n(X), with constant independent of n, holds iff X is UMD and μ(α,β) < p < M(α,β).
- **Parameter restriction on max(α,β)** (the point of audit-01 F3, now confirmed from the primary formulas): since 4(a+1)/(2a+3) is increasing in a, m(α,β) is governed by a = max(α,β). If a ≤ −1/2 then m = 1 and M = ∞ (no upper restriction besides p < ∞). If a > −1/2 then M(α,β) = 4(a+1)/(2a+1). Likewise μ(α,β) > 1 iff a > 1/2, and then μ = 4(a+1)/(2a+5). The necessity proof (arXiv p. 15) explicitly reduces to α ≥ β "by symmetry" and treats α ≤ −1/2 as known; the α-only expression M = 4(α+1)/(2α+1) printed there is under that ordering. The corrected record text (a = max(α,β)) is therefore right; add the a ≤ −1/2 convention (M = ∞).
- Eqs. (18)–(19) (arXiv p. 15): test polynomial q = p_n^{(α,β)} (α ≥ β, α > −1/2). The continuous L^p(w_{αβ}) norm behaves like 1 for p < M, like (log n)^{1/p} at p = M, and grows like a positive power of n beyond M (18). The discrete λ-weighted norm at the zeros of p_{n+1} stays bounded for every p < ∞ when α ≤ 1/2, and for α > 1/2 up to the larger threshold 4(α+1)/(2α−1) (19). Hence (7) fails for p ≥ M. Eq. (20) (p. 16) gives the analogous lower-endpoint test with the first cardinal function ℓ₁.
- U-nodes check (α = β = 1/2): μ = 1, m = 3/2, M = 3. So the converse inequality holds for 1 < p < 3 and fails at p = 3 with (log n)^{1/3} growth. Unchanged from the record.
- **New item, Remark (1) (arXiv p. 16):** if the converse inequality is required only for polynomials of degree k ≤ n/2 (with the n+1 nodes of degree n+1), it holds for all 1 ≤ p ≤ ∞ and all Banach spaces, at least for α, β ≥ −1/2; the authors attribute this to boundedness of generalized de la Vallée Poussin means and give no detailed proof. They note that the p- and X-restrictions in Theorem 1 come from requiring the number of nodes to equal dim Π_n.

## Old → new corrections to the existing LIT-294 record text

- Old: "Coverage: arXiv v1 read through WebFetch extraction (paraphrase-level; inequality signs partly garbled). Journal version not compared."
- New: "Coverage: arXiv v1 pp. 1–4, 13–17 read directly from the PDF text layer (2026-11-03, Claude Opus 5.5 high); earlier WebFetch extraction superseded for these items. Journal version: only the publisher preview of p. 183 was readable (matches arXiv pp. 1–2); journal body not accessible (De Gruyter 'Unlicensed'), so journal-vs-arXiv comparison of Theorem 1 and eqs. (18)–(19) remains open."
- Old: "M=4(a+1)/(2a+1) when a>−1/2."
- New: "M = 4(a+1)/(2a+1) when a = max(α,β) > −1/2, and M = ∞ when a ≤ −1/2; the lower endpoint is μ = 4(a+1)/(2a+5) when a > 1/2 and μ = 1 otherwise (arXiv p. 3)."
- Old citation: "(citation as given in Mastroianni–Russo 1999, ref. [15]; DOI not verified here)". New: "DOI 10.1515/form.1994.6.183 verified via Crossref (p2-links) and the publisher page (2026-11-03); pages 183–207 confirmed on the publisher page."
- Locator note: equation and page locators in this record are arXiv v1 locators; journal locators are unknown.

## Relation to campaign claims (no inherited proof status)

Unchanged verdict for PD-T017/018/019: RELATED, DIFFERENT SETTING (same-weight Gauss nodes and Christoffel weights; our problem mixes CC/Lobatto nodes and weights with Lebesgue measure). New: Remark (1) is the same-weight analogue of the "half-degree" regime of PD-T023/T024 and of ASV's weak-MZ picture: RELATED, DIFFERENT SETTING (Gauss nodes, k ≤ n/2 only, unspecified constants, no proof given).

## History

2026-11-03: journal access attempted (unlicensed); arXiv primary re-read; parameter restriction confirmed; Remark (1) added.
