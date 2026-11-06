# PD-T524 — reciprocal CC logarithmic model

2026-11-06 ID history: `PD-T?mz-sharp-codex-904` → `PD-T524`; statements, original registrations and historical dispositions are preserved.

Rules/source2143ad622fa98faf8fe7d5cb8ed2bb7e0062f861.
Prediction written 2026-11-06, before access to final K1 extrapolation.
Coordinator's committing SHA supplies the prospective timestamp.

ID kind: PD-T (original target PD-T020 was OPEN at registration; no new
finite-N claim is assigned here). Aliases: logarithmic primitive transfer model.
Split from: none. Split into: exact model norm S1-volterra-model.md;
that supporting result is not a proved case of the target.

## Statement and status

**Preregistered model prediction, CONDITIONAL on the transfer obligations
below:** for both parities of N,

    c_*^model = pi⁴/8 = 12.1761363792503...,
    (log N)² lambda_min(CC,N−1) -> pi⁴/8.

The decimal is arithmetic notation, not a fit or eigenvalue measurement.
The finite-N limit itself remains OPEN at this registration. In
particular a continuum model's exact norm is not a finite-N theorem.

## Definitions and exact starting point

CC nodes x_k=cos(theta_k), theta_k=k*pi/N, weights w_k, measure dx.
Write v_k=p(x_k), a_k=(−1)^k v_k, with endpoint c_0=c_N=2 and
interior c_k=1. Exact cardinal interpolation gives

    p(cos theta) = −sin(theta)*sin(N theta)/N
                    *sum_(k=0)^N a_k/[c_k*(cos theta−cos theta_k)]. (1)

The coefficient of T_N is N^−1 sum a_k/c_k. Hence the exact condition
a_(N−k)=−a_k, with any central index set to0, gives degree<=N−1.
This holds for both parities, and corresponds to polynomial parity N−1.
Endpoint values may be set to0. No strictly positive full-space
alternating trial is transferred to the constrained space.

## Derivation of the coefficient

Set L=log N and t=N theta/pi. Near the left endpoint, k,t large but
k,t=o(N), (1)'s homogeneous kernel is

    p(cos(pi*t/N)) approximately
       (2*t*sin(pi*t)/pi) sum_k a_k/(t²−k²).             (2)

Use the family a_k=(N/k)f(log(k)/L), and reflect with opposite a sign
at the right endpoint. For k much smaller than t, the kernel in (2)
is (2*sin(pi*t)/(pi*t))*a_k. Therefore, with x=log(t)/L,

    sum_(k<t) a_k approximately N*L*(Vf)(x),
    p approximately 2*N*L*sin(pi*t)/(pi*t)*(Vf)(x).     (3)

The exact CC weight expansion from PD-T017 is
w_k=(pi/N)sin(theta_k)+O(N^−2), so in this mesoscopic range
w_k approximately pi²*k/N². Thus each endpoint has discrete energy

    Q_left approximately pi²*L integral_0^1 f(x)² dx.   (4)

Retain dx=sin(theta)dtheta approximately pi²*t*dt/N² in (3).
Averaging sin²(pi*t) gives1/2, hence continuous mass per endpoint

    M_left approximately 2*L³ integral_0^1 (Vf)(x)² dx. (5)

The two endpoint factors cancel in the quotient. Consequently the
model scaled Rayleigh quotient is

    (pi²/2) integral f² / integral(Vf)².                 (6)

The exact norm calculation in S1-volterra-model.md makes its infimum
pi⁴/8, with f(x)=cos(pi*x/2). The reflected pair (f,−f) attains the
same value and enforces the exact degree constraint. Therefore the
model predicts equal constants for even and odd N.

## Mellin structure and threshold coefficient

With y=log t, s=log k, the kernel multiplying f(s) is

    H(y−s)=1/(1−exp(−2*(y−s))).

In principal value it decomposes exactly as

    H(u)=1_(u>0)+r(u),
    r(u)=sgn(u)/(exp(2*abs(u))−1).

The remainder is odd, behaves as1/(2u) at0 and decays exponentially
at infinity. Its convolution is a bounded singular-integral part;
the primitive gives the Mellin pole1/(i*xi). After the weight and
oscillation factors in (4)–(5), the reciprocal mass multiplier has
principal part sqrt(2)/(pi*i*xi), so the corresponding direct Gram
symbol has second-order part (pi²/2)*xi². The boundary F(0)=0 with
F(1) free has first frequency pi/(2L), producing pi⁴/(8L²), rather
than the full Dirichlet-wave frequency pi/L.

This symbolic discussion motivates the proposed route. A bounded
continuum remainder is insufficient without the discrete-to-continuous
operator estimates below; no such transfer is assumed proved here.

## Finite-N proof obligations

1. For smooth f compactly supported in0<x<1, prove (4)–(5) with o(L)
   and o(L³) errors for the exact parity-reflected nodal interpolant.
   Density of these envelopes approaches the model infimum and gives
   the sharp one-sided limsup<=pi⁴/8.
2. In the entire full interpolation space, split node and angle scales
   dyadically. On comparable scales, retain signed cardinal interpolation
   and use exact unweighted DCT L² stability; do not replace it by an
   absolute harmonic near-diagonal majorant.
3. On separated scales extract the one-sided primitive with leading
   coefficient2/pi. Bound its other tail and kernel error in normalized
   operator norm by o(L). Control microscopic and bulk inputs, endpoint
   cardinal columns, and cross-endpoint terms at o(L) scale.
4. Prove the uniform oscillatory averaging factor1/2 for the extracted
   discrete primitive. Prove the sharp discrete primitive norm
   (2/pi+o(1))*L with actual CC normalization.

The full-space upper interpolation estimate in2–4, combined with the
degree-constrained trial from1, would prove PD-T020 for all N and also
the same leading constant for the full degree-N space. That stronger
consequence is a prediction only until its proof is written.

## Checks, limitations and sources

No S1 numerical experiment or K1 final data was read. The exact
starting identities are PD-T013/017; the admissibility warning is
PD-N006; the supporting-profile comparison is PD-T294. Local
predecessor coverage is in novelty-gate-S1.md. No external theorem or
priority claim; handoff literature formulas are not imported.

## History

2026-11-06: first model/prediction written after the prospective gate.
Developer requested gpt-6.1-sol xhigh; runtime metadata unexposed.
The coordinator receives this file before K1 final numbers and must
commit it before sharing those numbers. The target is still OPEN.

### Dated K2 disposition, appended after registration

The coordinator committed this prediction in977c07a before K1 fits.
K1 subsequently passed its prescribed two-window stability test on
each parity, with final-window fitted intercept about13.06114. Its
7.268% difference from pi⁴/8 exceeds K2's5% threshold. Accordingly
this **model route is deferred and stopped**. No justified
revision of the leading coefficient was found; the permitted revision
is unused. The original criterion has not been changed.

This measured gate is not a mathematical refutation of the continuum
norm or of the independently completed one-sided theorem
[S1-sharp-one-sided](S1-sharp-one-sided.md). An uncontrolled finite-fit
intercept above a proved limsup is compatible with finite-window bias;
no bound on that bias or claim that the fit calculation is wrong is
made. A matching lower bound and the original PD-T020 limit are OPEN.
The earlier numbered transfer obligations describe the stopped route,
not authorized continuing work after the kill.


## 2026-11-06 audit-01 A1 interpretation

The K1 final-window intercept 13.0611 exceeds the PROVED upper bound
limsup (log N)² lambda_min <= pi⁴/8 = 12.1761. The fitted intercept therefore
cannot be the true limit under S1-02. K2 KILL_MODEL remains the unchanged
registered operational outcome, but carries no evidential weight against
equality: the equality route stopped on a misspecified numerical test.
Disposition: **deferred**, not rejected or refuted; no PD-N is created.
Resume on a proof of the reverse bound liminf (log N)² lambda_min >= pi⁴/8,
or a new prospectively registered numerical protocol. The one-sided theorem
and classical model norm remain independent PROVED records.

## 2026-11-06 P3 completes the reverse-bound resume condition

The newly authorized [P3 reverse-bound proof](P3-reverse-bound.md) proves the matching liminf and therefore the exact pi^4/8 limit on Pi_(N-1) and Pi_N, both parities. The historical S1 gate/disposition above records its original stop; P3 is the separately gated analytic continuation that fulfills its stated resume condition. Original K1/K2 criteria, data and operational outcomes are unchanged. The proof was accepted in [audit-02](../audit-02.md). Current disposition: **resolved via P3** (PD-T546 together with PD-T523); the deferred route's reverse-bound resume condition is met and PD-T020 is PROVED. The earlier K2 stop and deferred disposition remain historical records, with no PD-N.

## 2026-11-06 audit-02 C2 wording history

The pre-response-01 disposition read “operationally rejected”. Response-01
replaced that wording in place with “deferred” (in the model record,
“model route is deferred and stopped”), to distinguish the unchanged
K2 operational outcome from mathematical rejection. This History entry
preserves the original wording; it changes no disposition, gate or proof.
