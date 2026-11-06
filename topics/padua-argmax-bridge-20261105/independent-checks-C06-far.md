# Independent supplementary review — C06 full far profile

2026-11-06. Reviewer: distinct Codex `/root/c06_far_review`, parent-allocated
Astra high; runtime serving identity and effective effort are not independently
exposed. This is a mathematical correctness supplement, not the required Claude
audit. No developer proof, earlier report, shared record or Git state was edited.

## Disposition and exact scope

**Accepted at the two stated scopes; no unresolved mathematical finding.**

1. On the whole closed phase diamond, for every integer n>=10^6,
   S_n <= (4a/pi^2)(log n)^2+b_full log n+200, with the displayed
   coefficient continuous and b_full<8/3. The assembled remainder is <114.
2. On 1/2<=|alpha|+|beta|<=pi, for every integer n>=ceil(exp(256)),
   Lambda_c-S_n >191L^2/15360-22L/15-200>=3592/15.

The practical n>=10^6 far exclusion is **OPEN**. This review does not establish
any near-phase, other-center or actual-corner comparison, nor a global argmax
onset by itself. It does not review the author's subsequent separate finite-part
sharpening files. The original full-phase H4 block is the premise here; no
corrected near-only formula is extended outside its domain and no second near
model correction is introduced.

## Provenance and reading

Rules/input supplied by the coordinator:
`b6e67b3c78cb668b6d2f9da5a5560537d2960bf3`; reconciled main recorded in
handoff06: `f654e32daff27b6846849311092f6daebbbf235b`. Read AGENTS,
WORKFLOW, CODEX, handoff06 and the topic LOG. The managed-environment skill
and current environment status were read; no network operation was needed.

Executed `sha256sum` confirmed the exact frozen submissions:

| File | SHA-256 |
|---|---|
| theory/C06-far-full-profile.md | `13e2af07a7a1e27d5cc5e1b74065e27a27734ea33fffa0f7b457d2deb367b033` |
| theory/C06-far-comparison.md | `1484279404e9a54f2cafcd6f090dba5e922a0aecb1a78860b0639909930baa75` |

Read and reconstructed the relevant complete bodies of N2-01, N1-01/02/03/04/05,
N1-06/07/08 and the scoped round4 budget obstruction. Read the recorded F1
double-collision finding, author response and corrected endpoint-block proof.
For the corner comparison read PD-T271, PD-T269's analytic integral/series
proof and N1-16's scalar k normalization; no near-model coefficient inequality
was imported for far phases.

This review generates no candidate or historical novelty claim and excludes
exhaustiveness/timing of the author's novelty gate. Accordingly the workflow's
no-novelty audit exception applies: the full IDEAS registry was not reread.
The C06 candidate and recorded closest variant IDEA-459 were inspected, including
its full H2/H3 retained record and adjacent leading-only obstruction. The claimed
distinction is an explicit one-sided full-diamond coefficient and constant
remainder, not a new mechanism. The old small-margin error-floor obstruction
does not reject this different, growing-margin far comparison.

## Independent reconstruction

### Finite normalization, collision continuity and row partition

The source keeps G=D-cos(nu), with coefficient one at (n,0), and
F=(-1)^j G/2. Thus S=(nm)^-1 sum |F| and a row contains n terms.
The regular row identity has C=(p-q-2a cot(v/2))/4 and
D=(p+q+2a cot(v/2))/4. Separate finite-polynomial reflections establish
phase evenness; no interchange of the n and n+1 meshes is needed.

Before any approximation, the row triangle bound is exactly the combined
regularized quantity

    [c_e F_n(eta_-)+c_d F_n(eta_+)]/[2 sin(v/2)].

For each fixed row with 0<v<2pi this and the finite row norm are continuous
in the phase triangle, including its boundary. Collision loci and v=pi are
finitely many affine loci with dense generic complement. The inequality therefore
extends to them; it does not assert equality to a separately assigned 0*cot(0).
N1-04's error vanishes at integer offsets, and the continuous identities
|C|=c_e|sin(pi eta_-)|/[2sin(v/2)] and its D counterpart give precisely
5(|C|+|D|)/n^2. This includes simultaneous collisions and central rows of either
degree parity. The v=0 or 2pi rows are treated polynomially in the endpoint block.

With R=2, delta=pi/4 and n>=10^6, all four extracted end rows lie in the
endpoint strips; both central rows lie outside them. The ordinary endpoint
rows are therefore a subset of N1-02's nonspecial rows. Their nonnegative BV
errors sum to at most E_n, and their N1-05 residual errors sum to at most Q.
Collision rows in the strips are already exact in E. The interior complement
uses the one-sided row bound, including its central and collision rows. Hence
no Rhat/r_n cost is needed, and no row is lost or counted twice.

All profile approximations outside the exact end rows use disjoint subsets of
1<=r<=2m-2. Summing the coefficient bound gives exactly
10/n^2+20a H_n/(pi n^2). Extending an upper bound to an omitted subset cannot
increase this total. This establishes the single D_n charge in the final budget.

### Original endpoint dependencies

N1-04's paired-cell expansion handles the odd-n cusp explicitly. Its harmonic
tail is uniform in the offset, and multiplication by the vanishing sine gives
the continuous integer value one with zero endpoint error. The stated Phi_0
boundedness/Lipschitz estimates suffice for N1-05 without inverse phase distance.

The N1-02 cancellation integrand is nonpositive by the scalar triangle
inequality. Its periodic variation includes the pole jumps; centered cells
give half the variation. The endpoint subset used here avoids its two central
exclusions, so its E_n bound applies exactly. N1-03's equal-opposite reference
integral and perturbation split remain valid when a=0. Their joint subtraction
in N1-05 retains A(v)L and yields the integrable residual envelope used in Q.

For N1-06, the centered reciprocal/logarithmic sums give the coefficient
Z_n=D0-B0 log(m/n), so the potentially growing log(m/n)*L terms cancel.
The endpoint floor conventions and constant extension of the final cell give
the stated BV error; both t=0 and t=1 are included. For N1-07 the sinc chart
retains the polynomial values, its signed mesh has n representatives, and the
reference absolute sum is bounded by 4R+9. The w=0 endpoint has the continuous
value one. Thus |C_R|<=1+(2R-1)(4R+9)=52 is a valid uniform bound.

The corrected N1-08 proof includes the earlier F1 case: at the right double
collision alpha=0, beta=pi-z, both c_e and c_d equal sin(z/2), and the two
distinct pole samples each have F=n/2. All other samples vanish, so R=n and
H=1 exactly. The remaining single-channel right collision can cancel by at
most 1/2, as retained in its error. No omitted double-collision assumption is
carried into C06. Adding the unperforated mesh, extracted finite rows and
at most two collision replacements gives precisely the old e4.

### Interior quadrature and the full coefficient

For T=2a cot(z/2), the absolute-sum identity gives

    pi A_L=max(p,q+T),    pi A_R=max(p,|q-T|).

On delta<=z<=pi, T decreases from <5 to zero. Each maximum is a
1-Lipschitz function of T, giving combined variation <10/pi<4 and
sup A<6/pi<2. Their values agree at z=pi. With step h=pi/m the selected
interior cells differ from the integration interval by total length at most h.
Constant endpoint extension and the centered BV bound therefore give
(Var(A)/2+sup A)/m<4/m, also when a mesh point equals delta or 2pi-delta.
This is the source's 4L/m charge. Phi_0 bounded by four and
sin(v/2)>=sin(pi/8)>3/8 bound the constant interior contribution by
64/3<22. No cancellation integral evaluation is needed there; dropping I<=0
is consistent with the direct row triangle bound.

Put x=max(alpha,beta), y=min(alpha,beta). On x+y<=pi,
sin x>=sin y. The sum of the two maxima has thresholds T=p+q and
T=|p-q|, hence the three pieces 2T, T+p+q, and 2sin x at
z=pi-(x+y) and z=pi-(x-y). This remains true whichever coordinate is larger.
The primitive integral of T is 4a log sin(z/2), and the two switch sines
have product a. Subtraction of 8a/z therefore yields

    integral_0^pi(f_L+f_R)
      =[8a log(2/pi)+4a log a+2(alpha sin alpha+beta sin beta)]/pi.

The endpoint kappa logarithms cancel against the interior coefficient,
giving exactly b_full. This is a full-domain calculation, independently of
the near-domain theorem. When a tends to zero, the max remainders are bounded
and -4a/pi<=T-4a/z<=0; thus |f_s|<1 is a common integrable bound.
Dominated convergence validates the closed-boundary extension. On x+y=pi,
U0=sin x and b_full=4sin x/pi, including zero at either vertex. The
separate absolute-phase extension is continuous on the whole closed diamond.

### Constants and far comparison

The centered-cell kernel for log(x)/x gives
|g_R(t)|<=log^2(a_R)/2+(log a_R+2)/(8a_R^2)<2/3 for
3/2<=a_R<=5/2. Together with |h_R|<19/18, |D0|<4 and B0<1/2,
this gives |c_mesh|<26. The displayed K4 is <1630. At n>=10^6,
monotonicity of (1+log n)/n gives e4<1, Q<8, E_n<3, D_n<1 and
4L/m<1. The final sum is exactly

    52+26+1+8+3+1+22+1=114<200.

For b_full, the reciprocal-pair formula has R(t)<=4t^2<=1 on
0<t<=1/2. The source's rational gamma<3/5 and log pi>11/10 bounds
make its remaining sine bracket strictly negative; consequently Phi_0<=1
globally by reflection/periodicity. Therefore U0<=2, a log a<=0 and
x sin x+y sin y<=pi give b_full<=6/pi+8log2/pi^2<8/3.

PD-T271 uses the same corner normalization and the full integer sequence.
N1-16's rational scalar check establishes k>3/2, hence b_c=8k/pi^2>6/5.
Its certified c enclosure implies c>1; no new numerical evaluation is being
assumed or claimed here. This coarse inequality is also consistent with its
analytic dependency PD-T269, whose positive l=1 integral and equation(10)
imply kappa>=8/pi^2, while c1^2>9/pi^2. At L>=256 each of the five explicit
remainder terms is <1/10 and decreasing, so c+R_n>0 and
Lambda_c>(4/pi^2)L^2+(6/5)L.

On the far diamond a<=cos(1/4), so 1-a>=191/6144. Using 4/pi^2>2/5
and the strict b_full bound gives the claimed strict gap polynomial.
Its derivative is positive for L>=256 and its value there is exactly
3592/15. The comparison onset is far inside the validity domains of the
profile and corner expansion. All logarithms are natural.

## Executed controls and limits

An independent inline `python -` command used Python 3.12.14,
`fractions.Fraction` and integer factorials in `/workspace/padua_research`.
It executed eleven exact assertions: the three rational k-normalization
inequalities, the three gamma/log/exp inequalities used for Phi_0<=1,
the rational c_mesh and K4 budgets, the value and derivative sign of the
gap polynomial at 256, and the integer budget sum. All passed, exit0,
process CPU 0.000225516 seconds. No random seed, quadrature, finite-degree
kernel run, phase grid, fitting or floating mathematical premise was used.

These controls check elementary arithmetic in the written reconstruction;
they are not a computer-assisted replacement for its continuum proof. The
analytic assertions above are independently checkable without that execution.
No independent rerun of PD-T271's historical Arb enclosure is claimed or needed
for this scoped analytic application of the already established theorem.

No requested mathematical case remains unreviewed within these two frozen
statements. Formal Claude audit, subsequent material changes, the practical far
onset and any global assembly remain separate obligations.
