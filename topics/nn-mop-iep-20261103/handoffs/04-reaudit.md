# Handoff 04 — NN MOP response-01 re-audit

- Status: open
- Previous handoff: 03-response.md
- Next agent / model / effort: Claude, Opus 5.5, xhigh.
- Role: independent auditor of Codex response-01.
- Branch: codex/nn-mop-iep-20261103
- Input head SHA: `5b36f8f8ac5b3c9a426d22a9375155a2b4d86e1b`
- Main / base: `5db1e01dcd2258f45de2adcaef43859e59734618`
- Stage: AUDIT
- Written by / date: Codex, 2026-11-05; exact orchestrator backend/effort
  unexposed. Bounded workers: gpt-6.1-sol xhigh mathematics/primary checks,
  gpt-6.1-sol medium numerical pilot, gpt-6-astra high supplementary review.

## Task

Independently re-audit response-01 to Claude audit-01. Fetch topic/main and
record rules and audited SHAs; published history must not be rewritten.
Main5db1e01 was merged at9ec2a54c5b6af56514feaf11c9fc329f19a88820.
Rule files did not change. The new response output is the exact input above;
the following commit only closes handoff03 and adds this handoff.

1. Read AGENTS.md, WORKFLOW, Claude roles, LOG, audit-01, handoff03,
   response-01 and its linked records. The gate/negative-disposition scope
   calls for the complete IDEAS registry and obstruction/disposition tables;
   read the shortlisted entries and linked theory, including newly listed
   IDEA-197. Read literature/INDEX.md before opening primary sources.
2. **F1:** reconstruct theory/interior-divisor-nonvanishing.md (T?…03) and
   theory/marginal-reconstruction.md (T?…04), both proposed PROVED. Check
   the successor difference, normal opposite corner, independent polynomial
   family in E/F, signs/indices in A/B1/B2, axis data, induction coverage,
   N=1 and finite domain. Each requested coefficient layer t uses lower
   denominators t−2 and diagonal denominators t−1, never terminal d.
3. Verify the primary locators in source-recheck-01.md and the literature
   addendum as access permits: FHV1406.0364v2 Thm3.1/(3.3)–(3.10), pp16–18;
   Thm3.3/(3.11)–(3.15), pp20–21; VanAssche1104.3778v1 Thm3.1/(3.1)–(3.5),
   pp9–10; KV2407.13946v2 §2.2 p5, Def2.8 p8, Lemma2.18b p11,
   Thm3.6/Remarks3.7–8 pp16–17. Distinguish your own primary checks from
   the developer recheck; the full local proofs do not assume external
   theorems. If access fails, record exact coverage/gaps rather than inherit
   primary clearance. No paper copies/text were committed.
4. Check withdrawal of the former PD-N?…01 active failure classification:
   its full historical wording remains in terminal-division-obstruction.md;
   positive content maps to T?…03/04 via SPLITS.md. The original algebra is
   retained. The proposed failed step would produce out-of-domain degree-N
   coefficients and is not a C4 step. Verify this meets L5 and split rules;
   no administrative negative ID, status downgrade or silent claim deletion.
5. **F2:** same-site tests refute only a literal dictionary. Blockwise
   PD-T057 also couples neighboring levels. The actual mismatch is that both
   NN difference operators have eigenvalue x on consistent MOP states,
   while two coordinate multiplications give joint values (x_l,y_l).
   No universal impossibility of alternate/covariant/lifted encodings.
6. **F3:** audit the new bounded C4-only pilot, code/c4_float_baseline.py,
   c4-baseline-01.md and MEASURED T?…05. Verify primary family weights
   in arXiv2608.25758v1 §5.1 Examples5.1–2 p20, N nodes k=0,...,N−1,
   z=2k/(N−1)−1 and monic a/b conventions. Inspect genuine binary64
   Stieltjes marginals+A/B layers versus140/220-digit references. Check
   fieldwise sup-norm-relative metric and epsilon/digits formula, no-terminal
   division, exact independent moment comparison atN4 only, and precision
   convergence limitations at largerN. Completion is not accuracy: errors
   exceed one for several cases. No general instability, conditioning
   decomposition, C3 comparison or source residual reproduction is claimed.
7. Independently execute the commands below and record code/input/output
   identities, versions, exit status and results. Auditor layer code is
   unchanged from audit-01; its new developer replay is not an independently
   implemented proof. Check the supplementary report's actual coverage; it
   is additional evidence, not acceptance of this re-audit.
8. **F4 / N1 / N2:** confirm version-field and timing-dependent raw hashes
   are distinguished from case-payload identity, source coverage is scoped,
   and IDEA-197's non-applicability reason is sound. Check report/candidates/
   results/log/PR consistency with every finding and new record.

## Reproducible commands

From repository root, write raw outputs outside Git:

```sh
python topics/nn-mop-iep-20261103/audit-01/claude_layer_recursion_check.py > /tmp/nn-mop-reaudit-layer.json
python3 topics/nn-mop-iep-20261103/code/c4_float_baseline.py --family krawtchouk --sizes 4 8 12 16 24 32 --dps 140 220 > /tmp/nn-mop-reaudit-krawtchouk.json
python3 topics/nn-mop-iep-20261103/code/c4_float_baseline.py --family hahn --sizes 4 8 12 16 24 32 --dps 140 220 > /tmp/nn-mop-reaudit-hahn.json
```

Layer checker: standard-library Fraction; expected24 cases,467 sites,
809 nonzero divisions,128 terminal zero-d sites, max divisor degree N−2.
Baseline: Python+mpmath1.3.0 in developer environment, code SHA-256
9ce76ae88fb798f73127f75819bcdfb6c7bffb0d9cd092d70957164cb9b6a2e8.
Every reference comparison passed1e−60; worst1.42e−99. Source/input/code
identities and all values in c4-baseline-01.md. New outputs include version,
platform, argv and timing; raw hashes need not reproduce across executions.
Compare mathematical case payloads and record any variation honestly.

## Read first / do not reopen

Read all response-owned files listed in response-01.md, source-recheck-01.md,
SPLITS.md, response-independent-01.md and topic results. Audit-01 and its code
are immutable auditor evidence. The accepted original T?…01 and original
MEASURED counts T?…02/N?…02 need not be redeveloped; only F2 wording and
F4 metadata notes changed their surrounding records. Do not reframe this
response as a new novelty claim or a solution of stable coupled updating.

## Scope limits

Write only audit-02.md, necessary short topic-owned evidence, LOG/results and
handoff status/next instructions as orchestrator. Never silently fix developer
claims in an audit. No shared scientific registry integration or final IDs in
this step. Preserve the permanent ranges T286–293,N100–103,IDEA376–383,
LIT562–573 and all inherited reservations/gaps; fresh scan waits for final
assignment/readiness. Do not merge PR22, force-push, alter tags, touch .github
or contact anyone. Raw data remains local/regenerable; no cold-storage
transfer is claimed or needed for these bounded receipts.

Draft PR: https://github.com/aacchhee/padua_research/pull/22.

## Acceptance and outputs

Produce audit-02.md with full audited SHA/hashes, model/effort, primary-source
coverage, independently executed commands, severity-ranked findings and limits.
Explicitly disposition F1–F4/N1/N2, split/withdrawal, T?…03/04 PROVED and
T?…05 MEASURED. Update only topic LOG/results and PR AUDIT; retain draft
status until preparation/readiness obligations are met.

If findings remain, return WORK with handoff05 for Codex gpt-6.1-sol xhigh
(medium for purely technical fixes). If clean, set PR and handoff05 for Codex
gpt-6.1-sol medium preparation: refresh main/open/closed-unmerged reservation
union, deduplicate same-source LIT addenda, assign final IDs from the unchanged
ranges, keep the withdrawn provisional negative historical, and make additive
topic-only registry/index/crosswalk/results/frontier updates. Material new
changes require audit. Do not declare readiness before preparation completes.

Commit audit outputs first. Then in a following commit change only this
handoff status to done in the output SHA and add the complete handoff05.
Link that handoff in the output log before its commit, preserve exactly one
open handoff and push before replying. Only AC merges.
