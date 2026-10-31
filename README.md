# Padua research

An independent research campaign owned by AC. The scientific question, scope, assumptions and success criteria will be set in the first research topic.

## Start here

1. Read [AGENTS.md](AGENTS.md), [agents/WORKFLOW.md](agents/WORKFLOW.md) and your role file: [Codex](agents/codex/CODEX.md) or [Claude](agents/claude/CLAUDE_ROLES.md).
2. Read [state/CURRENT.md](state/CURRENT.md) for the current frontier and open decisions.
3. Before a new idea, use [state/IDEAS.md](state/IDEAS.md). Before opening a paper or making attribution or novelty claims, read [literature/INDEX.md](literature/INDEX.md).
4. AC starts work with `New topic: <objective>.` The agent creates a topic branch, records the work, obtains an independent audit and opens a PR. AC merges.

## Research database

| Location | Purpose |
|---|---|
| `state/CURRENT.md` | Frontier, priorities and next decisions |
| `state/IDEAS.md` | Ideas, aliases, novelty gates, obstructions and dispositions |
| `PROOF_STATUS.md` | Canonical result IDs, statuses, dependencies and evidence |
| `ID_CROSSWALK.md` | Provisional-to-final ID provenance |
| `PAPER_MAP.md` | Manuscripts and their supporting results |
| `literature/CORPUS.md` | Sources known or supplied, whether read or unread |
| `literature/INDEX.md` | Extracted published statements by claim type |
| `literature/records/` | Source records with hypotheses and page/theorem references |
| `tracks/` | Scientific tracks, theory files and scoped negative results |
| `topics/` | Branch logs, proposals, audits, responses and reproducible checks |
| `templates/` | Reusable records for ideas, results, sources, topics and cold storage |

The registries start empty. No scientific result, source, negative result, numerical evidence, priority claim or subject-specific assumption is preloaded. IDs are local to this repository; external statements require explicit citations.

## First research prompt

`Codex (Sol 6.1 xhigh): New topic: define the Padua campaign around <research question>, with <scope and constraints>. Establish the literature baseline, success criteria and cheapest decisive first tests before developing new ideas.`

No automation, CI or repository permissions are configured by this scaffold.
