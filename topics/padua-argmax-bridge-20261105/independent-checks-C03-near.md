# Independent supplementary review — C03 quadratic remainder and onset

Reviewer: distinct Codex `/root/c01_near_review`, parent-assigned Astra high;
serving identity and effective effort are not independently exposed.
Date: 2026-11-06. Rules were read at
`4b728b04216a5490910780bc609a82b853058426`; the AGENTS/WORKFLOW/CODEX
diff to current input HEAD `b6e67b3c78cb668b6d2f9da5a5560537d2960bf3`
is empty. Branch: `codex/padua-argmax-bridge-20261105`.

**Disposition: accepted at both stated scopes, with no mathematical
finding.** The noncentral bound includes the actual fixed-truncation
beta slope. The actual near-model comparison holds for log n>=32.
The original n>=10^6 comparison and the global argmax theorem remain
OPEN. Formal Claude audit is separate and remains pending.

## Frozen scope and method

| Reviewed source | SHA-256 |
|---|---|
| `theory/C03-near-quadratic-remainder.md` | `70e8488b9cb1070c599e0172ff3235e1dfcec471122220c50e04386d50915675` |
| `theory/C03-near-onset.md` | `01177205a83c58280cbd89b188f1b0f65b9730c110e8dd65fafb77c21acd977f` |

Both sources and the C03 idea were read in full and the source identities
checked. The fixed T definition, C02 finite-degree bound, C01 central bound
and N1 normalizations are the same sources reconstructed in the preceding
C01/C02 reports. This review additionally refreshed full N1-04, read
PD-T270's full harmonic-remainder proof, and inspected PD-T269's local
cotangent partial fraction supporting the odd reciprocal-square sum.
All R=128 and J=4096 constants below remain finite truncated constants.

This is an analytic validity review without a historical novelty or
priority verdict. No full registry/search audit is claimed. No mathematical
program, numerical quadrature, fit or sampled diagnostic was run. Source
reads, hashes and the unchanged-rules diff were the checking operations.
Only this new report was written; author sources, prior reviews, shared
files and Git state were not edited.

## Paired periodic pole contribution

For x=(pi-z)/(2pi), reflection and periodicity give exactly

    N_L+N_R=c_e[Phi(x+t_-)+Phi(x-t_-)]
             +c_d[Phi(x+t_+)+Phi(x-t_+)],
    t_-=(alpha-beta)/(2pi), t_+=(alpha+beta)/(2pi).

The sampled x interval and |t|<=1/(4pi) can cross the integer zero but
no other integer. The second derivative on open periods has absolute
bound 35 and the integer atom has magnitude below 6. The positive
triangular kernel for a second difference has total mass t² and
atom weight (|t|-x)_+ at zero, proving the stated absolute bound (4).
This includes t_-<0 and the coincident t_-=0 case.

The reciprocal-pair series implies C(s)>=C0 on a period. Since
C0>3>2log pi, the continuous periodic Phi is nonnegative, including
its integer value one. The baseline cosine change is therefore
nonpositive and can be dropped in an upper bound. The cosine weights
are nonnegative and at most one. Using t_-²+t_+²=r²/(2pi²) gives the
smooth coefficient 315/(2pi³). On the atom support z>=pi-1/2,
sin(z/2)>=31/32. Integrating (|t|-x)_+ with dz=2pi dx and the
normalization 1/[2pi sin(z/2)] gives 96t²/31 per t. The total atom
coefficient is 48/(31pi²). Their sum is below 6, as claimed.

The same absolute second-difference estimate, together with the quadratic
cosine change, also establishes a zero first derivative at the origin for
this integral. An upper bound alone is not being used to infer that
derivative. There is no missing cusp or additional folded factor.

## Endpoint reciprocal products and their linear term

Partial fractions in N1-07 yield (6) exactly: its r positive denominators
become c_j+b-alpha and c_j+b+alpha with c_j=(2j+1)pi. The factor
4a/(r*pi+b) is correct. Setting a to one only increases this positive
part and leaves its value and first derivatives unchanged at the origin.

For the radial Taylor expansion of [(1+lambda u)(1+lambda v)]^-1,
|u|,|v|<1/6. The second derivative, integrated with weight 1-lambda,
is bounded by (6/5)^4(u²+|uv|+v²). Since |uv|<=(u²+v²)/2 and
(3/2)(6/5)^4<25/8, the written remainder follows. Averaging the two
alpha signs replaces (b+/-alpha)² by alpha²+beta². The two b signs
cancel linear terms for all paired rows.

The resulting reciprocal remainder coefficient is

    (50/pi^4)[sum H_odd(r)/r³+sum S_odd,3(r)/r].

The first sum is below 2. The second is below (35/32)*6, so the
bracket is below 137/16. With pi²>49/5 the coefficient is below 5
even after the unpaired sine remainder 1/(36R) is included.
The paired sine terms are negative, the closest sinc row contributes
no positive increment, and the only unpaired sine remainder satisfies

    -sin beta/(R*pi-beta)+beta/(R*pi)
        <=(beta-sin beta)/(R*pi)<=r²/(36R).

The derivative of the unpaired reciprocal row is positive and equals
the two sum terms in (7); its sine term contributes -1/(R*pi).
Thus d_C is exactly the stated coefficient, not an estimated or
artificially deleted boundary slope. The alpha derivative is zero.

## Exact finite-truncation slope cancellation

The finite telescoped h_J formula gives

    h_J'(0)-h_J'(1)=-1/R²+1/(J+1)²
                         -1/[(J+1)²-1/4].

The finite g_J formula gives f'(R) plus the difference between the
one-cell integral of f' and its midpoint value. The explicit rational
q_R gives the analogous expression at R+1. These are exactly the
three e_h,e_g,e_q identities in the source, with the offset derivative
factor 1/pi in H'(0) and G'(0). No infinite constant replaces a
finite J or R value.

Combining d_C,d_S,d_J and using S_odd,2(R)=pi²/8-V_R cancels
the 1/(R*pi) term and yields precisely (10). In particular its constant
numerator is +2: the +4 from g is reduced by the -2 from the jump.
The remaining apparent logarithmic term also cancels exactly because

    H_odd(R)=H_(2R)-(1/2)H_R,
    C0=2gamma+4log2.

PD-T270 therefore bounds 8H_odd(R)-2C0-4log R between
-1/(4R²) and 1/(2R²). For V_R, the midpoint sum of 1/(4x²)
over cells [j,j+1] lies below its integral over [R,infinity).
The centered-cell remainder bounds their difference by 1/(16R³).
It follows that 0<=2-8R V_R<=1/(2R²). The first numerator in
(10) consequently has magnitude at most 1/R².

The rational formulas give |e_h|<1/(3J^4) and |e_q|<1/(4R^4).
The one-cell midpoint error for f' is bounded by sup|f'''|/24;
f'''=(11-6log x)/x^4 gives |e_g|<9/(4J^4). With C0<4 and
pi>3, the combined bound is strictly

    |d_C+d_S+d_J|<1/(18R^4)+1/J^4<10^-9.

The final inequality is valid already from R^4>10^8 and J^4>10^12.
This establishes both existence of the one-sided beta derivative and
its magnitude. Its sign or vanishing is neither assumed nor proved.

## Remaining noncentral constants

The identity D0=a(2C0+D)/pi² follows from N1-16's exact U0 formula;
it includes the cancellation of the log pi terms in D0. The bounds
C0<4, |h_J|<5 and |g_J|<13 follow from PD-T270 at m=10 and the
finite centered-cell corrections. They imply W0>4t²-16t-184>-100
for 7<t=|k|<9. Hence the baseline a variation contributes below
3r². The D term is nonpositive since D>=0 and 2k+H(beta)<0.

Differentiating the finite formulas twice gives the asserted
|h_J''|<1/15000 and |g_J''|<1/2500. In particular the bounds by
1/127²+1/J² and (log127+1/2)/127²+9/J² fit those constants.
The two offset derivatives and Taylor's factor 1/2 give the stated
beta remainders 1/120000 and 1/20000. After the coefficients
2C0 and 4 and division by pi², their contribution is below
beta²/30000. Replacing a*d_S*beta by d_S*beta costs at most r²/8.
These terms total less than 4r² beyond the exact d_S beta.

The endpoint-half cancellation integral is a times its origin value;
its absolute origin bound 256/pi² and 1-a<=r²/4 give less than 7r².
For the limiting jump, the stated q and q' bounds give a remainder
below r² after its exact d_J beta is removed. Consequently the five
quadratic allocations sum to 6+5+4+7+1=23<25. Their linear terms
sum to the actual d just bounded. This proves the claimed
25r²+10^-8 beta on the full triangle, with nonstrict zero values
at the origin and continuous restrictions to either axis.

## Actual near-model onset at log n>=32

C01 contributes the radial fractional term, r² and half the radial
entropy term. C02 contributes the independently checked finite error
5,000,000(L+1)e^-L. Thus (3) in the onset record is a bound for
the actual Q_n, with coefficient 26 on r², not only a bound for T.

For L>=32, A(L)>L²/11 gives A-58>35. Allocate 32r² to the
fractional term and A-58 to the entropy term. Since r²>=rho²/2,
the fractional maximum is 27c^4/(32*32³)<2*10^-6. The entropy
maximum is (1/(4e))exp[-4(A-58)]<10^-8. The fixed beta term
is at most 5*10^-9. From e>8/3 and (8/3)^16>6,000,000,
the finite-degree term is below 5*10^-6. Their sum is strictly
below 1/40000, including zero phase.

Finally the N1-18 artifact allowance fits the exact remaining eta
budget for every n>=10^6, and e^32 exceeds that validity threshold.
The N1-17 origin identity and the already proved origin approximation
then yield the stated M_near<=Lambda_c+1/4096. Both parities and all
integer n with log n>=32 are covered. This does not cover the whole
original n>=10^6 range or any phase outside the near triangle.

## Completion

No BLOCKING, MAJOR or MINOR finding in the two frozen C03 sources.
No author repair was made or required before acceptance. The fixed model,
truncated constants, central fractional term and finite-degree error all
remain explicit. The sharper original target and the global theorem are
OPEN; certified degrees 2–40 are unchanged. Claude formal audit remains
pending.
