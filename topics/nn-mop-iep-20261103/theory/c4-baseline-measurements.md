# PD-T?nn-mop-iep-codex-05 — bounded C4 floating-point pilot

ID kind: PD-T.
Aliases: C4 marginal Stieltjes plus A/B layer baseline; digits lost pilot.
Split from: none; numerical evidence requested by audit-01 F3.
Split into: none.

## Statement

For each N in {4,8,12,16,24,32}, on the Krawtchouk and Hahn rational
weights specified below, the executable `code/c4_float_baseline.py`
produced finite binary64 NN coefficient arrays on n+m≤N−1 without zero
division. Against its 220-decimal-digit reference, whose agreement with a
140-digit calculation was better than 1e−60 in the metric below, maximum
fieldwise relative errors ranged from 1.01e−13 to 7.29e4 (Krawtchouk) and
1.34e−12 to 6.78e5 (Hahn). These are observations for this implementation
and the twelve inputs, not a general instability theorem or a comparison
with C3. The reference shares the algorithm except at the two N4 exact
mixed-moment cross-checks.

## Definitions

N nodes k=0,...,M=N−1; coordinate z=2k/M−1. Coefficients are monic in z.
For field t in {a1,a2,b1,b2}, define
E_t=max_ν|computed_t−reference_t| / max_ν|reference_t| and E=max_t E_t.
Correct digits are −log10(E), lost digits log10(E/ε), ε=2^−52.
The numerical comparator computes two marginal monic Jacobi recurrences
by Stieltjes on node values, then the known A/B layer recursion, using
no reorthogonalisation. Input coordinates and weights are constructed
as exact Fractions before each arithmetic conversion.

## Assumptions

Krawtchouk weights binom(M,k) p_j^k(1−p_j)^(M−k), p1=2/5,p2=1/2.
Hahn weights (β_j+1)_k/k! · (γ+1)_(M−k)/(M−k)!,
β1=1,β2=3/2,γ=1. Each N rebuilds its weight vectors independently.
Numerical environment and exact input/code hashes are frozen in the
[receipt](../c4-baseline-01.md). No randomness or claim beyond these inputs.

## Status by part

Overall status: **MEASURED**.

| Part | Status | Evidence / gap |
|---|---|---|
| Twelve finite binary64/reference comparisons | MEASURED | Full commands, metrics, hashes and values in receipt |
| Two N4 exact mixed-moment cross-checks | MEASURED | Separate exact solver executed by developer; not a computer proof |

## Depends on

Known marginal-Jacobi to NN compatibility reconstruction, audit-01
relations (A)/(B). This measured record does not supply its general proof.
The independent-formulation small checker is the existing auditor script
`audit-01/claude_layer_recursion_check.py`, imported solely for N4.
Source family specification: LIT?nn-mop-iep-codex-12, strengthened here by
a fresh primary check of arXiv:2608.25758v1 §5.1 Examples 5.1–5.2 p.20.
No new novelty claim.

## Checks

The executable and [run receipt](../c4-baseline-01.md) carry exact commands,
source/rules head, code and input SHA-256 identities, Python/mpmath
versions, output SHA-256, local locations, sizes, reference precision
checks and the measured error table. All twelve final reference checks
passed the 1e−60 convergence threshold; all final runs returned exit 0.
Relative error exceeds one for Krawtchouk N24/32 and Hahn N16/24/32.
The code reports that condition separately from successful completion.

## Sources

LITERATURE input-family definitions only:
[Faghih–Van Barel–Vandebril, arXiv:2608.25758v1](https://arxiv.org/pdf/2608.25758v1),
printed p.20, Examples 5.1–5.2. Fresh web PDF text extraction verified
formulas, parameters and number-of-nodes convention. Paper algorithms,
scaling and error metrics differ from this local experiment.

## Proof or evidence

The finite measurements are tabulated in the receipt. Small exact
Fraction moment solves at N4 agree with the reference to E=2.43e−218
(Krawtchouk) and E=3.58e−217 (Hahn). Every final reconstruction divided
only at degrees ≤N−2. It did not divide by terminal d=0. Measured
subtraction cancellation ratios and terminal boundary residuals are
separate diagnostics, not proofs of a source of error.

## Scope

This is a bounded double-precision baseline. Precision convergence does
not establish independent reference correctness for all larger cases.
Large errors do not isolate conditioning from marginal Stieltjes errors
or layer propagation. No C3 implementation/comparison, broad stability
claim, new algorithm, or optimality/complexity conclusion is supplied.

## Open items

Supplementary independent replay of both full commands completed;
[response-independent-01.md](../response-independent-01.md) records its own
outputs and exact case-payload comparison. Required Claude re-audit remains
pending; this attribution-only receipt update changes no executable or result.
No cold-storage transfer of local regenerable JSON is claimed; the code and
receipt suffice to reproduce this bounded observation. Larger runs and detailed error-source analysis
are not required for this finite statement and have not been executed.

## History

2026-11-05: Codex technical developer, gpt-6.1-sol medium as dispatched;
backend runtime model/effort metadata not exposed. Rules/input head
`9ec2a54c5b6af56514feaf11c9fc329f19a88820`. Added executable and bounded
pilot for audit-01 F3; reference raised from 100/160 to 140/220 dps after
Hahn N32 missed the chosen convergence threshold in an intermediate run.
No Git operation or shared-file edit by this worker.
