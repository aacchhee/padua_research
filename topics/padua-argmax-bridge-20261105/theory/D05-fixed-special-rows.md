# PD-T?argmax-bridge-codex-D05-fixed — Fixed exact rows by weighted continuity

ID kind: PD-T. Aliases: collision-free dense-phase extension; fixed
special-row set; periodic weighted-Phi continuation; continuous bounded
cancellation integral. Split from: the D04 full-phase row reduction.
Split into: none. This is a new model, not a correction of D04.

## Statement and definitions

Fix integers R>=2 and n>=8R, and set m=n+1 and L=log n. On the closed
phase triangle

    T={alpha,beta>=0 : alpha+beta<=pi},

use the corrected finite polynomial and actual row norms

    a=(cos alpha+cos beta)/2,
    p=sin alpha, q=sin beta, P=p+q,
    h_0=1, h_i=2 for i>0,
    D_n(u,v)=sum_{i+j<=n} h_i*h_j*cos(iu)*cos(jv),
    G_n(u,v)=D_n(u,v)-cos(nu),
    delta_r=(1-r) mod 2,
    u_rk=(delta_r*pi+alpha+2k*pi)/n,
    v_r=(r*pi+beta)/m,
    F_rk=(-1)^delta_r*G_n(u_rk,v_r)/2,
    R_r=sum_{k=0}^{n-1}|F_rk|,
    S_n=(nm)^-1 sum_{r=0}^{2m-1}R_r.

In particular the exceptional highest first-coordinate mode is part of
each retained exact polynomial row. Define the phase-independent sets

    A_fixed={0,...,R-1} union {2m-R,...,2m-1} union {m-1,m},
    O_fixed={0,...,2m-1} minus A_fixed.                 (1)

For 0<v<2pi, v!=pi, use exactly D04's actual weighted profile:

    c_e=cos((alpha+beta)/2), c_d=cos((alpha-beta)/2),
    eta_-(v)=1/2+(alpha-beta+v)/(2pi),
    eta_+(v)=1/2+(alpha+beta-v)/(2pi),
    C_v=(p-q-2a cot(v/2))/4,
    D_v=(p+q+2a cot(v/2))/4,
    g(C,D,v;X)=|C cot X+D cot(X+v)|-|C cot X|-|D cot(X+v)|,
    I(C,D,v)=integral_0^pi g(C,D,v;X)dX.

The integral has the ordinary bounded piecewise meaning, with arbitrary
values at its finitely many pole points. Section 2 proves the boundedness
needed here. With psi the digamma function, put

    Phi_L(t)=sin(pi*t)[2L-psi(t)-psi(1-t)-2log pi]/pi,
                                                        0<t<1,

and extend this function periodically and continuously, setting
Phi_L(integer)=1. Thus the sine in the displayed interval is nonnegative;
one does not use an unperiodized signed sine at other arguments. Define

    H(L,v)=[c_e Phi_L(eta_-(v))+c_d Phi_L(eta_+(v))]
                         /[2sin(v/2)]+I(C_v,D_v,v)/pi. (2)

At an integer offset, (2) means the value of the whole weighted Phi
factor. It never assigns a value to a separately unweighted 0*psi term.

For completeness, retain D04's exact continuous endpoint constant in
its absolutely convergent series form. Let x=alpha/pi, t=beta/pi and,
for j>=2 and x+|s|<=1, set

    q_+=(1+s+x)/2, q_-=(1+s-x)/2,
    B_j(s)=psi(j+q_+)+psi(j+q_-)-2log(j+s),
    Xi_j(s)=(2a/pi^2)*B_j(s)/(j+s),
    Delta_R=sum_{j=R}^infinity[Xi_j(t)+Xi_(j+1)(-t)]. (3)

This is exactly E_infty-E_R of D04-reference-matching.md; there is no
new cutoff constant. The new model is

    K_fixed=(nm)^-1 sum_{r in A_fixed}R_r
                      +(1/m)sum_{r in O_fixed}H(L,v_r)+Delta_R. (4)

All rows in O_fixed use their actual weighted value (2), even when
u_rk-v_r or u_rk+v_r belongs to 2pi*Z for some k. No moving collision
rows are added to (1).

Then, throughout T,

    |S_n-K_fixed|<=E_D04(n;alpha,beta),                 (5)
    E_D04={ [52a/pi^2+352P/(3pi)]H_n+7a+2P/pi }/n
                                +10/n^2+20a H_n/(pi*n^2),
    H_n=sum_{k=1}^n 1/k.                              (6)

The bound is exactly the accepted D04 error, with no additional
collision charge. Extend K_fixed and E_D04 by separate absolute phases;
then (5) holds on the whole closed diamond |alpha|+|beta|<=pi.

The three sets in A_fixed are disjoint, so |A_fixed|=2R+2. In particular
R=2 and n>=16 leave exactly six fixed exact row labels and 2n-4 ordinary
profile labels. This is an O(n) outer-row count, with no assertion about
operation count, bit cost, runtime, validated evaluation or argmax onset.

Status: **PROVED**, analytic developer contract; distinct independent
review pending. No compact S_n-M_infty rate is asserted.

## Dependencies and frozen input

The accepted D04 theorem is used only at phases with no actual
polynomial collision. Its three proof files are unchanged:

- D04-half-line-defect.md, SHA256
  `593c7e32f2cd4f83a68507e8c25ca26ca7f8e45e4735e20d373cc3efe3404e6f`.
- D04-reference-matching.md, SHA256
  `bb89a7e3c3b3c174c877e465500ddfd033ceba00e2e578aeae0151856024c622`.
- D04-row-reduction.md, SHA256
  `2eed7940022efbc0e018ddf6a06da68bb2b40d947af305e28d641c5d4b3050cf`.

Root reported their distinct Astra xhigh acceptance in
independent-checks-D04-row-reduction.md, frozen SHA256
`cacbab625421e4d269bc2a3047aa523caee8c4f08a709748721291178f9976d7`.
The proof below uses D04-reference-matching's bound (5) on Xi, N1-04's
periodic weighted Phi extension and N2's separate evenness of S_n.
C06's one-sided collision continuation is a close predecessor, not the
two-sided statement (5). No old theorem or obstruction is revised.

## Proof

### 1. Uniform separation of every fixed ordinary row

Fix r in O_fixed. Its index satisfies

    R<=r<=2m-R-1, r not in {m-1,m}.

Since 0<=beta<=pi, either r<=m-2 and

    R*pi/m<=v_r<=(m-1)*pi/m,

or r>=m+1 and

    (m+1)*pi/m<=v_r<=(2m-R)*pi/m.

Consequently, uniformly over the entire closed triangle,

    dist(v_r,pi*Z)>=pi/m,
    R*pi/m<=v_r<=2pi-R*pi/m,
    sin(v_r/2)>=sin(R*pi/(2m))>0,
    |cot(v_r/2)|<=cot(R*pi/(2m)).                    (7)

This proves that (2) is defined on every required row, including all
closed phase edges and vertices. Since 0<=a<=1 and 0<=P<=2 on T,

    max(|C_vr|,|D_vr|)<=M_(n,R),
    M_(n,R)=[1+cot(R*pi/(2m))]/2.                   (8)

The constants in (7)-(8) may depend on fixed n,R. Continuity here needs
no bound uniform as n tends to infinity.

### 2. Continuity of the cancellation integral through all collisions

For finite real A,B, the triangle defect is exactly

    |A+B|-|A|-|B|=-2min(|A|,|B|) if AB<0,
                    0 if AB>=0.

Thus, away from the two pole sets, with M=max(|C|,|D|),

    |g(C,D,v;X)|<=2M min(|cot X|,|cot(X+v)|).       (9)

Let e=dist(v,pi*Z)>0. On the circle of circumference pi, the triangle
inequality implies

    e<=dist(X,pi*Z)+dist(X+v,pi*Z).

At least one of the two distances is therefore at least e/2. Because
|cot Y|=cot(dist(Y,pi*Z)) and this cotangent decreases for distances in
(0,pi/2], (9) yields

    |g(C,D,v;X)|<=2M cot(e/2).                    (10)

In particular, for a fixed ordinary row over all T, choose value zero
at the finitely many pole points. Equations (7)-(10) give the uniform
integrable majorant

    |g(C_vr,D_vr,v_r;X)|
                <=2M_(n,R) cot(pi/(2m)), 0<=X<=pi. (11)

Changing those values on a finite set has no effect on I. This choice
is only an integral representative; it is never a definition of a
sampled polynomial value.

Now let phases (alpha_j,beta_j) in T approach (alpha_0,beta_0). Their
coefficients and v_r converge continuously. Except at the finite set
where X or X+v_r(alpha_0,beta_0) is a multiple of pi, the cotangents
are finite in a neighborhood of the limit and the integrands converge
by continuity of absolute value. Dominated convergence using (11)
therefore gives

    I(C_vr(alpha_j,beta_j),D_vr(alpha_j,beta_j),v_r(alpha_j,beta_j))
       ->I(C_vr(alpha_0,beta_0),D_vr(alpha_0,beta_0),v_r(alpha_0,beta_0)).

This proves the required phase continuity. The estimate contains no
division by a, C, D or CD. It applies unchanged when either coefficient
vanishes, when both vanish, or when their signs change. Moving a sample
onto a pole does not change this argument: its conclusion concerns the
ordinary cancellation integral, not a pointwise extension of g at that
sample.

### 3. Continuity of both complete sides of the proposed inequality

For fixed L the weighted Phi function is continuous on the circle.
Indeed N1-04 proves that the digamma singularities have weighted limit
1 at either end of (0,1); explicitly the singular part is 1/t+O(1)
at t down to zero and 1/(1-t)+O(1) at t up to one. Multiplication by
sin(pi*t)/pi gives 1 in both cases, while the finite 2L term vanishes.
Periodic extension with integer value 1 is therefore continuous even
when an offset crosses an integer. Since c_e,c_d,eta_-,eta_+ are
continuous and the denominator is uniformly positive by (7), section 2
now proves that each complete H(L,v_r), r in O_fixed, is continuous
on T.

Each R_r and S_n is continuous: it is a finite sum of absolute values
of finite trigonometric polynomials evaluated at continuously moving
mesh angles. This includes the actual collision values directly from
G_n; no rational or cotangent representation is needed for that claim.

For (3), every summand is continuous on T: j+s is positive and the
digamma arguments j+q_+,j+q_- are positive. The accepted reference
bound is

    |Xi_j(s)|<=4a/[pi^2*(j+s)^2].

For t in [0,1], j+t>=j and j+1-t>=j. Consequently

    |Xi_j(t)+Xi_(j+1)(-t)|<=8/(pi^2*j^2),           (12)

uniformly on T. The convergent numerical series in (12) proves uniform
convergence of (3), hence continuity of Delta_R on T, including its
vertices. Formula (6) is continuous as well. Because the index sets
(1) are fixed, K_fixed is continuous on all T.

### 4. Dense-phase extension of the unchanged D04 inequality

For fixed r,k and either sign, an actual polynomial collision is the
condition

    (delta_r*pi+alpha+2k*pi)/n +/- (r*pi+beta)/m=2ell*pi.

For each relevant integer ell this is a nonconstant affine equation
in alpha,beta. The phase triangle is compact, the index sets are finite,
and the left side is bounded there, so only finitely many ell occur.
All collision phases lie in a finite union of affine lines. Its
complement in the open phase triangle is dense in T: every relative
neighborhood of a boundary point meets an open interior wedge, and
finitely many lines cannot contain that open set. In particular every
point of T is the limit of an interior sequence having no collision
on any polynomial row.

At each such collision-free phase, D04's special set is exactly
A_fixed. Its K_D04 is therefore exactly (4) at that phase, and its
accepted theorem gives (5) with exactly (6). Given any target point
of T, take a collision-free approximating sequence. Section 3 proves
continuity of S_n, K_fixed and E_D04, so passing to the limit proves
(5) at that point. This proves the whole closed triangle.

The moving-membership model K_D04 itself is not passed to the limit.
Only its collision-free identity with the new continuous K_fixed is
used. In particular no claim that K_D04=K_fixed at a collision, no
rowwise equality R_r/n=H there, and no pointwise collision estimate for
the D04 reference sample are required. D04's original omission charges
remain a permitted conservative part of the unchanged bound (6).

### 5. Signs, boundaries and the row count

The inherited exact polynomial sum S_n is separately even in alpha
and beta. Define the new model outside T by

    K_fixed(alpha,beta)=K_fixed(|alpha|,|beta|),
    E_D04(alpha,beta)=E_D04(|alpha|,|beta|).

The triangle result therefore proves (5) on all four sign sectors of
the closed diamond. This includes its axes, oblique boundary and
vertices. The argument does not interchange the unequal n and m
coordinate meshes.

Since m=n+1>=8R+1, the central pair {m-1,m} is disjoint from the
first and last R labels, and those endpoint label sets are disjoint
from one another. Thus (1) contains exactly 2R+2 labels. At R=2 the
six labels are {0,1,2m-2,2m-1,m-1,m}; the remaining count is
2m-6=2n-4. There are at most 2(n+1) profile terms. Each retained exact
row still has n polynomial samples, and no claim about its evaluation
cost or that of (2)-(3) follows from this count.

## Explicit double-collision consistency check

One important degenerate case illustrates why weighted continuation
is necessary. Set alpha=0, beta=b with 0<b<pi, and suppose a row has
v_r=pi+b. Then

    p=0, q=sin b, a=(1+cos b)/2,
    2a cot(v_r/2)=-sin b,
    C_vr=D_vr=0,
    eta_-(v_r)=1, eta_+(v_r)=0,
    c_e=c_d=sin(v_r/2)=cos(b/2).

Hence the integral is zero but the actual weighted profile is H=1,
not zero, because both integer Phi values are 1. For instance n=16,
R=2,b=7pi/8 gives m=17,r=31, outside the six fixed exact labels.
The exact finite-polynomial double-collision row R_r=n is established
in the corrected N1-08 endpoint proof; its z=pi-b=pi/8 lies in that
proof's allowed endpoint strip. This algebraic illustration is not
needed for the dense-phase proof, but explicitly guards against an
unweighted 0 times singular-function substitution.

## Scope, verification and provenance

This is a new exact-real mathematical contract for a fixed-row model.
It supplies no interval evaluator, outward error allocation, quadrature
algorithm, implementation cost, compact M_infty remainder, phase cover,
global argmax threshold or validated producer. Such downstream work
must retain the complete weighted functions and the actual corrected
polynomial values on the six rows when R=2.

No numerical helper, native computation, board evaluation, quadrature,
fit or cover was executed. The proof uses only finite-polynomial
continuity, the accepted D04 bound, uniform row separation, an explicit
cotangent cancellation majorant, the existing periodic weighted Phi
extension and uniform convergence of the exact Delta_R series.

2026-11-06. Rules/input HEAD
`41c4c804456fbaf952dda344a5ff9795a0252f64`. Parent-assigned Sol xhigh
analytical block, serving metadata not independently exposed. The
candidate and canonical freshness/timing qualification are recorded in
the new owned idea/attempt. Root owns Git and shared records. Distinct
review of frozen hashes is required; developer status is not reviewer
acceptance. Original D04 files and their accepted report stay frozen.
