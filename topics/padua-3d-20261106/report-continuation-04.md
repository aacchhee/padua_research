# Handoff04 results — 2026-11-06

The continuation answers audit01 and explores the three newly authorized
directions. **A minimal-node 3-D family with a proved polylogarithmic
Lebesgue constant remains OPEN.** No historical novelty is claimed.
The original accepted T1–T6 mathematics is retained. Rules/input, worker
allocation, checkpoint history and deviations are recorded in [LOG](LOG.md).

## Audit response

[Response01](response-01.md) disposes all five MAJOR and fifteen MINOR
findings. Material changes are the predecessor comparisons, retained
candidate dispositions, permanent gate-timing qualifier, full-class D3
diagnostic and short-relation PD-N→PD-T mapping. The full n2..6 invariant
diagnostic has636/1392/757/2520/4803 target-count cases and zero necessary-
screen survivors. Exact normalized-generator symmetry counts are
18/100/301 classes from36/171/561 pairs. The lexicographic n4 cyclic
representative is(1,15,19); its apparent near tie was rounding.

The original T2 timing deviation and unexecuted T5 completion probe are
preserved for AC in [canonical deviations](response-deviations-01.md).
They are not retrospectively cured by these fixes. Historical source
coverage limits remain explicit; no final IDs or shared registries are changed.

## T7: general cosets and a rank-two survivor

- **PROVED:** the [general-H character dictionary](theory/t7-general-character.md)
  works for every finite subgroup and every real phase. The compatible
  [short-relation lemma](theory/t7-short-relation.md) extends the old cyclic
  argument, with its compatibility assumption retained.
- **PROVED:** [finite symbolic reduction](theory/t7-finite-reduction.md).
  The bound |H|<=8N makes subgroup enumeration finite. Phase collision
  strata have constant node count, but evaluation rank can vary within
  a stratum. Complete existence tests require symbolic minors; one generic
  phase or one rational grid is not exhaustive. The all-coset n2/n3 census
  was not run and remains OPEN.
- The [rank-two analysis](theory/t7-rank-two.md) refutes the inference that
  abstract group rank forces a sufficiently short compatible plane relation.
  The supplied [ten-point example](theory/t7-ten-point.md) is reproduced
  exactly, including its determinant and cubature boundary.
- An isolated [cubic survivor](theory/t7-rank-two-survivor.md) uses
  H=<(7,7,4)/10,(5,0,5)/10> and phase(1,2,4)/101. It has20 distinct nodes.
  Its exact finite rank certificate is separately corroborated on the
  actual cosine nodes modulo5051, using a primitive1010th root32.
  This is no degree-uniform family or Lebesgue upper bound.
- **PROVED:** the survivor's [quartic cubature obstruction](theory/t7-survivor-cubature.md).
  With U=T2(x), V=T2(y), delta=-4pi/101, the polynomial
  U²+V²-2cos(delta)UV-sin²(delta) vanishes on every node but has positive
  product-Chebyshev integral cos²(delta). No signed weights on this set
  are exact through degree4; the degree5 Padua cubature marker fails.

Stop: the finite-phase and rank-two exclusion shortcuts are refuted,
the fixed survivor's cubature route is obstructed, and the unsolved
symbolic census/uniform construction require the stated new premises.
No n4/n5 rescue or post hoc phase optimization was performed.

## T8: larger cyclic classes and their quality boundary

The [finite reduction](theory/t8-cyclic-reduction.md) includes every
zero-phase primitive cyclic subgroup with order<=8N, including even
orders and generators with no unit coordinate. **MEASURED exact finite
classifications:** n2 has95 minimal node sets from15733 generator classes;
n3 has300 from112314. The only cubic full-rank class is M38,z=(1,6,17).
The [n5/n6 odd-modulus slice](theory/t8-finite-screens.md) has one/five
full-rank sets. These are finite results, not a uniform construction.

All three fixed translated formulas have [written quadratic obstructions](theory/t8-phase-obstructions.md)
at n2. The stronger [order-ten theorem](theory/t8-phase-order-obstruction.md)
is **PROVED for every continuous phase**: if all10 nodes are distinct,
the half-period induces a free sign involution; nodal and Pi2 parity
dimensions disagree. Thus M=N cannot provide an every-n>=2 cyclic family.
Other moduli and degree sequences omitting n2 remain outside this theorem.

The [even-order trace gate](theory/t8-even-parity.md) motivates a prospectively
frozen odd-degree selector with M=2N-2 and the lexicographically first
full-rank generator. It selects by exact rank, never by measured quality.

| n | Selected generator | Mesh Lebesgue sample | Leja | QR |
|---:|---|---:|---:|---:|
|3|(1,6,17)|12.2314|13.1747|8.3207|
|5|(1,11,46)|123.7517|26.3366|13.8575|
|7|(1,19,44)|539.9463|49.8126|26.9351|
|9|(1,14,121)|831.0070|84.4580|44.1798|

All values are **MEASURED** on the same21³ mesh, below or equal to the
true continuous suprema. The [selector](theory/t8-even-family.md) hits its
registered two consecutive admissible Leja-loss stop at n7/n9. Degree11
was not run; growth fits are INCONCLUSIVE. No D2-promising family survives.
Unions, corrections, other phase strata and mod6 routes retain specific
resume conditions in [T8 attempts](attempts/T8.md).

## T9: improved universal lower bounds and the remaining gap

**PROVED** for every bounded real projection P onto total-degree Pi_n
in the cube, hence for every minimal-node interpolation operator:

    ||P|| >= 3/4 + 3/(2pi) > 1.2274, n>=1.

The [retained-kernel proof](theory/t9-averaged-projection-lower.md) avoids
the old norm27 correction. A [square-wave dual](theory/t9-squarewave-lower.md)
also proves, with O_m=sum_{a=0}^m1/(2a+1),

    ||P|| >= O_floor(n/2)^3/(3pi^3),
    liminf ||P_n||/(log n)^3 >= 1/(24pi^3).

The explicit leading coefficient improves27-fold over the earlier local
certificate. Sharpness and historical novelty are not asserted. The new
harmonic term first exceeds1 near n2420 by a MEASURED scalar evaluation;
the all-degree1.2274 bound is analytic and does not rely on that decimal.

The [unshifted Haar reduction](theory/t9-haar-packing-reduction.md) is
**PROVED**, including its2-D Padua consistency and phase-cancellation
boundary. The [n>=110 count obstruction](theory/t9-packing-conditional.md)
is **CONDITIONAL** on an unverified lattice-packing density bound<=18/19.
It excludes neither arbitrary phases nor non-Haar weights or coset unions.

[Refined maxima](theory/t9-measured-maxima.md) cover26 frozen cases:
QR/Leja n4..12, historical stack n4..7, the old cyclic n4 representative
and local determinant controls n2..4. Mesh41 plus local searches raises
some old samples by up to7.30%; none is a certified continuous maximum.
The finite power fits have lower residuals than the tested log powers;
no asymptotic conclusion follows. No killed stack family was continued.

[Lower-set transfer](theory/t9-lower-set-transfer.md) and
[projection correction](theory/t9-projection-extraction.md) are PROVED
implications, retaining the missing explicit prefix/inverse premises.
They supply no new explicit polynomial family. Classical global Fekete
existence gives Lambda<=N=O(n³); the minimal-node log³ versus n³ gap remains.
T9 stops after its bounded programme, with all five routes and resume
conditions preserved in [its attempt](attempts/T9.md).

## Verification and next step

Distinct Astra checks separately reconstruct the new mathematics and
actually rerun the consequential computation. Their precise scope and
input identities are in [the T7/T9 review](independent-checks-new-math.md)
and [the response/T8 review](independent-checks-response-t8.md).
[Sol xhigh development](mathematical-development-T8.md) separately reconstructs
the T8 analytic proofs, preserving the original worker's actual allocation.
The required
next step is a focused Claude re-audit of the PartA material changes and a
substantive Claude audit of T7–T9. No merge or readiness decision is requested.
