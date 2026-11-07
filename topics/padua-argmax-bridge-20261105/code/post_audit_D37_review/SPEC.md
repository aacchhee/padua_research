# D37 independent fixed1024 replay: preregistered specification

Rules 7a5cd42. This independently implemented scalar replay is supplementary
mathematical/result review, not the formal cross-family audit. Requested
reviewer role: Astra xhigh; actual serving model and effort are unexposed.
Parent explicitly released one independent run after the published primary
at input head ea078d27790b515e5d2d4043e2e681973d5a1345 completed once.
This specification and its source must be hashed and communicated before
the first import, execution, exact-control evaluation or scalar observation
from this independent source. No independent run has occurred at this freeze.

## Scope and immutable execution

Run exactly once, from the repository root:

    python3 topics/padua-argmax-bridge-20261105/code/post_audit_D37_review/verify.py --run-once

Only N=1024 is allowed. The whole Python process has cumulative CPU limits
soft9/hard10 seconds, including startup, imports, output and finalization.
There are no subprocesses, native/model/phase evaluations, scans, optimizer
calls or author/helper imports. Decimal, binary-float mathematical arithmetic
and transcendental libraries are absent. Floats occur only in clock/resource
metadata. Exact integer and Fraction arithmetic are the mathematical kernel.
The primary receipt is read after the independent calculation is complete.
The source and primary/helper paths in FREEZE are read only for metadata pins;
none of the pinned author/helper code is imported, selected or executed.

Exclusive creation of
local-output/argmax-bridge-20261105/post-audit-D37/independent
consumes the sole attempt before calculation. No first failure permits a
change of source, degree, parameters, precision, terms, CPU cap, inequalities
or evidence budget. The complete compact result must be strictly below16384
bytes; no pruning or splitting is allowed. A serialization/resource failure
consumes the attempt. Source/FREEZE/primary pins are checked before arithmetic,
after it and before successful completion. The process must directly return
EXIT0; a receipt alone does not establish completion. The recorded CPU value
is a before-receipt checkpoint, not a fabricated full-process measurement.

## Independent arithmetic inclusion proof

An interval is stored as two ordered integer endpoints in units of 10^-65.
Its denotation is the closed real interval [low/S,high/S], S=10^65. Conversion
of a rational a/b takes floor(a*S/b) and ceiling(a*S/b). Addition and negation
are exact in this grid. Multiplication takes the smallest and largest of all
four endpoint products, then divides outward by S. Division takes outward
rounded extrema of all four endpoint quotients after asserting the divisor
interval avoids zero. Python integer floor division and
ceildiv(a,b)=-floor(-a/b) work for either sign of b. Thus signed Ex/Ey and all
subtractions retain their signs; no positive-part replacement is introduced.
Squaring by interval multiplication is an inclusion even when an interval
straddles zero. All real radicals in this task have nonnegative arguments.

For square roots, the lower integer endpoint is isqrt(low*S), and the upper
is isqrt(high*S), incremented unless its square equals high*S. The resulting
grid endpoints enclose both exact endpoint roots without an assumed floating
sqrt or a transcendental-library rounding contract.

For log at an exact positive grid endpoint x, exact powers of two give
x=2^k*r with 1<=r<2. Put z=(r-1)/(r+1), so 0<=z<1/3. Logarithms use

    log(r) = 2 sum_{j=0}^{89} z^(2j+1)/(2j+1) + remainder,
    0 <= remainder <= 9/[4*181*3^181].

The tail follows from replacing every denominator by181 and bounding the
remaining geometric series at z=1/3:
2*z^181/[181*(1-z^2)] <= 9/[4*181*3^181]. Every partial-sum operation is an
interval inclusion, and the tail is rounded upward to the integer grid.
Log(2) is the same series at z=1/3. Multiplication by the signed integer k
uses the full interval rule, so negative k is safe. Monotonicity of log
encloses an input interval using its lower and upper endpoint evaluations.
Repeated endpoint logarithms may be cached; the cache stores already
validated inclusions and does not change the calculation or precision.

Pi uses the Machin identity 16*atan(1/5)-4*atan(1/239). Each atan is an exact
Fraction alternating sum, with respectively100 and32 terms. The interval
between its partial sum and partial sum plus the first omitted signed term
contains the true value by the alternating-series theorem. Combining the
four exact rational endpoints with the coefficient signs and rounding once
to the 65-digit grid gives the independent pi enclosure.

## Exact endpoint formulas and domains

The already accepted D37 paper/static report fixes the mathematics and all
59 scalar definitions. This source recomputes that identical set, including
the six z/Psi pairs, signed Ex/Ey, five gates and minimum_gate. The ten-degree
log is recomputed from the fixed integer1024. Three algebraic rearrangements
make the implementation less dependent on author operation order:

* Gg is collected as [7*MA*L+111/2+
  (63+log2+4logpi+7logm+16log(2m)+(3/2)gpar)/pi]/m.
* E6old is (193+21L)/n+21600/n^2, and the last mesh denominator is (2n-1)^2.
* KN=[(55/2)L+310/3]/n+4/n^2 and KW=[28L+316/3]/n+4/n^2.

These are exact identities with the frozen source/paper expressions.
The old outer Cnew, new KD35, complete actual-origin E0 and the independent
near/wide CN,KN,CW,KW remain distinct. No D31 or D33 result is used.

All16 predicates must pass: CN,KN,CW,KW,Cnew,E0,KD35 nonnegative, and
V,qNx,qNy,qBx,qBy,qLx,qLy,tail_x,tail_y strictly positive. Each Psi uses
z=(3B+sqrt(9B^2+32qk))/(8q) and Psi=B*z^3/4+k*z^2/2. The source also checks
B>=0, q>0 and k>=0 at every one of the six calls. Box calls use k=KW+1/2;
large-coordinate calls use k=KW, exactly as the fixed multiplier proof.

The33 controls are exact rational/integer statements, with the same names
and truth values as the primary. They cover fixed degree, log and T paper
bounds, near/wide coefficient sums, modulus and cubic coefficients, fixed
multiplier, cosine factors, all floor case losses, f4/H and retained-row
constants, actual-origin charges, old global endpoint/six-row counts,
outer root/cosine factor, uniform Dc and the paper tail domain. None is
pre-evaluated by this specification or a test invocation.

## Frozen acceptance and evidence

Every one of the 59 independently computed scalar intervals and pi must be
contained in its primary interval, compared using exact Fraction conversion
of the primary decimal strings. Key sets must match, and all16 domain and33
control dictionaries must be identical. Containment is supplementary
cross-check evidence; correctness of each fresh enclosure follows from the
independent arithmetic construction, not from the primary containing it.

All five independently recomputed gate lower endpoints must be positive.
The additional, preregistered strengthening is GN.lower>1/200 and all of
GB,GX,GY,GO.lower>3/100, together with Ex.upper<0 and Ey.upper<0. Failure of
any comparison, domain, control, sign or stronger margin consumes the first
attempt and is preserved without repair. All59 values, pi, all16 domains,
all33 controls, all60 containment predicates and all three margin predicates
are retained in the complete compact receipt.

The primary receipt is pinned at8965 bytes, SHA256
b893df4ec4ebb1668600783617200c7a224203bbc7d8071f76c46084f3e1d1fd.
Root reported its exact sole command returned EXIT0 in direct tool chunk
2898d0. This reviewer read the resulting JSON; it did not rerun the primary.
The own source, this SPEC and relevant code/data pins are frozen by metadata
before the own run. The prerelease review's entire29250-byte prefix, SHA256
4fadf00da570f6e6ac92cc1c21bea575003ba61dd971e8a4bce9a09fddc7eaeb,
will be preserved unchanged when the result review is appended.

If successful, this replay discharges the scalar conditions in the accepted
all-n proof for every integer n>=1024. It independently supports the near
noncorner gap1/200 and closed far gap3/100 in their stated physical domains.
D27's accepted actual-corner loss1/8 and all prior analytic/limiting-origin
dependencies remain explicit; this run does not repeat those proofs or Arb
computations. No minimal-onset, below1024, universal all-degree or literature
priority claim follows. The parent makes the final registry/adoption update.
