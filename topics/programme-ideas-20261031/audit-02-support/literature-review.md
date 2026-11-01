# Audit-02 supplementary review — registration, literature and input provenance

- Candidate/rules: `cadb35066160e466cb1704b9791ad6f374446422`.
- Auditor: independent Codex `audit_literature`; requested `gpt-6-astra xhigh`; separately resolved runtime metadata is unexposed.
- Date: 2026-11-01.
- Scope: audit-01 A7 registration/inventory, A8 reproducible source identity, A9.1–2 retention/coverage, and attribution of the recorded A9.8 disposition. Mathematical validation of newly stated theorems is assigned to the other audit components.
- No developer source, previous audit or Git state was changed by this agent. Only new `audit-02-support/literature-*` files were written.

## Decision

**Accepted in this scope, with the access/coverage limits below. No new blocking finding.** The missing campaign context and transferred source identities are now retrievable. All 159 history-backed source rows and five committed context/prompt rows independently match their declared bytes. All eleven theory records have matching provisional proof/crosswalk rows, and all twenty IDEA records have matching shared-IDEAS rows. This accepts the registration/provenance repair; it does not independently certify their mathematics, the original reading history or the Windows archive.

## A7 — durable claims and shared provisional registrations

`response-01.md:56–81` inventories substantive claims and justifies keeping minor routine identities/observations with parent IDEA records; its addendum at `response-01.md:123–130` adds the three new scoped negative records after AC's instruction to register negatives. The theory directory contains exactly PD-T provisional 01–06 and PD-N provisional 01–05. The independent checker verifies one canonical row in each of `PROOF_STATUS.md` and `ID_CROSSWALK.md` for every theory file, with the same status and resolving file link.

The current statuses are:

| IDs | Status in file and proof registry |
|---|---|
| PD-T?programme-ideas-claude-01–03 | PROVED |
| PD-T?programme-ideas-claude-04–05 | OPEN |
| PD-T?programme-ideas-claude-06 | MEASURED |
| PD-N?programme-ideas-claude-01, -03, -04 | PROVED |
| PD-N?programme-ideas-claude-02, -05 | MEASURED |

Original-to-split mappings are recorded in `ID_CROSSWALK.md:322–333`; the original broad claims are retained by the source-SHA locators and the response's inline corrections. The 20 unique topic IDEA IDs 01–20 each have exactly one shared-IDEAS row (`state/IDEAS.md:462–485`); their closest-predecessor, kill-test and retained-evidence details remain in the topic records. Rejected mechanisms are scoped separately from programme-level equivalence/abandonment. The PROVED/OPEN/MEASURED distinctions in the revised report are explicit and the status word `PROVED-in-file` is withdrawn. No final ID or acceptance is represented as already granted.

This is a check of complete, consistent registration, not independent approval of all eleven statements. In particular, the proof completeness of the positive-pivot Favard/dimension statement and new exact counterexamples must be resolved by the mathematical components of audit-02. Existing supporting finite measurements remain bounded; no original large sweep was rerun here.

## A8 — controlling context and exact source retrieval

`sources/campaign-inputs/README.md:5–20`, `provenance.json` and `COLD_STORAGE.md` repair the former path-only handoff:

- The five criteria and exclusions are in committed `CAMPAIGN_CONTEXT.md`; the three common task instructions and branch-snapshot note are also committed. All five match the manifest's size, SHA256 and Git blob. The six entries in `SHA256SUMS.txt` (including the producer script) independently verify.
- Every one of the 159 transferred snapshot/reading-record blobs matches its declared byte size and SHA256, and at least one listed immutable `commit:path` resolves to that exact blob. This includes all Lanczos transferred records after root fetched the recorded Lanczos head `4406ac029ec56d5c131321d9760bfc1271ccb87e`; current branch contents were not substituted for the recorded versions.
- The source producer intentionally lists commits adding **or removing** the blob. In 34 rows the first history hit is not the introducing version; each nevertheless includes a matching retrievable version. The audit receipt records a verified matching `commit:path` per row. Use that pair or `git cat-file blob <git_blob>` for retrieval rather than assuming the first history hit contains the file.
- The committed context is transparently identified as the final version with the web-access section appended. `README.md:17` discloses that the earlier Step 0/1 bytes were not preserved; the asserted difference is that trailing section. This limitation is retained, rather than falsely certifying the earlier full-file identity.
- Three source reports remain independently hash-identifiable. The actual private `RESULTS.md` and research notes are represented by the Padua-specific ZIP manifest, with archive size/SHA256, member sizes/hashes, generating/checking commands and custodian/retrieval instructions. They need not be committed to repair source provenance.

**Windows access limitation:** the stored ZIP is not present in this executor. I reviewed the manifest and its developer-reported bridge read-back receipt, but did not retrieve, inspect, extract or rehash the Windows file. The same applies to the listed original local PDFs. Thus A8's archival identity/procedure is documented; actual Windows retention/readability is not independently attested by this review. No computer-assisted proof is accepted on the basis of those unavailable private notes. No additional AC confirmation or public disclosure of private notes is required by this review.

The producer's frozen receipt identifies the declared input mirror; this audit proves the byte identity/retrievability of its listed rows. Neither receipt independently establishes that every listed source was historically read, or that unlisted saved web pages were captured. The revised source summaries keep those historical-reading claims attributed.

## A9 — counts, source coverage and recorded model disposition

The gate/report/LOG now consistently distinguish eleven original passing draft records from nine distinct adversarial candidates (two merged and seven single). Historical drafts remain retrievable at `25161235fe430ec05723796afe0f20a923a69ebd`; the 20 topic IDEA records and 111 literature rows remain present. The earlier independently checked 12-returned/8-not-returned split is preserved.

`report.md:23` and the §4 legend (`report.md:69`) now distinguish complete reading, selected sections and a WebFetch digest, and explicitly limit the audit's own source checks to primary excerpts. The source-specific limitations survive. This closes A9.2 at the summary level; it does not convert the 41 statement-level VERIFIED rows into complete readings or give exhaustive novelty/ownership clearance. The previously checked primary statements remain those of the version-pinned BDS maxima table/remark, KL leading asymptotics and KR planar border-basis chart; no fresh source search or PDF reading was needed for this re-audit.

`response-01.md:121–123`, `report.md:210` and the dated LOG addendum preserve AC's recorded instruction to disregard the model issue and register negatives. The earlier response section saying the disposition was open is identifiable as the pre-addendum history, superseded by that later instruction. The recorded acceptance does not claim Sonnet ran the campaign, rewrite model history or amend the standing allocation rule. This review accepts that scoped disposition as supplied task context; it does not claim independent access to an original external conversation receipt.

## Executed checks and identities

Executed successfully:

```text
python topics/programme-ideas-20261031/audit-02-support/literature-check.py > topics/programme-ideas-20261031/audit-02-support/literature-check.json
```

The independent script reads the candidate at the full SHA through read-only Git, checks all 164 provenance rows and six context hashes, resolves all history-backed file identities, compares all eleven theory status/link rows and checks the twenty shared/topic IDEA IDs plus 111 literature rows. Its output records input hashes and a verified immutable retrieval pair per history row. No Git mutation is performed. Neither this command nor source inspection is a mathematical rerun.

Rules, full current `state/IDEAS.md` including both new campaign blocks and obstruction/disposition tables, `literature/INDEX.md`, all eleven theory records, revised report/proposal/source summaries, response/addendum, original A7–A9 findings, context/snapshot note, producer/manifest and cold-storage manifest were inspected. No new mechanism, literature claim, shared-ID allocation or external message was generated.
