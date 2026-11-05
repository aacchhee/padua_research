# Generated-output migration — 2026-11-05

AC directed: **“generated outputs should go to cold storage.”** This authorizes
actual archival reduction, not an exception to the budget. Orchestrator Codex,
configured gpt-6.1-sol medium, read rules at
`40347d11071c81c1c633a2578cb52325bb92584a`. Main remains
`5db1e01dcd2258f45de2adcaef43859e59734618`. This is storage/provenance work,
with no new mathematics, idea or novelty claim. Handoff05's reduction route applies.

## Selection and retention

Archived **326 files / 1,155,908 original bytes**: raw process/progress streams,
generated analysis tables, and selected raw output/error/timing captures with
retained scientific summaries. Selection follows artifact function, not size.
No artifact was split. The **42 manifests** follow preexisting logical experiment
and audit components, preserving each component's separate generation context.
All are below 16 KiB; largest **14,271 bytes**, total **163,549 bytes**.

Retained all mathematical statements, code, auditor Markdown reports, compact
JSON checker/control/global receipts, essential JSON-shaped checker stdout and
PR17's explicitly retained scientific stdout summaries. Existing manifests and
all historical source identities are unchanged. Only the raw boundary generation
log is relocated among this topic's original auditor files; its original bytes
remain pinned, retrieved and verified. No proof acceptance predicate or result
changed. Added default Git ignores for raw streams to avoid recommitting them.

Every new entry pins its exact original path, Git blob, SHA-256 and byte size
at pushed source **40347d11071c81c1c633a2578cb52325bb92584a**. Existing old
manifests retain their own source pins. We never append new-source objects to
an incompatible old single-source manifest or rewrite Git history.

## Command provenance and limitations

Each component's COLD_STORAGE.md records exact byte reconstruction and checker
commands, retained short summaries, and frozen historical command records where
recovered. Direct output invocations are distinguished from partial argv,
script/output mappings and checker/input mentions. Missing original command
or stdout-capture details are explicitly **retrieval-only**; no parameters or
new scientific reruns are invented. Source:path/blob and SHA verification
reconstructs exact historical output bytes independently of those limitations.
For example, the boundary generator is recorded verbatim from its audit README,
while its missing stdout-redirection detail remains disclosed.

## Actual executed transfer and checks

For every manifest directory below, executed the unchanged repository utility:

```sh
python tools/cold_storage.py export <manifest-directory> --dest /workspace/scratch/padua-cold-storage-20261105-v2
python tools/cold_storage.py verify-archive <export-directory> --manifest <manifest-path>
python tools/cold_storage.py restore <manifest-directory> --dest /workspace/scratch/padua-cold-restore-20261105
python tools/cold_storage.py verify <manifest-directory> --dest /workspace/scratch/padua-cold-restore-20261105
```

All 168 commands exited 0. Export read back destination bytes before writing
its deterministic v2 receipt; verify-archive reread each payload, checking the
trusted final manifest. Separate restoration matched every original SHA/size.
The orchestrator additionally compared all source/export/restored bytes before
`git rm` of exactly those 326 tracked copies. No other file was removed.
An earlier staging pass used preliminary provenance metadata; final v2 exports
below replace it for reliance. The original raw bytes did not change.

Actual export root: `/workspace/scratch/padua-cold-storage-20261105-v2`.
Each export directory is the manifest directory with `/` replaced by `_` under
that root, as the existing utility defines. Receipt identities below pin final
export-time readback; later reliance requires a fresh verify-archive.

| Component / machine manifest | Files | Artifact bytes | Export receipt SHA-256 |
|---|---:|---:|---|
| [topics/bivariate-lanczos-20261031/audit-01](../../bivariate-lanczos-20261031/audit-01/cold-storage-20261105/cold-storage.json) | 1 | 1279 | `88f847013b0983605248eaa0b7552a9f3eaa5cf3341f1d3c4494322b42b87b42` |
| [topics/bivariate-lanczos-20261031/audit-01/L1-foundations](../../bivariate-lanczos-20261031/audit-01/L1-foundations/cold-storage-20261105/cold-storage.json) | 2 | 5636 | `472bab49e0b5969d984b72f8f91fb36feadce922d86554a1e9f26d8a10e21e3f` |
| [topics/bivariate-lanczos-20261031/audit-01/L1-later](../../bivariate-lanczos-20261031/audit-01/L1-later/cold-storage-20261105/cold-storage.json) | 11 | 15231 | `7b1904507daa5c37ec6262ed26be7a47417e287c73370a57fa5bfc28cd45058c` |
| [topics/bivariate-lanczos-20261031/audit-01/L2](../../bivariate-lanczos-20261031/audit-01/L2/cold-storage-20261105/cold-storage.json) | 7 | 36950 | `89a00dfa1af5c4add181357fa1ca46998e49cd0a55b5a07554a3fa6ea27c9d28` |
| [topics/bivariate-lanczos-20261031/audit-01/L3-certificates](../../bivariate-lanczos-20261031/audit-01/L3-certificates/cold-storage-20261105/cold-storage.json) | 7 | 16845 | `7a1948e955379ff1222dff07911d4b918c8a7b109766bd6b55d8c5c5901fb3b8` |
| [topics/bivariate-lanczos-20261031/audit-01/L3-framework](../../bivariate-lanczos-20261031/audit-01/L3-framework/cold-storage-20261105/cold-storage.json) | 7 | 14932 | `bf1d1737b53ea048f0f12c01e9380e46aed14e799b808f6a347ce50d08a2b7dd` |
| [topics/bivariate-lanczos-20261031/audit-01/L5](../../bivariate-lanczos-20261031/audit-01/L5/cold-storage-20261105/cold-storage.json) | 8 | 38684 | `080b6569dd80eb0533e6e3c3157a8502531886d2373d7b6517217783975ea1f9` |
| [topics/bivariate-lanczos-20261031/audit-02/L1](../../bivariate-lanczos-20261031/audit-02/L1/cold-storage-20261105/cold-storage.json) | 4 | 22816 | `9af7e23a1b0b45414a35ad9636153889509fa988f0aa0eccc480a3ae12e85a49` |
| [topics/bivariate-lanczos-20261031/audit-02/L2](../../bivariate-lanczos-20261031/audit-02/L2/cold-storage-20261105/cold-storage.json) | 3 | 5013 | `fb3bc6769670d1ae3eee59170328aa0b79ffd77d5d190f4a5e651e61b9cfbd9d` |
| [topics/bivariate-lanczos-20261031/audit-02/L3-conventions](../../bivariate-lanczos-20261031/audit-02/L3-conventions/cold-storage-20261105/cold-storage.json) | 2 | 2252 | `956cc77f9c87aed387964eb7bc85a4264ff6360733c89a212365fab2425dffec` |
| [topics/bivariate-lanczos-20261031/audit-02/L3-formula-scope](../../bivariate-lanczos-20261031/audit-02/L3-formula-scope/cold-storage-20261105/cold-storage.json) | 4 | 4902 | `c89f36c2668cf55833e24011fd098ae528808755f9eead799c8a405add58a6d7` |
| [topics/bivariate-lanczos-20261031/audit-02/L5](../../bivariate-lanczos-20261031/audit-02/L5/cold-storage-20261105/cold-storage.json) | 2 | 8840 | `668a794def2342410b70eced9f6e9d9e749a033103ba04b3b11bb847a4735a73` |
| [topics/bivariate-lanczos-20261031/audit-03](../../bivariate-lanczos-20261031/audit-03/cold-storage-20261105/cold-storage.json) | 1 | 7992 | `f4dd97ef306922b12a035939bafc14bce69f741e5a5d564f7ce1f1e0a883d988` |
| [topics/bivariate-lanczos-20261031/audit-04/literature](../../bivariate-lanczos-20261031/audit-04/literature/cold-storage-20261105/cold-storage.json) | 1 | 1575 | `4f1161993c43d04eac85252e69a40558ec6ca97c49ecf5421630b70f13a3aa5f` |
| [topics/bivariate-lanczos-20261031/directions/L1](../../bivariate-lanczos-20261031/directions/L1/cold-storage-20261105/cold-storage.json) | 40 | 86901 | `beb8381d102c99a3ff4a354157b77136d5af7c6d8f662765d07f398aca3ecde5` |
| [topics/bivariate-lanczos-20261031/directions/L2](../../bivariate-lanczos-20261031/directions/L2/cold-storage-20261105/cold-storage.json) | 8 | 77019 | `191c8d094306cb8a307c3a3d2d4552cf9d87f02c9ad0a35aad529497ef279b75` |
| [topics/bivariate-lanczos-20261031/directions/L3](../../bivariate-lanczos-20261031/directions/L3/cold-storage-20261105/cold-storage.json) | 33 | 50405 | `1a0b7659597e87d2d7484f78467f35ef7563d62f5c1184def6f090c87c3490c2` |
| [topics/bivariate-lanczos-20261031/directions/L5](../../bivariate-lanczos-20261031/directions/L5/cold-storage-20261105/cold-storage.json) | 28 | 156304 | `e4df200309dab27ea8dedb5cb11719168f2cb9809ee33b3bb045886e209d6918` |
| [topics/bivariate-lanczos-20261031/repro/analysis](../../bivariate-lanczos-20261031/repro/analysis/cold-storage-20261105/cold-storage.json) | 5 | 28383 | `6a4e1ce620e7e3ca18c4823337daf3e3bf10b2afb4fb38922895f9593961e790` |
| [topics/bivariate-lanczos-20261031/repro/logs](../../bivariate-lanczos-20261031/repro/logs/cold-storage-20261105/cold-storage.json) | 16 | 25794 | `f4f5cdf296d8fee6c244593c944b4ab77aed2d9cf10b21aeb9a92956aa32334f` |
| [topics/bivariate-lanczos-20261031/reviews/logs_L1](../../bivariate-lanczos-20261031/reviews/logs_L1/cold-storage-20261105/cold-storage.json) | 8 | 34244 | `00cbc8bbfd848f2a408aefc7a62ef8c7a0b04748272efc1ea8ec911fdefcf320` |
| [topics/bivariate-lanczos-20261031/reviews/logs_L1b](../../bivariate-lanczos-20261031/reviews/logs_L1b/cold-storage-20261105/cold-storage.json) | 13 | 20425 | `f11a0c014d99cd1457a2ebc1e469b5d0c90f24f39e6670cd71e0970c21070c40` |
| [topics/bivariate-lanczos-20261031/reviews/logs_L2](../../bivariate-lanczos-20261031/reviews/logs_L2/cold-storage-20261105/cold-storage.json) | 11 | 66724 | `b4ee11acd62cc47df9387aba98284067d203c5d3c95e8a9303ffe1d4a3f2769a` |
| [topics/bivariate-lanczos-20261031/reviews/logs_L3](../../bivariate-lanczos-20261031/reviews/logs_L3/cold-storage-20261105/cold-storage.json) | 11 | 17219 | `cc5a519c91bdc8146d2e15cba24794010952b629e11c802e2020a44193fd9c18` |
| [topics/bivariate-lanczos-20261031/reviews/logs_L3b](../../bivariate-lanczos-20261031/reviews/logs_L3b/cold-storage-20261105/cold-storage.json) | 10 | 28784 | `2ac245167308356b3840fcb93607d052b7f91937b2a4bf67c3f09ce15c638bdf` |
| [topics/bivariate-lanczos-20261031/reviews/logs_L5](../../bivariate-lanczos-20261031/reviews/logs_L5/cold-storage-20261105/cold-storage.json) | 11 | 51802 | `8bc98900293c4510d22417431f9a04a20d5d16d57063d5206f3bcda7508b3778` |
| [topics/lattice-unisolvence-20261031/independent](../../lattice-unisolvence-20261031/independent/cold-storage-20261105/cold-storage.json) | 4 | 20058 | `4a55caa71bedb52603f42ae8f4f8a98ab3c9be87949ea58aaeaacc481c027d03` |
| [topics/mz-constants/directions/M2](../../mz-constants/directions/M2/cold-storage-20261105/cold-storage.json) | 1 | 3701 | `b8533360ca58fbd028794506339dfa720803182cbf477e92fa8047d8365c4785` |
| [topics/padua-argmax-alln-20261101/audit-support/claude-audit-01/files/A/indep](../../padua-argmax-alln-20261101/audit-support/claude-audit-01/files/A/indep/cold-storage-20261105/cold-storage.json) | 2 | 20801 | `56d6a1a9dff473f0ea8cc581223780a683426582eb4748bc163f1c81af30991f` |
| [topics/padua-argmax-alln-20261101/audit-support/claude-audit-01/files/B](../../padua-argmax-alln-20261101/audit-support/claude-audit-01/files/B/cold-storage-20261105/cold-storage.json) | 1 | 6010 | `12d6c558d228673669c8708b14228ad995fc9779b1ce36c3b8a66187a211e904` |
| [topics/padua-argmax-alln-20261101/audit-support/claude-audit-01/orchestrator](../../padua-argmax-alln-20261101/audit-support/claude-audit-01/orchestrator/cold-storage-20261105/cold-storage.json) | 1 | 6719 | `600c85687eed1589a3c4886b01d7eaab09762bfc4fab50e63842d781d381a761` |
| [topics/padua-lebesgue-followups-20261103/audit-support/claude-audit-01](../audit-support/claude-audit-01/cold-storage-20261105/cold-storage.json) | 1 | 1019 | `b8bb94e7e01271c3046691fb0ac0da657841e2c92000c4fbf9191036c9fece51` |
| [topics/padua-mz-2d-20261101/audit/claude-audit-01](../../padua-mz-2d-20261101/audit/claude-audit-01/cold-storage-20261105/cold-storage.json) | 6 | 991 | `422ca81bea5679220a87bbf4d70b72cbd2fd534a47e0d3c1c507eaeb1db343bd` |
| [topics/padua-proof-attempts-2-20261101/outputs](../../padua-proof-attempts-2-20261101/outputs/cold-storage-20261105/cold-storage.json) | 26 | 99089 | `e7d4bbf0b8672bfc6aabc289123c6a01c929734998b92da3d5bce9ddffd7e765` |
| [topics/programme-ideas-20261031/checks/code/adv/M1](../../programme-ideas-20261031/checks/code/adv/M1/cold-storage-20261105/cold-storage.json) | 2 | 9734 | `12ba15a82429c26aaa91d91162d34586e737ccc967bf437886132eb79dafe27f` |
| [topics/programme-ideas-20261031/checks/code/adv/gen1-2](../../programme-ideas-20261031/checks/code/adv/gen1-2/cold-storage-20261105/cold-storage.json) | 3 | 10062 | `934775c74c1010523656a2237d636a9cae7cca2c9f0f4ec96afc9b15af88a8f7` |
| [topics/programme-ideas-20261031/checks/code/adv/gen3-3](../../programme-ideas-20261031/checks/code/adv/gen3-3/cold-storage-20261105/cold-storage.json) | 1 | 4315 | `89d2d7632d00da260dff9726bd5d1a0607803eed371d19fb2ef9174cba3b550c` |
| [topics/programme-ideas-20261031/checks/code/adv/gen4-1](../../programme-ideas-20261031/checks/code/adv/gen4-1/cold-storage-20261105/cold-storage.json) | 3 | 15478 | `6c494d1c8c67657f058b9c9d09ec7c675b86a5e7ef76f8d5c441f2057b44d489` |
| [topics/programme-ideas-20261031/checks/code/adv/gen4-2](../../programme-ideas-20261031/checks/code/adv/gen4-2/cold-storage-20261105/cold-storage.json) | 6 | 15392 | `d82267e0e0b05b4ce4a2b12d6ad353ac9b312dfd5f1921e4e79433b9bf86c2ed` |
| [topics/programme-ideas-20261031/checks/code/decisive/gen1-3](../../programme-ideas-20261031/checks/code/decisive/gen1-3/cold-storage-20261105/cold-storage.json) | 4 | 42277 | `8a7fba4896c697a98933db305b8183c3a9af04a093017c00c8fde686fe486662` |
| [topics/programme-ideas-20261031/checks/code/decisive/gen4-2](../../programme-ideas-20261031/checks/code/decisive/gen4-2/cold-storage-20261105/cold-storage.json) | 10 | 69610 | `64182781b61acf69a5f9f230345e381b9534597ea6d75ca88af4a4b504ea79b3` |
| [tracks/mz-constants/evidence](../../../tracks/mz-constants/evidence/cold-storage-20261105/cold-storage.json) | 1 | 3701 | `1f77a477e67b164a2ca533ecd86d833b52df6842267313fd04a989bea2ffaca6` |

## Budget and integrity checks

Conservative count uses every current Git blob except extensions
md/py/sh/tex/bib/svg/gitignore, exactly the preparation method. Before:
**4,851,736 B**. Removed **1,155,908 B**; added **163,549 B** of required
small manifest metadata. Expected current total: **3,859,377 B**, leaving
**1,140,623 B (22.81%)** below 5,000,000. All metadata remains counted; no
classification subtraction or budget waiver is used. Reproduce against the
final commit using response-01's documented `git ls-tree -r -l` method.

The registration verifier now resolves a missing raw file only through an
explicit manifest, pinned source:path/blob, SHA and size, then compares the
original audited bytes. It does not skip missing inputs. The new storage
verifier checks the exact deletion/manifest bijection, every source/export and
restored payload, genuine component trees, JSON size limits, all repository
mathematics/code/auditor-report preservation and unchanged prior manifests.
Its source and actual results are recorded with the independent review.

## Retention and physical delivery

Physical delivery to AC's `Downloads/padua/cold_storage` remains **PENDING**:
that folder is not available through this cloud filesystem or configured tools.
The local export is staging, not a claim of AC delivery or guaranteed retention.
All historical blobs remain reachable in the pushed branch; fresh cloud sessions
can fetch source40347d1 and repeat export/restoration with committed manifests
and the unchanged utility. Do not purge history. Keep staging while available.
A packaged copy will be offered for delivery; it does not change this status.

## Review disposition

The former S1 budget finding is addressed by this concrete reduction, not waived.
Independent technical/protocol review of the final migration is pending here;
PR20 remains draft until that check and refreshed readiness checks pass.
The existing T2/T3 timing qualification is still confirmed and unwaived.

## Transfer package

Actual staged package: `/workspace/padua-cold-storage-20261105.tar.gz`,
**458,735 bytes**, SHA-256
`a0bc746b89e5d1300dcc01d8633e11c58a2ba96483b645b9aaf825c8ccdb000b`. It contains all 42 verified exports, their
v2 receipts, matching manifests/provenance records, the unchanged verifier
utility and a README. This makes transfer reviewable; it is not a receipt of
delivery to AC. After transfer, extract and run the documented offline
verify-archive commands against the delivered copies.

## Final verification and disposition

Executed `verify_cold_storage.py --staging /workspace/scratch/padua-cold-storage-20261105-v2
--restored /workspace/scratch/padua-cold-restore-20261105`: PASS 42 logical
manifests, 326 files / 1,155,908 bytes, exact deletion map, every export/restore,
1,075 protected repository files unchanged. Registration verification passes
138 immutable inputs (including archived-byte resolution), 9 mathematical bodies,
123 manifest rows, 9 mappings and 757 local links. `git diff --check` passes.
The committed inventory at4952cdd is exactly **3,859,377 bytes**.

The transfer package was additionally extracted to a separate scratch directory;
all 42 archives passed offline verify-archive using its packaged tool/manifests.
The distinct Astra medium [independent storage review](cold-storage-review.md)
accepts the migration with no unresolved finding. S1 is resolved through reduction,
not an exception. Fresh reservation and sequential squash checks pass, retaining
all topics’ records and all 326 archival removals. PR20 is ready for AC decision.
Physical delivery remains pending; the trusted retrieval source is still pushed
40347d1 and no history purge is authorized.
