# MZ cleanup — development report

Branch `codex/padua-mz-cleanup-20261105`, [draft PR26](https://github.com/aacchhee/padua_research/pull/26).
Rules/input ad503cb0603fc017444b0aa732240981eefa4d24; source/base
21dbfc90257b952d8923f6d01739d12aa8d6e0a1. Current main aff30e8ad5542c94fab642ae024dc9aab4fa7ad7
was merged without conflicts in ef9723b. Rules did not change. Codex
development: user-requested gpt-6.1-sol xhigh; supplementary mathematical
reviews: distinct gpt-6-astra high. Claude [audit-01](audit-01.md) accepted the mathematics, finite reduction
and measured scopes without a correctness finding. Editorial/provenance
dispositions are in [response-01](response-01.md); final registration is recorded in [preparation](preparation/record.md).

## Outcomes and exact scope

| Target | Development result | Durable record |
|---|---|---|
| C1 | **PROVED, computer-assisted:** actual signed forms are indefinite at m1101,1240,1600. Each has an exact dyadic polynomial, positive exact continuous norm, and strictly negative producer and alternate-arithmetic enclosures. | [Finite theorem](theory/finite-indefiniteness.md), PD-T376 |
| C2 | **PROVED:** odd-m fixed-node logarithmic weights have the same signs and constants as the even case. Odd-m y carriers extend both spectral divergences and the sharp half-degree ratio classification to all integers. | [Odd weights](theory/odd-weight-asymptotic.md), [odd carriers](theory/odd-carriers.md), PD-T377/378 |
| C3 | **PROVED:** exact continuous carrier norms and one-sided logarithmic spectral bounds. Sharp spectral limits remain **OPEN**. | [Normalized bounds](theory/growth-carrier-bounds.md), PD-T379 |
| C4 | Expanded manuscript builds cleanly to **25 A4 pages**, with accepted PR23 results and clearly labeled cleanup development results. | [Section/change/build record](manuscript-changes.md) |
| C5 | Prior PR14/23 inventories retained; final C1 package locally staged and verified; literal shared-record replacements prepared. Actual delivery remains **PENDING**. | [Storage](COLD_STORAGE.md), [proposals](proposed-record-changes.md) |
| C6 | Optional one-dimensional round not run; PD-T027 remains **OPEN**. | [Disposition](attempts/C6.md) |

Final preparation assigns PD-T376–381 and IDEA466–471 from reservation
ee49035, whose permanent ranges remain T376–391/N138–145/IDEA466–489,
no LIT. Four new theory results are PROVED, PD-T380 is MEASURED and
PD-T381 remains OPEN. Historical WORK/AUDIT records retain their aliases. [Union scan](allocation-scan.json)
and [reservation](ALLOCATIONS.md) preserve earlier parallel reservations.

## Finite certificates and measured crossing

The committed producer uses exact integer tensor contractions, outward
Arb-certified node tables, the exact signed weight formula and a proved
global energy-error bound. The independent worker uses new certified
tables and floating tensor contractions with explicit forward-error
bounds under its documented IEEE/BLAS arithmetic model. Neither path
uses an eigenvalue approximation as a premise. The exact nonzero
Legendre coefficient array has degree at most m-1 and a positive exact
rational continuous norm. Together with Q_m(1)=4, a negative energy
therefore proves indefiniteness.

| m | Rigorous trial-Rayleigh lower bound | Upper bound |
|---|---|---|
| 1101 | -35067/10^6 | -35066/10^6 |
| 1240 | -273/10^7 | -270/10^7 |
| 1600 | -23415/10^6 | -23414/10^6 |

These are bounds on explicit trial quotients, not brackets for minimum
eigenvalues. The m1600 float vector reproduces the PR23 SHA exactly.
Small producer/checker receipts, source hashes and witness identities
are committed. Large coefficient arrays and exact norm files are staged
locally with identities and regenerating commands, pending delivery.

Every even integer1230..1240 was scanned, along with coarse even probes
1100,1200,1280,1400. The largest scanned positive float minimum is
0.00012076189285820084 at 1238; the next even degree1240 has
-0.000027148072763036893. The local measured even crossing window
is thus1238–1240. The smallest even degree **certified negative in this
campaign** is 1240. No earlier positivity, global first crossing or
spectral monotonicity is proved. Odd probes1101,1201,1241,1281,1401,1601
are all negative; only1101 has a separately certified odd witness.
The odd first crossing is not located.

## Parity completion and growth normalization

At odd m the exceptional integrated x mode vanishes. Repeating the
floor-half triangular tail argument gives the same fixed-index limit
m^4 w_jk/log m -> -16 e_j e_k (-1)^j and an explicit whole-grid
majorant. The even mesh is now m+1 in y, so the negative cosine or
positive sine-product carrier belongs in y. Exact parity selection,
the total-degree budget and dominated convergence yield both signed
energy limits. Hence lambda_minus tends to minus infinity and
lambda_plus to plus infinity on all integers, at the endpoint and
at every fixed ratio theta>1/2. Exactness still gives identity at
theta<=1/2.

The handoff's raw extrema1/9 and 1/36 are correct suprema of unnormalized
sampled-energy coefficients. They are not spectral constants. Exact
continuous envelope/carrier norm limits supply the missing denominator.
The resulting rigorous bounds are

    limsup lambda_minus(m,m-1)/log m <= -c_minus,
    liminf lambda_plus(m,m-1)/log m >= c_plus,
    c_minus = 1/[9 A J_minus(1/4)],
    c_plus = 1/[36 A J_plus(1/8)].

Here c_minus ≈ 0.02962182360 and c_plus ≈ 0.01277888644. Rounded
display values do not define the inequalities; the exact formulas do.

Their exact logarithmic formulas, not the display decimals, define the
constants. No matching opposite bound, optimal normalized parameters,
sharp spectral coefficient or existence of either spectral limit is claimed.

The completed predeclared K2 fit compares windows800/1000/1200/1600 and
1600/2000/2400/3000 by least squares in log m. Final measured values,
fit slopes-0.0915300430 and-0.0921215962 (a movement toward raw-1/9)
are recorded in
[measurement record](theory/finite-measurements.md) and
[small summary](evidence/scan-summary.json). Movement toward raw-1/9
is a diagnostic observation only, after the normalization caveat.

## Gates, independent checks and manuscript

K0 PASS: float m800 agrees within3e-17 and a fresh exact m60 producer
accepted the recorded strict endpoints. K1 PASS: m400 fixed-point
producer3.375s and alternate checker1.89s, with relative widths below
2.54e-9 and 5.854e-8 respectively. K2 was preregistered before any
m>1600 execution. Gates and actual receipts are in [gates](gates.md).
No killed or unexecuted gate is relabeled a successful mathematical result.

[Supplementary C2/C3 reconstruction](independent-checks-math.md) passed,
including distinct small-m moment solves, exact parity identities and
rational continuous-norm checks. [Supplementary finite review](independent-checks-finite-astra.md)
passed the reduction/error bounds, reran both m60 paths, and separately
verified the three large artifact identities and rational bracket
implications. It did not rerun the large tensors. [Independent witness runs](independent-checks-witness.md)
actually did execute those alternate large arithmetic paths. Shared
FLINT/Arb dependencies and the independent checker's IEEE/BLAS assumption
are explicit. These supplementary reviews preceded the completed Claude audit-01.

The manuscript retains the exact compression and adds weight asymptotics,
both carriers, the sharp signed threshold, the uniform C-to-L2 bound,
odd parity, normalized one-sided bounds, and the three finite witnesses.
The abstract/introduction/open-problem list and scope/history pointers
are updated. No unmerged PR21 citation, historical priority sentence or
provisional ID is introduced. refs.bib is unchanged. The 25-page final
build has no warning, error, unresolved-reference or layout markers;
its source/PDF hashes and actual commands are in manuscript-changes.md.
The PDF remains outside Git and the preserved earlier PDFs are untouched.

## Artifact delivery and remaining work

The verified local C1 package is 159,265,962 bytes, SHA-256
`ac6a628153746729688851baa3aa50f41dc31509d9ce4058dc221fb0550982b1`,
with 71 members and its off-repository full inventory. It includes final
witnesses/norms and a dated scan/vector snapshot. The completed final scan supplement is 44,618,351 bytes, SHA-256
`257fa21a83b5bb74b93483e371efcc87cf5e0ac965bb32fab2ddfadd808bc338`;
it is separately recorded and verified in the storage manifest.
PR14 and PR23 historical pending deliveries retain their original
identities/provenance; nothing is claimed recovered or delivered merely
because an old scratch locator exists. See COLD_STORAGE.md for AC's
Padua-specific destination, sizes and hashes. No external machine used.

Claude Opus 5.5 audit-01 accepted the scientific scopes; response-01
addresses every minor/editorial finding. Final-ID assignment and scoped
shared registration now use the checked original reservation; completed preparation
verification and independent protocol PASS are recorded separately in
[the preparation record](preparation/record.md). Only AC merges.

## Candidate records and remaining mathematical frontier

The three primary completion/normalization candidates are IDEA-467
(odd weights), IDEA-468 (odd carriers) and IDEA-469 (continuous norm
limits). IDEA-466 retains the finite certifier variant, IDEA-470 the
deferred full-signed localization route, and IDEA-471 the abandoned
raw-slope interpretation. The [full candidate record](novelty-gate-math.md)
preserves all original comparisons, dispositions and timing qualifications;
the [crosswalk](../../ID_CROSSWALK.md) preserves every provisional alias.
No new mechanism or historical-priority claim is added by registration.

PD-T381 keeps the original sharp spectral-limit target OPEN. PD-T379's
proved normalized one-sided bounds remain separate support, not a proved
conjunct or a PARTIAL resolution. Global first crossings, opposite-direction
sharp logarithmic estimates, optimal normalized packet parameters and
PD-T027 remain separate unresolved questions. Completed registration and
build tasks are retained in the preparation record instead of the frontier.

## Preparation outcome

Final registration and validation are complete. The independent Astra
medium [protocol review](preparation/protocol-check-01.md) passes with no
unresolved finding; all nine refreshed-head integration rehearsals pass.
The source/receipt identities, other topics' results/registries and AC's
owner line are preserved. PR26 is ready for AC review; assigned agent work
is complete. Only AC decides whether to squash-merge this PR. No other
branch, mathematical OPEN target, delivery or novelty status is closed.
