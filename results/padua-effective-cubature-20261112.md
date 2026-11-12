# padua-effective-cubature-20261112 — effective Theorem A and the Padua Lebesgue-constant corollary

This file is written only by the topic orchestrator. Branch `claude/padua-effective-cubature-20261112`. Provisional IDs `PD-T?padua-effective-cubature-20261112-claude-NN`; final IDs are assigned at PR preparation. Every claim here awaits the Codex audit.

## Status (2026-11-12): session 1 complete, Codex audit pending (handoff 02)

- **C0 (-01), PROVED, assembly of merged results; independent Opus check done, no BLOCKING.** The Padua Lebesgue constant equals the corner value Λ_c(n), attained exactly at the two non-node corners, for 2 ≤ n ≤ 32 and for n ≥ N_* (N_* non-effective). Hence, for n ≥ max(32, N_*),
  Λ(Pad_n) = (4/π²)log²N + b log N + c + R_n (for n ≥ max(32, N_*)), N = n + ½,
  with PD-T271's explicit R_n → 0 and c = 1.8461603104239260797598387379… (parity independent).
  [record](../topics/padua-effective-cubature-20261112/theory/lebesgue-constant-corollary.md)
- **Delsarte bound (-02), PROVED.** Every positive closed-cube rule exact on Π_{2n−2} satisfies N ≥ (n − ½)³ D(int 2O)/8 for every n ≥ 1, and N ≥ n³D(int 2O)/8 if it is exact on Π_{2n−1}, where D is the Delsarte constant of the open double octahedron. The finite form is M ≥ f(0)/c₀ for nonnegative trigonometric f whose coefficients are ≤ 0 beyond the exact range.
  [record](../topics/padua-effective-cubature-20261112/theory/delsarte-bound.md)
- **Uniform Theorem A (-03), PROVED with LITERATURE dependency** on Kolountzakis–Lev–Matolcsi 2025, Thm 6.4, which shows that a non-tiling convex body has Delsarte constant above its volume:
  N ≥ (1 + γ_A)n³/6 for all n (rules exact on Π_{2n−1}), with γ_A = (3/4)D(int 2O) − 1 > 0.
  This is an alternative to the D1 compactness proof of Theorem A (PD-T557), with an explicit dependence on a single constant.
  [record](../topics/padua-effective-cubature-20261112/theory/uniform-theorem-a.md)
- **Cap (-04), PROVED.** D(int 2O) ≤ 38/27, so γ_A ≤ 1/18, from an exact check of the Betke–Henk/Minkowski lattice. Finite torus LPs are bounded by lattice-rule counts. Consequence: the uniform bound -03 can exclude Padua packages only for n ≥ 110, the same threshold as the merged lattice-class bound 19n³/108 (the case γ_A = 1/18).
  [record](../topics/padua-effective-cubature-20261112/theory/lp-cap.md)
- **Explicit γ (-05), OPEN.** Target: a certified Delsarte function with ∫φ > 4/3.
  [record](../topics/padua-effective-cubature-20261112/theory/explicit-gamma-target.md)
- **Torus-LP finite limitation (-06, PD-N), PROVED by exact lattice witnesses.** The finite torus LPs (plain or Delsarte, any spectrum), combined with M ≤ 8N, cannot exclude a package at any n in the witnessed range given in the record.
  [record](../topics/padua-effective-cubature-20261112/theory/limitation-torus-lp-finite.md)
- **Plain Turán route (BRIEF E1 as written), deferred and MEASURED-killed.**
  - Deciding it would require showing that the octahedron is a non-Turán domain, which KLM report as a major open problem.
  - The plain torus LP measures at Fisher: ρ_n = 1 within 3e-6 for n = 2…12.
- **Delsarte torus LP, MEASURED:** ρ^Del ≈ 1.08 at n = 5…8 (K = 3n−2). It has no rigorous finite certificate.
- **Cube-native LP, MEASURED:** λ ≈ 1.20–1.21 at n = 2, 3, 4, far below the 1 + 3/n needed for an exclusion.
- **Gates.** Q0 PASS; Q1 PASS; Q2 plain KILL, Delsarte INCONCLUSIVE; Q3 not exercised (no finite exclusion claimed).
- [Report](../topics/padua-effective-cubature-20261112/report.md).

## Next step

The Codex audit of session 1 is in handoff 02 (`topics/padua-effective-cubature-20261112/handoffs/02-audit.md`). After it: the certified Delsarte function (-05) and the cube-Delsarte LP (IDEA?…-claude-06).
