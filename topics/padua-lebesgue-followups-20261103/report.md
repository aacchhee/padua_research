# Padua Lebesgue follow-ups — development report

Development branch: `codex/padua-lebesgue-followups-20261103`.
Base: `440d1079e42c3ef21c40d1cf8870f5b206410c6a`.
Stage: WORK. Required Claude audit: PENDING.

## T1 — degree-eight maxima

In progress. Existing PD-T183 proves at least 44 strict interior maxima.
The exact interior and closed-square counts remain OPEN pending complete
finite checks. Fresh producer and boundary executions preserve the frozen
acceptance predicates; independent replay is separate. See
[attempt](attempts/T1.md) and [independent checks](independent-checks-t1.md).

For the paper: do not replace the historical numerical total with a certified
total until the complete interior, edge and corner checks pass. The existing
lower bound already exceeds LIT-388's numerical interior entry; the bounded
[primary-source comparison](literature-comparison.md) preserves this distinction.

## T2 — centre minima and endpoint behaviour

**PROVED; supplementary independent reconstruction accepted.** Both limiting
edge-defect integrals are reflection symmetric and strictly decrease towards
the centre. Their unique minima are `g_v(pi/2)=g` and `g_h(pi/2)=1` exactly.
The vertical proof gives an explicitly positive excess above g; the horizontal
proof reduces to a complete elliptic integral and evaluates the central square
integral exactly. Different inherited numerators are retained throughout.

A separate theorem proves the common endpoint expansion

`g_e(beta) = [8 log(2)/pi^2] log(1/d) + 1/3 + 12 log(2)^2/pi^2 + O(d)`,

where `d=min(beta,pi-beta)`, with explicit bounds in terms of `sin(beta)`.
No interchange of the endpoint limit with the degree limit is asserted.

For the paper: the [centre theorem](theory/t2-01-edge-centre-minima.md)
and [endpoint theorem](theory/t2-02-common-endpoint-expansion.md) are standalone
integral statements, using PD-T211/212 for definitions and PD-T187/188 for g.
Combined with the inherited compact-envelope theorems, they identify the
minimum limiting gaps on compact intervals containing the centre. They do not
prove finite-degree cell ordering or an effective all-degree argmax threshold.

## T3 — general-position formulas

**PROVED; supplementary independent reconstruction and reruns accepted.**
The exact one-dimensional representations have computable geometric series
with explicit tails. The vertical ratio is at most 1/2; two horizontal charts
ensure a selected ratio at most 1/2 at every interior angle. Prefactors are
not asserted to remain bounded at the endpoints.

An exact-Fraction evaluator with outward elementary enclosures and a separate
directed-Decimal Darboux quadrature agree at five positions with
`cos^2(beta)=0, 1/4, 1/2, 3/4, 99/100`. The series gives sixteen-decimal
enclosures, including `0.5485148423995582 < g < 0.5485148423995583`; the direct
quadrature gives coarser certified containing intervals. Both routes were
actually rerun independently. A separately implemented original-double-integral
floating diagnostic agrees too, but remains MEASURED and is not a proof premise.

For the paper: [the series theorem](theory/t3-01-general-position-series.md)
provides general-position evaluation and exact central agreement with PD-T188.
The published evaluator accepts rational `cos^2(beta)`; the analytic formulas
hold for every real angle strictly between the endpoints. Numerical evidence
and source hashes are in [attempt T3](attempts/T3.md) and the independent report.

## T4 — parity-independent corner constant

**PROVED; supplementary independent reconstruction and outward reruns accepted.**
The signed deformation `Lambda_c(n)-L_n^2` has a common even/odd limit kappa,
given by a positive integral and a geometric coefficient series. The local
one-dimensional estimate `|L_n-A_n| <= 1/(4n^2)` is proved without importing an
unread classical asymptotic. Thus, with `N=n+1/2`,

`Lambda_c(n) = (4/pi^2) log^2 N + b log N + c + o(1)`

with the specified `b` and `c=c1^2+kappa`, independent of parity. An explicit
vanishing remainder is given, with leading bound `604 n^(-1/5)`; it is weak
but proved. Independent Arb arithmetic plus the analytic tail bound gives

`0.919710118388492535099518225790 < kappa < 0.919710118388492535099518225791`,

`1.846160310423926079759838737947 < c < 1.846160310423926079759838737948`.

For the paper: cite the three separate records for the
[defect limit/series](theory/t4-01-corner-defect-limit.md),
[one-dimensional remainder](theory/t4-02-one-dimensional-remainder.md), and
[corner constant](theory/t4-03-corner-constant.md). Their substantive inherited
dependency is PD-T159, and through it the exact corner identity PD-T101.
The full PD-T098 expansion with `-1/N` and `O(log N/N^2)` remains OPEN.
Two finite PSLQ searches found no relation in their specified bases and height;
that is MEASURED evidence and does not exclude a closed form.

## Verification and limitations

[Analytic independent check](independent-checks-analytic.md) records exact
candidate hashes and actual enclosure reruns. Required cross-family Claude
audit remains distinct and pending. Provisional IDs are retained during WORK;
permanent reserved ranges are in [ALLOCATIONS.md](ALLOCATIONS.md).

Protocol qualification: the T2/T3 worker completed some linked predecessor
candidate/attempt reading after the first mechanisms, while the initial
registry and inherited-theory screen preceded them. The gate and independent
report disclose this timing deviation. Later reading and a clean mathematical
check do not retroactively satisfy the prospective rule or grant clean protocol
clearance; the required Claude audit must retain that distinction.

No manuscript, all-degree finite bridge, author contact, merge, global registry
rewrite or physical cold-storage delivery is part of this development step.
