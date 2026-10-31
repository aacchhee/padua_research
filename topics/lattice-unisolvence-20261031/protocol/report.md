# Supplementary protocol and evidence review

Rules read at `9444c274d1ac06ef3b047e7bf2f9531d22b6d744`; final scientific head `61dcbe5e5a9a020810c0b8a9be974e1eba98f0ca`. Rules are unchanged from original `d36722823441dc40c6e19d69a174459348dd309c`. Reviewer: separate Codex agent, assigned **gpt-6-astra medium**, confirmed by orchestrator; runtime model/effort independently unexposed. No ultra. No Git mutation, fetch, acceptance decision or scientific edit was performed by this reviewer.

**No unresolved finding in this protocol scope. Required Claude audit remains PENDING.** This supplementary review neither replaces Claude nor asserts merge readiness or mathematical acceptance. Scientific reconstruction is separately recorded in [the Astra report](../independent/report.md). The scope adds no novelty content; the full IDEA novelty audit is assigned to that independent mathematical reviewer, while this review checks schema coverage and retention.

## Exact target and reproducible checks

[Snapshot](snapshot.json), SHA-256 `062ad98a6cb689c6b78126f50e76763c0d1e0b21f9398227899d27755b171d3b`, records exact reviewed campaign and shared-registry file hashes/bytes. It excludes this protocol envelope to avoid self-reference. Its global-manifest digest records the **pre-envelope checkpoint**, not a claim that the later enclosing manifest is byte-identical. Root may regenerate that manifest without changing the frozen scientific ZIP. [Final checks](final-checks.json) records independently checked archive identity and branch/rules/stage results.

Actually executed:

- `python topics/lattice-unisolvence-20261031/protocol/check_protocol.py > topics/lattice-unisolvence-20261031/protocol/snapshot.json` after the final freeze; the committed checker performs local-link, SHA-256, C0-row, historical Git-byte and size screening.
- Separate Python `zipfile`/`hashlib` verification of ZIP CRC and all 160 enclosed manifest entries' bytes, SHA-256 and Git blob hashes, without relying on the developer's check result. ZIP has 161 entries including its own manifest. Nested independent/audit-targets.json is present; protocol envelope is absent as intended.
- Read-only `git rev-parse`, `git log`, `git status`, `git for-each-ref`, `git ls-files`, `git show` for the 18 historical integration byte identities, `git merge-base --is-ancestor` for original and current parent, rule-file `git diff`, and `git diff --check`. The latter passed. No mathematical computation is represented here as independently rerun.
- Python checks of the provisional map: 66 distinct IDs, all existing target paths, all listed in ledger and crosswalk; 21 theory IDs present in PROOF_STATUS, with 13 PROVED, 6 MEASURED and 2 OPEN. `git diff 317a265 -- state/CURRENT.md` confirms exactly one additive campaign paragraph. One exploratory map query initially treated all entries as theory and raised KeyError; the corrected query explicitly filtered PD entries and passed.

## Evidence, retained patterns and public sources

C0 has 5,061 distinct keyed trial rows, 4,610 count failures, and 451 admissible rows in exact bijection with catalogue IDs; orbit sizes total 77,616. The common IDEA fields plus dimension-family fields and keyed row overrides cover every retained trial. C1/C3 own candidate/outcome records preserve their narrower outcomes. A finite count failure is not relabeled as universal singularity. The registry preserves provisional scientific IDs per AC's explicit request; no competing final block was allocated.

All 113 checked source/output/historical-identity hash fields resolve, with no unmatched hash. Logical point-set digests were recomputed separately rather than mistaken for file hashes. C0 hashes.txt and the pre-envelope global manifest have no mismatches. All reviewed local Markdown links resolve, including the completed review reports; remote source availability was not re-fetched by this reviewer. Literature records/search log distinguish primary excerpts, abstracts, slides, unverified originals and pending-reference claims. They supply paraphrases and source locators, not imported proof status.

Tracked filename/format screening finds no PDF, HTML, EPUB, fulltext or extracted-source artifact, and manual review of the campaign literature records finds source summaries rather than third-party fulltext. This is not an automated plagiarism guarantee. Generated-extension inventory at staged checkpoint totals **3,071,540 bytes**, largest **535,225 bytes** (independent/c3-rerun.json); no generated artifact exceeds 1,000,000 bytes. The small protocol JSON envelope adds far less than the remaining 1.9 MB margin. Duplicate rerun outputs preserve independent execution provenance; files were not split to evade limits. Root must keep the final staged total below 5,000,000 bytes after enclosing-manifest regeneration.

## Storage, ancestry and dispositions

Final staged archive: **832,029 bytes**, SHA-256 `7b173b14f12eb73661e165e544f189a42faa13c08d94e957126a08eb7b7ba53a`; independently verified. COLD_STORAGE.md gives actual path, AC's Windows destination, generating/check commands, exact identities, retrieval procedure and retention limit. Essential scientific evidence is committed. Windows receipt remains unconfirmed; the parent's separate waiver is not passed off as this campaign's receipt.

Original base eb7bdcd and refreshed charter317a265 are ancestors of the reviewed head. Rule files are unchanged. Ledger preserves charter/MZ final reservations, named MZ allocation ownership, explicit lattice provisional reservations, refreshed member pins and charter-first dependency. Two historical merge commits lack trailers; LOG explicitly discloses their Agent/runtime metadata rather than rewriting history. Parent acceptance/status and campaign Claude audit remain separate. Direct squash rehearsal records are checked through pinned historical identities; the wider batch's ten conflicts and incomplete rehearsal remain explicit, not a passed integration claim.

Early findings were resolved by development: missing inherited remote-file links, mixed historical/current branch pins, owner ambiguity, current-vs-historical LOG labels, nested audit-manifest exclusion and archive-check recursion. Final storage uses a one-way scientific ZIP then protocol envelope. Remaining limitations are explicit: Claude audit, coordinated final allocations/member reconciliation, wider integration conflicts and unconfirmed Windows receipt. None is silently waived by this review.

Stage: **AUDIT**. Exact LOG next action verified:

`Claude (Opus 5.5 xhigh): Continue codex/lattice-unisolvence-20261031.`
