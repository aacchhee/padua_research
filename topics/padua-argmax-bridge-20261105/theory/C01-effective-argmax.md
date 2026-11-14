# PD-T?argmax-bridge-C01-effective-argmax — explicit global argmax onset

ID kind: PD-T.
Aliases: numerical PD-T229 continuation; impractical explicit upper boundary
of the finite argmax gap.
Split from: the effective large-degree parameter range of PD-T099;
the original all-degree theorem remains OPEN.
Split into: the explicit global primitive constant is the separate
[C01-effective-global](C01-effective-global.md) lemma.

## Statement

Set

\[
N_0=\left\lceil\exp(10^{12})\right\rceil.
\]

For every integer `n>=N0`, use exactly PD-T101's even-checkerboard Padua
nodes, total-degree cardinal polynomials and corrected exceptional x mode.
The conclusion is

\[
\max_{[-1,1]^2}\lambda_n=\Lambda_c(n),
\]

with exactly the following two global maximizers:

\[
\{(-1,-1),(1,-1)\}\quad(n\text{ even}),\qquad
\{(-1,-1),(-1,1)\}\quad(n\text{ odd}).
\]

This is an actual global argmax-onset claim, not a model-validity or energy
onset. The bound is impractical. It neither certifies the intervening
finite range `41<=n<N0` nor resolves all-degree PD-T099.

## Definitions and assumptions

Physical angles are `(theta,phi) in [0,pi]^2`, with
`(x,y)=(cos theta,cos phi)`. Set `m=n+1`, `N=nm`, `L=log n`,
`rho=|alpha|+|beta|` and `a=(cos alpha+cos beta)/2`.
Use PD-T216's primitive `S_n` and PD-T215's exact triangle defect
`Delta=S_n-lambda_n`. Every collision and initially zero cardinal is
evaluated by the original finite polynomial. Exact real arithmetic;
there is no finite energy or numerical maximizer assumption.

## Status by part

Overall status: **PROVED**. The complete analytic assembly below and
its separate global lemma received distinct Astra high reconstruction
with no findings; see the dated disposition below. The original OPEN
status was a prereview boundary, now resolved. Formal Claude audit
remains separate.

| Mathematical part | Status | Evidence / remaining obligation |
|---|---|---|
| Explicit global argmax onset and exact equality set | PROVED | Written analytic proof; independent constants, cover and assembly reconstruction accepted |

Candidate disposition: retained explicit-constant quantitative continuation
of IDEA-326/327/328/331/336 and PD-T229. No new mechanism or priority claim.

## Depends on

- [C01-effective-global](C01-effective-global.md): for `n>=64`, full closed
  phase diamond, `S<=a Lambda_c+10^6 log(n+1)`.
- PD-T157: `Lambda_c>=(4/pi^2)L^2-54` for every `n>=2`.
- PD-T215 and PD-T225's exact physical odd-center cover: translation and
  endpoint reflection identify the same `S`, and `lambda=S-Delta` with
  `Delta>=0`.
- PD-T221: for `rho<=1/64`,
  `S<=a Lambda_c+242000 rho^2 log(n+1)+2048 rho^(3/2)+640 rho H/n`,
  `H=1+log(n+1)`; collisions and exact zeros included.
- PD-T224: for every admissible noncorner physical odd center, `n>=48`
  and `rho<=1/64`, `Delta>=1/4096`, uniformly in both phase signs.
- PD-T228: at either actual nonnode corner, `log n>=10^7` and inward
  `0<rho<=1/64` imply `lambda<Lambda_c`; this theorem averages before
  taking each cardinal absolute value and includes zero-cardinal terms.
- PD-T101/159 or PD-T229's exact parity reflection gives equality of the
  two nonnode-corner values.

No ineffective limiting threshold from PD-T217/225/229 is used in this
assembly. PD-T366's larger-radius defect and all-n energy estimates are
unnecessary here.

## Candidate proof

### 1. Uniform scalar bounds and the full physical cover

For `L>=20`, `pi^2<10` and PD-T157 give

\[
\Lambda_c\ge\tfrac25 L^2-54\ge\tfrac14L^2.             \tag{1}
\]

On the full closed phase diamond, the cosine chord bound yields

\[
1-a\ge\frac{\alpha^2+\beta^2}{\pi^2}
     \ge\frac{\rho^2}{2\pi^2}\ge\frac{\rho^2}{20}.       \tag{2}
\]

Every physical angle point belongs to a closed mesh rectangle with
vertices at `(J*pi/n,K*pi/m)`. Use an adjacent rectangle at a physical
boundary. Its two odd vertices are opposite. In coordinates normalized
to the unit mesh rectangle, the two L1 distances to these vertices sum
to two; at least one is at most one. Choosing that vertex gives a
physical odd center

\[
0\le J\le n,\quad0\le K\le m,\quad J+K\text{ odd},\qquad
\theta=(J\pi+\alpha)/n,\quad\phi=(K\pi+\beta)/m,
\quad\rho\le\pi.                                      \tag{3}
\]

This covers all edges, corners, nodes and mesh boundaries; uniqueness of
the center is unnecessary. As in PD-T215/225, translation by this odd
vertex turns the even periodic kernel board into the odd board of
PD-T216, and its positive endpoint factors retain the exact primitive
normalization. Hence `lambda=S_n(alpha,beta)-Delta`, `Delta>=0`,
for this very representation. The corrected mode remains in x.

### 2. Exclude all far phases

Suppose `L>=10^12` and `rho>=1/64`. By (1)--(2),

\[
(1-a)\Lambda_c\ge\frac{L^2}{327680}.
\]

The new numerical global bound and `log(n+1)<=L+1<=2L` imply

\[
S_n-\Lambda_c\le-\frac{L^2}{327680}+2\cdot10^6L<0,      \tag{4}
\]

since `10^12>327680*2*10^6=655360000000`.
Thus every point represented by a far phase is strictly below the
corner value. In particular the closed phase-diamond boundary, where
`a` may vanish, is covered without a separate limiting argument.

### 3. Explicit optimization of the entire near primitive envelope

For `rho<=1/64`, PD-T221 and (1)--(2) give

\[
S_n-\Lambda_c\le
 -\left(\frac{L^2}{80}-484000L\right)\rho^2
 +2048\rho^{3/2}+\frac{640H}{n}\rho.
\]

For `L>=10^12`, the coefficient in parentheses is at least
`A=L^2/160`, because `L>=160*484000`. Split its negative quadratic
term into two halves, and maximize each resulting expression over all
`rho>=0`. With `B=2048`, `D=640H/n`, elementary differentiation gives

\[
-\tfrac A2\rho^2+B\rho^{3/2}\le\frac{27B^4}{32A^3},
\qquad -\tfrac A2\rho^2+D\rho\le\frac{D^2}{2A}.          \tag{5}
\]

The first equality case has `sqrt(rho)=3B/(2A)`; the second has
`rho=D/A`. Hence no finite cusp or fractional term has been dropped.
The bounds also apply at `rho=0` by continuity. Since `H<=L+2<=2L`,

\[
\frac{27B^4}{32A^3}<\frac{10^{21}}{L^6}
   \le10^{-51}<\frac1{16384},\qquad
\frac{D^2}{2A}\le\frac{131072000}{n^2}
   <2^{-33}<\frac1{16384}.                              \tag{6}
\]

For the last bound, `L>=10^12` implies `n>2^30`, and
`131072000<2^27`. Therefore the uniform near-primitive excess obeys

\[
S_n-\Lambda_c<\frac1{8192}.                            \tag{7}
\]

### 4. Exclude every noncorner center

If the selected center `(J,K)` in (3) is not an actual nonnode corner,
PD-T224 applies to every such center for `n>=48`, both phase signs and
`rho<=1/64`. It includes the first four interior indices at every
endpoint, horizontal and vertical cases, and all remaining centers.
Consequently (7) and the exact defect identity give

\[
\lambda_n\le S_n-1/4096<\Lambda_c-1/8192.               \tag{8}
\]

There is no use of a defect restricted only to a vertical edge, or of a
limiting/macroscopic center argument. PD-T224 supplies the required
finite all-center quantifier.

### 5. Exclude punctured actual-corner phases and classify equality

The remaining selected center is a pair of odd endpoint indices.
Because the point is physical, its phases are inward, and `rho` is
exactly the inward scaled angle distance. Since `L>=10^12>10^7`,
PD-T228 gives strict inequality whenever `0<rho<=1/64`. Its polynomial
reflection proof includes the initially zero cardinals, corner collision
and both parity-correct corners, so no sign-preservation assumption or
new energy premise is required.

Thus every physical point other than the two nonnode corners is strictly
below `Lambda_c`. At phase zero at either such corner, the value is
`Lambda_c` by definition and the parity-valid reflection equality. The
odd endpoint pairs are `(n,m)` always, and `(0,m)` when n is even or
`(n,0)` when n is odd. Under the cosine map these are precisely the two
sets in the statement. This proves the proposed equality set.

Finally `n>=ceil(exp(10^12))` implies `log n>=10^12`, so every numerical
threshold used above is met. The preceding argument is pointwise on the
entire closed square and therefore establishes the proposed maximum
without an unquantified maximizing-sequence or compactness threshold.

## Checks, scope and open items

Written analytic developer assembly only; no numerical sampling, degree
extension, fit or energy extrapolation is a premise. Before a public
PROVED claim, the parent requires a distinct Astra high reconstruction
of the separate global lemma and this entire assembly, including all
quantifiers, normalizations, endpoints and exact equality classification.
Formal Claude audit remains separate.

The proposed `ceil(exp(10^12))` is an explicit upper boundary only. It
does not make the finite bridge feasible, improve the sharp N1 near-model
target, authorize an old-tech full-cover run or justify a Syvert pack.
The global finite certified range remains exactly `2--40`, and PD-T099
remains OPEN.

## History

2026-11-06, auxiliary Codex developer, parent-assigned mathematics;
serving model/effort not independently exposed. Rules/input
`4b728b04216a5490910780bc609a82b853058426`. The bounded global lemma is
kept separate so its proof survives even if this full assembly needs a
repair. The OPEN review boundary is explicit; no older proof or shared
registry has been changed.

## Dated independent acceptance — 2026-11-06

Current status is PROVED at the exact n>=ceil(exp(10^12)) scope above.
Distinct Astra high accepted the original complete proof at freeze
158ba6d607949697b9665ae663392613110aebc72e743697c92196d9608f1f42
and the global lemma d51554d208dd9e2fd92d2ec2f1b7b6f95e27dfa60e237146445ba49c498cb949.
See [independent reconstruction](../independent-checks-C01-effective.md),
report SHA7d834363647e2a2edf2688c00e194c1657e0d79a6ba19688c1bc3d5a3d90e4e5.
Only current-status/title/disposition prose is promoted; the mathematical
statement, assumptions, numerical constants and proof are unchanged.
Earlier candidate/review-boundary wording is historical. No claim of
practical feasibility, finite bridge closure or formal Claude audit.
