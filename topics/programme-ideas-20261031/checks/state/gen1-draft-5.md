# Bivariate modified Chebyshev algorithm: block Jacobi pairs from Chebyshev-modified moments with Gautschi-type conditioning
Model: claude-fable-5-1, effort xhigh (as requested by the orchestrator) · Angle A · 2026-10-31 · Status: not returned (note-sized after R3 F9; its exact-arithmetic side is exclusion (a))

## Central question
What is the condition number of the map from Chebyshev-product modified moments of a bivariate measure on [−1,1]² to its block recurrence pair (H_x,H_y) in total degree n, and does a block modified-Chebyshev algorithm (block Lanczos on the modified-moment Hankel form) attain it?

## Template theory
Gautschi's modified Chebyshev algorithm (Math. Comp. 1982; "Orthogonal Polynomials: Computation and Approximation", OUP 2004): recurrence coefficients from modified moments ν_k = ∫p_k dμ via a mixed-moment table; conditioning of the map ν → (α,β) is governed by the Christoffel-type kernel and is benign for Chebyshev moments on [−1,1] (Fischer 1996, Beckermann–Bourreau 1998). A bivariate version must deliver: the block mixed-moment recursion for the pair (Xu's three-term block relations), its cost O(n⁴) vs the N² = n⁴/4 output, and the conditioning bound via the bivariate Christoffel–Darboux kernel.

## Sub-problems (≥3, each with a separate payoff)
| # | Sub-problem | Kind | Payoff |
|---|---|---|---|
| 1 | Block mixed-moment algorithm and its exact-arithmetic cost | algorithms + exact arithmetic | — but exact moments → OPs is exclusion (a) (drl Scalar-FGLM, X4) |
| 2 | Conditioning theorem (bivariate Fischer/Beckermann–Bourreau) | theory | a note: R3 F9 "what is left is an error analysis of the block-Lanczos / modified-Chebyshev map with Chebyshev-modified moments" |
| 3 | Application to cubature/Prony from modified moments | numerics | absorbed by the Prony/flat-extension literature (R3 F9) |

## Entry points and cheap decisive tests
1. (seconds) n ≤ 6, product-Chebyshev-weighted random positive measure (M = 50 points): compute modified moments to degree 2n, run the block algorithm, compare with QR-based pair; measure the error amplification vs the kernel-based bound. Kill: amplification exceeds the bound by > 10× — then the univariate theory does not transfer.

## Plausible first paper (≈6 months)
"Conditioning of bivariate modified moments" — a note.

## Closest prior work
Gautschi 1982; Fischer 1996 (LZ record fischer-1996, modified-moment conditioning); Beckermann–Bourreau 1998 (NOTES `adv_F2_F5_F10_F9.md` F9); Liu–Narayan SISC 2023 (multivariate Stieltjes from moments/samples; inputs); Mourrain FoCM 2018 (Gram–Schmidt on the Hankel form); Sauer–Xu arXiv:2303.16030 (continued fractions, assumes commuting truncations). Web search 2026-10-31 "modified Chebyshev algorithm multivariate/bivariate": only univariate items (ORTHPOL, chaospy, Gautschi slides, Beckermann–Bourreau) returned — consistent with R3 F9 "no paper titled multivariate modified Chebyshev found".

## Why it is not an exclusion
It is: the exact-arithmetic/complexity side is (a) (moments → OPs); the remaining floating-point conditioning question is R3 F9's "narrow remainder", judged essentially solved / note-sized. No new mechanism is offered here.

## Fit with AC's expertise and 2–5-year horizon
Fit is fine; horizon absent.

## Risks and obstructions
Popov curse for the exact side (not escaped); F9 verdict for the numerical side.

## IDEA-template record
# IDEA?programme-ideas-claude-1-5 — Bivariate modified Chebyshev algorithm
Aliases: block modified-moment algorithm; bivariate Gautschi conditioning; P11 of recent_adjacent_areas; F9 remainder.
- Question / scope: as above.
- Mechanism and hypotheses: block mixed-moment recursion.
- Closest registry entries (read in full): LZ IDEA?bivariate-lanczos-claude-043 (X1/X4/F9 out of scope); CH IDEA-034 (F9), IDEA-040 (X4(i)).
- Separation criterion vs closest entry (and observation that falsifies it): none; it is F9's remainder.
- Literature baseline and search limitations: one web search 2026-10-31.
- Applicable obstructions and exact hypotheses broken: Popov curse (exact side); none broken.
- Novelty gate verdict: duplicate (F9 remainder).
- Cheapest decisive test: entry point 1.
- Kill criterion written before testing: amplification > 10× the kernel bound.
- Test discriminability: adequate for a note.
- Resources / cost ledger: seconds.
- Actual test results and committed evidence:
- Disposition and precise rejected scope, if any: not returned (note-sized); scope: moments → pair in two variables.
- Disposition reason: equivalent (R3 F9 remainder) / deferred as a note.
- Canonical theory / negative-result ID: none.
- Topic / audit / history: programme-ideas-20261031, gen1-draft-5, 2026-10-31.
