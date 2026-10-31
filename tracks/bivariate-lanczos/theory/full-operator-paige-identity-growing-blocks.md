# PD-T?bivariate-lanczos-claude-103 — Growing-block Paige identity for a (complex) symmetric diagonal operator with a computed Krylov-type relation; specialisations to F, J and N = J + iF

ID kind: PD-T.
Aliases: block Paige identity with growing blocks; per-operator Paige identity for the full operator; bilinear (complex-symmetric) Paige identity for X + iY; "Paige identity with commutator term".
Split from: none.
Split into: none (the commutator residual that enters the J- and N-specialisations is PD-T?…-104).

## Statement

[EXACT algebra on computed quantities] Let A ∈ C^{M×M} be diagonal (hence complex symmetric, Aᵀ = A), Q̂ ∈ R^{M×m}, Q̂_+ ∈ R^{M×q}, and let T ∈ C^{m×m}, B ∈ C^{q×m}, E ∈ C^{M×m} be **any** matrices with

  A Q̂ = Q̂ T + Q̂_+ B + E.   (R)

Write C = Q̂ᵀQ̂ = I + Δ + R + Rᵀ (Δ diagonal, R strictly upper triangular), c = Q̂ᵀQ̂_+, S = (T + Tᵀ)/2, K = (T − Tᵀ)/2, G = C − I, and let b be the bandwidth of S (S_{kl} = 0 for |k − l| > b). Let R_loc be the part of R with 0 < l − k ≤ b, and assume B vanishes outside its last r columns; let c_loc be the last r rows of c. Define

  Φ := EᵀQ̂ − Q̂ᵀE − 2K − GK − KG,  X_loc := R_loc S − S R_loc,
  Ω := low(X_loc) + low(X_loc)ᵀ + dg(X_loc) − up(ΔS − SΔ) + up(Bᵀcᵀ) + lowd(cB) + up(Φ),

with up/low the strictly upper/lower parts, dg the diagonal and lowd the lower part including the diagonal. Then:

1. **(Identity.)** For every s ∈ C^m and θ ∈ C, with ρ := Ss − θs,
   sᵀ c B s = sᵀ Ω s − sᵀ (R − Rᵀ) ρ.
2. **(Locality of Ω.)** up(Bᵀcᵀ) and lowd(cB) depend on c only through c_loc; the first three terms of Ω depend on R only through R_loc; and
   ‖Ω‖₂ ≤ 6‖S‖₂‖R_loc‖_F + 2‖Δ‖₂‖S‖_F + 2‖B‖₂‖c_loc‖_F + 2‖E‖_F‖Q̂‖₂ + (2 + 2‖G‖₂)‖K‖_F.
3. **(Ritz-type corollary.)** For unit s (Euclidean norm), y := Q̂ s and any θ,
   |(Q̂_+ᵀ y)ᵀ (B s)| ≤ ‖Ω‖₂ + 2‖R‖₂ ‖(S − θ)s‖,
   so the component of the new block along y in the (bilinear) direction Bs is bounded by (‖Ω‖₂ + 2‖R‖₂‖ρ‖)/‖Bs‖, and ‖Q̂_+ Bs‖ ≤ ‖Ay − θy‖ + ‖Q̂‖₂(‖ρ‖ + ‖K‖₂) + ‖E‖₂ (B s is the boundary part of the residual).

Specialisations (with the window recurrence of PD-T?…-101/-102, n ≥ 1, Q̂ = Q̂_{n−1}, Q̂_+ = block n, q = n+1, r = n):

- **F (full operator).** A = F, T = T_F^{sq}, B = B_F (computed coefficients), E = E_F (local rounding only). All terms of Ω are local (window Gram entries, normalisation errors, local rounding, coefficient asymmetry) apart from the second-order product G·K. The corollary holds for **every** approximate eigenvector of the F-section, in particular for the Ritz vectors of the joint section Z (ρ = residual of s for S).
- **J (injecting operator).** A = J, T = P(Ĥ_J)^{sq}, B = P(Ĥ_J)[block n, :] with Ĥ_J the implicit J-section built from the computed coefficients (PD-T?…-104) and P the restriction to the exact-arithmetic support pattern of PD-T?…-101 part 3 (the recursion with computed coefficients also produces tiny entries outside that pattern; they are moved into E so that S keeps bandwidth b), and E = C_res + Q̂_n(Ĥ_J − P(Ĥ_J)), C_res := J Q̂_{n−1} − Q̂_n Ĥ_J (the commutator residual). Ω contains 2‖E‖_F‖Q̂‖₂, which is not a local rounding quantity.
- **N = J + iF (joint, bilinear).** A = X + iY (complex symmetric), T = P(Ĥ_J)^{sq} + i T_F^{sq}, B = P(Ĥ_J)[block n,:] + i B_F, E = (J-part of E) + i E_F. With s an eigenvector of the complex-symmetric S (normalised in the Euclidean norm; the identity is bilinear, no conjugation) this is the Paige identity for the joint Ritz pairs that HL SIMAX p. 1088 alludes to; its error term carries the commutator residual.

## Definitions

Bilinear form uᵀv without conjugation throughout. Bandwidth of the F-section with the exact window: b ≤ n (entries between (t, j) and (t+1, r ≤ j+1) are at index distance t + 2 + r − j − 1 ≤ t + 2, t ≤ n − 2); with the block window b ≤ 2n − 2.

## Assumptions

None beyond (R) for parts 1–3 (pure algebra). The specialisations assume the computed relations of PD-T?…-102 and, for J and N, the analysis objects of PD-T?…-104.

## Status by part

Overall status: PROVED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| 1. identity | PROVED | proof below; numerical check `l1_identities.py` (R02) |
| 2. locality and norm bound | PROVED | proof below |
| 3. corollary | PROVED (routine from 1.–2.) | |
| F, J, N specialisations | PROVED (substitution) | sizes of the terms MEASURED in R02 |
| "the error term is small" for J and N | not claimed here | depends on ‖C_res‖ (PD-T?…-104: exact recursion PROVED; growth MEASURED) |

## Depends on

PD-T?…-102 (relation (R) for F with computed coefficients); PD-T?…-104 (C_res, Ĥ_J) for the J- and N-specialisations. Literature: the scalar identity is Paige's (LIT?bivariate-lanczos-claude-004, as reported; not inspected); the block form is reported for fixed/shrinking blocks in sinha-2026 (abstract-level, LIT?…-018). Neither is used as a dependency; the proof below is self-contained.

## Checks

`tracks/bivariate-lanczos/code/L1/l1_identities.py` evaluates the identity (*) below and part 1 at rounding level for F, and the N-specialisation, on random, rotated and tensor sets (R02 log `topics/bivariate-lanczos-20261031/directions/L1/logs/r02_identities.log`).

## Proof or evidence

*Step 1.* Since A is diagonal, Q̂ᵀAQ̂ is (complex) symmetric. Multiplying (R) by Q̂ᵀ: Q̂ᵀAQ̂ = CT + cB + Q̂ᵀE, so (*) CT + cB + Q̂ᵀE = TᵀC + Bᵀcᵀ + EᵀQ̂.
*Step 2.* With T = S + K and C = I + G: CT − TᵀC = (CS − SC) + (CK + KC) = [G, S] + 2K + GK + KG. Hence [G, S] = Bᵀcᵀ − cB + Φ. With G = Δ + R + Rᵀ and X := RS − SR one has [Rᵀ, S] = −Xᵀ, so
  X − Xᵀ + [Δ, S] = Bᵀcᵀ − cB + Φ.   (1)
*Step 3.* All terms of (1) are antisymmetric. Taking strictly upper parts, up(X) − low(X)ᵀ + up([Δ,S]) = up(Bᵀcᵀ) − up(cB) + up(Φ). Writing X = up(X) + dg(X) + low(X) and up(cB) = cB − lowd(cB):
  X = low(X) + low(X)ᵀ + dg(X) − up([Δ,S]) + up(Bᵀcᵀ) + lowd(cB) − cB + up(Φ).   (2)
*Step 4 (locality).* For k ≥ j, (RS)_{kj} = Σ_{l>k} R_{kl}S_{lj} needs l − j ≤ b, hence 0 < l − k ≤ b; (SR)_{kj} = Σ_{l<j} S_{kl}R_{lj} needs k − l ≤ b, hence 0 < j − l ≤ b. Hence low(X) + dg(X) = low(X_loc) + dg(X_loc). Substituting into (2) gives X = Ω − cB. B vanishes outside its last r columns, so cB vanishes outside the last r columns and lowd(cB)_{kj} ≠ 0 only for k ≥ j ≥ m − r + 1, involving rows k of c in the last r rows; Bᵀcᵀ vanishes outside the last r rows and up(Bᵀcᵀ)_{kj} ≠ 0 only for m − r + 1 ≤ k < j, involving (cᵀ)_{·j} = row j of c, again in the last r rows. So these terms depend only on c_loc.
*Step 5 (identity).* For any s and θ, since S is symmetric, sᵀXs = sᵀRSs − (Ss)ᵀRs = sᵀR(θs + ρ) − (θs + ρ)ᵀRs = sᵀRρ − ρᵀRs = sᵀ(R − Rᵀ)ρ. Combining with X = Ω − cB gives part 1.
*Step 6 (bound).* ‖low(X_loc)‖ + ‖low(X_loc)ᵀ‖ + ‖dg(X_loc)‖ ≤ 3‖X_loc‖_F ≤ 6‖S‖₂‖R_loc‖_F; ‖up(ΔS − SΔ)‖_F ≤ 2‖Δ‖₂‖S‖_F; ‖up(Bᵀcᵀ)‖_F + ‖lowd(cB)‖_F ≤ 2‖B‖₂‖c_loc‖_F; ‖up(Φ)‖_F ≤ ‖Φ‖_F ≤ 2‖E‖_F‖Q̂‖₂ + (2 + 2‖G‖₂)‖K‖_F. (Spectral ≤ Frobenius for each piece.)
*Step 7 (corollary).* sᵀcBs = (cᵀs)ᵀ(Bs) = (Q̂_+ᵀy)ᵀ(Bs); |sᵀΩs| ≤ ‖Ω‖₂ and |sᵀ(R − Rᵀ)ρ| ≤ 2‖R‖₂‖ρ‖ for ‖s‖ = 1. Finally Ay − θy = Q̂(T − θ)s + Q̂_+Bs + Es = Q̂(ρ + Ks) + Q̂_+Bs + Es.
*Specialisations.* Substitute the relations of PD-T?…-102 (F) and PD-T?…-104 (J: J Q̂_{n−1} = Q̂_n Ĥ_J + C_res exactly, by definition of C_res), and add them with weights 1 and i for N.

## Scope

The identity controls, for each approximate eigenvector s of the section, **one** (bilinear) combination of the n+1 components Q̂_+ᵀy of the new block along y — the combination weighted by the boundary vector Bs — exactly as in fixed-block block Lanczos; it does not bound the remaining n components. For F all error terms are local; this is the per-operator theory that transfers (PD-T?…-401, Transfer 1). For J and N the error term contains the commutator residual, so these identities are Paige-like only while ‖C_res‖ stays at rounding level.

## Open items

(i) A priori bounds on R_loc and c_loc for BJ (CGS); for HL they are the twice-is-enough local level (as reported). (ii) Whether the uncontrolled n components of Q̂_+ᵀy matter: R02 measures the fraction |⟨Q̂_+ᵀy, Bs/‖Bs‖⟩| / ‖Q̂_+ᵀy‖. (iii) Size of C_res (PD-T?…-104).

## History

- 2026-10-31: created (Claude Opus 5.5, xhigh; L1 R02).
