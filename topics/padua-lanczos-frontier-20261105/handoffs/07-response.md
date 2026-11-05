# Handoff 07 — padua-lanczos-frontier-20261105 — response to Claude audit-01

- Status: open
- Previous handoff: [06-audit.md](06-audit.md)

- Next agent / model / effort: Codex. Use gpt-6.1-sol **high** for status, scope and statement wording (A-M1, A-m1, A-m4) and for the gate-timing remediation (A-P1). Use gpt-6.1-sol **medium** for mechanical record, receipt and manifest work (A-m2, A-m3, A-m5–A-m8) and the L7 platform addendum (A-M2). Any supplementary check is gpt-6-astra; it does not replace the Claude re-audit below.
- Role: developer and orchestrator for this step. Only the orchestrator changes Git state.
- Branch: `codex/padua-lanczos-frontier-20261105`
- Input head SHA: `3f1e74cc73cd09351e673341ddf2ba73f5d46633`. This is the audit-01 output commit; the commit that publishes this handoff comes later.
- Main / base: branch base `aff30e8ad5542c94fab642ae024dc9aab4fa7ad7`; current main `330fab835f43e5ba5b24e320c2d7e9647e6cbd60` (PR26 merged; not yet merged into this branch).
- Stage: WORK
- Written by / date: Claude, Opus 5.5 xhigh (`claude-opus-5-5`) · 2026-11-05

## Task

Answer every finding of [audit-01.md](../audit-01.md) in a new `topics/padua-lanczos-frontier-20261105/response-01.md`. Each finding gets one of: a fix (with file:line and commit), an evidence-based rejection, or an explicitly unresolved item. Use the audit's finding IDs (A-M1, A-M2, A-P1, A-m1 … A-m8) and cite the family-report IDs they consolidate (L1-n, L2-n, L3-n, L4-n, L5-n, L6-n, L7G1-n, PROT-n). Address the family-report NOTEs too, briefly (accept / decline / defer).

Order of work:

1. **Start.** Read the rules at the branch head and record the SHA. Fetch main and the topic. Merge `origin/main` (`330fab8` or newer) into this already-pushed branch; never rebase or force-push. Delta-read what main changed (PR26 is MZ work; check that no Lanczos source or rule changed) and record the result.

2. **A-M1 — L3 status** (L3-1 = PROT-3).
   - Relabel the broader L3 target **OPEN** in `attempts/L3.md:3` and `ideas-l3-continuation.md:123–124`. Name `PD-T?lanczos-frontier-codex-L3-01` as a PROVED supporting result proved under a stronger per-column budget than PD-T143's Hres.
   - Make every file agree (report, results, proposals). Add a dated History note giving the original wording and the reason.
   - If you instead want an explicit PARTIAL split, write it in full and refer the classification to AC rather than deciding it yourself.

3. **A-M2 — L7 platform scope** (L7G1-1). Add a dated additive addendum to `theory/l7-natural-suite-measurements.md` and the L7 methods/storage docs. It must:
   - record the BLAS kernel/CPU that produced the committed counts;
   - pin `OPENBLAS_CORETYPE` in the regeneration recipe;
   - disclose the audit's cross-kernel rerun (default AVX-512 kernel: 18 cells and 9 paired directions; Haswell: exactly 20 and 6);
   - list the robust features;
   - state that the specific cells and pairs depend on the platform.

   Keep the label MEASURED. Do not re-run the suite to "fix" counts. An additional pinned-kernel rerun is optional; if you run one, label it as new evidence.

4. **A-P1 — gate timing** (PROT-2). Complete R1 (one dated table), R2 (a qualifier in each affected IDEA and in each descended PD-T/PD-N History, including that L3-01's constants were drafted before the gate) and R3 (the closest-entry omissions: IDEA-130/134 for SH_n; IDEA-148/PD-N013 and IDEA-151/PD-N015 for W/R). Record R4 as process. Do not describe the deviation as waived or cured. Whether to accept it is AC's decision, so put that question to AC explicitly in response-01 and in the PR body.

5. **A-m1 to A-m8.** Apply the record, wording and evidence fixes. Use additive dated updates and keep history.
   - Where a checker pins a file's hash (for example `l2-smooth-rule-closure-reduction.md` via `g2_screen.py`/`g2_independent.py`, and the `l6-02` contract via `l6_n1_independent.py`), choose one of two routes:
     - keep the pinned bytes frozen and add the update in a separate file or pointer; or
     - re-pin as a recorded packaging change and rerun the affected checker once, recording the command and result.
   - **A-m5:** write literal old→new blocks for every affected registry row. That includes `state/CURRENT.md:103`, the `ID_CROSSWALK` split mapping and this topic's RESULTS section. Register L6-02 as IDEA-262's contract and L4b as a variant of IDEA-250.
   - **A-m7:** commit compact per-degree outward-rounded G1 endpoint tables (each file under 16 KiB), so rotQ24's INCONCLUSIVE verdict can be rechecked without hours of regeneration. Commit the full 20-row L7 loss list, document a repository-only n1 rerun recipe that does not overwrite committed evidence, and record the BLAS dispatch and CPU ISA in numerical receipts from now on.
   - **A-m8:** `code/check_manifest.py` fails because `audit-01/` was added. Fix the inventory scope or regenerate it with provenance, without editing any audit file.

6. **G0/G4 note** (PROT-1). Add a dated additive note to `g0-disposition-02.md` and `g4-disposition-04.md` recording the audit's bit-for-bit reproduction of all 12 historical own-method gaps under the SkylakeX OpenBLAS kernel on an AVX-512 host.
   - Keep the original FAIL and the class-level explanation.
   - State the scope: own methods only; upstream_xy not rerun.
   - State the orchestrator's nuance that Haswell does not bit-reproduce the developer's own recorded current gaps (about 8e-8 and 7e-5 relative).

7. **Checks.** Run the topic's fast checks on what you changed: manifest, JSON parse, links, `git diff --check`, any re-pinned checker. Record exact commands and results.

8. Update LOG (header, Runs needed with exact commands where possible), report and results for the actual changes. Update PR24's WORK/AUDIT sections: AUDIT = Claude audit-01 FINDINGS REQUIRE WORK, response pending or complete. Keep the PR draft.

## Read first

- Rules at the branch head; [audit-01.md](../audit-01.md) and every family report in [audit-01/](../audit-01/).
- [handoff06](06-audit.md) and the original [handoff01](01-work.md) targets.
- LOG, report, results and [proposed-record-changes.md](../proposed-record-changes.md).
- The theory, attempts and ideas files named in each finding.

## Scope limits

- Do not edit or delete `audit-01.md`, anything under `audit-01/`, or earlier handoff bodies. Record any disagreement in response-01 for AC.
- No new scientific claims, status upgrades or tolerance changes. Accepted mathematics need not be reopened.
- Any statement or status change goes to the re-audit below. Original OPEN targets stay OPEN: PD-T055, F, PD-T056(G), U2 and G3 (n4–8, with handoff01 asking n3–10), degree-uniform/efficient selection, and scalar/IEEE activation.
- No final IDs and no edits to shared registries before audited PR preparation. When IDs are eventually needed, refresh the full active and retired reservation union first. Range T324–363/N116–131/IDEA414–453/LIT582–593 was first published at `40b3eb6`; PR25 holds T364–375/N132–137/IDEA454–465/LIT594–597 and PR26 holds T376–391/N138–145/IDEA466–489.
- Scope is this topic directory and its results file, plus the authorized main merge. Nothing on `main`, no merge, no force-push, no tags, nothing under `.github/`, and no computation on an external machine.
- Large outputs stay off Git, following COLD_STORAGE.md.

## Acceptance and outputs

- `response-01.md` answers every audit finding, citing the commit and file:line of each fix. A-P1 is presented to AC as an explicit decision.
- Fixes are committed and pushed, and the fast checks pass, with their commands recorded.
- When this step is done:
  1. Commit the outputs.
  2. In a following commit, set this handoff's status to `done in <output-commit-sha>` and add `08-reaudit.md`.
- Handoff 08 is for **Claude, Opus 5.5 high**: a focused re-audit of the response. Use xhigh only if a proof or claim statement changed. It covers A-M1, A-M2, A-P1 remediation, A-m1–A-m8 and any re-pinned checkers, against the exact response head.
- If the re-audit accepts, PR preparation follows: reservation refresh, final IDs, literal registry application, integration checks and AC's merge decision. Only AC merges.
