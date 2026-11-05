# PR21 final preparation record

AC explicitly assigned Codex to finalize this PR, overriding the earlier Claude preparation assignment. Requested model/effort gpt-6-astra high; actual serving identity/effective effort are unexposed. This is mechanical preparation of literature already accepted by audits01–03, not new scientific development. The role redirection and its checkpoint timing are recorded in LOG and handoff12.

Rules/source head67b3e01e0109793e34d43b8c98d5f9064dc568f0. Current main9322fba83eb8d942e04209bb3262ad15d52bfb1e incorporates PR25 and26. Published integration commits c1a99f8 (main330fab8) and65b2497 (main9322fba) preserve the audited topic files; preparation input checkpoint4a8acf7 records AC's assignment. No main branch or tag was created/changed. The isolated checkout was hydrated through read-only GitHub GETs with exact real Git commit/tree/blob identities because the shell proxy was unavailable; no artificial Git replacements were used.

## Registration and application

- [Final map](final-id-map.json): all58 provisional aliases;31 new statement IDs LIT482–512 and27 same-statement reuses. LIT513–561 permanent unused. The source-statement distinction and grouped coverage rationale are in [deduplication](literature-dedup.md). Accepted PR22 aliases and both distinct source halves of LIT420 remain intact. Local numeric suffixes were not treated as offsets.
- [Fresh allocation scan](allocation-scan.json):39 complete registry/ledger copies across current main/open PR21/24, including inherited and retired reservations; all returned closed PRs merged. Highest qualified LIT mention597; no collision with unchanged own range482–561. First reservation publication remains fe946c9701916dce042af48c0e2705eac9d87db9. No new range, PD-T/PD-N/IDEA assignment or mathematical status change.
- [Application receipt](application-receipt.json):60 parsed literal blocks;35 changed targets,31 new canonical INDEX rows and27 reused-statement coverage bullets. The explicitly conditional old-report paragraph1112 is omitted as permitted; its update is in P2 comparison. The earlier blocked-AMS note is historical; later audited Xu/Dunkl supplements are linked from the canonical records.
- [apply_records.py](apply_records.py) computes all literal/manual operations before writing and preserves existing coverage cells/PR22 additions. [finalize_metadata.py](finalize_metadata.py) installs ID labels/crosswalk/own results and administrative appendices. These are initial application helpers, not idempotent whole-repository migrations.
- Existing same-key CORPUS entries receive coverage appends, not duplicate keys. Reused INDEX IDs retain one canonical row, with full newly read scope in coverage bullets. New source-record headings retain provisional aliases and original scientific bodies. Existing source/rule/audit history is preserved.
- Final rendering fixes rebase root RESULTS links to its own directory, escape mathematical absolute-value pipes in the new INDEX table, and give appended seven-column CORPUS rows their own table. These change presentation only. The checker verifies the root/topic results equivalence after link rebasing.

The application helpers and receipt describe the operation before the final presentation normalizations, implemented reproducibly by render_tables.py after finalize_metadata.py. The final diff, registration checker and independent preparation review are authoritative for the resulting tree. No new source reading, numerical run or theorem proof is claimed. Earlier independent SVZ and literal-block reruns remain at their recorded pins.

## Acceptance boundary

All F1–F7 were resolved by audits02/03. Source-reading VERIFIED labels credit the original developer, not independent auditor verification of inaccessible journal/image/NTNU/Crossref material. The finite-p journal Xu claim, journal SVZ locators, Pimenova/Kuznetsova images and other specifically qualified readings remain developer-verified where auditors could not access them. No exhaustive novelty, source-theorem proof, manuscript acceptance or submission readiness is inferred. Historical mathematical-status language in the comparison memos is not a replacement for current PROOF_STATUS and newer accepted PR25/26 scopes.

## Verification and review

Run from the repository:

```sh
python3 topics/padua-literature-20261103/preparation/check_registration.py --repo .
git diff --check
```

Checks cover all58 aliases/new IDs/gaps, preservation of untouched canonical rows and every existing corpus key, record body preservation modulo registration labels, immutable audits/rules, unchanged PD statuses/IDEAS, exact foreign-section prefixes, own results with link rebasing, new local links, JSON size limits and a conservative whole-repository generated-output inventory. The registration check and independent preparation review passed; see registration-check.json and protocol-review.md. The disposable integration rehearsal passed against current main and current PR24 (integration-rehearsal.json), preserving all78 prepared files and current protected statuses. The final live refresh retained main9322fba and found only open PR21/24; PR24's allocation delta only imports already merged PR26. No new LIT overlap. Administrative completion records do not change the reviewed scientific/registry bytes. All assigned preparation work is complete; publish this result, close handoff12 in the following commit and mark PR21 ready for AC review. Only AC merges.
