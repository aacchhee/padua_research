# Independent supplementary reconstruction — P1 elliptic kernel

Rules/input: `0205690b9c4e959a28e949083e9a1808735abf4b`; response R
publication `17ca9f441cece178354e70504a6c739df501a224`.
Reviewer: distinct Codex supplementary agent, requested `gpt-6-astra` high;
actual serving-model and effort metadata are unexposed. Date: 2026-11-06.
Frozen candidate: theory/P1-elliptic-kernel.md, SHA-256
`d1c965b1df81a4a19ed5f34a50c0955f3532c3f190fc08032790c26e7306fa36`.

**Outcome:** no mathematical gap found in the stated identification of
the accepted product-truncated B with the nonpositive elliptic integral
kernel. The proof supplies boundedness and identifies the exact original
ordering; it does not derive a certified spectral decimal. This is a
supplementary mathematical reconstruction, not the focused Claude audit,
registry readiness. The separate spectral consequences were subsequently
checked in the distinct frozen-file addendum below.

## Scope

Read the entire frozen proof, candidate ideas/P1-kernel.md and
novelty-gate-P1.md; reread S3-03's exact operator definition, tail and
normalization. Earlier audit-01 accepts S3-03 at that exact scope. No
change to that dependency is assumed. This check addresses mathematical
validity of the supplied identification only, with no novelty, priority or
new negative-mechanism assessment. The developer's documented full-registry
gate is attributed to that developer; I do not claim a separate new
complete-registry search in this narrowly scoped reconstruction.

No numerical computation was needed or executed. Classical summation or
special-function formulas were not imported as unverified proof premises.
Only this independent record was written; no developer or auditor file,
Git state, shared registry, protocol or numerical receipt was edited.

## Independent reconstruction

1. **Arcsine normalization.** The density
   w_a(t)=1/(pi sqrt(a^2-t^2)) on |t|<a has mass one. Substitution
   t=a cos(theta), then expansion and the even cosine moments, gives
   its Fourier transform J0(ax) with the stated power-series normalization.
   Independent uniform orientations justify the conditional uniform
   orientation after fixing relative angle. The radius in (3) therefore
   gives the convolution density q=w_a*w_a', not a different normalized
   Bessel product. The minus sign inside the radius is immaterial under
   uniform relative angle.

2. **Period 2 and the zero coefficient.** Periodizing the probability
   density on length 2 gives Fourier coefficients Fq(pi n)/2. Poisson
   convolution uses one half of the unnormalized integral, since P has
   integral 2. At s=0 the resulting cosine series is
   1/2 + sum_(n>=1) rho^n J0(pi n a)J0(pi n a'); at s=1 the nth term
   acquires (-1)^n. Thus e_0=1/2 is correct in both scalar kernels.
   Their positivity follows from convolution of nonnegative functions,
   and does not require falsely asserting positivity term by term.

3. **Scalar limits and elliptic factors.** Since a+a'<2, periodization
   at zero contributes only q(0); at one it contributes q(1)+q(-1)=2q(1).
   The exclusions a=a' and a+a'=1 are null sets. Away from them, q is
   continuous at the evaluation point, so the stated approximate-identity
   proof applies even though q may be singular elsewhere. At zero the
   half-angle substitution gives 2K(k0)/(pi^2(a+a')). At one, put
   sin u=k1 sin v in the retained interval: the density integral becomes
   K(k1)/sqrt(aa'), and its periodized value is
   2K(k1)/(pi^2 sqrt(aa')). The support condition a+a'>1 and
   |a-a'|<1 imply 0<k1<1. Both factors and the cutoff match (1).

4. **No missing concentrated mass in the limit.** Directly integrating
   w_a against a da gives A(t)=sqrt(max(1-t^2,0))/pi. Its convolution
   Z=A*A is continuous, supported on [-2,2], and zero at both endpoints.
   Tonelli identifies the integrated periodized q with the periodized Z.
   Consequently the masses of the positive regularized kernels tend to
   Z(0) and 2Z(1), which are also exactly the masses of the proposed
   limiting kernels. The minimum-function identity proves L1 convergence
   from this equality of masses and a.e. convergence. Pointwise convergence
   alone would not suffice; the proof has supplied the additional step.

5. **Tensor products and triangle restriction.** In the four-variable
   product measure, (a,a') and (b,b') are independent pairs. The L1 norm
   of a separated product is the product of its L1 norms. Telescoping a
   product difference therefore proves L1 convergence of both terms in
   (1). Restricting by the two triangle indicators cannot enlarge that
   norm. Multiplying by bounded f(a',b')g(a,b) is legitimate. This passage
   controls the singular curves and boundary regions without an unproved
   uniform pointwise majorant.

6. **Bounded closed operator.** Direct scalar row integration gives
   (w_a*A)(0) and 2(w_a*A)(1). Since w_a is a probability density and
   ||A||_infinity=1/pi, the row bounds are 1/pi and 2/pi. Symmetry gives
   the corresponding column bounds. The Schur quadratic-form estimate
   applies to these nonnegative measurable kernels; truncation extends
   the integral operators to weighted L2. Their tensor products have
   norm at most 2/pi^2 each. Compression to D and coefficient -8 yield
   ||C||<=32/pi^2. This use of tensor products occurs on the full square
   before compression and does not assume D itself is a product domain.

7. **Exact product-cutoff identification.** A smooth function compactly
   supported inside D extends smoothly by zero and is separated from
   both axes and the slanted boundary. Repeated radial-Laplacian
   integration by parts under a da and b db has no boundary terms and
   gains j^(-2r)k^(-2s), treating zero indices separately. Hence the
   products of test coefficients are absolutely summable over the full
   double index set. The original expanding product cutoff, the full
   sum and the Abel-damped limit consequently give the same bilinear
   form. The identity
   `1[j+k even](-1)^j = ((-1)^j+(-1)^k)/2`
   turns -16 into -8 exactly. For fixed rho the separated series are
   absolutely convergent; the L1 passage just established identifies their
   kernel form with C. Equality on the dense smooth domain, with B and C
   both bounded, proves B=C. No pointwise undamped double-series
   rearrangement, alternative summation order or extra distributional
   term is assumed.

## Clarification and residual limits

I suggested specifying real smooth f,g in §6 because (12) is written
bilinearly without a conjugate. The file already declares real kernels
and permits complexification afterwards, so this is a MINOR clarity point,
not a missing mathematical argument: prove equality on the real dense
domain and complexify. No substantive revision was requested.

The argument identifies the kernel almost everywhere and as a bounded
operator. It neither bounds singular pointwise values uniformly nor
certifies quadrature, practical truncation error, finite-m onset, or
decimal values of c_minus/c_plus. Positive simple ground-state and
irreducibility claims require the separate P1-positive-spectrum proof.

## Subsequent reconstruction — positive spectrum

Independently read and reconstructed the entire frozen
theory/P1-positive-spectrum.md, SHA-256
`4a1e0fe2b3db1e6a8ad19e0a1607d3aace86b9aa3c208d09305aeda49570e64b`.
No mathematical gap found for its stated claims. The only external basic
functional-analytic premise is the explicitly named compact selfadjoint
spectral theorem; accepted S3-03 supplies compactness and c_plus>0, and
the kernel identification reviewed above supplies A=-B>=0 as a kernel
operator. Kernel nonnegativity is not confused with a positive semidefinite
quadratic form.

For nonzero f>=0, choose delta in (0,1) so the positive support of f
with a'>delta has positive measure. For almost every intermediate point
z=(s,t) with s>1-delta, Af(z)>0. For each interior x=(a,b), the intersection
s>max(1-delta,1-a), 0<t<1-s has positive weighted triangle measure and
A(x,z)>0 there. This proves A^2f>0 almost everywhere, although A itself
has a substantial zero set. Boundedness supplies the needed a.e. finite
integrals; singular null curves and boundary sets do not invalidate the
argument. Nonzero A is witnessed by two positive smooth bumps coupled
across a+a'>1.

Compact selfadjointness supplies a real eigenvector at one norm endpoint.
Taking its absolute value makes the positive-kernel Rayleigh inequality
an equality at r=||A||. The stated positive-semidefinite estimate for
rI-A then makes that absolute value an r-eigenvector. Applying the
two-step result makes it strictly positive a.e.

If the r^2 eigenspace of A^2 had dimension greater than one, choose a
nonzero real vector w orthogonal to the positive eigenfunction. Both
w_+ and w_- are nonzero. Two-step positivity gives
<w_+,A^2w_->>0, so replacing w by |w| strictly increases its A^2 Rayleigh
form above r^2||w||^2, contradicting ||A^2||=r^2. This proves simplicity
and also excludes a -r eigenvector of A. Thus c_minus=-||B|| is simple
with an a.e. positive eigenfunction. Since the negative spectral infimum
of compact A is a nonzero eigenvalue and cannot equal -r, accepted
c_plus>0 implies the strict inequality 0<c_plus<||B||.

These consequences do not establish a practical gap size, smoothness or
boundary positivity of the eigenfunction, or a certified decimal. They
remain new analytic development for the focused Claude audit.

## Subsequent reconstruction — finite rectangle reduction

Independently read and reconstructed the entire frozen
theory/P1-rectangle-certificate.md, SHA-256
`4cee5449c0b1634e4d868a41c474b0c938a5394bc87e8f45e197219508a911a9`,
and its child candidate. No mathematical gap found in this analytic
certificate format. No numerical instance, budget feasibility or certified
digit count is inferred, and no code or calculation was run for it.

Direct integration of the source arcsine density against a' da' over
[u,v] gives the square-root difference E_[u,v] divided by pi. Averaging
it against w_a with s=a cos(theta) supplies the second factor 1/pi;
the periodized alternating case has the same factor kappa_1=2 as the
reviewed kernel theorem. This establishes both source-row identities.
The supremum of E is sqrt(v^2-u^2)/pi at |s|=u, which proves the uniform
nonnegative row bound by convolution with a probability density.

For the explicit modulus, the squared arguments differ by at most
2(t+1)(|a-a_tilde|+|theta-theta_tilde|). The positive-part square-root
inequality applied to each of the two terms, then angular integration,
gives exactly 2sqrt(2)/pi for t=0 and 8/pi for t=1, multiplying the
square root of the argument error. The same estimate proves the angular
quadrature error. Direct interval/Darboux evaluation may safely clip the
integrand bounds to [0,sqrt(v^2-u^2)]. These are bounds for integrated
source kernels, not erroneous finite point values on the elliptic
diagonal. Outer integration with the exact a da masses gives the J_t
enclosures in (8).

The tensor factors in (4), (5) and (11) retain the multiplier 8 and
the measure a'b' da' db' exactly. For the upper bound, each cut source
cell C_j is enlarged to its full rectangle R_j; positivity makes that
an upper inequality, so no triangular sliver is dropped. A finite
positive simple h has both a positive minimum and a finite maximum.
The displayed weighted 2pq inequality therefore proves a bound on the
absolute quadratic form of the selfadjoint A, hence its norm, without
assuming that A is positive semidefinite.

For the lower bound, only rectangles contained in D are used in the
numerator; all omitted terms are nonnegative because h and the kernel
are nonnegative. The denominator still includes every actual clipped
cell with its true h_i^2 weight. Integrating a/2 times
[(min(t,1-a))^2-s^2] where a<1-s, with breakpoints 1-t and 1-s, gives
the correct weighted cell mass and a rational value for rational data.
Consequently N_L/d is a legitimate Rayleigh lower bound while max Q_i/h_i
is the upper bound. Boundary cells cannot be treated as full rectangles
in the lower numerator or dropped from the upper computation.

The final statement properly requires a future published finite protocol,
exact inputs, rigorous arithmetic, an actual checked enclosure and an
explicit rounding-bin test. This reduction by itself proves no practical
three-digit enclosure or convergence rate for a chosen grid sequence.
