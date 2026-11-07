# PD-T?padua-3d-20261106-codex-T8-r06-01 — exact parity permission for M=N

ID kind: PD-T. Aliases: phase parity admissibility; no-fold half-period
degree set. Split from: none. Split into: none.

## Statement

Let n>=1, N=binom(n+3,3), and X={cos(2pi(a+kz/N)):0<=k<N}, for
z in Z^3 and arbitrary real phase a. Assume |X|=N. If N is even,
Pi_n-unisolvence requires n odd and exactly two odd coordinates of z.
Consequently the degrees *allowed by this half-period parity test for
some sign pattern* are exactly n not congruent to 2 modulo 4.
This is a necessary condition only: it asserts neither existence nor
sufficiency at any permitted degree. At n=0 the single-node case is trivial.

## Definitions and assumptions

Cosine acts coordinatewise; turns are used. The full orbit has N distinct
nodes, so k is a bijective node parameter. The test concerns only the
order-two translation when N is even. For odd N there is no such group
element; 'allowed' means this test supplies no obstruction.

## Status by part

Overall status: **PROVED**, elementary analytic proof. Finite witness searches
are separate MEASURED claims in t8-r06-measurements.md. Candidate retained;
the general minimal polylogarithmic cyclic target remains OPEN.

## Depends on

The sign-intertwining argument of PD-N?padua-3d-codex-T8-02 and elementary
coefficient extraction, rederived here. No numerical or source premise.

## Proof

For even N, translation k->k+N/2 is a free involution on distinct nodes,
acting physically as R(x)_j=(-1)^(z_j)x_j. At least one z_j is odd,
otherwise nodes repeat. Let r in {1,2,3} count odd coordinates. The trace
on R^X is zero. Evaluation intertwines this action with R on Pi_n, so
bijectivity requires polynomial trace D_r(n)=0. The monomial basis gives

    sum_(n>=0) D_r(n)t^n = (1-t)^(-(4-r))(1+t)^(-r).

Writing n=2m or 2m+1, use G_1=1/[(1-t)^2(1-t^2)] and
G_3=1/[(1+t)^2(1-t^2)]; expansion gives

    D_1(2m)=(m+1)^2,     D_1(2m+1)=(m+1)(m+2),
    D_2(2m)=m+1,         D_2(2m+1)=0,
    D_3(2m)=(m+1)^2,     D_3(2m+1)=-(m+1)(m+2).

Thus for n>=1 a zero trace occurs exactly for odd n,r=2.
For completeness G_2=1/(1-t^2)^2, whose coefficient at 2m is m+1.

For n=4q, the consecutive numbers n+1,n+2,n+3 contain exactly one
factor of 2 in their product, removed by division by 6, so N is odd.
For n=4q+2 the middle number n+2 is divisible by 4, so N is even.
For odd n, n+1 and n+3 are consecutive even numbers, one divisible by 4,
so N is even. Hence N odd iff n=0mod4. Odd degrees allow r=2 (for
example z=(1,2,3) reduced modulo even N preserves parity); even n=2mod4
allow no sign pattern. This proves exactly the stated permission set.

## D3 and finite reduction

The trace principle admits 2D Padua: its cyclic modulus is 2n(n+1),
z=(n+1,n); the half-period flips one axis, with floor(n/2)+1 fixed nodes.
That is the polynomial trace on Pi_n in dimension 2. Padua's multiple
folds mean its node action is not the free action assumed above. The
checker repeats count/trace equality at n<=12, but the argument is all-n.
For fixed n the sign test enumerates all eight parity patterns exactly;
it makes no finite-phase claim. Existing n2 all-continuous-phase theorem
is recovered, rather than reopened.

## Sources, checks, scope and open items

No external theorem used; literature-T8-round06.md records comparison limits.
Checker: code/t8_r06_routes.py controls and witnesses. Independent rerun of
new finite certificates remains required; it is not needed for this analytic
proof. Full rank may fail for reasons beyond parity. Exact witnesses through
12, and any all-degree construction or quality bound, are separate tasks.

History: 2026-11-06, Codex assigned gpt-6.1-sol xhigh; rules 7afa6a54.
