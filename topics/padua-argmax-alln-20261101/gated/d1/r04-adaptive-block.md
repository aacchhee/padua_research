# Direction 1, round 4 — adaptive block and shrinking corner reduction

Date: 2026-11-02. Codex, assigned gpt-6.1-sol xhigh; runtime metadata not
independently exposed. Rules/snapshot
`2dde541f1e5af239cae6e93e4438b9be89d15d87`; scientific base
`7d308b10d946b607ae0690454f6c0103690775a4`.
Pre-execution contract: [round 4](r04-contract.md). Read that contract,
the exact projected-defect normalization in theory01, the finite block in
theory05 and the previous compact-complement assembly. The completed
registry/alias/obstruction gate and full IDEA-305 / original Claude-02 /
fallback-04 shortlist from round 1 are reused. This bounded adaptive
positive-rectangle variant introduces no external literature or priority
claim. The coarse-constant implementation's round-3 STOP remains scoped
to that implementation.

## Registered candidate and completed output

Candidate: choose the physical cancellation rectangle according to the
relevant angle's endpoint distance gamma. Its separation from the old
fixed-delta block is that a small-angle point defect grows as 1/gamma,
exactly compensating for a selected interval of width gamma. The kill
tests were numerator positivity, reflected-angle geometry, collision
avoidance, parity-grid counts and a common phase radius. All are checked
by explicit finite inequalities in
[adaptive finite defect](../../theory/gated-codex-08-adaptive-finite-defect.md).

The written result is: for every n>=48 and rho<=1/8, Qv>=1/1536 whenever
min(phi,pi-phi)>=4pi/n, and Qh>=1/1536 whenever
min(theta,pi-theta)>=4pi/n. Each is uniform in the unused coordinate.
Status: **PROVED by the written finite argument; independent review and
required Claude audit pending at publication**. No numerical check is a
premise.

The separate [shrinking-corner reduction](../../theory/gated-codex-09-shrinking-corner-reduction.md)
combines this finite bound with the independently checked global/local
primitive estimates. It proves that for all sufficiently large n the
whole moving complement of the four 4pi/n corner boxes has a gap at
least 1/3072. Every global maximizer therefore lies in one of those boxes.
The degree threshold is **non-effective**. All-degree PD-T099 remains
OPEN, and no finite degree beyond the separately certified range is closed.

## Constant and normalization checks

| Case | Selected physical row / periodic interval | Point defect | Minimum counts | Bound |
|---|---|---:|---|---:|
| Small gamma, vertical | b' in [pi/3,pi/2], u in b'+[-gamma/2,gamma/2] | 3/(8gamma) | m/12 rows, n*gamma/(4pi) points | 1/(128pi) |
| Middle gamma, vertical | b' in [pi/12,pi/6], u in gamma+[-b'/2,b'/2] | 3/4 | m/24 rows, n/48 points | 1/1536 |
| Small gamma, horizontal | a' in [pi/3,pi/2], v in a'+[-gamma/2,gamma/2] | 3/(8gamma) | n/12 rows, m*gamma/(4pi) points | 1/(128pi) |
| Middle gamma, horizontal | a' in [pi/12,pi/6], v in gamma+[-a'/2,a'/2] | 3/4 | n/24 rows, m/48 points | 1/1536 |

All selected physical rows are interior and have endpoint factor 1.
The periodic parity interval spacings are 2pi/n or 2pi/m. Both projection
normalizations are 1/(nm) times the displayed row/point sum, with no extra
factor two. The common numerator lower bound is 223/512>3/8 at rho<=1/8.
All selected periodic angles lie strictly between the folded targets,
so no selected rational denominator vanishes. Replacing a physical row
angle b by pi-b' (or a by pi-a') when the relevant coordinate is near pi
gives exactly the same cosine target pair. The sine perturbations were
bounded absolutely, so reflection does not alter positivity.

## Retained variants and failure scope

| Variant | Disposition / precise reason |
|---|---|
| Fixed-delta finite rectangle from round 2 | Retained at its exact scope; its margin shrinks with delta and cannot itself supply the new uniform constant by substituting delta=4pi/n. |
| Adaptive small-angle rectangle | Retained; pointwise 1/gamma bound cancels the gamma interval width after exact grid counting. |
| Adaptive middle-angle rectangle | Retained; supplies the smaller common constant 1/1536. |
| Physical reflection near pi | Retained; exact cosine identities, not a symmetry assumption about the corrected x mode. |
| Copy vertical count without changing the periodic mesh horizontally | Not used; horizontal parity, endpoint factor and n/m roles are verified separately in theory08. |
| Claim a usable explicit threshold from finite defect positivity alone | Not pursued; quantitative global phase entry remains missing. |

No registered candidate failed development's discriminating tests. This
does not substitute for the independent checker. The full statements and
proofs live in theory08/09; this round note does not replace them.

## Gate and next obligation

**GO to independent verification of theory08/09.** New information is an
exact positive finite defect down to endpoint distance 4pi/n, followed by
a localization into a fixed-size scaled corner domain. This is distinct
from larger degree scans or adjusting the coarse local constants.

After acceptance, the remaining corner obligation can be stated on a
bounded domain: at each of the four corners, let xi=n times the first
angular endpoint distance and eta=n times the second; both are in [0,4pi).
Prove lambda_n<=Lambda_c uniformly there for sufficiently large n, with
the required equality classification. A pointwise or fixed-phase limit
does not suffice: the comparison must cover all moving xi,eta, exact
kernel collisions, the true endpoint cusp, and both node/nonnode corners.
The present result provides a concrete finite-width input for that next
task, but neither proposes nor executes an unregistered corner mechanism.
Any distinct next direction-1 round remains the orchestrator's gate
decision. No direction-2 work begins here.

## Executed work and limits

Actual work: read/search commands and analytic reconstruction of the
finite numerator, normalization, reflections, mesh counts and sequence
argument. No numerical phase or degree scan, scalar fit, external source
transfer, Git operation or shared registry edit was executed. Required
independent mathematical verification remains pending at initial
publication; required Claude audit remains pending throughout.
