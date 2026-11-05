# PD-T288 — nonzero NN differences on a normal interior square

Final ID: **PD-T288**. Provisional alias: `PD-T?nn-mop-iep-codex-03`.

ID kind: PD-T.
Aliases: interior divisor; opposite-corner normality; successor difference.
Split from: the interior assertion of PD-N?nn-mop-iep-codex-01,
[terminal-division-obstruction.md](terminal-division-obstruction.md).
Split into: none.

## Statement

Use the moment-matrix convention of
[PD-T?nn-mop-iep-codex-01](finite-moment-formulation.md). Let N be the
number of distinct common support points, and let nu=(n,m) satisfy
|nu|<=N-2. Suppose the four indices

    nu, nu+e_1, nu+e_2, nu+e_1+e_2

are normal. Write t_eta for the coefficient of x^(|eta|-1) in the monic
polynomial P_eta, with t_0=0, and define

    b_(nu,j)=t_nu-t_(nu+e_j),   d_nu=b_(nu,2)-b_(nu,1).

Then

    P_(nu+e_1)-P_(nu+e_2)=d_nu P_nu,   d_nu != 0.

In particular, normality of every index through degree N implies
d_nu != 0 for every |nu|<=N-2, including indices on the axes.
For N=1 this interior set is empty.

## Definitions and assumptions

Two functionals L_j(f)=sum_l w_(j,l)f(x_l) on real polynomials, with
distinct real x_l and w_(j,l)>0. A multi-index eta is normal when its
square mixed moment matrix M_eta is invertible. The homogeneous
orthogonality conditions at eta are
L_j(x^i q)=0 for 0<=i<eta_j. The empty matrix has determinant one.
Arithmetic is exact. Four local normality assumptions suffice; positivity
alone is not being used as a replacement for them.

## Status by part

Overall status: PROVED. Claude audit-02 accepted; preparation protocol check pending.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Successor difference and nonvanishing on the stated normal square | PROVED | Written kernel argument below |

Candidate / claim disposition: none. This is known exact MOP algebra,
split into a positive record because marginal reconstruction depends on it.
No novelty or new candidate is asserted.

## Depends on

PD-T?nn-mop-iep-codex-01: normality, monic polynomials and the
subleading-coefficient convention. Elementary linear algebra. The proof
does not assume a published theorem or a computational result.

## Proof

Put s=|nu|. Inside polynomials of degree at most s, the s homogeneous
orthogonality conditions at nu have rank s: their restriction to degree
at most s-1 is the invertible matrix M_nu. Their kernel therefore has
dimension one and is spanned by the monic polynomial P_nu. This also
holds for s=0, when the kernel consists of constants.

The difference Q=P_(nu+e_1)-P_(nu+e_2) has degree at most s, because
its two terms are monic of degree s+1. Both terms satisfy all conditions
at nu. Consequently Q=c P_nu. Comparison of coefficients of x^s gives

    c=t_(nu+e_1)-t_(nu+e_2)=b_(nu,2)-b_(nu,1)=d_nu.

Thus the successor-difference identity follows from normality; it is not
an additional assumption.

If d_nu were zero, the two successors would coincide in a monic
polynomial R of degree s+1. For L_1, R satisfies the conditions with
0<=i<=n, inherited from P_(nu+e_1). For L_2, it satisfies those with
0<=i<=m, inherited from P_(nu+e_2). These are exactly all s+2
homogeneous conditions at nu+e_1+e_2. The nonzero coefficient vector
of R, in degrees 0,...,s+1, would then be a null vector of
M_(nu+e_1+e_2). This contradicts its normality and proves d_nu != 0.

## Checks

This is a written proof, not a computer proof. The earlier exact runs
and audit-01's layer-reconstruction checker are finite MEASURED support;
this response worker did not execute those checkers. Primary-source
locators were rechecked in [source-recheck-01.md](../source-recheck-01.md).

## Sources

LITERATURE: Van Assche 2011, arXiv:1104.3778v1, determinant identity
(2.12), printed p. 9; Kozhan–Vaktnäs, arXiv:2407.13946v2,
Lemma 2.18(b), printed p. 11. The latter states a stronger local
equivalence between nonzero diagonal difference and opposite-corner
normality. Only the direction proved above is claimed locally.
These locators refine the existing topic entries LIT?nn-mop-iep-codex-02
and -09; no final literature ID is assigned here.

## Scope and open items

This result certifies nonzero exact divisors, without a lower bound on
their magnitudes or a floating-point stability claim. It does not assert
normality of arbitrary positive inputs or nonvanishing at the last
coefficient layer |nu|=N-1. The latter has d_nu=0 under full triangular
normality; its role is a boundary condition in
[PD-T?nn-mop-iep-codex-04](marginal-reconstruction.md).
Claude audit-02 accepted; final IDs are assigned and the preparation protocol check remains pending.

## History

2026-11-05: Codex bounded mathematical developer; rules/head
`9ec2a54c5b6af56514feaf11c9fc329f19a88820`. Requested allocation:
gpt-6.1-sol xhigh; exact backend model/effort metadata is not exposed,
so no exact runtime attestation is claimed.

Original interior wording in PD-N?nn-mop-iep-codex-01:
"For |nu|<=N-2, if nu,nu+e_1,nu+e_2,nu+e_1+e_2 are normal and the
successor-difference identity holds, then d_nu !=0."
The positive statement is preserved, its redundant identity assumption is
proved, and its dependency role in PD-T?nn-mop-iep-codex-04 warrants this
substantive split. The historical record retains its earlier wording and
the correction of its former C4-failure interpretation.
