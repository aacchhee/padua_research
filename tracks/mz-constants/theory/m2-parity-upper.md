# PD-T018 — parity-exact matching logarithmic upper bound

Review update, 2026-10-31: final ID allocation and scoped independent Astra review are complete; see topics/mz-constants/independent-astra-01.md and ID_CROSSWALK.md. The original development-stage pending-review wording below is historical. Required Claude audit and unresolved literature/novelty coverage remain PENDING. This administrative update changes no mathematical claim or proof.

ID kind: PD-T.
Aliases: endpoint-cancelled harmonic U witness; degree-constrained log-squared upper estimate.
Split from: the original M2 two-sided logarithmic endpoint target and the endpoint discussion retained in [PD-T019](m2-u-witness.md). PD-T019 is a related independent supporting witness, not a proof dependency or a parent whose exact norm statement is decomposed here.
Split into: none. The lower bound is PD-T017; the simpler U witness is PD-T019, whose header reciprocally records this separation.

## Statement

For every integer N≥2,

    λ_min(CC,N−1) ≤128000/(log N)².

Together with PD-T017 this proves λ_min(CC,N−1) asymp (1+log N)^−2 with explicit nonsharp comparison constants. No limit constant is asserted.

## Definitions

Use CC nodes, weights, λ_min and Lebesgue measure from PD-T017. The Chebyshev polynomials of the second kind satisfy U_r(cosθ)=sin((r+1)θ)/sinθ and U_r(±1)=(±1)^r(r+1). For N≥3 put M=floor((N−1)/2), and define

    p_N=Σ_(m=1)^M [U_(N−1−2m)−(1−2m/N)U_(N−1)]/m.

## Assumptions

Integer N≥2; no upper-spectrum hypothesis. The witness p_N is used only at the large N covered below; the small-N extension uses the constant polynomial.

## Status by part

Overall status: PROVED (development; independent audit and acceptance pending).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| All-N explicit upper comparison | PROVED | Analytic proof below |

Candidate / claim disposition: active.

## Depends on

Only the elementary weight upper bound w_k≤5sinθ_k/N proved in PD-T017. Its logarithmic lower theorem is not used in this proof.

## Checks

Developer command, rules SHA and environment: as in the lower-bound file. The measured p_N Rayleigh quotients at N=8,16,32,64,128,256,512,1024 were respectively 0.760525, 0.630681, 0.515415, 0.421689, 0.347829, 0.290004, 0.244527, 0.208428. These are floating diagnostics, not essential evidence. For the same sequence RQ·log²N grew from 3.289 to 10.014. This does not identify any limiting constant.

Runs needed: independent Astra proof reconstruction and executed replay with pinned hashes.

## Sources

Supplied `bttbmap_b2b_cc_testvec.py` reports an alternating normalized-node vector for the full interpolation space. This witness is a different construction that enforces the actual degree constraint and cancels both endpoints exactly. Historical interpolation duplicate screen remains incomplete; no novelty or priority claim is made. No private C4 formula is used.

## Proof or evidence

### 1. Degree, endpoint cancellation, and nodal values

Every term has degree at most N−1 and parity N−1. At ±1 each bracket vanishes because N−2m=(1−2m/N)N. Therefore p_N(±1)=0. Set

    B_M(θ)=Σ_(m=1)^M sin(2mθ)/m,
    A_M(θ)=Σ_(m=1)^M cos(2mθ)/m,
    C_M(θ)=A_M(θ)−H_M+2M/N.

The exact formula is

    p_N(cosθ)=[sin(Nθ)C_M(θ)−cos(Nθ)B_M(θ)]/sinθ.   (1)

At an interior node this becomes p_N(x_k)=−(−1)^k B_M(θ_k)/sinθ_k. In particular this is an admissible degree-N−1 nodal vector; it does not use the unconstrained full-degree alternating vector.

### 2. Elementary harmonic bounds

For 0<θ≤π/2 put K=floor(1/sinθ). For any a≤b the geometric-sum bound gives

    |Σ_(m=a)^b exp(2imθ)|≤1/sinθ.

Abel summation therefore bounds the harmonic tail from K+1 through any M>K by 1/((K+1)sinθ)≤1. For m≤K,

    |Σ sin(2mθ)/m|≤2Kθ≤π,
    |Σ cos(2mθ)/m|≤H_K≤1+log(1/sinθ).

If M≤K the same initial-segment bounds apply. Thus, using reflection for π/2<θ<π,

    |B_M(θ)|≤π+1<5,                               (2)

and for 0<θ≤π/2,

    A_M(θ)≤2+log(1/sinθ)≤2+log(π/(2θ)).            (3)

Since H_M≥log(M+1), M+1≥N/2 and 2M/N≤1, (3) gives

    C_M(θ)≤3+logπ−log(Nθ)≤5−log(Nθ).              (4)

### 3. Discrete norm

Endpoints contribute zero. From the weight upper bound, (2), and sin(kπ/N)≥2min(k,N−k)/N,

    Q_N(p_N²)≤(125/N)Σ_(k=1)^(N−1)1/sinθ_k
             ≤125H_(floor(N/2))≤125(1+log N).

For log N≥1 this is at most 250log N. The middle-node overcount in the harmonic bound is harmless.

### 4. Continuous norm on a mesoscopic interval

Write L=log N and suppose L≥128. On E=[N^−1/2,1/4], (4) gives C_M≤5−L/2≤−L/4. The inequality (a−b)²≥a²/2−b² in (1) gives

    ∫[-1,1]p_N² dx ≥ (L²/32) I−25J,
    I=∫_E sin²(Nθ)/sinθ dθ,  J=∫_E 1/sinθ dθ.

Since sinθ≤θ,

    I≥(1/2)log((1/4)√N)−(1/2)|∫_E cos(2Nθ)/θ dθ|.

One integration by parts bounds the last absolute value by 1/(N·N^−1/2)=N^−1/2: the endpoint terms plus the integral of θ^−2 telescope to this bound. Thus

    I≥L/4−log2−1/(2√N)≥L/8.

Also sinθ≥θ/2 on E, so J≤2log((1/4)√N)≤L. Consequently

    ∫p_N² ≥L³/256−25L≥L³/512,

where the last inequality follows from L²≥128²>12800. In particular the witness is nonzero.

### 5. All N

For L≥128, its quotient is at most 250·512/L²=128000/L². If 0<L<128, the constant polynomial gives λ_min≤1<128000/L². This proves the all-N statement without numerical checking of an enormous initial range.

## Scope

This supplies the matching upper order in the precise degree-N−1 space. The large constants are analytic comparison constants, not estimates of the optimal leading coefficient. The lower theorem and this theorem establish a full two-sided order result, subject to independent acceptance.

The witness estimate starts at log N≥128, but its bound 128000/(log N)² is below the trivial upper bound 1 exactly when log N>√128000≈357.7709 (equivalently N>exp(√128000)); it is therefore vacuous throughout all computationally feasible full-spectrum calculations considered here, and the finite tables do not exhibit or determine an asymptotic leading constant.

## Open items

Prior-art comparison and independent adversarial audit. Determining lim (log N)²λ_min, or proving that it exists, remains open. This result alone implies liminf η_N≥1 for η_N=||I−G_N||₂; asserting η_N→1 also requires upper-spectrum control and is not done here.

## History

2026-10-31, Codex subagent, gpt-6.1-sol xhigh (explicit orchestrator assignment); rules/base d36722823441dc40c6e19d69a174459348dd309c. The full-space alternating-node trial was not transferred; the harmonic U construction was derived to satisfy degree and endpoint constraints.

2026-10-31, audit-01 L2/P4 response, Codex gpt-6.1-sol xhigh (explicit assignment), rules `6d10a82cf6fd6f7ef6fbe76e68133ccbcbe51994`: stated the exact non-vacuity threshold and finite-table limitation without introducing a fit or changing the comparison constant. Added reciprocal semantic provenance to PD-T019, distinguishing separation of the endpoint discussion from decomposition of its exact norm statement. The proof, statement and PROVED status are unchanged.
