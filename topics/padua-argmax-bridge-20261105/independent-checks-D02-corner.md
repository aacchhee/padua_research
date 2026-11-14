# Supplementary independent mathematical review: D02 corner

2026-11-06. Rules/input `084a64f6465956f9c75b5538f83752c30318f151`.
Distinct Codex reviewer, requested `gpt-6-astra high`; serving model/effort
metadata unexposed. AGENTS/WORKFLOW/CODEX were read in this continuing
review session; their diff from the preceding rules head e654917 is empty.
Root owns Git and shared records. This is supplementary acceptance of
the named mathematical claims, not the later formal Claude audit.

## Verdict and finding

**Mathematics ACCEPTED at the three stated scopes.** No BLOCKING or MAJOR
finding. The strip bound holds for every integer n>=1000; the uniform
K_new<7.8 bound and actual-corner loss r2/4 hold for every integer
n>=10000, at both parity-correct nonnode corners. The written arguments
are analytic proofs, not extrapolations of the D01 diagnostic table.

**MINOR D02-C1 — historical OPEN qualifier.** In
[D02-corner-strip](theory/D02-corner-strip.md), the initial `Split from`
line calls the parent uniform corner target OPEN without identifying
that as its preregistration status. The new comparison record now supplies
a developer PROVED claim, accepted mathematically within this review.
Clarify the historical qualifier with a dated addendum preserving the
audited bytes. This requires no proof, hypothesis, threshold or status
change to the strip theorem. Returned to root; the reviewer made no
author-file edits. Root has stated that it will make that record-only
clarification. This report does not claim the addendum already exists.

The global threshold remains500000. No new finite global degree or
all-degree argmax claim is accepted here. D01 remains a failed trial for
its old frozen allocation.

## Audited identities and scope read

The reviewed authored theory files have these SHA256 identities:

| File | SHA256 |
|---|---|
| D02-corner-strip.md |156b3a824bfd060ab17908423dd964f7869866ca1a39ffa97ad322b9bccafe5c|
| D02-corner-sums.md |565673f330832668ac2b85880b3b37b8d4b245e9d9a584cf97cf7c0070f4c018|
| D02-corner-comparison.md |0c5cc2dd59d75272f9f3ff2f798c40054b86929090e3cb3f9dbb4a0aba516d6b|

Read the complete D02 idea, attempt and three theory files. Dependency
coverage includes the complete C02 half-diamond proof, C07 million-onset
and positive-deformation proofs, PD-T159's same-mesh square proof,
PD-T228's reflection-first proof, PD-T270's one-dimensional remainder,
and the relevant C05 derivative/regular/sine sections. C13's comparison
was read to verify the old-domain boundary and existing allocation.
The preceding D01 supplementary review reconstructed its frozen envelope;
that failure was not reopened or reclassified.

For the novelty/obstruction check, read all1112 lines of the current
state/IDEAS.md, including all obstruction/disposition tables; truncated
combined outputs were filled by smaller overlapping reads. Its SHA256 is
`68bf789c82967944421e6fc54f8164dbdb91d1096fa10694008261fbd54f9e9d`.
Searched rectangular/coordinate averaging, symmetric differences,
collision strip, quarter angle and Fourier moments across the registry,
Padua argmax idea/theory directories and literature/INDEX.md. Read full
matched C05/C07 and D01/D02 candidate records, IDEA-331's final and
original gated entries, IDEA-288's registration and linked proof, the
IDEA-457/460/461 entries, and the complete PD-N079/085/086 statements
and proofs. No external theorem or historical novelty claim is used.

The classification as a quantitative variant is sound: C05/C07 already
use coordinate averaging on regular f, while the inspected predecessor
strip proof charges directional rho^2 and then uses rho^2<=2r2. D02
applies the same rectangular identity on B to eliminate that factor2.
PD-N079 concerns the primitive cusp, PD-N085 an individual affine sign
test, and PD-N086 coarse-cell individual sign stability. None supplies
an obstruction to the actual four-copy absolute remainder proved here.
This review's completed reading does not retrospectively enlarge the
developer's separately documented gate coverage.

## Strip lemma: independent reconstruction

The finite U/V factorization is applied on exactly
B={(j,j+1):j>=ceil(n/2)}. With h=n-j, its largest h is floor(n/2),
so the signed rectangle gives |X|<=pi/2+1/(4n),
|T|<=pi/(4m)+1/(4n). Both remain below8/5 at n=1000 and thereafter.
The Fourier frequency set k-1,k-3,...,1-k gives first absolute moment
k^2/2 for even k and(k^2-1)/2 for odd k, and second moment
k(k^2-1)/3. The pure phase derivative factors are at most1/(2n).

The secant estimates and all degree-sensitive V and F bounds were
reconstructed. In particular the positive product-rule polynomial at
tau=1001/1000 is strictly below71/10. After dividing the D derivative
by2 and charging the exceptional -cos(nu) correction, the resulting
bound is |F_ii|<=(71/80)n+1/2<=9n/10 on n>=1000. At h=0 the exact
polynomial gives F0=n, not a limiting rational zero. At h>=1,
the baseline sine ratio and sin T0>=.99T0 give |F0|<n; its upper
T0 bound is already below1/1000 at n=1000.

For E=F-aF0 these bounds yield |E_gamma,gamma|,|E_delta,delta|<=7n/5.
Split the rectangular average into the delta-average of the gamma
symmetric difference and the delta symmetric difference on gamma=0.
Each one-dimensional Taylor remainder has coefficient1/2. Since E0=0,

    |sum_four E|<=4*(1/2)*(7n/5)*(alpha^2+beta^2)
                 =(14/5)n r2.

There is no mixed-derivative term, and no sign continuation is needed.
The factor4 is essential and is present. The strip consists of exactly
floor(n/2) weight-one indices plus(n,m) of weight1/4, for either parity.
Division by nm proves the exact claimed charge. The bound applies on
the closed rectangle, including axes, the origin, repeated copies and
every removable collision. The node-preserving reflection is x for
even n and y for odd n; it does not swap the meshes or correction.

## Uniform reciprocal sums

The three offset ranges are correct. The positive-one range has
t=0,...,n-1; the negative-one range ends at
J=floor((n-1)/2), hence (J+1)/n<=1/2+1/(2n). Offsets k>=3 have the
stated denominator bounds, and the three-term-plus-integral estimates
for Q3,Q4,R3,R4 have the correct integral starting point.

For A1, the centered-cell convexity bound gives the harmonic tail
denominator95/6. Its use for positive and negative one-offset classes
produces hL+h(2c+log2/2), with h=q^-3. For either sign,

    H_+(x)=1/[q(q+x)^3]+1/[q^2(q+x)^2]+1/[q^3(q+x)],
    H_-(x)=1/[q(q-x)^3]+1/[q^2(q-x)^2]+1/[q^3(q-x)].

Thus H_+ decreases and H_- increases. The negative increment is bounded
above by the integral through1/2+1/(2N). With s=t+1, the positive
denominator2t+q<=2s bounds the beneficial decrease below by the right
Riemann sum, hence by I_+-H_+(0)/(2N). It must be subtracted, and the
proof has that sign. Combining the logarithms gives exactly
h[-log(95/6)+(1/2)log(2q^2/(z(q+1)))]. The rational z and Y, logarithm
series directions, coefficient7427/4000 and constant331/50 all check.

The other-offset harmonic estimate uses b>=11/6 and
(1+2n/b)/m<=1/10001+12/11<11/10<exp(1/10); the improved1/20 is valid
uniformly. No old small-j factor(1-120/n)^(-2) is imported.

For A2/A3, the formulas contain33 exact terms t=0,...,32, followed by
the decreasing tail integral starting at32. This is consistent with
the named split at32; no row is lost. For negative one-offset terms,
q-t/n>=q-t/N on those33 rows and q-t/n>1/3 beyond them. Other offsets
use b/(b-1)<=17/11 and p+r=4. The O_pr formula and all four displayed
finite rational upper bounds are valid, giving A2<4.38 and A3<5.11.

For G2 the positive class may first drop its positive k/n shift and
extend to t<=n. Decreasing integral comparison gives the stated
integral plus b^-2/n. Negative k>=3 has(tmax+1)/n<1, so increasing
integral comparison gives its stated difference of reciprocals. Joint
partial sums through k=2M+1 equal

    1/q-1/(q+2M+1),

and therefore tend to1/q. The negative-one integral supplies the
remaining1/z-1/q. Its rounding endpoint and the51/(25n) correction
are retained. Endpoint inverse-square multiplicities give the complete
P/Z sine charge. The H/n factors and positive powers of tau decrease
on n>=10000, so evaluating the displayed bound at N is legitimate.
The same argument applies termwise to the complete harmless remainder.

## Actual-function assembly and lower-domain comparison

The regular geometry is valid down to n=1000: the phase errors are
at most1/(4n), with3tau<pi; S,d>=1; and the enlarged removed strip
leaves g>1/2 in the only delicate negative-one class. The overshoot
estimate |T|-Z<=1/(2n), combined with Z>=5pi/(12m), gives
|T|<7Z/5<3Z/2. These conditions justify the quarter-angle majorant
without reusing a high-degree theorem below its floor.

The exact four-copy normalization gives the regular factor2/(nm n^2).
Its first three terms yield16tau^3 A1/pi^4 and
4tau^3(A2+A3)/pi^2. The remaining four terms produce C_rem. Odd sine
averaging gives1/(2n^2m), hence exactly the specified C_sine. The new
strip charge is strictly below7/5. Initially zero cardinals and the
exceptional endpoint remain included throughout.

With fixed rational f1,f2 at n=10000, the coefficient of L in the
upper bound for K_new is negative. Substitution of the lower bound
L>46/5 is therefore in the correct direction. The rational result is
7.771035546065068...<7.772<7.8; the decimal is only a presentation of
an exact comparison, not a fitted constant.

The corner lower bound uses the n>=2 positive paired-deformation
theorem and PD-T270's all-n remainder. Its A_n is exactly
(2/pi)[log n+kappa], or equivalently
(2/pi)[L+kappa-log(1+1/n)]. In particular no kappa shift is lost.
The positive square at n>=10000, the n/(n+1) prefactor and the endpoint
1/(n+1) are accounted for before discarding positive terms. The ensuing
error E(n) retains both finite terms and decreases on the stated domain.

The elementary kappa>3/2 bounds, kappa<2, log10000>46/5 and
log10000<10 suffice. The cosine loss1-a>=47r2/192 and
L<=log n+1/n give the increasing polynomial with
p(46/5)=5501/16000. After the full E0 and1/(3n) deductions, the lower
coefficient is0.3402545044439202...>1/4 by exact rational comparison.
No division by r2 is used, so equality at the origin and strict descent
at every arbitrarily small positive phase both follow.

## Actual independent scalar execution

Executed from repository root:

    python3 topics/padua-argmax-bridge-20261105/code/post_audit_D02_corner_review/check.py

The [separate review script](code/post_audit_D02_corner_review/check.py)
reconstructs the scalar expressions directly; it does not load or
execute the developer's embedded checker. All44 named strict
comparisons passed in exact Fraction arithmetic, along with exact
identities for the A1 slope, finite telescope and final polynomial.
The script includes additional secant, geometric, sine-chord,
logarithm/kappa and monotonicity endpoint controls. No native board,
new degree, phase sample, numerical quadrature or certificate was run.

Selected explanatory values:

| Quantity | Independent value |
|---|---:|
| A1 constant upper |6.616079161147975|
| A2 unrounded rational budget |4.379379395201811|
| A3 unrounded rational budget |5.102948516890186|
| C_sine upper |1.6940793984033402|
| C_rem upper |0.00030574314466089516|
| K_new upper |7.771035546065068|
| Strict-loss lower |0.3402545044439202|

The [receipt](evidence/d02-review-corner.json) is2997bytes, SHA256
`d2268e413956bc63490889b2be802d9ff5a12d8db26e005fd4307c79d0d1ee07`.
It records the reviewed file identities, checker hash,44 verdicts,
exact final fractions and0.028295 process/children CPU seconds through
checks. Final receipt writing/teardown is outside that timing label.
All scalar comparisons are inspectable proof arithmetic; these checks
supplement, rather than replace, the analytic uniform arguments above.

No mathematical author file, old proof, D01 evidence, registry or Git
state was changed. No further computation is needed for this bounded
supplementary acceptance; the MINOR historical-status clarification
and later formal Claude audit remain separately owned by root.
