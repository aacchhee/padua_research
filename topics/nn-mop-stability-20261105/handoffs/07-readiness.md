# Handoff 07 — nn-mop-stability-20261105 — Claude readiness check

New numbered handoff; earlier instruction bodies remain immutable. Only the orchestrator changes statuses or Git.

- Status: open
- Previous handoff: [06-g5-audit-prep.md](06-g5-audit-prep.md)
- Next agent / model / effort: Claude, Opus 5.5 high
- Role: independent readiness reviewer and topic orchestrator
- Branch: codex/nn-mop-stability-20261105
- Input head SHA: `dd092fb74b3030fe28dd8dd221ef59e0e80b2b72` (prepared outputs; the commit publishing this handoff comes later)
- Main / base: `f654e32daff27b6846849311092f6daebbbf235b`, already an ancestor; main and foreign PR27 were unchanged at publication check.
- Stage: PR (draft; readiness not yet accepted)
- Written by / date: Codex, requested gpt-6-astra medium; Solmedium preparation helpers and Solhigh statement-bearing registry helper; serving identities/effective efforts not independently exposed · 2026-11-06

## Task

Perform the proportionate readiness check, not another full scientific audit. audit01 accepted the substantive scientific scope; audit02 accepted response01; Codex independently audited Claude's G5 run. Review the preparation diff, confirm record hygiene, and refresh reservations. Only AC merges.

1. Read rules at current head, LOG's latest entries, audit01/02 dispositions, audit-g5-01.md, and preparation/id-map.json. The G5 audit was published at `80086a1af5d232c110f9c7c754d43b47332cbe71`, after separate in-place MINOR correction `05d7e9844e8ccc55f78450beccdf90516624a3e0`.
2. Review `git diff 80086a1af5d232c110f9c7c754d43b47332cbe71..dd092fb74b3030fe28dd8dd221ef59e0e80b2b72`, particularly the seven shared registries: PROOF_STATUS.md, state/IDEAS.md, literature/INDEX.md, ID_CROSSWALK.md, state/CURRENT.md, PAPER_MAP.md and RESULTS.md. Check the scopes/statuses/dispositions against accepted durable records, every provisional/natural alias and split/parent relation, no process stage in new registry content, and preservation of unrelated content.
   - 18 PD-T: T432–449; 7 PD-N: N162–168; 26 IDEA:530–555; one new LIT614, reuse567/568.
   - PD-T statuses:9PROVED/5MEASURED/4OPEN. PD-N:6PROVED/1MEASURED. OPEN T446/447 are copy/pair sub-target and bivariate parent; T448/449 preserve original sharp-growth and stable-solver targets. Supporting results do not make them PARTIAL.
   - Every deferred, equivalent, refuted, failed and abandoned candidate remains represented. IDEA090 and378 remain deferred with resume conditions;117 has the continuation pointer. The unallocated handoff naming-template placeholder is not a result.
   - Original seven shared files at414e781 are a useful comparison for full application: five were pure append, IDEAS changed only original090/117/378 pointers, PAPER_MAP changed only the original NN-row pointer. No foreign identifier/range was renumbered.
3. Confirm audit02 R1–R8 by diff:
   - dated canonical D6/D4 chronology below the AC-decision entry, with response01 parenthetical insertions marked as Codex text; D6 scan heading qualified;
   - finite Hahn Split from none and generic certificate dependency;
   - two-way parent/child relations;
   - verbatim handoff01 conditioning target quotation plus explicit reformulation/reason;
   - localized dependency wording;
   - first-axis(n,0) wording;
   - historical-only convergence/100dps comparison scope;
   - old source/checker pins explicitly historical at4e87fc0, current identities in manifest.
   No accepted statement, proof, threshold, input or numeric table was changed. Optional G-record alias/selfsplit/neither leftovers are corrected. All original result-bearing code, projection data and audit01/02/scripts are untouched.
4. Verify evidence-manifest.json identities, including its two input-inventory fields and listed additional_code_and_data. Original fields retain the campaign's823cf6a/b4d292e provenance; preparation_source_commit414e781 and preparation/source-inputs.json identify this input snapshot. The manifest's69 file rows include the new G5 driver/comparison code/output, audit output/inventory/checker and preparation data; no new prose checker pins. The original collector covers its historical glob set; do not discard additional rows by blindly running that collector alone.
   Re-run the small relevant checks if useful:

```sh
python topics/nn-mop-stability-20261105/code/conditioning_verify_normality.py
python topics/nn-mop-stability-20261105/audit-g5-01/check.py
# If AC's ZIP is present:
python topics/nn-mop-stability-20261105/audit-g5-01/check.py --archive <IEP-MOP-main.zip>
```

   Normality should pass61 sizes/43,676 checks/code pins; all61 original receipt table rows remain unchanged, with final-ID/record metadata only. G5 artifact checker checks committed auditor outputs and optional full27-file archive identity; it explicitly reports paper_table_verified=false. This checker was added as audit reproducibility support, not a new external algorithm or scientific claim. Current projection fixture SHA remains37c3c060ad42cad679a78f256d9a5bdf5c129ed338cc8dcda9afbae6a5fef23f; its12 cases were accepted in audit02 and need no new full fit.
5. G5 scope/limitation:
   - AC's ZIP SHA256cdd0e98d2b411f24cfcecb49d83e16f9d50a7622a0d4f0d3eb17eb334a405145,1,020,330bytes,27 regular files/33 total entries, MIT. Source Git revision unknown; no third-party code/data committed.
   - Claude Octave8.4 source run and Codex independently inspected/reran all52 paper family/size cases with isolated Octave9.4/reference BLAS. Selected Krawtchouk paperN10 (11nodes), IEP_CORE decade gate passes: auditor2.691214553706643e-10 vs developer-quoted paper6.851191e-10, log10ratio-0.4058177524. Developer gave1.772147e-9, +0.413. Full tables vary; no bitwise/all-size/platform reproduction claimed.
   - **Direct paper-source table/hash authentication and cmp.py against that bundle were not rerun by Codex**: its arXiv GET received CONNECT403. Those parts remain review only and attributed to Claude's f736e8f03b536382141c2c98620c3cd408e0ff2c772ce58f47030e944864d461 bundle record. If you have that bundle/access, verify hashes and the selected ordinate/comparison; record actual execution. If unavailable, preserve the explicit unresolved NOTE for AC without inventing an independent paper-data rerun.
   - Required current wording: G5 reproduction gate PASS(one configuration, Octave8.4, to the decade); large-N variation measured; topic-metric comparison not yet run. The NN fieldwise metric is distinct from the step-line matrix2-norm. G4 never PASS; no general stable algorithm or sharp matching growth theorem.
6. Refresh the full reservation union against current main and **every** open PR (drafts included), ledgers/used IDs/retired reservations, plus newly closed-unmerged PRs if any. Preparation checked mainf654e32, PR27`4b728b04216a5490910780bc609a82b853058426`, ownPR28`80086a1af5d232c110f9c7c754d43b47332cbe71`;27 closed PRs all merged,50 ledger/registry copies via18 distinct blobs. Preparation receipt and ALLOCATIONS record exact hashes/heads. Assignedmax T494/N178/IDEA584/LIT630, reserved/gaps/retiredmax T501/N180/IDEA589/LIT632. Our earlier permanent reservation stays T432–471/N162–177/IDEA530–569/LIT614–629, with unused gaps unchanged. Refresh rather than inherit the old check. Main/peer drift requires impact/base reconciliation without rewriting history.

## Read first

AGENTS.md, agents/WORKFLOW.md, agents/claude/CLAUDE_ROLES.md; LOG latest/canonical entries; handoff06; audit01, response01, audit02; audit-g5-01.md and its receipt/source inventory/check.py; preparation/id-map.json, reservation-check.json, source-inputs.json and normality-check.json; relevant durable records and the shared diff; report, gates, results and PR28.

## Scope limits

Do not reopen unrelated accepted proofs, retune algorithms or rerun the complete conditioning sweep without a concrete issue. New mathematical changes or material findings require the scoped response/audit path; record hygiene should remain proportionate. From topic audit round3 onward, fix MINOR items allowed by WORKFLOW in place, list them and commit them separately from the readiness report. Preserve disagreements for AC.

Do not alter audit01/02 or scripts. Preserve scientific claim scopes and all provisional mappings. No new final range or foreign-ID edits without the full procedure. No source/paper-data commits, access-control bypass, Leuven contact or storage cleanup (topic about1.21MB, AC's no-cleanup threshold10MB). Approved GitHub noreply author exception persists. No main commits, PR merges, force pushes, tags or .github changes. No multi-PR integration/merge order is assigned by this handoff; only AC merges.

## Acceptance and outputs

- Write readiness-01.md identifying exact prepared input SHA, reviewed diff, actual checks, reservation refresh, dispositions and residual scientific/reference-data limits.
- Update LOG and PR28 WORK/AUDIT/PR accurately. Keep draft until readiness actually passes; if accepted, mark it ready only through supported preauthorized PR metadata operation and state the concrete decision requested from AC. A passing readiness must not imply the unrun NN comparison, closed sharp targets or full source-table reproduction.
- If findings remain, preserve draft and hand off the bounded response. If ready awaiting AC, record that state and a precise AC decision; do not merge.
- Commit/push outputs first, then in a following commit close07 as done in that outputSHA and create the next numbered handoff if agent work remains. If all assigned agent work is complete and only AC's merge decision remains, follow the closing-topic rule with no invented additional task. Preserve every earlier body and one open handoff whenever work remains.
