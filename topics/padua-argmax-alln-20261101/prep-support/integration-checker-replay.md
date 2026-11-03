# Checker replay after repository-wide cold-storage integration

2026-11-03. Codex developer, requested/configured `gpt-6.1-sol` high; serving metadata unavailable. This is a bounded integration check after AC merged PR18 as main `1acebf7af47885654dfd1ffe0b9c8cda19c8f2a6`. It adds no mathematics, certificate, numerical scan or checker predicate. The final independent reviewer assesses this new adapter separately; the earlier checker-hardening report/receipt and final audit remain frozen.

## Dependency finding

The merged main leaves the n8 field source and the PD-T101 dependency theory unchanged. Their relevant identities and all 74materialized inherited code/theory blobs inspected match the new main tree. In particular, the general constructor's `dependency_sha256` remains `ea59aa077a4d021fc69354383f69340f21d17d87d3a28c6ecaaf302cc763612c`, exactly its frozen certificate pin. No source-version compatibility change is needed for this integration.

One direct inherited scientific input moves off the head:

| Path | Bytes | SHA-256 | Git blob | Source commit |
|---|---:|---|---|---|
| `topics/padua-proof-attempts-2-20261101/outputs/a5_n4_certificate.json.gz` |64,360|`14a69a131b3c20416fd5521bd971efdadd4e3741f70546d0fc5f0d9f25a2cf61`|`d768d04857c580459547f090a1256fd4ed8bed58`|`2b52b432fe59c9a50aef9deebe5152c5d6874465`|

It is one of 23 entries in the inherited part2 cold manifest. The 4,148-byte `a5_n4_global.json` remains at the head. The field n8 and general n8–16 replays do not need the moved JSONs. The two exact O-Lt pairing routines read the n4 certificate's accepted root boxes, so the frozen replay runner's direct command assumes a now-cold file is materialized. This diagnosis is from source/manifest inspection; no separate failing full direct replay is claimed.

## Scratch-only integration adapter

The new [integration-checker-replay.py](integration-checker-replay.py) leaves every existing checker, arithmetic source, certificate and frozen replay script unchanged. It:

1. Reads the merged inherited manifest, requires an actual source Git commit and exact regular-file source-path/blob association, verifies the archived n4 byte size and SHA, and requires that the file is absent from the source worktree.
2. Copies current materialized scientific inputs into an exclusively owned outer temporary mirror, omitting every inherited cold path. It restores **only** the one required 64,360-byte n4 artifact there and verifies its readback hash. The other 22 inherited cold entries stay unrestored.
3. Gives that isolated fixture Git object access through a read-only alternates locator to the real source repository's object store. No commit identity is invented, no shared index/ref is changed, and no artifact is restored to the source checkout. This allows the frozen runner's existing source-pinned retrieval of its own historical pairing input to work unchanged.
4. Executes the exact byte-identical frozen [checker-replay.py](checker-replay.py) in that outer mirror. That runner creates its own inner scratch mirror and performs the same 40 subprocess invocations. The adapter requires exact equality of the semantic summary, optimization-refusal count, invocation count and all guarded-source hashes to the frozen hardening receipt.
5. Verifies all 17 monitored source/frozen-record hashes unchanged and that the newly cold n4 file remains absent from the source worktree. Both mirrors are removed when the command completes.

After the main integration, use:

```text
python -B topics/padua-argmax-alln-20261101/prep-support/integration-checker-replay.py > <fresh-scratch>/integration-checker-replay.json
```

Run from a checkout with the actual source commits/trees/blobs available. A selected-file snapshot must retrieve missing pinned objects through the authorized connector; a blob-only hash is not substituted for source-path verification. The original pre-integration report remains a true record of its earlier input. This dated adapter is the current full-replay command; it does not grant permission to put cold evidence back on the head.

## Actual integration execution

Executed the command above from the merged working candidate in `/workspace/padua-prep-20261103`, with stdout/stderr only in new `/tmp/padua-integration-checker-replay.*` files. Environment: Python 3.12.14, SymPy 1.14.0, Linux. **PASS**:

- 40 invocations and 21 optimization refusals, identical to the frozen replay scope;
- standalone n2 and all 10 existing field/general certificates replay;
- 14 general, 5 field, 4 independent-general and 17 D3 malformed controls reject;
- exact pairing and independent rational reconstruction pass;
- D3 retains 10 whole-cell pairs and 8 exact witnesses;
- the two forged n2-source-pin controls reject;
- all 242 inner scientific input hashes and 17 outer monitored source/frozen-record hashes remain unchanged;
- zero cold-dependency writes to the source worktree; only the one inherited n4 certificate restored in scratch.

This does **not** rerun the full inherited n4 completeness/count certificate proof; the pairing inference retains the same accepted inherited dependency and scope as before. No global degree>=17 certificate or research round is run.

The [small integration receipt](integration-checker-replay.json) pins the driver, merged cold manifest, restored object, current guarded sources and actual output hashes. Its `working_copy_git_head` remains the genuine local selected-snapshot head `cdb12257af24ea2542de707b9730f8278d69a168`, distinct from main's integration commit and the parent's subsequent connector publication. The frozen runner's declared input is also preserved verbatim; current candidate source-file hashes identify what was executed. Neither field is relabeled as a later commit.

Delivery to AC cold storage and any history purge remain separate from this scientific integration check. Scratch retrieval is not AC delivery. No native Windows or WSL execution is claimed.
