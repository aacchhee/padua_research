# Independent compiled checker route

Current status: corrected checker b0c871e7… accepted certificates n9–32
across the attributed workers below. Isolated n40 remains unverified after
its corrected replay reached the configured 600 CPU second cap. The older ae4f20b6… results below are
historical measurements, superseded for proof use by the GMP finding.

Rules read: `8a1f394739293953e1566fd24a0a193cc78ff26f`.
Base: `440d1079e42c3ef21c40d1cf8870f5b206410c6a`.
Agent: Codex, gpt-6.1-sol medium, explicitly tool-configured by the
orchestrator with fork_turns=none; runtime internals beyond that tool
configuration are unexposed.
Role: delegated independent checker implementation; no Git authority.

Scope: independently port the historical PD-T210 finite-general verifier
into a compiled GMP arithmetic path. No new mechanism, literature,
priority or novelty claim is proposed, so this bounded implementation
work does not require an additional ideas gate. The topic orchestrator
owns the campaign gate and mathematical status records.

Plan (before execution, sent to orchestrator): independently implement
Machin/Taylor, outward 192-bit integer constructor, exact rational tensor
Bernstein conversion, recursive subdivision and leaf predicates in C++;
use Python only for strict JSON, provenance, prefix cover and receipts.
Crossvalidate historical n9–16 and new producer n9–24; reject every
historical corruption case and malformed inputs. Kill criterion: any
metadata or leaf-bound mismatch blocks all finite-range extension claims
until explained and fixed. CPU work stays inside the authorized ~30 min
round; no external dependencies or network access needed.

Independence: read historical reference checker, `finite_general.py`,
`finite_bernstein.py`, `finite_general_controls.py`, provenance guard and
PD-T210 theorem. Did not inspect or import producer-agent arithmetic.
Shared inputs are mathematical formulas, certificate schema, prescribed
rounding sequence and source compatibility convention. Implemented all
arithmetic separately using C++ GMP mpz/mpq. See `code/native_checker/README.md`.

Executed validation of the frozen final candidate:

- Built with `g++ -O3 -std=c++17 .../kernel.cpp -lgmpxx -lgmp`.
- Historical certificates n9–16 all accepted with exact metadata and
  every integer leaf verdict reproduced. n12 historical input has basename
  `finite_n12_pilot.json.gz`; the others use `finite_nN_general.json.gz`.
- Authoritative final native producer n9–31 all accepted by this worker
  with exact reconstructed metadata and integer leaf verdicts. Required
  overlap n9–24 is complete. n24 has 152 bound and 2 corner leaves, 153
  splits; final-path replay took 37.584 s. n31 has 280 bound and 2 corner
  leaves, 281 splits; 194.124 s. These are wall measurements under shared
  load. Native n32 was independently accepted by the Codex gpt-6-astra
  high worker, using the same frozen checker sources and independently
  built binary; this worker did not redundantly replay n32. Its explicitly
  attributed receipt is incorporated in the compact summary.
- All 14 historical corruptions rejected on n9 and n17. Added 22 malformed
  JSON, strict-type, frontier, and compiled-protocol negatives: 36 rejected
  in total on each degree. Complete positives were accepted; genuinely
  partial positives were verified with accepted=false. Receipts:
  `controls-n9-final.json`, `controls-n17-final.json`.
- Repeated all 36 n9 controls under `PYTHONOPTIMIZE=1`; every negative
  remained rejected and both positive behaviors were preserved. Driver
  validation uses explicit exceptions, so optimization cannot remove it.
- Compiled signed-floor/ceiling, mixed-sign multiplication, negative
  rational transform, de Casteljau, Machin bracket and exact cosine-axis
  identity controls passed via `unit.cpp`; receipt `unit.json`.

External evidence root: `/workspace/padua-work/checker/`.
Source candidate hashes: kernel
`ae4f20b69c5e676a5d2fefa55c903c8b3efd87a5807a5c5617ca21390a1cab3d`,
driver `b6c7320db2f7cfebf27fe33aa38ffdd45ff719870e3d23e15f845b6e8026eb2e`.

Required scope is complete through n32 using the explicitly attributed
independent n32 receipt. Pending: optional isolated n40 replay, authorized
by root after its producer probe completed. It runs with RLIMIT_CPU=600
and nice increment 10. No degrees n33–39 were run. Different-worker review
and the separate Claude audit remain distinct. No theorem status upgrade
is made in this implementation record.

Implementation refinement: the independent reviewer identified avoidable
rational normalization in subdivision. Replaced half-averages and
scaled-product rounding by GMP direct integer floor/ceiling shifts,
without changing the arithmetic result; repeated unit controls passed.
All required n9–24 production and n9–16 historical replays were regenerated
with the final source and binary hashes. Earlier receipts are superseded.

Provenance-final artifact transition: producer subsequently froze native
source provenance and wrote authoritative certificates under
`/workspace/padua-work/producer/final/`. Earlier top-level artifacts have
identical mathematical payloads through n24 but different raw hashes.
Explicit fresh replays of final-path artifacts n9–31 completed; their
receipts use `nN-final-producer.json` and `controls-nN-final.json`. Earlier
`nN-producer.json` receipts remain historical and are not the authoritative
final-provenance receipts.

Final-range compact evidence: `evidence/native-checker-summary.json`,
9975 bytes before the optional n40 result. It records all source, binary,
certificate and receipt hashes and verifies the repository evidence
copies n17–32 against the authoritative raw certificate hashes. The n32
row explicitly cites the independent worker's receipt instead of claiming
an own run. The wrapper for the sequential batch was intentionally
terminated after its n31 child completed, to avoid a redundant n32 replay;
that wrapper's exit137 is cancellation, not a failed mathematical check.
An obsolete top-level n27 continuation was likewise cancelled after the
provenance-final artifact transition.

Fresh checker CPU benchmark (driver plus waited native child), measured by
RUSAGE_CHILDREN deltas: n17 = 5.416757 user + 0.056735 system = 5.473492 CPU
seconds; n24 = 35.021238 user + 0.261824 system = 35.283062 CPU seconds.
The CPU measurement differs from the concurrent wall measurements above.
Reproducible external script and receipts: `cpu_bench.py`, `cpu-bench.json`,
`n17-cpu-benchmark-check.json`, `n24-cpu-benchmark-check.json`. These values
were supplied to the producer worker for an end-to-end budget projection.


## GMP operand contract finding and correction

The checker worker found, and the independent worker confirmed, that GMP
`mpq_class(num, den)` initializes an unreduced representation. The old
Bernstein weight summation supplied such temporaries to rational addition,
which formally requires canonical operands. Matching prior finite outputs
did not waive this precondition. Root classified this as a blocker and
withdrew proof use of the old acceptance snapshots. The original kernel
and binary are retained externally as `kernel-precanonical.cpp` and
`kernel-precanonical`; the old summary is `summary-precanonical.json`.

Correction: added `ratio(Z a,Z b)` which constructs the rational and calls
`canonicalize()`, and replaced the actual Bernstein weight term constructor
by this helper before `+=`. Corrected unit comparisons also use canonical
rationals. Other direct two-argument constructors have numerator one and
positive power-of-two denominator and are canonical already. No formula,
rounding sequence, predicate, or certificate changes.

Frozen corrected kernel SHA256:
`b0c871e7711219edfe3ce01480d8d1de3503a20d9b59f82b63a00eff248bc6e0`.
Corrected binary SHA256:
`f17fed2e69a98c952d1ad5e72de03c08b2ceb07970c49fc0db1b35396fe3e605`.
Driver unchanged at `b6c7320d…`. Corrected unit controls passed; receipt
`unit-corrected.json`.

Root's final allocation: this worker replays n9–24 and n29–31 sequentially
and repeats controls; gates worker independently rebuilds and replays
n25–28; independent gpt-6-astra high worker checks every actual corrected
Bernstein weight against Python Fraction for n2–40 and replays n32 and
n40. Four heavy jobs maximum under the 16 GiB limit. An initial corrected
n29 child was cancelled without a receipt when root clarified the one-job
allocation for this worker. It is not a mathematical failure.

Old n40 was cancelled by root's instruction after 399.397 CPU seconds,
without acceptance. Its cancellation receipt is
`capacity-n40-precanonical-cancelled.json`; no proof claim uses it. The
corrected n40 replay has a separate 600 CPU second limit.

Corrected CPU17/24 measurements are instrumented around the normal fresh
replays, and supersede the old performance values as the primary cost
model. Old benchmark receipts remain historical; corrected values will
be published as `cpu-bench-corrected.json`. The final compact repository
summary will be replaced only after every attributed corrected acceptance
and required control is checked.


## Corrected acceptance completed through n32

Final corrected kernel b0c871e7… and binary f17fed2e… remained frozen.
Actual corrected full replays: checker worker n9–24 and n29–31, gates
worker (Codex gpt-6.1-sol medium) n25–28, independent worker (Codex
gpt-6-astra high) n32. Every accepted receipt pins the canonical final
certificate, exact new kernel/driver and executable hashes. Source/bin
hashes agree across the independently compiled builds. The compact v2
`evidence/native-checker-summary.json` is 12653 bytes before the optional
n40 outcome and explicitly attributes the external worker rows.

Corrected controls on n9 and n17 rejected all 36 historical/malformed
cases, accepted the complete positives and verified genuinely partial
positives with accepted=false. Corrected Python-optimized n9 repeated
those behaviors. Corrected unit controls passed. Receipts are
`controls-n9-canonical-final.json`, `controls-n17-canonical-final.json`,
`controls-n9-canonical-python-optimized.json` and `unit-corrected.json`.
The independent worker checked all 23816 actual production Bernstein
weights for n2–40 against Python Fraction/binomial arithmetic, including
canonical numerator/denominator gcd and sign. That committed-path receipt
is `evidence/canonical-weight-differential.json`, SHA256
`8d102246ae2b5e1796628c7cff59b0d6914bbcfecc8e402b86e688b58394d88a`.

The summary generator directly checks every original Python acceptance
receipt for n9–24 against its raw checked certificate and source hash,
then compares every field of that certificate with the final corrected
native input, excluding only setup/search/total timing and producer
provenance. All mathematical fields agree exactly. Root instructed that
this crossvalidation suffices; no redundant corrected historical n9–16
sweep was executed. The queued wrapper was retired after n31 and only
required controls were then run. No such wrapper cancellation is a
mathematical failure.

Corrected primary CPU benchmark, `cpu-bench-corrected.json`: n17 user
4.982995 plus system 0.027509 = 5.010504 CPU seconds; n24 user 34.565649
plus system 0.212411 = 34.778060 CPU seconds. These fresh normal replays
include the driver and waited native child via RUSAGE_CHILDREN deltas.
Earlier CPU data remain historical and were not relabeled as corrected.
Root and the producer received the corrected values for the final cost fit.

No remaining checker finding blocks the corrected n9–32 receipts. The
separate Claude audit remains required. No degree n33–39 certificate was
checked. Isolated n40 is delegated to the independent worker and is usable
only if its actual corrected replay accepts within its resource cap.


## Final scope and isolated n40 capacity outcome

All assigned corrected acceptance/control work is complete. The independent
n40 replay reached its configured 600 CPU second limit (SIGXCPU), wall
605.562 s, and produced no acceptance receipt. This is a resource-limited
unverified case, not a rejection of the supplied certificate or of the
mathematical claim. Independent run/resource receipts are
`/workspace/padua-work/independent/canonical-check-n40-run.json` and
`canonical-check-n40-resources.json`; the final compact summary hashes
both. The producer-complete n40 artifact remains evidence of discovery
only. No isolated accepted degree is listed. No degree n33–39 certificate
was checked, and the highest contiguous newly accepted range remains
n17–32 (with existing earlier proofs handled by the topic orchestrator).

Final `evidence/native-checker-summary.json`: 13147 bytes, SHA256
`caeaf733c68fd0cce5ac1e8f8125f78ed4c1149c595f937a3107a67fc8262997`.
It retains the GMP finding, validates all corrected raw receipt/source/
binary/certificate hashes, directly rechecks Python crossvalidation,
and attributes gates/independent worker executions. All own code and
summary sources are frozen. Root explicitly requested no further runs.
The separate Claude audit and topic Git/handoff actions are root-owned.
