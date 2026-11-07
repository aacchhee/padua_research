# Handoff18 — Claude audit of manuscript and completed results

- Status: open
- Previous handoff: 17-constructive-approximation-draft.md
- Next agent / model / effort: Claude, recommended Opus5.5 xhigh; record actual model/effort and choose appropriate audit depth
- Role: independent auditor
- Branch: codex/padua-argmax-bridge-20261105
- Input head SHA: 9cfddd2b36dffccd391daf2a3744945d328127ae
- Main / base: f70a260e5b5f9a01209dc8a05faabdcf8db1feeb
- Stage: AUDIT
- Written by / date: Codex requested Astrahigh coordinator, serving metadata unexposed; 2026-11-07

## Full pending audit, now with the requested manuscript

Carry out the ENTIRE substantive audit requested in preserved handoffs15
and16: sharp H, previous F/compact/G01 batch, chronology, actual evidence,
source comparison and readiness limits. That Claude audit has not been
performed. AC redirected it to a Constructive Approximation paper draft;
WORK17 is now complete. Do not mistake the supplemental Astra checks for
a completed Claude audit or waive original findings. Read15 and16 fully.

The new paper adds faithful exposition of those established results, not
a new research campaign. AC permits intermediate IDs until PR and asks
for an accessible conceptual main narrative, with heavy estimates only
supporting it. The attached Morrow–Patterson CA paper guided the opening's
pacing; no thirdparty paper text was copied into Git.

## Read and check

Read rules/Claude role/current LOG, paper-positioning.md, the full pending
audit inputs of15–16, and paper/{README.md,main.tex,BUILD.md,references.bib,
review.md}, all paper/sections/*.tex, and template provenance.

The exact manuscript TeX/bibliography source commit is
a948b24c3faeba1e475ce64f4c7fc9d4123d42a5. paper/review.md pins16source
files, accepts consistency with canonical statements/proofs, and explicitly
excludes exhaustive upstream reproof, Claude acceptance and readiness.
Root verified every pinned file size/hash. Review original proof records
as needed rather than assuming this source-fidelity check proves all
compressed derivative/mesh estimates. Its corrected findings include MP
upper-bound attribution, corner-leaf quantifiers, phase pi² factors,
model definitions and damaged TeX parity/roman escapes.

The paper has two main results: analytic sharp corner expansion with
-1/N and O(logN/N²), both parities, and exact global parity-correct
nonnode-corner maximizers for all n>=2 with explicit computer-assisted
dependencies. Core corner proof assumes neither argmax nor numerical
constant enclosures. Global transfer and effective tail retain G01's
trust/PD271 dependencies. Do not erase those by observing that scalarH
maximum is analytic. Old PD098/099/shared statuses remain preserved pending
reviewed registration; no new final IDs were assigned.

New appendices contain full corner quadrature/centering, finite-row and
model identities, scalar maximum, pole norms/reference matching, defect
floors, exact physical cover, tail inequalities and certificate predicates.
Check their standalone definitions, quantifiers and arithmetic, especially
compressed row/model estimates. Verify no internal ID is used to conceal
a missing published/fully written premise. Assess whether technical
support and the main narrative fulfill AC's conceptual exposition request.

## Compilation and template boundary

Run from repo root:

```sh
bash topics/padua-argmax-bridge-20261105/paper/build.sh
python3 topics/padua-argmax-bridge-20261105/code/evidence_index.py --check
```

Actual root converged build:88pages, appendices begin18; no unresolved
references/citations, multiply-defined-label warnings or overfull boxes.
First two rendered pages were inspected. PDF837560B SHA256
668a96ad2d314099180537925b7a398230d58c450de26ae2f1c51de6c47cbc10
is a regenerable offGit local artifact; BUILD.md gives exact locator,
command and TeX versions. Source, not PDF bytes, is pushed.

Actual Springer sn-jnl v3.1 interface is used; official downloads returned
403, so class/BST are pinned from a documented public mirror, not byte
compared against the inaccessible official archive. They remain offGit.
CA requires alphabetically ordered numerical references; the10entry
ordered nocite list implements this with the unchanged publisher BST.
Check the journal/provenance and bibliography scope without claiming
submission or editorial approval. Authorship/human declarations, final
AI assistance wording, durable public release and final paper preparation
remain explicit. No editor was contacted and no submission was made.

## Scientific evidence and limits unchanged

Existing source/engine/scienceFREEZE/return identities and actual native
checks in15–16 are unchanged; manuscript work ran no new scientific
numerical jobs. All560 returned essential rational proofs were checked
locally; only199/238 have sampled complete histories/fresh local native
replays. Unsampled full histories remain Syvert-local by AC's explicit
retention policy. No statistical inference or complete raw cold retention
is claimed. Data availability correctly restricts the compact-return
coverage statement to41–319 (and recorded control511 elsewhere), not
inherited2–40. Preserve canonical protocol deviations in LOG.

Conservative tracked-generated bound9707846B<AC10000000B; essential
index372entries/30593B PASS within reviewed32KiBexception. No bulk PDF,
class/BST, source papers, archives or build logs committed. Existing
permanent ID reservations unchanged; refresh live/retired reservations
only when final IDs/readiness are actually prepared.

## Outputs and boundary

Write audit-03.md (or next appropriate audit record if another current
record intervenes), identifying exact candidate/scope/model/actual checks,
findings and dispositions. Follow the later-audit MINOR-fix rule; return
material findings to development. No whole-batch readiness follows from
a clean narrow manuscript check. No new research campaign or mass rerun
is requested. Keep draft PR27 unready until actual audit/preparation.

Commit actual outputs first; then only18status and new numbered successor
in a separate commit, push before final. Preserve all earlier handoff
bodies. No main push/merge/force/tags/.github/settings change. Only AC merges.
