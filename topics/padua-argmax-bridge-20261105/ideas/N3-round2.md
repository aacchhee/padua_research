# N3 round 2 — larger aggregate corner patch, unchanged first order

Rules/input: `3dda890275a7599caa707b0fb8c0b6e6f6a80643`.
Developer: requested Sol medium, serving metadata not independently exposed.

This is an implementation variant of IDEA-454/457. The corner helper owns the
per-degree energy-radius gate, proof and computation; this worker uses only its
declared interface and does not recalculate or assume its pending arithmetic.
Round 1 code/receipts remain frozen in commit 3dda890.

Separation test: keep exactly the round-1 first-order kernel and replace the
local-corner sufficient predicate by |alpha|,|beta|<=1/128 at n33/64/128,
only under the helper's independently accepted radius premise. Before that
acceptance a run is explicitly CONDITIONAL what-if, while numerical output
remains MEASURED float. This isolates the corner-patch effect from precision
and enclosure-order changes. No new sign-stability assertion is made.

Before a full outward campaign, diagnose the old n128 frontier: exact rational
box membership in the proposed phase patch; sampled old point values versus
stable sinc values; and old box upper bound versus its center value. This
does not establish a causal explanation outside its samples.

Predeclared float schedule is again n33/64/128, 600 CPU seconds each, one
million visited-box cap, identical breadth-first longest-side policy. Only
complete counts enter B2. Preserve capped frontiers. No second-order kill is
inferred from an incomplete frontier. The original B2 growth/radius criteria
remain unchanged; raise order once if their actual hypotheses trigger.

Outward next step is limited calibration at inherited n17/24/32, at most 32
visits and 30 CPU seconds each initially, plus narrow sample boxes for an
independent checker's formula/leaf controls. No hours-long tree run precedes
corner and tightness feedback. The phase checker owns another arithmetic path
and its controls; sharing tree schema and mathematical predicates is permitted,
sharing the producer arithmetic kernel is not. A validated full phase cover
requires complete coverage, all-center physical admissibility, strictness
except at the two actual nonnode corners, and different-agent acceptance.
