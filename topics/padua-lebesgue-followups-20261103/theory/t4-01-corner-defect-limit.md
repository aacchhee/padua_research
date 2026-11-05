# PD-T269 — Parity-independent corner defect limit

Dated 2026-11-05 PR registration: Final ID: PD-T269. Preserved provisional alias: `PD-T?lebesgue-followups-codex-t4-01`. [Claude audit-01](../audit-01.md) accepts the mathematics; [response-01](../response-01.md) answers its minor findings. Earlier pending-audit wording below records the development stage and is superseded by this dated status. T2/T3 prospective-gate timing remains unwaived; physical cold-storage delivery remains pending. See [final map](../preparation/final-id-map.json). Mathematical text below is unchanged.

ID kind: PD-T.
Aliases: T4; A3 constant; diagonal-offset signed deformation.
Split from: PD-T098, existence and identification of κ.
Split into: the one-dimensional expansion is t4-02; the c-term consequence is t4-03.

## Statement

For the Padua corner value Λ_c(n) and same-mesh sum L_n of PD-T159,

\[
 \lim_{n\to\infty}(\Lambda_c(n)-L_n^2)=\kappa,
 \qquad
 \kappa={8\over\pi}\int_0^1 t^2\cot{\pi t\over2}
       \sum_{\substack{l\ge1\\l\ {\rm odd}}}{1\over l(l^2-t^2)}\,dt.       \tag{1}
\]

The limit is over all integers, hence the even and odd limits agree. More explicitly, for n≥32,

\[
 |\Lambda_c(n)-L_n^2-\kappa|
 \le 604 n^{-1/5}+{(\log n+2)^2+1\over n+1}.                         \tag{2}
\]

There is also a geometrically convergent coefficient series, with the coefficients defined below:

\[
 \kappa={8\over\pi^2}\sum_{k=0}^\infty {c_k\over k+1},\qquad
 \left|\kappa-{8\over\pi^2}\sum_{k=0}^K{c_k\over k+1}\right|
 \le {8\over3(K+2)4^{K+1}}.                                         \tag{3}
\]

## Definitions

Use n≥2, a_j=jπ/n, b_k=kπ/(n+1), endpoint weights ε_j=1/2 at j=0,n and 1 otherwise, η_k=1/2 at k=0,n+1 and 1 otherwise, and

\[
 f(a,b)={1+\cos b\over|\cos a-\cos b|},\quad
 L_n={2\over n}\sum_{r\le n,\ r\ {\rm odd}}d_r\csc{r\pi\over2n},
 \quad d_n=1/2,\quad d_r=1\ (r<n).
\]

The integrand in (1) has its continuous limiting values at 0 and 1. Define

\[
 a_0=1,\quad a_p=1-2\sum_{r=1}^p{\zeta(2r)\over4^r}\quad(p\ge1),
\]
\[
 b_0={7\over8}\zeta(3),\qquad
 b_q=(1-2^{-2q-3})\zeta(2q+3)
       -(1-2^{-2q-1})\zeta(2q+1)\quad(q\ge1),
 \quad c_k=\sum_{p+q=k}a_pb_q.
\]

## Assumptions

Exactly the Padua convention and exact identities of PD-T159. No argmax or asymptotic conjecture. Natural logarithms.

## Status by part

Overall status: **PROVED**, written analytic proof; supplementary independent reconstruction accepted; required Claude audit pending.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Limit, parity independence, integral (1), explicit rate (2) | PROVED | Analytic argument below |
| Geometric series and exact tail bound (3) | PROVED | Analytic coefficient bounds below |

The numerical enclosure is a separate verification record; no floating evaluation proves these statements.

## Depends on

PD-T159, specifically its exact positive corner sum, exact same-mesh square, and its pointwise bound (8). PD-T101 enters only through PD-T159. Elementary sine inequalities and the cotangent partial fraction derived below.

## Checks

The proof has no computational dependency. Enclosure code: `../code/t4_constant.py`; developer receipt: `../evidence/t4-constant.json`. Distinct Astra reconstruction and independent enclosure reruns are recorded in [independent-checks-analytic.md](../independent-checks-analytic.md).

## Sources

No external theorem is used without a local proof. Literature index read as recorded in `../gate-t4.md`; no historical novelty claim.

## Proof or evidence

### 1. Exact signed deformation

By PD-T159, with its actual endpoint weights,

\[
 \Delta_n={4\over n(n+1)}\sum_{j+k\ {\rm odd}\atop0\le j,k\le n}
 \varepsilon_j\eta_k\{f(a_j,b_k)-f(a_j,a_k)\},
 \qquad
 \Lambda_c-L_n^2=\Delta_n+{1-L_n^2\over n+1}.                      \tag{4}
\]

There is no diagonal on this board. Its k=n reference row is zero, so using η_n rather than its same-mesh half-weight makes no change to that reference. For every present pair, l=|j−k| is odd and PD-T159 gives

\[
 |f(a_j,b_k)-f(a_j,a_k)|\le{\pi^2n\over2l^2}.                    \tag{5}
\]

Put t=j/n and k=j+sl, s=±1. For each fixed l and 0<t<1,

\[
 {f(a_j,b_k)-f(a_j,a_k)\over n}\longrightarrow
 h_{s,l}(t)={\cot(\pi t/2)\over\pi}
       \left({1\over|sl-t|}-{1\over l}\right).                   \tag{6}
\]

Indeed b_k=a_j+π(sl−t)/(n+1), whereas a_k=a_j+πsl/n; expand the two sine factors of the cosine difference. For s=+1, |sl−t|=l−t, and for s=−1 it is l+t. Taking limits in (5) proves |h_{s,l}|≤π²/(2l²) on (0,1). Thus these functions extend boundedly to both endpoints. Pairing orientations gives

\[
 4(h_{+,l}+h_{-,l})={8\over\pi}\cot(\pi t/2)
              {t^2\over l(l^2-t^2)},                            \tag{7}
\]

which is positive. The majorant is summable in l. The quantitative argument next also proves all limit exchanges, including endpoint/parity independence.

### 2. Quantitative central-strip comparison

Let 0<δ≤1/2 and M≥1 be an integer, with n≥2(M+1)/δ. Retain odd l≤M and rows δ≤j/n≤1−δ. Then all k=j±l and j are strictly inside the grid, and all weights equal one. Set a=πt, u=b−a. For the two meshes |u|≤π(M+1)/n≤πδ/2. Write

\[
 f(a,a+u)={H(a,u)R(u)\over|u|},\quad
 H={1+\cos(a+u)\over\sin(a+u/2)},\quad
 R={|u|\over2\sin(|u|/2)}.
\]

Here sin(a+u/2)≥δ, H(a,0)=cot(a/2)≤1/δ, |∂_uH|≤2/δ², R≤2 and |R−1|≤u². The last two bounds follow from sin x≥x−x³/6 on |x|≤π/8 and R's evenness. Therefore

\[
 |f(a,a+u)-H(a,0)/|u||\le6/\delta^2.
\]

The difference between (n+1)/n and 1 in the deformed reciprocal contributes at most 1/(nδ²), since |sl−t|≥δ. Consequently the absolute difference between the left side of (6) and h_{s,l}(t) is ≤13/(nδ²), uniformly on the retained rows. Also |h_{s,l}|≤1/δ² there. The normalization 4n/(n+1), in place of 4 after row averaging, can therefore be included to give total central approximation error ≤112M/(nδ²).

On [δ,1−δ], differentiating (6), using |(cot(πt/2))'|≤π/(2δ²), gives |h'_{s,l}|≤2/δ³. A mesh-1/n Riemann sum restricted to this interval differs from its integral by at most (sup|h'|+2sup|h|)/n≤4/(nδ³). This estimate includes the two fractional endpoint cells; it does not require nδ to be an integer. Summing the at most 2M orientation/offset terms and multiplying by 4 gives ≤32M/(nδ³).

### 3. Discarded rows and offsets

There are at most 2δn+2 discarded row indices. From (5), at most two orientations at each offset, and Σ_{l odd}l⁻²=π²/8, their total finite-sum contribution is at most

\[
 \pi^4{\delta n+1\over n+1}\le100(\delta+1/n).
\]

The corresponding integrals over a set of length 2δ contribute at most π⁴δ≤100δ, by the limiting majorant. Missing pairs near j=0,n are covered by this same estimate. Hence no endpoint weight or parity term remains unaccounted for.

Using Σ_{l>M}l⁻²≤1/M, the finite offset tail in Δ_n is ≤4π²/M<40/M. The integral tail is bounded identically. Combining all terms yields the more flexible bound

\[
 |\Delta_n-\kappa|\le {80\over M}+200\delta+{100\over n}
                      +{144M\over n\delta^3}.                    \tag{8}
\]

For n≥32 choose x=n^{1/5}, δ=1/x, M=⌊x⌋. Then x≥2, M≥x/2 and n=x⁵≥2x(x+1)≥2(M+1)/δ. The right side is at most 604n⁻¹/⁵. Finally PD-T159's elementary L_n≤log n+2 and (4) give (2). This proves (1) over the full sequence of integers.

### 4. Geometric series after cancellation of the endpoint pole

The elementary cotangent partial fraction is

\[
 \cot{\pi t\over2}={2\over\pi t}
       -{4t\over\pi}\sum_{m\ge1}{1\over4m^2-t^2}.                 \tag{9}
\]

For completeness, expand cos(zx) in its Fourier cosine series on [0,π]. Direct integration gives coefficients a₀=2sin(πz)/(πz), a_m=2(−1)^m z sin(πz)/(π(z²−m²)). Their absolute summability permits evaluation at x=π; rearranging gives (9) with z=t/2. The identity extends by continuity at the removable values used below.

Since Σ_m(4m²−1)⁻¹=1/2 by telescoping,

\[
 {t^2\cot(\pi t/2)\over1-t^2}
 ={2t\over\pi}+{4t^3\over\pi}
       \sum_{m\ge1}{1\over(4m^2-1)(4m^2-t^2)}
 ={2t\over\pi}\sum_{p\ge0}a_pt^{2p}.                             \tag{10}
\]

This proves the formula for a_p, and 0<a_p≤4⁻ᵖ for p≥1; also a₀=1. The second factor

\[
 (1-t^2)\sum_{l\ {\rm odd}}{1\over l(l^2-t^2)}
       =\sum_{q\ge0}b_qt^{2q}                                  \tag{11}
\]

has the stated b_q. Its l=1 pole has canceled. We have b₀<10/9 and, for q≥1,

\[
 |b_q|\le\sum_{l\ge3}l^{-2q-1}
 \le 9^{-(q-1)}\left({1\over27}+\int_3^\infty x^{-3}dx\right)
 <9^{-q}.
\]

Thus |c_k|≤4⁻ᵏ(10/9+Σ_{q≥1}(4/9)^q)<2·4⁻ᵏ. Products and termwise integration are uniformly absolutely convergent on [0,1]. Substitution of (10)–(11) in (1) proves (3), because 8/π²<1 and

\[
 \sum_{k>K}{2\,4^{-k}\over k+1}
 \le{8\over3(K+2)4^{K+1}}.
\]

## Scope

Corner constant only. Rate (2) is deliberately weak; it does not establish the conjectured -1/N correction or O(log N/N²) rate.

## Open items

Required Claude audit; supplementary reconstruction and reruns are complete. Sharper finite-n asymptotics remain separate stretch targets. PD-T098's full expansion remains OPEN.

## History

2026-11-03, Codex gpt-6.1-sol xhigh, rules `3f5196cf3639407c25b021fa30f70cc1d3ae113a`. Derived after the recorded T4 gate. No historical fit was used as a proof input.
