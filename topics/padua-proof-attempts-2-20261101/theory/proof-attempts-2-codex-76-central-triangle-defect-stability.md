# PD-T?proof-attempts-2-codex-76 — Joint stability of the central triangle defect

Final ID: **PD-T191**. Provisional ID `PD-T?proof-attempts-2-codex-76` is retained as an alias. Registered after accepted Claude audit-01 and response-01; historical pending-audit notes below are superseded.

Canonical Split from (registration): PD-T099 (finite global or exact edge/central-scope split; full-square all-n statement remains OPEN).

Current audit note, 2026-11-01: Claude audit-01 accepted this record at its stated scope. Historical audit-pending statements below describe development checkpoints.

ID kind: PD-T.
Aliases: A4(a) phase-dependent defect; moving central grid; exact crease stability.
Split from: exact phase decomposition and the central-envelope comparison.
Split into: the combined central-envelope theorem is77.

## Statement

Use70/74's exact kernel and primitive S_n(s). For a complementary vertical-edge phase beta=q*pi/(n+1), epsilon^n(−1)^q=−1, put phi=beta+s/(n+1). Reflect the first mesh to a'_j with A_j=epsilon cos a_j and tau_j=epsilon^n(−1)^j. Define the two half kernels by the polynomial formula

`H_jk^±=[tau_j D_n(a'_j,phi±b_k)−1]/2`,

and their weighted triangle defect

\[
 \Delta_n(\beta,s)=\sum_{j+k\,\mathrm{even}}w_{jk}
 \{|H_{jk}^+|+|H_{jk}^-|-|H_{jk}^++H_{jk}^-|\}.             \tag{1}
\]

Then exactly, for every real s,

`lambda_n(epsilon,cos phi)=S_n(s)−Delta_n(beta,s)`, `Delta_n>=0`. (2)

For every sequence `(epsilon_n, beta_n, s_n)` with `epsilon_n in {−1,1}`, complementary phases `epsilon_n^n (−1)^q_n=−1`, `beta_n=q_n*pi/(n+1)->pi/2`, and real `s_n->0` (the edge sign may vary with n),

\[
 \Delta_n(\beta_n,s_n)\longrightarrow g,                    \tag{3}
\]

with exactly the constant g in72/73. All exact zeros, cusps and removable values are included; no separation assumption on a critical point is made.

## Assumptions and status

The given even-checkerboard Padua convention and exact real arithmetic. Overall status: **PROVED**, by the analytic proof below; required Claude audit PENDING. No computation or numerical limiting evidence is used.

## Depends on and independent contribution

70/74's polynomial kernel and phase algebra, and72's definition of g. The indirect A1 dependency retains **PD-T?proof-attempts-codex-01 (audit pending)** and70's dated acceptance/merge qualification.

The full joint-stability proof was independently supplied by `/root/a5_checker` in independent-checks-a4-central.md and reconstructed by the lead. It is written out here as a durable supporting theorem, not assumed from a claimed numerical coincidence. Supplementary independent reconstruction does not replace the required Claude audit.

## Proof

Equation(2) follows directly from70: its corrected averaged kernel is tau_j(H_jk^++H_jk^-). The elementary triangle-defect identity gives(1). Reflecting endpoint-weighted physical meshes and translating by the complementary q makes the sum of the two separate absolute half kernels precisely the periodic odd-board primitive S_n(s). This is74's exact normalization, and remains valid at all polynomial removable values.

Write u=a'_j,b=b_k and z_±=cos(phi±b). Away from a zero denominator, each half kernel equals

\[
 H_\pm=\frac{a(s)(1+z_\pm)+b(s)\sin(\phi\pm b)}{\cos u-z_\pm},
 \quad a(s)=\cos^2(s/2),\quad b(s)=\tfrac12\sin s.            \tag{4}
\]

Eventually |s|<=1/4 and phi in[5pi/12,7pi/12]. For0<b<pi the two denominator targets have separation z_−−z_+=2sin phi sin b>=sin b. At least one denominator thus has magnitude at least sin b/2. Each numerator has magnitude<3. For the pointwise triangle defect d in braces in(1),

\[
 0\le d\le2\min(|H_+|,|H_-|)\le12/\sin b.                 \tag{5}
\]

This holds even if the other half kernel is removable: the separated denominator is regular and bounds the minimum. At b=0 orpi the two original finite D_n terms coincide, so d=0 exactly.

### 1. Uniform endpoint tails

Fix0<delta<=pi/12. If0<b<=delta, both phi±b lie in[pi/3,2pi/3]. At the other endpoint pi−delta<=b<pi their cosines have the same bounds. Consequently1+z_±>=1/2, a(s)>=63/64, |b(s)|<=1/8, and both numerators in(4) are at least47/128>0. A coincident denominator with positive numerator cannot occur on the actual grid because the finite-polynomial identity(4), after clearing its denominator, would force that numerator to vanish. Therefore positive defect can occur only when cos u lies between z_+ and z_−.

The possible u interval has length at most2b near0, or2(pi−b) nearpi. Ignore parity for an upper bound; a fixed physical b row contains at most2n b/pi+2 eligible j indices near0. With w_jk<=2/[n(n+1)],(5) and sin b>=2b/pi, the first K=floor((n+1)delta/pi) rows contribute at most

\[
 \frac{24}{n(n+1)}\sum_{k=1}^K\left(n+\frac\pi{b_k}\right)
   =\frac{24K}{n+1}+\frac{24}n\sum_{k=1}^K\frac1k.
\]

The other end has the same estimate. In particular their combined tail is at most100[delta+(1+log(n+1))/n], uniformly in the stated beta,s neighborhood. The corresponding limiting integral tails are O(delta). This estimate retains exact endpoint rows and does not assume bulk signs.

### 2. Bounded bulk and moving pole curves

On delta<=b<=pi−delta, bound(5) is uniform. Remove angular tubes of width eta around both pole curves u=fold(phi+b),u=fold(phi−b), and around their limiting curves at phi=pi/2. Each is a finite union of angle line segments of slopes±1. Per b row the tubes meet O(n eta+1) j indices, so their total weighted contribution is O_delta(eta+1/n), uniformly in phi, even at removable kernel values.

Outside these tubes all denominators are bounded away from0. Indeed for u,v in[0,pi], |cos u−cos v|>=2|u−v|^2/pi^2. Formula(4) and its triangle defect therefore converge uniformly as phi->pi/2 and s->0. Absolute value is Lipschitz; no separate sign or zero-cardinal exception is needed. The limiting defect is

\[
 d_0(u,b)=\begin{cases}
 2\min\{(1-\sin b)/(\cos u+\sin b),
         (1+\sin b)/(\sin b-\cos u)\},&|\cos u|<\sin b,\\
 0,&\text{otherwise},
 \end{cases}                                                \tag{6}
\]

up to arbitrary values on the finitely many pole curves. It is bounded on the truncated strip by the same minimum estimate.

### 3. Checkerboard Riemann limit

The positive endpoint-weighted checkerboard sums converge to pi^(-2) times the angular integral of a continuous function: write the parity indicator as[1+(−1)^(j+k)]/2; the full tensor term is its ordinary trapezoidal Riemann sum, and the alternating term tends to0 by pairing adjacent first-coordinate indices. Continuous approximation away from the bounded pole tubes extends this to(6). It also makes the convergence uniform for the moving integrands just considered and for either parity after first-coordinate reflection.

Take n->infinity with delta,eta fixed, then eta->0, then delta->0. The uniform tail estimate proves

`Delta_n(beta_n,s_n) -> pi^(-2) integral_0^pi integral_0^pi d_0(u,b) du db`.

Using b->pi−b symmetry and t=pi/2−b on the first half gives exactly72's integral for g. This proves(3), including every removable or cusp event. ∎

## Scope and open items

This stability theorem alone gives no upper bound on S_n(s). It combines with the distinct global phase localization74 and local gain bound75 in the now complete result77. Root and the independent analytic workers fully inspected the durable proof and its underlying module with no blocking finding. It does not locate a global square maximizer, assert critical-point uniqueness, or identify the historical searched runner-up. Required Claude audit remains PENDING.

## History

2026-11-01, Codex gpt-6.1-sol xhigh, within the15:24–18:24UTC box. Primary derivation by the separate central-envelope worker; lead reconstruction preserves its uniform endpoint, pole-tube and parity limits. No numerical run was required or claimed.
