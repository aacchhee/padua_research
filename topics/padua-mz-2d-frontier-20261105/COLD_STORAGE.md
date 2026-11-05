# Cold storage — signed Padua MZ frontier

**External delivery PENDING.** AC’s intended destination is
`Downloads\padua\cold_storage\padua-mz-2d-frontier-20261105\`.
No Windows or other external-machine access was used, and no retrievable
archive at that destination is claimed.

## Actual staging and identity

[cold-storage.json](cold-storage.json) inventories only present local
G0/G1 scratch output and the m1600 vector, with exact byte sizes,
SHA-256 and embedded generating commands. The source checkpoint pins
the committed G1 regeneration code; the detailed receipts also pin
actual source hashes. The m1600 vector is10,246,528 bytes, SHA-256
`a23cb0e6e241993e5458474c64f153c965e8dc5047c2f1dfe08c7bc293e0a338`,
at `/tmp/g1-frontier/minimum-only-vectors/m1600-n1599-min.npy`.
It is an uncertified measured witness candidate, not necessary evidence
for the analytic countersequence theorem.

The native and independent certificate receipts record their own exact
pencil and transform paths, sizes, hashes, actual generating/checker
commands and accepted results. Those bulky matrices are regenerable;
some contiguous-batch matrices were pruned after checking and are not
listed as present staging. Small committed exact acceptance receipts,
independent reconstructions and full regeneration code support the
finite computer-assisted records. No unretained scratch bytes are
silently treated as an archive or as a uniquely necessary certificate.

## Storage procedure and limitation

AC’s policy says not to store large outputs that can be regenerated.
Accordingly no bulk file was committed for later removal. Actual run:

```sh
python tools/cold_storage.py plan topics/padua-mz-2d-frontier-20261105 --threshold 16384
```

It found zero tracked generated files above threshold. The existing
storage tool restores/exports historical Git blobs; fresh scratch files
have no Git blob and cannot be honestly exported by that interface.
The standard manifest therefore has zero Git-backed `entries`; its
separate `local_staging` inventory records actual temporary files.
Verification of the empty standard entry set does not verify or deliver
those local files. No dummy export or historical blob identity is
invented. Delivery remains pending rather than blocking analytic work.

## Regeneration and checks

Commands, seeds, versions, code hashes, actual acceptance and limitations:
[numerical-results](numerical-results.md), [G0](independent-checks-g0.md),
[native results](certifier-results.md),
[independent exact checks](independent-checks-cert.md),
[independent analytic checks](independent-checks-math.md).
Run the committed producers and then the separate checker exactly as
those records describe. For all-integer producer2..60, independent
coverage is only10/20/30/40/60; m80 is separately independently checked.
No m100 acceptance or finite exact m1600 counterexample is claimed.

The staging inventory can be refreshed using
`python topics/padua-mz-2d-frontier-20261105/code/staging_inventory.py`;
changed timing/proposal outputs need not reproduce historical byte
hashes. Recomputed measurements are new executions. Analytic proofs
have no bulk-output premise.

## Retention and retrieval

Temporary scratch has no promised retention; workspace loss can remove
it. AC is the eventual custodian only after an actual delivery/verification
receipt. The code and short evidence remain in the topic branch. To
retrieve historical scratch bytes, use an actually present listed file
and verify its hash; after loss, regenerate instead and do not claim
byte-exact retrieval. No archive was transferred in this session.
