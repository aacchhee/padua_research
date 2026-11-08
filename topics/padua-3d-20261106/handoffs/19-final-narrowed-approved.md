# Handoff 19 — padua-3d-20261106 — audit-04 response and final narrowed set, with AC's decisions

- Status: open
- Previous handoff: [18-final-narrowed.md](18-final-narrowed.md), superseded by this handoff because AC's approval settles its pending decisions.
- Next agent / model / effort: as in handoff 18.
  - **Codex** coordinator: gpt-6-astra high.
  - Mathematics: gpt-6.1-sol xhigh. Astra ultra is allowed for a stalled D1 proof, with written justification.
  - Code and checks: gpt-6.1-sol high.
  - Mechanical record work: gpt-6.1-sol medium.
- Role: developer and orchestrator.
- Branch: `codex/padua-3d-20261106`.
- Input head SHA: `91c24f14d8ceaf44fe5c608983da51ed9ea62066`, the published handoff-18 head. The following commit publishes this file.
- Main / base: `f70a260e5b5f9a01209dc8a05faabdcf8db1feeb`. Fetch first.
- Stage: **WORK**.
- Written by / date: Claude, claude-opus-5-5 xhigh · 2026-11-08.

## AC's decision (verbatim, 2026-11-08)

> "so far I approve current solutions for everything you asked"

Claude records this as AC approving each item put to AC in Claude's reply of 2026-11-08, in [frontier-assessment.md](../frontier-assessment.md) and in [audit-04.md](../audit-04.md):

1. **Frontier plan approved.** NARROW, then FREEZE, with the bounded set D1–D5 exactly as in handoff 18:

   | Item | Content | Ceiling |
   |---|---|---|
   | D1 | spectral obstruction | 6 rounds |
   | D2 | determinantal / symmetroid | 3 |
   | D3 | certified n=3 Padua-type set | 1 |
   | D4 | Gram / certified intervals and Lee bound | 2 |
   | D5 | framing and paper note | 3 record rounds |

   All other construction, optimization and pruning directions stay frozen.
2. **E4 label convention approved, as proposed.**
   - A result that depends on a cited theorem whose exact primary statement, normalization and application have been checked is labelled **"PROVED with explicit LITERATURE dependency"**.
   - It is labelled **CONDITIONAL** when an application premise, hypothesis or lemma chain remains unverified.
   - The label is never shortened to bare PROVED.
   - The response-03 proposal labels the packing consequence, the R-Leja transfer and the T10 log³ corollary. In each case check that the application really meets the first branch; otherwise use CONDITIONAL. Record AC's approval where the proposal said "pending AC".
3. **Storage allowance, as interpreted.**
   - Up to 100% over the storage limits, provisionally: 32 KiB per file and manifest, 10 MB of committed generated output repository-wide.
   - Round budgets are unaffected.
   - Still note its use in the PR body for discussion there.
4. **Earlier canonical deviations accepted as disclosed.** These are the T2 gate timing, the unexecuted T5 completion probe, the old stops and budgets, the T9 gate timing and in-place edit, the T7 reading coverage, and the allocation notes (response-deviations-01/02).
   - Do not rewrite them. Add one dated line in each deviations record: "Accepted by AC 2026-11-08 (see LOG)".
5. **Lattice stop(a) boundary accepted as recorded.** The measured 120-second implementation gate stands as the recorded boundary. Retain the auditor's unreplicated n6/n7/n8 probes (audit-04 A1 N3) as NOTE-level information. They may be reused in D4 if cheap.

## Task

Carry out the **complete instruction body of [handoff 18](18-final-narrowed.md)**, Part A (G1–G7 and the returned items) and Part B (D1–D5), together with its read-first list, scope limits and acceptance. Change it only in two respects:
- the decisions above are settled and must not be presented as pending;
- where handoff 18 asks you to put E4 or the deviations to AC, apply decisions 2 and 4 instead.

## Acceptance and handoff

As in handoff 18. Commit the outputs. In a following commit, close this handoff `done in <sha>` and open handoff 20 for the Claude audit (Opus 5.5 xhigh): a focused review of the audit-04 response plus D1–D5. If that audit accepts, the next step is Codex PR preparation (reservation, registry application, readiness), which freezes the direction. Only AC merges.
