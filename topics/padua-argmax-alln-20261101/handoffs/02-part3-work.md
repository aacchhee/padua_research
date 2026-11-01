# Handoff 02 — padua-argmax-alln-20261101 — part 3: toward the all-degree Padua argmax

- Status: open
- Previous handoff: 01-update-after-part2.md

- Next agent / model / effort: Codex, gpt-6.1-sol xhigh for mathematics. Ultra is allowed for P1/P3/P4 proof steps with a written justification in LOG. gpt-6.1-sol medium for code, mechanical and replay work.
- Role: orchestrator and developer (part 3 development)
- Branch: claude/padua-argmax-alln-20261101 (continue this branch; do not open a second topic)
- Input head SHA: `61e8f81aeddc41d8f9594e2b70ec3f6135e74fff`
- Main / base: `2b52b43` (PR #12 merged)
- Stage: WORK
- Written by / date: Claude, claude-opus-5-5 · 2026-11-01

## Task

Goal: make as much progress as possible toward PD-T099. The target, for every n ≥ 2, is max_{[−1,1]²} λ_n = Λ_c(n), attained only at the non-node corners. Follow plan v2 ([plan.md](../plan.md) §4 obligations P0–P6, §6 tests T1–T5). This is an adventurous campaign: run directions in parallel subagents with disjoint file ownership and chase surprises. The honesty rules do not relax.

Steps, in order. Steps 2–4 may run in parallel once step 1 is done.

0. **Setup and replay.**
   - Read the rules at the branch head and record the SHA. Fetch main. If main moved, merge it, recording the impact first.
   - Independently rerun Claude's measured scripts with a different subagent, using its own outputs under `outputs/codex-replay/`:
     - `code/check.py`, `cell.py`, `interior.py`, `edgeprofile.py`, `strips.py`, `n2_edges.py`;
     - commands as in the two observations records;
     - compare with `outputs/*.out`.
   - Record the replay in `independent-checks-claude-records.md`. This replay is the Codex check of Claude's MEASURED records PD-T?argmax-alln-claude-01/02.
1. **Pre-registered tests T1–T5** (plan v2 §6). The kill criteria are already written there. Do not change them before running; if one proves ill-posed, record why and add a new criterion as a separate dated entry.
   - Put code under `code/part3/` and outputs under `outputs/part3/`.
   - The numerics are MEASURED. Exact or interval work needs outward rounding and an independent rerun.
2. **P0 and the finite range (IDEA?argmax-alln-claude-05).**
   - Build a global-max-only certifier: majorant/interval discard, plus a local strict-maximum certificate at the non-node corners.
   - Certify n = 2 first, then n = 8 (PD-T181 OPEN), then extend as far as cost allows, reporting box counts and times.
   - Apply IDEA-05's kill criterion.
   - Reuse part 2's certified machinery (PD-T160–178) where it helps, without modifying merged files.
3. **P1/P2 (edges).**
   - Generalize PD-T191 to every macroscopic ordinate: Δ_n(β_n, s_n) → g(β), uniformly on compacts of (0, π).
   - Give g(β) by a positive integral or series as in PD-T188, and prove inf g = g(π/2) = g, or at least inf > 0.
   - Do the same on the horizontal edges (n ↔ n+1). PD-T189/190 supply the phase control.
   - The goal is sup over each edge, minus δ-neighbourhoods of its ends, ≤ Λ_c − c + o(1).
4. **P6 effectivity (T4 first).**
   - If T4 projects n₀ ≤ 60: make the constants of PD-T189/190/191 and of P1/P2 explicit, aiming at an explicit n₀.
   - If T4 projects n₀ > 60: record the kill and pivot to IDEA?argmax-alln-claude-03 (monotonicity/pairing along edges, then in 2D), whose test is in ideas.md.
5. **P3 and P4 (corner neighbourhoods, interior)**, after T2/T3 verdicts.
   - Interior: two-phase localization of the four-copy majorant (generalize PD-T189), plus a positive limit and stability of the four-copy defect (generalize PD-T191).
   - Corner zone: the local comparison of how the majorant rises and how the defect grows near the coset point. Expect cusp-linear behaviour.
   - Read the 1-D literature (plan v1 §5.4) and record LIT entries before transferring a technique.
6. **P5 (strips).** Join P1/P2 to P4.
7. **Assembly.** If P0–P6 close, write the all-n theorem with its explicit threshold, the finite certificates for n < n₀, and the dependency list. Otherwise, report precisely which obligations remain, with every partial theorem in its own theory file.

## Read first

- AGENTS.md, agents/WORKFLOW.md and agents/codex/CODEX.md at the branch head.
- This topic: LOG.md, plan.md (v2 and History), ideas.md, gate.md, theory/ (both MEASURED records), code/, outputs/.
- Part 2 (merged): `topics/padua-proof-attempts-2-20261101/`:
  - attempts/T-A4a.md, theory 70–77 (PD-T185–192), theory 01–04 (PD-T156–159), theory 05–19 and 40–65 as needed for the certifier;
  - audit-01.md and response-01.md.
- PD-T101 and programme-ideas OPEN_TARGETS A4. PROOF_STATUS rows PD-T098–T101 and PD-T156–197. IDEAS entries IDEA-206, IDEA-290…305.
- literature/INDEX.md before any priority or attribution claim.

## Scope limits

- Write only inside `topics/padua-argmax-alln-20261101/`, plus `results/padua-argmax-alln-20261101.md`. Edit no merged topic, theory or registry file. Put proposed changes to shared records in `proposed-record-changes.md` as literal old→new blocks.
- Use provisional IDs `PD-T?argmax-alln-codex-NN`, `PD-N?argmax-alln-codex-NN`, `IDEA?argmax-alln-codex-NN`, `LIT?argmax-alln-codex-NN`. When the draft PR opens, reserve final-ID ranges by the WORKFLOW fresh-range procedure (main, every open PR, retired reservations, the batch ledger), with headroom.
- Make no PROVED claim without a written proof. A computer-assisted claim needs a proved reduction, exact or outward-rounded arithmetic, committed checker code and evidence, and an independent rerun by a different subagent. Numerical agreement is MEASURED.
- Never commit third-party PDFs or fulltext extracts (the repo is public).
- Generated files: ≤ 1 MB each, ≤ 5 MB in total. Larger certificates go to cold storage `Downloads\padua\cold_storage\padua-argmax-alln-20261101\` with COLD_STORAGE.md (path, sha256, size, command, script blobs, checker result); hand them to AC.
- Commits are authored as Andrey Chesnokov <aacchhee@gmail.com>, with the trailers `Agent: Codex` and `Model: <exact model and effort>`.
- Never commit to main, merge PRs, force-push, create tags or touch .github/. Only AC merges.

## Acceptance and outputs

- Each result has its own THEORY-template file in `theory/`, with an attempt note per obligation in `attempts/`. Also write `independent-checks*.md`, `evidence-manifest.json`, and a LOG entry per step boundary.
- Push at every step boundary, and at least every ~10 minutes while something changed.
- Open a draft PR to main early, with WORK / AUDIT (PENDING) / PR sections and the ID reservation.
- Update `results/padua-argmax-alln-20261101.md` as results arrive.
- Finish with `report.md`:
  - T1–T5 verdicts;
  - P0–P6 status with record links;
  - the certified finite range;
  - any counterexample (scoped PD-N);
  - effectivity numbers;
  - what remains OPEN.
- When done, commit the outputs. Then, in a following commit, set this handoff's status to `done in <sha>` and open handoff 03 for the audit: Claude, Opus 5.5 xhigh, which reads the complete state/IDEAS.md because this branch carries mechanism and novelty content. Reply to AC with only `Claude (Opus 5.5 xhigh): Continue claude/padua-argmax-alln-20261101.`
