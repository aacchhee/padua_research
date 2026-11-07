# D15 source reviewer synthetic-only preregistration

2026-11-06; rules/input head dca0be979944bb0ad5eec818078906b59c796c2a.
Independent reviewer requested through API as gpt-6-astra medium; serving
metadata is unexposed. Root owns all mutable Git and source-author files.

Exactly one independent replay of the existing frozen controls.py --run-once
is authorized, under its existing hard RLIMIT_CPU=1. The author's slot is
already consumed. This consumes the remaining reviewer slot, even on failure.
No retry, native compilation/loading, actual phase evaluation, producer or
scientific checker instance is permitted. The checker import is pure exact
synthetic predicates only, as inspected before this execution.

Before execution copy the five D15 Python sources, SOURCES.json, FREEZE.json,
and the eight immutable code dependencies into an exclusive isolated directory
under /tmp/padua-d15-source-review-20261106. Preserve repository-relative paths.
Verify every copied code/data hash. Do not copy old outputs. Run the unmodified
controls once with python3 -B, in that isolated root. Retain its preregistration
and summary at the isolated local-output path; never overwrite the author's
output directory. Use /usr/bin/time to retain whole-process CPU and exit status.

Frozen candidate:

- FREEZE: 4e12e141f774ac2bea65f2581c7d2a5a4b35b795ef45f635c31fecc35e31a45e
- SOURCES: c9b232cceab301eae8c500fb9c3984702c21bef89f144b89d087f01a5cf1ab4f
- SPEC: e57664ab4f92290f21c09bece0ccb8845d2e5a98d9d403cdd2a5cfbbf216d325

Expected checks are the frozen five synthetic groups: source syntax without
stage imports; rational/degree/tree rejection; quarter-grid absorption;
closed-edge canonicalization and strict pi-fourth corner criterion; closed
union/tangency/oracle/cache/alias failures. They establish no real enclosure,
throughput, mathematical theorem, successful cover, or native supervisor test.

This review adds no mechanism or novelty claim. The full IDEAS read is omitted
under the parent's explicit technical-adapter scope waiver; the mathematical
generic D15 contract is reviewed by a distinct mathematical reviewer.

## Prelaunch infrastructure correction

The registered /usr/bin/time wrapper was absent; Bash returned127 before
launching Python. No control import, target execution or exclusive output
creation occurred. Preserve that failure; use Bash's built-in `time` for the
same single unmodified controls invocation instead. This correction precedes
the actual controls run and changes no code, input, cap or test strategy.
