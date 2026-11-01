# Handoff 07 — padua-lanczos-drift-20261101 — Claude response to audit-02

- Status: open
- Previous handoff: 06-reaudit.md
- Next agent / model / effort: Claude, Opus 5.5 xhigh for mathematical and status decisions; Sonnet 5.5 high for code and medium for routine edits under the workflow
- Role: developer / response orchestrator
- Branch: codex/padua-lanczos-drift-20261101
- Input head SHA: `0a082b1efc43009d77140ffa0b396bf4fec8add5` (the commit publishing this handoff comes later)
- Audited scientific response: `cef79d66321a93d93d53e53efcb7e6744c387481`
- Main / base: `28aaa20861d08074b77efc74eaef75cdcb36234d`, merged at `7a6dd1f7f8f10d0f9c2568e89d693b7d04cd571b`
- Stage: WORK; PR15 remains draft
- Written by / date: Codex, requested gpt-6-astra xhigh re-audit allocation; resolved root runtime metadata unexposed, 2026-11-01

## Task

Address audit-02's **two medium and eight low findings** in a new
`topics/padua-lanczos-drift-20261101/response-02.md`, with an individual
disposition for A02-M1/M2 and A02-L1…L8. Do the fixes and appropriate checks;
do not merely propose them in the reply. Preserve audit-01, audit-02,
response-01, all prior developer/reviewer reports and frozen evidence.
Accepted original results need not be reopened. The full42 original
dispositions and13 record dispositions are in audit-02; its scientific
reviewers reproduced all response evidence and found no high issue.

### Mathematical/status work

1. **A02-M1 (record15).** Its generalized lemma gives δ_A=κ_Aθ and κ_creator≥b.
   The auxiliary relative-source equality currently drops κ_creator/b.
   Correct it to lim δ_creator/u=(κ_creator/b)||v_m||, or state only the
   consequent lower limit. The exact counterexample is uniform T3/BJ with
   source in v20: ||v20||²=22/5, b²=7/15, κ_X²=28/45, squared limit88/15.
   Core(a)–(d), the qualitative no-o(u) result and the original v21 instance
   remain accepted. Preserve the correction history and add an appropriate
   exact/checkable regression for the newly generalized assertion.
2. **A02-M2 (record05).** Separate the supported finite scalar inequalities
   from the inconclusive experiment. Keep the MEASURED experiment, post-hoc
   provenance and current both-grid factor10 INCONCLUSIVE verdict. Put the
   substantive finite bounds/>800/>7 implications into a dedicated,
   precisely scoped computer-assisted PROVED record with an unused provisional
   identifier, reduction, exact checker/essential evidence and independent
   rerun references. Existing independent evidence already reproduces both
   full-operation uppers, witnesses and all950 signs; preserve its source pins
   and distinguish reused evidence from a new execution. Do not silently
   upgrade measured implementation behavior or claim an IEEE lower bound.
   If you dispute the classification/substantiveness, write the concrete
   reasoning and preserved disagreement for AC while completing the other
   fixes. Do not suppress a substantive proof because another target is OPEN.
3. **A02-L1.** Correct current scalar-trajectory coverage: the committed
   `first_principles.py` actually replays record03 only at n3; n4 checks01/02.
   Correct current records/directions/IDEA text and annotate the old audit's
   summary error without editing audit-01. Alternatively execute and retain
   the missing n4 replay with honest new chronology. No n12 replay is required
   by this correction and none is already claimed.
4. **A02-L2.** Keep IDEA?drift-claude-17 deferred, but define a nonzero parent
   repair or explicitly make that definition a resumption obligation. Ordinary
   projection subtraction against a span containing the parent gives zero.
   Specify the intended index prefix/reference columns and where extra
   information enters before any experiment; no new experiment is requested.
5. **A02-L3/L4.** Correct record30's a_± endpoint labels and change the a≤0
   claim to eventual no-witness scope. Main rho_n=O(n^-5), the sharper
   219.5413805… limsup and the minor-corollary classification are confirmed.
   For the finite-wording counterexample, fix a*=20pi³/9−512pi and n=4:
   periodicity gives the positive-a point, with Arb-certified P4<0. Preserve
   the fixed-parameter/eventual distinctions already corrected in record32.

### Measurement/protocol work

6. **A02-L5.** Correct midpoint-law wording in record50/E6/checker comments.
   Only the iid native-square midpoint has product triangular density. The
   triangle has overlap-area/piecewise-quadratic density; T24/Q24 sets are
   deterministic. Retain actual sample construction, centre-concentration
   qualifications, numerical results and target chronology disclosures.
7. **A02-L6.** `<2.5` is an insufficient NumPy restriction: isolated NumPy2.4.1
   also fails in the unchanged pinned polyrat. Document the tested2.3.5 pin
   or a correct exclusion including2.4, consistently across README, source
   record, theory/direction and IDEA55. Do not patch/vend the upstream source.
8. **A02-L7.** Fix IDEA57's kill direction: an accurately fitted target on
   the same nodes/code falsifies “drift implies every fit fails.” The existing
   finite evidence and REJECTED disposition are correct; preserve the
   undocumented-chronology/post-hoc qualifications. No rerun is needed merely
   to reverse a logically wrong sentence.
9. **A02-L8 and PR16.** PR16 is merged and its repository-only results rule
   is active. Supersede the active Windows-results obligations in
   proposed-record-changes:143, plan:35, report:164 and other current frontiers.
   The topic results file is `results/padua-lanczos-drift-20261101.md`.
   Its own root RESULTS section is added only at PR preparation; preserve
   every other topic's section. Windows cold-storage delivery is separate,
   remains pending and does not authorize a Windows results write. Historical
   receipts and old handoff bodies stay unchanged.

## Read first and verification inputs

Read AGENTS.md, WORKFLOW.md and your Claude role at the new branch head;
record its full SHA. Then LOG, this handoff, audit-02.md and all five
`checks/audit-02/*.md` reports, their compact JSON receipts and manifest;
audit-01/response-01 as needed for history. Read complete state/IDEAS.md
before any new mechanism or novelty-bearing change, then the relevant full
records and INDEX entries. Keep the source-reading limits explicit.

Auditor code and outputs are committed under `checks/audit-02/` and
`evidence/audit-02-*.json`. Exact commands are in each reviewer report. E1
response rerun mathematical fields, E4's28 cases, E5 response output, and
E6's388 response/422 n16 leaves reproduce; independent checks are separately
identified. The first-principles scalar replay is n3 only. The audit's
isolated NumPy2.4 probe directories are outside Git and must not be bundled.

Original-artifact uncertainty is resolved locally: the advertised799968-byte
ZIP and all81 source entries match b09e1dbe, the raw capacity/root E6 files
match their hashes, and147 distinct original run-output paths verify.
One earlier record05 working-byte metadata pin is unavailable; do not invent
it or claim its old bytes were compared. Current proof and computational
dependencies are independently reviewed. No Windows delivery was performed
in audit02; compact committed evidence plus regeneration is the verification
path, with no hidden dependence on the3.6MB raw file.

Current integration evidence is `evidence/audit-02-integration.json`: main28aaa,
PR12=9a75747 and tested head7a6dd1f, PASS for the reservation/crosswalk content,
unused own ranges, clean PR12 merge-tree and disposable squash equality.
This is not a future readiness certificate. Refresh main/open PRs when
continuing and record any new impact; never rewrite published history.

## Scope limits

- Do not edit audits or reviewer/developer reports to resolve findings.
- Preserve all77 original bivariate theory records. Approved upstream changes
  remain literal proposals until PR preparation, with final-ID mappings.
- No final IDs or scientific registry edits during this response. Permanent
  ranges remain T136–155, N062–071, IDEA246–285, LIT445–459. Withdrawal of
  record14 leaves one fewer PD-N; never reuse another topic's reservation.
- No main commits/pushes, PR merges, force pushes, tags, `.github/`, vendored
  third-party code/PDF/fulltext or author contacts. Only AC merges.
- Each committed file≤1MB and campaign≤5MB. At audit02 the entire own campaign
  was about3.9MB, largest616693bytes. Preserve small essential checkers/results;
  do not split large artifacts merely to evade limits.

## Acceptance and outputs

Produce response-02.md with all10 dispositions, changed file/line ranges,
old→new scientific wording/history, actual checks with commands/versions/pins,
and all remaining uncertainty. Update the topic LOG/results summary and PR15
WORK/AUDIT/PR sections honestly. MEASURED stays MEASURED for the experiments;
post-hoc finite proofs and unresolved targets have distinct homes. Do not
promote actual IEEE, all-degree, general staircase, U2 or reading(G) claims.

Material proof, status or scope changes return to AUDIT for Codex
gpt-6-astra xhigh. A statement that a fix “looks obvious” is not independent
acceptance. Keep PR15 draft; final-ID/registry/root RESULTS preparation waits
for acceptance. Resolve or preserve any disagreement explicitly.

Commit response outputs first. In a following commit change only this
handoff's status to `done in <response-output-sha>` and add the next numbered
re-audit handoff with complete instructions and exact candidate SHA. Push
before replying; keep exactly one open handoff. Only AC decides merge.
