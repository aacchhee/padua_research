# PD-T?padua-3d-codex-T9-06 — refined finite Lebesgue samples

ID kind: PD-T. Aliases: T9-MAX; T9-LOCALDET. Split from: none.
Split into: none.

## Statement / assumptions / status

Overall status: MEASURED. The frozen binary64 procedure in
preregistration-T9.md produced the following refined lower samples for
the specified total-degree node sets on[-1,1]³. These numbers are neither
upper bounds nor certified global maxima, and prove no asymptotic law.

| n | QR approximate Fekete | discrete-Leja lower set |
|---|---:|---:|
|4|11.263055|19.689122|
|5|14.077221|26.610086|
|6|22.508222|40.335643|
|7|27.643157|49.973900|
|8|45.564648|80.474687|
|9|45.194828|86.520078|
|10|66.720286|99.967716|
|11|81.746878|125.826153|
|12|117.738030|181.478650|

Leja-height Padua stacks n4–7 give18.61089895,34.00730862,
45.11601950,51.98712439. The frozen n4 cyclic(1,15,19)/69
control gives37.52145653. All lose to QR at the matching degrees.
Local determinant ascent controls n2,3,4 give3.859363921,6.390025526,
11.46325063; no claim of global Fekete optimality. The n4 determinant
control has a higher sampled Lebesgue value than its QR starting control.

## Definitions / dependencies

Same inherited deterministic nodes and tie choices as T2/T4; real
Chebyshev-product basis indexed by total degree. Operator Lebesgue values
are computed as sum of absolute cardinal values. Two nested angular
meshes21³→41³ and twelve local starts are specified in the preregistration.
Sources are hashed in evidence/t9-maxima.json. No exact-rank result is
silently inherited for these fresh floating node computations.

## Checks and evidence

Command actually run:
`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-3d-20261106/code/t9_maxima.py`

All26 frozen cases completed, none suppressed, none unrun. Maximum
condition number134.215; maximum residual||VV^{-1}−I||∞<5.82×10^-13.
The refined maximum exceeded its21³ sample by as much as7.30055%
(QR,n10), so historical mesh values should be read as lower samples.
All values passed the nested-mesh guard. L-BFGS-B supplies no global
exclusion; finite angular boundary starts can terminate at stationary points.

Log-response SSE over the nine degrees4–12:

| Family | log¹ | log² | log³ | log⁴ | constrained power | power exponent |
|---|---:|---:|---:|---:|---:|---:|
| QR |2.95690|1.44270|.537246|.240536|.118437|2.12237|
| Leja |2.36565|1.02095|.285001|.157792|.0665634|1.96491|

These are descriptive fits, using fixed log powers and a fitted exponent
α≥1, exactly as frozen. Both power fits have lower SSE than every tested
polylog model; this does not establish polynomial growth. The T2 D2
promising test is not met: Leja/stack/cyclic do not win the finite QR
comparison, and fresh exact unisolvence has not been established here.

## Scope / open items / history

Candidate disposition: bounded measurement continuation completed; no
competitive new family selected. There is no negative theorem about
all lower-set, lattice or Lissajous families. Global certification, larger
degrees and new competitors require a fresh preregistration and budget.
Raw nodes and full stdout in/tmp/t9-* are regeneration-only; small receipts
and producer code suffice to reproduce these measurements. Source records
and the inherited T4 failure remain unchanged. 2026-11-06 Codex; source
and receipt hashes identify final runnable version. Independent checks are
recorded separately by the coordinator, not claimed by this producer.
