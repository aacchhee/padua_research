# Evidence retention and regeneration — Padua Lebesgue follow-ups

Physical delivery to AC's Padua cold storage is **pending**. This records actual
sandbox working outputs, not a claimed delivery or a verified export receipt.
Regenerable bulk certificates and logs are not committed. The sandbox has no
promised retention period; its paths alone are not durable retrieval locators.

## Actual working artifacts

| Artifact | Actual path | Bytes | SHA-256 | Status |
|---|---|---:|---|---|
| Historical full-interior proposal, restored from pinned Git history | `/workspace/scratch/lebesgue-frozen-reference/topics/padua-proof-attempts-2-20261101/outputs/a5_n8_interior_candidate.json.gz` | 637163 | `a3b4f278a322338fb65f60922b4251265288148e1a09fd22882215004e81c324` | Both complete interior replays finished; historical archive notes describe its earlier unverified status. |
| Fresh full-boundary proposal | `/workspace/scratch/lebesgue-t1/fresh-boundary-v1.json` | 4822048 | `adfe1107a326d17cfdd083a2ef9b8ab7ce0aeaa6b906f7a825c53a4fa1da6f08` | Generation and both complete original-method boundary replays finished, with identical verified facts. |
| Fresh first-phase interior checkpoint | `/workspace/scratch/lebesgue-t1/fresh-interior-memo-v1.json.gz` | 248930 | `5d7771a8248ee95d27ce45bf9dd8faec34986b200c63dcd19ad35998eba0973c` | Partial: 35591 leaves, 9 pending paths, zero unresolved. Actual exit 0; continuation input only, not a complete proof. |
| Fresh native V4 continuation checkpoint | `/workspace/scratch/lebesgue-t1/fresh-interior-native-v4.json.gz` | 377094 | `2f08f3b3f29e3b69d3846b71601ddf40d77e275a4f706115905c8b045c17f642` | Partial: 72539 leaves, 8 pending paths, zero unresolved. Actual exit 0; V5 lineage preflight passed. |
| Fresh native V5 completed negative half | `/workspace/scratch/lebesgue-t1/fresh-interior-native-v5.json.gz` | 391896 | `d6642d630ea387486e1a685fd0cce1c3df3fc0d1e4d6f16d7a6d2cee11920a43` | Negative half complete: 76760 leaves, only parked right path pending, zero unresolved; input to frozen reflection. |
| Fresh reflected full interior | `/workspace/scratch/lebesgue-t1/fresh-interior-reflected-v1.json.gz` | 637165 | `c5cdcfed9f19f2161b1d55d4f2154bc06a1cd5bd51e28c5c2187ca57c67cc45f` | Complete; developer and independent typed comparisons match all 18969878 canonical mathematical bytes of the separately replayed archive, SHA-256 `e22a9b5592d26756aa63bf143ae19f7c55fd56d1d5ecd5860088c0f2587089a1`. |
| Fresh literal closed-square join | `/workspace/scratch/lebesgue-t1/fresh-closed-square-v1.json.gz` | 1696013 | `033e851676969bde6a730f76ee1b4819b87de26b79aac775de6d487dade27fdf` | Literal join completed; both actual final-accounting compositions and both predicate-replay pairs passed. Mechanical join alone never certifies the count. |
Progress logs and atomic edge checkpoints remain in the
same named scratch directory; they are diagnostics, not accepted count evidence.

## Historical retrieval

The historical proposal is durably available as Git blob
`3f65a77df46ed9ba3c665fd80cd8509fefefaa17` at pushed source commit
`2b52b432fe59c9a50aef9deebe5152c5d6874465`. Its original source chain and frozen
commands are in the predecessor's `cold-storage.json`, entry for the path above.
The root actually restored that manifest's artifacts using:

```sh
python -B tools/cold_storage.py restore padua-proof-attempts-2-20261101 --dest /workspace/scratch/lebesgue-frozen-reference
```

A cloud checkout can fetch the pinned source commit if its objects are missing,
run the same restore command into a fresh external directory, then use
`tools/cold_storage.py verify` with that destination. The tool verifies raw
SHA-256 and size against the manifest. The independent executor separately
restored the proposal under `/workspace/scratch/lebesgue-t1-independent/cold`.
No third-party paper or extract is part of these artifacts.

## Fresh regeneration and checking

Actual commands, caps, exits and outcomes are maintained in [attempt T1](attempts/T1.md)
and [independent checks](independent-checks-t1.md). Python 3.12.14, SymPy 1.14.0,
python-flint 0.9.0 and FLINT 3.6.0 are the executed environment. The sandbox-local
package prefix is `/workspace/scratch/lebesgue-t1/deps`; it is not committed.
A new cloud session can install the pinned packages and select its own scratch
prefix. Native optional execution additionally needs the compiler/build recipe
and exact backend controls recorded in the native receipts.

The actual boundary generating command, from repository root, was:

```sh
PYTHONPATH=/workspace/scratch/lebesgue-t1/deps timeout 3600 python -B topics/padua-lebesgue-followups-20261103/code/t1_boundary.py --output /workspace/scratch/lebesgue-t1/fresh-boundary-v1.json
```

Its executed entry SHA-256 is
`7753e4ba8bc440133a46e6f5325e8b5531f20e5a20d8d0aa6778a32bacbdb7f0`,
Git blob `011b8c4174bf1506479021f306c65da71f173e1e` at pushed commit
`f346d99261aa695a55d118f6d543b8fb417c2bb7`. That commit also preserves the imported
frozen source paths. Use an isolated checkout when reproducing historical entry
bytes; never replace the source of a live run. Later optimized-Python refusal
changes must retain a guard-only mapping to this executed source identity.

Timing/provenance fields mean regenerated raw files need not match the original
raw SHA. A new artifact requires a new raw identity and its own actual replay.
Only the separately reviewed typed proof-payload comparison may establish exact
mathematical identity; it is not itself a proof of unchecked input.

The historical restore/export utility accepts pinned Git-backed manifests. It
cannot export these never-committed fresh working files through that schema;
no successful tool export is claimed. Physical archival work remains pending.
All generation/checker source and small executed receipts are preserved in Git,
so loss of the sandbox requires regeneration of fresh bulk evidence, not access
to AC's computer. Retain the listed working artifacts until audit and archival
resolution while this sandbox remains available; no sandbox cleanup is requested.

## Executed fresh-chain source locators

The following immutable entries identify the generating phases. Exact commands,
input/output hashes, time caps and actual exits are in the corresponding small
receipts and attempt T1; imported source identities are pinned by their freeze
receipts. Reproduction uses an isolated checkout of the listed commit plus the
pinned dependency environment, not substitutions in an active process.

| Phase | Entry | Commit | Git blob | SHA-256 |
|---|---|---|---|---|
| V3 first phase | `topics/padua-lebesgue-followups-20261103/code/t1_produce.py` | `f346d99261aa695a55d118f6d543b8fb417c2bb7` | `cd78c69852b8500d0e16e5fe26f7ee9bc09ecc3f` | `1ac5cbb83302d12006f35f042954fd6c76881e263ed6de065ca22c5302a77664` |
| V4/V5 native continuation | `topics/padua-lebesgue-followups-20261103/code/t1_native_produce.py` | `1b7ebd88bf95b4ef123f24bde3ec724ef1128a09` | `d46ad00394e35d1684f9168d2ed1b68344040771` | `6c69b3ed4e08ed238e5ab141c2280a954c37b0d66702ced4a32cbc9cc15b0e2c` |
| Full-square reflection | `topics/padua-proof-attempts-2-20261101/code/a5_n8_reflect_axis.py` | `440d1079e42c3ef21c40d1cf8870f5b206410c6a` | `c9408d0da4237a9007aa210d9581aa127dc42087` | `f77056651bb1bbf8eb3b154190eadad47ce33cbb3b793b4f32ae31f0834497e5` |
| Literal boundary join | `topics/padua-lebesgue-followups-20261103/code/t1_join.py` | `05cca840c714a065d4e7be0ce5b4ebaaa5207668` | `dee7b00077c2966192c488df38c4d7c8e103031c` | `a88b18f2a617d7dac03a5db7ba2a89a32cae731cd2f7b6c5a0ea400e5b554b61` |

The generation chain is V3 → V4 → V5 → reflected interior → literal join with
the independently generated boundary. The V3/V4/V5 source-version labels and
lineage checks are retained literally; checkpoint labels are not silently
rewritten. Operational interruptions and capped partial outputs remain recorded
as such. Native code accelerates proposal generation only; the completed
mathematical predicate replays use the original exact Python checker.

## Completed acceptance references

The two complete original interior replays are
[evidence/t1-reference-interior-check.json](evidence/t1-reference-interior-check.json)
and [independent interior replay](evidence/t1-independent-reference-interior-check.json).
The two complete original boundary-method replays are
[evidence/t1-boundary-check.json](evidence/t1-boundary-check.json) and
[independent boundary replay](evidence/t1-independent-boundary-check.json).
The actual fresh proof identity, literal join and original final accounting are
bound by [developer composition](evidence/t1-final-composition.json) and
[independent composition](evidence/t1-independent-final-composition.json), with
the actual different-agent execution record in the independent report.
These sources and receipts are listed by hash and size in the evidence manifest.
No monolithic joined run or completed physical archival export is claimed.

The joiner binds the boundary producer's physical source identity. When joining
the historical 7753-boundary artifact again, use the isolated source snapshot
at `05cca840c714a065d4e7be0ce5b4ebaaa5207668`, which preserves both the accepted
joiner and old producer. Do not point that historical artifact at today's
guard-only a70e producer and pretend its provenance matches. A newly generated
boundary under the guarded source carries its own truthful metadata and needs
new input identities and replay receipts. The final guard-delta and independent
controls document exact mathematical source equivalence without relabeling old
runs. See [guard map](evidence/t1-boundary-optimization-guard-delta.json) and
[independent guard check](evidence/t1-independent-boundary-guard-controls.json).

## 2026-11-05 audit addendum — reproducible boundary proof identity

The durable mathematical boundary identity is the typed proof payload
SHA-256 `1316b929ec142e0274f8c68a37e59a85b2136f8b322077ecd8172918719b54f2`,
**4,821,831 bytes**, recorded in [the developer payload receipt](evidence/t1-boundary-payload.json).
Claude independently regenerated that exact payload from committed code;
[audit-01 §T1.3](audit-01.md#t13-auditor-boundary-regeneration-executed)
records the equality. The regenerated raw artifact has a different truthful
SHA-256, `cf141babf23d1178c0fe6b250d7569c9529bdc2cf23b6e4192b9deb58ae64357`
(4,822,048 bytes). This demonstrates regeneration stability of the mathematical
payload for that independent execution, not byte identity of raw metadata/timing.

Claude also executed the complete original monolithic Verifier.run on the
Git-retrievable archived interior plus its regenerated boundary; the
[monolithic receipt](audit-support/claude-audit-01/monolithic-receipt.json)
records exit 0, count_certified true and 44+16+2=62, with unchanged frozen sources.
This additional audit execution is distinct from the developer's separately
executed predicates and composition; the developer receipts remain unchanged.
Auditor bulk artifacts remain in the auditor's sandbox, with identities and
commands in the [audit support](audit-support/claude-audit-01/README.md).
Physical cold-storage delivery remains pending. Scratch paths in the historical
table are not durable remote retrieval locators.

### Receipt reproduction requirement: CPython 3.12.x

The AST pins used by `code/t1_check_boundary.py` (`frozen_boundary_ast`) and
`code/t1_compose.py` (`summary_predicates`) and their recorded receipts require
**CPython 3.12.x** (developer executions: 3.12.14). Python 3.13 changes ast.dump
serialization: the boundary AST pin `73fc0216…` and summary pin `61812bc0…`
do not match that version. Use CPython 3.12.x when reproducing those historical
boundary/composition contracts and receipts; do not substitute hashes or edit
executed sources to bypass a rejection. This is an AST serialization constraint,
not a different mathematical predicate. Claude's independent monolithic wrapper
successfully used Python 3.13.18 and does not reuse the 3.12 composition pins;
see audit-01 F6 and §T1.4. Old source/receipt hashes retain their original meaning.
