# IDEA?argmax-bridge-codex-N1-02 — Pole norms and cancellation integral

Aliases: outer-row compactification; cutoff-free cancellation quadrature;
two cotangent channels; bounded variation at moving numerator zeros.

- Scope: continue N1-01 toward a finite-dimensional all-degree model.
  The original N1-01 theorem and proof remain frozen.
- Precise mechanism: write an absolute row as the sum of two individual
  absolute cotangent norms and the cancellation
  g=|C cot x+D cot(x+v)|-|C cot x|-|D cot(x+v)|. Keep the singular
  one-dimensional sums exact and replace only g's sample sum by its integral.
  Use bounded variation, not a derivative bound through coalescing zeros.
  Extract finitely many endpoint and central rows if required.
- Closest full records: IDEA-329/337/459; T216/T217/T221/T226; T269's
  fixed-offset dominated-sum argument; the round-1 N1/N2/N5 records.
  Their exact row identities, midpoint pole subtraction and finite collision
  terms are dependencies, not a new mechanism merely under a new name.
- Gate: round-1 full registry baseline remains the complete campaign scan.
  Round 2 searched IDEAS, argmax topics, Lebesgue follow-ups and INDEX for
  finite-part, pole-subtraction, diagonal-pole/profile, outer-row,
  turning-point, bounded-variation and cutoff-rounding terms. T269's full
  proof was read; it controls a corner deformation, not this signed-channel
  cancellation. No external source theorem or historical novelty claim.
- Separation criterion: remove the numerator-root floor/ceil data with a
  proved quantitative error uniform through all sign transitions. A bound
  that diverges at unextracted rows or still needs a growing number of
  sign-cutoff parameters does not satisfy this compactification step.
- Cheapest decisive test / prewritten kill: prove an explicit total-variation
  bound for g over one period, then sum its error with the actual row weights.
  If endpoint/central singularities prevent a summable uniform error, either
  give one explicit finite-chart correction or stop this formulation.
- Test discriminability: exact sign arcs and variation inequalities can
  prove the stated domain; additional phase samples cannot prove uniformity.
- Status/disposition at formulation: active, no fit or new run. The complete
  full-diamond compact model and usable n1 remain OPEN.
- Canonical theory: to be assigned only to the precise proved subclaim;
  scope must not silently shrink the original compactification goal.

## Retained alternatives

1. **Direct smooth Euler–Maclaurin on a row quotient:** deferred unless
   all moving pole products are first regularized. Holding phases fixed
   while continuously interpolating a row index can introduce poles absent
   on the actual parity mesh. The existing finite row identity supplies no
   uniform derivative bound for such an extension.
2. **Numerator-root rounding from an unqualified bounded derivative:**
   deferred. The combined kernel vanishes at a regular root, but a root can
   coalesce with a pole; a separate chart is required before a uniform
   second-order rounding conclusion. No failure of the true model is claimed.
3. **Same-mesh pure A-channel product reference:** deferred as a complete
   model. The paired reference suggests J_n(alpha+beta)J_n(alpha-beta),
   but on the diamond boundary it captures only half the known logarithmic
   coefficient. Sine channels and unequal-mesh corrections cannot be dropped.
   This is an algebraic diagnostic of the proposed reference, not a new
   leading-only PD-N entry; PD-N132 already preserves that broad warning.
4. **Nearest-pole sinc chart:** retained as a possible correction. The
   coefficient zero and its nearby cotangent pole must be multiplied before
   taking limits. No standalone collision bound is claimed from this remark.

History: 2026-11-05, round 2 after parent-pushed boundary 714f3ca;
Codex requested gpt-6-astra ultra. No new numerical run or fit at formulation.

## Round-2 outcome

Retained developer-PROVED supporting lemma
PD-T?argmax-bridge-codex-N1-02 in
[N1-cancellation-quadrature](../theory/N1-cancellation-quadrature.md).
It proves periodic variation <=8 max(|C|,|D|)/|sin v|, a half-variation
shifted-grid error, and the complete weighted full-diamond error

    r_n+2(sin alpha+sin beta)H_n/n+2a(n+1)/(n(R-1)).

The model keeps at most 2R+4 exceptional rows for fixed R. Every other row
uses single-pole norms with explicit offsets and a cancellation integral;
its moving numerator-root integer cutoffs are eliminated. This satisfies
the stated intermediate separation test. It does **not** remove the outer
sum or supply the full compact model, so those original goals stay OPEN.
No scoped negative theorem is claimed for the deferred alternatives above.
The next correction must keep the pole norms and cancellation integral
together when extracting their endpoint logarithmic profile.
