# PD-N?bivariate-lanczos-claude-302 — In the square case no backward construction achieves δ = O(ε)

ID kind: PD-N.
Aliases: kill-test alternative "construction always works with δ = O(ε)" refuted for M = N_n; √ε necessity in the square case.
Split from: none (case of the target PD-T?bivariate-lanczos-claude-300).
Split into: none.

## Statement

For every n ≥ 1, every Π_n-unisolvent node set with M = N_n points and every positive weights, there are C > 0 and, for every small ε > 0, a consistent ε-perturbation Ĥ = Φ(L_μ + E) of the degree-n sections such that every positive measure whose exact degree-n sections equal Ĥ has a support point at distance ≥ (ε/C)^{1/2} from the nodes. In particular no construction with δ = O(ε) works in the square case (Padua or not).

## Negative-result scope (PD-N only)

Attempted mechanism: the second branch of the frozen L3-Q1 kill test ("a construction that always works with δ = O(ε)") in the square case; IDEA?bivariate-lanczos-claude-306.
Parameter range: square case M = N_n, n ≥ 1, perturbative regime, exact representation (or residual ≤ θε, θ < 1, with the residual defined with fixed scale c = 1 as in PD-T?…-302). The overdetermined case is not affected (there δ = 0, PD-T?…-303(a)).

## Status by part

Overall status: PROVED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| S_1 ≠ {0} in the square case | PROVED | dim Π_{2n+1} − 3N_n = n(n+1)/2 > 0 |
| r(δ) ≤ Cδ² ⇒ δ* ≥ (ε/C)^{1/2} | PROVED | PD-T?…-303(c), PD-T?…-302(b) |

Candidate / claim disposition: REJECTED (the δ = O(ε) construction, square case). Rejection reason: refuted.

## Depends on

PD-T?…-302, 303 (alternatively PD-T?…-304(a) via the commutator).

## Checks

Proof only; MEASURED illustrations in PD-T?…-307.

## Sources

None.

## Proof or evidence

PD-T?…-303(c) and PD-T?…-302(b) (take E along the minimiser p of r(δ) for δ = (ε/C)^{1/2}/2).

## Scope

As stated.

## Open items

None for this statement.

## History

2026-10-31, Claude Opus 5.5 (xhigh, requested), L3 developer, base 2d8c3ab: created in round R01.
- 2026-10-31T23:54:00+01:00, L3 developer: "atom" → "support point" and the residual convention c = 1 (finding M2) per L3-reconstruction-01 (topics/bivariate-lanczos-20261031/reviews/L3-reconstruction-01.md, audited head 0b7b396).
- 2026-11-01T00:47:14+01:00, L3 developer: finding L11 of L3-reconstruction-02 (reviews/L3-reconstruction-02.md, audited head ae991c1) — original wording of the passages replaced at 2026-10-31T23:54 (round-1 response): «has an atom at distance ≥ (ε/C)^{1/2} from the nodes.»; «exact representation (or residual ≤ θε, θ < 1).».
