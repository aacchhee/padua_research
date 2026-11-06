# PD-T?argmax-bridge-codex-C02-defect-01 — Dense finite-band projected floors

ID kind: PD-T. Aliases: C02 dense band; two-branch capped reciprocal bound.
Rules/input: `4b728b04216a5490910780bc609a82b853058426`.
Status: **PROVED analytic developer result; independent review required**.

The preregistered n64 primary 1/16 target remains OPEN. This result closes
explicitly preregistered weaker targets and the later preregistered
1/16 target at onset n4096. It does not change N5's OPEN
quarter target or its proved obstruction to one quarter certificate.

## Statement

Let n>=64 be an integer, m=n+1, N=nm. Let 0<=J<=n, 0<=K<=m,
J+K odd, and let

    theta=(J*pi+alpha)/n, phi=(K*pi+beta)/m in [0,pi],
    |alpha|+|beta| <= r <= 1/2.                         (1)

The full projected defects Q_v(K), Q_h(J) have exactly the definitions
below, including polynomial collision values. Then

    Q_v(K)>1/64 if 0<K<m;
    Q_h(J)>1/64 if 0<J<n.                              (2)

If n>=160, both applicable bounds improve to >1/32. If n>=4096, both
improve to >1/16. There is also a
fixed-work radius-dependent bound. Put

    a=1-r^2/4,
    U=347*a/1000-157*r/500,
    V=17*a/20-r/2,
    W=779*a/750-5*r/6,
    B_n(r)=11711*U/48400-120*V/(157*n)
           -250*W/(157*n)-100*V/(3*n^2).              (3)

Each applicable projection is at least min(1/20,B_n(r)). Consequently
every noncorner odd center satisfies

    Delta >= max(1/64, min(1/20,B_n(r)))               (4)

and 1/64 may be replaced by 1/32 in (4) when n>=160, or by 1/16 when
n>=4096. Here
Delta=S-lambda>=max(Q_v,Q_h). Thus subtracting (4) from a valid upper
bound for S gives a valid upper bound for lambda. Actual corners are
excluded. There is no claim below n64 or outside the full radius guard.

This is a quantitative continuation of the existing selected-pair
method. Both periodic branches and a dense reciprocal band provide the
larger margin. No finite-degree scan, asymptotic minimum, fitted
constant, sampled value or numerical quadrature is a proof premise.

## Exact normalization and numerator

The following polynomial and projection identities are PD-T364 and
C01's accepted identities; the numerator is also reconstructed here.
Let P=T_(n+1)+T_n and

    G(u,v)=[P(cos u)-P(cos v)]/(cos u-cos v)-cos(nu),

using the finite polynomial divided difference at equality. On the
odd periodic board Gamma={(p,q):0<=p<2n,0<=q<2m,p+q odd}, set
u_p=(p*pi+alpha)/n and v_q=(q*pi+beta)/m. With
d(x,y)=|x|+|y|-|x+y|,

    Q_v=(1/(4N))*sum_Gamma d(G(u_p,v_q),G(u_p,v_(2K-q))),
    Q_h=(1/(4N))*sum_Gamma d(G(u_p,v_q),G(u_(2J-p),v_q)). (5)

Indices are periodic and the phases stay unchanged. Folding the
reflected coordinate, and replacing the kernels by common-sign halves,
gives coefficient 1/N on every interior physical row. Explicitly,

    Q_v=(1/N)*sum_(k=0)^m f_k
            sum_(p+k=J mod2,0<=p<2n) d(V_+,V_-),
    V_+/-=(-1)^p G(u_p,phi +/- k*pi/m)/2,
    f_0=f_m=1/2, f_k=1 otherwise;                     (6)

    Q_h=(1/N)*sum_(j=0)^n e_j
            sum_(q+j=K mod2,0<=q<2m) d(H_+,H_-),
    H_+/-=(-1)^(J+j) G(theta +/- j*pi/n,v_q)/2,
    e_0=e_n=1/2, e_j=1 otherwise.                     (7)

Every row selected below is interior, so its weight is exactly 1/N.
Both opposite periodic branches are counted explicitly, not absorbed
into this coefficient. Their parity meshes each have spacing 2*pi/L.

At regular denominators, angle addition on the odd board gives the
common-sign half kernel

    H(u,v)=A(u,v)/(cos u-cos v),
    A(u,v)=a_actual*(1+cos v)
           -(sin alpha/2)*sin u+(sin beta/2)*sin v,
    a_actual=(cos alpha+cos beta)/2 >= a=1-r^2/4,
    (|sin alpha|+|sin beta|)/2 <= r/2.                 (8)

For example (-1)^p P(cos u)=cos alpha*(1+cos u)
-sin alpha*sin u, while the corresponding second-coordinate value is
-cos beta*(1+cos v)-sin beta*sin v. Subtracting cos alpha after division
by cos u-cos v gives (8). This retains the exceptional highest mode in
the first coordinate. Horizontally the second angle v is fixed, so
the baseline is 1+cos v in both halves. No mesh interchange is used.
All selected denominators below have opposite nonzero signs. Thus a
positive common numerator lower bound A0 gives

    d(H_+,H_-)=2*min(|H_+|,|H_-|).                    (9)

Omitted terms, including polynomial collision terms, are nonnegative.

## Common geometry and two-branch mesh bounds

For a vertical proof use physical mesh M=m, periodic mesh L=n and
center angle chi=phi. For a horizontal proof use M=n, L=m and chi=theta.
The selected periodic angle is u vertically and v horizontally. Let

    gamma=min(chi,pi-chi), 0<gamma<=pi/2.

A physical row at b=l*pi/M is used near the bottom; near the top use
the physical row M-l. The two varying physical cosine targets are,
in either case and up to order,

    z0-D, z0+D,
    z0=cos gamma*cos b >=0, D=sin gamma*sin b>0.       (10)

Indeed reflection replaces the original chi and pi-b by gamma and b
inside cosine. In the vertical case these are the two second-coordinate
cosines; horizontally they are the first-coordinate cosines. A periodic
cosine strictly between them makes the two denominators opposite.

For any prescribed row parity, the periodic angles form a translated
grid of L points on a circle, spacing h=2*pi/L. An arc of length ell
contains at least ell/h-1 points, also for an open arc. For a nonnegative
function of the periodic cosine whose positive superlevel sets are one
interval on each half-circle, layer cake therefore gives

    sum_grid f(cos w) >= (L/(2*pi))*integral_0^(2*pi) f(cos w)dw
                        -2*max f.                    (11)

The two intervals may meet an endpoint; assign that endpoint to one
half-circle. The count with loss one per arc still holds. This argument
uses either shifted parity; no endpoint-center parity is inferred.

For a decreasing positive function f on [a0,b0], physical mesh h=pi/M
also gives

    sum_(l*h in [a0,b0]) f(l*h) >= (M/pi)*integral f-f(a0),
    sum_(l*h in [a0,b0]) f(l*h) <= (M/pi)*integral f+f(a0). (12)

Integrating the lower/upper step sums proves these inequalities; they
do not assume that band endpoints are mesh points.

## The four closest endpoint distances

Let s be the center-index distance from an endpoint, 1<=s<=4. The small
center angle is t=(s*pi +/- physical_phase)/M. Select every integer

    M/4 <= l <= M/2,
    q=-(s-1),-(s-3),...,s-1,                           (13)

and the two periodic indices l+q and 2L-(l+q), interpreted modulo 2L.
There are s choices of q, and at least M/4-1 choices of l. The physical
row is l at the bottom and M-l at the top.

Parity is explicit: q=s-1 modulo 2. At the bottom the row plus periodic
index has parity q=1-s, the required complementary-center parity. At
the top it has parity M+q=1-M+s, again the required parity. Negating the
periodic index leaves parity unchanged. This verifies both parities,
both axes, both endpoint orientations, every n, and every admissible
value of the other center coordinate.

Write b=l*pi/M. The two effective angles are
w=((l+q)*pi +/- periodic_phase)/L. Since M,L are adjacent and >=64,

    |M*(w-b)| <= (s-1)*pi+(71/128)*pi
                 +(65/64)*|periodic_phase|
              < s*pi-|physical_phase| <= M*t.        (14)

For the first inequality use |q|<=s-1, l<=M/2,
M/L<=65/64 and 3/L<=3/64. The strict slack in the second is at least
(57*pi-65)/128>0 by (1). Also

    t <= (4*pi+1/2)/M <7/30,
    pi/4<=b<=pi/2,
    0<b-t<w<b+t<pi.                                  (15)

All selected indices lie in their prescribed ranges: l+q>=13 and
l+q<=M/2+3<L. They and the reflected branches are distinct. Therefore
both periodic cosines straddle the targets regularly. Vertically both
target cosines are >=-sin t>=-t; horizontally the fixed periodic cosine
has that same lower bound. Equation (8), with a>=15/16 and r/2<=1/4,
gives a numerator >=15/32 in each half. The full cosine span is at most
2*t, so (9) gives a pair defect >15/(32*t). After normalization,

    Q > [15*s/(16*(s*pi+1/2))]*(M/L)*(1/4-1/M)
      >=225/[1040*(pi+1/2)] >1/20.                    (16)

Here M/L>=64/65 and 1/4-1/M>=15/64. The final comparison follows from
pi+1/2<51/14. This proves both projected bounds for these near centers.

## Small angles beyond the four closest distances

If s>=5 then gamma>4*pi/L. Indeed gamma>=(5*pi-1/2)/M and M<=L+1;
the required inequality reduces in the worst case to
L*(pi-1/2)>4*pi, valid for L>=64.

Suppose gamma<pi/6. Choose every physical row b in [pi/6,pi/3]. On
each periodic branch take all angles w in the open interval
(b-gamma,b+gamma), or its reflection about 2*pi. These arcs are disjoint
and inside their half-circles. They put cos w strictly between the two
physical cosine targets. Both target baselines vertically, and the
fixed periodic baseline horizontally, are >=1 since b+gamma<pi/2.
Thus each numerator is >=11/16. The full denominator span is
2*sin gamma*sin b, giving

    d >=11/[16*sin gamma*sin b]
       >=11/[8*sqrt(3)*gamma].                        (17)

There are at least M/6-1 physical rows. The two periodic arcs give
at least 2*L*gamma/pi-2 >=3*L*gamma/(2*pi) points because
L*gamma/pi>4. Normalization now yields

    Q >=957/[3072*pi*sqrt(3)] >1/20.                  (18)

The last comparison already follows from pi<22/7 and sqrt(3)<7/4.
This argument counts either parity independently and applies to both
axes using the fixed-v observation following (8).

## Middle angles: dense capped reciprocal band

It remains to treat gamma>=pi/6. Select physical rows in

    a0=pi/20 <= b <= b0=pi/4.

Set C=a-r/2 and A(b)=C-a*sin b. Both half numerators are >=A(b): in
(10), z0>=0, D<=sin b, and the horizontal fixed periodic cosine is at
least z0-D on the selected sign band. A(b)>0 throughout this band even
at r=1/2, since sin(pi/4)<11/15.

For |x-z0|<D, the actual defect is at least

    2*A(b)/(D+|x-z0|).

Keep only the capped function

    f_b(x)=(A(b)/D)*min(c,2/(1+|x-z0|/D)), c=5/4,   (19)

and set it to zero outside the open band. It has maximum c*A(b)/D.
Its exact cosine-coordinate integral is

    integral f_b(x)dx =T*A(b),
    T=4-2*c+4*log c=3/2+4*log(5/4).                  (20)

To check this, split at |x-z0|/D=2/c-1, integrate the central constant
and the outer reciprocal on both sides. Also
integral_0^(2*pi) f_b(cos w)dw >=2*integral f_b(x)dx, because
1/sqrt(1-x^2)>=1. Thus (11) proves the exact finite row bound

    sum_row d >=(L*T/pi)*A(b)-2*c*A(b)/D.             (21)

Let

    A0=C-a*sin a0,
    I=C*(b0-a0)+a*(cos b0-cos a0),
    R=C*log[tan(b0/2)/tan(a0/2)]-a*(b0-a0).          (22)

These are the integrals of A(b) and A(b)/sin b. Both functions are
positive and decreasing on the band. Sum (21) over the physical rows,
apply (12), use sin gamma>=1/2 and L,M>=n. The result is

    Q >= T*I/pi^2 -T*A0/(pi*n)
                    -5*R/(pi*n)-5*A0/(n^2*sin a0). (23)

Every lattice loss is explicit. In particular no convergence rate for
a limiting center-minimum theorem is assumed.

## Rational constants and the cheap radius formula

The following elementary strict bounds suffice:

    157/50<pi<22/7, 3/20<sin(pi/20),
    cos(pi/20)<247/250, cos(pi/4)>707/1000,
    239/100<T<12/5,
    log[tan(pi/8)/tan(pi/40)]<5/3.                   (24)

For completeness: sin x>=x-x^3/6 and
cos x<=1-x^2/2+x^4/24 at x=pi/20 give the first trigonometric bounds;
cos(pi/4)>707/1000 follows by squaring. For T use
log(5/4)>2*(1/9+1/(3*9^3)) and
log(5/4)<1/4-(1/4)^2/2+(1/4)^3/3. Finally
tan(pi/8)=sqrt(2)-1<83/200, tan(pi/40)>157/2000;
the ratio is <830/157, while
sum_(k=0)^7 (5/3)^k/k!=5833853/1102248>830/157.
Hence the logarithmic bound follows. These are analytic rational
comparisons, not floating certificates.

Equations (22)-(24) give I>U, A0<V and R<W, with U,V,W exactly (3).
All are positive for 0<=r<=1/2. Substitute the lower bounds for the
positive main term and upper bounds for the three losses in (23).
This is precisely Q>=B_n(r) from (3). Equations (16),(18) give >1/20
in the other two cases, proving the radius-dependent statement.

For the simpler uniform constants take r=1/2, a=15/16. The same bounds
give I>21/125, A0<11/20, R<14/25. Thus the middle case is strictly above

    E_n=(239/100)*(21/125)/(22/7)^2
        -(12/5)*(11/20)/[(157/50)*n]
        -5*(14/25)/[(157/50)*n]
        -5*(11/20)/[n^2*(3/20)].                     (25)

E_n increases with n, and exact rational arithmetic gives

    E_64-1/64=34466881/729484800000>0,
    E_160-1/32=88079689/182371200000>0.               (26)

Together with (16),(18), these prove (2) and the n160 improvement.

## Uniform 1/16 at onset n4096

This onset-restricted continuation was separately registered before
evaluating its new rational constants. Keep the same three-case proof.
For the four nearest distances, n>=4096 gives
t< (4*pi+1/2)/4096 <1/45. Thus the numerator in (15) is now >=2/3.
Repeating the count in (16) gives

    Q>20/[65*(pi+1/2)]>1/16.                          (27)

For the small-angle case retain the sharper row count M/6-1 in (18):

    Q >= [33/(16*pi*sqrt(3))]*(1/6-1/n).

Using pi<22/7 and sqrt(3)<26/15, its lower bound at n4096 exceeds 1/16
by the exact positive rational 1733/3407872. It increases with n.

For middle angles use the same capped reciprocal proof with

    a0=pi/100, b0=pi/4, c=2, T=4*log 2.

Use r=1/2, a=15/16, C=11/16 for this uniform estimate. The analogues
of (22) obey

    I>6/25, A0<11/16, R<8/5,
    sin a0>3/100, 11/4<T<14/5.                       (28)

Here b0-a0=6*pi/25; cos a0<1 and cos b0>707/1000 prove the I bound.
The sine bound follows from sin x>=x-x^3/6. To prove the R bound, the
tangent ratio is <4150/157, whose logarithm is <10/3: square the
positive exponential lower bound used in (24). Hence
R<(11/16)*(10/3)-(15/16)*(6/25)*(157/50)<8/5.
The series log 2=2*sum_(j>=0) (1/3)^(2j+1)/(2j+1) gives
log 2>56/81>11/16 and log 2<25/36<7/10, proving the T bounds.

Equation (23) has loss coefficient 4c=8 in place of 5. Its resulting
uniform rational lower bound is

    H_n=(11/4)*(6/25)/(22/7)^2
        -(14/5)*(11/16)/[(157/50)*n]
        -8*(8/5)/[(157/50)*n]
        -8*(11/16)/[n^2*(3/100)].                    (29)

This increases with n, and

    H_4096-1/16=3436012187/1086534451200>0.            (30)

This proves both applicable projected 1/16 floors for all n>=4096,
including both center parities and horizontal boundary classes. No
asymptotic passage is used, and it does not establish the n64 1/16 target.

## Backend premise and limitations

A full phase box may use (2) only under exact integer n>=64 and

    maxabs(alpha interval)+maxabs(beta interval)<=1/2.

For (3)-(4), choose any validated radius r between that sum and 1/2.
The expression is fixed rational work in n and r; use outward arithmetic
or exact rational arithmetic. The n160 or n4096 improvement additionally
needs n>=160 or n>=4096 respectively. Actual corner centers are separate. Merely intersecting the
radius diamond is insufficient for a whole-box bound. The result
licenses a mathematical premise only after independent reconstruction;
it does not approve an executable implementation or a complete cover.

The primary n64 uniform 1/16 target, the stronger quarter target, the global
upper comparison and effective all-degree argmax remain OPEN. This
proof uses no numerical pilot and makes no claim about global n1
coverage or extrapolation of earlier finite-energy computations.
