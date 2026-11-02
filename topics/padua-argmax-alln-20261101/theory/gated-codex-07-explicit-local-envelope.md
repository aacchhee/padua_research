# PD-T?argmax-alln-gated-codex-07 — Explicit two-phase local envelope

ID kind: PD-T.
Aliases: direction1 round3 Q3-final; explicit square-root sign-change bound;
quantified two-phase primitive gain; 242000/2048/640 local envelope.
Split from: quantitative refinement of PD-T?argmax-alln-gated-codex-03;
the original qualitative local theorem remains unchanged. Historical
round record: `gated/d1/r03-explicit-local.md`.
Split into: none. PD-T099 remains OPEN.

## Statement

Use the exact primitive and corrected polynomial convention of
[the local gain theorem](gated-codex-03-two-phase-local-gain.md):
m=n+1, N=nm, Gamma^-={(j,r):0<=j<2n,0<=r<2m,j+r odd},
u=(j*pi+alpha)/n, v=(r*pi+beta)/m,
F_jr=(-1)^j[D_n(u,v)-cos(nu)]/2,
S_n=N^(-1) sum_Gamma^- |F_jr|,
a=(cos alpha+cos beta)/2 and rho=|alpha|+|beta|.

For every integer n>=2 and every real pair of phases with rho<=1/64,

\[
 S_n(\alpha,\beta)\le a(\alpha,\beta)\Lambda_c(n)
       +242000\rho^2\log(n+1)+2048\rho^{3/2}
       +640\rho\frac{1+\log(n+1)}{n}.                 \tag{Q}
\]

Every polynomial collision and exact zero is included. All constants and
the radius are numerical and independent of n and both phases.

## Definitions and assumptions

Exact real arithmetic, the odd periodic mesh above and PD-T185's corrected
finite polynomial kernel. The endpoint-weighted four-reflection formula
is the identity (2) of the local gain theorem. There is no hypothesis on
a critical point, defect, pole avoidance or differentiability of an
absolute value at zero. The proof below uses physical base angles
u0=j*pi/n,v0=r*pi/m and endpoint half weights as in that identity.
The factors e_j,f_r are <=1; retaining them only lowers positive error
bounds. Zero phase is exactly S_n(0,0)=Lambda_c(n).

## Status by part

Overall status: **PROVED**, by the complete written analytic estimates
below. Supplementary independent Astra xhigh review and required Claude
audit are pending at initial publication. No numerical check is a premise.

| Mathematical part | Status | Evidence / limits |
|---|---|---|
| Explicit uniform local envelope (Q) | PROVED | Derivative sums, sign-change counts and positive finite collision family below |

Candidate disposition: retained quantitative implementation variant of
IDEA-305 / original Claude-02 / fallback-04. The coarse quantitative route
can be stopped while retaining this lemma; no failure of the theorem is
inferred from the large constants.

## Depends on

PD-T185 for the finite polynomial kernel and its divided difference;
PD-T189 for the zero-phase normalization; the local theorem
PD-T?argmax-alln-gated-codex-03 for the exact reflection formula and
phase algebra, both reused with their full conventions. The small-radius
geometry, all numerical derivative constants and all numerator-sign errors
are bounded explicitly below. No external literature transfer.

## Checks and sources

Developer: Codex, parent-assigned gpt-6.1-sol xhigh; runtime metadata not
independently exposed. Rules/snapshot
`2dde541f1e5af239cae6e93e4438b9be89d15d87`, scientific base
`7d308b10d946b607ae0690454f6c0103690775a4`, 2026-11-02.
The complete earlier gate and failed proof variants remain in
[round 1](../gated/d1/r01-phase.md). This round was registered in
[round-3 contract](../gated/d1/r03-contract.md). The orchestrator read the
explicit proof and reported no blocking finding; the distinct independent
review is recorded separately in
[round-3 check](../gated/checks/d1-r03.md) when completed.

The deterministic scalar arithmetic script and receipt are linked from
[round 3](../gated/d1/r03-explicit-local.md). They calculate the sum of
constants and the finite defect budget; they are MEASURED float arithmetic,
not a phase scan, computer proof or uniform verification premise.

## Proof

## 1. Explicit regular geometry and derivative bounds

Keep the same removed family B={r=j+1,j>=2n/3}. On every remaining odd
physical pair set L=|j-r|>=1, d=min(j+r,2n+1-j-r)>=1. Along every phase
path of total size <=1/64, put P=(u+v)/2,T=(u-v)/2,b=sin P,t=|sin T|.
Then

\[
 b\ge d/(2m),\qquad t\ge L/(4m).                        \tag{1}
\]

For the first bound the distance of the base P from either endpoint is
at least pi*d/(2m); its change is at most rho/(2n)<=3rho/(4m).
The sine chord bound gives (1). For T the base |u-v| is at least
pi*L/(3m): j>r and r-j>=3 have larger gaps; the unremoved r=j+1 cases
have gap >=pi/(3m). Its change is at most rho/n<=3rho/(2m).
For |T|<=pi/2+1/256, sin|T|>=(3/5)|T|, giving t>=L/(4m).
All regular denominators retain their signs. The slight endpoint
overshoots satisfy |sin u|,|sin v|<=3b: compare the base sine inequality
|sin u0|<=2sin P0 with changes at most rho/n and rho/(2n), and use
b>=1/(2m), m/n<=3/2.

For f=(1+cos v)/(cos u-cos v) and gu,gv as in the local theorem,
ordinary coordinate derivatives obey

\[
 |f_i|\le2b^{-1}t^{-2},\qquad
 |f_{ij}|\le8(b^{-2}t^{-2}+b^{-1}t^{-3}),                 \tag{2}
\]
\[
 |g_u|,|g_v|\le t^{-1}+b^{-1},\quad
 |(g_*)_i|\le t^{-2}+b^{-2},\quad
 |(g_*)_{ij}|\le t^{-3}+b^{-3}.                           \tag{3}
\]

For (2), differentiating the denominator 2b*sin T and using the preceding
3b sine bound gives first derivative coefficient at most 3/2; the pure
second derivative terms have coefficients <=1/2 and 9/2, and the mixed
ones <=9/4 and 9/2, respectively. All are bounded by the displayed 2 and 8.
For (3) use gu=-(cot T+cot P)/2, gv=-(cot T-cot P)/2; their actual
derivative coefficients are <=1/4, so the displayed constants are safe.

Let H=1+log m. For a fixed signed j-r, each d has multiplicity <=2;
therefore for a fixed absolute L the multiplicity is <=4. L,d<=m.
Use sum k^-1<=H, sum k^-2<=2 and sum k^-3<=2. For a single L there
are at most 2m total pairs; for a single d at most 4m. These facts give
the following explicit normalized sums (termwise suprema along paths
are permitted by (1)):

| Sum, normalized by 1/(nm) | Upper bound |
|---|---:|
| sum max_i |f_i| / n | 1152 H |
| sum max_ij |f_ij| / n^2 | 55296 H |
| sum |g_*| | 24 H |
| sum max_i |(g_*)_i| / n | 216 |
| sum max_ij |(g_*)_ij| / n^2 | 1080 |

For transparency, before the factor 2 in f_i the b^-1*t^-2 sum is
<=256 m^3 H; division by n^2*m and m/n<=3/2 gives 576 H.
For the second derivative, b^-2*t^-2 sums to <=1024 m^4, and
b^-1*t^-3 to <=1024 m^4 H. Multiplication by 8, division by n^3*m,
and (m/n)^3<=27/8 give <=55296 H. The sums of t^-1+b^-1,
t^-2+b^-2, t^-3+b^-3 are respectively <=16m^2 H,96m^3,320m^4,
which give the other rows.

Apply symmetric Taylor to E(s)=F(s alpha,s beta)-a(s alpha,s beta)f0.
Here |a'|,|a''|<=rho^2/2. The f terms in E'' have normalized sum at most

\[
 576\rho^3H+1152\rho^3H+55296\rho^2H.
\]

For each sine channel the three product-rule terms have sum at most
12rho^3 H+216rho^2+540rho^3. Thus the entire sum of |E''| is at most
59000 rho^2 H (using rho<=1/64; even using rho<=1 gives 58560 H).
There are two simultaneous-negation pairs in the four-reflection formula.
Their normalized signed excess is therefore at most

\[
 118000\rho^2H\le236000\rho^2\log m.                    \tag{4}
\]

The factor from symmetric Taylor is one, since the two integral
remainders have total weight one. This signed estimate does not discard
negative numerators; their full absolute-value correction is bounded next.

## 2. Explicit sign-change support and counts

Write x=pi-u0,y=pi-v0,X=x-alpha/n,Y=y-beta/m. The numerator of F is

A=a(1-cos Y)-sin(alpha)sin X/2+sin(beta)sin Y/2.

On this radius a>=.99 and |Y|<=pi+1/192. The elementary sine chord
bound gives 1-cos Y>=Y^2/6, hence a(1-cos Y)>=Y^2/7.
If A<0, it follows that

\[
 |Y|^2\le4\rho(x+\rho/2+|Y|),\quad
 |Y|\le5\rho+2\sqrt{\rho x},\quad
 y\le6\rho+2\sqrt{\rho x}.                              \tag{5}
\]

Split at x=64rho. In the near part x<=64rho,y<=22rho. A regular
odd pair has x+y>=2pi/m; the common zero endpoint was removed into B.
Consequently |X|+|Y|<=2(x+y), X+Y>=.99(x+y), and
b=sin((X+Y)/2)>=(x+y)/4. Also (-A)+<=rho(x+y).
Together with (1) this gives

\[
 (-\chi F)_+\le 2\rho/t\le8m\rho/L.
\]

There are at most 21n*rho+1 first rows. In each one the reciprocal L
sum is <=2H. The normalized sum is bounded by
336rho^2 H+16rho H/n. Absolute-value correction is 2 per term and
there are four reflected phases, so its contribution to S is at most

\[
 2688\rho^2H+128\rho H/n.                               \tag{6}
\]

In the far part x>64rho, (5) gives |Y|<=21x/64<x/2, and
3x/4<=X<=129x/128. Both (X+-Y)/2 lie in [0,7pi/10]. On that interval
sin z>=z/3 (concavity, sin(7pi/10)>3/4 and 7pi/10<9/4). Therefore

\[
 |\cos X-\cos Y|\ge(X^2-Y^2)/18\ge x^2/64,
 \qquad (-\chi F)_+\le64\rho/x.                          \tag{7}
\]

There are at most 2m*rho+m*sqrt(rho*x)+1 eligible second indices.
For the first mesh,

(1/n)sum x^-1/2<=2,

(1/n)sum_{x>64rho} x^-1<=1+log(1/rho),

and the full latter sum is <=H. The harmonic cutoff is at least
max(1,64n*rho/pi); these bounds include rho<1/n. Since
sqrt(rho)(1+log(1/rho))<=1 for rho<=1/64, summing (7) gives normalized
cost <=256rho^(3/2)+64rho H/n. With the same factor 8 as in (6),
the far absolute-value correction is at most

\[
 2048\rho^{3/2}+512\rho H/n.                             \tag{8}
\]

No sign-change support of width O(rho) is assumed in the far rows.

## 3. Explicit collision-family positivity and Hessian

For r=j+1 write h=n-j and set
x_B=(h*pi-alpha)/n,y_B=(h*pi-beta)/m,
X_B=(x_B+y_B)/2,T_B=(x_B-y_B)/2. These are the half angles for
this reflected collision-family representation. Use the exact finite-sum
factorization

\[
 D_n=(-1)^n\{V_n(X_B)U_m(T_B)+U_n(X_B)V_n(T_B)\},\quad
 V_n(z)=\cos((2n+1)z/2)/\cos(z/2).
\]

On B and rho<=1/64, |X_B|,|T_B|<=1.1. Thus sec(z/2)<=5/4,
|sec(z/2)'|<=5/8, |sec(z/2)''|<=1; since n+1/2<=5n/4,

\[
 |V_n|\le5/4,\quad |V_n'|\le2n,\quad |V_n''|\le3n^2.
\]

The global finite Fourier sums give |U_k^(q)|<=k^(q+1), q=0,1,2.
Unlike quotient differentiation, these require no h-dependent factor.
Each phase derivative of X_B,T_B has magnitude <=1/(2n).
Using m<=3n/2 in the product rule gives |D_i|<=145n/32,
|D_ij|<=831n/128. After the factor 1/2 and corrected cosine,

\[
 |F_i|\le3n,\quad |F_{ij}|\le4n,\quad |F(0,0)|\le2n.    \tag{9}
\]

The zero-phase positive bound is F(0,0)>=4n/(3pi^2). Indeed for
h>=1, with x=h*pi/n,y=h*pi/m,X=(x+y)/2,T=(x-y)/2 at zero phase,
F(0,0)=sin^2(y/2)/(sin X sin T)>=y^2/(pi^2 X T)
>=4n/(3pi^2); use sin(y/2)>=y/pi, X<=x,
T=h*pi/(2nm), and n/m>=2/3. At h=0 the finite polynomial has
F(0,0)=n. The gradient bound implies

\[
 F(\alpha,\beta)\ge(4/(3\pi^2)-3/64)n>2n/(3\pi^2)>0.
\]

Thus no cusp occurs on B on the explicit radius. Symmetric Taylor and
1-a<=rho^2/4 show that a simultaneous-negation pair's excess is
<=5n*rho^2. There are two pairs and at most n indices in B. Its
normalized contribution is therefore <=10rho^2.

Combining (4), (6), (8), and (9), the quadratic coefficient is
236000+5376+10/log(3)<241386<242000. Therefore

\[
 \boxed{S_n\le a\Lambda_c
       +242000\rho^2\log m+2048\rho^{3/2}
       +640\rho\frac{1+\log m}{n},\quad \rho\le1/64.}     \tag{Q3-final}
\]

This completes the proof of the stated explicit local bound.

## Scope and open items

This is an explicit local primitive envelope, not an effective all-square
or compact-complement argmax threshold. On delta=pi/4 its radius fits the
finite defect block, but the coarse regular Hessian constant yields an
unusable sufficient scale n>=exp(10^7) for the local-excess comparison;
quantitative global phase entry remains separate. The complete comparison
and scoped STOP recommendation are in [round 3](../gated/d1/r03-explicit-local.md).
No finite degrees beyond the separately certified range are settled here.
The qualitative local theorem and all-degree PD-T099 retain their scopes.

## History

2026-11-02: explicit-constant development in authorized direction1 round3.
A preliminary 240000 quadratic coefficient was insufficient for the final
bookkeeping: retaining the factor 2 in the f_i bound gives
236000+5376+10/log(3)>240000. It was corrected to 242000 before this theorem's
statement was published. That trial is retained in the round record and
here; it is a failed bookkeeping choice, not a counterexample to an
inequality with coefficient 240000. The Statement and proof claim only
the final coefficient 242000. The complete analytic proof is preserved
here independently of the round diagnosis. No shared registry or final
ID allocation is made by this worker.
