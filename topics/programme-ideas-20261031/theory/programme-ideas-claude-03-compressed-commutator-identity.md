# PD-T?programme-ideas-claude-03 — Compressed commutator of a commuting pair on a graded Krylov space equals minus the boundary-block skew product

ID kind: PD-T.
Aliases: basis-invariant commutator block identity (gen3-1 adversary, (iii)); [Q_nᴴXQ_n, Q_nᴴYQ_n] = −(B_xᴴB_y − B_yᴴB_x).
Split from: `checks/adversarial-gen3-1.md` (iii), first bullet, at `614709d`: the identity **and** the clause "nonzero whenever K_n ≠ ℂ^M". Only the identity is retained; the nonvanishing clause is withdrawn (audit-01 A9.5).
Split into: none.

## Statement

Let X, Y be commuting Hermitian M × M matrices (e.g. diagonal node matrices), v ∈ ℂ^M, and for d ≥ 0 let K_d = span{X^a Y^b v : a + b ≤ d}. Let Q_n have orthonormal columns spanning K_n, ordered by degree blocks, and Q′ orthonormal columns spanning K_{n+1} ⊖ K_n. Put B_x := Q′ᴴ X Q_n and B_y := Q′ᴴ Y Q_n (their only nonzero columns are those of the degree-n block, since X K_{n−1} ⊂ K_n). Then

  [Q_nᴴ X Q_n, Q_nᴴ Y Q_n] = −(B_xᴴ B_y − B_yᴴ B_x),

which is supported in the degree-n diagonal block. Its Frobenius and spectral norms are invariant under unitary changes of coordinates of ℂ^M and of the orthonormal basis of each degree block.

## Definitions

P = Q_nQ_nᴴ, P^⊥ = I − P. For a discrete measure with nodes z_i and weights w_i, X = diag(x_i), Y = diag(y_i), v = (√w_i), and Q_nᴴXQ_n, Q_nᴴYQ_n are the degree-n sections.

## Assumptions

Exact arithmetic; X, Y Hermitian and commuting. No assumption on the node geometry.

## Status by part

Overall status: PROVED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| identity and block support | PROVED | proof below; MEASURED agreement ≤ 8e-15 (≤ 2e-12 where conditioning is large) for rhodonea k = 7, a generic degree-4 curve and Lissajous (5,6), M = 64, 128, 512, n ≤ 8 (`checks/code/adv/gen3-1/commutator_sections.py`, `commutator_out.txt`); independent QR replay by the Codex audit (rhodonea-7, M = 64: norms 0.25, 0.375, 0.0833333, 0.2414547 for degrees 1–4, agreement 1.67e-16) |
| basis invariance | PROVED (routine) | unitary invariance of the norm |

Withdrawn clause ("nonzero whenever K_n ≠ ℂ^M"): not a theorem. Properness of K_n does not force a nonzero commutator (degree 0 gives scalars; Y = cI gives zero at every degree). Only the measured nonzero instances above are retained.

Minor classification: kept as its own record because `report.md` §3 at `614709d` reported it on its own as a lemma for transfer to (b) L3; it is a routine two-line identity.

## Depends on

None.

## Checks

As in the table. Commands: `python checks/code/adv/gen3-1/commutator_sections.py > checks/code/adv/gen3-1/commutator_out.txt` (frozen at `614709d`).

## Sources

The same block identity appears for the Lanczos sections' last block in `PD-T?bivariate-lanczos-claude-301`(a) (commutator vanishes outside block (n,n); pinned at `5f523313b7b388cb114103734028f0a850dfeaad`) and, for commuting extensions, in Degani–Schiff–Tannor 2005 Thm 2 (LITERATURE; primary excerpt checked by the audit). The explicit boundary-product form is stated here; no novelty is claimed.

## Proof or evidence

Q_nᴴXQ_nQ_nᴴYQ_n − Q_nᴴYQ_nQ_nᴴXQ_n = Q_nᴴ(XPY − YPX)Q_n. Since XY = YX, Q_nᴴ(XY − YX)Q_n = 0, so this equals −Q_nᴴ(XP^⊥Y − YP^⊥X)Q_n. Now P^⊥YQ_n has range in K_{n+1} ⊖ K_n, so P^⊥YQ_n = Q′Q′ᴴYQ_n = Q′B_y, and Q_nᴴXP^⊥ = (P^⊥XQ_n)ᴴ = B_xᴴQ′ᴴ. Hence Q_nᴴXP^⊥YQ_n = B_xᴴB_y and likewise for the swapped term. The columns of B_x, B_y of degree < n vanish because XK_{n−1}, YK_{n−1} ⊂ K_n. ∎

## Scope

Algebraic identity for exactly commuting X, Y. It does not say the commutator is nonzero, nor how large it is; it says that "Fourier-basis commutation" cannot remove it, since the norm is coordinate-invariant.

## Open items

None.

## History

- 2026-11-01, gen3-1 adversarial agent (claude-fable-5-1, xhigh): identity, basis invariance and the nonvanishing clause.
- 2026-11-01, Codex audit-01 A9.5 / rejections-review R2: nonvanishing clause is false as stated; identity confirmed.
- 2026-11-01, response-01 (claude-opus-5-5, effort not exposed): clause struck in the source (original kept), record created with the identity only.
