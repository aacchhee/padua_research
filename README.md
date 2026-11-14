# Padua research

An independent research campaign owned by AC on algebraic unisolvence of structured bivariate interpolation sets over arbitrary fields, motivated by Padua points. The charter is in state/CURRENT.md; the first campaign and exact scope are in tracks/unisolvence/README.md.

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

The first campaign registers scoped proofs, measured checks, open targets and source dispositions. Claude audit-01 accepted the mathematical scope and classifications; response-01 records administrative resolutions and AC’s Windows-verification waiver. IDs are local; external statements retain explicit reading coverage, and no input-source proof or novelty claim is inherited.

## First research prompt

`Codex (Sol 6.1 xhigh): New topic: define the Padua campaign around <research question>, with <scope and constraints>. Establish the literature baseline, success criteria and cheapest decisive first tests before developing new ideas.`

No automation, CI or repository permissions are configured by this scaffold.

## Licence

Copyright (C) 2026 Andrey Chesnokov.

Everything in this repository — code, data, evidence, records and manuscript sources — is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version (SPDX `AGPL-3.0-or-later`). It is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License in [LICENSE](LICENSE) for more details.

Exceptions: material by others keeps its own terms. These are
- the SIAM LaTeX macros `tracks/mz-constants/paper/siamart251216.cls` and `tracks/mz-constants/paper/siamplain.bst`, under SIAM's distribution conditions stated in their headers;
- short quotations from published sources in the literature records, which remain their authors'.

Third-party code used by the campaigns is referenced by URL and hash and is not committed (see the topics' `external-code.md` files).

