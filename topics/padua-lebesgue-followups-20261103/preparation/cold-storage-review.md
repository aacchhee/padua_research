# Independent cold-storage review — 2026-11-05

**PASS within the bounded storage/protocol scope. S1 is resolved by actual
archival reduction; no budget exception is needed for this candidate.**

Reviewer: distinct Codex subagent `/root/cold_storage_review`, configured
`gpt-6-astra medium`; serving metadata is not separately exposed. Rules and
source read at `40347d11071c81c1c633a2578cb52325bb92584a`; reviewed candidate
`4952cdd7e9f433ff40632d88cf2d319114ad7fdf`. Read AGENTS.md,
agents/WORKFLOW.md, agents/codex/CODEX.md, handoff05, the prior independent
review and storage assessment, the migration report, manifests/provenance,
selection inventories, affected verifier code and unchanged storage utility.
The cloud-environment runtime skill was read and current runtime queried.
No mutable Git operation or developer-file correction was performed.

This is the **bounded no-new-novelty exception**: moving existing generated
bytes adds no mathematical claim, mechanism, candidate, literature comparison
or priority claim. No new novelty campaign, mathematical proof review or long
mathematical rerun was needed or performed. Existing Claude mathematical
acceptance and the disclosed T2/T3 timing qualification are unchanged. This
supplementary independent check does not replace that Claude audit.

## Selection and preservation

The selected set is exactly **326 files / 1,155,908 bytes**: 277 raw process
streams, 15 generated numerical analysis tables, and 34 secondary captures.
The latter are 26 programme-ideas raw output tables with retained matching
adversarial/decisive summaries, plus eight bivariate timing/error companions.
I inspected the generated-table payload headers and the selection's retained
summary context, including finite-scope and historical correction wording.
This review does not independently re-establish the scientific results in
those summaries. Essential compact JSON/checker/control/global records,
JSON-shaped proof-attempts checker stdout, and PR17's expressly retained
scientific stdout summaries remain. All source and mathematical records stay.

Every artifact matches its source path, Git blob, SHA-256 and byte size at
40347d1. There are no duplicate paths. The 42 manifest components are actual
preexisting directories at that source, not partitions invented by byte size.
No artifact was split. Exact comparison of the deleted path set and manifest
entry set passes: every removal has one retrieval record and no other file
was removed. Prior machine manifests remain byte-identical; additions to
prior COLD_STORAGE.md files preserve their complete earlier contents.

The repository-wide storage verifier confirms **1,075 protected files
unchanged**, including mathematical records, source, audit reports and shared
scientific registries. Inspection of the complete modified-path list confirms
only storage documentation, this topic's LOG, .gitignore and the preparation
verifier changed among existing files. RESULTS.md and other topics' results
were not edited in this candidate. The unchanged cold-storage utility is used.

The sole relocation among this topic's original auditor files is the 1,019-byte
boundary-regeneration.log. Its SHA-256 remains
`3d13d4bff0089cb248bb2ddc3c0c8bee9bf0e86d2b8a2ea70f7ce9e5b0ba41d3`.
The registration verifier now retrieves absent paths only through explicit
manifest entries and validates source:path/blob, SHA and size before comparing
original audited bytes. It does not skip missing evidence. Its added-link
check similarly accepts only a verified archival target; fenced verbatim
historical command text is correctly excluded from rendered-link checking.
Neither scientific acceptance predicates nor recorded auditor results changed.

## Provenance finding resolved before the candidate

During preparation I raised a provenance concern: generic links to retained
records did not distinguish recovered original commands from unrecovered
history. The candidate fixes this with per-entry command references and explicit
status: **99 D** (recorded named-output invocation), **71 P** (partial argv,
input or script mapping), **156 R** (original command not recovered, exact-byte
retrieval only). All command references resolve in the component records.
I independently compared **142 frozen-command quote occurrences** and their
source blob identifiers with pinned Git content: all quotes are verbatim.

The boundary command is explicitly partial because stdout capture redirection
was not recorded. Missing details are not invented. Exact archival retrieval
is fully verified; universal command-level scientific regeneration is not
claimed. This is an honest limitation inherited from the original records,
not a reason to rewrite or discard them. No unresolved actionable finding
remains in this review's scope.

## Independently executed checks

From the repository root I executed, all exit 0:

```sh
python topics/padua-lebesgue-followups-20261103/preparation/verify_cold_storage.py --staging /workspace/scratch/padua-cold-storage-20261105-v2 --restored /workspace/scratch/padua-cold-restore-20261105
python topics/padua-lebesgue-followups-20261103/preparation/verify_registration.py
git diff --check 40347d11071c81c1c633a2578cb52325bb92584a 4952cdd7e9f433ff40632d88cf2d319114ad7fdf
```

Storage result: 42 logical manifests; 326 relocated files / 1,155,908 original
bytes; exact deletion map; all exports/restores verified; 1,075 protected files
unchanged. Registration result: 138 immutable inputs; nine unchanged
mathematical bodies; 123 manifest rows; nine unique mappings; other RESULTS
preserved; 757 added links.

I also independently executed `export`, `verify-archive --manifest`, and
`restore` for **each of all 42 manifests**, using fresh reviewer destinations:
`/workspace/scratch/padua-review-export-20261105` and
`/workspace/scratch/padua-review-restore-20261105`. All 126 completed commands
exited 0. Every exported and separately restored payload was read and compared
against its manifest SHA/size, and all source identities were checked against
Git. This is an independent archival rerun, not merely reading the developer's
receipt. An initial reviewer wrapper incorrectly expected an `accepted` field
in export output and stopped after its first successful export; the corrected
wrapper checked export exit status and verify-archive acceptance and completed
the full set. There was no utility or payload failure.

The manifest-set identity is SHA-256 of sorted
`<repository-manifest-path> <manifest-sha256>\n` lines:
`fed618215c96444542df63fff936fd5882751d35c63847e362bc5287cac874fa`.
All 42 current manifest bytes were also compared with candidate4952cdd.
Their total is **163,549 bytes**, maximum **14,271**, each below 16,384.

## Budget and remaining boundary

I independently enumerated `git ls-tree -r -l 4952cdd...`, excluding exactly
extensions md/py/sh/tex/bib/svg/gitignore as in the prior conservative inventory.
Result: **970 files / 3,859,377 bytes**. SHA-256 of sorted
`<decimal-size>\t<path>\n` inventory lines:
`f479f0c565a87ba14571bebcbe3fd68ce113dc22fdfeb5820a2a1edd594e7d30`.
The reduction is **992,359 bytes net**, including all 163,549 bytes of new
manifest metadata. Margin below 5,000,000 is **1,140,623 bytes / 22.81246%**.
No source or manifest classification subtraction was needed. This materially
resolves the former narrow-margin S1 concern and satisfies “well below 5 MB”
for this conservative candidate inventory without an AC exception.

I verified the transfer package's 458,735-byte size and SHA-256
`a0bc746b89e5d1300dcc01d8633e11c58a2ba96483b645b9aaf825c8ccdb000b`.
Physical delivery to AC's Padua folder remains **PENDING**, permitted by the
workflow's unreachable-destination route. Scratch is not guaranteed durable;
pushed historical Git blobs and committed manifests provide retrieval. No
history purge is authorized. Delivered archive integrity must be checked again
at delivery; this review does not certify physical receipt by AC.

The orchestrator still owns live reservation/population refresh, integration
impact checks and final readiness/lifecycle records. This report resolves only
the bounded storage blocker at the pinned candidate. Later material divergence
requires an impact check. Only AC merges; the prior T2/T3 qualification remains
confirmed and unwaived.

## Operational refresh inspected after the candidate

Read the appended reservation and integration refreshes. The live 23-PR
population (open20–24, all returned closed PRs merged) is the orchestrator's
fresh query, not a separate network query by this reviewer. Independently
compared every selected PR20 and PR23 registry/ledger file at the refreshed
heads to the preceding checked heads: all are byte-identical. This supports
the unchanged reservation/registration conclusion without manufacturing a
new allocation or repeating the already passed mathematical review.

I independently inspected the actual detached squash objects in the recorded
five-stage chain, checking tree IDs, consecutive parents, all nine protected
shared paths at each stage and every input's new paths against its source
bytes: counts **264 / 70 / 31 / 107 / 58**. All 326 archived paths remain
absent in the final tree. The final commit
`66658c610c83b182fd71fe1b68ee426ec53825bd` has tree
`415f132524d9fe40bf78c9f0318bb140d0df1cfa`. Independent `git diff --check`
on each stage passes PR20–23 and reproduces exit2 for PR24's same two known
EOF warnings. This verifies the rehearsal's resulting objects/preservation;
the actual merge executions remain the orchestrator's recorded run. It does
not assert the other drafts' readiness. No further storage finding arises
from this refresh; final status-only integration remains the orchestrator's
responsibility.
