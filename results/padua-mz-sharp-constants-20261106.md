# padua-mz-sharp-constants-20261106 — sharp MZ constants

## Analytic results developed in this continuation

- **CC lower endpoint:** PROVED local one-sided bound limsup (logN)^2 lambda_min<=pi^4/8, on both parities. The full sharp limit is proved in the new P3 development below; shared PD-T020 remains untouched. [Theorem](../topics/padua-mz-sharp-constants-20261106/theory/S1-sharp-one-sided.md); [independent reconstruction](../topics/padua-mz-sharp-constants-20261106/independent-checks-S1-S3.md).
- **CC upper endpoint:** PROVED local uniform all-N upper constant5/3, the deficit law1−eta asymp(1+logN)^−2, and qualitative convergence of lambda_max to the exact registered endpoint normLambda_edge, common to both parities. [Uniform bound](../topics/padua-mz-sharp-constants-20261106/theory/S2-uniform-upper.md); [deficit](../topics/padua-mz-sharp-constants-20261106/theory/S2-eta-deficit.md); [limit](../topics/padua-mz-sharp-constants-20261106/theory/S2-qualitative-limit.md); [limit check](../topics/padua-mz-sharp-constants-20261106/independent-checks-S2-limit.md). [Explicit finite brackets](../topics/padua-mz-sharp-constants-20261106/theory/S2-finite-certificate.md) and their vanishing error are also proved and [independently checked](../topics/padua-mz-sharp-constants-20261106/independent-checks-S2-certificate.md); no finite certificate solve was run. Certified decimal evaluation and a practical elementary convergence rate remain OPEN.
- **Signed Padua logarithmic limits:** PROVED local complete signed-form reduction, compact Bessel-corner spectral limits, exact operator characterization of both constants, common even/odd values, and an explicit finite approximation error. [Full form](../topics/padua-mz-sharp-constants-20261106/theory/S3-full-form-log-model.md); [kernel](../topics/padua-mz-sharp-constants-20261106/theory/S3-corner-kernel-hard.md); [operator theorem](../topics/padua-mz-sharp-constants-20261106/theory/S3-corner-operator-limit.md); [independent check](../topics/padua-mz-sharp-constants-20261106/independent-checks-S3-operator.md). A strict normalized carrier improvement is also proved. Decimal constants and a closed scalar expression remain OPEN.

These are local theory statuses with supplementary independent checks. Shared final IDs/registries and the manuscript have not been changed. [Proposed manuscript statements](../topics/padua-mz-sharp-constants-20261106/manuscript-insert.md) keep all limitations explicit.

## Measurements and next step

K0 replays pass;42-row CC scan throughN102401 and repository-only K1/K3 replays pass numerical checks. K1 two-window intercept stability passes, but K2 operationally rejects the first lower equality model; no arbitrary revision. K3 agrees with the finiteJ512 upper model proxy within5.344e-8, MEASURED only. Finite Padua model proxies are about−0.1336,+0.0456, with uncertified decimal accuracy.

All16registered Padua minima complete with guards passing; the independentm3000 value agrees to2.78e-17 absolute. Stable negative slopes near−0.092 operationally reject the finiteK128−0.1336 proxy by31%; finite-window parity slopes agree. Upper numerical gates remain INCONCLUSIVE after the capped pilot. A bounded normalization diagnostic found no tested factor mismatch but substantial full-form trial correction; neither it nor the fits certifies the asymptotic window. [Claude audit-01](../topics/padua-mz-sharp-constants-20261106/audit-01.md) accepts the mathematics at every stated scope; the K1 intercept lies above the proved π⁴/8 bound, so K2 is no evidence against equality, and the K4 finite-window minimiser is B's second mode (MEASURED audit diagnostic). Registry mapping of PD-T027/PD-T381 awaits AC. Next: [response and closing development](../topics/padua-mz-sharp-constants-20261106/handoffs/03-response-and-work.md). [Log](../topics/padua-mz-sharp-constants-20261106/LOG.md); [gates](../topics/padua-mz-sharp-constants-20261106/gates.md).


## 2026-11-06 audit-01 K2 interpretation addendum

The K1 final-window intercept 13.0611 exceeds the PROVED bound
limsup (log N)² lambda_min <= pi⁴/8 = 12.1761. It therefore cannot identify
the true limit under S1-02. K2 KILL_MODEL remains the registered operational
outcome and carries no evidential weight against equality; the equality
route stopped on a misspecified numerical test. The candidate is **deferred**,
with resume condition: a proof of the reverse bound liminf >= pi⁴/8, or a
new prospectively registered numerical protocol. No PD-N is created.

## 2026-11-06 audit-01 K4 interpretation addendum

S3-03 (3)/(4) predict limits, and make no prediction about finite-window
slopes. K4 compared those limits with finite-window slopes and retains its
unchanged KILL_HEURISTIC_PROXY outcome. The audit diagnostic
[big.json](../topics/padua-mz-sharp-constants-20261106/audit-01-support/S3/big.json) and
[mid.json](../topics/padua-mz-sharp-constants-20261106/audit-01-support/S3/mid.json) is MEASURED floating evidence:
at m=400,800,801 the Q-minimiser has about 94–96% weight on the second
L_m mode, while L_m's bottom mode already lies near the B proxy −0.1336.
Mode-dependent O(1) corrections explain the registered slopes near −0.092
without contradicting the theorem. This is a finite-scope interpretation,
not a certified crossing law or a PD-N.

## 2026-11-06 original-target decision still reserved for AC (audit A3)

No registry mapping is chosen. PD-T020 stays OPEN. For PD-T027 and
PD-T381, option (a) accepts the explicit computably approximable operator
characterizations as identifying the values, yielding PROVED mappings;
option (b) conservatively maps existence/uniform-gap/parity-agreement
conjuncts to PROVED split records and leaves numerical-value conjuncts OPEN,
yielding PARTIAL. The exact original target wording must be preserved in
History. The auditor recommends deciding after P1/P4 development and notes
that (a) remains defensible if decimal enclosure attempts fail. AC decides;
registries are untouched in R.

Durable MEASURED records: [S1](../topics/padua-mz-sharp-constants-20261106/theory/S1-measured.md), [S2](../topics/padua-mz-sharp-constants-20261106/theory/S2-measured.md), [S3](../topics/padua-mz-sharp-constants-20261106/theory/S3-measured.md).

## Handoff03 closing results (2026-11-06)

- Local PROVED [reverse CC bound](../topics/padua-mz-sharp-constants-20261106/theory/P3-reverse-bound.md) completes the exact limit pi^4/8 on Pi_(N-1) and Pi_N, through both parities. Independent signed-remainder and full-assembly reconstruction pass; no new CC fit. This supersedes the earlier local OPEN description while preserving the original gates and registry.
- Local PROVED [elliptic kernel](../topics/padua-mz-sharp-constants-20261106/theory/P1-elliptic-kernel.md) and [positive spectrum](../topics/padua-mz-sharp-constants-20261106/theory/P1-positive-spectrum.md) identify c_minus=-norm(B), the simple positive ground state and 0<c_plus<norm(B). The [exact rectangle instance](../topics/padua-mz-sharp-constants-20261106/theory/P1-numeric-certificate.md) yields the independently rerun coarse enclosure [-0.477809279990884889210594,-0.013164946500379018110831] for c_minus, with no useful digits certified. Three-digit values and a c_plus-specific certificate remain deferred.
- Local computer-assisted PROVED [endpoint lower certificate](../topics/padua-mz-sharp-constants-20261106/theory/P4-certified-lower.md) gives Lambda_edge>=1.0044369, with exact arithmetic and actual distinct checker rerun. A sharp practical upper bound remains OPEN.
- [P2 finite-mode measurements](../topics/padua-mz-sharp-constants-20261106/theory/P2-measurements.md) retain the prospective criteria and calibration. All four main cases pass the registered finite test (prospectivity is qualified below), including mode2 weights above0.9589, parity branch rates0.03844594/0.03759102 and Qmin secants-0.09212119/-0.09246210 within0.006 of registered b2. Distinct m1600 rerun and final summary replay pass. This remains finite MEASURED evidence; K4 is unchanged.

[Claude audit-02](../topics/padua-mz-sharp-constants-20261106/audit-02.md) accepts P3 (full limit pi^4/8), P1, P4 and P2 at their stated scopes; the P1 interval certifies no useful digits, and P2's secant criterion was largely postdictive (audit-02 B1). Next: [bounded records response](../topics/padua-mz-sharp-constants-20261106/handoffs/05-response-02.md); applying P3 to registry PD-T020 waits for PR preparation. AC alone chooses A3 registry interpretation; no shared registry or manuscript edit is made here.

## 2026-11-06 audit-02 B1/C2 scope correction

Q_min at m=1400/1401,1800/1801 and3000/3001 was already committed at5110954b07fd834982167780daa8cd22bef13ce1 before the P2 protocol. The registered secant-to-b2 criterion was essentially postdictive; only the mode-2 weight, L-distance and branch-difference-rate criteria were prospective. [Existing-row diagnostic](../topics/padua-mz-sharp-constants-20261106/audit-02-support/P24/P2-preexisting-predictivity.json). This dated correction qualifies earlier fresh/prospective wording without changing thresholds, receipts or PASS_FINITE_TEST.

The earlier phrase “PD-T020 stays OPEN” describes the unchanged shared registry only. Audit-02 accepts the full P3 pi^4/8 limit; applying it to PD-T020 waits for PR preparation and readiness. A3 is a separate AC decision concerning PD-T027/PD-T381 only. The coarse P1 enclosure certifies no useful digits.

## Handoff05 bounded response completed (2026-11-06)

[Response-02](../topics/padua-mz-sharp-constants-20261106/response-02.md) answers B1/B2/C1–C4. The [PROVED supporting denominator identity](../topics/padua-mz-sharp-constants-20261106/theory/P4-denominator-closed-form.md) records all existing S2/P4 diagonal and off-diagonal formulas; [distinct supplementary reconstruction](../topics/padua-mz-sharp-constants-20261106/independent-checks-P4-denominator.md) passes. No mathematical statement, threshold, receipt, PASS outcome or accepted certificate status changes. The manifest now excludes audit-*-support; original scientific evidence is unchanged. Next is the focused Claude recheck of this derivation and diff confirmation of the remaining record edits, followed by PR preparation with the existing A3 decision reserved for AC.
