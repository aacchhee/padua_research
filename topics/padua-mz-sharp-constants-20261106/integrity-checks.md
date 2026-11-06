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
