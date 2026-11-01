# PD-T?bivariate-lanczos-claude-106 — Exact ω-recurrence of the window recurrence, with local-rounding sources for F-products and commutator sources for J-products

Final ID: **PD-T034** (allocated at PR preparation, 2026-11-01; the provisional ID above and in the text is retained as provenance — see ID_CROSSWALK.md).

ID kind: PD-T.
Aliases: 2D ω-recurrence; Simon-type recurrence for the window recurrence; commutator-defect ω-recurrence (IDEA?…-008 made exact); loss-source identity.
Split from: none.
Split into: none.

## Statement

[EXACT algebra on computed quantities] With the notation of PD-T?…-102/-104, ω_{ab} := q̂_aᵀq̂_b, T_F the computed F-coefficients, E_F := F Q̂ − Q̂ T_F, T_J := Ĥ_J and E_J := C_res (PD-T?…-104): for every column k ≥ 1 with parent p = p(k), operator A_k ∈ {F, J}, and every l < k of degree ≤ n−1,

  β_k ω_{lk} = Σ_r (T_{A_k})_{rl} ω_{rp} + (E_{A_k} e_l)ᵀ q̂_p − Σ_{l′∈W_k} (h_k)_{l′} ω_{ll′} − q̂_lᵀ f_k.

The **sources** are s_{lk} := (E_{A_k} e_l)ᵀq̂_p − q̂_lᵀf_k: for F-products they consist of local rounding only (E_F, f); for J-products, (C_res e_l)ᵀq̂_p enters in addition. For l outside the window W_k the first sum involves only ω_{rp} with r of degree ≤ deg(l)+1 ≤ deg(k) − 2, i.e. older entries of the Gram matrix [correction 2026-10-31, recon-01 minor: the inequality deg(l)+1 ≤ deg(k) − 2 holds for the block window (BJ) only. For the exact window (HL) an l = (t−2, i < j−2) lies outside W_k with deg(l)+1 = t−1. The conclusion still holds, because those ω_{rp} have r and p of degree ≤ t−1 < t = deg(k), so they are older entries]: the identity is a linear recursion for the loss of orthogonality driven by these sources.

## Definitions

As in PD-T?…-102/-104.

## Assumptions

Those of PD-T?…-104. The relation A q̂_l = Q̂ T_A e_l + E_A e_l is used for l of degree ≤ n−1 (for F it is the computed relation of l's child; for J it is the definition of C_res).

## Status by part

Overall status: PROVED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| identity | PROVED | proof below; numerical check in long double: residual ≤ 1e-19 (R02 log `r02_identities.log`, "omega-recurrence sources") |
| interpretation of sources | PROVED (reading of the identity) | |
| sizes of sources vs loss — cross-reference, not a claim of this file | MEASURED in PD-T?…-107 (d) | [pointer corrected 2026-11-01T08:41:34+01:00; it read "MEASURED (PD-T?…-107 (e))"] |

## Depends on

PD-T?…-102, PD-T?…-104.

## Checks

`tracks/bivariate-lanczos/code/L1/l1_identities.py::omega_sources` (both sides in long double; per degree: loss outside the window split by F-/J-columns, propagation term, F-sources, J-commutator sources).

## Proof or evidence

From β_k q̂_k = A q̂_p − Q̂_W h − f: β_k q̂_lᵀq̂_k = q̂_lᵀAq̂_p − Σ_{l′}h_{l′}ω_{ll′} − q̂_lᵀf. Since A is symmetric (diagonal), q̂_lᵀAq̂_p = (Aq̂_l)ᵀq̂_p = (Q̂T_Ae_l + E_Ae_l)ᵀq̂_p = Σ_r (T_A)_{rl}ω_{rp} + (E_Ae_l)ᵀq̂_p.

## Scope

This is the exact counterpart of the ω-recurrence models (Simon 1984, Bai–Day–Ye 1999, as reported), not a first-order model: given the computed quantities it holds identically. It shows where a bivariate term enters the loss dynamics: only through the J-products, via the commutator residual. It does not by itself bound loss: the recursion's amplification must be controlled. R02 measurements show that on non-product supports the loss grows through the propagation term with sources at rounding level (PD-T?…-107 (e)), i.e. the instability is an amplification property of this recursion. Hand-off: this is the identity plan L2-Q1 asks to derive ("ω-recurrence from the L1 local relations").

## Open items

Bound the amplification of the recursion (equivalently of the node propagators of PD-T?…-104) in terms of computable quantities; product case: PD-T?…-105.

## History

- 2026-10-31: created (Claude Opus 5.5, xhigh; L1 R02).
- 2026-10-31T23:05Z (response to reconstruction 01): CONFIRMED by recon-01 (exact rational check, 155 pairs). The one wrong inequality for the exact window is corrected in place, with the original text kept.
- 2026-11-01T08:41:34+01:00 (Claude Opus 5.5, xhigh; response to Codex audit-01, consolidated item 5, stale pointers). The status row on the sizes of the sources pointed to PD-T?…-107 (e), which is the within-degree coupling. The source sizes are PD-T?…-107 (d), and the row is now relabelled as a cross-reference. Original row: "| sizes of sources vs loss | MEASURED (PD-T?…-107 (e)) | |". The identity and its status (PROVED) are unchanged.
