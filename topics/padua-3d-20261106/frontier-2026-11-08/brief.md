# 3-D Padua frontier brief (for literature/inspiration scouts) — 2026-11-08

## Target (unchanged since 2026-11-06)
Find explicit point sets X_n ⊂ [-1,1]^3 with exactly N = binom(n+3,3) points that are unisolvent for
total-degree polynomials Π_n(R^3) and whose Lebesgue constant (uniform norm of the interpolation operator)
grows polylogarithmically, ideally O(log^3 n), as 2-D Padua points achieve (4/π²) log² n in the square.
Second-best: a proved polynomial bound with a small exponent beating the numerical baselines; or a theorem
that natural classes cannot work. Padua mechanism in 2-D: cosine image of a rank-1 lattice / generating
Lissajous curve whose self-intersections give exactly N nodes, Haar pushforward = positive cubature of degree
2n−1 on those N nodes, and an explicit reproducing-kernel Lagrange formula.

## What is PROVED in this repository (topic padua-3d-20261106)
- Single torus cosets invariant under every coordinate reflection never give minimal unisolvent sets (n≥2).
- Monotone Padua-plane stacks: unisolvent, but Λ ≥ exp(0.1827 n) (3ζ(3)/(2π²)); stacks are poor generally.
- Universal lower bounds: Λ ≥ 3/4+3/(2π) > 1.2274 for all n; Λ ≥ O_{⌊n/2⌋}^3/(3π³) (leading (log n)³/(24π³)).
  Subbotin (1983) already has the log^d order. Classical Fekete: Λ ≤ N = O(n³).
- Explicit R-Leja lower set (Chkifa 2015 premise): Λ ≤ 8·binom(n+9,9) = O(N³) — known theory, poly but huge.
- Cosine coset classification: complete n=2 all-phase classification (36 representatives); cyclic orbit
  M=N (phase-shifted) witnesses exist exactly at parity-admissible degrees n≢2 mod 4 (verified n≤12) but quality poor.
- Haar/dual-lattice reduction: an unshifted coset's equal-weight rule is exact through degree D iff its dual
  lattice has no nonzero vector of ℓ1-norm ≤ D. Strictly positive full-support unshifted rules exact to 2n−1
  need ≥ 19n³/108 nodes (Betke–Henk octahedron lattice packing density 18/19), so exact-N fails for n≥110;
  exhaustive: NO positive full-support unshifted exact-N rule at n=3..7. "Padua-type" (unisolvent + exact N +
  positive degree-(2n−1) cubature) exists only at n=1,2 in that class (order-19 cyclic sets at n=2, Λ≈8.13).
- Global minima of folded node count for Haar degree-(2n−1) cubature: n1..5: 2,7,16,35,54; among full-rank
  (Π_n-determining) ones: 4,10,24,45,75 (vs N = 4,10,20,35,56).
- Anisotropic parity grid (orders n,n+1,n+1; ≈1.5N nodes; DMVX 2009-type): exact Gram I+ee^T, least-squares
  projection norm O(log⁴ n) proved locally, O(log³ n) CONDITIONAL on Kolomoitsev–Lomako polyhedral Dirichlet
  theorem. So log³ is (essentially) achieved with ~1.5N nodes by least squares, NOT interpolation.
- Several exact finite node sets: a 455-point Π_12-unisolvent optimized set; pruned 546-site (n12) and
  1163-site (n16) full-rank LS sets.

## MEASURED state (21³/41³ mesh lower samples; not certified)
| n | QR approx Fekete (tensor Lobatto candidates) | locally optimized (U2 bounded update) | log³n |
|---|---|---|---|
| 4 | 11.2 | 5.54 | 2.7 |
| 8 | ~? | 12.30 | 9.3 |
| 12 | ~? | 26.0 | 15.3 |
| 16 | 161.5 (QR), 93.6 localdet | 71.7 (969-site) | 21.2 |
Best minimal-node sets grow roughly linearly-to-quadratically in n numerically; nothing near log³.
Oversampled LS with 1.5N nodes: ~12.7–16.6 at n=16.

## KILLED / exhausted-in-scope routes (do not re-propose without a new separating idea)
Single reflection-invariant cosets; generic Lissajous curves (no self-intersections in 3D); unshifted cyclic
orbits at M=2N−1 (degree 3 fully excluded mod 39); fixed formula generators; phase-shifted M=N rules optimized
by determinant (quality kill n7/8); cyclic unions of 2–4 cosets (gates killed); half-shift M=2N first-unit class
(even n fail by theorem; odd n quality loss vs QR); folded rank-two classification; mixed folded/unfolded
witnesses (quality loss); Padua-plane stacks (monotone exponential; others lose to Leja); fixed Gauss-grid
thinning for degree-5 cubature (21 positive / 15 signed minimum); extraction of N nodes from near-minimal
lattice cubature by restricted QR or boundary removal (killed n6/7); pruning of oversampled grids (finite only);
direct norm optimization (works finitely but Λ still grows ~ like 2–5× log³ and costs grow).

## OPEN, concretely
- Any explicit family with proved polynomial Λ smaller than O(N³)? Any with polylog?
- Phased cosets / non-Haar positive weights / unions escape the packing obstruction — unexplored at scale.
- A Padua-type set (unisolvent, N nodes, positive degree-(2n−1) cubature) for some n ≥ 3 — excluded only for
  unshifted single cosets; Möller/commutator lower bounds (degree 2n−1 needs ≥ 12/24/41 nodes at n=3/4/5 vs
  N=20/35/56) do not forbid it.
- Is log³ achievable at all by minimal-node interpolation in the 3-cube? Literature status?
