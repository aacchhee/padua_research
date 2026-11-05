# Handoff 06 — PR22 preparation protocol check

- Status: done in 751d47debdfd716eb4054d69e4a47c6e50dcdf65
- Previous handoff: 05-pr-preparation.md
- Next agent / model / effort: Claude, Sonnet 5.5 high for protocol review;
  Opus 5.5 high is also allowed at the auditor's choice.
- Role: independent protocol checker of audited preparation.
- Branch: codex/nn-mop-iep-20261103
- Input head SHA: `7881e1cf771a70cad94b835c0580c2e3d4f94ece`
- Main / base: `21dbfc90257b952d8923f6d01739d12aa8d6e0a1`
- Stage: PR
- Written by / date: Codex, 2026-11-05; exact orchestrator backend/effort
  unexposed. Preparation workers gpt-6.1-sol medium, supplementary checker
  gpt-6-astra medium, as dispatched.

## Task

Read rules at the branch head, log and handoff05. Fetch current main/topic and
record source/rule SHAs. Claude audit-02 accepted scientific content at
5b36f8f8ac5b3c9a426d22a9375155a2b4d86e1b. This step is a short protocol
check of approved editorial edits and final-ID/registry preparation, not a new
mathematical audit or campaign. Do not silently change audited claims.

1. Verify E1 terminal max-|d| wording is nonmonotone (Hahn N24=71.15), E2
   distinguishes marginal-only Jacobi data from shifted-line family/boundary
   data and says no C3 comparison. X1 attributes exact references to auditor
   audit-02 R4 at sampled N4,8,12,16,24; N32 remains precision convergence.
   These are the exact edits audit-02 allowed without scientific re-audit.
2. Verify the fresh scan, live PR classification and final map: unchanged
   permanent T286–293/N100–103/IDEA376–383/LIT562–573 first published a0abe8b.
   Assignments T286–290 (3PROVED,2MEASURED), N100 (MEASURED), IDEA376–379,
   LIT562–568. Unused gaps T291–293,N101–103,IDEA380–383,LIT569–573 remain
   permanent. No accepted ID is renumbered or foreign reservation used.
3. Check withdrawn provisional PD-N?nn-mop-iep-codex-01 has no final ID;
   split content goes to PD-T288/289 and the full original text stays
   historical. PD-N100 maps only the accepted former provisional N?…02.
   IDEA-117 records AC's resume and audited outcome, C3 remains deferred.
4. Review same-source deduplication: LIT420's separate FHV and ADY coverage
   addenda,346,119(related347),348(related117/118) are reused. PR21 at890f56c
   has no final assignments: no offsets from its provisional numbers were
   invented. Seven absent sources use562–568. All twelve aliases have local
   records and explicit coverage, with pinned PR21 correspondence where
   relevant. No unmerged PR21 file is required for the essential statements.
   Developer-verified primary locators are not relabelled as Claude-verified.
5. Check additive topic-only PROOF_STATUS/IDEAS/INDEX/CORPUS/CROSSWALK,
   CURRENT/PAPER_MAP/RESULTS and batch-ledger updates. Preserve every foreign
   section and inherited gap. RESULTS copies only this topic's results file
   with the necessary relative-link conversion. No completed prep task is
   presented as continuing research in the frontier; open questions stay open.
6. Compare accepted code/proof bodies and historical auditor files to the
   accepted pins. Changes should be ID headers/aliases, process-status
   metadata, E1/E2 and X1 only, plus preparation records and registry rows.
   No new scientific run was executed during preparation. Review the
   supplementary integration check as additional evidence, not your approval.
7. Execute the registration check below and inspect its assertions. Check
   the scoped squash-rehearsal receipt and any unresolved merge-order
   limitations. Refresh main/open PRs and reservations before a readiness
   decision; if heads advanced, record the impact rather than assume the
   frozen scan is still current.

```sh
python topics/nn-mop-iep-20261103/preparation/check_registration.py
git diff --check
```

## Read first

- AGENTS.md, agents/WORKFLOW.md, Claude roles.
- audit-02.md, handoff05, LOG.md, preparation/verification.md,
  preparation/final-id-map.json, reservation-check.md/reservation-scan.json,
  pr-population.json, literature-dedup.md/literature-map.json,
  integration-check.md, and the registration checker.
- Changed current summaries, canonical record headers/status metadata and
  shared registry/index/frontier sections. Historical auditor reports remain
  unchanged and retain their actual source-coverage limitations.
- PR22: https://github.com/aacchhee/padua_research/pull/22.

## Scope limits

No new mathematics, candidates, scientific runs or primary reading beyond
checking dedup metadata. A material discrepancy returns to the appropriate
Claude mathematical audit rather than approval as a protocol edit.
Never merge the PR, force-push, alter tags, touch .github or contact anyone.
PR22 remains draft during this check. Only AC merges. Raw pilot data remains
local/regenerable; no cold-storage delivery is claimed.

## Acceptance and outputs

Write preparation/protocol-check-01.md with checked SHA/hashes, actual model/
effort, coverage, commands, findings and limitations. If mechanical findings
remain, return a bounded Codex gpt-6.1-sol medium correction handoff07. Do not
silently fix developer files and call that independent approval.

If clean, confirm readiness only for PR22, update PR WORK/AUDIT/PR with the
protocol receipt and current base/head/reservation check, and mark ready for
review if appropriate. No other draft's readiness or AC merge order follows.
Commit outputs first; in a following commit close this handoff and add a short
handoff07 for AC's merge decision/finalisation, or close the topic if AC has
already merged and all assigned work is complete. Preserve exactly one open
handoff while work remains and push before replying. Only AC merges.
