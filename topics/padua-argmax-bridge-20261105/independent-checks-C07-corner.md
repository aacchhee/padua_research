# C07 million-degree actual-corner patch: independent reconstruction

Rules read at `4b728b04216a5490910780bc609a82b853058426`. Reviewer: distinct Codex supplementary reviewer, allocated gpt-6-astra high; serving model/effort metadata unexposed. Date: 2026-11-06.

Frozen sources:

- `theory/C07-corner-positive-deformation.md`: `2b2870f236cf1c6ab58a01d3331c413b07b50bdbdf8e73fd839a47cd8479893c`.
- `theory/C07-corner-million-onset.md`: `9fa0d3f3b507f1a772adda1bbc4841e42b13b7f0adada39b6ede2ab8ee5247e4`.

**Verdict: ACCEPTED, no unresolved finding.** The finite corner-value comparison holds for every integer n>=2. The resulting corner lower bound and actual-cardinal estimates prove, for every integer n>=10^6 and both inward half-diamond corner patches,

    lambda<=a Lambda_c+[(1/3)log(n+1)+16]r2,
    lambda<=Lambda_c-r2,

where r2=alpha^2+beta^2. Both punctured patches are therefore strictly excluded at every degree in that range. This is not a global-localization or global-argmax conclusion. Formal Claude audit and executable implementation review remain separate.

## Reading and scope

Read both frozen proofs in full, the complete C07 gate/candidate and attempt records, and the complete PD-T159 and PD-T269/270/271 proofs. None of these reads was truncated. The C07 idea record preserves its explicit chronology qualification for the finite pairing derivation; this review does not replace that record with a retrospective prospective-gate claim.

C02's exact four-copy normalization and finite-polynomial bounds, C05's quarter-angle estimates and all regular sums, and N1-16's elementary cosine/constant bounds were already independently reconstructed or read in full in this review session. Changed estimates are rederived below. The verdict covers analytic correctness and exact scope, not historical novelty, priority, search completeness or an audit of the whole IDEAS registry. No asymptotic constant, measured corner value or fixed-sign assumption is imported.

## 1. Exact finite positive deformation

PD-T159 gives the two exact sums with coefficient 4/(nm) for the deformed corner and 4/n^2 for the same-mesh square. Its endpoint (n,m) contributes exactly 1/m from the finite polynomial; the other k=m terms vanish. The reference k=n numerator vanishes, and odd parity excludes every diagonal. Thus the two identities (3) in the new deformation proof have exactly the correct endpoint and normalization conventions.

For j<k, set A=cos a_j, B=cos a_k, d=A-B>0, u=cos b_j-A>=0 and v=cos b_k-B>=0. The angular ordering b_k>a_j follows from n(k-j)>j: k-j>=1 and j<=n-1. It implies v<d. Exact subtraction yields

    forward increment=(1+A)v/[d(d-v)],
    reverse increment=-(1+B)u/[d(d+u)].

These signed increments need not be individually nonnegative. For k<n, the monotone quantity

    q(x)=(cos(tau*x)-cos x)/(1+cos x)
        =[cos(tau*x/2)/cos(x/2)]^2-1

has logarithmic ratio derivative tan(x/2)-tau tan(tau*x/2)>=0 on [0,pi). Hence (1+A)v>=(1+B)u. The positive forward term has the smaller denominator d(d-v)<=d(d+u), so the paired sum is nonnegative. At k=n, B=-1 makes the reverse increment exactly zero; the forward increment is nonnegative directly. No division by 1+B is performed at that endpoint. The j=0 case is included because u=0 and the ratio q is defined at zero.

Pairing both orientations with symmetric weights epsilon_j epsilon_k proves nonnegative total finite deformation. The actual k=n weight is larger by 1/2, which adds only nonnegative actual terms and adds no reference term. Comparing the two normalization factors therefore proves

    Lambda_c>=n L_n^2/(n+1)+1/(n+1)

for every integer n>=2. This is a finite pairing statement. PD-T269's positive limiting integral and its coarse convergence rate are not used to infer finite positivity.

## 2. Corner lower bound from degree one million

PD-T270 applies to both parities and supplies |L_n-A_n|<=1/(4n^2), with A_n=(2/pi)(ell+kappa0). Its exact L_n definition matches PD-T159. The recalled elementary bounds give kappa0>3/2 and A_n<=ell+2. The upper estimate is also immediate from gamma<1, log(8/pi)<1 and 2/pi<1. There is no use of the numerical constant enclosure in PD-T271.

Since A_n-1/(4n^2)>0 on n>=10^6, squaring the lower estimate for L_n and applying the finite comparison gives

    Lambda_c>=A_n^2-A_n^2/m-A_n/(2n^2).

Here positive square and endpoint terms were discarded, and replacing the factor n/m in the negative linear error by one only weakens the bound. With 4/pi^2>2/5, kappa0>3/2 and A_n<=ell+2 this yields

    Lambda_c>=(2/5)(ell+3/2)^2
                  -(ell+2)^2/n-(ell+2)/(2n^2).

Both error functions decrease on n>=10^6. At n=10^6, ell<14 bounds their sum by 256/10^6+8/10^12<1/1000. Consequently the asserted corner lower bound is uniform over every integer n in the domain, with no finite-degree sampling, asymptotic substitution or unquantified threshold.

## 3. Enlarged split and the changed regular sum

The new B={r=j+1,j>=n/2} contains C05's B, so the new regular set is a subset of the previously checked one. The original lower bounds for P,Z,|T| and the exact g=|j-r+j/n| remain valid. In the only altered regular class, r=j+1, one now has j<n/2, so g>1/2. C05's quarter-angle pure derivative majorant and its positive A2<6,A3<7 sums therefore carry over without enlarging a domain or changing a sign.

For A1, the positive differences and negative differences of magnitude >=3 retain their combined bound (33/16)(L/2+5/8)+89/40. In the remaining class q0=5/6 and J=max{integer j:j<n/2}. The exact residual sum is bounded by

    sum_(j=0)^J (2j+q0)^-1(q0-j/n)^-3.

The j=0 term is <21/10, and the constant part for j>=1 costs <=(108/125)(1+L). For the increment, the same monotone derivative argument as C05 bounds it by half the integral of h' to (J+1)/n. Now q0-(J+1)/n>=1/3-1/n>=(999/1000)/3 and 27(1000/999)^3<28. Subtracting h(0)=216/125 makes this integral bound <14. The changed class is thus <(108/125)L+17.

The combined log coefficient remains 7581/4000, while the constant is 13129/640<21. This proves the new A1 allocation and accounts for every regular r=j+1 index. With the unchanged factor 16tau^3/pi^4<6464/38809, the constant contribution is 135744/38809<7/2; the log coefficient remains <1/3. The A2/A3 contributions are still <5/2 and <3. The last four pure-derivative terms have the already checked <1/100 cost on the larger old regular set, so the new regular f budget is <=[L/3+901/100]r2.

Rectangular averaging is unchanged: a is identical at the four reflected evaluation points and factors out there. The factor from four copies and the two pure coordinate second differences is exactly 2r2/(Nn^2). No derivative of a is charged in the regular f calculation, and no mixed derivative is silently dropped.

## 4. Improved sine-channel sum

Pairing each sine-odd channel in its own coordinate gives the same exact normalized coefficient r2/(2n^2m) multiplying sum(csc^2T+csc^2P) as in C05. The positive-difference separation-square sum costs <=(51/25)m; negative differences >=3 cost <=(69/121)m. The changed r=j+1 class now satisfies

    sum_(j=0)^J(q0-j/n)^-2
       <=n[3000/999-6/5]<(181/100)n.

The increasing-function integral includes j=0, with upper limit (J+1)/n. The three coefficients sum to 10697/2420<9/2. Substituting the lower |T| bound and csc^2T<=(25/9)T^-2 gives T-channel coefficient 25tau^2/pi^2<8/3. The P-channel cost remains <1/100 by the old P/Z square sums. Hence both sine channels together cost <3r2. Initial zero cardinals are covered because these are signed smooth channel differences before the final absolute value.

## 5. Fourier moments and the complete enlarged finite family

For k even, the absolute frequencies in U_k are the odd integers through k-1, each twice; their sum is k^2/2. For k odd, the nonzero frequencies are the even integers through k-1, each twice; their sum is (k^2-1)/2. The square-frequency sum in either parity is k(k^2-1)/3. Differentiating the finite exponential polynomial therefore proves the uniform bounds in (18), including every sine collision. No quotient derivative near zero is used.

On the enlarged B, h=n-j satisfies 0<=h<=n/2. Thus |X|<=pi/2+1/(4n)<8/5 and |T_B|<=pi/(4m)+1/(4n)<8/5. At |z|/2<=4/5, cosine Taylor gives cos(z/2)>=17/25 and sin(z/2)<=|z|/2 gives |tan(z/2)|<6/5. These imply |sec(z/2)|<=3/2, first derivative <=1 and second derivative <=3/2. Product differentiation of V_n=sec(z/2)cos((n+1/2)z) yields exactly

    |V_n'|<=3n/2+7/4<=1.51n,
    |V_n''|<=3n^2/2+7n/2+23/8<=1.51n^2

on n>=10^6.

Each first phase derivative of X,T_B has magnitude <=1/(2n), and the second derivatives vanish. Applying the product rule to the exact finite factorization gives the bracket

    (151/100)tau+(151/100)tau^2+(1/2)tau^3+88/25.

The cross-product factor 2 combines with |U_m'|<=m^2/2, producing the coefficient 151/100 of tau^2. For the second product its three contributions are 1/2,151/100,151/100, whose sum is 88/25. At tau=1001/1000 the bracket is 14092066021/2000000000<71/10. Consequently |D_ij|<(71/40)n. The corrected exceptional cosine has phase Hessian magnitude <=1; after the factor 1/2, |F_ij|<=71n/80+1/2<=9n/10. Thus the exceptional first-coordinate mode is included explicitly.

The baseline bound also survives the enlarged family. At h=0 the exact value is F0=n. For h>=1 the two baseline cosine arguments are distinct, and

    F0=sin^2(y0/2)/(sin X0 sin T0)>0.

Here X0<=pi/2 and T0<=pi/(4m). Using sin X0>=2X0/pi, sin T0>=(99/100)T0 and sin(y0/2)<=y0/2 yields

    F0<=(50pi/99)y0^2/(x0^2-y0^2)
       =50pi n^2/[99(2n+1)]<n.

Only the baseline is assigned this sign. The perturbed cardinals need not retain it.

## 6. Charge the enlarged family and assemble

For E(s)=F(s alpha0,s beta0)-a(s alpha0,s beta0)F0, the phase Hessian bound contributes <=(9/10)n rho^2 and |a''F0| contributes <=(1/2)n rho^2. Hence |E''|<=(7/5)n rho^2. Two opposite phase pairs have total cost <=(14/5)n rho^2 per B index.

The actual count is at most n/2+1, including the finite endpoint and all indices moved out of the old regular set. Division by N and rho^2<=2r2 therefore give a total <=[14/5+28/(5n)]r2<3r2. Endpoint weights were already present in the exact orbit formula and can be discarded upward only in this positive bound.

Adding regular f, both regular sine channels and the complete new B family gives fixed coefficient

    901/100+3+3=1501/100<16.

The identity sum_four F=4aF0+sum_four(F-aF0), with a>0, then gives (1) by a triangle inequality after the four-copy sum. There is no phase-independent absolute error and no sign-stability hypothesis. Every contribution is proportional to r2, including arbitrarily small positive phases and the axes.

## 7. Uniform scalar loss from degree one million

On the half diamond cosine Taylor gives 1-a>=47r2/192. Combining the newly proved lower bound with L=log(n+1)<=ell+1 gives the scalar loss p(ell) in (26). At ell=69/5,

    p(69/5)=25443/12800=381645/192000>1,
    p'(69/5)=6391/2400>0.

Its derivative increases with ell. The positive geometric-integral series used in the source gives the rational lower bound log10>58726/25515>23/10. Therefore n>=10^6 implies ell>=6log10>69/5, and p(ell)>1 for every such integer degree. Subtracting this loss from the bound in (1) gives lambda<=Lambda_c-r2, with equality allowed at r2=0 and strict inequality whenever rho>0.

For even n, x reflection preserves the node set and permutes cardinals; for odd n the corresponding y reflection does so. Inward phase magnitudes and the common corner value are unchanged. Thus the same two estimates hold at the other nonnode corner without exchanging mesh coordinates or the exceptional mode.

## Findings, checks and use boundary

No BLOCKING, MAJOR, MINOR or mathematical NOTE finding. One short independent standard-library Fraction invocation checked the new A1 and sine-sum constants, Fourier Hessian bracket, total allocation, corner lower-bound error and scalar threshold, exit 0. The exact values are given above. It used no transcendental evaluation, kernel or phase sample and is not a proof premise. No author source, old report, shared record or Git state was edited.

The accepted result is strict at both entire inward half-diamond corner patches for every n>=10^6. The finite positive deformation has its separate all-n>=2 scope. This does not place every global maximizer in those patches, supply a global far/noncorner comparison, extend the finite certified range 2–40 or validate a runtime implementation. Formal Claude audit and any subsequent global assembly remain separate.
