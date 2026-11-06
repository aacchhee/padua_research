# PD-T?mz-sharp-codex-P3-03 — the sharp reciprocal CC limit

ID kind: PD-T.
Aliases: reverse Volterra transfer; sharp logarithmic CC minimum.
Split from: PD-T020's original limit-existence/value target, completed here.
Split into: P3-01 and P3-02 are separate supporting lemmas, not cases.

## Statement

For unnormalized Lebesgue Clenshaw–Curtis quadrature with N+1 nodes,

    lim_(N->infinity) (log N)^2 lambda_min(CC,N-1)=pi^4/8. (1)

The limit holds through all integers N, hence on both parities. The
same limit holds on the full interpolation space Pi_N. No numerical
fit, eigenvalue computation or regularity assumption on minimizers is
used. The finite inequality proved below holds for arbitrary nodal data.

An explicit, deliberately coarse finite bound is as follows. For
integer N with L=log N>=16 put

    J=floor(N/2), K=ceil(L^2), M=floor(N/L),
    H_r=sum_(k=1)^r 1/k, A=2H_J/pi+1, epsilon=2/L^2,
    C_N=sqrt(2A^2+6)/[pi sqrt(1-epsilon)],
    D_N=160+2sqrt(L H_K)+30sqrt(L+5).

For every real or complex polynomial p of degree at most N,

    ||p||_(L2(dx)) <=(C_N+D_N) sqrt(Q_N(|p|^2)).       (2)

Here C_N/L ->2sqrt(2)/pi^2 and D_N/L ->0. Thus (2) proves
liminf L^2 lambda_min(CC,N)>=pi^4/8. The already proved S1-02
admissible trial supplies the matching limsup on Pi_(N-1).

## Definitions and assumptions

N>=2 integer, theta_k=k pi/N, x_k=cos(theta_k),
Q_N(|p|^2)=sum_(k=0)^N w_k|p(x_k)|^2, where w_k are the exact
positive Lebesgue CC weights of PD-T013. Norms use unnormalized dx
on [-1,1]. Let c_0=c_N=2 and c_k=1 otherwise; these c_k are
reciprocal endpoint factors, not PD-T013's endpoint halfweights.
The spectral minimum uses the indicated exact polynomial space.
Natural logarithms throughout. No small-N validation is required for
an asymptotic statement; (2) is asserted only when L>=16.

## Status by part

Overall status: PROVED. The complete assembly received supplementary
checks and was accepted in [audit-02](../audit-02.md); registry application
to PD-T020 remains deferred to PR preparation.

| Mathematical part | Status | Evidence |
|---|---|---|
| Full-space finite interpolation bound (2) | PROVED | Exact kernel split and all-input estimates below |
| Reverse liminf and both sharp limits (1) | PROVED | (2), restriction and existing S1-02 limsup |

The shared PD-T020 registry is deliberately unchanged under handoff03.
Its original wording is preserved; this result claims its full limit,
not a narrowing to a trial family or a subsequence.

## Depends on

PD-T013 and PD-T017 proof section 1: exact cardinal interpolation,
weight floor and uniform weight expansion. P3-01
(P3-signed-remainder.md): signed homogeneous error norm <=40.
P3-02 (P3-discrete-primitive.md): sharp discrete primitive with uniform
oscillation factor 1/2. S1-02 (S1-sharp-one-sided.md): admissible
degree-(N-1) trial with limsup <=pi^4/8. Its Volterra dependency is
already separately proved. No other asymptotic theorem is assumed.

## Proof

### 1. Weight estimates and the exact global half-interval split

PD-T017 proves, writing d_k=min(k,N-k),

    w_k >=(1+d_k)/N^2,
    w_k >=sin(theta_k)/N             (0<k<N),
    |w_k-(pi/N)sin(theta_k)|<=3/N^2  (0<k<N).        (3)

The last bound follows directly from its telescoping Fourier tail:
the sharper bound is 2/(N^2-1)<=3/N^2 for N>=2. In particular,

    sum_(k=0)^N 1/w_k
      <=2N^2 H_(floor(N/2)+1)<=2N^2(L+1).           (4)

For arbitrary nodal input u let I_N u be its degree-N interpolant,
a_k=(-1)^k u_k, and Q(u)=sum w_k|u_k|^2. Exact cardinal interpolation
on the left physical half, theta in [0,pi/2], equivalently x in [0,1],
with theta=pi t/N and 0<=t<=N/2, gives

    (I_N u)(cos theta)=H_u(t)+r_u(theta),
    H_u(t)=(2t sin(pi t)/pi)
                    sum_(k=0)^N a_k/[c_k(t^2-k^2)]. (5)

To derive it, use

    -sin(theta)/(cos(theta)-cos(phi))
       ={cot((theta-phi)/2)+cot((theta+phi)/2)}/2,
    e(z)=cot(z/2)-2/z.

The function e extends continuously at zero and satisfies |e(z)|<2
on [-pi,3pi/2]. Indeed it is odd and nonincreasing for 0<z<2pi, since
e'(z)=2/z^2-(1/2)csc^2(z/2)<=0; its largest magnitude on the
positive interval is 1+4/(3pi)<2. All arguments theta-phi and
theta+phi in the left half lie in this interval. The remainder in
(5) therefore obeys

    |r_u(theta)| <=(2/N) sum_k |u_k|/c_k
                  <=2sqrt(2(L+1)) sqrt(Q(u)).        (6)

The left physical half theta in [0,pi/2], x in [0,1], has dx mass 1. Apply the reflected calculation on the
right half as well; reflection sends u_k to u_(N-k), preserves the
CC energy and only changes harmless alternating signs. The combined
cotangent remainder has norm <=4sqrt(L+1) sqrt(Q(u)). All nodal
poles in (5) are interpreted by continuity. This calculation includes
theta=0 and theta=pi as measure-zero limiting values.

### 2. One-edge inputs, the signed error, and the cross-edge term

First suppose u is supported on interior indices 1<=k<=M<N/4.
Put g_k=k a_k/N and E=sum |g_k|^2/k. By (3), E<=Q(u).
On the left output half, the exact homogeneous expression is

    H_u(t)= [2N sin(pi t)/(pi t)] S(t)
              +[2N/(pi t)] (Eg)(t),
    S(t)=sum_(k<t)g_k/k.                             (7)

Here E in Eg denotes the operator of P3-01, not the scalar energy.
The exact mass element satisfies

    sin(theta)dtheta <= pi^2 t dt/N^2.

Thus the signed error term in (7) has squared physical norm at most
4||Eg||_(L2(dt/t))^2<=6400 E, by P3-01. Its norm is at most
80sqrt(Q(u)), uniformly even on microscopic output cells.

To control the other edge's input on this output half, its global
indices k satisfy k>=N-M>=3N/4. There

    |2t/[pi(t^2-k^2)]|<=3t/N^2,  0<=t<=N/2.

Use (4) and Cauchy–Schwarz on that input to obtain

    |H_cross(t)|<=[3t/N]sqrt(2(L+1)Q(u_right)).

Integration against pi^2 t dt/N^2 gives squared norm at most
(9pi^2/32)(L+1)Q(u_right)<3(L+1)Q(u_right). The reflected
cross-edge estimate is identical. Because the two output halves
and two input groups are disjoint, the combined cross operator has
norm <=2sqrt(L+1) in the CC input norm. With (6), the signed error
and cross terms together are bounded by

    [80+6sqrt(L+1)]sqrt(Q(u_left)+Q(u_right)).         (8)

This holds for any two opposite interior edge groups within width
M<N/4. No estimate near k=N/2 was omitted: those indices will be
handled separately by exact angular DCT stability in section 5.

### 3. The two good endpoint layers and the sharp coefficient

For L>=16 one has 1<K<=M<N/4; for example e^L/L^3 is increasing
there and e^16>2^16>4*16^3. Let the good layers be K<=k<=M and
N-M<=k<=N-K. For the left layer, z=pi k/N<=pi/L, so (3) gives

    N^2 w_k/k
       >= pi^2 sin(z)/z-3/k
       >= pi^2[1-pi^2/(6L^2)]-3/L^2
       >= pi^2(1-2/L^2).                            (9)

The last inequality uses 9<pi^2<10. The reflected layer obeys the
same bound. Consequently their two scalar energies satisfy

    E_left+E_right
       <= Q(u_good)/[pi^2(1-epsilon)].               (10)

Apply P3-02 with T=N/2, J=floor(N/2), extending each g by zero
through J. From (7) and its mass element, each extracted primitive
has squared physical norm at most

    4 integral_0^(N/2) sin^2(pi t)|S(t)|^2 dt/t
       <=(2A^2+6)E.

Both primitives have disjoint output halves, so (10) bounds their
combined norm by C_N sqrt(Q(u_good)). With (8),

    ||I_N u_good||
       <=[C_N+80+6sqrt(L+1)]sqrt(Q(u_good)).          (11)

This is the only leading O(L) contribution. In particular the
sin^2 factor is averaged with a uniform bound for every discrete
primitive, rather than by assuming a smooth limiting envelope.

### 4. Microscopic nodes, including the two endpoint columns

For interior microscopic inputs 1<=k<K and their reflections,
the scalar energies in (7) still obey E_left+E_right<=Q(u_micro,int)
by the coarse floor in (3). For every t,

    |S(t)|^2<=H_K E,

and S(t)=0 for t<1. Since integral_1^(N/2)dt/t<=L, their two
primitive pieces have combined norm <=2sqrt(L H_K)sqrt(Q).
The error (8) still applies because K-1<=M. Thus

    ||I_N u_micro,int||
      <=[2sqrt(L H_K)+80+6sqrt(L+1)]sqrt(Q).          (12)

For the left endpoint k=0, c_0=2 in (5) gives exactly the self-edge
homogeneous contribution a_0 sin(pi t)/(pi t). Its squared mass is
at most

    |a_0|^2/N^2 integral_0^(N/2) sin^2(pi t)dt/t
       <= (L+pi^2/2)|a_0|^2/N^2 <=(L+5)Q(u_0).     (13)

Here t<1 uses |sin(pi t)|<=pi t, and t>=1 uses the logarithm.
The right endpoint is identical. Their cross-edge and e terms have
the same bounds proved above (c_k>=1 only improves them). Therefore
the combined two-endpoint operator has norm at most

    sqrt(L+5)+6sqrt(L+1)<=10sqrt(L+5).               (14)

Combine (12) and (14), conservatively bounding each sub-energy by
the total microscopic energy. For all indices k<K or N-k<K,

    ||I_N u_micro||
      <=[2sqrt(L H_K)+80+20sqrt(L+5)]sqrt(Q(u_micro)). (15)

Thus endpoint columns and shrinking physical cells cost only
O(sqrt(L log L)), uniformly over all their nodal inputs.

### 5. Every bulk index, including the central index on even N

All remaining bulk indices satisfy M<k<N-M. For any nodal input
supported there, exact angular DCT-I orthogonality gives

    integral_0^pi |(I_N u)(cos theta)|^2 dtheta
       <= (pi/N) sum_(k=0)^N |u_k|^2/c_k.

Indeed the trapezoidal angular norm is the continuous cosine norm
plus (pi/2)|b_N|^2, where b_N is the interpolant's top Chebyshev
coefficient. Endpoints vanish for the bulk input. Passing to the physical norm uses
dx=sin(theta)dtheta<=dtheta in the integral after x=cos(theta)
and reversal of endpoints. Since
sin(theta_k)>=2min(k,N-k)/N>2/L, (3) implies

    ||I_N u_bulk||^2 <= (pi/N)sum |u_k|^2
                        <=(pi L/2)Q(u_bulk).         (16)

This includes k=N/2 when it exists. It also includes every
transition index between the two good layers, with no boundary
regularity or parity assumption.

### 6. Assembly and the sharp limit

The good, microscopic and bulk input supports partition all nodes;
their squared CC energies sum exactly to Q_N(|p|^2). Interpolation
is linear. Sum (11), (15) and the square root of (16), bounding each
group norm by the total input norm. The nonleading coefficients are
at most

    160+2sqrt(L H_K)+6sqrt(L+1)+20sqrt(L+5)
         +sqrt(pi L/2) <=D_N.

This proves (2) for every polynomial in Pi_N. H_J<=L+1 gives
C_N/L ->2sqrt(2)/pi^2; more precisely H_J/L ->1 since
log(J+1)<=H_J<=1+log J. Also H_K=O(log L), so D_N/L ->0.
Consequently

    liminf L^2 lambda_min(CC,N)>=pi^4/8.

Restriction yields lambda_min(CC,N-1)>=lambda_min(CC,N). S1-02
proves the opposite limsup <=pi^4/8 on Pi_(N-1). Both limits,
including the full-space limit by monotonicity, are therefore pi^4/8.
Every estimate holds through all sufficiently large integer N, so
both parity subsequences have the same limit.

## Checks, sources and limitations

Analytic development only; no new numerical execution. The proof uses
the exact registered norms and preserves K1/K2 outcomes. R was
published at `17ca9f441cece178354e70504a6c739df501a224` before this
development. Gate and candidate: ../novelty-gate-P3.md and
../ideas/P3-reverse.md. The explicit finite bound is coarse and no
practical threshold or decimal eigenvalue accuracy is asserted.

Independent review of the supporting signed remainder and the full
assembly is separate from development. No shared registry, accepted
proof, final ID, numerical gate or original target wording is edited.

## History

2026-11-06, P3 round2. Codex mathematical developer, requested
gpt-6.1-sol xhigh; serving metadata unexposed. Rules/source
`0205690b9c4e959a28e949083e9a1808735abf4b`. The logarithmic error
O(sqrt(L log L)) is sufficient for the sharp limit and makes no
claim of the stronger O(sqrt L) remainder suggested in the audit lead.
