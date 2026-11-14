# Independent supplementary review — C05 finite-degree noncorner comparison

Reviewer: distinct Codex `/root/c01_near_review`, parent-assigned Astra high;
serving identity and effective effort are not independently exposed.
Date: 2026-11-06. Rules were read at
`4b728b04216a5490910780bc609a82b853058426`; their unchanged status at
review input HEAD `b6e67b3c78cb668b6d2f9da5a5560537d2960bf3` was checked
in the preceding reviews. Branch: `codex/padua-argmax-bridge-20261105`.

**Disposition: accepted at all three written scopes, with no mathematical
finding.** The direct F_n finite-error increment is bounded as stated;
the unchanged near model is below Lambda_c+1/32 for every n>=10^6;
and the accepted projected-defect premise gives the stated actual
noncorner gap on the radius-half domain. The tighter model tolerance
1/4096 and the global theorem remain OPEN. Formal Claude audit is separate
and remains pending.

## Frozen sources and review method

Reviewed source: `theory/C05-finiteh-model-comparison.md`, SHA-256
`a0a29f76ad72abab9c44684c8793e9a7c500d12abfefce51dab9fcfed7ba5e4e`.
The file was read in full and its identity checked. The following
load-bearing inputs retain their separately reviewed identities:

| Input | SHA-256 |
|---|---|
| C05 exact endpoint increment | `0e8616a3f23ba42ca31b5967d3e9bf44186472b8ff51d105da38c704cba693f7` |
| C02 fixed T and finite component bounds | `a42be2a78546b02eec20326beba872965abc20810b879b70c770ae0d33d2f928` |
| C04 limiting comparison, corrected wording | `3544d01605560ad498e96648841d8ce9c1a4bfbe69e1b94573112995df6aac1a` |
| C02 projected-defect theorem | `d28bbc8f7ae3823ff220b452630b0c30c939b9851fa0c151d2ac5962a301dec7` |
| Accepted C02 defect review | `a435cc44786a4f16903fdcb0563ea435081c36224e357170fabd867e65d73013` |

The full C02 defect source and its accepted review were read for this
assembly. The exact N1-09/10/11/15 model, N1-13/14 regular and central
profiles, N1-16/17 coefficients and normalization, and N1-18 construction
were read for the preceding reports and used here without changing them.
The endpoint increment and limiting comparison were independently
reconstructed in `independent-checks-C05-endpoint.md` and
`independent-checks-C04-near.md` respectively.

The scope is analytic validity and exact dependency matching, with no
historical novelty/priority verdict or full registry/search audit. There
was no kernel evaluation, numerical integral, fit, phase scan, energy
extrapolation or certificate cover. One small standard-library Fraction
check verified the final rational budgets; its exact output is recorded
below and is not a proof premise. Only this new report was written. No
author source, old review, shared file or Git state was changed.

## Exact strip/outer cancellation

The local profile decomposition is correct: N1-10 gives

    H_s/pi=[U0/pi+B0(L+log z)]/z+V_s/pi+E_s/pi,

whose singular term is S'(z). The actual boundary u_s differs from delta
by at most h/2 and lies inside the enlarged interval already treated by
N1-18. Thus its uniform |E_s|<3/1000 bound is applicable.

Set y=log u_s and x0=log pi-L. Since log h=x0-epsilon and
Z_n=D0-B0*epsilon, expansion of the actual singular primitive gives

    Z_n(y-x0+epsilon)+(B0/2)(y-x0+epsilon)²
      =(D0-B0*x0)y+(B0/2)y²-D0*x0+(B0/2)x0²
          +D0*epsilon-(B0/2)epsilon².

The y-dependent part is exactly S(u_s), because
D0-B0*x0=U0/pi+B0*L. All cross terms involving L*epsilon cancel.
This proves (6) without replacing m by n inside a logarithm.

Also u_s-l_s=h(K_s-R+1), so U_s*N_s/m equals the exact
normalized integral of U_s over that strip. The derivative with respect
to the common boundary of the strip plus its outer integral is therefore
S'+V_s/pi-H_s/pi=-E_s/pi. Moving the actual boundary to delta
gives exactly the signed expression (7). Its two-side absolute cost is
below 3/(1000m), not a term proportional to L or delta^-1. The collision
holes are near pi, so none is crossed in this local boundary movement.

The retained h_J terms have coefficient Z_n, yielding an additional
-B0*epsilon*H_J. Together with the two copies of the constant in (6),
the entire finite-epsilon term is precisely
epsilon*(2D0-B0*H_J)-B0*epsilon². The bounds |D0|<4,
|H_J|<12, B0<=4/9 and epsilon<=1/n give absolute size below 14/n.
The g_J coefficient is unchanged, so there is no hidden truncation error.

At epsilon=0, the singular contribution on each side has polynomial
part (B0/2)L²+(D0+B0*k)L and constant D0*k+(B0/2)k².
Adding the actual finite h_J,g_J constants produces exactly the stated
T constant. Adding the full regular-strip and outer A integrals then
gives precisely N1-16's b_M. No residual logarithmic coefficient is lost.

## Paired lower strip boundaries

The remaining lower-boundary discrepancy is exactly (9). Here
|l_L-l_R|<=h, and both l_s lie strictly between 1/n and 1 for the
stated degree range. The derivative of z log z-z between them has
magnitude at most L. Thus opposite U_s coefficients cost at most
4/m, and opposite q_s coefficients in the logarithmic term cost
L/(2pi*m). The q_s part of the regular A coefficient costs the same
L/(2pi*m). Bounding the two integrals separately would lose this
cancellation; the submitted proof pairs them correctly.

The common u_a part satisfies |u_a(z)|<=pi*z/6 on the actual lower
intervals. With max l_s<516/n its normalized cost is below
15000L/n²<L/(60n). Consequently all lower regular losses fit
[4+(7/20)L]/n. Adding the seam and epsilon terms gives

    [18+3/1000+(7/20)L]/n<5(L+1)/n.

The last inequality holds for L>=3, and n>=10^6 is well inside that
domain. This verifies the first rest-error allocation without carrying
over C02's coarse independent strip/outer absolute bounds.

## Central ends, collision holes and actual special rows

For each folded side the upper ordinary endpoint is
h(m-3/2+t_s). Its distance from pi is h(3/2-t_s); the two distances
sum to exactly 2h. Noncentral collision cells add at most 2h in total.
The permanent central rows are already excluded by these upper endpoints
and are not counted again as holes. Coincident collision indices are
merged as in N1-15. Therefore the complete removed ordinary set has
measure at most 4h on the two folded copies.

Every such set lies in z>pi-1/2-h/2>5/2, so epsilon0=pi-z<1.
The exact max formulas give |A_s|<1: even the larger q+2a cot(z/2)
is below 5/2 before division by pi. The pole part is below five
because |N_s|<=8 and sin(z/2)>4/5. Finally N1-14 gives
I_s=d log epsilon0+Z_s, d<=1/2 and |Z_s|<3. Division by pi
therefore yields the full bound

    |H_s|<L+6+(-log epsilon0)/6.

The two-copy rearrangement bound M[1+log(2/M)] applies to the complete
removed set, including intervals that touch epsilon0=0. It increases
for M<2, and M<=4h together with m/(2pi)<n gives an upper bound
4h(L+1). Including the model's outer normalization 1/pi yields

    [4(L+6)+(2/3)(L+1)]/m<10(L+1)/n.

The same construction includes the beta=0 central row without assigning
separate infinite cotangent values to it: that row remains special and
only its omitted improper integral is bounded here.

There are at most four actual nonendpoint special rows. Their exact
normalized polynomial rows are each bounded by 2(L+5)/m. The whole
Rhat/H8 discrepancy is less than 1/n at a phase, so the actual model
special-row sum has absolute value below
[8(L+5)+1]/n<50(L+1)/n. This includes both permanent central
rows, all noncentral collision rows, merged duplicate indices and all
prescribed H8 branches. Their removed integrals were separately charged
in the preceding paragraph, as required by the actual model definition.
There is no additional collision-mark envelope to add to these charges.

## Jump term and direct F_n identity

C02's independently reconstructed jump component bound applies to the
unchanged M_jump: its error from the exact signed limiting q_R expression
is below 10(L+1)/n. That proof retains m/n, both actual half-cell cutoffs,
the finite harmonic constant and both W_b integrals. It covers the beta=0
half-angle cutoff as part of the pointwise model expression. No extra
half-angle step allowance is required here.

Collecting the terms now gives an exact decomposition

    R_n-T=E_end+E_rest,
    |E_rest|<75(L+1)/n.

The rest allocations are 5 for the paired strip/lower-boundary terms,
10 for all omitted ordinary integrals, 50 for the actual special rows,
and 10 for the finite jump error. The endpoint term is exactly the
previously reviewed E_end, without any part of its old absolute row
approximation error added again.

Subtract the identity at the origin. The endpoint theorem gives
45000r²/n+40beta/n, and two pointwise rest errors give
150(L+1)/n. Thus the displayed increment inequality (1), with its
relaxed coefficient 200, follows for the actual F_n. It covers all
floor values and collision loci because their terms were included
pointwise before subtraction.

This argument never invokes Q_n or removes its artifacts. N1-18's
9/(2n) is therefore not a term in this direct F_n estimate. A later
conversion to Q_n would use that separate allowance once. No such
conversion is needed for the present model or noncorner conclusions.

## Model comparison and actual noncorner consequence

The accepted C04 theorem bounds T(phase)-T(origin)-G_n by
1/50000+3/(2*10^9) for every n>=10^6. Combining this with the
new direct F_n bound is legitimate; pointwise convergence is not used
as a substitute for finite-degree control.

N1-17's exact origin identity includes
M_near(0,0,L)-Lambda_c<3/14000. On rho<=1/2, r²<=1/4
and beta<=1/2, so the endpoint allowance is at most 11270/n.
The function (1+log n)/n decreases for n>1, and log(10^6)<14.
The total upper budget in (19) is consequently

    3/14000+1/50000+3/(2*10^9)+11270/10^6+3000/10^6
      =203060021/14000000000 <1/32.

This proves the actual model comparison uniformly for every integer
n>=10^6, including both parities and the zero phase. It is the larger
1/32 tolerance, not the tighter 1/4096 tolerance.

The accepted C02 defect theorem applies to every physical odd center
J+K odd with at least one interior center coordinate, under physical
angle membership and |alpha|+|beta|<=1/2. Its hypotheses are thus
exactly every stated noncorner odd center; no actual corner is included.
For n>=10^6 its n>=4096 floor gives Delta>1/16. Its exact normalized
primitive satisfies lambda=S_n-Delta. N1-15 provides the additional
phasewise S_n<M_near+3/14000 estimate in the same corrected-kernel
normalization. Therefore

    lambda<Lambda_c+1/32+3/14000-1/16
          =Lambda_c-869/28000.

The origin representation allowance and the phasewise S_n allowance
serve different comparisons and are both legitimately retained. No sum
of two projected floors, mesh interchange or finite-energy premise is
used. Separate phase evenness of the primitive extends the model bound
to the signed phases admitted by the physical defect theorem.

For a whole phase box, the full radius guard remains necessary:
maxabs(alpha interval)+maxabs(beta interval)<=1/2. Merely intersecting
that triangle would not justify applying this result to the entire box.

## Executed exact scalar check

A single inline standard-library Python Fraction invocation exited zero.
It evaluated the budget above and checked positivity of its slack below
1/32, the exact noncorner deficit, and the two elementary lower-boundary
comparisons at n=10^6 and L=3. Its exact output was:

    model budget: 203060021/14000000000
    strict slack below 1/32: 234439979/14000000000
    physical noncorner deficit: 869/28000
    paired-boundary scalar checks: PASS

The checks were `slack>0`, `deficit==Fraction(869,28000)`,
`Fraction(15000,10**6)<Fraction(1,60)`, and
`18+Fraction(3,1000)+3*Fraction(7,20)<20`.
No phase or degree search was performed. This elementary arithmetic
check supplements the analytic reconstruction rather than supplying
any unproved reduction or computational premise.

## Findings and limits

No BLOCKING, MAJOR or MINOR finding in the frozen C05 assembly. No
author repair was made or required before acceptance. This is an actual
finite-degree near noncorner exclusion for n>=10^6, derived from the
larger accepted defect budget. It does not establish the tighter C1
model tolerance, the proposed 1/250000 finite-Q_n error, actual corner
comparison, far phases, the finite degree gap or the global all-n theorem.
Certified degree and finite-energy ranges are unchanged. Required Claude
formal audit remains pending.
