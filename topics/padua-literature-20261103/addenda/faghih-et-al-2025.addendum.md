# faghih-et-al-2025 — addendum (LIT-347, LIT-119)

A. Faghih, M. Rinelli, M. Van Barel, R. Vandebril, R. Vermeiren, "Krylov and Core Transformation Algorithms for an Inverse Eigenvalue Problem to Compute Recurrences of Multiple Orthogonal Polynomials", SIAM J. Numer. Anal. 64(4) (2026) 1190–1216, doi [10.1137/25M1770965](https://doi.org/10.1137/25M1770965); preprint arXiv 2506.19796; code https://gitlab.kuleuven.be/numa/public/IEP-MOP (cited by the authors, not loaded).

- Basis of this addendum: `topics/padua-literature-20261103/notes/faghih-sinum-2026-assessment.md`. Claude (claude-opus-5-5) read the AC-supplied published PDF on 2026-11-03: §1 pp. 1190–1193, §3.2 pp. 1195–1198, §4.2–4.4 pp. 1198–1203, §5 opening and Alg. 5.1 pp. 1203–1205, §6.2–6.3 pp. 1210–1213, §7 p. 1213, references. **P4 did not re-read the paper.** The corrections below carry over the assessment note's verified readings. P4 adds only the cross-references found in arXiv 2608.25758.
- Reader of this addendum: Claude P4 literature reader (claude-opus-5-5, high).

## Corrections (old → new)

1. **LIT-347 / LIT-119, stability.** Old: "the core-transformation (LU-eliminator) variant appears backward stable for N < 25 and loses it beyond" (LIT-347), and "IEP_CORE … appears backward stable only for N < 25" (LIT-119). New: **IEP_CORE and IEP_KRYLREORTH(full) are backward stable for most N < 25** and lose backward stability for N ≥ 25. IEP_KRYL is not backward stable for any N considered. Backward errors on nodes and weights come from the eigen-decomposition of the computed H in quadruple precision (§6.2, p. 1211). For the Kravchuk and Hahn IEPs all methods are weakly stable (§6.2, p. 1211). On the better-conditioned random-weight IEPs (§6.3), IEP_KRYLREORTH(full) is the most accurate, at a higher cost (§7, p. 1213).
2. **LIT-347 / LIT-119, Laurie.** Old: "authors … know no extension of Laurie's approach to MOPs" / "authors not aware of an extension of Laurie's approach to MOPs". New: §7 (p. 1213) names extending Laurie's approach, via vector or branched continued fractions, as a possibility not discussed in the paper. It is **not** a statement that no extension is known.
3. **LIT-347, "systematic comparison would be interesting".** This is kept as a paraphrase of §7, together with the full future-work list: IEP conditioning theory; updating and downdating (now arXiv 2608.25758, LIT-348); Laurie extension via vector or branched continued fractions; other recurrences, notably nearest-neighbour; comparison with Filipuk–Haneczok–Van Assche 2015 and ref. [35] (§7, p. 1213).
4. **Locators and citation.** Old LIT-119 locator: "no locator". New: Alg. 4.1 p. 1199 (IEP_KRYL), §4.3 (reorthogonalized variants), Alg. 5.1 p. 1205 (IEP_CORE), §6.2 p. 1211 (stability), §7 p. 1213 (future work). Add the journal citation SINUM 64(4) (2026) 1190–1216 and the code URL (cited, not loaded).
5. **Coverage.** Old: "UNVERIFIED … secondary". New: "VERIFIED-fulltext for the statements above (published PDF; assessment note 2026-11-03); §2 and §4.1 proofs and the full §5 example not read line by line".
6. **Record header (`literature/records/faghih-et-al-2025.md`).** Old: "title not given in inputs". New: the full title above. The key stays `faghih-et-al-2025` for stability, even though the journal year is 2026.

## Cross-references found by P4 (arXiv 2608.25758, read in full)

- 2608.25758 cites this paper as [14], with the published SINUM pages (p. 25). It states that the type II MOP Hessenberg matrix is monic here (unit subdiagonal, p. 10). It also says that the Kravchuk/Hahn generation in double precision is ill conditioned enough to make large degrees infeasible, pointing to [14, §6] (p. 3, pp. 20–21).
- 2608.25758 reuses this paper's Prop. 3.7 (starting vectors) and Prop. 4.2 (uniqueness) (pp. 6, 19).

## History

2026-11-03: P4 addendum, carrying over the assessment-note corrections. No new provisional ID: the statements remain LIT-347 / LIT-119, corrected.
