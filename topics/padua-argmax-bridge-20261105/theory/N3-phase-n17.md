# N3 n17 phase verification — complete producer, replay enclosure gap

Verification record; no new global result ID. The inherited n17 global argmax
is already proved in the accepted finite range. This attempt does not extend
that range or reclassify the inherited theorem.

## Exact attempted instance and status

Instantiate PD-T364 at n=17 using a four-quadrant phase cover, first-order
whole-sum enclosures, every physically admissible odd noncorner center and
only the inherited PD-T251/369 local radius. The intended new phase-route
verification remains **OPEN**: the producer completed its own cover, but the
independent arithmetic path did not validate every leaf on that partition.

The finite numerical outcomes below are **MEASURED execution records** of
outward producer/checker software. No new computer-proof promotion is made.

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

## Actual independent replay

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

## Next step and limits

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
