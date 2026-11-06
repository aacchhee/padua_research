# Supplementary mathematical audit: S2 qualitative upper limit

Date: 2026-11-06. Codex supplementary independent checker, requested
`gpt-6-astra high`; actual runtime model/effort metadata is unexposed.
Rules/source corpus: `2143ad622fa98faf8fe7d5cb8ed2bb7e0062f861`.
This is a focused mathematical-validity audit of the newly claimed
qualitative theorem. Full novelty, historical priority and registry
classification are excluded; the required Claude audit remains separate.
No new mechanism is proposed here, and no full IDEAS/literature audit
is claimed under this proof-only assignment.

## Verdict and reviewed inputs

**PASS for the stated qualitative theorem.** No unresolved BLOCKING,
MAJOR or MINOR mathematical finding was identified after reconstructing
the complete argument, including the core density and arbitrary-vector
upper-limit direction. Earlier fixed-J approval alone was not treated
as approval of this new theorem. No numerical experiment was used or
claimed for this analytic audit.

Read all255 lines of [S2-qualitative-limit.md](theory/S2-qualitative-limit.md).
Its frozen SHA-256, verified again at completion, is
`978dfa4332eb8146f69da3b9d83a84188627fd72ec91c5fa50a19ee89e0d5943`.
The previously reconstructed dependencies remained at the same hashes:

- [Fixed-J theorem](theory/S2-fixed-trial-limit.md):
  `e11070a2876f3ea87857f00ab471a55713ccdfba13aa5af77e11ef38a6db91c1`.
- [Uniform upper bound](theory/S2-uniform-upper.md):
  `3a45f40aad550a50da4871ab2d3554adb60b41513b08b2427e10b203408b9e6b`.

PD-T013 and PD-T015 were read/reconstructed in this session's earlier
checks. Their exact coefficient convention, parity blocks, positive
weights and mass floor were used explicitly below. The exact endpoint
model and its finite-core identification were also read in full in the
[model check](independent-checks-S2-model.md).

The approved statement is

    lambda_max(G_(N,N−1)) → Lambda_edge,
    1 <= Lambda_edge <=3/2,

through all integers N and therefore through both parities, with
Lambda_edge the exact registered variational norm. This is not a
certified decimal value or an effective convergence-rate theorem.

## 1. Density in the actual endpoint-energy domain

For real g in the stated domain, let G be its even zero extension.
With the unnormalized Fourier transform, hat(G)=2F_g on the real
axis. Consequently

    integral_R |t||hat(G)(t)|²dt =8M(g).

For G_r(s)=G(s/r), the Fourier transform is r hat(G)(rt). This is
indeed an isometry in L²(|t|dt): changing variable u=rt cancels the
two powers of r from the amplitude against the weight and measure.
Strong continuity follows by first checking continuous compactly
supported annular functions and then using their density in that
weighted L² space. Ordinary spatial L² dilation is strongly continuous
as well. Thus inward dilation preserves the relevant energy and
approximates the original function without assuming an endpoint trace.

After fixing r<1, an even nonnegative smooth unit-mass mollifier with
sufficiently small support keeps the convolution inside(−1,1). Its
Fourier multiplier has modulus at most1 and tends pointwise to1.
Dominated convergence in the weighted Fourier norm and the ordinary
L² approximate-identity property give simultaneous approximation.
The resulting function is even, smooth and zero near±1.

Its cosine coefficients decrease faster than every power: all odd
derivatives vanish at0 by evenness and at1 by compact support, so
repeated integrations by parts have no endpoint contribution. The
value at1 expresses the constant coefficient as minus the absolutely
convergent alternating sum of the remaining coefficients. Partial
sums in the registered core therefore converge in C² and vanish
exactly at1. For their difference h, two integrations by parts give
the stated t^−2 bound because h(1)=0; the bound near0 is ||h||_1.
Hence

    M(h) <= (||h||_1²+
              (|h'(1)|+|h'(0)|+||h''||_1)²)/2 →0.

This proves the required density in L² and M, including the critical
endpoint-energy cases. It does not rely on assuming that every domain
element has an ordinary zero boundary trace.

## 2. Continuum identity and its extension

For a finite core vector, multiplying the exact constrained cardinal
trial by N produces Chebyshev coefficients g(i/N) for1<=i<N and
g(0)/2 at i=0. This follows from the interior2/N DCT coefficient
formula, with the additional constant-mode halfweight; the top mode
cancels. The fixed-J theorem therefore gives continuous mass M(g)
and discrete mass D(g), with precisely the registered samples and
weights. No second endpoint is inserted in this finite-core limit.

The coefficient forms K_N and H_N only couple equal parity indices.
For a smoothly sampled single profile this contributes one half of
the full double integral. For H, the integral kernel is
(2−s−r)^−2: integrating y exp(−(2−s−r)y) gives this value.
The finite core has g(1)=g'(1)=0, so |g(s)|<=C(1−s)². This makes
the product-weighted singular kernel absolutely integrable and
justifies Fubini and the corner Riemann limit.

More explicitly, for u,v>=1/N, the discrete denominator is at least
(3/4)(u+v)². The resulting product bound is proportional to
u²v²/(u+v)² and tends uniformly to zero when u,v approach0.
Removing the corner and then shrinking it justifies the claimed
limit without uncontrolled singular entrywise convergence. The
exceptional coefficient at i=0 changes the form by O(1/N), since
that row's rescaled kernel is bounded. Thus the exact finite identity
passes to

    D(g)=M(g)+(K(g)−H(g))/2

on the core, with both factors1/2 checked independently.

The finite coefficient floor gives M(g)>=||g||²_2 on this core.
Since |k|<=1 and the interval has length1,
|K(g)|<=||g||_1²<=||g||²_2<=M(g). Positive D then gives
H(g)<=2M(g)+K(g)<=3M(g). These are upper estimates on positive
quadratic forms and therefore also control differences of core
vectors. They make the Laplace transform a bounded map into
L²(y dy) in the M norm.

The density result now extends the identity to the whole stated
domain. This extension really is the displayed Laplace integral:
L² convergence of g gives pointwise convergence of each Laplace
transform, while the H bound gives convergence in L²(y dy); a
subsequence identifies the two limits almost everywhere. The same
argument applies to D using its weighted sequence-space map and
pointwise convergence of F_g at every sample. No boundary values of
an arbitrary weighted-L² function are presumed; the samples arise
from its underlying L² cosine-transform representation.

The registered norm is the supremum of D/M on this dense core. The
identity and H>=0 give D<=3M/2, hence Lambda_edge<=3/2. They also
give, on every limiting profile in the form domain,

    (K−H)/2 <=(Lambda_edge−1)M.

The earlier fixed-J proof supplies Lambda_edge>=1. These two facts
are exactly what is needed when some continuous mass escapes the
endpoint profiles.

## 3. Arbitrary coefficient profiles and mass splitting

For a^T M_N a=1, the floor gives sum a_i²<=N. The even and odd
cell profiles therefore have total squared L² norm at most2; their
half-sum and half-difference have total squared norm at most1.
Joint weak subsequences exist in the real Hilbert space L²×L².

For a C¹ test v, a full pair cell has length2/N. The half-sum
profile produces the coefficient sum with factor1/N, up to a
quadrature error bounded by C||v'||_infinity/N because
sum|a_i|<=N. The half-difference gives the alternating sum in the
same way. At odd N the final half-cell creates a discrepancy bounded
by C||v||_infinity|a_(N−1)|/N<=C||v||_infinity/sqrt(N).
Thus both asserted test limits hold without a pointwise coefficient
bound stronger than the mass floor.

Taking v(s)=cos(ts) identifies the two endpoint amplitudes of p_N/N
as F_(g^+) and F_(g^-). The right endpoint has exactly the phase
(−1)^i from cos(i(pi−t/N)); no N-parity factor is missing.
The normalized sums have absolute value at most1 by Cauchy–Schwarz.
For fixed T, the exact endpoint mass element is
t sinc(t/N)|p_N/N|²dt. The two endpoint intervals are disjoint for
large N, so dominated convergence on them and positivity of the
remaining mass give the finite-T lower bound. Letting T increase
after N proves

    M(g^+)+M(g^-)<=1.

In particular both weak limits belong to the precise form domain
needed for the continuum inequality. This is lower semicontinuity
of the actual mass under the endpoint observation, not an assumed
norm identity for all of the original mass.

## 4. Compact K limit and positive H lower limit

The rescaled K entries converge uniformly because
max(s+r,2−s−r)>=1. The limiting kernel is continuous on the compact
square, hence its integral operator is compact by finite-rank step
approximations. The slight displacement between even and odd grid
points changes the form by the kernel's modulus of continuity times
(sum|a_i|/N)², which tends to zero. The exceptional last half-cell
has an error O(N^−1/2); its diagonal term is O(N^−1).

If e and o denote the two cell profiles, the discrete same-parity
form corresponds to [K(e)+K(o)]/4. Since
e=g^++g^- and o=g^+−g^-, this becomes
[K(g^+)+K(g^-)]/2. Compactness turns weak profile convergence into
convergence of these quadratic forms, establishing equation(6).

For H, start from its exact positive integral with prefactor1/2 and
substitute x=exp(−y/N). The coefficient sum equals
(N/2)exp(y/N)E_N, so the transformed prefactor is

    (1/2)(1−exp(−2y/N))(N²/4)exp(2y/N)
          exp(−y/N)/N = (N/4)sinh(y/N).

This verifies the finite formula before any limit. At fixed y, the
two E_N limits are the Laplace transforms of g^++g^- and g^+−g^-.
Their squared sum is twice the sum of the two separate profile
squares. Since (N/4)sinh(y/N) tends to y/4, Fatou's lemma gives
exactly [H(g^+)+H(g^-)]/2. Positivity is retained at every stage;
there is no unjustified weak convergence of the unbounded reflected
matrix or cancellation of uncontrolled singular entries.

## 5. Upper limit, escaping profiles and parity

Select any upper subsequential limit L and actual maximizing vectors
normalized by M_N. The established uniform bound makes L finite.
After extracting weak profiles, K converges and H has the checked
lower-limit bound. The exact R_N=M_N−H_N+K_N identity therefore gives

    L−1 <= [(K−H)(g^+)+(K−H)(g^-)]/2
         <=(Lambda_edge−1)[M(g^+)+M(g^-)]
         <=Lambda_edge−1.

The final inequality has the correct direction because Lambda_edge>=1.
If both weak profiles are zero, the compact remainder contributes zero
and positivity of H gives L<=1; escaping mass cannot create a missed
upper eigenvalue above the model. Partial escape is handled by the
same mass inequality. There is no assumption that a maximizing
sequence stays in a fixed endpoint block.

The fixed-J theorem independently gives the reverse lower limit on
each parity. The upper argument used arbitrary integer sequences,
including the odd final-cell estimate, so it applies simultaneously
to both parities. These bounds prove the claimed full qualitative
convergence and the common limit.

## Scope of approval

This is a complete qualitative upper-direction argument, not a
promotion of fixed-entry or fixed-vector convergence into norm
convergence. Its additional ingredients—core density, compactness of
the bounded transition term, positive-form Fatou and endpoint mass
splitting—supply the missing arbitrary-vector control.

It does not supply an explicit epsilon(N), a usable infinite-Galerkin
tail estimate or a certified decimal evaluation of Lambda_edge.
The finite J512 measurement remains separate. No numerical fit or
K3 agreement is a premise of this theorem, and the campaign's stronger
quantitative acceptance criterion remains unfulfilled by this result
alone. Full Claude mathematical/novelty audit remains required.
