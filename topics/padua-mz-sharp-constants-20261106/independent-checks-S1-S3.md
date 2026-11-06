# Supplementary analytic checks: S1 and S3

Date: 2026-11-06. Codex supplementary independent checker, requested
`gpt-6-astra high`; actual runtime model/effort metadata is unexposed.
Rules/source input: `2143ad622fa98faf8fe7d5cb8ed2bb7e0062f861`.
This is mathematical-validity review, not full novelty, priority or
registry-disposition approval. The required Claude audit remains separate.

## Verdict and frozen records

**PASS for all three statements at the final hashes below.** One MINOR
complex-valued display issue in the Volterra proof was returned to the
developer and fixed. No unresolved BLOCKING, MAJOR or MINOR finding
remains in this scope. No numerical mathematical experiment was executed
or used as evidence for these analytic conclusions.

| Record | Final audited SHA-256 |
|---|---|
| [S3 normalized carrier improvement](theory/S3-normalized-carrier-improvement.md) | `4347162a0ed3cfb2c830860530f7a22c500d1d4889a1b395db8728ef76c8bd13` |
| [S1 Volterra norm](theory/S1-volterra-model.md) | `13975d980264e3b89304ebd14f20f8d07207fe3ec066fb019566615038f65f0e` |
| [S1 one-sided CC bound](theory/S1-sharp-one-sided.md) | `b560b08db44f25417e36c4ff53f76baf0f14e2ae9130eb7457d1249b11a32eb0` |

Read each target in full. PD-T013/017 and PD-T379 were read in full
during this session's earlier checks; their normalization, degree and
parameter restrictions were rechecked for these applications. The
statements/definitions of PD-N105 and PD-T378 were reread to verify
the inherited both-parity signed carrier scope. The S1 preregistered
model record was read to distinguish its transfer claim from the
separate theorems. No full novelty audit is claimed: this assignment
tests the specified proofs and explicit dependencies, proposes no new
mechanism, and leaves full IDEAS/literature coverage to Claude.

## S3: rational strict improvement

For h(q)=q²log q on q>0,

    h''''(q)=−2/q²,
    (1/2) Delta^4 h(q−2)
      = 3h(q)−2h(q+1)−2h(q−1)+(h(q+2)+h(q−2))/2.

Thus four fundamental-theorem integrations give exactly the displayed
unit-four-cube integral for C(q). Its arguments lie in [q−2,q+2],
strictly inside the positive axis for q>2. Differentiating this smooth
compact integral gives C'(q)=2 integral x^−3. Its argument has mean q;
convexity, or the stated tangent inequality, gives C'(q)>=2/q³.
All signs and factors check.

On 1/4<=a<=51/200, q=1/a is between200/51 and4, hence above2.
The inherited norm representation supplies J(a)>0. C(q)<0 and the
chain rule yield

    J(a)<2log2<7/5,       J'(a)<=−a.

The logarithm estimate is strict: the fourth Taylor partial sum of
exp(7/10) equals482921/240000>2, and the omitted terms are positive.
For N(a)=a(1/2−a), N' lies in [−1/100,0]. Consequently

    N'J−NJ' >= −7/500+a²(1/2−a)
              >= −7/500+(1/16)(49/200)
               =21/16000>0.

Both lower factors are valid simultaneously on the entire interval.
Division by J² is legitimate, so N/J is strictly increasing there.
At a=1/4,16N(a)=1, recovering exactly the previous constant;
a=51/200 therefore gives a strict improvement, not merely a decimal
comparison. The reported numerical optimizer plays no role.

The application to spectra respects the open parameter triangle:
first fix a=51/200 and b<49/200, apply the inherited signed quotient
limit on each parity, and only then let b rise to49/200 in the scalar
upper inequality. No boundary-degree family or interchange of m and
parameter limits is required. The limsup over all integers is the
maximum of the two parity limsups. This proves the stated one-sided
bound but neither existence of extremal limits nor their equality.

## S1: Volterra norm and resolved MINOR finding

The original hash was
`8b2ba6af453b521a190772c3365acab4521b3023a67b53925cbdb2da66b1d111`.
Its statement allowed complex L², but the completed-square display
wrote an ordinary square. The developer changed that display to the
absolute square. A byte-level check confirmed that reversing precisely
this display change restores the original hash; no other bytes changed.
This corrects notation for the stated complex case and changes no
theorem or argument. Finding disposition: **fixed**.

For a=pi/2 and beta(x)=a cot(ax), expansion of the corrected square
uses −2Re(F' conjugate(F))beta=−beta (|F|²)'. Integration by parts
therefore gives beta²+beta'=−a² in the bulk and boundary term
−[beta|F|²]_0^1. At1 beta vanishes. At0 smooth F with F(0)=0 is
O(x), so beta|F|²=O(x) tends to zero. All integrals in this smooth
calculation are finite.

It follows that ||F||<=a^−1||F'||. Smooth approximation preserving
the zero trace extends this inequality to all H¹ functions with
F(0)=0; no extra condition at1 is introduced. Explicitly one may
approximate in H¹ and subtract the approximant's value at0, using
continuity of the trace. It is the resulting inequality that passes
to the limit, so no unstated weighted convergence of beta F is needed.

Every L² f has primitive F=Vf in this H¹ space. Taking F=sin(ax)
attains equality; equivalently f=cos(ax) is an extremizer after a
harmless scalar normalization. Thus ||V||=2/pi and the displayed
quotient infimum is pi⁴/8. The direct-sum norm is unchanged, and the
pair (f,−f) has twice each squared norm, attaining the same ratio on
the antisymmetric subspace. This is a continuum theorem only.

## S1: finite CC one-sided theorem

The separate theorem proves an actual finite-problem asymptotic
limsup bound. Its argument was reviewed in full, not inferred from
the Volterra calculation. The checks below keep f fixed first, then
take N→infinity, then remove output cutoffs and optimize f.

### Admissibility and discrete mass

For fixed nonzero compactly supported C¹ f, choose0<a<b<1 around its
support. The left nonzero nodal amplitudes lie at N^a<=k<=N^b<N/2
eventually. Reflection gives a_(N−k)=−a_k and zero endpoints/central
value, cancelling the top DCT coefficient exactly. Hence the nodal
interpolant lies in Pi_(N−1) for both parities. Its nodal values obey
v_(N−k)=(−1)^(N−1)v_k, so polynomial uniqueness gives the asserted
reflection parity and equal endpoint masses. Continuity and a nonzero
interval of f ensure a nonzero sample for every sufficiently large N.

PD-T017's uniform absolute weight error O(N^−2), divided by the main
weight pi²k/N², is O(N^−a) on this support. The sine expansion error
is O(N^(2b−2)). For h(u)=f(log u/L)²/u, its integrated absolute
derivative is O_f(N^−a), justifying the log Riemann sum with o(1)
absolute error. Multiplying by the nodal square and summing both
equal endpoint contributions yields exactly

    Q_N(p_N²)=2*pi²*L*||f||²+o_f(L).

### Residual of the homogeneous kernel

Below t the residual kernel is k/(t²−k²); above t it is
t²/[k(t²−k²)]. Summing the ranges k<=t/2 and k>=2t gives an
absolute O(1) bound by comparison with k/t² and t²/k³ respectively.
In the middle range, subtraction of 1/[2(t−k)] leaves exactly
−1/[2(t+k)] below t and (2t+k)/[2k(t+k)] above t. Their absolute
sum is bounded.

Replacing g_k by g(t) in the pole sum costs O_f(1/L): the Lipschitz
bound in logarithmic coordinates cancels |k−t|, leaving O_f(1/(Lt))
per term and O(t) terms. Around the nearest integer j, the paired
pole terms are2u/(u²−r²), where u=t−j and |u|<=1/2. Their r>=1
sum is absolutely bounded; the center1/u is bounded after multiplying
by sin(pi t). An endpoint-rounding term in the pairing is at distance
comparable with t and is harmless. Unpaired tails have O(t) terms at
distance at least a fixed multiple of t. Bounded small t can be
handled directly. This proves the uniform sine-weighted residual.

The truncated log sum S(t) differs from L F(log t/L) by O_f(N^−a)
uniformly in t. Sum-integral comparison uses the integrated derivative
of f(log u/L)/u, with a possible endpoint term of the same order.
Multiplication by the homogeneous prefactor absorbs this error into
O_f(N/t). At integral t the sine cancels the interpolation pole;
the products, rather than the unsmoothed pole sums, extend continuously.

### Exact cotangent error

The exact identity for −sin(theta)/(cos theta−cos phi) has the stated
sign and factor1/2. Put e(z)=cot(z/2)−2/z. Its removable extension
is odd with bounded derivative on a fixed small interval. Thus

    e(theta−phi)+e(theta+phi)
      = e(theta−phi)−e(−theta−phi)=O(theta),

uniformly even when theta approaches phi. This verifies the curvature
error without estimating each singular term separately. On the right
reflected support cos theta−cos phi stays away from zero, giving
O(theta). Since sum|a_k|=O_f(NL) and the exact cardinal formula has
factor1/N, both curvature and reflected-support errors contribute
O_f(theta L). The homogeneous error remains O_f(N/t). These estimates
give the displayed formula(H) uniformly on the prescribed output range.

### Continuous mass, factors and limits

For fixed delta in (0,1/2), use N^delta<=t<=N^(1−delta).
The Jacobian is pi²t/N² times1+O(N^−2delta). The two error terms
in(H) have squared norms O_f(L) and O_f(L²N^−4delta), respectively.
The leading term has squared norm

    4L² integral sin²(pi t)F(log t/L)² dt/t
      =2L³ integral_delta^(1−delta) F²+o_f,delta(L³).

The coefficient4 follows by multiplying the squared interpolation
prefactor by the Jacobian. The factor1/2 follows by one integration
by parts of the cosine term: the amplitude and its integrated
derivative are O_f(N^−delta). This uses only bounded F and f.
Cauchy–Schwarz, or the norm triangle inequality, bounds the cross
terms by O_f,delta(L²)+o(L²), below the L³ leading scale.

Reflection doubles the endpoint mass, and these two intervals are
disjoint eventually. Discarding the remaining nonnegative continuous
mass is valid regardless of the sign of f. For every fixed delta this
gives a lower liminf4 integral_delta^(1−delta)F². Letting delta tend
to zero after N establishes the full factor4||Vf||² in(C).

Since Vf is nonzero for nonzero f, the Rayleigh quotient now gives
limsup L²lambda_min <= (pi²/2)||f||²/||Vf||². Compactly supported
C¹ functions are dense in L², and V is bounded by the checked model
lemma. Approximating cos(pi x/2) therefore takes these quotients to
pi⁴/8. This final approximation occurs after the fixed-f limsup;
no uniform-in-f asymptotic estimate is assumed. All constructions
apply to every sufficiently large integer N, proving both parity
versions as well as the all-integer statement.

## Limits and K2 disposition

The coordinator reported K1 PASS and an operational K2 kill of the
preregistered equality prediction. This report does not independently
audit those fitted numbers. That gate verdict does not refute the
Volterra norm identity or the separate one-sided theorem: a fitted
intercept is not the true finite-N limit, and a limsup upper bound
alone asserts neither equality nor convergence.

The approved results are precisely the S3 strict one-sided carrier
improvement, the continuum norm, and the S1 limsup upper bound.
No reverse S1 inequality, full model transfer, sharpness, spectral
limit existence, extremal parity agreement, or fit validation is
approved here. Required Claude mathematical/novelty audit and final
registry classification remain separate.
