# PD-T294 — a low-Rayleigh harmonic family escapes every fixed microscopic edge layer

Development alias: `PD-T?mz2d-frontier-codex-11`. Final ID assigned during audited preparation; [mapping](../preparation/final-id-map.json).

ID kind: PD-T.
Aliases: mesoscopic harmonic mass; endpoint escape of the PD-T018
witness; Padua marginal edge escape.
Split from: IDEA-385's supporting localization question.
Split into: none. This is not a split-off case of F1/F2's spectral targets.

## Statement

For every integer N>=3 let

\[
 M=\lfloor(N-1)/2\rfloor,\qquad
 p_N=\sum_{j=1}^M
 \frac{U_{N-1-2j}-(1-2j/N)U_{N-1}}{j}.                \tag{1}
\]

Fix any real K>0. For all N with `log N>=128` and `K/N<=pi/2`,
the mass fraction of p_N in the angular endpoint set

\[
 E_N(K)=\{x=\cos t:\min(t,\pi-t)\le K/N\}
\]

satisfies

\[
 \frac{\int_{E_N(K)}p_N(x)^2dx}{\int_{-1}^1p_N(x)^2dx}
 \le\frac{512\pi^2K^2}{(\log N)^3}\longrightarrow0.    \tag{2}
\]

Nevertheless this exact degree-N−1 witness has

\[
 0<\frac{C_N(p_N^2)}{\|p_N\|_2^2}
 \le\frac{128000}{(\log N)^2}\longrightarrow0.          \tag{3}
\]

Now put `P_m(x,y)=p_m(x)/sqrt(2)` for m>=3, and let

\[
 \mathcal E_m(K)=\{(\cos t,\cos s):
 \min(t,\pi-t,s,\pi-s)\le K/m\}
\]

be the union of all four angular K/m edge neighborhoods. For the
same range of m,

\[
 \frac{\int_{\mathcal E_m(K)}P_m^2\,dxdy}{\|P_m\|_2^2}
 \le\frac{512\pi^2K^2}{(\log m)^3}+\frac{K^2}{2m^2}
 \longrightarrow0,                                   \tag{4}
\]

while its signed Padua Rayleigh quotient is exactly the 1D quotient
in (3). In particular, vanishing Rayleigh quotients do not by themselves
force concentration in a fixed microscopic edge layer.

## Definitions

`U_r(cos t)=sin((r+1)t)/sin t`, and C_N denotes the positive Lebesgue
Clenshaw–Curtis rule of PD-T013. Padua Q_m and its total-degree space
use the frozen campaign definitions. Continuous mass means dx in
(2) and dxdy in (4), with the angular Jacobians retained.

The construction (1) is the existing exact PD-T018 witness. It is
not asserted to be an actual minimum eigenvector or to attain a sharp
asymptotic eigenvalue constant.

## Assumptions

Integer N,m>=3, real K>0 fixed independently of the mesh. The explicit
constants use the inherited large-N estimate `log N>=128`; the limiting
statements concern N tending to infinity, so no initial finite check is
needed. The neighborhoods must satisfy K/N<=pi/2 to keep their endpoint
pieces disjoint except on a null boundary.

## Status by part

Overall status: **PROVED** (analytic development; supplementary Astra
review found no gap; Claude audit-01 accepted).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| 1D fixed-width endpoint escape (2) | PROVED | Elementary endpoint bound plus PD-T018's norm lower bound |
| Exact Padua lift and full edge escape (4) | PROVED | Marginal isometry, product measure and union bound |

The quotient bound (3) is inherited from PD-T018, not a new endpoint
order theorem. Candidate disposition: retained supporting property.

## Depends on

PD-T018: this same witness has `||p_N||_2² >= (log N)^3/512` and
`C_N(p_N²)<=250 log N` when log N>=128. PD-T021: exact isometric
Padua marginal compression. PD-T013: positive CC weights, for the
strict positivity in (3). No 2D positivity or spectral asymptotic is
assumed.

[Claude audit-01](../audit-01.md) accepted the mathematics at its stated scope; [response-01](../response-01.md) addresses the editorial findings. Supplementary reconstruction is recorded in [independent-checks-math.md](../independent-checks-math.md).

## Checks

Rules/input `83cf6f1ee244f2e72057332a7ec04ee74db1f0de`.
The exact PD-T018 polynomial and its full norm proof were reread.
No mathematical computation, numerical integration or independent rerun
was executed by this worker. The proof needs none. Gate G3 data
reported separately by the parent are not used as proof evidence here.
A distinct gpt-6-astra high supplementary checker read this file and its
PD-T018/021 dependencies in full, finding no mathematical gap; exact
scope and final hashes belong in ../independent-checks-math.md.

## Sources

Local IDEA-066/072/215 and PD-T018/021, read in full. The complete
novelty gate and bounded search coverage are in ../ideas-f12.md.
No external source theorem or historical priority claim.

## Proof or evidence

The degree of (1) is at most N−1, its parity is N−1, and its endpoint
values are zero, as in PD-T018. For 0<t<=pi/2 write each numerator in
its angular form:

\[
 F_j(t)=\sin((N-2j)t)-(1-2j/N)\sin Nt.
\]

By the Lipschitz bound for sine and `|sin Nt|<=Nt`,

\[
 |F_j(t)|
 \le |\sin((N-2j)t)-\sin Nt|+(2j/N)|\sin Nt|
 \le2jt+2jt=4jt.
\]

Divide by j, sum over j and use `M<=N/2` to obtain

\[
 |p_N(\cos t)|
 \le\frac{4Mt}{\sin t}
 \le\pi N,\qquad 0<t\le\pi/2.                         \tag{5}
\]

The last inequality uses `sin t>=2t/pi`. At t=0 it holds by continuity.
By the parity of p_N the same squared bound holds near pi. Integrating
only the two endpoint layers, with `sin t<=t`, gives

\[
 \int_{E_N(K)}p_N^2dx
 =2\int_0^{K/N}p_N(\cos t)^2\sin t\,dt
 \le2\pi^2N^2\frac{K^2}{2N^2}=\pi^2K^2.              \tag{6}
\]

The norm lower bound in PD-T018 proves (2). Its discrete upper bound
and the same denominator bound prove (3), with strict positivity from
the positive CC weights and unisolvence.

For the Padua lift, integration in y shows
`||P_m||_2²=||p_m||_2²`. Its normalized x-edge mass is exactly the
left side of (2). Its normalized y-edge mass is

\[
 \frac12\int_{\{y=\cos s:\min(s,\pi-s)\le K/m\}}dy
 =1-\cos(K/m)\le\frac{K^2}{2m^2}.
\]

A union bound proves (4). Finally PD-T021 gives
`Q_m(P_m²)=C_m(p_m²)` exactly. Thus the low-quotient property and
vanishing microscopic edge mass coexist for these admitted Padua
polynomials. ∎

## Scope

This gives a rigorous distributed low-Rayleigh family. The corner
neighborhoods are subsets of the edge union, so their mass also tends
to zero. It does **not** prove that actual minimum or maximum
eigenvectors escape a fixed layer, that G3 fails, that a limiting
operator does not exist, or that the signed Padua minimum has any
particular order or sign. A different lower branch may localize.

The result cautions against inferring microscopic concentration from
the mere existence of endpoint Rayleigh decay. Mesoscopic or growing
K_N windows remain possible and require a separate statement.

## Open items

Claude audit-01 accepted. Relate an actual extremal-vector family to a
distributed or localized limiting operator with quantitative errors.
This profile theorem does not decide the 2D spectral targets; the
separate signed carrier theorems now refute the all-m upper threshold,
positivity, positive endpoint lower orders, and eta convergence. Sharp
growth constants and odd-m behavior remain unresolved.

## History

2026-11-05, Codex F1/F2 developer, requested gpt-6.1-sol xhigh; runtime
model metadata unexposed. The predecessor witness is retained unchanged;
only its stated mass profile is new in this local development. No Git.

2026-11-05: mechanical final-ID registration after accepted Claude audit-01 and response-01. The earlier audited source/receipt identities are historical; proof content changes only by ID substitution.
