# PD-T230 (PD-T?argmax-alln-gated-codex-16) — Compact horizontal-edge envelope

Final registration: **PD-T230**, 2026-11-03. The provisional identifier in the title remains an alias; mathematical statement and historical evidence are unchanged.

ID kind: PD-T.
Aliases: direction3 round1 horizontal P2 envelope; horizontal primitive
equals first-phase two-angle primitive; compact horizontal maximum gap.
Split from: the compact horizontal-envelope obligation retained OPEN in
PD-T?argmax-alln-codex-05 and PD-T099. That earlier supporting theorem is
unchanged; the all-square all-degree target remains OPEN.
Split into: none. Center minimality and effective thresholds remain separate.

## Statement

Let m=n+1 and use the even-checkerboard Padua convention of PD-T101/185.
Let I=[A,B] be any fixed nondegenerate closed interval with
0<A<B<pi. Let g_h be exactly the finite, continuous and positive
horizontal defect integral of prior theorem argmax-alln-codex-05:

\[
 g_h(t)=\frac2{\pi^2}\int_0^\pi\int_0^\pi
           h_t^h(\cos b,a)\,db\,da,
\]

where, with z_+-=cos(t+-a),

\[
 h_t^h(B,a)=
 \begin{cases}
 (1+B)\min\{1/(B-z_+),1/(z_--B)\},&z_+<B<z_-,\\
 0,&\text{otherwise}.
 \end{cases}
\]

Then, uniformly over epsilon in {+1,-1},

\[
 \max_{\theta\in I}\lambda_n(\cos\theta,\epsilon)
            =\Lambda_c(n)-\min_{t\in I}g_h(t)+o_I(1).    \tag{1}
\]

The same equality holds when the maximum also ranges over epsilon.
The limit includes both parities of n. In particular, if
I subset [delta,pi-delta], 0<delta<pi/2, then

\[
 \max_{\epsilon=\pm1,\theta\in I}\lambda_n(\cos\theta,\epsilon)
 \le\Lambda_c(n)
       -\frac{\delta^2[1-\cos(\delta/2)]}{16\pi^2}+o_I(1).
                                                               \tag{2}
\]

No value of g_h(pi/2), center-minimality assertion, effective remainder,
numerical degree threshold, endpoint-neighborhood comparison or all-degree
corner equality is asserted.

## Definitions and assumptions

Exact real arithmetic, the finite polynomial D_n and corrected x mode
of PD-T185. Use the periodic odd board Gamma^- with 0<=j<2n,
0<=r<2m,j+r odd, and the two-phase primitive of gated-codex-02/03,

\[
 F_{jr}(\alpha,\beta)=\frac{(-1)^j}{2}
       \{D_n(j\pi/n+\alpha/n,r\pi/m+\beta/m)
                                -\cos(j\pi+\alpha)\},
\quad S_n(\alpha,\beta)=\frac1{nm}\sum_{\Gamma^-}|F_{jr}|.
\]

On the horizontal edge epsilon=(-1)^ell, complementary centers are
xi=q*pi/n with q+m*ell odd. With theta=xi+s/n, prior theorem
argmax-alln-codex-05 defines

\[
 F^h_{jr}(s)=\{(-1)^rD_n(j\pi/n+s/n,r\pi/m)+\cos s\}/2,
\quad S_n^h(s)=\frac1{nm}\sum_{\Gamma^-}|F^h_{jr}(s)|,
\]

and its exact nonnegative horizontal triangle defect Delta_n^h satisfies
lambda_n(cos theta,epsilon)=S_n^h(s)-Delta_n^h(epsilon,xi,s).
Every kernel value, including a collision, is defined by the original
finite polynomial. The compact defect convergence and positivity used
below are exactly that theorem's previously proved statements.

## Status by part

Overall status: **PROVED**, by the analytic argument below; distinct
Astra xhigh independent mathematical reconstruction accepted at the stated
scope. Required Claude audit remains pending at initial publication. No numerical calculation
is a premise.

| Mathematical part | Status | Evidence / limit |
|---|---|---|
| Compact envelope (1) and positive gap (2) | PROVED | Exact primitive identity, phase localization, same-phase local gain and uniform horizontal defect |

Candidate disposition: retained completion of the existing IDEA-305 /
original Claude-02 horizontal phase/gain/defect route. No novelty claim.

## Depends on

- Prior argmax-alln-codex-05: exact horizontal decomposition, compact-uniform
  defect limit, continuity and positive lower bound for g_h.
- Gated-codex-02: global two-phase leading bound on the phase diamond.
- Gated-codex-03: vanishing local two-phase primitive excess.
- PD-T157 (proof-attempts-2-codex-02-corner-explicit-leading):
  Lambda_c(n)>=(4/pi^2)log^2 n-54.
- PD-T185 and PD-T101: finite polynomial kernel, corrected mode and weights.

There is no interchange of n and n+1 in a one-phase theorem, no imported
horizontal symmetry, and no dependence on unread one-dimensional sources.

## Proof

### Exact identification of the primitive

For every real s and every odd-board pair, cos(j*pi+s)=(-1)^j cos s.
Thus the actual polynomial half kernel is

\[
 F_{jr}(s,0)=\{(-1)^jD_n(j\pi/n+s/n,r\pi/m)-\cos s\}/2.
\]

Since (-1)^r=-(-1)^j on Gamma^-, comparison with the defining horizontal
half gives the termwise exact identity

\[
                      F^h_{jr}(s)=-F_{jr}(s,0),\qquad
                      S_n^h(s)=S_n(s,0).                 \tag{3}
\]

This uses the corrected cosine term itself, not a quotient formula.
Consequently it is valid at every polynomial collision, for both parities
and all real s. In particular S_n^h(0)=Lambda_c(n).

The two-phase global bound applied to (s,0) gives, for |s|<=pi,

\[
 S_n^h(s)\le\cos^2(s/2)\Lambda_c(n)+C\log(n+1).         \tag{4}
\]

The local theorem gives S_n^h(s_n)<=Lambda_c(n)+o(1) along every
s_n->0, uniformly along such sequences. It also gives a fixed local
phase window on which the supremum excess is O(log^-2 n). The same
primitive is used in the exact horizontal decomposition throughout.

### Lower envelope, including interval-boundary minimizers

Continuity of g_h implies g_*:=min_I g_h is attained at some t_* in I.
For each horizontal edge epsilon=(-1)^ell, its complementary first
indices q have a fixed parity q+m*ell odd and spacing 2pi/n in angle.
For all sufficiently large n choose a complementary xi_n in I with
|xi_n-t_*|<=2pi/n. Such a choice exists even if t_*=A or B: choose
the first grid point inside the interval from that endpoint. Since
I is nondegenerate and away from 0,pi, the chosen indices are physical
interior indices eventually.

At s=0 the exact decomposition and compact-uniform defect limit give

lambda_n(cos xi_n,epsilon)
 =Lambda_c(n)-g_h(xi_n)+o(1)=Lambda_c(n)-g_*+o(1).

The estimate is uniform over the two choices of epsilon, so it supplies
the lower bound in (1) on each edge, for both degree parities. No point
outside I was used for this lower comparison.

### Arbitrary maximizing phases and upper envelope

For every n choose an edge epsilon_n and a maximizer theta_n in I on
that edge. The edge may vary with n. Select its nearest complementary
center xi_n=q_n*pi/n and write theta_n=xi_n+s_n/n with |s_n|<=pi.
For sufficiently large n the center is a physical interior index. It may
lie just outside I at an interval boundary, but dist(xi_n,I)<=pi/n;
all such centers lie in one fixed compact K subset (0,pi).

The just proved lower comparison, the exact nonnegative-defect identity
and (4) imply

\[
 \sin^2(s_n/2)\Lambda_c(n)
                       \le C\log(n+1)+g_*+o(1).
\]

The quadratic-logarithmic corner lower bound forces s_n->0. For example
|s_n|<=pi and the sine chord bound give |s_n|=O(log^-1/2 n).
Apply the local gain estimate from (3) at exactly these maximizing
phases: S_n^h(s_n)<=Lambda_c(n)+o(1). The previous horizontal theorem's
compact-uniform limit, on the same centers and phases, gives

Delta_n^h(epsilon_n,xi_n,s_n)=g_h(xi_n)+o(1).

Uniform continuity of g_h on K, with dist(xi_n,I)<=pi/n, gives
g_h(xi_n)>=g_*-o(1), even when a nearest center is outside I. Therefore

lambda_n(cos theta_n,epsilon_n)
 <=Lambda_c(n)-g_*+o(1).

This proves the matching upper bound uniformly over both edges and
degree parities. It holds for any maximizing sequence; no differentiability,
stationarity or unique maximizing branch is assumed. Combining lower
and upper comparisons proves (1). The prior positive lower bound for
g_h on [delta,pi-delta] proves (2).

## Checks, scope and history

Developed in authorized direction3 round1, 2026-11-02, Codex assigned
gpt-6.1-sol xhigh; runtime metadata not independently exposed. Rules
read at administrative head `3aebb299a4154dac822974b7245a9d243f21374e`;
unchanged rule source reference `aa1883f2fd9a837bb931ce804cb4b210c7475886`.
Scientific campaign base `7d308b10d946b607ae0690454f6c0103690775a4`.
The refreshed candidate/obstruction gate and exact source-reading scope
are in gated/d3/r01-edge-analysis.md. No external theorem transfer,
numerical horizontal scan, Git action, shared registry change or
future-round work is a premise.

This completes the previously missing horizontal primitive estimates
and compact envelope at the stated non-effective scope. It does not
change the prior supporting theorem, prove g_h(pi/2)=1, order whole edge
cells, handle endpoint corner neighborhoods, or establish PD-T099.
The completed supplementary reconstruction is recorded in
[gated/checks/d3-r01.md](../gated/checks/d3-r01.md); required Claude audit
remains pending at initial publication.


### Current review correction — 2026-11-03 (R1)

The pending-Claude labels above describe the initial publication boundary.
Claude [audit-01](../audit-01.md) accepted this record at its written
mathematical or MEASURED scope; [response-review-01](../response-review-01.md)
accepted the record/provenance response. Those completed reviews are the
current state. This dated correction changes no statement, epistemic
status, proof, numerical value, source pin or frozen receipt. All remaining
mathematical open items retain their stated scopes.
