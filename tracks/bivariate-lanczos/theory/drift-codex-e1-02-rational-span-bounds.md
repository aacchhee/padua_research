# PD-T?drift-codex-02 — Rational lower and upper certificates for aggregate span sensitivity

ID kind: PD-T.
Aliases: node-impulse lower bound; trace upper bound; independent-node upper bound; quotient gain certificate.
Split from: E1's combined sensitivity-and-separation target (comparison remains OPEN).
Split into: none.

## Statement

Use PD-T?drift-codex-01, fix a stage s, and let J be a nonempty subset of source columns 1,...,N_s-1. Put sigma_h^2=||A_h b_p(h)||_2^2>0. Restrict f_h=0 for h outside J and equip the remaining injections with

    ||f||_src^2=sum_(h in J) ||f_h||_2^2/sigma_h^2.

The actual spectral-output condition number is

    kappa_s(J)=sup_(||f||_src=1) ||T_s(f)||_2.

For each source h and node i define the nonnegative rational quantities

    v_hi=sigma_h^2 sum_(k=h)^(N_s-1) g_kh(z_i)^2/d_k,
    ell_hi=(1-P_s,ii) v_hi.

Then

    L_s^2=max_(h in J,i) ell_hi <= kappa_s(J)^2
        <= min(H_s^2,U_s^2),
    H_s^2=sum_(h in J,i) ell_hi,
    U_s^2=max_i sum_(h in J) v_hi.

All squared endpoints are rational on rational nodes, and all ordering/ratio decisions between these squared endpoints can be checked with exact integer cross-multiplication. This gives a certified interval for kappa, without claiming that either endpoint equals it.

## Definitions

L_s is the maximum gain of a single node/source impulse. H_s is the Hilbert–Schmidt norm of the derivative as a map to Frobenius output. U_s is a rowwise trace upper bound before the final orthogonal projection. The Frobenius output condition number is different from kappa_s, although the norms are equivalent within sqrt(N_s). The formulas above bound the spectral-output condition number itself.

## Assumptions

Exactly those of PD-T?drift-codex-01. All-source sensitivity uses J={1,...,N_s-1}. Degree-two sources J={h:deg h=2} define a restricted screen; their lower bounds also bound the full condition, but their upper bounds do not upper-bound the full condition.

## Status by part

Overall status: PROVED (analytic; Claude audit-01: CONFIRMED; Codex re-audit pending).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Bounds and rational finite-check reduction | PROVED | Explicit proof below |

Candidate / claim disposition: retained. Tightness and finite separation are separate computational obligations.

## Depends on

PD-T?drift-codex-01, with its precise aggregate-injection model and fixed choices.

## Checks

Actual checker paths, outputs and hashes belong in E1.md and the separate finite-certificate record. No computation or independent rerun is claimed by this analytic result.

## Sources

PD-T041 is the exact impulse-response predecessor. No historical novelty claim; Frobenius domination and single-column lower bounds are standard norm arguments written here for the precise quotient operator.

## Proof or evidence

Write f_h=sigma_h u_h, so the source budget is sum_h||u_h||_2^2=1. The unit source coordinate u_h=e_i produces output

    sigma_h (R_s e_i) [g_0h(z_i)/sqrt(d_0),...,g_(N_s-1),h(z_i)/sqrt(d_(N_s-1))].

This has rank at most one. Its squared spectral and Frobenius norms agree and equal sigma_h^2 ||R_s e_i||_2^2 sum_k g_kh(z_i)^2/d_k. Since R_s is an orthogonal projector, ||R_s e_i||_2^2=R_s,ii=1-P_s,ii. Maximizing gives L_s.

For an arbitrary linear map between Euclidean spaces, its operator norm is at most its Hilbert–Schmidt norm. View the output as a Euclidean vector using its Frobenius norm and then use spectral norm <= Frobenius norm. Summing the squared output norms of the orthonormal input coordinates (h,i) gives exactly H_s^2. This proves the first upper bound.

For the second upper bound, let W be the unprojected normal-coordinate matrix with W_ik=sum_h sigma_h g_kh(z_i)u_hi/sqrt(d_k). For each fixed i, its row is C_i u_i, where (C_i)_kh=sigma_h g_kh(z_i)/sqrt(d_k) and u_i=(u_hi)_h. Thus

    ||T_s(f)||_2 <= ||R_s W||_F <= ||W||_F
      <= max_i ||C_i||_2 (sum_i||u_i||_2^2)^(1/2)
      <= max_i ||C_i||_F = U_s.

The formulas use only squares, d_k, sigma_h^2 and the rational diagonal of P_s. Rationality and exact cross-multiplication follow.

## Scope

Large L_s proves an amplification capacity attained to first order by a specified residual pulse. It is not a lower bound on drift for all f, random f, or actual rounding errors. An overlap of [L_s,min(H_s,U_s)] across selections is INCONCLUSIVE. A ratio of lower bounds alone cannot disprove or prove a ratio of the actual conditions.

## Open items

Tighter certified upper bounds if the row traces are too pessimistic. One option is an exact positive-semidefinite check: writing G_i=(g_kh(z_i)) and S=diag(sigma_h^2), the rational matrix lambda S^(-1)-G_i^T D_s^(-1)G_i being positive semidefinite for every i implies kappa_s^2<=lambda. This follows from the rowwise argument above; implementation and any finite certificate are not asserted here.

## History

- 2026-11-01: Codex mathematics developer; requested gpt-6.1-sol xhigh allocation, runtime metadata unexposed. Node/HS setup sent before computation; independent-node tightening sent before receiving results. Frozen comparison thresholds unchanged.
- 2026-11-01 (Claude response-01, Sonnet 5.5): E1-F4: the statement about the Urow tightening reconciled with `evidence/e1-freeze.json`, which records the Urow bound as added "after initial n2 restricted-source run" (present already in the earliest committed freeze 6920ba6 under `frozen_before_run`), at a time not separately logged; "before receiving results" is therefore dropped as unverifiable (details: `directions/E1.md`, Response-01 annotations); original wording: «Node/HS setup sent before computation; independent-node tightening sent before receiving results.»
- 2026-11-01 (Claude response-01, Sonnet 5.5): status line updated for audit-01 (status PROVED unchanged); original wording: «Overall status: PROVED (analytic; independent audit pending).»
