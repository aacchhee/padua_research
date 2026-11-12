# PD-N?padua-3d-20261106-codex-T7-09 — one sample does not decide a phase stratum

ID kind: PD-N. Aliases: one generic phase per stratum; constant-rank shortcut.
Split from: the refuted-inference paragraph of PD-T?padua-3d-20261106-codex-T7-03 ([t7-finite-reduction.md](t7-finite-reduction.md)).
Split into: none. The positive finite symbolic reduction keeps its PD-T ID.

## Statement, assumptions and status

There is a finite subgroup H of T^2 and one all-free cosine-collision
stratum whose node count is constant but whose Pi_1 evaluation rank is
not constant. Therefore a rank-deficient specialization cannot certify
rank deficiency of the entire stratum.

Overall status: PROVED by the exact counterexample below. Candidate
IDEA?padua-3d-20261106-codex-T7-06 is REJECTED: refuted only for the
inference "one arbitrary phase per stratum decides maximum rank".
This is a classification correction of accepted mathematics, not a new
mechanism or a claim that symbolic strata fail.

## Proof and negative-result scope

Use H={(k/3,k/3):k=0,1,2}, with angles in turns. The phases
(1/12,1/12) and (1/12,1/4) are both all-free: no coordinate is in
(1/6)Z/Z. Their cosine images have three distinct points. The evaluation
columns in basis 1,x,y have rank two at the first phase because x=y;
the nonconstant cosine column ensures rank is exactly two.

At the second phase, cos(2*pi*k/3) and sin(2*pi*k/3), together with 1,
are independent on the three residues. Their coefficient determinant is
sin(2*pi*(a_1-a_2))=sin(-pi/3), nonzero; rank is three. Thus the same
node-count stratum contains both ranks. A full-rank exact specialization
still certifies a nonzero symbolic minor. A deficient one supplies no
upper bound on the symbolic maximum.

## Dependencies, checks and scope

The construction and its hand proof are preserved in
[t7-finite-reduction.md](t7-finite-reduction.md), accepted in
[Claude audit-02/T7](../audit-02/T7.md). Exact finite checks there supplement
this proof; no new execution is claimed. The positive finite reduction and
the complete-census target keep their PROVED and OPEN statuses respectively.
The refutation is about a rank-inference shortcut; it excludes no family
of interpolating nodes and is compatible with 2D Padua.

## History

2026-11-06, audit-02 C4 response: split the previously embedded refutation
into a scoped PD-N, preserving all accepted mathematics and the original
PD-T paragraph. No final ID is allocated. Rules read at
7afa6a54a4db4652267e38cd48658ba435d20481; response worker assigned high.
