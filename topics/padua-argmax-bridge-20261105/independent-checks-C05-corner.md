# C05 actual-corner quarter-angle bound: independent reconstruction

Rules read at `4b728b04216a5490910780bc609a82b853058426`. Reviewer: distinct Codex supplementary reviewer, allocated gpt-6-astra high; serving model/effort metadata unexposed. Date: 2026-11-06.

Frozen proof: `theory/C05-corner-quarterangle-bound.md`, SHA256 `f440f331de15eaf1e8b87849549110c75bb68a75cb3779a537f564fd7f042282`.

**Verdict: ACCEPTED, no unresolved finding.** For n>=10^6 and inward rho<=1/2 at either actual nonnode corner,

    lambda<=a Lambda_c+[(1/3)log(n+1)+38](alpha^2+beta^2).

The strict punctured-patch consequence is proved for every integer n with log n>=25. This does not prove strictness at every n>=10^6 or a global argmax onset. Formal Claude audit and any backend implementation review remain separate.

## Scope and inherited material

Read the entire frozen C05 source. This reviewer previously read and reconstructed C02's complete signed-half-diamond geometry, exact cardinal-orbit normalization and finite B-family derivative bound, and read PD-T157/221/228 and the underlying polynomial conventions in full. This review independently reconstructs every new quarter-angle identity, separation sum, numerical allocation and strict-threshold step. C07 and any later improvement are outside scope and are not used.

Historical novelty, priority and the completeness of the author's gate are excluded; no full IDEAS novelty audit is invoked. The verdict concerns the exact frozen mathematics. No sample, fitted derivative constant, energy statement, global norm equality or model correction is a premise.

## 1. Exact orbit and regular geometry

The actual-corner identities have the same normalization as the accepted C02 proof:

    lambda=(1/N)sum_O e_j f_r |sum_four F_jr|,
    Lambda_c=(4/N)sum_O e_j f_r |F_jr(0,0)|.

Four reflected copies stay together before each cardinal absolute value. The initial zero row r=m,j<n remains included, and the endpoint (n,m) has the finite polynomial value F0=n. Dropping endpoint weights only in positive error estimates is safe.

On R=O minus {r=j+1,j>=2n/3}, odd parity gives odd nonzero j-r, S=j+r>=1 and d=2n+1-S>=1. With tau=m/n<=1001/1000, the phase perturbation of P and T is at most 1/(4n), whose rescaled size m/(2pi n) is <1/6. Hence the displayed lower bounds by S-1/6, d-1/6 and g-1/6 follow, where

    g=|j-r+j/n|

is the exact unperturbed separation in units pi/(2m). Positive differences have g>=j-r; negative differences of magnitude >=3 have g>=r-j-1. In the remaining r=j+1 regular class, j<2n/3 gives g=1-j/n>1/3. Thus g-1/6>1/6 there. This delicate class is retained explicitly in the sums rather than replaced by a false spacing of order one without its dependence on j/n.

The base sum-angle distances and phase bound also imply 0<P<pi and |T|<8/5 on the full signed rectangle. The relation |T|-Z=max(u,v)-pi, Z=pi-P, bounds its positive part by the endpoint overshoot 1/(2n). Since Z>=5pi/(12m), that overshoot is <(2/5)Z. Therefore |T|<=3Z/2 holds throughout the same domain, including endpoint overshoots. Every rectangle used below has |gamma|<=alpha, |delta|<=beta and hence total absolute phase <=1/2.

## 2. Quarter-angle identity and pure second derivatives

Writing v=P-T gives cos v=cos P cos T+sin P sin T, while cos u-cos v=-2sin P sin T. Also

    cot(P/2)cot(T/2)+tan(P/2)tan(T/2)
       =2(1+cos P cos T)/(sin P sin T).

These identities prove the exact formula (5), with its -1/2 constant and -1/4 product coefficient. No numerator cancellation at the upper endpoint is discarded.

For X=cot(P/2), the chord bound on P/2 in (0,pi/2) and cot x<=1/x give the stated coefficients 2, pi^2/2 and pi^2 for X,X',X''. For Y=cot(T/2), the Taylor bound on |T|/2<=4/5 proves csc^2 x<=x^-2+1: the needed polynomial difference is x^2(24-11x^2+x^4)/36>=0. Differentiation then gives |Y'|<=2/T^2+1/2 and |Y''|<=4/|T|^3+1/|T|.

For U=tan(P/2)=cot(Z/2), the same X bounds apply with Z. For V=tan(T/2), cos(T/2)>=17/25 and |sin(T/2)|<=|T|/2 give |V|<=|T|, |V'|<=2 and |V''|<=2|T|. The pure u or v derivative changes both P and T by magnitude 1/2. Therefore the XY contribution has factor 1/16 multiplying X''Y, 2X'Y' and XY'', which yields exactly the first five terms of (6).

For UV the same factor gives

    [pi^2|T|/Z^3+2pi^2/Z^2+4|T|/Z]/16
       <=(7pi^2/32)Z^-2+3/8<3Z^-2+1.

This verifies the last two terms of (6). The estimate is valid for either sign of T and does not assume cardinal sign stability. Mixed second derivatives are unnecessary for the rectangular averaging argument.

## 3. Discrete sums A1, A2 and A3

For j-r=l>=1 odd, write j=r+l. Replacing g by l gives q=l-1/6 and S-1/6=2r+q. Integral comparison for decreasing functions gives the displayed (8). Its logarithmic constant is safe: for q>=5/6 and m>=10^6, log(1+2m/q)<=log m+5/4. The positive odd-l series have Q3<29/16 and Q4<21/10; separating l=1 and integrating the step-two tails gives exactly the rational bounds printed in the proof. The tails starting at l=3 satisfy Q3_tail<2/25 and Q4_tail<3/125.

For negative l=r-j>=3, g>=l-1, so h=l-7/6 and S-1/6>=2j+h. The first-term-plus-integral bounds are sum h^-3<1/4 and sum h^-4<1/8. Combining these with the positive classes gives

    A1_other<=(33/16)(L/2+5/8)+89/40.

For negative l=1, put q0=5/6 and J=max{integer j:j<2n/3}. The exact remaining denominators are 2j+q0 and q0-j/n. The j=0 contribution to A1 is q0^-4<21/10. For j>=1, the constant part of (q0-j/n)^-3 contributes at most (108/125)(1+L). For its increment, the mean-value inequality gives

    [f(j/n)-f(0)]/(2j+q0)<=f'(j/n)/(2n).

Monotonicity bounds that sum by half the integral of f' to (J+1)/n. Here q0-(J+1)/n>=1/6-1/n>=(999/1000)/6, and 216(1000/999)^3<217. Subtracting f(0)=216/125 makes this increment <108. Thus the entire negative-l=1 part is <(108/125)L+111. Addition gives the exact logarithmic coefficient

    33/32+108/125=7581/4000,

and constant 73289/640<115, proving the A1 bound.

For A2 and A3 in this class, j<=100 permits (q0-j/n)^-s<=1.01 q0^-s, s=1,2, because n>=10^6. Enlarging those finite sums to their infinite positive sums gives the stated head terms. For j>100, q0-j/n>1/6 and 2j+q0>=2j. The integral tails are exactly 3/80000 for A2 and 9/100 for A3. Their complete bounds are 5061387/2000000<51/20 and 191061/62500<31/10, respectively.

The positive classes cost Q4+Q3/4<13/5 for A2 and Q4+Q3/2<31/10 for A3. For negative l>=3, q/(q-1)<=17/11<8/5, so comparison with the positive tails gives costs <1/10 and <1/5. Consequently A2<6 and A3<7, with all regular physical indices and both difference signs included.

## 4. Rectangular averaging and regular f allocation

At the four reflected endpoints a=(cos alpha+cos beta)/2 is identical, so it factors out exactly. Applying the one-coordinate symmetric second-difference bound successively yields

    |Av f-f0|<=alpha^2 sup|f_uu|/(2n^2)
                  +beta^2 sup|f_vv|/(2m^2).

Multiplication by the four copies in the cardinal formula gives the stated overall factor 2r2/(Nn^2) against the common majorant (6). There is no derivative of a along this argument; a is only factored at the four actual evaluation points, and a<=1 can then be dropped in the positive remainder.

Substituting the lower bounds for P and |T| gives leading coefficient 16tau^3/pi^4 times A1. With tau^3<101/100 and pi^2>197/20, this coefficient is <6464/38809. Its product with 7581/4000 is 1531362/4851125<1/3, and its product with 115 is 743360/38809<20. The next two terms have coefficient 4tau^3/pi^2<404/985; multiplication by A2<6 and A3<7 gives <5/2 and <3. These reproduce (11)–(12), with L=log m throughout.

The remaining sums are also explicit. For fixed S there are at most 2S pairs; for fixed d at most 4d. Since S-1/6>=5S/6 and d-1/6>=5d/6, harmonic comparison gives the printed P^-2 and Z^-2 bounds with coefficients 288/25 and 576/25. The bound g-1/6>=1/6 and sum(S-1/6)^-1<5m give sum(P|T|)^-1<120m^3/pi^2. The number of pairs is <4n^2.

Multiplying the last four terms of (6) by 2/(Nn^2) gives exactly (13), including its factors 30, 18/25, 3456/(25pi^2) and 8. At n=10^6, H2=1+log(2m)<16; the stated logarithmic ratios decrease thereafter. Using tau<1001/1000 and pi>3 makes the displayed sum <1/100 with ample slack. Thus the full f allocation is <=[L/3+20+5/2+3+1/100]r2, without a hidden O-constant.

## 5. Odd sine channels and their normalization

For the first sine channel, the fourfold signed sum pairs g_u(+alpha,delta)-g_u(-alpha,delta) at each of the two delta signs. Each difference is bounded by 2alpha/n times its u derivative. Including the coefficient sin(alpha)/2 and dividing by N yields 2alpha^2/(nN) times the derivative majorant. Since |partial_u g_u|<=[csc^2T+csc^2P]/4, this is alpha^2/(2n^2m) times the csc sum. The second channel gives beta^2/(2nm^2), which is no larger than beta^2/(2n^2m). This independently verifies the coefficient in (14).

For the separation-square sum, positive differences cost at most (51/25)m, negative differences >=3 cost at most (69/121)m, and negative l=1 costs at most

    n[6000/999-6/5]<(481/100)n.

The last estimate follows from the increasing-function integral up to (J+1)/n, including j=0. The three coefficients sum to 17957/2420<15/2. Using csc^2T<=(25/9)T^-2 and the exact geometry therefore gives coefficient 125tau^2/(3pi^2)<9/2 in (14).

The plus-angle part obeys csc^2P<=pi^2(P^-2+Z^-2)/4. Substitution of the previous sums gives 108mH2/(25n^2)<1/100 from n10^6 onward. Hence the two sine channels together cost <5r2. These estimates apply to signed smooth kernel channels before the cardinal absolute value, so initially zero cardinals do not require a separate sign argument.

## 6. Polynomial B family and final coefficient

The B family and signed half diamond are exactly those of the accepted C02 theorem. Its finite U/V factorization gives phase Hessian |F_ij|<=4n and |F0|<=2n, including h=0 and every sine/divided-difference collision. For E(s)=F(s alpha,s beta)-a(s alpha,s beta)F0 this gives |E''|<=5n rho^2. Two opposite phase pairs cost <=10n rho^2 per index.

There are at most n/3+1 B indices. Dividing by N and using rho^2<=2r2 gives

    10(n/3+1)rho^2/m<=(20/3+20/n)r2<=(27/4)r2.

All repeated endpoint copies were already counted in the exact orbit formula. No formal quotient replaces the polynomial endpoint value.

The complete fixed allocation is

    20+5/2+3+1/100+5+27/4=1863/50=37.26<38.

Applying the triangle inequality to sum_four F=4aF0+sum_four(F-aF0), with a>=15/16, proves the stated coefficient L/3+38 uniformly on the closed half diamond. The argument does not insert the primitive's fractional or linear cusp bounds into an actual-cardinal estimate.

## 7. Strict onset and domain

Cosine Taylor on [0,1/2] gives 1-a>=47r2/192. With ell=log n, PD-T157 and pi^2<10 imply

    (47/192)Lambda_c-[log(n+1)/3+38]
      >=(47/192)[(2/5)ell^2-54]-(ell+1)/3-38.

The last polynomial equals 21/16 at ell=25. Its derivative is 73/16 there and increases thereafter. It is therefore strictly positive for all ell>=25. The result is strictly below Lambda_c whenever r2>0, including arbitrarily small nonzero inward phases. The onset ceil(exp(25)) exceeds 10^6, so no degree below the proved analytic domain is used.

The parity-valid x reflection for even n and y reflection for odd n preserves the Padua node set and permutes corrected cardinal polynomials. It transfers the bound and inward phase magnitudes to the other nonnode corner. No exchange of mesh coordinates or exceptional mode is made.

## Findings, checks and limitations

No BLOCKING, MAJOR, MINOR or mathematical NOTE finding. A single independent standard-library Fraction calculation checked the rational series allocations, leading coefficients, sine-square total, final fixed budget and strict-threshold polynomial; it exited 0. The exact values are recorded above. It used no phase/kernel sample or numerical transcendental evaluation and is not a proof premise. Frozen author source was not edited.

The accepted bound starts at n>=10^6; its proved strict patch starts at log n>=25. The original strict n>=10^6 target remains OPEN in this record. No C07 improvement, global localization, weighted-energy premise, prior global maximum or new certified finite degree is included. Backend guards and formal Claude audit remain separate.
