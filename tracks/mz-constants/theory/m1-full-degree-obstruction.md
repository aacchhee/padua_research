# PD-T016 — full-degree CC exceeds the threshold

Review update, 2026-10-31: final ID allocation and scoped independent Astra review are complete; see topics/mz-constants/independent-astra-01.md and ID_CROSSWALK.md. The original development-stage pending-review wording below is historical. Required Claude audit and unresolved literature/novelty coverage remain PENDING. This administrative update changes no mathematical claim or proof.

ID kind: PD-T. Aliases: Chebyshev top-degree obstruction; full Lobatto upper MZ obstruction.
Split from: none; this is a substantive source-reported assertion independently reconstructed.
Split into: none.

## Statement, definitions and assumptions

For every integer \(N\ge2\), the Lebesgue CC rule on \(N+1\) Lobatto nodes satisfies
\[
\frac{Q_N(T_N^2)}{\int_{-1}^1T_N(x)^2\,dx}
=\frac{2(4N^2-1)}{4N^2-2}>2.
\]
Thus its maximum Gram eigenvalue on \(\Pi_N\) is strictly greater than two. The M1 upper bound on \(\Pi_{N-1}\) cannot be extended to full degree \(N\).

## Status and dependencies

Overall status: **PROVED** in development, pinned independent review pending. Depends only on CC exactness for constants and the elementary moment formula, locally proved in PD-T013. This is a positive theorem about an obstruction, rather than a record of a new failed mechanism; it retains a PD-T ID.

## Proof

At every node \(x_j=\cos(j\pi/N)\), \(T_N(x_j)=(-1)^j\), so \(Q_N(T_N^2)=Q_N(1)=2\). The product formula gives \(T_N^2=(1+T_{2N})/2\), hence
\(\int T_N^2=1-1/(4N^2-1)\). Division proves the formula and strict inequality.

## Checks and sources

Exact finite rational checks are in `tracks/mz-constants/code/m1_exact_check.py`, with actual commands/hashes in `topics/mz-constants/directions/M1/RUNS.md`. The all-N proof is the calculation above. The source-supplied `notes/bttb_repo_numeric_mapping.md`, O4, reported this formula; its assertion was independently reconstructed rather than inherited. This result is not claimed novel.

## Scope and open items

It gives a lower bound for the full-degree maximum eigenvalue, not its exact value, and says nothing adverse about the degree-\(N-1\) theorem. Independent pinned review remains pending.

## History

2026-10-31, Codex gpt-6.1-sol xhigh, rules `d36722823441dc40c6e19d69a174459348dd309c`: split substantive reconstruction in M1 scope.
