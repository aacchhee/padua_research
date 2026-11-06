# Independent supplementary check — P2 implementation and calibration

Rules/input: `0205690b9c4e959a28e949083e9a1808735abf4b`.
Numerical protocol publication:
`d03e74dcf94020ba26d9fae84d3ff6c5519db901`.
Reviewer: distinct Codex supplementary agent, requested `gpt-6-astra` high;
actual serving-model and effort metadata are unexposed. Date: 2026-11-06.

**Outcome:** P2's mathematical definitions, calibration implementation and
small dense validation check out at their stated MEASURED scope. One
summary failure-path finding was returned to the developer and fixed;
ten independently executed synthetic control-flow cases pass. No
unresolved implementation finding remains in this reviewed scope.
The four main cases were not executed or reviewed by this checker at
this point. Main release still requires the coordinator's separate
publication of measured b2/K-stability and authorization.

## Scope and code identities

Read ideas/P2-protocol.md, attempts/P2.md, theory/P2-measurements.md,
P2_modes.py and P2_summary.py in full. Inspected g1_spectral's DCT weights,
orthonormal Legendre contraction and the frozen Chebyshev weight/operator
implementation. Read the complete calibration, m12/13 validation and
m400-overlap receipts, checking their finite scope and guard calculations.
This is a protocol/implementation check of the supplied finite-m test,
not a new novelty assessment or proof of its mechanism.

| Item | SHA-256 |
|---|---|
| P2_modes.py | 8e15fe58b19a1ef1a2ff71da80d18de04349d90081e02a885bcbb38b143d1161 |
| Original reviewed P2_summary.py | 6eddb283b84a076631c72eaf29fab3d26b2072477b6fa5053cee8e48d66de97e |
| Corrected P2_summary.py | 85d8e7d5bd3e876bd1f3addfbf03998042077b498b300357d44dbe26ada9f102 |
| P2 protocol prose at execution | 2dc19f83257528f338ce642d6a9f2b63963627d1f816294610a9e075bdb50f39 |

The source identities of the inherited DCT and independent Chebyshev
implementations are recorded in every numerical receipt. The missing
definitions-file preflight and unchanged verified-copy repair are
disclosed in attempts/P2.md; they are not numerical retuning.

## Mathematical and protocol checks

The Q contraction retains the full signed weights, endpoint factors,
exceptional Chebyshev coefficient and j+k-even grid. The basis factors
sqrt((2l+1)/2) make coefficient Euclidean norm equal continuous L2 norm
on the full square; triangular coefficient indices impose Pi_(m-1).
The L weights match S3-02, including -2/(m(m+1)R^2), both endpoint
halfweights, both cosine terms and R=floor(m/2). No upper Q solve is
introduced.

Lowest-six L eigenvectors are sorted before pairing. Squared projector
weights and the two-by-two compressed Q eigenvalues are invariant under
an orthogonal change within a doublet. Symmetrizing the compressed
matrix is appropriate for floating evaluation of a selfadjoint form.
The second-mode distance is to the interval between L indices 2 and 3,
not an arbitrary chosen vector. The residual, orthogonality, pair-width
and neighboring-gap guards match the protocol.

For B_K the triangle substitution b=(1-a)s gives weighted Jacobian
a(1-a)^2 s, exactly the implemented quadrature weights. Nodes satisfy
(1+j)(1+k)<=K and j+k even. The coefficient -16 e_j e_k(-1)^j includes
both zero-index halves. Factoring the Gram eigenbasis gives
sqrt(G) D sqrt(G) on its retained range; the code's equivalent reduced
matrix is correct. Index 1 is the second eigenvalue of one corner,
whereas finite L uses the second doublet. Those meanings are not mixed.

The fixed measured b2 is -0.0955298083997758, taken without display
rounding from order128/K128. The recorded K64 difference
7.78663282741121e-8, audit-proxy difference 2.9808399775801964e-5 and
order160 difference 3.0531133177191805e-16 pass their predeclared
thresholds. This is measured low-eigenvalue stability, not a certified
operator value: the Gram minima change materially with quadrature order
and the analytic tail remains 0.9375. The record discloses both limits.

The m400 overlap compares already observed audit data and is explicitly
an implementation replay, not a fresh hypothesis confirmation. The
recorded Q difference 2.05e-14, L-at-Q difference 2.08e-16 and mode-2
weight difference 3.89e-15 satisfy its tolerances. Its L-distance
0.0051505829 exceeds the main 0.005 band, but m400 is outside the main
test domain; treating it as contextual is consistent with the protocol.
I read this receipt; I did not rerun m400.

Summary formulas use physical log m for Q secants and log R for branch
decrease rates, with the correct minus sign. Weight >0.9 is strict;
L-distance and slope bands are inclusive. A branch-rate departure outside
0.038 +/-0.006 but within 50% is INCONCLUSIVE, not a kill. None of these
tests changes historical K4.

## Finding returned and verified fix

The original summary directly opened all expected files and accessed
their row keys. A missing receipt or failed-producer receipt therefore
raised an exception instead of producing the registered INCONCLUSIVE
record. It also prioritized any accumulated kill over all_valid=false,
allowing a global scoped-kill outcome despite a failed calibration or
another invalid required row. This contradicted the published prerequisite
guard. The defect concerned result disposition, not the underlying
eigensolver or numerical thresholds.

The developer changed only the summary to record missing/unreadable,
failed and mismatched-row prerequisites, skip incomplete pairs, and
force overall INCONCLUSIVE if calibration or any required numerical
guard is invalid. Departures on valid rows remain visible separately.
No fit, target, model, case list, threshold or main producer changed.

I executed ten synthetic cases against the corrected summary: all-valid
pass; valid weight kill; missing receipt; failed producer; invalid
calibration plus a departure; invalid other row plus a departure;
ambiguous doublet; rate outside the target but inside the kill band;
valid rate kill; and valid slope kill. Every process exited 0 and
returned its independently specified expected outcome. Evidence:
`evidence/check-P2-summary-control.json`. These artificial rows test
software decision paths only and are not scientific observations.
The independently written driver is preserved as
`code/check_P2_summary.py`, with repository-relative source lookup and
disposable temporary input directories. I reran its final preserved
version from repository root with
`python topics/padua-mz-sharp-constants-20261106/code/check_P2_summary.py`;
its identity and all ten case results are in that receipt. No synthetic
input replaces a scientific receipt.

## Actual independent small rerun

Executed from /workspace/sharp-work:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python topics/padua-mz-sharp-constants-20261106/code/P2_modes.py validate --output topics/padua-mz-sharp-constants-20261106/evidence/check-P2-independent-validation.json
```

Exit 0. Both m=12 and m=13 pass. All error fields are bit-identical to
the developer receipt, with largest diagnostic difference
5.355850311861143e-15. The total recorded CPU time is about 0.01872 s.
The receipt includes exact source/input identities, seed, tolerances,
Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0 and one-thread settings.

This was an actual distinct execution of the inspected validation code.
Its dense comparison uses separately implemented Chebyshev weights and
literal scalar-node L assembly, while sharing the inherited basis
tables. It is not described as a wholly independent new numerical
implementation. I did not rerun calibration, m400 or any main case.

The remaining uncertainty is floating numerical accuracy and the
unexecuted main test, not a theorem proved by small-case agreement.
Future main receipts and their final summary need an outcome check.
Focused Claude audit, publication and registry decisions remain separate.
