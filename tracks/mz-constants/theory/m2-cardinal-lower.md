# PD-T017 — an all-N cardinal lower bound

Review update, 2026-10-31: final ID allocation and scoped independent Astra review are complete; see topics/mz-constants/independent-astra-01.md and ID_CROSSWALK.md. The original development-stage pending-review wording below is historical. Required Claude audit and unresolved literature/novelty coverage remain PENDING. This administrative update changes no mathematical claim or proof.

ID kind: PD-T.
Aliases: weighted cell Schur bound; full Lobatto interpolation lower spectrum.
Split from: M2 target, two-sided logarithmic endpoint order.
Split into: none. The matching upper bound has its own result PD-T018.

## Statement

Let N≥2 be an integer. For every real polynomial p of degree at most N,

    ∫[-1,1] p(x)² dx ≤ K_N Q_N(p²),
    K_N=4π²(π+1)² h_N(h_N+2H_(floor(N/2)+1)),
    h_N=2H_(N+1)−1,   H_s=Σ_(r=1)^s 1/r.

Consequently λ_min(CC,N)≥1/K_N, and restriction gives λ_min(CC,N−1)≥λ_min(CC,N)≥1/K_N. In particular both are bounded below by a positive explicit constant times (1+log N)^−2. The statement includes the full interpolation space Π_N.

## Definitions

θ_k=kπ/N, x_k=cos θ_k, k=0,…,N; ℓ_k is the degree-N polynomial cardinal at these nodes. The Clenshaw–Curtis weights are w_k=∫ℓ_k dx, and Q_N(f)=Σ w_k f(x_k). All integrals use unnormalized Lebesgue measure. λ_min(CC,n)=inf_(0≠p∈Π_n) Q_N(p²)/∫p². Put c_0=c_N=2 and c_k=1 otherwise; m_k=1+min(k,N−k).

## Assumptions

Only the stated integer range, real coefficients, nodes, measure and interpolatory weights. No unverified literature theorem or private result is used.

## Status by part

Overall status: PROVED (development; acceptance and independent audit pending).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Explicit all-N inequality | PROVED | Analytic proof below |

Candidate / claim disposition: active; no rejection.

## Depends on

Elementary finite interpolation and the explicitly proved Fourier/Schur calculations below. No dependency on M1.

## Checks

Rules read at d36722823441dc40c6e19d69a174459348dd309c. Developer performs no Git operations. `python tracks/mz-constants/code/m2_endpoint.py --exact 512 --measure 8 16 32 64 128 256 512 1024` ran 2026-10-31, Python 3.12.14 / NumPy 2.3.5 / SciPy 1.17.0. The measured floor min(w_k N²/m_k) was ≥1 for these eight even N; this supports, but is not needed by, the analytic inequality. Code/input hashes and independent audit are recorded in the M2 direction log.

Runs needed: independent Astra reconstruction of the bounds and rerun. No finite experiment is represented as a proof of all N.

## Sources

Closest supplied predecessor: `bttbmap_b2_cc_schur.py`, a reported entrywise mass-defect/Schur route, not used as proof. Its exact input identity is retained in the supplied SHA256SUMS.txt and M2 direction log. Historical Lobatto interpolation literature is FULLTEXT UNVERIFIED; see topic literature-search.md. No priority claim is made.

## Proof or evidence

### 1. Weight bounds

For 0<θ<π, the absolutely convergent cosine series

    (π/2)sinθ = 1−2Σ_(r≥1) cos(2rθ)/(4r²−1)

follows by integrating sinθ against cos(2rθ). The coefficient calculation and absolute convergence identify the continuous function (for example, cosine-polynomial density proves uniqueness). The inverse cosine interpolation formula gives, at an interior node,

    w_k=(2/N)S_N(θ_k),

where for odd N=2q+1, S_N=1−2Σ_(r=1)^q cos(2rθ)/(4r²−1), and for even N=2q,

    S_N=1−2Σ_(r=1)^(q−1) cos(2rθ)/(4r²−1)−cos(Nθ)/(N²−1).

The tails telescope since 2/(4r²−1)=1/(2r−1)−1/(2r+1). Thus

    |S_N−(π/2)sinθ| ≤ 1/N  (N odd),
    |S_N−(π/2)sinθ| ≤ N/(N²−1)  (N even).

At an interior node sinθ_k≥2/N. The error is therefore at most (2/3)sinθ_k for all N≥2 (the even worst case is N=2; the odd bound is 1/2). Since π/2−2/3≥1/2 and π+4/3<5,

    sinθ_k/N ≤ w_k ≤5sinθ_k/N.                         (1)

At the endpoints the same finite telescoping sums give w_0=w_N=1/N² for odd N, and 1/(N²−1) for even N. Also sinθ_k≥2min(k,N−k)/N. Hence, including endpoints,

    w_k ≥ m_k/N².                                    (2)

### 2. Cardinal domination and cell masses

The nodal polynomial (1−x²)T_N′(x) gives

    ℓ_k(cosθ)= (−1)^(k+1) sinθ sin(Nθ) /
               [c_k N(cosθ−cosθ_k)],

with continuous extension at a node. Since

    sinθ ≤2sin((θ+θ_k)/2),
    |sin((θ−θ_k)/2)|≥|θ−θ_k|/π,

the absolute value is at most min(π,1/|t−k|), where t=Nθ/π; here |sin(Nθ)|≤min(1,N|θ−θ_k|). It follows that

    |ℓ_k(cosθ)|≤(π+1)/(1+|t−k|).                     (3)

Partition [0,π] into cells E_j where |t−j|≤1/2, truncating at endpoints. On E_j, (3) is at most D/(1+|j−k|), D=2(π+1). Moreover sinθ≤πm_j/N and the cell length is at most π/N, so

    ∫_(E_j)sinθ dθ ≤π²m_j/N².                        (4)

### 3. Weighted Schur bound

Let A_jk=1/(1+|j−k|), B_jk=√(m_j/m_k) A_jk, and h_j=m_j^−1/2. Its weighted row sums satisfy

    Σ_k B_jk h_k/h_j = m_j Σ_k A_jk/m_k
       ≤Σ_k A_jk +Σ_k 1/m_k
       ≤h_N+2H_(floor(N/2)+1),

because m_j≤m_k+|j−k| and each distance to the nearer endpoint occurs at most twice. Its weighted column sums satisfy

    Σ_j B_jk h_j/h_k =Σ_j A_jk≤h_N.

For completeness the nonnegative-matrix Schur inequality follows from
`(Σ B_jk z_k)² ≤(Σ B_jk h_k) Σ B_jk z_k²/h_k`, then summing in j and applying the column bound. Thus

    ||B||₂²≤h_N(h_N+2H_(floor(N/2)+1)).

For v_k=p(x_k), combine interpolation, (3), (4) and this bound:

    ∫p² ≤(π²D²/N²) Σ_j m_j(Σ_k A_jk|v_k|)²
         ≤K_N Σ_k (m_k/N²)|v_k|² ≤K_N Q_N(p²),

using (2). Finally H_s≤1+log s proves the stated logarithmic order.

## Scope

This proves the desired lower order for all N, including the full interpolation space. It does not estimate the upper spectrum or yield the optimal endpoint asymptotic constant.

## Open items

Independent mathematical acceptance and full historical duplicate screen. Improve constants only if scientifically useful; the explicit matching upper order is split into PD-T018.

## History

2026-10-31, Codex subagent mathematical development, gpt-6.1-sol xhigh (explicit orchestrator assignment), rules/base SHA above. The supplied matrix-entry hypothesis was replaced by a separately derived cardinal-cell argument. No private text copied.

2026-10-31, audit-01 L3 response, Codex gpt-6.1-sol xhigh (explicit assignment), rules `6d10a82cf6fd6f7ef6fbe76e68133ccbcbe51994`: the original consequent stated only λ_min(CC,N−1)≥1/K_N although the unchanged inequality and proof cover Π_N. Stated λ_min(CC,N)≥1/K_N explicitly and retained the degree-N−1 consequence by restriction. Status remains PROVED.
