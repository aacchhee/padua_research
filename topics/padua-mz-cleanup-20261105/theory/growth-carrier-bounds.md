# PD-T?mz-cleanup-codex-04 — exact carrier norms and one-sided logarithmic spectral bounds

ID kind: PD-T.
Aliases: normalized Fejer packet constants; Rayleigh normalization repair.
Split from: C3's sharp-growth target, which remains OPEN.
Split into: none. This supplies only explicit one-sided bounds.

## Statement

Use the even-m carriers of PD-N105/106 and the odd-m carriers of
PD-T?mz-cleanup-codex-03, with their exact definitions, measures and
strict parameter inequalities. Put g(u)=[sin(u/2)/(u/2)]^4 for u>=0,
with g(0)=1, and

    A=4 log 2,
    C(q)=3q²log|q|-2(q+1)²log|q+1|-2(q-1)²log|q-1|
                 +[(q+2)²log|q+2|+(q-2)²log|q-2|]/2, (1)

where 0²log0 means zero. For admissible a define

    J_-(a)=[A+C(1/a)]/2,
    J_+(a)=[A-C(1/a)-C(2)
                 +(C(1/a+2)+C(1/a-2))/2]/4.          (2)

On each parity, with r=floor(am),s=floor(bm),

    ||p^-_m||² -> A J_-(a)>0,
    ||p^+_m||² -> A J_+(a)>0.                         (3)

Consequently the actual signed extrema obey, over all integers m,

    limsup lambda_-(m,m-1)/log m <= -c_-,
    liminf lambda_+(m,m-1)/log m >=  c_+,             (4)

with the exact positive constants

    c_-=1/[9 A J_-(1/4)],
    c_+=1/[36 A J_+(1/8)].                           (5)

For orientation only, their floating decimal evaluations are
c_-≈0.02962182360 and c_+≈0.01277888644. Equations (1),(2),(5),
not these rounded decimals, define the proved constants. No assertion
that either bound is sharp, or that either spectral limit exists.

More generally, for each fixed admissible a,b the limiting packet
Rayleigh quotients divided by log m are respectively

    -16ab/[9 A J_-(a)],    8ab/[9 A J_+(a)].          (6)

## Definitions and assumptions

Unnormalized Lebesgue dxdy, signed even-checkerboard Padua rule, fixed
parameters a,b>0 with a+b<1/2 for minus or 2a+b<1/2 for plus.
On even m the carrier coordinate is x with mesh m; on odd m it is y
with mesh m+1. The envelope index r always belongs to the carrier
coordinate; s belongs to the other coordinate.

## Status by part

Overall status: **PROVED** (analytic development; [supplementary independent
check completed](../independent-checks-math.md); required Claude audit pending).

| Part | Status | Evidence |
|---|---|---|
| Exact continuous norm limits | PROVED | Rescaled dominated convergence and cosine transform |
| Explicit one-sided all-m spectral bounds | PROVED | Quotient limits and variational principle |

Candidate disposition: retained quantitative normalization variant.
The original sharp-growth target remains OPEN; no matching opposite
bounds or new refutation of the original targets is claimed.

## Depends on

PD-N105/106's accepted even-m signed-energy limits and
PD-T?mz-cleanup-codex-03's odd-m limits. The continuous norm calculation
below is proved independently of any spectral fit or measured crossing.

## Checks

Rules/input ad503cb0603fc017444b0aa732240981eefa4d24.
Analytic proof. A Python 3 `math` evaluation of (1),(2),(5) executed by
this author printed A=2.772588722239781, J_-(1/4)=1.3528830227442048,
J_+(1/8)=0.7840053676911357 and the decimals above. This arithmetic
was only a display check, not a proof premise. The [separate independent
checker verified the integral identity and normalization](../independent-checks-math.md);
required Claude audit remains pending.

## Sources

Local gate ../novelty-gate-math.md. No external theorem or historical
priority claim used.

## Proof

### Rescaled continuous envelope mass

Let L=r+1 and set u=Lt. From the exact Fejer formula,

    F_r(cos(u/L))/L=[sin(u/2)/(L sin(u/(2L)))]².

For u in [0,Lpi], its magnitude is at most min(1,pi²/u²),
using the sum-of-coefficients endpoint bound and sin(t/2)>=t/pi.
After changing variables in the Lebesgue integral
int_0^pi F_r(cos t)² sin t dt, the integrand becomes

    [F_r(cos(u/L))/L]² L sin(u/L),

extended by zero beyond Lpi. It is dominated by
u min(1,pi^4/u^4), an integrable function on [0,infinity).
Pointwise it tends u g(u). Thus every unmodulated envelope with its
index tending to infinity has squared continuous norm tending to
int_0^infinity u g(u)du, independently of its positive degree ratio.

For the carrier coordinate, let its even mesh denominator be D_m:
D_m=m on even m, D_m=m+1 on odd m. In either case D_m/m->1 and
L/m->a. The negative carrier is cos(D_m t/2); the positive carrier
is sin(D_m t/2)sin(rt). At t=u/L they tend respectively to
cos(u/(2a)) and sin(u/(2a))sin u. Their magnitudes are <=1, so the
same integrable domination applies. Their squared-envelope masses
therefore tend to the strictly positive integrals

    J_-(a)=int_0^infinity u g(u)cos²(u/(2a))du,
    J_+(a)=int_0^infinity u g(u)sin²(u/(2a))sin²u du.   (7)

They are positive because each continuous nonnegative integrand is
positive on a nonempty interval; they are finite by the same majorant.
Product integration for the separated polynomials proves (3) once
these integral expressions are identified with (1),(2).

### Exact cosine transform

The absolutely integrable function u g(u) equals

    2[3-4cos u+cos(2u)]/u³.

We claim

    int_0^infinity u g(u)cos(qu)du=C(q)              (8)

for every real q. To prove this without using a quoted transform,
write the numerator after product-to-sum as

    2 H_q(u),
    H_q(u)=3cos(qu)-2cos((q+1)u)-2cos((q-1)u)
                  +[cos((q+2)u)+cos((q-2)u)]/2.

For the five coefficients c_t and signed frequencies t=q,q±1,q±2,
we have sum c_t=0 and sum c_t t²=0. Hence H_q(u)=O_q(u^4)
as u decreases to zero. Integrating twice by parts, with finite upper
and lower cutoffs and then taking limits, gives

    int_0^infinity 2H_q(u)/u³ du
       =int_0^infinity H_q''(u)/u du.                (9)

All boundary terms vanish: H_q/u² and H_q'/u vanish at zero by
the fourth-order cancellation, and at infinity by boundedness of
H_q,H_q'. The last integral is conditionally convergent at infinity
by Dirichlet for nonzero frequencies; zero frequencies have coefficient
c_t t²=0 and contribute nothing.

For positive |t|, the elementary Abel-damped identity

    int_0^infinity exp(-eps u)[cos(tu)-cos u]/u du
        = log((eps²+1)/(eps²+t²))/2

follows by differentiating in t and integrating t/(eps²+t²).
Let eps decrease to zero (Dirichlet tail bounds also identify the
ordinary improper integral); this gives -log|t|. Because
H_q''=-sum c_t t² cos(tu) and sum c_t t²=0, equation (9) equals
sum c_t t² log|t|, with zero terms interpreted continuously. This
is exactly (1), proving (8). In particular C(0)=4log2=A.
Expanding the squared cosine in (7) gives J_-(a) in (2).
Expanding sin²(u/(2a))sin²u gives J_+(a) in (2). This proves (3).

### Energy versus Rayleigh normalization

The signed-energy limits are -16ab/9 and 8ab/9. Division by (3)
proves (6). The variational principle bounds lambda_- above by the
negative packet quotient and lambda_+ below by the positive packet
quotient. The same quotient limits on both parities give these bounds
over all integers m.

For a=1/4 in the negative packet, let b increase to 1/4 through
admissible fixed values. The numerator 16ab/9 tends to 1/9; the
limiting denominator A J_-(1/4) is independent of b>0. This gives
the first constant in (5). For a=1/8 in the positive packet, let b
increase to 1/4; its numerator tends to 1/36 and its denominator is
A J_+(1/8). No boundary-value polynomial family is assumed admissible:
the bounds follow from every fixed interior parameter followed by a
scalar supremum. This proves (4),(5). ∎

## Scope and normalization warning

The elementary optimizations in handoff C3 are correct for **raw sampled
energies**: sup_(a+b<1/2)16ab/9=1/9, and
sup_(2a+b<1/2)8ab/9=1/36. The first uses a=b=1/4 on the closure;
the second uses a=1/8,b=1/4. The strict triangles give suprema, not
attained interior maxima. These raw coefficients are not normalized
spectral constants. Even the previously accepted bounds from C0² would
include that denominator. Equation (3) supplies the actual carrier
normalization and (5) gives useful explicit spectral bounds instead.

These constants are not claimed optimal even within the normalized
carrier family: optimizing (6) is different from optimizing its raw
numerator. The proof identifies no minimizing eigenvector or first
negative degree and makes no inference from an observed slope.

## Open items

Existence and values of the two spectral limits, matching logarithmic
upper/lower controls in the opposite directions, and optimal normalized
packet parameters remain OPEN. Further variants need a new recorded
gate. [Supplementary independent check completed](../independent-checks-math.md);
required Claude audit pending.

## History

2026-11-05, Codex, inherited gpt-6.1-sol xhigh; input/rules ad503cb.
C3 exact-norm calculation preserves the accepted raw carrier formulas
and corrects only their conversion into proposed spectral bounds.
