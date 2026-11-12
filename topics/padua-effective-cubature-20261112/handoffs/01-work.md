# Handoff 01 — padua-effective-cubature-20261112 — effective Theorem A, and the Padua Lebesgue-constant corollary

- Status: open
- Previous handoff: none (new topic)

- Next agent / model / effort: **Claude** (another Claude thread, as AC requested).
  - Orchestrator and mathematics: Opus 5.5 xhigh.
  - Code, numerical LP and certificate checkers: Sonnet 5.5 high.
  - Mechanical work: Sonnet 5.5 medium.
  - Independent subagent checks: a separate Opus 5.5 instance.
  - Per agents/claude/CLAUDE_ROLES.md, AC's standing preference is development subagents on Sonnet and reviews on Opus.
- Role: orchestrator and developer
- Branch: claude/padua-effective-cubature-20261112
- Input head SHA: `b5388c2` (main, PR #33 merged; this branch adds only BRIEF.md, this handoff, LOG and the results stub)
- Main / base: `b5388c2` (PR #29 rules)
- Stage: WORK
- Written by / date: Claude, claude-opus-5-5 · 2026-11-12

## Task

Read [BRIEF.md](../BRIEF.md) first. It holds the Theorem A proof chain with its non-effective steps (§1.2), the constraints on any effective statement (§1.3), routes E1–E3 (§1.4–1.6), the target outcomes (§1.7), and the exact corollary to register (Part 2).

### C0 — register the Lebesgue-constant corollary (first, small)

1. Write one theory file in THEORY-template form, `theory/lebesgue-constant-corollary.md`, with provisional ID `PD-T?effective-cubature-claude-01`, stating BRIEF §2.1 (i)–(ii) exactly. Include:
   - status-by-part: PROVED, assembled from the merged dependencies of BRIEF §2.2, with no new mathematics;
   - the dependency list;
   - the priority wording of BRIEF §2.3;
   - a dated note that PR #27, once merged, extends (i) to 2–40 and makes the threshold effective.
2. Run the novelty gate and record it as a corollary assembly.
3. An independent Opus subagent checks the statement against the four dependency files, verifying that the conventions, constants and quantifiers match.

### E1–E3 — make Theorem A effective (main work)

**E1 (Delsarte LP and the Turán problem for the octahedron), main route.**
1. **Literature first.** Search for the known value or bounds of Turán's constant T(2O) for the octahedron, or a general convex-body result: Kolountzakis–Révész, Arestov–Berdysheva, Gorbachev, Ivanov and others. Record LIT entries after fulltext reads.
2. Then compute the finite LP optimum ρ_n = max f(0)/c₀ / m_n for n = 2…16 or more, numerically, in both the torus-lift and the direct-cube forms.
3. **Decision:**
   - If T(2O) > |O| is known, or provable, and ρ_n stays bounded above 1, derive an explicit γ and n₀ with all finite-n error terms explicit.
   - If T(2O) = |O|, record that the LP cannot give a fixed fraction (a scoped negative). Try one strengthening from BRIEF §1.4 (Cohn–Elkies forbidden differences from separation, or keeping the leverage identity) before stopping E1.

**E2 (quantitative compactness), parallel or fallback.** Quantify D1-02/D1-03 and prove an explicit quantitative non-spectrality of O (BRIEF §1.5). One bounded attempt. Explicit but tiny constants count as success.

**E3 (finite certificates), parallel, Sonnet for code.**
- Certified finite LP bounds L_n ≤ N for every positive rule with nodes in the closed cube, n = 4, 5, …, as far as is affordable.
- Before any exclusion claim, the pipeline must:
  - reproduce Fisher's bound;
  - be consistent with the D3 package at n = 3;
  - be consistent with the lattice complement table.
- The target is the exact list of degrees with a positive package.

## Gates (write them in `gates.md` before running)

- **Q0, replay.** Verify the D1-01 identities on the committed controls (`topics/padua-3d-20261106/evidence/fd1-controls.json` and its producer), and the D3 certificate at n = 3, from committed code. **Kill:** mismatch.
- **Q1, LP sanity.** The LP code with f = |D_n|² must return exactly m_n. Its optimum must never exceed the true minimum node count of a known positive rule, using the D3 rule (n = 3) and the lattice minima (BRIEF §1.3) as upper references. **Kill:** violation, which means a bug.
- **Q2, E1 asymptotic screen** (MEASURED). Pre-register: "a fixed-fraction route is promising if the numerical LP optimum ρ_n is ≥ 1.02 at every n ≥ 8 tested and non-decreasing over the last four degrees". **Kill (fixed-γ by plain LP):** ρ_n − 1 decreasing like 1/n or faster over n ≤ 16, or a literature or proof result T(2O) = |O|.
- **Q3, certificate acceptance.** A finite exclusion at degree n needs:
  - an exact rational nonnegative dual certificate, with nonnegativity proved, for example by an SOS or Fejér–Riesz certificate, or by exact sign analysis on a certified mesh with a derivative bound;
  - a committed checker;
  - an independent rerun on a separate code path.

  It must not contradict D3 at n = 3.

## Budget and parallelism

- Up to 10 rounds each for E1 and E3, and up to 6 for E2. C0 is one round.
- Run in parallel after Q0, with disjoint file ownership. Only the orchestrator writes LOG, `rounds.md`, `gates.md`, results and the report.
- A round ends in a pushed LOG entry. A direction continues only after recorded progress; two empty rounds end it.
- AC may raise the budget.

## Read first

- AGENTS.md, agents/WORKFLOW.md, agents/claude/CLAUDE_ROLES.md at the branch head; record the SHA.
- [BRIEF.md](../BRIEF.md) and every file it links.
- `topics/padua-3d-20261106/`: report.md, final-narrowed-report.md, final-d1/ (all), final-d3/, theory/r08-lattice-complement.md, theory/r08-lattice-higher.md, audit-05.md, response-05.md, final-check/d1-audit.md.
- For C0:
  - the records of PD-T101, PD-T229 (`topics/padua-argmax-alln-20261101/theory/gated-codex-15-eventual-global-argmax.md`), PD-T246 and PD-T269–T271 (`topics/padua-lebesgue-followups-20261103/theory/t4-0*.md`);
  - `topics/padua-literature-20261103/p1-comparison.md`.
- PROOF_STATUS rows for the above, and the PR #33 rows (Theorem A and its lemmas). IDEAS entries from PR #33 (the D1 candidates) and IDEA-206.
- `literature/INDEX.md`: LIT-659 to LIT-669 and their records.

## Scope limits

- **Where to write.** Only inside `topics/padua-effective-cubature-20261112/` and `results/padua-effective-cubature-20261112.md`.
  - Do not edit merged files.
  - At PR preparation, edit the shared registries directly; the readiness check reviews them by diff.
  - Do not write to PR #27's branch or any other open branch.
- **IDs.** Provisional IDs `PD-T?effective-cubature-claude-NN`, and likewise for PD-N, IDEA and LIT. Reserve final ranges when first needed (normally at PR preparation), and recheck at readiness.
- **Statuses follow AGENTS.md.**
  - Numerical LP optima and fits are MEASURED.
  - An explicit γ or n₀ needs a written proof with every constant explicit.
  - A finite exclusion needs an exact certificate, a committed checker and an independent rerun.
  - Never infer a constant from a fit.
- **Storage:** commit code and small evidence, normally under 16 KiB per file. Larger certificates go to cold storage via `tools/cold_storage.py`, with `cold-storage.json` and `COLD_STORAGE.md`.
- **Compute.** Sandbox: up to 6 h wall per run and about 48 h of cumulative CPU. Ask AC before using Syvert. If you do, build packs in the "Syvert run pack" structure of the bridge handoff: `git show origin/codex/padua-argmax-bridge-20261105:topics/padua-argmax-bridge-20261105/handoffs/01-work.md`.
- **Literature.**
  - Open any legally accessible literature without asking per link (AC standing authorization).
  - Cite only after a fulltext read, and record LIT entries.
  - Give AC clickable DOI or journal links for anything unreachable.
  - Never commit third-party PDFs or extracts (the repo is public). Do not bypass captchas or bot checks.
- **Commits** are authored as Andrey Chesnokov <aacchhee@gmail.com>, with trailers `Agent: Claude` and `Model: <exact model and effort>`, plus the session's Co-Authored-By and Claude-Session lines. Never commit to main, merge, force-push, create tags or touch .github/. Only AC merges.

## Acceptance and outputs

- **Files.**
  - `LOG.md`, `plan.md` and `rounds.md`.
  - `gates.md`, with Q0–Q3 verdicts and pre-registrations.
  - `attempts/E1…E3.md` and `novelty-gate-*.md`.
  - `theory/` records: the C0 corollary, each lemma or bound, each certificate theorem, each PD-N.
  - `independent-checks*.md`, `evidence-manifest.json`, `literature-effective.md`.
  - `results/padua-effective-cubature-20261112.md`, kept current, and `report.md`.
- **Pushes and PR.** Push at every gate and round boundary, and at least every ~10 minutes while something has changed. Open a draft PR early.
- **The report contains:**
  - the C0 corollary as registered;
  - the Q0–Q3 verdicts;
  - the Turán-constant finding;
  - any explicit γ and n₀;
  - certified finite bounds and the degree list;
  - what remains OPEN;
  - a short paragraph on how this changes the 3-D note (`topics/padua-3d-20261106/paper-note-draft.md`).
- **Closing.** When done, commit the outputs. Then, in a following commit, set this status to `done in <sha>` and open handoff 02 for the single substantive audit by **Codex, gpt-6-astra high or higher at its choice**: Codex audits Claude development. That audit reads the complete state/IDEAS.md if mechanisms or novelty claims are present. Reply to AC only with `Codex (gpt-6-astra high): Continue claude/padua-effective-cubature-20261112.`
