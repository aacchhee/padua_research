<a id="pd-tlanczos-nonproduct-codex-p2-02--disk-algorithm-covariance-and-the-fixed-order-limitation"></a>

# PD-T475 — disk algorithm covariance and the fixed-order limitation

Provisional alias: `PD-T?lanczos-nonproduct-codex-P2-02`.

ID kind: PD-T.
Aliases: radial symmetry transports the entire algorithm; coordinate swap mixes disk GS columns.
Split from: P2 continuous disk candidate; its capacity-rate target remains OPEN.
Split into: none.

## Statement

Let μ>-1, H=L²(ν_μ), and U_O f(z)=f(Oᵀz) for an orthogonal 2×2
matrix O. Fix a finite ordered polynomial Gram–Schmidt/parent algorithm
through degree s, including its parent choices, positive normalization
conventions and declared source columns. Transport **all** its inputs:
ordered seed polynomials, coordinate multipliers, parent labels and
additive H-valued sources. Then every computed column, exact or perturbed,
is the U_O image of its original counterpart, as long as both runs are
defined. Relative raw-product source scales and budgets are preserved.
Consequently the subspace distances, and their first-order normal
capacities when defined, are equal for these two transported algorithms.

This statement does not identify two named parent rules that use the
same original graded-lex order. In particular, for μ=0, coordinate
interchange mixes the first and third degree-two orthonormal GS columns
by a nontrivial orthogonal matrix, rather than permuting them.

## Definitions

The disk measure ν_μ and Π_s are defined in PD-T474. Ordered graded-lex
monomials here are 1,x,y,x²,xy,y²,…, within each degree increasing the
exponent of y. For the creator convention, an unnormalized raw product
is a_i b_parent, and its source scale is σ=||a_i b_parent||_H. Additive
sources f_h have squared relative budget Σ_h ||f_h||²/σ_h². Transported
multiplication uses a_i∘Oᵀ, and retains the original labels and parent
graph. It does not re-sort the transported seeds in the old coordinates.

## Assumptions

All choices, including ties, are fixed. The finite runs have nonzero
normalizing pivots. The source model is the arbitrary H-valued additive
model, with no coordinate-dependent restriction imposed on its sources.
The claim also applies to any restricted source class preserved by U_O,
but makes no claim for a class not preserved by that map.

## Status by part

Overall status: PROVED (analytic covariance statement).

| Mathematical part | Status | Evidence |
|---|---|---|
| Entire-algorithm orthogonal covariance | PROVED | Unitary intertwining proof below |
| Degree-two fixed-order swap mixing at μ=0 | PROVED | Exact moment calculation below |

Candidate disposition: retained structural result. The symmetry-only
identification of fixed-order BJ and mirror is abandoned as a proof
route. No inequality or equality between their full capacities is
refuted by this result.

## Depends on

PD-T474 supplies ν_μ and its moments. The definition of normal capacity is
the weighted monic model of PD-T482 and its continuous extension PD-T483 in
[p4-continuous-capacity.md](p4-continuous-capacity.md). The covariance
proof also applies directly to finite-epsilon subspace distance, without
using P4's formula for its derivative.

## Checks

The degree-two formulas agree with the exact finite reconstruction in
[p2-disk-probe.json](../evidence/p2-disk-probe.json), μ=0, degree8. The
written proof below is independent of that execution. Independent audit
is pending; no independent replay is claimed here.

## Sources

No external theorem is imported. This is an algorithm invariance lemma,
not a historical novelty claim for unitary invariance.

## Proof or evidence

The disk and its density are invariant under O, and an orthogonal change
of variables preserves area. Thus U_O is unitary. It takes Π_s onto Π_s
and satisfies

    U_O(a_i f) = (a_i∘Oᵀ) U_O f.

For arbitrary nonzero vectors v,w, unitarity gives

    U_O [v - <v,w>/<w,w> w]
      = U_O v - <U_O v,U_O w>/<U_O w,U_O w> U_O w.

It also preserves positive normalization, additions, and fixed scalar
multiples. Induction over every raw product, source addition and
projection in the algorithm proves covariance, for every fixed epsilon
where the run exists. The exact raw-product norm σ is unchanged, and
||U_O f_h||=||f_h||, so the source budget is unchanged. The correspondence
on source tuples is bijective.

For any finite-dimensional subspace V, its orthogonal projector obeys
P_(U_O V)=U_O P_V U_O*. Hence projector differences, principal angles and
graph normal derivatives have the same operator norm after transport.
Taking the source supremum proves the capacity assertion. This transports
the ordered seeds and the parent graph together; it supplies no relation
between algorithms obtained by changing only one of them.

For the stated fixed-order limitation, PD-T474's moments at μ=0 give the
monic degree-two GS polynomials and norms

    b20=x²-1/4,                    d20=1/16,
    b11=xy,                        d11=1/24,
    b02=y²+x²/3-1/3,              d02=1/18.

For example, ∫x²=1/4, ∫x⁴=1/8 and ∫x²y²=1/24. Subtracting the mean
and the projection onto b20 from y² gives b02, and its squared norm is
1/18. The other lower projections vanish by reflection. Thus

    q20=4x²-1,
    q11=√24 xy,
    q02=√18 (y²+x²/3-1/3).

Writing S(x,y)=(y,x), direct substitution yields

    U_S q20 = -(1/3)q20 + (2√2/3)q02,
    U_S q11 = q11,
    U_S q02 = (2√2/3)q20 + (1/3)q02.

Both coefficients in the first equality are nonzero. The transformation
is orthogonal, but is not a signed permutation of these fixed GS columns.
Accordingly, swapping the coordinates and then imposing the original
graded-lex seeds is not the transported ordered computation in the first
part of the statement.

## Scope

The lemma removes a proposed symmetry shortcut. It neither proves nor
disproves BJ=mirror, an exponential separation, or comparison with every
staircase ordering. A finite grid has this transport symmetry only for
orthogonal maps that preserve its measure: D36x9 has the declared D4
symmetries, not all O(2). It is not identified with the continuous disk.

## Open items

The fixed-order capacities, N2 finite-grid controls and N3 bounded-order
capacity closure remain separate. A sparse coordinate recurrence alone
does not establish a recurrence for the all-source normal operator norm.

## History

- 2026-11-05, Round2 after coordinator's pushed Round1 checkpoint
  `7e56471`: Codex P2 developer, assigned gpt-6.1-sol xhigh; runtime model
  metadata unexposed. Rules read at `cafb74ab6f7738c8af83d0cd0f518b81af16f253`.
