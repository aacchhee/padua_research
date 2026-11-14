# IDEA?argmax-bridge-codex-N5-05 — A quarter-unit full projected-defect budget

Aliases: N5 round5; large vertical projection budget; full-periodic
quarter floor; budget escape from independent N1 error addition.

## Preregistration — 2026-11-06, before this round's computations

- Exact target: every integer n>=64, m=n+1, J in {0,n}, interior
  integer 1<=q<=m-1 with J+q odd, and real alpha,beta with
  |alpha|+|beta|<=1/2 and (J*pi+alpha)/n in [0,pi]. In particular
  alpha>=0 at J=0 and alpha<=0 at J=n. Prove

      Q_v(n,q;alpha,beta)>=1/4.                         (C5)

  This is the full periodic vertical projection, not merely N5-04's
  selected blocks and not the actual full defect S-lambda.
- Exact definition: N=n(n+1), Gamma={(r,s):0<=r<2n,0<=s<2m,r+s odd},
  u_r=(r*pi+alpha)/n, v_s=(s*pi+beta)/m. Let P=T_(n+1)+T_n and

      G_rs = D_n(cos u_r,cos v_s)-cos(n*u_r),
      D_n(x,y)=[P(x)-P(y)]/(x-y), polynomially at x=y,
      d(x,y)=|x|+|y|-|x+y|,
      Q_v=(1/(4N))*sum_Gamma d(G_rs,G_(r,2q-s)),        (D5)

  with the second index modulo 2m. The phase beta is unchanged in
  the reflected partner. The equivalent signed-half numerator is

      a*(1+cos v)-(sin alpha/2)*sin u+(sin beta/2)*sin v,
      a=(cos alpha+cos beta)/2,
      H=[(-1)^r D_n(cos u,cos v)-cos(alpha)]/2.

  The exceptional subtraction is cos(alpha), not 1; the folded
  physical-row/periodic-first normalization is 1/N. All total sums
  retain every finite polynomial collision value.
- Mechanism/hypotheses: obtain a substantially larger rigorous lower
  bound from a sufficiently complete family of sign bands or exact
  lattice/count-integral comparisons, using (D5). The only analytic
  attempt after the cheap gate is a uniform sign-band/count-integral
  lower bound. No fitted profile, optimized phase sweep, whole-phase
  certifier, automatic successor or silent smaller constant.
- Closest predecessors read in full: T222, T366, N5-04 with its distinct
  review; T224/N5-03 for thin endpoint lines; T215/T364 for exact
  normalization. IDEA318/327/328/330/459 retain the earlier documented
  meanings. PD-T266's unique limiting vertical minimum is now read in
  full as an additional comparison; it supplies no finite rate at
  n64 or fixed phases. N1-round4-budget.md is read in full: its 3/50
  formula floor is not a true-error lower bound.
- Separation: T222/T366/N5-04 prove small positive floors, the last
  1/2048 on this same domain. None proves (C5). This is a quantitative
  continuation of the same positive-defect mechanism, without a new
  mechanism or historical novelty claim. Its distinguishing obligation
  is the exact quarter-unit full projection floor, not extra samples.
- Registry/literature gate: the complete 1031-line registry coverage
  completed at the end of round4 is already available before this
  round. Rules and IDEAS are unchanged at input
  fc8c2885f47b08cecc7f65328db0e740cbc205ea; this was checked by diff
  and SHA256 0e1813b1f53e6aa4a970f19b86ebb3864dd6546b7f55c0bc2ffc4033320825f7.
  This prospective use of completed coverage does not alter round4's
  recorded timing qualification. No new external source is used.
- Cheapest MEASURED test: n64/65, both J endpoints, q nearest 1,m/2,m-1
  subject to J+q odd, the six phases (0,0),(0,+/-1/2),
  (inward*1/2,0),(inward*1/4,+/-1/4). Compute every term in (D5)
  with a new finite corrected polynomial implementation, independent
  of earlier developer code. Use full Q_v directly; S-lambda is not
  a proxy or premise. Record floating precision and control differences.
- Kill criterion: a well-separated measured Q_v<1/4 at an admissible
  case ends this specified strong-floor proof candidate, with its
  finite witness and measurement limits. This does not refute an
  actual-lambda quarter deficit because Delta can exceed Q_v. If
  samples survive, attempt one explicit uniform analytic bound; if
  it cannot close, state the unresolved inequality and stop this round.
- Test discriminability: a full direct Q_v evaluation tests exactly
  (C5) at the chosen finite inputs; successful samples cannot prove
  its continuum/all-degree quantifiers. PD-T266 asymptotics alone also
  do not discharge those quantifiers.
- Resource limit: bounded initial cases plus one analytic attempt;
  small receipt and off-Git raw rows within the existing aggregate
  allowance. No expensive certifier, unbounded scan or round6.
- Actual result: not run at preregistration.
- Disposition: OPEN quantitative candidate at preregistration.
- Canonical theory: only if the single attempt gives a substantive
  proof or bounded obstruction/obligation; global PD-T099 stays OPEN.
- History: parent-authorized N5 round5 after published round4+review
  fc8c288. All round4 source/report/receipt hashes stay frozen. Parent
  proposed (C5), explicitly unproved; the old measured minimum is not
  a premise. Developer model/effort inherited; serving metadata unexposed.

## Surviving cheap gate and the single analytic attempt

The 72 direct full-Q_v diagnostics pass: minimum
0.5230485747479166311, with gap 0.2730485747479166311 above 1/4.
The new finite corrected triangular polynomial kernel uses a 64-bit
significand longdouble; separate binary64 and 80-digit scalar polynomial
recurrence controls are reported in the receipt. These are MEASURED
checks, not premises of (C5).

Before evaluating the analytic certificate, fix the following sole
attempt. Use N5-04's global numerator lower bound, but sum its exact
sign-band envelope over **all** physical rows and periodic first
indices, with no old rectangle restriction. Put a0=15/16,c0=11/15,
x=cos u,y_+=cos(phi+b),y_-=cos(phi-b), so y_+<y_- for interior b.
On y_+<x<y_- and c0+y_+>0, define

    ell(u,b)=2*a0*min((c0+y_+)/(x-y_+),
                       (c0+y_-)/(y_--x)),

and set ell=0 elsewhere, in particular at collisions. The actual
numerators exceed a0*(c0+y_+) and a0*(c0+y_-), since
a>=a0 and the total sine perturbation is at most1/4. Thus the exact
finite sum F_n=(1/N)sum_k f_k sum_(r+k=J mod2) ell(u_r,b_k)
is a uniform lower bound for Q_v. The attempt is F_n>=1/4 on (C5)'s
domain. This preserves exact within-band fractions and full counts,
but separates the global worst numerator errors before summing.

Cheapest analytic test: the admissible central zero-phase subsequence
n=4t+1>=65,J=0,q=(n+1)/2,alpha=beta=0. Compute or bound its
count-integral limit before seeking a uniform lower estimate. If this
certificate is below 1/4 there, it cannot prove (C5), although (C5)
itself remains OPEN. Stop after this single analytic attempt; no second
phase-sensitive envelope is developed in this round.

## Final bounded disposition — 2026-11-06

The single analytic certificate fails: along admissible
n=4t+1>=65,J0,q=(n+1)/2,alpha=beta=0, its F_n has a limit
strictly below487302379/1968469140<1/4. The exact scoped statement
is **PROVED** in ../theory/N5-large-budget.md,
PD-N?argmax-bridge-codex-N5-01. This certificate's mechanism is
**REJECTED: failed**. The entropy integral and lattice-tail argument
are analytic; the code's rational checks reproduce only arithmetic.

Original C5 status: **OPEN**. Candidate disposition: **deferred**, with
the original exact quarter floor and domain retained. Resumption would
require separate authorization and an additional argument beyond this
phase-blind envelope. No full-Q counterexample was found and no
actual-lambda quarter margin was refuted. The successful finite direct
measurements remain diagnostics. No smaller replacement constant or
second analytic candidate is introduced. This round stops here.
