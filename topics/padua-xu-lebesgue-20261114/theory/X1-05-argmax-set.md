# PD-T?padua-xu-lebesgue-20261114-claude-05 — The maximizers of the Xu Lebesgue function are exactly the non-node vertices

ID kind: PD-T.
Aliases: X1-05; G3 for X1; argmax part of BCDMV Conjecture (17); X1-C2 / X1-C3 of the novelty gate.
Split from: BRIEF §1.2 outcome 1 (argmax set for every n) and round X1-2 target T4 (which asked only for a plan).
Split into: none.

## Statement

Let n ≥ 2. Then

  {x ∈ Q : λ_n(x) = Λ^Xu_n} = V*,

where V* is the set of all four vertices of Q = [−1,1]² if n is even, and V* = {(1,−1), (−1,1)} if n is odd. Equivalently: λ_n(x) < L_n² for every x ∈ Q ∖ V*, and λ_n = L_n² on V*.

For n = 1, λ_1 ≡ 1 = Λ^Xu_1 on Q (every point is a maximizer).

## Definitions

As in X1-01 to X1-04.

## Assumptions

Exact real arithmetic; conventions of `literature-xu-mp.md` §1. Even n is the setting of BCDMV Conjecture (17); odd n is the separately labelled variant.

## Status by part

Overall status: **PROVED** (written proof below, valid for every n ≥ 2 with no finite certificate range; audit pending).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Even n ≥ 2: argmax = four vertices (second part of Conjecture (17), with uniqueness) | PROVED | Proof below |
| Odd n ≥ 3: argmax = {(1,−1), (−1,1)} (variant) | PROVED | Proof below |
| n = 1 | PROVED | Remark at the end of the proof |
| Complementary-grid enumeration n ≤ 12, witness lifts, float grids n ≤ 24, G1 screen n ≤ 60 | MEASURED (verification only) | Checks |

Gate G3 note: G3 asks, for an all-n claim, for an analytic tail with explicit onset n₃ and certificates below it. Here the analytic proof covers every n ≥ 2, i.e. n₃ = 2, and the range below the onset is n = 1 (treated by hand). No computer certificate is part of the proof.

## Depends on

X1-01 (lift formula, Γ-invariant fibers), X1-02 (b) incl. (χ), and (c) (equality set of the one-dimensional bound, which is where n ≥ 2 is needed), X1-03 (b), X1-04 (2).

## Checks

`python3 code/xu/research/x1_argmax_check.py --nmax 12 --fmax 24` (run 2026-11-14, 24 s):
- mpmath 30 digits, general Path B kernel, every point (aπ/n, bπ/n) with a + b ≡ n (mod 2), n = 2..12: λ_n = L_n² at V* (deviation ≤ 3.9e−30) and λ_n < L_n² elsewhere; largest non-vertex ratio λ_n/L_n² per n: 0.5, 0.76, 0.7929, 0.7978, 0.7944, 0.8242, 0.8385, 0.8464, 0.8511, 0.8614, 0.8678 (n = 2..12), at the centre of Q for n = 2 and at an edge point for n ≥ 3; `witness_failures: 0` (the two explicit lifts of the proof lie over one node and have d-products of opposite signs, for every non-vertex complementary point).
- float64 grids with 6n+1 points per axis, n = 2..24: the set of grid points within 1e−9 of the grid maximum is exactly V*.
- `evidence/xu-g1-summary.json` (orchestrator's G1 screen, n = 2..60): vertex conjecture supported, relative gaps g_n between 0.5 and 0.0697.

## Sources

LITERATURE: BCDMV, Computing 76 (2006), p. 318 (numerical observation that the maximum is at the four vertices, n even ≤ 100), eq. (17) p. 319 and pp. 323–324 (conjecture, listed as open); `literature-xu-mp.md` §4. No source read proves it; novelty wording as in X1-04.

## Proof or evidence

Let n ≥ 2 and let x ∈ Q with λ_n(x) = Λ^Xu_n = L_n² (X1-04 (3)). Write x = (cos θ₁, cos θ₂) with θ₁, θ₂ ∈ [0, π] and u = (θ₁+θ₂)/2, v = (θ₁−θ₂)/2.

**Step 1 (u and v are midpoints).** By X1-04 (2), L_n² = λ_n(x) ≤ ω_n(u)ω_n(v) ≤ L_n², and 0 ≤ ω_n ≤ L_n, L_n > 0; hence ω_n(u) = ω_n(v) = L_n. By X1-02 (c) (n ≥ 2), u = u_i and v = u_j with integers i ≡ j ≡ n (mod 2). So θ₁ = aπ/n, θ₂ = bπ/n with a = (i+j)/2, b = (i−j)/2 integers in [0, n], a + b = i ≡ n (mod 2). Every term t_{pq} = d_n(u_i − u_p) d_n(u_j − u_q), (p, q) ∈ C_n², is nonzero and has the sign χ(i−p)χ(j−q) (X1-02 (b)).

**Step 2 (a sign identity).** For every even integer e with e ≢ 0 (mod 2n): χ(e+1) χ(e−1) = −1.
Proof. By (χ) we may replace e by its residue e₀ ∈ {2, 4, …, 4n−2} ∖ {2n}. If e₀ < 2n, then e₀ ± 1 ∈ {1, …, 2n−1} and χ(e₀+1)χ(e₀−1) = (−1)^{e₀/2}(−1)^{(e₀−2)/2} = −1. If e₀ > 2n, put e₁ = 4n − e₀ ∈ {2, …, 2n−2}; then e₀ ± 1 ≡ −(e₁ ∓ 1) (mod 4n), so χ(e₀+1)χ(e₀−1) = χ(e₁−1)χ(e₁+1) = −1 by the first case. ∎

**Step 3 (a cancelling pair unless x is a vertex).** Suppose x is not a vertex. Then b ∉ {0, n} or a ∉ {0, n}.

*Case b ∉ {0, n}.* Then i − j = 2b ≢ 0 (mod 2n). Take (p, q) = (i+1, j+1) ∈ C_n² and s(p, q) = (q, p); both lie in the same fiber F(ξ₀) (fibers are Γ-invariant, X1-01 (a)). Their signs are
 χ(i−p)χ(j−q) = χ(−1)χ(−1) = +1 and χ(i−q)χ(j−p) = χ(i−j−1)χ(j−i−1) = χ(e+1)χ(e−1) with e = j − i (χ is even),
and the latter is −1 by Step 2.

*Case a ∉ {0, n}.* Then i + j = 2a ≢ 0 (mod 2n). Take (p, q) = (i+1, j−1) ∈ C_n² and c(p, q) = (−q, −p) = (1−j, −1−i), in the same fiber F(ξ₀). Their signs are
 χ(i−p)χ(j−q) = χ(−1)χ(1) = +1 and χ(i+q)χ(j+p) = χ(i+j−1)χ(i+j+1) = χ(e−1)χ(e+1) with e = i + j,
which is −1 by Step 2.

In both cases F(ξ₀) contains two (necessarily distinct) elements whose terms t_{pq} are nonzero and of opposite signs, so |Σ_{F(ξ₀)} t_{pq}| < Σ_{F(ξ₀)} |t_{pq}|, i.e. Δ_n(θ₁, θ₂) > 0 in X1-04 (1). Then λ_n(x) = ω_n(u_i)ω_n(u_j) − Δ_n < L_n², a contradiction.

**Step 4 (which vertices).** So x = (z_a, z_b) is a vertex, a, b ∈ {0, n}, and a + b ≡ n (mod 2) by Step 1. For n even all four vertices satisfy this congruence. For n odd it holds only for (a, b) = (0, n) and (n, 0), i.e. for x = (1,−1) and (−1,1); the other two vertices are nodes, where λ_n = 1. Hence x ∈ V*. Conversely λ_n = L_n² on V* by X1-03 (b). ∎

*n = 1.* X_1 = {(1,1), (−1,−1)}, V_1 = span{1, x+y}, ℓ_{(±1,±1)} = ½(1 ± (x+y)/2) ≥ 0 on Q, so λ_1 ≡ 1.

## Scope

- Settles the second part of BCDMV Conjecture (17) for every even n ≥ 2, in the strong form "attained exactly at the four vertices", and the odd-n variant.
- It does not describe the other local maxima of λ_n. By X1-04 (1), at every complementary grid point (aπ/n, bπ/n), a + b ≡ n (mod 2), λ_n = L_n² − Δ_n with Δ_n > 0 off V*; the measured size of Δ_n (bounded away from the vertices, about 0.89 at the edge centre) is recorded in X1-08.

## Open items

- Audit. The auditor should check Step 1's use of X1-02 (c) (the only place where n ≥ 2 enters) and the two sign evaluations of Step 3.
- Novelty gate for the exact argmax statement (orchestrator/auditor).

## History

2026-11-14, Claude Fable 5.2 (xhigh), round X1-2 researcher. The assigned target T4 was a plan for an argmax localization modelled on PR #27 (analytic corner expansion, localization away from the corners, finite certificates). That architecture is not needed for Xu points: the product bound of X1-04 confines maximizers to the complementary checkerboard, and a two-term sign cancellation excludes every non-vertex point of it. No lemma of the unmerged PR #27 is used.
