# C02 dense-band defect: independent mathematical reconstruction

Rules read at `4b728b04216a5490910780bc609a82b853058426`. Reviewer: distinct Codex supplementary reviewer, allocated gpt-6-astra high; serving model/effort metadata unexposed. Date: 2026-11-06.

Frozen proof: `theory/C02-defect-dense-band.md`, SHA256 `d28bbc8f7ae3823ff220b452630b0c30c939b9851fa0c151d2ac5962a301dec7`.

**Verdict: ACCEPTED**, no unresolved finding. Both applicable projections are strictly greater than 1/64 for n>=64, 1/32 for n>=160, and 1/16 for n>=4096, on the complete stated radius-half domain. The separate fixed rational B_n(r) screen is valid. These are mathematical premises; executable source and formal Claude audit require their separate reviews.

## Scope and dependencies

Read the complete frozen proof and its C02 idea/attempt scope and fallback records. The accepted C01 all-class reconstruction, PD-T215/364 exact projection identities, and N5-03/04 finite-band predecessors were read in full earlier in this review session. The numerical constants and dense-band construction here were independently reconstructed below; no prior asymptotic minimum or observed full-Q value is used.

Historical novelty, priority and the claimed completeness of the author's gate are excluded. The full IDEAS novelty audit is therefore not invoked. The n64 uniform 1/16 primary target remains OPEN, and the n4096 conclusion does not close it. The record explicitly distinguishes the weaker fallback floors and later onset from that primary target. N5's quarter target and the earlier failed quarter certificate are not revived.

## Signed halves, parity and both branches

The exact pair-defect coefficient is 1/N after folding the reflected coordinate: an interior physical row represents two periodic orientations, and replacing both G values by common-sign halves contributes a further factor 2 to d. Endpoint half weights remain in the formulas, but every selected physical row is interior. The two opposite periodic branches counted below are additional distinct points within this already normalized sum; they are not an extra change of weight.

For a vertical row, periodic p+k has the parity of J. For a horizontal row, periodic q+j has the parity of K; the first-coordinate integers J+j and J-j have the same parity, so both halves share the sign factor. The numerator is exactly

    a_actual(1+cos v)-sin(alpha)sin u/2+sin(beta)sin v/2.

The horizontal baseline is the fixed second angle v. All numerator estimates use a_actual>=1-r^2/4 and total sine perturbation <=r/2, preserving the exceptional x mode.

Near the upper endpoint the proof uses the reflected physical row M-l. Its two cosine targets are cos(t+b) and cos(t-b), just as for a lower center with row l. Thus the selected periodic angles can be close to b on both orientations; no unproved positivity under a kernel transpose is used.

For endpoint distance s=1,...,4, q runs through s integers from -(s-1) to s-1 in steps of 2. At a lower center the physical-plus-periodic parity is q=1-s modulo 2; at an upper center it is M+q=1-M+s modulo 2. These are the required complementary-center parities for either axis, regardless of the other center's position. Negation modulo 2L preserves parity.

The selected positive indices l+q lie strictly between 0 and L; their negative representatives are distinct and lie on the other half-circle. Distinct q values are distinct indices for each fixed physical row. Hence the count really is 2s points per selected row, with no duplicate endpoint or branch.

## Near and small-angle bounds

The near displacement is

    M(w-b)=(M/L-1)l*pi+(M/L)q*pi+(M/L)phase.

Adjacency of M,L and the bounds l<=M/2, |q|<=3 give the residual coefficient 71/128 after extracting (s-1)pi. Including both phase magnitudes leaves strict slack at least (57pi-65)/128>0. Therefore every selected periodic angle lies strictly between b-t and b+t. With b in [pi/4,pi/2] and t<7/30, all selected angles are inside (0,pi), and all denominators are regular and opposite in sign.

The vertical targets and horizontal fixed periodic cosine are >=-sin t>-t. Thus each numerator exceeds (15/16)(1-7/30)-1/4=15/32. The full denominator span is <=2t, giving d>15/(32t). Counting 2s(M/4-1) points and dividing by LM gives the displayed bound (16). Using M/L>=64/65 and 1/4-1/M>=15/64 yields 225/[1040(pi+1/2)]>1/20. This covers all four closest center distances for both axes and orientations.

For remaining distances, gamma>4pi/L follows from L(pi-1/2)>4pi in the worst adjacent-mesh orientation. When gamma<pi/6, physical rows in [pi/6,pi/3] give two disjoint periodic arcs of length 2gamma each. Each arc contains at least Lgamma/pi-1 points of either shifted parity, so together there are at least 3Lgamma/(2pi), since Lgamma/pi>4. All relevant baselines are >=1, giving d>=11/(8sqrt(3)gamma). The row count M/6-1 yields 957/(3072pi sqrt(3))>1/20 uniformly from n64. Retaining the exact row count gives the stronger expression used at n4096.

## Dense middle band and finite lattice losses

For gamma>=pi/6, write the two targets as z0±D with z0=cos(gamma)cos(b)>=0 and D=sin(gamma)sin(b)>0. They lie in [-1,1]. On their open cosine interval, both numerator baselines are >=1-sin b, including the horizontal fixed-v baseline. Thus A(b)=a-r/2-a sin b is a common positive lower bound on [pi/20,pi/4]. Positivity at r=1/2 follows from sin(pi/4)<11/15; smaller radii retain it.

The larger absolute denominator is D+|x-z0|, so the pair defect is at least 2A(b)/(D+|x-z0|). Capping this by (A/D)c, c=5/4, gives precisely the nonnegative function (19). Its positive superlevel set is one cosine-coordinate interval; its inverse image consists of one arc per half-circle. The shifted parity-grid count therefore loses at most two points per level. Layer-cake integration proves the loss 2 max f in (11), including when a superlevel arc touches 0 or pi. Strict/open band endpoints cause no additional loss.

Direct integration with y=(x-z0)/D and split |y|=2/c-1 gives

    integral f(x) dx =A(4-2c+4log c)=TA.

The full-circle angular integral equals 2 integral f(x)/sqrt(1-x^2) dx and is >=2TA. Thus the finite row bound is LT A/pi-2cA/D. No limiting Riemann-sum assertion is substituted for this exact finite inequality.

Both A(b) and A(b)/sin b=C csc b-a are positive and decreasing. For any band endpoints, their physical-mesh sums differ from their integral divided by mesh spacing by at most their left endpoint value. Using the lower estimate for the positive main term and the upper estimate for the negative loss is essential. With sin gamma>=1/2 this gives

    Q >= TI/pi^2 -T A0/(pi M)-4cR/(pi L)
                        -4cA0/(LM sin a0).

Replacing L,M by their lower bound n produces exactly (23), with 4c=5, including its n^-2 loss. This verifies every lattice-loss coefficient independently.

## Rational radius screen and uniform onsets

The elementary trigonometric/exponential bounds in (24) suffice with strict rational slack. In particular, the positive exponential sum through degree 7 at 5/3 equals 5833853/1102248>830/157. The logarithm bounds are therefore analytic inequalities, not floating approximations.

The substitutions in (22) give

    I>347a/1000-157r/500=U,
    A0<17a/20-r/2=V,
    R<779a/750-5r/6=W.

They are positive on 0<=r<=1/2. Applying T>239/100 and pi<22/7 to the positive main term gives coefficient 11711/48400. Applying upper T and lower pi or sine to the three negative terms gives respectively 120/(157n), 250/(157n), and 100/(3n^2). Thus the stated B_n(r) is a valid lower bound in the middle case. Together with >1/20 in the other cases it gives min(1/20,B_n(r)), even if B is negative. Taking its maximum with an independently valid constant floor is safe.

At r=1/2 the weaker constants I>21/125, A0<11/20, R<14/25 give E_n. Every negative term decreases in magnitude with increasing n, so E_n increases. Exact Fraction arithmetic independently reproduces

    E_64-1/64=34466881/729484800000>0,
    E_160-1/32=88079689/182371200000>0.

For n>=4096, t<1/45 raises the near numerator to >=2/3 and yields the claimed near floor >1/16. The sharper small-angle row count, with pi<22/7 and sqrt(3)<26/15, exceeds 1/16 at n4096 by 1733/3407872 and increases thereafter.

In the middle case, c=2 and band [pi/100,pi/4] give T=4log2 and loss coefficient 4c=8. The stated bounds I>6/25, A0<11/16, R<8/5 and sin a0>3/100 follow from the same finite trigonometric bounds. Squaring the positive exponential lower bound gives the required logarithm <10/3; the series for log2 supplies 11/4<T<14/5. Exact arithmetic reproduces H_4096-1/16=3436012187/1086534451200>0. Monotonicity again extends this to every larger n.

## Exhaustion and backend boundary

Every applicable interior-coordinate projection is covered by near distance 1–4, remaining small gamma, or middle gamma. Every odd noncorner center has at least one interior coordinate. Delta>=max(Q_v,Q_h) therefore proves the whole-class floors, with true-corner centers explicitly excluded.

A future implementation needs exact integer degree checks and a full-box bound maxabs(alpha)+maxabs(beta)<=r<=1/2. The constant tiers additionally require n>=160 or n>=4096. The rational B_n(r) formula needs exact or directed arithmetic throughout; a float sample or box intersection with the diamond is insufficient. The accepted theorem does not approve such an implementation, remove the separate corner predicate, or certify a global degree.

No mathematical NOTE, MINOR, MAJOR or BLOCKING finding. One independent standard-library Fraction invocation checked the exact margins and constants reported above, exit 0, negligible CPU within the 60 CPU-s cap. No phase, kernel, degree scan or numerical integration was run, and that arithmetic check is not a proof premise. Frozen author bytes were preserved.
