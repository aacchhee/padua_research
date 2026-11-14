# D03 supporting corner baseline — Exact normalization and deferred endpoint cancellation

Rules/input f1ba23cfbfb557dd491730f9837f5efe413e7c75;2026-11-06.
Codex parent-assigned Sol xhigh, serving metadata unexposed. The
[prospective candidate and fresh gate](../ideas/D03-corner-baseline.md)
precede this bounded analytic inspection. D02 corner files remain frozen.

## Outcome and status

The requested useful uniform O((1+log n)/n) lower loss relative to the
full limiting corner polynomial remains **OPEN**. Candidate disposition:
**DEFERRED**, with the exact missing cancellation specified below.
No optional Lambda_c>=M_infty(0,log n) inequality is claimed or refuted.
No new mathematical theory file is warranted: the established pieces
below are routine exact consequences of the named existing proofs;
the substantive new estimate has not been proved.

This is not a new global onset or finite-degree claim. It does not
replace C08's valid coarse margin, weaken PD-T269's limit, change a
quantifier, relabel D01, or infer a rate from the D02 limit theorem.

## 1. Distinct constants and the exact phase-zero polynomial

Use separate names throughout:

    kappa_shift=gamma_E+log(8/pi),
    A_n=(2/pi)(log n+kappa_shift),
    D_infty=(8/pi) integral_0^1 t^2 cot(pi*t/2)
                    sum_(l odd>=1)1/[l(l^2-t^2)]dt.          (1)

The integral has PD-T269's continuous endpoint interpretation.
kappa_shift is approximately1.51; D_infty is approximately.92.
These approximate descriptions identify the distinct constants and are
not inputs to any estimate. PD-T269's historical symbol kappa denotes
D_infty, not kappa_shift.

The exact phase-zero full polynomial is

    M_infty(0,log n)=A_n^2+D_infty.                         (2)

This identification does not come from a fit or an assumed profile.
PD-T269 gives Lambda_c-L_n^2->D_infty, and PD-T270 gives
|L_n-A_n|<=1/(4n^2), so Lambda_c-A_n^2->D_infty. Independently,
D02-far-uniform-limit identifies its exact declared quadratic model
with the true primitive limit, and S_n(0)=Lambda_c exactly. Therefore
the difference between M_infty(0,L) and
[(2/pi)(L+kappa_shift)]^2+D_infty is a polynomial in L tending to
zero along L=log n. Each coefficient must vanish. This proves the
routine identification(2), using the explicit integral(1) as its
constant rather than leaving a D02 constant unnamed. No sharp rate is
inferred from polynomial uniqueness.

## 2. Exact finite deformation, weights and factor4

Let m=n+1,a_j=j*pi/n,b_k=k*pi/m, and
f(a,b)=(1+cos b)/|cos a-cos b|. Define epsilon_j=1/2 at0,n and1
elsewhere. On0,...,n,eta_k=epsilon_k except eta_n=1. Write

    d_jk=f(a_j,b_k)-f(a_j,a_k),
    Delta_n=(4/(nm))sum_(j+k odd,0<=j,k<=n)
                                      epsilon_j eta_k d_jk. (3)

PD-T159 and C07's exact normalization give

    Lambda_c=(n/m)L_n^2+1/m+Delta_n.                       (4)

The1/m is the actual finite polynomial contribution of the removed
(n,m) endpoint. The reference k=n row vanishes; no diagonal lies on
the odd board. Thus eta_n rather than epsilon_n does not alter the
reference sum. All other endpoint half weights stay in(3).

For clarity, the exact finite positive-pair representation is

    Delta_n=(4/(nm))[
        sum_(j<k,j+k odd)epsilon_j epsilon_k(d_jk+d_kj)
              +(1/2)sum_(j+n odd)epsilon_j f(a_j,b_n)].    (5)

C07 proves each bracketed unordered-pair term nonnegative. The
unmatched second-endpoint half-row in(5) is nonnegative too; its
reference value is zero. This derives every factor and weight before
any limiting profile is introduced. It does not assert positivity of
an individual signed d_jk or equality of a finite profile to its limit.

## 3. The missing normalization compensation

Combining(2),(4) gives exactly

    Lambda_c-M_infty(0,log n)
      =Delta_n-D_infty-(L_n^2-1)/m+(L_n^2-A_n^2).          (6)

The final one-dimensional square error is already controlled for every
n>=1 by PD-T270:

    |L_n^2-A_n^2|<=A_n/(2n^2)+1/(16n^4)=:e_1(n).         (7)

Consequently a sufficient new deformation estimate would be

    Delta_n>=D_infty+(L_n^2-1)/m-C(1+log n)/n.            (8)

It would give the target with the explicit additional e_1(n), which
has the smaller order O((1+log n)/n^2). No such estimate(8) is proved
in this block, and the positive pair/profile comparison needed for it
has not been assumed.

The cheapest proposed shortcut was to regularize just the limiting
paired profile and use a lower Darboux sum to prove

    Delta_n>=D_infty-C(1+log n)/n.                        (9)

Even if(9) were established, inserting it into(6) leaves the explicit
negative term (L_n^2-1)/m. Its ratio to(1+log n)/n is unbounded:
PD-T270 implies L_n~(2/pi)log n. Thus that particular estimate cannot
by itself supply a fixed constant for the requested full baseline loss.
This is an insufficiency of the proposed bookkeeping step, not a
counterexample to the target or a negative theorem about endpoint-
complete Darboux methods. The cancellation in(8) must be established
within the finite deformation; it cannot be erased by rounding d(n)
or naming D_infty as the corner constant.

C07's nonnegative pairing supplies Delta_n>=0. C08's retained central
strip gives its positive coarse d(n) with its own degree conditions.
Neither includes the extra finite compensation in(8). PD-T269's
existing all-n>=32 absolute remainder remains valid but weak; no
estimate there is transferred below its floor or promoted to the new
rate here.

## 4. Retained alternatives and the stop boundary

The desired target stays OPEN. The absolute baseline route is deferred
until a concrete application needs it and an endpoint-complete finite
profile or another exact identity supplies(8), with all weights and
an explicit useful constant. The optional exact lower inequality in
the idea record stays unproved and untested; no rejection is inferred.

The phase-relative alternative already declared in D02 uses the exact
identity S_n(0)=Lambda_c and studies

    [S_n(phi)-S_n(0)]-[M_infty(phi,log n)-M_infty(0,log n)].

A practical bound for this difference could make a separate absolute
corner baseline unnecessary. That practical bound is itself unresolved;
its availability as an alternative is not called proof of cancellation.
This D03 candidate is retained for that decision rather than expanded
solely to create another counted round.

The bounded analytic inspection stops with the exact formulas(3)–(8)
and the scoped missing step. No new executable numerical board, native
kernel, quadrature, degree job, fit, producer or child agent was run.
Read-only registry/proof searches and exact symbolic algebra were the
only work. No CPU timing or independent proof acceptance is invented.
Distinct review of any future substantive estimate remains necessary.
