# Handoff 10 — padua-lanczos-frontier-20261105 — audited PR preparation (A-P1 accepted by AC)

- Status: open
- Previous handoff: [09-pr-prep.md](09-pr-prep.md), superseded unworked by this handoff after AC's decision. Before that: [08-reaudit.md](08-reaudit.md).

- Next agent / model / effort: Codex. Orchestration and the R2 wording fixes run on gpt-6.1-sol **high**. Mechanical registry application, ID assignment, crosswalk, ledger and inventory work run on gpt-6.1-sol **medium**. A supplementary gpt-6-astra check is allowed, but it does not replace the Claude preparation audit below.
- Role: developer and orchestrator for this step. Only the orchestrator changes Git state.
- Branch: `codex/padua-lanczos-frontier-20261105`
- Input head SHA: `05bbe0669c76575934d19d868b7e9839fc307cf7`. This is the head that published handoff 09; it is unchanged except for the LOG entry recording AC's decision, which the same publication commit as this handoff adds. The audit-02 output commit is `767b822163106c85c31c61be77dd546733c3d0d6`.
- Main / base: last merged main `330fab835f43e5ba5b24e320c2d7e9647e6cbd60` (via `7f50cae`). Current main is at least `b4d292e`: PR25 merged as `9322fba`, then PR21, the literature campaign, as `b4d292e`. Refresh before acting.
- Stage: PR (audited preparation). **A-P1 accepted by AC on 2026-11-05**; see below.
- Written by / date: Claude, Opus 5.5 high (`claude-opus-5-5`) · 2026-11-05, after AC's A-P1 decision

## AC decision and amendments (take precedence over handoff 09)

- **A-P1 accepted.** AC, 2026-11-05, in reply to the explicit question in response-01, PR24 and audit-02: "I accept the deviation".
  - The pre-gate drafting deviation stays **permanently disclosed**, in the same way as before.
  - It is accepted by AC, **not waived and not cured**. The R1–R4 remediation and every qualifier stay in place.
  - Record the acceptance additively in:
    - gate-timing-response-01 (dated addendum);
    - the topic results file and the ROOT RESULTS block;
    - report.md;
    - the IDEA registrations and descendant History qualifiers, as one line: "AC accepted the disclosed deviation on 2026-11-05". Use dated companions where a file is hash-pinned.
    - the PR body.
  - Do not rewrite earlier dated text.
- **R2-5 amended.** results line 12 must now say the deviation was accepted by AC on 2026-11-05, and is disclosed, not waived and not cured. It must not say "pending".
- **PR21 has merged into main.** The P3 memo blob `4741c38943f37ae05ba525552ceafc3f32ac5537` is unchanged at `topics/padua-literature-20261103/p3-comparison.md` on main.
  - After merging main, update the "PR21 (unmerged)" attribution wording, additively and per statement, to cite the merged path with the same blob. Keep its coverage limits unchanged.
  - PR21's LIT482–561 assignments do not touch this topic's LIT582–593, but include them in the reservation refresh.
  - Check every literal OLD block again after the merge: PR21 and PR25 changed shared registries. If an OLD block no longer matches, stop and reconcile; never overwrite another topic's text.
- **Numbering.** This handoff replaces 09. The Claude preparation audit therefore becomes **handoff 11**.

## Task

Work in this order. Record exact commands and results in LOG.

1. **Start.**
   - Read the rules at the branch head and record the SHA.
   - Fetch main and the topic branch.
   - Merge current `origin/main` into this already-pushed branch. Never rebase or force-push.
   - Delta-read what main changed: PR25 registers Padua local-descent and boundary-profile results and touches the shared registries. Record the result.

2. **R2 fixes from [audit-02](../audit-02.md).** Apply each fix additively. Never edit audit-01/audit-02 files or earlier handoff bodies.
   - **R2-1:** add the "neither contains nor is contained in Hres" clause wherever L3-01's model is called "stronger" (locations in audit-02).
   - **R2-2:** add a literal additive PD-T143 cross-reference block to L3-01's adaptive corollary (9), scoped to model (1). Alternatively, make it a tracked checklist item.
   - **R2-3:** add a dated erratum giving the G5 receipt as first preserved at `844e812` (blob `6b811daa…`), with a same-commit caveat for L5a. Apply it in gate-timing-response-01, response-01 (by addendum) and LOG.
   - **R2-4:** state the L3 constant survival as verifiable from `0574c47:attempts/L3.md`, and limit the `cdcf…` caveat to the intermediate draft.
   - **R2-5 (as amended above):** change results line 12 to say the deviation was accepted by AC on 2026-11-05 (disclosed, not waived, not cured), and refresh the ROOT RESULTS proposal block.
   - **R2-6:** fix the LOG header IDs (PD-T L4-01 alias L4a; PD-N L4-01) and complete the claim list.
   - **R2-7:** add pointers to the root's executed n1 recipe and `evidence/response-n1-recheck.json`.
   - **NOTEs:** record a disposition for each audit-02 NOTE (accept, decline or defer). Include the preserved audit-01 logs (R2-8) in the inventory.

3. **Reservation refresh**, following WORKFLOW "Reserve fresh ranges; never reallocate".
   - **Read** main and every open PR (drafts included): their ledgers, the final IDs they use, and every retired reservation.
   - **Ranges:** the permanent ranges T324–363 / N116–131 / IDEA414–453 / LIT582–593 (first published at `40b3eb6`) stay as they are; never shift or reuse them. Also record PR25 (merged), PR26 (merged) and PR21 (open).
   - **If more IDs are needed,** reserve a fresh range by the same procedure and record it in ALLOCATIONS.md and the PR body.

4. **Final IDs.**
   - Assign final IDs from the reserved ranges to every provisional record.
   - Candidate proposals (19 IDEA, 16 PD-T, 3 PD-N) apply only if there is no duplicate or equivalence. The L6-02 contract and L4b are not new IDs (IDEA-262 contract; IDEA-250 variant).
   - Keep every provisional→final mapping and alias, including the historical L1a/L3a/L4a/L5a–d/G1-fit/L7 spellings. Put the canonical numeric agent-qualified provisional IDs in ID_CROSSWALK.
   - AC's L5 rule and PROT-12 apply: whether light negative records get separate PD-N IDs may be put to AC. Do not merge or drop a scoped negative record silently.

5. **Registry application.**
   - Apply the literal OLD→NEW blocks of [registry-proposals-response-01.md](../registry-proposals-response-01.md), with R2 fixes and final IDs substituted, to PROOF_STATUS.md, state/IDEAS.md, state/CURRENT.md, ID_CROSSWALK.md and this topic's own RESULTS.md section.
   - Each OLD block must still match byte-exactly at the merged base. If one does not, stop and reconcile; never overwrite another topic's text or section.
   - Status changes stay limited to the audited ones:
     - PD-T140's target part becomes PROVED; its experiment stays MEASURED/INCONCLUSIVE.
     - Every original OPEN target keeps its status and wording.

6. **Integration checks.**
   - Rehearse sequential squash integration in a disposable local branch if relevant, without touching main.
   - Registry consistency checks: duplicate IDs, header/status agreement, broken links.
   - Manifest regeneration, JSON/size checks (<16 KiB per generated file; repository JSON total well below 5 MB) and `git diff --check`.

7. **PR24.** Update its WORK/AUDIT/PR sections: audit-01 FINDINGS REQUIRE WORK → response-01 → audit-02 ACCEPTED WITH MINOR FINDINGS → preparation, with the Claude preparation audit PENDING. Keep the PR **draft**. Record **A-P1 accepted by AC on 2026-11-05**, with the disclosure retained.

## Read first

- Rules at the branch head.
- [audit-02.md](../audit-02.md) and its family reports [TXT](../audit-02/TXT.md), [EVD](../audit-02/EVD.md) and [GATE](../audit-02/GATE.md).
- [audit-01.md](../audit-01.md) A-m5 and PROT-7/12/13.
- [response-01.md](../response-01.md), [registry-proposals-response-01.md](../registry-proposals-response-01.md) and [ALLOCATIONS.md](../ALLOCATIONS.md).
- [gate-timing-response-01.md](../gate-timing-response-01.md).
- WORKFLOW's sections on reservations, retired reservations, priority/collisions and splitting.

## Scope limits

- Do not edit `audit-01*`, `audit-02*` or earlier handoff bodies.
- No new scientific claims, status upgrades beyond those audited, tolerance changes or new runs. A rerun is allowed only where a re-pinned checker requires it; record it.
- Do not reopen accepted mathematics.
- **Original OPEN targets stay OPEN:** PD-T055/F, broader L3 (degree-uniform/efficient selection), PD-T056(G)/corrected models, U2 and full G3 (n6–8; handoff01 n3–10), scalar/IEEE activation, and the disclosed external-code/literature tasks.
- Do not mark the PR ready. A-P1 is already decided by AC; do not reword the decision beyond recording it.
- Allowed scope: this topic, its results file, the shared registries changed only through the audited literal blocks, ID_CROSSWALK/ledger links, and the main merge.
- Not allowed: pushing to main, merging, force-pushing, tags, `.github/` changes, or computation on external machines.

## Acceptance and outputs

- R2-1–R2-7 are fixed, and every NOTE has a recorded disposition.
- Main is merged and the reservation refresh is recorded.
- Final IDs are assigned, with complete mappings.
- The literal registry blocks are applied exactly. Integration checks pass, with commands recorded. PR24 is updated and still a draft.
- When done:
  1. Commit the outputs.
  2. In a following commit, set this handoff to `done in <output-commit-sha>` and add `11-prep-audit.md`.
- **Handoff 11** is for Claude, Opus 5.5 high: an audit of the preparation. It covers registry application, IDs and reservations, crosswalk and splits, and integration checks against the exact preparation head.
- That audit also checks that AC's A-P1 acceptance is recorded accurately. If it passes, readiness still needs AC's merge decision. Only AC merges.
