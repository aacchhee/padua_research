# Local onset-512 campaign

The historical `runner.py` was a local orchestration adapter around the unchanged frozen engine
and trusted compact-pack validator/storage implementation. Its campaign procedure created one
exclusive output root with `preregister`, ran the actual n=320 `pilot`, then
`remaining` (321..510), at most four cases concurrently. Each degree received
one primary and one separate fresh verification. Failures stopped new admissions.
There is no retry or resume command.

See [the preregistration](../../preregistration-onset512-local.md) for pins, scope,
caps, prior cheap controls and the exact historical execution commands. The
campaign wrote its evidence under the named `local-output/` tree; current
availability is limited as recorded below and in response-05.md. No large
evidence is committed.

The local validator subclasses `Access` only to authenticate identities directly
at their retained local paths and to read the separately trusted release's
arithmetic-pin record. Every other pass check is the released `validate_pass`.
The scientific engine, reduction and arithmetic have not been modified.

## Runner and reader provenance — 2026-11-13

The recorded 320..510 campaign ran historical runner
`459d0728a0cb264d241bc76d270209842fc2aa55c0fadd32e23f8e3b0523af9e`.
The current runner is
`a198b65182590be13cb91110ff976d90e7e885c778180e59699fbe9b067ccdad`;
it has executed no campaign. Its repairs cannot be attributed to the historical
run, and its runner-identity check prevents continuing that run with this file.

The current reader candidate, `return_bundle.py`, is
`3f903e62b5c155e85603be43a60724c226b800dd9908685146fd7c5b69c2c234`.
It preserves the historical runner pin and adds the producer-written per-pass
`storage-dedup.json` (exact schema, nonnegative integer counts and fixed scope)
and the empty top-level `.preserve.lock` to the allowlist, addressing
[audit-05 E5-01](../../audit-05.md). The supplementary response-05 evidence review accepts this repair within its
synthetic storage/export scope; the canonical onset ZIP remains unavailable
and has not been checked with it.

Run the synthetic regression from the repository root:

```sh
python3 -E -B topics/padua-argmax-bridge-20261105/code/local_onset512_campaign/check_reader_repairs.py
```

The roundtrip calls the real `deduplicate()`, `completed()` and `export()` on
inert synthetic data, retains the actual empty lock and all 382 storage receipts
in the produced archive, and checks that archive with the reader. Trust pins,
proof arithmetic and sampled closure verification use explicit adapters; this
is a storage/export compatibility control, not a canonical-data or arithmetic
rerun. No native engine or campaign runs in this test.
