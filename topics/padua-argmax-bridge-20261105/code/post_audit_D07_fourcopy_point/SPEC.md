# D07 actual four-copy point prototype: source/contract freeze

**PREPARATION ONLY. No numerical library call or linked run has occurred.**
Rules/input2e4ac49fa0687a7736bc1df82c12e6483b1c7a94,2026-11-06.
Codex parent-assigned Sol medium; serving metadata unexposed. Root owns
Git/shared state. Source, complete controller and controls require distinct
review, then explicit root release before the proposed invocation.
The accepted D06 proof8eb7d781... and its review7599cbbc... supply the
point-only structural identity; this implementation is a separate gate.

## API and exact finite definition

`d07_point(long n,const char*xi_pi,const char*zeta_pi,double out[3],long counts[13])`
accepts LP64 integer n2..2048 and rational inward turns in[0,1], as base10
fraction/integer strings of at most512 bytes. The represented physical
point is(theta,phi)=(pi-pi*xi_pi,pi-pi*zeta_pi). Output is outward binary64
lower,upper and full Arb radius. Caller supplies valid output buffers.
Nonzero status invalidates outputs; production failures return NaNs.
No approximate decimal-radian interpretation or mesh exchange is used.

For every physical row r0..m=n+1 and j0..n with j+r odd, define
V=sum_(sigma,tau)G_n(pi*(xi+sigma*j/n),pi*(zeta+tau*r/m)). Actual lambda is
sum e_j*f_r*|V|/[2nm], with separate half endpoint factors. G is the
corrected finite kernel. Every direct evaluation uses accepted C11's
entire sine-ratio polynomial expression, including integer-pi removable
turns, BEFORE taking the four-copy absolute value. No off-grid rational
alias limit supplies a collision value.

Exact mesh nodes n*xi=J,m*zeta=R,J+R odd return1 by cardinality. Exact
xi=zeta=0 is the nonnode corner; accepted C11 pointS(n,0,0) gives its
lambda by the accepted S0 identity. The two shortcuts are reported.
Other points use the algorithm below, including other edges/corners.

## Ordinary row, roots, buffers and signs

Use the accepted D06 definitions epsilon=(-1)^(r+1), a=cos(pi xi),
b=sin(pi xi), A=cos(n*pi xi), E=sin(n*pi xi), eta=zeta+/-r/m,
y=cos(pi eta), k=epsilon*A*(1+y)-[cos(n*pi eta)+cos(m*pi eta)].
For each tau form

```
d_tau(c)=c²-2a*y_tau*c+y_tau²-b²
ell_tau(c)=2[(a*k_tau+epsilon*E*b*y_tau)c
                         -(k_tau*y_tau+epsilon*E*b*a)]
U=ell_+ d_-+ell_- d_+ ; W=d_+d_-
```

These are ball enclosures of the complete coefficient families at Arb160.
U degree<=3, W monic quartic. The alias equals V only at the parity
samples away from the ORIGINAL four denominator events. Exact zeta=0
reduces to2ell_+/d_+ (the tau quotients coincide). Exact xi=0 reduces
the two sigma copies to2k_tau/(c-y_tau), leaving an affine numerator
and quadratic denominator. These exact reductions avoid artificial
common factors but do not delete any original denominator event.

All exact-zero leading coefficients are trimmed. An uncertain leading
coefficient causes whole-row fallback. An exact zero polynomial requires
no numerator roots; regular samples are zero, while direct original
poles/endpoints remain. Multiple or insufficiently separated roots may
cause fallback, with no precision/order retry.

The installed FLINT acb_poly.h declares acb_poly_find_roots (roots,
polynomial,initial,maxiter,precision) and acb_poly_taylor_shift. The code
uses maxiter32,precision160; find_roots is ONLY a candidate generator.
It does not trust its count as coverage of a ball-polynomial family.
For degree d, take exact dyadic complex midpoint centers and fixed disk
radius r0=2^-60. Taylor-shift the complete coefficient balls at each
center and require, strictly and outward,

    lower|p1|*r0 > upper|p0|+sum_(j=2)^d upper|pj|*r0^j.

The strict boundary comparison gives one zero in each disk for every
polynomial in the enclosed coefficient family: homotopy from p1*h to
p(center+h) never vanishes on |h|=r0, hence preserves the one-zero
count (the standard argument-principle/Rouche step). Require all d
disks disjoint and the leading coefficient separated from zero. Fixed
degree d then gives ALL roots inside these d disks for every member.
Failure of any step falls back; an unverified Acb root list is never used.
This source-level complex root-count argument requires independent review.

A disk whose imaginary rectangle excludes0 has no real root. Otherwise
intersect its real projection with[-1,1], apply acos to exact clamped
outward endpoints separately, and map to the parity k-coordinate
(n*acos(c)/pi-delta)/2. The four ORIGINAL denominator locations are
known exact rational folded turns fold(xi+/-eta_tau), also mapped to k.
They remain events even if U/W has a canceled common factor.

For each event interval, direct all integers from floor(lower)-1 through
ceil(upper)+1, clamped to the physical parity index range. Width>5 or
more than40 buffered samples causes whole-row fallback. All admitted
j=0,n endpoints are direct with half factors. Thus numerical buffering
can exceed D06's six mathematical direct events; its actual counts are
reported, not replaced by the theorem's ideal object count.

Remaining consecutive parity blocks are used only after every root/pole
event interval is strictly outside the whole block's sample-index span.
Evaluate U/W at its first sample and require a certified strict sign.
Complete root coverage plus excluded events makes that sign constant on
the continuous alias interval and hence on every sample in the block.
No per-cardinal affine-sign assumption is introduced.

## Eight channels, complete errors and fallback

For each ordinary signed block use exactly the eight D06 channels

```
c_tau=epsilon*E/2-k_tau/[2sin(pi eta_tau)]
d_tau=epsilon*E/2+k_tau/[2sin(pi eta_tau)]
```

at half-angle turns(xi+sigma*j/n +/- eta_tau)/2. Reverse the block for
sigma=-1, reduce its first turn modulo one using exact rational floor,
and pass its rational offset ball to unchanged C11 partial(n,q,y).
The inherited literal positive left/right pole-distance guards are
mandatory. A pole wrap or uncertain guard cannot be silently accepted.
Multiply each COMPLETE returned ball by its FULL coefficient ball;
add every returned CP640/J16 smooth, K32/L16 harmonic and WD96 derivative
remainder and all coefficient/arithmetic uncertainty. There is no old
common-S coefficient budget, discarded radius, midpoint-only partial
or external fitted correction.

Rows where either eta is an exact integer are evaluated wholly with the
finite four-copy formula; mathematically these are at most two labels.
Any other numerical root/degree/sign/pole/nonfinite candidate failure
also discards the attempted row sum and evaluates the entire row directly.
This can happen on ANY number of rows and can incur quadratic point
work. Discarded partial/direct attempts remain in work counters. A
nonfinite direct result propagates failure. No universal O(n), total
success, accuracy or cheap-certifier claim follows from bounded root count.

Counts are physical rows, eta-degenerate rows, numerical fallback rows,
root-coverage failures, sign failures, all direct four-copy evaluations
including discarded work, signed blocks, partial calls, verified root
disks, axis-reduced rows, node shortcut, S0-corner shortcut and maximum
numerical direct-buffer size. Other fallback causes contribute to the
numerical fallback total; no unclassified failure is relabeled a success
of the fast row path.

## Independent finite controls and frozen future cases

CASES.json is the exact machine input contract; SPEC is passive review
provenance. Invalid degree1/2049 and negative/over-one/malformed/zero-
denominator rational controls must fail without valid outputs.
For n2,17,32: generic xi=1/(16n),zeta=1/(32m); node xi=1/n,zeta=0;
nonnode corner xi=zeta=0. Then n128 generic with the same scaled turns.
All ten have a512-bit independent finite reference: direct corrected
Chebyshev divided differences, with derivative nU_(n-1)+mU_(m-1) at
EXACT rational-angle collisions. This reference does not use production
sine ratios, row aliases, roots or partial sums. Production must contain
the complete reference ball; the exact nodal1 shortcut may instead be
contained by the reference. A mere loose overlap is insufficient.
The reference is limited n<=128 and never a production fallback.

Finally n512 generic and its two axes (zeta0,then xi0), using the same
rational scaled turns, call the point API only. One accepted C11 S
context at n512,af=1/16,bf=1/32 may follow; it is an upper context, not
an independent actual-lambda reference or accuracy proof at large n.
No additional point, n2048 pilot, tuning or rescue is scheduled.

Generic n512 measured call CPU<=10s is the practical performance gate;
all radii and fallback counts are reported independently. Failure of this
finite gate does not refute the identity or exclude other implementations.
No comparison to D04/C08 whole-box CPU is claimed.

## Controller, resource and provenance contract

Proposed invocation, after distinct review and ROOT RELEASE ONLY:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 topics/padua-argmax-bridge-20261105/code/post_audit_D07_fourcopy_point/controller.py --run-once

Later run cap180 aggregate CPU-s INCLUDING fresh build, helpers, controls,
reference and point calls, supervisor startup and finalization. Safety
trigger170, worker175 hard limit and wall cap360s. Stop the entire run
after the first completed native call>20CPU-s; kill an unfinished call
at25 process-group CPU-s. Before another case require worker+supervisor
aggregate<160. No retries, new cases, precision changes or budget transfer.
Generic512 performance failure is recorded; the fixed axes continue only
within the stricter completed-call/resource stops. No automatic followup.

Exclusive registration/worker-entry files refuse overwrite or manual
worker reuse. Direct immutable child stdout/stderr avoid pipe deadlock.
Atomic checkpoints retain the current uncomputed call, prior complete
calls, raw output repr/first exceptions and pending cases. Registered
FREEZE identity and runtime code/data pins are checked at worker start
and exit; prose hashes are passive provenance only.

Builder is the accepted preprocessed-TU C11 builder adapted only for the
new source/include/output paths. It snapshots the full source/header,
compiler/toolchain, linked dependencies and actual loaded native closure
before/after. All raw output remains under authorized Padua local-output
`argmax-bridge-20261105/post-audit-D07/point/`. A hard stop retains the
last checkpoint and loaded-before closure without claiming an after-check.
No source/prep file grants execution authority.

## Preparation actually performed

Read full D06 proof/idea/attempt/review and C11 point/partial/attempt/source
review. Existing registry full gate is reused at unchanged SHA68bf789c...;
D07 is implementation of that accepted structural variant, not a new
novelty claim. Compilers only parsed source: syntax2 passed .483437CPU;
syntax3 failed .438618CPU due reference Chebyshev argument order;
syntax4 corrected that order against the installed header and passed
.415403CPU. Aggregate measured syntax CPU1.337458s, below30 allowance.
The initial shell meter failed127 because /usr/bin/time is absent; its
stderr is preserved. No library was linked/loaded and no polynomial,
root, partial sum, reference board or numerical diagnostic was executed.
All prospective mathematical/numerical success claims remain OPEN until
review and the separately authorized bounded run.
