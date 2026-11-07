# PD-T?argmax-bridge-codex-D35-fixed — Fixed-row reduction with the sharper ordinary charge

ID kind: PD-T. Aliases: D04/D05 coefficient-six application.
Split from: D35 ordinary perturbation application. Split into: none.

## Statement, definitions and status

For every integer R>=2 and n>=8R, let m=n+1 and use EXACTLY D05's
corrected polynomial primitive S_n, weighted profile H(log n,v),
continuous Delta_R, fixed special labels and intermediate model

    A_fixed={0,...,R-1} union {2m-R,...,2m-1} union {m-1,m},
    O_fixed={0,...,2m-1} minus A_fixed,
    K_fixed=(nm)^(-1) sum_(r in A_fixed) R_r
                         +(1/m) sum_(r in O_fixed) H(log n,v_r)+Delta_R.

All definitions are literally those of D05-fixed-special-rows equations
(1)--(4), including the original corrected highest first-coordinate mode,
finite polynomial collision values, periodic weighted Phi, the exact
bounded integral I(C,D,v), and unequal n,m meshes. With

    a=(cos|alpha|+cos|beta|)/2,
    P=sin|alpha|+sin|beta|, H_n=sum_(j=1)^n 1/j,

on the entire CLOSED signed phase diamond |alpha|+|beta|<=pi one has

    |S_n-K_fixed|<=E35,
    E35={ [52a/pi^2+(6+16/(3pi))*P]H_n+7a+2P/pi }/n
                                  +10/n^2+20a H_n/(pi*n^2).       (1)

The model is unchanged. Only the proved coefficient in its error bound
is decreased. For R=2 the statement holds for every n>=16 and retains
the same six exact polynomial rows.

Overall status: **PROVED**, analytic developer corollary. Distinct review
required before adoption. No scalar premise, implementation or onset.

## Proof with all charges retained

First work at a phase in the first quadrant with no polynomial collision.
The D04 exact row decomposition and D05 model identity give

    S_n-K_fixed=(nm)^(-1) sum_(r in O_fixed) T_r+Epsilon-Delta_R,
    |Epsilon|<=10/n^2+20a H_n/(pi*n^2).                 (2)

The weighted pole approximation in (2) is unchanged. The actual special
rows are exact. Subtract the same bounded symmetric reference T0_r.
D35-ordinary-perturbation applies to this exact ordinary set and gives

    |(nm)^(-1) sum_(r in O_fixed)(T_r-T0_r)|<=6P H_n/n. (3)

D04-reference-matching, with its original endpoint omissions, half-line
defect, central complement and Delta_R, gives unchanged

    |(nm)^(-1) sum_(r in O_fixed)T0_r-Delta_R|
            <={[52a/pi^2+16P/(3pi)]H_n+7a+2P/pi}/n.   (4)

Adding (2)--(4) proves (1) at those collision-free phases. No reference
row or endpoint term has been replaced by (3).

For fixed n,R, D05 sections1--4 prove that S_n and the COMPLETE K_fixed
are continuous on the closed phase triangle: weighted pole products
have their periodic finite limits, the cancellation integrals have a
uniform integrable majorant, actual rows are finite polynomial norms,
and Delta_R converges uniformly. Collision-free phases are dense because
all collisions lie on a finite union of affine lines. E35 is continuous.
Pass to the limit in the COMPLETE inequality (1). This does not pass
T0_r, unweighted cotangent samples, or a single pole error through a
collision. Separate absolute-phase extension gives the signed diamond.

## Dependencies, scope and checks

Dependencies: D35-ordinary-perturbation; D04-row-reduction and its accepted
reference-matching/half-line proof; D05-fixed-special-rows continuity.
These predecessor models and proofs are unchanged. D35 replaces only
D04's old 112P H_n/(pi*n) ordinary perturbation by6P H_n/n. Every actual
root, collision and removed endpoint retains the original treatment.

No compact-profile comparison or argmax conclusion follows from (1)
alone. The direct outer model remains degree-dependent; no runtime bound
is asserted. Paper proof only, 2026-11-06 bounded D35 block, rules/input
eb9329c28be18d77eeb817f634202d626ee11f92, requested Astra ultra with serving
metadata unexposed. Gate/attempt are the D35 ordinary records.


## Root review closure — 2026-11-06

Distinct adversarial [D35 review](../independent-checks-D35-ordinary.md), SHA256 `781e1077eb52c87e4f9f1718a0d658c3f8a342b0db3733c15c8ac1851c31083e`, accepts all three frozen scopes without unresolved findings. Root adopts the6PH_n/n ordinary perturbation, its fixed-row application and complete near allowance at their exact stated domains/exclusions. All pole jumps, roots, actual shifted-grid sampling and unchanged Cnear/uE0 charges were reconstructed. No new onset or numerical job follows from this support alone; D13 full relative remains OPEN. Reviewed prefix is preserved; final Claude audit is separate.
