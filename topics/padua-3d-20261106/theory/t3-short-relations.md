# PD-T?padua-3d-20261106-codex-T3-02 — Short compatible relations obstruct injectivity

ID kind: PD-T (reclassified 2026-11-06, audit M5).
Aliases: cosine-addition annihilator; three-coordinate Chebyshev surface;
short dual-vector degree barrier.
Split from: none. Split into: none.

## Statement

Fix d=3, n>=0, M>=1, z in Z^3, phi in R^3 and the full cyclic cosine
image X defined in PD-T?padua-3d-20261106-codex-T3-01. Suppose a nonzero u in Z^3
satisfies

    u dot z = 0 (mod M),   u dot phi = delta*pi (mod 2*pi),

where delta is an integer. Write a_j=|u_j| on its nonzero support S,
s=(-1)^delta, and define

    q(u)=a_i                              if S={i},
    q(u)=max(a_i,a_j)                     if S={i,j},
    q(u)=max(2a_1,2a_2,2a_3,a_1+a_2+a_3) if S={1,2,3}.

If q(u)<=n, evaluation Pi_n -> R^X is not injective. The conclusion holds
for every M,z,phi,u satisfying these hypotheses, not only small degrees.
It does not require coordinate-reflection invariance of the coset.

In particular for a fixed positive integer generator triple z independent
of n at zero phase, every sample on that cosine curve is noninjective for
n>=min_(i<j) max(z_i/gcd(z_i,z_j),z_j/gcd(z_i,z_j)). This is a standard
pairwise implicit-curve degree barrier, not a statement about generators
growing with n.

## Definitions and assumptions

Chebyshev T_a and the cyclic nodes have the conventions of the linked
rank record. All polynomials and ranks are over R in exact arithmetic.
A prescribed node subset of the same coset inherits the annihilator.
The phase condition is an explicit hypothesis; without it the particular
polynomials below are not asserted to vanish. No signed-frequency
collision test is substituted for it.

## Status by part

Overall status: **PROVED** by the explicit analytic annihilators below.

| Mathematical part | Status | Evidence / limits |
|---|---|---|
| Noninjectivity with one-, two- or three-coordinate compatible relation | PROVED | Nonzero polynomial of degree exactly q(u) |
| Fixed-frequency corollary | PROVED | Explicit two-coordinate relation |

Candidate disposition: the certificate mechanism is retained as a known
prerequisite. The class satisfying q(u)<=n cannot supply injective Pi_n
sets; no universal cyclic or growing-generator family is rejected.

## Scope of the obstruction tool (corrected 2026-11-06, audit M5)

This is a retained prerequisite theorem, not a failed-mechanism record.
IDEA?padua-3d-20261106-codex-T3-02 proposed the annihilator tool itself, which succeeded;
no independently proposed construction is rejected here.
Parameter range: precisely all integer n,M,z,u and real phi satisfying
the stated congruence, phase and q(u)<=n conditions. A failed search for
u does not prove unisolvence or absence of another annihilator.
The result is an obstruction tool; T2 owns the actual failed-family IDs.

## Depends on

Elementary cosine addition and Chebyshev leading coefficients. The rank
record supplies notation only; this hand-polynomial proof does not need
an exact finite rank computation or an external theorem. Closest local
predecessor is IDEA-189's explicit grid annihilators; novelty is not claimed.

## Proof

For every node parameter k,

    sum_j u_j theta_j(k) = delta*pi (mod 2*pi).

On support one, P=T_(a_i)(x_i)-s vanishes. Its degree is a_i and it is
nonzero since a_i>=1.

On support two, the two signed angles add to delta*pi. Their cosines
are unaffected by either sign, so T_(a_i)(x_i)=s T_(a_j)(x_j).
Thus P=T_(a_i)(x_i)-s T_(a_j)(x_j) vanishes, is nonzero (the variables
are distinct), and has total degree max(a_i,a_j).

On support three, put A=u_1 theta_1, B=u_2 theta_2 and C=-u_3 theta_3.
Then cos C=s cos(A+B). Let U=T_(a_1)(x_1), V=T_(a_2)(x_2),
W=T_(a_3)(x_3). The cosine addition formula implies

    (cos(A+B)-UV)^2=(1-U^2)(1-V^2).

Substitute cos(A+B)=sW and expand. The polynomial

    P=U^2+V^2+W^2-2sUVW-1                         (1)

vanishes at every node. It is nonzero: its monomial with exponent vector
(a_1,a_2,a_3) has coefficient -2s times the three nonzero leading
coefficients; no squared single-variable term can cancel it. Its degree
is exactly q(u), since the three squared leading monomials and the
three-variable leading monomial are distinct. For q(u)<=n this nonzero
Pi_n polynomial proves noninjectivity.

For the fixed-frequency corollary choose u_i=z_j/g, u_j=-z_i/g,
u_l=0 and g=gcd(z_i,z_j); then u dot z=0 exactly and phi=0 gives s=1.
Choose the pair with smallest stated degree. This annihilator vanishes
on the continuous curve as well as every finite cyclic sample. It gives
no uniform degree bound when the generator triple changes with n. ∎

## Checks

The proof is analytic. `t3_checks.py` checks exact rational substitutions in the three-variable identity
and finite-field examples; this is a
sanity check, not a proof dependency. Receipt: `evidence/t3-checks.json`.
Independent analytic review/replay remains for the coordinator to arrange.
No exhaustive search of relations is claimed.

## Sources

No new external citation is used. Standard trigonometric/Chebyshev
implicitization mechanism; existing literature limits in
[literature-T3](../literature-T3.md). No publication-priority claim.

## Scope and open items

The theorem covers a natural, explicitly tested condition on a general
cyclic coset, including non-reflection-invariant ones. It supplies no
all-large-n obstruction to T2's n-dependent generators, no proof that
its q(u) is the minimum vanishing degree, and no bound on Lebesgue
constants. The all-degree total-degree polylog target stays OPEN.

## History

2026-11-06, Codex T3, assigned model `gpt-6.1-sol` xhigh (resolved runtime metadata not
exposed), rules ccd9e905. Gate and IDEA record preceded derivation. T1
confirmed separation from its reflection-invariant subgroup classification.

## Supplementary check addendum — 2026-11-06

[Distinct Astra high check](../independent-checks-computation.md) completed
within its stated scope, including actual separate execution. Earlier
pending-check wording records the development state. Required Claude
substantive audit remains due; this addendum changes no mathematical claim.


## ID-kind response addendum — 2026-11-06 — M5

Old provisional ID `PD-N?padua-3d-20261106-codex-T3-01` maps to
**PD-T?padua-3d-20261106-codex-T3-02**, the same theorem in this same file.
The old label is retained only as provenance, not a second result. The
statement, proof, assumptions and PROVED status are unchanged. The original
post hoc attempted-mechanism wording was removed above because no genuine
failed candidate supported a PD-N allocation. This mapping is to be carried
into ID_CROSSWALK at PR preparation; no final ID is allocated here.


## Completed-audit process addendum — 2026-11-06 — m5

[Claude audit-01](../audit-01.md) completed the substantive independent audit
of candidate f1a5b0936d8fb2b033c69af59a6366550f170999, including the recorded
independent executions, after the supplementary Astra checks. Its accepted
mathematical scopes supersede earlier “audit/replay/rerun pending” and
“planned, no run claimed” process descriptions where those refer to that
completed work. This addendum changes no mathematical statement or status;
MEASURED observations remain MEASURED and OPEN targets remain OPEN. The
response dispositions, ID-kind mappings and evidence changes were covered
by [Claude audit-02](../audit-02.md); its accepted mathematical scope is
recorded there. This dated correction changes no statement or status.
