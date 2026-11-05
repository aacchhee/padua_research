# laudadio-mastronardi-vandooren-2025 — T. Laudadio, N. Mastronardi, P. Van Dooren, "Computational aspects of simultaneous Gaussian quadrature", Numer. Algorithms 100(2) (2025) 621–643 (online 28 Mar 2024)

Registration (2026-11-05 PR21 final registration): LIT-508. Original provisional aliases remain below; [exact map](../../topics/padua-literature-20261103/preparation/final-id-map.json). Source statements, versions, reader attribution and reading limits are unchanged. Developer-only source checks remain qualified by audit02/03; no independent auditor page-image verification is inferred.

- DOI / URL: https://doi.org/10.1007/s11075-024-01785-0 ; PDF https://link.springer.com/content/pdf/10.1007/s11075-024-01785-0.pdf (open access, "© The Author(s) 2024", p. 621). No arXiv version found (p4-links.md 5b).
- Access and reading date: 2026-11-03, Springer PDF (23 pp.) loaded on the link.springer.com origin in the built-in browser, pdf.js text extraction. No paywall or captcha.
- Reading coverage: exact pages: pp. 621–623 (abstract, introduction with outline), p. 627 (Algorithm Scale, Theorem 1, Remark 2 start), p. 628 (power-of-2 variant), p. 629 (start of §5), p. 632 (Ehrlich–Aberth remarks), p. 635 (eigenvectors, Remark 3, §7 outline), pp. 639–641 (§9 Concluding remarks, appendix, acknowledgements); keyword searches over all pages. Not read: §3 TN verification (pp. 624–627), §5 reduction details and Theorem 2 (pp. 629–631), §6 (pp. 631–635), §8 results (pp. 636–639).
- Reader, model and effort: Claude P4 literature reader (claude-opus-5-5, high).
- Named gaps requiring future re-reading: Theorem 2 and the backward-stability argument of §5; the numerical results of §8.

## Extracted published statements

### LIT-508 (LIT?padua-literature-claude-81) — what is computed, stability claims, future work

- Statement in faithful paraphrase: The paper computes the nodes and weights of n-point simultaneous Gaussian quadrature (r = 2) from the banded lower Hessenberg recurrence matrix H_n of type II MOPs. The families come from Van Assche's Golub–Welsch paper (modified Bessel weights). The key observation is that H_n is **totally nonnegative (TN)** for these families. This is used to (i) scale H_n by a diagonal similarity so that its tridiagonal part is symmetric, which reduces eigenvalue sensitivities tremendously (Fig. 1, p. 629); (ii) reduce the bandwidth to a symmetric tridiagonal TN matrix by 2×2 elementary similarities whose TN-preservation is shown in the appendix; (iii) use those eigenvalues as starting values for an Ehrlich–Aberth iteration on the scaled matrix, with left and right eigenvectors from Givens-based null-space computations. The total cost is O(n²) (pp. 621–623). Stability claims: the scaling is forward stable elementwise, with |ΔĤ| ≤ γ_{3n}|Ĥ| (Theorem 1, p. 627). A power-of-2 variant has no rounding error (p. 628). The bandwidth reduction "aims at guaranteeing" backward stability (p. 629). The eigenvector computation is called stable by reference to their earlier work, because the eigenvalues of the scaled matrix are well separated for the examples considered (p. 635). The introduction states that the Golub–Welsch approach adapted to H_n is highly unstable because of non-normality (p. 622). The concluding remarks report nodes to almost full relative accuracy and weights to almost full absolute accuracy. They state that the method depends heavily on TN, and they **conjecture** that the technique applies to all such rules with a nonnegative integration interval and also for r > 2, although only r = 2 was coded and tested (pp. 639–641). The introduction adds that, when recurrence coefficients are unknown, a discretized Stieltjes–Gautschi procedure can provide them (p. 623).
- Hypotheses and notation: TN banded Hessenberg matrices; nonzero super-diagonal; explicit recurrence coefficients.
- Page / theorem / equation: pp. 621–623; Theorem 1 p. 627; p. 628; p. 629; p. 632; p. 635; pp. 639–641.
- Reading evidence and limitations: pages listed above read. The backward-stability proof of §5 was not read, so the backward-stability claim is recorded as the authors' stated aim only.
- Relation to campaign claims: the forward (eigenvalue) side of the MOP story. The future-work item (r > 2, nonnegative intervals) is phrased as a conjecture. It is univariate. The dedication to Marc Van Barel (p. 621) is the only mention of Leuven IEP authors.

## Search and attribution notes

- Searches on 2026-11-03 over all 23 pages: "bivariate", "multivariate", "Chesnokov", "two variables", "several variables", "Padua", "Faghih", "Vandebril": 0 hits. "Van Barel" appears only in the dedication (p. 621) and acknowledgement (p. 641).

## History

2026-11-03: new record (P4); provisional ID 81.
