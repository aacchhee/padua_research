# N3 n17 phase verification — independently checked complete cover

Verification record; no new global result ID. The inherited n17 global argmax
is already proved in the accepted finite range. This attempt does not extend
that range or reclassify the inherited theorem.

## Exact attempted instance and status

Instantiate PD-T364 at n=17 using a four-quadrant phase cover, first-order
whole-sum enclosures, every physically admissible odd noncorner center and
only the inherited PD-T251/369 local radius. The new phase-route
verification is **COMPLETE**, using the separately reviewed round5 kernel:
all1288 original leaves passed its actual independent replay. The existing
PD-T364 finite implication therefore supplies an alternative computer-assisted
verification of the already proved n17 instance. This adds no global degree.

Timings and diagnostic measurements below remain **MEASURED execution
records**. The round3 failure is historical; round5 supplies the completed
verification obligation. No new global result ID or degree is promoted.

## Completed producer

`n3_outward_full.py` completed 2572 visits and 1288 leaves, with zero pending
prefixes, in 222.37 search CPU seconds under its 600-second initial cap.
Leaves comprise 32 outside, 524 far, 704 corner-orbit plus defect and 28
inherited-local plus defect. Producer accepted=false is retained.

The actual build snapshots contain the compiled C source, interval header,
MPFR header and driver. Its manifest records 42 compiler-discovered source/
header dependencies, the compiler and linked runtime hashes. Source/binary
identities were checked before/after search; a collector additionally verified
53 closure identities after execution. The 9946-byte manifest is preserved
as `../evidence/n3-full-n17-build.json`.

The original 192042-byte candidate had a gzip exceeding 16 KiB. After measuring
that size, a deterministic nonnumerical projection removed only the diagnostic
numeric leaf fields ignored by the independent checker. All root/path/kind,
degree, constants, geometry and provenance metadata are retained. Exact compact
plain SHA-256 is
`64f7befd86658c8d9f29b05c1cb5a0162e611b726b161e737610547bed218c4b`;
its deterministic gzip is 5266 bytes. The projection code, original identity
and decompressed identity are recorded; no file splitting was used.

## Historical round3 independent replay (failed)

The distinct phase checker read exactly the compact candidate bytes, used
its corrected immutable-input/fresh-build path, and actually checked all
1288 leaves in 60.60 CPU seconds. It reported accepted=false with 364
independent enclosure failures: 184 far and 180 corner-orbit/defect leaves.
The remaining 924 predicates passed, including every inherited-local and
outside leaf. The structural complete-prefix checks passed.

For example, root0/path01010 is a producer far leaf, but the independent
finite-cosine enclosure gives S_upper about 12.869, above its Lc lower bound
about 8.618. This is failure of that backend's sufficient enclosure on the
given box, not a witnessed function value, counterexample, contradiction,
or proof that the producer bound is unsound. The independent checker does
not trust producer numeric diagnostics or infer acceptance from completeness.

The exact replay report and source/runtime closure are owned by the checker;
the compact input requires a new exact-byte whole replay after any refinement.
No replay of a different candidate may be transferred to this one.

## Round3 next-step record and limits (historical)

Retain the complete producer candidate and failed replay. The cheapest
prospective test is geometric refinement of failed leaf paths, followed by
actual whole replay of a newly frozen input. A stronger separately implemented
kernel is another option. Neither has run in this round. The first-order
family, the global argmax target and B2's measured float results are not
refuted. No second-order growth kill follows from this single-degree test.

History: 2026-11-05 Codex requested Sol medium, serving metadata not exposed;
rules/input c000899f3fb10d6ba0f1725341a045fe11ec943a. Independent execution is
attributed to /root/phase_checker, not to this developer. Mathematical/source
review and required Claude audit remain separate.

## Round5 disposition — 2026-11-06

The exact same candidate (plain hash64f7befd..., committed5266-byte gzip)
was checked once with the independently reviewed Arb hybrid v2, explicit
`--kernel round5`. All1288/1288 leaves passed:32 outside,524 far,704
corner-orbit-plus-defect and28 inherited-local-plus-defect; no failed or
pending region, accepted=true, complete=true, process exit0. No tree
refinement, max-leaf cap or numeric producer bound was used for acceptance.

Actual checker CPU109.449514 seconds, below the preregistered120-second
cap; compiler/build-helper child CPU1.287483 reported separately, wall
131.282938seconds. This is one known-degree overlap calibration, not an
outward throughput/box-growth law for33/64/128.

[Full short receipt](../evidence/phase-checker-full-n17-round5.json) SHA256
49060e7633068f6ffb531e63614855a5d88c466c10e6d4d1b07a8c21043e6423
records actual commands, input snapshot, fresh source/binary/build-closure
identities, worker code/CPU caps, raw identity and complete outcome counts.
The465506-byte raw receipt remains local; its unique diagnostics are not a
proof input. Kernel source SHA256
17fea91d4fa02e4183823e5d70b44705e96da7acfd26b04a0f3ed1cac443d9a2
and the required checker, fresh-build code, essential input and receipt
are committed. Trusted dependencies include Arb/FLINT outward arithmetic,
its elementary functions, GMP, Python parsing and compiler/runtime closure.
The math reduction is the existing reviewed phase-checker-reduction.md.

[Focused source review](../independent-checks-phase-round5.md) accepts this
exact v2 and closes R4-1. The old failed hybrid and NaN finding, baseline
364-failure replay, source snapshots and receipts remain unchanged. The
bare/default checker still selects the original baseline; experimental
round5 selection is explicit and its manifest records the selected source.

Original round3 version of this record, SHA2564d9da85d659919d487c5592e38d97291b1dd24b134e1bd6e02b98a51f9fdfd65,
is preserved at bcba739. The freeze receipt describes those historical
bytes. This dated update changes verification disposition after an actual
new-source replay; it does not relax a predicate or overwrite the failure.

Next: separately gated higher-degree overlap calibration and practical cost,
using the accepted local patch where authorized. Global accepted range is
2–38 via the independent native certificates; full all-degree theorem and
analytic onset remain OPEN. Required Claude audit is still separate.
