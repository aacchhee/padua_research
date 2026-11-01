# Audit 03 — independent re-audit of Claude response-02

- Auditor/orchestrator: Codex; user-requested `gpt-6-astra` xhigh. Resolved
  root serving variant/effort is not independently exposed. Five distinct
  reviewers were explicitly configured `gpt-6-astra` xhigh, with fresh contexts,
  for E1, E3/E4, E5, E6 and protocol. They did not develop response-02.
- Rules/read head: `c8849a89a601e0a56342d3d568086ab8abdbc4c0`.
- Scientific candidate: `ea829d92d509f79326a1cc037844a1bac3b4de13`.
- Response diff: `1df5f89fe52f62c49d5addd58dcfea7246c5a688..ea829d9`.
  Candidate-to-read-head changes only handoff07's status and handoff08.
- Main: `28aaa20861d08074b77efc74eaef75cdcb36234d`; PR16 is merged and
  incorporated. Other open draft PR12: `7f226c1cec873fd8069feae1f4749f13d95f5c9d`.
- Date: 2026-11-01. PR15 stays draft; no final IDs allocated.

## Verdict

**CHANGES REQUIRED: 0 high, 0 medium, 3 low findings. Stage WORK.**

All ten audit02 findings are resolved in their original scope. The corrected
creator limit is valid; the new record06 is a substantive finite computer-assisted
PROVED result in its declared formal scalar model; the factor-ten target's
PARTIAL classification is accepted. Its T24 conjunct is proved under record06
and its rotated-square conjunct remains OPEN. The experiment remains MEASURED
and the both-grid sufficient test remains INCONCLUSIVE.

The new findings concern a checker that accepts absent regeneration files and
two overly strong statements about a stopping condition and a deferred repair.
They do not refute the main mathematical results or measured endpoints. The
auditor has not fixed developer code, theory, ideas, prior audits or responses.

Detailed reviewer records, reconstruction code and receipts are part of this
audit:

| Scope | Report | Essential new evidence |
|---|---|---|
| E1 scalar proof, classification and replay | [E1.md](checks/audit-03/E1.md) | [audit-03-e1-checks.json](evidence/audit-03-e1-checks.json) |
| E3/E4 limit and parent repair | [E34.md](checks/audit-03/E34.md) | [audit-03-e34-checks.json](evidence/audit-03-e34-checks.json) |
| E5 endpoint labels and quantifiers | [E5.md](checks/audit-03/E5.md) | [audit-03-e5.json](evidence/audit-03-e5.json) |
| E6 sampling, NumPy and falsifier | [E6.md](checks/audit-03/E6.md) | [audit-03-e6-checks.json](evidence/audit-03-e6-checks.json) |
| Protocol, frozen objects and results rule | [Protocol.md](checks/audit-03/Protocol.md) | [audit-03-protocol-checks.json](evidence/audit-03-protocol-checks.json) |

## Findings

### A03-L1 — explicit regeneration verification succeeds with missing files

Location: `tracks/bivariate-lanczos/code/drift/e1_scalar_finite_check.py:176`
(`check_regenerated`, particularly its two missing-file branches).

When `--regenerated` is supplied, `ok` starts True and neither absent-file
branch makes it False. Passing a nonexistent directory therefore produces four
`exists:false` entries alongside `new_regeneration.pass:true` and
`all_pass:true`. The reviewer executed this negative case separately. A partly
populated directory can likewise pass without checking all four promised runs.

Make requested regeneration verification fail when any required upper or
reproducer output is absent. Preserve the intentional mode without
`--regenerated`, which checks only committed finite certificates. Demonstrate
the absent/partial cases and a complete valid case. Retain the old response02
receipt as historical evidence; this defect does not show that its four runs
were absent. Existing independent reconstructions support the finite theorem.

### A03-L2 — an alternating-only reversal does not refute the minimum target

Location: `tracks/bivariate-lanczos/theory/drift-codex-e1-05-finite-scalar-cgs2-capacities.md:55`.

The explicitly stated rotated-square target is
`K_BJ > 10 min(K_alt,K_pivot)`. The proposed reversal
`U_BJ² < 100 L_alt²` refutes only the named-alternating comparison. For example,
exact capacities `K_BJ=9`, `K_alt=1`, `K_pivot=1/10` satisfy that reversal while
the minimum target is true (`9>1`). These are a logical countermodel for the
inference, not measured capacities on rotQ24.

For the minimum target, require an upper bound on BJ and lower bounds on both
comparators, for example `U_BJ² <= 100 min(L_alt²,L_pivot²)` with squared bounds
defined consistently. Alternatively distinguish the named-comparator target
explicitly and scope its reversal to that statement. Do not change the
accepted PARTIAL classification, current INCONCLUSIVE test or original scope.

### A03-L3 — an external reference need not produce an outside-span correction

Location: `topics/padua-lanczos-drift-20261101/ideas-e3-e4.md:194`, IDEA17's
separation criterion.

R17b is now well-defined and nonzero under its stated component guard, but the
criterion asserts that its discarded component lies outside the stored span.
External reference information does not guarantee this geometric conclusion.
For orthonormal reference vectors `r0,r1,r2`, take stored columns
`r0,(3r1+4r2)/5,(4r1-3r2)/5` and parent index p=1. They are orthonormal and
`gamma_p=3/5>1/2`. Projection onto `span(r0,r1)` returns the direction r1.
Both the discarded component `-4r2/5` and the normalized replacement difference
belong to the stored span. Rational small-angle variants give the same issue
arbitrarily close to the exact basis.

Describe the external-reference operation as the source of additional
information, and condition any outside-span separation on checking its normal
component. Preserve the valid R17a/R17b recipes, deferred disposition, H17
hypothesis and absence of a new experiment or novelty claim.

## Disposition of every audit02 finding

| Finding | Disposition |
|---|---|
| A02-M1 | RESOLVED: general limit `(kappa_A/b)||v_m||` reconstructed independently; exact 25-case producer rerun and independent spectral/Gram checks confirm the equality criterion and strict examples. |
| A02-M2 | RESOLVED: record06 has a valid finite reduction, explicit source norm/model, exact committed evidence/checker and separate independent reconstructions. PROVED split and target PARTIAL accepted. New A03-L1/L2 concern verification and a stopping condition. |
| A02-L1 | RESOLVED: actual degree4 normalized-trajectory replay independently executed for all four rules, 17710 formal operations per case; degree3 control agrees. Old audit summary error annotated without editing it. |
| A02-L2 | RESOLVED as an operational definition: R17a uses the strict stored prefix, R17b the exact graded reference prefix with a nonzero-component guard. Deferred variant retained. New A03-L3 corrects a stronger separation assertion. |
| A02-L3 | RESOLVED: ordered roots reconstructed from the exact limit polynomial; labels agree. |
| A02-L4 | RESOLVED: fixed-negative-a statement is eventual only; the fixed n4 periodic counterexample independently certified by Arb384 in two formulations. |
| A02-L5 | RESOLVED: square iid, triangle iid and deterministic midpoint constructions distinguished; triangle overlap density independently derived and exactly checked. |
| A02-L6 | RESOLVED: exact NumPy2.3.5 pin consistent; actual unchanged upstream freshly passes there and fails at NumPy2.4.1 as disclosed. |
| A02-L7 | RESOLVED: one accurate same-code/node fit correctly falsifies the universal failure inference; finite measured disposition preserved. |
| A02-L8 | RESOLVED: active plan/report/proposals/COLD_STORAGE instructions now use repository-only results and preparation-only root RESULTS updates. Windows archive delivery stays separate/pending. |

Audit02's accepted dispositions of the earlier42 findings remain in force;
resolved-by-proposal items still await preparation. This is a delta re-audit,
not a new claim that every unchanged original record was rederived this session.

## Coverage and execution

Each report records its complete reads, inspected code, commands actually run,
versions, input hashes, output identities and limitations. E1, E3/E4 and E6 read
the complete 783-line `state/IDEAS.md`, including obstruction/disposition tables,
and the relevant full predecessors. E5 and protocol record justified
non-novelty exemptions. Root read the rules, handoff08, audit02, response02,
new scalar statements/status split, relevant IDEA17/proposals/results, the
reviewer reports and both complete allocation ledgers, with differences across
all current heads. No new mechanism, source novelty or priority claim is made;
no new paper fulltexts were acquired.

Fresh independent executions include:

- E1 exact/Arb512 scalar reconstruction with an independent implementation:
  all950 node signs agree with zero ambiguous decisions; exact T24 and rigorous
  rotQ24 endpoints support squared ratios 657331.0774535 and 62.0855366899.
  The degree3/4 trajectory replay is numerical corroboration at 80 digits,
  not an exact proof or a degree12 replay. Missing-regeneration verification
  was challenged separately from the successful finite-certificate checks.
- E3/E4 exact producer regression plus independently reconstructed full
  closure/spectral quantities and the reference-repair countermodel.
- E5 fresh developer checker plus independently expanded cosine series and
  a 25-term polynomial/Arb384 finite evaluation; true balls certify negativity.
- E6 fresh actual-source run: all370 numeric leaves equal response02 exactly;
  separate JSON comparison, exact midpoint geometry and isolated NumPy probes.
- Root ran `integration_check.py --head c8849a89a601e0a56342d3d568086ab8abdbc4c0
  --main 28aaa20861d08074b77efc74eaef75cdcb36234d
  --pr PR12=7f226c1cec873fd8069feae1f4749f13d95f5c9d
  --output topics/padua-lanczos-drift-20261101/evidence/audit-03-integration.json`:
  PASS. The temporary squash tree equals the tested head tree; the PR12
  merge-tree is explicitly clean. No live branch/PR merge was performed.

Remote inventory and [union scan](evidence/audit-03-union-scan.json) confirm
main28aaa, only PR12/15 open, all returned closed PRs merged, no reserved-range
final assignment, preserved ledger/crosswalk content and all77 original theory
files unchanged. No scientific registry, protected rule or root RESULTS change
was made. Fresh readiness checks remain necessary at preparation.

## Status and remaining uncertainty

Records01–04,06,10–11,15,30–32 retain their scoped PROVED conclusions; record05's
experiment and record50 retain MEASURED. Record05's explicitly decomposed target
is PARTIAL. Record14 remains a withdrawn tombstone awaiting preparation deletion.
Neither post-hoc discovery nor an unresolved separate target lowers record06's
proved finite inequalities. Its formal capacity does not establish IEEE error
realization or finite-epsilon/all-degree behavior.

The original all-degree drift target, general staircase safety, PD-T055,
PD-T075(U2), PD-T056(G) and rotated scalar factor ten remain OPEN. No broader
numerical suite, literature coverage or storage delivery is implied by these
reruns. Earlier raw response02 regeneration files are absent in this workspace;
their historical receipt is distinguished from freshly reproducible committed
inputs. The original Codex ZIP/raw artifact identities verified in audit02 are
unchanged; Windows cold-storage delivery remains pending and is not a
verification blocker for the committed regeneration path.

Size/pin inventory is recorded in the audit03 manifest. All artifacts remain
within the conservative whole-campaign decimal5MB and per-file1MB limits.
Return the three narrow findings to Claude in handoff09. Re-audit material
checker changes in a bounded follow-up; do not repeat accepted development or
allocate final IDs before the audit closes.
