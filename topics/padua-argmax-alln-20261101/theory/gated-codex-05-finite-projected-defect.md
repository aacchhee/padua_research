# PD-T219 (PD-T?argmax-alln-gated-codex-05) — Explicit finite projected-defect block

Final registration: **PD-T219**, 2026-11-03. The provisional identifier in the title remains an alias; mathematical statement and historical evidence are unchanged.

ID kind:PD-T.
Aliases: finite positive cancellation rectangle; explicit phase-radius defect.
Split from: quantitative projected-defect obligation in gated-codex-01.
Split into:none.

## Statement

Use gated-codex-01's exact Qv,Qh and odd-coset phases α,β. Let0<δ<π/2, κδ=1−cos(δ/2), ρδ=κδ/4, and

Nδ=ceil(16π/δ), dδ=δ²κδ/(256π²).

For every integer n≥Nδ and every physical point represented by an odd coset with |α|+|β|≤ρδ,

Qv≥dδ whenever φ∈[δ,π−δ];

Qh≥dδ whenever θ∈[δ,π−δ].

Each assertion is uniform in the other coordinate, including arbitrary moving strip distances. There is no limiting error in these inequalities.

## Assumptions/status/dependencies

Exact real arithmetic and the corrected kernel/weights of PD-T101. Overall status:PROVED by finite inequalities and grid counts below; supplementary independent review is complete; Claude audit-01 ACCEPTED the mathematics at its stated scope (record fixes pending).
Depends on gated-codex-01's exact pairwise normalization and numerator identity. No numerical quadrature, fitted constant, limit theorem or computer-proof premise.

## Proof

Letρ=|α|+|β|≤ρδ. Sinceκδ<1 andρ<1/4, a=(cosα+cosβ)/2≥1−ρ²/4≥63/64.

For Qv restrict physical second-mesh rows to b∈[δ/4,δ/2] and the periodic first angle to |u−φ|≤δ/8. The two targets are cos(φ±b), and u is strictly between the corresponding angles. Both target angles lie in[δ/2,π−δ/2]; therefore1+cos(φ±b)≥κδ. The half-kernel numerator from gated-01 is at least

aκδ−(|sinα|+|sinβ|)/2
≥(63/64)κδ−ρ/2≥(55/64)κδ>κδ/2.

The two denominators have opposite signs and magnitude≤2. Each half magnitude is≥κδ/4, hence their triangle defect is≥κδ/2. None of these selected points is a quotient collision because the angular separation is at leastδ/8.

For a fixed b row, the parity-restricted periodic first mesh has spacing2π/n. A closed interval of lengthδ/4 contains at least nδ/(8π)−1 such points, hence at least nδ/(16π), because n≥16π/δ. The physical b interval has at least mδ/(4π)−1≥mδ/(8π) rows; all are interior rows with endpoint factor1. Formula(B) of gated-01 has weight1/(nm). Thus

Qv≥[1/(nm)]·[nδ/(16π)]·[mδ/(8π)]·[κδ/2]=dδ.

For Qh restrict physical a rows to[δ/4,δ/2] and the periodic second angle v to|v−θ|≤δ/8. Now v∈[7δ/8,π−7δ/8], so1+cos v≥κδ. In the horizontal half representation the extra sine terms have total magnitude≤ρ/2; the same numerator bound applies. The two first-angle targets straddle v, so again the pair defect is≥κδ/2. Count at least nδ/(8π) physical rows and mδ/(16π) parity-restricted periodic second points. The same normalized product proves Qh≥dδ. ∎

## Scope and quantitative frontier

This gives explicit finite defect positivity once both phases are within the explicit radiusρδ and n≥Nδ. It does not itself localize the phases or bound the primitive excess. The unknown quantitative primitive constants remain the obstacle to a usable explicit global degree threshold.

This theorem is a finite strengthening discovered during direction1 round2's quantitative diagnosis. It is a variant of the existing positive-rectangle edge argument and the round1 projection, without a novelty claim. No all-degree corner theorem or finite coverage beyond16 follows.

## Checks/history

Codex Sol xhigh, scientific source7d308b10d946b607ae0690454f6c0103690775a4, authorized direction1 round2. Written grid-count proof; supplementary independent review is complete; Claude audit-01 ACCEPTED the mathematics at its stated scope (record fixes pending). PD-T099 remains OPEN.


### Documentation correction — 2026-11-02

N4: Nδ here is the explicit finite-block threshold ceil(16π/δ), not the existential compact-complement threshold denoted Nδ in gated-codex-04. Neither notation nor quantifier in either theorem is changed.

Current review scope (F3): [Claude audit-01](../audit-01.md) ACCEPTED the mathematics exactly as stated; its record/protocol findings and the protocol check of this response remain pending. Supplementary independent checks are complete and do not replace that Claude audit. No proof status, statement, checker predicate or certificate changes. Earlier publication-time review wording is preserved here as history:

> independent check and required Claude audit pending
> independent mathematical review pending

F13 closest-prior citation: [PD-T103](../../padua-proof-attempts-20261101/theory/proof-attempts-codex-03-degenerate-maxima.md) supplies an earlier excluded-zero-cardinal local certificate at the two degree-3 degenerate maxima: it controls a signed background and the excluded cardinal by exact Hessian bounds on fixed angle discs. It is a conceptual predecessor for retaining cancellation and zero cardinals, not a proof of this compact projection/defect result or an additional hypothesis here. No duplicate, priority or exhaustive novelty claim is made.
