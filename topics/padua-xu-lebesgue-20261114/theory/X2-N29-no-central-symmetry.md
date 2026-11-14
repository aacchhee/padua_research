# PD-N?padua-xu-lebesgue-20261114-claude-29 — the Morrow–Patterson Lebesgue function is not centrally symmetric and its maximum is not attained at the lower vertices (negative answer to BBDM §7.1)

ID kind: PD-N.
Aliases: X2-N29; novelty-gate candidate X2-C2; target T4(a) of round X2-2; C-MP corner check (gates addendum 2026-11-14).
Split from: none.
Split into: none.

## Statement

For every even n ≥ 2, for the Morrow–Patterson points MP_n as defined in BBDM (Constr. Approx. 63 (2026) pp. 31–32; `literature-xu-mp.md` §2) and interpolation in Π_n:

(i) λ_n(1, 1) ≠ λ_n(−1, −1); precisely λ_n(1,1) = λ_n(−1,1) > n + 1 = λ_n(−1,−1) = λ_n(1,−1). Hence the identity "λ_n(x, y) = λ_n(−x, −y) for all (x, y) ∈ [−1,1]²" is **false** for every even n ≥ 2 (it already fails at (x, y) = (1, 1)).

(ii) Λ_n = max_{[−1,1]²} λ_n ≥ λ_n(1,1) > λ_n(±1, −1). Hence the statement "the Lebesgue constant is attained at each corner of the square" is **false** for every even n ≥ 2: it is not attained at (1, −1) or (−1, −1).

Quantitatively the defect is of order n²: λ_n(1,1) − λ_n(−1,−1) = c*(n+5/2)² − 2(n+1) + O(log² n) (X2-25), while λ_n(−1,−1) = n + 1.

Both statements were posed as open problems to be *proved* in BBDM §7.1 (p. 64), on the basis of numerical observation.

## Definitions

As in X2-21. λ_n is the Lebesgue function Σ|ℓ_{p,q}|; the vertex set is {(±1, ±1)}.

## Assumptions

n even, n ≥ 2. The node set is exactly BBDM's (ordinates cos(2kπ/(n+3)) in the columns m odd, cos((2k−1)π/(n+3)) in the columns m even). For the reflected set −MP_n (BBDM Remark 1, p. 34) the roles of the upper and lower vertices are exchanged; the negative statements hold for it verbatim.

## Status by part

Overall status: PROVED (the negative statements (i), (ii), for every even n ≥ 2).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (i) λ_n(1,1) ≠ λ_n(−1,−1), all even n ≥ 2 | PROVED | X2-22 + X2-24 |
| (ii) Λ_n not attained at (±1,−1), all even n ≥ 2 | PROVED | X2-22 + X2-24 |
| independent certified confirmation, even n ≤ 30 | computer-assisted verification record (adds no claim) | `evidence/mp-cmp-certificate.json` (path A), `evidence/mp-cmp-check.json` |

Candidate / claim disposition: REJECTED (the two published conjectural statements).
Rejection reason: refuted — the negation is established for every even n ≥ 2.

## Negative-result scope (PD-N only)

Attempted mechanism: the two conjectural statements of BBDM §7.1 — (1) central symmetry λ(x,y) = λ(−x,−y) of the MP Lebesgue function; (2) attainment of Λ_n at each of the four vertices.
Parameter range: every even n ≥ 2, MP_n as in BBDM, interpolation space Π_n.

What is *not* refuted: the symmetry λ_n(x, y) = λ_n(−x, y) (BBDM Lemma 1; true, re-derived at the vertices in X2-21 part 4); attainment of Λ_n at the two upper vertices (±1, 1) (open, supported by the G1-MP screen for n ≤ 60; X2-28).

## Depends on

- X2-22 (λ_n(±1,−1) = n+1), X2-24 (λ_n(±1,1) > n+1), both PROVED; X2-25 for the quantitative remark only.

## Checks

- Path-A certificate (orchestrator; python-flint ball arithmetic on a Vandermonde solve, independent of the closed forms): for every even n ≤ 30 the enclosures of λ_n(1,1) and λ_n(1,−1) are disjoint (`claim_lam(1,1)_ne_lam(1,-1): true`), e.g. n = 2: 5.8455592331681269… versus 3.
- `python3 code/mp/research/x2_corner_arb.py --nmax 60`: `gt_n+1: true` for every even n ≤ 60 (closed form, ball arithmetic).
- `python3 code/mp/research/x2_corner_checks.py ident`: λ_n(±1,−1) − (n+1) = O(1e−38), λ_n(−1,1) − λ_n(1,1) = O(1e−37) (40 digits).
- Independent rerun: pending (auditor).

## Sources

- LITERATURE: BBDM, Constr. Approx. 63 (2026), §7 p. 63 (numerical statement that the constant is attained at each corner), §7.1 p. 64 (the two open problems), Remark 1 p. 34 (−MP_n is a different set), Lemma 1 p. 45 (x-symmetry). Read by the literature subagent from the published PDF (`lit-notes/X2-sources.md` §1); flags F1, F2 there discuss a possible source of the discrepancy in the authors' code (not verified).

## Proof or evidence

By X2-22, λ_n(1,−1) = λ_n(−1,−1) = n + 1. By X2-24, λ_n(1,1) = λ_n(−1,1) > n + 1. So λ_n(1,1) ≠ λ_n(−1,−1), which contradicts central symmetry at the point (1,1), and Λ_n ≥ λ_n(1,1) > λ_n(±1,−1). ∎

Remark (structural reason). MP_n is invariant under x ↦ −x but not under y ↦ −y: the ordinate sets of the odd and even columns, {cos(2kπ/(n+3))} and {cos((2k−1)π/(n+3))}, are exchanged by y ↦ −y. At (±1, 1) the reflected node lattice has the parity class "p + q odd" of X2-21 (kernel ∼ (x−y)⁻³), at (±1, −1) the class "p + q even" (kernel ∼ (x+y)⁻²), and the two kernels differ by a factor of order n.

## Scope

The two negative statements above, for every even n ≥ 2 and the stated node set. No statement about interior points beyond the failure of the global identity, and no statement about where Λ_n is attained.

## Open items

- Location of the maximum (X2-28).
- Independent rerun (auditor).

## History

- 2026-11-14, Claude Fable 5.2 (xhigh), researcher subagent of round X2-2; uncommitted at writing. First version. The readers' numerical observation of the asymmetry is in `lit-notes/X2-sources.md` §6.2 (flag F1); the certified C-MP check is the orchestrator's.
