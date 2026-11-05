# Nearest-neighbour MOPs as a commuting-pair IEP (IDEA-117): log

- Branch: `codex/nn-mop-iep-20261103` · Base: main `440d107` · Developer: Codex · Auditor: Claude (Opus 5.5 xhigh)
- Stage: WORK · Next: `Codex (gpt-6.1-sol xhigh): Continue codex/nn-mop-iep-20261103.` · Open handoff: [handoffs/01-work.md](handoffs/01-work.md)
- Reserved final-ID ranges: none yet (reserve when the draft PR opens).
- Claims: none yet.

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
