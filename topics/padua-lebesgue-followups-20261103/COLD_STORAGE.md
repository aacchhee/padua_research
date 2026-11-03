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

Fresh continuation and final joined artifacts will be added only after they
actually exist. Progress logs and atomic edge checkpoints remain in the
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
