# Nearest-neighbour MOPs and the commuting-pair IEP

**Answer: exact reconstruction reduces to known MOP algebra. The usual NN
transfers form a lattice compatibility system, rather than the two finite
symmetric multiplication sections of PD-T057.** No new stable updater has
been obtained; the numerical question remains open here.

## Precise objects

The input is N distinct common real nodes and two positive weight vectors.
There is one polynomial variable x and two orthogonality functionals. The
multi-index (n,m) counts constraints against those functionals, rather than
the monomial x^n y^m of a two-variable positive moment functional. At each
normal index a square mixed moment system uniquely determines the monic
type-II polynomial. Full normality through degree N supplies the polynomial
triangle and both NN arrays through degree N-1.
[Elementary derivation](theory/finite-moment-formulation.md).
Positivity alone does not give mixed normality: proportional measures fail
already at (1,1).

For the standard three-component state the relation is

    L2(nu+e1;x) L1(nu;x) = L1(nu+e2;x) L2(nu;x).

This compares products at different sites. It does not assert commutation
of L1(nu;x), L2(nu;x) at one site. Exact examples exhibit shifted flatness
and nonzero fixed-site commutators. [Matrices and scope](exact-runs.md).
Covariant shifts on a suitable lattice state space can encode commuting
transport, but that known zero-curvature description still needs a state
space, boundary and gauge. It does not supply PD-T057's finite positive
two-variable moment model. The [gate](gate.md) gives the precise mismatch.

## Corrected exact baseline and boundary

FHV2015 gives known routes between NN, marginal and shifted step-line
recurrences. Two fixed shifted lines do not fill the lattice. One needs
recursively generated shifted lines and actual second-measure boundary
information, or the two marginal recurrence families, under the algorithm's
nonzero-divisor hypotheses. A single step-line loses some information about
the second measure. [Primary source coverage](literature.md).

For shared finite support all normal degree-N polynomials are the common
node polynomial F. At |nu|=N-1 both successors coincide and b2-b1=0.
A rule requiring division by this difference at every site therefore fails,
even on a normal finite triangle. Direct moment systems still give the
terminal polynomials and coefficients. The [boundary proof](theory/terminal-division-obstruction.md)
refutes only this unmodified division rule, not solvability or the published
theorem under its own nondegeneracy assumptions.

Kozhan–Vaktnäs also treat finite-support inverse/compatibility questions.
Their perfect finite-rectangle hypotheses are not silently substituted for
our normal common-support triangle: total rank here is at most N, so
perfectness through (N,N) is impossible. This prior work defeats a broad
claim that finite-support inverse theory is absent. It supplies no local
stability result. Precise reading limits are in literature.md.

## Evidence and stopping decision

All 14 deterministic rational cases (N=2,...,8, two weight families) pass
476 recurrences, 238 successor differences and 70 shifted flatness squares.
All 70 final-layer differences vanish; all 112 tested fixed-site commutators
are nonzero. All 84 terminal systems are normal and return F; all 98 tested
degree-(N+1) systems are singular. These are MEASURED finite observations,
not an all-N normality theorem or computer-assisted general proof.

A separate Astra agent reran the original checker and independently
implemented small determinant/coefficient calculations, including N=1 and
a different N=4 input. Its [receipt](independent-check.md) found no substantive
gap in the two elementary proofs and identified one comment error, corrected
with a new hash and rerun. The required Claude audit remains PENDING.

[All four prescribed candidates](candidates.md) are retained: C1 is the
standard formulation; C2's literal fixed-site dictionary is refuted within
the finite scope; C3 is deferred because no distinct algorithm and preserved
invariant have been specified; C4 is retained as a corrected known algebraic
baseline, with its naive terminal division scoped separately.

Apply the handoff's early gate stop to new method development. There is no
surviving new C3 implementation to compare against C4. No floating-point
comparison, digits-lost table, comparable-cost result or comparable-stability
claim was produced. The source papers' Kravchuk/Hahn accuracy reports remain
attributed literature, not local runs. This stop does not settle whether a
better numerical NN updater exists.

## Possible Leuven question and next step

No contact was made. A useful later question would specify a boundary-aware
coupled NN update, the normal region it preserves, normalization and residual
or backward-error metric, and the corrected FHV baseline. Then test whether
maintaining both directions improves accuracy or cost over repeated known
reconstruction on identical input families. The zero-curvature interpretation
is established background; an algorithmic advantage needs separate evidence.

Draft [PR22](https://github.com/aacchhee/padua_research/pull/22), rules/input
320fe07f5231ac7e72a4da45e64a38e5ff381b4a, base/main
440d1079e42c3ef21c40d1cf8870f5b206410c6a. Only topic files changed;
registries and final assignments await audited PR preparation. Next is
Claude Opus 5.5 xhigh audit of the scoped results and literature gate.
