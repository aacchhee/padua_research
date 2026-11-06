# PD-T?mz-sharp-codex-S1-02 — a sharp-model one-sided CC bound

ID kind: PD-T.
Aliases: logarithmic half-wave trial; parity-reflected nodal envelope.
Split from: supporting variational upper bound toward PD-T020.
Split into: none. PD-T020 itself remains OPEN without the reverse bound.

## Statement

For Lebesgue Clenshaw–Curtis on degree N−1,

    limsup_(N -> infinity) (log N)² lambda_min(CC,N−1) <= pi⁴/8. (A)

The same assertion holds on the even-N and odd-N subsequences. This
does not assert that pi⁴/8 is the true limit or that a limit exists.

More precisely, let f be a nonzero real C¹ function with compact support
in (0,1), put L=log N, and extend f by0 outside (0,1). At the nodes
choose signed amplitudes

    a_k=(N/k) f(log k/L),    1<=k<N/2,
    a_(N−k)=−a_k,
    a_0=a_N=0; a_(N/2)=0 if N even,
    v_k=(−1)^k a_k.

For all sufficiently large N, these define a nonzero interpolant
p_N in Pi_(N−1). With F(x)=integral_0^x f(s) ds,

    Q_N(p_N²)=2*pi²*L*||f||²+o_f(L),                  (B)
    liminf_N ||p_N||²/L³ >=4*||F||².                 (C)

## Definitions and assumptions

Actual positive CC weights and unnormalized Lebesgue dx, N+1 nodes
cos(k*pi/N), natural logarithm. Norms of f,F use (0,1); p_N uses
[-1,1]. Every asymptotic estimate below holds through all integers N.

## Status by part

Overall status: PROVED (analytic development; independent audit required).

| Part | Status | Evidence |
|---|---|---|
| Exact degree-constrained trial and (B)–(C) | PROVED | Written kernel and harmonic-sum estimates |
| One-sided bound (A) | PROVED | Variational principle and density applied to the model norm |

Candidate disposition: retained one-sided result. PD-T020 stays OPEN;
these are supporting bounds, not proved cases of its limit statement.

## Depends on

PD-T013: exact cardinal/DCT formula and positivity of weights.
PD-T017: w_k=(pi/N)sin(k*pi/N)+O(N^−2), uniformly at interior nodes.
PD-T?mz-sharp-codex-S1-01: exact primitive model norm2/pi.
No external theorem or numerical eigenvalue data.

## Checks and sources

No numerical experiment is needed or claimed. Rules/source2143ad6;
model preregistered by coordinator in977c07a before K1 fits/disclosure.
The proof below was developed without reading K1 final data.
Bounded local predecessor screen: ../novelty-gate-S1.md. Requested
developer model gpt-6.1-sol xhigh; runtime metadata unexposed.

Supplementary distinct Astra review reconstructed the frozen proof at
SHA256 b560b08db44f25417e36c4ff53f76baf0f14e2ae9130eb7457d1249b11a32eb0
and returned PASS for its exact one-sided scope; see
../independent-checks-S1-S3.md. The required later Claude audit is separate.

## Proof

### 1. Degree and discrete energy

Fix0<a<b<1 containing supp f. Nonzero left amplitudes have
N^a<=k<=N^b, so for sufficiently large N they lie below N/2 and the
reflected supports are disjoint. The top DCT coefficient of the
degree-N interpolant is N^−1 sum_k a_k/c_k, where c_0=c_N=2 and
c_k=1 otherwise. The reflected opposite signs cancel this sum exactly.
Thus p_N has degree<=N−1. In fact
p_N(−x)=(−1)^(N−1)p_N(x), by uniqueness of interpolation; its squared
mass is the same near the two endpoints, for either parity of N.
Nonzero f gives at least one nonzero value for all sufficiently large N.

Uniformly on the support, the weight expansion and sin theta=theta
(1+O(theta²)) give

    w_k=(pi²*k/N²) [1+O(N^(2b−2)+N^−a)].

The log Riemann sum is

    sum_k f(log k/L)²/k = L*integral_0^1 f²+o(1).

For example apply sum-integral comparison to h(u)=f(log u/L)²/u;
the integral of |h'| on u>=N^a is O_f(N^−a). Both reflected weights
are equal. This proves (B), with relative error
O_f(N^(2b−2)+N^−a)+o_f(1/L).

### 2. A bounded residual of the homogeneous endpoint kernel

Write g_k=f(log k/L), S(t)=sum_(k<t)g_k/k and, for noninteger t>=2,

    B_k(t)=t²/[k*(t²−k²)]−1_(k<t)/k,
    R(t)=sum_(k>=1) g_k B_k(t).

The sum is finite. We claim, uniformly in N,t,

    |sin(pi*t) R(t)| <= C_f.                         (D)

For k<=t/2, B_k=k/(t²−k²), whose absolute sum is bounded by an
absolute constant. For k>=2t, B_k=t²/[k*(t²−k²)], with the same
property by comparison with t²/k³. On t/2<k<2t,

    B_k=1/[2*(t−k)]+E_k,    |E_k|<=C/t.

Indeed E_k=−1/[2*(t+k)] below t and
E_k=(2t+k)/[2*k*(t+k)] above t. Their total is bounded. Replacing
g_k in the pole part by g(t)=f(log t/L) changes its sum by at most
C*||f'||_infinity/L, because
|log(k/t)|<=2|k−t|/t on this range.

It remains to bound sin(pi*t) sum_(t/2<k<2t)1/(t−k).
Write t=j+u, |u|<=1/2. Pair the integers j−r,j+r up to distance
at most t/2: their sum is2u/(u²−r²), whose absolute sum for r>=1
is uniformly bounded. The r=0 term, if present, is1/u and
|sin(pi*u)/u|<=pi. Remaining unpaired terms have distance bounded
below by c*t and O(t) terms, so their absolute sum is bounded.
The finitely many small t cases satisfy the same bound. This proves
(D); removable singularities at integral t are interpreted continuously.

It follows that the homogeneous interpolation expression satisfies

    (2*t*sin(pi*t)/pi) sum_k [(N/k)*g_k]/(t²−k²)
      = (2*N*sin(pi*t)/(pi*t)) S(t)+O_f(N/t).          (E)

Uniform sum-integral comparison also gives, for x=log(t)/L,

    S(t)=L*F(x)+O_f(N^−a).                          (F)

The strict versus non-strict endpoint in S costs at most O_f(N^−a)
on its support and none outside; the formulas concern noninteger t
before continuous extension in (E).

### 3. Exact cardinal formula versus its homogeneous kernel

Fix0<delta<1/2 and put N^delta<=t<=N^(1−delta), theta=pi*t/N.
The exact formula, with endpoint values zero, is

    p_N(cos theta)=−sin(theta)*sin(N theta)/N
                    *sum_(k=1)^(N−1) a_k/(cos theta−cos theta_k).

For the left support theta_k<=pi*N^(b−1), the cotangent identity gives

    −sin(theta)/(cos theta−cos phi)
      = [cot((theta−phi)/2)+cot((theta+phi)/2)]/2
      = 2*theta/(theta²−phi²)+O(theta),               (G)

uniformly when theta,phi tend to0. To see uniformity even at theta=phi,
cot(z/2)−2/z is odd with bounded derivative on a fixed small interval.
Its values at theta−phi and theta+phi have sum O(theta); the singular
residues agree exactly. On the reflected right support the denominator
is bounded away from0, and the entire corresponding factor is O(theta).
Since sum |a_k|=O_f(N*L), (E)–(G) imply uniformly on this output range

    p_N(cos(pi*t/N))
      = [2*N*L*sin(pi*t)/(pi*t)] F(log t/L)
          +O_f(N/t)+O_f(theta*L).                   (H)

### 4. Continuous mass with the oscillation and Jacobian retained

On this range the angular mass element is

    sin(theta)dtheta=(pi²*t/N²)[1+O(N^−2delta)]dt.

The O_f(N/t) remainder in (H) has squared norm O_f(L), since the
integral of dt/t over this range is O(L). The O_f(theta*L) remainder
has squared norm O_f(L²*N^−4delta). The leading term's squared mass is

    4*L² integral_(N^delta)^(N^(1−delta))
          sin²(pi*t)*F(log t/L)² dt/t
       +O_f(L³*N^−2delta)
      =2*L³ integral_delta^(1−delta) F(x)² dx+o_f,delta(L³). (I)

For the last equality use sin²=(1−cos(2*pi*t))/2. Integrating the
cosine term once by parts bounds it by C_f*N^−delta: the derivative
of F(log t/L)²/t is O_f(t^−2). Thus the factor1/2 is justified,
not assumed. The norm triangle inequality controls the cross terms
with the two remainders by O_f,delta(L²)+o(L²).

The right endpoint interval has exactly the same mass and is disjoint
for sufficiently large N. Discarding all remaining nonnegative mass
and then taking delta down to0 proves (C).

### 5. Optimize the trial family

(B)–(C) and the Rayleigh principle imply for every such f

    limsup L² lambda_min <= (pi²/2)||f||²/||Vf||².

Choose C¹ compactly supported f_j converging in L²(0,1) to
cos(pi*x/2). The primitive operator is bounded, so Vf_j converges
in L² to V cos(pi*x/2); its norm is positive. The quotient tends
pi⁴/8 by the exact model lemma. This proves (A). Every construction
and estimate held for all sufficiently large integers N, so it holds
on both parity subsequences. No numerical input enters the proof.

## Scope and open items

This is a one-sided asymptotic spectral bound with an explicit constant
and admissible trial family. Sharpness of the constant for the true
finite-N minima remains OPEN. A matching liminf requires a uniform
upper bound on the entire reciprocal cardinal interpolation operator,
including signed near-diagonal interactions, microscopic cells, bulk
and cross-endpoint terms. The model's exact norm and this limsup do
not alone prove convergence or justify changing PD-T020 to PARTIAL.

## History

2026-11-06: S1 round2, after prediction commit977c07a and without K1
final-data access. This strengthens the prior nonsharp upper comparison
without changing its proof or status; no historical novelty claim.
