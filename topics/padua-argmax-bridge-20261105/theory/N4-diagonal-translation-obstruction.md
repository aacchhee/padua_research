# PD-N?argmax-bridge-codex-N4-01 — Exact mode-diagonal nodal translation is positive only on the complementary grid

ID kind: PD-N.
Aliases: finite Chebyshev spectral translation; dual diagonal translation; nodal-closure obstruction.
Split from: IDEA?argmax-bridge-codex-N4-02.
Split into: none.

## Statement

Fix an integer n>=2, m=n+1, the even-checkerboard Padua nodes
`B_jk=(cos(j*pi/n),cos(k*pi/m))`, and c=(-1,-1). Let L be the
complete cardinal vector from PD-T101. For a real matrix M define
its dual nodal operator on Pi_n by

    (A_M p)(B_j)=sum_i M_ij p(B_i),                            (1)

with the unique interpolating polynomial A_M p. Require that every
product-Chebyshev polynomial q_ab=T_a(x)T_b(y), a+b<=n, is an
eigenvector of A_M. For each z in [-1,1]^2:

1. There is exactly one matrix in this mode-diagonal class satisfying
   `M L(c)=L(z)`. It has column sums exactly1.
2. That matrix is nonnegative **if and only if** -z is a Padua node.
   Equivalently, z lies on the complementary tensor checkerboard
   `z=(cos(l*pi/n),cos(r*pi/m))`, l+r odd.

Consequently the universal positive-translation candidate within this
fixed class fails for every n>=2 at z=(0,0). In particular, at n=3
the entry M_(00,00) there is exactly -1/8.

## Definitions and assumptions

The diagonal class is fixed by the modes before testing; it allows
arbitrary real eigenvalues and imposes no guessed sign pattern or
target norm bound. It is an additional constraint on M, not part of
the unrestricted N4 class. All node/corner zero cardinals are retained.
At c, q_ab(c)=(-1)^(a+b), which never vanishes.

## Status by part

Overall status: **PROVED**, analytic proof below.

| Mathematical part | Status | Evidence / limitation |
|---|---|---|
| Unique diagonal operator and column normalization | PROVED | Basis reproduction |
| Exact positivity set and off-grid obstruction | PROVED | Generic variance rigidity and direct periodic-grid construction |
| Explicit n3 center entry | PROVED | Three surviving modes in the exact kernel |

Candidate disposition: **REJECTED: failed** as an operator family
positive for every z in the square. It remains positive on its exact
finite complementary-grid locus. This is a class-only failure, not a
refutation of general N4 or PD-T099.

## Negative-result scope

Attempted mechanism: IDEA?argmax-bridge-codex-N4-02, nonnegative
mode-diagonal dual nodal operators transporting L(c) to L(z).
Parameter range: every n>=2; positivity is impossible at every z
outside the complementary checkerboard. No restriction is imposed
on the eigenvalues before their unique forced values are derived.

## Depends on

PD-T101 cardinal identity/unisolvence; elementary cosine addition;
PD-T?argmax-bridge-codex-N4-02 for the variance rigidity corollary.
No source product-formula theorem is assumed.

## Proof

Write A_M q_ab=d_ab q_ab. Multiplying M L(c)=L(z) by the row of
nodal q_ab values gives, using(1) and interpolation,

    q_ab(z)=(A_M q_ab)(c)=d_ab q_ab(c).

Hence necessarily d_ab=q_ab(c)q_ab(z). Conversely, define

    tau_z q_ab=q_ab(c)q_ab(z)q_ab,
    (M_z)_ij=(tau_z L_i)(B_j).                               (2)

Interpolation gives `M_z L(c)=L(z)`. A mode basis determines tau_z
and then all entries uniquely. Since tau_z 1=1, every column sums
to1. These identities are independent of positivity or lambda.

The node B_00=(1,1) belongs to the Padua set. Its column in(2) is

    (M_z)_(i,00)=(tau_z L_i)(1,1)=L_i(-z),                    (3)

because q_ab(1,1)=1 and q_ab(-z)=q_ab(c)q_ab(z). If M_z>=0,
(3) is a nonnegative cardinal vector. Variance rigidity forces -z
to be a node. Since n+m is odd, reflection in both coordinates
exchanges the even and odd tensor checkerboards; this proves the
stated equivalent description of z.

For sufficiency let z=(cos(l*pi/n),cos(r*pi/m)) with l+r odd.
Set h=n-l and k=m-r; then h+k is even. For every polynomial p,
modewise cosine addition proves

    (tau_z p)(cos(theta),cos(phi))
      =1/4 sum_(sigma,eta=+/-1)
        p(cos(theta+sigma*h*pi/n),
          cos(phi+eta*k*pi/m)).                              (4)

At any node theta=j*pi/n, phi=t*pi/m, each of these four arguments
is again a Padua node: integer indices j+sigma*h,t+eta*k have
even sum; reduction modulo2n,2m and folding by cosine preserve
parity. This argument includes endpoints, repeated arguments and
all collisions. Apply(4) to L_i. Each cardinal evaluation is0 or1,
so every matrix entry in(2) is an average of four nonnegative
numbers. Thus M_z>=0.

The point(0,0) is not a tensor node: zero cosine would require
j=n/2 and t=m/2, while consecutive n,m cannot both be even.
It is therefore outside the positivity set for every n>=2.

At n=3 and z=(0,0), equation(3) gives M_(00,00)=L_00(0,0).
In the PD-T101 kernel only modes(0,0),(2,0),(0,2) survive there;
their values at B_00 are1 and their contributions are1,-2,-2.
The exceptional(3,0) mode vanishes. Since w_00=1/[2*3*4]=1/24,

    L_00(0,0)=(1-2-2)/24=-1/8.

This completes both directions and the exact witness. QED.

## Checks and sources

The proof is analytic. Small-degree exact cyclotomic verification at
n=3,...,8 and rational point z=(0,0) is recorded by
`../code/n4_exact_invariants.py` and `../evidence/n4-exact-invariants.json`.
No LP was run. These checks are supplementary, with no computer-proof
premise. Independent Astra review is pending.

No Askey–Gasper or Koornwinder–Schwartz theorem has been transferred;
their fulltexts remain unread by this worker. Formula(4) is derived
directly from finite cosine addition, not attributed to those papers.

## Scope

The complementary-grid scalar bound supplied by these positive
matrices is already an immediate consequence of PD-T364:
lambda=S_n(0,0)-Delta<=Lambda_c. It is not a new scalar argmax
result. The useful new gate information is the exact limitation of
this matrix class. Convex combinations of these diagonal matrices
remain diagonal and cannot escape its proven restriction.

Unrestricted substochastic matrices remain equivalent to the target
norm inequality by N4-01. Other non-diagonal positive matrix classes,
lifted spaces, grouped features and operators using cancellation
are not excluded.

## Open items

A repair must relax exact mode-diagonality or finite nodal closure;
merely mixing the positive diagonal translations does not suffice.
An unspecified repair is not an active candidate or a general N4 kill.
PD-T099 remains OPEN, with certified range unchanged at2–32.

## History

2026-11-05, N4 round1 after novelty-gate-N4.md was completed, Codex
parent-assigned gpt-6.1-sol xhigh; runtime metadata not independently
exposed. Rules/input `98d6c00d8a474cf97602c9cfdea631a837191ac0`.
Candidate(2) was frozen before the exact test. The proof's sufficiency
sharpening was derived after the initial zero-variance obstruction;
no retrospective preregistration is claimed. Original B5 unchanged.
