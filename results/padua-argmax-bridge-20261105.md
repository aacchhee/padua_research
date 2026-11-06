# Padua argmax bridge — current research results

## Fresh campaign checkpoint — 2026-11-06

The independently checked global tail is now **n>=ceil(exp(10^7))**
([proof](../topics/padua-argmax-bridge-20261105/theory/C03-effective-argmax.md),
[review](../topics/padua-argmax-bridge-20261105/independent-checks-C03-effective.md)). The exact finite range
remains2–40; the intervening gap is OPEN. C06 separately proves strict
far comparison for log n>=256; C05 proves strict actual-corner comparison
for log n>=25. Their global assembly is in progress, rather than already
counted as an accepted global theorem.

More substantially, C05 closes the **actual near NONCORNER comparison
for every n>=10^6**, with gap869/28000, using the unchanged fixed model
and the stronger all-class defect. [Finite-h proof](../topics/padua-argmax-bridge-20261105/theory/C05-finiteh-model-comparison.md)
and [independent review](../topics/padua-argmax-bridge-20261105/independent-checks-C05-finiteh.md). The model
bound needed here is1/32. Original tight C1 with1/4096 remains OPEN;
the limiting residual estimate alone is not a finite-degree proof.

The first cheap whole n32 replay **failed76/364 leaves**, in31.965CPU-s;
this failure is preserved. The new C03 endpoint-monotonicity refinement
has passed separate mathematical/source controls, and its mode0 whole
replay controller has now passed distinct review. One full original-case
run is pending publication/release; no new degree is claimed. The C02
MPFR port is experimental and failed one of two saved tightness cases;
no complete producer ran. The independently checked C06 partial-cotangent
backend is a useful fixed-work component (76 cases,784 exact moment
checks in2.69CPU-s), but full point-S and whole-box interfaces remain OPEN.

Formal Claude audit remains PENDING; PR27 stays draft WORK. Historical
checkpoints below retain earlier outcomes and are superseded by this dated
checkpoint where thresholds or OPEN obligations have changed.


The exact global corner-argmax range is **2–40**. Small complete
certificates33–40 and separate exact C++/GMP checks prove the maximum
and exact two-nonnode-corner equality set.
[Finite theorem](../topics/padua-argmax-bridge-20261105/theory/native-finite-range.md).
Fresh C01 proves an actual effective analytic upper boundary
**N0=ceil(exp(10^12))**: every n>=N0 has exactly those two maximizers.
[Effective tail](../topics/padua-argmax-bridge-20261105/theory/C01-effective-argmax.md),
[independent reconstruction](../topics/padua-argmax-bridge-20261105/independent-checks-C01-effective.md).
All-degree **PD-T099 remains OPEN** on the intervening41<=n<N0. This
bound is astronomical; it does not make a practical finite bridge.

**Finite-dimensional near-phase model.** The degree-growing sums are now
removed on rho=|alpha|+|beta|<=1/2. For every n>=10^6, the explicit
fixed-count model satisfies |S_n-M_near|<3/14000<1/4096.
[Model](../topics/padua-argmax-bridge-20261105/theory/N1-round6-near-model.md),
[independent review](../topics/padua-argmax-bridge-20261105/independent-checks-n1-round6.md).
This is an approximation-validity threshold, not an argmax onset. The
one authorized correction is used; earlier proofs and the obstruction
to the unchanged reported error bound are preserved.

Round7 proves both exact logarithmic coefficients are below the corner
coefficients by explicit quadratic phase gaps. The remaining bounded
residual still needs a small phase-increment bound; the full comparison
remains OPEN.
[Coefficient theorem](../topics/padua-argmax-bridge-20261105/theory/N1-round7-coefficients.md),
[residual target](../topics/padua-argmax-bridge-20261105/theory/N1-round7-comparison.md).
Round8 bounds all branch artifacts by9/(2n), leaving a continuous
phase-increment comparison with more than1/40000 tolerance. The
continuous modulus, including possible fractional/entropy terms, is OPEN.
[Branch helper](../topics/padua-argmax-bridge-20261105/theory/N1-round8-jumps.md),
[remaining target](../topics/padua-argmax-bridge-20261105/theory/N1-round8-modulus.md).

**Actual-lambda deficit.** For n>=64, all interior complementary vertical
edge centers and inward rho<=1/2, lambda<S_n-1/2048.
[Two-phase defect](../topics/padua-argmax-bridge-20261105/theory/N5-two-phase-defect.md).
Combining it with the new model gives lambda<M_near-1/4096 on that
class for n>=10^6. The model condition M_near<=Lambda_c+1/4096 would
therefore prove strict corner comparison there; that uniform condition
is still OPEN.
[Comparison criterion](../topics/padua-argmax-bridge-20261105/theory/near-edge-model-criterion.md).

**Independent outward certifier.** Complete phase covers at known
degrees17/24/32 pass the separate Arb path, with zero failed/pending
regions. Matched24/32 use1020/992 leaves and202.07/382.57checkerCPU-s.
[Calibration](../topics/padua-argmax-bridge-20261105/theory/N3-outward-overlap-r6.md).
This validates the method; it adds no degree or all-n complexity law.
The earlier failed whole replay and experimental NaN finding are retained.

**Corner bootstrap.** A proved maximum-absorption reduction eliminates
the need for a prior global/corner norm ratio under an explicit energy
premise. That premise W<=(3/4)n^4Lambda_c is now independently verified
for every n2–128. It supplies half-phase corner patches for the
explicit finite cover below. All-degree complement coverage and the
intermediate energy range remain OPEN.
[Reduction](../topics/padua-argmax-bridge-20261105/theory/N3-bootstrap-corner.md),
[finite energy](../topics/padua-argmax-bridge-20261105/theory/N3-bootstrap-finite.md).
The earlier pointwise phase-square1/128 local patch remains separate.

A separately reviewed analytic bound gives
W_n<=n^4[(21/32)Lambda_c+1.5e9(1+log(n+1))] for n>=32, hence the
same3/4 premise when log n>=128000000000. The enormous energy onset
does not establish an argmax onset or close the intermediate energy range.
[Energy bound](../topics/padua-argmax-bridge-20261105/theory/N3-uniform-energy-r8.md).

The explicit maximum-bootstrap certificate mode has passed independent
source/math review and controls. One known n32 producer completes364leaves
in222.813CPU-s. The first full replay on the old Arb backend rejected
20of364bootstrap predicates with insufficient projected-defect enclosures,
in136.175CPU-s. That failed receipt is preserved; it was not a
mathematical counterexample.
[Cover reduction](../topics/padua-argmax-bridge-20261105/theory/N3-bootstrap-cover-r8.md).
The separately reviewed round9 Arb pair-defect refinement accepts the
same364-leaf candidate,0failed/0pending,139.405totalcheckerCPU-s. The
first failed receipt is preserved; no producer rerun/tree change. This
accepted known n32 case costs about2.8times less combined CPU than
round6, without a higher-degree scaling claim.
[Accepted replay](../topics/padua-argmax-bridge-20261105/independent-checks-phase-r9-n32.md).

Other retained results include exact full-phase cotangent rows, uniform
shifted-cotangent block error and scoped transport/trace obstructions.
The stronger N5 quarter-defect target stays OPEN; only its preregistered
phase-blind certificate was disproved by a strict limiting bound.
[Obstruction](../topics/padua-argmax-bridge-20261105/theory/N5-large-budget.md).
No unread external theorem or historical priority claim is transferred.

Next: validated model evaluation/maximum comparison, far phases and
remaining center classes/corner coherence; gate any higher-degree cost
assessment after the accepted bootstrap calibration. No B3 PASS,
practical meeting onset or B4/Syvert release. Required Claude audit remains pending.
AC permits10MB total generated outputs for now and directs major cleanup
to a separate topic; see the canonical LOG instruction.

**Fresh research campaign C01.** An all-center analytic defect>1/2048
now holds for n>=64,rho<=1/2, including both parities and orientations.
Fixed-work ratio/derivative charts and an independently reviewed cheap
Arb prototype remove harmonic loops and skip justified profile scans.
Bounded n128 timing falls24.120 to1.136CPU-s; full known-case validation
is pending, with no extra degree or higher-degree complexity claim.
[Allclass defect](../topics/padua-argmax-bridge-20261105/theory/C01-allclass-defect.md),
[ratio charts](../topics/padua-argmax-bridge-20261105/theory/C01-ratio-enclosures.md).

A sharp central fractional upper and actual nonzero axis coefficient are
proved; the pure-quadratic/vanishing-cusp modulus is specifically ruled
out. Full sharp near Q comparison still needs its other coupled parts.
[Central bound](../topics/padua-argmax-bridge-20261105/theory/C01-near-central-upper.md),
[axis limit](../topics/padua-argmax-bridge-20261105/theory/C01-near-axis-limit.md).

AC authorizes15fresh coordinated rounds; C01 is complete and C02/C03
continue without an early handoff. No legacy degree-extension campaign.
