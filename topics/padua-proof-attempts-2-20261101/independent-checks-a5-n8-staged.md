# N8 staged verifier — pre-run scope and kill criteria

Parent assigned14:16UTC, Codex gpt-6.1-sol xhigh. This record precedes
implementation. Own new staged driver/controls/output prefix and this receipt;
all frozen main/control sources remain immutable. No search or new mathematical
acceptance predicate is authorized. Root reviews the full new sources before
any real staged run; a different executor must run its own driver and controls.

Stage1 calls the original `Verifier.run(interior,allow_partial=True)` on the
actual supplied full interior, requires complete prefix/interior coverage,
zero pending/unresolved regions and independently checked root counts, and
atomically records ONLY interior verification. It never certifies a count.
The same live verifier state is retained while awaiting an atomic READY file.

Stage2 requires READY-bound raw hashes/paths for the final self-contained
count/global pair, exact equality of every interior mathematical field with
Stage1, unchanged summary except complete/edge/corner/total, and only explicitly
allowed join provenance in metadata. It executes the exact original run tail
from `no_unresolved` to return, extracted and AST-guarded against frozen main
SHA a9cff574…, with the already verified node result/prefix/leaves; then calls
the original `global_values`. Full flags appear only after all original tail
and global guards pass. Deadline15:19UTC; no pending stage is count acceptance.

Kill criteria: source/AST mismatch; changed interior data or forbidden summary/
metadata change; incomplete Stage1; missing/malformed/misbound READY; wrong raw
pair hashes; any original boundary/global predicate failure; deadline reached;
or inability to establish exact tail equivalence. Controls must reject those
structural mutations without running a new search. A failed stage retains its
explicit scope and cannot be silently upgraded. No actual staged run exists
at this writing.

## Implemented exact scheduling equivalence, before real execution

The chosen implementation retains the guarded-tail design. It imports only
the frozen independent checker, not a producer. Stage1's original run does
all original node/root/leaf checks on the full supplied interior; because
edges/corners are required absent, its tail performs no boundary mutation.
All live verifier state, including roots, node cones, compatible-mask counts,
gradient counters and global exception occurrences, is retained unchanged.
No verifier state is deserialized or accepted from a receipt.

After exact typed-JSON equality of every reused field, the corresponding
original full run would have the same state immediately before its tail.
The staged call supplies the four original node-result keys copied from
Stage1's returned node result, the identical leaves, and complete_partition
True only after Stage1 verified that fact. It passes allow_partial=False.
The literal original tail then checks all boundaries, final summaries and
complete coverage, and original global_values checks the raw-bound final
global certificate. Stage1's earlier tail adds no mathematical premise and
does not change this state. No new exclusion, root or count predicate exists.

The extracted AST is exactly original Verifier.run's statements from the
no_unresolved assignment through return, with SHA256
`14ec9c77c3afef4d585b3017a0d3b2f32f6cf0b705ff73c188fea92f4c2be7a5`.
Extraction first checks the entire frozen a9 source hash, then the AST hash.
Its wrapper only supplies the original locals and executes against the
unchanged checker globals. The four node-result keys exactly match the
original node_certificates return. Root read the full new driver and found
no mathematical issue with this equivalence; this is supplementary review,
not the required Claude audit.

Final fields must equal every original field except explicitly allowed
summary changes complete/edge/corner/total and metadata changes source_sha256
plus a mechanically bound join-provenance dictionary. Only edges, corners
and boundary_summary may be added. Equality uses canonical JSON bytes,
preserving types and rejecting true-for1 or1.0-for1 substitutions. Join
provenance must bind the exact original raw SHA/size/source. The READY marker
has exactly format,interior_sha256,certificate_path,certificate_sha256,
global_path,global_sha256, with format a5-n8-staged-ready-v1. Raw pair hashes
are checked before decoding, and input files/source bytes again after proof.
An atomic interior-only receipt is saved before waiting; a15:19UTC real-time
alarm and external termination fail closed. No real run started during design.

| Frozen new source/evidence | Bytes | SHA256 |
|---|---:|---|
| code/a5_checker_n8_staged.py |13914|`82385dd392513c476e83ed7c5a59c63e602e77d50279fb51a3976ac5857021ef`|
| code/a5_checker_n8_staged_controls.py |9059|`cff61e955854b4f07fb652593acefc5093a0b0c84177bad885bdc7cdb58dda8a`|
| outputs/a5_checker_n8_staged_controls.json |6682|`d04c12030d287cdcddc46a79bc8c105ba8badaf576c391385968953d4267010d`|

Actual local structural controls completed with exit0,43 cases passing,
controls-body time0.022297089seconds (whole shell call0.2564seconds).
Before/after staged-driver/control hashes and original main/control guards
passed. Controls cover typed interior changes, forbidden summary/metadata,
incomplete original state, missing/malformed/misbound READY, raw pair tampering,
expired deadline, AST/source change and receipt overwrite rejection. The
unchanged tail is also exercised on an explicitly nonmathematical structural
stub; that stub supplies no N8 acceptance. The complete control output has
count_certified=false and states this structural scope.

Exact actual command from /workspace/padua_research:

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/padua2-deps python -B topics/padua-proof-attempts-2-20261101/code/a5_checker_n8_staged_controls.py --output topics/padua-proof-attempts-2-20261101/outputs/a5_checker_n8_staged_controls.json > /tmp/a5_checker_n8_staged_controls.stdout 2>/tmp/a5_checker_n8_staged_controls.stderr
```

The different executor was asked to run these same controls with its own
output before either real staged run. Actual real-interior acceptance,
READY/final pair, full tail/global pass and different-executor results remain
pending. Original a9 main and7f57 controls are unchanged. This implementation
record does not claim any full N8 computation was executed.

## Released real execution: pre-launch record14:26:38UTC

Root read the full staged driver and explicitly released the real execution
after different-executor controls. That executor then reported an ACTUAL
exit0,43 controls (4 positive/39 negative), output6683bytes SHA256
`e0e512642f7e37f019d0eba8400c670d63da24114b504a25872c55c55564ed43`,
and both new/all prior source pins unchanged. This message, not merely an
existing output file, satisfies the release condition. My pre-launch raw
source checks again match82385dd3…/cff61e95…/a9cff574…/7f57ed9b….

At14:26:38UTC these exact commands are recorded BEFORE launch. Their actual
process completion and mathematical results remain pending at this entry.
The timer deadline is15:19:00UTC. Stdout tee preserves progress; pipefail
preserves the driver's actual failing exit if any. Outputs are fresh.
This root-released staged protocol supersedes the earlier proposed two
full-controls invocations: two actual staged verifications retain every
original full mathematical predicate, with separate old local controls,
instead of redundantly repeating the full positive in a controls process.

```bash
set -o pipefail
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/padua2-deps python -B topics/padua-proof-attempts-2-20261101/code/a5_checker_n8_staged.py --interior /tmp/a5-n8-interior-reflected-v1.json.gz --interior-sha256 a3b4f278a322338fb65f60922b4251265288148e1a09fd22882215004e81c324 --ready-file /workspace/padua_research/topics/padua-proof-attempts-2-20261101/outputs/a5_n8_staged_ready.json --interior-output /workspace/padua_research/topics/padua-proof-attempts-2-20261101/outputs/a5_checker_n8_staged_interior.json --output /workspace/padua_research/topics/padua-proof-attempts-2-20261101/outputs/a5_checker_n8_staged_full.json --deadline-utc 2026-11-01T15:19:00Z 2>/tmp/a5_checker_n8_staged.stderr | tee /tmp/a5_checker_n8_staged.stdout
```

The separate frozen old-control invocation exercises local tamper checks and
deliberately omits global-file, so it does not repeat the full interior proof:

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/padua2-deps python -B topics/padua-proof-attempts-2-20261101/code/a5_checker_n8_controls.py /tmp/a5-n8-interior-reflected-v1.json.gz --spatial-certificate /tmp/a5-n8-interior-reflected-v1.json.gz --output topics/padua-proof-attempts-2-20261101/outputs/a5_checker_n8_final_local-controls.json > /tmp/a5_checker_n8_final_local-controls.stdout 2>/tmp/a5_checker_n8_final_local-controls.stderr
```

Both commands actually launched after that record, staged session17005 and
local-controls session26410. The local controls have now ACTUALLY completed
exit0, all37 cases, in97.159733777seconds; original main/control source guards
are true and the input SHA is the declared a3b4f278… developer interior.
Output `outputs/a5_checker_n8_final_local-controls.json`,6498bytes, SHA256
`f7da11314963f0ad3f129f8f618b34b73d64faeb27c9419e3796fec7490b7998`.
Its generic scope is honestly local verifier controls with no degree-eight
count; no global/full-positive replay was requested or performed there.

Staged progress first observed at14:30:58UTC already includes1000 and2000
verified leaves (7180/8076 ordinary records), after all45 node records passed.
The elapsed260seconds from the pre-launch timestamp is only an observation
upper bound including node overhead; exact1000 emission occurred between
polls. No interior-only final receipt or complete count exists yet.

At14:32:25–30UTC, sampled stdout includes5000 leaves/9504 ordinary records
and6000/9810. Thus first5000 was observed no later than approximately347s
from pre-launch; recent sampled progress from2000 to6000 is about4000 leaves
in92s, with polling granularity. This is a throughput observation, not a
completion prediction or proof result. No error or completion receipt exists.

## Completed disposition of this original execution

Root subsequently approved the separately controlled bit-identical cache
entry (see independent-checks-a5-n8-staged-cache.md). After actual different-
executor endpoint controls and full source review, only own old PID59884 was
terminated. This original stage ACTUALLY returned exit1 with an explicit
interruption failure, accepted=false and count_certified=false, after
1227.026785059seconds. Last complete stdout checkpoint was35,000 leaves/
79,674 records, not the full153,520-leaf partition. No interior-only completion
receipt was produced and no old verifier state was reused in the fresh run.

Preserved failed output outputs/a5_checker_n8_staged_full.json,1355bytes,
SHA256 `162c29003dd4f2294cba156804cd54dfcf46274ac795eb6b2d5d8209b90d74b8`.
All original source before/after hashes match. The successful old local37
control output remains retained and unchanged. This original attempt is
closed as interrupted/nonaccepting; its replacement is documented separately,
with honest new runtime evaluator identity. Active replacement logs and future
cached_interior/full outputs are not part of this completed checkpoint.

## Final replacement outcome, administrative addendum

The separately documented bit-identical cached replacement ended ACTUAL
exit1 at the original15:19UTC alarm. It had not completed Stage1: the last
progress milestone was152,000/153,520 leaves and538,131 ordinary records,
and NO atomic complete-interior receipt exists. Its failed2052-byte result
`outputs/a5_checker_n8_cached_full.json` has SHA256
`55b2a328238f18e550783a0e827d85b3daf9b6efc8fd6b034f047c287bfeea9d`,
accepted=false/count_certified=false, with the actual cached runtime entry
declared and every source identity unchanged. Full details/log identities
are in independent-checks-a5-n8-staged-cache.md. No complete count or global
verification followed; no extension or restart was performed. The separately
proved lower bound does not supply missing regional completeness. Theory65
therefore remains OPEN alongside61/62; required Claude audit is pending.
