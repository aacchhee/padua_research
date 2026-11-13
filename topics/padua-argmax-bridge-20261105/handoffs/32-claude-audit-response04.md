# Handoff 32 — focused Claude audit of response-04

- Status: open
- Previous handoff: 31-answer-audit04-and-editorial-batch.md
- Next agent / model / effort: Claude, Opus 5.5, xhigh
- Role: auditor and topic orchestrator
- Branch: codex/padua-argmax-bridge-20261105
- Input head SHA: `f81682557c104e18497d2e08278a99bb97572773`
- Main / base: `b5388c25a2a5ccb8d0faf816ab87023cf347bcd3` (merged at `941aa335e60ca7058c8a0113faa76e31217f4753`)
- Stage: AUDIT for the response; unavailable data checks remain blocked
- Written by / date: Codex under AC's gpt-6-astra high request; serving metadata unexposed · 2026-11-13 Europe/Oslo

## Read first

Read AGENTS.md, agents/WORKFLOW.md and agents/claude/CLAUDE_ROLES.md at the
current head, then the 2026-11-13 LOG entries, response-04.md, audit-04.md,
audit-04-manuscripts.md and their relevant finding reports. No novelty
mechanism is added by this response; document that scoped exception rather
than generating ideas or re-running the complete novelty campaign.

Inputs for this focused review:

- Final TeX/Bib freeze `ad908acb21d3589d85635618ff68f63dd01cfbca` in paper/
  and companion-paper/; respective BUILD.md files identify current PDFs.
- Reader repair at `b5a6946` and subsequent records. The current reader,
  runner and compact verifier hashes are in zenodo-deposit/README.md and
  MANIFEST.json.in. Use current trusted repository code, not the historical
  unrepaired verifier inside padua30.zip.
- supplementary-reader-review-20261113.md and
  reader-repair-execution-20261113.md, including actually executed commands,
  authenticated original-return inputs and missing-input limits.
- supplementary-manuscript-review-20261113.md and
  manuscript-duplicate-dispositions-20261113.md. These state precise review
  coverage, failed intermediate checks and restored unique reasons.
- pr-update-20261113.md and results/padua-argmax-bridge-20261105.md
  (the latter is repository-root relative).

## Task

Perform one focused substantive audit of material changes since audit-04.
Do not re-audit unchanged analytic components just to repeat the earlier
round. Review both revised manuscripts for AC's mathematical clarity,
definitions-before-use and named-tool criteria, with attention to the actual
changed proofs and exposition rather than only the code.

1. Reconstruct the restored scalar-max reasons, J1/J2 gate clauses, row
   average/atomic identities, strict-positivity interior qualification and
   closed-boundary continuation, termwise maximum/correlated saving,
   corner-loss chains and elementary-constant explanations. Confirm that
   notation changes preserve meaning and that no necessary reason was lost
   in the 19 C4C and 13 C4B duplicate-pair consolidations. The supplementary
   reviewer directly compared all 32 pairs to original24a98db, returned
   several omissions and reread every restoration; this is evidence, not a
   substitute for your own focused audit.
2. Check E4-01..04 repairs: no removable assertions, optimization refusal,
   strict production parser, pins before checker construction, external
   manifest/archive identity, unsampled pair linkage, exact member/type
   checks and enforced coverage output. Review prospective recipes and
   historical/current provenance wording. The runner has a new identity;
   historical run records are not retroactively attributed to it.
3. Rerun the cheap commands below independently and record exact inputs,
   exits and results. They perform no native degree campaign:

```sh
python3 -E -B topics/padua-argmax-bridge-20261105/code/local_onset512_campaign/check_reader_repairs.py
python3 -E -B topics/padua-argmax-bridge-20261105/code/independent_phase_checker/runtime_probe.py
python3 -B topics/padua-argmax-bridge-20261105/code/onset512_analytic/check.py
python3 -B topics/padua-argmax-bridge-20261105/companion-paper/check_correspondence.py
python3 -B topics/padua-argmax-bridge-20261105/companion-paper/check_correspondence.py --archival
python3 -B topics/padua-argmax-bridge-20261105/companion-paper/check_baseline_controls.py
```

4. Confirm the final source baseline update is separate from the committed
   TeX/Bib freeze, and that the paired mutation controls fail altered copies
   without changing manuscript files. The rename-aware scanner against old
   24a98db deliberately reports material differences beyond its literal
   map; do not count that as a rename-only acceptance or suppress differences
   with a permissive map. Actual pair and final strict baseline pass.
5. Review disposition accuracy, including explicitly superseded response-03
   FIXED claims, model/runtime disclosures, 471 distinct trees versus942
   records, native endpoints neither premises nor universally validated,
   Popen/ECHILD historical-exit limitation and the finite runtime-probe scope.

## Available and missing evidence

AC supplied padua30.zip (25,111,335 B, aac08e5f...) and the two parts of the
original return (joined36,045,486 B, b00fd57f...). Full hashes and original
part identities are in reader-repair-execution-20261113.md. Root and distinct
Astra independently authenticated all250 package manifest rows and reran the
repaired compact verifier:560 certificates/280pairs, exactly41..319 plus511,
complete_plan, sampled histories199/238, observed exit0. Three positive I25
endpoint substitutions at old n41 also pass in independent runs. If those
inputs are still locally accessible, an additional data-only rerun may use
the recorded one-run180CPU/240wall cap. Do not run package launch scripts.

**Still absent:** onset512-return-20261108.zip (81,602,992 B, da63280a...),
i25-evidence-20261108T112304Z.zip (2,843,611 B, d1d03156...), the382-proof
derivative/inventory/review ZIPs, historical PDF bytes and the632MiB unsampled
native histories. AC does not know where the I25 ZIP is. Windows Downloads
is not mounted here; tool discovery exposes no prior-workspace filesystem.
AC requests retaining/transferring histories if accessible, not accepting
their loss. No transfer or permanent custody is claimed.

Do not repeat an already answered request for the I25 location without new
evidence. If new inputs become available, authenticate their full recorded
pins and preregister the focused checks in audit-04/WHEN-INPUTS-ARRIVE.md
before execution: actual repaired canonical reader, selected320/384/458/510
I25 data checks and cross-archive witness identities. Do not silently
regenerate a new native campaign or claim a reconstructed bundle has the
missing historical ZIP identity. Missing checks remain OPEN otherwise.

Current 57/150-page PDFs build cleanly, with116 matching built labels.
Root inspected selected rendered pages. Original48/162 and51/147 source
freezes remain in Git; old PDF byte preservation was not retested. Full
--artifacts mode needs those original PDF files and was not reported as
executed. Current artifact comparisons were executed separately.

## Scope limits and authority

No Syvert calls, new native degree campaign, retries/rescues of scientific
failures, changed thresholds, final-ID assignments or shared-registry
application. Frozen scientific engine, finite witnesses, J01/J02 constants
and historical records remain intact. Do not edit earlier audits. AC's
funding confirmation and P1–P4 dispositions stand. AI declaration, ORCID,
contributions and draft marker remain AC's decisions. No external contact,
submission, merge, tag, force-push, settings or .github changes.

The current global generated-class bound is11,751,309 B (actual classified
sum11,729,562 B), above the inherited10MB cap. Most excess arrived from
already-published Padua3D files in main; no unrelated evidence was deleted
or relabelled. Report this budget/readiness limitation; do not remove another
topic's evidence or invent a cold-storage destination. No new range is
needed; reservations are unchanged and a union refresh is required before
future assignment/readiness.

PR27 remains draft. You may update its WORK/AUDIT/PR record after your audit;
do not mark it ready while material evidence, budget or review obligations
remain. Only AC merges or publishes.

## Acceptance and outputs

Write audit-05.md and a manuscript-focused companion record if useful, with
audited SHA/hashes, actual model/effort, scoped independent executions,
finding dispositions and data-access limits. Do not call supplementary
Astra review the required Claude audit. Apply the third-and-later-round
MINOR-in-place rule only within its permitted wording/link/record scope;
return material changes to development. Inspect actual final source/PDF
coverage and avoid a blanket correctness or custody claim.

Update LOG and topic results accurately, preserve draft status and the
missing-input/global-budget limitations, and record the exact next step.
Commit outputs first. In a following commit close this handoff done in that
output SHA and open the next numbered handoff; keep exactly one open while
work remains. Push before replying. No merge or publication request yet.
