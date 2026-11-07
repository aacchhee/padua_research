# D08 attempt — Adopt the already certified limiting corner margin

Rules/read input `cbfdb044e184731984e3bf8be487008a86e68c37`.
2026-11-06; parent-assigned Sol xhigh, serving metadata unexposed.
Developer/provenance check only; root owns Git/shared files.
The fresh gate and duplicate kill test are in
[ideas/D08-corner-limit.md](../ideas/D08-corner-limit.md).

## Decisive outcome

The target is already **PROVED** in the stronger accepted enclosure of
[PD-T271](../../padua-lebesgue-followups-20261103/theory/t4-03-corner-constant.md),
Statement(2). Its constant kappa is exactly

    D_infty=(8/pi) integral_0^1 t^2 cot(pi*t/2)
                   sum_(l odd>=1)1/[l(l^2-t^2)]dt.

The exact strict lower endpoint is

    D_infty>0.919710118388492535099518225790>9/10.          (1)

The second inequality is just comparison of two exact terminating
decimals/rationals. There is no finite-degree or sampled premise.
Disposition: **EQUIVALENT / CONSOLIDATED**, with no new theory file,
scientific ID, numerical proof or mathematical run. The current assembly
can cite PD-T269 for the integral and PD-T271 for the accepted strict
bound, retaining its stated computer-arithmetic trusted base.

## Normalization and exact mathematical dependency

[PD-T269](../../padua-lebesgue-followups-20261103/theory/t4-01-corner-defect-limit.md)
proves Lambda_c(n)-L_n^2 tends to the integral above, with continuous
endpoint values and both parities. Its coefficient identity and exact
tail are

    D_infty=(8/pi^2) sum_{k>=0} c_k/(k+1),
    |D_infty-(8/pi^2)sum_{k=0}^K c_k/(k+1)|
                               <=8/[3(K+2)4^(K+1)].     (2)

The full series coefficient definitions and proof were read, including
the cancellation of the l=1 endpoint pole and every factor8/pi^2.
The finite reduction is mathematical, rather than an assumed quadrature
or a decimal fit. PD-T271 labels the decimal enclosure PROVED and gives
the reduction to outward Arb arithmetic plus exactly the tail in(2).
The n>=32 assumption for its finite expansion is not an onset for a
constant depending on n: D_infty in(1) is one fixed real number.

Keep the distinct names

    kappa_shift=gamma+log(8/pi),
    A(L)=(2/pi)(L+kappa_shift),
    M_infty(0,L)=A(L)^2+D_infty.

The last equality is the routine phase-zero polynomial identification
in D03's record, using PD-T269/270 and the accepted D02 true limit:
S_n(0)=Lambda_c exactly, both limits agree, and a polynomial in log n
tending to zero has all coefficients zero. No fitted limiting value
is involved. C08's E_infty=a/3+a C(t_d)C(t_e)/pi^2 is a different
renormalized endpoint constant and is not substituted for D_infty.

## Code, exact tail and essential committed evidence

All paths below are under `topics/padua-lebesgue-followups-20261103/`.
Their availability was checked locally and with read-only `git ls-files`.
These are current observed identities, not newly manufactured receipts.

| Path | Bytes | Current SHA256 |
|---|---:|---|
| code/t4_constant.py |4582| b48d488e2229e7c60293673ffeeec0214fed344858f7ddaebe9975c0dd7347e5 |
| evidence/t4-constant.json |4736| eff53b81ab76245d923846a80a10ae8116a29701bbefb8d34e8c8afa1ced78b9 |
| evidence/analytic-independent-t4.json |5285| 74f3bf87293df345154d84bd1ef29deb7009f317c38507c9d94ef4a6c287e97f |
| audit-support/claude-audit-01/reruns/t4-constant-claude-64-320.json |1398| 08726c48298a2b6c0a6a49331bb2942035daf0d3b1a1599c652c2bc49ac3d224 |
| audit-support/claude-audit-01/reruns/t4-constant-claude-96-448.json |1437| 2a07645bf8c6e15eb7c2a7bb1659e4625669fd4bbdf9e990c5889f9123508abe |

The complete developer source was inspected. It sets Arb precision,
forms the a_p,b_q,c_k coefficient balls from(2), evaluates the partial
sum with outward zeta/pi arithmetic and adds a symmetric tail ball.
At inclusive order64/bits320 the exact tail radius is

    8/(3*66*4^65)
      =8/269503634601383263062992689085960423473152.

It then ASSERTS strict containment between exact decimal endpoints;
this comparison is stronger than merely printing a midpoint. Arb's
conversion encloses each exact decimal, so a successful strict ordering
of the balls establishes strict ordering with the exact endpoints.

The developer receipt has `rational_bracket_checks:true`, source hash
b48d488e..., order64, precision320, and exactly that analytic tail.
The current developer receipt SHA eff53b81... EXACTLY equals the final
independent rerun SHA recorded in analytic-independent-t4.json. Thus
the locally available small result is byte-identical to that actual
independent execution's output, not merely consistent in printed digits.

## Actual independent executions and accepted status

[independent-checks-analytic.md](../../padua-lebesgue-followups-20261103/independent-checks-analytic.md)
records distinct Astra high analytic reconstruction and actual runs at
order64/bits320, order80/bits384, then a final order64/bits320 replay.
Their commands, exit codes0, exact source hash, output identities and
trusted dependencies are in the committed independent receipt above.
The source hash there is the current b48d488e... . The first/final runs
included finite regressions, explicitly separate from the enclosure.

[Claude audit-01](../../padua-lebesgue-followups-20261103/audit-01.md)
has the explicit disposition `T4 t4-01,t4-02,t4-03: ACCEPTED,PROVED`.
It reconstructs the analytic coefficient/tail proof and reports actual
separate reruns of the same unchanged source at64/320 and96/448.
Both small rerun receipts are present above, have strict bracket checks
true, pin source b48d488e... and use Python3.13.18/python-flint0.9.0.
The string OUTWARD_ENCLOSURE_DEVELOPER_RUN is the source's generic output
label even in an auditor rerun; independent execution ownership comes
from the actual audit and its separate receipt, not renaming that label.

The cross-family audit also wrote its own code without importing topic
code and certified the same bracket by an independent digamma integral
and a rigorous [0,2^-200] head bound. Its committed independent code and
essential result remain locally readable:

- audit-support/claude-audit-01/claude_analytic_checks.py,
  14674B, SHA256
  `5dd1483baacd699c23f4f3807a91c40ba9d8244b22937326d0cba1ec53797c3d`;
- audit-support/claude-audit-01/claude_analytic_checks.json,
  8394B, SHA256
  `7ef3a015be81ce75cc28a6c4789a70994fffbe71b8d197b0a80c87572526cb81`.

Its `kappa_arb_rigorous` block reports precision480, exact delta2^-200,
strict containment true and the outward ball
`[0.91971011838849253509951822579023674611 +/-8.72e-39]`.
The code's rigorous section and JSON were inspected, not executed in D08.
The accepted coefficient route already suffices for(1); this second
analytic reduction is corroborating independent accepted evidence.

Current prose hashes differ from historical theory hashes in execution
receipts. Final-ID headings, dated registration notes and the documented
notation/predecessor corrections account for the subsequent prose
history; response-01 expressly preserves executed code/evidence and
mathematical claims. Old execution identities have not been relabeled
as current bytes. Current PD-T271 Statement(2) is exactly the strict
enclosure accepted in those mathematical checks.

## Trusted arithmetic, retrieval limits and non-premises

The certificate's trusted numerical base is Python integer arithmetic
and python-flint0.9.0/Arb outward elementary and zeta arithmetic, together
with the inspectable analytic coefficient reduction and exact tail.
Historical developer Python is3.12.14; Claude reruns use3.13.18. No
uncertified fixed-precision rounding assumption is substituted.

The developer's optional mpmath finite-n regressions, the auditor's
float64 corner values, its mpmath integral/series agreement, PSLQ nulls
and grids are all MEASURED and are not premises for the strict bound.
The command without `--regressions` evaluates the proof series alone;
no board computation or numerical integration is required by that route.
No such command was rerun here, and ambient package availability was
not assumed or checked as a new execution claim.

Code, essential developer result, independent rerun records and audit
are committed and locally retrievable; their proof does not require an
unavailable scratch transcript. The old topic's raw-output cold-storage
delivery remains pending, and scratch paths in old receipts are not
promised future retrieval locators. Its storage addendum explicitly
retains small essential receipts/summaries/code in Git. This finding
does not claim physical delivery or guaranteed external retention.

## Scope and stop

The constant target is closed by existing PD-T271, with its established
computer-assisted proof. No duplicate PD-T or new numerical run is made.
The proposed ordinary positive l=1+l=3 polynomial route is unpursued,
not refuted; it is unnecessary unless a different arithmetic dependency
is separately requested. All generated D08 records stay below16KiB each.

In particular, (1) does NOT imply Lambda_c(n)>=A(log n)^2+9/10 at a
finite n. D03's exact finite identity still contains
Delta_n-D_infty-(L_n^2-1)/(n+1), and no error compensation is supplied
by this constant fact. The prospective D08 onset40000/50000 assembly
must prove its own finite comparison. Old quantifiers, corrections,
native sources and degree certificates remain unchanged.

Resource receipt: first clock17:11:41 UTC; parent cap20 analytic minutes.
Only read-only proof/code/JSON inspection, searches, hashes, tracked-path
checks, metadata extraction and these two Markdown records were used.
No mathematical scalar computation, native/board/quadrature/degree job,
producer, child agent, Git mutation or shared-file edit occurred.
