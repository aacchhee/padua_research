# PR11 independent primary-source subset audit

Target: `4f937137f9baac5e51814964e6a83aeb2df38815`. Rules read at `9739a0c56b7a3976422ce60a8441bfbbfd6554df`. Date: 2026-11-01. Independent Codex subagent; exact runtime model/effort is not exposed in this subagent context. No Git mutations or edits to developer files. Scope: source fidelity for the assigned comparison rows, not an exhaustive novelty search or proof audit. Parent owns the complete IDEAS gate. Read AGENTS, WORKFLOW, CODEX, literature INDEX, comparison.md, and the two assigned source records. Primary statements below were obtained independently; Claude's records were comparison targets, not verification evidence.

## Findings

1. **P2: missing parameter restriction in König–Nielsen's upper endpoint.** `literature/records/mz-prior-art-2026-additions.md:20` gives `M=4(α+1)/(2α+1)` whenever `α>−1/2`, with no ordering of α,β. The primary Theorem 1, arXiv pp.3–4, defines `M=m(α,β)'`, where `m=max{1,4(α+1)/(2α+3),4(β+1)/(2β+3)}`. Its proof on p.15 assumes `α≥β` before giving the abbreviated α-only formula. Fix by adding that assumption or using `a=max(α,β)`. For α=0,β=1 the recorded formula gives 4 rather than 8/3. The same-weight versus mixed-weight verdict remains correct. [Primary](https://arxiv.org/pdf/math/9208201).

2. **Scope correction needed for mechanism attribution.** Comparison lines 54 and 58 should distinguish a classical Jacobi-polynomial norm-growth mechanism from the *specific* U-polynomial Lebesgue-L² mechanism. In König–Nielsen, the U specialization α=β=1/2 has critical p=3 and continuous weight √(1−x²); eqs.(18)–(19), p.15, yield `(log n)^(1/3)` there. At p=2 the same-weight Gaussian quadratic form is exact. Thus those equations do not directly prove √log growth in Lebesgue L², nor CC weighted nodal unboundedness. Mastroianni–Russo may supply the intended mixed-weight attribution, but its primary text was inaccessible here. Also, failure of a uniform family bound alone establishes an unbounded subsequence, not automatically a full-sequence `λ_-→0`. Keep any full-limit assertion tied to an explicit witness/quantitative argument. This is a limitation of the supplied implication, not a refutation of the manuscript theorem.

## Independently verified coverage

### König–Nielsen, arXiv math/9208201v1

Read definitions and Theorem 1 on pp.2–4 and necessity examples eqs.(18)–(19) on p.15. Gauss nodes, Christoffel numbers and continuous measure all use the same Jacobi weight. The nodal-to-continuous inequality is on Π_n and has the stated open p interval, with UMD needed for vector values. The upper critical test has continuous growth `(log n)^(1/p)` and bounded discrete side. The comparison's main setting mismatch is verified; parameter correction above applies. Journal version uninspected. [Primary PDF](https://arxiv.org/pdf/math/9208201).

### Smith 1986

Read primary text pp.375–379, including Theorem 1 and Corollary 1. Nodes are zeros of Q_n for ρ plus both endpoints, output Π_(n+1), continuous measure `ρ/(1−x²) dx`. Theorem 1 and its proof explicitly use uniform C-input and a uniformly bounded C→weighted-L² operator. Corollary 1 gives the CC specialization through α=β=1/2; its continuous measure is Chebyshev. The comparison verdict is supported, and domination of Lebesgue measure by Chebyshev measure indeed transfers the uniform-input bound. [Primary PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/D75D44DF457585411AB846A65AD8E79A/S000497270001025Xa.pdf/erdos-turan-mean-convergence-theorem-for-lagrange-interpolation-at-lobatto-points.pdf).

### Erdős–Feldheim 1936

Read original scan text pp.913–915. Equation (1), p.914, concerns every positive even power and Chebyshev measure, with notation referred to the earlier note at p.650. This supports the limited measure/convergence comparison. The exact preceding-note node convention and function assumptions remain unverified; this pass does not upgrade them. [Original scan](https://www.renyi.hu/~p_erdos/1936-10.pdf).

### Askey

1972 journal body inaccessible: Springer article page confirms citation and displays subscription-only access. Independently read the 1969 CWI report introduction and Gaussian-quadrature discussion (PDF pp.3–7): Gauss zeros, continuous f, same/mixed measures distinguished, mixed-weight result explicitly conjectural there. This supports the general setting mismatch but does not verify journal corrections, exact Theorem 1 range, or absence of all relevant journal estimates. [Journal landing page](https://link.springer.com/article/10.1007/BF01889904), [1969 primary report](https://ir.cwi.nl/pub/7742/7742D.pdf).

## Sources inaccessible for independent theorem verification

- **Nevai III 1984:** AMS PDF repeatedly returned 403; alternate AMS paths failed. Author homepage exposes bibliography but no usable paper copy. Properties (g), eq.(24), p.675, and Theorems 1–7 are **not independently verified**. There is corroborating *secondary attribution within another primary paper*: Mastroianni–Milovanović–Notarangelo 2012, p.167, eq.(2.15), cites Nevai p.675 for a discrete≤continuous inequality. That corroborates the forward-direction description but is not a page-image check of Nevai's exact hypotheses. [Attempted primary](https://www.ams.org/journals/tran/1984-282-02/S0002-9947-1984-0732113-4/S0002-9947-1984-0732113-4.pdf).
- **Mastroianni–Russo 1999:** DOI, Springer article and PDF routes inaccessible. Author bibliography independently confirms publication, not Theorem 2.7. Its formula, auxiliary v, necessity proof and exact relation to Nevai remain unverified in this audit. [Attempted primary](https://doi.org/10.1007/s003659900107), [author bibliography](https://service.unibas.it/utenti/mastroianni/listOfPublications.html).
- **Xu II 1994:** DOI inaccessible; author bibliography confirms title/year/volume/pages, with no linked PDF for this entry. Theorem 3.2, condition (3.2c), Theorem 3.4 and Remark 3.1 not independently verified. [Attempted primary](https://doi.org/10.1006/jath.1994.1006), [author bibliography](https://pages.uoregon.edu/yuan/pub.html).

## New directly relevant follow-up lead

Mastroianni–Milovanović–Notarangelo, *On an interpolation process of Lagrange–Hermite type*, Publ. Inst. Math. 91(105) (2012), 163–175, DOI 10.2298/PIM1205163M. Primary extraction pp.163–167 inspected; Theorem 2.3 and Corollary 2.2 concern Jacobi interior nodes **with endpoint data**, nodal p-norm, and Π_(m+2r−1). The criterion is `−1/p < r+γ−α/2−1/4 < 1/q`; endpoint data are σ_m(P)/m^(2γ+2/p). With r=1,γ=0,α=1/2,p=2 the central exponent equals the excluded upper endpoint 1/2. This is closer to actual CC/Lobatto qualitative unboundedness than the Gauss-only comparison. The interior coefficients may be replaced by Christoffel functions of the target weight. However: extraction renders ≥ as > in several hypotheses, so γ=0 and r=1 inclusion needs a visual check before importing the specialization. Degree is full Π_N when m=N−1, not automatically Π_(N−1); no critical quantitative rate was verified. [Author primary PDF](https://www.mi.sanu.ac.rs/~gvm/radovi/n105p163.pdf).

## Execution limitations

Used web search/open/find/screenshot commands through the discovered web connector. Screenshots returned text placeholders without image bytes in this interface, so they do **not** count as visual inspection. Did not download or archive third-party PDFs. Shell networking policy is enforced and does not allow publisher hosts, so no shell bypass attempted. Read-only shell commands inspected local Markdown and line numbers; report is the sole created artifact. This report supports only the named verifications and findings; inaccessible primary sources remain residual audit risk.
