# Handoff 09 — padua-lanczos-drift-20261101 — narrow response to audit-03

- Status: done in 02bd97b892ed409ec64e9b281130c71a85e914e9
- Previous handoff: 08-reaudit.md
- Next agent / model / effort: Claude, Opus 5.5 high (mathematical scope and checker response)
- Role: developer/orchestrator; Claude responds to Codex audit
- Branch: codex/padua-lanczos-drift-20261101
- Input head SHA: `695506324de7d61812c00b0a2522d9f8434d87c1` (audit outputs; publication commit follows)
- Scientific candidate audited: `ea829d92d509f79326a1cc037844a1bac3b4de13`
- Main / base: `28aaa20861d08074b77efc74eaef75cdcb36234d` (PR14/PR16 merged)
- Stage: WORK; PR15 remains draft
- Written by / date: Codex, requested gpt-6-astra xhigh; resolved root runtime metadata unexposed · 2026-11-01

## Task

Answer only A03-L1/L2/L3 in audit-03.md and write response-03.md. The independent
re-audit resolved all ten audit02 findings; there are no remaining high/medium
findings. Record06's finite formal scalar theorem is accepted as PROVED, and
record05's explicit T24/rotQ24 factor-ten target is accepted as PARTIAL. Preserve
the MEASURED experiment, INCONCLUSIVE both-grid sufficient test and OPEN rotQ24
conjunct. Do not repeat accepted development or enlarge the claims.

1. **A03-L1: requested regeneration must require its files.** Fix
   `tracks/bivariate-lanczos/code/drift/e1_scalar_finite_check.py`, function
   `check_regenerated` (currently lines174–203). A supplied nonexistent or
   partially populated directory currently returns success despite absent
   required files. Make all four expected outputs mandatory when the option is
   supplied. Demonstrate absent-directory, partial-directory and complete-valid
   cases, and preserve successful committed-certificate checking without
   `--regenerated`. Make failure explicit in the result; a nonzero CLI status
   is preferable if consistent with its failure contract. Use additive compact
   response03 receipts, not edits to response02 evidence. If needed regenerate
   the two comparator uppers/two reproductions using record06/README commands;
   those raw files stay outside Git. Document actual runs separately from reused
   historical evidence. Update active checker/proof provenance only as needed;
   the accepted mathematical reduction does not need replacement.

2. **A03-L2: scope the reversal to the target it settles.** Record05's status
   table at line55 gives `U_BJ² <100 L_alt²` as a reversal for its written
   `K_BJ >10 min(K_alt,K_pivot)` target. That only refutes the named-alt target.
   Valid minimum-target reversal requires both comparator lower bounds, e.g.
   `U_BJ² <=100 min(L_alt²,L_pivot²)`, with bound conventions explicit. Or
   distinguish the two targets and state exactly which one the alt-only
   reversal settles. Preserve original wording/history and the accepted PARTIAL
   classification. No new capacity search is required. The audit's illustrative
   capacities9,1,1/10 show the logical error; they are not rotQ24 measurements.

3. **A03-L3: qualify IDEA17's outside-span assertion.** In
   `topics/padua-lanczos-drift-20261101/ideas-e3-e4.md:194`, using an independently
   built reference does not guarantee that the discarded component or normalized
   replacement difference is outside the stored span. Describe the external
   reference information accurately; condition an outside-span separation on
   its checked normal component. The displayed discarded component is before
   normalization. Preserve the accepted R17a/R17b recipes, gamma guard, deferred
   disposition, H17 hypothesis and no-run/no-novelty disclosures. Audit03/E34
   contains an exact orthonormal countermodel with gamma3/5, also checked in the
   independent script. No repair experiment is requested.

Update this topic's LOG/results summary to reflect the actual response and
pending bounded re-audit. Leave the root RESULTS section for PR preparation.

## Read first

- AGENTS.md, agents/WORKFLOW.md, agents/claude/CLAUDE_ROLES.md at fetched head;
  record its full SHA and actual configured/runtime-exposure metadata.
- Latest LOG, audit-03.md, response-02.md, checks/audit-03/E1.md and E34.md,
  their receipts/scripts, the checker, record05/06 and IDEA17's full entry.
- Full state/IDEAS.md and relevant predecessor entries/obstructions for the
  IDEA17 scope, following WORKFLOW. No new candidate generation is requested.
- Protocol report and audit03 manifest for frozen-file/pin and size limits.

## Integration and scope limits

Fetch main/topic/other open PRs before work; do not rewrite published history.
At audit03 main stayed28aaa and sole other draft PR12 was
`7f226c1cec873fd8069feae1f4749f13d95f5c9d`; root integration PASS, clean
merge-tree, squash tree equality,77 old theory files unchanged. Recheck current
state as needed. Existing integration_check.py is pre-preparation tooling.

No final IDs or scientific registry edits. Own ranges remain PD-T136–155,
PD-N062–071, IDEA-246–285, LIT-445–459. Do not edit original77 theory files,
prior audits/responses/reports/evidence or earlier handoff bodies. No main
commits/pushes, force-pushes, tags, PR merges or .github edits. Only AC merges.
Do not write results to Windows. Cold-storage delivery remains separately
pending; committed regeneration needs no hidden raw input. Conservative whole
campaign size before this handoff is4566509bytes; keep additions compact and
recount against decimal5MB/1MB limits. Do not delete history to free space.

## Acceptance and outputs

- response-03.md gives each disposition, exact changed inputs, commands actually
  run, negative/positive checker evidence, model/effort and remaining limits.
- Changes are narrow; accepted mathematics/status decisions remain intact.
- Update LOG, own results and PR15 WORK/AUDIT/PR sections; keep draft and mark
  independent acceptance pending for material changes.
- Commit outputs first, then in a separate commit mark this handoff
  `done in <output SHA>` and add handoff10 for Codex gpt-6-astra high bounded
  re-audit of the checker fix and two scope corrections. That audit should not
  repeat the full campaign. If accepted it opens PR preparation, retaining the
  final-ID/registry/proposal/tombstone/root-RESULTS/fresh-union requirements
  specified by handoff08. Keep exactly one open handoff and push before reply.
