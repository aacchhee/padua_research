# PD-N?padua-3d-codex-T1-01 — no minimal total-degree set from a reflection-stable coset

ID kind: PD-N. Aliases: binary-coupling node excess; reflection-coset obstruction.
Split from: original T1 C_k target (preserved OPEN in t1-open-class.md).
Split into: none. This is a proved restricted-class result, not a weakening
of the original OPEN target's status.

## Statement

Let n>=2, H<=T^3 finite, and a in T^3. Assume the **whole coset**
A=a+H is invariant under negation of any single torus coordinate. Then
X=c(A) cannot simultaneously satisfy

    |X|=binom(n+3,3),  and evaluation Pi_n(R^3) -> R^X injective. (1)

Consequently it cannot give minimal-cardinality Pi_n interpolation by
discrete orthogonality, positive cubature, or the full Padua package.
The conclusion requires neither of these extra assumptions.

## Definitions

Pi_n denotes real polynomials of total degree at most n. Torus, cosine
map, canonical m_j, binary code B, affine parity code C, coupled Lobatto
denominators q_j=m_j/2, and counts e(q),o(q) follow the classification
PD-T?padua-3d-codex-T1-01. Injectivity is the necessary property; for
cardinality (1) it is equivalent to unisolvence.

## Assumptions

Finite single coset; full coordinate-reflection invariance of A; n>=2.
Since differences of points of A equal H, invariance of A implies
R_j H=H, so the classification applies. No restriction on subgroup order,
no fixed modulus, no prescribed axis offsets, no weights or exactness.

## Status by part

Overall status: **PROVED**, by the written proof below; independent audit pending.
Candidate disposition: T1-01's obstruction route is retained/successful.
The minimal-node construction mechanism within its stated class is
**REJECTED: failed**. The classification result has its separate PROVED
home. Unrestricted C_k remains OPEN.

## Negative-result scope

Attempted mechanism: IDEA?padua-3d-codex-T1-01, one reflection-stable coset.
Parameter range: every n>=2, every such finite coset in T^3. An arbitrary
cosine image is not sufficient to meet the reflection hypothesis.

## Depends on

PD-T?padua-3d-codex-T1-01. The coordinate annihilator behind PD-N032 is
reproved below. No external cubature bound, including the LSX conjecture,
is used.

## Checks

D3 exact finite enumeration: `../code/t1_reflection_enum.py`,
receipt `../evidence/t1-reflection-enum.json`; exact scope and actual run
record in `../attempts/T1.md`. Independent rerun pending. The theorem is
proved by hand; finite checks do not supply its quantifier over all orders.

## Sources

See `../novelty-gate-T1.md` and `../literature-T1.md`. Classical parity
aliases and short-axis arguments are acknowledged; no priority claim.

## Proof

If a coordinate projection of X has r<=n levels z_1,...,z_r, then
product_(s=1)^r(x_j-z_s) is a nonzero polynomial in Pi_n vanishing on X.
Thus injectivity forces at least n+1 levels in every coordinate. Coupled
coordinates consequently have q_j>=n; independent coordinates have at
least n+1 folded levels. We now use the complete d=3 code list.

**No parity relation, B=0.** The fold is a Cartesian product with at
least (n+1)^3 nodes, strictly greater than binom(n+3,3) for n>=1.

**One pair relation, B=span(110).** Put e=e(n),o=o(n). Both e(q) and o(q)
are nondecreasing in q. At q_1,q_2>=n, the smaller of the two parity
counts is at least min(e^2+o^2,2eo)=2eo. The independent third axis has
at least n+1 levels. For even n, 2eo=n(n+2)/2; for odd n,
2eo=(n+1)^2/2 >= n(n+2)/2. Therefore

    |X| >= n(n+1)(n+2)/2 > (n+1)(n+2)(n+3)/6                 (2)

for n>=2, since the strict comparison reduces to 3n>n+3.

**One triple relation, B=span(111).** Every active denominator is >=n.
Monotonicity of each parity-level count reduces to q_1=q_2=q_3=n.
The smaller parity class has

    ((e+o)^3-|e-o|^3)/2 = ((n+1)^3-delta)/2,
    delta=1 if n even, and 0 if n odd.

This is at least n(n+1)(n+2)/2, since the numerator difference is
n+1-delta>=0. Hence (2) applies again.

**Two relations, B=span(110,101).** The admissible parity vectors are
p and p+(1,1,1), for some p. On the folded nodes

    T_(q_j)(x_j)=(-1)^(i_j).

For any two axes j,k their parity difference is fixed. Thus
T_(q_j)(x_j)-(-1)^(p_j+p_k)T_(q_k)(x_k) vanishes on X. It is a nonzero
polynomial of total degree max(q_j,q_k): q_j,q_k>=1 and its two
nonconstant terms depend on different formal variables. If two q_j were
<=n, injectivity would fail. Since each is >=n, after permutation

    (q_1,q_2,q_3) >= (n,n+1,n+1) coordinatewise.             (3)

For fixed p the sum of its two product counts is nondecreasing in all
denominators. At the lower endpoint (3), its minimum over p is exactly

    M_n = (n+1)(n+2)^2/4         for even n,
          (n+1)^2(n+3)/4         for odd n.                  (4)

Indeed for even n=2r the parity counts are (r+1,r) on the first axis
and (r+1,r+1) on the other two, so every p gives (2r+1)(r+1)^2.
For odd n=2r+1 the first axis has (r+1,r+1), and the other two have
(r+2,r+1); opposite parities on the latter minimize the sum, giving
2(r+1)^2(r+2). These are (4).

For even n, M_n/binom(n+3,3)=3(n+2)/(2(n+3))>1 for n>0.
For odd n, the ratio is 3(n+1)/(2(n+2))>1 for n>1. Thus every n>=2
is excluded, finishing the proof.

### D3: the d=2 specialization admits and spares Padua

Take m=(2n,2(n+1)), B=span(11), the even parity coset, and zero phase.
Its fold is the standard checkerboard
cos(pi i/n),cos(pi j/(n+1)), i+j even. It is reflection stable.
All projections have n+1 or n+2 levels; the pair alias has degree n+1,
so it is outside Pi_n. Its exact count is

    e(n)e(n+1)+o(n)o(n+1)=(n+1)(n+2)/2.

Thus neither the short-projection nor the alias/count proof excludes it.
For completeness, injectivity itself has a direct independent check.
Uniform averaging on the torus subgroup gives a positive cosine Gram.
Its annihilator is generated by (2n,0),(0,2n+2),(n,n+1). Inside the
l1 ball of radius 2n its only nonzero points are (+/-2n,0): a mixed
half-period word has l1 norm at least 2n+1. For distinct modes
T_a(x)T_b(y), T_c(x)T_d(y) with a+b,c+d<=n, product-to-sum frequencies
have l1<=2n. The exceptional frequency (+/-2n,0) could occur only if
a=c=n,b=d=0, which is the same mode, not two distinct modes. All other
nonconstant frequencies average to zero by the elementary character-sum
argument. The offdiagonal Gram entries vanish. Its diagonal entries
are positive: they are the positive continuous cosine norms except for
T_n(x), whose square is 1 on the subgroup. Hence evaluation is injective,
and the displayed count proves Padua unisolvence. This verifies the
sanity requirement with a proof rather than only finite ranks.

### Degree-one boundary

n>=2 is essential to this proof and is sharp as a class obstruction.
For q=(1,2,2) with parity vectors 001 and 110 the four folded points are
(1,+/-1,0),(-1,0,+/-1). Their affine evaluation determinant has absolute
value 8, so they are Pi_1-unisolvent. No n=1 exclusion is claimed.

## Scope

A finite reflection-stable single coset is ruled out already by
injectivity and minimal cardinality. Noninvariant cosets, noninvariant
subgroups, unions of cosets, noncubature constructions and non-total-degree
spectral spaces are not ruled out. This result therefore does not prove
the broad expected nonexistence statement E1 or the LSX cubature conjecture.

## Open items

Independent audit/rerun; original C_k remains in t1-open-class.md.

## History

2026-11-06, Codex, assigned gpt-6.1-sol xhigh, rules/input
ccd9e905d19c0c625c196c4a3f3e707058ed042a. Restricted-class theorem split
from the unchanged original OPEN target, with full reflection assumption.
