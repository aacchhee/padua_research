# Supplementary audit: surviving gen4-2 proposal

- Candidate/rules SHA: `614709d4a60fb0c2593b05764e8d5aceda1be381`.
- Current-main base: `07c5f5465d6de306aa81dbe8ca1f615295163864`.
- Auditor: independent Codex subagent, requested `gpt-6-astra xhigh`; runtime model/effort metadata is not separately exposed. Parent orchestrator publishes the audit.
- Scope: surviving gen4-2 proposal and its T1–T3 evidential claims. This is an audit, not development; developer files were not changed. Read AGENTS, WORKFLOW, Codex role, full `state/IDEAS.md` including all obstruction/disposition tables, `literature/INDEX.md`, full IDEA-17, `report.md`, `proposal-1.md`, adversarial/decisive gen4-2 records; inspected decisive evaluator, T1/T2/T3 producer/checker code and relevant stored outputs. No global novelty clearance is claimed.

## Verdict

**Changes required.** The finite numerical observations are reproducible, and the conservative outcome “no programme” is reasonable. The surviving project's claims of complete certification, an immediately publishable corrected table, and twelve-digit asymptotic constants exceed the checked evidence. These findings do **not** establish that the numerical counts or fitted constants are false.

## Findings

### P1 — Major: complete maxima certification is not established

Locations: `proposal-1.md:19,28,49`; `report.md:57,182`; `checks/decisive-gen4-2.md:64–87`; `checks/code/decisive/gen4-2/t3_certify.py:187–207,222–258`.

The code replays the counts, but its degeneracy treatment uses tolerances as exact identities. In `degenerate_max`, tiny cardinal values/gradients and a negative background Hessian are converted into a claim of one strict maximum in a tiny unresolved ball. Those local jet inequalities do not imply one maximum: the model

`lambda(x,y) = 2 - x^2 - y^2 + epsilon*abs(x)`

has two strict maxima at `(±epsilon/2,0)` for every positive epsilon, however small. The supplied local implication returns success at epsilon = 1e-12. `proposal-degenerate-counterexample.py` executes that implication on four polynomials summing to one; it is explicitly **not** a Padua counterexample or a complete Lagrange basis. It shows why numerical indistinguishability cannot certify an exact count without additional algebraic identities or root isolation. The actual n=3 run uses the degenerate-max path twice, and no exact identity is supplied to discharge the missing hypotheses.

Other completeness obligations also remain: `last_resort` can return `'max'` immediately after the first accepted sign-pattern root (line249) without checking other surviving patterns in the discarded box; it discards a pattern when an unconstrained Newton iterate lands outside the box (lines233–234), whereas its injectivity bound is asserted only on the box. The latter requires a proved enclosure/convergence argument or a hull certificate; the ordinary concave-box path elsewhere does check a hull. The regular-crease branch uses numerical near-coincidence as exact coincidence (lines241,253–257). Merely replacing floating-point evaluations by interval arithmetic will not supply these missing logical steps.

All observations remain MEASURED. Retain the counts as independently reproduced candidate maxima and proposed corrected counts. Before describing the table as certified/settled/publishable, provide the finite reduction and exact or rigorously enclosed certificates, prove the degenerate identities and all box-discard implications, and rerun an independently checkable certifier. Alternatively downgrade the claims and put certification under Runs needed. The preliminary discrepancy with the published table is valuable evidence even after that downgrade. A small factual correction: the overall minimum reported margin is not1.5e-6; n=6 has pattern margin4.34e-7 in both the committed output and this replay (still above the chosen1e-8 threshold).

### P2 — Major: selected-fit stability replaced the preregistered uncertainty

Locations: `proposal-1.md:17,27`; `report.md:56,182`; `checks/decisive-gen4-2.md:19–20,60–62,86`.

The preregistration defines uncertainty from the spread over the K=3,4,5 unshifted fits plus ten times their residual. Independent replay of 18 fits gives c in `[1.846095095877555..., 1.846161206769239...]`, half-spread `3.3055445842289e-5`, confirming the developer's disclosed strict uncertainty. A later selected/shifted fit gives a much narrower stability range, but neither that selection nor an assumed Euler–Maclaurin model supplies a bound on the unknown asymptotic remainder. Proposal/report summaries drop the strict result and present `±2e-12` and twelve-digit resolution as if the preregistered test achieved them.

Report both as different measurements, explicitly marking the narrower result as post-registration model-conditioned fit stability. The absence of a PSLQ relation at a selected tolerance does not prove a genuinely two-dimensional/new constant or establish that Paper A is more than a note. State the T2 result as inconclusive under its original precision target, or provide independently justified remainder/error control. Preserve the high-precision finite corner evaluations and the measured expansion conjecture.

### P3 — Minor: keep the finite T1 quantifiers

Location: `checks/decisive-gen4-2.md:93` calls the corner theorem “true for all n ≤ 200.” The actual scope is all n=2…64 and twelve selected larger degrees, using finite meshes and polished candidate maxima. Replace with “no counterexample found at the 75 tested degrees”; the all-n argmax and complete continuous-domain bounds remain OPEN. Other portions of the proposal already state the finite scope correctly.

### P4 — Minor: current counting implementation is Padua-specific

Locations: `proposal-1.md:19`; `checks/decisive-gen4-2.md:89` describe node-set-agnostic code. `LebDense` imports `padua`, uses Padua kernel weights/correction, and the degeneracy handlers rely on its square/corner/node geometry. State generalisation as planned until another node family is implemented and checked. The record correctly says Morrow–Patterson and Xu were not run.

## Executed checks and observed results

All commands below run from the pinned snapshot root with `OPENBLAS_NUM_THREADS=1`; T3 also sets `OMP_NUM_THREADS=1`. No producer output was overwritten.

1. `python topics/programme-ideas-20261031/audit-support/proposal-rerun.py`: executes the developer's imported certifier separately for n=3…8. Totals `15,27,25,41,50,62`; interior `7,13,14,25,33,44`; edge `6,12,9,14,15,16`; corners two each; zero undecided. Box/depth statistics match the stored output. Times approximately `0.99,6.26,9.23,19.85,42.99,94.84` seconds on this executor. This is an independent execution of developer code, not an independent proof.
2. `python .../audit-support/proposal-independent.py`: independently constructs cardinal polynomials by inverting an unscaled product-Chebyshev Vandermonde; imports no developer evaluator. All 220 listed points agree in lambda to at most `7.994e-15`; gradient norms at most `2.881e-14`; every point passes 64-direction rings at radius1e-5. Larger rings sometimes cross shallow valleys, as the developer already reports. This supports the existence of the numerical candidates, not completeness of the list. Vandermonde condition numbers are below3.
3. `python .../audit-support/proposal-fit.py`: independent mpmath QR fit implementation on stored long-double finite observations; result above. This replays fits, not the original costly large-degree corner evaluations.
4. `python .../audit-support/proposal-degenerate-counterexample.py`: tests the local one-maximum implication, returning success despite two nearby strict maxima; limitation stated above.

Environment: Python3.12.14, NumPy/SciPy versions in `proposal-independent.json`; deterministic runs, no random seeds. Source/output content identities and byte sizes are in `proposal-manifest.json`.

## Primary-source spot checks

Read selected primary HTML sections on 2026-11-01:

- [Białas-Cież–De Marchi–Suder, arXiv2605.23299v1](https://arxiv.org/html/2605.23299v1), §3.3/Table3 and introduction: the table reports total15,27,25,39,42,56 for n3…8 and presents numerical observations. The developer's quoted table is accurate. I did not independently read this full paper.
- [Kolomoitsev–Lomako, arXiv2009.07114v1](https://arxiv.org/html/2009.07114v1), §2.1 Theorem2.1 and §2.2 equations2.3–2.6: the stated Padua leading coefficient and the rhombus projection coefficient are supported. These statements do not establish the proposed second-order corner expansion. I did not read its full proof or conduct a new follow-up search.

No contacts were made. No exhaustive ownership/priority verdict follows from these checks. Full source reading and independent remainder control remain needed before a paper-level novelty claim.
