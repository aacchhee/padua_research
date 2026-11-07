# C10 Arb640 moment replacement — independent check

2026-11-06. Input head
`547a473a6e1c1268ff4f1ada7243b12afb02d0bc`. Rules were read by this
reviewer at `e8fad1671fb736247e4c510284f6f935e6345efb` and are unchanged
at the supplied input. Distinct Codex supplementary reviewer, assigned
Astra high; serving model/effort metadata independently unexposed.
Formal Claude audit remains separate.

**ACCEPTED within the existing successful-call C06/C07 contracts on the
recorded LP64 target. No unresolved enclosure finding.** The changed
moment implementation encloses the same exact recurrence, retaining
all recurrence rounding and the existing input-radius extension. The
point assembly is unchanged except for its source include. This accepts
the implementation replacement; it does not establish total success,
whole-box/gradient/corner/defect integration, a certified degree, a
general speedup law or production throughput.

Read the prospective C10 attempt, all four C10 code/control files,
C09/C10 receipts, snapshot builder, and the source diffs against frozen
C06/C07. This reviewer previously reconstructed C02/C06/C07 and their
accepted interfaces. The work is a numerical implementation substitution
with no new mathematical mechanism, historical novelty or priority claim;
a fresh full registry/literature gate is outside this review's scope.
No author, shared, prior-review or Git state was changed.

## Frozen identity and scope of the change

| File in code/cheap_rows_C10 | SHA256 |
| --- | --- |
| partial.cpp | `209fa24300219884b97ce267e898b085593534d97ecc31640909c4c772061ac5` |
| point.cpp | `6e2f1920ca293ac5a34f01c6369d94345b0d0c9b8a03d3e58ef15d453fbcf1d9` |
| controls.cpp | `72a66e861a0c7bb2dbc7b9573f70e8c8b3a7e9eacfa55eec41959cfecb65c8c8` |
| control.py | `ab3fdfbefba57c135ed4f9e11eb2dc4713b4733be42a61793d542d0d60dac127` |

A complete source diff against C06 shows only its introductory comment
and moments() changed. Coefficient construction, J48/K32/L16/WD96,
smooth/harmonic/derivative remainders, guards, final assembly, interfaces
and their explicit160-bit operations remain byte-identical. The exact
identity and its analytic error budget are therefore the accepted C06
dependencies, not fresh approximations chosen from the timing results.

The C10 point source is exactly the accepted C07 source after replacing
its one C06 include with `#include "partial.cpp"`. The independent driver
asserted that bytewise relation before and after execution. There is no
changed root selector, parity, normalization, finite primitive, epsilon,
coefficient branch, direct-set limit or source-level fallback.

Old exact-rational code occurs inside namespace Old only in the author's
controls.cpp, with renamed C exports. It serves diagnostics and the one
micro-profile. Neither production moments/partial nor pointS refers to
Old; a failed new computation cannot silently select the old algorithm.
The remaining Q arithmetic supports exact phase/turn handling and bounded
diagnostics. It is not a hidden rational-moment production branch.

## Recurrence and precision reconstruction

Let ym be the exact Arb input midpoint, s=1/n, and

    left=(ym-1/2)/n-1/2,
    right=(ym+q-1/2)/n-1/2.

`arb_set_arf(ym,arb_midref(y))` copies that midpoint exactly, including
when the caller supplies more than640 midpoint bits. It does not round
to160 first. All subsequent inexact operations that form s,left,right
take explicit MP=640. Integer B constructors, assignments, arb_one and
power-of-two scaling are exact operations; their lack of an MP argument
does not introduce a160-bit rounding path.

The local lp/rp vectors enclose powers of left/right through degree98;
hp encloses half-step powers through97. All power recurrences use
`arb_mul(...,MP)`. These arrays are freshly constructed for each call,
so no n,q or input-dependent quantity can leak across calls through a
cache. Their dimensions cover every d+1 and k access for d<=97.

Starting from exact work[0]=q, the same accepted identity is evaluated:

    M_d=(right^(d+1)-left^(d+1))/((d+1)s)
        -sum_even k>=2 binom(d,k)(s/2)^k M_(d-k)/(k+1).

Every subtraction, denominator formation, division, binomial update,
half-step product and earlier-moment product explicitly takes MP=640.
No overloaded B addition, subtraction, multiplication, division or power
occurs in that uncertain recurrence. The binomial loop includes the
correct factor(d-k+1)/k before each even-k correction. All work entries
are balls, including any cancellation uncertainty; prior work is never
replaced by its midpoint. Interval inclusion therefore encloses the
exact recurrence inductively, independently of whether640 bits happens
to make the resulting radius useful.

`arb_set_round(out[d],work[d],160)` rounds the entire ball outward. It
does not extract the640-bit midpoint or drop the old radius. The sole
new input-extension charge is then the unchanged

    d*q*2^(1-d)*rad(y)/n.

The strict pole-domain guards ensure every normalized sample has
absolute value<1/2 throughout y, so the accepted mean-value bound
applies to the full input ball. Converting its magnitude radius to an
Arb midpoint is exact; the subsequent160-bit B operations give an
outward error bound. This uncertainty is added once to out[d], while
work[d] remains the enclosure for the exact midpoint only. Thus input
uncertainty is neither omitted nor repeatedly propagated through the
moment recurrence. M0=q is exact and independent of y.

All changed loops are bounded by the fixed degree97/98, not by q or n.
The existing C06 native guards and finiteness/exception behavior remain
in force. On LP64 the reviewed integer arithmetic bounds are unchanged;
there is no new native product of large n and q in this replacement.

## Independent executed controls

Executed once:

    python topics/padua-argmax-bridge-20261105/code/cheap_rows_C10_review/control.py

Exit0, **PASS**, 2.084498 parent-plus-child CPU seconds including fresh
compilation, below the30-second allocation. Python3.12.14; g++14,
Debian14.2.0-19, x86-64 LP64. No random inputs or seed.

The reviewer translation unit includes the frozen production C10 point
source and therefore its actual new partial implementation. It does not
include the author's controls.cpp or the old rational backend. Its
native partial tests comprise11 complete512-bit direct cotangent
endpoint-hull containments, six invalid-input failures with nonfinite
native output, and one q=0 exact-zero result for NaN y as permitted by
the unconditional empty-block contract.

Partial cases cover n=2,3,7,64 and the maximum supported2147483647,
both poles, a1e-60 left-pole input, nonzero-radius balls, removable
cell endpoints and q=31,32,33 around the harmonic transition. Since
the cotangent sum decreases in y on the guarded domain, the independently
computed endpoint hull encloses the full image of each tested input
ball. No large-q reference loop was run at the maximum n; those cases
use a singleton block.

The1218 exact rational moment comparisons check midpoint and both exact
ball endpoints. Four independent interval cases exercise degrees0..97:
(n,q)=(3,3),(11,5),(5,1),(2147483647,1). They use distinct offsets and
radii, including a right-side interval at the maximum n, so the checks
are not restricted to a symmetric y=1/2 midpoint. A fifth input is
formed from1/3 at1024-bit precision with n7,q2 and degrees0..13. This
checks that midpoint information beyond640 bits is enclosed rather
than silently truncated before recurrence evaluation. Each reference
is a direct exact-rational sum of sample powers, not the old recurrence.
Endpoint comparisons are finite diagnostics; validity over the entire
interval follows from the derivative extension reconstructed above.

Small receipt `evidence/c10-review-rows.json` pins the reviewer source,
driver, builder, compiler/binary and local raw manifest
`c10-review-rows/check-3dfq5ha3/review.json`,49750 bytes, SHA256
`4f6c172cc1d1712b033d309fe4a0963f89514111105bb6f50e633814ac977c8d`.
The raw record contains all case outputs and196 source/header identities,
four compiler tools,13 tool dependencies, eight linked dependencies and
eight actually mapped runtime dependencies. Source/preprocessed/toolchain
identities are checked through the build; loaded identities match
before/after execution. All four C10 source hashes also match
before/after. Large artifacts remain local/regenerable, with physical
archival transfer pending and no remote retrieval claim.

Separately, a recursive byte-size/SHA256 check verified264 identity
records in the developer receipt and raw manifest. The developer receipt
is5372 bytes, SHA256
`1b77cca35c6d48a0dcde029ad2125faf87f19801c9ddb3c3f044b1761f9239e6`.
This is identity verification, not a rerun of the developer's suite.

## Measured cost claims and limits

Reading the preserved C09/C10 receipts confirms the n32 and n128 calls
use the same rational phases1/12,1/16 and report identical binary64
endpoints, full-radius diagnostics and all six row counters. Those
observations support the developer's finite comparison. They are not
an equality proof for all Arb output bits or every possible input.

The recorded C10 native times0.161941s/0.687725s and prior C09 helper
times2.776525s/11.546109s have different scopes: C10 runs after library
loading/primitive initialization, whereas C09 helper timing includes
load/closure overhead. The attempt expressly discloses this, and no
precise general speedup factor is approved here. Its micro-profile's
new0.0 value is timer resolution, not zero cost. The simple y=1/2
micro-input does not establish that rational moments dominate every
point call. No timing or large reference-board replay was needed for
this focused validity review.

**NOTE — inherited comments.** The unchanged text immediately above Q
still says “Exact rational moment construction,” and point.cpp's first
comment still says frozen C06 is included unchanged. Those are inherited
comments, not an accurate description of the new moment implementation.
The new moments comments, source diff and attempt correctly specify
Arb640 enclosure followed by outward160-bit rounding. This wording does
not affect the reviewed computation; no author file was edited.

Acceptance preserves all C06/C07 limitations: possible numerical failure,
wide valid enclosures, fixed-order tails and input conditioning, LP64
domain bounds and separate bit complexity. C08 is an analytic whole-box
contract, not an implemented capability of this point source. No
gradient, corner-orbit, projected-defect or production cover interface
is added by this backend replacement.
