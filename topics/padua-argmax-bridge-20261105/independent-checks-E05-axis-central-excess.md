# Independent E05 alpha-axis central-excess audit

2026-11-07. Distinct reviewer `/root/d29_floor_review`, requested Astra high;
actual serving metadata is unexposed. This component review owns ONLY
this report. Root controls publication/adoption. Pack remains PAUSED.

## Verdict and frozen scope

**ACCEPT** the frozen supporting theorem: the exact collision-safe finite
axis decomposition, its central cusp remainder, the outer-root-strip
first-coordinate quadrature bound, and the explicitly retained one-sided
second-coordinate boundary. No unresolved mathematical finding or author
correction remains. The complete cusp-aware upper and full D13 remain
OPEN; neither follows from these component estimates.

| Frozen input | Bytes | SHA256 |
|---|---:|---|
| theory/E05-axis-central-excess.md |12863|27c706d57536f2410922629a52ed6d3988aa8a84f8d0b6be6a785e6eea1bf6bc|
| ideas/E05-axis-central-excess.md |5784|75f8db12812f7058b67aa4bad1f4721f34cf2c7bc9547f8ae242dfa57edab43e|
| attempts/E05-axis-central-excess.md |2488|6a9766f547066ba677e60b14615fef738fefd1ff53d43127d20095988cdc87fb|

All three files were read completely and their hashes/lengths checked.
For EVERY integer n>=2, m=n+1, N=nm, beta=0 and0<=alpha<=2/5,
with p=sin alpha and the original corrected primitive, the accepted result is

```
S_n(alpha,0)=B_n(alpha)+ell_n*p+Rcen(alpha)
                       +(4/N)*sum_(r=1)^(m-1)Y_r(alpha),
B_n(0)=S_n(0),
ell_n=(1/N)*sum_(k=1)^floor(n/2)cot(k*pi/n),
0<=Rcen(alpha)<=alpha^2/(3m).
```

For the ACTUAL outer-strip rows alpha<e_s=s*pi/m<e*,
e*=arccos(1-tan(alpha/2)), X_s=Y_(m-s), and the signed completed-model
excess E(e) defined in the source, the further accepted estimate is

```
abs((4/N)*sum_outer X_s-(2/(pi*m))*sum_outer E(e_s))
 <=16*alpha/(5n).
```

This is a uniform first-coordinate quadrature estimate, including
alpha comparable to m^-2. It is not a bound on the complete remaining
two-coordinate error. The exact second-coordinate upper retains
(2/pi^2)*theta*E(k0*h), with h=pi/m,
k0=floor(alpha/h)+1 and theta=alpha-h*floor(alpha/h).
No uniform small bound on this last expression is accepted here.

## Gate, predecessors and limits of reuse

Read the current E05 LOG authorization and the complete new theory,
idea and attempt. The unchanged fully read rule baseline and complete
registry gate from the immediate E02/E03/E04 audits are reused; the
registry was again hashed at
d7ec3aa6cf36f72e8057bcb90d8ac6eae8bf285a5b17f12526b26472ff4bddef.
This reuses every registry/obstruction/disposition row already read,
rather than representing a search result as a new complete gate.
The fresh shortlist concerns origin-sign masks, positive root strips,
finite cotangent rows, collision values and the model's signed excess.

Read PD-T226's full exact axis-row theorem and proof, N2's complete
finite two-phase row algebra, C01-near-central-upper in full, and
D10-relative-constant in full. PD-T220 and the full E03-unified
obstruction were completely read in the immediately preceding audit
blocks and are reused at their stated fixed-degree scope. The latter's
accepted negative conclusion remains intact: dropping the logarithmic
linear cusp cannot be justified by fixed-phase cancellation. E04's
wide retained-origin estimate is not a premise and was not re-audited.
Old numerical receipts mentioned in N2/PD-T226 are not proof premises.

This is a quantitative continuation of the existing exact row/central
root mechanism, not a new kernel or a priority claim. The natural
untransported positive sum's artificial discontinuity is preserved as
the reason that particular absolute comparison was abandoned. It is
not promoted to a refutation of a complete one-sided cusp-aware bound.
The signed background, inner strip and second-coordinate coupling
remain the precise unresolved objects. No source, computational or
whole-domain conclusion is inherited from this paper component.

## Finite rows, fixed masks and true origin

The kernel is exactly G=D-cos(nu), exceptional top x coefficient ONE,
with signed F=(-1)^delta G/2, n first-coordinate residues per row and
normalization1/(nm). The unequal n,m meshes and original periodic
representation of physical endpoint half weights are unchanged.
At beta0, reflection of the second row gives R_(2m-r)=R_r with no
coordinate swap. Rows0,m occur once, and each1<=r<m occurs twice.

At the origin in1<=r<m, the full numerator is strictly positive and
coprimality excludes a cosine collision; thus no reference F is zero.
Its sign is precisely positive outside D_r^0 and negative inside it.
For a sample with positive origin sign, Y contributes(-F)_+ and B
contributes0. For a negative-origin-sign sample, B contributes-F and
Y contributes F_+, so B+Y=(-F)_+ again. Consequently Z_r=B_r+Y_r
is exact for every phase, including actual polynomial collisions.
B_n is a finite smooth trigonometric function and Y_r is continuous.

The inherited signed rows are T_r=na for r!=0, and the endpoint row
has R_0=n(m-a). Summing R_0,R_m=na+2Z_m and twice every interior
folded row gives exactly

```
S_n=1+(2n/m)*a+(2/N)*Z_m+(4/N)*sum_(r=1)^(m-1)Z_r.
```

Substituting B_r+Y_r proves the stated B_n formula and decomposition.
At alpha0 every Y_r is zero and Z_m=0; hence B_n(0) is the SAME
finite S_n(0), not a completed-model limit. All original fixed-six
labels are included, though this proof folds them differently. There
is no omitted central row or additional endpoint-weight factor.

## Collision transport and the actual jump

For a regular sample, sign(F) is determined by the denominator mask D
and numerator mask I, so Z_r=-sum_D F+sum_I|F|. On positive alpha
up to2/5 the lower denominator boundary is crossed at alpha=e=pi-v
by exactly j=r-1: solving ((r-1)pi+alpha)/n=v gives that phase.
The opposite boundary crossing lies at-e modulo2pi; it is outside
this positive interval. Subsequent crossings are separated by2pi in
phase. Thus there is at most one transported sample in each row.

For alpha>e the crossed sample has u>v and denominator negative.
Writing e=s*pi/m and u=pi-(s*pi-alpha)/n, its numerator becomes
negative just after the collision and remains negative on the stated
interval. The proposed derivative check is valid: the logarithmic
derivative of tan(alpha/2)*sin((s*pi-alpha)/n) is
1/sin alpha-cot((s*pi-alpha)/n)/n, bounded below by
1/sin alpha-1/(s*pi-alpha)>0, since s>=1 and alpha<=2/5.
The sine argument here stays positive and below pi. Thus the complete
F is positive and belongs to I after crossing.

The fixed mask did not include this point originally, so subtracting
the new denominator-mask contribution requires exactly

```
Y_r=sum_I|F|-1_(alpha>e)*F_(j=r-1,r).
```

At alpha=e the open masks both omit the point; the polynomial value
is (n+cos v)/2>0, as proved in PD-T226. Its fixed-origin Y contribution
is zero. The natural background jumps downward by this finite value
and the natural positive sum jumps upward by the same value. The
transport formula and fixed-mask definition therefore agree at and
on both sides of the collision. No zero-times-pole substitution or
suppression of an O(n) sample value occurs. The natural pieces need
not themselves be continuous; the finite primitive and the chosen
fixed-mask split are continuous.

## Central cusp and all-n quadratic remainder

PD-T226 gives exactly

```
(2/N)*Z_m=(p/N)*sum_(k=1)^floor(n/2)
                       cot((k*pi-alpha/2)/n).
```

Its central zero mask, floor(n/2), and both parities are retained.
Subtracting ell_n*p produces a nonnegative remainder, because each
shifted cotangent argument decreases within(0,pi/2]. For every
intermediate argument x,

```
csc^2 x <= [pi/(2*(pi-1/5))]^2*n^2/k^2
         <=(225/784)*n^2/k^2 <n^2/(3k^2).
```

The first bound uses sin x>=2x/pi; the second follows from pi>3
and monotonicity of pi/(pi-1/5). Integrating over the actual shift
alpha/(2n) and using sum_(k>=1)k^-2<2 yields a cotangent-difference
sum at most alpha*n/3. Multiplication by p/N<=alpha/N proves
Rcen<=alpha^2/(3m). This includes n2, where ell_2=0; positivity of
ell_n at larger n is not an unspoken n2 premise. At alpha0 the linked
formula gives zero remainder. The estimate is uniform in phase and
degree, rather than an extrapolation from a fixed-degree derivative.

## Exact outer-strip root density and model normalization

Put b=tan(e/2), tau=tan(alpha/2), c=cos e, and u0=a*tau=p/2.
In the strict outer strip alpha<e<e*, one has b>tau and
w=(1-c)/tau in(0,1). Moreover w>sin e since b>tau. The root arc
(asin w,pi-asin w) is therefore strictly between e and pi-e,
and before the lower pole v=pi-e. Its numerator-negative part has
positive denominator, so it contributes precisely the nonnegative
K_e in(9). There is no crossed sample or transport term on this
strip. The equality X_s=sum_k K_e(u_rk) uses the actual parity grid
and offset alpha/n. Beyond e* the numerator-negative arc is empty;
at e* it shrinks to a zero-valued endpoint.

The normalization of integral K_e=E(e) is essential and checks
independently against C01's positive integral. One direct check fixes
a and e, temporarily varies tau, and sets b=tan(e/2). For
1-c<tau<b, differentiating integral K_e is legitimate on its compact
root arc: the boundary values vanish and it stays away from the poles.
Writing d=sqrt(1-((1-c)/tau)^2), this derivative is

```
a*log((c+d)/(c-d)).
```

C01 gives E=H(a*tau,a*b,e) in this coefficient-sign regime, with
H=2*integral_e^(pi/2)sqrt((a^2*tau^2-a^2*b^2*sin^2 t)_+)/sin t dt.
Its derivative with respect to tau is the same expression, by the
substitution y=cos t. Both quantities vanish at tau=1-c, where the
root interval closes. This verifies their equality, including the
normalizing factor, without assigning any divergent pole integral
a separate value. It agrees with the source's paired-channel/dx=du/2
derivation. Continuity gives the zero endpoint; on e>alpha the identity
is equality with the signed model excess, not merely the C01 majorant
used on s<u0.

D10's exact near decomposition applies because alpha<=2/5<1/2.
On beta0 its two central channels are identical, so
E_c=(2/pi^2)*integral_0^(pi/2)E(e)de. At alpha0, E_c=0. Accordingly
the model subtraction in(7) has exactly the displayed sign, background
M_nc=M_infty-E_c, and true origin. The inner e<alpha integral is
still the signed same-sign expression. It is not replaced by the
positive outer density or its positive majorant.

## Unimodality and first-coordinate error, including microscopic phases

With lambda=tau/b<1 and y=b*tan(u/2), the support lies in0<y<1.
The rational expression for K_e/a in(11) differentiates with sign
lambda*(1+y^2)-2y. This has a single zero in(0,1), giving an increasing
then decreasing positive arc with zero endpoints. Its exact maximum is

```
a*(cos e-sqrt(1-lambda^2))/(1+cos e).
```

Here e*<pi/2, so0<cos e<=1. The maximum is at most lambda^2.
The estimates tan(e/2)>=e/2 and tan(alpha/2)<=8alpha/15 give
lambda^2<=(256/225)*alpha^2/e^2<=(6/5)*alpha^2/e^2. The latter
tangent bound follows on alpha/2<=1/5, for example from sin x<=x
and cos x>=49/50. No inverse root/pole separation is dropped in this
step. The whole periodic function has variation exactly twice its
maximum, even when the strip becomes arbitrarily narrow.

For any shifted n-point circle mesh, centered cells have normalized
point-versus-uniform discrepancy at most1/(2n). Pairing this with
the total variation gives an error at most Var(K_e)/(2n)=max(K_e)/n.
Equivalently each half cell's integration weight is at most half the
cell length, and all cell variations sum to the periodic variation.
This proves(12) with its factor6/5. Every first-coordinate cell and
actual offset remains included; the inequality needs no grid alignment
or root separation measured in mesh units.

For x=alpha/h, sum_(s>x)s^-2<=2/max(1,x): the x<=1 case uses the
full sum<2, and for x>=1 the integral tail starting at floor x gives
at most1/floor x<=2/x. Consequently

```
(alpha^2/m)*sum_(sh>alpha)(sh)^-2 <=2alpha/pi
```

in BOTH x<=1 and x>=1 regimes. The alpha0 case is handled directly,
with an empty root strip. Enlarging the actual outer-strip indices
to this positive tail is legitimate. Multiplying the row error by4/m
gives48alpha/(5*pi*n)<=16alpha/(5n), using pi>3.
The integral coefficient is exactly
(4/m)*(1/(2pi))*E=2E/(pi*m). Thus the folded-row factor, circle
normalization and model coefficient all match. No asymptotic inference
or finite-degree scan is needed at alpha of order m^-2 or smaller.

## Remaining second-coordinate boundary and acceptance limits

For e>=alpha, the C01 equality E=H applies, including s=u0 at the
boundary by continuity. H decreases separately in s and e, and
s=a*tan(e/2) increases with e. Hence E(e) is nonnegative decreasing
until e*, then zero. In expressions extending the e integral or grid
to infinity, this is its zero extension beyond e*, not a new periodic
logarithm branch. All nonzero rows still belong to the actual finite
folded set, since e*<pi/2.

The interval from alpha to k0*h has length h-theta. Its integral is
at least(h-theta)*E(k0*h); each subsequent right rectangle lies below
its own integral. The first rectangle has length h, so exactly

```
h*sum_(s>=k0)E(s*h)-integral_alpha^infinity E(e)de
 <=theta*E(k0*h).
```

Multiplication by2/pi^2 yields the normalized boundary charge in
the complete error identity. At mesh-aligned alpha, theta0 and the
upper is zero. For other phases it has not been bounded by C*alpha/n
or a quadratic budget. This is a one-sided statement, not an absolute
second-coordinate error estimate. The unresolved signed background,
inner-strip finite excess and signed inner model integral must remain
coupled with this boundary if a complete upper is to be proved.

The result stays on beta0 and0<=alpha<=2/5. No signed-phase extension,
two-dimensional zero-mask assertion, full cusp-aware upper, D13
closure, defect comparison, onset or new finite certificate is accepted.
The complementary E05 two-dimensional helper is not a premise.
Final Claude audit and root adoption remain separate obligations.

## Activity and preservation

Only paper reasoning and exact hand algebra were used. Tools performed
read-only file reads, searches, byte counts and cryptographic metadata
checks; the only write is this report. No script, scalar/endpoint
preview, source import, native/compiler/control/phase/degree job, pack
work, remote execution, Git operation, author edit or shared-record
edit occurred. The first frozen candidate passed without a requested
correction. Its explicitly failed/deferred natural split and complete
OPEN target are preserved, not silently promoted into accepted bounds.
