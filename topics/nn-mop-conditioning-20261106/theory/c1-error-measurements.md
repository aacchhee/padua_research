# PD-T?nn-mop-cond-codex-C1-06 — source error against matrix sensitivity bounds

ID kind: PD-T. Aliases: first-order source-error diagnostic; authenticated
monic spectral comparison; integer versus normalized node boxes.
Split from: none. Split into: none.

## Statement and status

Overall status: MEASURED. For the final C4 CORE, REORTH and KRYL tables,
both exact benchmark families, every N4–32 and both input-node conventions,
348 relative spectral errors E were compared with the numerically
evaluated analytic condition bounds L_N<=kappa_2,N<=U_N from
`c1-matrix-metric.md`. With binary64 unit roundoff u=2^-53, the resulting
diagnostic bounds are

    E/(U_N u) <= E/(kappa_2,N u) <= E/(L_N u).

These concern the authenticated monic output with unit subdiagonal. They
do not calculate the exact induced box-to-spectral norm and are not
outward arithmetic certificates. They do not prove or disprove a
weak-stability theorem with an unspecified polynomial factor.

## Input fidelity and dependencies

The final C4 receipt supplies executed M2/M4 PASS. All58 shared binary64
input cases passed bit equality using IEEE754 hexadecimal import/export;
all116 family/size/input cases completed without solver failure, for348
external calls. An earlier decimal-JSON run altered some normalized nodes
by one ulp; its exploratory diagnostic is superseded here.

`code/c1_error_diagnostic.py` checks those receipt fields and hashes all
six final external CSVs before accepting them. `c1-error-comparison.json`
stores its code hash, final receipt/table hashes, the matrix-bound raw
hash, all twelve aggregate cases and selected N16/N32 details. C4 owns
source normalization, external execution, exact references and source
fidelity; no paper table or licensed random experiment was rerun by C1.
The matrix bound has the exact rational benchmark as its base input;
the reported solver error also includes input rounding and arithmetic.

For `archive_integer`, node perturbations have absolute scale one in
k=0,...,N-1. For `shared_normalized`, they have absolute scale one in
z=2k/(N-1)-1, and the output is converted to the same integer monic H.
Weights have componentwise-relative scale in both cases. These are
different input boxes, so their condition lower bounds differ.

## Results

The following bounds contain the numerically evaluated maximum over
N4–32 of E/(kappa_2,N u). Endpoints are printed away from the numerical
interior; the floating bounds and table-rounded errors are MEASURED.

| Family | Method | Integer nodes | Normalized nodes |
|---|---|---|---|
| Krawtchouk | CORE | [0.07814,15.30591] | [0.01262,0.69028] |
| Krawtchouk | REORTH | [0.03693,5.69908] | [0.01749,0.87518] |
| Krawtchouk | KRYL | [145.11281,18721.76490] | [0.51885,28.63507] |
| Hahn | CORE | [0.59371,107.82542] | [0.02013,2.65648] |
| Hahn | REORTH | [0.01101,1.33581] | [0.01501,1.30015] |
| Hahn | KRYL | [6.64017,597.03640] | [0.26626,12.02997] |

For example, archive-integer Krawtchouk KRYL at N16 has E=0.924412653
and numerically evaluated kappa_2 u in
[4.9376362658e-5,0.006370303415], giving diagnostic bounds
[145.11281376,18721.76489391]. This demonstrates that a unit-constant
first-order scale does not explain every observed error. It does not
refute an error bound with a larger constant or polynomial factor.

For both node conventions L_N u first exceeds one at N21 for Krawtchouk
and N19 for Hahn. At these sizes and beyond the local condition already
allows order-one first-order amplification. Very small later diagnostic
ratios therefore supply no finite-perturbation accuracy guarantee and
do not establish backward stability. Worst-case condition capacity alone
does not show that actual rounding errors follow its maximizing direction.

## Checks and scope

The producer completed with all final receipt/table hashes accepted and
all348 rows covered. Its arithmetic is direct evaluation of the two
displayed ratios; matrix bounds and source errors retain their separate
proof and execution records. Supplementary independent review is in
`independent-checks-01.md`; this record is not self-approval.

No universal constant, polynomial error theorem, exact spectral-condition
optimizer, finite-epsilon radius or outward enclosure is asserted. The
results depend on the recorded Octave/platform/source execution and the
printed error precision. The earlier exploratory input serialization
has no role in these final numbers.

## History

2026-11-06, Codex gpt-6.1-sol xhigh, rules/input snapshot
`b4a04981d42c7cd872957facf5e3995e4096ca67`. Round3, after C4 supplied
the final bit-preserving rerun; no new NN derivative sweep or Git action.
