# PD-T?padua-3d-codex-T8-03 — parity gate for the minimal even half-grid

ID kind: PD-T. Aliases: half-period trace obstruction; signed eigenspace
dimension test. Split from: none. Split into: none.

## Statement

Let n>=2, N=binom(n+3,3), M=2N-2, z=(1,b,c) modulo M and
X={cos(2pi kz/M):k in Z/M}. This set has exactly N nodes. If it is
Pi_n-unisolvent, n is odd and exactly two coordinates of z are odd.
Thus every even-degree member of this first-unit-coordinate even-order
class is singular. Odd degree and the parity condition are necessary,
not sufficient, and make no quality assertion.

## Definitions and assumptions

Ranks/eigenspace dimensions are exact over R. The first coordinate is a
unit normalized to1, M is even, and the phase is zero. The full orbit is
used. This is a tool for retaining the M38 cubic survivor as a possible
odd-degree lead; it does not classify even moduli with no unit coordinate,
arbitrary phases or arbitrary node sets. No failed universal-family claim
is manufactured: ID kind PD-T reflects this prerequisite scope.

## Status by part

Overall status: **PROVED**, elementary written argument below.
Candidate disposition: retained structural gate for the T8-01 even-order
variant. The broader target remains OPEN.

## Depends on

T3-01 first-unit exact count (or its elementary proof below), polynomial
monomial basis and an involution's plus/minus eigenspaces. No external
source, cubature or numerical rank premise.

## Proof

Equality of first coordinates implies k=l or k=-l mod M, and either
choice makes the entire zero-phase node equal. Thus X consists exactly
of the global-inversion classes, numbering M/2+1=N.

Translation k->k+M/2 induces a physical sign reflection R flipping
precisely the r odd coordinates of z, with1<=r<=3. It is an involution
of X. A fixed physical node must have cos(2pi k/M)=0 since z_1=1.
Such k exist iff4 divides M, and are M/4 and3M/4. These two parameters
give the same node; every odd coordinate vanishes and every even one
is unaffected by R, so this is indeed fixed. Thus the number f of fixed
nodes is1 if4|M and0 otherwise, in particular f<=1.

R acts on R^X with plus/minus dimensions (N+f)/2 and(N-f)/2, so its
trace is f. Evaluation intertwines R on Pi_n and on R^X. If evaluation
is bijective these representations have equal traces. In the monomial
basis the polynomial trace is

    D_r(n)=sum_{|alpha|<=n} (-1)^(alpha_1+...+alpha_r).

Summing first by total degree gives the generating function

    sum_{n>=0}D_r(n)t^n = (1-t)^(-(4-r))(1+t)^(-r).

For n=2m or2m+1, coefficient extraction yields

    D_1(2m)=(m+1)^2,       D_1(2m+1)=(m+1)(m+2),
    D_2(2m)=m+1,           D_2(2m+1)=0,
    D_3(2m)=(m+1)^2,       D_3(2m+1)=-(m+1)(m+2).

For r=1 or3 and n>=2 these never equal f in{0,1}. For r=2 and even
n>=2, D_2>=2 also differs from f. Hence n must be odd and r=2.
For completeness, N is even at every odd n: among n+1,n+2,n+3 two are
even with one divisible by4, and dividing their product by6 leaves an
even integer. Then M=2N-2 is2 mod4 and f=0, so the required trace
equality is consistent. It supplies no sufficiency.

## D3 control and finite scope

The trace principle itself also holds in d=2 and admits 2D Padua.
For Padua's cyclic M=2n(n+1), z=(n+1,n), translation by M/2 flips the
axis with odd generator. Its fixed nodes have that coordinate zero;
parity folding gives floor(n/2)+1 such nodes. The polynomial trace for
a single-axis flip in d=2 is also floor(n/2)+1, from
1/((1-t)(1-t^2)). Thus the criterion does not exclude Padua. The special
first-unit M=2N-2 assumptions do not silently transfer to the usual
Padua generator, whose non-unit coordinates create extra folds.

The preregistered U census tests the full finite cyclic class at n=2,3,
including this first-unit even-order part. It finds no quadratic full-rank
even-order set and the cubic M38 survivor has parity(odd,even,odd),
consistent with the theorem. Separate independent enumeration/rerun is
still a verification obligation; the theorem's all-n proof is analytic.

## Checks and sources

No family run was needed for the proof. A small scratch coefficient-count
sanity at n2..12 agrees with the formulas, is not a proof dependency and
is not a preregistered family screen. U controls/receipts and their actual
commands are in attempts/T8.md. Literature limits: literature-T8.md.

## Scope and open items

Only the exact first-unit zero-phase even half-grid class stated above.
The natural permitted odd-degree class needs a prospectively fixed
generator selector and then all of D2. No arbitrary no-unit-even-modulus,
phase, union or unbounded-family impossibility follows.

## History

2026-11-06, Codex T8, assigned gpt-6.1-sol high, rules e5b64450.
Derived after U found the M38 survivor; no higher-degree even-modulus
quality/rank observation informed the theorem or continuation proposal.
