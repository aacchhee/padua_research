# mz2d-sommariva-vianello-zanovello-2008 — Sommariva–Vianello–Zanovello, Nontensorial Clenshaw–Curtis cubature, Numer.Algorithms49 (2008),409–427

- DOI / URL / supplied location: see primary links in the extracted source record below.
- Access and reading date: 2026-11-01.
- Reading coverage: selected primary author-text sections; exact pages/equations below.
- Reader, model and effort: Codex campaign literature worker, allocated gpt-6.1-sol xhigh; runtime metadata unexposed.
- Named gaps requiring future re-reading: final journal body/comparison limits below.

## Extracted published statements

### LIT-427 — coverage-qualified primary source reading

Sommariva, Vianello, Zanovello, *Nontensorial Clenshaw--Curtis cubature*,
Numer. Algorithms 49 (2008), 409--427.
[DOI/journal](https://link.springer.com/article/10.1007/s11075-008-9203-x),
[author preprint](https://www.math.unipd.it/~marcov/pdf/hyperquad.pdf).

Coverage: preprint §§2--3.3 selected, especially equations (16)--(19),
(24)--(36), PDF pp. 6--12. Equations (19), (31), (33), (36) give normalized
Chebyshev moments, the half correction, integrated-interpolant weights, and
degree-`m` exactness. PDF p. 12 explicitly allows negative weights (journal p. 421, developer reading). Equation
(18) gives `sum(abs(w))->4`: this controls the integration functional.

**Misprint in preprint and journal:** eq. (25) prints 1/((n+2)(n+3)) in the author preprint and in the published version (journal p. 417, checked on the page image by the developer 2026-11-03). Normalization requires 1/((n+1)(n+2)) = 1/(m(m+1)). The authors' Table 1 (p. 421) is reproduced only with the correct normalization, so the misprint is typographical. No erratum was found (search not exhaustive). Independent journal-image verification is not claimed; see audit02/03.

- Statement in faithful paraphrase: the source statements above retain their attributed scope.
- Hypotheses and notation: positive Chebyshev/Xu or signed Lebesgue conventions exactly as distinguished above.
- Page / theorem / equation: exact primary locators above.
- Reading evidence and limitations: selected reading only; no blanket fulltext or proof-audit claim.
- Relation to campaign claims (no inherited proof status): see [campaign comparison](../../topics/padua-mz-2d-20261101/literature.md).

## Search and attribution notes

Complete base literature INDEX inspected before source-ID choice; same-source prior rows were reused where present. These two sources have no same-source row in that index. Coverage-qualified attribution, no novelty clearance.

## History

2026-11-01: final source-ID registration during PR14 preparation; no source theorem is promoted to a locally proved claim. Provisional alias `LIT?mz2d-codex-02`.

## 2026-11-03 journal-body reading — padua-literature-20261103

# Addendum to mz2d-sommariva-vianello-zanovello-2008 (LIT-427) — journal body read

Sommariva, Vianello, Zanovello, *Nontensorial Clenshaw–Curtis cubature*, Numer. Algorithms 49 (2008), no. 1–4, 409–427, DOI <https://doi.org/10.1007/s11075-008-9203-x>; journal page <https://link.springer.com/article/10.1007/s11075-008-9203-x>; author preprint <https://www.math.unipd.it/~marcov/pdf/hyperquad.pdf>.

- Access and reading date: 2026-11-03. Publisher PDF (19 pp., journal pp. 409–427) loaded on the link.springer.com origin in AC's built-in browser (institutional access was active there); text layer extracted in-page with pdf.js 3.11.174. Journal pp. 415 and 417 and 419 were additionally rendered to canvas and inspected as page images. Nothing from the PDF is stored in the repository; this file is paraphrase only.
- Reading coverage: journal pp. 409–421 read in full (abstract, §1, §2 with Theorem 1 and proof, §3.1, §3.2, §3.2.1, §3.3 including Table 1); pp. 422–427 (figures, Table 2, numerical discussion, reference list) keyword-screened for negative/positive/stability/Lebesgue/minimal/erratum. No erratum notice was seen on the article page; no separate erratum search was run.
- Reader, model and effort: Claude, Opus 5.5, high (P2 literature reader, topic padua-literature-20261103). Rules read at `af1ac9fde6b23cb9cd826a33d5611680566c52cb`.
- Named gaps: the preprint was not re-read in this session; the preprint-vs-journal equation-number match rests on the earlier Codex reading (same equation numbers and roles for (16)–(19), (24)–(36)).

## Decision on the open question: eq. (25)

**The journal prints the same denominator as the preprint.** On journal p. 417, eq. (25) gives the near-minimal Padua cubature weights as 1/((n+2)(n+3)) times 1/2, 1, 2 for vertex, edge and interior points. The page image confirms this; the text layer agrees.

- The grid in (24) (same page) is C^odd_{n+2} × C^even_{n+3} ∪ C^even_{n+2} × C^odd_{n+3}, where by (21) (p. 416) C_{ν+1} denotes the ν+1 Chebyshev–Lobatto points cos(jπ/ν). The grid denominators are therefore n+1 and n+2, the interpolation degree is n+1 = m, and the normalized (mass-one) weights require 1/((n+1)(n+2)) = 1/(m(m+1)), as already verified in the repo (topics/padua-mz-2d-20261101 literature.md, record 01) and in BCDMVX 2006 Theorem 1 (LIT-312).
- Consequence: the printed (n+2)(n+3) is a misprint present in **both** the preprint and the published version. It is not "preprint-specific". No erratum was found (not searched exhaustively).
- Evidence that the authors' computations used the correct normalization (reader's check, not a repository claim): the Padua row of Table 1 (journal p. 421) is reproduced to all printed digits by the correctly normalized signed weights (formula (L2) of padua-mz-2d literature.md) with interpolation degree m = n, i.e. formula (36). With the literal (25) the weight sum would be 4m/(m+2), e.g. 3.81 at m = 40, contradicting the table. Script: `/tmp/claude-0/-home-claude/4c2a0c26-2b65-599a-bd8f-ad2ed6486be9/scratchpad/p2/check/svz_table1.py` (Python 3.13.18, NumPy 2.5.3, float64; run with `python3 -I`). Output, m = 5,10,…,40: Σ|w|−4 = 4.15e−2, 2.50e−3, 8.86e−4, 2.39e−4, 1.38e−4, 5.68e−5, 3.97e−5, 2.01e−5 (Table 1 prints 4.1E−2, 2.5E−3, 8.9E−4, 2.4E−4, 1.4E−4, 5.7E−5, 4.0E−5, 2.0E−5). At each of these m exactly two weights are negative, and they sit at the two Padua corners; at m = 3, 4, 5, 10, 40 the negative nodes are the two corners only. Float computation within that finite scope; MEASURED-type observation by the reader, not registered.

## Equations (16)–(19) and (24)–(36), journal page locators

| Eq. | Journal page | Content (paraphrase) |
|---|---|---|
| (16) | 415 | Hyperinterpolation on the square for the normalized product Chebyshev measure (1/π²)(1−x₁²)^{−1/2}(1−x₂²)^{−1/2}; basis p_α = T̂_{α₁}(x₁)T̂_{α₂}(x₂), |α| ≤ n, with T̂₀ = 1, T̂_k = √2 T_k; dimension (n+1)(n+2)/2. |
| (17) | 415 | For λ ≡ 1 (Lebesgue integral on the square), the error of the hyperinterpolation-based rule is at most π² E_n(f) (best uniform approximation error). |
| (18) | 415 | Limit of the absolute weight sums: Σ|λ_ξ| → 4 (area of the square), from Theorem 1. |
| (19) | 415 | Product moments m_α = μ_{α₁}μ_{α₂} with μ₀ = 2, μ_k = 2√2/(1−k²) for even k > 0, μ_k = 0 for odd k. Only even-even pairs contribute. |
| (20)–(23) | 416 | Möller's minimal-node count; CGL notation C_{ν+1}; Morrow–Patterson–Xu points for n odd (22) and n even (23) with their weights (n+1)^{−2} on the boundary, 2(n+1)^{−2} inside, half the boundary value at two corners for even n (p. 417). |
| (24) | 417 | Padua points X_n^{Pad} as union of two Chebyshev-like subgrids of sizes n+2 and n+3 per axis (odd/even index restrictions); cardinality (n+2)(n+3)/2 = dim Π_{n+1}. Rule is exact on degree 2n+2 polynomials orthogonal to T_{2n+2}(x₁), in particular on Π_{2n+1} (p. 417). |
| (25) | 417 | Weights printed as 1/((n+2)(n+3)) × {1/2, 1, 2} (vertex, edge, interior). See decision above: should be 1/((n+1)(n+2)). |
| (26) | 418 | V_{n+1}: polynomials of degree ≤ n+1 orthogonal to T_{n+1}(x₁). |
| (27)–(29) | 418 | Extended hyperinterpolant on V_{n+1}; corresponding signed rule λ̂_ξ = w_ξ Σ_{|α|≤n+1} p_α(ξ)m_α; error ≤ π² times best approximation from V_{n+1}; (18) asserted to hold for λ̂ ("easy to show", no proof given). |
| (30)–(31) | 419 | Interpolation polynomial at the Padua points = hyperinterpolation coefficients with the coefficient of index (n+1,0) halved (citing CDMV computational paper). Unisolvence gives reproduction of Π_{n+1}. |
| (32) | 419 | L^p_{dμ} (Chebyshev-measure) error of Padua interpolation ≤ c_p E_{n+1}(f), 1 ≤ p < ∞, cited from BDMVX (ideal theory approach). |
| (33) | 419 | Interpolatory nontensorial CC weights λ*_ξ = w_ξ Σ_{|α|≤n+1} p_α(ξ)m*_α with m*_α = m_α except m*_{(n+1,0)} = m_{(n+1,0)}/2; the formula refers back to (19), (24), (25). |
| (34) | 419 | Error ≤ c₂(π²/2)E_{n+1}(f). The text then states that (18) again holds with λ* (no separate proof) and that at exactness n the rule uses (n+1)(n+2)/2 Padua points. |
| (35) | 419 | Summary formula: integral of the degree-n MPX hyperinterpolant. |
| (36) | 420 | Summary formula: integral of the degree-n Padua interpolant at X^{Pad}_{n−1}, N = (n+1)(n+2)/2 points, exactness n. |

Other statements used in the comparison:
- Theorem 1 (p. 413, proof pp. 413–414): for hyperinterpolation-based product-integration weights (positive base rule exact to 2n, h ∈ L²_{dμ}), Σ|λ_ξ| → ∫|h|dμ. Hypotheses: positive base weights and exactness 2n; it is stated for λ, not for the interpolatory λ*.
- p. 421: the authors state that both nontensorial CC formulas are not positive (some weights can be negative), that negative weights are few and small, and that MPX weights at odd degrees were all positive. Table 1 (p. 421) gives Σ|λ| − 4 at n = 5, 10, …, 40 for MPX and Padua points.

## Old → new corrections to the existing record and to topics/padua-mz-2d-20261101/literature.md

- Old: "**Preprint-specific discrepancy:** its equation (25), as extracted by the public web tool, prints denominator (n+2)(n+3) … This discrepancy is not called a journal error or erratum: the journal body was not compared. Publisher access was subscription-preview only."
- New: "**Misprint in preprint and journal:** eq. (25) prints 1/((n+2)(n+3)) in the author preprint and in the published version (journal p. 417, checked on the page image 2026-11-03). Normalization requires 1/((n+1)(n+2)) = 1/(m(m+1)). The authors' Table 1 (p. 421) is reproduced only with the correct normalization, so the misprint is typographical. No erratum was found (search not exhaustive)."
- Old coverage line "preprint §§2–3.3 … PDF pp. 6–12" stays as history; add: "Journal body read 2026-11-03: pp. 409–421 in full, 422–427 screened; equation locators above."
- Old "PDF p. 12 explicitly allows negative weights" → add journal locator "journal p. 421".

## Relation to campaign claims (no inherited proof status)

See `p2-comparison.md`. In short: degree-m exactness of the signed rule (part of PD-T106) and its weight formula are published (IMPLIES PART); the existence of negative weights at m = 5, 10, …, 40 is published numerically (RELATED to PD-T111; corner identification, exact formula, all-m negativity and asymptotics are not in the source); the limit Σ|λ*| → 4 is asserted for the interpolatory weights without separate proof (RELATED to PD-T112/T113/T114, which concern the hyperinterpolation operator, not the integration functional).

## History

2026-11-03: journal body read; eq. (25) question decided (misprint in both versions); locators added. Reader Claude Opus 5.5 high.
