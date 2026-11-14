# N3 round9 — Verification of a per-pair lower enclosure for the independent projected-defect screen

ID kind: none; implementation reduction/verification of inherited
PD-T364 and the accepted round8 cover theorem, with routine PROVED lemmas.
Aliases: interval-rectangle defect infimum; opposite-sign pair lower;
nonnegative pair clipping; independent Arb projected-profile enclosure.
Split from/into: none. No new mathematical mechanism or global ID is
allocated for an elementary formula already used by the producer.

## Statement and assumptions

For real x,y define

    d(x,y)=|x|+|y|-|x+y|.

Let X=[l,u] and Y=[s,t] be **nonempty finite closed real intervals**,
allowing zero width. Define

    delta(X,Y) = 2min(l,-t) if l>0 and t<0;
                 2min(-u,s) if u<0 and s>0;
                 0 otherwise.                                    (R)

Then

    delta(X,Y)=min_{x in X,y in Y} d(x,y)>=0.                       (1)

Consequently, if X,Y enclose two primitive values throughout a phase
box, any exact or downward-rounded scalar ell<=delta(X,Y) is a valid
lower bound for their pair defect throughout that box. Correlation
between the two values does not invalidate the bound; sharpness in(1)
concerns the **whole enclosing rectangle**, not the actual correlated
phase image.

Apply such bounds to each pair in the existing full odd-board formulas
for Q_v(K) and Q_h(J), sum them before dividing by4n(n+1), and retain
the same complete physical-center screen. This yields another valid
uniform lower bound for Delta_JK. A maximum with the old independently
valid natural lower screen remains valid and preserves the old scalar
lower bound. All certificate predicates, phase domains, finite premises
and geometry remain unchanged.

## Status and dependencies

Overall: **PROVED implementation reduction**, analytically. The scalar
identity is inherited; its routine interval minimization and preservation
proof are verified below. No changed source, numerical box or complete
round9 replay is asserted in this author record.

| Part | Status / scope |
|---|---|
| Scalar identity, sharp rectangle infimum and zero cases | PROVED routine verification, all finite nonempty closed rectangles |
| Safe directed lower-only implementation and profile/center reduction | PROVED conditional on valid outward primitive balls and directed arithmetic |
| Particular new executable correctness | Requires separate source review and actual controls |
| Acceptance of the original364-leaf n32 candidate | Not asserted; first round8 replay remains failed |

PD-T186 already states the scalar identity including zero-numerator
degeneracy. PD-T215/364 supply the full reflected-cardinal defect,
projected profiles, endpoint weights and all-center formula. The accepted
N3-bootstrap-cover-r8.md supplies the unchanged holistic sufficiency
theorem. Existing reviewed Arb finite harmonics/quotient refinements and
whole-sum value/derivative enclosures supply primitive intervals; their
formulas are not modified by this lemma. Trusted numerical components
remain Arb/FLINT, GMP, directed conversion, compiler, Python and hardware
when an actual source is used.

## Proof of the sharp rectangle bound

If x,y have the same weak sign, |x+y|=|x|+|y| and d=0. In particular
this covers every pair with x=0 or y=0. If x>=0 and y<=0, set a=x,
b=-y. Then a,b>=0 and

    d=a+b-|a-b|=2min(a,b).                            (2)

For a>=b the right side follows by subtracting a-b; for a<=b subtract
b-a. This includes a=b and either zero. Exchanging x,y covers the other
opposite-sign orientation. Thus d is always nonnegative, vanishes at
any zero argument and equals2min(|x|,|y|) for strictly opposite signs.
This is the elementary identity already used in PD-T186.

Suppose l>0 and t<0. Throughout XxY, x>=l>0 and -y>=-t>0, so(2)
gives d>=2min(l,-t). The endpoint pair x=l,y=t belongs to the closed
rectangle and attains equality. If u<0 and s>0, use x=u,y=s and the
same argument with the signs reversed, giving2min(-u,s). These statements
remain exact for degenerate positive/negative point intervals.

It remains to prove that the minimum is0 in every other case. If0 is
in X or Y, choose that zero argument and any point of the other nonempty
interval. Then d=0. If neither interval contains0, each interval lies
strictly on one side of0: l>0 or u<0, and s>0 or t<0. The two strictly
opposite combinations are exactly the two cases already handled in(R).
In the remaining combinations all points have the same sign and d=0.
This exhausts every ordered pair of nonempty closed intervals. It
explicitly includes a zero endpoint, crossing intervals, an interval
reduced to0, two zero points and same-sign degenerate points. Since a
witness is exhibited in every case, the asserted minimum is attained,
not just an infimum. Equations(R),(1) follow. QED.

## Directed Arb implementation contract

The following specifies mathematical lower bounds, not producer code.
For finite valid Arb input balls X_ball,Y_ball:

1. Certify each whole ball's sign with the independent Arb positive/
   negative predicates. Never use the midpoint sign or a positive
   floating sample to declare sign separation.
2. If the signs are strictly opposite, extract **downward** lower
   endpoints a0<=inf|X_ball| and b0<=inf|Y_ball| using Arb/ARF directed
   endpoints. Clamp each against0 if needed; nonnegativity of absolute
   values justifies this independently. Form

       ell_sign = downward(2min(max(0,a0),max(0,b0))).               (3)

   Select the minimum on exact ARF endpoints and use exact multiplication
   by2 or a directed rounding mode such as ARF_RND_FLOOR. Intermediate
   nearest-rounded binary64 conversions are unnecessary and must not
   turn a lower endpoint into an upper approximation. Clamping the final
   result against0 is safe too. If signs are not certified strictly
   opposite, set ell_sign=0.
3. The resulting scalar satisfies0<=ell_sign<=delta(X_ball,Y_ball)
   and hence ell_sign<=d(x,y) for every real pair represented by the
   balls. It may be smaller than the sharp exact expression(R) because
   the balls or extracted endpoints were rounded outward. Strictly
   positive exact balls can have a downward endpoint rounded to0; this
   conservatism is valid. Nonfinite/reversed/malformed inputs must reject
   rather than return a success value inferred from a sign test.
4. The old natural interval T=abs(X)+abs(Y)-abs(X+Y), evaluated outward,
   is another independently valid enclosure. If a_nat is its downward
   lower endpoint, then

       ell_pair=max(0,ell_sign,a_nat)                              (4)

   is a valid lower bound. Taking this maximum is optional; retaining
   the old full profile screen separately is also safe. No positive
   lower constant is invented for a sign-crossing ball.

The lower endpoint of abs(Y_ball) in the positive/negative case plays
the role of -t in(R). It is not the lower endpoint of Y itself. At
exact zero or a zero-touching ball the strict sign branch is unavailable
and the safe lower bound is0. Directed rounding must not turn an
unproved strict sign or a tiny lower endpoint into a positive claim.

A point Arb ball storing ell_pair represents a **lower-bound constant**;
it is not a two-sided enclosure of all true d values. Any accumulator
of such constants is likewise lower-only and may be used only through
its lower endpoint in the subsequent profile screen. Its upper endpoint
must not be treated as an upper bound for d or Q. This distinction is
part of the implementation contract, not an optional comment.

## Profile normalization and all-center reduction

Fix an integer n>=2, m=n+1, N=nm. On the odd board Gamma^- use exactly
the existing outward-enclosed primitive values

    H_rs=G_n((r*pi+alpha)/n,(s*pi+beta)/m),

with r modulo2n and s modulo2m. PD-T364 proves

    Q_v(K)=(1/(4N))*sum_Gamma^- d(H_rs,H_r,2K-s),
    Q_h(J)=(1/(4N))*sum_Gamma^- d(H_rs,H_2J-r,s),
    Delta_JK>=max(0,Q_v(K),Q_h(J)).                  (5)

Integer reflections retain the phase offsets alpha,beta unchanged and
preserve odd parity. The endpoint multiplicities and all reflected terms
are those of the inherited formulas; there is no extra factor2 from
opposite-sign reduction(2), since that factor is already inside ell_pair.
Each ordered board term is still counted exactly as in(5).

For every pair, enclose its two H values on the whole phase rectangle
and compute a valid ell_pair as above. For every fixed physical K or J,
outward summation of these lower constants followed by a **downward**
lower endpoint and division by the positive exact integer4N supplies

    q_v(K)<=inf_box Q_v(K), q_h(J)<=inf_box Q_h(J).                   (6)

Indeed for each phase all summands of(5) dominate their respective
constant simultaneously; adding finitely many inequalities is valid
regardless of correlations or whether the individual minima are attained
at the same phase. Downward rounding preserves the inequality. If the
positive sum/division is held in a rounded Arb ball, its lower endpoint
is used; this ball's upper endpoint does not describe the true profile.
Clipping each final lower bound against0 is safe because Q_v,Q_h>=0.

Pairs whose reflection fixes the same index have exactly d(H,H)=0.
The rectangle helper also gives0 if both identical balls have a fixed
same sign or include zero. Finite arithmetic may broaden a natural
interval around0, but(4) cannot create a positive lower bound for that
identical-value pair. Thus endpoint/fixed-pair zeros are retained without
deleting terms or changing weights.

For a phase box retain every possibly admissible odd noncorner physical
center, using the existing endpoint sign omissions only: omit J=0 only
if alpha_hi<0; J=n only if alpha_lo>0; likewise K=0 or m for beta.
Touching zero retains the center. For the unchanged retained set A,

    d_new=min_(J,K in A) max(0,q_v(K),q_h(J))                        (7)

is a lower bound on Delta_JK for every admissible noncorner center and
all physical phases in the box. For each particular retained center its
profile maximum in(7) is valid by(5),(6), and the minimum cannot exceed
that center's value. An extra nonphysical center only weakens the lower
bound. Actual corner centers remain excluded from A and are handled by
the unchanged corner predicates. If A is empty the conservative output0
is valid; an implementation need not assign an infinite lower screen.

Let d_old be the independently valid v2 final screen. Then

    d_final=max(d_old,d_new)                                       (8)

is valid uniformly for every one of these centers and phases. Retaining
the old computation and its final scalar output exactly makes the final
defect bound no smaller than before, even if Arb operation/radius rounding
prevents an apparent interval-nesting or per-term monotonicity argument.
Similarly, separate base/hybrid boards each supply valid complete screens;
their global scalar maximum is valid. One may combine valid alternatives
earlier at each profile too, provided every claimed lower endpoint is
directed and both old/new proofs apply on the same box and retained set.

## Why per-pair treatment can improve the old enclosure

The following is exact rational algebra, **not an executed experiment**.
For X=[1,4],Y=[-4,-1], equation(R) gives the sharp lower bound2.
Natural interval evaluation instead gives

    |X|=[1,4], |Y|=[1,4], |X+Y|=[0,3],
    natural d interval=[-1,8].

Clipping this pair's natural lower bound against0 still returns0,
whereas the sign formula returns2. For sign-uncertain pairs the natural
lower bound can be negative; letting those negative artifacts enter a
sum can erase positive lower mass from other pairs before final-profile
clipping. Every true pair defect is nonnegative, so applying(3)/(4)
before summation removes this particular source of enclosure loss.
This explains a possible improvement; it does not prove that any of
the20 actual failed boxes becomes accepted.

## Unchanged certificate implication and independence

The only changed datum presented to the outer checker is its own valid
uniform defect lower bound. The primitive, its phase derivatives,
whole-sum S and corner-orbit bounds, corner constants, pi bounds and
phase boxes remain the same. The strict noncorner acceptance test stays

    U_S-d_final<Lc_lower,

with exact rational subtraction. Equality still fails. No leaf kind,
bootstrap rho<=1/2 guard, old pointwise radius, finite energy receipt,
degree range, tree partition or zero-phase equality exception changes.
Therefore PD-T364 and the already accepted round8 holistic proof apply
without a new maximum-exclusion argument. A lower-bound improvement
does not justify accepting a pending or partially checked partition.

The finite energy guard remains the specific accepted2..128 theorem;
the independently failed round8 replay and immutable compact input
SHA97c339181652d37e7e3c34522959f1b7157b8ea26d3f0ab83c0ebc1c3901528e
remain preserved. A new source must be explicitly selected and reviewed;
no old source is substituted under the same identity.

Producer header `n3_outward_interval.h` already has equivalent pairlower
mathematics. The proof above was reconstructed from the real-variable
identity before that helper was inspected, as recorded in the idea and
attempt. It licenses a separate Arb/ARF implementation, not importing the
producer's interval operations, transcendental enclosures, numeric bounds
or verdict. Mathematical identity reuse and arithmetic implementation
independence are compatible; no priority claim is made.

## Required bounded controls and remaining work

Before any selected failed-box evaluation, controls should compare the
helper's lower result to the exact rectangle infimum, not merely sample
interior point values. Include both sign orientations, swapped arguments,
all same-sign cases, zero endpoints/crossings, singleton zero/nonzero
intervals, unequal widths, tiny dyadic distances from0 and wide signed
intervals. Endpoint witnesses in the proof decide the exact expected
infimum. Test finite/malformed input handling and directed conversion.
Test additive profile normalization and fixed reflected-pair zeros.

For any bounded old/new kernel comparison, all six nondefect returned
bounds must remain unchanged and the final defect lower must dominate
the old scalar. The finite primitive/derivative controls remain in force.
No selected box, new source control or full replay was executed by this
mathematical author. The separate developer/reviewer records must freeze
their own command, source, box list, arithmetic, CPU budget and outcomes.

After the exact controls and chosen-box gate, distinct Astra high math/
source review is required before the coordinator may release one complete
replay of the unchanged original n32 certificate. No other degree, new
partition, automatic retry or whole job is authorized by this lemma.
Global2..40, finite energy2..128 and all-degree PD-T099 OPEN are unchanged.

## History

2026-11-06, Codex mathematical developer, assigned Sol xhigh; serving
metadata unexposed. Rules/input
`d974329331ee4090e8ca1d5100342e69039edbf0`. Prospective gate, complete
scope/shortlist, scalar derivation before producer-helper comparison and
all considered alternatives are in `../ideas/N3-defect-enclosure-r9.md`.
Unexecuted verification plan is in `../attempts/N3-defect-enclosure-r9.md`.
No old artifact, mathematical predicate or shared file is modified.
