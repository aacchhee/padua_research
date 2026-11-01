# All-degree Padua argmax (A4 / PD-T099) — proof plan, v2

Status: **planning note, WORK stage, no proof claimed.** This is v2, written 2026-11-01 by Claude (claude-opus-5-5) after PR #12 (part 2) merged as `2b52b43`. v1, from before part 2 finished, is preserved verbatim under History at the end. It supersedes v1 wherever they differ.

## 0. Target

PD-T099 (OPEN): for every n ≥ 2,

  max_{[−1,1]²} λ_n = Λ_c(n), attained only at the non-node corners.

Here λ_n = Σ_B |L_B| on the even-checkerboard Padua nodes of PD-T101.

## 1. What is now proved (main `2b52b43`)

| Area | Final IDs | Content |
|---|---|---|
| Corner value | PD-T101 | Exact corner formula, every n ≥ 1 |
| Corner asymptotics | PD-T156–159 | Λ_c = (4/π²)log²n + b log n + O(1), \|error\| ≤ 68 for n ≥ 2, b = (8/π²)(γ+log(8/π)); \|Λ_c − L_n²\| ≤ 54 |
| Finite argmax | PD-T162, 166, 169, 174, 177 | Global max only at the two non-node corners for n = 3, 4, 5, 6, 7 (certified counts in PD-T161/165/168/173/176) |
| n = 8 | PD-T183 PROVED; PD-T180/181/184 OPEN | At least 44 strict interior maxima; exact count and global max OPEN |
| Edges | PD-T185 | Exact Padua formula on all four edges (divided-difference limits) |
| Edge grid | PD-T186 | Corner minus value > 0 at every complementary vertical-edge ordinate, all n |
| Edge constant | PD-T187, PD-T188 | Central complementary sequence: C_n = Λ_c − g + o(1); g given by positive 1-D and alternating-series formulas; 0.548504986190 < g < 0.548525055355 |
| Edge mechanism | PD-T189–191 | Along a vertical edge, λ_n = S_n(s) − Δ_n(β,s) exactly (S_n is the edge majorant, Δ_n ≥ 0 the triangle defect, β the macroscopic ordinate, s the phase in units of π/(n+1)). S_n(s) ≤ cos²(s/2)Λ_c + C log(n+1) (phase localization), and near s = 0, S_n − Λ_c = O(log⁻² n). Δ_n(β_n, s_n) → g when β_n → π/2 and s_n → 0 |
| Central edge envelope | PD-T192 | R_cen(n) := max over x = ±1, \|t − π/2\| ≤ π/(n+1) of λ_n = Λ_c − g + o(1), both parities |

The edge mechanism PD-T189–191 is exactly the edge restriction of the reflected-lattice identity (R) and majorant S of §2. Two copies are involved on an edge; there are four in the interior. So part 2 has already carried out the IDEA?argmax-alln-claude-02 programme in one regime, the central vertical edge, with non-effective o(1) remainders.

## 2. Reformulation (unchanged from v1 §1–2)

λ_n(θ,φ) = |Λ|⁻¹ Σ_{λ∈Λ} | ¼ Σ_σ G_n(σ∘(θ,φ)+λ) |. Here Λ is the Padua torus lattice and G_n is the corrected Padua kernel. Writing S for the four-copy majorant and Δ := S − λ_n ≥ 0 for the four-copy triangle defect:

  λ_n = S − Δ  everywhere.

The edge identity PD-T191(2) is the case where the copies coincide in pairs. The majorant alone fails: max S exceeds Λ_c by ≤ 1.4e-3 off the coset point (MEASURED, IDEA?argmax-alln-claude-01). Every proof must use the defect.

## 3. Measured landscape (float64; PD-T?argmax-alln-claude-01 and -02)

- **Vertical edges x = ±1**: the corner gap Λ_c − (cell maximum) is smallest at the central cell, 0.639, 0.583, 0.567 and 0.557 at n = 12, 24, 48, 96. This agrees with g ≈ 0.5485 (PD-T192). The gap rises toward the corners: about 0.87 at 25 % of the edge and about 1.4–1.5 at 10 %. In the first cells next to the node corner it grows with n (1.9, 2.3, 2.7, 3.1 at n = 12, 24, 48, 96).
- **Horizontal edges y = ±1**: minimal gap at the centre, 0.954, 0.973, 0.986 and 0.993 at n = 12, 24, 48, 96, apparently tending to about 1.
- **Interior**: the gap on [π/4, 3π/4]² is about 1.75 for n = 8…48.
- **Strips** at distance 1–5 cells from an edge: their maxima lie on the strip's edge boundary. The near-edge interior is not a separate competitor at n = 24, 48.
- **n = 2**: the maximum found is 3 = Λ_c, only at the corners. The grid's near-corner points come close only by continuity. **No certificate exists for n = 2.**

Picture: the unique runner-up is the central vertical-edge envelope, with gap g ≈ 0.5485, as part 2 proved in the limit. Every other region is separated by more. Corner cells are the only places where the gap tends to 0, at the corner itself.

## 4. Remaining obligations for an all-n proof

A4 for all n ≥ 2 follows from P0–P6 together with the finite certificates above.

- **P0 (n = 2).** Certify the global maximum for n = 2 (exact; tiny case; not covered by part 2, which starts at n = 3).
- **P1 (whole vertical edge).** For every compact [δ, π−δ] of ordinates, sup λ_n ≤ Λ_c − inf_β g(β) + o(1), with g(β) ≥ g.
  - Route: generalize PD-T191 to Δ_n(β_n, s_n) → g(β) for every β ∈ (0, π), uniformly on compacts. Prove inf g(β) = g(π/2) = g, or at least inf > 0.
  - Reuse PD-T189/190 for the phase, which is β-independent.
- **P2 (horizontal edges).** The analogue of P1 on y = ±1, with the roles of n and n+1 exchanged. Measured gap is about 1.
- **P3 (corner neighbourhoods).** On a fixed δ-neighbourhood of each corner, λ_n ≤ Λ_c with equality only at the non-node corner, for n ≥ n₀.
  - This needs a two-free-angle phase estimate (part 2 route note (b)), and a local comparison of how S rises and how Δ grows near the coset point. Both are probably cusp-linear, not quadratic, because absolute-value sums have kinks.
  - Near-corner edge zones (β ≤ δ) are included here. Their measured gap grows like log n away from the corner cell.
- **P4 (interior).** On the square minus δ-strips, sup λ_n ≤ Λ_c − g_int + o(1) with g_int > 0 (measured about 1.75).
  - Route: two-phase localization of S, generalizing PD-T189, together with stability and a positive limit of the four-copy defect, generalizing PD-T191, and uniformity in position.
- **P5 (strips).** Uniform control at distance between O(1/n) and δ from an edge, joining P1/P2 to P4. Measured: dominated by edge values.
- **P6 (effectivity and the finite range).** Every o(1) above must become an explicit bound with an explicit threshold n₀. Then certify the global maximum for 8 ≤ n < n₀. The n = 8 global maximum (PD-T181) is still OPEN.
  - Use a global-max-only certifier (IDEA?argmax-alln-claude-05), much cheaper than counting all maxima: the majorant S discards boxes away from coset points, exact or interval λ_n is used near them.
  - **This is the main risk.** Part 2's remainders are non-effective, and the A2 constants (54, 68) are far too crude against a gap of 0.5485.

## 5. Routes

- **Main route (IDEA-02, now a variant of IDEA-305).** P1–P5 by the S − Δ mechanism of PD-T189–191, extended from the central edge to all regimes, then P6.
- **Alternative routes, deferred and unchanged.** IDEA-03 (monotone decrease of cell maxima toward the corner, with a pairing comparison) and IDEA-04 (generating-curve factorization). The measured edge profile, smallest at the centre and rising toward the ends, is compatible with IDEA-03 along edges. A pairing argument along an edge that moves the competitor toward the centre would reduce P1 to PD-T192.
- **Literature.** The 1-D analogues listed in v1 §5.4 have still not been read. Read them before P3, where 1-D endpoint and midpoint arguments are most likely to transfer.

## 6. Decisive tests for part 3 (pre-registered here)

- **T1, edge profile.** Compute the cell-wise gap profile G_n(β) on all four edges for n up to 400 (edge evaluation is 1-D). Also compute the conjectured limit g(β) from a β-generalization of the PD-T188 series, and compare.
  - Kill P1's "inf = g at π/2" form if the minimizing β moves off the centre as n grows, or if G_n(β) falls below g − 0.01 anywhere for n ≥ 100. Then retain only "inf > 0" or reformulate.
- **T2, interior profile.** At macroscopic positions on a 9×9 lattice of the square and fixed cell phases, measure the cell-max gap for n ∈ {32, 64, 128}, and fit convergence.
  - Kill P4 in its "o(1) to a limit" form if the gaps do not stabilize: changes > 0.05 between n = 64 and 128 at a fixed position.
- **T3, corner zone.** Compute λ_n(corner + ξπ/n) − Λ_c on a box |ξ| ≤ 3 for n ∈ {16, 64, 256}.
  - Kill the n-independent local-profile form of P3 if the scaled profile does not converge, or if a second near-zero gap appears off ξ = 0.
- **T4, effectivity estimate.** Numerically estimate the constants in PD-T189/190 (sup_s (S_n(s) − cos²(s/2)Λ_c)/log(n+1), and the local excess), and the rate of R_cen(n) → Λ_c − g. Project an achievable explicit n₀.
  - Kill the asymptotic-plus-finite strategy if the projected n₀ exceeds 60. A global-max-only certifier is expected to reach a few dozen. In that case pivot to IDEA-03.
- **T5, n = 2.** P0 directly: exact or interval certificate.

## History

### v1 — 2026-11-01, commit `f44a606`, superseded by v2 above (verbatim; headings demoted so they nest under History)

### All-degree Padua argmax (A4 / PD-T099) — proof strategy

Status: **planning note, WORK stage, no proof claimed.** Written 2026-11-01 by Claude (claude-opus-5-5) at AC's request ("write this down on a new branch, then we'll update it after part2 is done"). It records the strategy proposed in chat, and the quick float64 checks it rests on. It is to be revised once `codex/padua-proof-attempts-2-20261101` (PR #12) finishes A4(a), B3 and B1 and is audited; see [handoff 01](handoffs/01-update-after-part2.md).

#### Target

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

#### 1. Exact reformulation as a reflected lattice sum

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

#### 2. The majorant, and why it is not enough by itself

The triangle inequality gives λ_n ≤ S(t) := (1/|Λ|) Σ_λ |G_n(t+λ)|. S is a shifted lattice sum of one fixed kernel, Λ-periodic, and equal to λ_n at the corners.

Measured findings (float64; [observations record](theory/argmax-alln-claude-01-measured-observations.md)):
- The maximum of S over a fundamental cell is **not** at the coset point. It sits about 0.01·π/n off it and exceeds Λ_c(n) by 1.4e-3 at n = 3, 2.3e-4 at n = 20 and 9.2e-5 at n = 40. So "S is maximal at the coset" is false as stated (IDEA?argmax-alln-claude-01).
- S is about Λ_c at **every** coset point (j+k odd), including the interior anti-nodes, where λ_n is much smaller.
- So S is useful away from coset neighbourhoods, and as the discard test in a branch-and-bound. It cannot by itself control corner or anti-node neighbourhoods.

#### 3. All gaps are O(1)

Measured:
- Corner minus the maximum of λ_n over the central box [π/4, 3π/4]²: 1.79, 1.87, 1.84, 1.79, 1.75, 1.75 at n = 8, 12, 16, 24, 32, 48.
- Corner minus the edge runner-up: about 0.548 + 0.84/n (PD-T099 record, MEASURED). Part 2's records 72–73 give the limiting edge gap analytically.

Consequences:
- No region is separated from the corner at the log²n or log n level, so every region ties with it to two orders.
- An all-n proof therefore needs either uniform O(1)-sharp asymptotics with small explicit remainders, or an exact comparison inequality.
- The current A2 constants (54, 68) are about two orders of magnitude too crude to be used directly.

#### 4. Proposed architecture (IDEA?argmax-alln-claude-02)

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

#### 5. Cheaper routes to test first

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

#### 6. Scope remarks

- A5's maxima counts remain finite-n statements. Any all-n count statement (for example #maxima ~ c n²) would be a separate, measured-only conjecture.
- This note claims no PROVED result. The only status-bearing content is the MEASURED observations record.

#### 7. Intended execution (to be revised after part 2)

1. Wait for part 2 to finish A4(a), B3 and B1, and for its Claude audit.
2. Update this plan from part 2's final A4(a) records: which edge and central-envelope pieces are proved, and their constants.
3. Run route-1 and route-2 tests as a part 3 Codex topic, with the kill criteria above pre-registered.
4. Commit to (A)–(D) only if the profiles converge at about rate 1/n. Otherwise pivot to the monotonicity/pairing route.
