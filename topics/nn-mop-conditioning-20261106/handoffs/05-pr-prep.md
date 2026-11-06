# Handoff 05 — NN MOP conditioning — PR preparation

- Status: open
- Previous handoff: [04-reaudit.md](04-reaudit.md)

- Next agent / model / effort: Codex, `gpt-6.1-sol` medium. Use high for the PD-T448 PARTIAL registry wording if needed.
- Role: developer and topic orchestrator for PR preparation
- Branch: codex/nn-mop-conditioning-20261106
- Input head SHA: `e6c596f678faced08e4b2f9a2f329994128804c6` (audit-02 output commit; this handoff is published in the following commit)
- Accepted scientific content: `cc1edd2` as amended by response `b3350ad` ([audit-01](../audit-01.md), [audit-02](../audit-02.md))
- Main / base: `76ba4214b100c86a44941f5e9a662ce9ce48efb8` at audit time. Refresh it, and merge `origin/main` into the branch if main has moved; never rebase or force-push.
- Stage: PR
- Written by / date: Claude, Opus 5.5 xhigh · 2026-11-06

## Task

1. **MINOR fixes.** Fix [audit-02](../audit-02.md) MINOR-1 to MINOR-5, MINOR-8 and MINOR-9 as listed there, in a short `response-02.md` table.
   - Each fix must be a wording, record or link fix only, with no change to a claim, status, proof, threshold or result-bearing code.
   - MINOR-6 and MINOR-7 (c4_compare.py hardening and response_code_checks.py reproducibility) are optional. Either record the limitation in external-code.md, or change the code. A code change is material: show the healthy payload and the 14 table bytes unchanged, and flag it for a focused check at readiness.
2. **Reservation.** Run the full reservation check in agents/WORKFLOW.md (**Reserve fresh ranges; never reallocate**, steps 1–4) against current `main` and every open PR, including drafts and retired reservations.
   - Reserve fresh PD-T, PD-N and IDEA ranges, with headroom, for every provisional ID in [candidate-result-map.md](../candidate-result-map.md) and the theory files. Add LIT only if a new LIT record is created.
   - Record the reservation in `topics/nn-mop-conditioning-20261106/ALLOCATIONS.md` and in the PR body: namespace, range, count, branch, date and heads checked. Link it from ID_CROSSWALK.md.
3. **Registry application by reviewed diff.**
   - Assign final IDs, keeping every provisional alias. Apply the results to PROOF_STATUS.md, state/IDEAS.md, ID_CROSSWALK.md, state/CURRENT.md (if it reports this line), RESULTS.md (this topic's section only, from the results file, without the next-step line) and the topic results file.
   - Apply the PD-T448 **PARTIAL** classification from [classification-proposal.md](../classification-proposal.md) as NOTE-1 of audit-02 lists:
     - edit PROOF_STATUS.md :531 and :541, and ID_CROSSWALK.md :1605 and :1617;
     - in the predecessor conditioning-growth-target.md, update the Split-into line, cite the all-N Hahn normality in its assumption, and keep the earlier OPEN rationale as dated History;
     - preserve the original statement wording;
     - state how the D1 mechanism questions (History :64–69) are treated.
   - Record IDEA dispositions for the touched entries: IDEA-533, 535, 117, 090 and 531 as relevant, the C1–C4 candidates, the C2-03 r4/r5/r6 subforms and the gauge candidate. Keep all failed, deferred and equivalent candidates.
   - The refuted/failed PD-N rows need their `REJECTED: failed` dispositions and links.
   - Shared registries carry only claim content, status, dependencies, dispositions and links; no process stage.
4. **Finish.** Update the LOG and the PR #32 body (WORK / AUDIT / PR sections, the reservation and the decision requested from AC). Remove completed preparation items from any shared frontier.
5. **Hand off.** Commit and push. Then open handoff 06 for the **Claude readiness check** (Opus 5.5 high). That check is a reviewed `git diff` of the shared files against `main`, a confirmation of the MINOR fixes, and the reservation refresh at readiness. It is not a new audit round unless the application makes a material change.

## Read first

- AGENTS.md, agents/WORKFLOW.md (especially **Reserve fresh ranges**, **Retired reservations**, **Split results**, **Candidate dispositions**, **Proportionate audit and records**) and agents/codex/CODEX.md at the branch head.
- [audit-02.md](../audit-02.md), [response-01.md](../response-01.md), [classification-proposal.md](../classification-proposal.md), [candidate-result-map.md](../candidate-result-map.md), the results file and LOG.
- The current ledgers and registries on `main` and on every open PR.

## Scope limits

- Do not reopen accepted mathematics or measurements.
- Do not edit audit reports or earlier handoff bodies.
- Edit another topic's files only where the registry application above requires it (the PD-T448 predecessor record), and never another topic's RESULTS.md section.
- Do not touch `main`, `.github/`, rules, templates or tags. Never merge or force-push. Only AC merges.

## Acceptance and outputs

- `response-02.md` records the MINOR fixes.
- ALLOCATIONS.md records a collision-free reservation with the heads checked.
- The final IDs and the alias crosswalk are applied, and the registry diff is reviewed.
- RESULTS.md and the topic results file are consistent.
- `code/verify_evidence.py` passes, and the PR body is complete.
- Commit the outputs first. Then, in a following commit, set this status to `done in <sha>` and add handoff 06 (Claude readiness check).
