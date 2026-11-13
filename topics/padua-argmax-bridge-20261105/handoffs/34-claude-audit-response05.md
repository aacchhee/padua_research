# Handoff 34 — focused Claude audit of response-05

- Status: open
- Previous handoff: 33-answer-audit05.md
- Next agent / model / effort: Claude, Opus 5.5, xhigh
- Role: auditor and topic orchestrator
- Branch: codex/padua-argmax-bridge-20261105
- Input head SHA: `26ab08d3d64eb29420752d4318fdb34a8ccdbbd0`
- Main / base: `b5388c25a2a5ccb8d0faf816ab87023cf347bcd3`, already merged
- Stage: AUDIT for material response05 changes; data/custody/budget limits remain
- Written by / date: Codex under AC's gpt-6-astra high request; serving metadata unexposed · 2026-11-13 Europe/Oslo

## Read first

Read current rules and your role, then handoff33, audit-05.md,
audit-05-manuscripts.md, response-05.md and the latest LOG entry. This batch
fixes existing code and explanations, with no new mechanism, theorem,
threshold or final-ID assignment; record that novelty-gate exception.

Relevant reports are supplementary-evidence-review-response05-20261113.md
and supplementary-manuscript-review-response05-20261113.md. They are
bounded Astra checks, not this required Claude audit. Code checkpoint is
074c7da; final paired TeX/Bib freeze is
`8937d3b723c09c004f49d3e565d0b02976713a37`; the pointer update follows in
26ab08d. BUILD.md files give exact new artifact hashes and commands.

## Focused task

Audit material response05 changes only. Audit05 accepted the earlier
mathematics; do not repeat unchanged whole-component or whole-program
audits merely to add a round. Review both revised texts where changed.

1. **E5-01:** reconstruct the producer-file allowlist fix and receipt schema.
   The reader accepts only the registered empty preserve lock and valid
   producer storage receipts. Check a real deduplicate→completed→export→reader
   synthetic round-trip and the malformed-data controls. The positive
   fixture has explicit source/trust, arithmetic and sampled-closure
   adapters: it is storage compatibility evidence, not canonical-data or
   proof-arithmetic acceptance. Check optimization refusal, external pins
   and strict parser/linkage behavior remain intact.
2. **E5-02 / E5-04:** check the analytic optimization guard and explicit
   log(pi)>11/10 assertion. The normal eleven-field receipt is unchanged
   on the recorded runtime; historical receipt/preregistration is preserved.
   Review the runtime bit-pattern probes and independently challenge
   FTZ|DAZ/rounding sensitivity as useful. Scope remains finite/prospective,
   not universal IEEE certification or a historical worker's mode.
3. **Changed analytic explanations:** verify rho>=pi-v at omitted collisions,
   restored prefactor/wrap/primitive/amplitude reasons, the psi/trapezoid/
   recurrence/kappa steps, the cell-width and local variable scopes, the
   base-table definition/provenance/order and the cosine-correction
   cancellation. No comparison constant or threshold changes. The new
   kernel equation label numbers an existing evaluation form.
4. **Custody/wording:** both texts now distinguish recorded witnesses from
   present availability and identify the missing new-range files/checks.
   IEEE model is assumed; bounds are proved under it. Corrected response04
   closures are documented, including the old supplementary B5/C1/C10
   retained-reason overstatements. Do not treat those old rows as evidence
   that the omitted lines survived the old freeze.
5. **Source/layout:** current pair is19 statements,86 numbered environments,
   120 matching built labels;58/152pages. Root and distinct reviewer ran
   source, archival and seven mutation controls. The reviewer actually
   inspected all twelve B5-02 tag placements at11/20/26/40/51/55 and the
   relevant figures/roles/base-table pages. No-overfull logs alone are not
   offered as equation-tag evidence. Check newly changed layout as needed.

Cheap independent commands (from repository root):

```sh
python3 -E -B topics/padua-argmax-bridge-20261105/code/local_onset512_campaign/check_reader_repairs.py
python3 -E -B topics/padua-argmax-bridge-20261105/code/onset512_analytic/check.py
python3 -E -B topics/padua-argmax-bridge-20261105/code/independent_phase_checker/runtime_probe.py
python3 -E -B topics/padua-argmax-bridge-20261105/companion-paper/check_correspondence.py
python3 -E -B topics/padua-argmax-bridge-20261105/companion-paper/check_correspondence.py --archival
python3 -E -B topics/padua-argmax-bridge-20261105/companion-paper/check_baseline_controls.py
```

The cumulative33-entry notation map targets24a98db, not already-renamed
ad908ac. It adds the missing F_0(hk) rename and cell-width rename. Root
also used a one-entry incremental cell-width map againstad908ac: content
alignment distinguishes the certificate wording, seven display-format
changes, new labelled kernel and nine unchanged index shifts. Do not
interpret index mismatches as changed mathematics or broaden a rename map
to conceal material edits. The exact new baseline passes independently.

## Evidence and authority limits

Actual onset512 ZIP, I25 bundle and related derivative/inventory/review
payloads remain unavailable. The selected320/384/458/510 checks and
cross-archive comparisons stay OPEN. AC does not know the I25 location;
do not ask again without new evidence. If inputs arrive, authenticate full
recorded identities and preregister the existing data-only checks in
audit-04/WHEN-INPUTS-ARRIVE.md after reviewing the new reader. No native
campaign or witness regeneration is authorized by this handoff. Do not
call a regenerated artifact the missing historical ZIP.

Original return/padua30 were authenticated and accepted at recorded scopes
in prior root/Astra/Claude executions. Current developer also checked
3,978 authentic old JSON records against the strict parser. No replacement
native run occurred. New data positives remain synthetic/adapted.

Historical PDF bytes and632MiB histories remain unavailable. No historical
PDF preservation, transfer or permanent custody is claimed. Earlier source
freezes and timestamped57/150 artifacts are preserved. AC requests retaining
and transferring histories if reachable; no connected prior-workspace
filesystem is available. Both data statements explicitly leave permanent
post-repair snapshot/DOI pending rather than citing a433c7d as current.

Budget: main alone9,733,758bytes; this topic's current classified share
2,000,636; union11,734,394. Including the topic's2,087byte FREEZE.md exception
gives11,736,481; conservative no-shrink bound11,756,141. The10MB cap is not
met. Neither original branch alone exceeded it; their union did. AC's
cap/storage/share disposition remains open. Do not remove/reclassify
another topic's evidence or invent a cold-storage destination.

No Syvert calls, scientific retries/rescues, threshold changes, native
engine/independent numerical checker changes, final-ID assignment or
shared-registry application. Old audits/preregistrations/receipts remain
unchanged, except expressly dated corrections already documented. P1–P4
and funding confirmation stand. AI declaration, ORCID, contributions and
draft marker remain AC's. No external contact/submission, settings/.github
changes, merge, tag or force-push. PR27 stays draft; only AC merges/publishes.

## Outputs and acceptance

Write audit-06.md, with a manuscript companion if useful: exact candidate
SHA/hashes, actual model/effort, commands and real exits, coverage, findings
and access limits. Use the third-and-later-round minor-in-place rule only
within its allowed wording/link/record scope; return material edits to
development. Preserve disagreements and do not silently fix then approve.

Update LOG, topic results and draft PR WORK/AUDIT/PR record accurately;
no readiness while evidence/budget/publication obligations remain. Commit
outputs first. In a following commit close this handoff done in that output
SHA and open the next numbered handoff; exactly one remains open while
work remains. Push before replying. Focused audit completion does not
close the missing-data, custody, source-deposit or AC budget decisions.
