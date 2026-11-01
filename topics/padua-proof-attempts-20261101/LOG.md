# First proof attempts on programme-ideas open targets

- Branch: `codex/padua-proof-attempts-20261101` · Base: `cadb35066160e466cb1704b9791ad6f374446422` · Developer: Codex · Auditor: Claude (Opus 5.5 xhigh), pending
- Stage: WORK · Next: `Claude (Opus 5.5 xhigh): Audit codex/padua-proof-attempts-20261101.`
- Claims: A1 PROVED in `theory/proof-attempts-codex-01-padua-corner.md`; B5 active; A5-partial queued. Local theory IDs only.
- For the PR: draft against `claude/programme-ideas-20261031`; no final IDs, shared registry edits, base-file edits, main merge or PR merge.
- Open for AC: none needed for authorized development; independent Claude audit remains a handoff.

## 2026-11-01 — Codex, requested gpt-6.1-sol xhigh

- Rules read in full at `cadb35066160e466cb1704b9791ad6f374446422`: AGENTS.md, agents/WORKFLOW.md, agents/codex/CODEX.md. Root's runtime-resolved model/effort is not separately exposed. No ultra allocation.
- Base SHA: `cadb35066160e466cb1704b9791ad6f374446422` (PR #6 head). Fetched main: `9739a0c56b7a3976422ce60a8441bfbbfd6554df`. PR #6 queried through GitHub connector: open, draft, unmerged. Main was not merged, per AC.
- Clean starting checkout: local `work` at `07c5f5465d6de306aa81dbe8ca1f615295163864`; preserved as its branch. Created requested topic branch from pinned programme head.
- Setup commands: `git fetch origin main claude/programme-ideas-20261031`; `git fetch origin refs/heads/claude/programme-ideas-20261031:refs/remotes/origin/claude/programme-ideas-20261031`; `git switch -c codex/padua-proof-attempts-20261101 cadb35066160e466cb1704b9791ad6f374446422`. First default-sandbox fetch failed to connect to the session proxy; the supported explicit network permission succeeded. Read cloud runtime/networking skill and enforced policy; no credentials printed or overridden.
- Input scope: authoritative OPEN_TARGETS; theory programme-ideas-claude-01/-04/-06/-N04; decisive-gen4-2 with response notes; audit-01 A1 and proposal-review; all named reuse code, t3_maxima.json and t3_certify.log. Original inputs remain pinned and untouched. Source identities will accompany the evidence manifest.
- Subtasks: `/root/a1_develop` develops only A1 in its allocated new files. `/root/input_review` reviews inputs/gate, may write only inputs-review.md. Both inherit the requested allocation; no independent runtime metadata receipt. Root alone controls Git. Neither is the required Claude audit.
- Novelty gate: full state/IDEAS.md heading/alias/summary and obstruction/disposition review; literature/INDEX.md; searches `corner`, `rhombus`, `Dirichlet`, `commutant`, `degenerate`, `absolute.cardinal`, IDEA-047/048/069 across state, literature, theory and programme candidate records. Closest entries: programme IDEA-17 (same corner/geometry project), IDEA-08 (pattern structure); charter IDEA-047 (Morrow–Patterson bound, different node family), IDEA-048 (Padua maxima), MZ IDEA-069 / PD-N005 (failed L1 column domination, different norm mechanism). This work attempts exact proofs of supplied targets; no renamed mechanism or literature-priority claim. Detailed receipt pending inputs-review.md.
- Kill criteria and ordering: [plan.md](plan.md). A1 currently active; B5 and A5 have not started.
- Environment: Python 3.12.14, SymPy 1.14.0, NumPy 2.3.5, SciPy 1.17.0; managed Linux; no Windows bridge exposed.
- Latest pushed checkpoint: first A1 checkpoint prepared below; commit identity is in Git history.

### Ordered target checkpoint: A1 complete, B5 starts

- A1 done: written all-n discrete-cosine Gram and Fourier-rhombus proof, including n=1 and removable sine singularities. Primary CDMV 2008 eqs. (1),(3),(6a–c) checked by developer; the task's even checkerboard is named the third family there. No coordinate/parity definition changed. Bos et al. 2006 Theorem 2 orientation and normalization also checked as LITERATURE. Source coverage is limited to named statements, never inherited proof.
- Executed developer command: `python topics/padua-proof-attempts-20261101/code/a1_exact_check.py > topics/padua-proof-attempts-20261101/outputs/a1_exact_check.json`. All 332 corner-cardinal comparisons and six universal Laurent coefficient identities pass in exact SymPy arithmetic for n=1,…,6.
- `/root/input_review` actually executed the same command separately to `outputs/a1_independent.json`, inspected the checker and written proof, and found no issue within its declared scope. This is a supplementary check, not the Claude audit; see independent-checks.md for hashes and source-reading limits.
- Root read the complete A1 proof and code; normalization, parity split and singular limits checked. A1 stops on its done criterion; no PD-N or failed mathematical route.
- B5 starts only after A1 written proof and checks were saved. `/root/a1_develop` now owns new `attempts/T-B5.md`, `theory/proof-attempts-codex-02-generic-commutant.md`, `code/b5_*`, `outputs/b5_*`. Root proposed the distinct-x/cyclic-constant-vector route, which gives an all-degree theorem and avoids disconnected-domain genericity problems. The supplementary reviewer checked that route read-only. The exact finite-witness code remains to be written/run. A5 has not started.

## Runs needed

- Required independent Claude audit, after development and draft PR: `Claude (Opus 5.5 xhigh): Audit codex/padua-proof-attempts-20261101.`
- AC's computer is not reachable through available tools. Intended local working-track entry: `C:\Users\andreyac\Downloads\padua\results\padua-proof-attempts-20261101.md`. Deliver this topic's final statuses, evidence commands and audit prompt there when a bridge is available. Do not touch RESULTS.md before PR preparation, and do not write another topic's section.
- If an essential output exceeds the user limits, archive only to `C:\Users\andreyac\Downloads\padua\cold_storage\padua-proof-attempts-20261101\` with a COLD_STORAGE manifest when a bridge is available; otherwise record the specific run here. No large output currently planned.
