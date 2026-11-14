# PD-T?argmax-bridge-E05-axis-central-excess — A transported axis excess and root-strip quadrature

ID kind: PD-T. Aliases: collision-safe origin-sign split; exact central cusp;
one-coordinate positive-root quadrature. Split from: supporting finite
operator obligation of the OPEN cusp-aware alpha-axis error target.
Split into: none; this is one supporting decomposition/charge theorem.

## Statement and scope

For integer n>=2,m=n+1,N=nm and 0<=alpha<=2/5, beta=0, use the EXACT
corrected odd-board primitive S_n and the unchanged completed model
M_infty. Put p=sin alpha,a=(1+cos alpha)/2,tau=tan(alpha/2),h=pi/m.
There is an explicit finite continuous origin-sign background B_n and
nonnegative transported root excesses Y_r, defined below, such that

    S_n(alpha,0)=B_n(alpha)+ell_n p+Rcen(alpha)
                                      +(4/N)sum_(r=1)^(m-1)Y_r(alpha), (1)
    B_n(0)=S_n(0),
    ell_n=(nm)^(-1)sum_(k=1)^floor(n/2)cot(k*pi/n),
    0<=Rcen<=alpha^2/(3m).                              (2)

For the outer central root strip alpha<e_s<e*, e_s=sh,
e*=arccos(1-tau), let X_s=Y_(m-s) and let E(e) be the EXACT C01
excess J(p/2,a tan(e/2),e)-2a tan(e/2)log(sin e). Then

    |(4/N)sum_outer X_s-(2/(pi*m))sum_outer E(e_s)|
                                      <=(16/5)alpha/n.  (3)

The estimate is uniform through alpha comparable to m^-2 and all root
crossings; alpha=0 gives zero sums. It concerns quadrature in the FIRST
coordinate only. The remaining e-grid, inner strip and signed background
are NOT declared small. The complete cusp-aware upper

    [S_n-M_infty](alpha,0)-[S_n-M_infty](0)
       <=ell_n sin alpha+C alpha/n+K(1+log n)alpha^2/n    (4)

remains **OPEN**, as does full D13. Overall status of the supporting
theorem(1)--(3): **PROVED**, paper developer result, distinct audit needed.
No new onset, phase cover or numerical premise is asserted.

## Definitions, original labels and exact model match

The polynomial is D_n=sum_(i+j<=n)h_i h_j cos(iu)cos(jv),
Gpoly_n=D_n-cos(nu), h0=1,hi=2. Its exceptional (n,0) coefficient is
ONE. For delta_r=(1-r) mod2 set

    u_rk^0=(delta_r*pi+2k*pi)/n, u_rk=u_rk^0+alpha/n,
    v_r=r*pi/m, F_rk=(-1)^delta_r Gpoly_n(u_rk,v_r)/2,
    R_r=sum_(k=0)^(n-1)|F_rk|, S_n=N^-1 sum_(r=0)^(2m-1)R_r.

All F values at collisions are actual finite polynomial values. On beta=0,
R_(2m-r)=R_r without exchanging n,m. For1<=r<=m-1 define the FIXED mask

    D_r^0={k:cos u_rk^0<cos v_r},
    sigma_rk=sign F_rk(0)=+1 outside D_r^0, -1 inside D_r^0,
    B_r(alpha)=-sum_(k in D_r^0)F_rk(alpha),
    Y_r(alpha)=sum_k(-sigma_rk F_rk(alpha))_+,
    B_n(alpha)=1+(2n/m)a+(4/N)sum_(r=1)^(m-1)B_r(alpha). (5)

No reference value in these interior folded rows is zero: the only origin
zero row is r=m, and coprimality excludes the other cosine collisions.
Thus sigma is defined, and B_n is a finite smooth trigonometric function.
Y_r is continuous even at a root or a polynomial collision. This complete
folding retains ALL original rows, including the original fixed-six labels
{0,1,2m-2,2m-1,m-1,m}; none is discarded or replaced by a regularized pole.
The row r=0 and the zero row r=m are treated exactly in the proof.

The completed model is the SAME signed M_infty=B0 L^2+b_full L+C_infty,
L=log n. D10's accepted exact near decomposition is

    C_infty=E_infty+2cos(alpha/2)Hscalar(alpha)-c*a+E_c,
    E_c(alpha,0)=(2/pi^2)integral_0^(pi/2) E(e)de,         (6)

with its unchanged scalar Hscalar,c and E(e) above. This is the signed
integral, including e<alpha where the same-sign entropy formula applies.
Define M_nc=M_infty-E_c. Equations(1),(6) give the EXACT error identity

    E_n(alpha,0)-E_n(0)
       =[B_n(alpha)-B_n(0)-M_nc(alpha)+M_nc(0)]
          +ell_n p+Rcen+(4/N)sum_r Y_r-E_c(alpha,0).      (7)

This is a reduction of the requested COMPLETE error, not a model change.
Only the outer-strip portion of the last difference is bounded in(3).

## Dependencies and gate

PD-T216/220/226 supply normalization, zero mask, signed rows, exact central
row and positive collision values. N2 proves the same full row algebra;
its numerical receipts are NOT premises here. C01 central upper gives the
exact generic J/root correction and positive integral H on e>alpha.
D10-relative-constant supplies(6) for the actual completed C_infty.
Accepted E03-unified proves why the finite ell_n term must remain.
The complete unchanged registry baseline, fresh full immediate shortlist,
all candidate dispositions and limited literature coverage are recorded
in the companion idea. No external theorem or priority assertion is used.

## Proof

### 1. Fixed-origin signs remove a spurious collision jump

PD-T226 proves T_r=sum_k F_rk=na for1<=r<2m, R_0=n(m-a), and
R_m=na+2Z_m, Z_m=sum_k(-F_mk)_+. For each other folded row the finite
identity |F|=sigma F+2(-sigma F)_+ gives

    Z_r=sum_k(-F_rk)_+=B_r+Y_r.

Sum R_0,R_m and twice R_r for1<=r<m. This gives exactly
S_n=B_n+(2/N)Z_m+(4/N)sum_r Y_r. At alpha=0, Z_m=Y_r=0,
so B_n(0)=S_n(0).

To see the transport explicitly, let 0<v=v_r<pi, e=pi-v. On the actual
grid away from a collision,

    F=a[(1+cos v)-tau sin u]/(cos u-cos v).

Let D(alpha)={k:cos u_rk<cos v} and
I(alpha)={k:sin u_rk>(1+cos v)/tau}; I is empty when tau=0 or its
threshold is>=1. The natural negative-part split is
Z_r=-sum_D F+sum_I|F|. As alpha increases through e, exactly the sample
with original first label j=r-1 crosses the lower denominator boundary.
There is no positive-alpha upper-boundary crossing for alpha<=2/5:
the corresponding crossing phases are e and -e modulo2pi, and a shift
alpha/n<pi/n moves at most one such sample. For alpha>e this crossed
sample has F>0 and lies in I. Therefore the continuous fixed-mask excess is

    Y_r=sum_I|F|-1_(alpha>e) F_(j=r-1,r).               (8)

For the stated sign of the crossed sample, write e=s*pi/m. Its angle is
u=pi-(s*pi-alpha)/n. At alpha=e the numerator vanishes. For alpha>e,
tan(alpha/2)sin((s*pi-alpha)/n) increases: its logarithmic derivative is
1/sin alpha-cot((s*pi-alpha)/n)/n, positive since it is at least
1/sin alpha-1/(s*pi-alpha)>0. Thus the numerator is negative while
the denominator is negative; the complete F is positive. This checks
the transport sign without replacing its polynomial collision value.

At alpha=e both the open I and the open D exclude that point, while its
actual polynomial value is (n+cos v)/2>0. Equivalently use the fixed
mask(5), which requires no singular convention. The natural background
and natural positive sum have opposite jumps of that finite value;
(8) transports it instead of treating either jump as a small phase error.
No conclusion about the COMPLETE upper(4) follows from those artificial
jumps. In particular the full primitive is continuous.

### 2. Extract the exact central cusp with a uniform quadratic remainder

PD-T226's actual row formula is

    (2/N)Z_m=(p/N)sum_(k=1)^floor(n/2)
                                cot((k*pi-alpha/2)/n).

Subtract ell_n p. Cotangent is decreasing, so the difference is nonnegative.
All arguments lie in(0,pi/2], and sin x>=2x/pi. Since alpha/2<=1/5 and
pi>3, for every intervening argument

    csc^2 x <= [pi/(2(pi-1/5))]^2 n^2/k^2
                 <=(225/784)n^2/k^2 <n^2/(3k^2).

Integrating csc^2 over the argument shift alpha/(2n) and summing
sum_(k>=1)k^-2<2 gives

    0<=sum_k[cot((k*pi-alpha/2)/n)-cot(k*pi/n)]<=alpha n/3.

Multiplication by p/N<=alpha/N proves(2), including alpha=0.

### 3. The outer root-strip density matches the signed model exactly

For alpha<e<e*, write v=pi-e,c=cos e,s=a tan(e/2),u0=p/2.
Then s>u0 and the numerator-negative arc is

    I_e=(asin w,pi-asin w), w=(1-c)/tau<1.

Because e>alpha, tau<tan(e/2) and w>sin e, so I_e lies strictly
inside(0,pi-e), BEFORE the lower pole. No transport/collision occurs.
Define the periodic continuous function K_e on[0,2pi] by

    K_e(u)=a[tau sin u-(1-c)]/(cos u+c) for u in I_e,
    K_e(u)=0 otherwise.                                  (9)

It is nonnegative, zero at both arc endpoints, and X_s=sum_k K_(e_s)(u_rk)
for r=m-s in the outer strip. There are no separately unweighted pole
values in this formula.

The SAME generic cancellation integral in C01 obeys

    E(e)=J(u0,s,e)-2s log(sin e)=integral_0^(2pi)K_e(u)du. (10)

Here is a direct normalization check. Pair u with2pi-u in the continuous
two-channel expression. Their numerator absolute values exceed the
positive-numerator baseline by2[-F]_+, supported exactly on I_e. In the
generic J integral x=(u-v)/2, so dx=du/2; the resulting excess is precisely
the right side of(10). The separate-pole absolute coefficients have sum s
for s>u0, independent of u0, so their finite differences cancel under
equal pole cutoffs; no divergent integral is assigned a value. The baseline
is J(0,s,e)=2s log(sin e). I_e is compactly separated from the poles for
strict e>alpha, so the remaining integrand in this calculation is bounded.
This also follows by the moving-root formulas of N1/C01. Beyond e* both
sides of(10) vanish. Thus the row integral is the actual signed completed
constant excess, rather than the positive majorant on the inner strip.

### 4. Unimodality controls every first-coordinate mesh at once

Put b=tan(e/2),lambda=tau/b<1 and y=b tan(u/2). On the arc in(9),
0<y<1 and

    K_e/a=[lambda(1+b^2)y-b^2-y^2]/(1-y^2).

Its derivative has the sign of lambda(1+y^2)-2y. There is exactly one
critical point in(0,1), y=(1-sqrt(1-lambda^2))/lambda. Hence K_e is
unimodal and

    max K_e=a[cos e-sqrt(1-lambda^2)]/(1+cos e)
                   <=lambda^2 <=(256/225)alpha^2/e^2
                   <=(6/5)alpha^2/e^2.                  (11)

The middle inequalities use a<=1,0<=cos e<=1,
1-sqrt(1-lambda^2)<=lambda^2, tan(e/2)>=e/2 and
tau<=8alpha/15. On the strip the displayed maximum is positive; its
variation on the whole periodic circle is twice that maximum.

For ANY shifted n-point circle mesh, periodic centered-cell BV quadrature
therefore gives

    |n^-1 sum_k K_e(u_rk)-(2pi)^-1 integral K_e|
                                     <=(6/5)alpha^2/(n e^2). (12)

This includes the ACTUAL delta_r parity and alpha/n offset; no shift or
cell is replaced. All n cells tile the circle, so there are no omitted
first-coordinate cells in(12).

For x=alpha/h, the elementary tail bound
sum_(s>x)s^-2<=2/max(1,x) gives, in BOTH regimes x<=1 and x>=1,

    (alpha^2/m)sum_(sh>alpha)(sh)^-2 <=2alpha/pi.         (13)

One may enlarge the strip to this full positive tail. Multiply(12) by
4/m and sum over the actual outer-strip rows; use(10),(13). The error is
at most48alpha/(5pi n)<=(16/5)alpha/n. This proves(3), including an empty
strip and the microscopic alpha~m^-2 range without a scan or asymptotic.

### 5. Preserve the remaining signed second-coordinate boundary

For e>=alpha, C01 gives E(e)=H(u0,a tan(e/2),e), decreasing in BOTH
arguments; it is nonnegative and decreasing with e, then zero beyond e*.
Set k0=floor(alpha/h)+1,theta=alpha-h floor(alpha/h). A right-endpoint
sum for a decreasing function gives the exact one-sided bound

    h sum_(s>=k0)E(sh)-integral_alpha^infinity E(e)de
                                      <=theta E(k0h).   (14)

Indeed the first rectangle has length h, the interval from alpha to k0h
has length h-theta, and the remaining right rectangles lie below their
integrals. At a mesh-aligned alpha the boundary charge is zero. The
corresponding normalized charge in(7) is (2/pi^2)theta E(k0h), not an
uncharged endpoint value. Its control must retain the inner strip and
the signed background in(7). Taking an additional absolute estimate
can restore a logarithmic phase loss; none is suppressed here.

## Remaining obligation, checks and history

The exact target after this partial reduction is to bound the bracketed
background in(7) together with the inner e<=alpha positive parts, the
SIGNED inner integral in(6), and boundary(14). The finite polynomial
collision transport(8) is essential there. The estimates above do not
prove that this remainder fits C alpha/n+K H alpha^2/n, and do not
refute that family. The complete microscopic result of the separate
2D helper is not a premise of this theorem.

Paper only: bounded complete reads/searches and cryptographic metadata,
then exact algebra and written inequalities. No scripts, source edits,
scientific import, scalar/endpoint/phase/degree/threshold/native/compile/
pack/shared/Git action. Only the three assigned E05 paper records are
written. The accepted E02/E03 files remain frozen. Independent proof
audit and root adoption are required; no global onset/coverage change.

2026-11-07, Codex mathematical developer, parent-requested Sol xhigh;
actual serving metadata unavailable. Rules baseline017f8ec, unchanged
complete registry authenticated as in the idea record. One E05 component,
not a new round per identity. Root owns shared registration and release.


## Root adoption —2026-11-07

Root adopts the exact frozen 12863-byte proof (SHA256 27c706d57536f2410922629a52ed6d3988aa8a84f8d0b6be6a785e6eea1bf6bc) after the distinct independent ACCEPT in [independent-checks-E05-axis-central-excess.md](../independent-checks-E05-axis-central-excess.md). Original proof bytes above are preserved. The opening pending-adoption wording is historical. Final Claude audit remains separate; no new numerical or source job was run.
