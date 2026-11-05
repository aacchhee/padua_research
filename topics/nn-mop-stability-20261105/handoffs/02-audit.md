# Handoff 02 — nn-mop-stability-20261105 — independent Claude audit

- Status: open
- Previous handoff: [01-work.md](01-work.md)
- Next agent / model / effort: Claude, Opus 5.5 xhigh
- Role: independent mathematical auditor and topic orchestrator
- Branch: codex/nn-mop-stability-20261105
- Input head SHA: `ff783d59587100ab291cb83d690ef27a09f0f154` (scientific outputs; the later commit publishing this handoff is distinct)
- Main / base: `5adc3e2b7226e2c3c5577335058823a8e5cc3629`
- Stage: AUDIT
- Written by / date: Codex, requested gpt-6-astra high · 2026-11-05

## Task

Audit the completed bounded development campaign at the input SHA. Do not treat the supplementary Astra checks as the required independent Claude audit. Reconstruct the mathematics, inspect actual code and evidence, execute independent checks, and state coverage and limits. Do not expand local first-order theorems or finite measurements into a general stable NN solver result.

Read the complete state/IDEAS.md because the campaign includes mechanisms and scoped negatives. Read the full relevant entries, obstruction/disposition tables and linked theory. The D6 worker discloses that some summary coverage completed after the prescribed background probe; assess that timing honestly, without retrospective prospective clearance or a historical novelty claim.

Prioritize:
1. The self-contained Krawtchouk lower proof, scalar generating polynomials, exact NN coefficients/field scale, terminal jets, formal coefficient transformations and summed-coefficient addendum. With M=N−1 it proves
       kappa_N >= 5/(2M^2)*[(5+2sqrt(6))^(M−1)+(5−2sqrt(6))^(M−1)].
   Check all quantifiers, small N, fixed-mass admissibility, input/output norms and the distinction between a lower exponential base and a sharp rate. Separately check the fixed-N proximity theorem: kappa*d_min diverges for each N>=4 as p2 decreases to p1=2/5.
2. The coarse upper/normality proof; noncircular generic d-normality reduction; finite exact Hahn theorem for precisely every N4–64. Check its 61 committed input/payload fingerprints, 43,676 exact nonzero tests, checker code and independent receipt.
3. The exact local derivative/induced-norm formula and monic step-line extraction. Check all 3N directions, mass-null gauges, zero coefficients, structural zeros, output field scales, N versus M, and unit roundoff u=2^-53 versus epsilon=2^-52. The every-integer conditioning table is MEASURED at180/260dps, not an outward enclosure. Independent exact Jacobian checks cover N3,4,6; larger numerical precision agreement is not an independent all-grid rerun.
4. G0/G1/G2 on the frozen six-size baseline grid, both families. The fixed10*kappa*u criterion fails at listed cases; do not rename this a general instability theorem. Verify stable/oracle marginals, input-rounding separation and path-plus-anchor limitations. Independently challenge the off-path and missing-anchor traps.
5. Both native whole-triangle designs, monic/basis scaling and full-array coefficient extraction. The forward threshold is achieved in finite attainable cases; known reformulations are not claimed historically novel.
6. The actual joint-data image embedding/left inverse and local SPD nearest projection theorem. Check normalized masses, ordered common nodes, positivity/normality and full compatibility. Verify the exact five-field dyadic obstruction independently. Distinguish a standalone exact certificate from platform-dependent reproduction of a floating producer.
7. Numerical fits/witnesses: N4/8, two families, C4/LU/nodeqr,100/160dps. Returned rational witnesses, exact N4/N8 normality, coefficient correction and input displacement are separate from optimizer convergence and from strict backward error. Final code names pre-round optimizer stationarity separately from returned-witness180dps stationarity. No certified global nearest point or general100u stability claim.
8. Finite Christoffel transport/Toda closure and terminal boundary, positivity-to-normality counterexample, fixed common-ratio orbit obstruction and scoped failed predivide solver. Oracle initialization is not an IEP solution.
9. Graph mixed-test encoding and its scoped standard-grade/two-sheet obstructions. Full NN-to-Padua recurrence dictionary/stable transfer remains OPEN.
10. Actual source-access limits and literature coverage. G5 is BLOCKED: GitLab and SIAM ZIP retrieval return CONNECT403, web connector cannot readZIP, Octave absent/uninstalled. No external code or paper configuration was run, and no Leuven contact was made.

## Read first

- AGENTS.md, agents/WORKFLOW.md and agents/claude/CLAUDE_ROLES.md at the candidate head; record full rule SHA.
- LOG.md, plan.md, rounds.md, gates.md and report.md in this topic.
- All attempts/D1.md through D7.md, attempts/D1-hard.md, novelty-gate-*.md and candidates-D3-D5.md / candidates-D4.md.
- Every theory/*.md and code/*.py needed by the claims, including finite receipt/checker and exact dyadic witness.
- independent-checks-01.md,02.md,03.md and their own checker code; these are supplementary, with exact scope/hash records.
- evidence-manifest.json, input-snapshot.json, COLD_STORAGE.md, cold-storage.json, external-code.md, literature-D4.md, literature-access.md and plot-receipt.md.
- Original handoff01 and the predecessor PR22 evidence/theory/audits cited there; relevant LIT-347/348/562–568 and primary sources before relying on them.
- results/nn-mop-stability-20261105.md and proposed-record-changes.md.

## Reproducible checks

Run from repository root with NumPy/SciPy/mpmath; plotting additionally needs matplotlib. Actual versions and all commands are in direction receipts. At minimum independently execute and inspect:

    python topics/nn-mop-stability-20261105/code/conditioning_verify_normality.py
    python topics/nn-mop-stability-20261105/code/backward_dyadic.py --reproduce
    python topics/nn-mop-stability-20261105/code/independent_check_moments.py
    python topics/nn-mop-stability-20261105/code/independent_check_backward_integrable.py
    python topics/nn-mop-stability-20261105/code/independent_check_diagnostics.py
    python topics/nn-mop-stability-20261105/code/independent_check_followup_parity.py
    python topics/nn-mop-stability-20261105/code/independent_check_followup_proximity.py
    python topics/nn-mop-stability-20261105/code/independent_check_followup_projection.py

The follow-up projection checker compares its own fit to two producer receipts at /tmp/backward-projection-{family}-r2-160.json. If they are absent, first regenerate the two160dps producer commands in attempts/D5.md at those explicit paths; record that preparation separately from the checker's own fit. Other listed exact checkers generate their inputs from the repository. Do not call regenerated local producer output an archived developer artifact.

Re-run both frozen C4 commands in attempts/D2.md. For the full conditioning table use the producer/timing wrapper commands in attempts/D1.md, separate auditor output paths, then conditioning_compare.py with the corresponding prefix. Audit depth and additional direct-moment/large-N runs are yours to choose and disclose; never describe reviewing developer output as a rerun. Use the exact plotting command in plot-receipt.md for the full61 grid, not substituted sampled data.

The large local artifacts may not survive this cloud session. All essential finite exact evidence is committed; raw floating data/figures are regenerable. No external cold-storage delivery or historical-Git-blob export is claimed. A byte digest is an identity, not a correctness check.

## Scope limits

Only write inside this topic and its results file during audit. Do not silently fix developer mathematics/code and approve your own fixes. Return actionable findings, let development respond, and reaudit material changes.

No final IDs or shared scientific registries were assigned. Ranges T432–471,N162–177,IDEA530–569,LIT614–629 are permanently reserved at first publication d87925630e9e460031df319f3994ca2e7fad8ca0 in draft PR28. Refresh main/all live and retired reservations before eventual assignment/readiness. Do not alter another topic's ranges or branch.

AC explicitly allowed the GitHub connector's Andrey Chesnokov <59649991+aacchhee@users.noreply.github.com> author address for campaign commits; this is a session authorization overriding handoff01's email requirement. Keep Agent/Model trailers and metadata limits. Only the orchestrator changes Git. No main commits, merges, force pushes, tags, .github changes, Syvert/other-machine compute or messages to Leuven. Sandbox compute limits remain handoff01's limits.

## Acceptance and outputs

Write audit-01.md with audited SHA/hashes, exact coverage, actual model/effort, executed commands/observations, findings by severity and residual limitations. Update LOG/results and PR28's AUDIT section honestly. Accepted scope sets PR for preparation; findings set WORK. Draft remains until the required audit and preparation are complete.

Commit/push the audit outputs first. Then, in a following commit, change only this handoff's status to done in that output SHA and add handoff03 for Codex response or audited preparation, as appropriate. Give a complete bounded instruction and correct model allocation; preserve all earlier handoff bodies. Link the new handoff in the log and end with the short continuation prompt. Only AC merges.
