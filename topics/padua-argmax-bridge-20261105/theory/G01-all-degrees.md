# G01 — Exact two-corner Padua argmax for every degree n>=2

Provisional ID: PD-T?argmax-bridge-codex-G01. Split from: PD-T099 (all
degree cases assembled here). Final-ID assignment and shared registration
are deferred to PR preparation. No new mechanism or novelty claim.

## Statement and convention

For every integer n>=2, for the original corrected Padua interpolation
cardinals on [-1,1]^2,

    max lambda_n = Lambda_c(n) = lambda_n(-1,-1),
    argmax lambda_n = {(-1,-1),(1,-1)} if n is even,
                     {(-1,-1),(-1,1)} if n is odd.

The convention is PD-T101: nodes (cos(j*pi/n),cos(k*pi/(n+1))) with
0<=j<=n, 0<=k<=n+1, j+k even, total interpolation degree <=n. The
exceptional highest first-coordinate coefficient is ONE. The inequality
is strict at every other point of the closed square. Lambda_c is the true
symbolic corner value; a computed lower bound is never substituted for it.
No assertion is made for n=0 or n=1.

## Status

**PROVED, computer-assisted**, under the named accepted mathematical and
trusted implementation dependencies below. The actual complete return and
both prescribed fresh native checks passed distinct technical review.
This mathematical development status does not supply the final Claude
audit, shared-registry application or PR readiness.

## Proof by exhaustive degree decomposition

1. The inherited accepted finite results cover n=2..40: PD-T209 (2),
   PD-T162/166/169/174/177 (3..7), PD-T181 (8), PD-T214 (9..16),
   PD-T246 (17..32), and the [native finite extension](native-finite-range.md)
   (33..40), using its own PD-T210/Bernstein reduction. Their canonical
   links and completed audits remain in PROOF_STATUS.md; the
   [finite-base inventory](../../../results/padua-argmax-bridge-20261105.md)
   records this topic's applications.
2. The actual Syvert compact return contains every integer n=41..319,
   plus control511. Its 280 primary/fresh pairs include all273 previously
   missing degrees and the seven controls41,42,63,64,159,160,511. The
   trusted local checker reconstructs every returned primary AND fresh
   certificate using exact rational arithmetic. These are closed finite
   covers of the continuum, not samples of the Lebesgue function.
3. [E14](E14-assembly320.md), with its
   [distinct complete mathematical acceptance](../independent-checks-E14-global320.md),
   proves the exact displayed equality set for every integer n>=320.

Thus the finite cases2..319 and analytic tail320..infinity partition every
integer in the statement. For each returned degree41..319, the accepted D32/D29
physical signed chart, exact defect floors, outward point bounds and
squared Peano enclosure exclude the complement. Strict actual-corner
patches exclude every point except the two corner origins. The engine's
analytic branches use E12 only from256 and E15 only from192. Closed seams,
axes, endpoints, node and collision values retain the original reductions.
D14's global GRID norm or D19's complete numerical TREE norm supplies the
required norm premise. Any analytic far leaf forces GRID, since a partly
numerical tree cannot supply the complete TREE norm.
Parity reflection preserves the node set/cardinals and equates the two
corner values. Continuity on the compact square yields the attained
maximum. Neither a finite search nor numerical agreement supplies this
argument; its dependencies are the accepted finite-reduction theorems.

## Computer-assisted dependencies and verification boundary

The finite proof depends on the released
[final hybrid engine](../code/final_hybrid_engine/SPEC.md), its
[source/result acceptance](../independent-checks-final-hybrid-engine.md),
and unchanged scientific FREEZE SHA256
0d9ce0a5dbb7fb37cf1a05f07040b72d046b61b8d36b6a5a8bf137eb7d9914eb.
The production source is996fedcad4ba79a28e45a3fe3678adc12f1e5358;
runtime manifest SHA256
5b89fa66e742952497f99a49110a965ada2828b1861917268d3074af0eb22a16.
PD-T271 remains a named computer-assisted dependency of the analytic
constants/branches; the separate analytic scalar H maximum does not remove
that dependency. The Arb/GMP/MPFR arithmetic implementation, captured
compatible runtime, finite-polynomial collision formulas, compiler/native
interfaces and exact-rational checker remain trusted implementation inputs.

Primary and retained-witness fresh verification executed separately on
Syvert for all280pairs. The collector validated every full history there.
Locally, all560 essential certificates/accounts/exits/source links are
checked, but only the two randomly selected residual degrees199,238 have
their full histories independently inspected and fresh native replays
executed and independently reviewed. This is not an independent local native rerun of all273degrees,
an independent arithmetic implementation, or a statistical proof of the
unsampled numerical premises. Those premises retain their explicit trust
in the released outward arithmetic and server-side fresh verification.

AC explicitly accepts selective retention: unsampled full histories stay
on Syvert; not all certificates require cold storage. The compact return
retains every essential proof and both sampled full closures. Durable
external cold-storage retrieval of the new compact return is not yet
verified; source/pins/commands permit regeneration, not byte-identical
historical timing or paths. These limits do not silently become missing
degree cases or an assumption that all unsampled raw histories were read
in the sandbox.

## Evidence, limitations and next step

Actual archive36,045,486B, SHA256
b00fd57f85ce6d96a6c1fa01e2307abd815088bb8fcb28b1587657ef142b109a.
[Return record](../compact-return.md) records commands, random draw,
coverage, native replays and retention. Independent
[technical](../independent-checks-compact-return.md) and
[mathematical](../independent-checks-compact-return-math.md) checks supplement
the substantive Claude audit; they do not replace it or grant PR readiness.

This establishes no minimum analytic onset, useful asymptotic constant,
novelty/priority verdict, or F07/F10 integration. F01–F10 are separate,
completed paper-only supports. Shared PD-T099 history/status is preserved
until reviewed registry application; no earlier OPEN snapshot is rewritten.

## Dated clarification — 2026-11-08 (Claude audit-03 MINOR fix G-6)

"Both prescribed fresh native checks" above (Status section) should read
"both fresh native checks, which were executed and independently reviewed";
see [compact-return](../compact-return.md). The trusted-implementation list
above is extended by audit-03 finding G-1 (the accepted evaluator theorems
D23/C02/C06/N5 for S vertex bounds and D06/C11 for the actual lambda points)
and by G-4 (FLINT, the Python interpreter/parsing and the LP64/binary64
conventions); that extension is returned to the developer for a reviewed
update of this record and is not applied here. See [audit-03](../audit-03.md).

## Dated dependency and replay correction — 2026-11-08 (G-1–G-5, F-01)

This addendum makes the audited dependencies explicit without changing the
statement or the accepted proof above. The original finite computation uses
[D23 equation (2)](D23-cheap-backend.md), with the C02 row decomposition,
N5 partial-cotangent identities and C06 error bounds, for S vertex
enclosures. Actual lambda point enclosures use the
[D06 four-copy rows](D06-four-copy-rows.md) and the accepted C11 row
implementation identified by the engine freeze. These are mathematical
evaluator premises, in addition to outward library arithmetic. The planned
I25 checker can supply a separate direct-sum route only after its complete
run and distinct review; that work is not presumed here.

Floor provenance is D29-radius41 for 41..63, C02's 1/64 tier for 64..159,
and C02's 1/32 tier from160, with the recorded clamped band bounds.
The [auditor's degree table](../audit-03/g-assembly.md#34-degrees-41319-the-d32-phase-implication-d)
checks each domain. The finite results 2..32 have registered links;
the provisional 33..40 extension is linked directly above and was covered
by the completed [audit-01](../audit-01.md), rather than by a nonexistent
PROOF_STATUS row.

Implementation trust includes Arb/FLINT, GMP and MPFR; the C++ compiler and
native interface; the Python interpreter, integer/rational semantics and
strict JSON parsing; and the recorded LP64/binary64 conventions. The
small-degree Bernstein route separately trusts its C++/GMP checker and
Python driver. The runtime manifest and freeze identify the implementations.
The [elementary constant replacement](J02-elementary-constant-enclosure.md)
now has distinct mathematical acceptance and supplies the consumed scalar
inequalities without PD-T271; the frozen historical E12/E15/E14 records
retain their original dependencies and pins.

The later [Claude replay276](../audit-03/replay276.md), together with its
four earlier calls, natively re-executed all280 old degrees off Syvert.
All passed and matched retained fields on a non-pinned Ubuntu runtime.
This supersedes the limited local-native scope described above, while
remaining a same-engine replay rather than independent arithmetic.
External archival custody remains pending. New sandbox certificates and
their review have their own record; this addendum makes no completion claim
for that campaign.

The F03 exact identities are PROVED premises of the separate H corner
expansion, under [their split supporting record](F03-identities-support.md).
F03's original sign target remains OPEN. No claim that all F-series content
is absent from the paper's dependency chain is intended; F07/F10 are not
used in this assembly.

## Dated alternative proof assembly — 2026-11-08 (onset512)

The simpler manuscript route now combines the preserved finite results2..40,
the original280 phase-certificate pairs41..319 and511, the new191 pairs
320..510 in the [sandbox campaign](../local-onset512-summary.md), and
[J01](J01-onset512-gates.md) for every integer n>=512. These ranges cover
every integer n>=2. J01 uses the elementary [J02](J02-elementary-constant-enclosure.md)
inequalities, the uniform1/20 floor and the retained corner256 descent;
its one absolute gate also supplies the finite certificates' far192 branch.
The [distinct review](../independent-checks-onset512-response.md) accepts
the exact gate reductions, independent Fraction execution and all new
native-campaign/accounting/archive data at their explicit scopes. This
provides a second complete assembly with the same equality set and native
evaluator premises listed above. The original stronger analytic onset320
proof remains valid and preserved; no minimum-onset claim is made.

The new computation was entirely local. Its complete proof return and small
certificate-only ZIP have pinned local identities, with external custody
pending. The full I25 independent-arithmetic result is not inferred from
this native run or its eight-certificate pilot.
