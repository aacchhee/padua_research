# D25 regular outer increment — bounded paper attempt

2026-11-06; input/rules476208fe080cc79cae5b2578344b2e18f442a1e8.
Requested Astra ultra under root's prospective justification; serving
metadata unexposed.35min aggregate paper bound, no helper. D22 files
stay frozen. Work begins20:40UTC; a restart does not reset this bound.

## First exact test

For m=n+1,h=pi/m,t=beta/pi, let

    Q_tau[f]=(1/m)sum_(k=2)^(m−2) f(h(k+tau))
                                         −(1/pi)integral_0^pi f(z)dz.

The actual D07 operator is EXACTLY
Eout(phi)=Q_t[F_L(phi)]+Q_(1−t)[F_R(phi)]. At zero phase both
profiles equal F0, but their offsets remain0 and1. Therefore

    delta_a Eout=Q_t[F_L−aF0]+Q_(1−t)[F_R−aF0]
          +(a/m)sum_(k=2)^(m−2)
            [F0(h(k+t))+F0(h(k+1−t))−F0(hk)−F0(h(k+1))].

This is the complete actual-origin operator. The last finite sum is
not zero by symmetry and will be bounded explicitly. The integral
terms in that last difference cancel exactly. All fixed row labels,
the unequal n,m conventions and full regularization are unchanged.

## Prospective proof structure

Use actual centered cells. Their initial missing lengths total4h and
central missing lengths total2h. All retained cells lie in
[h/2,pi−h/2]. Separate the complete profile difference into its exact
log-n coefficient, weighted pole numerator, and cancellation integral
minus its central logarithm. This decomposition is inside the exact
operator above, not independent substitutions into the original model.

The angular weighted profile has a BV first derivative; translating it
in L1 retains the periodic cusp atoms. The cancellation component uses
its actual generic J identity. On an interval e>=epsilon, rho<=epsilon²/8
forces both central channels into the exact root-free regime. Otherwise
the inherited entropy bound is controlled by2log(1/epsilon)+log8.
Each missing-cell integral is still charged with an integrable
rho(1+abs(log distance)) envelope. The discrete baseline shift has a
separate derivative bound away from the omitted endpoints.

## Execution and limits

Only read-only rg/cat/git-diff/status and owned prose writes have run.
No scalar, native, phase, board, root, quadrature, fit, source or degree
job has run. No numerical endpoint is planned for this supporting lemma.
The full D13 target, any physical defect comparison and any new global
onset are outside its statement. Distinct review is required.

## Completed developer proof

The full theory now gives, for every integer n>=32 and rho<=1/2,

    |Eout(phi)−aEout(0)|<=rho[(35/2)log n+75]/n.

The exact intermediate coefficient before rational simplification is

    rho/m [(7/pi+8/3)L+(9/2+4/3+20/pi)log m
                                      +46+40/3+175/(4pi)].

The four independent charges are the log-n coefficient difference,
the weighted pole numerator difference, the regular cancellation
difference with every missing interval, and the actual baseline mesh
shift. The generic J entropy is controlled using a proved root-free
alternative at rho<=epsilon²/8, not by assuming phase exceeds a mesh
scale. No floating calculation or endpoint assessment was used.

Overall supporting status is developer-PROVED, pending distinct review.
The coefficient decreases for all real n>=32. The full finite relative
remainder stays OPEN, and there is no new threshold claim. Frozen D22
files were neither edited nor used as proof premises for this result.
