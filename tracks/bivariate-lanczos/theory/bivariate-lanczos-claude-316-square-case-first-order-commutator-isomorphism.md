# PD-T?bivariate-lanczos-claude-316 — OPEN: in the square case the last-block commutator is, to first order, an isomorphic image of the S_1*-component of the perturbation

Final ID: **PD-T072** (allocated at PR preparation, 2026-11-01; the provisional ID above and in the text is retained as provenance — see ID_CROSSWALK.md).

ID kind: PD-T.
Aliases: 304(c) isomorphism; first-order identification of κ; V*/T ≅ Skew_{n+1}; "κ is, to first order, the S_1*-component of the perturbation".
Split from: PD-T?bivariate-lanczos-claude-304(c), second clause, pre-audit wording: «when the 3N_n jet conditions are independent (verified exactly for Padua n = 1, 2, 3 and numerically for n ≤ 7, PD-T?…-307) S_1 ≅ (V*/T)* and κ is, to first order, the S_1*-component of the perturbation.»
Split into: none.

## Statement

Target (OPEN). For every n ≥ 1, every Π_n-unisolvent set of M = N_n nodes whose 3N_n jet functionals {ev_{z_i}, ∂_x ev_{z_i}, ∂_y ev_{z_i}} are linearly independent, and all positive weights: the map V*/T → Skew_{n+1} induced by d(κ∘Φ)_{L_μ} (PD-T?…-304(c)) is a linear isomorphism.

## Definitions

As in PD-T?…-304 and 318: V = Π_{2n+1}, T = span of the jet functionals, S_1 = T^⊥, κ(Ĥ) = ([Ĥ_x, Ĥ_y])_{nn}, F = {p_C : C ⊥ Hankel}.

## Assumptions

[EXACT]; square case; independent jets (dim S_1 = n(n+1)/2).

## Status by part

Overall status: OPEN.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| target, general node sets | OPEN | equivalent, by PD-T?…-318(d) (PROVED), to injectivity of C ↦ p_C on {C ⊥ Hankel} (given independent jets, injectivity ⟺ F = S_1); that conjunct is MEASURED only (PD-T?…-309, 307 item 5) |

Supporting results under their own IDs (not parts of this statement's proof): PD-T?…-304(c) (factorisation through V*/T, PROVED), PD-T?…-318 (derivative formula and the equivalence, PROVED), PD-T?…-317 (finite rank measurements, MEASURED).

## Depends on

PD-T?…-304(c), PD-T?…-318, PD-T?…-309.

## Checks

None for the general statement. Measurements: PD-T?…-317.

## Sources

None.

## Proof or evidence

No proof. Reduction: by PD-T?…-318(d) the target holds for a given node set iff dim F = n(n+1)/2 (given dim S_1 = n(n+1)/2). Evidence: rank d(κ) = n(n+1)/2 numerically for Padua n = 1..4, one equispaced and one random set at n = 3 (PD-T?…-317); rank(C ↦ p_C) = n(n+1)/2 numerically for Padua n ≤ 7 and a random square set n ≤ 6 (PD-T?…-307 item 5); exact rank(C ↦ p_C) = dim S_1 for Padua n ≤ 3 reported by L3-reconstruction-01 (`indep_generator_cert.py`; reviewer computation, not rerun).

## Scope

Square case only. The weights do not enter (318(d) is a condition on the nodes).

## Open items

(1) Prove (or refute) injectivity of C ↦ p_C on {C ⊥ Hankel} for all Π_n-unisolvent square sets, or for the Padua family (an algebraic question about quadratic relations among the n+2 generators of the vanishing ideal in degree n+1). (2) Runs needed: independent rerun of `python3 -I -B tracks/bivariate-lanczos/code/review_L3/indep_generator_cert.py` (Padua n ≤ 3, exact); if it passes, register "the target holds for Padua n = 1, 2, 3" as its own claim via 318(d).

## History

- 2026-11-01T08:33:39+01:00, Claude Opus 5.5 (xhigh, requested), L3 developer: split from PD-T?…-304(c) per finding LF-M2 of Codex audit-01 (topics/bivariate-lanczos-20261031/audit-01/L3-framework.md; candidate 5ccfac2). Pre-audit wording preserved in "Split from"; in 304 the clause had status MEASURED inside an overall-PROVED file. Restated with explicit quantifiers ("for every n, every such node set") and "isomorphic image of" instead of "is" (the induced map is σᵀ of PD-T?…-318(d), not an identity map).
