# D05 attempt — Translate the matched half-line residual before bounding

Rules/read input `a6d7a788b3ce457a4631bbb507624303240c570c`.
Parent-assigned Sol xhigh; serving metadata unexposed. Developer only;
root owns Git and all shared files. Fresh gate and retained alternatives
are in [the idea](../ideas/D05-relative-reference.md).

## Exact main target, still OPEN

Use exactly D04's intermediate model K_D04, including its actual corrected
polynomial special rows, ordinary H profiles and Delta_R=E_infty-E_R.
Define

    R_n(phi)=S_n(phi)-K_D04(n,R;phi),
    Rrel_n(phi)=R_n(phi)-a(phi)R_n(0,0).

The parent requested a useful bound for Rrel with phase factor P or rho,
then the analogous normalized full M_infty comparison. A possible
supporting near-domain contract is |Rrel|<=C*rho*H_n/n for n>=16,R=2,
alpha,beta>=0,rho=alpha+beta<=pi/2, with explicit useful C. No such
full bound is proved here. In particular it does not follow by subtracting
D04's two absolute estimates: their a(phi)H_n/n allowances survive that
triangle inequality at phase zero.

D04 was a named pending dependency at the prospective gate. During this
block root reported that the three support proofs were accepted unchanged
by distinct Astra xhigh review, with report
[independent-checks-D04-row-reduction.md](../independent-checks-D04-row-reduction.md),
reported SHA256 `cacbab625421e4d269bc2a3047aa523caee8c4f08a709748721291178f9976d7`.
This developer does not self-approve D04 or the new result.

## Cheapest separation test and outcome

D04's half-line proof already subtracts the reciprocal from cotangent.
The prospective D05 distinction was to compare the resulting ONE matched
quadrature functional at its two actual translated offsets before taking
absolute values. The gate's kill tests were nonvanishing incremental
constants, invalid divergent subtraction, or an uncharged offset wrap.

The test survives for the scoped residual. The new separate
[supporting theory](../theory/D05-relative-halfline.md) proves:

1. The continuous cotangent-minus-reciprocal residual r has exact
   derivative variation 5/3, including its derivative jump of1 at pi/2.
   Its whole variation is 4/pi.
2. Its matched cell defect E satisfies
   |E-(1/2-t)r(v)|<=5h/24 and
   |Delta E|<=(5/3)|Delta v|+(4/pi+5h/3)|Delta t|.
   Both infinite objects are used only as convergent matched cell
   differences. E(t=1)-E(t=0)=-r(v), so it is explicitly not periodic.
3. With h=pi/n, the ACTUAL shifted finite offsets
   theta_±=(1-s±alpha/pi)/2+(j+s)/(2m), s=±beta/pi, give

       (nm)^-1 sum_fixed_endpoint_rows
         |(T0-Theta)(phi)-a(phi)(T0-Theta)(0)|
                               <=2a*rho*H_n/n.

   The fixed rows are j=R,...,floor((m-1)/2) on the left and
   j=R+1,...,floor((m-1)/2) on the right; n>=8R,R>=2 and
   rho<=pi/2. Every one of these physical-row offsets is strictly
   between0 and1; no collision or root value is substituted. The finite
   displacement (j+s)/(2m) is essential and retained.

This is a substantive PROVED developer supporting lemma, with independent
review still required. Its contract is the half-line residual part of
the fixed endpoint rows, not a reworded full relative theorem. No sample,
fit, old quantifier transfer or C2 primitive assumption was used.

## Parent-suggested absolute alternative

Before deriving it, the parent suggested keeping the boundary value
r(v)=O(v) against w=O(a/v). The first-order cell identity justifies this
idea; the pointwise bound alone would not suffice. On D04's whole closed
diamond it changes the aggregate endpoint T0-Theta charge from

    32a*H_n/(pi^2*n)

to the proved bound

    2pi*a/(3n)+5a*H_n/(3n^2).

The other D04 reference charges remain. For example its reference proof
and the new bound imply the absolute corollary

    |(nm)^-1 sum_O T0-Delta_R|
       <={[20a/pi^2+16P/(3pi)]H_n+(7+2pi/3)a+2P/pi}/n
                                            +5a*H_n/(3n^2).

This corollary still has an a H_n/n term from the separate displaced
digamma comparison. It is not a pass of the phase-relative target and
does not by itself provide a useful near-noncorner defect comparison.

## Precisely unclosed obligations

To turn the supporting lemma into Rrel, all the following must be joined:

- Phase increments of Theta/(nm)-Xi using displaced digamma arguments,
  including the finite n/m logarithm and exact integer recurrences.
  Two absolute errors do not prove the required increment.
- The reference contribution in the central region. The fixed endpoint
  lemma deliberately does not claim a central moving-root estimate.
- Rows crossing the endpoint/central partition near pi/2. A half-line
  component can have its own boundary bookkeeping value even when the
  actual g0 contribution vanishes; the complementary central term must
  be compared before bounding that change.
- Changes of the exact polynomial-collision special set. At most two
  simultaneous marks is useful, but old N1-18's 4/n mark bound is for
  another fixed model/domain and is not a vanishing-in-phase bound for
  D04. It has not been imported.
- Phase increments of the actual weighted single-pole profile error.
  N1-04's 5/n^2 absolute bound alone still leaves a phase-independent
  relative allowance. Exact regularized offset limits must remain.

D03's accepted perturbation quadrature already has its phase factor
112P H_n/(pi*n); it vanishes at zero. That fact does not discharge the
five missing items above. The separate D05 outer-profile worker owns
K_D04 to M_infty comparison and is not assumed to have supplied a rate.

## Retained routes and bounded-block disposition

- Naive subtraction of two D04 absolute bounds: inadequate sufficient
  estimate; consolidated away, without a negative theorem about the
  actual relative error.
- Translated matched residual: retained successful supporting lemma.
- Boundary-value first-order identity: retained successful absolute
  improvement of one charge; no claim that all a H_n/n terms disappear.
- Whole-phase scalar offset wrapping: deferred for the relative
  application. E is not periodic; any extension must retain the exact
  wrap recurrence rather than replace real displacement by circle distance.
- Smooth h-Taylor through numerator roots, a pure quadratic primitive
  bound, and a leading-factor-only model: not pursued. PD-T220/PD-N079
  and PD-N132 retain their actual scopes. In particular no cusp failure
  is transferred from the primitive to the physical Lebesgue function.

Disposition: full D05 relative-reference target **OPEN/deferred** after
the bounded support lemma. Resume only with the actual five-item joint
increment assembly and a prospective useful constant; do not label this
supporting result as full target PARTIAL or infer an onset from it.
Old D01/D02 results, D04 formulas, M_near's one correction, original native
sources, certified ranges and all-n argmax claims remain unchanged.

## Checks and resource receipt

The block began with a read-only clock at2026-11-06 15:40:30 UTC. The
20-minute limit covers gate, analytic work and these records. All executed
commands were repository/rules/theory reads, searches, clock reads and
Markdown edits; later hashes/whitespace checks only identify these outputs.
No numerical code, native executable, board, quadrature, scalar diagnostic,
fit, degree job or producer was run. No child agent was spawned. Paper
algebra and finite constant comparisons in the proof are not reported as
an executed numerical check. Distinct mathematical review remains needed.
