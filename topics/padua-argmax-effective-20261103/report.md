# Effective Padua argmax campaign — development report

Rules/input `8a1f394739293953e1566fd24a0a193cc78ff26f`; base `440d107`.
Branch `codex/padua-argmax-effective-20261103`; [draft PR19](https://github.com/aacchhee/padua_research/pull/19).
Claude [audit-01](audit-01.md) accepts the mathematics at the stated scopes; the [developer response](response-01.md) to minor record findings awaits the Claude response protocol check.

The exact finite global range now reaches **2<=n<=32**, with the new
cases17–32 in the [finite theorem](theory/argmax-effective-codex-01-finite-global-argmax.md).
The isolated n40 producer completed352 leaves (286.38CPU seconds), but
its corrected independent checker reached the authorized600CPU-second
limit without an acceptance receipt. Degree40 is **not certified** here;
this is a capacity checkpoint, not a mathematical counterexample or a
rejected certificate. Degrees33–39 were not run.

The all-degree global conjecture PD-T099 remains **OPEN**. No effective
global threshold n0 and no counterexample were obtained. The principal
analytic advance is an exact corner-active spectrum giving, for every
n>=2, both normalized inward slopes

    A_n,B_n <= -n^2 Lambda_c/8.

It also gives strict descent on the explicit physical neighborhood
0<h_x+h_y<=1/(2[n(n+1)]^3). This closes the all-degree slope premise of
IDEA-330/PD-T227. It does not close the weighted-energy premise or the
fixed scaled phase neighborhood needed by the proposed global assembly.
See [spectrum](theory/argmax-effective-codex-06-corner-active-spectrum.md)
and [slopes and radius](theory/argmax-effective-codex-06-uniform-slopes-local-radius.md).
The supplementary independent reviewer reconstructed these proofs; the
required Claude audit remains separate.

## Gate outcomes

| Gate | Outcome and scope |
|---|---|
| G0 | PASS: fresh independent Python production/checking17–24, identical mathematical payloads to canonical native certificates, and actual independent native acceptance. Finite continuation17–32 also accepted. |
| G1 | Separate C/GMP producer and C++/GMP checker implement the exact 192-bit arithmetic. Measured timing fits and speedups are in the producer receipt/attempt; extrapolations are capacity estimates, not certified degrees. |
| G2 | MEASURED local K decreases from about .2893 at n17 to .2215 at n1000; no continuous remainder bound follows. |
| G3 | MEASURED sampled primitive constant about1.594 at n17 and1.454 at n200; sampled far margins positive. |
| G4 | MEASURED3458 centers and25365 offsets. Full odd-center sets at n17,18,24,25; sampled classes beyond. Not exhaustive continuous or all-degree control. |
| G5 | Not evaluable: no uniform remainder E(n), phase zones, noncorner defect d(n) and far margin f(n) have been proved with explicit constants. Original factor-two/10-times-capacity kill criterion preserved, not triggered. |
| G6 | No reversal in1536 floating E-C comparisons n13–60. Three whole-cell comparisons at n13,17,24 proved exactly with positive rational margins. The all-n E-C route survives but is unresolved. |
| G7 | Original unspecified envelope class makes its universal kill criterion ill-defined. The dated precise G7-F variant is refuted analytically at n4; this does not kill every envelope or IDEA-319. |
| G8 | Bounded source reading and access gaps recorded. No one-dimensional theorem is transferred into any proof. |

The numerical detail, diagnostics and sample limitations are in
[gate measurements](theory/argmax-effective-codex-02-gate-measurements.md),
[comparison screen](theory/argmax-effective-codex-03-comparison-screen.md),
[exact comparisons](theory/argmax-effective-codex-03-exact-edge-spots.md),
[n4 obstruction](theory/argmax-effective-codex-04-coarse-cell-sign-obstruction.md),
and [source reading](literature-g8.md). Floating maxima/minima in these
records are finite sampled extrema, never universal bounds.

## Measured capacity and its limits

Fresh full native-driver CPU runs, including cold compilation and output,
used2.1284s at17 and13.9374s at24, against25.3967s and161.6771s for the
Python constructor/search: about11.93x and11.60x. The Python boundary
omits final output compression/write, so this comparison charges the
native implementation extra work. Separate hot-path fits must not be
mistaken for full-driver times.

The native producer-plus-independent-checker CPU sums at17 and24 are
7.138904s and48.715504s. Their two-point power fit has exponent5.5691
and projects cumulative production and one replay for degrees17..N to
N=61 in24h or82 in7days. These use the corrected canonical-rational checker. The Python producer-only two-point exponent is
5.3677, with cumulative projections51 and70; Python checker CPU was not
measured, so those are not complete Python certification-pipeline budgets.
The Python full-pipeline n_cert was not measured: G1 is answered only for
the native port and Python producer-only, and is partly unanswered for
the reference pipeline.
The broader native hot-path fit, including the isolated40 probe, has
exponent about5.8264 and producer-only projections70 and94.

These are heuristic **MEASURED cost extrapolations**, not proved or
validated n_cert. Sparse-fit uncertainty, fixed192-bit enclosure growth,
memory and the implementation's n<=100 cap all remain constraints.
Single-degree projections in the receipt are separate from cumulative
bridge costs. None supplies the missing G5 remainder model or an n0,
and the pre-registered factor-two/10-times-capacity decision rule has
not been silently replaced by these fit values.

## Route decisions and remaining obligations

- **R1:** retained, deferred. Explicit uniform primitive excess and
  noncorner cancellation margins are needed before a numerical n0 can be
  derived. Fitting the sampled true constants does not supply them.
- **R2:** retained, deferred. An exact fixed-index near field plus a
  uniform logarithmically graded tail is needed before a parameter
  interval h=1/n can certify infinitely many degrees.
- **R3:** retained finite comparisons. The exact three-instance result
  adds useful cases, but does not prove a general phase-alignment or
  interior-to-boundary comparison. No exact reversal occurred.
- **R4:** precise fixed-sign individual-cardinal factorization rejected
  by the n4 analytic obstruction. Regrouped or sign-changing envelopes
  survive; the broad class remains unspecified.
- **R5:** bounded round complete, no new mechanism. Requiring every
  sign-polynomial Bernstein coefficient to lie below the corner value
  is algebraically equivalent to the current coefficientwise l1 test.
  This is a variant/duplicate of IDEA-320, not a new negative theorem.
- **R6:** retained analytic advance. Both all-degree normalized slopes
  are proved and an n^-6 physical radius is explicit. Separate scoped
  obstructions refute complete spectral positivity and uniform per-cardinal
  affine sign preservation; neither refutes actual-cardinal sign stability. Reaching the
  required n^-2 physical scale needs aggregate sign-change/remainder
  control, such as the still-open weighted-energy estimate.

Attempt and idea records retain the earlier targets and explain each
scope reduction. No historical priority or globally novel method is
claimed. The independent native arithmetic implementations improve
finite capacity; they do not change the PD-T210 certificate implication.

Final inspection found noncanonical GMP rational operands in the checker.
The corrected kernel canonicalizes every transform-weight summand before
arithmetic. All23,816 weights at2–40 matched independent Fraction values,
and every new finite case17–32 was fully replayed with the corrected kernel.
The36 malformed controls also passed after correction. Earlier native
receipts are explicitly historical and do not supply the final proof
premises. See [the correction review](independent-checks-canonical.md) and the
[recorded build provenance limits](checker-provenance-01.md).

## Evidence, reservations and audit

Small essential certificates and acceptance receipts are committed under
`evidence/`; [evidence-manifest.json](evidence-manifest.json) pins their
bytes and the source files. Bulk regenerable measurements remain outside
Git, with inventory and pending delivery disclosed in
[COLD_STORAGE.md](COLD_STORAGE.md) and [cold-storage.json](cold-storage.json).
No third-party fulltext or external-machine computation is included.

Permanent reservations were first pushed in `ed8db2fc364d0ba34c3c06815460b3b2971787b5`:
PD-T246–265, PD-N084–091, IDEA336–355, LIT466–473. Provisional aliases
remain until audit and final registration; unused reservations stay gaps.
Shared ledgers and earlier records were not edited. Proposed dated
updates are in [proposed-record-changes.md](proposed-record-changes.md).

The completed [audit-01](audit-01.md) records its full read coverage and
independent analytic and certificate checks. The response now awaits a
Claude protocol check before final registration. Preserve the distinction between the proved slope bound,
the smaller radius, finite global cases, sampled gates and the still-open
all-degree global maximum problem.
