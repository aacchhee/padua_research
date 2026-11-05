# Candidate dispositions — the four candidates prescribed by handoff01

Final IDs assigned at audited PR preparation; provisional aliases retained. These are retained interpretations of the supplied C1–C4,
not a fresh family of generated algorithms. Gate: [gate.md](gate.md).
Parent/home: IDEA-117 (and IDEA-031/090/111/193 aliases/predecessors identified
by the gate). No claim of exhaustive novelty clearance.

## IDEA-376 — C1: finite discrete formulation

Provisional alias: `IDEA?nn-mop-iep-codex-01`.

- Aliases: normal moment triangle; common-support nearest-neighbour IEP.
- Question / scope: N distinct common real nodes, two positive weight vectors;
  determine monic type-II polynomials through total degree N and recurrence
  coefficients through degree N-1, assuming every required index normal.
- Mechanism and hypotheses: solve each square mixed moment system. Positivity
  alone does not supply invertibility. Terminal polynomials coincide.
- Closest full records: IDEA-117 and IDEA-193; FHV/Van Assche and the
  finite-support Kozhan–Vaktnäs literature discussed in the gate.
- Separation criterion: a claimed new solvability formulation would have to
  add information beyond defining moment systems and known NN compatibility.
  A direct standard moment solve kills that distinction.
- Literature baseline / limitations: gate.md and literature.md. Common support
  permits a normal triangle; it is not a perfect rectangle of two disjoint
  supports, so the newer rectangle theorem is not silently applied here.
- Applicable obstruction: positive proportional measures have singular mixed
  systems; perfectness beyond common-support rank N is impossible.
- Novelty verdict: variant/direct formulation; no new mechanism.
- Cheapest decisive test / pre-existing kill criterion: compare with the
  defining linear systems and FHV before any expensive computation.
- Test discriminability: exact definitions settle algebraic equivalence;
  finite experiments alone would not establish general normality.
- Actual results: [formulation proof](theory/finite-moment-formulation.md),
  [finite checks](exact-runs.md), [independent check](independent-check.md).
- Disposition: equivalent to the standard direct moment baseline within its
  explicit normality domain. Not a rejected theorem and no administrative PD-N.
- Canonical record: PD-T?nn-mop-iep-codex-01.
- History: 2026-11-05, Codex; prescribed candidate from handoff01.

## IDEA-377 — C2: literal commuting-pair interpretation

Provisional alias: `IDEA?nn-mop-iep-codex-02`.

- Aliases: fixed-site transfer commutator; zero curvature versus multiplication.
- Question / scope: identify the two usual 3-by-3 NN transfer matrices at one
  lattice site with the commuting coordinate pair of PD-T057.
- Mechanism and hypotheses: the tested literal proposal identifies the usual
  same-site transfers with a commuting pair. The real spectral question is
  whether there are two independent coordinate multiplications. Both NN
  difference operators instead have eigenvalue x on the MOP state. Precise
  standard transfer state/matrices: exact-runs.md.
- Closest full records: IDEA-117/193 and PD-T057; Van Assche/FHV zero curvature
  and integrable-systems predecessors in literature.md.
- Separation / kill criterion: the actual matrices must commute at the same
  site; a nonzero exact commutator kills this literal dictionary. This does not
  test every possible lifted encoding.
- Literature baseline / search limitations: gate.md. Global covariant lattice
  shifts can commute under flatness; their entries and state spaces are not
  PD-T057's finite symmetric multiplication sections.
- Applicable obstruction: both NN directions have the same eigenvalue x,
  versus independent joint coordinate values (x_l,y_l). PD-T057 blockwise
  interior commutativity also couples adjacent levels. The fixed-site test
  therefore rejects only the named literal dictionary, not every lattice
  encoding or an analogy based on coupled identities.
- Novelty verdict: existing zero-curvature interpretation, no new mechanism.
- Cheapest decisive test: rational transfer multiplication at x=0.
- Test discriminability: distinguishes the named matrices only; not a
  no-go theorem for all encodings or algorithms.
- Actual results: 112 nonzero fixed-site commutators; 70 shifted flatness
  squares pass. Independent N=4 example confirms both at one site.
- Disposition: REJECTED: refuted within the tested finite scope for the
  literal fixed-site dictionary. Broad useful analogy retained as background.
- Canonical negative record: PD-N?nn-mop-iep-codex-02.
- History: 2026-11-05, prescribed C2; no universal impossibility claim.

## IDEA-378 — C3: a new path-wise node update

Provisional alias: `IDEA?nn-mop-iep-codex-03`.

- Aliases: Van Barel–Chesnokov-style NN update; coupled path transport.
- Question / scope: add a common node with two weights, maintaining a chosen
  normal triangle, both recurrence directions, moment/weight conditions and
  shifted compatibility, with a boundary rule and useful numerical accuracy.
- Mechanism and hypotheses: the supplied proposal names an analogy, not a
  fully specified transformation or invariant-preservation proof.
- Closest full records: IDEA-117/193, the 2010 bivariate updater and 2026
  step-line updater; corrected C4 is the algebraic comparison baseline.
- Separation criterion: provide an explicit update that preserves the above
  constraints and has a demonstrated advantage over corrected C4.
  Repeating known compatibility or invoking same-site commutation kills a
  claimed distinction. No statement that all possible updates are equivalent.
- Literature baseline / limitations: gate.md and literature.md. Numerical
  stability remains a research question; literature residual reports are not
  local experiments or comparative proofs.
- Applicable limits: C2's literal dictionary fails; terminal d=0 is a final
  boundary condition, not a C4 obstruction. Nonnormal input cannot be cured
  by positivity or changing path names.
- Novelty verdict: no separated new method survives this gate.
- Cheapest decisive test: write exact objects and invariant before an update
  implementation. This test is conceptual; no C3 implementation was run.
- Test discriminability: prevents measuring an unspecified method as though
  it were a candidate algorithm; does not refute existence of a stable method.
- Actual results: no new algorithm, complexity bound or floating-point claim.
- Disposition: deferred, not rejected. Resume only with a concrete coupled
  update and comparison metric, or AC's refined request.
- Canonical theory / PD-N: none for deferral; underlying update question OPEN.
- History: 2026-11-05, prescribed C3; gate stopping condition applied.

## IDEA-379 — C4: known algebraic reconstruction baseline

Provisional alias: `IDEA?nn-mop-iep-codex-04`.

- Aliases: shifted step-lines; marginal Jacobi data; FHV compatibility.
- Question / scope: reconstruct NN data from the actual two measures, using
  known marginal recurrences or recursively generated shifted step-lines.
- Mechanism and hypotheses: FHV's reconstruction with all required shifts,
  actual second-measure boundary information, normality and nonzero divisors;
  stop at coefficient degree N-1. Its terminal b equality is automatic.
- Closest full records: IDEA-117/193 and FHV2015; newer finite-support
  compatibility/inverse literature, carefully qualified in gate.md.
- Separation / kill criterion: if known conversion plus the actual input
  suffices algebraically, a new exact-solvability claim adds no method.
  Conversely two fixed lines must not be claimed to cover the entire triangle.
- Literature baseline / limits: the step-line alone loses part of the second
  measure. There are arbitrarily indexed shifted lines. No comparison of cost
  or floating-point stability is implied by exact reconstruction.
- Applicable domain limit: b2-b1=0 at common-support degree N-1, but C4
  through that coefficient layer divides only by d of degree <=N-2. No
  terminal modification is needed under full normality through degree N.
- Novelty verdict: known exact baseline after the stated corrections.
- Cheapest decisive test: inspect FHV's shift and boundary requirements, then
  check exact finite terminal behavior. Both performed before any new solver.
- Test discriminability: source formulas settle needed data; exact checks
  identify the divisor degrees used and cannot prove numerical stability.
- Actual results: primary layer-formula recheck, positive reconstruction
  proof and exact layer-recursion rerun; see source-recheck-01.md.
- Disposition: equivalent/background exact reconstruction, complete on the
  stated normal triangle. The former failed-submechanism classification is
  withdrawn under F1: the terminal division would produce out-of-domain
  degree-N coefficients and is not used by C4.
- Canonical record: PD-T?nn-mop-iep-codex-04; former PD-N?nn-mop-iep-codex-01
  survives only as a historical redirect, with no final negative allocation.
- History: 2026-11-05, corrected interpretation of prescribed C4.
