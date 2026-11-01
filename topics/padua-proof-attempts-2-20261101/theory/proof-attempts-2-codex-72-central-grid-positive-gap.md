# PD-T?proof-attempts-2-codex-72 — A positive limiting gap at central complementary edge points

ID kind: PD-T.
Aliases: A4(a) central-grid auxiliary sequence; positive cancellation integral.
Split from: complementary-grid identity71 and the point-value portion of A4(a).
Split into: the central envelope/nearby critical-branch comparison remains OPEN.

## Statement

For each n let m=n+1. Choose an interior complementary grid point as in71, with beta_n=q_n*pi/m->pi/2. Then

\[
 \Lambda_c(n)-\lambda_n(\epsilon_n,\cos\beta_n)\longrightarrow g,
                                                               \tag{1}
\]

where the following fixed explicit integral is finite and strictly positive:

\[
 g=\frac4{\pi^2}\int_0^{\pi/2}\int_t^{\pi-t}
 \min\left\{\frac{1+\cos t}{\cos t-\cos a},
             \frac{1-\cos t}{\cos a+\cos t}\right\}\,da\,dt,
 \qquad \frac1{45}<g\le2.                                  \tag{2}
\]

Integrand values at the domain's boundary are immaterial. This defines g without a fit or an unverified numerical limit.

A concrete all-n choice is: for odd n, q_n=m/2 and epsilon_n=(−1)^(q_n+1); for even n, q_n is the unique odd integer nearest m/2 and epsilon_n=1. Then beta_n is exactly the nonnode midpoint angle for odd n and is displaced from pi/2 by pi/(2m) for even n. Write C_n=lambda_n(epsilon_n,cos beta_n). The proved expansion is `C_n=Lambda_c(n)−g+o(1)`. No assertion C_n=R_search(n), or C_n=R_cen(n)+o(1), is included.

## Definitions and assumptions

All nodes, weights and complementary parity are those of71. The source R_search denotes its finite numerical searched runner-up. R_cen is the compact central-edge envelope defined in T-A4a.md. They are separate objects from C_n until a further theorem connects them. All limits in(1) hold for any sequence of the stated complementary points, not only the concrete choice.

## Status by part

Overall status: **PROVED** (written analytic limit and positive bounds; required Claude audit PENDING).

| Part | Status |
|---|---|
| All-parity complementary sequences beta_n->pi/2 have limit(2) | PROVED by uniform endpoint-tail control and parity-grid Riemann convergence |
| Explicit positive constant g and bounds1/45<g<=2 | PROVED analytically |
| Identification with searched runner-up or central maximizing branch | OPEN and excluded from this statement |

This is a point-sequence component of the requested work, not completion of the runner-up/envelope target by substitution.

## Depends on

71 and elementary trigonometric/Riemann integration estimates. Indirect literal dependency: **PD-T?proof-attempts-codex-01 (audit pending)**, with the dated acceptance/merge qualification in70. A2's fitted constant or conjectured A3 limit is not a premise.

## Checks

The odd-sequence limit and its positive integral were reconstructed independently in independent-checks-a4.md. The same independent agent also verified the all-parity endpoint and translation argument underlying71. No numerical approximation of g or exact regression has run at this initial writing. The proof is analytic; subsequent executed checks will be labelled separately and independently replayed.

## Sources

Registered A4(a), source05 and the measured central-edge competitor motivate this auxiliary sequence but supply no premise for the limit. The relaxed gate, including new MZ records and their different signed-norm scopes, is in T-A4a.md. No novelty or priority claim.

## Proof

### 1. Uniform control of the moving grid's endpoint tails

Use h_beta(A,b) from71. For beta,b in(0,pi), let z_±=cos(beta±b), so z_−−z_+=2sin beta sin b>0. When1+z_+>0, the two positive fractions in h are respectively decreasing and increasing as A runs from z_+ toz_−, and their minimum is maximized where they agree. Solving that equality gives the upper bound

\[
 \frac{2+z_++z_-}{z_--z_+}
   =\frac{1+\cos\beta\cos b}{\sin\beta\sin b}.
\]

On the degenerate line beta+b=pi, one has z_+=−1 and h=0 throughout the open band, so the same upper bound holds; it need not be attained there. For beta in[pi/3,2pi/3], the displayed bound is at most2/sin b. The angular set of a in[0,pi] with z_+<cos a<z_− has length

`2 min(beta,b,pi−beta,pi−b) <= 2 min(b,pi−b)`.

On one fixed k row the compatible first-coordinate indices have angular spacing2pi/n, even after reflecting the chosen endpoint. Thus if s=min(k,m−k)>=1, the band contains at most n*s/m+1 such indices. The endpoint weights are at most1. The sine chord bound gives sin(b_k)>=2s/m, so h<=m/s. After multiplying by the gap normalization4/(nm), this row contributes at most

\[
 \frac4m+\frac4{ns}.                                       \tag{3}
\]

The k=0,m bands are empty. For either end b<delta or pi−b<delta, sum(3) over s<=delta*m/pi. The combined end-tail contribution has limsup at most8delta/pi; the extra harmonic contribution is O(log m/n) and tends to0. Since beta_n->pi/2, the required beta neighborhood holds for all sufficiently large n. The exceptional2/(nm) in71 also tends to0.

### 2. Riemann convergence on each remaining compact strip

Fix delta>0. On delta<=b<=pi−delta, h_beta is uniformly bounded for beta nearpi/2. As beta->pi/2 it converges uniformly off arbitrarily thin neighborhoods of the limiting band's boundary curves. Those curves are finitely many straight angle segments after reflection of beta±b into[0,pi]; they have area zero, and a width-rho neighborhood meets only O(rho*n*m+n+m) mesh sites. On its complement the positive fractions, their minimum and their zero extension are uniformly continuous in all variables. Therefore the moving integrand has the same parity-grid Riemann limit as h_(pi/2).

For clarity, half-density is essential. A first-coordinate parity subsequence has mesh2pi/n; a second-coordinate row has meshpi/m. The area per compatible pair is2pi^2/(nm). Consequently

\[
 \frac4{nm}\sum_{j+k\,\mathrm{even}}\epsilon_j\eta_k
 h_{\beta_n}(A_j,b_k)
 \longrightarrow \frac2{\pi^2}
 \int_0^\pi\int_0^\pi h_{\pi/2}(\cos a,b)\,da\,db,           \tag{4}
\]

first with the fixed endpoint strips removed. The estimate(3) and the analogous integrable tail bound permit delta down to0, proving(4) on the whole rectangle. Boundary weights or a reflected parity do not change the density; their contribution on a compact strip is O(1/n+1/m).

At beta=pi/2, z_+=−sin b,z_−=sin b. Reflection b->pi−b leaves the integrand unchanged. On b in[0,pi/2] substitute t=pi/2−b, so c=cos t=sin b. The allowed a band becomes t<a<pi−t and h is the minimum in(2). This converts(4) exactly to the stated g. Apply71 and let its2/(nm) tend to0 to prove(1).

### 3. Finiteness and a positive explicit lower bound

For0<t<pi/2 set c=cos t and A=cos a in(2). The equality switch is A=−c^2. If A>=−c^2, the smaller fraction is(1−c)/(A+c)<=1/c. If A<=−c^2, the smaller fraction is(1+c)/(c−A)<=1/c. Thus the integrand is at most1/c. With u=pi/2−t, its a-domain has length2u and c=sin u>=2u/pi, so the inner integral is at mostpi. This proves g<=2 and supplies the integrable tail bound used above.

For a lower bound, restrict to t in[pi/4,pi/3], a in[pi/3,2pi/3]. Here1/2<=c<=1/sqrt2 and−1/2<=A<=1/2, with the band condition except on a measure-zero boundary. Both fractions are at least

`(1−1/sqrt2)/(1/2+1/sqrt2)=3sqrt2−4>1/5`.

The rectangle has area pi^2/36. Hence g> (4/pi^2)*(pi^2/36)*(1/5)=1/45. This proves all bounds without computing the integral numerically. ∎

## Scope

Only the explicitly specified complementary central point sequence. Odd-degree node midpoints instead have value1 and are not substituted. A complementary point may also fail to be stationary: at n=3 the nonnode midpoint value is8/3, while the historical searched edge competitor is approximately3.021223. Even asymptotic agreement with R_cen needs an additional proof; it is not inferred from the source fit.

## Open items

Prove or disprove `R_cen(n)−C_n=o(1)` or obtain rigorous two-sided envelope bounds; identify any selected stationary branch only under explicit hypotheses. Required Claude audit and supplementary independent finite checks remain separate. Full A4(b)/(c) are not attempted here.

## History

2026-11-01, Codex gpt-6.1-sol xhigh, within the15:24–18:24UTC A4 box. Positive cancellation and endpoint tail argument were independently reconstructed analytically; all numeric gap fits remain MEASURED source context.
