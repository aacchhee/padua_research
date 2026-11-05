# Handoff 05 — NN MOP IEP — PR preparation after audit-02 acceptance

- Status: open
- Previous handoff: 04-reaudit.md
- Next agent / model / effort: Codex, gpt-6.1-sol, medium (mechanical and registry preparation). Use gpt-6-astra medium for a supplementary integration check if wanted.
- Role: orchestrator (PR preparation).
- Branch: codex/nn-mop-iep-20261103
- Input head SHA: `a1ff14f8e89be268f0e0cfdd50d0f47bd319c708` (audit-02 output commit). Audited scientific content: `5b36f8f8ac5b3c9a426d22a9375155a2b4d86e1b`.
- Main / base: `5db1e01dcd2258f45de2adcaef43859e59734618` (merged at `9ec2a54`). Refetch first; if main moved, merge `origin/main` into the branch and record it.
- Stage: PR
- Written by / date: Claude, claude-opus-5-5 xhigh (independent auditor), 2026-11-05.

## Task

Prepare PR22 for AC's merge decision. [audit-02](../audit-02.md) accepted response-01 with no open mathematical, status or evidence finding. Read the rules at the branch head first and record the SHA.

1. **Editorial items from audit-02.** Apply them as worded; no re-audit is needed for exactly these edits.
   - E1: in c4-baseline-01.md, "Divisor diagnostics", correct "grows to … 6.47 (Hahn N32)". Terminal max |d| is not monotone: Hahn N24 has 71.15.
   - E2: in the results bullet "Known exact reduction; numerical question OPEN":
     - state that the marginal route (T?…04) needs only marginal Jacobi data, while the shifted step-line route needs the shift family plus boundary data;
     - replace "no C3/C4 floating-point comparison" with "no C3 comparison".
   - X1 (optional): narrow the receipt and T?…05 limitation "only N4 has an independent exact reference" to "exact references at N≤24 (audit-02 R4); N32 relies on precision convergence". Cite it as auditor-executed MEASURED evidence.
2. **Fresh union reservation scan.** Run the WORKFLOW "Reserve fresh ranges" procedure:
   - scan main, every open PR (drafts included), and closed-unmerged PRs and their retired reservations;
   - record heads and file hashes in a new compact receipt.
   Then confirm that the permanent ranges T286–293, N100–103, IDEA376–383 and LIT562–573 (first pushed `a0abe8b`) are still uncontested.
3. **Final-ID assignment from the unchanged ranges.**
   - **PD-T:** T?…01–05. PD-T?…02 and T?…05 are MEASURED; T?…01, 03 and 04 are PROVED.
   - **PD-N:** only PD-N?…02 (MEASURED; C2 REJECTED: refuted). PD-N?…01 is withdrawn: record it in ID_CROSSWALK as "withdrawn, no final ID", with split mappings to T?…03/T?…04 per SPLITS.md. Unused IDs remain permanent gaps.
   - **IDEA:** C1–C4. Also record the IDEA-117 resume and its outcome per handoff01: resumed on AC's request, gate stop, C3 deferred.
   - **LIT:** first deduplicate same-source records against live main and `claude/padua-literature-20261103` (PR21; e.g. FHV = LIT?padua-literature-claude-82 there). Do not allocate a second final LIT for a source PR21 already allocates; add an addendum or crosswalk reference instead, following the repository's existing same-source practice.
4. **Additive topic-only registry updates.** In PROOF_STATUS.md, state/IDEAS.md (a new NN-MOP section plus the IDEA-117 disposition), literature/INDEX.md, ID_CROSSWALK.md, the frontier/state files where applicable, and this topic's section of RESULTS.md (from results/nn-mop-iep-20261103.md):
   - never rewrite another topic's section;
   - preserve all inherited reservations and gaps;
   - keep the withdrawn provisional negative historical.
5. **PR22 body.** Update WORK, AUDIT (audit-01 findings → response-01 → audit-02 accepted) and PR (base/head SHAs, final-ID table, scan receipt, verification commands, remaining items, the exact decision requested from AC). Keep it draft until steps 1–4 are complete; then you may mark it ready for review. Do not merge.

## Do not reopen

- Any mathematics or status accepted in audit-01/02: T?…01–05, N?…02, the withdrawal, and the C1–C4 dispositions.
- No new candidates, novelty claims, runs or literature reading beyond what step 3's same-source deduplication strictly requires.
- Any change to a claim, proof, code or evidence beyond E1/E2/X1 is material and returns to Claude audit.

## Scope limits

- No merge, force-push, tags or `.github/` changes. Only AC merges.
- Do not contact anyone.
- Raw outputs stay local and regenerable.
- Shared registries change only as additive topic entries in this preparation step.
- If a collision or ambiguous priority appears, stop allocation in that namespace and ask AC.

## Acceptance and outputs

- Preparation commits: editorial edits, scan receipt, final-ID map, registry and RESULTS.md additions, and the PR body updated.
- `git diff --check` passes; registry consistency checked (IDs unique; provisional-to-final map complete).
- Commit outputs first. In a following commit, set this status to `done in <sha>` and add handoff 06:
  - if preparation stayed within E1/E2/X1 and registry/ID work, handoff 06 is a short Claude protocol check of the preparation (Sonnet 5.5 high or Opus 5.5 high, auditor's choice) or AC's merge decision, as WORKFLOW requires for registry-structure changes;
  - otherwise it is a Claude audit of the material change.
- Push before replying; preserve exactly one open handoff.
