# Native exact producer attempt

- Rules/input head: `8a1f394739293953e1566fd24a0a193cc78ff26f`.
- Base/main supplied by orchestrator: `440d1079e42c3ef21c40d1cf8870f5b206410c6a`.
- Role: bounded technical developer; tool-configured model `gpt-6.1-sol`, medium, fresh fork (`fork_turns=none`). No Git mutations; ownership limited to this
  attempt and `code/native_producer/`.
- Status: MEASURED implementation/verification record; no new theorem or novelty
  claim. Gate exemption: port of the existing PD-T210 algorithm with unchanged
  mathematical criterion, source schema, and operation order.
- Dependencies read: root rules/workflow/Codex role, handoff02, BRIEF, and frozen
  `finite_general.py`, `finite_bernstein.py`, producer/checker/controls modules.

## Scope and implementation

C/GMP performs the corrected PD-T101 cardinal monomial construction, both
rational tensor Bernstein transforms, all de Casteljau subdivision, sums of
absolute interval endpoints, and corner/bound comparisons. Python supplies only
exact rational cosine seeds, small exact transform/monomial constants, and JSON.
This is a compiled heavy path rather than a Python arithmetic wrapper.

GCC14.2.0, GMP6.3.0, Python3.12.14 were available locally; no installs/network or
proxy changes. Native single thread, scale2^192, inherited n<=100.
Build/commands and limits are in `code/native_producer/README.md`.

The initial allocation-per-child version was replaced by in-place left halves
and one reusable right coefficient table per active depth. Each line is fully
copied before writing; only storage lifetime changes, not arithmetic order.
The first driver hashed sources after execution; concurrent editing could give
misleading provenance. Final driver instead compiles a frozen source copy and
records its early hash. Earlier artifacts are retained as interim evidence and
must not supply final provenance; final regenerated certificates live in
`/workspace/padua-work/producer/final/` and their entire mathematical payload is
compared against the earlier replayed output.

## Executed controls and evidence

`validate.py --work /workspace/padua-work/producer/optimized-validation` passed
n=2 and9: every initial coefficient interval equals the reference constructor
(54 and5500 intervals respectively), every metadata field agrees, unchanged
Python checker accepts, all14 deliberate corruption cases reject, and a valid
partial certificate remains unaccepted. Receipt is `validation.json` in that
work directory. This is developer validation, not independent audit.

Reference Python replay of produced n=9..24 is in progress; individual receipts
are `/workspace/padua-work/producer/nN-reference-check.json`. Final-source reruns
and exact mathematical-payload equality receipts are in
`/workspace/padua-work/producer/final/producer-timings.jsonl`. No pure-Python
producer is run here above32. Larger native runs remain bounded by this round's
budget and independent replay is required before any finite theorem upgrade.

## Runs needed

Finish the overlap range, contiguous extension through32, and bounded capacity
pilots if time permits; summarize actual CPU/wall timings and hashes. All large
or regenerable artifacts remain under `/workspace/padua-work/producer/` outside
Git; orchestrator owns cold-storage manifest/publication and independent status.
