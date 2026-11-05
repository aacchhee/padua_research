# Supplementary independent mathematical checks

Date: 2026-11-05. Checker: distinct Codex subagent `independent_math`,
allocated **gpt-6-astra high** by handoff 01 and the orchestrator. This is
an additional independent check of Codex development, **not the required
Claude audit and not PR readiness approval**. Only the orchestrator owns
Git and shared records; this checker performed no Git operation.

Final supplementary verdict: no unresolved mathematical finding in the
reviewed F1/F2 countersequences, exact F3 half-degree classification,
positive reference theorem, or F4 uniform norm bound. The signed spectral
assertions are refuted along even degrees; required Claude audit remains
pending. Full proof hashes, independent derivations and executed checks
appear below.

Rules read: `AGENTS.md`, `agents/WORKFLOW.md`, `agents/codex/CODEX.md` at
orchestrator-supplied input/rules SHA
`83cf6f1ee244f2e72057332a7ec04ee74db1f0de`. Also read handoff 01 and plan.
Review binds to the file hashes below; no claim that working files had
already been committed is made.

## Initial scope and disposition

The first review boundary below preceded the signed carrier results.
The final scope and signed-target verdict are in the addendum below.

| Record | Reviewed SHA-256 | Supplementary outcome |
|---|---|---|
| `theory/f4-uniform-density-bound.md` | `cee004269514e238499885ae32154deb0f6616e56d2e52806d37b282df8621b2` | No mathematical gap found; complete analytic uniform bound reconstructed, including all integer m>=2 and 0<=n<m |
| `theory/f3-smooth-diamond-reference.md` | `a55b401d450fe3e0510eb605051fd7ea99ee59743a1a3fc46ee14de992773aaa` | No gap in the positive reference equivalence; signed PD-T116 was OPEN at this first boundary and is refuted in the final addendum |
| `code/g1_spectral.py` | `f246b7a436fa9e6133153a87fd5af887d80f6fb0ab12dc2208fbd9ade223c241` | Limited distinct numerical validation of DCT weights against direct moment solves; not an audit of large-degree runs, fits, localization, or certification |

One minor notation collision was reported: `c_0` denoted both the
Chebyshev coefficient convention and the raw sampling constant. The
F4 developer renamed the latter to `kappa`; the hash above includes
that correction. No mathematical finding remains unresolved within
this review scope.

## Mechanism and predecessor coverage

Read the **entire 889-line `state/IDEAS.md`**, including all obstruction
and disposition tables; repeated smaller reads recovered truncated tool
output. Read the full relevant canonical candidate records
`topics/padua-mz-2d-20261101/ideas-d2.md`, `ideas-d4.md`, `ideas-d5.md`,
and the M3 `IDEAS.md`, together with the current `ideas-f4.md` and
`attempts/F3.md`, `attempts/F4.md`. The key comparisons are IDEA-073–076,
212–214, 219–226, and the explicit scope of PD-N044–053. Screened local
literature-index rows for Padua/MZ/hyperinterpolation; no primary source
was contacted and **no historical novelty or exhaustive prior-art
clearance is claimed**.

Proof inputs read directly: frozen 2-D definitions; PD-T101's cardinal
normalization proof; PD-T111's complete finite triangular-sum proof;
PD-T112's exact operator norm proof; PD-T114's unchanged target and
failed-majorant discussion; PD-T017 and PD-T022 proofs. F3 repeats the
checkerboard and filter argument needed from PD-T115, so its changed
kernel was reconstructed directly rather than inherited by analogy.

F4's separation is real at the proof-step level: the density remainder
is tested against one power of |p|, and the estimate never requires a
uniform absolute-Gram bound. This respects PD-N052. F3 is a smoothing
variant of IDEA-226 that proves a positive reference bound using a
quartic envelope; it does not claim a signed comparison or eta<1.
These local mechanism distinctions are not historical priority claims.

## Independent analytic reconstruction: F4

1. Integrating the corrected cardinal kernel gives
   `w=rho*d_m`, where the exceptional term is **-2h_m T_m(x)**.
   The factor two is the integral of the constant in the y coordinate.
   The positive rho has mass one, whereas signed w has mass four.
2. In the cosine density expansion, `t_0=2` and
   `t_r=-4/(4r^2-1)` for r>=1. Its absolute coefficient sum is four.
   The finite signed triangle is `A_R`; changing signs changes exactly
   the two nonzero coordinate axes. Thus its omitted absolute tail is
   `16/(2R+1)-A_R`, not merely the product of one-dimensional tails.
   The proof's harmonic bound gives `A_R>=-4/(2R+1)` for R>=1.
   With R=floor(m/2), this yields tail<=20/m. The exceptional term
   contributes at most 8/(3m), including m=2. Hence 68/(3m) is valid.
3. The angular endpoint intervals each have length 1/m. Their total
   contribution to normalized Chebyshev L2 is <=m/pi times Lebesgue
   L2, using the Legendre evaluation bound m^2/2. The middle interval
   contributes <=m/2. Applying the one-dimensional estimate twice and
   taking square roots gives exactly `kappa*m`, not m^2, in raw L1.
   Discrete Chebyshev exactness applies because p^2 has total degree
   <=2m-2; an alternating checkerboard contribution would need degree
   at least m+(m+1). The exceptional top x mode is absent.
4. The CC floor constant is `a=pi-4/3`, from the displayed PD-T017
   truncation error, with both N=m and N=m+1 at least two. Positivity
   permits enlargement to the full tensor grid. Applying the coordinate
   CC upper bound twice gives the main Gram bound 8pi^2/a^2.
5. The positive main density has total mass <=4, not the weaker factor
   eight obtained by discarding checkerboard structure. One of m,m+1
   is odd, so its alternating sine sum vanishes by reflection. The two
   unalternated sums are cotangents, yielding the displayed exact mass.
6. The exact PD-T112 weighted-L1 identity then gives
   `C*=4sqrt(2)pi/(pi-4/3)+(68/3)(1/2+1/pi)`.
   The rational inequality `C*<1336/45<30` is valid; its floating value
   is approximately 28.3763348311. Constants are reproduced, so the
   lower bound two holds also for n=0. No F1/F2 result is used.

This is a complete analytic resolution of the stated uniformity target
within the checked dependency chain. It does not provide a sharp norm,
Gram positivity, upper Gram threshold two, endpoint higher reproduction,
or fixed-function convergence.

## Independent analytic reconstruction: F3

The nonnegative Fourier coefficients of F_L^2 have total L^2 and support
[-2L+2,2L-2]. Convolution with D_(n+2L-2), divided by L^2, gives plateau
one on [-n,n] and cutoff n+4L-4<=m-1, including L=1. The scalar decay
bound uses 2M+1<=2m and L>=epsilon*m/4, producing exactly
A=512(1+pi)^4. Parity projection converts the scalar frequency square
to an integer diamond. The minimum nonzero checkerboard alias length
is 2m, exceeding n+m-1, so both reconstruction identities hold.

For either diagonal lift branch, original circle distances are bounded
by d_u+d_v. The two regularized sine factors each have relative ratio
at most 1+m(d_u+d_v); after the square root of their product this costs
one such factor, bounded by (1+md_u)(1+md_v). This leaves cubic decay
in both diagonal distances. Reversing source and target obeys the same
estimate, as required for both Schur orientations.

The torus homomorphism has degree two, preserves normalized Haar measure,
and has exactly two lifts of each checkerboard point. The square-packing
argument is valid: coordinate differences of points in a half-open square
of side a=pi/[2(m+1)] are strictly less than a, so original differences
are strictly less than 2a, hence smaller than either grid spacing. The
four-square shell count, series integral 2/pi, division by 2N_m, and
continuous factor 1/(4pi^2m^2) agree. They imply the claimed conservative
Schur constant M_epsilon=A^2 B^2 epsilon^-8.

Finally the regularized angular norm differs from physical dxdy by at
most C_2^2 with C_2=2+pi/2, using degree at most m-1 separately in each
coordinate. The pi^2 conversion is correct for normalized full-torus
measure and even cosine polynomials. Squaring M_epsilon gives the
claimed C(epsilon). Edge case m=1,n=0 is covered by the same proof.

## Executed independent checks

These are separate executions written by this checker. Numerical
agreement is **MEASURED**; the rational checks are finite regressions.
Neither is a premise of the all-integer analytic proofs above.

Commands, from the repository root:

```sh
OPENBLAS_NUM_THREADS=1 python topics/padua-mz-2d-frontier-20261105/code/independent_f4_check.py topics/padua-mz-2d-frontier-20261105/evidence/independent-f4-check.json
python topics/padua-mz-2d-frontier-20261105/code/independent_f3_check.py topics/padua-mz-2d-frontier-20261105/evidence/independent-f3-check.json
```

The actual invocation used the equivalent absolute paths, recorded in
receipts. Both scripts use deterministic inputs and no random seed.
Receipts record complete source hashes, Python/platform and applicable
NumPy/SciPy versions. Both receipts are small and reproducible from
committed checker code; no bulk external artifact is needed.

- **F4 PASS**, elapsed about 0.71 s: exact Python Fraction triangular
  identity, sign bookkeeping and bound for R=1..100. At
  m={2,3,4,5,6,9,10,15,20}, independently solved the full Vandermonde
  moment equations and compared with the density formula and G1 DCT.
  Maximum discrepancies were 8.89e-16 and 8.96e-16, respectively.
  Discrete Chebyshev Gram maximum error was 2.45e-15. Main mass,
  density error and raw/main Gram bounds all passed at these degrees.
  All sign vertices modulo global sign were enumerated at m=2,3,4
  (32,512,16384 vertices), giving float operator norms approximately
  2.0000000000, 2.4355900241, 2.3392876409. These are **not certified
  enclosures** or asymptotic observations.
- **F3 PASS**, elapsed about 3.00 s: exact Fraction plateau and diamond
  checks for m=1..24 and all n<m (300 degree pairs, 379900 frequency
  tests); 205311 supported input/output alias tests for m=1..10;
  exact lift cardinality for m=1..24 and 92064 pairwise circular lift
  separation checks for m=1..8. No float arithmetic is used here.

## Coverage limits and remaining audit

The full native GMP/FLINT certificate port, high-degree spectral runs,
scaling selection and localization results are **not independently
certified by this report**. The G1 comparison here tests DCT weight
construction only. F1/F2 theory files were not yet available at the
initial review boundary. The decisive signed results were subsequently
reviewed in full as recorded below. The required
cross-model Claude audit must inspect the final candidate SHA and any
subsequent material changes. Literature overlap remains qualified.

## Final addendum: signed logarithmic countersequences

Later on 2026-11-05 the orchestrator extended this same supplementary
review to the consequential F1/F2 carrier proofs and F3 classification.
The checker remained at the handoff's **gpt-6-astra high** allocation;
this does not constitute the required Claude xhigh mathematical audit.

**Verdict: no mathematical gap found in the complete proofs below.**
The earlier OPEN description of signed F3 is historical and superseded:
these analytic arguments refute the all-m upper threshold and positivity,
refute the proposed positive endpoint orders and eta->1, and refute
uniform strong signed MZ at every fixed theta>1/2. Divergence is proved
along even m; no effective onset or first finite crossing is supplied.
The F4 uniform C-to-L2 bound is compatible with these L2 Rayleigh results.

| Fully reviewed file under `theory/` | SHA-256 |
|---|---|
| `f12-local-weight-asymptotic.md` | `ec60d98c4bbaefe5daf3281efb5a32fe742687ee4ac8fc7a789f2d0a66867b8d` |
| `f12-eventual-negative-carrier.md` | `0ef7c078dc8a71bac882e6d61669211b89e1295b33be7f51f0488073b5bae09d` |
| `f12-eventual-upper-carrier.md` | `b57334029a4676c5ddea0827e9c34e5c07cc931fdc2dbe8457340380439cd3fb` |
| `f3-fixed-ratio-threshold.md` | `3dbde58f88a2c96c7239b701a03d812006ad2aac06f79b6bb539255bc0e6dbc4` |

Read the common lemma and both packet files in full, independently
reconstructed their coefficient and limit calculations, and read the
complete F3 corollary. Current candidate memory `ideas-f12.md` was also
read; the relevant inherited registry/obstruction coverage is above.
The parity carrier and complete signed sum escape the precise
hypotheses of PD-N047/048: neither a product of two critical CC packets
nor subtraction of a divergent unsigned corner estimate is used.
No historical novelty or priority claim is accepted by this review.

### Common lemma: the load-bearing limit and majorant

For m=2R the integrated cardinal formula gives the signed density as
`S_R-2h_m cos(m theta_j)`. Independently expanded the finite triangle as

`S_R=f(t)f(s)-f(t)T_R(s)-f(s)T_R(t)+T_R(t)T_R(s)-V_R(t,s)`.

The zero-index axes are absent from V_R. The global estimate splits its
indices into a<=R/2, b<=R/2, and both>R/2. The first two regions each
have bound `64 H_floor(R/2)/(9R²)`; the third has bound `256/(9R²)`.
The stated constants in the subsequent weight inequality, including
`260+16/3` for the constant term, are valid, and C=4096 suffices.

For fixed j,k and fixed 0<delta<1/2, a<=delta R has exactly a choices
of b near R. Its uniform expansion is
`R² t_b cos(2b phi_k)=-(-1)^k+O_k(delta)+o_R(1)`.
Multiplication by t_a and summation uses
`sum_(a<=delta R) a t_a=-log R+O_delta(1)`.
The accumulated uniform errors are O(delta log R), which vanish after
normalization and the subsequent delta->0 limit. The swapped strip
gives (-1)^j. The remaining middle has absolute size
`O_delta(R^-2)`, hence vanishes after R²/log R normalization. Thus the
limit coefficient is the sum of these two endpoint phases. The order
of limits R->infinity first, delta->0 second is essential and explicit.

All remaining product/tail terms and the exceptional cardinal correction
are O_(j,k)(m^-2), without a logarithm. Checkerboard parity and the
prefactor therefore give precisely
`m^4 w_(j,k)/log m -> -16 e_j e_k (-1)^j`.
The moving endpoint halfweights are correctly distinguished from e_j.

### Packet consequences and their normalization

The degree-r convention is explicit: F_r has amplitude r+1 and degree r.
The elementary bound `F_r/m<=C_a(1+j)^-2` holds on the **entire** x grid,
with the adjacent y denominator changing only the constant. After
multiplication by the global weight bound, every normalized energy
summand is dominated by a constant times
`(1+j)^-3(1+k)^-3`. Zero extension to the integer quadrant and dominated
convergence therefore apply; no merely local asymptotic is summed
without control of the far nodes.

For the negative carrier, cos²(j*pi/2) selects even j. The exact DCT
constant of F_r² is `D_r=1+r(2r+1)/(3(r+1))`. Degree 2r<m makes its
alternating trapezoid sum zero, so the selected x profile has limiting
halfweighted mass a/3. The y profile has mass 2b/3 and zero alternating
mass, leaving b/3 on even k. The signed logarithmic energy coefficient
is consequently **-16ab/9**.

For the positive carrier, the difference of two Chebyshev polynomials
is exactly `sin(mt/2)sin(rt)`, a polynomial despite the individual sine
notation. It selects odd j. The auxiliary polynomial
`h_r=sin²(rt)F_r²` has degree 4r<m; its constant coefficient is
`D_r/2-1/[2(r+1)²]`. The correction follows from the top Chebyshev
coefficient `2/(r+1)²` of F_r² and the product-to-sum factor one half.
Its ordinary mass, followed by odd-j selection, tends to a/6. The y
odd mass is b/3. The coefficient is therefore **+8ab/9**.

Both carriers are bounded in modulus by one on the continuous domain.
Splitting the Fejer integral at 1/(r+1) proves
`0<||p||²<=[(1+pi^4)/2]²`. Total degrees are respectively
m/2+r+s and m/2+2r+s, so the stated strict parameter conditions ensure
membership in Pi_(m-1) eventually. Dividing a negative numerator by this
norm upper bound gives an **upper** bound on its Rayleigh quotient;
dividing a positive numerator gives a **lower** bound. Thus the two
spectral endpoints diverge to opposite infinities along even m.

The F3 choice a=b=(theta-1/2)/4 is admissible and gives the exact
negative energy limit `-(theta-1/2)²/9`. Its degree is below theta*m,
hence at most floor(theta*m). This proves failure for every fixed ratio
above one half. Its subsequently added upper specialization was also
checked: 2a+b=3(theta-1/2)/4<1/2, degree<theta*m, and logarithmic
energy coefficient +(theta-1/2)^2/18. Both spectral endpoints therefore
diverge at each such fixed ratio along even m. At or below one half,
exactness proves eta=0. The positive reference theorem does not conflict
with this classification.

### Separate executed check and limits

Ran the following independent command (equivalent absolute paths are
in its receipt):

```sh
OPENBLAS_NUM_THREADS=1 python topics/padua-mz-2d-frontier-20261105/code/independent_carrier_check.py topics/padua-mz-2d-frontier-20261105/evidence/independent-carrier-check.json
```

**PASS**, about 9.28 s. Exact Fraction Fourier arithmetic checked both
carrier ordinary/alternating DCT identities, the top coefficient and
the h_r correction for every even m=8..64 and integer 1<=r with 4r<m
(239 cases). Distinct direct triangular-sum float probes checked seven
fixed node indices at m=128,256,...,8192. The final doubling slopes of
m^4 w were approximately -4.016, -8.002, +16.112, -8.002, -15.757,
+16.224, -7.979, against predicted coefficients -4,-8,+16,-8,-16,+16,-8.
Those slope probes are **MEASURED only**, not a convergence proof or
finite signed spectral counterexample. Source hashes and environment
are recorded in the small receipt; the analytic verdict uses the proofs.

The independent checker did not certify a finite violating spectrum,
sharp logarithmic extremal constants, the odd-m branch, or the 1-D
upper-gap target. A minor candidate-memory mismatch in the harmonic mass bound was
reported to the developer for synchronization; it does not concern the
carrier proofs. Required Claude review remains pending on the final
published candidate and its full dependency chain.

Finally inspected both warmup files in full, with no mathematical gap
found: `f12-1d-sign-discard-obstruction.md` at SHA-256
`79763179157fc5db651ea30b7ab9c299dc4356aeeb622ef38db261cadbc60bf3`,
and `f12-harmonic-boundary-escape.md` at
`665c853d0575160d57e3f7adbbb46a8f3ec1daa79c4385d907d8f92047529249`.
The first comparison uses ||q_L||^2=O(log N) and
||p_L||^2>=L/16, with the constant in its displayed ratio correct.
The second uses |p_N(cos t)|<=pi*N, endpoint mass<=pi^2*K^2,
and the inherited norm lower bound log^3(N)/512. Read the complete
PD-T018 and PD-T021 dependency proofs; the marginal and y-edge factor
1-cos(K/m) are correct. These are analytic inspections, with no separate
program run or statement about actual extremal eigenvector localization.

The positive-reference F3 file subsequently received review/status
metadata updates, with the signed target now cross-referenced as refuted;
its current full-file hash is
`dfbc44a3ec0589f794457fe14c3212b730d62a26c66bffa3e1d4a7295e62550d`.
The executed F3 receipt correctly retains its earlier input hash. No
mathematical change to that positive-reference estimate was reported;
the new signed classification was reviewed separately above.
