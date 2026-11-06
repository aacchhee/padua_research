# Handoff 08 — padua-3d-20261106 — response to audit 03 and completion of the reopened routes

- Status: done in 8eb90342eaf323b889737b5160c55f2f619763bc
- Previous handoff: [07-audit.md](07-audit.md)
- Next agent / model / effort: **Codex**.
  - Coordinator: gpt-6-astra high.
  - Mathematical workers: gpt-6.1-sol xhigh.
  - Code and screens: gpt-6.1-sol high.
  - Astra ultra is allowed when necessary (AC), with a written justification each time.
- Role: developer and orchestrator.
- Branch: `codex/padua-3d-20261106`.
- Input head SHA: `a74c1b18d0d59515b549fc15c5be85c148190201`. This is the audit-03 output: report `c681ba0`, then the auditor fixes `a74c1b1`. The following commit publishes this file.
- Main / base: `f70a260e5b5f9a01209dc8a05faabdcf8db1feeb`. Fetch first and reconcile if main has moved.
- Stage: **WORK**.
- Written by / date: Claude, claude-opus-5-5 xhigh · 2026-11-06.

## Budget

The handoff-06 counters **continue; they are not restarted.** They stand at T7 = 3, T8 = 2, T9 = 2 and T10 = 2 of 25. Handoff 06's strict stop rule (a) still applies.

## Part A — `response-03.md`

Answer every MAJOR finding of [audit-03](../audit-03.md), E1–E6, and every item listed there as "Returned to the developer". Each gets a fix, an evidence-based rejection, or an explicit unresolved item.
- **Do not edit** audit reports, [audit-03-fixes.md](../audit-03-fixes.md) or earlier handoff bodies.
- You may **dispute any auditor fix**; disputes go to AC.
- When you next touch a theory file that the companion note corrects, apply its correction with a dated note, and update the prose pins or remove them. Under WORKFLOW, new checkers must not pin prose.

1. **E4, label convention (AC decides).**
   - Propose one criterion for results that depend on a cited theorem. Apply it to T9's packing consequence, the T9 R-Leja transfer and the T10 log³ corollary.
   - The audit's view: PROVED with an explicit LITERATURE dependency when the exact statement and normalization have been primary-read (precedent PD-N022). CONDITIONAL when a hypothesis or lemma chain has not been checked.
   - Never shorten such a label to bare PROVED. Put the question to AC in the PR.
2. **E2, T10 extraction kill.**
   - Restate it: the preregistered kill was met at n6/7, as `evidence/t10-quality.json` itself records. n8..16 is disclosed post-kill verification. The n8 exception depends on the mesh and on QR ordering (like-for-like global QR: 35.816 against 45.458).
   - Give the killed rules scoped PD-N records.
3. **E6, records.**
   - Scoped PD-N records for the D2-killed frozen rules: T8 F, U2, U3 and U4, the initial Φ3 selectors, and the T10 extraction rules.
   - IDEA-template records for the T7 and T10 candidates, with dispositions and resume conditions; no "Active" rows left.
   - A recorded outcome for T7's "degree-uniform H_n" sub-item, and resume items for folded and mixed unions.
4. **E5, gates.** Add the missed entries with their differences:
   - T10: LIT-391, IDEA-178, IDEA-013, PD-N035/037, LIT-382, LIT-512, and Belinsky's polyhedral log³ kernel theorem;
   - T7: IDEA-187, PD-N037.

## Part B — reopened routes (these count as rounds)

5. **E1, T10.1 census, reopened.** Keep three objectives strictly separate, for each n:
   - (i) minimum det L with shortest nonzero ℓ1-norm ≥ 2n;
   - (ii) minimum folded count |X|;
   - (iii) minimum |X| among Π_n-unisolvent sets, which equals N exactly when a Padua-type set exists.

   Run exhaustive exact searches as far as feasible, and record the measured cost where you stop. The audit found these runs cheap: n=4 det 92 and n=5 det 178 in seconds. With the imported packing bound, the n4..12 windows close in minutes.

   **Record the n=2 Padua-type sets.** The order-19 cyclic sets z = (1,3,7), (1,4,6), (1,5,8) give exactly 10 Π₂-unisolvent nodes with a positive degree-3 Haar cubature (dual ℓ1-minimum 4; Λ ≈ 8.134). Link them to T7's order-19 survivors and T2's old n=2 survivors.

   Then decide whether **any n ≥ 3 has a Padua-type set** (unisolvent, exactly N nodes, positive degree-(2n−1) cubature), within each searched class. This is the sharpest finite version of the topic's question. Restate the T10 headline table afterwards.
6. **E3, T9 finite complement.**
   - Run measured, exact unrestricted probes: all lattices with ℓ1-minimum ≥ 2n and det ≤ 8N. The audit timed them at 13 s, 125 s and 706 s for n = 2, 3, 4.
   - Record the observed positive unshifted rules with at most N nodes (minimum node counts 7, 16 and 35 at n = 2, 3, 4; the n=4 rule with 35 nodes has rank 30).
   - Continue to higher n, or record measured infeasibility. Share code with item 5.
7. **New leads to screen** (preregister first; each counts toward its direction).
   - **T8 half-shifted M = 2N orbits** (phase z/(2M)), which the special-strata grid could not reach. At n3, M40 the audit found 8 exactly unisolvent sets; for example z = (1,4,11) measures Λ₂₁ ≈ 9.79, better than Leja's 13.17. Screen n = 3..8 with exact certification and the D2 rule.
   - **Possible T8 PROVED upgrade (a material status change).** The finite witness certificates now meet the computer-assisted-PROVED conditions. If you propose the upgrade, list it as a material change for re-audit.

## Scope limits

- Do not reopen accepted theorems, killed families, or the n=2 classification.
- No final IDs, reservations or shared-registry edits.
- Do not touch other topics, main, tags, `.github/` or settings. Only AC merges.
- Receipts stay under 16 KiB. Raw outputs are regenerate-only with recorded identities, in unique scratch directories.

## Acceptance and outputs

- `response-03.md` and its fixes.
- Updated or new attempts, theory, gates, preregistrations and literature records, with explicit statuses.
- `rounds.md` with valid stop reasons, or the counters left running.
- Report, LOG, results file and PR body updated.
- Commit the outputs. In a following commit, close this handoff `done in <sha>` and open handoff 09: a focused Claude re-audit of the material changes and the new route work (Opus 5.5 xhigh).
- Push before replying, and end with the short continuation prompt.
