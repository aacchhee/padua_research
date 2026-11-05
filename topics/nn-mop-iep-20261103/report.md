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

This compares products at different sites. Exact examples also have nonzero
same-site transfer commutators, which refute only a literal identification
of these matrices with a commuting pair. PD-T057's blockwise interior
commuting conditions also couple adjacent degree levels; the shifted/fixed-site
contrast does not itself distinguish the theories. [Matrices and scope](exact-runs.md).
The decisive difference is spectral. Define the natural NN lattice operators
H_j f(nu)=f(nu+e_j)+b_(nu,j)f(nu)+sum_s a_(nu,s)f(nu-e_s).
On the MOP state both satisfy H_j P(x)=x P(x), with the same eigenvalue x;
H_1-H_2 annihilates consistent states. Bivariate multiplication has two
coordinate functions and joint values (x_l,y_l) on the full node space.
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

For common finite support, marginal-data reconstruction is complete on the
normal coefficient triangle |nu|<=N-1 without a terminal modification.
Producing coefficient layer K+1 uses d=b2-b1 from layers K-1 for lower
coefficients and K for diagonals. Thus every divisor used has degree <=N-2
and is nonzero by normality through degree N. This is the
[interior divisor lemma](theory/interior-divisor-nonvanishing.md) and
[finite reconstruction proof](theory/marginal-reconstruction.md), checked
against the [primary formulas](source-recheck-01.md).
All normal degree-N polynomials equal the common node polynomial, so d=0
on coefficient layer N-1 is a necessary final boundary condition. C4 does
not divide by those values. The former negative-result classification is
[withdrawn with its original wording preserved](theory/terminal-division-obstruction.md).

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
gap in the two original elementary proofs and identified one comment error,
corrected with a new hash and rerun. Claude [audit-01](audit-01.md) accepted
their mathematics but identified the erroneous significance attached to the
terminal equality. [Response-01](response-01.md) corrects it and addresses
all findings. Claude [audit-02](audit-02.md) accepts the response;
preparation now assigns final IDs without changing mathematical content.

[All four prescribed candidates](candidates.md) are retained: C1 is the
standard formulation; C2's literal fixed-site dictionary is refuted within
the finite scope; C3 is deferred because no distinct algorithm and preserved
invariant have been specified; C4 is retained as a known algebraic baseline
which is well defined on the entire stated normal triangle.

Apply the handoff's early gate stop to new method development. There is no
surviving new C3 implementation to compare against C4. C4 alone is an
executable numerical baseline, as audit F3 observed; its local pilot and
remaining runs are recorded separately in [c4-baseline-01.md](c4-baseline-01.md).
The bounded pilot uses monic Stieltjes marginals and A/B recursion in
binary64, checked against 140/220-digit references on N=4,8,12,16,24,32.
The maximum fieldwise normwise coefficient error exceeds one at N24/32
for Kravchuk and N16/24/32 for Hahn. Reference precision convergence is
checked; an exact independent moment formulation is used at N4 only. These
are MEASURED finite observations, not a proof of instability or an error-source
decomposition. No C3/C4 cost or stability equivalence is claimed. The source papers'
Kravchuk/Hahn accuracy reports remain attributed literature with their own
metrics; they are not reproduced by merely measuring local coefficient errors.
This stop does not settle whether a better numerical NN updater exists.

## Possible Leuven question and next step

No contact was made. A useful later question would specify a boundary-aware
coupled NN update, the normal region it preserves, normalization and residual
or backward-error metric, and the corrected FHV baseline. Then test whether
maintaining both directions improves accuracy or cost over repeated known
reconstruction on identical input families. The zero-curvature interpretation
is established background; an algorithmic advantage needs separate evidence.

[PR22](https://github.com/aacchhee/padua_research/pull/22) has completed
audited registration against main21dbfc90257b952d8923f6d01739d12aa8d6e0a1.
The topic ledger and [final map](preparation/final-id-map.json) assign
PD-T286–290, PD-N100, IDEA376–379 and LIT562–568, with same-source
reading addenda reusing existing IDs. The former provisional negative has
no final ID. Claude audit-02 accepted the science; approved E1/E2/X1 edits
are applied. The remaining step is a short Claude preparation protocol check.
The exact study is complete; stable coupled updating remains deferred,
with no further mathematical campaign assigned and only AC deciding merge.
