# PD-T?argmax-bridge-codex-F1 — Exact Padua corner argmax at degrees 33–40

2026-11-08 provenance clarification (audit-03 G-2): the audit-pending
sentence in the historical development section below is superseded by the
completed [audit-01](../audit-01.md) and [audit-03 assembly review](../audit-03/g-assembly.md).
This remains a provisional source record, rather than an already assigned
PROOF_STATUS row. Its theorem, certificates and implementation pins are unchanged.

ID kind: PD-T. Aliases: native bridge extension; accepted finite certificates.
Split from: the finite cases of PD-T099; the remaining bridge stays OPEN.
Split into: none.

## Statement

For every n in {33,34,35,36,37,38,39,40}, use the corrected even-checkerboard Padua
cardinals of PD-T101. On the closed physical square the maximum of
lambda_n is Lambda_c(n), and equality holds exactly at the two nonnode
corners: {(-1,-1),(-1,1)} for odd n and {(-1,-1),(1,-1)} for even n.

## Definitions and assumptions

The node weights, exceptional (n,0) coefficient, corner values and
certificate predicates are exactly PD-T101/210. GMP integer/rational
arithmetic is exact. The frozen checker reconstructs the cosine brackets,
cardinals, Bernstein coefficient enclosures and complete tree partition;
it does not trust a producer approval bit or floating measurements.

## Status

Overall status: **PROVED**, computer-assisted via PD-T210 and the executed
independent replays below. Development theorem; required Claude audit of
this campaign is pending. No phase-box prototype is a premise.

| n | Essential certificate | Bound/corner leaves | Separate acceptance |
|---|---|---:|---|
|33|[n33.json.gz](../evidence/n33.json.gz)|284 / 2|[receipt](../evidence/independent-n33.json)|
|34|[n34.json.gz](../evidence/n34.json.gz)|288 / 2|[receipt](../evidence/independent-n34.json)|
|35|[n35.json.gz](../evidence/n35.json.gz)|298 / 2|[receipt](../evidence/independent-n35.json)|
|36|[n36.json.gz](../evidence/n36.json.gz)|306 / 2|[receipt](../evidence/independent-n36.json)|
|37|[n37.json.gz](../evidence/n37.json.gz)|316 / 2|[receipt](../evidence/independent-n37.json)|
|38|[n38.json.gz](../evidence/n38.json.gz)|320 / 2|[receipt](../evidence/independent-n38.json)|
|39|[n39.json.gz](../evidence/n39.json.gz)|330 / 2|[receipt](../evidence/independent-n39.json)|
|40|[n40.json.gz](../evidence/n40.json.gz)|350 / 2|[receipt](../evidence/independent-n40.json)|

## Depends on

PD-T101's cardinal construction and unisolvence; PD-T210's proved exact
finite-certificate implication, including corner equality classification.
The unmodified native producer and separately authored C++/GMP checker
are the accepted implementations used for earlier degrees, with n<=100
implementation guards. No assumption of global corner maximality is used.

## Proof and actual checks

The certificates are finite complete binary partitions. Each normal leaf
has a strictly separating exact bound; each of the two corner leaves
has PD-T210's strict off-vertex predicate. The independent checker
reconstructs and verifies every supplied bound, both corner leaves,
metadata and the entire prefix partition. Therefore PD-T210 yields the
displayed maximum and equality set at each of the listed degrees.

The producer ran in a different worker from the checker. The producer
always writes accepted=false. The checker accepted all eight listed complete artifacts
in fresh independent executions, with these frozen identities:

- n33 certificate SHA256 `090f650ae5d52d72716857e8a67a8fac7c330fa208ff81487368e1ef89d82f90`.
- n34 certificate SHA256 `8c4866e2bda66e331e4940f17ace71b9caeb8ecf0bdd091bf026d215b21acb2d`.
- n35 certificate SHA256 `cdf5058f476692d1fc3847b8b59ca44ffe9cecd9ffc3271a2d47b733464935bb`.
- n36 certificate SHA256 `067fcf2af8eb2f112f65f2689ecd7102b87f1b2cb31b2508d97ba09be0d9f22c`.
- n37 certificate SHA256 `425fb779e3d476efe221f6d1bef118cb1752fa9f538a46110b7ea2b44f2cefae`.
- n38 certificate SHA256 `fcb900fab6b596b7d258668e0de49a4bf9b76bc9d3f4c879ebb358d7b792f1d2`.
- n39 certificate SHA256 `af0c1dfdf4ea59560c23e83ebd4136b9b7ce783a253d1165f0cdbd1ace01d8f6`.
- n40 certificate SHA256 `37cb278ad498d9f531634b2dca470426a86339b5d83cd437bfb2dd093afa374f`.
- checker driver SHA256 `b6c7320db2f7cfebf27fe33aa38ffdd45ff719870e3d23e15f845b6e8026eb2e`.
- checker kernel SHA256 `b0c871e7711219edfe3ce01480d8d1de3503a20d9b59f82b63a00eff248bc6e0`.

[Independent record](../independent-checks-initial.md) gives exact commands,
versions, binary/source pins and scope. [Native producer inventory](../evidence/n3-native-producer.json)
gives generating argv, inputs and setup/search CPU costs. Checker commands,
from repository root after compiling its kernel in a fresh work directory:

```sh
python topics/padua-argmax-effective-20261103/code/native_checker/check.py topics/padua-argmax-bridge-20261105/evidence/n33.json.gz --binary local-output/argmax-bridge-20261105/check-initial/kernel --output local-output/argmax-bridge-20261105/check-initial/replay-n33.json
python topics/padua-argmax-effective-20261103/code/native_checker/check.py topics/padua-argmax-bridge-20261105/evidence/n34.json.gz --binary local-output/argmax-bridge-20261105/check-initial/kernel --output local-output/argmax-bridge-20261105/check-initial/replay-n34.json
```

The original executions used the byte-identical candidate files in local
working output; the committed files above were copied and rehashed by the
coordinator. The record distinguishes actual argv from these portable
committed-file replay commands. The n33 [corruption suite](../evidence/independent-controls.json)
rejected36 defects, accepted the complete positive control and refused to
accept a genuine partial cover. Normal and control replays were separate;
only identical degree/frontier arithmetic was cached inside the controls.

The environment transition lost shell session handles after the normal
jobs finished. Their complete checker-written acceptance receipts persisted
and were read and verified; no shell exit status was invented or execution
repeated. The driver writes acceptance only after successful native replay.

## Sources, scope and open items

Internal accepted finite reduction only; no external theorem transfer or
novel mechanism. This is an ordinary finite-range extension of IDEA343.
Trusted components are the committed mathematics/checker code, Python
envelope parsing, compiler and GMP integer/rational implementation. The
small essential certificates and acceptance receipts are committed; unique
unarchived timing/sample files are not proof dependencies.

Combined with inherited degrees2–32 this gives the independently checked
finite range2–40. The eventual PD-T229 onset remains non-effective. The
remaining bridge is41<=n<N_*. All-degree PD-T099 stays OPEN.

## History

2026-11-05, Codex coordinator requested Astra high; producer worker requested
Sol medium; distinct checker requested Astra high. Serving identities and
effective efforts are unexposed. Certificates retained at0bca52b; independent
acceptance arrived during the subsequent WORK step. No shared registry or
final-ID assignment, and no Claude audit completion is claimed.

2026-11-05 scope extension: the first statement covered33/34. Subsequent
separate checker executions accepted35/36 with complete partitions and all
bounds verified, at820.595/925.802seconds wall under concurrent load. The
statement now covers33–36; no earlier receipt, audit scope or execution is
rewritten. The same proved reduction and unmodified independent kernel apply.

2026-11-06 scope extension: separate unchanged-kernel executions accept37
and38, with complete partitions, both corners and every supplied bound.
Actual checker CPU897.768536/1049.906113 seconds; wall918.566803/1072.093637.
[New independent block record](../independent-checks-native-37-40.md)
preserves exact argv, source/binary/input hashes and actual exit status.
The37–40 producer inventory is `../evidence/native-37-40-producer.json`;
producer acceptance remains false. Degrees39/40 are complete producer
candidates under separate checks and are NOT part of this proved statement.
No source/receipt or historical acceptance is rewritten.

2026-11-06 final fixed-block acceptance: independent39/40 executions also
finish with complete partitions and every exact bound/corner verified, exit0.
CPU1195.500276/1366.972668seconds; wall1216.615418/1367.457987.
The preceding39/40-pending statement records the earlier checkpoint, not
the current disposition. All37–40 first replays pass; total checker CPU
4510.147593seconds, no failure/restart. The statement now covers33–40 and
the inherited combined exact range is2–40. Required Claude audit remains
separate. The new phase-route calibrations at17/24/32 do not extend it.
