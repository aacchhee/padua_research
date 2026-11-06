# Integration integrity checks

Scope: mechanical integration support only, not a mathematical audit or an independent numerical rerun. No producer, eigensolver, degree scan or new fit was executed. The novelty gate does not apply because this work adds no mathematical mechanism or novelty claim.

Rules and source corpus: `2143ad622fa98faf8fe7d5cb8ed2bb7e0062f861`. This is a fetched source corpus, not a Git checkout; publication belongs to the coordinator. Assigned model/effort: `gpt-6.1-sol`, medium; actual runtime model/effort metadata is not exposed to this worker.

## Final snapshot

After the coordinator's completion signal, the [manifest](evidence-manifest.json) was regenerated with status `FINAL snapshot` and no dynamic exclusions. It records topic-relative paths, byte sizes and SHA-256 for all 23 Python sources, 39 other JSON files and the small SVG: 63 inventoried files, 317,474 bytes in total. The manifest itself is 7,135 bytes. Both completed Padua receipts, the final Padua fit and independent replay, and the S3 transfer diagnostic code/receipt are included.

The deterministic generator sorts paths and uses no clock or environment-dependent manifest fields. Verification checks membership as well as file sizes and hashes: an added, removed or edited inventoried file fails until intentional regeneration. The generator itself is inventoried. Prose, caches, external source files and large raw outputs are outside its hashing scope. JSON provenance inventories are included, but their referenced external payloads are not recursively verified. File identity does not establish correctness of numerical or mathematical claims.

The final size scope is the new topic's 40 JSON files including the manifest, totaling 213,859 bytes, plus the 15,720-byte SVG: 229,579 bytes of generated JSON/SVG evidence. Every generated file in that scope is below 16 KiB. The largest is `input-snapshot.json`, 16,342 bytes. Python source files total 95,030 bytes. These figures are not a whole-repository generated-output measurement. The coordinator records the applicable temporary repository-wide 10 MB allowance in [LOG](LOG.md); per-file limits remain in force. No whole-base size-compliance conclusion is claimed here.

## Executed final commands and results

```sh
python /workspace/sharp-work/topics/padua-mz-sharp-constants-20261106/code/evidence_manifest.py --write --checks
python /workspace/sharp-work/topics/padua-mz-sharp-constants-20261106/code/evidence_manifest.py --checks
```

Final checks passed: AST parsing of all 23 topic Python code files; JSON parsing and size checks for all 40 topic JSON files; and 61 Markdown documents comprising topic prose plus its results file, with 213 local file links and zero missing targets. Link checking ignores fenced and indented code, inline code, TeX math, remote URLs and section anchors. Plain path mentions are not links. It checks file-target existence, not anchor validity or remote availability. Prose is never hash-pinned. The final handoff's input-SHA replacement and original-handoff status transition are coordinator-owned publication actions; no approval of handoff semantics is implied by link checks.

The earlier provisional inventory explicitly excluded the two then-mutable Padua receipts. Those exclusions have been removed. No active receipt remains excluded from the final inventory.

## CC reporting figure

The [CC extrapolation SVG](figures/cc-extrapolation.svg) reuses all 42 measured CC rows and the four registered even/odd A/B fit coefficient vectors. It plots `x=1/log N`, `y=(log N)^2 lambda_min` and the existing curves `c-a*x*log(x)+b*x`, with value `c` at zero. Intercepts are labeled MEASURED; the dashed `pi^4/8` line is labeled a PROVED limsup bound and explicitly distinguished from a pointwise finite-N bound. No gate verdict changes.

Executed command:

```sh
python /workspace/sharp-work/topics/padua-mz-sharp-constants-20261106/code/plot_cc_extrapolation.py
```

Matplotlib 3.10.8 generated the 15,720-byte SVG and uncommitted preview `/tmp/sharp-S4/cc-extrapolation.png`. The PNG was visually inspected; the compact SVG parsed as XML, retained 22 SVG text nodes and contained no font-glyph definitions. Compact rendering syntax and three-decimal SVG display coordinates keep the figure below 16 KiB without splitting; scientific input values remain untouched. The SVG is hash-inventoried with its generator and source JSON.

Only this worker's assigned manifest generator, manifest, integrity record, plot generator and SVG were modified. No unresolved issue was found within the declared scope.

Coordinator final recheck after adding the final LOG/report links executed the same `--checks` command: all63manifest identities,23Python ASTs and40JSONfiles pass;61Markdown documents contain217local file links, with zero missing targets. The manifest is unchanged. Only prose link additions and the separately verified handoff metadata transition follow the worker's213-link snapshot.

## Handoff03 closing-development integrity (2026-11-06)

The original counts above are historical. Developer manifest scope now deliberately excludes auditor-owned audit-01-support, as requested in A13; the integration checker still parses those JSON files without inventorying their identities. New code, exact trial/certificates, independent outputs and prospective P2 rows are inventoried. Every generation uses an intentional --write followed by verification; no producer is imported by this check.

Remote tree comparison at checkpoint0d97ed6688d1048e7e340f078cba26b771bfc362 against the full pinned0205690b9c4e959a28e949083e9a1808735abf4b tree verifies4224 pre-existing blobs outside the permitted topic/results scope are unchanged, with zero added external blobs. All66 audit-01/report/support blobs are unchanged. Earlier local comparison also checks88 materialized external source files with zero differences. This verifies publication scope, not mathematical correctness.

Published protocol order: response17ca9f4 first; P2/P4 source/protocol d03e74d before evaluation; measured P2 b2 calibration64f3b76 before four main cases; P1 numerical protocol/source c1e6e59 before either instance. Every ref update uses an expected-head lease and a single-parent fast-forward. Current main remains76ba4214b100c86a44941f5e9a662ce9ce48efb8; no base merge is needed. Published author identity is the AC-approved59649991+aacchhee@users.noreply.github.com.

Final output counts and final remote identity comparison are recorded below after all P2 receipts complete. No shared registry, reservation, final ID, manuscript, old audit/support or earlier handoff body is changed by development. Required focused Claude audit remains separate from these integration checks.

### Final scientific output snapshot

After all four P2 main rows, actual independent m1600 and independent summary receipts complete, `evidence_manifest.py --write --checks` verifies90 identities (423930 inventoried bytes), a9988-byte manifest,30 Python ASTs,77 JSON files and356 local links across100 Markdown documents, with zero missing targets. All77 JSON files including audit support and manifest total327453 bytes; SVG15720 bytes; topic generated JSON+SVG total343173 bytes. Largest generated file16342 bytes, strictly below16KiB. This is the topic's generated-output scope, not a whole-repository storage measurement. No bulk artifact is needed for any new claim.

All campaign processes have exited. P1/P4 code inspection and actual exact reruns pass; P2 independent m1600 scientific fields match bit-for-bit and final summary/independent high-precision criterion arithmetic pass. P3 remainder and complete assembly reconstruction pass. These are separate from the forthcoming Claude audit. The only final publication after the scientific outputs changes handoff03's status and adds handoff04; it adds one Markdown document and is link-checked separately.
