# PD-T?argmax-effective-2-codex-06 — An explicit global-to-corner norm ratio

ID kind: PD-T.
Aliases: rotated-bin kernel bound; global logarithmic norm with explicit constants.
Split from: the global-norm premise used by H3's aggregate radius estimate.
Split into: the physical corner radius is a separate corollary.

## Statement

For every integer n>=2, let Lambda_n be the global Lebesgue constant of
the even-checkerboard Padua interpolation of PD-T101, and Lambda_c its
value at the nonnode corner. Then

\[
\Lambda_n\le110[1+\log(n+1)]^2\le27500\Lambda_c
                                      <30000\Lambda_c.       \tag{1}
\]

## Definitions and assumptions

Set m=n+1, N=nm. Use the corrected finite kernel G_n=D_n-cos(nu),
the same positive endpoint weights and all polynomial values at removable
collisions. All arithmetic is exact. No global argmax assumption.

## Status by part

Overall status: **PROVED**, analytic proof below. Independent supplementary
checker accepted the proposed argument; final-file review and required
Claude audit remain pending at first writing.

Candidate disposition: retained supporting explicit bound. No optimal
coefficient, sharp norm ratio or new historical mechanism is claimed.

## Depends on

PD-T101/PD-T185 finite rhombus kernel and endpoint-weighted reflection;
PD-T250's Lambda_c>=2; PD-T157's
Lambda_c>=(4/pi^2)log^2 n-54. The lattice count and constants are proved
below, without importing a global Lebesgue theorem from the literature.

## Checks and sources

Analytic proof only; no numerical run is a premise. The independent
checker was sent the complete count, normalizations and constants before
this file was written. Gate: `../novelty-gate-H2-H3.md` and the continuation
record `../attempts/H3.md`. No external theorem or priority claim.

## Proof

### 1. Bound by the full rectangular mesh

At a physical angular point (theta,phi), the cardinal reflection formula
and the triangle inequality give

\[
\lambda_n(\cos\theta,\cos\phi)
\le\frac1{2N}\sum_{\substack{0\le j<2n,\,0\le r<2m\\j+r\ {\rm even}}}
 |G_n(\theta+j\pi/n,\phi+r\pi/m)|.                         \tag{2}
\]

Indeed every interior reflected index occurs once in the periodic board;
at an endpoint its two coincident reflected copies are each multiplied
by the corresponding half weight. This is exactly the weighted
four-reflection triangle inequality, and (2) retains its normalization.
Enlarge the sum to all 4N rectangular mesh points, using nonnegativity.

Let P=(u+v)/2 and T=(u-v)/2. In absolute value the finite rhombus identity
is bounded by

\[
|G_n(u,v)|\le f_m(P)f_m(T)+f_n(P)f_n(T)+1,\quad
f_k(z)=\min\{k,1/|\sin z|\}.                               \tag{3}
\]

At a sine zero interpret f_k=k. This follows from both the finite
Fourier sum bound |U_k|<=k and |sin(kz)|<=1; each U_k has its polynomial
continuation at its apparent poles. Absolute values are pi-periodic
in P and T.

### 2. A uniform count in rotated bins

Put h=pi/m and partition each of the P and T circles of length pi into
m half-open bins I_l=[lh,(l+1)h), 0<=l<m. Every product bin contains at
most 18 images of the full 2n by 2m mesh, counted with multiplicity.

To verify the count, the map from (u,v) modulo 2pi to (P,T) modulo pi
has exactly two inverse branches. A chosen lift of a product bin gives
u=P+T in an interval of length 2h and v=P-T in an interval of length 2h.
The other branch is its translate by (pi,pi). This is exhaustive because
replacing (P,T) by (P+a*pi,T+b*pi) changes u and v by integer multiples
of pi with the same parity; modulo 2pi there are precisely the two
choices. Each circular u interval of length 2h contains at most three
points of the mesh with spacing pi/n>=h, and each such v interval
contains at most three points of its spacing-h mesh. Each inverse branch
therefore contains at most 3*3 points. The bound includes bin boundaries
and wrapped coordinate intervals; half-open choices cannot increase it.

For z in I_l write d_l=min(l,m-1-l). Its distance from pi*Z is at least
h*d_l. The sine chord inequality gives |sin z|>=2*d_l/m. Thus for
every k<=m,

\[
f_k(z)\le B_l:=\frac m{1+d_l}.                             \tag{4}
\]

For d_l=0 use f_k<=m; for d_l>=1 use f_k<=m/(2d_l)<=m/(1+d_l).
Every possible d_l occurs at most twice, so, writing H=1+log m,

\[
\sum_{l=0}^{m-1}B_l\le2m\sum_{s=1}^m\frac1s\le2mH.      \tag{5}
\]

Apply the count and (4)--(5) separately to the two products in (3).
Each full-mesh product sum is at most
18*(sum B_l)^2<=72m^2 H^2. The full correction sum is 4N. Equations
(2)--(3) now yield

\[
\lambda_n\le\frac{144m^2H^2+4N}{2N}
 =72\frac mn H^2+2\le108H^2+2\le110H^2.                   \tag{6}
\]

This holds at every physical point, hence for Lambda_n.

### 3. Compare to the corner

Put x=log n. Since n>=2, H=1+log(n+1)<=x+2. If x<=20,
H^2<=484<=242 Lambda_c, using Lambda_c>=2.
If x>=20, pi^2<10 and the inherited corner lower bound give

\[
\Lambda_c\ge\tfrac25x^2-54\ge\tfrac14x^2,
\quad H^2\le(11x/10)^2<\tfrac54 x^2\le5\Lambda_c.
\]

Thus H^2<=250 Lambda_c for all n>=2. Combine with (6) to prove (1).

## Scope and open items

This deliberately coarse explicit ratio is sufficient for a uniform
corner-radius implication. It neither proves Lambda_n=Lambda_c nor
gives a useful near-coset defect margin. Sharpening its constants is
separate from its all-degree validity. Required Claude audit pending.

## History

2026-11-05, Codex, AC-requested gpt-6-astra ultra; rules/input
ed21cc0bf205549936fccde90244a291bc6de324. The rotated-bin argument was
given to the independent checker before writing; no fit or external
global-norm theorem is used. No final ID allocated.
