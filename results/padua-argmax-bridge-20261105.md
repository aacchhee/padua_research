# Padua argmax bridge — current research results

The exact global corner-argmax range is **2–38**. Degrees33–38 have small
complete certificates and separately executed exact C++/GMP acceptance,
including strict off-corner equality classification.
[Finite theorem](../topics/padua-argmax-bridge-20261105/theory/native-finite-range.md).
The39/40 producer candidates are complete but still under independent
check. All-degree **PD-T099 remains OPEN**; no effective onset is known.

The independently reconstructed **local** corner patch covers every
n2–128: kappa>=1/16000 and phase-square radius1/128. This gives local
coverage, not a global maximum theorem for39–128.
[Local theorem](../topics/padua-argmax-bridge-20261105/theory/N3-corner-batch.md).

Analytic supporting results:

- Exact full-phase cotangent rows and sign/collision treatment
  ([N2](../topics/padua-argmax-bridge-20261105/theory/N2-row-decomposition.md));
  uniform fourth-order shifted-cotangent truncation
  ([N5-01](../topics/padua-argmax-bridge-20261105/theory/N5-partial-cotangent.md)).
- An explicit degree-dependent row-model error, cancellation quadrature
  and a joint endpoint residual uniform in degree/log-degree
  ([N1-05](../topics/padua-argmax-bridge-20261105/theory/N1-joint-endpoint-profile.md)).
- The entire singular endpoint mesh and finite polynomial endpoint rows
  now reduce to an explicit quadratic in log n, with fixed-size
  coefficient evaluation and phase-uniform K4(1+log n)/n error
  ([H4](../topics/padua-argmax-bridge-20261105/theory/N1-round4-endpoint-block.md)).
  Independent review accepts the corrected double-collision proof.
- The unchanged reported error certificate nevertheless exceeds0.06 for
  every admissible R and n<=10^6. It cannot serve half-margin budgets
  <=0.06; this is not a lower bound on true error
  ([budget obstruction](../topics/padua-argmax-bridge-20261105/theory/N1-round4-budget.md)).
- For n>=64, every interior complementary vertical-edge center and
  inward two-phase radius |alpha|+|beta|<=1/2, actual lambda is below S
  by1/2048 and below M by255/524288. Independent review accepts the
  quantified proof
  ([two-phase defect](../topics/padua-argmax-bridge-20261105/theory/N5-two-phase-defect.md)).
  This does not prove the model maximum or E-C.

**Practical certifier:** the unchanged complete n17 phase candidate now
passes its separate Arb path:1288/1288 leaves,0failed/0pending, exit0,
109.45checkerCPU-s plus1.29build/helperCPU-s. This is an alternative
verification at a known degree, not a new degree or scaling law. The old
364-failure baseline replay, failed hybrid and corrected NaN finding are
preserved. [Verification record](../topics/padua-argmax-bridge-20261105/theory/N3-phase-n17.md).
Floating33/64/128 covers remain measured at2028/1908/1794visits and
12.22/47.46/162.65CPU-s; higher-degree outward calibration is next.

N4/N6 provide scoped obstructions to specified transport/trace classes;
broader routes are deferred, not rejected. No unread external paper is
used as a transferred theorem or priority claim.

Next: a gated coupled-error correction, remaining central/interior charts,
and higher-degree outward cost/coverage. No B3/onset or B4/Syvert release.
The required Claude audit remains pending; supplementary reviews are
recorded in the topic. AC permits10MB total generated outputs for now
and directs major cleanup to a separate topic.
