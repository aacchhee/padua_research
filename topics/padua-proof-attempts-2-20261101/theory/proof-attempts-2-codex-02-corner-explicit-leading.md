# PD-T?proof-attempts-2-codex-02 — An explicit two-sided corner leading term

ID kind: PD-T.
Aliases: A2(ii); explicit O(log n) corner remainder.
Split from: OPEN_TARGETS A2 at programme SHA `9bd14a6d2c4da69139a10107d8a787f2be0c5c9e`, the two-sided leading-term part.
Split into: none; the sharper b-term is -03 and the lower-bound deliverable is -01.

## Statement

For every integer n≥2,

\[
 \frac4{\pi^2}\log^2n-54\le\Lambda_c(n)
 \le\frac4{\pi^2}\log^2n+\frac{12}\pi\log n+63.             \tag{1}
\]

Consequently

\[
 \left|\Lambda_c(n)-\frac4{\pi^2}\log^2n\right|\le95\log n. \tag{2}
\]

## Definitions

The same n, Λ_c, L_n, d_r, and B_n as in -01 and -04. All logarithms are natural.

## Assumptions

The specified Padua points, exact real arithmetic, n≥2. No global argmax hypothesis and no use of an unspecified literature O-constant.

## Status by part

Overall status: **PROVED** (written proof; Claude audit pending).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Explicit two-sided inequalities(1)–(2), closing A2(ii) | PROVED | Elementary upper estimate below and -01 |

## Depends on

`PD-T?proof-attempts-2-codex-01` and `PD-T?proof-attempts-2-codex-04`; indirectly **PD-T?proof-attempts-codex-01 (audit pending)**. Claude audit-01 at `95279b833bca5967fcf47c1b71a56ff622185b4e` accepted A1; the literal label is retained per user instruction while upstream dispositions are pending.

## Checks

Analytic proof, with no finite computational dependency. Independent hand-check of the -04 comparison and actual independent byte-identical exact/sanity reruns (separate receipt `../independent-execution-a2.md`) supplement the required Claude audit.

## Sources

LITERATURE context and complete KL reading coverage are in `../attempts/T-A2.md`. KL2021 Theorem2.1 proves only the global leading term with unspecified O(log n); the present explicit corner bound is derived locally.

## Proof or evidence

For0<x≤π/2,

\[
 0\le\csc x-1/x\le1.
\]

For a direct proof of the upper inequality, sin x/x≥(1+cos x)/2≥√(cos x), because tan(x/2)≥x/2. Hence g(x)=csc x−1/x has derivative1/x²−cos x/sin²x≥0. It extends with g(0)=0 and g(π/2)=1−2/π<1, proving the inequality.

There is total d_r weight n/2 in the odd-r sum. As in -04, B_n≤1+(1/2)log n. Therefore

\[
 L_n\le\frac4\pi B_n+1
 \le\frac2\pi\log n+\frac4\pi+1
 \le\frac2\pi\log n+3.
\]

Squaring and using the54 comparison yields the upper inequality(1); its lower inequality is -01. For n≥2, 54≤80log n and (12/π)log n+63≤95log n, since12/π+63/log2<95. This proves(2). ∎

## Scope

This closes A2(ii). The constant95 is loose and uniform for all n≥2. It does not locate the global maximum or identify b.

## Open items

Required Claude audit. The b-term is treated separately in -03; A3 remains outside this result.

## History

2026-11-01, Codex `/root/a2_develop`, requested gpt-6.1-sol xhigh; unchanged rules reread at `818ca4ad0942eb4743860f913a299ff30d959dae`. Written after the lower-bound deliverable -01. No finite fit was used to select constants.
