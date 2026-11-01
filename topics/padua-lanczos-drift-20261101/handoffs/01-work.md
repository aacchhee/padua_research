# Handoff 01 — padua-lanczos-drift-20261101 — develop and test

- Status: open
- Previous handoff: none
- Next agent / model / effort: Codex, gpt-6.1-sol xhigh (mathematics); medium (code)
- Role: orchestrator / developer
- Branch: codex/padua-lanczos-drift-20261101
- Input head SHA: `806cc7b4509fd93bae652f9545d32d95529f8281`
- Main / base: `806cc7b4509fd93bae652f9545d32d95529f8281` (initial base `cf89b140530d5838bdb208a8c28f3e7aa676ace3`)
- Stage: WORK
- Written by / date: Codex orchestrator (exact runtime variant and effort unexposed), 2026-11-01

## Task

Execute AC's independent second-line finite-precision bivariate Lanczos campaign.
First freeze E1's benchmarks, selections, drift definition, perturbation model,
and decisive kill criterion before running sensitivity computations. Compute the
first-order span map in exact/certified arithmetic on a rational triangle grid
and rotated square; distinguish a residual-injection model from a scalar-operation
rounding model. Use certified intervals to judge the actual condition number;
overlapping intervals mean INCONCLUSIVE, never a kill by a lower-bound proxy.
E2 (an explicit-family drift theorem and matching bounds) follows only if E1
supports that route. After E1 setup, develop E3 selection principles, E4 the
universal-reorthogonalization target, E5 Padua positivity-radius witnesses and
reading (G), and E6 actual public V+A code experiments in parallel.

Read and preserve all previous evidence and failed mechanisms. Keep MEASURED
observations measured. Split substantive proofs into new `drift-codex-` theory
files. Preserve every considered mechanism in local IDEA records, and scoped
negative results in new PD-N records where evidence warrants them. Use provisional
IDs until PR preparation. Open an early draft with WORK/AUDIT/PR and AUDIT PENDING;
reserve fresh final-ID ranges using the union of current main and all open PRs.
Push at direction boundaries and about every ten minutes of changes.

## Read first

`AGENTS.md`, `agents/WORKFLOW.md`, `agents/codex/CODEX.md`; this topic's LOG and
plan; complete `state/IDEAS.md` summaries and obstruction/disposition tables;
`literature/INDEX.md`; `tracks/bivariate-lanczos/README.md`, NEGATIVE_RESULTS and
theory PD-T029–080 / PD-N007–031. In particular read PD-T041,046,047,050,051,053–056,
058–060,069,075 and PD-N013,015,020,022. Read the old topic report, SPLITS,
directions/reviews (including L2 prior art), and reusable code under L1/L2/L3.

## Scope limits

Only the orchestrator changes Git. Never main commits/pushes, merges of PRs,
force pushes, tags, `.github/`, or existing theory edits. Proposed changes to
PD-T055/T056/T075/N013/N015 go in literal old→new blocks in
`proposed-record-changes.md`. No third-party PDFs, extracts or code in this public
repository. Run upstream code outside the repository with URL/version/hash.
Keep each new file under 1 MB and all campaign files under 5 MB. Windows results
and cold-storage delivery remain pending unless an actual bridge is verified.
Contact nobody. Only AC merges.

## Acceptance and outputs

Complete the requested topic log, plan, E1–E6 direction records, report,
independent-checks, code and new theory with precise epistemic statuses, actual
commands and provenance, and explicit unresolved obligations. Computer proofs
need a written finite reduction, exact/rigorous checker and independent executed
rerun. Handoff for the required final audit is Claude (Opus 5.5 xhigh), reading
the complete `state/IDEAS.md`; supplementary Codex checks do not replace it.
Commit step outputs first. In a separate commit mark this handoff done at that
output SHA and add the next numbered handoff, preserving this instruction body.
