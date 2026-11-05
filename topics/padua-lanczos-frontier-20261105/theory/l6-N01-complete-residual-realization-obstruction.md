# PD-N?lanczos-frontier-codex-L6-01 — No unbounded e/u realization under two complete square residual budgets

ID kind: PD-N.
Aliases: complete-square e/u separation obstruction; well-conditioned full-residual realization barrier.
Split from: IDEA?lanczos-frontier-codex-L6-01 and its saved L6 draft; only the specified realization mechanism is rejected.
Split into: none. Quantitative supporting theorem: [PD-T?lanczos-frontier-codex-L6-01](l6-01-full-square-residual-bound.md).

## Statement

There is no sequence indexed by k with `0<e_k<=1/300`, `u_k>0`, `e_k/u_k -> infinity`, a fixed finite constant `c>0`, commuting real 3-by-3 matrices `X_k,Y_k` of norms at most one, and invertible real 3-by-3 matrices `Q_k` satisfying all of

1. `||Q_k^T Q_k-I||_2<=1/2`;
2. `||X_k Q_k-Q_k Hx(e_k)||_2<=c u_k ||Q_k||_2`;
3. `||Y_k Q_k-Q_k Hy(e_k)||_2<=c u_k ||Q_k||_2`.

Here `Hx(e),Hy(e)` are exactly the PD-T145 sections in the common orthonormal gauge specified in l6-01, and both residual inequalities contain every column.

## Definitions

Spectral norm; complete residuals and section gauge as in l6-01. The original square coordinate matrices `X=diag(0,1,0)`, `Y=diag(0,0,1)` are a special case. No per-operation floating-point realizability assumption is made or needed for this necessary-condition obstruction.

## Assumptions

All listed hypotheses are required for this stated scope. In particular, fixed c is a uniform residual budget; c is not allowed to grow with k. A missing or implicitly completed Y relation is not a complete residual bound. No approximate data match or consistency correction is included.

## Status by part

Overall status: PROVED (analytic consequence of l6-01; distinct independent reconstruction PASS in [independent-checks-frontier-05.md](../independent-checks-frontier-05.md); later required Claude audit remains pending).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Nonexistence of the sequence satisfying 1–3 | PROVED | Uniform bound `e_k/u_k<=24 sqrt(3)c` below |
| General actual-run Greenbaum target PD-T056(G) | OPEN | Not the negation asserted here; no actual execution or universal obstruction is supplied |

Candidate / claim disposition: **REJECTED** for realization of PD-T145 with unbounded e/u by a near-orthogonal square Q and two complete uniformly O(u) local residuals.
Rejection reason: **refuted**, within exactly hypotheses 1–3 and the displayed parameter range.

## Negative-result scope

Attempted mechanism: IDEA?lanczos-frontier-codex-L6-01's possible realization of the exact PD-T145 reading-(E) family with a much smaller local roundoff scale, retaining near orthogonality and complete residual bounds for both original operators.

Parameter range: n1, square 3-by-3 Q, `0<e<=1/300`, norm-at-most-one commuting originals, Gram loss at most one half, exact family match and a fixed finite residual constant c. This rejects that conjunction, not every way to generate section perturbations. It does not reject a one-relation BJ run with an uncontrolled omitted Y residual, an ill-conditioned Q, a different family, corrected/approximately matching sections, e=O(u), or a positive nearby model for arbitrary actual runs. PD-N020/022 are reading-(E) predecessors and are not used to infer this actual-(G) negation.

## Depends on

PD-T?lanczos-frontier-codex-L6-01, inequality (3), including all complete-residual and norm hypotheses. PD-T145 only through that theorem. No external theorem.

## Checks

Written analytic implication; no scientific code or experiment. Distinct reviewer `/root/reviewer`, requested `gpt-6-astra` high (runtime metadata not independently exposed), independently reconstructed the theorem and no-sequence implication and accepted its limited scope: **PASS**, [durable review](../independent-checks-frontier-05.md), section "Additional root allocation: L6 necessary-condition review". Initial reviewed input SHA256 `ec5ab9b7cba2bc501a5e0b92485f0919d233e4d5e0f81e38398813b02be2f17b`. The reviewer's nonblocking wording change from "Every listed hypothesis is essential" to "All listed hypotheses are required for this stated scope" was accepted, with editorial successor SHA256 `ea73e94c0def8117e8095be6a1b07d8069d70665b4c42fc935176cf00b18866f`. The reviewer confirmed that this preserves the theorem; subsequent changes are review metadata only. Statement, quantitative hypotheses and proof body are unchanged. No execution or actual nearby measure is claimed. The independent reconstruction does not replace the required later Claude audit.

## Sources

Internal l6-01 and PD-T145. Completed gate and predecessor comparison: [ideas-l6-continuation.md](../ideas-l6-continuation.md). No external priority claim.

## Proof or evidence

For each k, l6-01 applies with `e=e_k`, `u=u_k`, `Q=Q_k` and gives `e_k/u_k<=24 sqrt(3)c`. The right side is a fixed finite number, contradicting `e_k/u_k -> infinity`. ∎

## Scope

The explicit complete-residual obstruction is an analytic diagnostic. A future actual n1 implementation may fail to match this family, may have a large omitted residual, or may simply have e comparable with u; none of those observations refutes general (G). No output bytes, actual recurrence or positive localized model is asserted here.

## Open items

Parent-owned registry allocation and later required Claude audit. A prospective actual-run contract is recorded separately in l6-02 and remains unexecuted. PD-T056(G) remains OPEN; the negative result is not a theorem about every actual run.

## History

2026-11-05, Codex mathematical developer, requested `gpt-6.1-sol`, xhigh; runtime variant/effort not independently exposed; rules `9825d184517db81d0aad8542fbd6639f2164b803`. New scoped negative statement separated from the quantitative theorem because the realization rejection is reported on its own. Exact target/kill and full continuation gate were saved before the proof. No final ID, Git mutation or scientific execution by this developer.

2026-11-05: distinct Astra-high routine reconstruction PASS; accepted the reviewer's nonblocking hypothesis-scope wording clarification. This avoids an unproved irreducibility assertion and changes no mathematical conclusion. Acceptance metadata added; proof body unchanged.
