# PD-N?mz2d-frontier-codex-f3-01 — half-exactness is the exact threshold for uniform signed strong MZ

ID kind: PD-N.
Aliases: F3 exact ratio threshold; every super-half ratio fails;
even-carrier Fejér countersequence.
Split from: the positive-inequality assertion in existing PD-T116.
Split into: none. The common fixed-node weight lemma is separately
PROVED as `PD-T?mz2d-frontier-codex-12`.

## Statement

Use the fixed signed interpolatory Lebesgue Padua rule Q_m, total-degree
spaces Pi_n and unnormalized dxdy measure from the campaign definitions.

For `0<=theta<=1/2`, every `m>=1,n<=theta*m,p in Pi_n` satisfies
`Q_m(p^2)=integral p^2`, so eta is zero. This is inherited routine
half-exactness, included to state the sharp threshold.

For every real `1/2<theta<1`, put

\[
 \delta=\theta-\tfrac12,\quad a=\delta/4,\quad
 r_m=s_m=\lfloor am\rfloor,\quad n_m=\lfloor\theta m\rfloor.
\]

Let the degree-r Fejér polynomial be

\[
 \mathcal F_r(x)=1+2\sum_{\ell=1}^r
   \left(1-\frac{\ell}{r+1}\right)T_\ell(x),
\]

and, for even m, define the explicit real polynomial

\[
 p_m(x,y)=T_{m/2}(x)\mathcal F_{r_m}(x)\mathcal F_{s_m}(y).
                                                               \tag{1}
\]

Then `p_m in Pi_(n_m)` and

\[
 \lim_{\substack{m\to\infty\\2\mid m}}
 \frac{Q_m(p_m^2)}{\log m}
 =-\frac{16a^2}{9}=-\frac{\delta^2}{9}<0.             \tag{2}
\]

Consequently Q_m(p_m^2)<0 for all sufficiently large even m, and

\[
 \lambda_{\min}(m,\lfloor\theta m\rfloor)\longrightarrow-\infty
 \quad\text{along even }m.                           \tag{3}
\]

In particular no uniform eta(theta)<1 exists at any theta>1/2.
The entire positive strong-MZ assertion of PD-T116 is **REJECTED:
refuted**; its counterexample alternative is resolved analytically.
No explicit first violating m or effective threshold is asserted.

## Definitions

The physical nodes are `(cos(j*pi/m),cos(k*pi/(m+1)))`, j+k even,
with j=0..m and k=0..m+1. Their weights are the actual signed
interpolatory dxdy weights. Let epsilon_j,eta_k equal one in the
interior and one half at the respective endpoints. In fixed-index
limits write e_0=1/2 and e_j=1 for j>=1.

Legendre Gram eigenvalues and eta use continuous orthonormal products,
as in PD-T116. The squared continuous norm of a nonzero polynomial is
strictly positive, irrespective of the signs of its sampled energy.

## Assumptions

Every fixed real theta in (1/2,1), even integer m tending to infinity,
real exact arithmetic, the stated Fejér/carrier polynomials and fixed
checkerboard/measure conventions. Only an even-m countersequence is
needed to refute the universal quantifier in PD-T116.

## Status by part

Overall status: **PROVED** in analytic development; required Claude
audit pending. Supplementary independent reconstruction of the common
weight lemma and packet argument is recorded separately by its checker.

| Mathematical part | Status | Evidence / limitations |
|---|---|---|
| Failure at every fixed theta>1/2, explicit countersequence (1)–(2) | PROVED | Fixed-node weight limit with a global summable majorant, plus exact finite trapezoid identities |
| Divergent negative Gram endpoint (3) | PROVED | Explicit uniform continuous-norm upper bound |
| Exactness at theta<=1/2 | PROVED, routine inherited context | Degree-m exactness; not a newly allocated positive result |

Candidate / claim disposition: the proposed uniform signed positive
bound above half-exactness is **REJECTED: refuted**. The countersequence
is retained. This is not merely failure of a proof route.

## Negative-result scope

Attempted assertion: PD-T116's positive lower inequality (and therefore
its strong symmetric eta(theta)<1 inequality), for every fixed ratio
below one. Parameter range refuted: **every** fixed theta in (1/2,1),
on all sufficiently large even m. Half-exactness theta<=1/2 remains
valid. The explicit positive reference form S_m from the separate smooth
diamond theorem is unaffected; it is not Q_m.

## Depends on

`PD-T?mz2d-frontier-codex-12`,
[fixed-node weight limit and global majorant](f12-local-weight-asymptotic.md),
whose complete proof was read and independently reconstructed by this
F3 developer before the corollary. Its derivation uses the locally
proved cardinal identity PD-T101/111 and elementary Fourier tails.
The carrier mechanism was supplied by the F1/F2 developer; the full
packet theorem is also retained in that developer's separate record.
The elementary finite trapezoid and norm calculations are given below.
No numerical spectrum, external MZ theorem or unverified asymptotic fit
is used.

## Checks

Analytic F3 reconstruction checks: exact weight prefactor and the m+1
y phase; thin-corner limit with R tending to infinity before its strip
width tends to zero; uniform triangle bound; moving far endpoints;
summable packet domination; finite alternating trapezoid identities;
polynomial degree; uniform physical norm. The F3 developer executed no
mathematical program for this result. An effective violating m is not
computed. Supplementary checker and required Claude audit are separate.

## Sources

Full local predecessors IDEA-216/217/218/226, PD-N047/048/049, and the
new F1/F2 candidate/weight development. Full novelty-gate scope is in
`../ideas-f3.md`. The countersequence is a variant using an exact
parity-selecting carrier; no historical priority claim is made.

## Proof or evidence

### 1. Admissible degree and bounded continuous norm

Since a<1/8,

\[
 \deg p_m=m/2+r_m+s_m
 \le(\tfrac12+2a)m=(\tfrac12+\delta/2)m<\theta m.
\]

The degree is an integer, so it is at most floor(theta*m). The polynomial
is nonzero. At the x grid the carrier is exactly
`T_(m/2)(x_j)=cos(j*pi/2)`, hence vanishes on every odd j.

For L=r+1 and 0<t<=pi, the finite geometric sum gives

\[
 0\le\mathcal F_r(\cos t)
 \le\min\{L,\pi^2/(Lt^2)\}.
\]

As sin t<=t, split its squared physical integral at 1/L to obtain

\[
 \int_{-1}^1\mathcal F_r(x)^2dx
 \le \int_0^{1/L}tL^2dt
 +\int_{1/L}^\pi\frac{\pi^4}{L^2t^3}dt
 \le C_0:=\frac{1+\pi^4}{2}.                        \tag{4}
\]

The carrier has absolute value at most one, so
`0<||p_m||_2^2<=C_0^2`, uniformly in m.

### 2. The common weight limit can be summed against these packets

For every fixed retained j,k the common lemma gives

\[
 \frac{m^4w^{(m)}_{j,k}}{\log m}
 \longrightarrow-16e_je_k(-1)^j,                    \tag{5}
\]

and, uniformly across the finite grid,

\[
 |w^{(m)}_{j,k}|\le Cm^{-4}
       \{(1+j)(1+k)+\log(m+1)\}.                   \tag{6}
\]

The Fejér estimate above shows that for all sufficiently large m,

`|F_(r_m)(x_j)|/m <= C_a(1+j)^(-2)` and
`|F_(s_m)(y_k)|/m <= C_a(1+k)^(-2)`.

For j>=1 this follows from the geometric bound with t=j*pi/m and
`r_m+1>=am/2`; the y bound uses the adjacent denominator m+1 and only
changes C_a. The j=0,k=0 values are bounded by `(r_m+1)/m`. The carrier
is bounded by one. Combining with (6), the absolute normalized summand
`w_(j,k) p_m(x_j,y_k)^2/log m` is dominated by a fixed multiple of

\[
 (1+j)^{-3}(1+k)^{-3}+(1+j)^{-4}(1+k)^{-4},
\]

which is summable on the nonnegative integer quadrant. Extend the
finite-grid summand by zero outside its grid. Fixed-index convergence
and this summable majorant justify passing the limit through the sum;
moving far endpoints cause no additional term.

Let f_j and g_k be the limits of `F_(r_m)(x_j)/m` and
`F_(s_m)(y_k)/m`; they exist by the geometric-sum formula, with
f_0=g_0=a. Define

\[
 A_x=\sum_{j\ge0}e_j\cos^2(j\pi/2)f_j^2,
 \quad B_x=\sum_{j\ge0}e_j(-1)^j\cos^2(j\pi/2)f_j^2,
\]
\[
 A_y=\sum_{k\ge0}e_kg_k^2,\qquad
 B_y=\sum_{k\ge0}e_k(-1)^kg_k^2.
\]

All converge absolutely. Inserting the checkerboard indicator
`(1+(-1)^(j+k))/2` into (5) gives

\[
 \lim Q_m(p_m^2)/\log m=-8(B_xA_y+A_xB_y).           \tag{7}
\]

### 3. Finite trapezoid identities evaluate all four factors

The squared Fejér polynomial has trigonometric degree 2r and constant
Fourier coefficient

\[
 c_r=1+2\sum_{\ell=1}^r(1-\ell/(r+1))^2
     =\frac{2(r+1)^2+1}{3(r+1)}.                    \tag{8}
\]

For any cosine polynomial h of degree less than M, the finite geometric
series and reflection give

\[
 \sum_{j=0}^M\epsilon_j h(j\pi/M)=M\widehat h(0),
 \qquad
 \sum_{j=0}^M\epsilon_j(-1)^j h(j\pi/M)=0.          \tag{9}
\]

The second identity is the periodic character at frequency M and uses
the strict degree cutoff. Here 2r_m<m and 2s_m<m+1. Since
`cos^2(j*pi/2)=(1+(-1)^j)/2`, (9) gives exactly

\[
 \frac1{m^2}\sum_{j=0}^m\epsilon_j
      \cos^2(j\pi/2)\mathcal F_{r_m}(x_j)^2
 =\frac{c_{r_m}}{2m}\longrightarrow a/3.
\]

The carrier vanishes on odd j, so B_x=A_x=a/3. Similarly the y
identities give

\[
 \frac1{m^2}\sum_{k=0}^{m+1}\eta_k
      \mathcal F_{s_m}(y_k)^2
 =\frac{(m+1)c_{s_m}}{m^2}\longrightarrow2a/3,
\]

while its alternating sum is exactly zero. The same profile domination
justifies passing these finite sums to their infinite limits. Therefore
`A_y=2a/3` and `B_y=0`. Substitution into (7) proves (2).

### 4. The signed spectral and ratio consequences

Equation (2) is strictly negative, so (1) is an actual negative-energy
polynomial for all sufficiently large even m. For such m, (4) and the
Rayleigh principle give

\[
 \lambda_{\min}(m,n_m)
 \le\frac{Q_m(p_m^2)}{\|p_m\|_2^2}
 \le\frac{Q_m(p_m^2)}{C_0^2}\longrightarrow-\infty.
\]

The direction of the second inequality uses the negative numerator.
In fact
`limsup lambda_min/log m <= -delta^2/(9 C_0^2)` and therefore
`liminf eta(m,n_m)/log m >= delta^2/(9 C_0^2)` along even m.
No nonnegative, uniformly coercive signed form—and in particular no
eta(theta)<1—can hold at this theta. For theta<=1/2, degree-m exactness
applies to every square in the target space. This proves the stated
threshold and its negative consequences. ∎

## Scope

The countersequence is explicit, but the proof gives a noneffective
eventual threshold. It is an analytic refutation of a universal
assertion, not a certified finite-degree numerical counterexample.
The prior finite spectra can all remain positive within their measured
or certified ranges. There is no assertion that their numerical results
were wrong, nor any inferred first crossing.

## Open items

Required Claude audit of the common lemma, packet summation and this
corollary. An effective remainder or a finite explicit violating m
remains a separate quantitative task. Positive-weight reference MZ
and actual signed MZ must retain distinct notation and conclusions.

## History

2026-11-05, Codex F3 developer, requested gpt-6.1-sol xhigh; rules/input
`83cf6f1ee244f2e72057332a7ec04ee74db1f0de`. The initial F3 continuation
correctly recorded OPEN after the positive-reference theorem. F1/F2's
new fixed-node/carrying-packet mechanism then supplied a genuine
countersequence. This corollary records the exact theta classification
without deleting the earlier incomplete proof routes. No mathematical
program was executed by this developer and no final ID allocated.
