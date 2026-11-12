# PD-N?padua-3d-20261106-codex-prune-P5 — first reflection-pair deletion under fixed preservation constraints

ID kind: PD-N.
Aliases: PRUNE-pair; P5 reflection-pair screen; first atomic block barrier.
Split from: none.
Split into: none.

## Status by part

Overall status: **MEASURED**; finite registered experiment P5.
Candidate disposition: **REJECTED: failed** for the frozen first-pair
preservation/continuation goal only. The general pruning target is OPEN.
Rejection reason: failed within the finite numerical scope below. This is a
known block-deletion/design operation, not a priority or algorithmic
novelty claim. The predecessor/formula gate is
[pruning-next-questions.md](../pruning-next-questions.md); the complete
prospective question is the P5 appendix of
[pruning-protocol.md](../pruning-protocol.md).

## Statement

On the original canonical anisotropic parity supports at n6/8, none of
all 48/100 nonfixed x1-reflection pairs is feasible under P2's unchanged
training-amplification limit 1.25 times the full-start value and physical
integer-budget risk limit 1.10 times the full-start value. All 148 pairs
pass the stated block-rank threshold. The numerical census finds zero
training-feasible pairs, with 45 of 48 n6 pairs and all 100 n8 pairs passing the noise limit separately.
This closes only the tested first atomic reflection-pair escape from the
measured singleton barrier. It does not prove impossibility for other
blocks, supports, reflections, counts or all-subset design problems.

## Definitions and assumptions

Canonical anisotropic parity supports, degrees n6/8, physical unweighted
OLS, fixed B=112/225, and P2's 985-query dense training set are fixed by
[the P5 protocol](../pruning-protocol.md#p5-prospective-appendix--one-reflection-pair-step).
Pair feasibility requires min eigenvalue(I−H_JJ)>1e−10, training ratio
<=1.25, integer-risk ratio <=1.10; finite binary64 computations use the
registered guards/ties. Sampled/searched values are lower values.

For starting physical-value OLS map C, H=QQ^T, deleted pair J and retained
indices K, the predicted map used the standard plus-sign identity

`C^-_K = C_K + C_J (I-H_JJ)^-1 H_JK`.

Training cardinal values use the same update with L=EC. Every candidate's
integer allocation has at least one real observation per retained site;
B remains the original 112/225 observations. Unit-noise trace is recorded
separately and increases on deletion. Haar weighting is only a separate
control; it is not substituted into physical iid covariance.

## Negative-result scope

Attempted mechanism: IDEA?padua-3d-20261106-codex-prune-pair, atomic removal
of one nonfixed x1-reflection pair while preserving all fixed-plane nodes.
Parameter range: all 48/100 specified pairs on the initial n6/8 supports;
no full block trajectory, other reflection/support or arbitrary subset.
The statement concerns measured first-step feasibility under unchanged
P2 constraints, not a universal lower bound or proof of impossibility.

## Depends on

[Pruning identities](../pruning-theory.md), the
[parity recipe](u1-parity-recipe.md), physical-noise convention in
[U1 OLS](u1-ordinary-ls-blue.md), and the separately measured
[P2 singleton boundary](pruning-p2-singleton-boundary.md). No theorem about
continuous amplification or optimal design is imported.

## Proof or evidence

| Quantity | n6 | n8 |
|---|---:|---:|
| Starting sites / polynomial dimension | 112 / 84 | 225 / 165 |
| Tested reflection pairs / fixed-plane sites | 48 / 16 | 100 / 25 |
| Training / noise / jointly feasible pairs | 0 / 45 / 0 | 0 / 100 / 0 |
| Best risk-feasible training norm / full | 1.405160 | 1.438422 |
| Infeasible diagnostic IDs | (37,69) | (57,157) |
| Diagnostic unit-noise trace | 0.760989 | 0.727302 |
| Diagnostic integer-budget risk | 0.750688 | 0.722320 |
| Diagnostic held-out/searched norm / full | 1.456458 | 1.532051 |

The diagnostic candidates leave 110/223 sites but do not change the
operational supports, which stop at the full 112/225 sites. Fresh QR maps
agree with their block predictions within 1.13e-15 relative error and pass
all rank/condition/reproduction/QR/orthogonality guards. Their two singleton
intermediates remain infeasible and reproduce the existing P2 training
scores within 6.29e-16 relative error. The n8 pair improves the best
risk-feasible singleton training norm by 0.414%; this finite interaction
still fails the predeclared bound. The n6 pair worsens it by 9.18%.

The same-count random/restricted controls have larger norms than these
pair diagnostics, but the strict full-start preservation goal fails and
neither degree passes the independent 1.30 held-out norm ratio. Full OLS
norms are 6.677336/7.902095, versus diagnostic norms 9.725262/12.106412.
Deterministic target errors are mixed: RMS and maximum regressions remain
in the all-target report, including a 75.99% uniform-query maximum-error
increase at n8. There is no universal approximation/noise/cost dominance.

## Checks

The [receipt](../evidence/pdpr-pair-screen.json) and
[results](../pruning-results.md) link the original executed sources,
protocol, complete full-precision raw inventory, queries/seeds, physical
maps, integer repetitions, all candidate scores and target/noise tables.
All 18 assessment aliases completed as 17 distinct maps, each with the
same meshes, fresh queries and 28 local searches. No assessment was
omitted or capped. Total time is 3.946726 CPU / 3.948788 wall seconds;
complete pair construction costs are 0.038943/0.117543 CPU seconds.
Rounded-coordinate fitting and sampled/searched norms are numerical
measurements, not exact full-rank or continuous-norm certificates.

[Engineering](../evidence/pdpr-p5-engineering.json) verifies 109 generic
block maps/cardinals/noise classifications against fresh QR, 21
rank-inadmissible deletions and explicit feasibility/tie/nonfinite/cap
branches. Independent preflight additionally passed 114 generic block
cases. [Consequential P5 review](../pruning-review.md) passed all 148
fresh-SVD pair states, both actual frozen screen reruns, 17 fits/18
aliases, 49 raw files and 952 stored search-point values. A further 280
fresh refinements preserve the negative outcome; the independently
sharpened n8 diagnostic ratio is 1.532947. No full paired trajectory is
justified by the fixed both-degree continuation gate. Other blocks remain
open; unused campaign rounds are a ceiling, not a quota.

2026-11-07, Codex gpt-6.1-sol high developer; root owns publication,
counters and formal handoff. The useful measured A546/A1163 tradeoffs and
separately certified exact canonical-ID artifacts remain separate results.

## Sources

Known block-Woodbury/design precedents and coverage limits:
[gate addendum](../gate-addendum-audit04.md). No new source theorem or
algorithmic priority is claimed.

## Scope and open items

Only the first specified reflection-pair screen fails. Other blocks,
supports, weights, budgets and universal subset questions remain OPEN.
The finite campaign is frozen at 5/15 by AC's approved narrowed plan;
resume requires an explicitly reopened, prospectively gated question.

## History

2026-11-07: original measured P5 negative, as above. 2026-11-12, Codex,
gpt-6.1-sol high: audit04 G7 completes the THEORY template, introduces its
provisional scoped PD-N home and spells out the 45/48 and 100/100 noise
counts; all measured values and the finite claim are preserved. This is
record repair, not a new run, theorem or mechanism. Final ID/crosswalk
application remains PR preparation.
