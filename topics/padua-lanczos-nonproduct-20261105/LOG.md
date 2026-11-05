# Span drift on genuinely non-product families: log

- Branch: `codex/padua-lanczos-nonproduct-20261105` · Base: main `be9a831` (PR #29 merged) · Developer: Codex · Auditor: Claude (Opus 5.5 xhigh)
- Stage: WORK · Next: `Codex (gpt-6-astra high): Continue codex/padua-lanczos-nonproduct-20261105.` · Open handoff: [handoffs/01-work.md](handoffs/01-work.md)
- Reserved final-ID ranges: none. Under the PR #29 rules, reserve when first needed (normally at PR preparation).
- Claims: none yet.

## 2026-11-05 — Claude, claude-opus-5-5 (configured; effort not exposed) — topic setup

- After Claude's PR #24 summary, AC said: "Yes make a handoff for nonproduct".
- Motivation: PD-T324/328/329 hold on SH_n, an affine image of a product measure. The target is an all-degree separation, or a proved obstruction, on a genuinely non-product family.
- Directions:
  - P1: the triangle (Proriol–Koornwinder and discrete Hahn/Krawtchouk);
  - P2: the disk (rotation invariance, with exact Pythagorean grids);
  - P3: non-affine perturbation of SH_n and its stability radius;
  - P4: a structural criterion;
  - P5: Padua (bounded);
  - P6: exact scans.
- Model allocation and round rule follow AC's instructions of the same day: 10 rounds per direction (P5 capped at 5), all in parallel.
- Rules read at `be9a831`. PR #29 changed WORKFLOW (proportionate audits, reservations at PR preparation, registry edits by reviewed diff). Branch created from main `be9a831`. Only this LOG, handoff 01 and the results stub were added. No computation was run and no claim made.

## Runs needed

- N0–N4 and P1–P6 as in handoff 01.

## 2026-11-05 — continuation setup — Codex, requested gpt-6-astra high

- Role: coordinator/developer. Serving metadata not independently exposed.
- Rules/input head: `cafb74ab6f7738c8af83d0cd0f518b81af16f253`.
  Fetched main: `be9a8318150204711d5446d2ea26284cf1ed0819`, already an
  ancestor; no merge needed. Working tree was clean.
- Read AGENTS, WORKFLOW, Codex role, LOG and open handoff 01. Its explicit
  model allocation and six parallel directions govern this campaign.
- Initial network attempt failed with an unavailable proxy; retry with the
  execution tool's network permission succeeded. No credential changes.
- Wrote [plan.md](plan.md) before new experiments, including exact N2 slope
  conventions and the distinction between sufficient and maximal N4 radii.
- Assigned predecessor replay to a Sol medium worker; direction workers wait
  for N0. No scientific claim or novelty content is added by this setup.

## 2026-11-05 — N0 PASS and parallel launch

- [N0 replay](n0-replay.md), Sol medium: six SH degree/rule cases, 88 symbolic
  identities and all four requested degree-12 endpoints match exactly. All 44
  native degree-2–12 prefix rows also match. Actual native wall seconds:
  triangle BJ/mirror 3.54/1.66; rotated BJ/mirror 87.21/96.23.
- Receipt-only missing legacy `pivot_ties` handling was corrected; unchanged
  completed native outputs were then verified without rerunning the native
  cases. No mathematical mismatch. Full provenance remains in N0's record.
- Opened [draft PR #30](https://github.com/aacchhee/padua_research/pull/30),
  audit pending, no final-ID reservation and no shared registry change.
- After N0 passed, dispatched P1–P5 to distinct Sol xhigh mathematics workers
  and P6 to Sol medium, disjoint ownership as in plan. P4 owns the common
  affine-product definition; each direction owns its full prospective novelty
  gate and family admissions. No new family scan is authorized before N1.
- Clarification for P1: coordinate-swap symmetry alone does not identify BJ
  and mirror capacities while keeping the within-degree Gram–Schmidt order
  fixed. Any equality or separation needs a derivation in the actual model.
