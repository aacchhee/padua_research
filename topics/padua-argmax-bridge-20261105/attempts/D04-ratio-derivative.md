# D04 — Ratio-derivative duplicate gate and existing-source adoption contract

Rules/input2db4a226dad798491be3ec2fe5ce0238e21cfaec;2026-11-06.
Codex parent-assigned Sol xhigh, serving metadata unexposed. This bounded
analytical inspection follows the [fresh gate](../ideas/D04-ratio-derivative.md).
No mathematical or native diagnostic was executed, no old file changed,
and the running D03 pilot/source freeze remains untouched.

## Decision

The mathematical request is an exact duplicate of the already accepted
[C01 ratio contract](../theory/C01-ratio-enclosures.md), with existing
[C03 tightness refinements](../theory/C03-ratio-tightness.md).
Consolidate there; no D04 theory file or new result ID is warranted.
The useful remaining task is a separately reviewed adoption/integration
choice, not derivation of another removable-pole formula.

## 1. Exact source issue and its limit

In code/n3_meanvalue.c,rp(k,x) switches to a k-term trigonometric sum
when minabs(sin x)<.02 or interval width>.1. Its kernel calls rp four
times for the two degrees at s=(u+v)/2,t=(u-v)/2. Since n3_box visits
2n(n+1) odd-board entries, this introduces a potential cubic factor in
its derivative evaluation count. This is a read-only source count, not
a measured assertion about which branch dominates the current pilot.

The later projected Q_v/Q_h loops each scan that board for every center,
also producing cubic arithmetic if reached. Removing rp's loop alone
does not remove those scans, change a whole-box predicate, or prove
practical certifier throughput. The source identifies itself as a float
diagnostic, not a directed-rounding certifier.

## 2. Accepted algebraic value-and-derivative contract

Here U_k follows the task's indexing sin(kx)/sin x; in standard
Chebyshev notation it is U_(k-1)(cos x). The finite continuation is

    U_k(x)=sum_(j=0)^(k-1)cos((k-1-2j)x).

For an exact integer ell, x=ell*pi+r and
eps=(-1)^(ell(k-1)), equivalently eps=-1 exactly for odd ell/even k,

    U_k(x)=eps*k*sinc(kr)/sinc(r),
    U'_k(x)=eps*k*[k*sinc'(kr)*sinc(r)
                          -sinc(kr)*sinc'(r)]/sinc(r)^2.     (1)

Both identities include negative turns and r=0; the exact collision pair
is(eps*k,0). k=1 is identically(1,0). No division by sinc(kr) occurs,
so the first numerator zero and negative lobe are retained.

Given an arbitrary finite real interval Z, form A=Z-ell*Pi outward,
with Pi enclosing exact pi. An approximate midpoint may propose ell,
but ell must be stored exactly. Literal chart guards are

    sup|A|<=3/2, k*sup|A|<=4.                              (2)

On this complete residual interval,sinc(r)>=5/8. C01 supplies fixed
polynomials P_J,D_J for sinc and its derivative, with whole-interval
remainders

    |sinc(x)-P_J(x)|<=|x|^(2J+2)/(2J+3)!,
    |sinc'(x)-D_J(x)|<=(2J+2)|x|^(2J+1)/(2J+3)!.

J32 and |x|<=4 give fixed remainder bounds for both A and kA. These
are truncation errors; outward polynomial arithmetic still contributes
its own radius and the derivative scales with k^2. No fixed-precision
accuracy or guard-admission promise is assumed.

When a validated sin(Z) excludes zero, the separated whole-interval
candidate is

    sin(kZ)/sin Z,
    [k*cos(kZ)*sin Z-sin(kZ)*cos Z]/sin^2 Z.              (3)

The sine square must be outward and separated from zero. Neither(1)
nor(3) substitutes a point value for a ball. Candidate value/derivative
pairs are staged before intersection; nonfinite optional pairs leave
the old finite pair intact, while finite contradictions are errors.

If both charts fail, the closed global pair[-k,k] and
[-floor(k^2/2),floor(k^2/2)] is valid for every finite interval,
including multiple poles. This supplies total bounded scalar work,
but no useful width guarantee. C01 already states the local caps from
C2=k(k^2-1)/3 and the corrected true pole-crossing root geometry for
phase widths P<16/5. Literal rounded guards remain mandatory.

C03's accepted quality refinements go beyond relying on that fallback:
U_k is even and strictly decreasing in |r| on the admitted chart,
including kr=pi and pi<kr<=4. Its whole folded value image therefore
comes from two guarded endpoints. Derivative signs are clipped on a
one-sided residual. Optional centered Taylor uses one nonrecursive
base point jet and C2; an optional sine-separated ODE curvature bound
uses U''=(1-k^2)U-2cot(x)U'. A sine-zero interval rejects the ODE
candidate rather than dividing through its removable point. These
steps and their limitations are already proved and reviewed in C03.

At fixed order/precision the formulas use bounded scalar work with no
degree-sized frequency sum. Integer length, transcendental argument
reduction and precision costs remain explicit. This is not uniform
constant bit time in k or a license to extend a finite native API.

## 3. Existing sources: what can actually be adopted

| source | existing ratio role | exact limitation |
|---|---|---|
|cheap_C03/prototype.cpp|Arb C01 base plus C03 modes0/1/2; reviewed value and derivative|native n2..512,k1..513; no automatic all-degree/throughput extension|
|cheap_C02_mpfr/producer.c,c02_interval.h|independent fixed J32 value/derivative pair; no harmonic fallback|earlier base chart lacks C03 folded-endpoint tightening; historical controls are not a new adoption review|
|cheap_C08_mpfr/producer.c,c08_interval.h|reviewed MPFR C03 endpoint mode0, nonrecursive endpoint calls and one-sided derivative signs|native n2..512,k1..513, fixed directed-endpoint arithmetic assumptions; no modes1/2|
|cheap_rows_C11/partial.cpp|fixed J16 cotangent partial sum, plus fixed K32/L16/WD96 corrections|its w' is a regularized cotangent derivative, not a whole-phase U'_k API|
|cheap_rows_C11/point.cpp|retained/direct finiteF uses exact rational-turn value sinc ratios|point-only row assembly; it does not supply a whole-ball derivative contract|
|cheap_rows_C12_box/box.cpp|ratio12 encloses whole-ball U_k, with quotient/sinc/endpoints and finite fallback|value-only; exposed S-upper API has no gradients/orbit/defect|
|cheap_rows_C15_global/global.cpp|reuses C12 ratios for special/direct actual terms|same value-only limitation; coherent vertex logic is a separate whole-S upper construction|

The C01 mathematical review accepts the total guarded contract, including
the corrected root-width addendum. C03's independent mathematical and
source reviews accept modes0/1/2 within their stated scopes. Its frozen
mode0 subsequently accepted the unchanged known-n32 candidate; this is
historical bounded evidence, not a D04 rerun or new-degree result.

The strongest direct MPFR ancestor is C08, not a fresh extension of C02.
Its independent source review explicitly reads the inherited C02 code
and states that those old controls alone were not source acceptance.
The final reviewed C08 producer is
270eb7b0f073efcb996c7c832f6e946d37b0e6f780fdac63fc66591332560a5e;
its unchanged header is
275936b502180f2d92af94eb2138815114ba75afb9c258cadffa44e580be0a03.
Arb C03's reviewed source is
9e357b25efde553211563bb69147644c67b7752bc703bf05ac502141c82e0861.
These are reported review identities, not newly executed source tests.

## 4. Existing analytic profile skip and the concrete integration gap

C08 producer line38 already skips projected profiles when n>=64 and
the entire signed box satisfies max|alpha|+max|beta|<=1/2, returning
the old analytic defect1/2048. Its exact-dyadic directed radius test
is in full_half_radius; a caller Boolean is not its proof. C03 Arb's
collector has the same old tier. Outside the guard, all-center cubic
profiles remain available, so no overall quadratic-cost theorem follows.

The existing C02 dense-band theorem permits prospectively stronger
fixed tiers on the same radius domain:

    1/64 for n>=64,
    1/32 for n>=160,
    1/16 for n>=4096.

The native C08/C03 cap remains512, so the4096 tier is not an executable
adoption within that unchanged range. No cap extension is proposed.
The physical theorem also requires an admissible odd center J+K odd,
theta=(J*pi+alpha)/n,phi=(K*pi+beta)/(n+1) in[0,pi], with the center
not an actual nonnode corner. Each available interior projection gives
its stated floor; at a noncorner center at least one is available.
Actual corner patches need their separate corner-orbit/local comparison.
The consumer must preserve this distinction; no uniform positive defect
at the actual corner is asserted.

Thus a sensible later integration gate would combine the existing
reviewed fixed-work C08 or Arb C03 component with the stronger proved
C02 tier, retain exact whole-box radius/physical-center guards, and
review the changed collector/consumer scope. It should measure useful
box bounds and cost, rather than treating a new trivial degree as its
objective. This inspection establishes neither the cost of that
combination nor recovery of a particular near-only pilot box.

The current D03 pilot remains on its frozen source5264178; no changed-
source rerun, producer, native control, quadrature or implementation is
authorized or performed by this D04 record. Adoption is **DEFERRED** to
the coordinator after the current pilot and a separate concrete gate.
The mathematical D04 candidate itself is **EQUIVALENT/consolidated**,
not OPEN mathematics and not a failed theorem. No new theory file or
PD-N is created.
