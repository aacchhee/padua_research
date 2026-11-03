# paige-2010-augmented — addendum (padua-literature-20261103, P3)

Addendum to `literature/records/paige-2010-augmented.md`. C. C. Paige, An augmented stability result for the Lanczos Hermitian matrix tridiagonalization process, SIAM J. Matrix Anal. Appl. 31(5) (2010) 2347–2359, [doi:10.1137/090761343](https://doi.org/10.1137/090761343); author PDF https://www.cs.mcgill.ca/~chris/pub/Pai10.pdf.

- Access and reading date: 2026-11-03 (author PDF, pdf.js in the built-in browser).
- Reading coverage: exact pages 2347–2349 (abstract, §1), 2350–2351 (Theorem 2.1, Corollary 2.2 start), 2351–2354 (§3.1 basic rounding-error relations (3.1)–(3.6), §3.2 start, Theorem 3.1 with (3.15)–(3.19)), 2355–2358 (Corollaries 3.2–3.4, §3.4 comments), reference list. Proof of Theorem 3.1 skimmed only.
- Reader, model and effort: P3 literature reader, Claude Opus 5.5 (claude-opus-5-5), high.
- Named gaps: §3.3 eigenproblem remarks in full.

## Extracted published statements

### LIT?padua-literature-claude-62 — Theorem 3.1 and Corollaries 3.2–3.4: augmented (not standard) backward stability

- Statement in faithful paraphrase: Assume the computed Lanczos quantities satisfy AV_k = V_{k+1}T_{k+1,k} + E_k with unit-norm columns (3.2) and the derived upper-triangular relation with residual F_k (3.4), both of size O(ε)‖A‖ for a good implementation ((3.2), (3.5)). With S_k = (I + U_k)^{−1}U_k from the strictly upper part U_k of V_kᴴV_k and the unitary Q^{(k)} of Theorem 2.1, Theorem 3.1 states that Q^{(k)ᴴ}(diag(T_k, A) + H^{(k)})Q^{(k)} equals the bordered matrix with T_k, the coupling β_{k+1}v_{k+1}, and A_k = A minus a rank-two term, where H^{(k)} is Hermitian and ‖H^{(k)}‖ ≤ 4(‖E_k‖ + ‖F_k‖) (3.15)–(3.19). Corollary 3.2: the columns of the first block of Q^{(k)} with q_{k+1} are the exact Lanczos vectors, with the computed T_{k+1,k}, for the matrix diag(T_k, A) + H^{(k)} (3.24)–(3.25). Corollary 3.4: those columns are an orthonormal basis of the k-th Krylov space of diag(T_k, A) + H^{(k)} with start vector (0, v₁). The introduction stresses that the Lanczos process is not backward stable in the standard sense, so this augmented result cannot be turned into standard backward stability (pp. 2347–2348).
- Hypotheses and notation: one Hermitian A, one unit start vector; results stated in terms of E_k, F_k so that any rounding bound can be inserted (p. 2352).
- Page / theorem / equation: Theorem 2.1 p. 2350; §3.1 pp. 2351–2352; Theorem 3.1 pp. 2353–2354; Corollaries 3.2–3.4 pp. 2355–2357; §3.4 p. 2358.
- Reading evidence and limitations: statements read; proof not checked.
- Relation to campaign claims (no inherited proof status): the computed vectors are exact Lanczos vectors of an augmented problem in which T_k itself appears; the paper gives no bound on the distance between the span of the computed vectors and the Krylov space of A (consistent with LIT-254). One operator.

## Corrections and upgrades (old → new)

- LIT-254: WebFetch digest → verified against the author PDF, Theorem 3.1 pp. 2353–2354, Corollaries 3.2–3.4 pp. 2355–2357; add: the paper explicitly states (p. 2348) that the result cannot be transformed into standard backward stability. UNVERIFIED → verified.

## History

2026-11-03: addendum by the P3 reader (Claude Opus 5.5 high), padua-literature-20261103.
