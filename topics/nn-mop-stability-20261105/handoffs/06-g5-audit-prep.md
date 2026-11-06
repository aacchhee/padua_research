# Handoff 06 — nn-mop-stability-20261105 — Codex audit of the Claude G5 run, then PR preparation

A new numbered file each time work passes to another agent or session, opened by the orchestrator holding the previous handoff. Never overwrite an earlier handoff or alter its body; only the status line changes. AC starts the step with `<Agent> (<model, effort>): Continue <branch>.`

- Status: done in dd092fb74b3030fe28dd8dd221ef59e0e80b2b72
- Previous handoff: [05-reaudit.md](05-reaudit.md)

- Next agent / model / effort: Codex.
  - Part A (G5 audit): `gpt-6-astra` medium, the ordinary technical audit row.
  - Part B (PR preparation): `gpt-6.1-sol` medium, plus high for statement-bearing registry rows.
- Role: independent auditor of Claude's G5 development (part A); developer and topic orchestrator for PR preparation (part B)
- Branch: codex/nn-mop-stability-20261105
- Input head SHA: `3e3a8e99e2ea63fdf2348e34bd53516ef7cd02c3`. It contains audit-02 at `ad9f8b6` and the G5 run at `3e3a8e9`. The commit that publishes this file comes later.
- Main / base: `f654e32daff27b6846849311092f6daebbbf235b`, merged at `8a2b65d`
- Stage: PR
- Written by / date: Claude, Opus 5.5 xhigh · 2026-11-06

## Task

### Part A — independent audit of the Claude G5 run

Write `audit-g5-01.md`. Claude developed this step, so Codex audits it.

1. Read [../g5-run/README.md](../g5-run/README.md), [driver.m](../g5-run/driver.m), [cmp.py](../g5-run/cmp.py) and the committed outputs. The rule fixed before the run was: gate Kravchuk, paper N=10, IEP_CORE, |log10(ours/paper)| ≤ 1. Check that:
   - the driver replicates `experiment_Hahn_Kravchuk.m`: same parameters, algorithms and error formulas, plotting only removed;
   - the size convention is right (paper N ↔ N+1 integer nodes);
   - the interpretation of large-N variation is labelled as untested.
2. **Inputs.** The source archive `IEP-MOP-main.zip` (SHA-256 `cdd0e98d2b411f24cfcecb49d83e16f9d50a7622a0d4f0d3eb17eb334a405145`) exists only as AC's upload to the Claude session, and Codex's executor previously could not reach arXiv.
   - If AC supplies the archive and the arXiv source bundle (`f736e8f03b536382141c2c98620c3cd408e0ff2c772ce58f47030e944864d461`) to your executor:
     - verify both hashes and the per-file SHA-256 table;
     - read every executed script;
     - install Octave if it is installable on an authorized route;
     - independently rerun the driver, and compare with the committed outputs and with the paper's data.
   - If the inputs are not available to you, audit the receipt, code and committed outputs as review only. Say so explicitly, and leave the independent rerun as an explicit unresolved item for AC. Never call review a rerun.
   - Do not commit third-party code or data. Do not contact Leuven, and do not bypass access controls.
3. Findings use BLOCKING/MAJOR/MINOR/NOTE. If accepted, the G5 verdict text in gates.md, report.md, attempts/D7.md and external-code.md is updated in part B. It reads: "G5 reproduction gate PASS (one configuration, Octave 8.4, to the decade); large-N variation measured; topic-metric comparison not yet run". Any material finding returns G5 to Claude: open a handoff for a Claude response, instead of doing part B.

### Part B — PR preparation, only if part A accepts or leaves only MINOR items

4. Fix audit-02's MINOR items R-1 to R-8 exactly as worded in [../audit-02.md](../audit-02.md).
   - R-1: restore the D6/D4 gate chronology in one dated Codex addendum below the canonical AC-decision LOG entry, and mark the parentheticals that response-01 inserted into that Claude entry as Codex text.
   - Update evidence-manifest pins for every pinned file you edit, in the same commit.
   - Optionally address audit-02's NOTEs.
5. **Reservation check.** Run the full WORKFLOW reservation check before assigning any final ID: main plus every open PR (drafts included), their ledgers and used IDs, and retired reservations. Record the heads checked in ALLOCATIONS.md and the PR body.
   - PR #30 (now on main) uses PD-T472–494, PD-N178 and IDEA-571/575. These sit above this topic's permanent ranges: T432–471, N162–177, IDEA530–569, LIT614–629.
   - If the inventory needs more IDs than a range holds, reserve a fresh range by the same procedure. Never shift ranges.
6. **Final IDs and registries.** Assign final IDs from the reserved ranges and keep every provisional-to-final mapping in ID_CROSSWALK.md. Apply the registries by direct edit, which will be reviewed as a `git diff`:
   - PROOF_STATUS.md: every PD-T/PD-N theory record, with the true status, the REJECTED dispositions with reasons and refuting links, and the two OPEN parent targets;
   - state/IDEAS.md: all provisional IDEA records, including deferred, failed and equivalent ones, IDEA-117/378 pointers (378 stays deferred), and IDEA-090 kept deferred;
   - literature/INDEX.md: reuse LIT-567/568; only Branquinho et al. 2022 is new;
   - this topic's RESULTS.md section, from results/nn-mop-stability-20261105.md;
   - state/CURRENT.md and PAPER_MAP.md where relevant.

   Registries carry no process stage (be9a831 rule). Distinguish intrinsic conditioning, finite accuracy gains, and the absence of any proved stable algorithm. G4 is never PASS.
7. Update LOG, report and results, and PR #28's WORK/AUDIT/PR sections. The AUDIT section links audit-01, audit-02 and audit-g5-01. Keep the PR as a draft.

## Read first

- AGENTS.md, agents/WORKFLOW.md and agents/codex/CODEX.md at the branch head: the proportionate-audit rules, the reservation procedure, and "Registry application by reviewed diff".
- LOG.md: the canonical AC decisions and the latest entries.
- audit-01.md, response-01.md, audit-02.md, g5-run/README.md.
- ALLOCATIONS.md and the theory/candidate inventory: theory/*.md, candidates-*.md, novelty-gate-*.md.

## Scope limits

- Do not change any accepted claim, status, threshold or result. R-1 to R-8 are record hygiene only.
- Any material change, or a material G5 finding, returns to audit instead of readiness.
- Do not edit audit-01.md, audit-02.md, or their script directories.
- Do not alter another topic's ranges or registry sections, and never regenerate RESULTS.md from an older copy.
- No main commits, PR merges, force pushes, tags or `.github/` changes.
- Storage stays below 10 MB with no cleanup (AC). Only AC merges.

## Acceptance and outputs

- audit-g5-01.md is written, with an explicit statement of whether an independent rerun was performed.
- R-1 to R-8 are fixed.
- The reservation check is recorded, final IDs are assigned with their crosswalk, and the registries are applied in reviewable commits.
- LOG, report, results and the PR body are updated. The stage stays PR, awaiting readiness.
- Commit the outputs first. Then, in a following commit, set this status to `done in <output-sha>` and add handoff 07 for Claude (Opus 5.5 high) to do the readiness check:
  - review the registry `git diff`;
  - confirm R-1 to R-8 by diff;
  - refresh the reservation.

  If part A has a material finding, the next handoff instead goes to Claude for a G5 response.
