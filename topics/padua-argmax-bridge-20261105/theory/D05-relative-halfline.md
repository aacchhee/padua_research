# PD-T?argmax-bridge-codex-D05-halfline — Boundary and phase increments of the half-line residual

ID kind: PD-T. Aliases: translated reciprocal-subtracted cotangent;
origin-normalized half-line reference error; first-order endpoint cell.
Split from: D05 full phase-relative S-K target, OPEN.
Split into: none. This is a supporting lemma, not the full target.

## Statement and definitions

Put A=pi/2 and define the continuous function on [0,infinity)

    r(0)=0,
    r(y)=cot y-1/y, 0<y<A,
    r(y)=-1/y, y>=A.

For h>0, v>=0 and 0<=t<=1 define ONLY the matched cell difference

    E(h,v,t)=sum_{k>=0} [ r(v+h(k+t))
                   -(1/h) integral_{v+kh}^{v+(k+1)h} r(y)dy ].       (1)

This series converges absolutely. Its separate sum and improper integral
diverge, and are never treated as convergent objects. Then

    |E(h,v,t)-(1/2-t)r(v)|<=5h/24,                                (2)
    |E(h,v,t)-E(h,v0,t0)|
       <=(5/3)|v-v0|+[4/pi+(5/3)h]|t-t0|.                         (3)

These hold for all v,v0>=0, all t,t0 in [0,1]. In particular, for
0<=v<=A,

    |E(h,v,t)|<=pi*v/12+5h/24.                                    (4)

The offsets in (3) are real unwrapped offsets. In fact
E(h,v,1)-E(h,v,0)=-r(v); the functional is not periodic in t.

For D04's half-line expression Q and its h^-1 digamma approximation,
their difference is exactly E(h,v,t), for 0<v<A. Let T0 and Theta be
D04-half-line-defect.md's symmetric reference quadrature and displaced
digamma expression, with nonnegative weight w. Then

    |T0-Theta|<=pi*w*v/3+5w*h/6.                                  (5)

The same inequality holds at v=A by continuity when samples avoid poles.

Here is an application with the ACTUAL D04 finite offsets. Let n>=16,
m=n+1, h=pi/n, alpha,beta>=0, rho=alpha+beta<=pi/2 and
a=(cos alpha+cos beta)/2. Fix an integer R>=2 with n>=8R. Use fixed
index sets

    J_L={R,...,floor((m-1)/2)},
    J_R={R+1,...,floor((m-1)/2)}.

For j in J_L set s=beta/pi; for j in J_R set s=-beta/pi. Define

    z=pi*(j+s)/m, z0=pi*j/m, x=alpha/pi,
    theta_+=(1-s+x)/2+(j+s)/(2m),
    theta_-=(1-s-x)/2+(j+s)/(2m),
    w=a*cot(z/2)/2,
    D_j(alpha,s)=T0_j-Theta_j
       =-2w [ E(h,z,theta_+)+E(h,z,theta_-) ].                      (6)

T0_j is the actual folded D04 symmetric cancellation on the physical
row j or 2m-j, and Theta_j uses its exact finite-n displaced digamma
arguments. In D_j(0,0), set a=1 and alpha=s=0. Every offset in (6)
lies strictly between 0 and1 on this closed near-phase triangle, so
there is no wrap or sampled pole in these rows. The conclusion is

    (1/(nm)) sum_{j in J_L,J_R}
          |D_j(alpha,s)-a*D_j(0,0)|
                      <=2a*rho*H_n/n, H_n=sum_{k=1}^n 1/k.         (7)

This fixed-row relative bound vanishes at phase zero. It is not a bound
for the entire D04 reference remainder or S-K.

An independent absolute consequence, on D04's ENTIRE closed diamond,
is that the endpoint-row T0-Theta contribution in its reference proof
can be charged by

    2pi*a/(3n)+5a*H_n/(3n^2),                                     (8)

instead of 32a*H_n/(pi^2*n). All other D04 charges remain in force.
This changes no old theorem, model, degree floor or near correction.

## Status and dependencies

Overall status: **PROVED**, written developer result, distinct review
required. Exact real arithmetic; no numerical premise. The main D05
phase-relative target remains **OPEN**, not PARTIAL.

PD-T270 supplies the local cotangent partial fraction and its second
derivative formula; its proof was read. D04-half-line and reference-
matching supply the exact corrected-row offsets and folding, with
actual polynomial collisions excluded. At the D05 gate these D04
dependencies were pending; root subsequently reported distinct Astra
xhigh acceptance without changes in independent-checks-D04-row-reduction.md.
The elementary scalar estimates (1)-(4) are proved here independently
of D04's bounds. No smoothness in h through moving roots is assumed.

## Proof

### 1. Two exact variation budgets

On (0,A), PD-T270's differentiated partial fraction gives

    r''(y)=-4y sum_{l>=1}
             (3pi^2*l^2+y^2)/(pi^2*l^2-y^2)^3<0.

The expansion at zero gives r'(0)=-1/3. At A the left derivative is
-1+4/pi^2 and the right derivative is 4/pi^2, so its upward jump is
exactly1. On (A,infinity), r'=1/y^2 decreases to zero. Therefore

    Var_[0,infinity)(r')
      =(2/3-4/pi^2)+1+4/pi^2=5/3.                                (9)

Assign either one-sided value to r' at A; all derivative integrals
ignore that point, and its jump is included in the variation measure.
Also r decreases from0 to -2/pi and increases thereafter to0, giving

    integral_0^infinity |r'(y)|dy=4/pi.                            (10)

For 0<y<=A, integrate sin u-u cos u from its derivative u sin u to get
sin y-y cos y<=y^3/3. The chord sin y>=2y/pi then gives

    0<=1/y-cot y<=pi*y/6.                                        (11)

### 2. First-order cell identity, with no divergent subtraction

For 0<=s<=1 put

    K_t(s)=s for s<=t, and s-1 for s>t,
    mu=t-1/2,
    B_t(s)=s^2/2-mu*s-max(0,s-t).

Thus integral_0^1 K_t=mu, B_t'=K_t-mu away from its corner,
B_t(0)=B_t(1)=0, and |B_t|<=1/8. The last bound follows by locating
the stationary point on each quadratic piece and its shared endpoint:
the positive extremum is t(1-t)/2<=1/8, and a possible negative
extremum is no smaller than -(t-1/2)^2/2>=-1/8.

The fundamental theorem for absolutely continuous r gives on each cell

    r(v+h(k+t))-(1/h)integral_cell r
       =integral_cell K_t(frac((y-v)/h))*r'(y)dy.

Sum finitely many cells. The mean part is
mu[r(v+Kh)-r(v)]. Integrating the zero-mean part by parts against the
bounded-variation derivative gives an error at most
h Var(r')/8=5h/24; its boundary terms vanish at every cell endpoint.
As K tends to infinity, r(v+Kh) tends to0. This proves (2).
Absolute convergence in (1) also follows directly by bounding a cell
error by its variation and summing the integrable |r'| tail in (10).
Combine (2) and (11) to prove (4). Telescoping the matched differences
at offsets1 and0 gives the stated nonperiodicity identity exactly.

### 3. Translation and offset increments

For a finite matched sum of K cells, differentiation in v almost
everywhere gives the matched quadrature defect of r'. Its magnitude is
at most Var(r')<=5/3, by comparison with the average on each cell.
Every finite matched sum is therefore Lipschitz in v with that bound.
Its pointwise limit preserves the same bound, including sample crossings
of A, because r itself is continuous there.

For offset changes its derivative almost everywhere is
h sum_{k=0}^{K-1}r'(v+h(k+t)). Comparison of |r'| with its cell average
bounds this magnitude by

    integral_v^{v+Kh}|r'|+h Var(|r'|)
                              <=4/pi+5h/3.

The same limiting argument proves the offset Lipschitz bound for all
t in [0,1]. Adding the two separate increments proves (3). No derivative
of an absolute-value moving root has been taken.

D04's finite matched subtraction of the reciprocal gives exactly
Q-h^-1[log(v/h)-psi(v/h+t)]=E(h,v,t). Apply this twice in its exact
two-piece formula T0=-2w[Q_1+Q_2] to obtain (5) from (4).

### 4. Actual finite-offset near-phase bound

For the frozen sets, j>=2, |s|<=1/2, j<m/2. Thus
3z0/4<=z<=A. Both theta offsets are positive and at most1; equality
at1 would require x-s=1/2 and z=A simultaneously. On the left these
conditions force s=0, contradicting j<m/2; on the right z<A when
s<0, and the same contradiction applies when s=0. Hence they are
strictly below1. D04's floor integers are zero and no pole is sampled.

The actual shifts satisfy

    |z-z0|=beta/m,
    theta_+/- -theta_0=+/-x/2-n*s/(2m),
    sum_+/- |theta_+/- -theta_0|
                    =max(x,n|s|/m)<=rho/pi.                       (12)

Since h<=pi/16 and 3<pi<4, the offset coefficient in (3) is less than2.
Consequently, writing U for the sum of the two E's,

    |U(alpha,s)-U(0,0)|<=10beta/(3m)+2rho/pi,
    |U(0,0)|<=pi*z0/6+5h/12.                                     (13)

On the segment between z and z0, the chord sin(y/2)>=y/pi gives

    |cot(z/2)-cot(z0/2)|<=8pi^2*beta/(9m*z0^2),
    cot(z/2)<=8/(3z0).                                           (14)

Use D=-a*cot(z/2)U. Substitute (13)-(14), z0=pi*j/m and h=pi/n.
This gives for each fixed endpoint row

    |D_j(alpha,s)-aD_j(0,0)|
      <=a [16rho*m/(3pi^2*j)
          +(4pi^2/27+80/(9pi))*beta/j
          +(10pi*m/(27n))*beta/j^2].                              (15)

Sum over both fixed sets. Each harmonic sum is at most H_n, while
the combined inverse-square sum is at most
2[1/4+integral_2^infinity y^-2 dy]=3/2. Use beta<=rho,
m>=17, m/n<=17/16, H_n>=1 and 3<pi<4. After division by nm the
coefficient of a*rho*H_n/n is less than

    32/27+32/51+85/612<2.

This proves (7), with all finite displacement and mesh factors retained.

### 5. Full-phase absolute endpoint consequence

In D04's folded ordinary endpoint rows w=a*cot(z/2)/2<=a/z,
z=pi*nu/m. Formula (5) bounds each row by

    pi*a/3+5a*h/(6z).

There are fewer than2m such rows and their sum of1/nu is at most2H_n,
including right-end folding and collision exclusions, as in D04.
Divide the summed bound by nm and use h=pi/n. This is (8).
No wrap decision is needed here because (4) holds at all offsets;
D04's exact digamma/wrap terms remain part of Theta.

## Scope, remaining gaps and checks

Equation (7) addresses ONLY T0-Theta on the specified fixed endpoint
sets. It does not cover Theta/(nm)-Xi, the central region, rows changing
endpoint/central membership, changing actual-collision special sets or
weighted single-pole approximation errors. The full relative S-K error
cannot be deduced from it or from two absolute D04 bounds. In particular
the phase-independent leading allowance in the remaining displaced
digamma comparison has not been removed. Combining (8) with those old
charges leaves an absolute a H_n/n term, so (8) alone is not the full
relative success criterion either.

No primitive C2/quadratic assertion is made: PD-T220/PD-N079's finite-n
cusp remains. Every actual collision continues to use its finite corrected
polynomial value. No old M_near term or quantifier changes. Main practical
M_infty and phase-relative comparison targets remain OPEN.

Paper proof only: no scalar computation, native run, board, numerical
quadrature, fit or code job was executed. This supporting claim is
submitted for distinct review, not approved by its author.

2026-11-06, input/rules a6d7a788b3ce457a4631bbb507624303240c570c;
parent-assigned Sol xhigh, serving metadata unexposed. Candidate and
bounded-block disposition: ideas/D05-relative-reference.md and
attempts/D05-relative-reference.md.
