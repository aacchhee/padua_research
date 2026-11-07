# PD-T?argmax-bridge-codex-N5-02 — Explicit actual-edge margin on a central strip

ID kind: PD-T. Aliases: N5-02; wider-phase central two-copy defect;
finite actual-lambda cotangent-profile margin.
Split from: none; supporting quantitative variant for PD-T099.
Split into: none. Whole-cell E-C and PD-T099 remain OPEN.

## Statement

Let n>=32, m=n+1, epsilon in {-1,1}, and q an integer in [0,m]
such that epsilon^n*(-1)^q=-1. Write

    beta=q*pi/m, phi=beta+s/m,
    11*pi/24 <= phi <= 13*pi/24, |s| <= r <= 1/2.

Let S_n(s)=S_n(0,s) be the inherited vertical primitive from
PD-T185/189/364, and let lambda be the actual Padua Lebesgue function.
Define

    c(r)=1/5-5*r/16-r^2/20,
    d_n(r)=[c(r)/32]*(1-8/n)*(1-8/m).

Then, in exact real arithmetic,

    lambda_n(epsilon,cos phi) <= S_n(s)-d_n(r).          (1)

In particular d_n(1/2)>1/2048 and d_n(1/4)>1/512.

Using the explicit one-variable specialization M_n(0,s) of the
[N1 cotangent row model](N1-row-model.md), with its proved error

    r_n=[7*pi^4/1800+7*pi^3*H_n/900]/n^4,

one obtains the finite-n actual-lambda bound

    lambda_n(epsilon,cos phi) <= M_n(0,s)+r_n-d_n(r).   (2)

For n>=32, r_n<1/65536. Consequently throughout the stated physical strip,

    |s|<=1/2: lambda_n(epsilon,cos phi) < M_n(0,s)-31/65536,
    |s|<=1/4: lambda_n(epsilon,cos phi) < M_n(0,s)-127/65536. (3)

This gives an explicit actual-lambda margin for a one-dimensional model;
it does not assert an upper bound for that model or corner dominance.

## Definitions and assumptions

Use the even checkerboard, a_j=j*pi/n, b_k=k*pi/m, j+k even,
and weights w_jk=2*e_j*f_k/(nm), with endpoint factors 1/2 and all
other factors 1. The corrected exceptional highest mode stays in x.
Let u_j=a_j for epsilon=1 and u_j=pi-a_j for epsilon=-1, and put
tau_j=epsilon^n*(-1)^j. With the finite polynomial kernel D_n, set

    H_+(j,k)=[tau_j*D_n(u_j,phi+b_k)-1]/2,
    H_-(j,k)=[tau_j*D_n(u_j,phi-b_k)-1]/2.

PD-T185 gives the exact polynomial identities

    lambda=sum w_jk*|H_++H_-|,
    S_n(s)=sum w_jk*(|H_+|+|H_-|),
    Delta=sum w_jk*(|H_+|+|H_-|-|H_++H_-|),
    lambda=S_n(s)-Delta.                               (4)

All sums here are over the physical checkerboard. They retain every
finite polynomial collision value. The second line agrees with the
odd-periodic-board primitive S_n(0,s); N1 confirmed this interface.

## Status by part

Overall status: **PROVED**, analytic developer proof below. Distinct
mathematical review and the required Claude audit are pending.

| Part | Status | Evidence / limits |
|---|---|---|
| Finite central-strip actual-lambda defect and model margins (1)–(3) | PROVED | Exact numerator, parity counts, N1/N5 model error |

Candidate disposition: retained quantitative domain/constants variant of
the inherited positive-block method, not a new cancellation mechanism.

## Depends on

PD-T185 for the corrected two-copy edge kernel; PD-T189/191 and PD-T364
for the primitive identity (4). N1's
PD-T?argmax-bridge-codex-N1-01 is used only for (2)–(3), and in turn
uses PD-T?argmax-bridge-codex-N5-01. Their development proofs are written;
their current review states remain explicit in their own files. The
finite-block precedents T222/T224/T366 inform the gate but are not needed
as black-box bounds. No external source theorem is a premise.

## Proof

### 1. Uniform positive numerators on a central physical rectangle

Put A_s=cos^2(s/2), B_s=sin(s)/2. At regular denominator points the exact
edge identity gives

    H_+ = [A_s*(1+cos v_+)+B_s*sin v_+]/[cos u_j-cos v_+],
    H_- = [A_s*(1+cos v_-)+B_s*sin v_-]/[cos u_j-cos v_-],
    v_+=phi+b_k, v_-=phi-b_k.                          (5)

For completeness this follows by writing P_n=T_(n+1)+T_n and
D_n(u,v)=[P_n(cos v)-P_n(cos u)]/[cos v-cos u]. On the checkerboard,
tau_j*(-1)^(q+k)=-1. Since
P_n(cos v_+) and P_n(cos v_-) both equal
(-1)^(q+k)*[cos s*(1+cos v)+sin s*sin v], subtracting the -1 in
H gives exactly (5). Thus the corrected x mode has not been swapped.

Select the physical second angles

    pi/8 <= b_k <= pi/4.                              (6)

The physical-strip hypothesis implies that both v_+ and v_- lie in
[5*pi/24,19*pi/24]. Since A_s>=1-r^2/4 and |B_s|<=r/2, each numerator
in (5) is at least

    f_r(v)=(1-r^2/4)*(1+cos v)-(r/2)*sin v.            (7)

This f_r is strictly decreasing on [5*pi/24,19*pi/24]. Up to pi/2 its
derivative is negative. From pi/2 to 19*pi/24, sin v>1/2 and
|cos v|<=1, while 1-r^2/4>=15/16 and r/2<=1/4, so

    f_r'(v) <= -15/32+1/4 < 0.

The elementary bounds

    cos(5*pi/24)<4/5, sin(5*pi/24)<5/8                (8)

give f_r(19*pi/24)>=c(r). Here is a rational verification of (8):
cos(5*pi/12)=(sqrt(6)-sqrt(2))/4 lies strictly between 9/40 and 11/40,
using 12/5<sqrt(6)<5/2 and 7/5<sqrt(2)<3/2. Its upper bound implies
cos^2(5*pi/24)<51/80<16/25; its lower bound is >7/32 and implies
sin^2(5*pi/24)<25/64. All angles in (8) are in (0,pi/2).
Thus both numerators are >=c(r), and c(r)>=c(1/2)=1/32>0.

### 2. Strict sign bands, both endpoint parities, and exact counts

In each row selected by (6), select only first angles in the **open** band

    phi-pi/8 < u_j < phi+pi/8.                       (9)

Since b_k>=pi/8, this puts u_j strictly between v_- and v_+.
All three angles are in (0,pi), so their cosines are strictly ordered.
The two denominators in (5) therefore have opposite signs and are
nonzero. No selected term is a collision. Each denominator has magnitude
at most 2; hence |H_+|,|H_-|>=c(r)/2. The selected point defect obeys

    |H_+|+|H_-|-|H_++H_-|=2*min(|H_+|,|H_-|)>=c(r).  (10)

The interval (9) lies in (pi/3,2*pi/3), apart from possible bounds of
its closure. Thus all selected physical first indices are interior.
The selected second indices in (6) are also interior: e_j=f_k=1.

For epsilon=1 the selected first-grid parity in a physical row is
j=k mod 2. For epsilon=-1, reflecting j to j'=n-j makes u_j=j'*pi/n
and j'=n+k mod 2. Either parity is a grid of spacing 2*pi/n, and its
representatives in (9) are actual physical indices. An open interval of
length ell contains at least ell/h-1 points of any shifted grid of
spacing h: this includes the case where both interval endpoints are
grid points and excluded. The first-angle count is therefore at least
n/8-1 for **each** selected row. The closed second-angle interval has
length pi/8 and grid spacing pi/m, so there are at least m/8-1 rows.

Every selected pair has weight 2/(nm), and every unselected defect in
(4) is nonnegative. Inserting (10) gives

    Delta >= [2*c(r)/(nm)]*(n/8-1)*(m/8-1)
          = [c(r)/32]*(1-8/n)*(1-8/m)=d_n(r).         (11)

This proves (1). Notice that no periodic/physical factor has been
discarded: (11) uses physical checkerboard weights directly.

### 3. Explicit constants and the actual one-dimensional upper model

For n>=32, both factors in (11) increase with n, and their product is
at least (1-8/32)*(1-8/33)=25/44. Also
c(1/2)=1/32 and c(1/4)=19/160. Therefore

    d_n(1/2)>=25/45056>1/2048,
    d_n(1/4)>=475/225280>1/512.                     (12)

N1's uniform primitive theorem states |S_n(0,s)-M_n(0,s)|<=r_n, with
the r_n displayed in the Statement. Apply its upper inequality in (1)
to obtain (2). Since pi^4<100, pi^3<32 and H_n<=n,

    r_n < 7/(18*n^4)+56/(225*n^3).

This expression decreases with n. At n=32, its product with 65536 is
7/288+112/225=33831/64800<1. Thus r_n<1/65536. Subtracting that bound
from the two strict margins in (12) proves (3).

## Checks

The proof preceded the round-2 diagnostic. No ordering scan, phase
maximization or old 130-case replay supports (1). The developer actually
ran `../code/n5_central_edge_defect.py`: exact rational checks of c and
floor/error constants, then six 80-digit finite-polynomial cases at
n=32,33,48,64, with both endpoint orientations and both phase signs.
Every selected numerator, sign band and grid count passed. An independent
formula for the odd-periodic-board primitive agreed with the physical
two-copy primitive, with maximum absolute discrepancy 9.445809357e-79.
The smallest observed full defect/analytic-floor ratio was 117.013941479.
These are supplementary MEASURED developer diagnostics, not proof premises
or independent agent checks. The command and frozen receipt are in the
N5 attempt/evidence files; distinct review is pending.

## Sources

Full relevant predecessor reads and exact gate are in
`../novelty-gate-N5.md`, round-2 addendum. No unread classical argument
is transferred; the access limitations in `../literature-N5.md` persist.

## Scope and remaining obstruction

The conclusion concerns actual lambda on the stated phase/physical strip
with an explicit finite-degree margin. The one-variable model still has
degree-dependent outer sums and exact harmonic differences. This result
does not control its maximum, does not compare independently optimized
whole cells, and does not establish an effective full R_cen gap.

The fixed rectangle itself cannot handle every phase of a whole edge
cell by the same positive-numerator argument. Its extreme target is
v=19*pi/24. The exact numerator factors as
2*cos(s/2)*cos(v/2)*cos((v-s)/2) and vanishes at s=-5*pi/24, then changes
sign. This is an obstruction to this **fixed-rectangle positivity proof**,
not a refutation of a larger-phase defect bound or E-C. A prospective
repair must move the selected rectangle with the numerator-zero arc, or
bound the actual sign-changing pair defect directly. Corner dominance
would additionally require control of the one-dimensional model's excess.

## History

2026-11-05, Codex, assigned gpt-6.1-sol xhigh; actual runtime metadata not
independently exposed. Input/rules head
`714f3cad18859c07cd13f31561f2a185f9591a7f`. Candidate and exact kill gate
written in the N5 round-2 files before this proof and any new experiment.
The radius-1/4 candidate was consolidated into the parameterized <=1/2
statement before development, preserving its sharper constant. Round 1
theory/code/receipt remain frozen. No Git/shared registry write, new
source fetch or self-audit by this worker.
