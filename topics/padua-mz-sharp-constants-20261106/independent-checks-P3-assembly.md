# Supplementary independent check: P3 primitive and full CC assembly

Date: 2026-11-06. Distinct Codex supplementary mathematical checker.
Requested allocation: `gpt-6-astra high`; serving model/effort metadata is
unexposed. Rules/scientific source:
`0205690b9c4e959a28e949083e9a1808735abf4b`; R publication:
`17ca9f441cece178354e70504a6c739df501a224`.
Source files were supplied as a pinned non-Git corpus by the coordinator.

## Verdict, scope and frozen inputs

**PASS** for both frozen new statements below, including the explicit
finite interpolation bound and the resulting full limit on Pi_(N-1)
and Pi_N. No unresolved mathematical finding remains in this scope.
This is a supplementary independent check, not the required Claude audit
or authorization to change shared registries. No novelty or priority
claim is reviewed or made. The existing PD-T020 registry is unchanged.

| Frozen new record | SHA256 |
|---|---|
| [P3 discrete primitive](theory/P3-discrete-primitive.md) | `bf0a471590f2b8a385a98bad3df9f4d440f009590099401b6a64dc8a894efb44` |
| [P3 reverse bound and sharp limit](theory/P3-reverse-bound.md) | `fdcdd0e67531344b371e4a2de621a2368ff61473566653686b9466fb08738101` |

The signed remainder dependency remains at
`17f357a92a448ef2ad49d406111dcd0d7ce57de8519dc712424ae6f9eb4d29ed`;
its separate all-input reconstruction is in
[independent-checks-P3-remainder.md](independent-checks-P3-remainder.md).
That record's statement that assembly was still pending described its
earlier checkpoint; the present record completes this check's assembly
scope without changing that historical record or its frozen theorem.

The following dependency files were read and their relevant proofs
reconstructed, rather than importing an audit sketch or fitted constant:

| Current dependency record | SHA256 |
|---|---|
| S1-volterra-model.md | `518960c974e4e55cf035364610b4fe318db8b53bcfd7240b2f2e9750aadb98d4` |
| S1-sharp-one-sided.md | `ae7ef4e2b3167fb4c4b98a64de31edba7b7f29c8bd0364b3d8c2cc55ad252ebd` |
| tracks/mz-constants/theory/m1-cc-foundation.md (PD-T013) | `ce2731b5c585714b1e4011850ffd021b120dbec3d50f4fc2eff7eded0ab46d8e` |
| tracks/mz-constants/theory/m2-cardinal-lower.md (PD-T017) | `1c9a3bf5fe8bb9dfbb2943500fb7aafd092eb8a5892c43a2e292f117fabf7776` |

Also read the rules, handoff03, audit01 A1/P3, original PD-T020 wording,
PD-N005 and the earlier S1 supplementary checks. This assignment tests
specified mathematics and dependencies, adding no new mechanism; full
IDEAS/literature novelty review remains outside its declared scope.

## Discrete primitive: reconstruction for arbitrary complex input

The harmonic-cell embedding has cell length1/m, so its exact squared
L2 norm is sum |g_m|^2/m=E. Its primitive at H_m is S_m. On that
cell, Z-F equals g_m(H_m-x), giving exactly |g_m|^2/(3m^3) after
integration. Hence ||Z-F||<=sqrt(E), while rescaling the already
proved Volterra inequality to (0,H_J) gives
||F||<=2H_J sqrt(E)/pi. The triangle inequality therefore yields
sum |S_m|^2/m<=A_J^2 E. No nodal sampling theorem or smoothness of g
is assumed. The complex case follows from absolute squares throughout.

On an ordinary unit cell, sin^2(pi t)-1/2 has integral zero.
Subtracting the constant1/m from1/t in the oscillatory error is valid;
its absolute error is bounded by

    (1/2) integral_m^(m+1) (t-m)/m^2 dt =1/(4m^2).

This proves the cellwise factor1/2 plus its summable error. Also
|S_m|^2<=H_m E, H_m<=sum_(k<=m) k^-1/2<=2sqrt(m), and
sum m^-3/2<=1+integral_1^infinity x^-3/2 dx=3. Thus the aggregate
oscillation error is at most(1/4)*6E=3E/2.

For noninteger T, extending its last partial cell to the entire cell
only increases the integral. For integer T, the same upper sum may
include an extra nonnegative full cell; this is harmless. S=0 on(0,1),
and the finitely many integer points have no effect. The full statement
therefore holds for every T>=1, including T=1, with exactly the stated
constant A_J^2/2+3/2. The asymptotic coefficient follows from
log(J+1)<=H_J<=1+log J and J=floor(T); no averaging assumption about
minimizers or input profiles occurs.

## Actual CC weights, kernel and normalization

The PD-T017 Fourier-tail bounds give interior absolute error2/N^2
for odd N and2/(N^2-1) for even N, both at most3/N^2 for N>=2.
Its sine lower bound gives w_k>=sin(theta_k)/N. Since
sin(theta_k)>=2d_k/N, this gives w_k>=(d_k+1)/N^2 at every
interior node; the exact endpoint formulas give the same bound there.
Thus sum1/w_k<=2N^2 H_(floor(N/2)+1)<=2N^2(L+1). This reciprocal
sum is used only in lower-order estimates, not to determine the sharp
constant.

PD-T013's endpoint symbols equal1/2, whereas the assembly explicitly
uses their reciprocals c_0=c_N=2. The cardinal identity in PD-T017 is

    ell_k(cos theta)=(-1)^(k+1) sin(theta) sin(N theta)
                      /[c_k N(cos theta-cos theta_k)].

Combining it with the stated cotangent identity gives exactly the
homogeneous coefficient2t sin(pi t)/pi in equation(5). This includes
the full interpolation space Pi_N, not merely the constrained subspace.
There is no missing degree-N coefficient in this representation.

For output theta in[0,pi/2] and all input phi in[0,pi], the cotangent
arguments lie in[-pi,3pi/2]. The function e(z)=cot(z/2)-2/z is odd,
removable at0 and nonincreasing for positive z<2pi because
|sin(z/2)|<=z/2. Its largest absolute value on the required interval
is1+4/(3pi)<2. Therefore the two-error sum divided by2 has modulus
at most2. Weighted Cauchy-Schwarz yields exactly equation(6).
Each physical output half has dx mass1; combining the reflected halves
gives cotangent-remainder norm at most4sqrt(L+1) times the full input
CC norm. All constants are uniform at the removable nodal poles.

## One-edge operator and cross-edge terms

For interior inputs on one edge put g_k=k a_k/N. Then
E=sum k|a_k|^2/N^2<=Q. Direct algebra in equation(5) gives

    H(t)=2N sin(pi t) S(t)/(pi t) + 2N(Eg)(t)/(pi t).

The output measure is exactly (pi/N)sin(pi t/N)dt, bounded above
by pi^2 t dt/N^2. Thus each term's squared prefactor converts to
4dt/t; the signed remainder has physical norm at most80sqrt(E).
This covers all positive microscopic t, not just cells away from0.

For opposite-edge input k>=3N/4 and output t<=N/2,

    k^2-t^2>=5N^2/16,
    2t/[pi(k^2-t^2)]<=32t/(5pi N^2)<3t/N^2.

Together with the reciprocal weight sum this gives the displayed
cross-edge pointwise estimate. The physical squared-norm integral is

    18pi^2(L+1)Q/N^4 * integral_0^(N/2) t^3 dt
      = (9pi^2/32)(L+1)Q <3(L+1)Q.

The reflected cross map has disjoint input and output supports, so the
combined norm is at mostsqrt(3(L+1)), safely below2sqrt(L+1).
The self-edge signed remainders likewise combine as a direct sum,
with norm80. Adding them and the global cotangent remainder yields
80+6sqrt(L+1), as stated. No cross term is discarded as orthogonal
unless its output halves are in fact disjoint; the remaining pieces
are combined by the norm triangle inequality.

## Good layers: every factor in the leading constant

L>=16 implies N>4L^3: exp(L)/L^3 is increasing there, and
exp(16)>2^16>4*16^3. Thus K=ceil(L^2)<=M=floor(N/L)<N/4,
including all rounding margins. Good layers are nonempty and disjoint.
For K<=k<=M, z=pi k/N<=pi/L. The elementary sine lower bound and
absolute weight error give

    N^2 w_k/k >= pi^2 - (pi^4/6+3)/L^2
                >= pi^2(1-2/L^2).

The last step follows from pi^2/6+3/pi^2<10/6+1/3=2.
It therefore holds uniformly over every good-layer input, without an
assumption on where its energy concentrates. Reflection gives the same
bound on the right layer, and their E energies add to at most
Q_good/[pi^2(1-epsilon)].

Use the discrete primitive theorem with T=N/2 and J=floor(N/2),
zero-extending each edge's finite g to J. The physical-measure factor4
turns its constant A^2/2+3/2 into2A^2+6. The left and right leading
primitive functions occupy disjoint physical halves, so summing their
squared norms introduces no factor2 beyond that already present.
Consequently their joint norm coefficient is exactly

    C_N = sqrt(2A^2+6)/[pi sqrt(1-epsilon)],
    A=2H_J/pi+1.

Since H_J/L tends to1, C_N/L tends to2sqrt(2)/pi^2. In particular
the oscillatory average1/2, physical Jacobian, endpoint weight scale
pi^2 k/N^2, and Volterra norm2/pi are all accounted for independently.

## Microscopic nodes and endpoints

For interior inputs with k<K, Cauchy-Schwarz gives
|S(t)|^2<=H_K E and S=0 below1. Integrating to N/2 against dt/t
costs at mostL, so the primitive norm is at most2sqrt(L H_K).
The signed and cross errors remain bounded by the preceding one-edge
estimate because K-1<=M. This applies to arbitrary data on the whole
microscopic group, not just a fixed number of nodes.

For the endpoint itself, c_0=2 gives the self-edge term exactly

    a_0 sin(pi t)/(pi t).

After multiplication by the physical mass upper bound, its squared
norm is at most |a_0|^2/N^2 times integral sin^2(pi t)dt/t.
Splitting at1 gives at most pi^2/2+L<=L+5. Since w_0>=1/N^2,
the resulting bound is(L+5)Q(u_0). The right endpoint is identical.
Their cross terms obey the earlier separated-edge bound because c_k>=1;
the e terms obey the same global bound. Combining the two endpoint
self terms uses disjoint output halves. Thus equation(14), followed by
equation(15), is valid. Even taking the sum of the endpoint and interior
microscopic bounds gives a coefficient smaller than the stated
80+2sqrt(L H_K)+20sqrt(L+5). No endpoint amplitude is omitted or
controlled by the inapplicable interior sharp weight approximation.

## Bulk, central nodes and complete assembly

For q(theta)=sum_(r=0)^N b_r cos(r theta), exact DCT-I orthogonality
shows that the angular trapezoidal squared norm is the continuous
angular norm plus(pi/2)|b_N|^2. This identity also holds for complex
coefficients. Hence

    integral_0^pi |q(theta)|^2 dtheta
       <=(pi/N)sum |u_k|^2/c_k.

Lebesgue physical mass is bounded above by this angular mass. On the
bulk support, d_k>=M+1>N/L, so sin(theta_k)>=2d_k/N>2/L.
The weight lower bound then yields equation(16), with squared norm
coefficient pi L/2. Endpoints are absent in this group, and the central
index for even N is included without any separate exception.

The good, microscopic and bulk supports partition all N+1 nodes,
including the transition indices K and M. Their input CC energies add
exactly. Linearity and the triangle inequality permit bounding each
group's input norm by sqrt(Q_total); this is deliberately loose only
for lower-order contributions. The residual coefficient is at most

    160+2sqrt(L H_K)+6sqrt(L+1)+20sqrt(L+5)+sqrt(pi L/2)
      <=160+2sqrt(L H_K)+30sqrt(L+5)=D_N.

For example sqrt(pi L/2)<2sqrt(L+5), leaving ample margin.
This proves the exact finite bound in the frozen statement for all
integers N with log N>=16, over arbitrary real or complex nodal data.

## Spectral conclusion and order of limits

H_J/L tends to1 and H_K=O(log L), so D_N/L tends to0 and
(C_N+D_N)/L tends to2sqrt(2)/pi^2. The all-input finite inequality
therefore implies

    liminf (log N)^2 lambda_min(CC,N) >=pi^4/8.

Positivity of CC weights and uniqueness of interpolation justify taking
the reciprocal infimum; no data-dependent error term remains. Restriction
gives lambda_min(CC,N)<=lambda_min(CC,N-1). The accepted S1-02 trial
proves limsup of the latter scaled sequence<=pi^4/8. Squeezing proves
both complete limits, through all integers, and consequently both parity
limits. The S1 trial's order of limits remains fixed envelope first,
N to infinity, cutoff removal, then dense-envelope optimization; the new
lower bound is uniform and requires no exchange with those limits.

Thus the mathematical conclusion reviewed here answers the full original
PD-T020 existence-and-value target. This does not authorize editing its
registry under handoff03, and the required independent Claude audit and
future registry disposition remain separate workflow steps. The proof
claims only an O(sqrt(L log L)) norm remainder, sufficient for the limit;
it does not establish a sharper convergence rate, extremizer convergence,
or an effective numerical approximation at practical N.

## Verification activity

Executed full file reads, text searches and SHA256 hashing only. No
numerical experiment, eigenvalue calculation or heavy process was run.
No measured K1/K2 value enters any argument. The developer supplied the
frozen hashes, which were independently rechecked before this record.
No developer, accepted-proof, audit, registry or Git file was changed by
this checker; this assembly record is its only new edit in this followup.
