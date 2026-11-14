# PD-T?argmax-bridge-codex-N5-01 — uniform fourth-order truncated cotangent sums

ID kind: PD-T.
Aliases: two-pole extraction; arbitrary-offset sign-block quadrature;
corrected-midpoint cotangent partial sums.
Split from: supporting partial-sum obligation of IDEA329/T226, resumed
by the N1/N5 bridge workers. The original uniform primitive and E-C
targets remain OPEN.
Split into: none; N1 owns the separate Padua absolute-row assembly.

## Statement

For every integer n>=2 set h=pi/n. Let delta be real and a<=b integers
such that 0<a+delta<=b+delta<n. Put

\[
x_i=h(i+\delta),\quad q=b-a+1,\quad
L=x_a-h/2,\quad R=x_b+h/2,
\]
\[
w(x)=\cot x-\frac1x+\frac1{\pi-x},\qquad
W(x)=\log\frac{\sin x}{x(\pi-x)}.                         \tag{1}
\]

Both functions take their continuous values at 0 and pi. They are smooth
on the entire interval [-pi/4,5pi/4]; the ratio in W is positive there.
Define the completely explicit partial-sum expression

\[
\begin{split}
Q_{n,\delta}(a,b)={}&\frac1h\sum_{i=a}^b
 \left(\frac1{i+\delta}-\frac1{n-i-\delta}\right)\\
&+\frac{W(R)-W(L)}h
 -\frac h{24}\bigl(w'(R)-w'(L)\bigr).                    \tag{2}
\end{split}
\]

Then, with no lower bound on any sample's distance from 0 or pi,

\[
\boxed{\left|\sum_{i=a}^b\cot x_i-Q_{n,\delta}(a,b)\right|
\le\frac{1064}{3645\pi^5}\,q h^4
<\frac7{7200}\,q h^4.}                                  \tag{3}
\]

For an arbitrary finite union of disjoint such blocks on the same mesh,
the sum of their Q expressions has error bounded by the same constant
times the **total sample count**. There is no factor for the number of
blocks. In particular, any subset of at most n nonpole samples from one
period can be split into blocks and bounded by 7pi^4/(7200n^3).
For coefficients c_l and possibly different admissible block meshes,
the corresponding error is at most

\[
\frac7{7200}\sum_l |c_l|q_lh_l^4.                       \tag{4}
\]

## Definitions and endpoint values

All logarithms are natural. The shifted reciprocal sums in (2) are
retained exactly; no logarithmic approximation to those poles is made.
Useful continuous values are

\[
W(0)=W(\pi)=-\log\pi,\quad
w(0)=1/\pi,\quad w(\pi)=-1/\pi,
\]
\[
w'(x)=-\csc^2x+1/x^2+1/(\pi-x)^2,\qquad
w'(0)=w'(\pi)=-1/3+1/\pi^2.                              \tag{5}
\]

The last line is evaluated by its limit at the two endpoints.

## Assumptions and status

Exact real arithmetic and precisely the strict sample-domain condition
above. Formula (2) is an analytic model, not an outward-rounded evaluator.
Overall status: **PROVED**, by the written elementary proof below.
Independent review and the required later Claude audit are pending.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Uniform arbitrary-offset/block bound (3), all n>=2 | PROVED | Fourth derivative and one-cell kernel below |
| Union/weighted bounds (4) | PROVED | Triangle inequality; total counts add |

The claim is a supporting 1D result. It does not change the OPEN status
of all-degree E-C, the full-diamond profile or PD-T099.

## Depends on

Elementary Fourier-series proof of the cotangent partial fraction,
already written locally in PD-T269 §4 and restated below. No Padua
asymptotic, classical 1D ordering theorem, numerical experiment,
unproved quadrature formula or source-reading assertion is a premise.
T226 motivates the exact domain needed for the application; its row
identity is not needed to prove this standalone result.

## Proof

### 1. Removing both poles gives a uniform fourth derivative

The elementary partial fraction is

\[
\cot x=\frac1x+\sum_{k=1}^\infty
 \left(\frac1{x-k\pi}+\frac1{x+k\pi}\right).              \tag{6}
\]

For completeness, the cosine-series coefficients of cos(zt) on [0,pi]
are a_0=2sin(pi z)/(pi z) and
a_k=2(-1)^k z sin(pi z)/(pi(z^2-k^2)). Direct integration proves this.
For noninteger z the coefficients are absolutely summable; evaluation
at t=pi and division by sin(pi z) gives (6), with x=pi z. This is the
same local derivation as T269, not a citation of an unread source.

Removing the k=0 and k=1 poles gives

\[
w(x)=\frac1{x+\pi}+
 \sum_{k=2}^\infty\left(\frac1{x-k\pi}+\frac1{x+k\pi}\right).
                                                                    \tag{7}
\]

The paired series and its derivatives converge uniformly on
J=[-pi/4,5pi/4]. For the undifferentiated paired series the terms are
O_J(k^-2); for each positive derivative the series is absolutely
convergent. Thus w is smooth on J, including 0 and pi. Its fourth
derivative obeys

\[
|w^{(4)}(x)|\le24\sum_{k\in\mathbb Z\setminus\{0,1\}}
                  |x-k\pi|^{-5}
\le\frac{48}{\pi^5}\sum_{l=1}^\infty(l-1/4)^{-5}.        \tag{8}
\]

Indeed each of the two remaining half-lattices has its l-th pole at
distance at least pi(l-1/4) from J. A decreasing-integral comparison gives

\[
\sum_{l=1}^\infty(l-1/4)^{-5}
\le(4/3)^5+\int_1^\infty(t-1/4)^{-5}dt
=\frac{1216}{243}.
\]

Consequently

\[
M_4:=\sup_J|w^{(4)}|\le\frac{19456}{81\pi^5}<\frac45.     \tag{9}
\]

The final comparison follows already from the elementary pi>157/50
and the exact integer inequality
5*19456*50^5 < 4*81*157^5. The sharper first bound in (9) is retained
in (3); using merely pi>3 would also give M_4<1.

The function sin x/[x(pi-x)] is positive and smooth on J after its
removable endpoint values are restored. Its logarithmic derivative is
w, so W'=w on all of J. This also proves the required smooth extension
of W and the endpoint values (5).

### 2. One-cell corrected midpoint error with its exact constant

Let f be C^4 on [-r,r], where r=h/2. Define

\[
\mathcal L_h(f)=\frac1h\int_{-r}^rf(t)dt
 -\frac h{24}\bigl(f'(r)-f'(-r)\bigr)-f(0).
\]

Taylor's formula with integral fourth-order remainder, applied separately
on the positive and negative halves, gives exactly

\[
\mathcal L_h(f)=\int_0^r K_h(t)
                 \bigl(f^{(4)}(t)+f^{(4)}(-t)\bigr)dt,
\]
\[
K_h(t)=\frac{(r-t)^4}{24h}-\frac{h(r-t)^2}{48}.            \tag{10}
\]

The constant and quadratic terms cancel, and odd terms integrate to zero.
Since 0<=r-t<=h/2, K_h(t)<=0. Direct polynomial integration gives

\[
2\int_0^r|K_h(t)|dt=\frac{7h^4}{5760}.
\]

Therefore

\[
|\mathcal L_h(f)|\le\frac{7h^4}{5760}
                         \sup_{[-r,r]}|f^{(4)}|.          \tag{11}
\]

This derivation is included to fix the sign and coefficient of the
endpoint derivative correction; no Euler–Maclaurin theorem is imported.

### 3. Telescope over any block, retaining its exact pole terms

Because every x_i lies strictly between 0 and pi and n>=2, every centered
cell [x_i-h/2,x_i+h/2] is inside J. Apply (11) to f(t)=w(x_i+t)
and sum over the q consecutive indices. Adjacent cells share endpoints,
so their integrals and endpoint derivative differences telescope:

\[
\left|\sum_{i=a}^b w(x_i)
 -\frac{W(R)-W(L)}h
 +\frac h{24}\bigl(w'(R)-w'(L)\bigr)\right|
\le\frac{7q h^4 M_4}{5760}.                              \tag{12}
\]

For each sample the exact identity

\[
\cot x_i=\frac1h\left(\frac1{i+\delta}
                   -\frac1{n-i-\delta}\right)+w(x_i)
\]

has finite reciprocal denominators by the strict domain hypothesis.
Insert this in (12) and use (9). Since
7*19456/(5760*81)=1064/3645, this is exactly (3).
Errors of disjoint blocks, or weighted block expressions, add by the
triangle inequality, proving the union assertion and (4). Splitting an
arbitrary subset of one period at all gaps retains the same total count,
so its bound has no dependence on the number of blocks. This completes
the proof. ∎

## Quantitative interface and scope

The uncorrected midpoint formula has an h^2 error per sample; (3) has
h^4 with a small explicit constant. It applies to arbitrarily truncated
pieces of the T226 sign intervals, even when their nearest cotangent
sample is arbitrarily close to a pole. Shifted reciprocal sums remain
part of the model; replacing them by log integrals would need a separate
bound and would reintroduce a pole-distance question.

Multiplication by a coefficient tending to zero must be performed on the
full expression before any removable collision limit. A sample exactly
at a pole is outside this theorem. T226's finite polynomial collision
values cannot be recovered by separately substituting in (2). N1 owns
and must prove that Padua assembly, its endpoint rows and its sign-set
transitions. No finite degree cutoff or whole-cell supremum comparison
is proved here.

## Checks and sources

Analytic proof only. The 130 developer high-precision sanity checks in
`../evidence/n5-partial-cotangent.json` are separate MEASURED verification,
including offsets 10^-30 from either pole at n=2,3,7,33,128. The largest
observed error/bound ratio is approximately 0.11038. The exact quartic
functional check gives -7/5760. No computation is a premise; no distinct
rerun or audit is claimed. Exact source reading, gate, candidate dispositions and external
access limits are in `../novelty-gate-N5.md`,
`../ideas/N5-partial-cotangent.md` and `../literature-N5.md`.

## Open items

Distinct mathematical review; required later Claude audit. N1's complete
absolute-row application and its uniform-degree profile are separate
obligations. E-C with independent maximizing phases remains OPEN.

## History

2026-11-05, Codex assigned gpt-6.1-sol xhigh, rules/input
`98d6c00d8a474cf97602c9cfdea631a837191ac0`; actual model metadata not
independently exposed. N1 supplied the two-pole second-order midpoint
interface. N5 added the endpoint derivative correction and proved its
arbitrary-block fourth-order constant. No self-audit, source-theorem
transfer, global ID, Git action or shared registry edit.

## Provisional-label normalization — 2026-11-05

Coordinator normalized the provisional prefix to the handoff convention,
adding `codex` to the earlier `?argmax-bridge-N5-*` aliases.
Those earlier aliases remain historical references; no final ID, mathematical
statement, proof, executable source or run receipt changed.
