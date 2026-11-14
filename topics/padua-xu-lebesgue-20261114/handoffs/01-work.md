# Handoff 01 — padua-xu-lebesgue-20261114 — Xu-points Lebesgue conjecture (X1) and Morrow–Patterson lower bound (X2)

- Status: done in 971beb79b8edb93835b20d1b9148e93d4ba3aba4
- Previous handoff: none (new topic)

- Next agent / model / effort: **Claude**. The orchestrator and the researcher both run on **Fable 5.2 xhigh**. Per-round downgrade to Opus 5.5 xhigh is allowed (BRIEF §4).
  - Code and certificate checkers: Sonnet 5.5 high. Mechanical work: Sonnet 5.5 medium.
  - Independent subagent checks: a separate Opus 5.5 instance.
- Role: orchestrator and developer
- Branch: claude/padua-xu-lebesgue-20261114
- Input head SHA: `99a9b1d161e41a80c4fd425b63022c681fbe8779` (main, PR #34 merged; this branch adds only BRIEF.md, this handoff, LOG and the results stub)
- Main / base: `99a9b1d` (PR #29 rules)
- Stage: WORK
- Written by / date: Claude, claude-opus-5-5 · 2026-11-14

## Task

Read [BRIEF.md](../BRIEF.md) first. It holds the problem statements, the sources to verify, how to reuse PR #27, the target outcomes and AC's model and round rules.

### Setup (round 0, one round, counted for neither direction)

1. **Model check.** Confirm that Fable 5.2 is available to this thread. If it is not, stop before any mathematics, tell AC, and propose a substitute (BRIEF §4).
2. **Rules.** Record the rules SHA. Record in LOG the two AC rulings of 2026-11-14: Fable for mathematical development, and an Opus 5.5 xhigh Claude auditor in place of Codex.
3. **Literature reads**, recording LIT entries:
   - Xu 1996 (JAT), Bos–De Marchi–Vianello 2006 (JAT), and the missing sections of BCDMV 2006 (§§1–2 and 4, the named gap in its record, which justifies the re-read);
   - Beberok–Białas-Cież–De Marchi 2026 (arXiv 2412.14595), to upgrade LIT-378;
   - Morrow–Patterson 1978 and Caliari–De Marchi–Vianello 2005, as far as needed for definitions.
   - Run the documented forward-citation search (BRIEF §3).
4. **Novelty gate** for X1 and X2 (relaxed scan; `novelty-gate-X1.md`, `novelty-gate-X2.md`).
5. **Pre-register** gates G0–G5 in `gates.md` before running anything (see Gates).

### X1: Xu points (up to 10 rounds)

1. Fix the definitions for both parities (BRIEF §1.1), including which vertices are nodes. Restate Conjecture (17) precisely. Implement the Xu interpolant exactly (rational arithmetic or certified high precision); this is G0.
2. Run the G1 screen: argmax location for n = 2 up to about 60. The aim is to decide early between a proof programme and a counterexample.
3. **If G1 supports the vertex conjecture:**
   - prove the corner value in closed form and its sharp expansion (G2);
   - then localization and an explicit onset;
   - then finite certificates below the onset (G3).

   Follow PR #27's architecture (BRIEF §1.3). Re-prove its lemmas for the Xu kernel rather than citing unmerged ones.
4. **If G1 finds a non-vertex maximum:** certify it (G1-kill path), register a PD-N, then study the corrected conjecture: the true argmax and the leading constant.

### X2: Morrow–Patterson (up to 10 rounds; may run in parallel with X1 after setup)

1. Implement the MP interpolant exactly (G0). Reproduce the BBDM / CDMV numerics.
2. Locate numerically where Λ_MP is attained and where λ grows like n² (MEASURED).
3. Prove Λ_MP(n) ≥ c·n² with explicit c and n₀ (G4). Then attempt the sharp constant, the argmax and the MPX variants (BRIEF §2.2).

## Gates (write them in `gates.md` before running)

- **G0 — implementation sanity**, for each direction.
  - For n ≤ 12: exact interpolation at the nodes, unisolvence, the cardinality formula, and Λ values matching the published numerics.
  - Two independent code paths must agree: an exact or rational kernel formula, and a direct Lagrange basis by solving the Vandermonde system in exact arithmetic.
  - **Kill:** an unresolved mismatch.
- **G1 — X1 argmax screen** (MEASURED).
  - Pre-register the grid, the refinement and the tolerance.
  - "Vertex conjecture supported" means: at every tested n, max over non-vertex candidates < min over the non-node vertex values, with a relative gap reported per n.
  - **Kill (of the argmax part of (17)):** a point whose interval-certified λ value exceeds every vertex value at some n. This is then a PROVED negative, with a committed checker and an independent rerun on a separate code path.
- **G2 — corner expansion acceptance.**
  - A written proof of the closed form and of the expansion, with every constant explicit and the remainder bounded for every n ≥ some n₂.
  - The numerics must agree with the closed form to high precision for n ≤ 200. The agreement is MEASURED and is a check only.
- **G3 — argmax certificates.** A finite-degree argmax claim needs:
  - an exact or interval certificate for each degree;
  - a committed checker;
  - an independent rerun on a separate code path.

  An all-n claim needs a written analytic tail with an explicit onset, plus G3 coverage of every degree below it.
- **G4 — X2 lower bound.** A written proof with explicit c and n₀. The numerical location of the extremal point is MEASURED and serves only as a guide.
- **G5 — scope honesty.** Numerical fits never set a constant. "Eventually" and "for every n" are kept apart. Any use of an unmerged PR #27 lemma makes the claim CONDITIONAL (BRIEF §1.3).

## Budget, compute and parallelism

- **Rounds.** Up to 10 rounds each for X1 and X2, as BRIEF §4 says. Record the researcher model of each round in `rounds.md` before it starts.
  - Two consecutive empty rounds end a direction. AC may raise the budget.
- **Parallelism.** Run X1 and X2 in parallel after setup, with disjoint file ownership. Only the orchestrator writes LOG, `rounds.md`, `gates.md`, results and the report.
- **Compute.** Sandbox: up to 6 h wall per run and about 48 h of cumulative CPU.
  - The Syvert pre-approval was for the argmax bridge only, so ask AC before using syvert1 or syvert2 here.
  - If AC approves, build packs in the bridge's A/B/C run-pack structure: `git show origin/codex/padua-argmax-bridge-20261105:topics/padua-argmax-bridge-20261105/handoffs/01-work.md`, section "Syvert run pack". Do not overengineer.

## Read first

- AGENTS.md, agents/WORKFLOW.md, agents/claude/CLAUDE_ROLES.md at the branch head; record the SHA.
- [BRIEF.md](../BRIEF.md).
- `literature/records/bcdmv-computing-2006.md` (LIT-486), and the LIT-378, LIT-388 and LIT-302 rows of `literature/INDEX.md`.
- `state/IDEAS.md`: IDEA-047 and IDEA-048, plus the relaxed scan.
- PR #27 entry points as listed in BRIEF §1.3, read with `git show` from the bridge branch.
- Main records for conventions: PD-T101, PD-T229, PD-T246, PD-T269–T271 and PD-T674. Use `PROOF_STATUS.md` to find their files.

## Scope limits

- **Where to write.** Only inside `topics/padua-xu-lebesgue-20261114/` and `results/padua-xu-lebesgue-20261114.md`.
  - Do not edit merged files.
  - Do not write to PR #27's branch or any other open branch.
  - Shared registries are edited directly at PR preparation and reviewed by diff (PR #29 rules).
- **IDs.** Provisional IDs `PD-T?padua-xu-lebesgue-20261114-claude-NN`, and likewise for PD-N, IDEA and LIT. Reserve final ranges when first needed (normally at PR preparation), and recheck at readiness.
- **Statuses follow AGENTS.md.**
  - Screens and fits are MEASURED.
  - Certificates need exact or interval arithmetic, a committed checker and an independent rerun.
  - Every proved result gets a THEORY-template file in `theory/` when it is produced.
- **Storage.** Commit code and small evidence, normally under 16 KiB per file. Larger outputs go to cold storage via `tools/cold_storage.py`, with `cold-storage.json` and `COLD_STORAGE.md`.
- **Literature.**
  - Open any legally accessible literature without asking per link (AC standing authorization).
  - Do not bypass captchas or bot checks.
  - Never commit PDFs or extracts; the repository is public.
- **Commits** are authored as Andrey Chesnokov <aacchhee@gmail.com>, with trailers `Agent: Claude` and `Model: <exact model and effort>`, plus the session's Co-Authored-By and Claude-Session lines.
  - Never commit to main, merge, force-push, create tags or touch .github/. Only AC merges.

## Acceptance and outputs

- **Files.**
  - `LOG.md`, `plan.md`, `rounds.md` and `gates.md`, with G0–G5 pre-registrations and verdicts.
  - `literature-xu-mp.md`, `novelty-gate-X1.md` and `novelty-gate-X2.md`.
  - `attempts/X1-*.md` and `attempts/X2-*.md`.
  - `theory/`: one record per lemma, theorem and PD-N.
  - `code/`, `evidence-manifest.json` and `independent-checks-*.md`.
  - `results/padua-xu-lebesgue-20261114.md`, kept current, and `report.md`.
- **Pushes and PR.** Push at every gate and round boundary, and at least every ~10 minutes while something has changed. Open a draft PR early.
- **The report states:**
  - the precise form of Conjecture (17) and its verdict: proved, partially proved with exact scope, or refuted;
  - the Xu corner expansion;
  - the MP lower bound and any sharp constant;
  - the G0–G5 verdicts;
  - what remains OPEN;
  - a short paragraph on whether a manuscript is warranted, and in what relation to the PR #27 paper.
- **Closing.**
  1. Commit the outputs.
  2. In a following commit, set this status to `done in <sha>` and open handoff 02 for the single substantive audit by **Claude, Opus 5.5 xhigh** (AC ruling 2026-11-14), in a fresh thread distinct from the developer. That audit reads the complete `state/IDEAS.md` if mechanisms or novelty claims are present.
  3. Reply to AC only with `Claude (Opus 5.5, xhigh): Continue claude/padua-xu-lebesgue-20261114.`
