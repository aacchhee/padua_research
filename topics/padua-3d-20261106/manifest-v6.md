# Manifest v6 technical verification

Rules/input head: `97c323bfae15cf3c76f40802c3ebabedceeb0c60`.
Codex development, technical verification, zero research rounds. No new
mathematical claim, registry ID, novelty claim, or research mechanism; the
novelty gate does not apply. Independent audit remains the orchestrator's task.

The v6 codec preserves the complete recursive code/evidence identity map,
byte sizes, raw 256-bit digests, and the separate inherited-input identities.
It excludes only `__pycache__` and `.pyc`, as before. The generator retains both
rules provenance SHAs; historical receipt pins and history files are untouched.
The shorter envelope moves codec detail into code and condenses explanatory
text; identity scope and limits remain unchanged. `--list` emits the same
indented decoded v4 map as v5, including key order on the actual baseline.
The verifier/list reader also accepts v4 and v5 and rejects unknown schemas.

The binary stream is `P3M6` followed by NUL, an unsigned canonical base-128
entry count, then entries sorted by UTF-8 path bytes. Each entry contains a
path prefix byte count relative to the previous path, suffix byte count,
suffix bytes, and unsigned byte size. A contiguous table of raw 32-byte digests
follows in entry order. The entire stream is zlib level 9 compressed and RFC1924
base85 encoded. The reader checks integer canonicality, bounds, path scope,
strict ordering/uniqueness, complete digest table, and absence of trailing
binary or compressed data. Verification compares the entire decoded map and
inherited inputs to fresh observations; an internally consistent entry omission
still fails against the actual recursive file set.

Executed command (Python 3.12.14, zlib runtime 1.3.2):

```sh
python topics/padua-3d-20261106/code/manifest_v6_check.py \
  --legacy-manifest /tmp/padua-manifest-v6-frozen/topics/padua-3d-20261106/evidence-manifest.json \
  --output topics/padua-3d-20261106/evidence/manifest-v6-check.json
```

The legacy input was copied before codec edits from the live master into the
named `/tmp` topic/root snapshot. Its SHA-256 is
`ec763c5efcf8300d7329819485cef4eafae10bb218795b871f9c567b0f6358d8`.
For a later rerun, obtain that exact v5 manifest from the recorded input commit
and pass it with `--legacy-manifest`; its bytes are the required input, not the
continued existence of this temporary directory. The default input is the
current master manifest and can also be v6: the checker synthesizes a lossless
v5 fixture from its decoded map to exercise backward support.

The committed JSON receipt pins both final checker code files and records 28
passed controls, including malformed base85/zlib, unsupported schema/binary
version, truncation, trailing data, noncanonical integer, invalid path/prefix,
duplicate/order, omission/addition, size/hash changes, and inherited-input
changes. Addition, omission, size and equal-size hash changes were also executed
through the CLI against files in a disposable topic copy. Legacy v5 verification
and listing were rerun against this same copy. Each live artifact and inherited
file was read once into the copy; all subprocess checks then used only those
frozen bytes. The resulting map fingerprint is in the receipt. Concurrent
source changes after copying do not change these checks. The copy contained
270 artifacts/1,461,819 bytes and produced a 15,612-byte v6 manifest. Its identity
fingerprint is evidence of that snapshot, not a claim that concurrent working
files remained unchanged afterward.

For the actual 261-entry legacy map, v5 was 16,259 bytes; v6 is 15,132 bytes,
saving 1,127 bytes. The payload alone shrinks from 14,634 to 13,914 bytes (720
bytes); holding the old envelope fixed gives 15,539 bytes. Sixty additional
synthetic entries use independently hashed deterministic contents and roundtrip
losslessly, but require 17,806 bytes. Across 0–60 additions, 29 fit below 16 KiB.
At the orchestrator's explicit direction, this capacity limit is reported
honestly instead of introducing an exotic encoding. Capacity depends on path
lengths and byte sizes; the synthetic threshold is not a universal guarantee.
The generator continues to reject manifests at or above 16 KiB.

The master `evidence-manifest.json` was never written by this work. Its final
regeneration/verification belongs to the orchestrator after concurrent workers
freeze. The JSON receipt is a completed snapshot check; changing or adding
receipt files later necessarily changes the manifest generated for the final
tree. No code pins prose, and no old receipt or historical identity is rewritten.

## 2026-11-07 informational-envelope followup

At the orchestrator's request, only the informational `format`, `artifacts_codec`
and `limits` values were shortened. Full codec/scope details remain above and
in the code; the envelope still states identities only, no proof, no archival
delivery and no independent audit. The schema, codec implementation, decoded
map, identity bytes/digests, inherited inputs, rules SHAs and generate/verify
commands are unchanged. The original JSON receipt remains a historical check
of the original code pin and was not modified.

Executed `python /tmp/padua-manifest-envelope-check.py` using Python 3.12.14 and
zlib 1.3.2. The temporary checker loaded the old saved code and current code,
copied every current artifact/inherited input once to a disposable topic/root,
and compared their manifests on the identical frozen rows. Only those three
informational fields differed; binary encodings, payloads, remaining metadata
and decoded maps were exactly equal. CLI generation, verification and listing
all passed on the copy. For 286 artifacts/1,594,810 bytes, compact manifest size
fell from 16,305 to 16,050 bytes, saving 255 bytes. Normal generated formatting
used 16,162 bytes. Five additional deterministic independently hashed synthetic
entries roundtripped with 291 entries in 16,317 bytes, below 16 KiB. These are
snapshot measurements, subject to subsequent concurrent artifact changes.

Old code SHA-256:
`11dcb5d0239a7cc5ea6b583a00027c0ae50822fa2800e36dc8a723766d2fc23a`.
New code SHA-256:
`40332bb4bf5e306cf9eb49a8e24ca867e0ae7809203b65f3fc60041155ff6a92`.
Frozen decoded map SHA-256 (sorted-key compact JSON):
`0a86b874ad5be3c7485cae7a15a572b86f08a7add558841d9acaab7603260c7d`.
The orchestrator's reviewer records the independent new-code pin/check in its
audit namespace. No new code/data file, old receipt edit, master manifest write
or Git operation was performed for this followup.
