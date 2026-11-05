# PD-N105 — an admissible carrier has eventual negative Padua energy

Development alias: `PD-N?mz2d-frontier-codex-13`. Final ID assigned during audited preparation; [mapping](../preparation/final-id-map.json).

ID kind: PD-N.
Aliases: even-even carrier countersequence; signed Padua positivity
failure; negative logarithmic sampled energy.
Split from: IDEA-389. Original PD-T028 positivity
and endpoint-order targets are preserved; this proves a countersequence.
Split into: the common weight lemma is PD-T295;
the opposite-sign upper sequence is separate PD-N106.

## Statement

Fix real a,b>0 with a+b<1/2. Let m tend to infinity through even integers,
put `r=floor(a*m)`, `s=floor(b*m)`, and define the **degree-r** Fejer
polynomial by

\[
 F_r(\cos t)=\frac1{r+1}
 \left(\frac{\sin((r+1)t/2)}{\sin(t/2)}\right)^2
 =1+2\sum_{\ell=1}^{r}\left(1-\frac\ell{r+1}\right)\cos(\ell t).
                                                               \tag{1}
\]

Use removable endpoint values. Define

\[
 p^-_m(x,y)=T_{m/2}(x)F_r(x)F_s(y).
\]

For all sufficiently large even m this is a nonzero polynomial of total
degree `m/2+r+s<=m−1`, and the actual signed Padua rule satisfies

\[
 \lim_{\substack{m\to\infty\\2\mid m}}
 \frac{Q_m((p^-_m)^2)}{\log m}=-\frac{16ab}{9}<0.       \tag{2}
\]

Also, with `C_0=(1+pi^4)/2`,

\[
 0<\|p^-_m\|_{L^2(dxdy)}^2\le C_0^2.                 \tag{3}
\]

Consequently the endpoint signed minimum has

\[
 \lambda_-(m,m-1)\longrightarrow-\infty
 \quad\hbox{along the even integers}.                 \tag{4}
\]

In particular positivity on Pi_(m−1) for every m is false. The proposed
positive log^(-2) or log^(-4) endpoint orders and endpoint eta convergence
to one are false for this signed rule. The conclusion is an analytic
eventual countersequence; no explicit finite violating m is asserted.

## Definitions

Q_m, its signed interpolatory weights, dxdy normalization and total-degree
spaces are exactly the frozen previous-campaign definitions. In (1), F_r
has degree r and endpoint value r+1; this differs by one from the common
length-r notation for a Fejer kernel. Let `theta_j=j*pi/m`,
`phi_k=k*pi/(m+1)`, with endpoint halfweights epsilon_j,eta_k from -12.

## Assumptions

a,b fixed and positive; a+b<1/2; m even and sufficiently large that
r,s>=1 and the displayed degree fits m−1. No sign hypothesis on the
quadrature weights and no spectral conjecture is assumed.

## Status by part

Overall status: **PROVED** (analytic development; independent reconstruction complete; Claude audit-01 accepted).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Exact degree, bounded norm and negative limit (2) | PROVED | Finite DCT identities and dominated convergence |
| Eventual failure of positivity, endpoint positive orders and eta->1 | PROVED | Variational consequences of the explicit packet |

Candidate / claim disposition: the universal positivity claim is
**REJECTED: refuted** by the countersequence (2). The packet mechanism
is retained. No finite float observation is used as a refutation.

## Negative-result scope

Refuted statement: `lambda_-(m,m−1)>0 for every integer m>=2`, with the
fixed signed Lebesgue Padua conventions. The stronger divergence (4)
is along even m. No statement classifies the odd-m subsequence or names
an explicit threshold. Positive cubature and tensor-CC rules are outside
this conclusion.

For any fixed theta>1/2 one can choose a,b>0 with
`1/2+a+b<theta`; then this same polynomial belongs to
Pi_floor(theta*m) eventually. Thus it also supplies a fixed-ratio
countersequence. The full sharp-ratio classification is a separate
F3 synthesis, not duplicated here.

## Depends on

PD-T295: the exact fixed-node weight asymptotic and
its whole-grid majorant. Elementary finite cosine orthogonality below.
The argument uses no inherited positive Padua form, eigenvalue fit,
external theorem or unproved weight-sign classification.

[Claude audit-01](../audit-01.md) accepted the mathematics at its stated scope; [response-01](../response-01.md) addresses the editorial findings. Supplementary reconstruction is recorded in [independent-checks-math.md](../independent-checks-math.md).

## Checks

Rules/input `83cf6f1ee244f2e72057332a7ec04ee74db1f0de`.
This developer executed no mathematical computation. Independent
reviewers received the core lemma and finite-DCT constants, and their
finished reports must be attached separately with actual file hashes.
The proof is analytic; it does not require an exact computer certificate.

## Sources

Complete predecessor gate and the retained original unmodulated packet
are in ../ideas-f12.md. IDEA-216/PD-N047 excluded a different two-critical-
factor construction; IDEA-217/PD-N048 explained why negative corner
weights alone are insufficient. Here the whole signed form is evaluated.
No historical novelty claim is made.

## Proof or evidence

### Degree and norm

The finite cosine identity (1) proves polynomiality and exact degree.
The product has total degree m/2+r+s; since a+b<1/2, this is at most
m−1 eventually. The factors are nonzero, so p^-_m is nonzero.

For every integer u>=0 and 0<t<=pi,

\[
 |F_u(\cos t)|\le
 \min\left(u+1,\frac{\pi^2}{(u+1)t^2}\right).           \tag{5}
\]

The first bound follows from the sum of the nonnegative coefficients
in (1), and the second from `sin(t/2)>=t/pi`. With L=u+1, split the
continuous integral at 1/L and use sin t<=t:

\[
 \|F_u\|_2^2
 \le L^2\int_0^{1/L}t\,dt
 +\frac{\pi^4}{L^2}\int_{1/L}^{\pi}t^{-3}\,dt
 \le\frac{1+\pi^4}{2}=C_0.                            \tag{6}
\]

Since |T_(m/2)|<=1 on [-1,1], product integration proves (3).

### Limiting sampled energies, determined by finite DCT

For mesh denominator M let endpoint halfweights be c_0=c_M=1/2,
all others one. Elementary geometric sums give

\[
 \sum_{j=0}^M c_j\cos(\ell j\pi/M)=0
 \quad(1\le\ell\le2M-1),\qquad \sum c_j=M.           \tag{7}
\]

Thus a cosine polynomial h of degree <M has zero alternating sum
`sum c_j(-1)^j h(cos(j*pi/M))`; its ordinary weighted sum is M times
its constant Chebyshev coefficient.

The constant coefficient of F_u² is exactly

\[
 D_u=1+2\sum_{\ell=1}^{u}\left(1-\frac\ell{u+1}\right)^2
 =1+\frac{u(2u+1)}{3(u+1)},\qquad D_u/u\to2/3.        \tag{8}
\]

Because 2r<m and 2s<m+1 eventually, apply (7) to F_r² and F_s².
Set

\[
 U_{m,j}=\cos^2(j\pi/2)\left(\frac{F_r(\cos\theta_j)}m\right)^2,
 \qquad
 V_{m,k}=\left(\frac{F_s(\cos\phi_k)}m\right)^2.
\]

Then U_(m,j)=0 for odd j, and exactly

\[
 \sum_j\epsilon_j U_{m,j}=\frac{D_r}{2m}\to\frac a3,
\quad
 \sum_k\eta_k V_{m,k}=\frac{(m+1)D_s}{m^2}\to\frac{2b}{3},
\quad
 \sum_k\eta_k(-1)^k V_{m,k}=0.                       \tag{9}
\]

The first equality uses `cos²(j*pi/2)=(1+(-1)^j)/2` and the zero
alternating sum of F_r².

For completeness all uses of these finite sums in the infinite limit
are justified as follows. For fixed j>=0,

\[
 \frac{F_{\lfloor am\rfloor}(\cos(j\pi/m))}{m}
 \longrightarrow f_a(j):=
 \begin{cases}
 a,&j=0,\\
 \dfrac1a\left(\dfrac{\sin(a\pi j/2)}{\pi j/2}\right)^2,&j>0.
 \end{cases}                                         \tag{10}
\]

The y mesh m+1 has the same limiting formula with b. Uniformly over
their entire finite grids, for sufficiently large m,

\[
 |F_r(\cos\theta_j)|/m\le C_a(1+j)^{-2},\qquad
 |F_s(\cos\phi_k)|/m\le C_b(1+k)^{-2}.                \tag{11}
\]

Indeed r+1>am, the endpoint bound is `(r+1)/m<=2a` eventually, and
for j>=1 the inequality `sin(j*pi/(2m))>=j/m` gives the upper bound
`1/(a j²)`. For y the analogous bound has `(m+1)²/[m(s+1)]<=4/b`.
Enlarge the constants to join the endpoint and positive-index bounds.

Extend finite arrays by zero beyond their grids. Equation (11) gives
summable domination for every squared profile, including alternating
ones. The moving far halfweights therefore disappear harmlessly in
the limit. Writing

\[
 u_j=\cos^2(j\pi/2)f_a(j)^2,\quad v_k=f_b(k)^2,
 \quad e_0=1/2,\ e_j=1\ (j>0),
\]

equations (9) imply

\[
 \sum_j e_ju_j=\frac a3,\quad u_j=0\ (j\text{ odd}),
 \quad\sum_k e_kv_k=\frac{2b}3,\quad
 \sum_k e_k(-1)^kv_k=0.                              \tag{12}
\]

### Whole signed form and its negative coefficient

The common weight theorem gives pointwise convergence of the factors
in

\[
 \frac{Q_m((p^-_m)^2)}{\log m}
 =\sum_{\substack{0\le j\le m,\ 0\le k\le m+1\\j+k\ {\rm even}}}
 \frac{m^4w^{(m)}_{j,k}}{\log m}\,U_{m,j}V_{m,k}.       \tag{13}
\]

It also bounds the absolute summand, uniformly for m large, by a
constant times

\[
 \frac{(1+j)(1+k)+1}{(1+j)^4(1+k)^4}
 \le\frac2{(1+j)^3(1+k)^3},                           \tag{14}
\]

using that `log(m+1)/log m` stays bounded. This double series is
summable. Dominated convergence applies to (13); no unsigned corner
majorant is being subtracted from an unrelated norm estimate.

Only even j survive in the limit, and the checkerboard then retains
only even k. Equation (1) of -12 and (12) therefore give

\[
 \lim\frac{Q_m((p^-_m)^2)}{\log m}
 =-16\left(\sum_{j\ \text{ even}}e_ju_j\right)
       \left(\sum_{k\ \text{ even}}e_kv_k\right)
 =-16\frac a3\frac b3=-\frac{16ab}{9}.
\]

This proves (2).

### Spectral consequences

For any fixed `0<c<16ab/(9C_0²)`, (2) and (3) imply for all
sufficiently large even m that the actual signed Rayleigh quotient
of p^-_m is at most `−c log m`. The variational principle and inclusion
in Pi_(m−1) give the same upper bound for lambda_-(m,m−1), proving (4).
In particular it is eventually negative, so it cannot have either
proposed positive endpoint order. Also
`eta(m,m−1)>=1−lambda_-(m,m−1)` diverges along this subsequence, hence
cannot tend to one. ∎

## Scope

This is an analytic refutation of the all-m signed positivity target,
and stronger than a finite certificate for that quantifier. It does
not name the first violating m or supply a computable explicit onset.
The packet may become negative much later than a numerically optimized
eigenvector. No odd-m or sharp asymptotic extremal law is claimed.

These explicit carriers prove existence only; they are not usable finite witnesses at feasible degrees, as illustrated by the auditor’s MEASURED extrapolations ([audit-01, A2](../audit-01.md) and [carrier fits](../audit-01-support/subagent-f3/audit-diamond.md)); those extrapolations are not onset bounds and these carriers are unrelated to the m1600 float hit.

## Open items

Independent full-file reconstruction and Claude audit-01 are complete; see the references below.
Obtain an exact finite violating witness if useful; this is a separate
constructive/effective task. Determine the sharp growth constants of
the true extremes and behavior on odd m. The original positive-order
questions are refuted, rather than silently narrowed to a finite range.

## History

2026-11-05, Codex F1/F2 developer, requested gpt-6.1-sol xhigh; runtime
metadata unexposed. The original unmodulated Fejer packet was retained
as measured/deferred, and replaced here by an exact parity carrier.
This proof makes no use of a floating eigenvalue crossing. No Git.

2026-11-05: mechanical final-ID registration after accepted Claude audit-01 and response-01. The earlier audited source/receipt identities are historical; proof content changes only by ID substitution.
