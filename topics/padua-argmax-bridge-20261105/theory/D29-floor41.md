# PD-T?argmax-bridge-codex-D29-02 — Uniform noncorner floor from degree41

ID kind: PD-T. Aliases: D29 n41 floor; full open straddling arcs.
Split from: the two-target D29 local candidate.
Split into: none; the separate n512 and radius-dependent results have
their own files and IDs.

Status: **PROVED**, analytic developer result; distinct review remains
required before adoption as a checker premise.

## Statement and definitions

Let n>=41 be an integer, m=n+1, N=nm. Let 0<=J<=n and 0<=K<=m be
integers with J+K odd, and let alpha,beta be real with

    |alpha|+|beta|<=1/2,
    theta=(J*pi+alpha)/n in [0,pi],
    phi=(K*pi+beta)/m in [0,pi].                         (1)

Use the corrected even-checkerboard Padua kernel

    P=T_(n+1)+T_n,
    G(u,v)=[P(cos u)-P(cos v)]/(cos u-cos v)-cos(nu),
    d(x,y)=|x|+|y|-|x+y|.                              (2)

The divided difference is its finite polynomial value at equality.
Put u_p=(p*pi+alpha)/n, v_q=(q*pi+beta)/m and
Gamma={(p,q):0<=p<2n,0<=q<2m,p+q odd}. Define the full quantities

    S=(1/(2N))*sum_Gamma |G(u_p,v_q)|,
    Q_v=(1/(4N))*sum_Gamma d(G(u_p,v_q),G(u_p,v_(2K-q))),
    Q_h=(1/(4N))*sum_Gamma d(G(u_p,v_q),G(u_(2J-p),v_q)). (3)

Indices are periodic; reflected indices keep the same phases. The
exact PD-T364 identity supplies Delta=S-lambda>=Q_v,Q_h>=0. Then

    Q_v>1/512 whenever 0<K<m,
    Q_h>1/512 whenever 0<J<n.                          (4)

Consequently every noncorner odd center satisfies Delta>1/512 and
lambda<S-1/512. Here noncorner means that J,K are not both endpoints.
Actual nonnode corner centers are excluded; their zero-phase defect
vanishes. There is no assertion for n<41 or outside (1).

## Dependencies and normalization

PD-T364 supplies the exact full identity and folded projection formulas;
C01-allclass-defect.md reconstructs them in its equations(6)-(8).
C02-defect-dense-band.md is the nearest and small-angle predecessor.
The formulas themselves have no n64 premise. All estimates using the
new lower degree domain are proved here, rather than inferred from
C02's n64 statement. The prospective gate and alternatives are in
../ideas/D29-defect-floors.md. This is a quantitative/domain variant
of the accepted finite selected-pair mechanism, with no novelty claim.

Folding only the reflected physical coordinate and replacing both
kernels by their common-sign halves gives

    Q_v=(1/N)*sum_(k=0)^m f_k
              sum_(p+k=J mod2,0<=p<2n) d(V_+,V_-),
    V_+/-=(-1)^p G(u_p,phi+/-k*pi/m)/2;                (5)

    Q_h=(1/N)*sum_(j=0)^n e_j
              sum_(q+j=K mod2,0<=q<2m) d(H_+,H_-),
    H_+/-=(-1)^(J+j) G(theta+/-j*pi/n,v_q)/2.          (6)

The endpoint physical weights are1/2, every interior physical weight
is1. Each row selected below is interior, so its coefficient is exactly
1/N. Both periodic branches below are counted explicitly in that row;
they do not change its coefficient to2/N. Omitted terms, including
polynomial collisions, have nonnegative defect.

At regular denominators the common-sign half kernel is

    A(u,v)/(cos u-cos v),
    A(u,v)=a_actual*(1+cos v)
                 -(sin alpha/2)*sin u+(sin beta/2)*sin v,
    a_actual=(cos alpha+cos beta)/2>=15/16.            (7)

The total absolute sine perturbation is at most1/4. This is exactly
the numerator obtained by subtracting cos(nu) before halving; the
exceptional highest mode remains in the first coordinate. Horizontally
v is fixed in both halves, so its baseline remains1+cos v.

Whenever two regular denominators have opposite signs and both
numerators are at least A0>0, their signed halves have opposite signs:

    d(H_+,H_-)=2*min(|H_+|,|H_-|).                    (8)

If the full cosine span is at most W, then (8) is at least2*A0/W.

## Common geometry and mesh counts

Vertically set M=m,L=n,chi=phi; horizontally set M=n,L=m,chi=theta.
The physical and periodic meshes are adjacent, M,L>=41, ML=N.
For the applicable interior center, put gamma=min(chi,pi-chi)>0.
For a selected physical b=l*pi/M near the bottom use row l; near the
top use row M-l. The two actual physical cosine targets, up to order,
are exactly

    cos(gamma-b), cos(gamma+b).                       (9)

For example at the top chi=pi-gamma and the physical row angle is
pi-b, so angle addition gives the same cosines. These are second
coordinate targets vertically, first coordinate targets horizontally.
The periodic cosine between them makes the denominators opposite.

Each prescribed periodic parity is a translated grid of L points on a
circle, with spacing2*pi/L. Any open or closed arc of length ell has
at least L*ell/(2*pi)-1 points. A closed physical interval of length ell
has at least M*ell/pi-1 rows. These are lower bounds with real right
sides and need not be integers. An arc count is on the circle: when a
representative angle lies just outside[0,2pi), choose its periodic
representative. The kernel and the common-sign half are unchanged.
The two open arcs selected below are disjoint, so their counts add.

## The four closest endpoint distances, now at n>=41

Let s be the index distance of the applicable center from its nearest
physical endpoint and suppose1<=s<=4. The small center angle is

    t=(s*pi+/-physical_phase)/M.

Choose all integers l with M/4<=l<=M/2 and all

    q=-(s-1),-(s-3),...,s-1.                         (10)

For each row choose periodic indices l+q and2L-(l+q). The corresponding
effective positive angles have the form

    w=((l+q)*pi+/-periodic_phase)/L,
    b=l*pi/M.

These effective angles represent the two cosine branches. Using
|M-L|=1, M/L<=42/41, l<=M/2 and |q|<=3 gives

    |M*(w-b)|
      <=(s-1)*pi+(24/41)*pi+(42/41)*|periodic_phase|
       <s*pi-|physical_phase|<=M*t.                 (11)

Indeed M/(2L)+(s-1)/L<=21/41+3/41=24/41. Adding the
absolute physical phase to the first line leaves strict slack at least
(17*pi-21)/41>0, since the weighted total phase is at most21/41.
This proves strict straddling for both phase signs and branches.

The smaller-degree bounds are

    t<=(4*pi+1/2)/M <183/574<1/3,
    pi/4<=b<=pi/2,
    0<b-t<w<b+t<pi.                                  (12)

Here pi<22/7 proves the strict rational bound, and pi>3 suffices for
the angular endpoints. Selected indices satisfy

    l+q>=ceil(M/4)-3>=8,
    l+q<=M/2+3<L.                                    (13)

The last inequality is already true at M=L+1,L=41. Thus indices are
valid, the s choices are distinct, and their reflected branches are
distinct. The old n64 index lower bound13 is not asserted at n41.

For parity, q=s-1 modulo2. At the bottom the physical row plus
periodic index has parity q=1-s, the complementary-center parity. At
the top its parity is M+q=1-M+s modulo2. Negation preserves parity.
This proves the prescribed parity in (5) or(6) for both axes and both
center parities, independently of the other coordinate's index.

Both vertical target cosines are >=-sin t>-1/3. The horizontal fixed
periodic cosine between them has the same bound. By (7), each actual
numerator is > (15/16)*(2/3)-1/4=3/8. The full cosine span is at most
2*t. Therefore each selected pair has d>3/(8*t). At least M/4-1
physical rows and2s periodic points per row contribute. Consequently

    Q > [3*s/(4*(s*pi+1/2))]*(M/L)*(1/4-1/M)
      >=37/[224*(pi+1/2)]
       >37/816>1/32.                                (14)

The middle comparison uses s>=1, M/L>=41/42 and
1/4-1/M>=37/164; pi+1/2<51/14 gives the next comparison.

## Remaining centers with small angle

If s>=5 then gamma>4*pi/L. Indeed gamma>=(5*pi-1/2)/M,
M<=L+1, and L*(pi-1/2)>4*pi for every L>=41. For example
L*(pi-1/2)-4*pi> (5/2)*L-12>0 using pi>3.

Suppose gamma<pi/6. Choose every physical row

    pi/6<=b<=pi/3,

and all periodic angles in the two open arcs (b-gamma,b+gamma) and
its reflection about2pi. They are disjoint and contained in their
respective half-circles. The periodic cosine lies strictly between the
targets (9). Since b+gamma<pi/2, both vertical target baselines and
the horizontal fixed periodic baseline are >=1. The actual numerator
is at least11/16. The full cosine span is2*sin gamma*sin b, hence

    d>=11/[16*sin gamma*sin b]
      >=11/[8*sqrt(3)*gamma].                         (15)

The physical row count is at least M/6-1. The two arcs together have
at least2*L*gamma/pi-2 >3*L*gamma/(2*pi) points, using
L*gamma/pi>4. Thus

    Q >=[33/(16*pi*sqrt(3))]*(1/6-1/M)
       > (3/8)*(1/6-1/41)
        =35/656>1/20.                               (16)

For the strict coefficient comparison use pi<22/7, sqrt(3)<7/4;
their product is<11/2. All selected physical rows are interior.
This reuses the unsimplified C02 count and verifies its new domain.

## Remaining centers with middle angle: new full-arc count

Suppose gamma>=pi/6. Select every physical row

    pi/12<=b<=pi/6                                  (17)

and all periodic angles w in the two open arcs

    (gamma-b,gamma+b),
    (2*pi-gamma-b,2*pi-gamma+b),                     (18)

viewed on the circle. Since pi/6<=gamma<=pi/2, the first arc lies
inside(0,2*pi/3) and the second in its reflected half-circle. If
gamma=b=pi/6, zero is excluded by the open endpoint. The two arcs
are disjoint, and cos w is strictly between the targets (9).

Both vertical target cosines are >=cos(2*pi/3)=-1/2. Horizontally
the fixed periodic cosine lies between these targets and has the same
lower bound. Each actual numerator is therefore at least
(15/16)*(1/2)-1/4=7/32, with no coordinate interchange. The full
cosine span2*sin gamma*sin b is at most1. Equations(7)-(8) give

    d>=7/16.                                        (19)

There are at least M/12-1 physical rows. Each arc in (18) has length
2b>=pi/6, hence at least L/12-1 periodic points of either prescribed
parity. The two arcs count separate points with the same interior
physical coefficient1/N. Therefore

    Q >=(7/8)*(1/12-1/M)*(1/12-1/L)
      >=(7/8)*(29/492)^2
       =5887/1936512>1/512.                          (20)

For the final exact comparison, 512*5887=3014144>1936512.
This direct finite count has no dense-integral loss and no n64 premise.

## Exhaustion, interface and limitations

For each applicable interior projection, the center-index distance is
either1,...,4, or at least5; in the latter case gamma<pi/6 or
gamma>=pi/6. Equations(14),(16),(20) prove(4). Every noncorner odd
center has an applicable interior J or K, so the exact Delta identity
proves the stated noncorner consequence. The strict final floor does
not rely on omitting selection endpoints or polynomial collision terms.

A whole phase box can use the floor only with exact integer n>=41 and

    maxabs(alpha interval)+maxabs(beta interval)<=1/2.

The center's physical-domain guard still applies to its admissible
intersection. A box merely intersecting the radius diamond does not
qualify throughout the box. Actual corner classes require their own
predicate. No accepted checker/source/receipt is changed by this file.

This proves a mathematical lower premise. It does not prove that
S_upper-1/512 lies below the corner lower bound, a complete cover,
generic finite-certifier success, a global argmax degree, or any bound
below41. The known global2-40 range is unchanged. No empirical minimum,
parameter scan, native evaluation or numerical job is a proof premise.

## Checks and history

2026-11-06, rules/input `09cc533678a22b38f40b70be95426ebbe81faa93`.
Assigned Codex auxiliary developer, requested Sol xhigh; serving model
metadata unexposed. The gate preceded this proof freeze. All endpoint
and margin comparisons above are written rational inequalities; no
arithmetic script, kernel job or native job ran. Independent mathematical
review is pending; the developer cannot approve this premise for use.


## Root review closure — 2026-11-06

Distinct [D29 review](../independent-checks-D29-defect-floors.md), SHA256 `84fbde47c836c9d6689896b1610de3ef7d0628bf9722cf8ec7cafda16309b648`, accepts all three frozen scopes without unresolved findings. Root adopts the uniform1/512 floor from41, uniform1/20 from512, and guarded radius floor from41 at their exact physical/signed domains. No numerical job or generic finite instance is asserted. Reviewed prefix is preserved; final Claude audit remains separate.
