# Direction 1, round 5 — thin lattice lines and actual corner phases

Date: 2026-11-02. Codex, assigned gpt-6.1-sol xhigh; runtime metadata not
independently exposed. Rules/snapshot
`2dde541f1e5af239cae6e93e4438b9be89d15d87`, scientific base
`7d308b10d946b607ae0690454f6c0103690775a4`.
Pre-registration: [round 5](r05-contract.md), with the preserved
[prospective lattice candidate](r04-next-lattice.md). Read both, the
exact projection formulas and the accepted round-4 finite construction.
The full registry/alias/obstruction gate and IDEA-305 / Claude-02 /
fallback-04 shortlist from round 1 remain applicable. This is a bounded
discrete refinement, not a new source transfer or novelty claim.

## Completed finite candidate

[Theory10](../../theory/gated-codex-10-noncorner-coset-defect.md) proves
Delta>=1/4096 for n>=48, rho<=1/64 at every physical odd-coset center
other than an actual physical nonnode corner. It verifies all four thin
endpoint constructions and uses the adaptive finite block at center
endpoint index distance at least 5. Status: **PROVED by the written finite
argument; supplementary independent review and required Claude audit
pending at initial publication**. No numerical scan is a premise.

For the thin cases the registered constants survive unchanged:
numerators >=1/32, vertical span <26/m or horizontal span <26/n,
point defect >=m/416 or n/416, and at least n/8 or m/8 physical rows.
The exact projected normalization is 1/(nm), so the selected lines give
Q>=1/3328, stronger than the stated common defect constant.

| Orientation / endpoint | Physical row | Periodic index | q for odd / even endpoint distance |
|---|---|---|---|
| Vertical top K=m-s | k=l+q, n/4<=l<=n/2 | j'=n-l | 1 / 0 |
| Vertical bottom K=s | k=l+q, n/4<=l<=n/2 | j'=l | 0 / 1 |
| Horizontal top J=n-s | j=l+q, m/4<=l<=m/2 | k'=m-l | -1 / 0 |
| Horizontal bottom J=s | j=l+q, m/4<=l<=m/2 | k'=l | 0 / -1 |

All physical rows are interior, with endpoint factor 1. The vertical
parity condition is j'+k=J mod 2; the horizontal one is k'+j=K mod 2.
The table satisfies these conditions for every parity and endpoint.
The proof bounds the signed phase terms rather than assuming beta or
alpha has a preferred sign. All chosen points lie strictly inside their
cosine bands, so no selected denominator collision is hidden.

The horizontal fixed numerator was checked separately: the periodic
folded angle w lies in [pi/8,3pi/4], so its baseline 1+B is 1-cos w
near the top or 1+cos w near the bottom, each >1/16. This does not
interchange the asymmetric corrected mode with the vertical numerator.

## Consequence and true remaining gap

[Theory11](../../theory/gated-codex-11-corner-phase-localization.md)
combines that finite bound with the exact same global/local primitive.
Every sufficiently-large-degree global maximizer has an actual nonnode
corner as its odd center, and its phase distance rho tends uniformly to
zero over all global maximizers. The statement is quantified for every
fixed phase neighborhood, with a **non-effective** degree threshold.
It supplies neither equality at the corner nor any finite coverage up
to that threshold. PD-T099 and P6 remain OPEN.

## Retained failures and variants

| Variant | Disposition / exact scope |
|---|---|
| Round-4 adaptive intervals at all near-endpoint cells | Insufficient by themselves below 4pi/n; the finite line construction supplies that missing regime. The old theorem is unchanged. |
| Horizontal top q=+1 for odd s | Failed selected-line construction: at zero phase and s=1 its normalized band displacement has magnitude >=5pi/4>pi. Retained as the preliminary failure; not a refutation of the defect target. |
| Registered horizontal q=-1 for odd s | Retained; all band and parity cases verified. |
| Import vertical numerator without checking horizontal B | Not used; fixed-numerator positivity proved independently in theory10. |
| Infer an effective threshold or exact corner equality from phase localization | Not pursued; neither follows from the qualitative phase estimates. |

No registered corrected construction failed development's discriminating
tests. Its independent mathematical check is still required.

## Gate and next discriminating obligation

**GO to independent verification of theory10/11.** New information is a
finite positive defect at every noncorner odd center, and therefore a
reduction to vanishing phase neighborhoods of the actual two nonnode
corners rather than four boxes containing several possible centers.

The remaining corner issue has a precise cancellation test: expand or
bound the actual four-copy cardinal sum in a fixed small corner phase
diamond and show a uniform strict quadratic loss away from phase zero,
including its zero-cardinal terms and collisions. A primitive-only pure
quadratic estimate is already obstructed by the endpoint cusp; that cusp
must be canceled at the actual four-copy level before invoking a quadratic
corner comparison. No such comparison is asserted or developed in this
round. A future gate needs a concrete uniform sign/radius or cancellation
estimate; merely observing that the phases tend to zero would not justify
another round or an all-degree conclusion.

The orchestrator decides whether that remaining test belongs to another
direction-1 round or the separately authorized corner direction. This
worker performs only round 5 and starts no future round or direction-2
work.

## Executed work and limits

Actual work was read/search commands and analytic verification of the
four displacement formulas, parity conditions, physical index ranges,
positive numerator baselines, denominator spans, finite row counts and
uniform maximizing-sequence argument. No degree grid, phase scan, fit,
new literature transfer, Git operation or shared registry edit occurred.
The complete proofs, with assumptions and limits, are in theory10/11.
