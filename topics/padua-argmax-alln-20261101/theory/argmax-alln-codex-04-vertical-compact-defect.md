# PD-T?argmax-alln-codex-04 — Positive compact vertical-edge gap

ID kind: PD-T.
Aliases: P1; macroscopic vertical triangle defect; compact-uniform extension of PD-T191.
Split from: PD-T099, the restriction to vertical edges outside fixed corner neighborhoods.
Split into: none. The all-square target PD-T099 remains OPEN.

## Statement

Let \(m=n+1\), use the even-checkerboard Padua convention of PD-T185,
and let \(\Lambda_c(n)\) be its nonnode corner value. For \(0<\beta<\pi\), put

\[
 z_\pm=\cos(\beta\pm b),\qquad
 h_\beta(A,b)=\begin{cases}
 \min\{(1+z_+)/(A-z_+),(1+z_-)/(z_--A)\},&z_+<A<z_-,\\
 0,&\text{otherwise},
 \end{cases}
\]

with boundary values irrelevant to integration, and define

\[
 g_v(\beta)=\frac2{\pi^2}\int_0^\pi\int_0^\pi
                  h_\beta(\cos u,b)\,du\,db.                 \tag{1}
\]

This is finite, continuous and positive on \((0,\pi)\). For every
\(0<\delta<\pi/2\),

\[
 \min_{\beta\in[\delta,\pi-\delta]}g_v(\beta)
 \ge c_\delta:=\frac{\delta^2[1-\cos(\delta/2)]}{16\pi^2}>0.  \tag{2}
\]

For complementary phases \(\beta=q\pi/m\), \(\epsilon^n(-1)^q=-1\),
let \(\Delta_n(\epsilon,\beta,s)\) be precisely PD-T191's polynomial
half-kernel triangle defect. For every fixed compact \(K\subset(0,\pi)\)
and every sequence \(\rho_n\ge0\) tending to zero,

\[
 \sup_{\substack{\epsilon=\pm1,\ \beta\in K\text{ complementary}\\
                         |s|\le\rho_n}}
 |\Delta_n(\epsilon,\beta,s)-g_v(\beta)|\longrightarrow0.     \tag{3}
\]

An empty supremum is omitted. In particular,

\[
 \max_{\substack{\epsilon=\pm1\\\delta\le t\le\pi-\delta}}
 \lambda_n(\epsilon,\cos t)
 =\Lambda_c(n)-\min_{\beta\in[\delta,\pi-\delta]}g_v(\beta)+o(1)
 \le\Lambda_c(n)-c_\delta+o(1).                             \tag{4}
\]

The errors are uniform on each fixed compact interval; no effective rate
is claimed. Formula (1) gives \(g_v(\pi/2)=g\) of PD-T187–188.
Whether the global minimum occurs at \(\pi/2\) remains OPEN.

## Definitions and assumptions

Nodes have angles \(a_j=j\pi/n,\ b_k=k\pi/m\), \(j+k\) even, with
\(w_{jk}=2e_jf_k/(nm)\) and half endpoint factors. The kernel \(D_n\) is
PD-T185's finite polynomial divided difference. Reflecting the first mesh
about \(\epsilon\) gives \(u_j\in[0,\pi]\) and
\(\tau_j=\epsilon^n(-1)^j\). The half kernels are

\[
 H^\pm_{jk}=\{\tau_jD_n(u_j,\phi\pm b_k)-1\}/2,\quad
 \phi=\beta+s/m,
\]

and \(\Delta_n=\sum w_{jk}(|H^+|+|H^-|-|H^++H^-|)\).
Arithmetic is exact real arithmetic; the limit includes both parities.

## Status by part

Overall status: **PROVED**, for (1)–(4), by the written analytic proof;
independent mathematical audit is pending.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Compact moving-phase defect limit, positive integral and lower bound | PROVED | Uniform tails and pole tubes below |
| Compact vertical-edge envelope (4) | PROVED | PD-T189–190 applied to the same maximizing sequence |
| Center minimizes the gap on the whole edge | OPEN, excluded | No comparison with \(g_v(\pi/2)\) is asserted |

## Depends on

PD-T185 for the all-edge kernel; PD-T189–190 for the exact primitive
\(S_n(s)\), its global phase bound and local gain; PD-T191 for the exact
decomposition \(\lambda_n=S_n-\Delta_n\). The convergence extension is
proved below. PD-T156/159 supply the corner growth used in the phase
argument.

## Checks and sources

Codex, gpt-6.1-sol xhigh, 2026-11-01, source pin
328be35e55143013047ec03a70e9906e82b95353. No numerical run is a premise.
No external source or priority claim is added. Gate and dispositions:
[P1-P2-edges.md](../attempts/P1-P2-edges.md).
T1 profile comparisons remain separate MEASURED evidence.

## Proof

Write \(a(s)=\cos^2(s/2)\), \(b(s)=\sin(s)/2\). PD-T189's exact algebra
gives at regular denominators

\[
 H_\pm=\frac{a(s)(1+\cos(\phi\pm b))+b(s)\sin(\phi\pm b)}
                 {\cos u-\cos(\phi\pm b)}.                 \tag{5}
\]

At a collision the polynomial kernel remains the definition. Fix a compact
interval \([\delta,\pi-\delta]\) containing the parameters. Eventually
\(\phi\in[\delta/2,\pi-\delta/2]\), \(|s|\le1/4\). The targets differ by
\(2\sin\phi\sin b\), so at least one denominator has magnitude at least
\(\sin\phi\sin b\). Both numerators are bounded by 3. Consequently the
pointwise defect obeys

\[
 0\le d\le2\min(|H_+|,|H_-|)\le C_\delta/\sin b.             \tag{6}
\]

The separated half is regular even if the other one collides.
At \(b=0,\pi\) the finite halves coincide and \(d=0\).

### Uniform endpoint tails

Take \(0<\eta<\delta/4\). If \(b\le\eta\), or \(\pi-b\le\eta\),
both \(1+\cos(\phi\pm b)\) have a positive lower bound depending only on
\(\delta\). For sufficiently small \(|s|\), both numerators in (5) are
therefore positive. A collision on this actual grid is impossible:
clearing the denominator would equate zero to a positive numerator.
Positive defect occurs only between the targets. Its interval in \(u\)
has length at most \(2r\), \(r=\min(b,\pi-b)\); folding angles into
\([0,\pi]\) proves this bound also near \(\pi\).

One row contains at most \(C(nr+1)\) first indices. Combining this count,
\(w_{jk}\le2/(nm)\), (6), and
\(\sin b_k\ge2\min(k,m-k)/m\), the two endpoint tails total at most

\[
 C_\delta\{\eta+(1+\log m)/n\}.                             \tag{7}
\]

The limiting integral tails are bounded by \(C_\delta\eta\). These bounds
are uniform in the complementary phase and edge.

### Bulk and moving poles

On \(\eta\le b\le\pi-\eta\), (6) is uniform. Remove tubes of angle width
\(r_0>0\) around \(u=\operatorname{fold}(\phi\pm b)\) and the corresponding
curves with \(\phi=\beta\). Each is a finite union of line segments of
slopes \(1,-1\). Their combined weighted mesh mass is
\(O(r_0+1/n+1/m)\), and their area is \(O(r_0)\). The bounded defect
therefore gives the same contribution bounds. Off the tubes denominators
are uniformly separated from zero: for \(u,v\in[0,\pi]\),
\(|\cos u-\cos v|\ge2|u-v|^2/\pi^2\).
Thus (5) converges uniformly as \(s\to0\), uniformly in compact \(\beta\).
The limit defect is

\[
 d_\beta(u,b)=2h_\beta(\cos u,b).                            \tag{8}
\]

The parity Riemann normalization is
\(\sum w_{jk}F(u_j,b_k)\to\pi^{-2}\int F\).
Indeed split parity into its constant and alternating terms; the full
tensor trapezoidal sum converges, and adjacent first-index pairing kills
the alternating term for an equicontinuous family. Away from the tubes
the rational expressions have common derivative bounds on the compact
parameter set. A bounded Lipschitz extension across the tubes changes
sums and integrals by only the tube-mass bounds just given. This proves
uniform Riemann convergence for this moving family, also after first-mesh
reflection and either parity.

Take \(n\to\infty\), then \(r_0\downarrow0\), then \(\eta\downarrow0\),
using (7). This proves (3) with its uniform quantifiers. The same tube
and tail argument for nearby integral parameters proves continuity of
(1); (7) proves finiteness. At \(\beta=\pi/2\), PD-T187's change of
variables gives its constant \(g\).

### Positive rectangle and envelope assembly

For \(\beta\in[\delta,\pi-\delta]\), restrict to
\(\delta/4\le b\le\delta/2,\ |u-\beta|\le\delta/8\).
There is no folding, and \(u\) lies between \(\beta-b,\beta+b\).
Both numerators in (1)'s minimum are at least \(1-\cos(\delta/2)\);
each positive denominator is at most 2. Thus
\(d_\beta\ge1-\cos(\delta/2)\) on area \(\delta^2/16\), proving (2).

Let \(I=[\delta,\pi-\delta]\), \(\delta<\pi/2\), and
\(g_*=\min_I g_v\). Approximate a minimizing point from within \(I\) by
complementary ordinates on \(x=1\), whose odd \(q\) have spacing \(2\pi/m\).
The exact zero-phase primitive and (3) give the lower envelope bound
\(\Lambda_c-g_*+o(1)\), also for a boundary minimizer.

Choose any maximizing point and its nearest complementary ordinate on
the same edge, \(t_n=\beta_n+s_n/m,\ |s_n|\le\pi\).
Eventually \(\beta_n\in[\delta/2,\pi-\delta/2]\). By PD-T189 and the exact
nonnegative-defect decomposition,

\[
 \sin^2(s_n/2)\Lambda_c(n)\le C\log(n+1)+g_*+o(1).
\]

The lower bound \(\Lambda_c\ge(4/\pi^2)\log^2n-54\) forces \(s_n\to0\).
PD-T190 gives \(S_n(s_n)\le\Lambda_c+o(1)\). At these same moving
parameters (3) gives \(\Delta_n=g_v(\beta_n)+o(1)\).
Continuity and \(\operatorname{dist}(\beta_n,I)\le\pi/m\) imply
\(g_v(\beta_n)\ge g_*-o(1)\). The matching upper bound follows, proving
(4). No stationarity or differentiability of the maximizer was used. ∎

## Scope and open items

P1 closes on every fixed compact strip, with a non-effective margin.
There is no bound uniform as \(\delta\downarrow0\), center-minimality
theorem, effective threshold, or P3–P6 conclusion. Claude audit pending.

## History

2026-11-01, Codex gpt-6.1-sol xhigh. Preparation preceded the parent's
tests-done authorization; mathematical development followed it.
The central PD-T191 statement is unchanged in its own record.
