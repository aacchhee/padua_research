# C14 — coherent global coefficient vertices and a thin row-freezing error

Rules 4b728b0; 2026-11-06. Coordinator-seeded technical tightness variant
of accepted C09, not a new convexity/cotangent theorem or historical
novelty claim. Prospective gate: [ideas/C14-global-vertices.md](../ideas/C14-global-vertices.md).
Only this new C14 theory and its idea/attempt are changed.

**PROVED analytic upper-bound/operation-count contract; distinct review
pending.** A common global vertex can be maintained through the complete
ordinary-row sum. Its row scalar can be frozen with an explicit
O((w_beta/m)H_n^2) allowance. The total common coefficient-box relaxation
is a different error, bounded separately below; no total O(w/n) loss,
first-order phase-cancellation theorem, measured tightness or executable
speedup is claimed. No computation, fit or cover is a proof premise.

## 1. Domain and unchanged collision treatment

Use C09's n>=2,m=n+1,N=nm and closed phase set
P=B intersect {alpha+beta<=pi}, where B is a closed rectangle in[0,pi]^2.
Require P nonempty. Widths in actual radians are w_alpha,w_beta. The
implementation may impose the narrower requirement B contained in the
triangle, as current C12 does; it may not silently assume that for a
rectangle straddling the diagonal.

Retain rows{0,2m-1,m-1,m} under the ACTUAL complete finite primitive,
with full interval radii. For other rows form C09's ACTUAL denominator
pole index bands, buffer by one grid unit, include seam indices0,n-1,
and require actual outward pole-band width<1. Denote the resulting
fixed set by D_r and its complement by K_r. Then |D_r|<=8, every
possible actual collision is in D_r, and both surviving cotangent
channels have pole distance at least one grid unit. This step precedes
every artificial coefficient choice. No artificial quotient is evaluated
at a potentially removable collision.

Use the same grid and phase-dependent denominator for every coefficient
choice:

    delta=(1-r) mod2,
    lambda=(delta+alpha/pi)/2,
    u_k=2pi*(k+lambda)/n,
    v_r=(r*pi+beta)/m.

On K_r the actual rational row values are

    F_rk=[A(1+cos v_r)+q sin v_r-p sin u_k]
                              /[2(cos u_k-cos v_r)],
    A=cos alpha+cos beta, p=sin alpha, q=sin beta.       (1)

Their normalized sum of absolute values, together with retained/direct
actual terms, is exactly S. The factor1/2, exceptional mode and fixed
odd-board parity are the original N2/C09 conventions.

The following C09 buffer bounds will be used in their full all-row scope.
Put

    W_r(phi)=sum_(k in K_r) 1/|cos u_k-cos v_r|,
    H=H_n=sum_(j=1)^n 1/j.

For every phase and any subset of successful ordinary rows,

    W_r(phi)<=(2n/pi)*H/|sin v_r|,
    sum_r sup_B 1/|sin v_r|<=2m*H,
    sum_r W_r(phi)<=4N*H^2/pi.                         (2)

Also the endpoint-pole-only sum satisfies

    sum_r sup_B |cot(v_r/2)| <=(4m/pi)*H.              (3)

These follow from unit grid pole clearance, |cot x|<=1/dist(x,pi*Z),
the sine chord bound, and the row distance counts already proved in
C09/N1-01. Their use is not restricted to four special rows.

## 2. Eight shared vertices suffice

Choose ONE exact-endpoint coefficient box

    T=[A_lo,A_hi] times[p_lo,p_hi] times[q_lo,q_hi]
        contained in[0,2] times[0,1] times[0,1]         (4)

containing every actual(A,p,q) over P. Endpoints may be exact dyadics
extracted outward from valid interval enclosures. Clip only with proved
global ranges, and reject a finite contradiction. This box is shared by
ALL rows. It has at most eight vertices Z; duplicate vertices are merged.

The coordinator's four coordinates(X,Y,Z0,W) enter (1) only through
(X+Z0,Y,W). The affine image of an independent four-coordinate rectangle
is the three-coordinate box with A endpoints X_lo+Z0_lo and
X_hi+Z0_hi. Convex maxima in A attain one of its endpoints. Thus the
sixteen four-coordinate vertices reduce to at most eight effective
vertices. One may further intersect with A>=0 or choose a tighter valid
global A interval; that is an additional safe relaxation improvement,
not a need to retain the redundant mixed X/Z0 choices.

For z=(A0,p0,q0) in Z define, at a FIXED actual phase phi,

    c_r,z(v)=A0*(1+cos v)+q0*sin v,
    H_r(z;phi)=sum_(k in K_r)
        |c_r,z(v_r)-p0*sin u_k|/[2|cos u_k-cos v_r|],
    F_z(phi)=sum_r H_r(z;phi).                        (5)

Every summand of F_z is the absolute value of an affine function of
the three common coefficients, times a fixed positive weight. Therefore
the TOTAL F is convex in(A0,p0,q0), for each fixed actual phi. Let
D(phi) be the exact normalized sum of all retained actual rows and
actual D_r samples. The coherent global majorant is

    G(phi)=D(phi)+(1/N)*max_(z in Z) F_z(phi).          (6)

Expressing the actual coefficient triple as a convex combination of
the SAME shared vertices gives

    S(phi)<=G(phi).                                  (7)

Denominator/grid phases stay fixed at that same phi in this argument.
Convexity in the physical phase or in v is neither needed nor asserted.
Coefficient-box dependence on the original phase does not invalidate
(7): containing its image in(4) is precisely the relaxation.

For a whole box, the valid order is

    sup_P S <= sup_P D +(1/N)*max_z sup_P F_z.         (8)

Finite max commutes with sup, whereas replacing max_z sum_r by
sum_r max_z gives a potentially weaker upper. A numerical implementation
must accumulate each z through ALL successful rows before taking the
global max. Per-row interval enclosures of H_r can be added within that
z accumulator, but the vertex identity must not be forgotten.

## 3. Freeze each row scalar once; add a radius, not a new row max

Let beta_c be the exact midpoint of the beta interval and
v_r0=(r*pi+beta_c)/m. For fixed vertex z put

    c_r,z,0=A0*(1+cos v_r0)+q0*sin v_r0,
    L_z>=sqrt(A0^2+q0^2),
    epsilon_r,z=L_z*w_beta/(2m)+rho_r,z.              (9)

One may use L_z=A0+q0<=3. The ideal exact square-root choice is at most
sqrt5; a numerical square-root upper includes its own upward rounding
and need not literally be below sqrt5. The defining lower inequality
is mandatory; a rounded underestimate is invalid. Because

    d[c_r,z(v)]/dv=-A0*sin v+q0*cos v,

the derivative magnitude is at most sqrt(A0^2+q0^2). Choose ONE exact
dyadic coefficient ctilde_r,z with a validated center error

    |ctilde_r,z-c_r,z,0|<=rho_r,z.

For example enclose c_r,z,0 at adequate precision, choose its exact
dyadic midpoint and carry the full radius. Since |c_r,z,0|<=5, the
chosen point can be projected to[-5,5] without increasing the error.
Thus ctilde_r,z may be assumed in[-5,5]. Every actual phase then has

    |c_r,z(v_r)-ctilde_r,z|<=epsilon_r,z.              (10)

The nonzero center arithmetic radius is a real error term. It is not
absorbed into an asserted exact transcendental point or discarded.

Define the fixed-numerator centered row

    Htilde_r(z;phi)=sum_(k in K_r)
        |ctilde_r,z-p0*sin u_k|/[2|cos u_k-cos v_r|],
    Ftilde_z=sum_r Htilde_r(z;phi).                   (11)

The reverse triangle inequality and(2) give

    |Htilde_r-H_r|<=epsilon_r,z*W_r/2,
    |Ftilde_z-F_z|/N<=E_z,
    E_z=(2/pi)*max_r(epsilon_r,z)*H^2.                (12)

One can instead sum the sharper rowwise allowance using
W_r<=(2n/pi)H*sup_B1/|sin v_r|; it has O(n) scalar work. The simple
uniform form in(12) proves

    E_z <=[L_z*w_beta/(pi*m)+(2/pi)*rho_z]*H^2,
    rho_z=max_r rho_r,z.                             (13)

Only the freezing/center error appears in(13). Its phase-dependent part
is O((w_beta/n)H_n^2), with no phase-distance denominator or tangent-root
factor. This is a uniform VALUE estimate, not a derivative bound.

The proposed implementable exact-real upper model is

    M(phi)=D(phi)+max_z [Ftilde_z(phi)/N+E_z].         (14)

Equations(6),(12) imply the two-sided comparison

    S(phi)<=G(phi)<=M(phi)<=G(phi)+2*max_z E_z.        (15)

For the upper inequality, Ftilde_z/N+E_z<=F_z/N+2E_z;
take the finite maximum. Thus the ADDITIONAL loss from using centered
fixed numerators is controlled by twice the thin remainder. There is
no need to create two further local c endpoints or to take a rowwise
max after this freezing step. A common global z remains coherent.

In numerical whole-box form, if U_D>=sup_P D and U_z>=sup_P Ftilde_z/N
are validated, then

    U=U_D+max_z(U_z+E_z) >=sup_P S.                   (16)

U_D and different row intervals can overestimate at different phases.
Neither(15) nor(13) bounds U-sup_P S; ordinary interval dependence and
all numerical/tail radii must still be assessed separately.

## 4. Fixed roots, whole-box backend and bounded operation count

For each pair(r,z), (11) has the SAME form as a fixed C09 vertex with
coefficients(ctilde_r,z,p0). Its numerator roots are fixed in angular u.
If p0=0 the numerator is constant, including ctilde=0. If p0>0, exact
comparison of|ctilde| with p0 decides no roots or the three complete
root families asin(ctilde/p0), pi-asin(ctilde/p0), asin(ctilde/p0)+2pi.
Exact dyadic endpoints allow rational ratio/equality tests, and tangencies
use their exact pi/2 angles.

The real-index root band varies only by-alpha/(2pi), so its exact
width is at most w_alpha/(2pi)<=1/2. Outward root/index arithmetic must
literally certify band width<1. Closed equality points are direct, and
empty-integer bands still insert a cut. At most three regular artificial
samples per pair(r,z) lie outside the original D_r. They use the
ARTIFICIAL rational value, not an actual finite primitive substitute.
The original buffered pole clearance keeps these terms regular.

The remaining signed cores have at most12 blocks/channel. Their exact
artificial coefficients are

    C_r,z=(p0-ctilde_r,z/sin v_r)/4,
    D_r,z=(p0+ctilde_r,z/sin v_r)/4.                  (17)

Evaluate all positive and negative cores by their fixed sign times
C_r,z*Qminus+D_r,z*Qplus. Do not reuse the original correlated signed
row T. Offset balls supplied to C06 or another accepted C02-compatible
backend enclose the WHOLE phase box; fixed wraps and both strict pole
guards are checked on the actual balls. No derivative of a moving block
or point-only substitution is used.

At fixed orders and precision, each ordinary row needs at most eight
actual primitive evaluations once, and at most eight centered vertices
with three regular artificial terms and24 partial calls each. Four
retained rows use4n bounded-work actual primitive evaluations. Thus a
bounded attempt uses O(n) scalar work, with at most192 partial calls
per ordinary row in this conservative count. This is twice C09's
four-vertex upper count, rather than the32 vertex evaluations per row
that16 global choices times two local endpoints would require.
Duplicate global vertices and zero artificial rows can be merged.

Backend moment/prefix costs, elementary argument reduction, integer bit
lengths and higher precision are not constant bit cost. No unbounded
root-refinement/retry loop is included. The much larger constants may
erase any practical speed gain. Current C12 is an implementation of C09,
not this C14 algorithm; no range or whole-box capability is transferred
to code merely by this proof.

## 5. Fallback must preserve the common vertex family

Stage all artificial computations for a row before committing them to
the global vertex accumulators. If ANY vertex/root/sign/wrap/backend
branch fails, replace the ENTIRE ACTUAL row by the proved common upper
n*N, and remove that row from EVERY global vertex accumulator. Its
actual D_r contribution is replaced along with the row, not added twice.
Equivalently apply(5) only to the subset of successful rows and place
all failed-row caps in the common D term. Convexity of that subset sum,
all-row bounds(2) and the freezing estimate remain valid.

One may not drop a failed global vertex or replace only its artificial
row value by the actual polynomial cap: the artificial rational value
need not satisfy the actual finite-primitive bound. That would corrupt
the common maximum. Common whole-actual-row replacement avoids this.
The fallback loss is separate and may be enormous; it is not paid by
the small freezing remainder.

Retained actual primitive failures may use their proved finite global
caps. Since |F|<=N, row<=nN and S<=2N, every bounded attempt has a
finite validated fallback on valid mathematical input. Form all caps
with checked exact/arbitrary-precision or outward products. Invalid n,
nonfinite rectangles or unsupported native ranges require rejection,
not a mathematical fallback assertion. Respect the actual selected
backend/platform limits and its pinned source/library identities.

## 6. What common vertices improve, and what they do not prove

For the SAME common coefficient box, define the independent-row model

    R_sep(phi)=D(phi)+(1/N)*sum_r max_z H_r(z;phi).

Then purely algebraically

    S<=G<=R_sep.                                    (18)

The inequality can be strict: the elementary nonnegative convex rows
|1+a| and|1-a| on a in[-1,1] have common-vertex total2, whereas the
sum of their separate maxima is4. This illustrates the operational
difference; it is not a measured Padua tightness example.

If a C09 row(c,p) rectangle contains every image
(A0*(1+cos v_r)+q0*sin v_r,p0) for z in the common box and phi in P,
then R_sep is no larger than C09's exact row-rectangle majorant. This
holds for matching natural interval construction from the SAME global
A,p,q enclosures and whole-box v_r balls. A narrower row rectangle
computed from additional original-phase correlations need not contain
the artificial global images, so no comparison is asserted then.
When common direct/fallback rows also match, (15) gives

    M <= C09_row_majorant+2*max E_z.                  (19)

This is an exact-real comparison of mathematical relaxations. It does
not order two finite-precision executable uppers or different fallback
patterns. It is the precise sense in which the global construction can
retain row cancellations while paying only a thin additional centering
allowance.

There remains a separate relaxation from the common coefficient box
itself. In the following bound D contains exact actual common terms,
with no coarse fallback loss. If actual-row caps are used, their excess
over the corresponding actual rows is additional and is not paid here.
Let the box widths be Delta_A,Delta_p,Delta_q. At each actual phase,
the reverse triangle inequality bounds a vertex numerator change by

    Delta_A*(1+cos v_r)+Delta_q*|sin v_r|+Delta_p.

Using(2)–(3), its normalized effect satisfies

    0<=G-S<= [(4/pi^2)*Delta_A+(2/pi)*Delta_p]*H^2
                                  +(2/pi)*Delta_q*H.  (20)

For the A term, (1+cos v_r)W_r <=(2n/pi)H*|cot(v_r/2)|;
sum(3) and divide by2N to get4*Delta_A*H^2/pi^2. The p term follows
from the last bound in(2). For q, |sin v_r|W_r<=(2n/pi)H and at
most2m rows give2*Delta_q*H/pi. The same shared-vertex maximum is
bounded by the uniform estimate; no factor8 is multiplied into it.

Exact coefficient ranges permit Delta_A<=w_alpha+w_beta,
Delta_p<=w_alpha and Delta_q<=w_beta. Near the origin the cosine
range can instead be quadratic: on B=[0,a] times[0,b],
Delta_A=(1-cos a)+(1-cos b)<=(a^2+b^2)/2. Actual outward coefficient
widths, including any additional rounding, must replace those ideal
range widths in an implementation.

Bound(20) has no general1/n factor. It cannot be relabeled as the
freezing error(13). Nor does a single common vertex automatically
preserve every physical first-order cancellation. The elementary
function f(alpha)=cos alpha+sin alpha on
[pi/4-h,pi/4+h],0<h<pi/4, has actual maximum sqrt2, but the independent
global(cos alpha,sin alpha) rectangle maximum is
sqrt2*(cos h+sin h)=sqrt2+sqrt2*h+O(h^2). Thus a shared coefficient
rectangle can lose a physical stationary cancellation at first order.
This is a counterexample to that generic inference, not a refutation of
a sharper Padua-specific structural estimate or of(7)–(20).

Consequently C14 proves the global construction, its nearly dominating
comparison(19), and the thin freezing term. A Padua-specific total
artificial-loss O((w/n)H_n^2), numerical first-order cancellation or
useful finite-bridge tightness remains OPEN unless separately proved.

## 7. Full analytic tail and adoption boundary

Choose any accepted fixed-order C02-compatible partial backend. If its
smooth order is J, harmonic prefix/order K,Lh, and its separately
enclosed w' tail is tau, then one centered vertex/channel has analytic
allowance at most

    e=7*n*h^4*M_J/5760+24*eta_(K,Lh)/h+h*tau,
    h=pi/n.

Since ctilde in[-5,5] and p0 in[0,1], C09's artificial weight argument
gives sum_r sup(|C_r,z|+|D_r,z|)<=m(1+5H). Thus EACH complete global
vertex accumulator has normalized analytic allowance at most

    [7*pi^4*M_J/(5760*n^4)+24*eta_(K,Lh)/pi
                                    +pi*tau/n^2]*(1+5H). (21)

The global maximum uses the largest common allowance, not eight times
it. All actual direct primitive radii, ordinary arithmetic/phase widths,
coefficient calibration errors and freezing allowance remain additional.
For a backend returning complete balls these tails are already embedded;
(21) is an audit budget, not an instruction to add them twice. In
particular the released J16 backend must use its actual J16 tail, not
the old J48/J96 mathematical constants. No fixed tail is declared
arbitrarily small at unbounded degree.

The proof handles closed axes via p0/q0=0 constant branches, exact
tangencies via fixed root families, and collision/end rows by original
finite primitives. Negative phases require the existing separate evenness
and any necessary axis splitting. It provides S uppers only: a corner
orbit, projected/full defect, gradient, global phase cover, acceptance
margin and practical CPU cost each needs a separate reviewed contract.
No code, expensive diagnostic, board, fit or consequential replay was
performed in C14. C15 remains unstarted; no C16 is proposed.
