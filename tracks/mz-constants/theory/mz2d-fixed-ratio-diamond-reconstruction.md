# PD-T115 — exact diamond-filter reconstruction on the checkerboard

Provisional alias: `PD-T?mz2d-codex-40`. Final ID assigned at PR preparation, 2026-11-01; required Claude audit PENDING.

ID kind: PD-T. Aliases: diagonal-angle filtered reconstruction; parity
projected square-to-diamond filter. Split from: supporting reconstruction
step of D4, not a parameter case of its spectral target. Split into: none.

## Statement

For every integer `m>=1` and `0<=n<m`, an explicit kernel with frequency
support `|a|+|b|<=m-1` reproduces all trigonometric polynomials with
frequency support `|a|+|b|<=n` by normalized convolution with samples on
the periodic even checkerboard `Gamma_m` defined below. Consequently it
reconstructs every `p(cos t,cos s)` for `p in Pi_n` from the physical
Padua samples, via their angular reflection extension.

## Definitions

The periodic checkerboard and scalar kernel are

\[
 \Gamma_m=\{(j\pi/m,k\pi/(m+1)):
 0\le j<2m,\ 0\le k<2(m+1),\ j+k\equiv0\pmod2\},
 \quad |\Gamma_m|=2m(m+1),
\]
\[
 F_M(t)=\frac1M\left|\sum_{h=0}^{M-1}e^{iht}\right|^2,
 \qquad K(t)=\frac{mF_m(t)-nF_n(t)}{m-n},
\]

with `nF_n=0` at n=0. For real angles t,s put `u=(t+s)/2`,
`v=(t-s)/2`, and set

\[
 H_{m,n}(t,s)=\tfrac12\{K(u)K(v)+K(u+\pi)K(v+\pi)\}.              \tag{1}
\]

The reconstruction is the exact finite identity

\[
 q(t,s)=\frac1{2m(m+1)}\sum_{(t_j,s_k)\in\Gamma_m}
 H_{m,n}(t-t_j,s-s_k)q(t_j,s_k).                    \tag{2}
\]

All torus measures here are counting measures normalized by the displayed
factor. Equation (2) uses no signed Lebesgue weight and asserts no norm
comparison with that signed rule.

## Assumptions and status

Only integer `m>=1`, integer `0<=n<m`, and the stated Fourier-support
hypothesis. Overall status: **PROVED** in development; independent audit
pending. This substantive supporting theorem repairs the exactness step
of the failed rectangular transfer. The original fixed-ratio eta target
remains **OPEN**: reconstruction is not one of that target's parameter
cases and does not justify PARTIAL status for it.

Candidate IDEA-226: reconstruction retained; its proposed signed
weighted-Schur completion is deferred, with the missing obligation below.

## Depends on

The scalar finite Fejér formula, rederived here at coefficient level, and
the elementary checkerboard character sum. PD-T023/IDEA-074 and D1 are
local predecessors. No theorem on weight positivity or signed MZ
inequalities is assumed. PD-N053 is context, not a logically
necessary dependency on a negative statement.

## Proof

The finite Fejér formula gives K the coefficients

\[
 \kappa(r)=\frac{(m-|r|)_+-(n-|r|)_+}{m-n}.
\]

They equal one when `|r|<=n`, and vanish for `|r|>=m`. Expanding (1)
multiplies the `(r,k)` term by `(1+(-1)^(r+k))/2`. It therefore keeps
exactly the pairs of equal parity. The surviving frequencies in t,s are
the integers `a=(r+k)/2,b=(r-k)/2`, and conversely each integer (a,b)
corresponds to the unique pair `r=a+b,k=a-b`. Hence H is 2pi-periodic
in each original angle and has exact Fourier coefficient

\[
 \widehat H(a,b)=\kappa(a+b)\kappa(a-b).             \tag{3}
\]

For integers a,b, `max(|a+b|,|a-b|)=|a|+|b|`. Therefore (3) is
one on the diamond of radius n and zero outside the diamond of radius
`m-1`. This checks the plateau boundary, parity, and cutoff explicitly.

The normalized checkerboard character average is nonzero exactly for

\[
 \Lambda_m=(2m\mathbb Z\times2(m+1)\mathbb Z)
 \ \cup\ ((m,m+1)+2m\mathbb Z\times2(m+1)\mathbb Z),              \tag{4}
\]

and is then one. To see this, insert the checkerboard indicator
`(1+(-1)^(j+k))/2` in the full periodic rectangular sum and use the
geometric-series identity in each coordinate. Every nonzero vector in
the first set in (4) has l1 length at least 2m. Every vector in the
second set has coordinate magnitudes at least m and m+1, and hence l1
length at least `2m+1`. Thus every nonzero alias has l1 length >=2m.

Expand the right side of (2) in Fourier series. An input frequency a and
an output frequency b can couple only if `a-b in Lambda_m`. The support
bounds give

\[
 |a-b|_1\le |a|_1+|b|_1\le n+m-1\le2m-2<2m.
\]

Consequently a=b is the only possible coupling. Its multiplier is one
by (3). This proves (2), including n=0 and the m=1 edge case (where H=1
and q is constant).

Finally each algebraic product `T_a(x)T_b(y)` of total degree <=n
becomes `cos(at)cos(bs)`, whose Fourier frequencies lie in that diamond.
Every total-degree polynomial is a linear combination of these products.
Reflection of j modulo 2m and k modulo 2(m+1) preserves their parities,
so the even-checkerboard periodic samples are exactly the reflected
copies of the campaign's physical Padua samples. Equation (2) therefore
uses only those supplied values. ∎

## Checks and sources

Candidate and prewritten kill criteria: `ideas-d4.md`, IDEA-226.
The checks are analytic Fourier algebra, not a program run or a numerical
experiment. No independent audit or executed finite rerun is claimed.
The campaign literature record documents classical checkerboard Fourier
orthogonality (Dencker--Erb) and the known Fejér-filter ancestry. This
worker read that record, not those original PDFs. No priority claim.

## Scope and exact stopping point

The construction supplies the missing geometry for exact oversampled
reconstruction. Inverse-square scalar localization is in the diagonal
angles u,v. A weighted Schur estimate must respect that geometry and the
regularized product sine weight; transferring coordinatewise estimates
without checking the weight ratio is unjustified.

More decisively, even a successful positive sampled-energy estimate
does not identify the actual signed Padua quadratic form. The direct
positive-floor conversion is refuted by PD-N045. To resume the
signed lower route, prove a comparison on the admissible value subspace,
for example a bound of the negative sampled energy by a strict fraction
of a positive coercive sampled form, uniform in `n/m<=theta`. An upper
constant strictly below two is also separately required. Neither is
proved here, and no eta(theta) is asserted.

## History

2026-11-01, Codex `/root/d4_ratio`, requested gpt-6.1-sol xhigh, rules read
at supplied main `806cc7b4509fd93bae652f9545d32d95529f8281`. No Git mutation.
