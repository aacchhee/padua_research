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

### AC message 2026-10-31 22:12 — information from the parallel unisolvence topic

- Source: `codex/charter-unisolvence-20261031` at `eb7bdcdf3a587dd49ea9d692b1d27c7af053fe64` (verified present on origin; Stage AUDIT, Claude audit pending). PD-T001 `tracks/unisolvence/theory/u1/odd-characteristic-criterion.md` (det(V_e)²·∏w_i(X)w_j(Y) = 2^{−N}∏_{r=1}^{m+1}Δ_r(X)Δ_r(Y)); PD-T003 `tracks/unisolvence/theory/u1/kernel-cubature-corollary.md` (L_X⊗L_Y = 2Σ_{S_e} w_i(X)w_j(Y)f for total degree ≤ 2m). Status: developer PROVED with supplementary Astra reconstruction, **not accepted** — cited by branch/SHA/ID only, never as dependencies. PD-N001/PD-T002 (char 2, other fields) irrelevant here. FYI: `codex/mz-constants-20261031` at `33bf9e6` (out of scope; no action).
- Correction applied: Harris–Simanek needs ordered (monotone) nodes; recorded in plan Benchmarks, `literature/records/harris-simanek-2021.md` and IDEA?…-038 rows (state/IDEAS.md, baseline-candidates.md). Orchestrator check: `tracks/bivariate-lanczos/code/inputs/harris_simanek_check.py` builds all node lists monotone (random: sorted descending; warped: cos of a monotone map of [0,π]; Padua: Chebyshev–Lobatto descending) — usable as a benchmark. Cao–Ghimire–Wang 2022 (HS Conjecture 3) recorded UNVERIFIED.
- Integration: active rounds not interrupted; the checkerboard family is passed to L1/L3/L5 when each returns, and to L2 at launch.

### L1 R01–R03 returned; reviews launched (2026-10-31 ~22:55 local)

- L1+L4 developer (Opus 5.5 xhigh, requested; 119 tool uses, ~61 min) completed R01–R03; committed `b84af76`. Claims PD-T?…-101–109, -401 and PD-N?…-101, -102 (statuses in [progress.md](progress.md)). Developer disclosures: post-hoc change to the R01 decision rule (completion degree N = M excluded; "tracks" label needs ≥ 2 informative degrees); kill criteria for IDEA?…-106/-107 written after the runs (R01, R03 criteria written before).
- Remote branch had advanced by `48f7a02` (Codex MZ orchestrator propagated the shared batch ledger `topics/padua-batch-20261031/ALLOCATIONS.md`; ledger only). Merged into this branch (`1063469`) without rewriting history. Ledger states: charter PR #2 merged into main at `08fafe6`; allocation owner = Codex MZ orchestrator; this branch must merge charter/MZ-bearing main and obtain a disjoint reservation from that owner before final IDs. main not yet merged here (deferred to PR preparation, as AC instructed).
- Launched: independent adversarial reconstruction of L1 R01–R03 (separate Claude Opus 5.5 xhigh agent; owns reviews/L1-reconstruction-01.md, code/review_L1/); prior-art check of mechanisms (a)–(f) (separate Claude Opus 5.5 high agent; owns reviews/L1-prior-art-01.md). L1 developer resumed for R04+ with reviewed files frozen and the checkerboard benchmark passed on.
- RESULTS.md on AC's machine (`C:\Users\andreyac\Downloads\padua\RESULTS.md`): campaign entry appended (re-staged after a newer external edit; prior content preserved).

### AC authorization 2026-10-31 23:00

- AC authorized reading all related literature and papers anywhere on the net. Passed to all running agents (L1, L3, L5, L1 reconstruction, L1 prior-art). Launched an online resolution pass for the pending-reference load-bearing sources (Claude Sonnet 5.5 high, requested; owns those record files, their INDEX/CORPUS rows and a search-log section). Public-repo rule unchanged: no fulltexts or long extracts committed.

### L3 R01–R03 returned (2026-10-31 ≈ 23:05 local)

- L3 developer (Opus 5.5 xhigh, requested; 100 tool uses, ~73 min) completed R01–R03; committed `a5b993d`. Claims PD-T?…-300–309, PD-N?…-301, -302 (statuses in progress.md). Scope decision: literal L3-Q1 trivial; exact-representation reading answered (plan History). Protocol finding: STATUS.md timestamps for R02/R03 were in the future (estimates) — annotated, not edited.
- Next: independent adversarial reconstruction incl. independent reruns of the exact certificates (needed before PD-T?…-306 and PD-N?…-301 can move from CONDITIONAL), a prior-art check, and L3 R04.

### L1 prior-art check returned (2026-10-31)

- Claude Opus 5.5 high (requested), separate agent; report [reviews/L1-prior-art-01.md](reviews/L1-prior-art-01.md). WebFetch summarises pages (not verbatim); locators to be re-checked before citation.
- Verdicts: (a) non-product loss growth — **partially known**: Zaccaron 2014 Tables 2.1–2.2 (p. 16) already show geometry-dependent loss for the HL-type window recurrence (rotated square 0.74 at degree 60; quadrangle geometric growth from degree ~10). The bare observation is not new and must be cited; the product/non-product dichotomy, "before Ritz convergence" and "univariate on product measures" were not found. (b) row-selection: stacked overdetermined system and non-unique left inverses classical (Xu survey arXiv 1701.02709 §2.2; Liu–Narayan 2023 Thm 3.1; Olver–Townsend–Vasil 2019 §2.3); link to instability not found. (c) two-relation remedy: algorithmic predecessor Liu–Narayan SISC 45(3) 2023 (block Stieltjes, all coordinates, eigen/SVD completion); comparison not found. (d) ω-recurrence: template Simon 1984; two-operator version not found. (e) L4: weaker informal statements (Zhu–Nakatsukasa §3; Hokanson §2). (f) only the HL observation.
- **Must read before any priority claim:** Barrio–Peña–Sauer, J. Approx. Theory 162 (2010) 407–420 (three-term recurrence evaluation of multivariate OPs; metadata only — ScienceDirect blocked) — potential kill for (b)/(c); Sinha 2026 beyond §7.1 (relation (54) injection term may overlap (e) and PD-T?…-103).
- Record fixes queued for consolidation: liu-narayan-2023 author Zexin Liu; hokanson-2020 title ("Multivariate rational approximation using a stabilized Sanathanan–Koerner iteration"); zaccaron-2014 "two inconsistent reports" are rows of the same Table 2.1 (no conflict); 7 new and 6 upgraded records recommended in the review.

## Runs needed

(none yet; directions add exact commands)

## Open for AC

- (resolved 2026-10-31 21:41) Push access attached after AC approval.
