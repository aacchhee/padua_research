# PD-T?padua-3d-20261106-codex-T10-05 — near19/18 folded cubature target

ID kind:PD-T. Aliases: near-Padua Chebyshev lattice count. Split from:none. Split into:none.

Task provenance: handoff06 T10.4. Supporting dependency: PD-N?padua-3d-20261106-codex-T10-03, a counterexample to the density-only inference, not a case or conjunct of this target.

## Statement and status

Original target: find integer dual lattices of shortest l1 norm>=2n whose cosine images have `|X| <= (19/18+o(1)) binomial(n+3,3)`. Overall status:**OPEN**. The finite bounded census did not approach this ratio. Its best full-rank catalogue is the established anisotropic parity family tending3/2. The critical scaled family instead tends73/18, proved in its separate record. Neither fact rules out other families.

## Actual proof attempt and obstruction

The attempted proof was to combine determinant38n³/27 with eightfold cosine folding. Its missing assertion would be that almost every full sign orbit lies in H; determinant/8 is only a lower bound. Computing the sign closure of the standard critical lattice proves that this assertion fails there: four F19 lines produce146m³ sign-closure points, not38m³. Thus density alone cannot finish the target. A successful proof needs simultaneous control of all coordinate-reflection intersections of H, not just detL and its shortest vector. This is a specific failed proof route, not a whole-direction obstruction.

## Checks, sources and limits

Depends on the written proof in `t10-critical-folding.md`, the finite `t10-census.json`, and published packing optimum with coverage in literature-T10. No arbitrary phases, non-Haar weights or exhaustive n4..16 lattice minima have been settled. The handoff's conditional clause “if ratio tends19/18 numerically” did not occur, but its underlying inference was actually tested and corrected. History:2026-11-06 Codex Sol xhigh assigned. Next step: a new reflection-aware bound/search, with a fresh preregistration; no claim it has been exhausted.
