# PD-T?bivariate-lanczos-claude-505 — Unisolvent-prefix orders exist (greedy extension lemma)

Final ID: **PD-T080** (allocated at PR preparation, 2026-11-01; the provisional ID above and in the text is retained as provenance — see ID_CROSSWALK.md).

ID kind: PD-T.
Aliases: extension lemma; prefix-aware deferral completes; GEPP order; IDEA?bivariate-lanczos-claude-504 (support).
Split from: none.
Split into: none.

## Statement

[EXACT] Let z_1, …, z_N be distinct points of ℝ² with N = (n+1)(n+2)/2 that are unisolvent for Π_n (the N×N matrix V = [m_j(z_i)], with m_1, …, m_N the graded monomials 1, x, y, x², xy, y², … of total degree ≤ n, is nonsingular). For a subset S of the nodes with |S| = K < N, call S a *unisolvent K-prefix* if the K×K matrix [m_j(z)]_{z∈S, j≤K} is nonsingular. Then:

(i) If S is a unisolvent K-prefix, there is a node z ∉ S such that S ∪ {z} is a unisolvent (K+1)-prefix. More precisely, with B the K×K block, S_c = E − D B⁻¹ C the Schur complement of B in V (rows ordered S first), the candidate z_ℓ is admissible iff the ℓ-th entry of the first column of S_c is nonzero, and max_ℓ |(S_c e_1)_ℓ| ≥ σ_min(S_c)/√(N−K) > 0.

(ii) Hence every unisolvent K-prefix extends to a full ordering z_{π(1)}, …, z_{π(N)} of the nodes all of whose prefixes are unisolvent; in particular such orders exist (K = 0 start), and the order selected by Gaussian elimination with partial pivoting on V (or on any matrix V·T with T upper triangular nonsingular, e.g. the orthogonal product-Chebyshev matrix) is one.

## Definitions

Prefix, graded monomial order: as in the statement. Unisolvent prefix is independent of any weights and of any triangular change of the monomial basis that preserves the flag Π^{(1)} ⊂ Π^{(2)} ⊂ … (e.g. T_a(x)T_b(y) in place of x^a y^b).

## Assumptions

Only the unisolvence of the full node set and exact arithmetic.

## Status by part

Overall status: PROVED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (i) one-step extension | PROVED | Schur complement argument below |
| (ii) existence of all-prefix-unisolvent orders; GEPP order | PROVED | induction on (i); for GEPP, pivots of Gaussian elimination without breakdown are the quotients of leading minors |

Candidate / claim disposition: not applicable.

## Depends on

None.

## Checks

Numerical illustration (MEASURED, not part of the proof): for Padua n = 10..50 the GEPP order and the randomised threshold-pivoting order (`prefix.py`) have, among the refined/scanned prefixes, smallest numerical σ_min estimates (floating point, not certificates) of the prefix blocks of the orthogonal Chebyshev matrix between 4.7e-4 and 1.3e-1 (R01 logs `r01_prefix_*.jsonl`), i.e. all prefixes numerically unisolvent with a visible margin; the greedy-by-threshold *online* variant with the pivot detector is tested in R03 and is not covered by this lemma.

## Sources

None (elementary linear algebra).

## Proof or evidence

Order the nodes so that S comes first, and write V = [[B, C],[D, E]] with B = V[1:K,1:K] nonsingular, C = V[1:K, K+1:N], D = V[K+1:N, 1:K], E = V[K+1:N, K+1:N]. Since V is nonsingular and det V = det B · det S_c, the Schur complement S_c = E − D B⁻¹ C ∈ ℝ^{(N−K)×(N−K)} is nonsingular, so its first column s = S_c e_1 ≠ 0 and ‖s‖₂ ≥ σ_min(S_c). For a candidate z_ℓ among the remaining nodes (row ℓ of [D E]) and the next monomial m_{K+1} (column 1 of [C; E]), the (K+1)×(K+1) prefix matrix is [[B, c],[d_ℓ, e_ℓ]] with c = C e_1, d_ℓ = row ℓ of D, e_ℓ = E_{ℓ1}, and det = det B · (e_ℓ − d_ℓ B⁻¹ c) = det B · s_ℓ. Hence z_ℓ is admissible iff s_ℓ ≠ 0, some s_ℓ ≠ 0 exists, and max_ℓ|s_ℓ| ≥ ‖s‖₂/√(N−K) ≥ σ_min(S_c)/√(N−K). This is (i). (ii) follows by induction from the empty prefix (K = 0, B empty, det B = 1); a change of basis V → V T (T upper triangular nonsingular) multiplies every leading minor by the nonzero product of the leading diagonal entries of T, so the prefix property is basis-independent, and in Gaussian elimination with partial pivoting on a nonsingular matrix the pivot chosen in column k is the largest |s_ℓ| in the Schur-complement column, which is nonzero by (i), so the elimination never breaks down and the selected rows form an all-prefix-unisolvent order. ∎

## Scope

An existence statement for exact arithmetic. It does not say how large the smallest prefix singular value must be, nor that a *cheap online* test finds an admissible node (the measured detector `min_j |pivot_j| < 1e-10` in R03 is a separate MEASURED claim), and the bound σ_min(S_c)/√(N−K) is not claimed to be uniform in n.

**Scope notes added after reconstruction 01 (CONFIRMED, findings L3).** (a) The order produced by floating-point GEPP (scipy `getrf`) is an exact-arithmetic GEPP order only up to near ties; its use as 'all prefixes unisolvent' in measured claims rests on the numerical σ_min estimates of `prefix.py` (earlier wording: 'numerical certificate') and the reviewer's independent LU-based numerical lower estimates (smallest 6.5e-5 (n = 30), 2.4e-5 (n = 40), 1.2e-5 (n = 50) on the reviewer's orthonormal matrix; Codex audit-01's all-prefix LU lower estimate for the developer's GEPP order at n = 50 is 1.1564e-5 with max-entry factorization residual 4.62e-15), not on this lemma. All of these are floating-point estimates, not exact or interval certificates (audit-01 L5 M2). (b) For M > N (random nodes, where Algorithm 1 uses M graded monomials beyond degree n) the proof carries over verbatim whenever the M×M matrix of the nodes against the first M graded monomials is nonsingular (generic, not guaranteed); the lemma as stated is for N = dim Pi_n.

## Open items

Quantitative growth of the best achievable min_K σ_min(prefix block) over orders (Lebesgue-constant-type quantity); a proof that the online pivot detector is exact in exact arithmetic is OPEN (R03, gap described there).

## History

2026-10-31, Claude Sonnet 5.5 (high), L5 R03: created.

2026-10-31T22:58Z, Claude Sonnet 5.5 (high), response to L5 reconstruction 01: finding L3 and the M > N scope note added. Reconstruction verdict: CONFIRMED.

2026-11-01T08:22:09+01:00, Claude Sonnet 5.5 (high), response to Codex audit-01 (L5) finding **M2**. The lemma, its statement and its proof are unchanged (audit-01 accepts T505 as PROVED within scope); status unchanged (PROVED). Terminology in the two non-proof remarks changed: "all prefixes unisolvent with a visible margin" became "all prefixes numerically unisolvent ... (floating point, not certificates)"; "rests on the numerical certificate of `prefix.py` (and the reviewer's independent LU-based lower bounds, certified min sigma_min >= 6.5e-5 (n = 30), 2.4e-5 (n = 40), 1.2e-5 (n = 50) ...)" became "numerical σ_min estimates ... LU-based numerical lower estimates (smallest ...)"; added the audit's all-prefix LU lower estimate 1.1564e-5 (residual 4.62e-15) and the statement that none is an exact or interval certificate.
