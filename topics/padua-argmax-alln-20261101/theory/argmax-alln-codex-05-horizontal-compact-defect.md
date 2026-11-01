# PD-T?argmax-alln-codex-05 — Exact horizontal decomposition and positive compact defect limit

ID kind: PD-T.
Aliases: P2 supporting theorem; horizontal corrected-mode defect.
Split from: PD-T099, supporting cancellation analysis for horizontal edges.
Split into: none. The compact horizontal envelope target remains OPEN.

## Statement

Use PD-T185's convention, \(m=n+1,\ N=nm\). On \(y=\epsilon=(-1)^\ell\),
\(\ell\in\{0,1\}\), choose \(\alpha=q\pi/n\) with \(q+m\ell\) odd and put
\(\theta=\alpha+s/n\). Define a horizontal primitive by

\[
 \begin{split}
 F^h_{jr}(s)&=\{(-1)^rD_n(j\pi/n+s/n,r\pi/m)+\cos s\}/2,\\
 S_n^h(s)&=N^{-1}\sum_{\substack{0\le j<2n,\ 0\le r<2m\\j+r\text{ odd}}}
                                      |F^h_{jr}(s)|.
 \end{split}                                                \tag{1}
\]

The exact nonnegative triangle defect below satisfies, for every real \(s\),

\[
 \lambda_n(\cos\theta,\epsilon)=S_n^h(s)-\Delta_n^h(\epsilon,\alpha,s),
 \qquad S_n^h(0)=\Lambda_c(n).                               \tag{2}
\]

For \(0<\alpha<\pi\), put \(z_\pm=\cos(\alpha\pm a)\) and

\[
 h_\alpha^h(B,a)=\begin{cases}
 (1+B)\min\{1/(B-z_+),1/(z_--B)\},&z_+<B<z_-,\\
 0,&\text{otherwise},
 \end{cases}
\]
\[
 g_h(\alpha)=\frac2{\pi^2}\int_0^\pi\int_0^\pi
                        h_\alpha^h(\cos b,a)\,db\,da.       \tag{3}
\]

Boundary values are immaterial. The integral is finite and continuous.
For every fixed compact \(K\subset(0,\pi)\) and every \(\rho_n\ge0\)
tending to zero,

\[
 \sup_{\substack{\epsilon=\pm1,\ \alpha\in K\text{ complementary}\\|s|\le\rho_n}}
 |\Delta_n^h(\epsilon,\alpha,s)-g_h(\alpha)|\longrightarrow0. \tag{4}
\]

For \(0<\delta<\pi/2\),

\[
 \inf_{\alpha\in[\delta,\pi-\delta]}g_h(\alpha)
 \ge\frac{\delta^2[1-\cos(\delta/2)]}{16\pi^2}>0.             \tag{5}
\]

No upper bound for \(S_n^h(s)-\Lambda_c(n)\) is asserted. Thus this theorem
does not by itself prove P2's compact envelope inequality.

## Definitions and assumptions

For physical node indices \(j+k\) even set \(a_j=j\pi/n,\ b_k=k\pi/m\),
\(B_k=\epsilon\cos b_k\), and let \(\cos b'_k=B_k,\ b'_k\in[0,\pi]\).
Put \(\kappa_k=(-1)^{k+m\ell}\) and define finite polynomial halves

\[
 H^\pm_{jk}=\{\kappa_kD_n(\theta\pm a_j,b'_k)+\cos s\}/2,\qquad
 \Delta_n^h=\sum_{j+k\text{ even}}w_{jk}
 (|H^+|+|H^-|-|H^++H^-|).                                  \tag{6}
\]

Weights and all collision values are PD-T185's. Arithmetic is exact real
arithmetic; all limits include both parities.

## Status by part

Overall status: **PROVED**, for the supporting theorem (1)–(5), by the
analytic proof below. Independent mathematical audit is pending.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Exact horizontal decomposition and compact positive defect limit | PROVED | Correction algebra and uniform tail argument |
| P2 compact horizontal envelope bound | OPEN, excluded | Separate horizontal phase localization and local primitive-gain estimate needed |

## Depends on

PD-T185 for the horizontal cardinal kernel and divided difference;
PD-T189's zero-phase primitive normalization. The equicontinuous
parity-grid argument in [04](argmax-alln-codex-04-vertical-compact-defect.md)
applies after establishing the different horizontal tails below.
PD-T190 is not imported by swapping the two meshes.

## Checks and sources

Codex, gpt-6.1-sol xhigh, 2026-11-01, source pin
328be35e55143013047ec03a70e9906e82b95353. No computation is a premise.
No numerical evaluation of \(g_h\), and no claim \(g_h(\pi/2)=1\), is made.
Gate and dispositions: [P1-P2-edges.md](../attempts/P1-P2-edges.md).

## Proof

### Corrected-mode algebra and normalization

Write \(v=\theta\pm a_j\), \(B=B_k\), \(P_n=T_{n+1}+T_n\). Then
\(P_n(B)=\kappa_k(1+B)\). Complementary and physical parity give
\((-1)^{q\pm j}=-\kappa_k\), hence

\[
 \cos(nv)=-\kappa_k\cos s,\qquad
 P_n(\cos v)=-\kappa_k\{\cos s(1+\cos v)-\sin s\sin v\}.
\]

Insert these into the divided difference. At regular denominators,

\[
 H^\pm_{jk}=
 \frac{A(s)(1+B)-C(s)\sin(\theta\pm a_j)}
      {B-\cos(\theta\pm a_j)},\quad
 A(s)=\cos^2(s/2),\quad C(s)=\tfrac12\sin s.                 \tag{7}
\]

In particular its fixed numerator is \(1+B\); the vertical numerator has
the shifted cosine instead. At zero phase a regular horizontal half is
\(1+(1+z)/(B-z)\), so the defects are distinct.

PD-T185's corrected horizontal cardinal kernel is
\(\{D_n(v_+,b'_k)+D_n(v_-,b'_k)\}/2-\cos(n\theta)(-1)^j\).
Its correction equals \(-\kappa_k\cos s\). Multiplying the kernel by
\(\kappa_k\) therefore gives \(H^++H^-\).
The triangle identity now proves (2) with the separate-half sum as
primitive. To identify that sum, reflect the physical first mesh into
its complete periodic mesh and translate its index by \(q\).
Reflect the second mesh about the chosen endpoint; its parity changes
by \(m\ell\). Since \(q+m\ell\) is odd, the resulting board is odd.
Endpoint half weights turn into uniform periodic counting. The result
is exactly (1), with normalization \(1/N\).
At \(s=0\), \((-1)^r=-(-1)^j\) on the odd board, so \(F^h_{jr}(0)\) is
the negative of PD-T189's vertical half kernel. This proves
\(S_n^h(0)=\Lambda_c(n)\), retaining every polynomial collision value.

### Endpoint tails with possible opposite numerator signs

Fix \(\alpha\in[\delta,\pi-\delta]\), \(|s|\to0\). Eventually
\(\sin\theta\ge\sin(\delta/2)>0\). The targets in (7) differ by
\(2\sin\theta\sin a\); one denominator is therefore separated by at least
\(\sin\theta\sin a\). Numerators are bounded, hence

\[
 d^h\le C_\delta/\sin a,\qquad 0<a<\pi.                    \tag{8}
\]

This uses the regular separated half even if the other is removable.
At \(a=0,\pi\) the finite halves coincide, giving zero defect.

Let \(N_\pm\) be (7)'s numerators. Their difference is

\[
 N_+-N_-=-\sin s\cos\theta\sin a,\quad
 |N_+-N_-|\le |s|\sin a.                                   \tag{9}
\]

Outside the closed band \(z_+\le B\le z_-\), both denominators are
regular and have the same sign. A positive defect requires opposite
numerator signs; both magnitudes are then at most the bound in (9).
Using the separated denominator proves

\[
 d^h\le C_\delta|s|\quad\text{outside that band}.             \tag{10}
\]

Inside the closed band, the possible \(b\) interval has length at most
\(2\min(a,\pi-a)\), by folding \(\theta\pm a\). It contains at most
\(C(m\min(a,\pi-a)+1)\) mesh indices. Combine this count, (8), the
positive weights and the sine chord bound on \(a_j\).
For the two tails \(a\le\eta\) or \(\pi-a\le\eta\), their sum is at most

\[
 C_\delta\{\eta+(1+\log n)/m+|s|\}.                         \tag{11}
\]

Polynomial collisions are inside the closed band and counted there.
The integral tail bound at \(s=0\) is \(C_\delta\eta\).

### Bulk convergence and a positive rectangle

For \(\eta\le a\le\pi-\eta\), (8) is uniform. Remove width-\(r_0\) tubes
around \(b=\operatorname{fold}(\theta\pm a)\) and the corresponding
zero-phase curves. Their mass is \(O(r_0+1/n+1/m)\).
Off them, (7) converges uniformly as \(s\to0\) to
\((1+\cos b)/(\cos b-\cos(\alpha\pm a))\).
Its defect is exactly \(2h_\alpha^h(\cos b,a)\). The bounded,
equicontinuous parity-grid argument in 04 applies with density
\(\pi^{-2}\). Send \(n\to\infty\), \(r_0\downarrow0\), then
\(\eta\downarrow0\) using (11). All estimates are compact-uniform.
This proves (4), finiteness, and, by applying the same tube argument to
nearby integral parameters, continuity.

Finally restrict to \(\delta/4\le a\le\delta/2\) and
\(|b-\alpha|\le\delta/8\). This area is \(\delta^2/16\), lies strictly
inside the band, and has \(1+\cos b\ge1-\cos(\delta/2)\).
Each positive denominator is at most 2, so the defect is at least
\(1-\cos(\delta/2)\). This proves (5). ∎

## Scope and open items

P2 still needs its own global phase estimate to localize maximizing
phases, and a local bound \(S_n^h(s_n)\le\Lambda_c+o(1)\).
Merely exchanging \(n,n+1\) in PD-T189–190 is not a proof because the
corrected mode and numerator change. Center minimality, the central
horizontal constant, effectivity and the all-square theorem remain OPEN.
Required Claude audit is pending.

## History

2026-11-01, Codex gpt-6.1-sol xhigh. The P2 envelope target is retained
OPEN and is not silently narrowed to this supporting claim. Polynomial
correction algebra preceded the limiting quotient. Development followed
the parent's tests-done signal.
