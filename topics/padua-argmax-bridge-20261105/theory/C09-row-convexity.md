# C09 — coefficient-vertex whole-box upper bounds with buffered collisions

Rules 4b728b0; 2026-11-06. Coordinator-seeded technical convex-relaxation
variant of N2/C02/C06, not a new convexity theorem or historical novelty
claim. Prospective gate and live PR28 registry refresh:
[ideas/C09-row-convexity.md](../ideas/C09-row-convexity.md).

**PROVED analytic enclosure/operation-count contract; distinct review
pending.** No backend, finite-board test, speed measurement, successful
leaf or cover is a premise. The conclusion concerns a whole-box S UPPER
bound. It is neither an exact nonzero-width row representation nor a
corner-orbit cancellation/defect theorem.

## 1. Domain and main conclusion

Use n>=2, m=n+1, N=nm, the fixed row/grid labels and closed phase set
P=B intersect {alpha+beta<=pi}, B a rectangle in [0,pi]^2, from C08.
Keep lambda=(delta+alpha/pi)/2 without fractional relabeling, where
delta=(1-r) mod 2. Thus

    u_k=2pi*(k+lambda)/n, v=(r*pi+beta)/m,
    F_rk=(-1)^delta G_n(u_k,v)/2,
    S=(1/N)*sum_(r,k)|F_rk|.

Retain rows {0,2m-1,m-1,m} by n actual finite-primitive interval
evaluations each, with full enclosures. In every other row:

* retain at most eight actual grid samples near a possible denominator
  collision or the angular seam, before any coefficient relaxation;
* relax the two numerator coefficients into a rectangle and evaluate
  at most four vertex rows on all remaining indices;
* evaluate each vertex row with at most 12 fixed cotangent blocks per
  channel and at most three additional regular vertex samples.

Under the literal root/backend guards below, this yields a valid S(P)
upper using O(n) scalar operations at fixed backend orders/precision.
There is no factor proportional to the numerator-root motion over P.
If a guard fails, a proved finite actual-row cap can replace that entire
row in O(1) arithmetic. Thus total valid upper construction can retain
O(n) scalar work even on rejected analytic branches; useful tightness is
not guaranteed. Input integer bit lengths and exact-rational/backend
precision costs are counted separately, as in C02/C06.

The intrinsic coefficient-relaxation excess has the explicit bound

    0<=M(phi)-S(phi)<=(2/pi)*Delta_* H_n^2,
    Delta_*=max_r [width(c_rectangle_r)+width(p_rectangle)], (1)

for each phi=(alpha,beta) in P, where M is the exact-real relaxed
majorant defined below. Interval propagation over a nonzero-width P
and numerical/tail radii add further width beyond (1). A final computed
box upper is not asserted to be within (1) of sup_P S.

## 2. Remove and buffer actual denominator collisions first

For each ordinary row the two real-index pole locations have the closed
whole-box enclosures I_1,I_2 from C08:

    d_1=(n*v-alpha-delta*pi)/(2pi),
    d_2=(n*(2pi-v)-alpha-delta*pi)/(2pi).               (2)

Their exact width is d_D=(w_alpha+(n/m)w_beta)/(2pi)<1. Require the
ACTUAL outward intervals used in this construction to have width<1.
Replace I_j=[l_j,u_j] by its one-grid-unit buffer [l_j-1,u_j+1].
Let D_r be every integer k in these two closed buffered bands, clipped
to0,...,n-1, together with k=0,n-1. Merge duplicates. Each buffered
interval has width<3 and contains at most three integers, hence

    |D_r|<=min(n,8).                                  (3)

Let K_r={0,...,n-1} outside D_r. These sets are fixed for the whole
phase box. Evaluate every k in D_r using the ACTUAL finite primitive,
including full absolute-value, series and outward arithmetic radii.

For k in K_r, both cotangent channel coordinates have uniform pole
clearance of at least one grid unit:

    y_-(k)=(k+lambda-n*v/(2pi)) mod n,
    y_+(k)=(k+lambda+n*v/(2pi)) mod n,
    1<=y_-(k),y_+(k)<=n-1.                            (4)

To prove this, an ordinary row has v in (0,2pi), while lambda is in[0,1].
Thus each d_j is in(-1,n). The central pole image is more than one
unit away from a remaining k by the closed buffered deletion. Other
periodic images d_j+ell*n are also more than one unit away: k=0,n-1
were removed, so1<=k<=n-2, and all noncentral relevant images lie
below0 or above n-1. Images farther by another period are harmless.
This proves (4) for both channels and all phases. In particular
cos u_k-cos v never vanishes on K_r.

This order is essential. A relaxed coefficient vertex will generally
destroy the numerator cancellation at a removable collision. For example
n=3,r=1,k=0,alpha=3pi/4,beta=0 has u=v=pi/4 and actual coefficients
c=1/2,p=sqrt(2)/2, whose numerator vanishes. The complete F value is
(3+sqrt(2)/2)/2. The allowed coarse coefficient rectangle[0,1]^2 has
vertex(c0,p0)=(1,0), whose rational numerator does not vanish there.
Using that relaxed quotient at the collision would be infinite, not a
finite-polynomial enclosure. No such term is relaxed in this method.

## 3. Four coefficient vertices, with the denominator kept correlated

Write the actual N2 coefficients in row r as

    p=sin alpha,
    c=(cos alpha+cos beta)*(1+cos v)+sin beta*sin v.

Choose a closed rectangle C_r times P0 containing every actual(c,p)
over the phase set. Its endpoints must be exact chosen real numbers
(exact dyadics are convenient), not uncertain balls treated as point
vertices. Valid enclosure balls can be expanded to their exact outward
endpoints. Intersect with the known ranges c in[-5,5], p in[0,1]
before choosing endpoints. These ranges follow from |cos alpha+cos beta|
<=2, |1+cos v|<=2 and |sin beta*sin v|<=1. An empty purported valid
intersection is an error. Degenerate/duplicate vertices are merged.

For a FIXED actual phase phi, and arbitrary coefficients c0,p0, define

    H_r(c0,p0;phi)=sum_(k in K_r)
             |c0-p0*sin u_k(phi)|/[2|cos u_k(phi)-cos v(phi)|]. (5)

Every denominator in (5) is strictly positive after absolute value.
For fixed phi each summand is the absolute value of an affine function
of(c0,p0), times a fixed positive weight. Therefore H_r is convex in
the TWO coefficient variables. Express the actual coefficient pair as
a convex combination of the at most four rectangle vertices V_r to get

    H_r(c(phi),p(phi);phi)<=max_(z in V_r) H_r(z;phi).    (6)

The denominator/grid variables in (6) remain at the same actual phi.
No independence of c,p,u,v is assumed; enlarging their actual coefficient
image to a rectangle is the relaxation. Taking a whole-box bound of each
vertex side is a subsequent operation, not a convexity assertion in v.

At every actual phase the ordinary row consequently satisfies

    R_r(phi)<=sum_(k in D_r)|F_rk(phi)|
                              +max_(z in V_r) H_r(z;phi). (7)

This gives four vertices rather than the coordinator's generic
three-coefficient/eight-vertex seed, because the actual numerator has
only the two terms c-p*sin u. No sign family is restricted without proof.

## 4. Fixed vertex roots and bounded ambiguous work

For one vertex(c0,p0), p0>=0 by construction. If p0=0, its numerator
is constant; c0=0 gives exactly H=0. If p0>0 and |c0|>p0 it has no
numerator root. If |c0|<=p0, the roots in[0,2pi] are in the three
fixed angular alternatives

    theta=asin(c0/p0),      pi-theta,      theta+2pi.   (8)

The comparisons and ratio can be performed in exact rational arithmetic
when vertex endpoints are dyadic; tangent cases c0=+/-p0 use their
exact pi/2 multiples. These angular roots are independent of the phase
box variables. Their index bands vary only through lambda:

    t=(n*theta-alpha-delta*pi)/(2pi).                 (9)

With exact angular roots their width is w_alpha/(2pi)<=1/2. Validated
root arithmetic may enlarge this; literally require each retained actual
outward band to have width<1. For example an angular enclosure of width
less than pi/n leaves room for this guard, before other arithmetic
inflation. A rounded root alone is not a proof. Near a tangent the
arithmetic may require more precision, but there is no moving-coefficient
root sweep. Bounded fixed-precision failure is handled by row fallback.

Put every integer in these three closed vertex numerator bands, excluding
D_r, into E_(r,z). It has at most three members. At these regular
indices evaluate the RELAXED rational vertex function with its validated
nonzero denominator (or its equivalent cotangent form below), then take
absolute value. They are not actual F values unless the vertex happens
to equal the actual coefficients. Root-band equality points must be
included. An empty-integer band still inserts a cut at ceil(lower), as
in C08, so two opposite signs are not merged across an inter-grid root.

There are at most seven band components: two buffered denominator bands,
two seam singleton bands and three numerator bands. Their complement,
including empty-band cuts, has at most eight fixed integer cores. On
each core the vertex numerator and actual denominator have constant
strict signs over the connected real-index times phase domain. Certify
those signs at one parameter/index point using validated arithmetic.
An unresolved sign is failure, except a numerator proved identically
zero. Both cotangent wraps are constant because their pole indices are
already in the buffered denominator bands.

For a core k=a,...,b use the exact wrap ell and whole-box affine offset

    y=a+lambda +/- n*v/(2pi)-n*ell,
    qcount=b-a+1.                                     (10)

Check C06's literal whole-ball guards0<y and y+qcount-1<n. The exact
geometry has the stronger margin (4); outward arithmetic still must
certify the actual supplied ball. Successful C06 calls enclose the full
core sums over all phases. At most12 blocks/channel is conservative.
No q-sized inner loop or individual core sample scan is needed.

## 5. The relaxed cotangent coefficients and assembly

For arbitrary fixed(c0,p0), elementary addition identities give

    f_z(u,v)=[c0-p0*sin u]/[2(cos u-cos v)]
       =C_z(v)*cot((u-v)/2)+D_z(v)*cot((u+v)/2),
    C_z=(p0-c0/sin v)/4,
    D_z=(p0+c0/sin v)/4.                              (11)

Indeed sin u/(cos u-cos v)=-(cot((u-v)/2)+cot((u+v)/2))/2 and the
analogous sin v identity has their difference. Ordinary v avoids every
multiple of pi because the four special rows were retained; hence all
coefficients in (11) are finite throughout the phase box.

The old original signed row T_r MUST NOT be reused for these artificial
vertices. It follows from phase-specific Fourier identities that the
relaxed coefficients need not satisfy. Instead, for each vertex core
take its fixed sign s in{-1,1}, and evaluate

    s*[C_z*Qminus_core+D_z*Qplus_core].                (12)

This equals the sum of absolute vertex terms on that core. Sum (12)
over ALL its positive and negative cores, then add the absolute vertex
terms on E_(r,z). This gives a full interval enclosure J_(r,z) of
H_r(z;P). No actual finite primitive is substituted for a relaxed
vertex term. All C06, coefficient and regular rational radii remain.

Let U_Dr be the sum of upper absolute bounds of the actual finite
primitive on D_r. Define

    U_r=U_Dr+max_(z in V_r) upper(J_(r,z)).             (13)

Together with the four retained actual row uppers, sum (13) and divide
by N to obtain U>=sup_P S. Clamp each actual row upper by the proved
coarse n*N if useful. At a numerical failure, one cannot drop the failed
vertex from the maximum. Replace the entire actual row upper by n*N,
or use another independently proved complete row bound. Likewise an
unresolved coefficient rectangle or band guard never licenses selecting
only convenient vertices. The unconditional bound S<=2N is available.

For fixed backend orders the ordinary-row work is bounded by eight actual
primitive evaluations, at most four times three regular vertex terms,
and at most four times24 C06 calls, plus bounded root/interval arithmetic.
There are2m-4 ordinary rows and4n retained evaluations. This proves O(n)
scalar work. The constant may be expensive: no measured cheapness,
accepted-leaf count or cover-time improvement follows. C06's fixed-order
rational moment computation is included; bit complexity is not constant.
Fixed precision, degree ceiling and return-code checks remain mandatory.

## 6. Uniform intrinsic relaxation loss from the buffer

For a fixed phi, let A_r(phi)=sum_(k in K_r)1/|cos u_k-cos v|.
Every vertex differs from the actual coefficients by at most the full
rectangle widths. The reverse triangle inequality in (5) gives

    0<=max_z H_r(z;phi)-H_r(c(phi),p(phi);phi)
                 <=(Delta_c,r+Delta_p)*A_r(phi)/2.    (14)

The lower inequality is (6). The upper follows from |sin u|<=1.

For any shifted n-grid with the pole clearance (4),

    sum_(k in K_r)|cot(pi*y_-(k)/n)|
        <=(2n/pi)*H_n,

and the same holds for the plus channel. To see this, use
|cot(pi*y/n)|<=n/[pi*min(y,n-y)]. In each half, successive distances
from the adjacent pole are separated by one and start at least1.
Their reciprocal sum is at most H_n. The two halves give the factor2.

From (11)'s constant-numerator identity,

    A_r<= [sum|cotminus|+sum|cotplus|]/[2|sin v|]
        <=(2n/pi)*H_n/|sin v|.                       (15)

Uniformly on beta in[0,pi], the remaining ordinary-row angles satisfy

    sum_r sup_B 1/|sin v_r| <=2m*H_n.                 (16)

For r=1,...,m-2 the distance to pi*Z is at least
pi*min(r,m-r-1)/m; for r=m+1,...,2m-2 it is at least
pi*min(r-m,2m-r-1)/m. The sine chord bound gives reciprocal at most
m/(2d_r). Each positive distance integer occurs at most four times,
so their sum is at most2m*H_n. This proves (16), including both axes.

Adding (15) over rows yields sum_r A_r<=4N*H_n^2/pi. Multiply (14)
by1/N and use Delta_* to obtain (1). The buffered actual terms cancel
from this comparison, so their finite collision values cause no defect.

For exact coefficient ranges one may use the width estimate

    Delta_c,r+Delta_p <=3*w_alpha+4*w_beta.             (17)

Here |c_alpha|<=2, |c_beta|<=3+3/m<=4, and |p_alpha|<=1.
An implementation may construct a centered derivative-based rectangle
with these bounds, or use its actual wider interval rectangle and charge
that width. Ordinary interval overestimation is not erased by (17).

Consequently the intrinsic coefficient relaxation vanishes with box
width at each fixed n; its explicit growth is at most H_n^2. Formula
(1) measures the relaxation BEFORE per-row box supremum/interval
propagation. It is not a claim that the final U minus sup_P S is bounded
by (1), because different interval terms and rows can overestimate at
different phases. Shrinking boxes and reducing numerical/tail radii
are still needed for an arbitrarily tight final upper.

## 7. Complete analytic tail charge for C06 vertex rows

The original C02 coefficient-weight budget cannot simply be reused:
artificial c0,p0 destroy its special correlation with v. Instead,

    |C_z|+|D_z|=max(|p0|,|c0/sin v|)/2
              <=[1+5/|sin v|]/2.

Combining the separately taken row supremum with (16) gives

    sum_r sup_(z,phi)(|C_z|+|D_z|)<=m*[1+5H_n].        (18)

For one vertex, all its signed cores together contain at most n samples
per channel and12 blocks. With C06's M48,eta32,16 and separate w' tail
tau from C08, its per-channel analytic error is at most

    e=7*n*h^4*M48/5760+24*eta32,16/h+h*tau.

Equation (12) multiplies by |C_z|+|D_z|, with no factor2 from a
negative-part formula. Taking the maximum of four vertex bounds charges
the largest uniform per-vertex tail, not their sum. Thus the total
analytic vertex-tail allowance is at most

    [7*pi^4*M48/(5760*n^4)+24*eta32,16/pi+pi*tau/n^2]
                                          *[1+5H_n]. (19)

This is additional to coefficient relaxation, direct primitive enclosure,
and ordinary interval/roundoff error. It charges every approximated row.
All these C06 tails are already retained inside returned balls; (19)
is an audit identity and must not be added a second time. Arbitrary
precision/orders can reduce analytic tails on any declared finite degree
ceiling as in C02. No fixed nonzero tail is declared uniformly accurate
at all unbounded degrees.

## 8. Boundary, totality and remaining adoption work

No p>0 phase-box assumption is required: a vertex p0=0 is a constant
numerator branch, so boxes touching alpha=0 or pi remain in scope.
Exact numerator tangencies use fixed roots and the closed-band guard.
All possible v=0,pi,2pi rows are retained before the c0/sin v formula.
Exact zero terms, seams and coefficient-degenerate rectangles are merged
and counted once. The isolated phase vertices may use S=1 directly,
but nearby boxes require the complete whole-box upper contract.

Root intervals, coefficient endpoint extraction, signs, wraps and every
native C06 return code need independent implementation review. Successful
guarded calls and finite coarse fallback are both valid; pretending a
failed point/interval call succeeded is not. Form n*N, N and caps with
checked arbitrary-precision or outward arithmetic, avoiding native
overflow. Respect the accepted C06 LP64 range n<=2147483647 and its
actual library/source identities if that backend is used unchanged.

This proves a possible escape from C08's direct moving-numerator-root
enumeration obstruction. It preserves every actual denominator collision
term and pays a quantified convex-relaxation loss. It supplies neither
a pointwise equality for a nondegenerate coefficient rectangle, a
derivative bound, corner-orbit cancellation, nor a center-dependent
projected/full defect. Those require their own formulas and budgets.
Production tightness/speed and any consequential acceptance remain OPEN.
