# PD-T?argmax-bridge-codex-D07-mesh — Exact global singular meshes and completed-constant matching

ID kind: PD-T. Aliases: macroscopic h/g telescoping; central gamma
product; explicit finite-h difference from M_infty.
Split from: D07 global regular-profile step. Split into: none.

## Statement and exact scope

Use exactly D07-global-outer.md's n>=16,m=n+1,L=log n,h=pi/m,
closed phase diamond, six actual polynomial rows J6, Delta_2,
F_s and openly defined intermediate G_n. Define the unchanged constants

    B0=4a/pi^2, D0=U0/pi+B0 log pi,
    eps_n=log(m/n), Z_n=D0-B0 eps_n,
    t=beta/pi in[0,1], t_L=t,t_R=1-t.

First work at absolute phases, exactly as in that theorem. Let h_j(t)
and g_j(t) be the EXACT convergent constants of N1-round4-mesh.md:

    x_k=k+t, b_j=j+t-1/2,
    h_j(t)=-log b_j+sum_(k=j)^infty
       [1/x_k-log((x_k+1/2)/(x_k-1/2))],
    g_j(t)=-(log b_j)^2/2+sum_(k=j)^infty
       [log(x_k)/x_k
          -{log^2(x_k+1/2)-log^2(x_k-1/2)}/2].

No truncation or old-model parameter changes are made. Set

    Tmesh=Z_n sum_s[h_2(t_s)-h_(m-1)(t_s)]
                    +B0 sum_s[g_2(t_s)-g_(m-1)(t_s)],
    Cmesh=2(m-3)log h
             +log Gamma(m-1-t)+log Gamma(m-2+t)
                         -log Gamma(2-t)-log Gamma(1+t).  (1)

Every Gamma argument is positive, including t=0,1. Gamma/log Gamma
mean their positive-real functions. Then the exact finite equalities are

    (1/m)sum_s sum_(k=2)^(m-2) T(L,h(k+t_s))=Tmesh,
    sum_s sum_(k=2)^(m-2) log(pi-h(k+t_s))=Cmesh.       (2)

The full regular integral from D07-global-outer.md is exactly

    U(L)=(b_full-2D0)L+K_0-(2d/pi)(log pi-1),         (3)

where b_full,K_0 are the unchanged D02 completed-model quantities.
In particular no unknown cutoff constant or fixed-delta residue remains.
Define the unchanged endpoint constant

    E_2=C_2+D0[h_2(t)+h_2(1-t)]+B0[g_2(t)+g_2(1-t)]

as in D02/D04, with all original continuous polynomial-compatible
endpoint conventions. The exact finite-h difference is

    G_n=M_infty(L)+J_n,
    J_n=J6-E_2+Tmesh-B0 L^2-2D0 L
                  +(d/(pi*m))Cmesh-(2d/pi)(log pi-1). (4)

Status: **PROVED**, written analytic identity, distinct review pending.
The scalar mesh remainder has the separate explicit bound below, but
the retained-row error is not bounded by this file. Hence the useful
S_n-M_infty allowance stays **OPEN**. One may combine the accepted
D04 row bound and D07's new quadrature inequality to obtain only

    |S_n-M_infty|<=E_D04+E_global+|J_n|,              (5)

with the six actual finite rows still explicitly present. The old
near model/correction and the old far model are unchanged.

### Separate finite-h scalar mesh bound

To expose precisely the remaining row obligation, set

    H2=h_2(t)+h_2(1-t), G2=g_2(t)+g_2(1-t),
    Rmesh=Tmesh-D0*H2-B0*G2-B0*L^2-2D0*L,
    Rlog=Cmesh/m-2(log pi-1),
    Bmesh=B0*(2L+|H2|)/n
            +[|D0|+B0*(L+1/n)]/(4n^2-1)
            +B0/(2n-1)^2
            +[|Z_n|+B0*(log(n+1/2)+2)]/[4(n-1/2)^2],
    Blog=[3log m+log2+2log pi+2]/m.                    (6)

Then throughout the same full closed phase diamond,

    J_n=(J6-C_2)+Rmesh+(d/pi)*Rlog,
    |Rmesh|<=Bmesh, |Rlog|<=Blog,
    |J_n|<=|J6-C_2|+Bmesh+(d/pi)*Blog.                (7)

There is no e_rows or I_n in(6)--(7). All parameters are the original
constants and actual finite-h mesh. A useful bound on the FIRST term
|J6-C_2| remains a separate retained-row theorem; it is not inferred
from this scalar mesh estimate.

## Dependencies

N1-06 supplies the absolutely convergent h/g definitions and their exact
cell primitives. D02-far-bias-identity.md supplies K_delta,K_0,C_infty
and their full closed-phase weighted limits. C06-far-full-profile.md
and N1-06 supply the exact b_full coefficient integration. Accepted
D04-reference-matching.md gives Delta_2=E_infty-E_2 at R=2, not an
extension of an old R>=64 tail bound. D07-global-outer.md supplies the
finite-row model and proof that the subtracted integrals converge.
Only Gamma(x+1)=x Gamma(x) at positive x is needed in(2); no asymptotic
Gamma approximation or floating evaluation is used.

## Proof

### 1. Exact endpoint mesh to its actual last index

Subtract the definitions of h_j(t) and h_(K+1)(t) for K>=j. Their
infinite tails cancel, and the cell logarithms telescope exactly:

    sum_(k=j)^K 1/(k+t)=h_j(t)-h_(K+1)(t).

The same algebra with the squared-log cell primitive gives

    sum_(k=j)^K log(k+t)/(k+t)=g_j(t)-g_(K+1)(t).

Absolute convergence justifies the tail cancellation. Here j=2 and
K=m-2, so K+1=m-1 with no phase-dependent floor or wrap. Moreover

    T(L,h(k+t))/m=Z_n/(k+t)+B0 log(k+t)/(k+t),

because L+log h=log pi-log(m/n). This identity retains the exact n/m
mesh displacement before any error estimate. The two finite sums give
the first line of(2). No e_mesh, C_X, shrinking delta or tail
approximation is used in this step.

### 2. Exact central logarithmic mesh

For each folded side,

    pi-h(k+t_s)=h(m-k-t_s)>0,

and k=2,...,m-2 contains m-3 labels. Reverse the order with j=m-k.
Gamma's finite recurrence gives

    sum_(k=2)^(m-2) log(pi-h(k+t_s))
      =(m-3)log h+log Gamma(m-1-t_s)-log Gamma(2-t_s).

Add t_s=t,1-t to obtain Cmesh exactly. The smallest denominator
argument is1, and all numerator arguments are at least m-2>0.
This verifies endpoint phases and all phase edges directly.

### 3. Exact finite part and coefficient of the full regular integral

For any 0<delta<=pi/4, D02 defines

    K_delta=B0 log^2(delta/pi)+2D0 log(delta/pi)
                          +(1/pi)integral_delta^pi(B_L+B_R)dz.

Subtract S0(z)=[U0+(4a/pi)log z]/z on each folded side. Direct
integration of the two S0 terms gives

    K_delta=(1/pi)integral_delta^pi(Z_L+Z_R)dz.        (6)

For clarity, the log delta coefficients cancel because
D0=U0/pi+B0 log pi; the remaining log pi constants cancel by the
same identity. This is an algebraic cancellation of the combined
finite-part expression, not separation of divergent integrals at zero.
The accepted integrable endpoint envelope now gives

    K_0=(1/pi)integral_0^pi(Z_L+Z_R)dz.               (7)

Likewise N1-06's exact endpoint coefficient at delta is

    b_end=2B0 log(delta/pi)+2D0
                          +(1/pi)integral_0^delta(f_L+f_R)dz.

The exact C06 interior coefficient adds integral_D A/pi, equal after
folding to integral_delta^pi(f_L+f_R)/pi+2B0 log(pi/delta).
Therefore the same delta terms cancel, giving

    b_full=2D0+(1/pi)integral_0^pi(f_L+f_R)dz.        (8)

Finally F_s=L f_s+Z_s-(d/pi)log(pi-z), and
integral_0^pi log(pi-z)dz=pi(log pi-1). Combining(7)--(8) proves(3).
The proof is literal at a=0 and all coefficient/root transitions; the
subtracted integrals converge uniformly by their accepted envelopes.

### 4. Match to M_infty without discarding the finite rows

Insert(2)--(3) in the definition of G_n. Use the unchanged identities

    Delta_2=E_infty-E_2,
    M_infty=B0 L^2+b_full L+E_infty+K_0.

Cancellation of K_0,b_full and E_infty gives exactly(4), with its
displayed signs. Applying the triangle inequality to the D07 bound
for S_n-G_n proves(5), with no claim that the extra |J_n| is useful.
All formulas extend by the inherited separate absolute phases, without
exchanging the unequal coordinate meshes.

### 5. Bound the macroscopic mesh remainder separately from the rows

In N1-06's exact shifted sums use K=m-2, so the two upper cell
endpoints in its dimensionless coordinate are

    b_L=m-3/2+t=n+c, b_R=m-1/2-t=n-c, |c|<=1/2.

Let eta_+=log(1+c/n), eta_-=log(1-c/n), j=eta_++eta_-.
The accepted N1-06 tail bounds give, with b=b_L or b_R,

    sum_(k=2)^(m-2)1/(k+t_s)=log b+h_2(t_s)+e_h,
    0<=e_h<=1/(8b^2),
    sum_(k=2)^(m-2)log(k+t_s)/(k+t_s)
                           =(log b)^2/2+g_2(t_s)+e_g,
    |e_g|<=(log b+2)/(8b^2).

Insert these in Rmesh before taking an absolute value. All large
logarithmic terms cancel exactly, leaving

    Rmesh=-B0*eps_n*(2L+H2)
        +(D0+B0*L-B0*eps_n)*j
        +(B0/2)*(eta_+^2+eta_-^2)+tail.

The elementary log inequalities imply

    0<=eps_n<=1/n,
    |j|=-log(1-c^2/n^2)<=1/(4n^2-1),
    |eta_+|,|eta_-|<=1/(2n-1).

The sum of both tails is at most
[|Z_n|+B0(log(n+1/2)+2)]/[4(n-1/2)^2]. These bounds give Bmesh
exactly, including a=0 where B0=0 literally. No inverse phase occurs.

For Rlog apply centered-cell BV quadrature directly to log(pi-z).
On each of the two ordinary cell unions its variation is at most
log(2m), since its largest distance is below pi and its smallest
distance is at least h/2. Thus the normalized quadrature error is
<=log(2m)/m. The two initial gaps total4h and contribute at most
4log pi/m. The two central gaps have lengths c_L,c_R summing to2h,
each less than1; concavity of x(1-log x) gives their combined
absolute log integral <=2h(1-log h). After normalization its cost is
2(1+log(m/pi))/m. Adding these three terms gives Blog exactly.
Finally E_2=C_2+D0 H2+B0 G2 in(4) proves(7).

## Scope and checks

Equations(1)--(4) express the global surrogate with six exact rows,
the already defined endpoint constants, a bounded number of scalar
h/g and log Gamma values, and the fixed phase coefficients/constant.
This removes the growing OUTER H reference sums mathematically; it
does not give an operation/bit/runtime bound for those scalar values,
the exact rows, or K_0, nor an outward evaluator or a phase cover.
At a=0 all B0 factors are zero literally; no inverse a is used.
At integer weighted offsets one keeps the accepted complete Phi value.

No numerical code, native/board calculation, quadrature, scalar rerun,
fit or source change occurred. The needed next independent test is
review of these exact constants and the separate outer-budget proof.
An eventual useful bound on J_n still requires a separately reviewed
six-row bound; (6)--(7) isolate its scalar complement. Plugging the
old positive e_rows allowance back in would restore D06's obstruction.

2026-11-06, parent-requested Codex Sol xhigh, input
`2e4ac49fa0687a7736bc1df82c12e6483b1c7a94`, within the20min block.
New intermediate only;
old M_far/M_infty/M_near and global thresholds stay frozen.
