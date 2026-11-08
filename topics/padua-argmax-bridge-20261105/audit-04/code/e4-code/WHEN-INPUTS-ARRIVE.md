# Blocked checks: exact next commands once AC supplies the artifacts in audit4/inputs/
Preregister scope first (append PREREG-02.md). All runs under e4-code/observe.py.
1. sha256sum + stat each input; require the brief's bytes/SHA (da63280a..., c22d600c..., d7cea34d..., d1d03156..., 96f84b29...).
2. Canonical ZIP (needs the COMPLETE trusted package incl. 171 headers/6 debs; e4-run/pkg lacks them -> the reader's
   R.pins() cannot pass on this machine; supply padua30.zip aac08e5f... too): from a git-archive copy with
   local-output/argmax-bridge-20261105/{compact-release-aea62883/padua30,phase-checker/runtime/extracted/usr} restored:
   python3 -B topics/padua-argmax-bridge-20261105/code/local_onset512_campaign/return_bundle.py verify <zip>
   (confirm sys.flags.optimize==0 and PYTHONOPTIMIZE unset; record it).
3. Independent ZIP inspection with own code (no reader): member names/safety, COMPACT.json hashes, 191x2 receipts,
   exits/attempt/admission/stage linkage, seed->[475,458], sampled closure presence.
4. Certificates ZIP + inventory: byte-compare the 382 members to the canonical ZIP's jobs/n/{produce,verify}/essential-receipt.json.
5. I25 bundle: proofs/n*-*.json (942): 560 vs e4-run/old560-receipt-identities.json (byte), 382 vs step 4 (byte).
