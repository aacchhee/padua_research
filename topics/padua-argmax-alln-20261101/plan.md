# All-degree Padua argmax (A4 / PD-T099) — proof strategy

Status: **planning note, WORK stage, no proof claimed.** Written 2026-11-01 by Claude (claude-opus-5-5) at AC's request ("write this down on a new branch, then we'll update it after part2 is done"). It records the strategy proposed in chat, and the quick float64 checks it rests on. It is to be revised once `codex/padua-proof-attempts-2-20261101` (PR #12) finishes A4(a), B3 and B1 and is audited; see [handoff 01](handoffs/01-update-after-part2.md).

## Target

PD-T099 (OPEN; OPEN_TARGETS A4 of `topics/programme-ideas-20261031`): for every n ≥ 2,

  max_{[−1,1]²} λ_n = Λ_c(n), attained only at the non-node corners,

with the even-checkerboard Padua nodes of PD-T101 and λ_n = Σ_B |L_B|.

Known at the time of writing:
- PD-T101 (A1, PROVED): the exact corner formula.
- Part 2, audit pending, at pinned head `b5bba7cf1328b1f207aea001a439c3fe4af0146f`:
  - A2: Λ_c(n) = (4/π²)log²n + (8/π²)(γ+log(8/π)) log n + O(1), with |error| ≤ 68, plus the product comparison |Λ_c − L_n²| ≤ 54 (records 01–04).
  - A4 for n = 3,…,7: certified global argmax (records 07, 11, 17, 42, 52).
  - A4(a) so far: the exact all-edge kernel formula (70), the complementary-ordinate gaps (71), a common limiting edge gap g ∈ (1/45, 2] (72), and its certified rational-series characterization (73).
  - Central-envelope comparison: OPEN.

## 1. Exact reformulation as a reflected lattice sum

Let Λ be the Padua lattice on the torus T² = (ℝ/2πℤ)²:

  Λ = {(jπ/n, kπ/(n+1)) : j+k even},  |Λ| = 2n(n+1).

Equivalently it is the rank-1 "generating-curve" lattice {s·(n+1, n)·π/(n(n+1)) : s ∈ ℤ}.

Put h_0 = 1 and h_k = 2 for k ≥ 1, and

  G_n(u,v) = Σ_{a+b≤n} c_ab cos(au) cos(bv),  c_ab = h_a h_b except c_{n,0} = 1.

(This is the Padua reproducing kernel with the corrected x-term. It was checked against Vandermonde inversion at n = 3, 4; see `code/check.py`.)

Since T_a(cos t)T_a(cos s) = ½[cos a(t+s) + cos a(t−s)] and Λ is invariant under the four reflections σ ∈ {±1}², the Padua cubature identity gives

  λ_n(θ,φ) = (1/|Λ|) Σ_{λ∈Λ} | ¼ Σ_σ G_n(σ∘(θ,φ) + λ) |.          (R)

Endpoint weights are absorbed by the torus symmetrisation. To be written out and proved as a lemma; part 2's record 70 and PD-T101 contain the corner and edge cases.

- At a corner the four reflected copies coincide. This is the A1 formula.
- On an edge they coincide in pairs.
- In the interior they are distinct.

## 2. The majorant, and why it is not enough by itself

The triangle inequality gives λ_n ≤ S(t) := (1/|Λ|) Σ_λ |G_n(t+λ)|. S is a shifted lattice sum of one fixed kernel, Λ-periodic, and equal to λ_n at the corners.

Measured findings (float64; [observations record](theory/argmax-alln-claude-01-measured-observations.md)):
- The maximum of S over a fundamental cell is **not** at the coset point. It sits about 0.01·π/n off it and exceeds Λ_c(n) by 1.4e-3 at n = 3, 2.3e-4 at n = 20 and 9.2e-5 at n = 40. So "S is maximal at the coset" is false as stated (IDEA?argmax-alln-claude-01).
- S is about Λ_c at **every** coset point (j+k odd), including the interior anti-nodes, where λ_n is much smaller.
- So S is useful away from coset neighbourhoods, and as the discard test in a branch-and-bound. It cannot by itself control corner or anti-node neighbourhoods.

## 3. All gaps are O(1)

Measured:
- Corner minus the maximum of λ_n over the central box [π/4, 3π/4]²: 1.79, 1.87, 1.84, 1.79, 1.75, 1.75 at n = 8, 12, 16, 24, 32, 48.
- Corner minus the edge runner-up: about 0.548 + 0.84/n (PD-T099 record, MEASURED). Part 2's records 72–73 give the limiting edge gap analytically.

Consequences:
- No region is separated from the corner at the log²n or log n level, so every region ties with it to two orders.
- An all-n proof therefore needs either uniform O(1)-sharp asymptotics with small explicit remainders, or an exact comparison inequality.
- The current A2 constants (54, 68) are about two orders of magnitude too crude to be used directly.

## 4. Proposed architecture (IDEA?argmax-alln-claude-02)

**(A) Scaled local-profile theorem.** For x in each regime (corner zone, edge zone at distance k·π/n, deep interior), with ξ the position in its lattice cell in units of π/n:

  λ_n(x) = (4/π²)log²n + b log n + Φ_regime(ξ) + E_n,  |E_n| ≤ C log n / n,

with C explicit and small.
- Φ_int involves four non-coinciding reflected copies.
- Φ_edge involves two copies. Part 2's records 70, 72 and 73 are its first instances.
- Φ_c is the corner profile.

Tools: an Euler–Maclaurin-type expansion of shifted lattice sums of the U-product kernel in rhombus coordinates, with the A2 product comparison (part 2 record 04) as template, redone with sharp constants.

**(B) n-independent certificates.** On one fixed cell, prove by interval arithmetic:
- sup Φ_int ≤ Φ_c − δ_int (measured about 1.7);
- sup Φ_edge ≤ Φ_c − δ_edge (about 0.5);
- Φ_c has a strict local maximum at 0.

**(C) Transition zones.** For edge zones at distance kπ/n with Φ_k → Φ_int as k → ∞: treat k ≤ k₀ explicitly and k > k₀ by a tail bound.

**(D) Finite n < n₀: a global-max-only certifier.**
- Use exact or outward-rounded evaluation, with S as the cheap discard bound away from coset points and λ_n itself near anti-nodes and corners.
- This is much cheaper than A5's full count; the target is n up to a few dozen.
- The explicit C in (A) must make n₀ this small. That is the main quantitative risk.

## 5. Cheaper routes to test first

1. **Profile convergence (decisive).** Compute R_n(ξ) = λ_n − (4/π²)log²n − b log n at fixed scaled points (interior anti-nodes and cell centres, edge midpoints, corner) for n up to about 200. Determine the rate and any parity oscillation; the interior gaps above are not monotone in n.
   - Kill criterion for (A)–(D), written before running: if the rate is no better than (log n)/n with a fitted constant making n₀ > 200, or if R_n(ξ) does not converge at fixed ξ, record the failure and switch to route 2.
2. **Brutman-type monotonicity (IDEA?argmax-alln-claude-03).** Do the cell-wise local maxima decrease monotonically along rhombus directions away from the non-node corners?
   - Test on part 2's certified lists (n ≤ 7) and on float64 data up to n ≈ 50.
   - If it holds, look for a pairing comparison between λ_n(t) and λ_n(t + coset step toward the corner) in (R). That would be an exact all-n argument with no asymptotics.
3. **Generating-curve factorisation (IDEA?argmax-alln-claude-04).** In rhombus coordinates S = (u+v)/2, T = (v−u)/2 the lattice step is ((2n+1)τ/2, −τ/2), τ = π/(n(n+1)).
   - By product-to-sum, the numerator sin((n+1)S)sin((n+1)T) then splits into a term that does not depend on the lattice point (through cos((n+1)(S₀+T₀))) and an oscillating term.
   - This is the 2D analogue of the 1D common-factor trick behind midpoint maximality for trigonometric interpolation.
   - It may give an "envelope × convex sum" form on cells. One bounded attempt; unverified.
4. **Literature first.** Read the 1D analogues: midpoint maximality of the trigonometric-interpolation Lebesgue function; Brutman 1978 and Günttner on Chebyshev nodes; Brutman's 1997 survey on where Lebesgue-function maxima lie; Kolomoitsev–Lomako's discretisation lemma. Record them as LIT records before relying on any transferred technique.

## 6. Scope remarks

- A5's maxima counts remain finite-n statements. Any all-n count statement (for example #maxima ~ c n²) would be a separate, measured-only conjecture.
- This note claims no PROVED result. The only status-bearing content is the MEASURED observations record.

## 7. Intended execution (to be revised after part 2)

1. Wait for part 2 to finish A4(a), B3 and B1, and for its Claude audit.
2. Update this plan from part 2's final A4(a) records: which edge and central-envelope pieces are proved, and their constants.
3. Run route-1 and route-2 tests as a part 3 Codex topic, with the kill criteria above pre-registered.
4. Commit to (A)–(D) only if the profiles converge at about rate 1/n. Otherwise pivot to the monotonicity/pairing route.
