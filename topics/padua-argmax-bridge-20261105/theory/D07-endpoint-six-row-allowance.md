# PD-T?argmax-bridge-codex-D07-six — A practical six-row allowance against C2

ID kind: PD-T. Aliases: fixed R2 retained-row comparison; small endpoint
plus central component. Split from: D07 component target. Split into:
none. Dependencies are separate substantive results.

## Statement and status

Let n>=32 be an integer, m=n+1, alpha,beta>=0, alpha+beta<=1/2,
a=(cos alpha+cos beta)/2, P=sin alpha+sin beta, and L=log n.
Use the actual corrected row norms of D05-fixed-special-rows.md and set

    J6=[R_0+R_1+R_(2m-2)+R_(2m-1)+R_(m-1)+R_m]/(nm).

Let C2 be exactly N1-07/C08's C_R at R=2, explicitly restated in
D07-endpoint-finite-h.md. Then

    |J6-C2|<=B6(n;alpha,beta),
    B6=[14a+P(8+L)]/n+(71a+4P)/n^2.                 (1)

In particular, uniformly on this closed near half diamond,

    |J6-C2|<1/400   for every integer n>=10000.       (2)

For signed phases define J6 and C2 by their values at the separate
absolute phases, exactly as in D05's fixed-row model. This gives the
same conclusion for |alpha|+|beta|<=1/2. The six labels are distinct on the stated degree
range. Both parities, both axes and polynomial collisions are included.

Status: **PROVED**, analytic developer component theorem; distinct
review pending. This is the requested small retained-row allowance,
not a full S-M_infty or S-a*S(0) allowance or an argmax certificate.

## Proof

D07-endpoint-finite-h.md bounds the difference between the four actual
endpoint rows and C2 by (4a+7P)/n+(71a+4P)/n^2.
D07-endpoint-central-rows.md bounds the nonnegative central pair by
[10a+P(1+L)]/n. Adding these two bounds proves (1).

On this phase triangle, a<=1 and P<=alpha+beta<=1/2. Therefore

    B6<=[18+(1/2)log n]/n+73/n^2.

This scalar upper decreases for n>=1, since the derivative of its
first term has numerator -35/2-(1/2)log n and the second decreases.
The elementary bound log10000<10 follows from e>8/3 and
(8/3)^10>10000. Consequently at n=10000 the upper is less than

    23/10000+73/100000000=230073/100000000<1/400.

Monotonicity proves (2) for every n>=10000. This is an analytic rational
budget comparison, not an executed scalar experiment.

## Exact use and remaining obligations

The comparison is with the unchanged C2, so it can be inserted into a
separately proved identity containing J6-C2. No signed constant, central
logarithmic mesh or outer quadrature term has been removed implicitly.
The accepted D05 fixed-special model still has its ordinary weighted H
profiles, Delta_2, and its own ordinary-row error. Those must all be
included in any full primitive comparison. The complementary D07 outer
proof is developed separately and is not a premise of (1)-(2).

The old e_rows=(181+19log n)/n+21600/n^2 remains a valid conservative
full-phase bound; D06's obstruction to spending that unchanged formula
remains true. The new near-only estimate (1) changes the actual endpoint
allocation using the inherited exact finite-h identities. It does not
revise the old proof or claim the old allowance was false.

No full phase-relative S_n-a*S_n(0,0) theorem, small global onset,
validated implementation, runtime bound, phase cover, producer or new
degree certification follows. The old near model and its one allowed
correction remain frozen. No numerical run or source edit occurred.

Candidate and attempt: ../ideas/D07-short-endpoints.md and
../attempts/D07-short-endpoints.md. 2026-11-06, parent checkpoint
2e4ac49fa0687a7736bc1df82c12e6483b1c7a94, requested Astra ultra; serving metadata unexposed. The developer
claims a written proof, not independent acceptance.
