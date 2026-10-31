# Lanczos in two commuting variables — finite-precision theory, joint Ritz values and commuting extensions

- Branch: `claude/bivariate-lanczos-20261031` · Base: `d36722823441dc40c6e19d69a174459348dd309c` (origin/main) · Developer/orchestrator: Claude · Auditor: Codex (`gpt-6-astra`), PENDING
- Stage: WORK · Next: `Claude (Opus 5.5 xhigh): Continue claude/bivariate-lanczos-20261031.`
- Claims: none accepted; see [plan.md](plan.md) round ledger and [progress.md](progress.md).
- For the PR: one charter paragraph for this track in `state/CURRENT.md` (PR preparation only); final PD-T/PD-N/IDEA/LIT IDs via a shared ledger `topics/padua-batch-20261031/ALLOCATIONS.md` with `codex/charter-unisolvence-20261031`; merge `origin/main` first if the charter PR has merged.
- Open for AC: see bottom section.

## 2026-10-31 — Claude orchestrator (configured model `claude-opus-5-5`; reasoning effort not exposed by the runtime)

### Start and authority

- Rules read at `d36722823441dc40c6e19d69a174459348dd309c` (AGENTS.md, agents/WORKFLOW.md, agents/claude/CLAUDE_ROLES.md). The requested branch did not exist on the remote; it was created from that commit (= `origin/main`). Role: orchestrator; Claude develops, Codex audits.
- `origin/main` fetched: `d36722823441dc40c6e19d69a174459348dd309c`. Parallel branch `origin/codex/charter-unisolvence-20261031` at `59468bd52666b9cdc2749eccffaef194f26ead1b` (inspected read-only: it writes the charter, `state/CURRENT.md`, `state/IDEAS.md`, `literature/CORPUS.md`, `literature/INDEX.md` and 29 `literature/records/*`). Its literature keys are reused for shared sources so the two PRs merge into one record per source; overlap is reconciled at PR preparation.
- AC instructions that override default gate wording (as AGENTS.md allows): Step 0 literature baseline instead of a full novelty gate; exploration may precede a full duplicate screen; each candidate records closest predecessor and kill test and gets a prior-art check plus an independent adversarial reconstruction (separate Opus agent) before acceptance; labelled idealized scaffolding only; ≤10 rounds per direction (≤20 with written justification); ≤2 substantive directions at a time; floating-point experiments are MEASURED only; paywalled load-bearing source → pending-reference. Out of scope: finite-field unisolvence; bivariate moments→OP complexity; 3D Padua; MZ constants.
- Git: commits authored as Andrey Chesnokov <aacchhee@gmail.com> (repo-local config) with `Agent:`/`Model:` trailers. The session's `add_repo` request for push access was refused by the environment's permission classifier; the public repository is readable through the session proxy. Push is attempted at each checkpoint; if refused, work stays committed locally and the obstruction is reported to AC. 21:41 local: AC approved writing to the repo; push access attached; branch pushed at `5685668`.

### Inputs

- `padua_lanczos_inputs.zip`: SHA-256 `5498074f1547c7117a7167d31b7346462b381718b85e6644e75b7f0d0d7ecf5c`, 163906 bytes; unpacked to `sources/padua_lanczos_inputs/`; `sha256sum -c SHA256SUMS.txt` 23/23 OK. Not committed (see [sources/README.md](sources/README.md)).
- AC's computer linked; folder `C:\Users\andreyac\Downloads\padua` granted. Staged (read only, never committed): the seven named fulltexts from `papers\` and `RESULTS.md`.

### Model allocation (planned; actual models/efforts recorded per subtask below)

| Work | Model, effort |
|---|---|
| Literature extraction from local fulltexts and notes | Sonnet 5.5 high |
| Reproduction of input code, experiments | Sonnet 5.5 high |
| L1/L4 and L3 mathematics | Opus 5.5 xhigh |
| L5 side direction (experiments + routine analysis) | Sonnet 5.5 high |
| Independent adversarial reconstruction / prior-art check | separate Opus 5.5 xhigh agents |
| Mechanical integration | Sonnet 5.5 medium or orchestrator |

Subagent effort is set from the agent definition and is not independently exposed to the orchestrator; where the runtime does not confirm it, the log says "requested".

### Step 0 (complete 2026-10-31)

- Subtasks: (i) fulltext records, Claude Sonnet 5.5 high (requested), 65 tool uses, ~14 min — 7 records, LIT?…-101–162, complete fulltext coverage (page images checked where text layer garbled); PDFs/text kept in scratchpad only. (ii) notes baseline, Claude Sonnet 5.5 high (requested), ~14 min — 64 records, LIT?…-001–077, 16 web metadata calls (logged in lit/search-log.md), CORPUS/INDEX rebuilt, state/IDEAS.md seeded (48 candidates: 15 active, 12 settled-background, 15 deferred, 6 out-of-scope), baseline-candidates.md. Orchestrator merged fulltext rows into INDEX/CORPUS.
- Corrections that affect interpretation of the frozen questions are in plan.md History.
- Novelty gate (AC Step 0 override): registry before seed was empty apart from the template text; the seed is not an acceptance or novelty verdict. Each direction records closest predecessors and kill tests per candidate.
- Checkpoints pushed: 8edbc69, bef4490.

### Direction launch (2026-10-31, after Step 0)

- L1+L4: Claude Opus 5.5, xhigh (requested); owns directions/L1, code/L1, theory files 1nn/4nn.
- L3: Claude Opus 5.5, xhigh (requested); owns directions/L3, code/L3, theory files 3nn.
- L5 (side): Claude Sonnet 5.5, high (requested); owns directions/L5, code/L5, theory files 5nn.
- L2 queued. Reproduction of inputs (Sonnet 5.5 high) still running; owns repro/.
- Each developer returns after ≤ 3 rounds; the orchestrator checkpoints, then commissions prior-art checks and independent adversarial reconstructions (separate Opus 5.5 xhigh agents) before any acceptance.

## Runs needed

(none yet; directions add exact commands)

## Open for AC

- (resolved 2026-10-31 21:41) Push access attached after AC approval.
