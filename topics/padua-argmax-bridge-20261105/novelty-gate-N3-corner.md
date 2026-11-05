# N3 corner-energy quantitative gate — 2026-11-05

Rules/input: `714f3cad18859c07cd13f31561f2a185f9591a7f`.
Developer: Codex, parent-assigned gpt-6.1-sol xhigh; serving metadata is
not independently exposed. This gate precedes the implementation below.

This is a bounded implementation continuation, not generation of a new
mechanism. The inherited complete registry scan, full obstruction/disposition
coverage, searches and reading qualifications are preserved in
`novelty-gate-baseline.md`; the existing N3 gate is `novelty-gate-N3.md`.
I read those records, handoff01/plan, the full IDEA-330 final entry,
IDEA-454 and IDEA-457, registry argmax/phase-2 disposition and obstruction
rows, full PD-T227/251/367/369, and PD-T368's exact bound, definitions,
dependencies, source qualification and reduction. Targeted searches cover
weighted energy, aggregate sign changes, physical corner radii and W_n
across the three predecessor argmax topics and literature/INDEX.md.
I do not represent truncated registry displays as a fresh complete scan.

Verdict: quantitative implementation variant of IDEA-330/457 inside
IDEA-454. PD-T227 already supplies the exact aggregate Taylor model and
its radius implication. PD-T251 supplies normalized slopes, while
PD-T367–369 already supply all-degree energy/norm/radius constants.
The change is to evaluate the actual finite per-degree energy by outward
arithmetic, replacing the coarse 10^10 by a verified degree-specific bound.
There is no new mechanism, priority or first-constant claim.

The precise computational distinction is a larger rigorously justified
physical L1 radius H, usable by the existing phase-cover corner predicate.
It is falsified if actual outward bounds fail to enlarge the inherited
strict-descent domain, or if obtaining/checking them costs more than the
cover benefit. This is not a claim of a better uniform-in-n constant.

PD-N085 excludes fixed-scale per-cardinal affine sign preservation;
the aggregate inequality permits individual sign changes. PD-N086 excludes
fixed signs on coarse diamonds; no sign-fixed region is assumed here.
Initially zero cardinals are omitted from W_n exactly as PD-T227 requires,
but their inward slopes remain included through PD-T251. The exceptional
00 cardinal is included using its explicit removable formulas.

Cheapest test before large runs: independently reconstruct the elementary
radius implication; implement O(n^2) outward node-formula sums; compare
small n values/gradients to a direct corrected coefficient-kernel diagnostic;
then evaluate n=33,64,128. No per-degree computer claim becomes PROVED
without a distinct exact/outward replay. A complete phase cover and B2
verdict remain separate obligations. No new sign-radius or true-sign
preservation claim is proposed, so no smallest-root computation is needed.
