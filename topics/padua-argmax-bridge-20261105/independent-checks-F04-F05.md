# Independent mathematical checks — F04 entropy cells and F05 transport band

2026-11-07. Distinct Codex supplementary auditor; requested/API-accepted
`gpt-6-astra` ultra, actual serving metadata unexposed. Root's prior written
hard-mathematics justification is in LOG. Rules read at the supplied full
baseline `4a5de2012bad94601c713b2ff5517f2e3fb80af2`; observed HEAD during
dependency review was `7cf34bcee4be9bdd5b4a871426083333a89b7c15`.

Scope is **mathematical validity, definitions, dependencies and edge cases
only**. No novelty/priority judgment, complete novelty-gate certification,
protocol waiver, final-ID review or PR-readiness decision is supplied.
Accordingly the complete ideas registry is not reread for a novelty verdict;
the actual mathematical dependencies and current idea/attempt contracts are
read. F04's chronology remains canonical in
[its attempt](attempts/F04-entropy-cell.md), without disposition here.
Final Claude audit remains separate. Root alone owns Git and shared records.

## Review in progress; no final verdict

Root's exact F04/F05 freeze is required before a final verdict. Moving draft
files are not approved by this preliminary record. Only this audit file is
owned or edited by this auditor. No scientific script/import, numerical or
scalar evaluation, selected degree/endpoint, native or quadrature job ran.

The rules, handoff11, current campaign F contracts, F04/F05 local idea/attempt
records, accepted F01 review and all three F01 EM2 records were read. Relevant
mathematical predecessors read include C06-far-compact-error's generic J,
E12-signed-outer-coupling, E14-wide-signed-outer, E03-joint-row-origin,
E03-joint-outer-log, E05-axis-central-excess and E06-axis-boundary. Accepted
predecessors remain named dependencies; this review is not a recursive
re-certification of every earlier proof or numerical enclosure.

The literal Q operator has m-3 samples, centers h(k+tau), k=2,...,m-2,
and omitted lengths h(3/2+tau) and h(3/2-tau). The paired offsets t,1-t
therefore retain initial total4h and central total2h. For cancellation B,
the exact correction in F04 cancels the constant endpoint part of each
actual hole individually. Other logarithms, pole profiles, fixed-origin
Shift and the separate mesh component do not enter this scalar estimate.

F01's accepted entropy obstruction applies to these unchanged B profiles:
finite global Var(B') cannot be used. F04's proposed proof instead needs an
integrable first-derivative envelope on singular cells and variation only
on the union of cells a positive distance from the complete feature set.

For F05, the accepted exact starting point is the E05 identity

    E_n(alpha,0)-E_n(0)-ell_n sin(alpha)
      = B_n(alpha)-B_n(0)-M_nc(alpha)+M_nc(0)
        + Rcen + (4/(nm)) sum_r Y_r - E_c(alpha,0).

The fixed origin signs define continuous transported Y_r through alpha=e_s;
the natural moving-sign pieces individually have finite opposite jumps.
The signed inner model integral, full smooth background and finite ell_n
cannot be dropped. E06's finite convex-cell estimate has alpha<=h/2 and
cannot certify the new closed c interval through c=1 by substitution.

Further freeze-specific reconstruction and findings will be recorded below.

## F04 frozen reconstruction and verdict

Root explicitly confirmed the final F04 freeze. Independent `sha256sum`
and `wc -c` checks matched all three supplied identities, and the complete
theory was reread after that confirmation:

| File under this topic | Bytes | SHA-256 |
| --- | ---: | --- |
| theory/F04-entropy-cell.md | 14365 | `5408e6a26bb0588a2398cc6c78bae040890f3b5f7817ae97177572cc2aeda330` |
| ideas/F04-entropy-cell.md | 8530 | `49d1e469d8c3112a140dace859cc5c8a857c7d0061ed2ef318b498ea9b9b380a` |
| attempts/F04-entropy-cell.md | 4326 | `ccb336cdba14c52d26efe4dee0d799afc28a2716ecb0bd627a188a243fedb90f` |

The frozen outcome additions to idea/attempt were also read. The generic
N1-round6-central-log formulas were read in full, with D37 section6's
radius-one application checked separately; N1's older half-radius bounds
were not silently extended. A read-only Git comparison reports no change
to the three rule files between the supplied rule SHA and observed HEAD.

The central identity follows by substituting
`J=2(s-u)_+ log(sin e)+R` and subtracting the exact origin
`2a tan(e/2)log(sin e)`. Thus `b_s(0)=0` and the signs of the added
initial logarithms in equation(2) are correct. At zero the initial
formula has limit `-d log pi`; at pi the only nonzero limiting terms
are the finite entropy R and `sigma_s q log pi`. The logarithmic products
with b_s vanish there. These are profile limits, not substitutes for
actual retained polynomial rows.

For `s>u`, writing `D=sqrt(u^2-s^2 sin^2 e)` gives
`(u cos e)^2-D^2=(s^2-u^2)sin^2 e`. The elementary inequality
`A-B<=sqrt(A^2-B^2)` for `A>=B>=0` proves `R_e<=2s` in the root
branch; `u<=s sin e` proves it in the no-root branch. When u=0,
R is identically zero. On every affine-sign piece the nonzero slope
of s with respect to e has magnitude at least a/2>1/3. A coefficient
zero, or the endpoint of a piece containing no zero, therefore controls
the denominator in `log((u+s)/|u-s|)` by distance to a listed feature.
This proves the uniform distance envelope without a lower bound on p,
root separation or distance of a feature from a sample.

The quartic P is genuinely nonzero, since `u^2-4a^2<0`. Its four-root
bound applies across the right absolute-value switch because s^2 has
the same polynomial on both sides. Coefficient zeros and the switch
give at most8/10 total sites after endpoints and the join are included.
The derivative-critical equations were reconstructed directly:

    (R_s)'=0 implies 2X'P-XP'=0,
    (R_e)'=0 implies 2P-xP'=2u(1+x^2)sqrt(P).

The first polynomial has degree at most6 and the squared second has
degree at most8. Squaring is used only for an upper bound on candidates.
In the identically-zero first case the ratio sqrt(P)/X is constant on
each root interval. In the identically-zero second case the unsquared
left side cannot change sign while P>0 and u>0; the original derivative
is consequently identically zero or strictly negative. The same-sign
and no-root pieces are monotone directly. Adding the coefficient and
quartic boundaries gives the stated12/14 pieces per affine piece,
hence24/28 per side. Values agree at the finite root transitions;
the divergent coefficient-zero sites are excluded from the good set.
Repeated and coalescing roots only reduce the partition count.

The total variation on disconnected good intervals is correctly defined
without variation across gaps. Restrictions of one monotone piece spend
at most its full range, even if a number of gaps cut that piece. Product
variation then gives52A for R_s*s',84 for R_e,24A for b_s'log(sin e),
14A for b_s cot e, and the stated smooth and initial/join charges.
Thus each side costs at most90A+94, and their sum is below400A for A>1.
No claim of globally finite Var(B') is made.

For a singular cell, integrating the distance logarithm over an arbitrary
interval gives the bound at its actual center, including equality of a
sample and feature. Absolute continuity follows by truncating at finitely
many features, using their continuous limits and the integrable envelope.
At most100 bad cells is conservative: a site affects only centers in an
interval of length3h. The remaining actual cells use the centered Peano
kernel with maximum h^2/8. This is a fixed-sample estimate, not a
translation-averaged estimate.

The four omitted intervals have their literal lengths in[h/2,5h/2].
After the endpoint correction, their total cost is bounded by1125 times
`(h^2/pi)[1+log(24/h)]`. The bad and good cells add6000 and50 in the
same units. Their sum is7175. Since `h^2/pi=pi/m^2`, `pi<4`, and
`log(24/pi)<log8<3`, the resulting bound is strictly below
`114800(1+log m)/m^2`, hence below the claimed120000 bound. These
comparisons were reconstructed as written inequalities, without a scalar
evaluation or selected-degree job.

**F04 ACCEPT:** no unresolved mathematical finding in the frozen claim.
The accepted scope is precisely all integer n>=32 and the closed signed
band1/32<=rho<=1, with separate absolute phases, both parities, axes and
coincident features. For boxes extending beyond this band only their
intersection is covered. This certifies the cancellation-block feasibility
bound and its four endpoint corrections. It supplies no useful onset,
five-fourths extension, full I06/D13 estimate, implementation or numerical
certificate. F04 chronology, novelty/priority and final Claude audit remain
outside this mathematical verdict. F05 is still awaiting its exact freeze.

## F05 final freeze, resolved finding and reconstruction

Root confirmed the final five-file F05 freeze after author clarification.
Independent byte counts/hashes match the following; all three theories were
reread together after root confirmation and hashes rechecked:

| File under this topic | Bytes | SHA-256 |
| --- | ---: | --- |
| theory/F05-joint-error-background.md | 8945 | `fd23e025300a2855fcc6223727a6b722254a1b848bbc8457e45289e37c662c60` |
| theory/F05-joint-error-central.md | 8961 | `6f81cba073a0c4336251927315846b46c36d800b1281861f169908446e32972d` |
| theory/F05-joint-error-crossover.md | 5335 | `a879e964b911e1847f357faf255f5bada994ec4119c7a17c245b8c847132fa1f` |
| ideas/F05-joint-error-crossover.md | 10644 | `fc7ab94c71da51e851dbdaf513448c2b828de1d87d4b6b35b84a1fbd71d9678a` |
| attempts/F05-joint-error-crossover.md | 7775 | `785e5243aa3372bc828e125083d8aa16a22c8b6dca974891c85fb59f986aa487` |

**MINOR, resolved:** central section1 originally wrote the bare cotangent
reference as an unqualified sum over k, although the actual linked vector
runs over all n residues and the bare reference is undefined at k=0.
The author, after root direction, specified k=1,...,n-1 for that reference.
The actual linked vector keeps every residue. The original8951-byte central
hash was `dcf7c2542c1c315ddda2eb45d507a9926016736a813869c65385fe0d909f82b6`.
The changed display and preserved attempt chronology were inspected; this
correction supplies no artificial cotangent value and changes no bound.

A bounded supplementary reader, `f05_collision_check`, inherited the
requested audit model/effort (serving metadata unexposed), independently
checked the first-row masks, linked peaks, harmonic coefficient and stated
finite constants. It edited no files and ran no scientific computation.
Its check supplements this auditor's complete reconstruction and verdict.
The E08 full phase-global error and D16 phase-allowance records were read
in full; E02(24) and D27's global norm/period adapter were checked at the
relevant passages. Thus the background norm has its n>=32 support and
does not borrow C06's n>=10^6 conclusion below that degree floor.

For the background, the exact negative mask is
`j=r+1,r+3,...,2n-r-1`. Its cotangent reflection gives the displayed T_r
identity with q=n-r; the mask is empty at r=n. Direct differentiation gives
`B_r''(0)=-B_r(0)/2+cot(v_r/2)T_r''(0)-T_r'(0)`, which reconstructs
the full curvature formula including the constant1 in B_n. No transported
positive peak is inserted into this fixed mask.

The differentiated partial fractions have factors n/(2pi^3) and n/(2pi^2)
as stated. Missing positive tails, the nearest negative image and the two
distant image tails give the uniform S3/S2 bounds, including q=0. Splitting
r at m/2 correctly handles both ends of the cotangent weight. Replacing
Z3(nu_r) by Z3(1/2)=7zeta(3), then cot by its reciprocal and H_n by L,
produces A3=28zeta(3)/pi^4 with error below10 after the square contribution.
The accepted actual-origin allowance yields the coarse E0<10 directly,
without an origin-sign assertion. The model derivative is
`b''(0)=-b_c/2+A3+2/pi^2`; the alpha*sin(alpha) term is essential to
the final2/pi^2. Its cancellation with the actual background leaves
`-alpha^2 L/pi^2` after the Taylor factor1/2.

The global norm and endpoint polynomial functional justify the uniform
background Taylor estimate. The reciprocal-series and elementary model
remainders are within the stated coefficients. In particular
`H^2 h^2<1/4` follows from pi^2<10 and H/n<5/32, so
`29alpha^2+1002H^2 alpha^4<600alpha^2<=1350h^2` stays below2000h^2.
These are all-degree inequalities, not endpoint evaluations or asymptotic
constants depending on c.

For the first transported row r=n, the original negative mask is empty for
both parities, so Y_n is exactly its actual negative-part sum. Only this
row can cross a denominator on the c interval. The two linked peaks remain
positive. At c=1 the first has actual value `(n-cos h)/2`, including the
n/2 contribution that would be lost by using the off-grid rational limit.
Outside the peaks, the coefficient equality is exactly
`w(sin theta_-+sin theta_+)=sin(alpha)/2`. The two cotangent shift errors
are bounded by h^2*n/12 and5pi*h*n/4, totaling below14; the harmonic
replacement costs below3. The stated30 remainder therefore covers both
parities and every moving sample zero. The corrected reference sum includes
the even-n zero midpoint harmlessly through its negative-part definition.

The local signed model estimate on x in[0,5/2] keeps E(0)=-p log2.
Its entropy and positive-root branches give
`E(hx)/h=L min(x,c)+O(1)` with the explicit uniform50 bound. The small-h
and large-h estimates cover their common boundary; the positive-root
integral differs from log(1/X) by at most1/2 even as lambda approaches1.
This retains the inner negative entropy interval and requires no gap from
the crossing x=c.

The matched centered-cell functional of min(x,c) gives exactly
`c(c-1)/2` for c<=1 and `(c-1)(c-2)/2` for c>=1. Subtracting it does
not evaluate two divergent infinite quantities: every constant tail cell
has zero matched error. The first two cells and missing half-cell spend
at most225; convexity of the actual outer E beyond5h/2 bounds the remaining
derivative variation by4 and its unit midpoint error by1. This proves
the stated250h^2 signed grid remainder, including c=1/2,1,3/2.

All remaining actual rows have e_s>=2h>alpha, within the accepted outer
first-coordinate estimate. The first-row replacement adds precisely
`(2/pi^2)[c-min(1,c)]h^2 L` and less than28h^2. Consequently the central
coefficient is c(c-1)/pi^2 and its full error is below
`[28+500/pi^2+2]h^2<100h^2`, safely within200h^2. Neither a signed
boundary piece nor a first-coordinate cell is omitted.

Adding the background coefficient -c^2/pi^2, central coefficient
c(c-1)/pi^2 and the exact Rcen<h^2 gives the complete coefficient
-c/pi^2 with total remainder at most2201h^2<10000h^2. The finite ell_n
cusp remains explicitly subtracted throughout. Finally nh/c<=2pi<7 gives
the claimed C70000 corollary from the nonpositive logarithm. This establishes
uniformity by finite estimates before taking the limit.

**F05 ACCEPT:** all three frozen mathematical statements, including the
two2000/200 supports, complete10000h^2 remainder, uniform signed coefficient
and C70000 upper, hold at their stated n>=32, beta=0, closed c in[1/2,3/2]
scope with both parities and the polynomial collision. The sole MINOR
finding is resolved; no unresolved mathematical finding remains. The full
two-dimensional cusp-aware target, subsequent transported rows, useful onset
constants and all finite-degree/global argmax consequences remain outside
this verdict. No F04 result is a premise of F05.

## Final scope and verification boundary

**Final mathematical ACCEPT for F04 and F05 at the exact freezes above.**
No novelty/priority verdict, chronology waiver, final-ID application or
readiness approval is supplied. Root adoption and final Claude audit remain
separate. The preliminary pending text above records the actual review order
and is superseded only by these freeze-specific final verdicts.

Commands used: read-only pwd, rg, cat, sed/tail, git rev-parse, git diff,
wc and sha256sum, plus administrative runtime/skill reads and owned audit
prose edits. No developer file edit, scientific execution or Git mutation
occurred. Accepted predecessors retain their original proof/trust scope;
their full histories and computer enclosures are not recursively recertified.
