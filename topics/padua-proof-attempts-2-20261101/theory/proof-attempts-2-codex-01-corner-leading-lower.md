# PD-T?proof-attempts-2-codex-01 — The corner leading lower bound

ID kind: PD-T.
Aliases: A2(i); matching corner leading coefficient; explicit corner lower bound.
Split from: OPEN_TARGETS A2 at programme SHA `9bd14a6d2c4da69139a10107d8a787f2be0c5c9e`, the matching corner lower-bound part of the leading asymptotic.
Split into: none; explicit two-sided estimate is -02 and b-term is -03.

## Statement

For every integer n≥2 and the specified even-checkerboard Padua points,

\[
 \Lambda_c(n)\ge\frac4{\pi^2}\log^2n-54
              \ge\frac4{\pi^2}\log^2n-80\log n.              \tag{1}
\]

In particular the corner has the matching leading lower coefficient4/π². The second displayed inequality uses54≤80log2.

## Definitions

Λ_c is the maximum over the four corners of the total-degree Padua Lebesgue function. L_n, d_r, and the positive same-mesh square are defined in `PD-T?proof-attempts-2-codex-04`.

## Assumptions

Exact real arithmetic; n≥2; the node/parity/kernel conventions of the stated dependencies. No global corner-argmax assertion.

## Status by part

Overall status: **PROVED** (written all-n proof; Claude audit pending).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| The explicit lower bound(1), hence requested A2(i) | PROVED | Comparison plus elementary harmonic inequality below |

## Depends on

`PD-T?proof-attempts-2-codex-04`, especially |Λ_c−L_n²|≤54; its dependency is **PD-T?proof-attempts-codex-01 (audit pending)**. Dated qualification: Claude audit-01 at `95279b833bca5967fcf47c1b71a56ff622185b4e` accepted A1; the user's literal audit-pending label is retained while upstream dispositions are pending.

## Checks

Entirely analytic. Independent route agent reconstructed the supporting comparison by hand. No finite computation is needed for(1). Supplementary exact regression passed83 kernel terms and6 square identities for n=1,…,6; a different agent actually reran both exact and sanity scripts, exit0 with byte-identical outputs. Its separate receipt is `../independent-execution-a2.md`. These supplement the required Claude audit.

## Sources

LITERATURE: Kolomoitsev–Lomako2021, arXiv:2009.07114v1, Theorem2.1, printed p.4, supplies the *global* upper asymptotic(4/π²)log²n+O(log n). It alone supplies no lower bound for a corner. Its full16-page paper was read; see `../attempts/T-A2.md`. Together with(1), it gives the two-sided corner leading term with an unspecified O(log n); a fully explicit local two-sided estimate is independently provided in -02. Bos et al.2006, Theorem3 in the author preprint, printed pp.10–12, provides the classical global O(log² n) order.

## Proof or evidence

Put B_n=Σ_{1≤r≤n,r odd}d_r/r and H_n=Σ_{r=1}^n1/r. Pair each odd index2q−1 with2q. If n is even, each odd reciprocal is at least its paired even reciprocal, hence B_n≥H_n/2. If n is odd, the terminal1/n in H_n and the terminal half-weight1/(2n) in B_n cancel in this comparison, so the same inequality holds. Also H_n≥∫_1^n dt/t=log n. Since sin x≤x,

\[
 L_n\ge\frac4\pi B_n\ge\frac2\pi\log n.
\]

The right side is nonnegative. Squaring and applying -04 proves Λ_c≥L_n²−54≥(4/π²)log²n−54. The final logarithmic version follows as stated. ∎

## Scope

This closes A2(i), including an explicit stronger additive lower loss54. It is a statement about the corner, with no inference that a global maximizer lies there. No priority claim.

## Open items

Required Claude audit. A2(ii) and A2(iii) are separate records; the full A3 expansion is not addressed.

## History

2026-11-01, Codex `/root/a2_develop`, requested gpt-6.1-sol xhigh; rules first read at `a09d910ae7d5526b1e216066421a0bee7fc20da4`, reread at `818ca4ad0942eb4743860f913a299ff30d959dae`. Gate, pinned inputs, stop criteria, and audit interruption: `../attempts/T-A2.md`. This is the first ordered A2 deliverable; no status of the stronger original source expansion is silently changed.
