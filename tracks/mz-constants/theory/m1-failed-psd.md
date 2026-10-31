# PD-N?mz-constants-codex-11 — the nonnegative Hankel defect is indefinite

ID kind: PD-N. Aliases: entrywise positivity is not PSD; active anti-triangle obstruction.
Split from: candidate IDEA?mz-constants-codex-11. Split into: none.

## Statement and definitions

For every integer \(N\ge5\), the defect matrix \(D=2(M-R)\) on Chebyshev indices \(0,\ldots,N-1\), as defined in PD-T?mz-constants-codex-11, is indefinite. In particular, the mechanism “entrywise nonnegative defect implies \(Q_N(p^2)\le\int p^2\) for every \(p\in\Pi_{N-1}\)” is refuted in this range.

## Status and negative-result scope

Overall status: **PROVED** in development, pinned independent audit pending.
Attempted mechanism: IDEA?mz-constants-codex-11, inferring positive semidefiniteness from the signs of the active even anti-triangle.
Parameter range: all integers \(N\ge5\), exact Lebesgue CC rule, full degree-\(N-1\) coefficient space. Candidate disposition: **REJECTED: refuted**. This does not refute the upper threshold two or every possible use of the defect.

## Proof

Put \(i=\lfloor N/2\rfloor\), \(j=i+2\le N-1\). Then \(2i\le N\), so \(D_{ii}=0\), while \(i+j>N\) is even, so \(D_{ij}>0\). The principal two-by-two determinant is therefore \(-D_{ij}^2<0\). This block has eigenvalues of both signs, so the full symmetric matrix is indefinite. There is also a positive diagonal entry \(D_{N-1,N-1}>0\). A vector with negative defect quadratic form gives \(Q_N(p^2)>\int p^2\), disproving the candidate conclusion. For completeness, \(D=0\) at \(N=2\), and at \(N=3,4\) only the last diagonal entry is active, so those matrices are positive semidefinite of rank one.

## Dependencies, checks, sources and open items

Depends on the exact defect/support signs of PD-T?mz-constants-codex-11. The finite rational checker confirms the determinant formula in the executed range; see `topics/mz-constants/directions/M1/RUNS.md`. An independent adversarial developer separately derived this exact all-N minor before the draft. Pinned audit remains pending. The supplied source suggests entrywise positivity as an opening; it is not attributed the false PSD assertion. No external theorem is used.

## History

2026-10-31, Codex gpt-6.1-sol xhigh, rules `d36722823441dc40c6e19d69a174459348dd309c`: cheapest kill test retained, with its precise failed mechanism. The surviving sign-comparison route is separate, IDEA?mz-constants-codex-13.
