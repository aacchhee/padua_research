# Supplementary independent check: P3 signed remainder

Date: 2026-11-06. Role: distinct Codex supplementary mathematical checker.
Requested allocation: `gpt-6-astra high`; serving model/effort metadata is
unexposed. Rules/scientific source:
`0205690b9c4e959a28e949083e9a1808735abf4b`; R publication:
`17ca9f441cece178354e70504a6c739df501a224`.
The coordinator supplied the pinned source corpus in a non-Git directory.
No Git state or developer files were changed by this checker.

## Verdict and exact scope

**PASS** for the all-input signed homogeneous remainder theorem in
[theory/P3-signed-remainder.md](theory/P3-signed-remainder.md), frozen by
its developer and independently hashed as
`17f357a92a448ef2ad49d406111dcd0d7ce57de8519dc712424ae6f9eb4d29ed`.
No unresolved finding in this theorem's mathematical-validity scope.
This supplementary check does not replace the required Claude audit.

The reviewed conclusion is exactly

    ||Eg||_(L2((0,infinity),dt/t)) <= 40 ||g||_(ell2(1/k))

for every finitely supported real or complex sequence on positive integers,
with E and its strict indicator as defined in the theorem. In particular,
this is uniform in the support's size and location and does not assume a
smooth envelope. It does not yet prove the reverse CC bound or upgrade
PD-T020: the sharp primitive, actual weights, cotangent correction,
endpoint columns, bulk and interaction of opposite sides require their
own assembly verification.

Read the rules, handoff03, audit01 A1 and P3, the accepted S1 Volterra
and one-sided proofs, and the earlier supplementary S1 checks. The signed
remainder proof was read and independently reconstructed in full. This
is mathematical validity review with no new mechanism or priority claim;
full IDEAS/literature novelty coverage is outside this check's scope.
The newly present discrete-primitive file was read for context, but is
not included in this frozen verdict.

## Reconstruction

### Sinc identity and the meaning of the signed estimate

For integer shifts the finite Gram matrix of sinc(t-k) on the full real
line is the identity. The diagonal follows by integration by parts from
the Dirichlet integral. Its stated damping argument is legitimate:
exp(-epsilon u)/u decreases, so integration against sin(bu) has an
O(1/(bR)) tail beyond R uniformly in epsilon>=0. This supplies the
required passage from the damped arctangent value to pi/2.

For distinct integer k,l, partial fractions reduce the integral to a
constant times the difference of the symmetric-cutoff integrals of
sin^2(pi t)/(t-k) and sin^2(pi t)/(t-l). Each tends to zero after the
integer translation: the translated integrand is odd, and only intervals
of bounded length at distance R remain, giving O_(k,l)(1/R). The original
product is absolutely integrable. Thus no individually absolutely
convergent integral of sin^2(pi t)/(t-k) is incorrectly asserted.
Expansion of the finite absolute square proves the Gram identity for
complex coefficients as well.

Only this unweighted identity on R is invoked. No global weighted sinc
or Hilbert-transform theorem, and in particular no global A2 property
of dt/t, is assumed. The dyadic localization below is essential.

### Exact decomposition, dyadic overlap and poles

For nonintegral t,

    t^2/[k(t^2-k^2)] = 1/k + 1/[2(t-k)] - 1/[2(t+k)].

Subtracting 1_(k<t)/k gives exactly the displayed D_k. For t in
I_j=[d,2d), d=2^j, the near input set is d/2<k<4d. For any fixed
positive integer k these j lie in the open interval
(log2 k-2, log2 k+1), so at most four memberships is a valid conservative
bound. The output intervals partition (0,infinity); there is no output
overlap or missing interval.

On each such interval dt/t<=dt/d. For k<4d,

    (pi^2/(4d)) |g_k|^2 <= pi^2 |g_k|^2/k.

Use the full-line Gram integral to bound the interval integral and then
sum the nonnegative quantities over j. This yields the pole contribution
at most 4pi^2 times the input squared norm. The norm bound 2pi<7 is
valid, independent of all finite-support parameters.

At t=m a positive integer, only the k=m pole can survive multiplication
by sin(pi t); its continuous value is (pi/2)(-1)^m g_m. The indicator
jump is multiplied by a vanishing sine and contributes no jump. Other
summands tend to zero. Dyadic boundaries can be assigned half-open as
written and do not affect L2 estimates.

### Nonsingular comparable scales

The near-set inequality k>d/2>t/4 gives

    |D_k(t)| <= 1/[2(t+k)] + 1/k <= 9/(2t).

If this set is nonempty then d>1/4, hence dyadic d>=1/2. Consequently

    sum_(k in J_j) k <= 8d^2+2d <= 12d^2.

Weighted Cauchy-Schwarz therefore gives the stated factor
12d^2 * 81/(4t^2) <=243. Integration against dt/t contributes log2,
and the same membership bound gives 972log2 times the input squared
norm. This is below 32^2. Empty near sets for every j<=-2 are explicitly
covered, so local comparability is never used where k could approach
zero with t.

### Separated scales and both ends of the half-line

Outside J_j, k<=d/2<=t/2 or k>=4d>2t. With the input measure 1/k the
kernel is K=kB, rather than B. Below t, K=k^2/(t^2-k^2); above t,
K=t^2/(t^2-k^2). This proves the two bounds with factor4/3.
The actual complement can be dominated by those two separated ranges.

For the lower range let m=floor(t/2). If it is nonempty, t>=2, and

    (4/(3t^2)) sum_(k<=t/2) k
      <= 1/6+1/(3t) <=1/3.

For the upper range and t>=1/2 set n=ceil(2t). Monotone integral
comparison gives sum_(k>=n) k^-3 <=n^-3+1/(2n^2), whence its weighted
row sum is at most 1/(6t)+1/6<=1/2. If t<1/2, all positive integers
are eligible, and sum k^-3<=1+integral_1^infinity x^-3 dx=3/2 gives
row sum <=2t^2<1/2. Thus the full weighted row sum is <=5/6<1.

For fixed k the actual output support of the separated kernel lies
inside (0,k/2] union [2k,infinity). The two integrals with measure dt/t
each equal1/8 before multiplication by4/3. Their sum is therefore1/3.
These estimates remain uniform over all dyadic boundaries. Applying
the written discrete-to-continuous Cauchy-Schwarz argument gives squared
operator norm <=(5/6)(1/3)<1; the claimed norm<=1 is conservative.
Multiplication by the sine can only decrease this part's norm.

There is no finite-support exchange issue: sums over input are finite,
and sums over output blocks or integrals of nonnegative majorants are
justified directly by monotone convergence. For additional endpoint
clarity, fixed finite input has Eg(t)=O_g(t^3) as t tends to zero and
Eg(t)=O_g(t^-2) as t tends to infinity. These asymptotics are not used
for the uniform norm constant.

### Constant and conclusion

The three global operators are defined blockwise on the same disjoint
output partition and sum to E almost everywhere. Their norms are bounded
by2pi, sqrt(972log2), and1 respectively. In particular they are below
7,32,1, so the triangle inequality gives the stated 40 bound and hence
1600 for the squared inequality. The pole is always handled with its
signs intact; no absolute harmonic-pole sum or absolute-cardinal
L1-column bound is used. The known absolute-majorant obstruction is
therefore not reintroduced.

## Verification activity and limitations

Executed file reads/searches and SHA256 hashing only; no numerical
mathematical experiment or heavy process was run, and no numerical
output is evidence for this verdict. The developer independently
confirmed the frozen SHA256 by message before this record was written.
This proof's finite-input theorem can be used as a supporting estimate;
any extension or finite-CC identification must preserve its measures
and factors and be checked separately.
