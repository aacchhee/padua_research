# Programme-scale research directions (ideas campaign)

- Branch: `claude/programme-ideas-20261031` · Base: `d36722823441dc40c6e19d69a174459348dd309c` (= `origin/main` at start) · Developer: Claude · Auditor: Codex (`gpt-6-astra`)
- Stage: WORK · Next: `Claude (Fable 5.1 xhigh): Continue claude/programme-ideas-20261031.`
- Claims: none yet. This topic produces programme proposals, gate records, decisive tests (MEASURED within stated scope) and a literature baseline; it registers no PD-T result.
- For the PR: the rule amendment below (material rule change, to be audited by Codex); provisional `LIT?programme-ideas-claude-NN` and `IDEA?programme-ideas-claude-NN` records; allocations through the shared ledger `topics/padua-batch-20261031/ALLOCATIONS.md`.
- Open for AC: none yet.

## Rule amendment (first commit on this branch)

AC explicitly asks to change the rules (2026-10-31). The amendment adds Claude Fable 5.1 at xhigh effort as an allowed Claude model for ideas campaigns: brief writing, conceptual candidate generation, duplicate gating and adversarial idea checks. Every existing row is kept, the Codex column is unchanged, and the developer/auditor separation, evidence rules and status words remain binding. The amendment reaches `main` only through this topic's PR, and the Codex audit must cover it as a material rule change.

### agents/WORKFLOW.md — "Roles and model allocation" table

Before (last table row, followed directly by the "Use agentic orchestration" paragraph):

```
| Adversarial audit, novel mechanism, or a stalled proof | `gpt-6-astra`, xhigh; ultra only with written justification | Opus 5.5, xhigh |

Use agentic orchestration: ...
```

After (one row and one paragraph added; nothing removed):

```
| Adversarial audit, novel mechanism, or a stalled proof | `gpt-6-astra`, xhigh; ultra only with written justification | Opus 5.5, xhigh |
| Ideas campaigns: conceptual generation, gating and adversarial idea checks | unchanged (rows above apply) | Fable 5.1, xhigh (added 2026-10-31 at AC's explicit request); Opus 5.5 xhigh remains allowed |

The Fable 5.1 row is restricted to ideas campaigns: brief writing, candidate generation, duplicate gating and adversarial idea checks. It does not change the developer/auditor separation, the evidence rules, the status words or the Codex column. Where an ideas campaign runs a tiny sanity script, Sonnet 5.5 high remains the development model for it. Record the actual model and effort in every commit trailer and log entry.

Use agentic orchestration: ...
```

### agents/claude/CLAUDE_ROLES.md — "Development", first paragraph

Before:

```
Use Sonnet 5.5 high for code and technical development, Sonnet 5.5 medium for mechanical work, and Opus 5.5 high or xhigh for mathematics. Record the model and effort. Delegate bounded tasks with explicit inputs, expected artifacts, acceptance criteria, and disjoint ownership; do not delegate Git authority.
```

After:

```
Use Sonnet 5.5 high for code and technical development, Sonnet 5.5 medium for mechanical work, and Opus 5.5 high or xhigh for mathematics. For ideas campaigns (brief writing, conceptual candidate generation, duplicate gating and adversarial idea checks) Claude Fable 5.1 at xhigh effort is also allowed, as recorded in the `agents/WORKFLOW.md` allocation table (added 2026-10-31 at AC's explicit request); Opus 5.5 xhigh remains allowed for the same work. Record the model and effort. Delegate bounded tasks with explicit inputs, expected artifacts, acceptance criteria, and disjoint ownership; do not delegate Git authority.
```

### agents/claude/CLAUDE_ROLES.md — "Independent audit", first paragraph

Before:

```
The auditor chooses the model and depth: Sonnet 5.5 high or Opus 5.5 high for protocol/technical audit; Opus 5.5 high or xhigh for mathematics; Opus 5.5 xhigh for adversarial analysis or a novel mechanism. Record the choice and its reason.
```

After:

```
The auditor chooses the model and depth: Sonnet 5.5 high or Opus 5.5 high for protocol/technical audit; Opus 5.5 high or xhigh for mathematics; Opus 5.5 xhigh for adversarial analysis or a novel mechanism; for an adversarial idea check inside an ideas campaign, Fable 5.1 xhigh is also allowed. Record the choice and its reason.
```

Other rule files (`AGENTS.md`, `agents/codex/CODEX.md`, templates) are unchanged.

## 2026-10-31 — Claude, orchestrator (claude-fable-5-1; effort not exposed by the runtime)

- Rules read at the branch head before amendment: `d36722823441dc40c6e19d69a174459348dd309c` (AGENTS.md, agents/WORKFLOW.md, agents/claude/CLAUDE_ROLES.md). `git fetch origin main` returned the same SHA; the branch starts there.
- Parallel topics seen on `origin` at start: `codex/charter-unisolvence-20261031` (head `eb7bdcd`), `claude/bivariate-lanczos-20261031` (head `55320df`), `codex/mz-constants-20261031` (head `e9761aa`). None of them changes `agents/` or `templates/`. The charter branch carries a standalone ledger reserving `PD-T001–012`, `PD-N001`, `LIT-001–041`, `IDEA-001–051`; the other two use provisional IDs only. No `topics/padua-batch-20261031/ALLOCATIONS.md` exists on any branch yet; this topic creates it.
- Roles: Claude develops (orchestrator plus Fable 5.1 xhigh reasoning subagents, Sonnet 5.5 high for tiny sanity scripts), Codex (`gpt-6-astra` xhigh) audits.
- Novelty gate: applies to the campaign; recorded per step below (`state/IDEAS.md` on `main` is empty, but the three parallel branches seed it, so the gate reads their registries too).

## Runs needed

None yet.
