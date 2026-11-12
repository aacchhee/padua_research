# Effective Theorem A (positive cube cubature excess) and the Padua Lebesgue-constant corollary: log

- Branch: `claude/padua-effective-cubature-20261112` · Base: main `b5388c2` (PR #33 merged) · Developer: Claude · Auditor: Codex (gpt-6-astra)
- Stage: WORK · Open handoff: [handoffs/01-work.md](handoffs/01-work.md) (in progress, session 1)
- Reserved final-ID ranges: none. Reserve when first needed (PR #29 rules).
- Claims (provisional IDs `PD-T?padua-effective-cubature-20261112-claude-NN`):
  - -01: C0 corollary, PROVED (assembly);
  - -02: Delsarte bound, PROVED;
  - -03: uniform Theorem A, PROVED with LITERATURE dependency on KLM 2025 Thm 6.4;
  - -04: 1/18 cap, PROVED;
  - -05: explicit γ, OPEN.

## 2026-11-12 — Claude, claude-opus-5-5 (configured; effort not exposed) — topic setup

- AC: "I'd like a Claude topic on making theorem A effective. You may also register Lebesgue corollary on the same. Open a branch, write a brief, another Claude thread will continue then."
- Rules read at `b5388c2` (unchanged since `76ba421`). Branch created from main `b5388c2`. Only BRIEF.md, handoff 01, this LOG and the results stub were added.
- BRIEF contents:
  - the Theorem A chain and its non-effective steps (D1-02 compactness, D1-03 and Greenfeld–Lev qualitative);
  - constraints: packages exist at n = 1, 2 (lattice) and n = 3 (D3), so n₀ ≥ 4;
  - routes: E1 Delsarte LP, whose asymptotics are Turán's problem T(2O), with γ_LP = T(2O)/|O| − 1 if positive; E2 quantitative compactness; E3 finite certificates;
  - the exact C0 corollary: the Padua Lebesgue constant equals Λ_c(n) for 2 ≤ n ≤ 32 and n ≥ N_*, with the unconditional three-term asymptotics.
- The Delsarte inequality M ≥ f(0)/c₀ and its Turán reformulation are Claude's derivation in the BRIEF, written as a plan and not a claim. The statements on known Turán results are Claude's recollection, marked "verify".
- No computation was run and no claim made.

## 2026-11-12 — Claude, claude-opus-5-5 (xhigh per AC prompt; effort not exposed) — session 1

- **Session setup.**
  - AC: "Claude (Opus 5.5 xhigh): Continue claude/padua-effective-cubature-20261112." AC then sent, mid-turn: "I authorize all writing to this branch."
  - The session harness had pre-created a different branch (`claude/padua-effective-cubature-9927nw`). Per AC's message, work is on the topic branch. Nothing was written to the harness branch.
  - Rules read at `39a4bf5` (branch head; AGENTS.md, WORKFLOW.md and CLAUDE_ROLES.md are unchanged since main `b5388c2`). Base main `b5388c2`. Role: orchestrator and developer.
- **Gates.** `gates.md` and `plan.md` were pushed at `0abf5e7` before any run.
- **Q0 PASS.** fd1 controls are identical; D3 certificate PASS; D3 cube-LP cap λ₃ ≤ 1.6358. Details in gates.md.
- **C0.**
  - The corollary record and novelty gate were drafted by a Sonnet 5.5 high subagent and committed at `69c4455`. They list ten discrepancies with the BRIEF, none changing content. Notably, n = 1 is excluded and Λ_c is defined in PD-T159/229.
  - PR #27's branch now claims the argmax for all n ≥ 2, which is more than the BRIEF says; this is noted only, not used.
  - An independent Opus check is running.
- **Literature (decisive).** Kolountzakis–Lev–Matolcsi, arXiv:2510.10172 (2025), read in full text.
  - (1) T(U) = 2^{−d}m(U) for symmetric convex bodies is a major open problem, and no non-Turán convex body is known. So BRIEF E1 as written, the plain LP ↔ T(2O), would require solving it.
  - (2) Their Thm 6.4: for a convex body A, D(Δ(A)) = m(A) iff A tiles. So the Delsarte constant satisfies D(int 2O) > 4/3.
- **New mathematics** (records in `theory/`, commit `0f1d797`).
  - The cubature LP admits the Delsarte relaxation, with high-frequency coefficients ≤ 0 (-02).
  - Continuous transference gives N ≥ (n−½)³ D(int 2O)/8 for every n. With KLM this yields Theorem A in uniform form, N ≥ (1+γ_A)(2n−1)³/48 with γ_A > 0 (-03). This is independent of D1-02/D1-03.
  - Cap: D(int 2O) ≤ 38/27, from the exact check of the Betke–Henk/Minkowski lattice, so γ_A ≤ 1/18 (-04).
  - Consequence: this route can exclude packages only for n ≥ 138 (exact integer check), so 4 ≤ n ≤ 137 need other methods.
  - S4's "lattice value 1/18" is reconciled.
- **Novelty gate.** `novelty-gate-E1.md`: one surviving variant (-01) and four deferred or pending candidates.
- **LP code.** The Sonnet 5.5 high subagent is running the torus plain and Delsarte LPs, the lattice references and the cube LP. Results go in `evidence/lp-*.json`.

## Runs needed

- Q0–Q3, C0 and E1–E3 as in handoff 01.
