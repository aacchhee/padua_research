# brubeck-nakatsukasa-trefethen-2021 — addendum (padua-literature-20261103, P3)

Addendum to `literature/records/brubeck-nakatsukasa-trefethen-2021.md`. P. D. Brubeck, Y. Nakatsukasa, L. N. Trefethen, Vandermonde with Arnoldi, SIAM Rev. 63(2) (2021) 405–415, [doi:10.1137/19M130100X](https://doi.org/10.1137/19M130100X); free version [arXiv:1911.09988](https://arxiv.org/abs/1911.09988).

- Access and reading date: 2026-11-03.
- Version read: arXiv v1 (22 Nov 2019, the only arXiv version). The SIAM Review version was NOT read (SIAM pages not attempted).
- Reading coverage: exact PDF pages 1 (abstract and start of §1), 3 (§3, start of §4), 4–5 (§4), 8–9 (§7 discussion). Pages 2, 6–7 (Examples 1, 3, 4) NOT read. Text extracted with pdf.js in the built-in browser.
- Reader, model and effort: P3 literature reader, Claude Opus 5.5 (claude-opus-5-5), high.
- Named gaps: SIAM Review version of record; examples.

## Extracted published statements

### LIT?padua-literature-claude-53 — §4 stability statements (all univariate, none proved)

- Statement in faithful paraphrase: Arnoldi orthogonalisation of the Krylov sequence q₀, Xq₀, … gives XQ₋ = QH with Hessenberg H; only H is kept, and evaluation at new points reuses H (columns of the evaluation matrix are only approximately orthogonal) (pp. 4–5). The entries of H are recurrence coefficients for polynomials orthogonal on the discrete point set, approximating continuous ones, which is offered as the reason the method is effective (p. 5). Replacing the final least-squares solve by d = Qᵀf/m impaired accuracy in experiments; the authors add, parenthetically, that this shortcut becomes an extremely stable alternative if each column is orthogonalised twice (p. 5). For real nodes H is tridiagonal and Arnoldi equals Lanczos, which could reduce the cost, but there is a risk of reduced accuracy because the computed columns may lose orthogonality (p. 5). §7 credits Gragg–Reichel 1987 and Stylianopoulos et al. with earlier uses (p. 8).
- Hypotheses and notation: one variable (real or complex nodes); no theorem in the pages read.
- Page / theorem / equation: §4 pp. 3–5, eqs. (4.1)–(4.5); §7 pp. 8–9.
- Reading evidence and limitations: read on those pages; all stability statements are experimental or asserted.
- Relation to campaign claims (no inherited proof status): 1D background for the V+A comparison; no multivariate content.

## Corrections and upgrades (old → new)

- LIT-099: UNVERIFIED (reported) → verified, p. 5 (arXiv v1).
- LIT-285: digest → verified, p. 5, with a context correction: the "extremely stable alternative" remark is about computing d = Qᵀf/m (instead of the backslash solve) when each column has two orthogonalisation passes; it is a parenthetical assertion, not a claim about the basis.

## History

2026-11-03: addendum by the P3 reader (Claude Opus 5.5 high), padua-literature-20261103.
