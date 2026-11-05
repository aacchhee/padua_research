# Nearest-neighbour MOPs as a commuting-pair IEP (IDEA-117): log

- Branch: `codex/nn-mop-iep-20261103` · Base: main `440d107` · Developer: Codex · Auditor: Claude (Opus 5.5 xhigh)
- Stage: AUDIT · Next: `Claude (Opus 5.5 xhigh): Continue codex/nn-mop-iep-20261103.` · Audit handoff: [handoffs/02-audit.md](handoffs/02-audit.md)
- Reserved final-ID ranges: T286–293, N100–103, IDEA376–383, LIT562–573;
  first pushed in a0abe8b, [draft PR22](https://github.com/aacchhee/padua_research/pull/22).
  No final assignments yet.
- Claims and precise statuses: [report](report.md), [results](../../results/nn-mop-iep-20261103.md).

## 2026-11-03 — Claude, claude-opus-5-5 high — topic setup at AC's request

- AC's request (14:42): "make a handoff for codex thread on: B. Nearest-neighbour MOPs as a commuting-pair IEP. (proposal for a later topic, not registered; home: IDEA?bivariate-lanczos-claude-041) …" The full question is quoted in handoff 01.
- This is the "AC request" that IDEA-117's deferral ("resume only on AC request") requires.
- The source memo is P4 of the literature campaign (`claude/padua-literature-20261103` @ `d669363`, not yet merged).
- Branch created from main `440d107`. Only the handoff, this LOG and the results stub were written; no registry was edited.

## 2026-11-05 — Codex continuation, WORK

- Rules read at full topic head `320fe07f5231ac7e72a4da45e64a38e5ff381b4a`:
  AGENTS.md, agents/WORKFLOW.md and agents/codex/CODEX.md. Their bytes equal
  main `440d1079e42c3ef21c40d1cf8870f5b206410c6a`; fetched main is unchanged
  and is the recorded base. Literature campaign read-only at
  `d669363c9bce16da2af0f3b7db05a031b911edd5`; it is not merged here.
- Role: orchestrator/developer. Exact orchestrator backend model/effort is not
  exposed (runtime family GPT-6); no more specific runtime identity is claimed.
  Explicit bounded allocations: gpt-6.1-sol xhigh for the literature gate,
  gpt-6.1-sol medium for defining-system code, gpt-6-astra high for a
  supplementary independent mathematical check. Claude's required audit is
  distinct and PENDING. Only the orchestrator performs Git operations.
- AC's continuation resumes IDEA-117 under the 2026-11-03 authorization;
  no contact with Leuven is authorized or attempted.
- Gate scope, complete registry read, shortlisted predecessors and source
  coverage are recorded in gate.md and literature.md as the gate completes.
  Defining moment systems and existing recurrence identities are checked as
  baseline verification, with no generated new algorithm or priority claim.
- Completed exact developer run: [receipt](exact-runs.md), deterministic
  rational common-support examples N=2,...,8. 476 recurrence identities and
  70 shifted flatness squares pass. All 70 degree-(N-1) differences vanish;
  all 112 tested fixed-site transfer pairs fail to commute at x=0.
  These are finite MEASURED sanity checks; the elementary written proofs
  have separate durable homes under theory/.
- [Permanent reservation](ALLOCATIONS.md), scanned against main and all
  open PRs19–21. No final assignment or shared-registry edit during WORK.
  Small regenerable output remains local; no cold-storage write is claimed.

## 2026-11-05 — gate stop, exact records and supplementary check

- [Gate](gate.md) scans the complete IDEAS registry and obstruction/disposition
  tables, targeted linked theory including PD-T057, INDEX and pinned campaign
  sources. [Primary reading and search log](literature.md) checks Van Assche,
  FHV, Jacobi-on-tree, Hermite–Padé/Toda and newer finite-support predecessors.
  The explicit mismatch is one variable/two measures plus shifted flatness,
  versus two multiplication variables/one positive functional. It supplies no
  universal impossibility result for all alternative encodings.
- [C1–C4 records](candidates.md): C1 standard exact moment formulation;
  C2's literal fixed-site dictionary refuted only in the tested scope;
  C3 deferred pending an explicit distinct updater/invariants;
  C4 corrected to recursive shift families with boundary data or marginal
  recurrences. Two fixed shifted lines are insufficient. Existing finite
  perfect-rectangle theory is qualified, not imported for a normal triangle.
- Handoff01's early gate stop is applied to new method development, because
  exact reconstruction and zero curvature are established constructions and
  the suggested literal pair dictionary fails. This is not a claim of C4/C3
  stability or cost equivalence. No new C3 exists to run against C4; no
  floating-point Kravchuk/Hahn comparison or digits-lost experiment was run.
  The stability/update question remains OPEN and C3 is deferred, not rejected.
- Two elementary written PROVED records (no novelty claim):
  PD-T?nn-mop-iep-codex-01, finite normal moment formulation;
  PD-N?nn-mop-iep-codex-01, terminal zero-divisor obstruction for the specified
  naive all-layer propagation rule. Two MEASURED records preserve the finite
  checks and scoped fixed-site dictionary failure separately.
- [Supplementary Astra check](independent-check.md), gpt-6-astra high:
  original checker independently rerun, output byte-identical; separate Cramer
  and coefficient-matching implementation for N=1 and different N=4 input.
  No substantive gap found in the two elementary proofs. Finding S1: inaccurate
  dependent-predecessor comment, accepted and fixed. Code change is comment-only;
  [final rerun and hash comparison](exact-runs.md) shows identical results,
  with the output difference confined to the embedded source hash.
- Stage WORK → AUDIT. [Handoff02](handoffs/02-audit.md) requests the distinct
  required Claude Opus 5.5 xhigh audit. No audit acceptance, merge readiness,
  final-ID assignment or shared-registry integration is claimed.

## Runs needed / remaining work

- Required Claude audit: reconstruct the exact formulation/obstruction and
  scoped dictionary, check primary source coverage and candidate dispositions,
  independently rerun both committed checkers. Full commands in handoff02.
- If that audit finds a gap, developer responds to every finding before
  readiness. Final assignment and shared registries wait for PR preparation,
  including a fresh live reservation scan. No expensive numerical run is
  pending for a method that has not been defined.
- Any future stable coupled NN updater needs an explicit new scope, maintained
  invariant, terminal/breakdown handling and measurable comparison criterion.
  Large output archival is not needed for the reproducible summaries retained
  here; no claim of Windows cold-storage access is made.

Final integration verification: `git diff --check` passed. The orchestrator also
executed `python topics/nn-mop-iep-20261103/code/independent_nn_mop.py > /tmp/nn-mop-final-small.json`
(exit 0), reproducing the independent small output SHA-256
`9790542877736255d0b56d3b2285ff0d5334a4f3504587ffc0be6a96dbaee430`.
This additional integration run is not counted as a third independent check.
