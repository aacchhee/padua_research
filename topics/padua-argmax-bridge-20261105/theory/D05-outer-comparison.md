# PD-T?argmax-bridge-codex-D05-compare — Joint outer comparison without a cutoff floor

ID kind: PD-T. Aliases: signed endpoint residual assembly; fixed-strip
joint M_infty rate; D04 intermediate to completed constant.
Split from: D04 practical joint finite-degree target. Split into: none.
The practical size/onset obligation remains in that OPEN target.

## Statement and exact scope

Use exactly the corrected polynomial S_n, special set A_R, ordinary
set O, actual weighted H profile, and K_D04 of D04-row-reduction.md.
Use the unchanged D02 model

    M_infty(alpha,beta,L)=(4a/pi^2)L^2+b_full*L+C_infty,
    C_infty=E_infty+K_0,

with its continuous weighted products at all boundary phases. For

    alpha,beta>=0, alpha+beta<=pi,
    integer R>=2, 0<delta<=pi/8,
    integer n>=ceil(2pi R/delta), m=n+1, L=log n,

the explicit comparison is

    |K_D04(n,R)-M_infty(L)| <= e4+I_n+D_pole+T_Z,       (1)
    |S_n-M_infty(L)| <= E_D04+e4+I_n+D_pole+T_Z.        (2)

Every term is specified below. In particular R=2,delta=pi/8 applies
for every integer n>=32. For each fixed such R,delta, the right sides
are uniformly O((1+log n)/n) on the full closed phase diamond. There
is no nonshrinking R or delta floor.

Status: **PROVED**, written analytic developer result, distinct review
pending. Equations (1)--(2) are explicit pointwise analytic bounds.
No useful numerical onset, phase-cover result, argmax comparison or
global degree threshold is asserted. The practical small-onset target
is still **OPEN**: the constants here retain the conservative existing
interior I_n bound. A verified useful scalar/phase budget would be a
separate obligation, not a consequence of the asymptotic notation.

## Exact error definitions

Let a,p,q,P,U0,d be exactly D05-outer-profile-variation.md's quantities,
and H_n=sum_(j=1)^n 1/j. The accepted D04 error is

    E_D04={ [52a/pi^2+352P/(3pi)]H_n+7a+2P/pi }/n
                                  +10/n^2+20a H_n/(pi*n^2).

T_Z is exactly formula (TZ) of D05-outer-profile-variation.md, at these
same R,delta,n. Its floors are not relaxed in its proof. In particular
it compares the ordinary signed residual with its full strip integral,
rather than bounding the two separately by Q(P,delta).

For clarity all older scalar terms used in (1) are restated. These are
the same N1-06/07/08 and D02-uniform-limit bounds on their actual domain;
their old definitions and models are unchanged. Put

    X=delta*m/pi,
    HR=log(R+1/2)+1/[8(R-1/2)^2],
    CX=[5+(1/2)log(X+1/2)]/[2(X-1/2)]
                  +[6+(1/2)log(X+1/2)]/[8(X-1/2)^2],
    e_mesh=(2R+3)L/(2m)+2CX+(8+HR)/n+1/(2n^2),
    e_row=(10R+39+6L)/n+200(R+2)(R+1)^2/n^2,
    e_rows=(4+L)/n+(2R-1)e_row,
    e_collision=(2/m)[7+(2/pi)(3+2log(4m/R))]
                                      +5/(n^2*m)+1/(nm),
    e4=e_mesh+e_rows+e_collision,
    D_pole=10/n^2+20a(1+L)/(pi*n^2).

For the complete interior bound define

    u=p/2, sbar=1/2+4a/delta, f=log(pi/delta),
    G=2u[1+log((sbar+u)/u)] if u>0, G=0 if u=0,
    Astar=(1+8a/delta)/pi, VA=16a/(pi*delta),
    Vstar=2|U0|/delta+6, VV=4|U0|/delta+23,
    Jstar=max(5,2sbar*f+max(2u,sbar+u)log2),
    VJ=(16a/delta+4sbar)f+3G+2(sbar+u)log2+20,
    Wstar=Vstar+Jstar/pi, VW=VV+VJ/pi,
    I_n=[(VA/2+9Astar)L+VW/2+5Wstar+4Vstar
                             +(d/pi)(4+5log m)]/m.    (3)

All quantities have continuous finite phase limits at a=0, p=0,
axes and vertices. G uses its continuous zero limit, not division by
a vanishing parameter. Separate absolute phases extend the conclusions
to |alpha|+|beta|<=pi; the n,m meshes are never interchanged.

## Dependencies and proof

Dependencies: D05-outer-profile-variation.md's signed strip corollary;
N1-08 exact endpoint block with N1-06/07 errors; D02-far-uniform-limit.md
sections 1--2 for (3)'s actual interior topology; C06-far-full-profile.md
for the exact coefficient integration; D02-far-bias-identity.md for the
signed completed constant; accepted D04-row-reduction/reference-matching
for K and Delta_R. D04 distinct acceptance is recorded in
independent-checks-D04-row-reduction.md, SHA256
`cacbab625421e4d269bc2a3047aa523caee8c4f08a709748721291178f9976d7`.

### 1. Exact partition and endpoint block

Let z_r=min(v_r,2pi-v_r), and D=(delta,2pi-delta). The degree condition
puts every first/last R row strictly in z_r<=delta. The central rows
r=m-1,m are in D. Define X as all exact special rows in z_r<=delta,
and Y as the ordinary rows there. Define the unchanged N1-08 block

    E=(1/(nm))sum_(r in X) R_r
         +(1/m)sum_(r in Y) [A(v_r)L+S0(z_r)],
    S0(z)=[U0+(4a/pi)log z]/z.

The exact endpoint contribution to K before Delta_R is added equals

    E+(1/m)sum_(r in Y) Z_B(v_r),
    Z_B(v_s(z))=Z_s(z)=B(v_s(z))-S0(z).               (4)

This is an algebraic identity: endpoint collisions in X stay as actual
polynomial rows, and occur in neither residual sum. The signed strip
corollary bounds the difference between the residual sum in (4) and

                   J_Z=(1/pi)integral_0^delta(Z_L+Z_R)dz

by T_Z, retaining the actual shifted floors and at most two deleted
collision samples. N1-08 gives

    |E-[B0 L^2+b_end L+C_R+c_mesh]|<=e4.              (5)

Its proof and exact collision limits are unchanged. Our smaller strip
domain delta<=pi/8 lies inside its original delta<=pi/4 domain.

### 2. Interior rows, including every exact special row

Write the interior contribution to K as

    J_int=(1/m)sum_(r in O, v_r in D) H(L,v_r)
                  +(1/(nm))sum_(r in A_R, v_r in D) R_r.

There are at most four exact special rows here. The proof in D02's
uniform-limit theorem section 2 applies directly and gives

    |J_int-(1/pi)integral_D H(L,v)dv|<=I_n+D_pole.     (6)

To specify exactly what is inherited: ordinary H rows are already
profiles here, so no ordinary-kernel E_n or D_n error is charged.
Centered-cell variation pays (VA*L+VW)/(2m). Up to four missing
special cells and two boundary pieces of total length <=h pay
5(Astar*L+Wstar)/m. Actual special norms pay
4(Astar*L+Vstar)/m plus their weighted single-pole profile errors.
Those errors are a subset of the full D_pole bound; charging its full
value is conservative. Finally the central d*ell/pi quadrature and
missing cells pay (d/pi)(4+5log m)/m. Their sum is precisely (3).

This argument uses the accepted finite-polynomial continuity upper
bound for the exact central/collision rows, not H evaluated as their
actual value. Cells crossing a changed collision membership are not
inferred from a phase center; the statement is pointwise and uses each
phase's literal special set. It includes axes and the boundary.

### 3. Signed constant cancellation

The exact C06 coefficient integration joins b_end to b_full. The exact
constant algebra of the unchanged endpoint block gives

    C_R+c_mesh+(1/pi)integral_D B(v)dv=E_R+K_delta.

D04 defines Delta_R=E_infty-E_R with its sign. D02 proves

    K_0-K_delta=J_Z.

Consequently the sum of the polynomial in (5), the integral in (6),
J_Z, and Delta_R is EXACTLY

    B0 L^2+b_full L+E_R+K_delta+J_Z+Delta_R=M_infty.

Combining (4)--(6) proves (1). Combining (1) with the accepted D04 row
reduction proves (2). There is no appeal to a fitted limit and no
transfer of the old M_far quantifier or error claim.

For fixed R,delta, X is proportional to m, so CX=O(log n/n).
Every e4 term has the same or a smaller rate. The interior constants
are uniformly bounded on the compact phase domain (including the
continuous p=0 entropy limit), so I_n=O((1+log n)/n). Formula (TZ) of
the companion proof gives the same rate for T_Z. E_D04 and D_pole
also have that rate or a smaller one. This proves the uniform rate
claim without substituting a shrinking delta into any old bound.

## Checks, limits and remaining work

This theorem supplies an explicit full-phase pointwise rate and the
requested comparison of K to the completed model. It does not establish
that this conservative right side is below a useful argmax budget at
10^3--10^4, nor compare its phase-relative version with a corner norm.
The practical target in D04-practical-target.md remains OPEN under
that stronger size/onset requirement. A next gated step can improve
(3) by the new combined-profile variation, retaining every singular
reference and exact special cell, or evaluate the explicit bound with
validated scalar arithmetic under a separate resource contract.

The original fixed-cutoff M_far still has D02's exact nondecaying bias.
No old proof body, source, model correction, degree certificate,
producer, global threshold or quantifier changes. No kernel/native/
board/quadrature/fitting/numerical code run was executed; all checks
here are written analytic identities and inequalities. New D05 claims
await distinct review.

History: 2026-11-06, parent-requested Codex Sol xhigh, input
`a6d7a788b3ce457a4631bbb507624303240c570c`. The original practical
target's wording and OPEN status are retained; this result splits off
the explicit floor-free comparison without a practical-size claim.
