# Handoff 03 — padua-3d-20261106 — development response to audit 01

- Status: open
- Previous handoff: [02-audit.md](02-audit.md)
- Next agent / model / effort: **Codex, gpt-6-astra high** as coordinator, as in handoffs 01–02. Delegate record and mechanical fixes to gpt-6.1-sol medium. Delegate any new mathematical or computational work (M2 probes, M4 enumeration) to gpt-6.1-sol high.
- Role: developer and orchestrator (response).
- Branch: `codex/padua-3d-20261106`.
- Input head SHA: `64292b52db63404853000e2cc4ac90727797075b`. This is the audit output commit; the following commit publishes this handoff.
- Main / base: `76ba4214b100c86a44941f5e9a662ce9ce48efb8`. Fetch `main` first and reconcile if it has moved.
- Stage: WORK.
- Written by / date: Claude, claude-opus-5-5 xhigh · 2026-11-06.

## Task

Write `response-01.md`, answering every MAJOR (M1–M5) and MINOR (m1–m15) finding in [audit-01.md](../audit-01.md). Give each finding one of three answers:
- a fix, with file and location;
- an evidence-based rejection;
- an explicit unresolved item.

Make the fixes in the topic's own files. Use dated addenda for prose corrections; do not silently rewrite. The audit accepted the mathematics, so **do not change any theorem statement, proof or status** unless a fix forces it. If a fix does force one, report it as a material change.

In order:

1. **M1, missed predecessors.**
   - **T1.** Add to `novelty-gate-T1.md` and `literature-T1.md`, with differences:
     - De Marchi–Vianello–Xu 2009 (LIT-322/306; `literature/lattice-unisolvence/records/demarchi-vianello-xu-2009.md`), including its parity subgrid as a member of the T1 class and its "not interpolation" remark;
     - LIT-374, IDEA-109 and OBST?bivariate-lanczos-claude-11;
     - LIT-381.
   - **T5.** Bring `novelty-gate-T5.md` to template form, with closest entries read, falsifier, verdict and disposition reasons. Add the missing predecessors: IDEA-044, IDEA-108, IDEA-109, LIT-374, LIT-327, and Noskov–Schmid and Hirao–Sawa (X7 note).
   - **D4 control.** Attribute the 16-node same-parity Lobatto rule in `theory/t5-validation-and-measurements.md` to DMVX.
   - No novelty may be asserted.
2. **M2, candidate retention and dispositions.** Give each item below a provisional IDEA-template record, or extend the record it already has. Each must carry a disposition, a reason and, if deferred, a resume condition:
   - T2(a), Lissajous–Chebyshev alias-equivalence. Check and state whether unshifted Dencker–Erb nodes fall under PD-N?…T1-01 for n≥2.
   - T2(b) and T2(c), as not launched.
   - The T2 phase, omit-n3/even-degree, coset-union and mod-6 routes. Add IDEA-182 and PD-N034 to the union route's closest entries.
   - The Haar-lattice packing lead.
   - The Lobatto m4/m5 probes, T5-04 and T4-03.
   - IDEA?…T2-01, giving its final disposition.

   For the **T5 commuting-completion probe** (handoff 01:82, n≤4), either execute the small probe under a written preregistration (status MEASURED at most), or record its non-execution as a LOG deviation for AC with reason and resume condition. Fix `rounds.md:44` either way.
3. **M3, T2 gate deviation.**
   - Qualify `novelty-gate-T2.md:5`.
   - Add one canonical LOG disclosure.
   - State that the eventual IDEA registration will carry a permanent timing qualifier (IDEA-576 precedent).
   - Put the deviation in the PR body for AC's acceptance.
4. **M4, D3(b) coverage.** Either:
   - run an exact full-class enumeration (coordinate orders up to the finite class bound) at n=2 and every further feasible n, with committed code and a small receipt, then restate the D3 verdict; or
   - relabel D3(b) as partially met in `gates.md`/`report.md` and refer it to AC.

   The auditor's count-formula run (`audit-01/code/formula_enum.py`) is audit evidence, not a developer run.
5. **M5, ID kind of short relations.** Reclassify PD-N?…T3-01 as a PD-T, or name a genuinely proposed and failed mechanism. Record the old-to-new provisional mapping. Disputes go to AC.
6. **MINOR m1–m15.** Make the wording, link, stale-text and attribution fixes listed in the audit.
   - In particular, m3: record the survivor symmetry classes, and either apply the preregistered lexicographic tie rule or disclose the deviation.
   - m6/m7/m8: qualify the T6 attribution, state where the T6 constant becomes nontrivial, and correct the tautological multiplier-test wording.
7. Update `report.md`, the LOG, `results/padua-3d-20261106.md` and the PR #33 body as needed.

## Read first

- AGENTS.md, agents/WORKFLOW.md, agents/codex/CODEX.md at the branch head.
- [audit-01.md](../audit-01.md) and the scope reports in [audit-01/](../audit-01/). [novelty-records.md](../audit-01/novelty-records.md) has the exact file and line locations for M1–M3 and the MINOR list B1–B10.
- The LOG entry for audit 01, handoffs 01 and 02, and the files named in each finding.

## Scope limits

- Do not reopen the accepted mathematics, the H39 cover, the T4 kill at n=7, or any killed family.
- Do not edit the audit report or its appendices. Disagreements go in `response-01.md` and are preserved for AC.
- No final IDs, reservations or shared-registry edits (`state/IDEAS.md`, `PROOF_STATUS.md`, `ID_CROSSWALK.md`, `literature/INDEX.md`, `RESULTS.md`) in this step. Those belong to PR preparation after the focused re-audit.
- Do not change other topics, main, tags, `.github/` or repository settings. Do not merge; only AC merges. Keep earlier handoff bodies intact.
- Any new computation stays small (receipts under 16 KiB) with committed code. Large outputs stay regenerate-only, with identities recorded.

## Acceptance and outputs

- `response-01.md` disposes of every finding, and the fixes are committed.
- Each material change is listed with its exact files: changed dispositions, gate verdicts, ID kinds, new records, any new computation.
- Commit the outputs first. In a following commit, close this handoff as `done in <output-sha>` and open handoff 04:
  - for a **focused Claude re-audit** of the listed material changes only, with Opus 5.5 high or xhigh, auditor's choice; or,
  - if the response contains MINOR fixes only, for Codex **PR preparation**: fresh reservation procedure, direct reviewed registry diff, readiness check.
- Push before replying, and end with the matching short continuation prompt.
