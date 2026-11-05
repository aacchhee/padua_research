# PD-T?mz-cleanup-codex-02 — odd-degree fixed-node Padua weights

ID kind: PD-T.
Aliases: odd-m boundary logarithm; floor-half spectral triangle.
Split from: the missing odd-m case of PD-T295; its even-m statement is unchanged.
Split into: odd-m spectral consequences are in PD-T?mz-cleanup-codex-03.

## Statement

Use the frozen signed Lebesgue Padua rule with nodes
(cos(j pi/m),cos(k pi/(m+1))), j+k even, measure dxdy of mass four.
For every fixed j,k>=0 with j+k even,

    lim_(m odd -> infinity) m^4 w^(m)_(j,k)/log m
      = -16 e_j e_k (-1)^j,                         (1)

where e_0=1/2, e_l=1 for l>0. Moreover, for every odd m>=5 and
all its retained nodes (0<=j<=m, 0<=k<=m+1),

    |w^(m)_(j,k)| <= 8192 m^(-4)
                       [(1+j)(1+k)+log(m+1)].      (2)

The distances in (2) are indices from (1,1), not minimum distances
from a moving nearest corner. No uniform local limit is asserted.

## Definitions

R=(m-1)/2; theta_j=j pi/m; phi_k=k pi/(m+1).
t_0=2; t_a=-4/(4a²-1) for a>=1;
S_R(t,s)=sum_(a+b<=R) t_a t_b cos(2at)cos(2bs).
Finite endpoint factors epsilon_0=epsilon_m=1/2, eta_0=eta_(m+1)=1/2;
other finite factors equal one. They differ from fixed-limit e_j.

## Assumptions

Exact real arithmetic; odd m>=5 for the finite bound, fixed indices
before the asymptotic limit. No weight sign classification assumed.

## Status by part

Overall status: **PROVED** (analytic development; supplementary and
required Claude audits pending).

| Part | Status | Evidence |
|---|---|---|
| Fixed-index odd-m limit | PROVED | Two thin spectral corners below |
| Whole-grid majorant | PROVED | Explicit floor-half bounds below |

Candidate disposition: retained parity completion, no priority claim.

## Depends on

PD-T101's locally proved cardinal identity in the normalization integrated
in PD-T111; the elementary cosine-series and triangle estimates explicitly
proved in PD-T295. No even-m asymptotic is assumed at odd m.

## Checks

Rules/input ad503cb0603fc017444b0aa732240981eefa4d24.
This is an analytic proof without computational premises. Independent
mathematical reconstruction is requested from the separate checker.
No executed numerical evidence is claimed by this author.

## Sources

Local predecessor gate: ../novelty-gate-math.md. No external result used.

## Proof

Integrate the accepted cardinal identity. Only even coordinate modes
survive, so a+b<=floor(m/2)=R in half-frequency indices. The exceptional
x mode integrates to 2h_m T_m(x_j), which vanishes identically because
m is odd and h_m=0. Thus exactly

    w^(m)_(j,k)=2 epsilon_j eta_k S_R(theta_j,phi_k)/[m(m+1)]. (3)

This does not interchange the axes of the Padua cardinal formula.
With f(t)=pi sin t and T_R(t)=sum_(a>R)t_a cos(2at), the absolutely
convergent series identity and rectangle-minus-triangle decomposition
from PD-T295 give

    S_R(t,s)=f(t)f(s)-f(t)T_R(s)-f(s)T_R(t)
             +T_R(t)T_R(s)-V_R(t,s),                 (4)
    V_R=sum_(1<=a,b<=R, a+b>R)t_at_b cos(2at)cos(2bs),
    |T_R|<=1/R,
    |V_R|<=64(1+log R)/R².                          (5)

These identities/estimates involve only integer R>=2, not m=2R;
their proofs in PD-T295 therefore apply verbatim here. Since m=2R+1,
m/R<=5/2. Also |f(theta_j)|<=pi²j/m and
|f(phi_k)|<=pi²k/m. Multiplying the absolute bound from (4) by m²
therefore gives

    m² |S_R| <= pi^4 jk +(5pi²/2)(j+k)
                      +25/4 +400(1+log R).          (6)

Multiplication by 2epsilon_j eta_k/[m(m+1)]<=2/m² shows that
|w|m^4 is at most
2pi^4 jk+5pi²(j+k)+812.5+800log R.
Each coefficient of jk,j,k and the constant is below 8192, and
log R<=log(m+1). This proves (2), including moving far halfweights.

Fix j,k. Now f(theta_j),f(phi_k)=O_(j,k)(1/R); all terms other
than V_R in (4) are O_(j,k)(R^(-2)). To identify the logarithm,
fix 0<delta<1/2 and divide the triangle a+b>R into a<=delta R,
b<=delta R, and a,b>delta R. The first two regions are disjoint.
In the first, there are exactly a values R-a+1<=b<=R and

    R²t_b cos(2b phi_k) = -cos(k pi)+O_k(delta)+o_R(1),
    cos(2a theta_j)=1+O_j(delta²).

Indeed 2R phi_k=k pi (m-1)/(m+1) -> k pi. In the second region,
2R theta_j=j pi (m-1)/m -> j pi gives the corresponding formula.
The only required changes from even m are these two convergent phases.
Because sum_(a<=delta R)a t_a=-log R+O_delta(1), the first
and second normalized strip sums tend respectively to cos(k pi)
and cos(j pi), with O_(j,k)(delta) errors. In the middle each product
is <=16/(9delta^4 R^4) and there are <=R² pairs. Its contribution
after multiplication by R²/log R tends zero at each fixed delta.
Let R tend to infinity and then delta decrease to zero. Therefore

    R² V_R(theta_j,phi_k)/log R -> (-1)^j+(-1)^k.

Since m/R->2 and log R/log m->1, (4) implies
m²S_R/log m -> -4[(-1)^j+(-1)^k]. On the retained checkerboard
the two signs agree. In (3), m/(m+1)->1 and, at fixed indices,
epsilon_j eta_k eventually equal e_j e_k. Equation (1) follows.

As a convention check, j=k=0 gives -4, exactly the both-parity
corner asymptotic of PD-T111. Odd m has node corners (1,1),(1,-1);
this theorem is centered at the first and does not infer a uniform
moving-index limit at the second. ∎

## Scope

Together with PD-T295 this supplies the same pointwise limit on each
parity and a global summable packet majorant. Negative corner weights
alone still do not imply signed-form indefiniteness.

## Open items

Effective remainders, named onset degrees and sharp spectral constants
remain separate. Required independent/Claude audits pending.

## History

2026-11-05, Codex, inherited gpt-6.1-sol xhigh; input/rules ad503cb.
New odd-parity proof; accepted even-parity files remain untouched.
