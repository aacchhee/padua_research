# C4 floating-point baseline — response to F3

Date: 2026-11-05. Developer: Codex, gpt-6.1-sol medium as dispatched;
backend runtime model/effort metadata not exposed. Rules and input head:
`9ec2a54c5b6af56514feaf11c9fc329f19a88820`.
Scope: implement and execute the known C4 marginal-data comparator only.
No new novelty content, so no new candidate or novelty gate was opened.
Status: **MEASURED**, provisional `PD-T?nn-mop-iep-codex-05`;
see [durable statement](theory/c4-baseline-measurements.md).

## Source and numerical convention

Primary [arXiv:2608.25758v1](https://arxiv.org/pdf/2608.25758v1),
§5.1, printed p. 20, Examples 5.1–5.2, rechecked using web PDF text
extraction in this round after consulting literature/INDEX.md. These are
source-family inputs, not reproductions of the paper's algorithms or metrics.
Both measures have N nodes k=0,...,M=N−1; each N reconstructs its weights.
Krawtchouk: w_j(k)=binom(M,k) p_j^k(1−p_j)^(M−k), p1=2/5,p2=1/2.
Hahn: w_j(k)=(β_j+1)_k/k! · (γ+1)_(M−k)/(M−k)!,
β1=1, β2=3/2, γ=1. Weights are exact rationals before conversion.

The local experiment changes coordinates to z=2k/M−1. In both binary64
and reference runs the recurrence is monic in z and its domain is
n+m≤N−1. Thus a_z=(2/M)^2 a_k and b_z=(2/M)b_k−1.
It uses node-valued monic Stieltjes marginal recurrences, without
reorthogonalisation, followed by A/B layer reconstruction from audit-01.
The executable implements this reconstruction itself; the auditor's code
is imported only for the small exact check described below.

For field t∈{a1,a2,b1,b2}, E_t=max_ν|computed_t−reference_t| /
max_ν|reference_t|; E=max_t E_t. Structural zeros remain in the numerator.
This fieldwise normwise metric avoids division by individually zero or
small coefficients. It is not maximum componentwise relative error.
Correct digits = −log10(E); lost digits = log10(E/ε),
ε=2.220446049250313e−16 (binary64 epsilon, twice unit roundoff).
Negative correct digits mean relative error exceeds one; lost digits can
therefore exceed the nominal 15.65-digit budget.

## Completed runs and receipts

From repository root; both final commands returned exit 0:

```sh
python3 topics/nn-mop-iep-20261103/code/c4_float_baseline.py --family krawtchouk --sizes 4 8 12 16 24 32 --dps 140 220 > /tmp/nn-mop-c4-krawtchouk-final.json
python3 topics/nn-mop-iep-20261103/code/c4_float_baseline.py --family hahn --sizes 4 8 12 16 24 32 --dps 140 220 > /tmp/nn-mop-c4-hahn-final.json
```

Python 3.12.14; mpmath 1.3.0;
Linux-6.18.57-x86_64-with-glibc2.41. No random seed: deterministic rational
inputs. Source head is above; executable SHA-256:
`9ce76ae88fb798f73127f75819bcdfb6c7bffb0d9cd092d70957164cb9b6a2e8`.
Exact checker SHA-256:
`13d59af82304a712d792c6e2f96c76f42ec732575dcfa3452a92295071c011b3`.

| Local output (regenerable, not committed) | Bytes | SHA-256 | Seconds |
|---|---:|---|---:|
| `/tmp/nn-mop-c4-krawtchouk-final.json` | 7063 | `dc49b5f602f8d4f0df6e1cb74e2d892971750f6f82677b073eda0941f3dfd124` | 0.317890 |
| `/tmp/nn-mop-c4-hahn-final.json` | 7094 | `d6eb1e0c66b4bbe268d3719dc0ab4eb195a5d4a725215cde3dc3d448977ba876` | 0.328013 |

Raw hashes include elapsed time, argv, platform and version fields, so new
executions need not reproduce these hashes. Compare cases and code/input
identities for cross-environment replay; no cold-storage transfer was performed. The committed code and short receipt
provide regeneration; no bulk output is required for the bounded statement.

| Family | N | E | Correct digits | Lost digits | 140/220 dps agreement |
|---|---:|---:|---:|---:|---:|
| krawtchouk | 4 | 1.00901e-13 | 12.996 | 2.657 | 8.06e-139 |
| krawtchouk | 8 | 1.87057e-09 | 8.728 | 6.926 | 1.64e-134 |
| krawtchouk | 12 | 1.61249e-06 | 5.793 | 9.861 | 2.66e-130 |
| krawtchouk | 16 | 0.0966694 | 1.015 | 14.639 | 1.39e-126 |
| krawtchouk | 24 | 72940.6 | -4.863 | 20.517 | 2.21e-118 |
| krawtchouk | 32 | 5022.38 | -3.701 | 19.354 | 6.79e-110 |
| hahn | 4 | 1.34123e-12 | 11.872 | 3.781 | 3.07e-138 |
| hahn | 8 | 2.6143e-07 | 6.583 | 9.071 | 2.99e-132 |
| hahn | 12 | 0.00245984 | 2.609 | 13.044 | 8.71e-128 |
| hahn | 16 | 70.3138 | -1.847 | 17.501 | 6.35e-122 |
| hahn | 24 | 310.52 | -2.492 | 18.146 | 1.01e-110 |
| hahn | 32 | 677582 | -5.831 | 21.485 | 1.41e-99 |

All twelve final reference checks meet E<1e−60. The reference uses the
same recurrence with higher precision; this checks precision convergence,
not independence of the algorithm. For N=4 in each family the separate
exact Fraction mixed-moment solver and polynomial-coefficient matching in
`audit-01/claude_layer_recursion_check.py` was actually executed. Reference
agreement E was 2.43e−218 (Krawtchouk) and 3.58e−217 (Hahn). This is an
independent formulation executed by the developer, not an independent
agent rerun or a general proof.

Every final run completed with finite coefficients and no zero divisor;
this does not mean numerical success. E exceeds one at N24/32 for
Krawtchouk and N16/24/32 for Hahn. The code records failures for zero or
nonfinite divisors, nonpositive marginal norms, nonfinite coefficients,
reference convergence failure or exact-check failure. `relative_error_below_one`
separately records loss of all normwise relative accuracy.

## Divisor diagnostics and interpretation

Divisors are d_ν=b_(ν,2)−b_(ν,1). Maximum divisor degree is N−2 in all
runs; no terminal d is divided by. Division counts for N=4,8,12,16,24,32
are 12,70,176,330,782,1426, respectively. The reference maximum
subtraction ratio (|b1|+|b2|)/|d| is:

| N | Krawtchouk | Hahn |
|---:|---:|---:|
| 4 | 3 | 1.91259 |
| 8 | 11 | 29.2554 |
| 12 | 19 | 94.5056 |
| 16 | 27 | 195.774 |
| 24 | 43 | 506.305 |
| 32 | 59 | 960.825 |

These ratios describe subtraction cancellation at the divisors; they
are not a condition number of reconstruction. Binary64 corrupted
coefficients can produce much larger apparent ratios. Terminal max |d|
is recorded separately in the raw receipts and reaches 33.86 (Krawtchouk
N32) and 71.15 (Hahn N24); it is not monotone. Exact terminal equality is a boundary diagnostic,
not a division requirement. The pilot exhibits large errors in this
implementation on these finite inputs. It does not isolate input
conditioning, marginal Stieltjes error and propagation amplification.
It neither compares against C3 nor establishes a general stability result.

## Input identities

SHA-256 of canonical sorted-key JSON containing exact rational nodes and
weights, as implemented in the executable:

| Family | N | Input SHA-256 |
|---|---:|---|
| krawtchouk | 4 | `450b5178fccdbf1e78ba516c1ea408258ac4ff2a1b0cbbb9a14741bbabb30efc` |
| krawtchouk | 8 | `cd7128a4d07fbdc93819e61ceaeb4770e02a2e6ae63623923ba503e77957c269` |
| krawtchouk | 12 | `ba799d8139680252190720760b30bb809f743e558cf7c88103b98e7a81a9bd50` |
| krawtchouk | 16 | `7091248c4b65632244b67780815946bc956b1b806fcfa7bbcb377f32b19e62f9` |
| krawtchouk | 24 | `ed9b8c12224f90af886b5409c1a169b2c0f18166d3cebf384f3760fdee3b6d3f` |
| krawtchouk | 32 | `19bdb16863d29132b58106816bb6d719436dc621e7301a33ad34753873c47ac9` |
| hahn | 4 | `e5558865cb6eef2913ee27622d251d05a614db7fc509418d9c11779863c55f12` |
| hahn | 8 | `452dde0851f7bdd766176b8f554d60d40c7c63f676e43f796b4c1de8719c4af1` |
| hahn | 12 | `f95fb44fb4adeb29a25653f244d56c43ce0299650c037d08d10fee0d81b50336` |
| hahn | 16 | `2d4e8883120041c0221408d62f103ff307fbbaf9946e2387df429dd9fd936482` |
| hahn | 24 | `0fe9100b2fad839f38ed92e6b01ffb5f40d03028c12875187e35fdbede22afca` |
| hahn | 32 | `bacc69beb9e0ba2a5927752123b21020a1118d1d830d241cf9457cced6ab0a86` |

## Development history and Runs needed

A first Krawtchouk-only run preceded verified Hahn implementation.
The first Hahn implementation exposed an empty-product integer division
that produced a float; this was corrected to an exact Fraction product
before the final code and runs. An intermediate 100/160 dps pilot gave
Hahn N32 agreement 3.38e−59 and was correctly marked reference failure
under the 1e−60 threshold; both families were then rerun at 140/220 dps.
No inference uses that failed reference. The reported final hashes and
results all use the final executable.

Supplementary independent replay completed: see
[response-independent-01.md](response-independent-01.md). Its separate full
runs reproduced all twelve case objects exactly. Required Claude re-audit
remains pending (repeat the two commands above, compare source/input hashes
and case values). No larger run is needed to
support the bounded statement. Larger N, independent explicit-family
coefficient formulas and C3 comparisons are outside this pilot; no such
execution is claimed. Audit F3's planned comparator has now been executed
within this finite scope; broader numerical comparison remains open.

## Accepted audit-02 evidence addendum (X1)

Claude audit-02 R4 separately compared the 220-digit references against exact
Fraction moment ground truth at N=8,12,16,24 in both families, with distance
<=1.7e-190; the binary64 errors agree with this receipt. Combined with the
developer's N4 exact checks, independent-formulation exact-reference evidence
therefore covers the sampled N=4,8,12,16,24. N32 still relies on precision
convergence. This is auditor-executed MEASURED evidence, not a new execution
by the preparation agent or a gap-free all-size certification. See
[audit-02 R4/X1](audit-02.md) and its unchanged checker.
