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
