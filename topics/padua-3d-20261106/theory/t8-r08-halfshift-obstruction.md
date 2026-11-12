# PD-N?padua-3d-20261106-codex-T8-r08-01 — even-degree half-shift obstruction

ID kind: PD-N. Aliases: folded half-period trace; half-shifted2N parity
obstruction; fixed-node correction. Split from: none. Split into: none.

## Statement

For any integer n>=2 set N=binom(n+3,3), M=2N and choose integers b,c.
Let z=(1,b,c) and

    X={ (cos(2pi(2k+1)z_j/(2M)))_(j=1)^3 : k=0,...,M-1 }.

There are exactly N distinct real nodes. Put t=#{j:z_j odd} in{1,2,3},
f=N mod2 and D_t(n)=sum_(|alpha|<=n)(-1)^(sum_(j:z_j odd)alpha_j).
Then the exact characteristic-zero evaluation rank satisfies

    rank(Pi_n -> R^X) <= N - |D_t(n)-f|/2.

Every even n>=2 is therefore singular, for every b,c. At odd n,
unisolvence requires t=2. For the requested n4/6/8 the best possible
upper bounds over t are respectively34/82/163, strictly below35/84/165.
This is not an existence or sufficiency theorem at odd n.

## Definitions and assumptions

The image is the full cyclic orbit with phase a=z/(2M); Pi_n is the
three-variable total-degree real polynomial space. No arbitrary phase,
nonunit-coordinate generator or union of cyclic cosets is covered.
The broad T8 minimal-polylog target remains OPEN. b,c need not be distinct
or nonzero for this theorem, so it includes the narrower screened b<c<M
class. The rank upper bound is a hand proof, not a modular-deficiency claim.

## Status by part

Overall status: **PROVED**, by the analytic argument below.

Candidate/claim disposition: the all-degree construction interpretation of
IDEA?padua-3d-20261106-codex-T8-r08-H is **REJECTED: refuted** in this
first-unit exact-half-shift class, since already n4 fails. The separately
preregistered odd-degree Hdet selector is not refuted by this even-degree
obstruction; its quality is separately MEASURED.

## Negative-result scope

Attempted mechanism: take the coherent half-shift of an order2N cyclic
cosine orbit to fold to N nodes, as an all-degree3D interpolation family.
Parameter range: all integers b,c, every even n>=2, with first generator
coordinate1 and the exact phase z/(2M). No universal cyclic-family or
arbitrary-continuous-phase rejection is asserted.

## Depends on

The sign-intertwining method and trace coefficient identities are already
proved in PD-T?padua-3d-20261106-codex-T8-r06-01. The new fixed-node
calculation is written here. No external source theorem, computer output,
packing bound or numerical-rank assumption is a proof dependency.

## Proof

Write theta_k=pi(2k+1)/M. Equality of first coordinates at k,l is equivalent
to 2l+1=plus-or-minus(2k+1) modulo2M. Thus either l=k modM or
l=M-1-k modM. The latter map is a fixed-point-free involution because
M is even. It preserves every other cosine coordinate too, and no other
identification is possible by the first-coordinate equality. Therefore
|X|=M/2=N exactly.

Translation k->k+N induces the physical coordinate-sign involution
R(x)_j=(-1)^(z_j)x_j. A folded node is fixed precisely when k+N is its
partner M-1-k moduloM, namely

    2k=N-1 mod2N.

If N is even there are no solutions. If N is odd there are exactly two
parameter solutions differing by N, and these are the same folded node.
Thus the permutation representation on R^X has exactly f=N mod2 fixed
nodes, and its plus/minus eigenspace dimensions are(N+f)/2,(N-f)/2.

The monomial basis diagonalizes R on Pi_n, with trace D_t(n), so its
plus/minus eigenspace dimensions are(N+D_t)/2,(N-D_t)/2. Evaluation
intertwines R. Its rank on each eigenspace is at most the smaller of the
two corresponding dimensions. Summing these minima gives
N-|D_t-f|/2, proving the rank upper bound. In particular bijectivity would
force D_t=f.

For completeness the trace generating function is

    sum_(n>=0)D_t(n)s^n=(1-s)^(-(4-t))(1+s)^(-t).

Writing n=2m or2m+1, direct coefficient extraction gives

| n | D_1 | D_2 | D_3 |
|---|---:|---:|---:|
| 2m | (m+1)^2 | m+1 | (m+1)^2 |
| 2m+1 | (m+1)(m+2) | 0 | -(m+1)(m+2) |

At even n>=2 all three traces are>=2 while f is0 or1. Hence every sign
pattern fails. At odd n, N is even (the product(n+1)(n+2)(n+3)/6 has an
uncancelled factor2), so f=0 and only t=2 can pass. At n4,N35 the smallest
trace is3 and f1; at n6,N84 it is4 and f0; at n8,N165 it is5 and f1.
Substitution gives the stated ceilings. This proves the entire claim.

## Checks and sources

Independent analytic reconstruction: the separately assigned checker
reported the same fixed-node counts, trace formulas and ceilings before
seeing producer output; executed check/evidence is recorded in
[independent T8 check](../independent-checks-round08-t8.md) when completed.
Producer code: [t8_r08_halfshift.py](../code/t8_r08_halfshift.py).
No new external publication is used; the bounded predecessor/literature
comparison is [the gate](../novelty-gate-T8-round08.md).

## Scope and open items

This closes the requested even-degree rank questions analytically for the
stated class. Odd-degree rank and quality need separate certificates and
measurements. Escaping the even-degree obstruction would require changing
phase, folding/sign action, generator class or another explicit hypothesis;
additional determinant trials within the excluded class cannot help.
True Lebesgue growth, nonunit-only generators and general phase strata
remain OPEN. This new PROVED scoped obstruction is a material mathematical
change for the focused Claude re-audit.

## History

2026-11-06: Codex mathematical developer assigned gpt-6.1-sol xhigh,
rules9042e1c42964150f30fdbe8563c12ba6c6a8692a. Analytic necessity and the
frozen continuation were registered before mechanism execution, published
by root at69694f3a69ee139ac6b2d6d567c48e549575a8a5. No old killed rule or
accepted n2 classification was reopened.
