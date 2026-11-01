# Handoff 01 — padua-argmax-alln-20261101 — update the plan after part 2

- Status: open
- Previous handoff: none

- Next agent / model / effort: Claude, Opus 5.5 xhigh
- Role: orchestrator
- Branch: claude/padua-argmax-alln-20261101
- Input head SHA: `f44a606f6d9c0620c69e77c3b99b4dc59e6e4764` (plan, gate, ideas and observations; the commit that publishes this file comes later)
- Main / base: `28aaa20861d08074b77efc74eaef75cdcb36234d`
- Stage: WORK
- Written by / date: Claude, claude-opus-5-5 · 2026-11-01

## Task

Wait until `codex/padua-proof-attempts-2-20261101` (PR #12) has finished A4(a), B3 and B1 and has its Claude audit. If AC asks earlier, use the current head and say so. Then:

1. Fetch main and the part 2 head. Record both SHAs, and merge main into this branch if it moved.
2. Read part 2's final A4(a) records (70–79, or whatever exists), their audit dispositions, and its final LOG and results file. Note which pieces of plan §4 (A)–(C) they already supply: the edge profile, the central envelope and the constants. Note any new counterexample or obstruction.
3. Revise [plan.md](../plan.md): update §0 (known results) and §4–§5, re-estimate the error budget against the proved edge gap and the measured interior gap (about 1.75), and adjust the kill criteria if needed. Keep the original text in a "History" section; never delete earlier wording.
4. Update [ideas.md](../ideas.md) and [gate.md](../gate.md) if part 2 changes any verdict, and rerun the relaxed novelty gate against the current `state/IDEAS.md`.
5. Write the part 3 Codex prompt, built on plan §5.1 (profile convergence) and §5.2 (monotonicity) as pre-registered decisive tests. Store it as `handoffs/02-<step>.md` and give AC the short continuation line.

## Read first

AGENTS.md, agents/WORKFLOW.md and agents/claude/CLAUDE_ROLES.md at the branch head; this topic's LOG.md, plan.md, ideas.md, gate.md and theory/; part 2's LOG, attempts/T-A4a.md, theory records 01–04 and 70+, its audit, and `results/padua-proof-attempts-2-20261101.md`; PROOF_STATUS rows PD-T098–T101; programme-ideas OPEN_TARGETS A4.

## Scope limits

- Do not write to part 2's branch or files.
- Make no PROVED claim without a written proof and audit.
- Do not open final IDs until a PR is opened, and then by the fresh-range procedure.
- Only AC merges.

## Acceptance and outputs

- Revised plan.md, ideas.md and gate.md as needed, with the LOG entry and `results/padua-argmax-alln-20261101.md` updated.
- Handoff 02 with the part 3 prompt.
- Commit the outputs. Then, in a following commit, set this status to `done in <sha>` and add handoff 02 in the same commit.
