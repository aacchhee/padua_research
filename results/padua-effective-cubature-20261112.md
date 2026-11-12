# padua-effective-cubature-20261112 — effective Theorem A and the Padua Lebesgue-constant corollary

This file is written only by the topic orchestrator. Branch `claude/padua-effective-cubature-20261112`; no PR yet. Provisional IDs `PD-T?padua-effective-cubature-20261112-claude-NN`; final IDs are assigned at PR preparation. Every claim here awaits the Codex audit.

## Status (2026-11-12): WORK, session 1

- **C0 (-01), PROVED, assembly of merged results; independent check pending.** The Padua Lebesgue constant equals the corner value Λ_c(n), attained exactly at the two non-node corners, for 2 ≤ n ≤ 32 and for n ≥ N_* (N_* non-effective). Hence, for n ≥ max(32, N_*),
  Λ(Pad_n) = (4/π²)log²N + b log N + c + R_n, N = n + ½,
  with PD-T271's explicit R_n → 0 and c = 1.8461603104239260797598387379… (parity independent).
  [record](../topics/padua-effective-cubature-20261112/theory/lebesgue-constant-corollary.md)
- **Delsarte bound (-02), PROVED.** Every positive closed-cube rule exact on Π_{2n−2} satisfies N ≥ (n − ½)³ D(int 2O)/8 for every n ≥ 1, where D is the Delsarte constant of the open double octahedron. The finite form is M ≥ f(0)/c₀ for nonnegative trigonometric f whose coefficients are ≤ 0 beyond the exact range.
  [record](../topics/padua-effective-cubature-20261112/theory/delsarte-bound.md)
- **Uniform Theorem A (-03), PROVED with LITERATURE dependency** on Kolountzakis–Lev–Matolcsi 2025, Thm 6.4, which shows that a non-tiling convex body has Delsarte constant above its volume:
  N ≥ (1 + γ_A)(2n − 1)³/48 for all n, with γ_A = (3/4)D(int 2O) − 1 > 0.
  This is an alternative to the D1 compactness proof of Theorem A (PD-T557), with an explicit dependence on a single constant.
  [record](../topics/padua-effective-cubature-20261112/theory/uniform-theorem-a.md)
- **Cap (-04), PROVED.** D(int 2O) ≤ 38/27, so γ_A ≤ 1/18, from an exact check of the Betke–Henk/Minkowski lattice. Finite torus LPs are also bounded by lattice-rule counts. Consequence: these LP routes with 8N ≥ M can exclude Padua packages only for n ≥ 138.
  [record](../topics/padua-effective-cubature-20261112/theory/lp-cap.md)
- **Explicit γ (-05), OPEN.** Target: a certified Delsarte function with ∫φ > 4/3.
  [record](../topics/padua-effective-cubature-20261112/theory/explicit-gamma-target.md)
- **Plain Turán route (BRIEF E1 as written), deferred.** It would require showing the octahedron is a non-Turán domain, which KLM report as a major open problem.
- **Gates.** Q0 PASS; Q1/Q2 pending LP runs.

## Next step

See the open handoff in `topics/padua-effective-cubature-20261112/handoffs/`.
