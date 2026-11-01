# Independent checks — Padua MZ 2D

Required Claude Opus 5.5 xhigh audit: **PENDING**. Supplementary Codex checks do not replace it.

No separate-agent scientific rerun has completed at this initialization checkpoint. Exact computer-assisted claims cannot be promoted on the strength of the producer run alone. The exact reduction, committed checker, input identities and an actual different-agent rerun are required.

Mechanical allocation/input identities were independently inspected by the protocol worker: [receipt](protocol/README.md). This verifies pinned file identities and reservation provenance, not mathematical statements.

## Runs needed

Run the exact producer/checker independently after the initial exact evidence checkpoint, record commands and versions, compare mathematical output, and exercise certificate-rejection controls if a separate certificate interface is used. Reconstruct D1's alias and operator decomposition and challenge D2/D3 arguments. Record the precise candidate SHA or file hashes.

## Completed independent technical execution — 2026-11-01

This dated record supersedes the initialization statement above for the finite
exact run only. Worker: Codex `/root/protocol`, requested gpt-6.1-sol medium;
serving model/effort is not independently exposed. No theory status is changed
by this worker. Required Claude Opus 5.5 xhigh audit remains **PENDING**.

Frozen producer was committed at `e59f57c`; input head inspected and execution
started at `0b526915eed8fba9a5d5509d6ec62e763a9a7983`. Read the complete
producer, conventions and D6 exact reduction. The acceptance path forms rational
entries and exact integer congruences; floating eigenvectors only propose R.
Assertions were enabled (no Python `-O`). D6's algebraic reduction was inspected,
not independently mathematically audited by this mechanical worker.

Actually executed separately, exit 0:

```sh
PYTHONPATH=/tmp/padua-flint OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python tracks/mz-constants/code/mz2d_exact.py --m 10 20 30 40 --output topics/padua-mz-2d-20261101/evidence/independent-exact-spectra.json
PYTHONPATH=/tmp/padua-flint OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python tracks/mz-constants/code/mz2d_independent_check.py
```

Python 3.12.14, python-flint 0.9.0, SymPy 1.14.0, NumPy 2.3.5,
SciPy 1.17.0; Linux 6.18.57 x86_64/glibc2.41. Exact versions and commands
are retained in both receipts. The first additional-checker execution passed;
then root requested broader region/pencil checks, which were added and actually
executed again to produce the final receipt below. No producer source changed.

All four independent producer `results` objects equal the stored producer
objects after removing **only** nested `seconds` fields. This compares measured
extrema, exact endpoint counts, denominators, diagonal signs, positive dominance
margins, integer transform hashes, intervals and witness fields. The top-level
command differs by output path and is preserved rather than normalized away.
The four strict intervals therefore reproduce exactly as in D6.

Additional checks use a separately written moment/reflection implementation
and an explicit double sum over the **stored** 225 integer coefficient triples
at m=30. Both rational quadratic forms match the producer's stored fractions;
`b>0`, `b-4a>0`, the exact gap and exact Rayleigh quotient all match. No newly
selected eigenvector substitutes for the stored witness.

Independent cyclotomic-field interpolation at every m=1,...,5 constructs and
inverts the nodal Vandermonde and integrates the resulting cardinals to obtain
signed Lebesgue weights without using the alias formula. All 245 tested moments
(total degree <=2m+2) match the alias function. For all 371 endpoint Gram pairs
across these five m values, direct exact nodal products match Q; separate
symbolic integration of Chebyshev polynomials matches H. The six-region table
(L plus five inexact zones) agrees exactly with the all-degree formula for all
1,221 moments `a+b<=2m-2`, every m=2,...,12; each region is exercised.

All six negative controls reject: zero R, nonzero singular R, an exact singular
endpoint (t=1 at m=2), zero width, negative width, and a one-integer corruption
of the stored witness coefficient list with unchanged advertised forms. The
controls do not establish malformed-input rejection outside their stated scope.

Content identities:

| Artifact | SHA256 |
|---|---|
| Frozen exact producer | `5d1f005e2307d3a26badc9c1a44ce313dc9126625a49fba5d59430c151cf9c70` |
| Producer exact-spectra.json | `5456917afe8fea69b0a776270ef3ae79fdc33deb02d27f89648fc342f78b93de` |
| [Independent producer receipt](evidence/independent-exact-spectra.json) | `18c8623442664aa119d3581b701d200315d454071d6b8f6c89cbaf540fe34d9c` |
| [Additional checker](../../tracks/mz-constants/code/mz2d_independent_check.py) | `5e455d747dc5dca84c883ed900095ff4a2bb40767f4ebcb3261d7d583df7bdfc` |
| [Additional receipt](evidence/independent-additional-checks.json) | `2da16fa5c8f2f480ab7c12270b8c9b95ec49028f9df6b1cf4062af4f11897717` |

The receipt also records the definitions hash. Trusted exact arithmetic includes
Python integers/Fraction, SymPy's cyclotomic quotient and symbolic integration,
and python-flint integer matrices. These executions supplement mathematical
audit and do not extend the finite spectral certificates to all degrees, prove
a universal spectral floor, or establish historical novelty.
