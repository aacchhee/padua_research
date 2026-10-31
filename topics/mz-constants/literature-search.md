# M0 literature baseline — CC/Padua MZ constants

Rules read at `d36722823441dc40c6e19d69a174459348dd309c`; 2026-10-31. Literature developer: Codex, runtime-inherited model/effort (not independently exposed). This file records source evidence, not an accepted mathematical result. `literature/INDEX.md` and the complete `state/IDEAS.md` were read; both have no registered statements/candidates. No shared registry or Git mutation was made by this worker.

## Preliminary baseline (screen in progress)

The supplied F7/P1 notes identify An–Sommariva–Vianello (ASV), arXiv:2601.04708, as the direct numerical predecessor. Primary HTML v1 was inspected at the introduction and §3.1; the authors distinguish degree-dependent weak constants from strong uniform constants and explicitly describe their investigation as numerical. This supports neither an exhaustive openness claim nor an inherited proof of M1–M3.

An–Wu, arXiv:2202.13691v3, primary HTML has been accessed. Its positive-weight assumption and relaxed-exactness/MZ framework must stay attached to any statement of Corollary 4.1. A failure of an assumed numerical MZ bound would limit its application; it does not refute a conditional theorem. Exact §4.1 wording and published errata remain under review.

The highest-priority potential prior-art threats are Sloan–Smith's 1978/1980 CC product-integration papers and Mastroianni–Milovanović's 2008 book. In particular, a norm theorem for Lobatto interpolation from weighted nodal l2 to Lebesgue L2 can translate into the endpoint minimum-eigenvalue problem. These sources have not yet been checked in full text: **FULLTEXT UNVERIFIED**. The supplied assertion that general MZ theory only covers small ratios is likewise **FULLTEXT UNVERIFIED** pending exact hypotheses.

| Target | Closest source family to screen | Cheapest literature kill test |
|---|---|---|
| M1: CC lambda_max < 2 on degree <= N-1 | CC product integration; sharp MZ constants at Chebyshev extrema | Find an explicit upper discrete/Lebesgue L2 norm ratio below 2 with the actual CC weights and the same degree range. A generic unspecified constant does not settle M1. |
| M2: endpoint lambda_min of order log^-2 N | Lobatto interpolation norm; weighted MZ endpoint theory; Toeplitz/Hankel extreme-eigenvalue theory | Find an l2(CC weights) -> L2(dx) interpolation norm of order log N, or an exactly equivalent mass-matrix theorem. Matching nodes alone is insufficient; weights, degree, endpoint constraints and both directions must match. |
| M3: each fixed theta<1, uniform MZ bounds | Lubinsky–Máté–Nevai; Mastroianni–Totik; Lubinsky survey | Check whether every fixed theta<1 is permitted, whether CC weights are comparable to the theorem's weights uniformly, and whether the upper constant is <2 if eta<1 is claimed. |

The C4 transfer note is an input report, not external published literature. The orchestrator reports a mismatch: its older account labels D1' OPEN, whereas a pinned private file `21_literature_and_open_questions.md` reports an external one-level R04 audit with D1' PROVED. No private full text is reproduced here; neither report supplies a local CC proof. The exact map and hypotheses must be established independently.

## Queries and access log

All queries below were actually issued through the web search connector on 2026-10-31; coverage is partial and no exhaustive novelty claim is made.

1. `"2601.04708"`
2. `"2202.13691" erratum`
3. `"Sloan" "Smith" "Clenshaw-Curtis" 1978 1980`
4. `"Passi" "Padua" cubature 2025 2026`
5. `"On the role of weak Marcinkiewicz" "252"`
6. `"On the quadrature exactness in hyperinterpolation" erratum correction`
7. `"Mastroianni" "Milovanović" "Interpolation Processes" "Lobatto"`

Direct opens: <https://arxiv.org/html/2601.04708v1> and <https://arxiv.org/html/2202.13691v3> succeeded. <https://www.math.unipd.it/~alvise/TESI_STUDENTI/PASSI.pdf> timed out in the connector. The supplied note calls Passi's work an MSc thesis, while an author-CV search hit calls it a bachelor degree; exact thesis title page is pending. Journal version metadata and errata are pending primary verification.

## Next screen

Finish exact primary-source locators, then the named historical MZ/interpolation and matrix literature. Until that screen is complete, M1/M2/M3 remain research targets without a novelty verdict.
