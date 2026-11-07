# F01 EM2 entropy — Endpoint log subtraction does not give a BV derivative

ID kind: PD-N; final allocation belongs to root.
Alias: PD-N?argmax-bridge-codex-F01-em2-entropy; interior coefficient-zero entropy cusp.
Split from: P2/P7's test of the current log-subtracted cancellation profiles.
Split into: none. Full I06 remains OPEN.

## Exact negative statement

Use the LITERAL E09/E12/E14 regularized cancellation profiles on the
closed near half diamond, with separate absolute phases. For EVERY
c in[1/64,1/4], set alpha=beta=c, p=q=sin c, a=cos c, d=(q-p)_+=0.
Let I_R(phi,z) be the actual right folded cancellation integral and

    C_R(z)=I_R(phi,z)-a I_R(0,z)-d log(pi-z),
    B_R(z)=C_R(z)+q log z, z in(0,pi),
    z0=pi-2c.

Then B_R is differentiable on a one-sided punctured neighborhood of z0,
and

    lim_(z downarrow z0, z>z0) B_R'(z)=-infinity.        (1)

In particular its derivative has infinite total variation on every
closed interval having z0 in its interior. Any phase box containing this
balanced phase therefore has NO finite uniform Var(B_R') bound for this
unchanged profile. These phases have rho=2c in[1/32,1/2], wholly inside
I06's proposed band even before a larger finite domain is considered.

Overall status: **PROVED developer PAPER scoped obstruction**, distinct
review and root adoption pending. Candidate disposition: the finite-
BV-derivative certificate for THIS merely log-subtracted residue is
**REJECTED: refuted**. No whole EM2, first-order expansion, h^2 log m,
entropy-subtracted profile or actual argmax impossibility is asserted.

## Dependencies and definitions

N1-round6-central-log proves the exact entropy identity and central
parameter curves. E12 defines precisely B_R=C_R+q log z; its accepted
conclusion is BV of B_R, not BV of its derivative. With epsilon=pi-z,
the actual right parameters are

    u=p/2,
    s_R(epsilon)=|q/2-a tan(epsilon/2)|,
    I_R(phi,z)=J(u,s_R(epsilon),epsilon).

For 0<=s<u, the SAME-SIGN entropy branch is exactly

    J(u,s,epsilon)
       =2[c0 log(c0/u)+b0 log(b0/u)],
    c0=(u-s)/2, b0=(u+s)/2.                           (2)

It is independent of epsilon on that branch. No derivative through a
moving integration root or a separate cotangent pole is assumed here.

## Proof

Fix any allowed c. Then u=q/2>0 and epsilon0=2c lies strictly inside
(0,pi/2). Because a tan(c)=sin c=q,

    s_R(epsilon0)=|q/2-q|=u.

In some left neighborhood epsilon<epsilon0 the absolute-value argument
is negative, s_R=a tan(epsilon/2)-u>0, and s_R<u. Its derivative is

    s_R'(epsilon)=(a/2)sec^2(epsilon/2)>0,
    lim_(epsilon upward epsilon0)s_R'(epsilon)=1/(2cos c)>0.

Thus (2) applies throughout this neighborhood. Direct differentiation
WITH u fixed and 0<s<u gives

    partial_s J=log[(u+s)/(u-s)].                      (3)

As epsilon increases to epsilon0, s increases to u and (3) tends to
+infinity. Since J on this branch has no other epsilon dependence,
its derivative along the actual parameter curve tends to+infinity.
Changing variable z=pi-epsilon reverses the sign, giving the divergence
to-infinity for the derivative of I_R(phi,z) as z decreases to z0
from above.

The terms already subtracted in B_R cannot cancel this divergence.
Here d=0. At the origin N1's u=0 identity gives, on the central half,

    I_R(0,z)=2tan(epsilon/2)log(sin epsilon).

It is smooth on a neighborhood of epsilon0>0. The added q log z is
also smooth near z0 in(0,pi). Their derivatives are bounded on a
sufficiently small closed neighborhood. Equation(1) follows.

A function of bounded variation on a compact interval has a bounded
representative. On the one-sided open interval above, B_R' is continuous
and its values are unbounded in essential supremum by (1). Changing
values at the single cusp cannot alter that fact. Equivalently, variation
between a fixed interior derivative value and values approaching z0 is
arbitrarily large. Hence Var(B_R') is infinite on every interval stated
in the theorem. This holds at each fixed phase already; it therefore
precludes a finite uniform bound over a box containing that phase.

## Exact rejection scope and retained alternatives

Attempted certificate: remove only the known initial q log z and central
d log(pi-z) terms, then bound the second-order midpoint remainder by a
FINITE derivative-variation norm of the remaining B_R over[0,pi]. The
remaining interior coefficient-zero entropy cusp violates that premise,
even though B_R itself is continuous/BV as E12 correctly proves.

This does NOT refute a finite complete quadrature error of order
h^2(1+logm)^2. An exact entropy subtraction or a separately charged
singular-cell h^2 log m argument might provide such a certificate. Both
remain OPEN/deferred; no new alternative route is developed here. Nor
does (1) prove the full paired sum has no cancellation: a paired or
joint certificate must state and prove its own singularity treatment.
I06 as a broad program stays OPEN, not refuted by this narrower failure.

## Checks, provenance and history

This is an analytic consequence of accepted literal formulas, with no
new external theorem, numerical observation or historical-priority claim.
P2's transition test was registered before mathematics. The preliminary
N1 derivative-log observation arose during that released test; P7's exact
balanced-phase claim/kill and that chronology were then durably recorded
before the full proof, and root explicitly acknowledged the refinement.

No source/script/import/scalar/measurement/endpoint/phase/degree/native/
root/quadrature/threshold/compiler/build/pack or Git/shared action ran.
Only owned NEW F01-em2 prose was written. Rules/input
4a5de2012bad94601c713b2ff5517f2e3fb80af2;2026-11-07, requested Sol
xhigh, actual serving metadata unexposed. Same F01 as the I07 principal.
Distinct review and root final-ID/adoption decisions remain separate.
