# PD-T?proof-attempts-2-codex-77 — The central vertical-edge envelope has a positive limiting corner gap

Current audit note, 2026-11-01: Claude audit-01 accepted this record at its stated scope. Historical audit-pending statements below describe development checkpoints. Its A2 lower-bound/comparison dependencies01/04 are accepted in that same audit.

ID kind: PD-T.
Aliases: A4(a) precisely defined central competitor; midpoint/near-midpoint envelope; positive constant gap.
Split from: the edge-midpoint expansion requested in ordered target A4(a), with its source search object distinguished below.
Split into: exact all-four-edge formula70; complementary point identities/constant71–73; phase localization74, local gain75 and defect stability76.

## Statement

For the specified even-checkerboard Padua interpolation problem put m=n+1 and define the exact analytic central-edge competitor

\[
 R_{\rm cen}(n)=\max_{\substack{\epsilon\in\{-1,1\}\\
                         |t-\pi/2|\le\pi/(n+1)}}
                      \lambda_n(\epsilon,\cos t),\qquad n\ge2.
                                                               \tag{1}
\]

Then

\[
 \boxed{\ R_{\rm cen}(n)=\Lambda_c(n)-g+o(1)\quad(n\to\infty),\ }
                                                               \tag{2}
\]

over both parities, with the same explicit positive constant g in72/73. In particular

`0.548504986190 < g < 0.548525055355`,

where these are exact outward decimal representations of the independently replayed rational bounds in73. An entirely analytic description is

\[
 g=\frac8{\pi^2}\int_0^1
 \left(\operatorname{arsinh}x+\frac{x}{1+\sqrt{1+x^2}}\right)
                         \operatorname{artanh}x\,dx.       \tag{3}
\]

The selected complementary grid value C_n of72 obeys

`0 <= R_cen(n)−C_n=o(1)`.                                  (4)

Thus this result concerns the actual maximum in the specified central angular cell, not merely a fixed midpoint substitution. It does not identify that envelope with a searched list or the largest noncorner maximum on the whole square.

## Definitions and quantifiers

Lambda_c is the maximum of the four corner values; R_search denotes the programme's historical finite searched runner-up, not a newly assumed analytic object. For odd n, C_n uses the NONNODE midpoint on one x edge; the other exact midpoint is a node of value1. For even n, C_n uses the complementary ordinate nearest pi/2, displaced by pi/[2(n+1)]. The envelope(1) includes both vertical edges, the shifted critical branches or cusps they may contain, and both endpoints of its stated central cell. No assertion that a maximizing point is differentiable or unique is made.

## Assumptions

Exactly the nodes/parity/weights and total-degree cardinal polynomials in70, exact real arithmetic and n>=2. No measured count, fit, branch location, stationary-point uniqueness, full A3 constant or global argmax is assumed.

## Status by part

Overall status: **PROVED** (written all-parity asymptotic proof below; accepted by Claude audit-01, including its A2 lower-bound01 and comparison04 dependencies).

| Part | Status |
|---|---|
| Exact all-four-edge A1-type identity | PROVED separately in70 |
| Exact central envelope expansion(2), including possible shifted/cusp maxima | PROVED by74–76 and the comparison below |
| Same g for both parities, positive explicit integral/series/bounds | PROVED in72/73 |
| Identification R_cen=R_search or with the largest noncorner square-local maximum | OPEN, not a premise or part of(2) |
| Full all-n corner argmax / A4(b),(c) | OPEN and not inferred |

## Depends on and checks

70–76 and the explicitly proved A2 corner lower bound01. Indirect literal prerequisite: **PD-T?proof-attempts-codex-01 (audit pending)**; dated2026-11-01 qualification: accepted Part1 audit, completed minor dispositions and merge, final alias PD-T101. Required Part2 Claude audit remains PENDING.

The independent analytic contributions and complete reconstruction are recorded in independent-checks-a4.md and independent-checks-a4-central.md. The all-edge polynomial and complementary-point algebra regressions and K64 constant evaluation were actually run by separate agents with frozen sources; their exact finite scopes and output identities are in70/71/73 and independent-execution-a4-regression.md / independent-execution-a4-g.md. They verify finite supporting identities/evaluation, not the asymptotic theorem. The analytic convergence and phase arguments below do not rely on fitting any output.

Final development boundary2026-11-01 16:13:22UTC, observed by root's clock: root fully read70–77 and the complete independent modules, the independent route worker fully read/reconstructed the combined74–77 argument, and the separate central worker independently checked its global/local phase and joint-defect assembly. No blocking mathematical finding remained. This supplementary independent reconstruction is not the required Claude audit, which remains PENDING. No proof body was changed during the final metadata synchronization.

## Sources

Registered IDEA206 / programmeIDEA17, source05 and OPEN_TARGETS A4(a) at scientific pin9bd14a6d2c4da69139a10107d8a787f2be0c5c9e. The source describes R as the largest value found by a finite search and reports even-degree near-midpoint versus odd-degree midpoint behavior. It does not formally define an asymptotic critical branch. After recording that issue, the parent authorized the precise central-envelope continuation(1), retaining R_search as MEASURED until any equivalence is proved. The source fit≈0.548+0.84/n supplies no premise or error bound. No priority/novelty claim or author contact.

## Proof

Let C_n be72's concrete complementary central grid value. Its ordinate lies in(1)'s angular interval for every n: exactly at pi/2 for odd n and at distance pi/(2m) for even n. Therefore

\[
 R_{\rm cen}(n)\ge C_n=\Lambda_c(n)-g+o(1).                 \tag{5}
\]

For each n choose any maximizing point in(1); it exists by continuity and compactness. On the same chosen edge select a nearest complementary ordinate beta_n=q_n*pi/m. Its mesh spacing is2pi/m, so the maximizing angle has the form phi_n=beta_n+s_n/m with |s_n|<=pi. Since phi_n lies within pi/m ofpi/2, beta_n lies within2pi/m, hence beta_n->pi/2 and is an interior ordinate for all sufficiently large n. This construction covers either parity, either chosen x edge, ties, a complementary phase just outside the central interval, and maxima at its endpoints.

The exact phase decomposition76 gives

\[
 R_{\rm cen}(n)=S_n(s_n)-\Delta_n(\beta_n,s_n).              \tag{6}
\]

74's uniform phase-leading bound, together with Delta>=0 and the lower comparison(5), implies

`sin^2(s_n/2) Lambda_c(n) <= C log(n+1)+g+o(1)`.

The all-n A2 lower bound is Lambda_c>=(4/pi^2)log^2n−54. Therefore |s_n|=O(log^(-1/2)n) and in particular s_n->0. This step excludes a potentially larger fixed-phase branch; a small-window bound alone would not do so.

For sufficiently large n the phase lies in75's fixed local window. Its complete paired estimate, including numerator sign changes and the exceptional collision family, gives

\[
 S_n(s_n)\le\Lambda_c(n)+O(\log^{-2}n)
                         =\Lambda_c(n)+o(1).               \tag{7}
\]

76 applies to the same arbitrary moving phases beta_n->pi/2,s_n->0, and proves Delta_n(beta_n,s_n)->g. Thus(6)–(7) give

\[
 R_{\rm cen}(n)\le\Lambda_c(n)-g+o(1).                     \tag{8}
\]

Combining(5) and(8) proves(2); subtracting C_n's expansion proves(4). The proof used no stationarity or smoothness of the maximizing points, so exact midpoint creases and split nearby maxima are included. The positive formula and bounds for g follow from72/73. ∎

## Scope and remaining work

This completes the central-envelope formulation of the edge-midpoint expansion over both parities and supplies the requested all-edge closed formula through70. It does not silently close the historical R_search or the all-n A4 conjecture. In particular n=3's auxiliary midpoint8/3 differs from the historical searched runner-up approximately3.021223, so an all-degree identification of C_n with R_search would be false even before asymptotic considerations. Identification of R_cen with a globally selected noncorner competitor instead remains OPEN and needs an additional location theorem, not a fit.

Neighbourhood control around the actual corners and a uniform strict upper bound on the rest of the square remain the separate A4(b),(c) tasks. No effective n0 for a global theorem, explicit rate for the joint defect limit, uniqueness of an edge critical branch, or all-degree maxima count is asserted. Required Claude audit remains PENDING.

## History

2026-11-01, Codex gpt-6.1-sol xhigh, within the authorized15:24–18:24UTC A4(a) box. The central-envelope convention and its distinction from R_search were registered after analytic reductions70/71, before74–77 and before the first A4 numerical regression. The complete global/local phase and defect arguments are substantive supporting dependencies, each preserved under its own result number.
