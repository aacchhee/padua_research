# PD-T?argmax-bridge-codex-N5-04 — Radius-half two-phase deficit near all interior vertical-edge centers

ID kind: PD-T.
Aliases: N5-04; shifted middle lines; inward vertical-edge phase diamond;
radius-half projected vertical deficit; exceptional cos(alpha) correction.
Split from: none; quantitative domain variant of PD-T222/224/366 and N5-03.
Split into: none. Full two-dimensional corner comparison remains OPEN.

## Statement

For every integer n>=64, m=n+1, J in {0,n}, integer q with

    1<=q<=m-1, J+q odd,

and real phases alpha,beta satisfying

    |alpha|+|beta|<=1/2,
    theta=(J*pi+alpha)/n in [0,pi], phi=(q*pi+beta)/m,

the actual Padua Lebesgue function satisfies

    lambda_n(cos theta,cos phi) < S_n(alpha,beta)-1/2048.   (1)

Here S_n is the corrected odd-board primitive of PD-T215/364. The
physical restriction means alpha>=0 at J=0 and alpha<=0 at J=n;
both beta signs occur. Since q is interior, phi is automatically in
(0,pi). Equivalently these are the two inward phase diamonds attached
to every parity-complementary interior vertical-edge center.

With N1's full-diamond row model M_n and its stated analytic error

    r_n=[7*pi^4/1800+7*pi^3*H_n/900]/n^4,
    |S_n(alpha,beta)-M_n(alpha,beta)|<=r_n,

one consequently has

    lambda_n(cos theta,cos phi)
        < M_n(alpha,beta)+r_n-1/2048
        < M_n(alpha,beta)-255/524288.                    (2)

Neither assertion bounds the maximum of S_n or M_n. Actual nonnode
corner centers q=0,m remain excluded; their zero-phase defect is zero.

## Definitions and assumptions

Exact real arithmetic, even-checkerboard Padua convention. Put N=nm,
a_j=j*pi/n, b_k=k*pi/m, j+k even, with weights 2*e_j*f_k/N;
endpoint factors are 1/2 and interior factors 1. Set

    P_n=T_(n+1)+T_n,
    D_n(x,y)=[P_n(x)-P_n(y)]/(x-y),
    G_n(u,v)=D_n(cos u,cos v)-cos(nu).

D_n has its finite polynomial divided-difference value on x=y.
The exceptional highest mode stays in x. For 0<=r<2n with r+k=J
mod 2 set

    u_r=(r*pi+alpha)/n, v_+=phi+b_k, v_-=phi-b_k,
    H_+=[(-1)^r D_n(cos u_r,cos v_+)-cos alpha]/2,
    H_-=[(-1)^r D_n(cos u_r,cos v_-)-cos alpha]/2,
    d(r,k)=|H_+|+|H_-|-|H_++H_-|.

The exact inherited projection and full-defect identities are

    Q_v = (1/N)*sum_(k=0)^m f_k
                sum_(0<=r<2n, r+k=J mod2) d(r,k),
    lambda_n=S_n-Delta, Delta>=Q_v>=0.                 (3)

The sum uses weight 1/N for a selected interior physical second row
and periodic first representative. The weight 2/N from N5-03's
two-copy physical-edge formula is not valid here.

## Status by part

Overall status: **PROVED**, analytic developer proof below.
Required distinct supplementary review and Claude audit are separate.

| Mathematical part | Status | Evidence / limitation |
|---|---|---|
| Actual two-phase deficit (1) | PROVED | Uniform finite selected-block numerator, strict band and parity counts |
| Model margin (2) | PROVED | (1) and the existing N1/N5 error bound |

Candidate disposition: retained quantitative variant with the enlarged
phase domain and stated constant. No new cancellation mechanism or
historical originality claim.

## Depends on

PD-T215 and PD-T364 for the exact primitive/full/projected identities;
PD-T101/185 for the corrected kernel convention. PD-T222/224/366 and
N5-03 are predecessor finite selections, all read in full. Their
smaller-radius inequalities are not extrapolated: all radius-half
estimates are reconstructed below. N1's PD-T?argmax-bridge-codex-N1-01,
using N5-01, supplies the model error in (2) only. No external source
theorem, measured diagnostic or asymptotic limit is a premise.

## Proof

### 1. Correct exceptional term and uniform positive numerators

For v=((q +/- k)*pi+beta)/m, odd J+q and r+k=J mod 2 imply
r+q +/- k odd. Thus, writing x=cos u_r and y=cos v,

    P_n(x)=(-1)^r[cos alpha*(1+x)-sin alpha*sin u_r],
    P_n(y)=-(-1)^r[cos beta*(1+y)+sin beta*sin v].

Subtracting the exceptional term cos(nu_r)=(-1)^r cos alpha gives,
at every regular denominator,

    H(u_r,v)=A(u_r,v)/(cos u_r-cos v),
    A(u,v)=a*(1+cos v)-(sin alpha/2)*sin u
                         +(sin beta/2)*sin v,
    a=(cos alpha+cos beta)/2.                           (4)

In particular the subtraction in H is cos(alpha), not 1. The total
identities (3) retain the polynomial values at all collisions; the
selections below have strictly nonzero denominators.

Put rho=|alpha|+|beta|. Since rho<=1/2,

    a>=1-(alpha^2+beta^2)/4>=15/16,
    (|sin alpha|+|sin beta|)/2<=rho/2<=1/4.             (5)

Consequently, whenever the actual baseline 1+cos v is at least 2/5,
its numerator is >=1/8. If that baseline is at least 1/2, its
numerator is >=7/32. These estimates allow either sign of either sine
term and do not assume alpha=0.

A shifted grid of spacing h has at least ell/h-1 representatives in
a closed interval of length ell. This count follows by putting the
first grid point at distance less than h from the lower endpoint.
We use the parity-restricted periodic first grid, spacing 2*pi/n,
and physical second grid, spacing pi/m. All selected second rows
are interior, so f_k=1. Every unselected point defect is nonnegative.

### 2. Endpoint-distance indices 1 through 4

Let s=min(q,m-q) in {1,2,3,4}. For every integer l with

    3*n/8<=l<=n/2,                                     (6)

select one pair (r,k) as follows. If q=s (bottom), put

    eta=0 for odd s, eta=1 for even s,
    r=l, k=l+eta, w=(l*pi+alpha)/n,
    t=(s*pi+beta)/m, phi=t, u_r=w.

If q=m-s (top), put

    eta=1 for odd s, eta=0 for even s,
    r=n-l, k=l+eta, w=(l*pi-alpha)/n,
    t=(s*pi-beta)/m, phi=pi-t, u_r=pi-w.

Writing b=k*pi/m, the exact displacement is

    m*(w-b)=l*pi/n-eta*pi +/- (m/n)*alpha,              (7)

with the plus sign at the bottom and minus at the top. Its unperturbed
absolute value is <=5*pi/8 because l*pi/n lies in [3*pi/8,pi/2].
For n>=64,

    (m/n)*|alpha|+|beta| <= (65/64)*rho
                              <=65/128<3*pi/8.        (8)

The last strict inequality follows already from pi>3. Hence
|m*(w-b)|<pi-|beta|<=m*t, since s>=1. This proves

    b-t<w<b+t.                                        (9)

All selected r,k are interior representatives; they belong to the
periodic/physical ranges in (3). In the bottom case the target cosines
are cos(b-t),cos(b+t); in the top case they are their negatives,
and cos u_r=-cos w. Strict monotonicity of cosine on the folded
target interval will therefore give opposite regular denominators.

The folded targets lie in [3*pi/10,3*pi/5]. Indeed

    b-t >= [((3*n/8-4)*pi)-1/2]/m >=3*pi/10,
    b+t <= [((n/2+5)*pi)+1/2]/m <=3*pi/5.             (10)

After clearing m, the two sufficient inequalities are
(3*n/40-43/10)*pi>=1/2 and (n/10-22/5)*pi>=1/2.
Their left sides increase in n and are pi/2 and 2*pi at n=64.
On this interval both 1-cos z and 1+cos z exceed 2/5:
cos(3*pi/10)=sin(pi/5)<3/5, since
sin^2(pi/5)=(5-sqrt5)/8<7/20<9/25 using sqrt5>11/5;
and 3*pi/5<2*pi/3 gives 1+cos z>1/2 at the other end.

Thus the actual top baselines 1-cos(b +/- t) and bottom baselines
1+cos(b +/- t) each exceed 2/5. By (5) both actual numerators are
>=1/8. The denominator magnitudes are bounded by their full cosine
span, which is <=2*t<27/m because

    2*m*t <=8*pi+1<27.

They are nonzero and opposite by (9)–(10). Therefore

    |H_+|,|H_-|>m/216, d(r,k)>m/108.                  (11)

The required parity is explicit. At the bottom r+k=eta mod2, while
J+s odd implies J=1-s mod2=eta. At the top r+k=n+eta mod2,
while odd J+m-s gives J=n+s mod2 and eta=s mod2. Hence every
selected pair is in the exact projection (3), for both J endpoints.
There are at least n/8-1>=n/16 integers l in (6), in distinct rows.
Using the weight 1/N gives the strict bound

    Q_v > [1/(nm)]*(n/16)*(m/108)
        =1/1728>1/2048.                              (12)

### 3. Every remaining center has sufficient physical endpoint distance

If min(q,m-q)>=5, put gamma=min(phi,pi-phi). Then

    gamma >=(5*pi-1/2)/m>4*pi/n, gamma<=pi/2.          (13)

The strict comparison is equivalent to n*(pi-1/2)>4*pi; it holds
from n=64 onward. If phi=gamma use b=b'; if phi=pi-gamma use
b=pi-b'. In the latter orientation

    cos(phi+b)=cos(gamma+b'),
    cos(phi-b)=cos(gamma-b').                          (14)

Reflection preserves row counts and interior factors; the actual sine
signs remain allowed by (5). The first grid is now shifted by alpha/n,
with the same parity spacing 2*pi/n. The intervals below lie strictly
inside (0,pi). Since |alpha|<=1/2, every point of the infinite shifted
parity grid lying in them has an actual periodic representative
0<=r<2n: indices outside that range have u<0 or u>pi. Thus the
shifted-grid count applies directly, without discarding a factor.

### 4. Adaptive small-angle block

For 4*pi/n<=gamma<=pi/6 choose

    pi/3<=b'<=pi/2,
    b'-gamma/2<=u_r<=b'+gamma/2.                      (15)

The folded target angles b'-gamma,b'+gamma are in [pi/6,2*pi/3],
so both actual baselines are >=1/2. By (5), both numerators are
>=7/32. The selected u lies strictly between the targets, separated
from each by at least gamma/2. The opposite denominator magnitudes
are each at most the cosine span <=2*gamma. Hence

    d(r,k)>=7/(32*gamma).                             (16)

There are at least m/6-1>=m/12 physical rows. In each row the selected
interval length is gamma; either required parity therefore contributes
at least n*gamma/(2*pi)-1>=n*gamma/(4*pi), using gamma>=4*pi/n.
Formula (3) gives

    Q_v >= [1/(nm)]*(m/12)*(n*gamma/(4*pi))
                                      *[7/(32*gamma)]
        =7/(1536*pi)>1/2048.                         (17)

The final strict inequality follows from pi<4, since
7/(1536*pi)>7/6144>3/6144.

### 5. Adaptive middle-angle block

For pi/6<=gamma<=pi/2 choose

    pi/12<=b'<=pi/6,
    gamma-b'/2<=u_r<=gamma+b'/2.                      (18)

The target angles gamma-b',gamma+b' lie in [0,2*pi/3]. Again both
numerators are >=7/32, and the selected u is strictly between the
targets with separation at least b'/2. Their cosine span is
2*sin gamma*sin b'<=1, giving d(r,k)>=7/16.

The row count is at least m/12-1>=m/16, since m>=65>48. Each
first interval has length b'>=pi/12 and contains at least
n/24-1>=n/48 points of either shifted parity, since n>=64>48.
All selected rows are interior. Therefore

    Q_v >= [1/(nm)]*(m/16)*(n/48)*(7/16)
        =7/12288>1/2048.                             (19)

At gamma=pi/6 both constructions are valid, including their closed
selected intervals. Cases (12), (17), (19) exhaust the stated q.
Together with Delta>=Q_v and lambda=S_n-Delta, they prove (1).

### 6. Explicit row-model margin

N1's primitive/model error applies on the whole larger phase diamond,
so it applies here including every transition/collision. As in N5-03,
pi^4<100, pi^3<32 and H_n<=n give

    r_n<7/(18*n^4)+56/(225*n^3).

The right side decreases with n. At n=64 its product with 524288 is
7/576+112/225=66087/129600<1. Thus r_n<1/524288, and
1/2048=256/524288 leaves the strict margin 255/524288 in (2).

## Checks and evidence

The exact candidate/domain/parity/cos(alpha) correction was written in
[the candidate](../ideas/N5-two-phase.md) before the first computation.
The initial 72-case recurrence and full-function diagnostic survived;
its small/middle coverage gap led to the separately recorded bounded
36-case addition. The final command, source identity, actual scope,
environment and output identity are in
[the receipt](../evidence/n5-two-phase-defect.json). These high-precision
floating checks are **MEASURED developer diagnostics**, not rigorous
interval certificates, independent reruns or proof premises. The
analytic proof establishes all n>=64 and all phases in the Statement.

Selected terms compare the finite divided-Chebyshev recurrence with (4).
The full-function diagnostic evaluates the entire corrected odd board,
then sums all four reflected copies before the absolute value. Thus it
checks actual lambda, Q_v and their normalizations separately. Exact
zero-phase collisions use the finite recurrence. No external fulltext
was read or proof transferred; N5's existing literature limits persist.

## Scope and open items

The theorem extends N5-03 from alpha=0 to two varying phases and extends
T366's radius on these vertical-edge center charts from 1/10 to 1/2.
It uses the inherited positive-block mechanism. The bound is on actual
lambda relative to its primitive/model, with a fixed finite margin.
It does not cover all physical odd centers, horizontal-edge centers
with q an endpoint, actual nonnode corner centers, phases outside the
stated half diamond, or an independently optimized whole cell.

A uniform upper bound for M_n or S_n is still needed for a corner
comparison. No effective global onset, new certified degree, B3/B4
pass, all-degree E-C or PD-T099 conclusion follows. Distinct review
and the required Claude audit remain to be supplied by the coordinator.
This is the sole bounded N5 round4 result; no round5 starts here.

## History

2026-11-06. Codex mathematical worker, parent-assigned model/effort
inherited; serving metadata not independently exposed. Rules/input
3888dd37c362a0689943f33e6b7e44c1dd1c3050. Parent supplied the target,
explicitly unproved. Gate and corrected formula preceded the selected
test. First diagnostics survived; the written proof then reconstructs
the enlarged-domain estimates, preserving earlier rounds unchanged.
No Git, external write or shared registry operation by this worker.
