# Independent supplementary review — explicit near-model onset

Reviewer: distinct Codex `/root/c01_near_review`, parent-assigned Astra high;
serving identity and effective effort are not independently exposed.
Date: 2026-11-06. Rules and input HEAD:
`4b728b04216a5490910780bc609a82b853058426`, branch
`codex/padua-argmax-bridge-20261105`.

**Disposition: the main modulus, finite-to-limit estimate and near-model
onset are accepted mathematically, with two MINOR wording findings below.**
No BLOCKING or MAJOR finding. The original n>=10^6 near-comparison target
and the full global theorem remain OPEN. The established degrees 2–40
remain certified and unchanged. Required formal Claude audit is separate
and remains pending.

## Frozen scope, dependencies and method

Reviewed new source: `theory/C02-near-explicit-onset.md`, SHA-256
`ddf639380417ed3af686d4818aff3714aec78f0086c3c3b87b6a87817fb6805d`.
The full source was read and its hash checked. This review covers the
actual fixed model, all finite-to-limit error allocations, the explicit
noncentral phase bound, and the scalar onset calculation. It is not
limited to checking the last scalar inequality.

The rules, handoffs 05/06, LOG and N1 dependencies already read for the
two preceding reviews remain the input context. In particular full
N1-07, N1-09/10/11/13/14/16/18/19, the N1-15 model definitions,
N1-06's exact truncated-constant definitions, N1-17 and C1 were used.
Their identities and earlier analytic reconstructions are recorded in
`independent-checks-C01-near-central.md` and
`independent-checks-C01-near-axis.md`; those reports were not edited.
The central upper-bound source remains
`ef5b3b62e5c079889525f291b4874bb6aff8b1033ef790de67aa62f62ee361b7`.
The C01 idea's new full-residual fallback registration was read.

The scope is pure analytic correctness. No historical novelty/priority
verdict, full registry audit, allocation decision or independent chronology
certification is made. No mathematical program, numerical integral,
fitted constant, sampling or computational certificate was used. Source
reads, searches and hashes were the only checking commands. Only this new
review was written; no author source, previous report, shared file or Git
state was changed. Both findings were sent to the coordinator before
any author repair.

## Findings in the frozen source

**C02-1 — MINOR: the strict bound in equation (9) excludes its own origin.**
Section 2 asserts |[T-Ic](alpha,beta)-[T-Ic](0,0)|<1000rho on the
closed triangle. At rho=0 this reads 0<0. State the inequality with <=
on the closed triangle, or state strictness only for rho>0 and equality
at zero. The proof actually supplies the stronger coefficient 894 for
positive rho and the exact zero value at the origin. This does not change
the main nonstrict modulus (1), the strict onset (2), or their constants.
No proof repair or new estimate is needed.

**C02-2 — MINOR: the final sentence of the Statement mislabels the old
finite range.** Lines 28–29 say that the global theorem "and degrees
2–40 remain OPEN." The degrees 2–40 are already certified in the topic's
current records. Say that this certified range remains unchanged, while
the original near target and the all-degree/global theorem remain OPEN.
The source makes no new finite-degree claim, and its proof never uses
the erroneous status sentence.

These findings are reported against the frozen bytes above. No corrected
source or author response is silently presumed by this report.

## Exact limiting function and model accounting

The original model is not replaced. T in (3) is an auxiliary limit used
to estimate R_n=M_near-B0 L²-b_M L. The offsets t_L=beta/pi and
t_R=1-beta/pi remain phase dependent. The two J=4096 truncated strip
constants remain in H_J and G_J. Their truncation error is neither sent
to zero with n nor multiplied by an omitted logarithm.

For the one-summand jump constant, N1-11 gives exactly

    Q_R^[R](t)=1/(R+t)²+1/(R+t+1/2).

The left A2 coefficient is -2a beta/pi and the right is +2a beta/pi.
After the m/(n*pi²) factor tends to 1/pi², their sum is precisely
(2a beta/pi³)[q_R(t_R)-q_R(t_L)], with the sign in (3). This generally
does not vanish off the alpha axis and has correctly been retained.

N1-05 puts I/pi inside B and N1-15 integrates B with another 1/pi.
Thus the whole central part of T is exactly the previously reviewed
Ic with its pi^-2 normalization. Both folded copies are retained.

## Uniform finite-to-limit error

All bounds below apply for every n>=10^6 and every point of the closed
phase triangle. They cover changing cutoffs, collisions and degree parity.

1. **Endpoint rows: 1,000,000(L+1)/n.** Substituting R=128 and 2R-1=255
   in N1-07 gives exactly
   (334818+1531H_n)/n+110329830000/n². With H_n<=L+1 and n>=10^6,
   the proposed allowance follows with ample margin. N1-09 retains the
   exact finite-h polynomial rows, so this is an auxiliary comparison
   to C_R, not a second approximation inserted into the model.

2. **Remaining special rows: 50(L+1)/n.** The N1-16 exact-row bound,
   summed over at most four rows, is 8(L+5)/m. The N1-18 whole-row
   approximation discrepancy is less than 1/n. Their sum is bounded by
   (8L+41)/n<50(L+1)/n. Actual polynomial collision values and H8/Rhat
   branch changes are included; no count of transitions is multiplied in.

3. **Outer cells: 315,000(L+1)/n.** The two lower discrepancies total at
   most h, the omitted upper intervals total 2h, and at most two holes
   contribute 2h. All relevant points lie above delta/2. The A bound
   3000, after the 1/pi normalization and total length 5h, costs
   15000L/m<=15000L/n. For B, the pole part is below 16006 and the
   endpoint cancellation part is below (8000+1/2)*9/3, leaving the
   claimed slack below 50000. On the central half N1-14 supplies the
   additional integrable |log(pi-z)| envelope. Rearrangement on the
   two copies gives M[1+log(2/M)] for the epsilon<1 part. This increases
   for M<2, so M<=5h and 2/(5h)<n bound it by 5h(L+1). The epsilon>=1
   part adds at most 10h. Consequently the normalized B error is at
   most 5[50000+L+3]/m<300000(L+1)/n, giving the stated combined cost.

4. **Singular strip primitives: 160,000(L+1)/n.** Writing
   b_s=delta*m/pi+d_s with |d_s|<=1/2 proves
   log b_s=L+k+e_s, |e_s|<5000/n. Also
   Z_n-D0=B0 log(n/m), so |Z_n-D0|<1/n and |Z_n|<5.
   The linear replacement error is bounded by
   [(L+15)+25000]/n. The square replacement costs at most
   B0|L+k||e_s|+(B0/2)e_s², bounded by 3000(L+10)/n;
   the e_s² contribution alone is below 6/n. The two-side total
   is less than 8000(L+20)/n<=160000(L+1)/n. The surviving polynomial
   is exactly (7), with the fixed H_J and G_J terms included.

5. **Regular strips: 1,500(L+1)/n.** The bounds l_s<516/n,
   |u_s-delta|<2/n and |f_s|<3/5 give less than 104L/n per side.
   Integrating |log z| from zero to the lower boundary gives at most
   516(L+1)/n; the upper discrepancy adds at most 16/n. The coefficient
   |q_s|/pi²<=1/18 leaves less than 30(L+1)/n per side. Finally
   |U1|<4 and |N_s/m-delta/pi|<130/n leave less than 520/n per side.
   The totals fit the stated allowance. The two complete limiting
   q_s integrals and the two U_s constants cancel with their respective
   opposite signs. The only surviving regular-strip term is its exact
   L coefficient.

6. **Jumps: 10(L+1)/n.** The explicit bounds q_R<1/100,
   |A2_b|<=1/3 and b_K>=n/2 imply less than 1/n per side when
   m/n is replaced by one and 1/b_K is dropped. The remaining A1
   terms are bounded by 3(L+1)/n together, since |A1|<3/4,
   |h_R^[R]|<6 and log b_K<=L. The bounded W_b integrals add less
   than 4/n. The limiting signed A2 contribution was retained in T.

The six allowances sum to 1,476,560(L+1)/n, strictly below the asserted
2,000,000(L+1)/n. N1-16's coefficient identity cancels the exact L²
and L terms; no additional large logarithm is hidden in the remainder.
Taking the origin-normalized increment costs twice this uniform bound.
The N1-18 artifact allowance 9/(2n) then fits inside
5,000,000(L+1)/n. This proves (4) and (8), including the actual Q_n
construction and origin convention, rather than only a formal limit.

## Explicit noncentral phase constants

These are bounds for T-Ic itself. They do not assume cancellation of
first phase derivatives at the origin. The absolute-continuity arguments
are valid: finite denominators stay positive, finite truncated sums are
smooth, and the periodic pole profile is Lipschitz. Dominated integration
on the fixed interval away from z=0 preserves the required Lipschitz bound.

**Endpoint profile, 766.** With w=r*pi+b and |j|<=r-1,
w-|j*pi+alpha|>=pi-(alpha+|b|)>5/2 and w>(5/2)r. Hence
D>6r and each coordinate derivative of D has magnitude below 8r.
There are r summands, giving reciprocal-sum bounds 1/6 and 2/9
for its value and each derivative. Differentiating 8a times the sum
costs at most 1/3+16/9. The sin b/w term adds less than 1/2 to
its b derivative, so each row derivative is below 3. The 255 rows
and the closest-row sinc derivative below 1/2 give less than 766.
The sign b=-beta on right rows does not change these absolute bounds.

**Strip constants, 74.** Differentiating U0 gives the bound
1+12/pi<5, using |partial c_e|,|partial c_d|<=1/8. It follows that
|D0|<4, |partial D0|<2, B0<=4/9 and |partial B0|<1/9.
The finite telescoped formulas for h_J,g_J have exactly the stated
terminal half-cell logarithms. Centered-cell remainders and log129<5
give |h_J|<6, |g_J|<14 and |h_R^[R]|<6. Their derivatives satisfy
the displayed bounds 1/100 and 1/16 by comparison with integrals
from 127 to infinity. The offset slopes therefore give
|partial_beta H_J|<1/100 and |partial_beta G_J|<1/24.
Together with |k|<9 these yield derivative bounds
2*30+4/100<61 and 109/9+(4/9)/24<13. Their sum is 74.

**Pole integral, 45.** Each numerator derivative is below
1+12/pi<5, including the two translated Phi0 arguments and both
cosine weights. Two folded sides and the normalized denominator give
(5/pi)integral_delta^pi csc(z/2)dz<=5log(pi/delta)<45.
Integer cusps are handled by the original Lipschitz estimate; no
second derivative or unproved smoothness at integers is used.

**Endpoint cancellation, 8.** The exact sum is
4a cot(z/2)log(sin z). Its derivative is bounded by
pi^-2 log²(pi/(2delta))<8, using |4partial a|<=1,
cot(z/2)<=2/z and the sine chord. This is a fixed integration
interval and both q contributions already cancel exactly.

**Limiting jump, 1.** The rational q_R has q_R<1/100 and
|q_R'|<1/10000 on [0,1]. Product differentiation of
(2a beta/pi³)[q_R(t_R)-q_R(t_L)] therefore gives less than one
in each coordinate, including the derivative of the explicit beta.
The proof does not replace this finite constant by an infinite sum.

Thus every coordinate derivative is bounded in magnitude by
766+74+45+8+1=894<1000. Integrating along the phase segment proves
the asserted strict bound for rho>0 and equality at rho=0, as specified
in finding C02-1. Combining this with the independently accepted whole
central bound and (8) proves the main nonstrict modulus (1) as written.

## Scalar budget and precise onset meaning

N1-16 supplies A(L)>L²/11. If L>=10^6 then A>9*10^10. The allocations
D_l=A/2, D_f=A/4, D_e=A/4-1 sum to A-1, so the positive r² term
in (1) is charged exactly once. No negative coefficient loss is omitted.

From r²>=rho²/2, the linear maximum is 10^6/A<1/90000.
The fractional maximum is 27c^4/(32D_f³)=54c^4/A³<10^-8 for
c=15/32. For the entropy bracket, if it is negative the desired upper
bound follows from zero; if positive, r²<=rho² gives the scalar
maximum (1/(4e))exp(-4D_e)<10^-8. This sign distinction justifies
using the upper rather than lower comparison for r² in that term.
The formulas extend to rho=0 by continuity.

The exponential series gives e^L>=L^6/720, so
5,000,000(L+1)e^-L<=7,200,000,000/L^5<10^-8 on the stated
range. Hence Q_n-G_n<1/90000+3/10^8<1/40000. N1-18 and the
exact slack 1/40000+9/(2n)<107/3584000 then give the original
N1-17 increment comparison for every integer n>=ceil(exp(10^6)).

This is a proved explicit near-model comparison onset, not merely the
validity threshold of its approximation. It covers only the stipulated
near triangle and the associated C1 implications. It supplies neither
the original comparison at every n>=10^6 nor a global argmax onset,
far-phase result, new certified degree, or practical bridge computation.
The two MINOR findings above concern boundary wording and the inherited
finite-range status; the main quantitative proof survives both unchanged.

## Focused closure of the two wording findings — 2026-11-06

The author changed the source after the findings were delivered. Corrected
source SHA-256:
`a42be2a78546b02eec20326beba872965abc20810b879b70c770ae0d33d2f928`.
It states <= in (9) and says the certified finite range 2–40 is unchanged.
Both C02-1 and C02-2 are **closed**.

The reviewer read both corrected locations and independently verified the
complete change boundary: a read-only Python string/hash check reversed
exactly those two wording substitutions in memory and recovered the original
frozen SHA-256 `ddf639380417ed3af686d4818aff3714aec78f0086c3c3b87b6a87817fb6805d`.
The check passed; no other source byte changed. No file was reconstructed
on disk or edited by the reviewer. This was a source-integrity check, not
a mathematical diagnostic. The main mathematics and its constants are
unchanged, so the analytic acceptance above carries to the corrected source.

**Final disposition: accepted at the stated near-model scope, with no
unresolved finding.** Formal Claude audit remains pending. The original
n>=10^6 comparison and the global argmax theorem remain OPEN; certified
degrees 2–40 remain unchanged.
