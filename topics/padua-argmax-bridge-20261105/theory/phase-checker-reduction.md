# Independent phase-checker verification and reduction

Rules/input: `3dda890275a7599caa707b0fb8c0b6e6f6a80643`.
Developer: Codex, assigned Sol medium; runtime metadata is not independently
exposed. No ID requested. This verifies/implements inherited PD-T364;
novelty gate is the campaign baseline and N3 gate, not a new mechanism.

**Status:** OPEN for a checked full phase certificate. Bounded software
checks are MEASURED. The routine derivations below are supplied for separate
mathematical/source inspection; their presentation is not self-approval.
No new degree, corner radius, or PD-T099 status is claimed.

## Independent arithmetic and polynomial

`../code/phase_checker/arb_kernel.cpp` uses FLINT 3.1.3 Arb real balls at
160-bit working precision. Its operations and trigonometric calls do not
import, copy or link the producer's interval kernel. FLINT internally uses
GMP/MPFR, but the interval algorithm is Arb's ball arithmetic, independently
of the producer's directed-MPFR endpoint arithmetic. The compiled library
links FLINT, GMP and its ordinary runtime dependencies only.

The primitive uses PD-T364's finite identity

    G(u,v) = R_(n+1)((u+v)/2) R_(n+1)((u-v)/2)
           + R_n((u+v)/2) R_n((u-v)/2) - cos(nu).

It evaluates the different, denominator-free finite polynomial

    R_k(z) = [k odd] + 2 sum_{1<=j<k, j=k-1 mod 2} cos(jz),
    R'_k(z) = -2 sum_{1<=j<k, j=k-1 mod 2} j sin(jz).

These follow by pairing positive/negative frequencies in
sum_{ell=0}^{k-1} exp(i(k-1-2ell)z). They hold at every real z, including
all quotient collisions. In particular R_k(ell*pi)=k*(-1)^((k-1)ell).
No rounded collision detection, singular quotient, or numerical sign
pattern is used. Each harmonic is passed directly to Arb sin/cos; this
avoids an interval recurrence with uncontrolled dependency growth.

Write s=(u+v)/2, t=(u-v)/2. Compute

    D_s = R'_(n+1)(s) R_(n+1)(t) + R'_n(s) R_n(t),
    D_t = R_(n+1)(s) R'_(n+1)(t) + R_n(s) R'_n(t).

Since u=(r*pi+alpha)/n, v=(s_index*pi+beta)/(n+1), the phase derivatives
are ((D_s+D_t)/2+n*sin(nu))/n and ((D_s-D_t)/2)/(n+1).
Arb evaluates pi outward, and integer factors/divisors are exact at the
supported n<=512. The triangular-polynomial diagnostics in controls.py
use a different D_n sum, including exceptional coefficient 1 at (n,0).

## Nonsmooth whole-sum enclosure

Let B be a closed rectangle, c its exact midpoint, r_a,r_b its exact
half-widths. For finitely many C1 functions h_i on a neighborhood of B,
let H_i enclose h_i(B), A_i and B_i enclose their coordinate derivatives,
and C_i enclose h_i(c). Define

    D(H,A) = A if H is strictly positive;
             -A if H is strictly negative;
             [-supabs(A),supabs(A)] otherwise.

Then, with F=sum_i |h_i|,

    sup_B F <= sum_i supabs(C_i)
               + r_a supabs(sum_i D(H_i,A_i))
               + r_b supabs(sum_i D(H_i,B_i)).

To verify: for x in B, let z(t)=c+t(x-c). Each h_i(z(t)) is C1, and its
absolute value is absolutely continuous. At almost every t where it is
nonzero the chain derivative is sign(h_i) times the smooth derivative.
At a zero, whenever the chain derivative of the absolute value exists,
it belongs to the symmetric hull of that smooth chain derivative.
Equivalently the one-dimensional Lipschitz chain inequality supplies
that hull. Thus the derivative along this segment belongs almost
everywhere to

    (x_a-c_a) sum_i D(H_i,A_i)
      + (x_b-c_b) sum_i D(H_i,B_i).

Integrating gives the bound. The finite sum can be interchanged with
the a.e. derivative and integral. This retains cancellations between
signed derivative intervals of different nonzero terms. When a term's
range contains zero, the symmetric coordinate hull is conservative even
if its two derivative coordinates cannot independently attain extrema.
An identically zero term has zero actual derivative and is also safe.
Take the minimum with the independently valid natural bound
sum_i supabs(H_i). No derivative of a discontinuous sign function is used.

In code, c and r are Arb arithmetic on the exact binary64 endpoints:
(B(lo)+B(hi))/2 and (B(hi)-B(lo))/2. They are not rounded binary64 centers
paired with an insufficient half-width. The interval center evaluation
therefore contains the exact midpoint required by the derivation.

For S the terms are H_rs on the full odd board and normalization is
1/(2N). For the corner orbit they are
H_rs+H_-r,s+H_r,-s+H_-r,-s, with normalization 1/(8N).
All four values, center values, and coordinate derivatives are added
before the absolute-value/sign-hull operation. PD-T364's endpoint
multiplicity proof applies unchanged; there is no endpoint omission or
absolute value applied before orbit summation.

## All-center defect and admissibility

For each K=0,...,n+1 and J=0,...,n, compute the PD-T364 projected profiles
by natural interval evaluation of d(x,y)=|x|+|y|-|x+y|, normalized 1/(4N).
Their lower bounds may be negative; clipping each final profile lower
bound against zero is safe because the exact profile is nonnegative.
Then take the minimum, over every odd noncorner physical center, of
max(0, lower(Q_v(K)), lower(Q_h(J))). No representative-center sampling
is used. Integer reflections wrap on the periodic board and leave the
phase offsets unchanged.

A center at J=0 is omitted only if alpha_hi<0; at J=n only if
alpha_lo>0; analogously for K endpoints. Omitting these centers is
justified by the corresponding inward physical phase sign. Retaining
other centers, even when their precise physical/diamond intersection
is empty, only decreases the uniform lower bound. The checker therefore
does not need a delicate boundary intersection test. It excludes actual
corner centers from this minimum and handles them separately.

As a separate inherited predicate, n>=48 and the exact rational inequality
maxabs(alpha)+maxabs(beta)<=1/10 permit lower defect 1/8192 by PD-T366.
This is a full-box test in unscaled phase units.

## Geometry, strictness and accepted predicates

The checker independently validates outward pi and Lc constants against
its own Arb result. The four closed roots are exactly the quadrant
rectangles with outer endpoint +/-pi_hi. Their union contains the phase
diamond. A path reconstructs the producer's declared binary64 longest-side
bisection and rounded midpoint operation order; the two children share
that very midpoint. Stagnant splits are rejected. Prefix overlap,
duplicate leaves, uncovered siblings and absent roots are rejected.
Pending regions participate in the partition check but forbid acceptance.

Outside is accepted only when exact rational minabs(alpha)+minabs(beta)
exceeds the independent outward pi upper endpoint. Corner constants and
strict inequalities use exact Fraction conversions of binary64 bounds;
no rounding of the final subtraction can turn equality into strictness.

A far leaf needs own S_upper<own Lc_lower. A nonlocal leaf needs both
own corner_upper<own Lc_lower and own S_upper-own defect_lower<own
Lc_lower. A local leaf substitutes inherited corner descent for the
first of those inequalities. Its only current corner predicate is

    a²/(2n²)+b²/(2(n+1)²)
      <= max(1/(2[n(n+1)]³), 1/(10^11 n²)),

where a,b are maximum absolute endpoint phases. It is exact rational;
1-cos(t)<=t²/2 bounds physical corner distance, so PD-T251 or PD-T369
applies within its own domain. This preserves strictness for every
physical point except the actual two nonnode corners. No fixed positive
margin is imposed at the equality points. A proposed new kappa is not
implemented or accepted.

On a complete accepted partition, every odd-center representation is
handled: noncorner centers by defect/far comparison, and actual corner
centers by the orbit/local comparison. PD-T364 then gives the claimed
physical-square conclusion. An incomplete partition or bounded sample
replay yields no such conclusion.

## Present limits

Supplied numeric leaf-bound fields are diagnostic and intentionally
ignored. The checker recomputes its own leaf predicates; it does not
certify the producer's particular enclosure numbers. Mutating an ignored
number is therefore not a meaningful corruption control. Geometry,
constants, tree coverage, predicate changes, false outside and false
local-radius controls are executed instead.

The finite polynomial costs O(n) direct trigonometric calls per board
term, hence O(n³) work per board. Full projected profiles also cost
O(n³) arithmetic. There is no measured O(n²) claim. Full phase covers
and new degrees are unexecuted. Independent source/math inspection,
a different-agent replay, and any larger corner-patch proof remain
requirements before a consequential computer-proof claim.

## Authorized finite-instance extension and provenance follow-up

The original checkpoint above used inherited radii only. After the corrected
independent corner replay and parent authorization at published c000899,
the implementation additionally accepts the **fixed** degrees {33,64,128}
under the separately published finite-instance theorem in
`N3-corner-bounds.md` and analytic `N3-corner-radius-reduction.md`.
The premise is frozen corrected receipt
573afc5d5ae229b0fa1d47df9b6bf334e47e0e437288a3543826838e5403cb4b,
whose checker source is 3646f4e8b6b16957b9e1114f95ad2f0a7c18eec4687b49d5e6f1947a25eea6e3.
Every source pin is verified, using the exact c000899 historical prose when
the current status paragraph differs. No supplied candidate field selects,
widens or asserts success of this mathematical premise.

The guard requires maxabs(alpha),maxabs(beta)<=1/128 and checks exactly

    a²/2 + n² b²/[2(n+1)²] <= 1/12500.

Dividing by n² supplies the physical-distance bound required by that
finite-instance theorem. Equality in this geometric guard is allowed,
while strict descent away from H=0 is supplied by the theorem. Defect
comparison remains strict; only the two actual nonnode corners retain
equality. Neither the fixed guard nor any metadata converts a partial
cover into a complete certificate. A possible future common bound at
other degrees is not implemented or assumed.

For source/input provenance, revised `check.py` consumes one immutable
candidate byte snapshot and `build_snapshot.py` always constructs a fresh
library in a unique directory. The receipt pins the exact source snapshot,
preprocessed translation unit, flags/toolchain, header closure, runtime
closure, loaded mappings and binary. Source/closure stability checks reject
changes observed during build/replay. This repairs the original R1
provenance defect; it is independent of the mathematical enclosure lemma.
The unchanged Arb kernel remains subject to separate source/math review.

Actual full-overlap test: the complete outward n17 tree was replayed over
all1288leaves, yielding364failed enclosure predicates and acceptancefalse.
The finite polynomial remains a valid but insufficient enclosure on those
broad boxes; no finite degree is proved by this run. See
`../evidence/phase-checker-full-n17.json` for pinned input/output identities.
Any stronger formula/refinement is a subsequent implementation change that
requires its own review; it is not silently inherited from this reduction.

## 2026-11-06 implementation-status addendum

The prototype OPEN status above is historical. The original complete n17
candidate now passes all1288 predicates on the independently reviewed
round5 hybrid Arb kernel, with no tree change and actual exit0. See
[N3 n17 disposition](N3-phase-n17.md) and its committed short acceptance
receipt. The routine reduction/derivative/equality derivations above are
unchanged; quotient/global intersections are separately reviewed in
../independent-checks-phase-round5.md. This validates one known-degree
instance, not higher-degree throughput or all-n coverage.
