# C03 ratio tightness — independent mathematical check

2026-11-06. Rules/input `b6e67b3c78cb668b6d2f9da5a5560537d2960bf3`.
Distinct reviewer: Codex, assigned Astra high; serving metadata unexposed.
Frozen proof `theory/C03-ratio-tightness.md`,12946 bytes, SHA256
`8634fc469f18a9555032c140b9969a56a74c53dea388cadd54c29ed2b3e83a01`.
**ACCEPTED within its mathematical enclosure scope; no unresolved finding.**
Formal Claude audit, source conformance and full-candidate acceptance are
separate. No author proof or old record was changed.

This check reconstructs the new monotonicity step and its endpoint, sign,
Taylor and ODE consequences against the accepted C01 ratio specification.
The candidate is an internal tightness/backend variant. Historical
novelty/priority and a full registry/literature audit are excluded; no new
mathematical mechanism or complexity claim is supplied by this report.

## Monotonicity through the first numerator zero

Set F_k(r)=R_k(r), x=kr and b_k=min(3/2,4/k). The finite cosine polynomial
is even and has F_k(0)=k,F'_k(0)=0. For k1 it is identically1. Assume k>=2
and0<r<=b_k, so0<r<pi/2, sin r>0,cos r>0 and x<=4.

For f(t)=t*cot(t), the sign of f'(t) on(0,pi) is the sign of
sin t*cos t-t. That numerator starts at0 and has derivative
-2sin²t, hence is strictly negative thereafter. Thus f is strictly
decreasing from its continuous value1. If x<pi, then r<x and F_k(r)>0,
so F'_k(r)=F_k(r)[f(x)-f(r)]/r<0.

At x=pi this logarithmic-derivative expression is unusable. Directly
differentiating the uncancelled quotient gives F'_k(r)=-k/sin r<0.
This explicitly covers the numerator zero without dividing by F or sin x.

For pi<x<=4, write y=x-pi. Since pi>3,0<y<pi/3. Therefore cot y>1/sqrt3
and f(x)=x*cot y>pi/sqrt3>1>=f(r). Here F_k(r)<0 because4<3pi/2.
The same derivative identity away from its zero now has a negative
factor F and positive difference, so again F'_k(r)<0. These three
cases cover the entire admitted chart. The assertion is strict away
from r0 and does not extend globally; e.g.R3 increases at r2.

## Folded range, parity and actual endpoint guards

For any real interval A, its absolute-value image is exactly
[rho_min,rho_max]. Continuous strict decrease on[0,b_k] therefore gives
the exact image[F_k(rho_max),F_k(rho_min)]. This includes intervals
crossing0, where the upper value is k, and intervals past the numerator
zero, where both endpoint values can be negative.

Translation by an exact integer ell*pi multiplies value and derivative
by eps=(-1)^(ell*(k-1)). Negative odd ell obeys the same parity rule;
no product of potentially large signed integers is necessary. With an
outward residual A=Z-ell*Pi, interval inflation may enlarge the residual
set but never invalidate this translation identity for each true point.

The implementation must apply the chart test to the actual outward
residual and to the **extracted outward dyadic endpoints** l,u. If
0<=l<=rho_min<=rho_max<=u and u<=1.5,k*u<=4, monotonicity shows that
[lower(E_u),upper(E_l)] encloses the true folded image. Multiplying by
eps reverses endpoint order when eps=-1. l0 supplies exact value k;
all other point evaluations keep their C01 remainder and roundoff.
If extracting or inflating a nominal boundary causes a guard failure,
rejecting the optional endpoint candidate is correct.

F' is odd. Thus nonnegative residuals have F'<=0, nonpositive residuals
have F'>=0, and an exact zero residual has F'=0. Multiplication by eps
gives the stated derivative half-cap candidates. Crossing0 supplies no
one-sided sign. No sign assumption on F itself enters this step.

The base point evaluator is explicitly nonrecursive: at most two endpoint
values are requested, fewer at l0 or equal endpoints. Using a C01 point
pair when only its value is required costs extra fixed work but does not
alter validity or reintroduce a degree-growing loop.

## Centered and ODE candidates

The closed global cap C2=k(k²-1)/3 follows from the sum of squared
frequencies already reconstructed for C01. For an exact dyadic center c,
outward T=Z-c and H>=sup|T|, integrating the second derivative gives

    R(Z) subset Vc+Dc*T+[-C2*H²/2,C2*H²/2],
    R'(Z) subset Dc+[-C2*H,C2*H].

The interval product Dc*T retains the uncertain center derivative.
The center can be an exact stored proposal rather than the ideal
midpoint, provided T,H are actually recomputed. With global C2 it may
even lie outside Z. A rounded center with an unadjusted half-width
would not meet this contract. k1 returns the exact constant pair.

Twice differentiating sin z*R_k(z)=sin(kz) yields

    R''_k=(1-k²)R_k-2cot z*R'_k

where sin z is nonzero. If J contains Z,c and the paths between them,
validated enclosures V_J,D_J and a sine-separated cotangent enclose this
right side throughout J. Its absolute upper bound and C2 are both
curvature upper bounds, so their minimum is valid. In a real interval
ball its exact ARF midpoint lies inside the ball, permitting J=Z.
If c were external, a curvature bound only on Z would be insufficient;
the specification explicitly requires the larger hull. Sine-zero or
nonfinite ODE candidates must revert to global C2, without dividing
through a removable zero in the differential equation.

## Staging, cost and scope

Each optional value/derivative pair encloses the same true images, so
finite intersections preserve correctness. An empty finite intersection
is an inconsistency, not a width improvement. A nonfinite optional pair
leaves the finite old pair unchanged. A value-only refinement can safely
carry the old derivative through staging, and conversely for sign-only
refinement. Successful quotient evaluation must not bypass these optional
near-pole refinements if the intended tightening is to be exercised.

At fixed precision/order the candidates add at most two endpoint base
evaluations, one centered base evaluation and one curvature sin/cos call
to the original base interval evaluation. Exact integer and argument
reduction costs remain explicit. No k-term harmonic, polynomial recurrence
or repeated center refinement is required. Finite ball conversion can
slightly enlarge an exact intersection, so the specification properly
distinguishes enclosure validity from literal exported-width monotonicity.

The separate [prototype review](independent-checks-C03-prototype.md)
records executable controls, including negative lobes, parity, exact and
crossed poles, guard rejection and all three modes. These finite controls
supplement the analytic argument; they are not its premise. Sharp ratio
images do not guarantee acceptance of a whole primitive, orbit or tree.
The failed C02 full replay remains preserved, and no full replay or new
degree is approved by this mathematical report.
