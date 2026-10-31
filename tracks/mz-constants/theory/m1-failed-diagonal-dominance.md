# PD-N?mz-constants-codex-12 — unweighted diagonal dominance fails at N=5

ID kind: PD-N. Aliases: plain row diagonal-dominance failure.
Split from: candidate IDEA?mz-constants-codex-12. Split into: none.

## Statement, definitions and assumptions

Let \(N=5\), with \(M,R\) the degree-four continuous/discrete Chebyshev mass matrices of PD-T?mz-constants-codex-11. Then \(A=2M-R\) is not weakly diagonally dominant by rows: its row indexed by 2 has margin \(-2/35\).

## Status and negative-result scope

Overall status: **PROVED** in development, independent pinned audit pending.
Attempted mechanism: IDEA?mz-constants-codex-12, proving \(A\succ0\) for every \(N\ge2\) solely by unweighted row diagonal dominance of this matrix in the stated Chebyshev basis.
Parameter range: exact counterexample at \(N=5\); no universal claim of failure for every larger \(N\) is made. Candidate disposition: **REJECTED: failed**. The target theorem is not rejected.

## Proof

In row 2, the only nonzero entries are
\[
A_{20}=-\frac23,\qquad A_{22}=\frac{14}{15},\qquad A_{24}=-\frac{34}{105}.
\]
Thus \(A_{22}-|A_{20}|-|A_{24}|=-2/35<0\). This disproves the asserted universal row-diagonal-dominance property. It does not disprove a scaled criterion or positive definiteness itself.

## Dependencies, checks, sources and open items

Depends only on the exact cosine moment/alias formulas in PD-T?mz-constants-codex-11. The rational checker `tracks/mz-constants/code/m1_exact_check.py` separately calculates this margin; executed command/hashes are in `topics/mz-constants/directions/M1/RUNS.md`. No external source is used. Independent pinned audit remains pending.

## History

2026-10-31, Codex gpt-6.1-sol xhigh, rules `d36722823441dc40c6e19d69a174459348dd309c`: failure first observed numerically and then replaced by the exact counterexample above. The later weighted comparison applies to \(M\), rather than asserting this failed property for \(A\).
