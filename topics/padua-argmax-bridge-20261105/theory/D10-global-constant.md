# PD-T?argmax-bridge-codex-D10-global — A phase-aware global bound for the true constant

ID kind: PD-T. Aliases: weighted endpoint constant loss; cutoff-free full-phase budget.
Split into: the near increment and scoped axis obstruction have separate records.

Rules/input `9d5e8c7a1a8fab6017d5dd9406daec0d834b0bbf`; latest main
`64409c47a717aef074f611b31a9fd48b7a15101b`. Parent-assigned Sol xhigh;
serving metadata unexposed. **PROVED**, analytic developer result, distinct
review required. Exact real arithmetic; no numerical premise.

Split from: original combined D10-relative-constant first freeze, whose
EXACT complete text is preserved at
[attempts/D10-relative-constant-first-freeze.md](../attempts/D10-relative-constant-first-freeze.md),
SHA256 `56c69c6e39fc0fddf9ada3505c99c293d89fe56d74c2c1a7aa1d643d30c697af`.
This is a substantive split, with no new mathematics or altered constants.
Mapping/history: [attempt](../attempts/D10-relative-constant.md).

## Statement and definitions

Use EXACTLY D02's continuous completed constant C_infty on the signed
phase diamond |alpha|+|beta|<=pi. First take alpha,beta>=0 and put

    rho=alpha+beta, r2=alpha^2+beta^2,
    a=(cos alpha+cos beta)/2, u=1-a, p=sin alpha,
    e=alpha+beta, d=alpha-beta,
    c_e=cos(e/2), c_d=cos(d/2),
    C0=2gamma+4log2,
    c=1/3+(4/pi^2)(log^2 pi-log^2 2).

Let f(x)=Phi_0(1/2+x/(2pi)) and H(x) be exactly the scalar finite-part
functional of C08-far-pole-functional.md. Let E_c be the central
root correction of C01-near-central-upper.md. On the ENTIRE closed phase diamond,

    C_infty(phi)<320/197+66/125+49/100<8/3.               (1)

The stronger phase-aware upper is

    C_infty(phi)<320/197+43/125+(46/125)a+(9/20)sin alpha.

Other quadrants use separate absolute phases; no coordinate-mesh exchange.
The separately stated far relative consequence is in
[D10-far-relative-constant.md](D10-far-relative-constant.md).

## Dependencies

Accepted D02 exact bias and uniform true constant; C08 weighted coefficient,
endpoint constant, scalar pole functional and paired integral bounds. PD-T271
and the accepted D08 origin lower belong to the separate far corollary. The fixed
scalar H is distinguished from the row profile H(L,v). No finite-row theorem
is applied below its degree floor.

## Proof preserved from the combined first freeze

### 1. A cutoff-free decomposition, with every divergent term paired

D02 defines C_infty=E_infty+K_0 with

    E_infty=a/3+a C(t_d)C(t_e)/pi^2,
    t_d=1/2+d/(2pi), t_e=1/2+e/(2pi).

For every 0<epsilon<=pi/4, expand K_epsilon exactly as in C08:

    K_epsilon=K_V,epsilon+K_I,epsilon,
    K_V,epsilon=c_e H_epsilon(d)+c_d H_epsilon(e),
    K_I,epsilon=(4a/pi^2)(log^2 epsilon-log^2 pi)
                   +(1/pi^2)integral_epsilon^pi(I_L+I_R)dz.

Take epsilon down to zero, using D02's EXISTING finite-part limit
and C08's scalar H limit. Thus

    K_V,0=c_e H(d)+c_d H(e).                             (7)

For the cancellation piece the global pointwise inequality proved in
C08 is

    I_L(z)+I_R(z)<=4a cot(z/2)log(sin z)
                                         +2p|log(sin z)|.

Its baseline antiderivative is

    4a log^2(2sin(z/2))-4a log^2 2
                                      -2a Li2(sin^2(z/2)).

At z=pi it equals -a*pi^2/3. The value at epsilon, combined with
the displayed logarithmic counterterm, tends exactly to -c*a:
log(2sin(epsilon/2)/epsilon)=O(epsilon^2), its product with
log epsilon tends to zero, and Li2(sin^2(epsilon/2)) tends to zero.
Also integral_0^pi |log sin z|dz=pi log2. Therefore

    K_I,0<=-c*a+(2log2/pi)p.                            (8)

This rederives the limit for variable epsilon. It is not an application
of C08's FIXED epsilon=1/100 theorem at an unauthorized new cutoff.

### 2. Keep the full-phase weighted endpoint loss

The accepted C08 scalar inequality gives, with b=C0-7/2>0,

    cos(theta/2)C(1/2+theta/(2pi))
                <=C0-b[1-cos(theta/2)], |theta|<=pi.

Both sides are nonnegative. Set x_e=1-c_e, x_d=1-c_d. Their product
is at most

    C0^2-C0*b*u-(7/2)*b*x_e*x_d<=C0^2-C0*b*u,
    u=x_e+x_d-x_e*x_d=1-a.

Thus

    E_infty<=a/3+C0^2/pi^2-[C0(C0-7/2)/pi^2]u.          (9)

The following strict elementary bounds are already proved in the
dependencies: C0<4, C0>391/100>39/10, pi^2>197/20, pi^2<10,
log pi>11/10, log2<7/10, log2>69/100, pi>25/8. They give

    C0^2/pi^2<320/197,
    C0(C0-7/2)/pi^2>39/250,
    c-1/3>36/125,
    2log2/pi<9/20.                                     (10)

C08's global H<1/2 and c_e+c_d<=1+a imply from(7)--(10)

    C_infty<320/197+43/125+(46/125)a+(9/20)sin alpha.

Since a<=(1+cos alpha)/2,

    (46/125)a+(9/20)sin alpha
       <=23/125+sqrt((23/125)^2+(9/20)^2)
       <23/125+49/100.

The square comparison is rational; (23/125)^2+(9/20)^2=0.236356
is strictly below(49/100)^2=0.2401 (these are exact decimals).
This proves the first inequality(1). The exact remaining difference
8/3-[320/197+66/125+49/100]=7181/295500 is positive. All
phase weights, including a=0 and vertices, remain in the proof.

## Scope and history

The new upper improves the old123/40 allowance by at least49/120. No new
finite-degree onset or certificate is claimed: root must preregister and
review any new finite comparison. The old50000 theorem remains unchanged.
The through-origin quadratic form is separately ruled out in
[D10-axis-obstruction.md](D10-axis-obstruction.md); this does not conflict
with the restricted far corollary. The sharper near positive increment is
[D10-relative-constant.md](D10-relative-constant.md). Full finite S-aS(0)
remains OPEN. Paper proof only; no mathematical computation, native/board,
quadrature or degree job. 2026-11-06 split from the exact preserved first
freeze under root's explicit file authorization and reviewer classification.


### Supplementary review closure — 2026-11-06

Distinct Astra xhigh reconstruction ACCEPTED the preceding unchanged
final split scope; no unresolved findings. See
[independent-checks-D10-relative-constant.md](../independent-checks-D10-relative-constant.md),
report SHA256bdcadf119fb905f898612ad25b9123bf8ff58184d6ef573e1503a740d987964c.
The substantive split, inherited-Arb provenance and cutoff-domain wording
findings are closed there. This records no new analytic onset or finite
certificate. Final Claude review remains pending.
