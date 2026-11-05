# Padua argmax bridge — current results

Branch `codex/padua-argmax-bridge-20261105`, [draft PR27](https://github.com/aacchhee/padua_research/pull/27). Stage WORK; required Claude audit pending.

**Independently checked global finite range: 2–36.** New exact certificates
at33–36 pass the separate C++/GMP checker;36 corruption controls reject as
expected. The remaining bridge is37<=n<N_*, with N_* still non-effective.
PD-T099 remains **OPEN**. [Finite proof/evidence](../topics/padua-argmax-bridge-20261105/theory/native-finite-range.md).

Analytic development results, with supplementary reviews recorded:

- Exact full-phase cotangent rows and collision/sign-arc handling, extending
  the beta-zero predecessor. [N2](../topics/padua-argmax-bridge-20261105/theory/N2-row-decomposition.md).
- Uniform fourth-order arbitrary-offset cotangent block error, exact poles
  retained; no pole-distance lower bound. [N5-01](../topics/padua-argmax-bridge-20261105/theory/N5-partial-cotangent.md).
- Full-diamond n-dependent row-model error
  r_n=[7pi^4/1800+7pi^3H_n/900]/n^4, and a quantified cancellation-integral
  reduction eliminating moving numerator-root cutoffs. The outer sum remains
  degree-dependent; compactification and onset are OPEN.
  [N1](../topics/padua-argmax-bridge-20261105/theory/N1-cancellation-quadrature.md).
- Wider central vertical-edge actual-lambda defect floors, n>=32, phase
  windows .5/.25 and explicit strip hypotheses. Developer proof; distinct
  review in progress. [N5-02](../topics/padua-argmax-bridge-20261105/theory/N5-central-edge-defect.md).

**N3 measured throughput:** complete float covers33/64/128 use2028/1908/1794
visits and12.22/47.46/162.65CPU-s after a larger per-degree corner patch.
The corrected independent exact corner replay verifies that patch at those
three degrees; initial checker-contract error and actual corrected rerun are
disclosed. B2 finite floating throughput/count scope passes. No full outward
cover or new phase-certified degree is claimed.
[Measurements](../topics/padua-argmax-bridge-20261105/theory/phase-cover-measurements.md).

N4 and N6 produce scoped structural obstructions: unrestricted transport is
equivalent to the norm target; exact mode-diagonal positive translation works
only on the complementary grid; fixed same-t trace domination and probability
full-vector trace lifts fail. Broader routes are deferred, not rejected.
No external theorem or novelty claim is transferred from unread papers.

Next: full outward overlap/replay and practical cost, sharper actual-lambda
control, and a compact uniform-degree profile with a proved effective onset.
No Syvert pack until B4's analytic/throughput condition is met. Small evidence
stays in Git; raw outputs/libraries stay local with physical archival pending.
