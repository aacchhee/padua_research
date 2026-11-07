# PD-T?argmax-bridge-codex-F05-joint-error-01 — Complete cusp-aware first inner crossover

ID kind: PD-T. Aliases: F05 complete first transport band; joint finite-error
logarithmic cancellation with the real central cusp.
Split from: the OPEN full near-diamond cusp-aware target.
Split into: F05-joint-error-background and F05-joint-error-central are
supporting results with their own proofs; they do not close the full target.

## Exact statement and assumptions

For EVERY integer n>=32 set m=n+1,h=pi/m,L=log n. On beta=0,
alpha=c*h,c in CLOSED[1/2,3/2], define the COMPLETE actual-origin error

    E_n(phi)=S_n(phi)-M_infty(phi,L),
    ell_n=(nm)^-1 sum_(k=1)^floor(n/2)cot(k*pi/n),
    D_n(c)=E_n(c*h,0)-E_n(0)-ell_n*sin(c*h).

Then, uniformly on this closed interval and BOTH degree parities,

    |D_n(c)+(c/pi^2)h^2 log n|<=10000h^2,                  (1)
    D_n(c)<=70000*(c*h)/n.                               (2)

The actual c=1 polynomial collision is included. S_n is the original
corrected odd-board primitive, exceptional top mode ONE, original endpoint
weights and unequal n,m meshes; every origin is the SAME finite-degree
origin and M_infty is the unchanged TRUE completed model. Exact real
arithmetic; no numerical premise.

Overall status: **PROVED developer PAPER theorem**, requiring distinct
review/root adoption. The limiting signed coefficient follows uniformly:

    D_n(c)/(h^2 log n) --> -c/pi^2,

on the ENTIRE c interval. No effective sign threshold is selected or evaluated.
The constant70000 is deliberately coarse and supplies no useful global onset.

## Depends on and proof

Accepted E03 already gives the full same-mask row/retained/outer-log joint
identity; it is not new here. Accepted E05 gives the exact COMPLETE axis
decomposition before any triangle inequality:

    E_n(alpha,0)-E_n(0)-ell_n*sin alpha
      =B_n(alpha)-B_n(0)-M_nc(alpha)+M_nc(0)
        +Rcen+(4/(nm))sum_(r=1)^n Y_r-E_c(alpha,0),
    0<=Rcen<=alpha^2/(3m).

This includes all original rows, signed model terms and actual collision
transport. Ordinary/reference/pole/mesh costs have not been dropped; their
EXACT sum is this identity for S_n-M_infty. It is an actual-origin proof,
not a delta_a estimate with an origin charge silently removed.

The new background support proves that the first line has logarithmic term
-c^2*h^2*L/pi^2 and remainder at most2000h^2. It derives the exact
fixed-mask curvature, finite Hurwitz/cotangent tails and the full model
logarithmic curvature; no old H^2alpha^2 bound is substituted at this scale.
The new central support proves that the root sum minus the SAME SIGNED
E_c has coefficient c(c-1)*h^2*L/pi^2 and remainder at most200h^2.
It keeps both actual linked first-row peaks and the complete inner integral,
and proves uniform finite remainders at the c=1 entropy/collision crossing.
Finally Rcen<h^2. Therefore

    |D_n(c)+(c/pi^2)h^2L|<=2201h^2<10000h^2,

which proves (1) with the prospectively registered allowance. Dividing by
h^2 log n proves the uniform coefficient, with error at most10000/log n;
this uses the finite uniform theorem, not matching separate asymptotics.

The logarithmic term in (1) is nonpositive. Hence D_n(c)<=10000h^2.
Since n*h/c<=2pi<7, this implies (2). No degree endpoint or scan is
needed for this elementary conversion. The real finite cusp ell_n remains
explicit. Replacing sin alpha by alpha weakens the upper bound if desired.

## Scope and open items

This proves a previously uncovered COMPLETE parameter band at phase~1/n,
including its first transported inner row. It is a continuation of the
accepted joint-error program, not a new kernel, new completed model or new
algebraic cancellation identity. Its uniform signed coefficient does not
follow from E03's fixed-positive-alpha log match or E06's alpha~h^2 limit.

The full closed half-diamond target
E_n(phi)-E_n(0)<=ell_n|alpha|+C*rho/n+K*(1+log n)*rho^2/n
remains OPEN. Beta!=0, further inner transported rows and useful small
constants require further work. This support does not make D13 PARTIAL,
does not certify a residual degree, and changes neither global320 nor the
273-degree residual set. No actual-argmax obstruction is claimed: the
necessary logarithmic test passed with favorable sign.

The bounds use accepted analytic profile/origin/norm identities at their
literal scopes. No new PD-T271 numerical enclosure is performed or promoted
to a finite-origin sign. Any inherited quantitative norm premise keeps its
original dependency and trust basis. No unaccepted F02/F03/F04 result is a
premise.

## Checks and history

Only bounded reads/searches/metadata, exact hand reasoning and owned prose.
No scientific source/script/import, measurement/scalar/phase/degree/endpoint/
threshold/native/root/quadrature/compiler/build/pack job, Git or shared edit.
The F05 gate, explicit WAIT, separate root mathematical release, prospective
target and emergent stronger coefficient/remainder registration are preserved
in ideas/attempts F05-joint-error-crossover.md. Original F01 and D/E proofs,
failed scopes and unwaived P1–P4 remain unchanged.

2026-11-07, requested Sol xhigh, actual serving metadata unexposed; supplied
rules/input4a5de2012bad94601c713b2ff5517f2e3fb80af2. This is ONE F05 round.
Distinct Astra reconstruction and root adoption are separate from development.


## Root disposition after distinct mathematical acceptance —2026-11-07

Root adopts the exact mathematical statement under its written quantifiers, hypotheses and dependencies. The original frozen proof/record prefix is preserved and identified in [independent review](../independent-checks-F04-F05.md), final SHA256ccdb1d774bd3653aadb26df3382be462043a5a7256bba2f41c909967fcf080f4. No global-onset change, new finite degree, source integration, strict runtime saving, novelty/priority verdict, protocol waiver or readiness follows beyond the exact statement. Final Claude review remains separate.
