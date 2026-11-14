# PD-T?argmax-bridge-codex-D35-near — Complete near allowance with coefficient-six ordinary perturbation

ID kind: PD-T. Aliases: D22/D25/D31 allowance with sharpened ordinary rows.
Split from: D35 ordinary perturbation application. Split into: none.

## Statement and exact definitions

For every integer n>=32 let m=n+1,L=log n,H=1+L. Use EXACTLY D22/D31's
actual corrected primitive S_n, D02's completed M_infty, the fixed six
labels A6={0,1,2m-2,2m-1,m-1,m}, and D16's actual-origin allowance E0(n).
For signed phases rho=|alpha|+|beta|<=1/2 put

    a=(cos|alpha|+cos|beta|)/2, u=1-a,
    Cnear=22/n+162/n^2+40H/(pi*n^2),
    K35=[8H+(39/2)L+286/3]/n+4/n^2.

Then on the entire CLOSED signed near diamond,

    S_n(phi)-S_n(0)
      <=M_infty(phi,L)-M_infty(0,L)+Cnear+K35*rho+u E0.    (1)

Cnear and K35 are positive and decreasing for every real n>=32.
Overall status: **PROVED**, complete analytic developer assembly;
distinct review required. No scalar or new onset is asserted.

## The exact operator and every charge

Use the same D22/D31 quantities

    Erow=S_n-K_fixed, Eout=K_fixed-G_n, Eret=J6-C2,
    delta_a X=X(phi)-a X(0), E=S_n-M_infty,
    d=(sin|beta|-sin|alpha|)_+.

Here G_n is D07's intermediate, distinct from the corrected kernel
polynomial. Its exact accepted telescope is

    delta_a E=delta_a Erow+delta_a Eout+delta_a Eret
                                      +delta_a Rmesh+(d/pi)Rlog.  (2)

At collision-free phases, D22 section2 splits Erow into the ordinary
perturbation (T-T0), the symmetric endpoint/central reference, and
weighted pole errors. At the actual origin P=0, so T-T0 is EXACTLY zero.
For the actual phase, D35-ordinary-perturbation bounds that term by
6P H_n/n<=6rho H/n. D22's other terms remain literally unchanged. Thus

    delta_a Erow<=4a/n+20/n^2+40aH/(pi*n^2)
                                      +rho[6H+2H+10]/n.          (3)

The 4a/n pays the whole central reference complement with both parity
transition rows. The next two terms pay both absolute weighted-pole
errors. The (2H+10)rho/n charge is D13's complete endpoint reference
increment including all of Delta_2. No term is counted as relative
without its accepted proof. The COMPLETE Erow is continuous by D05,
and collision-free phases are dense; hence (3) extends to every phase
by D22's same complete-expression limiting argument. Individual
cotangent/reference samples are not extended through collisions.

D22's retained-row and singular-mesh bounds, and D25's exact shifted
outer operator with every cell removal and actual-origin mesh shift,
give unchanged

    delta_a Eret<=[18a+P(8+L)]/n+(142a+4P)/n^2,
    |delta_a Rmesh|+(d/pi)|Rlog|<=rho(L+7/3)/n,
    |delta_a Eout|<=rho[(35/2)L+75]/n.                       (4)

The nonnegative subtracted origin central rows have only the one-sided
treatment justified in D22. All four actual endpoint rows, both central
rows, the highest corrected mode and the unequal meshes are preserved.

Insert (3)--(4) in (2), use a<=1 and P<=rho, and collect terms. The
constant is unchanged:

    (4+18)/n+(20+142)/n^2+40H/(pi*n^2)=Cnear.

The linear coefficient is

    [8H+10+(8+L)+(L+7/3)+(35/2)L+75]/n+4/n^2
                      =[8H+(39/2)L+286/3]/n+4/n^2=K35.

Finally E(phi)-E(0)=delta_a E-u E(0). D16 bounds the SAME actual-origin
error by |E(0)|<=E0; therefore -uE(0)<=uE0. This proves (1), keeping
the full origin-conversion charge.

## Monotonicity, dependencies and limits

Cnear has the unchanged D31 positive inverse-power and H/n^2 terms.
For K35, write it as (cL+b)/n+4/n^2, with c=8+39/2 and b=8+286/3.
Since b>c>0, its derivative has numerator c-cL-b<0 for L>=0, plus
-8/n^3. This proves the stated real-n decrease.

Dependencies: D35-ordinary-perturbation; accepted D22-origin-reduction,
D25-outer-relative, D31-relative-allowance, and their unchanged D13,
D16 and D05 inputs. The only new mathematical estimate is D35's
ordinary coefficient6. All other terms of D31 are retained exactly.

Cnear is nonzero, so D13's complete vanishing relative target remains
OPEN. A physical noncorner exclusion additionally needs the appropriate
defect floor and a proved model comparison; actual corners and far
phases remain separate. This supporting allowance does not extend any
accepted degree range and does not alter a frozen scalar recipe/source.
No numerical/native/root/quadrature/threshold job was run. Written
2026-11-06 in the bounded D35 paper block, input/rules
eb9329c28be18d77eeb817f634202d626ee11f92, requested Astra ultra;
serving metadata unexposed. Gate/attempt: the D35 ordinary records.


## Root review closure — 2026-11-06

Distinct adversarial [D35 review](../independent-checks-D35-ordinary.md), SHA256 `781e1077eb52c87e4f9f1718a0d658c3f8a342b0db3733c15c8ac1851c31083e`, accepts all three frozen scopes without unresolved findings. Root adopts the6PH_n/n ordinary perturbation, its fixed-row application and complete near allowance at their exact stated domains/exclusions. All pole jumps, roots, actual shifted-grid sampling and unchanged Cnear/uE0 charges were reconstructed. No new onset or numerical job follows from this support alone; D13 full relative remains OPEN. Reviewed prefix is preserved; final Claude audit is separate.
