# I25 independent phase verification — completed outcome

The independent checker accepted **942 complete trees for 471 integer degrees
41..511**, including both witnesses at every degree: 560 old and 382 new
certificates. All four workers exited 0. Inclusive CPU was 2519.420775278 s,
wall time 646.839168173 s, and maximum individual child RSS 154176 KiB.
Every worker passed 31 exact arithmetic controls. The reviewed pilot also
rejected all 27 corruptions. A distinct reviewer separately executed both
passes at 41,458,511: six certificates plus 31 controls, exit 0, inclusive
CPU 27.276321227 s. All result fields matched the full run except timings.
The accepted supplementary review is
[the completed I25 section](../../independent-checks-onset512-response.md).
The independent Claude audit and public Zenodo deposit remain separate.

The 246-line core recomputes direct finite kernel/reflection sums and proves
the complete trees using its own upper vertices, lower corner values and
global norms. Its trusted arithmetic is Python integer/Fraction operations,
guarded NumPy integer/array operations, and IEEE binary64 round-to-nearest
with gradual underflow and correct `nextafter`; pi and sine bounds have
explicit rational/Taylor proofs. The analytic floor, corner, far and physical
cover lemmas remain premises. This establishes one finite conclusion per
degree. It does not prove every native endpoint: new uppers independently
prove 42174/43116 stored S uppers by `new upper <= old upper`; the other
942 are not assumed. Every tree passes using the new bounds.

Exact rational comparisons give all numerical near margins >289/50000,
far margins >33/200, and numerical corner gaps >159/5. Details and identity
pins are in [RESULTS.json](RESULTS.json) and
[J03](../../theory/J03-independent-phase-checker.md).

The compact evidence ZIP is outside Git:

- Path: `local-output/argmax-bridge-20261105/i25-evidence-20261108T112304Z.zip`
- Bytes: **2843611**; 1025 members, including all 942 proof JSON inputs.
- SHA256: `d1d03156dde4248fecaa25d0144cd73c7c5414f28b66a39099342b31f2f7e0f8`
- Export command, from repository root:
  `bash topics/padua-argmax-bridge-20261105/code/independent_phase_checker/bundle.sh local-output/argmax-bridge-20261105/i25-evidence-20261108T112304Z.zip`
- Verification: ZIP CRC check and every member's byte size/SHA256 in its
  `MANIFEST.json` passed during export. The member manifest excludes itself.

The ZIP contains exact executed full/pilot source snapshots, prospective
preregistrations and amendments, all run logs, receipts, runtime identities,
input hashes, the failed v1 pilot, independent review scripts/controls and
six-run evidence. V1 source bytes were reversibly reconstructed and matched
their original preregistered hashes; v2 bytes come from commit `4846913`.
The four executed full Python sources remain unchanged. Proof inputs were
read as authenticated JSON data; no native archive code was run. Full native
histories and binaries are excluded. Existing run outputs remain unchanged.

Original `pending`, `gated` and `prospective` strings in preregistrations are
preserved history. The current I25 outcome is completed and accepted as
described above. The v1 pilot conservatively rejected seam aliases before
numerical evaluation; the reviewed v2 correction and successful execution
are retained alongside that failure, without retrospective rewriting.
