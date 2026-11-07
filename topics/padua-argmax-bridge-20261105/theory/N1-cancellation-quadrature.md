# PD-T?argmax-bridge-codex-N1-02 — Uniform cotangent cancellation quadrature

ID kind: PD-T. Aliases: bounded-variation row cancellation; numerator-cutoff
removal; two-pole defect integral. Split from: N1 outer-row compactification,
whose full finite-dimensional profile and effective onset remain OPEN.
Split into: none. The round-1 N1 theorem is unchanged.

## Statement

For real C,D and v not in pi*Z, define on the circle R/(pi Z)

    g(C,D,v;x)=|C*cot x+D*cot(x+v)|-|C*cot x|-|D*cot(x+v)|

away from its two poles, and give g the value zero at either pole. Then

    Var_per(g) <= 8*max(|C|,|D|)/|sin v|.                 (1)

Consequently, for every n>=1 and any shifted n-point mesh avoiding both
poles,

    |sum_{k=0}^{n-1} g(x0+k*pi/n)
               -(n/pi)*integral_0^pi g(x) dx|
       <=4*max(|C|,|D|)/|sin v|.                         (2)

The variation includes all one-sided pole jumps. No differentiability at
an absolute-value zero, root/pole separation, or fixed sign pattern is assumed.

There is the following full-diamond Padua application. Let n>=2,
m=n+1, N=nm, 2<=R<=n, and use the phase convention and a,C_r,D_r of
N1-01. Work first with alpha,beta>=0, alpha+beta<=pi. Let A_R be the union of

    {0,...,R-1}, {2m-R,...,2m-1}, {m-1,m},

and every row containing an exact polynomial collision. It has at most
2R+4 members. Define the explicit model K_(n,R) below. Then

    |S_n-K_(n,R)| <= r_n + E_(n,R)(alpha,beta),           (3)
    E_(n,R)=2*(sin alpha+sin beta)*H_n/n
                     +2*a*(n+1)/(n*(R-1)),

where r_n is N1-01's proved fourth-order error. Extend K and E by separate
absolute phases to the other quadrants. Thus on rho<=rho0<=pi,

    E_(n,R) <= 2*rho0*H_n/n+2*(n+1)/(n*(R-1)).           (4)

Unlike N1-01, every nonexceptional row in K has **no moving numerator-root
integer cutoff**: it uses two single-pole norms and one explicit integral.
The remaining outer sum still has degree-dependent length. Therefore (3)
is a supporting quantitative reduction, not the requested compact profile,
not a proof of a maximum comparison, and not an effective argmax onset.

## Definitions and model (written before any new computation)

Throughout, rho=|alpha|+|beta|; in the first quadrant rho=alpha+beta.

Use G_n=D_n-cos(nu), F_rk=(-1)^delta_r G_n(u_k,v_r)/2,
delta_r=(1-r) mod 2, u_k=(delta_r*pi+alpha)/n+2k*pi/n,
v_r=(r*pi+beta)/m, and

    C_r=(sin alpha-sin beta-2a*cot(v_r/2))/4,
    D_r=(sin alpha+sin beta+2a*cot(v_r/2))/4.

These are N2's coefficients divided by two. Let

    I(C,D,v)=integral_0^pi g(C,D,v;x) dx,
    B_n(t)=sum_{k=0}^{n-1}|cot(pi*(k+t)/n)|, 0<t<1.

The integral is an ordinary bounded, piecewise continuous integral for
v not in pi*Z. Its sign pieces have explicit endpoints. On each piece
g is either zero or -2 times one of |C cot x|, |D cot(x+v)|, so elementary
logarithms of sine give its antiderivative; only the finitely many branch
endpoints need be determined. This definition keeps the integral exact.

Let Bhat_n(t) apply N5's Q formula to the positive and negative cotangent
blocks, changing the sign on the latter. Omit an exact zero. Its error is

    |B_n(t)-Bhat_n(t)| <= e_n=7*n*(pi/n)^4/7200.         (5)

There are only the following branch choices; no high-frequency numerator
cutoff occurs. If n=2s, the positive indices are 0,...,s-1 and the negative
indices are s,...,2s-1. If n=2s+1, the split is after s for t<1/2 and
before s for t>1/2; for t=1/2 the index s is an exact zero and is omitted.
N5's exact shifted harmonic sums may be written as digamma differences;
no approximation to them is assumed here.

For r outside A_R put

    t_r^- = frac(1/2+(alpha-beta+v_r)/(2pi)),
    t_r^+ = frac(1/2+(alpha+beta-v_r)/(2pi)).

Both lie strictly in (0,1), because all collision rows are in A_R. Define

    Vhat_r=|C_r|*Bhat_n(t_r^-)+|D_r|*Bhat_n(t_r^+)
                                +(n/pi)*I(C_r,D_r,v_r). (6)

For r in A_R use N1-01's Rhat_r, with its original exact definition for
the two endpoint rows 0 and 2m-1. Finally

    K_(n,R)=(1/N)*[sum_{r in A_R} Rhat_r
                            +sum_{r outside A_R} Vhat_r].           (7)

Every phase-dependent choice in (7) is specified exactly. The model may
use different finite exceptional-row sets at a collision; the error bound
holds pointwise with the stated set and does not assume a continuous
enumeration of those sets. A_R has bounded size for fixed R, but the second
sum in (7) is not yet replaced by a compact integral model.

## Assumptions and status

Overall status: **PROVED**, developer analytic proof below. Distinct
mathematical review and Claude audit pending. Exact real arithmetic.
There is no numerical, fitted, or source-theorem premise.

## Depends on

PD-T?argmax-bridge-codex-N2-01 for the exact two-phase row formula and
finite collision convention; PD-T?argmax-bridge-codex-N5-01 for (5);
PD-T?argmax-bridge-codex-N1-01 for the exceptional-row model and r_n.
The variation and quadrature argument is proved here. T269 is a
methodological predecessor only, not a premise.

## Proof

### 1. Exact periodic variation, including pole jumps

Periodicity in v and reflection x->-x reduce to 0<v<=pi/2. A simultaneous
sign change of C,D leaves g unchanged. Let M=max(|C|,|D|). If CD=0,
g=0, so assume both are nonzero. The identity

    |X+Y|-|X|-|Y| = -2*min(|X|,|Y|) if XY<0,
                   0 otherwise

fixes every sign piece.

If CD>0, take C,D>0. The nonzero pieces are the zero-to-zero interval
(pi/2-v,pi/2) and the pole-to-pole interval (pi-v,pi). On each interval
one positive magnitude increases and the other decreases. Their minimum
is unimodal. Its maximum on the first interval is at most M*tan(v/2),
and on the second at most M*cot(v/2): these follow by replacing both
coefficients by M and finding the crossing of the two unweighted
magnitudes. A negative unimodal function with values zero outside its
interval has periodic variation four times that maximum for g=-2*min.
This includes its jumps at the two poles, with the assigned value zero.
Hence

    Var_per(g)<=4*M*(tan(v/2)+cot(v/2))=8*M/sin v.

If CD<0, take C>0,D<0. The nonzero intervals are (0,pi/2-v) and
(pi/2,pi-v). On the first the minimum magnitude decreases from
|D|*cot v to zero; on the second it increases from zero to C*cot v.
Including each pole jump gives total variation

    Var_per(g)=4*(C+|D|)*cot v<=8*M/sin v.

For v=pi/2 the intervals in this second case are empty and g=0.
This proves (1), with every root and pole transition included.

### 2. A periodic shifted midpoint inequality for BV functions

Let h=pi/n and center a cell of length h at each sample. The sample is a
continuity point because it is not a pole; absolute-value zeros are
continuous. Integration by parts on each side of its center expresses

    g(x_k)-(1/h)*integral_cell g

as a Stieltjes integral against dg with weight between -1/2 and 1/2.
For example on the left half the weight is (t-left)/h, and on the right
it is -(right-t)/h. The sign is immaterial for its bound. These cells
partition one period. Summing and taking absolute values bounds the total
by Var_per(g)/2. This proves (2). The argument is valid for the one-sided
pole jumps inside cells; it assumes neither a bounded derivative nor
separation of a numerator zero from a pole.

### 3. Exact offsets and bounded collision-row count

For the minus cotangent channel,

    (u_k-v_r)/(2h)
      =k+(delta_r-r)/2+(alpha-beta+v_r)/(2pi),

and (delta_r-r)/2 is a half-integer. For the plus channel,

    (u_k+v_r)/(2h)
      =k+(delta_r+r)/2+(alpha+beta-v_r)/(2pi).

Thus their n-point cotangent grids have exactly the offsets t_r^- and
t_r^+ in (6), independently of any numerator-root cutoff.

Each of the maps (j,r)->mj-nr and (j,r)->mj+nr modulo 2N is a bijection
from the odd board to Z/(2N): on the full periodic board each has kernel
{(0,0),(n,m)}, and adding (n,m) changes parity. An equation u-v=0 modulo
2pi or u+v=0 modulo 2pi fixes a single residue, if its phase offset is
integral at all. There are therefore at most two collision points, and
at most two collision rows. This gives |A_R|<=2R+4.

### 4. Summing the cancellation error with the actual coefficients

For a nonspecial row, decomposition of |F| gives exactly

    sum_k |F_rk|=|C_r|*B_n(t_r^-)+|D_r|*B_n(t_r^+)
                                      +sum_k g(C_r,D_r,v_r;x_k).

Since |C_r|,|D_r| <= (p+q+2a*|cot(v_r/2)|)/4, where
p=sin alpha,q=sin beta, equation (2) bounds its cancellation error by

    (p+q)/|sin v_r|+a*csc^2(v_r/2).                     (8)

Here the exact identity
|cot(v/2)|/|sin v|=1/[2*sin^2(v/2)] removes the apparent extra
central singularity from the A-channel. The r=m-1,m exclusions ensure
the remaining sine denominators have uniform mesh-distance bounds.

For r outside A_R let k_r=min(r,2m-r-1)>=R. Its distance d_0 from
{0,2pi} is at least pi*k_r/m. Its distance d_pi from pi is at least
pi*l_r/m, where l_r=m-r-1 if r<=m-2 and l_r=r-m if r>=m+1.
Both l_r>=1. Sine chords give

    1/|sin v_r| <= (pi/2)*(1/d_0+1/d_pi)
                 <=(m/2)*(1/k_r+1/l_r),
    csc^2(v_r/2) <=m^2/k_r^2.

Each positive k occurs at most twice; likewise each positive l occurs at
most twice. All occurring values are <=n. Hence

    sum_{r outside A_R} 1/|sin v_r| <=2m*H_n,
    sum_{r outside A_R} csc^2(v_r/2)
             <=2m^2*sum_{k=R}^infinity k^-2 <=2m^2/(R-1).

Summing (8), dividing by nm and using (5) gives E_(n,R). The total
cotangent approximation error is no greater than r_n: the exceptional
rows cost at most 2e_n(|C_r|+|D_r|), as in N1-01, and every other row
costs only e_n(|C_r|+|D_r|). N1-01's coefficient sum over all nonendpoint
rows therefore still bounds the combination. Endpoint rows have zero
approximation error. This proves (3). Finally p+q<=alpha+beta and a<=1
give (4). Separate phase evenness gives every quadrant.

## Scope and unresolved compactification

This theorem supplies a degree-uniform error for eliminating the moving
numerator-root grid cutoffs outside a fixed number of exceptional rows.
It does not replace the outer sum of the functions in (6), control the
outer integral's endpoint/central singularities, or bound the exact
exceptional rows uniformly in h=1/n. In particular, it supplies no n1
for PD-T099 and no B3 PASS. E_(n,R) has a fixed O(1/R) term; R must be
chosen from an actual margin budget before proposing a finite certificate.

The next falsifiable step is an explicit outer-row expansion of
|C(v)| B_n(t^-(v))+|D(v)| B_n(t^+(v))+(n/pi) I(C(v),D(v),v),
keeping their joint endpoint cancellation. Bounding those three terms
independently near v=0,2pi loses the cancellation needed for a useful
logarithmic profile. That obligation remains OPEN.

## Checks and history

No computation is a proof premise and no new fit or repeated round-1 run
was performed. Independent review and any implementation checks remain
pending. Candidate/gate: ../ideas/N1-outer.md. 2026-11-05, round 2 after
parent-pushed boundary 714f3ca, Codex requested gpt-6-astra ultra.
