# D0/D1 replay — verification record

Rules read at `ccd9e905d19c0c625c196c4a3f3e707058ed042a`;
base `76ba4214b100c86a44941f5e9a662ce9ce48efb8`.
Developer: Codex bounded replay worker, assigned gpt-6.1-sol medium;
runtime model metadata is not exposed. The replay adds no mechanism or novelty
claim; the novelty-gate exemption applies. These are development checks, not
the independent audit. **D0 PASS; D1 PASS.**

Run from the repository root:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-3d-20261106/code/replay.py
```

Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0, SymPy 1.14.0.
The compact [receipt](evidence/replay.json) records actual results, source
hashes, pinned inputs, axes, primes and seeds. Code and receipt are each under
16 KiB. Large historical inputs and disposable reconstruction outputs live in
`/tmp/padua-3d-20261106/`; they were not restored into the old topic or track.
The code retrieves original `ranks.json` and `lebesgue.json` with read-only
`git show` from full commit
`b6e7f1b439f8582231213ce557596872f579156e`. Their original SHA256s are
`560471d0053fef785bcee9c64f1b7fe9a384e24c0c74ef3d4cd58b9d6c703130`
and `ee98828d9fe4b790c02059a60e00bacddcd9bceb835d90706c03cfb03bedb3a0`.

## Exact replay

PD-T082's six-row correction table agrees with integer residue convolution for
every n=0..60, and direct point enumeration for every n=0..17. The frozen
catalogue generator and its complete direct-count/symmetry self-check also ran:
451 patterns, 5,061 canonical trials, and exact agreement with the preserved
count-result summary. In particular the 3D cardinality-admissible counts for
n=1..6 are 119,68,78,45,56,46. These checks do not replace the inherited all-n
convolution proof.

PD-T093's exact normalized 10×10 determinant, in the stated row and monomial
column orders, agrees symbolically after expansion with

`-x^3(x-1)y^2 w(w-1)(y-w-1)s^3(t-1)(s-t-1)`

for axes X=(0,1,x), Y=(0,1,y,w), Z=(0,1,r,s,t). The unused z-coordinate r
cancels. This matches the theory's determinant including its minus sign.
Six historical modular draws each reproduce the recorded determinant and full
rank 10 for C3-8ea9e9f33e3d. Six draws reproduce rank 3 of 4 and zero
determinant for the known PD-N035 representative C3-81c2fc8bc42e. Every input
axis is in the receipt. These are draws of **generic distinct axis labels**;
they are not Chebyshev–Lobatto rank certificates. Nonzero specialization mod p
proves the generic determinant polynomial is nonzero over Q. Deficient draws
alone do not prove an identically zero determinant. PD-T093's Chebyshev
unisolvence instead follows from its inherited monotone-real-axis theorem.

## Original 3D evaluator and baselines

The frozen `c3_lebesgue.py` evaluator and its unchanged product-Chebyshev basis
were imported. Both rows use the original 21³ tensor Chebyshev–Lobatto mesh,
condition threshold 10^12, discrete-Leja ordering and pivoted QR selection from
the (2n+1)³ Lobatto candidate mesh. QR nodes were regenerated, not substituted
from recorded output. Every value below matches the complete original binary
floating value exactly on this environment, in addition to all recorded digits.

| n | best fibre ID | fibre | Leja lower set | QR approximate Fekete |
|---|---|---:|---:|---:|
| 3 | C3-d0ed9c729db2 | 88.99386899143866 | 13.174719819948162 | 8.32067061468994 |
| 4 | C3-c1d4f3e30a4a | 1497.7664105347994 | 19.498175044580467 | 11.24487768964798 |

This replays two selected historical best rows and their baselines, rather than
repeating the entire screen that identified those minima. BRIEF's 88.99,
1497.8, 13.2,19.5 and 8.32,11.2 are rounded summaries of these original values;
they are not conflicting targets or tolerances. These are MEASURED sampled
values, not certified global Lebesgue constants.

## Restriction to two dimensions

The replay's dimension-independent product-Chebyshev evaluator is restricted
to d=2. The even checkerboard is j+k even on axis indices 0..n and 0..n+1.
Exact modular monomial Vandermonde ranks equal N=(n+1)(n+2)/2 for n=1..10:
3,6,10,15,21,28,36,45,55,66. Because monomials and product-Chebyshev modes
are related by an invertible triangular basis change, this tests the same
interpolation space.

For each n, choose a prime p=1 mod L, L=2n(n+1), and a primitive Lth root zeta
in F_p. The rational cyclotomic coordinates
(zeta^e+zeta^(-e))/2 are the reductions of the real Padua cosine coordinates
under Z[1/2,zeta_L]→F_p. A zero characteristic-zero determinant would reduce
to zero under this homomorphism; the recorded nonzero determinants therefore
prove unisolvence at the actual algebraic Padua coordinates. This differs
from generic-axis random sampling. Primes and roots are recorded, with no
float rank decisions.

At n=1..8 all four corners were evaluated by direct Vandermonde solves and
compared cardinal by cardinal with the PD-T101 corrected cosine kernel.
Its product-U identity was separately evaluated using finite cosine sums,
which preserve removable singular limits. Errors are below 2e-12 (actual
errors in the receipt). The nonnode corner (-1,-1) values are:

| n | corner value |
|---|---:|
| 1 | 2.000000000000000 |
| 2 | 3.000000000000001 |
| 3 | 3.776142374915398 |
| 4 | 4.409725435508212 |
| 5 | 4.947805749036596 |
| 6 | 5.417499430143907 |
| 7 | 5.835657710636256 |
| 8 | 6.213459646909055 |

Degree-one nuance: PD-T101 includes n=1, whereas several later corner
derivative/argmax records assume n≥2. The degree-one nodes are (1,1),(1,-1),
(-1,0), and the two nonnode corners each have value 2; the two node corners
have value 1. In the original 3D PD-N037 table, the degree-one fibre and QR
value are also 2, but its Leja lower-set baseline is 5. Those are different
node constructions; a constant-one or three-dimensional baseline must not be
used as the 2D corner sanity target.

## Execution history and limits

An initial standalone command also completed the original C0 generator with
its self-check, writing only `/tmp/padua-3d-20261106/c0/`:

```sh
python tracks/lattice-unisolvence/code/c0_catalogue.py --output-dir /tmp/padua-3d-20261106/c0
```

The first combined replay completed every mathematical assertion but failed
its final <16 KiB receipt-size check because JSON was pretty-printed. Compact
serialization fixed that output-only failure and the full command reran
successfully. A subsequent final run added the explicit product-U comparison
and full historical commit pin. No mathematical mismatch occurred. No
mechanism search, fit, all-n extension, or new scientific claim is part of
this replay. Temporary inputs are reproducible from pinned Git objects;
their archival delivery is not claimed.
