# C02 half-diamond actual-corner bound: independent reconstruction

Rules read at `4b728b04216a5490910780bc609a82b853058426`. Reviewer: distinct Codex supplementary reviewer, allocated gpt-6-astra high; serving model/effort metadata unexposed. Date: 2026-11-06.

Frozen proof: `theory/C02-corner-halfdiamond.md`, SHA256 `57c729c91a1641d00fe93519a1a5c17d341a322775d215868da6653e9fdedf6c`.

**Verdict: ACCEPTED**, no unresolved finding. For n>=64, both actual nonnode corners and every inward rho<=1/2, the stated bound lambda<=a Lambda_c+24000rho^2 log(n+1) is supported. Strictness on the punctured patch follows under Lambda_c>240000log(n+1), with the sufficient explicit condition log n>=610000. This is a direct pointwise corner theorem, not a global localization or energy-bootstrap conclusion. Executable use and formal Claude audit require their separate reviews.

## Scope and inherited identities

Read the full frozen proof and its C02 candidate/attempt scope. PD-T221, PD-T228, PD-T157 and the exact PD-T215/364 conventions were read in full earlier in this review session. The new half-radius geometry, all derivative constants, the collision-family bounds and the full orbit assembly were independently reconstructed here. No radius-1/64 geometric estimate is silently transferred to radius 1/2.

Historical novelty, priority and completeness of the author's gate are excluded; the full IDEAS novelty audit is not invoked. No sampled phase, numerical kernel, finite-degree sweep, energy receipt or empirical sign-stability statement is a premise.

Reflecting original node indices (p,q) to (j,r)=(n-p,m-q) maps the even physical board to the odd board and preserves endpoint weights. Separate angular evenness and periodicity reduce the four kernel copies to F_jr at the four signed phases. Their factor (-1)^j is common. The exact normalization is therefore

    lambda=(1/N) sum e_j f_r |sum_four F_jr|,
    Lambda_c=(4/N) sum e_j f_r |F_jr(0,0)|.

Absolute values occur after each cardinal's fourfold sum. Endpoint duplicate copies and half weights are both retained. The zero initial row r=m,j<n stays in the sum, and the (n,m) collision has the finite polynomial value F0=n. These identities impose no nonvanishing or sign-stability assumption.

## 1. Plus-angle separation on the larger radius

For the regular set R, odd parity implies L=|j-r|>=1. The only same-endpoint odd pair (n,m) lies in the removed family B, so d=min(j+r,2n+1-j-r)>=1. The base half-sum has distance at least pi d/(2m) from both 0 and pi. A signed phase with |gamma|+|delta|<=1/2 changes it by at most 1/(4n). The sine chord bound gives

    b>=d/m-1/(2pi n)>=(d-65/(128pi))/m>=5d/(6m).

The last inequality uses d>=1 and pi>195/64; the proof's pi>25/8 is stronger. Hence P remains strictly inside (0,pi), including all closed half-diamond boundaries and endpoint overshoots.

## 2. Difference-angle separation, especially r=j+1

The perturbation of u-v has magnitude <=1/(2n)<=65/(128m).

- For j>r, the base gap is >=pi L/m. It remains >2L/m after perturbation.
- For r-j=L>=3, the base gap is >=pi(L-1)/m. Using L-1>=2L/3 gives a remaining gap >(2-65/384)L/m>(9/5)L/m.
- The remaining r=j+1 case must be checked separately. Membership in R gives h=n-j>n/3, hence the base gap exceeds pi/(3m). Therefore |T|>[pi/3-65/128]/(2m)>205/(768m). Its upper bound is <5/(2m)<=1/26. Taylor's sin x>=(99/100)x on this interval gives t>20295/(76800m)>1/(4m); the exact slack in its coefficient is 73/5120.

In the first two cases |T|<=pi/2+1/256<8/5 and sin|T|>=(3/5)|T|. The endpoint chord comparison follows from sin(8/5)=cos(8/5-pi/2)>24/25. Those two cases therefore also give t>=L/(4m), with ample slack. Every regular denominator stays nonzero throughout the entire signed half diamond. This independently checks the delicate unremoved r=j+1 class rather than assuming the old radius bound persists.

## 3. Endpoint overshoots and sine numerators

When both shifted angles are in [0,pi], sin u,sin v<=2sin((u+v)/2). An overshoot can occur only at a mesh endpoint. If just one coordinate overshoots, complementing both angles when necessary gives -epsilon and w in [0,pi], with epsilon<=1/(2n). The other base index cannot be at the same endpoint on R; consequently w>=(pi-1/2)/m and

    epsilon/w<=65/[128(pi-1/2)]<1/5.

Thus b=sin((w-epsilon)/2)>=(4/5)sin(w/2), so sin w<3b. The overshooting sine is at most epsilon<5/(6m)<=b. If both coordinates overshoot, they must be at opposite endpoints; P stays within 1/(4n) of pi/2, hence b>1/2 and both sine magnitudes are <2b. This exhausts all endpoint cases without assuming the corrected kernel is symmetric in its coordinates. It proves the uniform bound |sin u|,|sin v|<=3b used in the derivatives.

## 4. Derivative constants and finite multiplicities

The signed corrected numerator gives F=a f-(sin gamma/2)g_u+(sin delta/2)g_v, with f=(1+cos v)/(cos u-cos v). Direct quotient differentiation using |sin u|,|sin v|<=3b gives

    |f_i|<=2b^-1 t^-2,
    |f_ij|<=8(b^-2 t^-2+b^-1 t^-3).

For example f_u has numerator (1+cos v)sin u and coefficient at most 3/2 in the first bound. A pure second derivative has coefficients at most 1/2 and 9/2; the mixed derivative has at most 9/4 and 9/2 after using b<=1. These lie below the displayed constants. The identities g_u=-(cot T+cot P)/2 and g_v=-(cot T-cot P)/2 give the three g majorants stated in the proof. All derivatives are of signed smooth functions, not cardinal absolute values.

For fixed absolute L and d the physical board multiplicity is <=4. Enlarging the positive sums to all 1<=L,d<=m and using b>=5d/(6m), t>=L/(4m) gives the exact unnormalized coefficients

    768/5 for m^3 H,
    9216/25 for m^4,
    3072/5 for m^4 H.

After the derivative coefficients, 1/N normalization and phase scaling, these give

    (1536/5)(65/64)^2=2535/8<320,
    8(24576/25)(65/64)^3=32955/4<8240.

For the g channels, fixed-L count <=2m and fixed-d count <=4m give unnormalized majorants 16m^2H, 96m^3 and 320m^4. The normalized constants 24H, 216 and 1080 follow using m/n<=3/2. These are termwise uniform bounds on the same signed half diamond, so they can be integrated along paths before summation without a hidden supremum estimate.

## 5. Absolute orbit remainder, including initially zero cardinals

For E(s)=F(s alpha0,s beta0)-a(s alpha0,s beta0)F0, on R one has F0=f0 and E(0)=0. The physical angular speed is <=rho/n and |a'|,|a''|<=rho^2/2. Integration of the first derivative bound gives the stated 320rho H bound for f(s)-f0. Differentiating a(f-f0) twice gives 160rho^3H+320rho^3H+8240rho^2H.

Each sine channel contributes at most 12rho^3H+216rho^2+540rho^3. Its scalar coefficient, first derivative and second derivative are bounded respectively by rho/2, rho/2 and rho^3/2; the g derivatives are scaled by the physical path speed. With two channels, rho<=1/2 and H>=1, the total is at most 9464rho^2H<9500rho^2H.

The symmetric Taylor formula has total remainder weight one for each opposite phase pair. Two such pairs give the absolute fourfold remainder <=19000rho^2H after normalization. This bounds |sum_four E|, exactly the quantity needed in the cardinal triangle inequality. It never assumes F0, F, a numerator or a cardinal is nonzero or keeps its sign; the initial zero row is therefore included.

## 6. Removed collision family, with finite identities

On B, h=n-j is in [0,n/3]. The signed phase geometry gives |X_B|<=pi/3+1/(4n)<1.1 and |T_B|<=pi/(6m)+1/(4n)<1.1. The factorization can be checked directly: U_m-U_n=V_n, so

    U_m(X)U_m(T)-U_n(X)U_n(T)
       =V_n(X)U_m(T)+U_n(X)V_n(T).

Reflecting u,v from pi supplies the common factor (-1)^n. This establishes the stated D_n identity with the exceptional cosine correction still handled separately. U_k is its finite Fourier polynomial even at a sine zero, with q-th derivative bounded by k^(q+1) for q=0,1,2.

On |z|<=1.1, sec(z/2), its first derivative and its second derivative are bounded by 5/4, 5/8 and 1. Product differentiation then gives |V_n|<=5/4, |V_n'|<=2n, |V_n''|<=3n^2; the explicit second-derivative coefficient is 191/64<3. No quotient singularity occurs in this compact interval.

Each first phase derivative of X_B,T_B is <=1/(2n), and their second phase derivatives vanish. The product-rule Hessian coefficient is

    (n/4)[3r_*+4r_*^2+(5/4)r_*^3+33/4]
       <=831n/128, r_*=m/n<=3/2.

The first three terms come from V_n U_m; 33/4 comes from U_n V_n. Including the corrected cosine and the factor 1/2 yields |F_ij|<=4n. The direct value estimate gives |F0|<=2n. Thus |E''|<=5n rho^2, and two phase pairs over at most n B indices give normalized cost <=10rho^2. The h=0 endpoint, repeated orbit copies and all collisions are covered by the same finite-polynomial calculation. No positivity or energy assumption enters.

## 7. Final coefficient, strict threshold and second corner

Combining the two remainders in the exact cardinal formula gives

    lambda<=a Lambda_c+19000rho^2(1+log m)+10rho^2.

For m>=65, log m>4, so the coefficient is at most 23750+5/2<24000 times log m. Since a>0 on the half diamond, the cardinal triangle inequality supplies the claimed estimate at every rho<=1/2, including rho=0 and the closed outer boundary.

On [0,1/2], 1-cos t>=(2/5)t^2, so 1-a>=rho^2/10. Therefore Lambda_c>240000log m makes the comparison strict at every rho>0 in the patch. PD-T157 supplies Lambda_c>=(2/5)ell^2-54, while log m<=ell+1. For ell>=610000 their difference from 240000(ell+1) is >=4000ell-240054>0; at the endpoint its exact value is 2439759946. Thus the sufficient logarithmic threshold is fully numerical.

The x reflection for even n and y reflection for odd n preserves the node set and total-degree cardinal space, hence permutes cardinal polynomials. It sends the canonical corner to the other nonnode corner and preserves inward phase magnitudes. This proves the identical bound there without exchanging the kernel coordinates or moving its exceptional mode.

## Findings and use boundary

No mathematical NOTE, MINOR, MAJOR or BLOCKING finding. One independent standard-library Fraction invocation verified the delicate regular-gap coefficient, both normalized derivative coefficients, the total 9464 remainder coefficient and the strict-threshold slack, exit 0 with negligible CPU under the 60 CPU-s cap. The exact values appear above; the execution is not a mathematical premise. No phase/kernel test, finite-degree extension or numerical integration was run. Author bytes were preserved.

A future checker must enforce n>=64, an actual nonnode corner class and the full inward rho<=1/2 domain. Direct use of strict exclusion also needs the stated certified corner inequality or the sufficient logarithmic threshold. The theorem does not make a finite-energy premise valid outside its proved range, assume a known global maximum, or put arbitrary points into corner patches. Global localization, full-cover acceptance and executable guard correctness remain separate.
