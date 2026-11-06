# PD-T?argmax-bridge-codex-D05-outer — Full-phase regularized outer variation

ID kind: PD-T. Aliases: combined endpoint residual BV; shrinking-cell
profile quadrature; endpoint and central logarithm subtraction.
Split from: D04's practical joint finite-degree M_infty target, OPEN.
Split into: none. This supporting result does not resolve that target.

## Statement and exact definitions

Let alpha,beta>=0, alpha+beta<=pi, and set

    a=(cos alpha+cos beta)/2, p=sin alpha, q=sin beta,
    P=p+q, d=(q-p)_+, c_e=cos((alpha+beta)/2),
    c_d=cos((alpha-beta)/2),
    C(v)=(p-q-2a cot(v/2))/4,
    D(v)=(p+q+2a cot(v/2))/4.

Use precisely the actual weighted N1-04/05 profile H(L,v)=A(v)L+B(v)
from D04-row-reduction.md, its continuously periodic Phi_0, and

    v_L(z)=z, v_R(z)=2pi-z,
    eta_-(v)=1/2+(alpha-beta+v)/(2pi),
    eta_+(v)=1/2+(alpha+beta-v)/(2pi),
    N_s(z)=c_e Phi_0(eta_-(v_s(z)))
                       +c_d Phi_0(eta_+(v_s(z))),
    U0=N_L(0)=N_R(0),
    I_s(z)=I(C(v_s(z)),D(v_s(z)),v_s(z)),
    B(v_s(z))=N_s(z)/[2sin(z/2)]+I_s(z)/pi,
    I(C,D,v)=integral_0^pi
        (|C cot x+D cot(x+v)|-|C cot x|-|D cot(x+v)|)dx.

Values at the finitely many integral poles are immaterial. For 0<z<pi
define the exact references and regularized profile

    T_L(z)={U0+(4a/pi)(L+log z)}/z,
    F_s(L,z)=H(L,v_s(z))-T_L(z)-(d/pi)log(pi-z).        (1)

Here T_L's subscript denotes its dependence on the scalar L, not the
left folded side. This is an analytic subtraction, not a new model
term or a change to M_far or M_infty. At z=pi use the continuous
regularized limit; it is not an actual polynomial collision-row value.

For 0<epsilon<=pi/4, put

    u=p/2, S=1/2+2a/epsilon, ell=-log(sin epsilon),
    G=2u[1+log((S+u)/u)] if u>0, G=0 if u=0,
    V_A=2max(p,q)/pi+8a/pi^2,
    V_B=23+{3G+(2p+6P)ell+26a+20+2d log2}/pi.

For every L>=0, on the FULL closed phase triangle,

    sum_s Var_[epsilon,pi] F_s(L,.) <= L V_A+V_B,
    V_A<3/2,   V_B<=41+6log(6/epsilon).                (2)

Consequently, for any two unions U_s of disjoint centered cells of
width h=pi/m contained in [epsilon,pi], with centers z_j,

    |(1/m)sum_s sum_j F_s(L,z_j)
               -(1/pi)sum_s integral_(U_s) F_s(L,z)dz|
                           <=[L V_A+V_B]/(2m).        (3)

In particular let R>=2, n>=8R, m=n+1, L=log n, and use exactly the
ordinary rows O complementary to D04's special set A_R. Fold the rows
at pi, use their actual centered cells, and put
epsilon=pi(R-1/2)/m. Then their cells satisfy the hypotheses and (3) is
at most

                         (4log n+25)/(n+1).           (4)

The quadrature statement covers only the displayed regularized profile
on its actual cell union. It does NOT replace that union by [0,pi],
approximate exact special rows, or compare singular references with
their global harmonic/log mesh constants.

### Signed endpoint-strip corollary

Let R>=2, 0<delta<=pi/8, n>=ceil(2pi R/delta), m=n+1,
h=pi/m, t_L=beta/pi, t_R=1-beta/pi. Put

    Z_s(z)=B(v_s(z))-[U0+(4a/pi)log z]/z,
    K_s=floor(delta/h-t_s),
    Y_s={k:R<=k<=K_s and the corresponding row is not a collision},
    epsilon=h(R-1/2), lambda=h(R+1/2),
    W_P(z)=7+(P/pi)[3+2log(4pi/z)],
    Q(P,z)=(2z/pi)[7+(P/pi)(5+2log(4pi/z))],
    T_Z={32+6log(6/epsilon)}/(2m)+Q(P,lambda)
                   +{W_P(delta-h/2)+2W_P(hR)}/m.      (TZ)

Then, with all floors and collision holes retained literally,

    |(1/m)sum_s sum_(k in Y_s) Z_s(h(k+t_s))
               -(1/pi)integral_0^delta (Z_L+Z_R)dz|<=T_Z. (strip)

For fixed R,delta the bound T_Z is O((1+log n)/n), uniformly in phase.
There is no fixed-delta Q floor in (strip).

## Status, dependencies and domain conventions

Status: **PROVED**, written analytic developer result, distinct review
pending. No numerical premise. The practical small-onset comparison remains
**OPEN**, not PARTIAL.

- N1-04/05 supply the actual weighted profile and endpoint reference.
- C06-far-compact-error.md sections 1--2 prove on the full phase triangle
  the numerator regular variation <23, the generic cancellation formulas,
  and the central residue variation <20. Their full-domain constants,
  rather than the near-only N1-13/14 constants, are used below.
- The exact max formulas of N1-06/N1-13 are algebraic on this full domain;
  the parameter bounds are re-evaluated here using p,q<=1, not <=1/2.
- D04's exact ordinary/special topology is used only for (4), not (2).
  Its three support proofs were pending at the D05 gate; root subsequently
  reported distinct Astra xhigh acceptance unchanged, in
  independent-checks-D04-row-reduction.md, SHA256
  `cacbab625421e4d269bc2a3047aa523caee8c4f08a709748721291178f9976d7`.

The inherited separate phase evenness extends the statement to the
closed diamond |alpha|+|beta|<=pi by evaluating every coefficient at
(|alpha|,|beta|). The coordinate meshes are not interchanged. No signed
phase relabeling beyond that exact inherited symmetry is introduced.

## Proof

### 1. Remove the large endpoint coefficient before variation

For 0<z<=pi/2 put w=a cot(z/2), u=p/2. The actual coefficients and the
coefficient-swap/sign/separation invariances of I give exactly

    I(C(v_s(z)),D(v_s(z)),v_s(z))=J(u,s_s(z),z),
    J(u,s,z)=I((u-s)/2,(u+s)/2,z),
    s_L=w+q/2, s_R=|w-q/2|.                          (5)

For example the left coefficients already equal (u-s_L)/2,(u+s_L)/2.
On the right their difference parameter is q/2-w; coefficient exchange
changes its sign and separation reflection replaces 2pi-z by z.
These operations preserve I, so the absolute value in s_R is exact.

The generic identity, including its continuous coefficient-root limits,
is

    J=2(s-u)_+ log(sin z)+R(u,s,z),
    |R_s|<=log((u+s)/|u-s|),
    0<=R_z=2[u cos z-sqrt((u^2-s^2 sin^2 z)_+)]/sin z
                                      <=2u cot z  (s>u),
    R_z=0                                           (s<=u). (6)

At u=0 the remainder R vanishes identically, and no division by u is
used. For u>0 its parameter derivative has only an integrable logarithm
at s=u. The square-root/root/no-root formulas join continuously. Thus
(6) is not a Taylor expansion through moving zeros.

Subtract J0(z)=2w log(sin z) BEFORE taking variation. The resulting
logarithmic coefficients are exactly

    I_s-J0=k_s log(sin z)+R(u,s_s(z),z),
    k_L=max(q-p,-2w),
    k_R=max(-P,q-p-4w,-2w).                           (7)

Because w decreases, both k_s increase. Each lies in [-P,P], so the
sum of their variations is <=4P and the sum of their sup norms <=2P.
Consequently the product terms in (7) have total variation <=6P*ell
on [epsilon,pi/2]. This is where the separate O(a/epsilon) coefficient
bound is avoided.

Both s curves lie in [0,S], since cot(epsilon/2)<=2/epsilon and q<=1.
The left curve is monotone; the right has at most two monotone pieces.
Also S>=u. The elementary integral bound

    integral_0^S log((u+s)/|u-s|)ds
                       <=2u[1+log((S+u)/u)]=G

bounds their combined parameter-motion contribution by 3G. Integrating
the last inequality in (6) along the two curves contributes at most
2p*ell. Partitioning at the finitely many coefficient/root transitions
and passing by the displayed integrable bounds justifies the variation
estimate even when a transition is an endpoint. Thus

    sum_s Var_[epsilon,pi/2](I_s-J0)
                             <=3G+(2p+6P)ell.        (8)

### 2. Compare J0 with the exact singular endpoint reference

Let Q_a(z)=J0(z)-4a log z/z. On [0,pi/2] write

    Q_a=f(z)log(sin z)+g(z),
    f(z)=2a cot(z/2)-4a/z,
    g(z)=4a log(sin z/z)/z.

These terms have continuous zero limits at zero. On this interval,
|f'|<=a and |f|<=az. Indeed, for x=z/2,
csc^2 x-1/x^2<1 follows from
sin x>=x(1-x^2/6), x^2/6<1/8. Therefore

    Var(f log sin)<=a*integral_0^(pi/2) -log(sin z)dz
                         +a*integral_0^(pi/2) z cot z dz
                     <=a*(pi/2)(log2+1)<3a.

The elementary inequalities

    0<=1/z-cot z<=pi*z/6,
    0<=-log(sin z/z)<=z^2/(6-z^2)<=z^2/3

follow respectively from sin z>=2z/pi,
sin z-z cos z<=z^3/3, and sin z/z>=1-z^2/6.
Differentiating g now gives |g'|<=4a(pi/6+1/3), hence Var(g)<7a.
Thus Var(Q_a)<10a per side. Combining with (8),

    sum_s Var_[epsilon,pi/2](I_s-4a log z/z)
                        <=3G+(2p+6P)ell+20a.         (9)

### 3. Join the central subtraction and regular numerator

The full-phase C06 central result is

    sum_s Var_[pi/2,pi](I_s-d log(pi-z))<20,          (10)

with finite continuous limits at pi, including p=q, p=q=0 and a=0.
On [pi/2,pi], the variation of 4a log z/z per side is at most

    4a*(1+log pi)*integral_(pi/2)^pi dz/z^2
                      =4a(1+log pi)/pi<3a.

On [epsilon,pi/2], subtracting d log(pi-z) adds at most d log2 per
side. Thus the two-side variation of

    I_s-4a log z/z-d log(pi-z)

on [epsilon,pi] is at most the braces in V_B. There is no jump at
pi/2: all expressions there are the same continuous integral. The
regular numerator

    P_s(z)=N_s(z)/[2sin(z/2)]-U0/z

has total variation <23 on [0,pi] by C06's full-domain proof. This
proves the claimed V_B for the L-independent part of F.

For the coefficient of L the exact formulas are

    f_s(z)=A(v_s(z))-4a/(pi*z),
    pi*f_L=max(q,p-T)+u0,
    pi*f_R=max(-q,p-T,q-2T)+u0,
    T=2a cot(z/2), u0=T-4a/z.

The maxima increase and u0 decreases from zero to -4a/pi. The first
max changes by at most (p-q)_+, the second by max(p,q)+q; their sum
is <=2max(p,q). These remain upper bounds when a=0 and T is constant.
Hence sum_s Var(f_s)<=V_A<3/2 on the full domain.
Combining this with the L-independent bound proves the first part
of (2).

For the simpler uniform constants, epsilon<=pi/4<1 gives

    G<=p[1+log(6/epsilon)]+p log(1/p)
      <=p[1+log(6/epsilon)]+1/e,
    ell<=log(6/epsilon).

Use p<=1, P<=2, a,d<=1. The coefficient of log(6/epsilon) is at
most 3p+2p+6P<=17. The remaining braces are less than
3+3/e+26+20+2log2<52. Since pi>3,
23+52/pi<41 and 17/pi<6, giving the second part of (2).

### 4. Actual centered cells

On a centered cell of width h, integration of the left/right pointwise
variation bounds gives |h*f(center)-integral_cell f|<=h*Var_cell(f)/2.
Sum over disjoint cells and divide by pi to prove (3); holes do not
multiply the variation constant.

For the D04 row topology put t=beta/pi in [0,1]. Left ordinary centers
have z=h(r+t), r>=R, r<=m-2. Right ordinary centers have
z=h(k+1-t), k>=R, and z<=pi-h. The central rows r=m-1,m are exact
special rows. Their ordinary centered cells therefore lie inside
[h(R-1/2),pi]. Added collision rows delete cells and preserve this
property. This also covers t=0 and t=1 without changing a floor or
assigning a limiting unweighted pole value.

For n>=8R, epsilon=h(R-1/2)<=pi/4. Since R>=2,
6/epsilon<=4m/pi<2m. Also n>=16 and 2m/n<=17/8<e, so
log(2m)<=log n+1. Inserting these inequalities into (3) gives
[7.5log n+47]/(2m)<(4log n+25)/m, proving (4).

For the strip corollary use the UNDELETED cells R<=k<=K_s first.
Their left endpoints l_s=h(R+t_s-1/2) are <=lambda, and their right
endpoints u_s=h(K_s+t_s+1/2) satisfy |u_s-delta|<=h/2 exactly,
without replacing a floor. The degree condition gives h<=delta/(2R).
Thus these cells lie in [epsilon,pi/4], lambda<=5delta/8, and
delta-h/2>0. Equations (8)--(9), plus the numerator variation, bound
the combined variation of Z_s on their cells by

    23+{3G+(2p+6P)ell+20a}/pi
                         <=32+6log(6/epsilon).

Centered-cell quadrature pays the first term of T_Z. The N1-05
envelope |Z_s(z)|<=W_P(z) bounds the two initial integrals (0,l_s)
by Q(P,lambda). The two upper mismatches have combined length <=h
and pay W_P(delta-h/2)/m. Finally delete the at most two collision
sample terms: every such sample has z>=hR, so the loss is bounded
by 2W_P(hR)/m. This proves (strip). Only ordinary profile samples were
inserted temporarily; no actual collision polynomial value was
replaced. Each displayed term has the claimed fixed-parameter rate.

## Scope, checks and unresolved obligations

This is a pointwise full-phase analytic quadrature lemma. It has no
inverse a, p, d or phase-distance constant. At a=0 its formulas are
literal; at p=0 G=0 is the continuous limit. Coefficient switches and
moving integral roots were handled by integrable derivative bounds.
The endpoint references remain singular and are subtracted algebraically;
their actual finite weighted pole products and exact polynomial special
rows have not been replaced by separately evaluated pole limits.

The cell-union result alone does not compare K_D04 with M_infty. The
signed strip corollary instead permits a cheaper assembly at FIXED
delta using the old endpoint block, rather than replacing that block's
e_mesh by its value at delta~R/n (which leaves a nonshrinking CX term).
The separate D05-outer-comparison.md records any completed assembly.
The practical small-onset target is still OPEN; no phase cover,
certifier, argmax or threshold change follows here. No second near
correction is introduced.

Checks: analytic derivation only. No scalar numerical code, native
kernel, board calculation, quadrature, fitting or phase-cover run.
Independent adversarial review remains required for this new lemma.

History: 2026-11-06, Codex Sol xhigh at parent request, input
`a6d7a788b3ce457a4631bbb507624303240c570c`. The original practical
target was not narrowed; this is a split supporting claim only.
