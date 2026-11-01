# PD-T?programme-ideas-claude-04 — Second-order expansion of the Padua Lebesgue function at the non-node corner (conjecture with finite evaluations)

ID kind: PD-T.
Aliases: corner expansion; Λ_c(n); b = (8/π²)(γ + log(8/π)); c = 1.84616…; κ = c − c₁²; N = n + ½ structure; proposal-1 Paper A (analytic part).
Split from: the combined T2 claim of `checks/decisive-gen4-2.md` and its summaries in `proposal-1.md`/`report.md` at `614709d` ("b to 12 digits, c = 1.846160310424 ± 2e-12, κ a genuinely two-dimensional constant"). The argmax statement is split to `PD-T?programme-ideas-claude-05`.
Split into: none.

## Statement

Let Pad_n be the Padua points of degree n (first family; `padua` in `checks/code/gen4/gen4_tests.py`, after Bos–Caliari–De Marchi–Vianello–Xu 2006), λ_n the Lebesgue function of total-degree interpolation on Pad_n over [−1, 1]², and Λ_c(n) the maximum of λ_n over the four corners (attained at the two non-node corners: (±1, −1) for even n, (−1, ±1) for odd n). **Conjecture (OPEN):** with N := n + ½,

  Λ_c(n) = (4/π²) log² N + b log N + c − 1/N + O(log N / N²),  b = (8/π²)(γ + log(8/π)),

for a constant c independent of the parity of n.

## Definitions

γ Euler's constant; c₁ = (2/π)(γ + log(8/π)) the constant of the 1-D Chebyshev Lebesgue constant; κ := c − c₁².

## Assumptions

None beyond the definitions.

## Status by part

Overall status: OPEN (supported by MEASURED finite evaluations; no proof, no remainder bound).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| exact finite-sum form of Λ_c(n) (N closed-form kernel terms) | MEASURED | agreement with the O(Nn) formula to 2.1e-13, n = 3…64, all four corners (`t2_onepage.py/.out`); identity not written as a proof |
| finite high-precision values of Λ_c(n) | MEASURED | 80-bit long double with exact mod-4 argument reduction, 28 even n in [64, 8192] and 22 odd n in [65, 4097]; mpmath (30 digits) agreement ≤ 7e-16 at n = 64, 128, 256 |
| fitted constants, **pre-registered fit family** (unshifted variable, K = 3, 4, 5, n_min ∈ {64, 128, 256, 512}, b free and fixed) | MEASURED | c ∈ [1.846095095877555, 1.846161206769239], half-spread 3.3055e-5 (developer disclosure in `decisive-gen4-2.md` T2(c); independent 18-fit replay `audit-support/proposal-fit.py/.json`). The pre-registered target "≥ 9 digits of c" is **not met**: T2's precision/separation target is inconclusive. |
| fitted constants, **post-registration, model-conditioned** (refit in N = n + ½ with the −1/N term) | MEASURED (post-registration) | b = 1.2255221257453, c = 1.846160310424, κ = 0.9197101183886, stable to ±2e-12 across the selected model's fits; 1/N coefficient −1.000000002. This is fit stability inside a model chosen after seeing the data, not an error bound on the asymptotic remainder. |
| the conjectured expansion itself | OPEN | needs an analytic proof or rigorous remainder control |
| identification of κ | OPEN | PSLQ/small-height searches at the post-registration tolerance found no relation; at the pre-registered 3.3e-5 tolerance every search is at chance level. Neither result shows that κ is a genuinely two-dimensional or new constant. |

## Depends on

None (finite evaluations only).

## Checks

`checks/code/decisive/gen4-2/t2_onepage.py`, `t2_identify.py`, `t2_odd.py`, `t2_halfshift.py` with outputs beside them (frozen at `614709d`; environment in `decisive-gen4-2.md`). Independent: `audit-support/proposal-fit.py` (mpmath QR refit of the stored finite values; does not repeat the large-n evaluations). Runs needed: independent recomputation of Λ_c(n) at large n; any remainder bound.

## Sources

Kolomoitsev–Lomako, arXiv 2009.07114v1, Thm 2.1 (leading coefficient 4/π² with O(log n) remainder; primary excerpt checked by the audit). De Marchi, Constr. Math. Anal. 5 (2022): heuristic fit ((2/π) log(n+1) + 1.1)² (coverage as recorded in `checks/adversarial-gen4-2.md`). Smith 2006 / Günttner for c₁ (coverage as recorded there).

## Proof or evidence

Finite evidence only, as tabulated. The near-agreement of the fitted b with (8/π²)(γ + log(8/π)) and of the 1/N coefficient with −1 suggests the form of the expansion; it is not a proof and does not bound the remainder.

## Scope

Padua points, corner value only. No claim about the global maximum (see `PD-T?programme-ideas-claude-05`), about other node families, or about paper-level novelty (the source-reading coverage of Kolomoitsev–Lomako and De Marchi 2022 is partial).

## Open items

Precise targets: `../OPEN_TARGETS.md` A1 (closed form of the corner value), A2 (the b-term), A3 (full expansion and κ).

Proof of the expansion (or of the b-term alone); rigorous evaluation of Λ_c(n) with error bounds; identification or characterisation of κ; full reading of Kolomoitsev–Lomako 2021 to see whether their method yields the second term.

## History

- 2026-11-01, gen4-2 adversary and decisive agents (claude-fable-5-1, xhigh): finite evaluations and fits; summaries reported "12 digits" and "±2e-12" as if pre-registered.
- 2026-11-01, Codex audit-01 A6: pre-registered and post-registration uncertainties must be reported separately; T2 target inconclusive.
- 2026-11-01, response-01 (claude-opus-5-5, effort not exposed): this record; summaries in `proposal-1.md`, `report.md` and the decisive file's verdict corrected (originals struck, not deleted).
