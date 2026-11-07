# PD-T?argmax-bridge-codex-C01-allclass-01 — Radius-half defect at every noncorner odd center

ID kind: PD-T.
Aliases: C01 allclass; parity-complete half-radius defect; analytic
noncorner projected-profile floor; fixed-second-variable horizontal bound.
Split from: none; domain/quantitative continuation of PD-T222/224/366
and N5-04, not a new cancellation mechanism.
Split into: none. N5's full quarter target and PD-T099 remain OPEN.

## Statement

Let n>=64 be an integer, m=n+1 and N=nm. Let 0<=J<=n, 0<=K<=m
be integers with J+K odd. Let alpha,beta be real and suppose

    rho=|alpha|+|beta|<=1/2,
    theta=(J*pi+alpha)/n in [0,pi],
    phi=(K*pi+beta)/m in [0,pi].                         (1)

For the corrected Padua kernel and exact projected defects defined
below, the following two statements hold:

    Q_v(K)>1/2048 whenever 1<=K<=m-1,
    Q_h(J)>1/2048 whenever 1<=J<=n-1.                    (2)

Consequently, if (J,K) is not a pair of endpoint indices, then

    Delta_JK>=max(Q_v(K),Q_h(J))>1/2048,
    lambda_n(cos theta,cos phi)<S_n(alpha,beta)-1/2048.  (3)

The center class excludes precisely actual nonnode corner centers,
since centers already have odd index sum. Their defect is zero at zero
phase. No claim is made for n<64 or rho>1/2. This is a finite analytic
inequality, with no asymptotic or measured premise.

## Definitions and assumptions

Use exact real arithmetic and the even-checkerboard Padua convention.
Let P_n=T_(n+1)+T_n and

    D_n(x,y)=[P_n(x)-P_n(y)]/(x-y),
    G_n(u,v)=D_n(cos u,cos v)-cos(nu).                  (4)

D_n has its polynomial divided-difference value when x=y. In particular
the highest exceptional mode remains in the first coordinate. Write
d(x,y)=|x|+|y|-|x+y|, and put

    Gamma^-={(r,s):0<=r<2n,0<=s<2m,r+s odd},
    u_r=(r*pi+alpha)/n, v_s=(s*pi+beta)/m,
    G_rs=G_n(u_r,v_s),
    S_n=(1/(2N))*sum_(Gamma^-) |G_rs|,
    Q_v(K)=(1/(4N))*sum_(Gamma^-) d(G_rs,G_(r,2K-s)),
    Q_h(J)=(1/(4N))*sum_(Gamma^-) d(G_rs,G_(2J-r,s)).   (5)

Indices in (5) are periodic modulo2n,2m. The reflected partner keeps
the same alpha,beta; no phase sign is changed. PD-T364 proves the exact
identity lambda=S_n-Delta and Delta>=Q_v,Q_h>=0, including physical
boundary points and all polynomial collisions.

## Status by part

Overall status: **PROVED**, analytic developer proof; distinct review
and the required later Claude audit are separate obligations.

| Mathematical part | Status | Evidence / limitation |
|---|---|---|
| Both projected floors in (2) | PROVED | Exact signed-half identities, all parity cases, finite selections/counts below |
| All admissible noncorner centers (3) | PROVED | Exhaustion by an interior K or an interior J |

Candidate disposition: retained domain/quantitative variant. This does
not prove a bound on the maximum of S_n or an argmax onset.

## Dependencies and sources

PD-T364, full phase-structure.md, supplies only the exact identities and
positive endpoint reflection multiplicities in (5). Its kernel convention
is PD-T101/185. PD-T222/224/366 and N5-two-phase-defect.md are the full-read
finite-block predecessors. All half-radius estimates are reconstructed
here, including the previously unstated center parities and the new
horizontal statement. N5's accepted distinct two-phase review was read;
its edge quantifiers are not expanded by citation alone.

The complete prospective gate, shortlisted idea records, alternatives
and kill criteria are in ../ideas/C01-allclass.md and
../attempts/C01-allclass.md. No external literature theorem or numerical
experiment is a premise, and no historical originality is claimed.

## Proof

### 1. Corrected numerator and folded projection normalizations

Put a=(cos alpha+cos beta)/2. If u=(p*pi+alpha)/n and
v=(q*pi+beta)/m with p+q odd, angle addition gives

    P_n(cos u)=(-1)^p[cos alpha*(1+cos u)-sin alpha*sin u],
    P_n(cos v)=-(-1)^p[cos beta*(1+cos v)+sin beta*sin v].

Subtract cos(nu)=(-1)^p cos alpha before dividing by2. At a regular
denominator the signed half kernel is

    [(-1)^p G_n(u,v)]/2=A(u,v)/(cos u-cos v),
    A(u,v)=a*(1+cos v)-(sin alpha/2)*sin u
                                      +(sin beta/2)*sin v. (6)

In particular the subtraction inside the signed half is cos(alpha),
not1. The total formulas (4)–(5) retain all polynomial collision values;
only the selected terms below use the quotient (6).

Let a_j=j*pi/n and b_k=k*pi/m. Let e_j and f_k be1 except for half
weights at their respective two endpoints. Folding only the second mesh
in Q_v and only the first mesh in Q_h gives the exact formulas

    Q_v=(1/N)*sum_(k=0)^m f_k
                   sum_(0<=r<2n,r+k=J mod2) d(V_+,V_-),
    V_±=[(-1)^r G_n(u_r,phi±b_k)]/2;                 (7)

    Q_h=(1/N)*sum_(j=0)^n e_j
                   sum_(0<=s<2m,s+j=K mod2) d(H_+,H_-),
    H_±=[(-1)^(J+j) G_n(theta±a_j,v_s)]/2.           (8)

For example the periodic second indices K+k,K-k in (5) form one
unordered reflection pair; the interior k values each represent both
orientations. This contributes factor2. Passing from G to signed halves
contributes another factor2 in d, since the common sign is immaterial.
Together these change1/(4N) into1/N; fixed endpoint rows have exactly
f_k=1/2. Formula (8) is identical with coordinates folded in the other
order, not with the kernel swapped. The indicated signs are common to
both members of each pair. Odd J+K gives r+K±k odd in (7), and
J±j+s odd in (8), so (6) applies.

Although (5) makes Q_v independent of J at fixed phases, its folded
parity r+k=J depends on K through J+K odd. For even n the edge indices
J=0,n are both even and allow only odd K. Thus J-independence alone
cannot transfer the N5 edge theorem to even K. The selections below
explicitly prove both parities. When n is odd the two edge indices have
opposite parities, but no transfer across physical phase signs is needed
either: all estimates below allow both signs of alpha and beta.

Since rho<=1/2,

    a>=1-(alpha^2+beta^2)/4>=15/16,
    (|sin alpha|+|sin beta|)/2<=1/4.                  (9)

Every numerator in (6) is therefore at least1/8 when its actual baseline
1+cos v is at least2/5, and at least7/32 when that baseline is at least
1/2. These estimates allow both sine signs independently and preserve the
fixed-v baseline in every horizontal pair.

A grid of spacing h has at least ell/h-1 points in any closed interval
of length ell: place its first point at distance<h from the lower end.
Periodic grids of fixed parity have spacings2*pi/n or2*pi/m. The selected
intervals below lie inside(0,pi), so every counted infinite-grid point
has an actual periodic representative. Endpoint half weights never occur
in the selected physical rows. Every unselected pair has nonnegative d.

### 2. Vertical endpoint-distance indices1–4, every center parity

Suppose s=min(K,m-K) is in{1,2,3,4}. Let l range over all integers

    3*n/8<=l<=n/2.                                    (10)

Use the following choices in (7), with b=k*pi/m:

| Position | eta | r,k | w,t | m(w-b) |
|---|---:|---|---|---|
| K=s, s odd |0| r=l,k=l | w=(l*pi+alpha)/n,t=(s*pi+beta)/m | l*pi/n+(m/n)*alpha |
| K=s, s even |1| r=l,k=l+1 | same | l*pi/n-pi+(m/n)*alpha |
| K=m-s, s odd |1| r=n-l,k=l+1 | w=(l*pi-alpha)/n,t=(s*pi-beta)/m | l*pi/n-pi-(m/n)*alpha |
| K=m-s, s even |0| r=n-l,k=l | same | l*pi/n-(m/n)*alpha |

At the bottom phi=t,u_r=w. At the top phi=pi-t,u_r=pi-w;
the two target cosines are then -cos(b-t),-cos(b+t). Every index is
interior in its prescribed physical/periodic range. The base displacement
has absolute value at most5*pi/8. Also

    (m/n)*|alpha|+|beta|<=65/128<3*pi/8.

Hence |m(w-b)|<pi-|beta|<=s*pi±beta=m*t, so

    b-t<w<b+t.                                        (11)

Both folded target angles lie in[3*pi/10,3*pi/5]. Indeed

    b-t>=[(3*n/8-4)*pi-1/2]/m>=3*pi/10,
    b+t<=[(n/2+5)*pi+1/2]/m<=3*pi/5.                 (12)

After clearing m, the sufficient inequalities are
(3*n/40-43/10)*pi>=1/2 and(n/10-22/5)*pi>=1/2;
their worst n64 values are pi/2 and2*pi. On this interval both1-cos z
and1+cos z exceed2/5. For the lower endpoint,
cos(3*pi/10)=sin(pi/5)<3/5 follows from
sin^2(pi/5)=(5-sqrt5)/8<7/20<9/25. At the upper endpoint,
3*pi/5<2*pi/3 gives1+cos z>1/2. Thus (9) applies to both actual
vertical target baselines, top and bottom.

The denominators are strictly nonzero and opposite by (11)–(12). Their
magnitudes are bounded by the full cosine span, at most2*t<27/m, since
2*m*t<=8*pi+1<27. Therefore each half magnitude exceeds m/216 and
the pair defect exceeds m/108.

Parity is explicit for every J. At the bottom r+k=eta mod2 and
odd J+s gives J=1-s=eta mod2. At the top r+k=n+eta mod2 and
odd J+m-s gives J=n+s=n+eta mod2. No use of J=0 or n occurs.
There are at least n/8-1>=n/16 distinct selected l, so (7) gives

    Q_v>(1/(nm))*(n/16)*(m/108)=1/1728>1/2048.        (13)

### 3. Vertical remaining centers and both shifted parities

If min(K,m-K)>=5, put gamma=min(phi,pi-phi). Then

    gamma>4*pi/n, gamma<=pi/2,                         (14)

because gamma>=(5*pi-1/2)/m and n*(pi-1/2)>4*pi for n>=64.
For phi=gamma use b=b'; for phi=pi-gamma use b=pi-b'. The latter
has cos(phi+b)=cos(gamma+b') and cos(phi-b)=cos(gamma-b'). Thus
the actual target cosines always equal cos(gamma±b'), and reflection
preserves physical row counts and weights. Sine signs are already covered
absolutely by (9).

For gamma<=pi/6 select

    pi/3<=b'<=pi/2, b'-gamma/2<=u_r<=b'+gamma/2.

The two folded target angles lie in[pi/6,2*pi/3], so both baselines
are at least1/2. The selected angle lies strictly between targets. Their
cosine span is at most2*gamma, hence each half magnitude is at least
7/(64*gamma) and d>=7/(32*gamma). There are at least m/6-1>=m/12
physical rows. In each, either required shifted parity has at least
n*gamma/(2*pi)-1>=n*gamma/(4*pi) representatives, by (14). Thus

    Q_v>=7/(1536*pi)>1/2048.                           (15)

For pi/6<=gamma<=pi/2 select

    pi/12<=b'<=pi/6, gamma-b'/2<=u_r<=gamma+b'/2.

The targets lie in[0,2*pi/3], the selected angle is strictly between
them and their cosine span is at most1. Thus d>=7/16. There are
at least m/12-1>=m/16 physical rows, since m>=65, and at least
n/24-1>=n/48 points of either shifted parity per row. Consequently

    Q_v>=7/12288>1/2048.                               (16)

Every selected u interval in these two constructions lies strictly inside
(0,pi). Since |alpha|<=1/2, indices outside0<=r<2n cannot place u_r in
these intervals. This justifies the unrestricted shifted-grid count.
At gamma=pi/6 both constructions work; all closed selection boundaries
retain strict separation from pole angles. Equations(13),(15),(16)
prove the first line of (2), including even K at even n.

### 4. Horizontal endpoint-distance indices1–4, fixed numerator

Suppose s=min(J,n-J) is in{1,2,3,4}. Let l range over integers

    3*m/8<=l<=m/2.                                    (17)

Use b=j*pi/n in this subsection and select in (8):

| Position | eta | periodic index s' and physical j | w,t | n(w-b) |
|---|---:|---|---|---|
| J=s, s odd |0| s'=l,j=l | w=(l*pi+beta)/m,t=(s*pi+alpha)/n | -l*pi/m+(n/m)*beta |
| J=s, s even |-1| s'=l,j=l-1 | same | pi-l*pi/m+(n/m)*beta |
| J=n-s, s odd |-1| s'=m-l,j=l-1 | w=(l*pi-beta)/m,t=(s*pi-alpha)/n | pi-l*pi/m-(n/m)*beta |
| J=n-s, s even |0| s'=m-l,j=l | same | -l*pi/m-(n/m)*beta |

At the bottom theta=t,v_s'=w; at the top theta=pi-t,v_s'=pi-w.
Every selected index is interior and e_j=1. The base displacement has
absolute value at most5*pi/8, and

    |alpha|+(n/m)*|beta|<=1/2<3*pi/8.

Thus |n(w-b)|<pi-|alpha|<=n*t and b-t<w<b+t strictly. The targets
b±t lie in[3*pi/10,3*pi/5], since

    b-t>=[(3*m/8-5)*pi-1/2]/n>=3*pi/10,
    b+t<=[(m/2+4)*pi+1/2]/n<=3*pi/5.                 (18)

After m=n+1 is inserted, the sufficient inequalities become
(3*n/40-37/8)*pi>=1/2 and(n/10-9/2)*pi>=1/2.
Their worst n64 values are7*pi/40>1/2 and19*pi/10>1/2;
both left sides increase with n. These bounds also put the intervening
w in the same interval.

The horizontal numerator is exactly

    a*(1+cos v_s')+(sin beta/2)*sin v_s'
                           -(sin alpha/2)*sin(theta±a_j).

Its common baseline is1+cos w at the bottom or1-cos w at the top.
By (18) and the elementary bounds following(12), both exceed2/5.
This uses the fixed second angle, preserving the exceptional x mode;
it does not swap the meshes or apply a vertical target baseline to a
horizontal numerator. Therefore both actual numerators are at least1/8.
The cosine denominators are opposite and regular and their span is
at most2*t<27/n. Each pair has d>n/108.

At the bottom s'+j=eta=1-s=K mod2. At the top s'+j=m+eta,
and odd J+K with J=n-s gives K=m+s=m+eta mod2. Here eta=0,-1
has exactly the indicated parity in each table row. Thus every selection
belongs to (8), including both endpoint K classes. At least
m/8-1>=m/16 distinct l contribute, giving

    Q_h>(1/(nm))*(m/16)*(n/108)=1/1728>1/2048.        (19)

### 5. Horizontal remaining centers and adaptive counts

If min(J,n-J)>=5, put gamma=min(theta,pi-theta). Then
gamma>=(5*pi-1/2)/n>4*pi/m and gamma<=pi/2.
For theta=gamma use a_j=a'; for theta=pi-gamma use a_j=pi-a'.
The actual first-coordinate target cosines in either case are exactly
cos(gamma±a'). The periodic second coordinate remains v_s.

For gamma<=pi/6 select

    pi/3<=a'<=pi/2, a'-gamma/2<=v_s<=a'+gamma/2.

The selected v interval lies in[pi/4,7*pi/12], so its fixed baseline
1+cos v is at least1/2. Both numerators are at least7/32. The angle
v_s lies strictly between the two folded targets and their cosine span
is at most2*gamma. Hence d>=7/(32*gamma). The physical row count
is at least n/6-1>=n/12. Either required second parity contributes
at least m*gamma/(2*pi)-1>=m*gamma/(4*pi) representatives. Thus

    Q_h>=7/(1536*pi)>1/2048.                           (20)

For pi/6<=gamma<=pi/2 select

    pi/12<=a'<=pi/6, gamma-a'/2<=v_s<=gamma+a'/2.

Again v_s<=7*pi/12<2*pi/3, so the fixed baseline is at least1/2.
Strict target separation and cosine span at most1 give d>=7/16.
There are at least n/12-1>=n/16 physical rows and
m/24-1>=m/48 periodic representatives of either parity. Hence

    Q_h>=7/12288>1/2048.                               (21)

All selected v intervals lie in(0,pi), and |beta|<=1/2 guarantees
every counted point is represented by0<=s<2m. The reflected a' mesh
has the same spacing and interior weights. Closed band endpoints and
gamma=pi/6 retain positive separation. This proves the second line of(2).

### 6. Exhaustion and strictness

Every noncorner odd center has an interior K or an interior J. Apply
the corresponding line of(2) and PD-T364's exact identity to obtain(3).
Both adaptive case floors are strictly greater than1/2048:
7/12288>6/12288=1/2048, and pi<4 already gives
7/(1536*pi)>7/6144>3/6144=1/2048. The near floors are strictly
greater by(13),(19). Thus no closed phase/selection boundary loses the
strict final margin. This completes the proof.

## Quantitative checker interface and limits

For a phase box [a_l,a_h]x[b_l,b_h], an exact or outward validated check

    max(|a_l|,|a_h|)+max(|b_l|,|b_h|)<=1/2,
    integer n>=64,

is sufficient to use d_lower=1/2048 for every admissible noncorner
class throughout the box. A box partly outside a boundary center's
physical domain still has the same bound on its admissible intersection.
If no class is admissible the old vacuous handling can remain separate.
The two true-corner classes must retain their own predicate; (3) cannot
replace it. Outside this radius/degree scope the numerical all-class
screen or another proved predicate is still needed. A box merely
intersecting the half diamond is insufficient to apply the constant on
the entire box unless only that intersection is being certified.

This replaces the n-growing projected-profile scan on these boxes with
a constant-size logical premise. It does not remove the O(n^2) primitive
board, establish total certifier complexity, or prove a useful box-count
law. A stricter comparison than S_upper-1/2048<Lc_lower may still require
the numerical profiles. No existing checker or accepted receipt is
changed by this mathematical file; independent review precedes use.

No primitive upper comparison, effective argmax onset, all-degree E-C,
new finite degree or PD-T099 conclusion is asserted. The exact global
range stays2–40. Fixed finite energy2–128 supplies no extrapolation.
N5's Q_v>=1/4 target remains OPEN; its failed phase-blind certificate
is neither revived nor contradicted by the much smaller floor here.

## Checks and open items

Analytic proof only at initial freeze. The decisive checks are the exact
parity identities, the n64 endpoint inequalities and the monotone
degree dependence written above. No numerical measurement is a premise.
The candidate permits a bounded diagnostic, separately labeled MEASURED;
any such execution is recorded in the attempt file. Distinct mathematical
review and the required later Claude audit remain separate. Any checker
implementation must independently validate the exact domain guard.

## History

2026-11-06. Codex auxiliary mathematical developer, requested Sol xhigh;
serving metadata unexposed. Rules/input
4b728b04216a5490910780bc609a82b853058426; main
f654e32daff27b6846849311092f6daebbbf235b. Prospective candidate and
scope in ideas/C01-allclass.md preceded this proof. Vertical proof is a
parity-complete reconstruction of N5's selected geometry; horizontal
half-radius proof is new quantitative development of PD-T224/366's fixed
numerator selections. Only assigned new files were written; no Git,
shared record, old proof, checker premise or external message changed.

