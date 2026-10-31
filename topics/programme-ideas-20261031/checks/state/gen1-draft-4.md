# Isospectral flows on block Jacobi pairs: Toda/qd dynamics of bivariate recurrence matrices under Christoffel/Geronimus steps
Model: claude-fable-5-1, effort xhigh (as requested by the orchestrator) · Angle A · 2026-10-31 · Status: not returned (overlaps the "measure modification" judged item and the (a) exclusion's moment side; the genuinely new part is note-sized)

## Central question
Is there a Toda/qd-type isospectral flow on the pair (H_x,H_y) of a discrete bivariate measure (e.g. dμ_t = e^{t(αx+βy)} dμ) whose discrete-time versions are the LR/QR steps induced by Christoffel (multiply by a linear factor) and Geronimus (divide) transformations, and does the qd/dqds high-relative-accuracy machinery transfer to the block-bidiagonal factors?

## Template theory
Univariate: Toda lattice ⇔ Jacobi matrix of e^{tx}dμ (Flaschka; Moser; Deift–Nanda–Tomei QR flow); qd algorithm = Christoffel transform = LR step on the Jacobi matrix (Rutishauser; Gautschi); dqds with high relative accuracy (Fernando–Parlett 1994; Parlett). Key theorems: J(t) = Q(t)ᵀ J(0) Q(t) with QR of e^{tJ}; one Christoffel step x·dμ equals one LR step with shift; relative perturbation theory of bidiagonals (Demmel–Kahan) gives dqds its accuracy.
A bivariate version must deliver: the flow dμ_t = e^{t(αx+βy)}dμ as a QR flow of the pair with generator αH_x + βH_y (isospectral for both sections jointly — immediate since it is a unitary similarity by Q(t) from QR of e^{t(αX+βY)}); the discrete step: Christoffel by (αx+βy−c) as an LR-type step on the pair (this is the multivariate Christoffel formula of Delgado–Fernández–Pérez–Piñar–Xu / Ariznabarreta–Mañas written as a factorization); and a dqds-type shifted step with relative-accuracy analysis for the block factors.

## Sub-problems (≥3, each with a separate payoff)
| # | Sub-problem | Kind | Payoff |
|---|---|---|---|
| 1 | Multispectral Toda flow of the discrete pair: explicit ODE for the blocks of (H_x,H_y) under dμ_t; connection to Ariznabarreta–Mañas' multispectral Toda hierarchy (continuous functionals) in the finite discrete case | theory | note/paper linking NLA and integrable systems |
| 2 | Christoffel step by a linear factor as a block LR step on the pair; Geronimus as its inverse; Uvarov (point masses) as a rank-one bordering; the Padua uniform-weight rank-(2n+1) Uvarov as a test | algorithms | computational multivariate Christoffel transform (already known as formulas; the LR-step representation is the possible novelty) |
| 3 | dqds analogue: shifted block LR with relative-accuracy analysis for the block-bidiagonal Cholesky factors of the pair's Gram; joint eigenvalues (nodes) with high relative accuracy | theory + numerics | a bivariate dqds — but joint eigenvalues of truncated sections are not nodes (except Gaussian-cubature cases), so the target set is thin |

## Entry points and cheap decisive tests
1. (seconds) M = 20 random nodes; compare the pair of x·dμ computed from scratch with one block LR step (Cholesky of H_x − cI restricted appropriately, then reverse product) on the pair of dμ. Kill: the LR-step pair is not the (orthogonally equivalent) pair of x·dμ to 1e-13 — then the univariate identity "Christoffel = LR" has no block analogue beyond the Gram-level RJR⁻¹ (which is the measure-modification mechanism already in the inputs).
2. (seconds) Verify the Toda ODE for the blocks numerically by finite differences at t = 0.

## Plausible first paper (≈6 months)
"Christoffel transforms of bivariate discrete measures as block LR steps" — short.

## Closest prior work
- Ariznabarreta–Mañas, arXiv:1511.09129 (web-checked 2026-10-31: multivariate Christoffel–Geronimus–Uvarov formulas via quasi-determinants and a multispectral Toda hierarchy; analytic, no algorithms, no discrete/numerical content). They own the integrable-systems side.
- Delgado–Fernández–Pérez–Piñar–Xu, Numer. Algorithms 55 (2010) (inputs; multivariate Uvarov).
- Gutleb–Olver–Slevinsky FoCM 2024, Gumerov–Rigg–Slevinsky 2024 (inputs; measure modification by banded/displacement factorizations).
- Bultheel TW57 (1982) 2-D Padé qd (NOTES `exact_arithmetic_catalog.md`), uncosted.
- Rutishauser, Fernando–Parlett — UNVERIFIED (memory).

## Why it is not an exclusion
Nearest: "measure modification (narrow)" (R3 F2/T4: numerically sparse unless q nearly vanishes; curve zeros blocked) and the (a) exclusion's moment side. The LR-step viewpoint is a reformulation of R H R⁻¹ with R the Cholesky connection factor (R2 §1, RES 2b) — a renaming, not a new mechanism, unless sub-problem 3's relative accuracy delivers something; it cannot, because joint eigenvalues of sections are not the measure's nodes in general. Separation fails on the campaign's "no renaming" rule.

## Fit with AC's expertise and 2–5-year horizon
Good fit (LR/QR steps, bidiagonal factors), but no escalation path survives the exclusions: the continuous-measure modification complexity is F2 (narrow), the discrete reweighting is Uvarov (judged), the flow is Ariznabarreta–Mañas's.

## Risks and obstructions
Measure-modification obstruction (curve-zero ranks R04/R07) applies verbatim to Geronimus steps dividing by a factor vanishing on a curve. Not escaped.

## IDEA-template record
# IDEA?programme-ideas-claude-1-4 — Toda/qd flows on bivariate block Jacobi pairs
Aliases: bivariate Toda; block LR Christoffel step; multispectral Toda discrete; bivariate dqds.
- Question / scope: as above.
- Mechanism and hypotheses: Christoffel by a linear factor = block LR step on the pair.
- Closest registry entries (read in full): LZ IDEA?bivariate-lanczos-claude-039 (Uvarov), -046 (F2); CH IDEA-021, IDEA-030.
- Separation criterion vs closest entry (and observation that falsifies it): none that survives — the LR step is R H R⁻¹ renamed.
- Literature baseline and search limitations: one web search 2026-10-31 (Toda/qd/block Jacobi/multivariate Mañas).
- Applicable obstructions and exact hypotheses broken: R04/R07 curve-zero ranks for Geronimus; not broken.
- Novelty gate verdict: variant with difference (integrable-systems framing) of the measure-modification item; not programme-scale.
- Cheapest decisive test: entry point 1.
- Kill criterion written before testing: LR-step pair ≠ pair of x·dμ at 1e-13.
- Test discriminability: 0/1 at 1e-13.
- Resources / cost ledger: seconds.
- Actual test results and committed evidence:
- Disposition and precise rejected scope, if any: not returned; scope: discrete bivariate measures, linear-factor Christoffel/Geronimus steps.
- Disposition reason: abandoned (renaming of the Gram-level connection step; downstream questions are excluded or judged narrow).
- Canonical theory / negative-result ID: none.
- Topic / audit / history: programme-ideas-20261031, gen1-draft-4, 2026-10-31.
