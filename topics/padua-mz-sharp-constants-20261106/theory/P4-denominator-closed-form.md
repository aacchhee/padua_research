# PD-T548 — closed-form endpoint denominator

2026-11-06 ID history: `PD-T?mz-sharp-codex-P4-02` → `PD-T548`; statements, original registrations and historical dispositions are preserved.

ID kind: PD-T.
Aliases: S2 continuous Gram entries; sine-rational endpoint mass matrix;
P4 denominator identity.
Split from: none; durable supporting writeup of the already accepted S2
Gram calculation, requested by audit-02 B2.
Split into: none.

## Statement

For every pair of positive integers i,j, set a_j=pi*j, s_j=(-1)^j and

    F_j(t)=2s_j*a_j^2*sin(t)/[t(t^2-a_j^2)],       t>=0,

with removable singularities filled by continuity. These are exactly the
functions f_j in [S2-endpoint-model.md](S2-endpoint-model.md). Put

    d_j=Cin(2a_j),
    C_ij=integral_0^infinity t F_i(t)F_j(t) dt.

Every entry integral is absolutely convergent, and its exact value is

    C_ij=2s_i*s_j*(a_i^2*d_j-a_j^2*d_i)/(a_i^2-a_j^2),  i!=j,
    C_jj=2[a_j*Si(2a_j)+d_j].

Consequently, for every finite J>=1 and every real vector u in R^J,

    integral_0^infinity t (sum_(j=1)^J u_j F_j(t))^2 dt
      =sum_(i,j=1)^J u_i C_ij u_j.

## Definitions

All integrals use the real variable and unnormalized Lebesgue measure.
For x>=0,

    Si(x)=integral_0^x sin(v)/v dv,
    Cin(x)=integral_0^x (1-cos(v))/v dv,

where the integrands at zero have their continuous values. In the
conventional cosine-integral notation Ci(x)=gamma+log(x)-Cin(x), x>0,
this gives d_j=gamma+log(2a_j)-Ci(2a_j), the notation in the registered
S2 formula. The proof uses the convergent Cin integral directly; no
evaluation of gamma or Ci is needed.

Infinity integrals below mean limits with upper endpoint R tending to
infinity. Algebra involving terms that separately diverge at infinity is
performed only at a common finite R. At the internal point t=a_j the
integrands are extended continuously; no principal-value convention is
used. For integration by parts one may first omit
(a_j-epsilon,a_j+epsilon), then send epsilon down to zero at fixed R.

## Assumptions

The indices are positive integers, so every a_j is a positive integer
multiple of pi. This hypothesis supplies sin(a_j)=sin(2a_j)=0 and
sin^2(v+a_j)=sin^2(v), sin(2v+2a_j)=sin(2v). The basis is exactly the
signed, endpoint-cancelled S2 basis above. No extension to arbitrary
positive real frequencies or to infinite coefficient sums is asserted.

## Status by part

Overall status: **PROVED**.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Absolute convergence and removable-pole interpretation | PROVED | Endpoint estimates in proof, part 1 |
| All off-diagonal entries | PROVED | Common-cutoff identity for I(a), then partial fractions |
| All diagonal entries | PROVED | Diagonal partial fractions, integration by parts and the explicit Si integral |
| Every finite quadratic denominator | PROVED | Finite expansion under the absolutely convergent integral |

Candidate / claim disposition: not applicable.

## Depends on

Only the exact definition of the basis in
[S2-endpoint-model.md](S2-endpoint-model.md) and elementary integral
identities proved below. Neither model convergence nor a numerical
quadrature or special-function evaluation is a premise. Positive
definiteness and the variational interpretation used by P4 remain in
[S2-fixed-trial-limit.md](S2-fixed-trial-limit.md).

## Checks

This record expands the accepted derivations in
[independent-checks-S2-model.md](../independent-checks-S2-model.md),
section “Independent reconstruction of the closed-form Gram”, and
[independent-checks-P4.md](../independent-checks-P4.md), section
“Mathematical reconstruction”. [Audit-02](../audit-02.md), B2, accepts
the formulas and requests this durable record. Its independent
closed-form-free check is described in
[p4_independent.py](../audit-02-support/P24/p4_independent.py); no audit
support file is changed and no execution of that script is claimed here.

No new numerical run is needed for the written identity or was performed
for this record. 2026-11-06 (audit-03 F1): the distinct supplementary
check is [independent-checks-P4-denominator.md](../independent-checks-P4-denominator.md),
and the focused Claude recheck is [audit-03](../audit-03.md).

## Sources

The local definitions and accepted derivations linked above. No external
literature result, novelty claim or priority claim is used.

## Proof or evidence

### 1. Removable singularities and convergence

At zero, sin(t)/t tends to 1, so F_j(0)=-2s_j. At t=a_j+z the expression
is

    F_j(a_j+z)=2a_j^2*(sin(z)/z)/[(a_j+z)(2a_j+z)],

which tends to 1. At every other positive grid point a_k the value is
zero. Thus all apparent basis poles are removable. For each fixed j,
F_j is bounded on compact intervals and F_j(t)=O_j(t^-3) at infinity.
Therefore t F_i F_j=O_(i,j)(t) at zero and O_(i,j)(t^-5) at infinity,
and it is continuous at every internal point. This proves absolute
convergence of C_ij.

For a positive integer multiple a of pi, introduce

    H(x)=integral_0^x sin^2(v)/v dv=Cin(2x)/2,       x>=0,
    I(a)=integral_0^infinity sin^2(t)/[t(t^2-a^2)] dt,
    K(a)=integral_0^infinity t sin^2(t)/(t^2-a^2)^2 dt.

The I integrand is O(t) at zero, tends to zero at a and is O(t^-3)
at infinity. The K integrand is O(t^3) at zero, tends to 1/(4a) at a
and is O(t^-3) at infinity. Both integrals are absolutely convergent.
The identity for H follows from sin^2(v)=(1-cos(2v))/2 and substitution.

### 2. The common-cutoff integral I(a)

For R>a, partial fractions give

    a^2 I_R(a)
      =integral_0^R sin^2(t)[t/(t^2-a^2)-1/t] dt
      =(1/2)integral_0^R sin^2(t)/(t-a) dt
       +(1/2)integral_0^R sin^2(t)/(t+a) dt-H(R),

where I_R is I with finite upper endpoint R. Each finite integral has a
removable integrand at its apparent pole. Translation by a and the
integer-multiple-pi hypothesis give exactly

    integral_0^R sin^2(t)/(t-a) dt=H(R-a)-H(a),
    integral_0^R sin^2(t)/(t+a) dt=H(R+a)-H(a).

For the first equality, sin^2(v)/v is odd on [-a,R-a], so its negative
part contributes -H(a). It follows that

    a^2 I_R(a)=(1/2)H(R-a)+(1/2)H(R+a)-H(R)-H(a).

The absolute value of the first three terms on the right is at most

    (1/2)log(R/(R-a))+(1/2)log((R+a)/R),

which tends to zero as R tends to infinity with a fixed. Thus

    I(a)=-H(a)/a^2=-Cin(2a)/(2a^2).                (1)

No value was assigned to a separate integral of sin^2(t)/t on the
half-line; its divergent terms were combined before taking the limit.

### 3. Every off-diagonal entry

For i!=j, write a=a_i, b=a_j. The exact identity

    1/[(t^2-a^2)(t^2-b^2)]
      =[1/(t^2-a^2)-1/(t^2-b^2)]/(a^2-b^2)

gives, after multiplication by sin^2(t)/t and integration,

    C_ij=4s_i*s_j*a^2*b^2*[I(a)-I(b)]/(a^2-b^2).

All integrals here are absolutely convergent as shown above. Substituting
(1) gives precisely

    C_ij=2s_i*s_j*(a^2*Cin(2b)-b^2*Cin(2a))/(a^2-b^2).

This covers both orders of the unequal indices and is symmetric under
interchanging them.

### 4. The Si integral and every diagonal entry

First evaluate K(a). Since

    d/dt [1/(t^2-a^2)]=-2t/(t^2-a^2)^2,

integration by parts on [0,a-epsilon] and [a+epsilon,R] yields in the
limit epsilon down to zero, then R to infinity,

    K(a)=(1/2)integral_0^infinity sin(2t)/(t^2-a^2) dt.       (2)

The boundary expression is -sin^2(t)/[2(t^2-a^2)]. It tends to zero
at zero, at both sides of a, and at infinity. The integrand on the
right of (2) is O(t) at zero, tends to 1/a at a and is O(t^-2) at
infinity, so that integral too is absolutely convergent.

To evaluate it without omitting any cutoff terms, use R>a and

    1/(t^2-a^2)=[1/(t-a)-1/(t+a)]/(2a).

Translation, with sin(2v)/v even and sin(2v+2a)=sin(2v), gives

    integral_0^R sin(2t)/(t-a) dt
      =Si(2a)+Si(2(R-a)),
    integral_0^R sin(2t)/(t+a) dt
      =Si(2(R+a))-Si(2a).

The difference Si(2(R-a))-Si(2(R+a)) is the negative of
integral_(R-a)^(R+a) sin(2v)/v dv. Its absolute value is at most
log((R+a)/(R-a)), which tends to zero. Consequently

    integral_0^infinity sin(2t)/(t^2-a^2) dt=Si(2a)/a,
    K(a)=Si(2a)/(2a).                              (3)

Finally the diagonal partial fractions are

    1/[t(t^2-a^2)^2]
      =(1/a^4)[1/t-t/(t^2-a^2)]
       +(1/a^2)t/(t^2-a^2)^2.

The bracket is kept together at every finite cutoff; its product with
sin^2(t) is -a^2 times the I integrand. Since s_j^2=1,

    C_jj=4a^4 integral_0^infinity sin^2(t)/[t(t^2-a^2)^2] dt
        =4a^2[K(a)-I(a)]
        =2[a*Si(2a)+Cin(2a)],                     a=a_j,

by (1) and (3). The diagonal is evaluated directly, without treating
the integer index as a continuous parameter or taking an off-diagonal
limit. The finite quadratic-form statement follows by expanding a
finite sum and using the absolute convergence already established.

## Scope

This is the exact continuous denominator identity for the existing S2
finite basis and therefore supplies the formula dependency in
[P4-certified-lower.md](P4-certified-lower.md). It adds no new trial,
threshold, certificate, model, sharp-limit statement, decimal value or
upper bound. The earlier integral definition remains canonical. The
novelty gate adds no new candidate search here: this bounded task only
makes an already accepted derivation durable and claims no new mechanism
or priority.

## Open items

No mathematical case in the statement remains open. Supplementary review
and the focused Claude recheck are complete (audit-03 F1, 2026-11-06:
[audit-03](../audit-03.md)). The practical sharp upper enclosure and two-sided numerical value
of Lambda_edge remain separate open refinements in the existing records.

## History

2026-11-06, Codex bounded B2 mathematical developer, gpt-6.1-sol high;
actual serving-model/effort metadata unexposed. Rules and exact input
f3c14d7599b4bf25118ca86bc62aeb5e0fcafe29. Added the durable supporting
derivation requested by audit-02 B2 from the accepted S2/P4 checks, with
all finite cutoffs, removable poles and diagonal cases explicit. The
accepted formulas and their applications are unchanged. Provisional
theory ID only; no final ID or shared registry allocation.
