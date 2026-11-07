# PD-T?padua-3d-20261106-codex-T10-06 — log³ cubature-projection target

ID kind:PD-T. Aliases:T10.4 Dirichlet-kernel target. Split from:none. Split into:none.

Task provenance: handoff06 T10.4. Supporting dependency: PD-T?padua-3d-20261106-codex-T10-04, the log-four theorem, not a proved case or conjunct of this target.

## Statement and status

For the best tested full-rank cubature family, prove a degree-uniform `||Pn||∞=O(log(n+2)^3)`. Overall status: **PROVED with explicit LITERATURE dependency**, by the separate source-dependent corollary under the response03 E4 proposal. All finite mesh values remain MEASURED lower bounds. The separate self-contained theorem proves O(log⁴) and exact Gram control, but neither is a case or conjunct of the original log³ statement.

## Actual proof attempt and exact remaining gap

The reflection formula reduces the raw cosine kernel to the octahedral trigonometric Dirichlet kernel D_n. A Fejer reproducing argument proves that sampling on these parity grids costs an absolute constant13³, and exact Gram inversion changes the anisotropic operator by norm<=1. Thus the desired conclusion follows from the sharper continuous estimate `||D_n||L1 <= C log(n+2)^3`. The elementary generating-function/Cauchy argument was carried through completely and gives log⁴, with the extra logarithm at the factor J(rho) from the slack variable. No cancellation estimate removing that factor is supplied. A standard polyhedral Lebesgue-kernel theorem might close this gap, but no unread theorem is promoted into a proof.

The projection-bound attempt therefore produced a genuine uniform polylog supporting result and a precise remaining analytic estimate. It does not prove minimal-node interpolation stability: T9-05 still needs a uniform inverse restriction bound, and the frozen extraction measurements are adverse. Sources/coverage: literature-T10, particularly Cools–Poppe and the inherited De Marchi–Vianello–Xu records. Independent mathematical audit of the supporting theorem remains required. History:2026-11-06 Codex Sol xhigh assigned; next step is primary verification or direct proof of the sharp continuous kernel estimate.

## Dated source addendum, 2026-11-06

Subsequent actual primary retrieval found Kolomoitsev–Lomako arXiv1801.00608v1 Theorem4.1 in the exact form needed. The separate `t10-log3-corollary.md` records the local implication and the source-proof coverage limit. At that source-addendum boundary the implication was labelled CONDITIONAL. Response03 harmonizes it as **PROVED with explicit LITERATURE dependency**; the remaining self-contained proof task is OPEN. This does not change the initial proof-gap history or import the unread supporting §3 proofs.

History 2026-11-06 (response03): the original OPEN analytic gap and later
CONDITIONAL label are historical. The present target has one overall
status, **PROVED with explicit LITERATURE dependency**, via T10-07;
removing the external theorem is a distinct OPEN proof task, not a second
status for this statement. No claim about N-node interpolation follows.
