# MZ-CC restructuring plan (task 2)

Target: SIAM J. Numer. Anal. (`siamart251216`). arXiv and journal versions identical (AC, 2026-11-13). Long derivations go to appendices; no separate published supplement.

## Title and headline

**Title (proposal):** *Sharp Marcinkiewicz–Zygmund constants of Clenshaw–Curtis quadrature beyond half-exactness*.

**Headline:** for the Lebesgue Clenshaw–Curtis (CC) rule with N+1 Chebyshev extrema and its Gram matrix G_{N,n} on Π_n, beyond the half-exactness range n ≤ N/2:
1. a uniform upper bound λ_max(G_{N,n}) ≤ min{1+ρ_{N,n}, 5/3} for all n<N, and failure of any bound below two at n=N;
2. the sharp endpoint minimum: (log N)² λ_min(G_{N,N−1}) → π⁴/8, also on Π_N, with explicit all-N two-sided bounds;
3. the endpoint maximum: λ_max(G_{N,N−1}) → Λ_edge, an explicit endpoint-operator norm, with 1.0044369 ≤ Λ_edge ≤ 3/2;
4. consequences: (log N)²(1−η_N) → π⁴/8; κ_2(G_N) ~ (8Λ_edge/π⁴)(log N)²; explicit strong MZ constants at each fixed ratio n/N ≤ θ < 1; hyperinterpolation with factor (1+√(5/3))√2.

## Abstract (≈ 200 words, SIAM limit 250)

The problem, the four results above with their exact scope, one sentence on methods (sign structure of the Chebyshev mass matrices, a discrete Volterra/primitive estimate with a signed sinc remainder, an endpoint operator limit), and one sentence on prior work (qualitative full-space facts follow from classical weighted MZ results; no prior statement of these constants was found in a documented search). The decimal value of Λ_edge is not determined.

## Outline, location of each result, target length

Target: about 30–34 SIAM pages including appendices (current CC part is 16 A4 pages in `article`; SIAM's text block is narrower). AC: coherence and explanation before page count.

| § | Content | Results (IDs) | Source |
|---|---|---|---|
| 1 | **Introduction.** MZ constants and the half-exactness range; the CC setting and conventions (node index N, point count N+1, ADE d_N); main theorems stated up front: Thm 1.1 (upper bounds, 5/3, T_N obstruction), Thm 1.2 (π⁴/8 and explicit bounds), Thm 1.3 (Λ_edge), Cor 1.4 (defect, condition number, strong constants, hyperinterpolation). Relation to the literature (rewritten in task 5 after PR #21). Outline. | statements only | old §1 rewritten |
| 2 | **Preliminaries.** Chebyshev moments, exact CC identities (Lemma 2.1), weight comparison (Lemma 2.2, now with the explicit S_N error bound used later), mass floor (Lemma 2.3), cardinal formula (displayed), Gram/variational conventions, notation register summary. | PD-T013, PD-T015, weight lemma | old §2–3 |
| 3 | **Upper spectrum.** Sign argument: threshold below two (Thm 3.1); degree-sensitive bound 1+ρ (Thm 3.2, Cor 3.3); uniform bound 5/3 via the reflected completion R=M−H+K (Thm 3.4, new in text); the sign argument's boundary and T_N obstruction (Remark 3.5); historical 2−2/(πN) proof as a one-sentence remark. | PD-T014, PD-T022, PD-T526, PD-N002, PD-T016 | old §2, §4, PR #31 S2-01 |
| 4 | **Endpoint minimum eigenvalue.** 4.1 explicit all-N bounds: weighted cardinal lower estimate (Thm 4.1) and harmonic witness (Thm 4.2); 4.2 the sharp constant: Volterra model (Lemma 4.3), admissible logarithmic trial and limsup ≤ π⁴/8 (Prop. 4.4), reverse bound and limit (Thm 4.5) with the signed sinc remainder (Lemma 4.6) and discrete primitive (Lemma 4.7); proofs of 4.4–4.7 in Appendix A; a forward reference to the single-U evaluation of §8 motivates the harmonic witness. | PD-T017, PD-T018, PD-T522, PD-T523, PD-T544, PD-T545, PD-T546 | old §3, PR #31 S1/P3 |
| 5 | **Endpoint maximum eigenvalue.** Endpoint cardinal combinations p_{N,j}=ℓ_j−2(−1)^jℓ_0, model matrices C, D with closed forms (Lemma 5.1, Si/Cin entries), definition of Λ_edge (variational), fixed-J limits (Prop. 5.2), convergence theorem (Thm 5.3), certified lower bound Λ_edge ≥ 1.0044369 (Prop. 5.4, computer-assisted; reduction and checker named). Long proofs in Appendix B. The finite bracket PD-T531 is not stated (see correspondence: omitted, with reason). | PD-T528 (definition), PD-T529, PD-T530, PD-T548, PD-T547 | PR #31 S2/P4 |
| 6 | **Consequences at the endpoint.** Defect identity and sharp defect limit, condition number (Cor 6.1, new provisional PD-T?mz-paper-claude-01 (a)(b)); old Cor 3.4 absorbed; old Remark 3.5 ("rate not proved") replaced by a remark recording what is now proved and what is not (no effective onset). | PD-T527, PD-T?mz-paper-claude-01 | old §3, new |
| 7 | **Fixed degree ratios.** Filtered Fejér lower estimate (Thm 7.1), strong constants (Cor 7.2); comparison paragraph. | PD-T023, PD-T024 | old §4 |
| 8 | **The three-quarter assumption and hyperinterpolation.** An–Wu context, exact U witness at N=512 (Prop. 8.1), upper-Gram estimate (Prop. 8.2), CC application with B=min{1+ρ,5/3} (Cor 8.3, PD-T?mz-paper-claude-01 (c)). | PD-T019, PD-N004, PD-T025 | old §5 |
| 9 | **Numerical illustrations and open problems.** Table of measured spectra (MEASURED, PD-T026), measured endpoint proxy 1.004437 (PD-T532, MEASURED) with the explicit warning; fitted K1 intercepts (PD-T525) mentioned only as exceeding the proved limit, if at all; open: the decimal value of Λ_edge (PD-T027 decimal conjunct), effective onsets, signed analogues (pointer to MZ-SP). | PD-T026, PD-T525, PD-T532; OPEN items | old §7 |
| A | Proofs for §4.2 (Volterra lemma; trial; signed remainder; discrete primitive; reverse-bound assembly). | | PR #31 |
| B | Proofs for §5 (closed-form Gram entries; fixed-J estimates; convergence). | | PR #31 |
| C | Computer-assisted certificate for Λ_edge ≥ 1.0044369 (exact trial, outward arithmetic, remainders, checker, rerun). | | PR #31 P4 |
| — | Data and code availability; acknowledgements/AI declaration/funding placeholders reserved to AC. | | new |

The development-status box and all `\id{PD-…}` labels in theorem headings are removed from the submission text; the PD IDs move to TeX comments and to `correspondence-cc.md`.

## Literature (task 5)

Keep the CC MZ prior art (ASV, An–Wu, Sloan–Smith, Erdős–Feldheim/Askey/Nevai/Smith, Lubinsky, Mastroianni–Milovanović–Notarangelo, Mastroianni–Russo (incl. the 2000 paper now read in PR #21), Mastroianni–Totik, Lubinsky–Máté–Nevai, Xu, König–Nielsen, Trefethen, Xiang–Bornemann) plus LIT-633 (Toeplitz-plus-Hankel same-symbol norms) only at its read scope. Resolve "Still unread is a 2000 paper of Mastroianni–Russo" using p2-comparison.md. Remove repository-internal coverage notes from bibliography `note` fields.

## Risks

- Length of §5/Appendix B. If the convergence proof cannot be made readable in ≤ 8 pages, the plan reviewer may recommend presenting the fixed-J lower bound (liminf ≥ Λ_edge) with full proof and the convergence with full proof in the appendix anyway; no claim may be stated without proof in the paper.
- Notation clashes already visible: B (Gram bound vs. kernel matrix), K_N (constant) vs K (filter kernel) vs K (transition matrix of PD-T526), C_0 (two meanings), ρ (ratio parameter vs. auxiliary weights in SP), L (log N vs. Lagrange operator L_N), H (harmonic numbers vs. matrix H of PD-T526 vs. kernel H(t,j)). Resolved in `notation-cc.md` (task 6).
