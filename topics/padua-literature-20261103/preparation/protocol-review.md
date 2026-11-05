# Independent PR21 finalization review

Reviewer: supplementary Codex agent, inherited requested gpt-6-astra high; runtime serving metadata unexposed. Rules read at `65b24972954a6e13e950a489ef9ecb0397601328`. Scope: mechanical integration of already accepted Claude literature records, no new scientific source or novelty work; a fresh full IDEAS read is unnecessary for this scope. No Git mutations or candidate edits by reviewer.

Status: initial map reviewed; final candidate inspection pending orchestrator notification. This is not full acceptance.

Initial map: 58 canonical aliases, 27 reused aliases, 31 new IDs LIT-482–512; LIT-513–561 permanent unused gaps. Multiple aliases44/45→234 and75/76→346 correctly avoid duplicate accepted statement registrations. Existing PR22 identities420 (FHV half separately from ADY),346,119/347,117/118/348 and existing466/470 remain retained by the declared mapping. The declared grouped statement expansions preserve theorem distinctions in prose. No mapping finding at this stage.

Read: AGENTS, workflow, Codex role, handoff11, audits02/03, preparation/final-id-map.json, literature-dedup.md, allocation-scan.json, relevant PR22 dedup entries, topic LOG context. Audit acceptance retains developer-only inaccessible journal/image/NTNU/Crossref boundaries and F1–F7 dispositions.

Candidate inspection in progress at HEAD4a8acf7 + working edits. Actually executed independent `/workspace/scratch/check-final-independent.py`: canonical INDEX set delta exactly482–512, all old canonical IDs retained, new rows unique, no513–561 assignments,58mapping keys and crosswalk aliases, unchanged PROOF_STATUS/IDEAS, immutable audit/support/check history, foreign RESULTS content (separator whitespace excluded), PR22 INDEX/CORPUS alias lines preserved. Own RESULTS link-normalized body pending fix.22 source files outside proposal application targets independently normalized to exactly their baseline bodies after removing registration paragraph and final-ID heading annotations. Three proof-topic diffs inspected: source locator addendum only, no claim/proof/status changes.31 new INDEX rows inspected for source alignment; three require table presentation repair below.

Findings sent to orchestrator:
1. RootRESULTS own section retained ../topics paths from results-file context, resolving outside repository. Fix root paths to topics/, preserve own source paths and normalize copy equality accordingly.
2. New INDEX canonical482/484/501 rows contain unescaped absolute-value pipes, breaking seven-column Markdown cells. Escape math pipes in applied INDEX presentation without altering source statements.
3. New CORPUS seven-column source rows appended after PR22 five-column table lack campaign header/separator and contain blank lines between rows. Add heading and seven-column header, remove row separators, preserve foreign PR22 bytes.

No scientific, source-ID/dedup or accepted-verification-boundary finding found in inspected candidate. Final acceptance awaits these repairs and final candidate metadata/checks.

## Final disposition of inspected registration candidate

**ACCEPTED within mechanical source registration and preservation scope; no unresolved finding.** All three findings above were repaired by the orchestrator and independently rechecked. This supplementary review does not replace the accepted scientific Claude/Codex audit chain, independently verify inaccessible sources, certify exhaustive novelty, or merge the PR. Final disposable integration, publication, readiness metadata and handoff closure remain orchestrator actions.

At candidate HEAD4a8acf7 plus working preparation, compared against published integration baseline65b24972954a6e13e950a489ef9ecb0397601328, incorporating main9322fba83eb8d942e04209bb3262ad15d52bfb1e:
- Executed independent scratch checker `/workspace/scratch/check-final-independent.py`: all13 assertions passed. Canonical INDEX440→471 (31 new), old IDs retained, new rows unique, permanent gap unused,58map/crosswalk aliases,17 immutable audit/history/check files byte-identical, PROOF_STATUS/IDEAS unchanged, foreign RESULTS sections unchanged except appended separator newline, link-normalized own results equal, accepted PR22 alias lines retained in INDEX/CORPUS.
- Independently executed committed `python3 -I topics/padua-literature-20261103/preparation/check_registration.py --repo .`: PASS,58aliases/31new/27reuse,24normalized record bodies,140new local links with zero broken, immutable rules/audits/foreign content/statuses, generated budget4236223<5000000 and maximum topic JSON11112B. This is an actual rerun, not inspection of developer output.
- Independently parsed escaped-aware table delimiters: all31new INDEX rows have exactly7cells and matching CORPUS source keys; new CORPUS section has separate heading/header and contiguous rows. The three absolute-value rows now retain claim cells.
- Executed `git diff --check`: no findings.
- Read final preparation record, application receipt and registry/admin diffs; inspected the three proof-topic source-locator-only updates. No scientific claim/status/proof code change identified. Earlier source-reading and all F1–F7 acceptance qualifications remain explicit.

Exact SHA256 identities of inspected core bytes:

| Path | SHA256 |
|---|---|
| literature/INDEX.md | fc9d8dbc9a334979ed1e9d7ae26c85a0af330e718cead76a8597374304d0a924 |
| literature/CORPUS.md | 023d22676faba00f623c8702751e5d24b3bdde4dae5c7c909cd91ee6c74bb58e |
| ID_CROSSWALK.md | f447d05a7f9895169c59a028efe387918d1a90258b34e3bc7e661dab1ff826d9 |
| RESULTS.md | df4fea5e62bea3d893ec181afa16ee8bcaca6b0b188bd82db976a080d06cce12 |
| results/padua-literature-20261103.md | edb20f0562d79f89368fa8b720f89dece3d8f3199aecfe5da306c1feb7dddfde |
| PROOF_STATUS.md | a1536bc32f5609340fdccdda5e3d8893abe34d24d9bff6832156aadddb134bb5 |
| state/IDEAS.md | 948c30b35cdb3ffacefe398acfb35439fc7e69f8be33fd94bc605b052b8d03c6 |
| topics/padua-literature-20261103/preparation/final-id-map.json | 572499c213e71a0923c08a591b4fbf26f5e95a91cae7119bcc90d7010839fc85 |
| topics/padua-literature-20261103/preparation/check_registration.py | 15c8e100d32851bad7429603d7273d4434df815e9adb21bf524f4baa6f76d441 |

Any subsequent source/registry-byte change requires an impact check against these reviewed identities. Pure receipt/log/closure additions do not expand the scientific scope.
