# padua-mz-sharp-constants-20261106 — sharp MZ constants

## Analytic results developed in this continuation

- **CC lower endpoint:** PROVED local one-sided bound limsup (logN)^2 lambda_min<=pi^4/8, on both parities. The full PD-T020 limit and sharpness remain OPEN. [Theorem](../topics/padua-mz-sharp-constants-20261106/theory/S1-sharp-one-sided.md); [independent reconstruction](../topics/padua-mz-sharp-constants-20261106/independent-checks-S1-S3.md).
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
