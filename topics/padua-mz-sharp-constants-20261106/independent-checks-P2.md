# Independent supplementary check — P2 implementation and calibration

Rules/input: `0205690b9c4e959a28e949083e9a1808735abf4b`.
Numerical protocol publication:
`d03e74dcf94020ba26d9fae84d3ff6c5519db901`.
Reviewer: distinct Codex supplementary agent, requested `gpt-6-astra` high;
actual serving-model and effort metadata are unexposed. Date: 2026-11-06.

**Outcome:** P2's mathematical definitions, calibration implementation,
small dense validation and final finite-test disposition check out at
their stated MEASURED scope. One
summary failure-path finding was returned to the developer and fixed;
ten independently executed synthetic control-flow cases pass. No
unresolved implementation finding remains in this reviewed scope.
After measured-b2 publication and coordinator release, all four main
receipts were reviewed, m1600 was actually independently replayed, and
the fixed summary was independently replayed and recomputed. The outcome
is PASS_FINITE_TEST, with no asymptotic or certified-value inference.
The dated execution sections below distinguish the earlier pre-main
checks from that final completion.

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
implementation. At that pre-main checkpoint I did not rerun calibration,
m400 or a main case. The later actual m1600 replay is recorded below.

At that checkpoint the main test and its outcome check were still pending.
Floating numerical accuracy remains a limitation, not a theorem proved
by small-case agreement.
Focused Claude audit, publication and registry decisions remain separate.

## Actual independent main replay and final outcome (2026-11-06)

Measured b2/K stability was separately published at
`64f3b76d5f8eb149f52f296cb744d6dd45a1c708` before main release. I waited
for the producer's explicit release of its m3000 heavy-process slot;
only producer m3001 remained active when I launched this unchanged run:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 timeout 21600 python topics/padua-mz-sharp-constants-20261106/code/P2_modes.py run --m 1600 --output topics/padua-mz-sharp-constants-20261106/evidence/check-P2-independent-m1600.json
```

The actual command redirected stdout/stderr to regenerable `/tmp` logs.
Exit 0; wall time 197.76647720899928 s, CPU time 197.65640080999998 s.
Seed, tolerance, ncv, maxiter, precision and thread settings were unchanged.
All scientific row fields, source/input identities, residuals, iteration
counts and validity guards are bit-identical to the frozen producer
m1600 receipt. Only output path, timings and peak RSS differ. Producer
SHA-256 remains
`2817536e8f96cd70dcbb2725f9e8e993cdd8ae543288b71d4e57e77622d4bb01`;
independent receipt SHA-256 is
`27d1b98e99e23373b1cda5bd66af31601c6569633ff7cf8f70c325cbc05f01b2`.
This is a distinct execution of the same inspected implementation, not
an independent algorithm. I did not independently rerun the other three
main eigensolves, calibration or m400.

After all four frozen producer receipts existed, I executed:

```sh
python topics/padua-mz-sharp-constants-20261106/code/P2_summary.py --output topics/padua-mz-sharp-constants-20261106/evidence/check-P2-independent-summary.json
```

Exit 0, PASS_FINITE_TEST, no prerequisite failure or valid-row departure.
All scientific fields equal the producer summary exactly; the command's
output destination differs. Independent summary SHA-256 is
`8b662dc71b7b4a8ab56303384ecb127ea4c02c93a20fcacaeb491f25079d8b69`;
producer summary SHA-256 is
`a12aa19c6a757e7ff5392bbe386544fabe592d24e5e75af008a09833e0eee808`.
These receipts identify every calibration/main input by hash.

I also independently recomputed the guards and criteria directly from
all four rows, using 50-digit Decimal arithmetic and logarithms of the
integer m and R values, rather than the stored floating logs or the
summary implementation. The same pass follows. This recomputation
checks arithmetic/disposition of floating inputs; it does not certify
those inputs.

| Scope | Observed value | Registered test |
|---|---|---|
| All four mode-2 weights | 0.9589539148 to 0.9680259907 | >0.9 |
| All four L distances | 0.0028898546 to 0.0036209251 | <=0.005 |
| Even branch decrease per log R | 0.03844594388456076 | 0.038 +/-0.006 |
| Odd branch decrease per log R | 0.03759101681732508 | 0.038 +/-0.006 |
| Even Q-min secant per log m | -0.09212119390214092 | within 0.006 of b2 |
| Odd Q-min secant per log m | -0.09246210231483683 | within 0.006 of b2 |

All residual, orthogonality, width and gap guards pass. This supports
only the prospectively specified finite cases m=1600,1601,3000,3001.
It proves no two-term law, crossing degree, asymptotic regime or exact
value of b2. Historical K4 and its outcome remain unchanged. No new
parameter, additional degree, fit window or retry was selected from
these outcomes.

## Final integrated D-scope check

Read the coordinator's frozen closing-development sections in report.md
and results/padua-mz-sharp-constants-20261106.md after the main outcome
was integrated. No material scope mismatch was found: P2's four-case
finite pass, rate/secant values and actual single-row replay agree with
the receipts; no asymptotic or crossing law is inferred. P1 retains its
exact analytic identification and only the coarse certified enclosure;
P4 retains a lower-only endpoint claim. The P3 wording matches the
stated theorem for Pi_(N-1), Pi_N and both parities; its proof audit is
attributed to the separate P3 checkers, not reconstructed again here.
Original gates, deferred stronger claims, untouched registries and the
need for focused Claude audit remain explicit. This closes this
supplementary integration check without a readiness or merge decision.
