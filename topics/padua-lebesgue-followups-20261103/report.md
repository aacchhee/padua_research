# Padua Lebesgue follow-ups — development report

Development branch: `codex/padua-lebesgue-followups-20261103`.
Base: `440d1079e42c3ef21c40d1cf8870f5b206410c6a`.
Stage: PR; final registrations and preparation checks complete. Draft PR20 awaits AC decision on the 4,851,736-byte aggregate storage budget; no exception to “well below 5 MB” is inferred. Claude audit-01 accepts the mathematics; editorial/provenance findings F1–F9 are answered in [response-01](response-01.md).

Final registrations: PD-T266–271 and IDEA-356–358; existing PD-T180/184, IDEA-299 and LIT-388 reused. See the [exact alias map](preparation/final-id-map.json) and [fresh reservation scan](preparation/reservation-recheck.md).

## T1 — degree-eight maxima

PD-T184 and PD-T180 are **PROVED**: exactly 44 strict interior maxima and
62 strict relative maxima on the closed square, comprising 44 interior,
16 open-edge and 2 non-node-corner maxima. Two distinct executors completed
every original interior predicate (153520 leaves and 541882 ordinary mask
records), and separately every original boundary predicate (492 edge sign
patterns and 32 active corner masks), with matching complete verified facts.

The fresh V3/V4/V5 continuation and frozen reflection completed. Both actual
typed proof-input comparisons match all 18969878 canonical mathematical bytes
to the independently replayed archive. Literal joining and two actual final
composition executions passed every original summary/accounting condition
and raw/source/component guard. No acceptance predicate changed. This is a
proved composition of separately executed original predicates under PD-T170;
no developer monolithic joined Verifier.run execution is claimed. Its false machine
full-run/count flags preserve that execution distinction. See the
[composition record](theory/t1-replay-composition.md),
[attempt](attempts/T1.md) and [independent checks](independent-checks-t1.md).

Dated 2026-11-05 audit evidence: Claude independently regenerated the identical
boundary proof payload and completed one monolithic original Verifier.run,
with count_certified true and 62 maxima. See [audit-01 §T1](audit-01.md) and
the [monolithic receipt](audit-support/claude-audit-01/monolithic-receipt.json).
This audit execution supplements the developer composition.

For the paper: the [interior](theory/t1-interior-count.md) and
[closed-square](theory/t1-closed-count.md) completion records, with their
inherited finite-reduction dependencies, certify 44/62. This gives a certified
candidate correction to LIT-388 v1 Table 3's numerical 38/56. The bounded
[primary-source comparison](literature-comparison.md) claims neither an accepted
erratum nor later-version coverage. PD-T183's lower bound and PD-T181's global
maximum theorem remain separate.

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
candidate hashes and actual enclosure reruns. Cross-family [Claude audit-01](audit-01.md)
accepts all four targets; [response-01](response-01.md) answers its minor editorial
and provenance findings. Provisional IDs are retained pending preparation;
permanent reserved ranges are in [ALLOCATIONS.md](ALLOCATIONS.md).

Protocol qualification: the T2/T3 worker completed some linked predecessor
candidate/attempt reading after the first mechanisms, while the initial
registry and inherited-theory screen preceded them. The gate and independent
report disclose this timing deviation. Later reading and a clean mathematical
check do not retroactively satisfy the prospective rule or grant clean protocol
clearance. Claude confirmed the deviation, found minor impact, and stated that
once F1 is answered it does not by itself block readiness; AC retains the
decision whether to accept the topic with that recorded deviation.

No manuscript, all-degree finite bridge, author contact, merge, global registry
rewrite or physical cold-storage delivery is part of this development step.
