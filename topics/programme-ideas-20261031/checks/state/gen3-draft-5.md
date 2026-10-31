# Vanishing-ideal learning with a backward-certified ideal: Christoffel functions and approximate border bases as one object
Model: claude-fable-5-1, effort xhigh (as requested by the orchestrator) · Angle C · 2026-10-31 · Status: not returned (collides with the already-judged items "empirical Christoffel via QR" and "approximate border bases via tolerance-truncated recurrences"; the only residue is the whole-ideal backward certificate already listed as R3 rank 8 and deferred in (b) as candidates 028/029)

Aliases: approximate vanishing ideals (AVI/ABM/OAVI/VCA); Christoffel-function outlier detection (Lasserre–Pauwels; Ducharlet et al. 2025); Kera–Kehrein gradient-weighted border bases; streaming/sliding-window Christoffel; whole-ideal certificate; Buchberger–Möller residual ratios.

## Central question
Is there a single mathematical object — the discrete-OP recurrence of the empirical measure with pivot tolerances — from which both the empirical Christoffel function (outlier scores) and an approximate border basis with a certified *whole-ideal* backward error (a nearby point set whose exact ideal has the computed generators) are read off, so that "learning the variety" and "scoring the points" are the same computation with one shared certificate?

## Template theory
One variable: an N-point discrete measure on the line; its Jacobi matrix gives both the Christoffel function (1/Σ p_k²) and the "vanishing polynomial" (the characteristic polynomial of the truncated Jacobi matrix, which vanishes exactly on the points), and a backward statement is immediate (the computed Jacobi matrix is the exact Jacobi matrix of its own eigen-decomposition, a nearby N-point measure). In two variables the three pieces exist separately — Christoffel functions via QR (judged solved), approximate ideals via tolerance (Sauer 2007; KPR 2009; HL Cor. 2.2) — but the backward statement fails: computed (H_x, H_y) never commute, so there is no nearby point set with those exact recurrences (R2 row 1; brief §3). A bivariate version would need exactly the commuting-repair / quantitative-Lin machinery of (b)'s L3.

## Sub-problems (≥3, each with a separate payoff)
| # | Sub-problem | Kind | Payoff |
|---|---|---|---|
| 1 | Whole-ideal backward certificate from the computed sections (R3 rank 8; LZ 028/029) | theory | the rank-8 paper — owned by (b) as deferred 028/029 |
| 2 | Streaming/sliding-window Christoffel with recurrence memory only (NOTES `recent_adjacent_areas.md` P3; R3 F3 "essentially solved": standard QR-RLS; instabilities are Sherman–Morrison on monomial moments) | numerics-software | an application note, judged solved as a research question |
| 3 | Gradient-weighted border bases by GSVD/Givens (NOTES P6; Kera–Kehrein 2025) | algorithms | "low-medium difficulty companion" per NOTES; not programme-scale |

## Entry points and cheap decisive tests
1. (n ≤ 6) Compare the pivot-ratio (Buchberger–Möller residual) criterion with OAVI's absolute tolerance on a noisy circle sample; measure which gives the fewer false generators. Kill: no difference beyond scaling.
2. (n ≤ 6) Attempt the backward construction: from computed (H_x, H_y) with ‖[H_x,H_y]‖ = δ, find a commuting pair within O(δ) and its joint eigenvalues; this IS (b)'s L3-Q1 test.

## Plausible first paper (≈6 months)
None that is not already listed (R3 rank 8) or already judged (F3, F4 "substantially addressed").

## Closest prior work
Sauer 2007; Kreuzer–Poulisse–Robbiano 2009; Abbott–Fassino–Torrente 2008; Fassino 2010; Wirth–Kera–Pokutta ICLR 2023; Pelleriti et al. 2025; Kera–Kehrein 2025; Ducharlet et al. 2025; Lasserre–Pauwels–Putinar 2022; Mourrain ISSAC 2017; HL BIT 2002 Cor. 2.2. All in NOTES (`recent_adjacent_areas.md` P3, P6; R3 F3/F4). No web search run beyond those in the inputs; nothing new found for this draft.

## Why it is not an exclusion
It is not separable from the judged items: "empirical Christoffel via QR" (computation solved; the candidate brings no new mathematical question about Christoffel functions — the question here is the certificate, which is F4's residue) and "approximate border bases via tolerance-truncated recurrences" (substantially addressed; residue = whole-ideal certificate = R3 rank 8 = LZ 028/029, deferred inside (b) because its mechanism is L3's quantitative Lin). The "one object" framing is a renaming of HL Cor. 2.2 + QR Christoffel + F4's residue; no new mechanism.

## Fit with AC's expertise and 2–5-year horizon
High fit, but the escalation path leads straight into (b)'s L3 (commuting repair), which is owned.

## Risks and obstructions
**Computed H_x, H_y never commute exactly** blocks the backward statement literally; the escape (two-sections-plus-commutator; quantitative Lin) is LZ 004/029/031 — owned by (b).

## IDEA-template record
# IDEA?programme-ideas-claude-3-5 — Christoffel functions and certified approximate border bases from one recurrence

Aliases: approximate vanishing ideals; Christoffel outlier detection; gradient-weighted border bases; streaming Christoffel; whole-ideal certificate.

- Question / scope: one recurrence object yielding Christoffel scores and a whole-ideal-certified border basis.
- Mechanism and hypotheses: pivot = ratio of consecutive Buchberger–Möller residuals (R2 D); backward certificate needs a nearby commuting pair.
- Closest registry entries (read in full): LZ -025 (settled), -028, -029 (deferred), -030, -031 (active L3); CH IDEA-025, IDEA-026 (contextual).
- Separation criterion vs closest entry (and observation that falsifies it): none that survives: the certificate mechanism is LZ-029/031; the Christoffel computation is LZ-025 (settled).
- Literature baseline and search limitations: as in NOTES; no new search.
- Applicable obstructions and exact hypotheses broken: non-commutation of computed sections — not broken.
- Novelty gate verdict: duplicate (of LZ-028/029 + judged F3).
- Cheapest decisive test: entry point 2 (= (b) L3-Q1).
- Kill criterion written before testing: n/a (not pursued).
- Test discriminability: n/a.
- Resources / cost ledger (optional, when relevant): n/a.
- Actual test results and committed evidence: (empty)
- Disposition and precise rejected scope, if any: not returned; duplicate of owned/judged items in full scope.
- Disposition reason: equivalent — the candidate is the union of a judged-solved computation (F3/P7) and a (b)-deferred certificate (028/029); no separate mechanism.
- Canonical theory / negative-result ID: none.
- Topic / audit / history: programme-ideas-20261031, generator C, draft 5, 2026-10-31.
