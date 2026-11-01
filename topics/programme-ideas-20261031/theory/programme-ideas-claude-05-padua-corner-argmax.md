# PD-T?programme-ideas-claude-05 — The Padua Lebesgue function attains its maximum at a non-node corner (OPEN; finite search without counterexample)

Final ID: **PD-T099** (allocated 2026-11-01 under AC's authorisation; the provisional ID above and in the text is retained as provenance — see ID_CROSSWALK.md).

ID kind: PD-T.
Aliases: corner argmax; "Λ(Pad_n) = Λ_c(n)"; De Marchi 2022 corner observation; proposal-1 Paper A (argmax part); T1.
Split from: `checks/decisive-gen4-2.md` T1 and Verdict at `614709d` ("true for all 75 degrees tested up to 200").
Split into: none.

## Statement

**Conjecture (OPEN):** for every n ≥ 2, max_{[−1,1]²} λ_n = Λ_c(n), attained at the non-node corners ((±1, −1) for even n, (−1, ±1) for odd n), with notation as in `PD-T?programme-ideas-claude-04`.

## Definitions

As in PD-T?programme-ideas-claude-04. R(n): the largest value of λ_n found away from the corners by the search below; G(n) = Λ_c(n) − R(n).

## Assumptions

None.

## Status by part

Overall status: OPEN.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| no counterexample at the tested degrees | MEASURED | n = 2…64 and n ∈ {65, 72, 80, 81, 96, 97, 112, 128, 129, 160, 161, 200} (75 degrees; 192/193 dropped for time): no evaluated non-corner value of λ_n exceeded Λ_c(n) + 1e-9 on Chebyshev-angle meshes plus edge grids with Newton-polished candidate maxima (`checks/code/decisive/gen4-2/t1_argmax.py/.out/.json`, `t1_tail.py/.out`). Finite meshes only: this is not a bound on the continuous supremum. |
| runner-up and gap | MEASURED | runner-up always an edge maximum near the midpoint of an edge x = ±1; G decreases from 0.87 (n = 5) to 0.552 (n = 200); fit G ≈ 0.548 + 0.84/n for n ≥ 32 |
| the statement for all n, or for any single n on the continuum | OPEN | needs constant-order asymptotics at the corner and at the edge midpoint plus an a-priori bound elsewhere (since G does not grow) |

## Depends on

PD-T?programme-ideas-claude-04 for the definition of Λ_c(n) only.

## Checks

As in the table (frozen at `614709d`). Not independently repeated by the audit (the n ≤ 200 sweep is expensive). Runs needed: an independent rerun; a rigorous enclosure for any single n.

## Sources

De Marchi, Constr. Math. Anal. 5 (2022): corner observation (coverage as recorded in `checks/adversarial-gen4-2.md`).

## Proof or evidence

Finite search as tabulated.

## Scope

Padua points only; the statement is a conjecture. "No counterexample found at 75 tested degrees on finite meshes" is the full extent of the evidence.

## Open items

Precise target and decomposition: `../OPEN_TARGETS.md` A4.

Proof for all n; rigorous verification for small n (e.g. by a certified sup bound away from the corners).

## History

- 2026-11-01, decisive agent (claude-fable-5-1, xhigh): T1 run; Verdict said "true for all 75 degrees tested up to 200".
- 2026-11-01, Codex audit-01 A9.3: replace by "no counterexample found at 75 tested degrees on finite meshes"; continuous/global statement remains OPEN.
- 2026-11-01, response-01 (claude-opus-5-5, effort not exposed): this record; source wording corrected.
