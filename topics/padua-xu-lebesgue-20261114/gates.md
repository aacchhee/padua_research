# Gates — padua-xu-lebesgue-20261114

Written by Claude (Opus 5.5, orchestrator) on 2026-11-14 at rules `2d60e22`. Committed and pushed **before** any run in this topic. A pre-registration is never edited after its first push; changes go in a dated addendum below it. Verdicts are appended under each gate with date, commit and evidence path.

Notation. λ_n(x) = Σ_{A∈X_n} |ℓ_A(x)| is the Lebesgue function of the node set X_n on the square Q = [−1,1]², and Λ_n = max_Q λ_n. Angles: x = (cos θ, cos φ), (θ, φ) ∈ [0,π]². V = the four vertices of Q; V* ⊂ V the vertices that are **not** nodes. "Xu" and "MP" definitions are fixed in `literature-xu-mp.md` §Conventions before G0 runs; if a source disagreement remains, G0 is run for each variant and the variant used in a claim is named in it.

## G0 — implementation sanity (X1 and X2 separately)

For every admissible n ≤ 12 (both parities where defined):
1. **Path A (exact linear algebra).** Lagrange basis by solving the Vandermonde system of the interpolation space in the product Chebyshev basis T_i(x)T_j(y). Arithmetic: exact in ℚ(cos(π/n)) via sympy/flint algebraic numbers, or interval arithmetic (python-flint arb) at ≥ 200 bits with all output enclosures of width < 10⁻³⁰.
2. **Path B (closed form).** The compact kernel / fundamental-function formula of the source, evaluated in mpmath at ≥ 50 digits.
3. Checks:
   - cardinality equals the dimension of the interpolation space; the Vandermonde determinant is nonzero (exact, or its enclosure excludes 0);
   - ℓ_A(B) = δ_AB at all nodes (path A exactly; path B to 10⁻⁴⁰);
   - path A and path B agree at all nodes and at 200 seeded pseudo-random points of Q (seed 20261114) to 10⁻³⁰ relative;
   - Λ_n values agree with every published value available (`literature-xu-mp.md`) to the printed precision, **or** exceed it with the excess attributable to the source's sampling grid (documented by re-evaluating on that grid).

**Kill:** any unresolved mismatch in 3. A kill stops all claims depending on the implementation until resolved.

## G1 — X1 argmax screen (MEASURED only)

For n = 2, …, 60 (both parities):
1. Evaluate λ_n (path B in double precision, cross-checked against path A for n ≤ 12) on the uniform angle grid θ_i = iπ/M, φ_j = jπ/M, i, j = 0..M, M = max(64, 12n). Symmetry reduction may be used only for symmetries proved from the definition in `literature-xu-mp.md` (stated there with proof); otherwise use the full grid.
2. Take every discrete local maximum of the grid (8-neighbourhood, boundary included, edges handled as 1-D/0-D faces) with value ≥ 0.9 · max_{v∈V*} λ_n(v). Refine each by bounded quasi-Newton in (θ, φ) in double precision, then polish in mpmath at 40 digits (Newton on the gradient, restricted to the face it lies on).
3. A refined point within angle distance 10⁻⁸ of a vertex is classified as that vertex. Every other refined point is a non-vertex candidate.
4. Report per n: λ_n at each vertex, the best non-vertex candidate (location, face: interior / open edge, value), and the relative gap g_n = 1 − max_{non-vertex} λ_n / min_{v∈V*} λ_n(v).

**"Vertex conjecture supported"** at all tested n means g_n > 10⁻⁹ for every n, with every g_n < 10⁻⁶ re-polished at 60 digits.

**Kill (of the argmax part of Conjecture (17), for the variant tested):** at some n a non-vertex point x* and a vertex value with λ_n(x*) > max_{v∈V*} λ_n(v) **certified** by interval arithmetic (path A or an interval version of path B, enclosures disjoint), checked by a committed checker and rerun independently on the other code path. Only then is a PD-N registered (PROVED negative at that n). An uncertified numerical excess is MEASURED and only triggers certification.

If the statement of (17) on record concerns only one parity or only V* (decided from the literature before G1 runs), the kill criterion applies to that statement exactly; behaviour of the other parity is recorded as MEASURED context.

## G2 — corner (vertex) value and expansion

Acceptance needs:
- a written proof of a closed form for λ_n(v), v ∈ V*, and of an expansion λ_n(v) = (4/π²) log² N + b log N + c + R_n with every constant explicit and |R_n| ≤ (explicit bound) for every n ≥ n₂ (explicit), for a stated expansion variable N;
- agreement of the closed form with path B at 50 digits for every n ≤ 200 (a MEASURED check only, never the source of a constant).

## G3 — argmax certificates

A finite-degree argmax claim ("for n in S the maximizers of λ_n on Q are exactly V*") needs for every n ∈ S: an exact or interval certificate, a committed checker, and an independent rerun on a separate code path. An all-n claim additionally needs a written analytic tail with an explicit onset n₃ and G3 coverage of every n < n₃. An onset that is only existential gives an "eventually" statement, kept distinct from "for every n".

## G4 — X2 lower bound

A written proof of Λ_MP(n) ≥ c·n² for every admissible n ≥ n₀ with c > 0 and n₀ explicit. Numerical location of the extremal point is MEASURED and a guide only. A sharp-constant claim needs a written proof of the limit; numerical fits never set a constant.

## G5 — scope honesty

- Numerical fits never set a constant or a status.
- "Eventually" and "for every n" are kept apart, and so are the two parities and the source variants.
- Any use of an unmerged PR #27 lemma as a lemma makes the claim CONDITIONAL on it (BRIEF §1.3).
- Literature facts are LITERATURE, cited with locator; no source proof is inherited.

## Verdicts

(none yet)

## Addendum 2026-11-14 (before any run): G1-MP screen and X2 corner checks

Pre-registered by the orchestrator after the literature verdict in `literature-xu-mp.md` §3 (X2 lower bound already published). Same rules as G1, applied to MP points, n even, 2 ≤ n ≤ 60:
- grid M = max(64, 12n) in angles, symmetry reduction only by x ↦ −x (Lemma S / BBDM Lemma 15); refinement and classification as in G1 steps 2–3; report per n the four vertex values, the best non-vertex candidate, and g_n relative to max(λ(1,1), λ(−1,1)).
- **Corner check (C-MP):** λ_n at the four vertices by G0 path A (interval, ≥ 256 bits) for every even n ≤ 30. "BBDM corner symmetry refuted at n" means certified λ_n(1,1) ≠ λ_n(1,−1) (disjoint enclosures). A refutation is registered as a PD-N only with a committed checker and an independent rerun on path B (as in G1's kill clause).
- No numerical observation sets a constant (G5).

### Verdicts (2026-11-14, developer runs; independent rerun by the auditor still required)

- **G0 Xu: PASS** (n = 1..12, both parities). All G0 checks ran (path A arb 256-bit vs path B mpmath to ~1e−59; δ property; published BCDMV Table 7 values at n = 34, 48, 62, 76 reproduced at the vertex; Lemma S invariances numerically confirmed). Evidence: `evidence/xu-g0.json`; command `python3 code/xu/g0_check.py --nmax 12` (3 min 6 s). Developer: Sonnet 5.5 high.
- **G0 MP: PASS** (even n = 2..12). Evidence: `evidence/mp-g0.json`. Developer: Sonnet 5.5 high.
- **G1 Xu: "vertex conjecture supported"** for n = 2..60, both parities (MEASURED). min g_n = 0.0697 at n = 60; g_n decreases slowly (0.207 at n = 4, 0.13 at n = 12, 0.081 at n = 40). The runner-up is always the **edge midpoint** family (exactly the midpoint for n ≡ 0 mod 4); the best interior local maximum ratio is 0.866 at n = 60. No kill flag. Evidence: `evidence/xu-g1-summary.json`; command `python3 code/xu/g1_screen.py --nmin 2 --nmax 60`.
- **G1-MP: argmax at (±1,1) only** for even n = 2..60 (MEASURED). No local maximum reaches 0.9·λ(1,1); the best non-vertex local maximum is on the edge x = ±1 near y = −1 at ≈ 0.403·λ(1,1); g_n ≈ 0.597 for n ≥ 8. Evidence: `evidence/mp-g1-summary.json`.
- **C-MP:** Path-A enclosures for even n ≤ 30 contain n+1 at (±1,−1) and certify λ(1,1) ≠ λ(1,−1) at every tested n. Path-B checker: `evidence/mp-cmp-check.json`. A PD-N needs the theory record and the auditor's rerun.
