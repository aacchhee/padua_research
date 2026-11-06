# C02 row partial sums — independent mathematical reconstruction

2026-11-06. Rules/input `b6e67b3c78cb668b6d2f9da5a5560537d2960bf3`;
the frozen developer proof records its original rules head4b728b0.
Reviewer: distinct Codex, assigned Astra high; serving model/effort metadata
not independently exposed. No developer file, Git state or old review was
changed. Formal Claude audit remains separate.

**ACCEPTED within the stated analytic and exact-real point scope.**
Reviewed `theory/C02-row-cotangent.md`,17722 bytes, SHA256
`820e655e0df600299767b32712f2290d973c11d83f6d676a32daa3e36d11b4a8`.
No unresolved mathematical finding. This accepts the partial-cotangent
approximation, uniform positive shifted-harmonic bound, exact pointwise
row representation and complete analytic error charge through the stated
finite degree ceiling. It does not approve a production row backend,
whole-box enclosure, gradient, corner-orbit or defect interface.

Read the frozen proof, idea, attempt and developer scalar control; full
N2-row-decomposition, N1-row-model and N5-partial-cotangent dependencies;
and the relevant H8/special-row charges in N1-round6-near-model and
N1-round8-jumps. The existing C01 ratio specification and its bounded
implementation review were reconstructed in this reviewer's earlier
reports. This is a standard-mathematics/backend-variant check, with no
historical novelty or priority judgment. The full registry/literature
novelty audit is outside the declared scope.

## Smooth partial-sum reconstruction

For h=pi/n and consecutive samples strictly inside(0,pi), each centered
cell extends at most h/2<=pi/4 beyond either pole. Thus every cell is
inside[-pi/4,5pi/4]. Deleting the poles0 and pi leaves a smooth residual
w=cot x-1/x+1/(pi-x) there. Its integral primitive W is real because
sin x and x(pi-x) have the same sign on the interval, with positive
removable ratios1/pi at0 and pi. Differentiation gives W'=w and the
stated w' endpoint values. No singular interval subtraction is licensed
by these exact-real continuation statements.

Centering at pi/2 places the remaining poles at plus/minus
pi(ell+1/2), ell>=1. Pairing them gives

    w=-(2/pi)*sum_(ell>=1) z/[(ell+1/2)^2-z²],
    z=x/pi-1/2, |z|<=3/4.

The nearest residual pole is at|z|=3/2, so each geometric expansion has
ratio at most1/4 in z². Absolute convergence permits grouping coefficients
and differentiating four times on this closed domain. For tail j>=J+1,
the integral comparison

    a_j <= (3/2)^(-2j-2)*[1+(3/2)/(2j+1)]
        <= 2*(3/2)^(-2j-2)

is valid because J>=1 implies j>=2. The slightly stronger stated bound
also holds for j>=1. Combining the factors2/pi, pi^-4 from four x
derivatives, the coefficient bound, and (3/4)^(2j-3) gives exactly

    1024/(243*pi^5) * (2j+1)^4 * 4^-j.

Replacing j by J+1+s and using2j+1<=(2J+3)(s+1) leaves the positive
geometric fourth-power sum1520/81. Its additional factor1/4 gives
1024*1520/(243*81*4)=389120/19683, precisely M_J. Polynomial j0 and j1
terms have zero fourth derivative and introduce no endpoint exception.

The tan coefficient recurrence follows coefficient by coefficient from
tan'=1+tan² with t0=1. Locally near z0,

    -tan(pi*z)+(2z/pi)/(1/4-z²)

has coefficient2^(2j+3)/pi-t_j*pi^(2j+1), agreeing with-(2/pi)a_j.
Although the individual tangent series stops converging at|z|=1/2,
the **combined** coefficients belong to the already proved residual
series with radius3/2. The proof does not extend the uncancelled tangent
series. Severe coefficient cancellation is an outward-precision issue,
explicitly retained as an implementation obligation.

For any polynomial of degree d, the difference operator maps a degree
d+1 monomial to a polynomial with leading coefficient d+1. Descending
elimination therefore constructs B with B(t+1)-B(t)=P(h(t+t0)), up to an
irrelevant additive constant. This proves the exact endpoint telescoping
sum for all integer block lengths; there is no degree-q summation or
hidden special-function call. For J96, the maximal degree is193, so
the required discrete antiderivative has degree194, fixed across n.

Independently reconstructing N5's one-cell functional gives

    L_h(f)=(1/h)*integral f -(h/24)[f'(right)-f'(left)]-f(center),
    |L_h(f)| <= 7h^4*sup|f''''|/5760.

Its Peano kernel is nonpositive and has that absolute integral. The
quartic control gives L_1(x^4)=-7/240, confirming the derivative-correction
sign and the factor24 from f''''. Apply this to w-P_J, then telescope
cell integrals and endpoint derivatives. Restoring the exact polynomial
sum and the pole decomposition proves(1)–(2). The error is proportional
to the number of samples q; splitting a channel into blocks does not
multiply this smooth error by the number of blocks.

For the negative pole term, reversal gives

    sum_(i=b)^e 1/(n-i-t)=H(q,n-e-t).

Thus both H arguments in(1) are positive under the strict sample-domain
assumption, and the difference sign is correct. Exact pole samples are
excluded before this formula is used.

## Shifted harmonic remainder

For q>K, set x=y+K and z=y+q, so x>K>0 and z>x. Euler–Maclaurin for
the left-endpoint sum f(x)+...+f(z-1) with f(t)=1/t has endpoint term
(1/x-1/z)/2. Its odd derivatives are negative factorial multiples,
giving the correction signs

    B_(2r)/(2r) * [x^(-2r)-z^(-2r)].

The periodic Bernoulli remainder after Lh corrections uses the derivative
of order2Lh. The Fourier series of B_(2Lh)(t), absolutely convergent
even for Lh1, bounds its supremum by|B_(2Lh)|. Integrating
(2Lh)!/t^(2Lh+1) gives exactly(10). This is a valid bound using the
last included Bernoulli order, not an unsupported next-term assumption.
Since x>K, dropping the positive z term yields the uniform eta in(11).

Small y causes only the explicitly retained prefix to grow. It does not
alter the tail error or the fixed prefix length. For q<=K the direct
branch has at most K terms and zero harmonic truncation error. Each
cotangent block contains two H approximations, hence its error addition
is2eta/h. All logarithms have positive arguments; a numerical log-difference
or log1p implementation still needs outward rounding.

The Fourier coefficient identity gives
|B_(2L)|=2(2L)!*zeta(2L)/(2pi)^(2L). With zeta(2L)<2 and pi>3,
eta at K=2L is less than4(2L-1)!/[6^(2L)*(2L)^(2L)], in turn no larger
than2/[L*36^L]. Keeping the sharper factorial proves the stated
K64/L32 bound. No digamma implementation or degree-growing harmonic
routine is used in this cost model.

## Arc, collision and integer selection

The finite N2 numerator, with the exceptional first-coordinate mode
unchanged, gives regular sign

    sign F = sign[(c-p*sin u)/(cos u-cos v)].

Hence negative regular points lie in D symmetric_difference I, except
numerator zeros. D has at most two boundaries, and the sine superlevel
set I at most two, including coincident/tangent limits. Its full, empty,
minus-one-equality and p0 cases in the specification are correct. When
p=c=0, all regular numerators vanish and must be skipped regardless of
the formal symmetric difference. Exact collisions still use the finite
polynomial; their negative parts cannot be assumed zero.

The fractional relabeling of sigma shifts the circular mesh by an integer
index, including sigma0 at the closed phase vertex. It does not change
the row parity factor. On each open arc, solving
a<2pi(k+sigma)/n<b gives exactly the strict floor/ceil bounds(14).
An endpoint that equals a grid point is correctly excluded. The seam
u0 is treated once and can occur only when the shifted mesh contains it.

For the guarded construction, each of at most four disjoint boundary
enclosures has width strictly less than one grid spacing and therefore
contains at most one grid sample. Adding the seam gives|B|<=5. Four
arcs on the circle produce at most five open components after cutting
at zero; a cotangent-channel wrap splits at most one component. Thus
even the loose12-block allowance is conservative. Boundary-enclosure
endpoints are in the direct set if they contain a grid point, preventing
an excluded negative sample from being lost between an open core and
its boundary enclosure. D-boundary collisions are included in B and
merged with any separately supplied collision coordinates. No direct
sample is included again in either cotangent channel.

On B the exact identity |F|=F+2max(-F,0) gives the added correction in(15),
without deciding a rounded sign or evaluating zero times infinity.
Certified nonnegative samples outside the cores and B need no correction.
The resulting exact pointwise row decomposition is complete.

An actual implementation must preserve circular branches when taking
asin roots, reduce negative angular representatives consistently, and
validate the floor/ceil decisions. No unguarded atan/asin principal-branch
choice or rounded integer conversion is justified. The hypothesis that
distinct boundary enclosures are disjoint and each narrower than a grid
spacing is substantive. The proof does not establish uniformly bounded
refinement work at near-coincident roots or for arbitrary phase boxes;
it correctly allows failure or a separately proved fallback there.

## Row weights, all-row charge and degree ceiling

N2's Q is twice N1's F. The stated coefficients C,D and signed row
T=n[a-(sin beta/2)cot(v/2)] are precisely the halved N2 formulas.
Since S=(nm)^-1 sum|F|, the factor2 multiplying both negative cotangent
channels and direct corrections in(15) is correct. Separate phase
evenness justifies the first-quadrant triangle, without exchanging meshes
or the exceptional mode. On that triangle a is in[0,1].

Rows0 and2m-1 contain the only possible v0/2pi endpoints; rows m-1,m
contain the possible vpi cases at beta=pi/0. The four indices are distinct
for n>=2. Retaining them avoids every singular row coefficient or endpoint
collision branch. Ordinary rows have finite coefficients. The all-row
distance estimate yields

    sum_ordinary(|C|+|D|) <= m*[2+(4a/pi)H_n].

It is valid for this subset because the coefficients' absolute values
are nonnegative and N1-01 bounds the full interior set. The distances
1,...,n occur twice in that bound. No four-special-row H8 estimate is
substituted here: N1-round6/8's separate charge applies to at most four
rows and would not support this use over all ordinary rows.

Each channel has at most n samples and12 blocks. Consequently its total
error is7n*h^4*M_J/5760+24eta/h. Multiplying by2(|C|+|D|), summing the
row bound and dividing by nm gives exactly

    [7pi^4*M_J/(2880n^4)+48eta/pi] * [2+(4a/pi)H_n].

This charges every approximated row once, charges each of the two harmonic
tails in every block, and avoids a spurious block-count factor on the
smooth sample error. The retained rows and bounded direct sets have zero
**row-model** truncation because they retain the exact finite primitive.
Their elementary exact-real evaluation uses the collapsed sine-ratio
identity with its exact removable-pole values, rather than an n-frequency
sum per point. This costs O(n) point operations in total. If C01's
validated approximate evaluator is used in an implementation, its full
enclosure radius—including its own series tail—must be carried as an
additional error budget. “Retained exactly” does not mean silently
discarding a C01 interval radius. No present production claim does so.

For n>=2 the smooth prefactor is below M_J/5 by the decreasing bound
(2+4n/3)/n^4<=7/24. The rational pi>3 majorant gives M96<2^-165.
For n<=2^64, H_n<=1+log n<65; the harmonic multiplier is below2^11,
while eta64,32<2^-256. Thus E_n<2^-167+2^-245<2^-166. These are analytic
tails only; roundoff and root-selection enclosures are additional.

For fixed eta>0, the displayed estimate grows with H_n. It therefore
does not claim fixed uniform absolute accuracy at unbounded n. On any
declared finite ceiling, M_J and the explicit eta bound tend to zero as
the chosen orders increase, giving the stated finite order-selection
argument. Integer bit lengths, pole proximity, cancellation and outward
precision are not hidden in a constant bit-cost claim.

## Independent executed controls and remaining boundary

Executed once:

    python topics/padua-argmax-bridge-20261105/code/cheap_c02_row_review/control.py

Actual exit0: **118 exact assertions PASS**, Python3.12.14, process
CPU0.196677181s, below the60CPU-s allowance. No random seed, external
library, native kernel or production row evaluator was involved.

The controls independently derive the fourth-power generating sum from
Newton differences; compute Bernoulli numbers by Akiyama–Tanigawa; verify
the constants and complete scalar budget; construct/check discrete
antiderivatives through degree193; check four finite Euler–Maclaurin
remainders using exact rational logarithm enclosures; and check75 open-arc
index cases with exact rational grid coincidences and seams. The finite
reference sums are diagnostic code only, not hidden production work.
The symbolic reconstruction above supplies the universal conclusions.

Retained small evidence `evidence/c02-review-row.json`, SHA256
`8c6e782f65429487f540b50c6d36862c2fd2b8202f91f71b9da834eac7c16d55`;
control source SHA256
`97d0d0d211a5542da93abe72e5a2bd0d66a8c7c737d508f64cdac7ab9b1b79f5`.
The developer proof remained at its frozen SHA throughout this check.

No new numerical row backend, certified whole-box branch selector,
phase-gradient or mean-value bound, corner-orbit implementation or defect
certificate has been reviewed or executed. Those interfaces remain OPEN,
as do any useful practical performance conclusion and PD-T099. In
particular a uniform value error does not justify differentiating a
moving integer block without its boundary terms. This accepted supporting
point lemma does not authorize a full cover or certify another degree.
