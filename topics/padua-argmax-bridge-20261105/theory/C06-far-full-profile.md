# PD-T?argmax-bridge-C06-far-profile — A full-diamond upper with constant remainder

ID kind: PD-T.
Aliases: one-sided global log-graded profile; H4 far-budget reuse;
full-phase linear logarithmic coefficient.
Split from: the effective far comparison in ideas/C06-far.md.
Split into: the far comparison is a separate application.

## Statement

Let n>=10^6 be an integer, m=n+1, L=log n, and let S_n be the corrected
odd-board primitive of PD-T216/N2-01. For every real phase pair with
|alpha|+|beta|<=pi, put x=|alpha|, y=|beta| and

    a=(cos x+cos y)/2,
    c_e=cos((x+y)/2), c_d=cos((x-y)/2),
    U0=c_e Phi_0(1/2+(x-y)/(2pi))
                      +c_d Phi_0(1/2+(x+y)/(2pi)),
    b_full=2U0/pi+[8a log2+4a loga
                         +2(x sin x+y sin y)]/pi^2.             (1)

Here Phi_0 is exactly the continuous, periodic profile in N1-04, and
0 log0 means zero. Then

    S_n(alpha,beta) <= (4a/pi^2)L^2+b_full L+200,                (2)
    b_full < 8/3.                                              (3)

The coefficient in (1) is continuous on the closed diamond. On x+y=pi
it is exactly 4 sin x/pi, including value zero at the two vertices.
Every polynomial collision and both degree parities are covered.

## Definitions and assumptions

The finite kernel is

    D_n(u,v)=sum_{i+j<=n} h_i h_j cos(iu)cos(jv),
    G_n(u,v)=D_n(u,v)-cos(nu), h_0=1, h_i=2 for i>0.

The (n,0) coefficient of G is one. For
Gamma^-={(j,r):0<=j<2n,0<=r<2m,j+r odd}, set

    F_jr=(-1)^j G_n((j*pi+alpha)/n,(r*pi+beta)/m)/2,
    S_n=(nm)^-1 sum_{Gamma^-}|F_jr|.

All apparent rational singularities use this finite polynomial. Exact
real arithmetic; no fitted constant, sampled upper or energy premise.
Separate phase evenness permits x,y>=0. No coordinate-mesh exchange is
assumed. The symmetric expression (1) is a derived coefficient identity,
not an assertion that the finite primitive is symmetric under x/y swap.

## Status and dependencies

Overall status: **PROVED**, by the analytic argument below; distinct
supplementary review and the campaign's formal Claude audit are separate
publication obligations. The n>=10^6 far maximum comparison remains
OPEN; (2) is an upper profile, not that conclusion.

Dependencies read in full: N2-01 exact full-phase rows; N1-02's BV
cancellation estimate; N1-04's regularized single-pole norm; N1-05's joint
endpoint residual; N1-06/07/08's original full-diamond endpoint block.
The near-domain N1-16 coefficient algebra is a predecessor only: its
max-integral calculation is proved again on the full diamond below.
N1-12/15's corrected near model and near central formulas are not premises.

The scoped old N1-round4-budget obstruction concerns a small-margin near
certificate at n<=10^6. Here the constant remainder is allowed to be200,
and the far comparison uses a growing logarithmic gap. This is explicitly
a different scope of the inherited uncorrected full-phase formulas, not
a second correction of the fixed near model.

## Proof

### 1. Combined row bound, including central and collision rows

Work with alpha,beta>=0 and alpha+beta<=pi, and put p=sin alpha,
q=sin beta. Let v_r=(r*pi+beta)/m. For 0<v<2pi define

    eta_-(v)=1/2+(alpha-beta+v)/(2pi),
    eta_+(v)=1/2+(alpha+beta-v)/(2pi),
    A(v)=[c_e |cos((alpha-beta+v)/2)|
                  +c_d |cos((alpha+beta-v)/2)|]/[pi sin(v/2)],
    V(v)=[c_e Phi_0(eta_-(v))+c_d Phi_0(eta_+(v))]
                                                    /[2sin(v/2)],
    C(v)=(p-q-2a cot(v/2))/4,
    D(v)=(p+q+2a cot(v/2))/4.

Write R_r=sum_j |F_jr|, with n first-coordinate indices in that row.
On a row avoiding collisions, the exact two-channel triangle inequality
and N1-04 give

    R_r/n <= A(v_r)L+V(v_r)
                         +5(|C(v_r)|+|D(v_r)|)/n^2.             (4)

To see that this covers every omitted case as well, first write the
right side of the triangle inequality before approximating the pole norms:

    [c_e F_n(eta_-)+c_d F_n(eta_+)]/[2sin(v_r/2)],               (5)

where F_n(t)=|sin(pi t)| B_n(frac t)/n, with its continuous periodic
integer value1. This is N1-04's combined regularized expression; its
individual singular factors have not been assigned values. Both (5) and
R_r/n are continuous in phases whenever 0<v_r<2pi. The set of phases
with neither collision nor v_r=pi is dense in the phase triangle, also
relative to its boundary. Thus their inequality extends by continuity
through every collision, double collision, v_r=pi and phase vertex with
such an interior row. The error in replacing F_n by Phi_L is bounded by
5(|C|+|D|)/n^2 there as well, by the continuous coefficient identities
N1-05(5). This proves (4) on all these rows. Rows at v=0 or2pi will be
in the exact endpoint block below.

The existing coefficient sum, directly from N1-01/N1-05, is

    sum_{r=1}^{2m-2} (|C(v_r)|+|D(v_r)|)
                                      <=2m+4am H_n/pi.         (6)

Accordingly, every use below of the pole-profile approximation, over
any disjoint subsets of these rows, has total normalized error at most

    D_n=10/n^2+20a H_n/(pi n^2).                                (7)

No collision correction is hidden in (7): (4) is a one-sided inequality
obtained by continuity of the finite polynomial and combined products.

### 2. Join the actual endpoint rows to the old full-phase block

Fix R=2, delta=pi/4. Write z_r=min(v_r,2pi-v_r), and let E be exactly
N1-08's endpoint block with these parameters. Thus E contains the actual
polynomial norms of the first/last R rows and every endpoint collision
row. At every other row z_r<=delta it contains

    [A(v_r)L+{U0+(4a/pi)log z_r}/z_r]/m.

The first/last R rows contain all possible v=0,2pi rows. The two central
rows r=m-1,m have z_r>=pi-pi/m>delta, so the ordinary endpoint rows are
among the nonspecial rows of N1-02.

N1-02's exact cancellation quadrature and N1-05's residual give

    S_endpoint <= E+Q+E_n+D_endpoint,                          (8)
    Q=(2delta/pi)[7+(p+q)/pi*(5+2log(4pi/delta))],
    E_n=2(p+q)H_n/n+2am/[n(R-1)].

Here S_endpoint is the actual normalized sum over z_r<=delta.
D_endpoint is that subset's part of (7). Indeed on each ordinary row
R_r/n differs from H(L,v)=A(v)L+V(v)+I(C,D,v)/pi by at most the
single-pole approximation error plus N1-02's shifted BV error. Summing
the latter over this subset is bounded by E_n, whose proof bounds a sum
of nonnegative errors over all nonspecial rows. N1-05 bounds the entire
endpoint residual after the displayed singular subtraction by Q. The
extracted rows in E are already exact, so no Rhat or r_n error is used.
This also explains why the original endpoint cancellation is preserved.

N1-08 now yields

    E <= (4a/pi^2)L^2+b_end L+C_R+c_mesh+e4,                    (9)

with exactly its full-diamond coefficient functions and error. Define
B0=4a/pi^2, D0=U0/pi+B0 log pi and kappa=log(delta/pi)=-log4.
N1-06 supplies

    b_end=2B0 kappa+2D0+(1/pi)integral_0^delta(f_L+f_R),
    c_mesh=B0 kappa^2+2D0 kappa+D0 h_sum+B0 g_sum,               (10)
    f_L(z)=A(z)-4a/(pi z),
    f_R(z)=A(2pi-z)-4a/(pi z).

No new endpoint approximation has been introduced.

### 3. Interior upper and its coefficient integral

On delta<=v<=2pi-delta, sin(v/2)>=sin(pi/8)>3/8. N1-04's
|Phi_0|<=4 and 0<=c_e,c_d<=1 show that V(v)<32/3. Hence summing
(4) over the remaining rows gives

    S_interior <= (L/m) sum_{delta<z_r} A(v_r)+22+D_interior.  (11)

There are at most2m rows, so22 exceeds their constant contribution64/3.
D_endpoint+D_interior<=D_n by (6).

For the coefficient quadrature set T(z)=2a cot(z/2), delta<=z<=pi.
The elementary absolute-sum identity, valid on the full phase triangle,
gives

    pi A(z)=max(p,q+T(z)),
    pi A(2pi-z)=max(p,|q-T(z)|).                               (12)

T decreases from at most2cot(pi/8)<5 to zero. The first maximum is
monotone; the second is a1-Lipschitz function of T. Thus the total
variation of A on [delta,2pi-delta] is less than10/pi<4. The two
halves agree at pi, and sup A<6/pi<2.

For a shifted mesh of step h=pi/m, center a cell of length h at every
selected point. Extend A constantly at the two interval ends. The BV
midpoint error is at most h Var(A)/2. The union of cells differs from
the interval by total endpoint length at most h, costing h sup A. This
works for either convention when a sample is exactly an interval end.
Consequently

    |(1/m) sum_{delta<z_r} A(v_r)
                -(1/pi)integral_delta^(2pi-delta) A(v)dv|
                                                       <4/m. (13)

The entire logarithmic coefficient in (9)+(11) therefore is

    b_end+(1/pi)integral_delta^(2pi-delta) A
       =2D0+(1/pi)integral_0^pi(f_L+f_R).                      (14)

The two logarithms of delta/pi cancel exactly. The quadrature error is
less than4L/m and is charged below.

### 4. Evaluate that coefficient on the entire diamond

Assume first alpha+beta<pi, so a>0. Put x=max(alpha,beta),
y=min(alpha,beta), e=x+y and d=x-y. Since e<=pi,
sin x>=sin y. Formula (12) therefore has the three-piece sum

    pi(A_L+A_R)=2T,                 0<z<pi-e,
                  T+p+q,            pi-e<z<pi-d,
                  2sin x,           pi-d<z<pi.

This follows from T(pi-e)=p+q and T(pi-d)=|p-q|. Empty pieces
when y=0 or d=0 cause no change. Integrating T gives4a log sin(z/2).
Subtract8a/z before taking the lower limit to zero. Since
sin((pi-e)/2)sin((pi-d)/2)=a, the result is

    integral_0^pi(f_L+f_R)
       =[8a log(2/pi)+4a loga+2(alpha p+beta q)]/pi.            (15)

For completeness (15) extends to a=0 without exchanging a nonuniform
singular limit. From (12), with u(z)=T(z)-4a/z, one has

    pi f_L=max(q,p-T)+u,
    pi f_R=max(-q,p-T,q-2T)+u.

The maxima are bounded by1 in absolute value, and
-4a/pi<=u(z)<=0 for0<z<=pi: u decreases from0 to-4a/pi.
Thus |f_s|<1 uniformly on this full interval. Dominated convergence
proves the integral's continuity in phase as a->0, and a loga->0.
The right side of (15) has that same continuous limit. Inserting (15)
into (14) gives precisely (1).

On alpha+beta=pi, c_e=0,c_d=sin alpha and Phi_0(1)=1, so
U0=sin alpha. Both phase sine terms add to pi sin alpha. Hence
b_full=4 sin alpha/pi, including the vertices. This is the first-kill
boundary check; no inverse-a estimate enters the proof.

### 5. Every constant in the assembled remainder

The following elementary estimates make the numerical budget explicit.
We use3<pi, pi^2<10, log pi<3/2, log4<3/2 and H_n<=1+L.

N1-07 bounds the finite endpoint-row profile by

    |C_R|<=1+(2R-1)(4R+9)=52.                                 (16)

N1-06 gives |h_R(t)|<=log(5/2)+1/18<19/18, uniformly0<=t<=1.
For its g_R series put a_R=R+t-1/2 in[3/2,5/2]. The same centered-cell
kernel and |(log x/x)''|<=(2log x+3)/x^3 give directly

    |g_R(t)| <=(log a_R)^2/2+(log a_R+2)/(8a_R^2)<2/3.          (17)

Here log(5/2)<1. Thus |h_sum|<3, |g_sum|<4/3,
B0<1/2 and |D0|<4, using |U0|<=8 from N1-05. Equation (10) gives

    |c_mesh| <(1/2)(3/2)^2+2*4*(3/2)+4*3+(1/2)(4/3)<26.      (18)

The N1-08 coarse error coefficient for R=2,delta=pi/4 is

    K4=181+19+1350+2+36+H_R^*+40<1630.

Consequently e4<=1630(1+L)/n<1 for n>=10^6. The function
(1+log n)/n decreases there, and log(10^6)<14. The other bounds are

    Q<8,  E_n<3,  D_n<1,  4L/m<1.                            (19)

For Q use p+q<=2 and log16<3. For E_n use
4(1+L)/n+2+2/n; for D_n use (7) and the same monotonicity.

Add (8)--(19): the remainder is strictly below

    52+26+1+8+3+1+22+1=114<200.

This proves (2), with all rows accounted for once. The unused slack
is deliberate; no numerical run or interpolation of constants is used.

### 6. An elementary global bound for b_full

We sharpen only the upper bound on Phi_0. For0<t<=1/2, N1-04 proves

    Phi_0(t)=sin(pi t)/(pi t)
          +[2gamma-2log pi+R(t)] sin(pi t)/pi,
    0<=R(t)<=4t^2<=1.

The elementary bounds gamma<3/5 and log pi>11/10 imply the bracket
is negative. Here is a rational verification to avoid a numerical premise.
Integral comparison gives

    gamma<=H_4-log4-1/10=119/60-2log2<3/5,

since log2>2(1/3+1/81+1/1215)>83/120. To justify the first bound,
write H_4-log4-gamma as sum_{k=4}^infinity
[log(1+1/k)-1/(k+1)]; each summand is at least1/[2(k+1)^2],
and the sum is at least1/10. Also pi>31/10 and the positive log series
with t=21/41 give
log pi>2(t+t^3/3)>11/10. Thus Phi_0(t)<=1. Reflection, periodicity
and endpoint continuity prove Phi_0<=1 everywhere.

It follows that U0<=c_e+c_d<=2. Since a loga<=0,
alpha p+beta q<=alpha+beta<=pi and log2<3/4, equation (1) gives

    b_full <=6/pi+8log2/pi^2<2+2/3=8/3.

The inequality log2<3/4 follows already from the first three positive
terms of exp(3/4)>2. This proves (3). QED.

## Checks, limitations and history

Pure analytic proof. No numerical execution, fit or empirical coefficient
is a premise. The proposed target, errors, first kill and alternative
scopes were fixed in ../ideas/C06-far.md before this proof was written.
The exact coefficient uses full-phase max identities, not an unproved
extension of the near-model theorem. The full n>=10^6 far comparison
and global argmax assembly remain separate obligations.

2026-11-06, C06 developer under parent's prospective hard-math allocation;
requested Astra ultra, serving metadata unexposed. Rules/input
b6e67b3c78cb668b6d2f9da5a5560537d2960bf3. Distinct review requested
only after the separate far application and frozen file hashes are ready.
