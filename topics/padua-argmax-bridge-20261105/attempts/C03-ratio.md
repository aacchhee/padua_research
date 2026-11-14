# C03 — ratio tightness attempt

Rules 4b728b0; 2026-11-06. Own new C03 theory/idea/attempt records only;
no Git, shared files, old source/proof changes, subagents or cover runs.

Preregistration and refreshed novelty gate:
[ideas/C03-ratio.md](../ideas/C03-ratio.md). Classification is backend
tightness variant, including reuse of C01's already stated centered
Taylor formula. Any distinct review precedes consequential replay.

Analytic proof and exact enclosure contract are being written before
arithmetic controls or implementation. First controls explicitly include
the numerator zero, the removable zero, k=1, negative residuals, turn
parity and rejection outside the admitted chart.

## First freeze, before any executable control

`theory/C03-ratio-tightness.md` SHA-256:
`8634fc469f18a9555032c140b9969a56a74c53dea388cadd54c29ed2b3e83a01`.
Preregistration SHA-256:
`026eb4f40ebcefba4fee8d35fc0083d1f8d5340922462f693320263f73ce60e9`.

Developer result is PROVED, pending distinct review. The positive-chart
derivative is strictly negative for k>=2 and r>0 with r<=3/2, kr<=4.
Before pi this uses the decrease of t cot t; at pi it uses the uncancelled
derivative; after pi the inequalities kr-pi<pi/3 and
kr*cot(kr)>pi/sqrt(3)>1 give the reversed logarithmic factor while the
ratio itself is negative. This proves exact endpoint-image ordering,
without assuming a positive ratio or dividing by its numerator at zero.

Logical controls resolved in writing before implementation:

* k=1 is exactly constant; r=0 has zero derivative.
* kr=pi is treated directly and has negative positive-side derivative.
* Negative r reverses derivative sign but preserves value before parity.
* Negative odd turns and even k give eps=-1, reversing both orientations.
* A crossing residual interval includes the extremum eps*k; it has no
  uniform one-sided derivative sign.
* Outside the chart, R3 is increasing at r=2, so unrestricted monotonicity
  would be false. No such extrapolation is used.

The midpoint formula is explicitly C01's existing optional Taylor rule,
not new theory. The ODE curvature candidate is optional and rejects any
sine-zero interval. Exact dyadic center selection plus an outward radius
is required; a rounded center cannot reuse an unadjusted half-width.

The frozen spec was sent to root and the prototype owner with explicit
notice that root controls release after independent review. No C03
executable, arithmetic test, selected box, full case, fit or cover was
run by this owner; diagnostic CPU charged is zero. Point evaluation must
be nonrecursive, and the current quotient-success early return must not
silently bypass intended tightness candidates. Actual S/orbit recovery
on root0/path0101 is unmeasured here.
