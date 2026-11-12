# Effective Theorem A (positive cube cubature excess) and the Padua Lebesgue-constant corollary: log

- Branch: `claude/padua-effective-cubature-20261112` · Base: main `b5388c2` (PR #33 merged) · Developer: Claude · Auditor: Codex (gpt-6-astra)
- Stage: AUDIT (pending) · Open handoff: [handoffs/02-audit.md](handoffs/02-audit.md) (Codex); handoff 01 done
- Reserved final-ID ranges: none. Reserve when first needed (PR #29 rules).
- Claims (provisional IDs `PD-T?padua-effective-cubature-20261112-claude-NN`):
  - -01: C0 corollary, PROVED (assembly);
  - -02: Delsarte bound, PROVED;
  - -03: uniform Theorem A, PROVED with LITERATURE dependency on KLM 2025 Thm 6.4;
  - -04: 1/18 cap, PROVED;
  - -05: explicit γ, OPEN;
  - -06: PD-N, torus-LP finite limitation, PROVED (exact witnesses).

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
  - Consequence: the uniform bound can exclude packages only for n ≥ 138 (exact integer check). A finite-LP version for 4 ≤ n ≤ 137 is OPEN; the corrected wording follows independent check E1-M1.
- **Independent checks** (Opus subagents).
  - C0 (`independent-checks-C0.md`): no BLOCKING. M1 (PR #27 also claims the sharp expansion) and m1–m5 were fixed at `6680efe`.
  - E1 (`independent-checks-E1.md`, Opus xhigh): no BLOCKING. Every proof step was reconstructed, and the lattice and the threshold 138 were rerun independently. M1 (an overclaimed finite-LP range) and m1–m7 were fixed in the following commit.
  - S4's "lattice value 1/18" is reconciled.
- **Novelty gate.** `novelty-gate-E1.md`: one surviving variant (-01) and four deferred or pending candidates.
- **LP code.** The Sonnet 5.5 high subagent is running the torus plain and Delsarte LPs, the lattice references and the cube LP. Results go in `evidence/lp-*.json`.

## 2026-11-12 — Claude, claude-opus-5-5 (xhigh per AC prompt; effort not exposed) — session 1, numerics and closing (E1 round 3, E3 round 1)

- **LP subagent** (Sonnet 5.5 high) finished. About 2 h wall on 3–5 processes. Code is `code/lp_{torus,lattice,cube,report}.py`; small evidence is `evidence/lp-*.json`; bulky receipts are in the session scratchpad only, not archived.
- **Q1 PASS. Q2: plain-LP KILL, Delsarte INCONCLUSIVE. Q3 not exercised** (`gates.md`).
  - Plain torus LP: ρ_n = 1 within 3e-6 for n = 2…12.
  - Delsarte LP: ρ^Del up to 1.084 (n = 7, K = 19).
  - Lattice minima M_lat (avoid 0 < |k|₁ ≤ 2n−2): exhaustive for n = 2…8, upper bounds for 9…16. The orchestrator re-verified all 15 witnesses independently.
  - Cube LP: λ = 1.2034, 1.2104, 1.2010 at n = 2, 3, 4 (relaxation upper values).
- **Strengthening, found while setting up the witnesses.** The lift of a rule exact on Π_{2n−1} is exact up to |k|₁ = 2n−1, which gives L = n in the transference (-02 (d), with proof).
  - So -03 (ii′): N ≥ (1+γ_A)n³/6.
  - The package threshold under γ_A ≤ 1/18 moves from 138 to **110**; the exact integer check is in -03.
  - This matches the merged lattice-class threshold of `topics/padua-3d-20261106/paper-note-draft.md` §4 (19n³/108, n ≥ 110), which is the case γ_A = 1/18.
  - -04 and -05 updated. Records -02, -03, -04 and -05 have dated history notes.
- **-06 (PD-N).** `code/pdn_lattice_witness.py` searched for integer lattices with min ℓ₁ ≥ 2n and index ≤ 8·binom(n+3,3), using critical-lattice roundings, ±1 perturbations and the subagent's lattices. Each witness is verified by exhaustive coefficient-box enumeration, and again by direct ℓ₁-ball enumeration (`code/pdn_check_ball.py`, 0 failures). **Result: S = 2…109 for exactness 2n−1**, the full range where the uniform bound is silent; witnesses are impossible for n ≥ 110 by the packing bound. Evidence: `evidence/pdn-lattice-witness.json`.
- **Independent check E1b** (Opus): no BLOCKING. MAJOR-1 (placeholders and missing evidence) and MINOR-1–3 fixed; dispositions in `independent-checks-E1b.md`. Cross-check: the witnesses at n = 3, 6, 9, 12, 15 equal the merged exact minima of `r08-lattice-minima.md` (38, 304, 1026, 2432, 4750), and every witness is ≥ the merged minimum.
- **Candidates.**
  - Cube LP -03: killed for n = 3, 4 (MEASURED), deferred for n ≥ 5.
  - New pending candidate -06: Delsarte extension of the cube LP.
- **Outputs written:** `rounds.md`, `attempts/E1–E3.md`, `report.md`, `evidence-manifest.json`; results updated.
- **Handoff.** Handoff 01 closes in the following commit. Handoff 02 is the Codex audit.

## Runs needed

- Delsarte torus LP n = 9…12 at K = 3n−2 (`attempts/E1.md`); cube LP n ≥ 5 and its Delsarte extension (`attempts/E3.md`); certified φ (-05).
- Cold-storage archival of the scratchpad LP receipts (`runs/*.json`, `*.npz`): pending, AC's storage was not reachable from this session. They are regenerable from the committed code and commands in `evidence/lp-torus.json` and the subagent report summarised above.
