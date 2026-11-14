# PD-T?padua-xu-lebesgue-20261114-claude-26 — Λ_n ≥ λ_n(±1,1) > c* n² for every even n ≥ 2 (explicit, vertex-sharp lower bound for Morrow–Patterson points)

ID kind: PD-T.
Aliases: X2-26; explicit MP lower bound; target T4(b) of round X2-2; gate G4 with an explicit constant.
Split from: none.
Split into: none.

## Statement

Let c* = 0.51695365336… be the constant of X2-25 and Λ_n := max_{[−1,1]²} λ_n the Lebesgue constant of the Morrow–Patterson points MP_n (n even, interpolation in Π_n). Then for **every even n ≥ 2**

Λ_n ≥ λ_n(1,1) = λ_n(−1,1) > c* n² > 0.51695 n² > n²/2,

and more precisely Λ_n ≥ λ_n(1,1) ≥ c*(n+5/2)² − (n+1) − (0.4053 log²(n+2) + 2.9833 log(n+2) + 15.82).

The constant c* cannot be improved *for the vertex value*: sup{c : λ_n(1,1) ≥ c n² for all even n ≥ 2} = c* = lim λ_n(1,1)/n² (X2-25). Whether lim Λ_n/n² = c* is open (X2-28).

This is a **strengthening of a published result, not a new theorem type**: Beberok (JAT 311 (2025) 106191, Thm 0.1) proved Λ_n ≥ c n² with an existential c, by a lower estimate of λ_n(1,1); the constant readable from his final display is about 7.5·10⁻⁴ (n ≥ 8; `literature-xu-mp.md` §3.1). Here the same point gives the explicit constant c* ≈ 0.51695 for all even n ≥ 2.

## Definitions

As in X2-21, X2-25.

## Assumptions

n even, n ≥ 2.

## Status by part

Overall status: PROVED (analytic for n ≥ 18; computer-assisted by rigorous ball arithmetic for n ≤ 16; independent rerun of the finite part pending).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Second displayed inequality, all even n ≥ 2 | PROVED | X2-25 (lower bound) |
| λ_n(1,1) > c* n² for even n ≥ 18 | PROVED | X2-25 + elementary monotonicity below, with c* ≥ 0.51695 from the certified enclosure |
| λ_n(1,1) > c* n² for even n ≤ 16 | PROVED, computer-assisted | ball-arithmetic enclosures of the closed form X2-23 (a) and of c*; `x2_corner_arb.py`; also consistent with the independent path-A enclosures for n ≤ 30 |
| Optimality of c* for the vertex value | PROVED | X2-25 (limit) |

Candidate / claim disposition: none.

## Depends on

- X2-25 (two-sided estimate, enclosure of c*); X2-23 (a) (closed form evaluated in ball arithmetic); X2-21 part 4.

## Checks

- `python3 code/mp/research/x2_corner_arb.py --nmax 60` (python-flint 0.9.0, 256 bits; 2026-11-14): `cstar_ge_0.51695: true`, `cstar_le_0.51696: true`; `threshold_g(20)>0: true` (g(18) = −0.2419 < 0, so the analytic range starts at M = 20); flag `gt_cstar_n^2: true` for every even n ≤ 60, i.e. the ball of λ_n(1,1) − c*n² is positive (the ball of c* is the certified enclosure).
- Independent rerun: pending (auditor).

## Sources

- LITERATURE: Beberok, JAT 311 (2025) 106191, Thm 0.1 and final display (orchestrator's reading, `lit-notes/X2-sources.md` §1b); BBDM, Constr. Approx. 63 (2026) Thm 4 (upper bound O(n²)).

## Proof or evidence

Let M = n + 2, L = log M, ℓ(M) := 0.4053 L² + 2.9833 L + 15.82. By X2-25, λ_n(1,1) ≥ c*(M+½)² − (M−1) − ℓ(M). Since (M+½)² − (M−2)² = 5M − 15/4,

λ_n(1,1) − c* n² ≥ g_c(M) := (5c − 1)M − (15/4)c + 1 − ℓ(M) at c = c*.

For M ≥ 1 the map c ↦ (5M − 15/4)c is increasing, and c* ≥ 0.51695 (certified enclosure, X2-25), so g_{c*}(M) ≥ g(M) := g_{0.51695}(M). Now g'(M) = 1.58475 − (0.8106 L + 2.9833)/M, and (0.8106 log M + 2.9833)/M is decreasing for M ≥ 3; at M = 20 it equals 0.2706, so g' > 0 on [20, ∞). Ball arithmetic gives g(20) > 0 (g(20) ≈ 2.36). Hence λ_n(1,1) > c* n² for every even n ≥ 18.

For n ∈ {2, 4, …, 16} the inequality λ_n(1,1) > c* n² is verified by rigorous enclosures of both sides (closed form X2-23 (a) summed over all nodes; c* from the series of X2-25, Lemma C with its proved tail bound). For orientation: λ_n(1,1)/n² = 1.4614, 0.9276, 0.7785, 0.7092, 0.6692 for n = 2, …, 10.

Finally Λ_n ≥ λ_n(1,1) by definition, λ_n(−1,1) = λ_n(1,1) by X2-21 part 4, and c* > 0.51695 > ½. ∎

## Scope

A lower bound for Λ_n through the vertex value, for every even n ≥ 2. Together with BBDM's O(n²) upper bound (LITERATURE, no constant) it gives c* ≤ liminf Λ_n/n² ≤ limsup Λ_n/n² < ∞. It does not show that the vertices (±1, 1) maximise λ_n.

## Open items

- Is Λ_n = λ_n(±1,1) for every even n (then lim Λ_n/n² = c*)? See X2-28.
- Independent rerun of the finite range (auditor).

## History

- 2026-11-14, Claude Fable 5.2 (xhigh), researcher subagent of round X2-2; uncommitted at writing. First version.
