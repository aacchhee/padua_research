# Native checker recorded provenance — response F8


The source–binary link rests on the recorded build command in the
[pinned checker README](code/native_checker/README.md) and acceptance
summary, and the
source/executable hashes. `check.py` and `controls.py` hash the adjacent
`kernel.cpp` at replay time; they do not compile a frozen source snapshot
or embed compiler/GMP versions in each receipt. These drivers and all
existing receipts are unchanged by this documentation response.

Existing records establish the following, without reconstructing the old
environment from current tools:

- [native-checker-summary.json](evidence/native-checker-summary.json)
  records compiler `g++ (Debian 14.2.0-19) 14.2.0`, its build command, corrected
  source and binary hashes, and the corrected acceptance worker allocation:
  checker author n9–24 and n29–31; gates worker n25–28; supplementary
  reviewer n32. It does not record a GMP version per corrected receipt.
- [The producer attempt](attempts/native-producer.md) and
  [producer summary](evidence/native-producer-summary.json) record
  GCC 14.2.0, GMP 6.3.0 and Python 3.12.14 for the producer environment.
  That is campaign context, not a receipt-level GMP attestation for each
  checker worker's corrected build.
- [Claude audit-01, technical replay](audit-01.md#technical-replay-of-native-certificates-sub-auditor)
  records a fresh build and accepted replay of all n17–32 certificates,
  with GCC/G++ 13.3.0, GMP 6.3.0 and Python 3.13.18. These are the auditor's
  versions, not retroactive versions for developer receipts.

The per-run compiler/GMP mapping for every developer corrected acceptance
receipt cannot be completed from the retained records. This provenance
limitation remains explicit (F8 unresolved in that respect); a current
version query would not establish historical versions. Audit-01's fresh
build/replays support the accepted finite claims at their stated scope.
