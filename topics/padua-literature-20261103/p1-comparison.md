# P1 comparison — Padua Lebesgue-function results against the published literature

Claude (claude-opus-5-5, high), 2026-11-03.

**Basis.** Every source below was read by Claude at the pages named in its record. Link discovery was done by a Sonnet subagent. Its negative findings for other Padua papers (no statement about where the maximum lies) are summarising-fetch results and are labelled as such.

**Added after AC's downloads (2026-11-03):** Brutman 1978 (read in full) and Günttner 1980/1988 (partial). They add only 1-D context and change no verdict below.

**Verdict vocabulary** (handoff 01, step 4):
- SUBSUMES;
- IMPLIES PART;
- RELATED, DIFFERENT SETTING;
- no matching result found in the documented search.

**Documented search** (2026-11-03): Crossref/DOI checks; arXiv; author pages of Caliari, De Marchi, Sommariva and Vianello; the reference lists of KL 2021, Kuznetsova 1995 and Białas-Cież–De Marchi–Suder 2026; secondary surveys (Ibrahimoglu 2016, Smith 2006, Da Fies–Vianello 2013); web search. The search was not exhaustive: zbMATH and MathSciNet full-text search were not available to the tools.

## Sources read for P1

| Key (record) | Content used | Coverage |
|---|---|---|
| [kuznetsova-1995](../../literature/records/kuznetsova-1995.md) | Thm 1: pointwise asymptotics of the 2-D rhombic discrete-Fourier Lebesgue function, O(log n) remainder | complete (OCR); Thm 1 on the page image |
| [pimenova-1979](../../literature/records/pimenova-1979.md) | the m = n, odd-grid trigonometric-interpolation case (1979): constant 2/π², the same as Kuznetsova eq. (1) at m = n | complete (OCR); Thm 1 and (3) on page images (2026-11-05) |
| [kolomoitsev-lomako-2021](../../literature/records/kolomoitsev-lomako-2021.md) (LIT-379) | Thm 2.1 and the Padua sentence on p. 4; Lemmas 3.5–3.6; (3.27)–(3.30) are imported from Kuznetsova | locators confirmed for v1 |
| [cdmsv-poster-2008](../../literature/records/cdmsv-poster-2008.md) | Conjecture: maximum ≈ (4/π²) log² n, attained at a vertex | complete |
| demarchi-2022 (LIT-326/377; addendum proposed in [proposed-record-changes.md](proposed-record-changes.md)) | §3.3(2), p. 23: "maxima in the corners, where there are no Padua points" (observation, listed among open problems, Fig. 7) | §3.3, pp. 22–23, journal PDF |
| [bcdmv-computing-2006](../../literature/records/bcdmv-computing-2006.md) | Xu points: vertex observation and Conjecture (17) | pp. 318–319, 324 |
| [bialas-ciez-demarchi-suder-2026](../../literature/records/bialas-ciez-demarchi-suder-2026.md) (LIT-388) | 1-D argmax facts; NO 2-D global-maximum statement | complete |
| [ehlich-zeller-1966](../../literature/records/ehlich-zeller-1966.md) | 1-D: midpoint maxima (equispaced trigonometric), endpoint maxima (Chebyshev zeros), extrema case | complete (OCR) |
| [brutman-1978](../../literature/records/brutman-1978.md) | 1-D: local maxima decrease toward the middle (zeros) and increase (extrema); attribution chain Luttmann–Rivlin → Ehlich–Zeller (Powell) | complete |
| [guenttner-1980-1988](../../literature/records/guenttner-1980-1988.md) | 1-D constants with explicit remainders; deviation between local maxima | partial |

## Rows: our result against the closest published statement

| Our result (status) | Closest published statement | Verdict | Translation / mismatch |
|---|---|---|---|
| PD-T101 exact corner formula, all n ≥ 1, four corners (PROVED) | Kuznetsova 1995, Thm 1; Pimenova 1979, Thm 1 | RELATED, DIFFERENT SETTING | They give asymptotics with an O(log n) remainder for periodic trigonometric operators on full torus grids, with rhombic frequencies. PD-T101 is an exact finite identity for the Padua interpolant (even/cosine symmetrisation, checkerboard nodes). The rhombic-kernel mechanism is shared. No exact finite corner formula was found. |
| PD-T156 corner leading lower bound; PD-T157 explicit two-sided leading term (PROVED) | KL 2021, Thm 2.1 with its Padua sentence (p. 4): Λ^Pad_n = (4/π²) log² n + O(log n). KL's lower-bound construction, arXiv v1 §4 (4.8), evaluates the angular point (π/m, 0), i.e. the non-corner point (cos(π/m), 1), per audit-01 F1. Kuznetsova 1995 eq. (1) gives the pointwise torus asymptotics. | **Upper half: IMPLIES PART.** **Lower half at the corner: no matching result found in the documented search.** (Revised 2026-11-05, response-01 F1.) | Upper half, translation: the corner value Λ_c(n) is at most the global maximum Λ^Pad_n, so KL's global theorem gives Λ_c(n) ≤ (4/π²) log² n + O(log n). Lower half: KL's lower estimate is evaluated at a non-corner point. A lower bound near a corner does not give one at the corner without a transfer argument (parity and symmetrisation of the cited equations), and this topic supplies none, since that would be new mathematics. Kuznetsova's pointwise formula is for the periodic operator; its transfer to the Padua corner was not checked. So no source read states the matching lower bound for the corner value itself. The coefficient 4/π² is nevertheless published, as the coefficient of the global constant (KL 2021, building on Kuznetsova 1995), and must not be presented as new. Not implied either way: the explicit constants of PD-T156/157. |
| PD-T158 corner log coefficient b = (8/π²)(γ + log(8/π)) with \|remainder\| ≤ 68 for all n ≥ 2 (PROVED) | KL 2021 (remainder O(log n)); Kuznetsova 1995 and Pimenova 1979 (remainder O(log n)) | no matching result found in the documented search | Every published remainder found is O(log n), so none determines the log coefficient. De Marchi 2022 is reported (LIT-377, secondary, not rechecked here) to fit Λ ≈ ((2/π) log(n+1) + 1.1)² numerically; that is an empirical fit for the global constant, not a corner theorem. |
| PD-T159 bounded comparison of Λ_c(n) with the squared 1-D Chebyshev sum (PROVED) | Ehlich–Zeller 1966 Satz 3 (explicit 1-D Chebyshev-zeros constant); KL 2021 | RELATED, DIFFERENT SETTING | E–Z give the 1-D constant explicitly. No 2-D statement comparing the Padua corner value with the square of a 1-D constant was found. |
| Global argmax at exactly the two corners that are not nodes: n = 2 (PD-T209), 3–7 (PD-T162/166/169/174/177), 8 (PD-T181), 9–16 (PD-T214), and all n ≥ N_* (PD-T229, non-effective) (PROVED in these ranges; the all-n target remains OPEN) | Caliari–De Marchi–Sommariva–Vianello 2008 poster, Conjecture (maximum at a vertex). De Marchi 2022 §3.3(2), p. 23 (observation: maxima in the corners where there are no Padua points). | no matching result found in the documented search (for a proof). **The statement itself was conjectured (2008) and observed (2022).** | The finite and eventual theorems prove, in those ranges, the 2008 conjecture in the sharper form already worded by De Marchi 2022: exactly the corners that are not nodes. The poster also conjectures the size ≈ (4/π²) log² n, now known globally from KL 2021. |
| Edge formula PD-T185 and edge gaps and envelopes PD-T186–192, T211/212/230 (PROVED) | Kuznetsova 1995 Thm 1 (leading term); Ehlich–Zeller 1966 (1-D midpoint/endpoint symmetry arguments) | no matching result found in the documented search | Claude's observation: Kuznetsova's leading factor equals max(\|cos(a−b)\|, \|cos(a+b)\|). It equals 1 along whole lines a = ±b (mod π), so the leading term cannot separate edges from corners. The gaps need sub-leading information, which is exactly what PD-T186–192 supply. No published edge-versus-corner comparison was found. |
| Local-maxima counts n = 3–8 (PD-T161/165/168/173/176; PD-T183 is a lower bound only, and PD-T180/184 remain OPEN) | Białas-Cież–De Marchi–Suder 2026, Table 3 (numerical) | RELATED, DIFFERENT SETTING (numerical against certified) | Already recorded in the LIT-388 addendum of 2026-11-01: certified n = 6, 7 counts and the n = 8 lower bound conflict with their table. Unchanged by the complete reading. |
| 1-D framing: where the maximum lies | Ehlich–Zeller 1966 (Chebyshev zeros: ±1; equispaced trigonometric: midpoints; extrema: middle); Białas-Cież et al. 2026 §2.1, §4 | RELATED, DIFFERENT SETTING | For framing only. Claude's comparison: Padua points are built on Chebyshev–Lobatto (extrema) coordinates, yet their maximum sits at boundary corners outside the node set. That resembles the 1-D zeros case rather than the 1-D extrema case. The 1-D question "when is the maximum at an endpoint" is posed as open in Białas-Cież et al. 2026, §4. |

## Priority wording for the paper (proposed)

1. **Exact corner value (PD-T101).**
   - Proposed sentence: "To our knowledge no closed form for the value of the Padua Lebesgue function at a corner has appeared."
   - Cite for the rhombic-kernel mechanism and pointwise asymptotics: Kuznetsova 1995 [Ukr. Math. J. 47], with Pimenova 1979 [Dokl. 249] as the m = n trigonometric case; Kolomoitsev–Lomako 2021 for the transfer to Lissajous–Chebyshev and Padua points.
2. **Corner asymptotics (PD-T156–159).**
   - Proposed sentence (revised 2026-11-05, response-01 F1): "The Lebesgue constant of the Padua points satisfies Λ_n = (4/π²) log² n + O(log n) [KL21], with pointwise estimates going back to Kuznetsova [K95]; in particular the corner value is at most this. We show that the corner value has the same leading term, with explicit constants, and give the second term b log n, b = (8/π²)(γ + log(8/π)), with an explicit remainder bound valid for all n ≥ 2."
   - Do not claim the coefficient 4/π² as new. Do not say KL proved the corner lower bound: their lower estimate is at a non-corner point, and no transfer was checked.
3. **Corner argmax (PD-T209/T214/T229 and the finite cases).**
   - Proposed sentence: "Caliari, De Marchi, Sommariva and Vianello conjectured [CDMSV08] that the maximum is attained at a vertex, and De Marchi [DeM22, §3.3(2)] observed that it lies at the corners not occupied by Padua points. We prove this for 2 ≤ n ≤ 16 and for all sufficiently large n; the intermediate range remains open."
   - Also mention the analogous open conjecture for Xu points [BCDMV06, Conj. (17)].
4. **1-D context.**
   - Proposed sentence: "In one variable the location of the maximum is classical: ±1 for the Chebyshev zeros, the midpoints for equispaced trigonometric interpolation [Ehlich–Zeller 1966]. Characterising when it lies at the boundary is open in general [BCDMS26, §4]."
   - Local maxima: decreasing toward the middle for Chebyshev zeros, increasing for extrema [Brutman 1978, Thm 1 and (44)].
   - Explicit remainders for 1-D constants: [Günttner 1980].
5. **Attribution fixes.**
   - "Powell 1965" (as in BCDMS26) should be cited as Powell, Comput. J. 9 (1967) 404–407 ([10.1093/comjnl/9.4.404](https://doi.org/10.1093/comjnl/9.4.404); not read), or replaced by Ehlich–Zeller 1966, which was read.
   - Brutman 1978, p. 695, gives the chain: Luttmann–Rivlin conjecture, proof by Ehlich–Zeller, "see also Powell".
   - Brutman's survey is Ann. Numer. Math. 4 (1997).

## Reuse note for `codex/padua-argmax-effective-20261103` (gate G8)

After this topic merges, that branch can reuse the following records for its 1-D and priority sources:
- ehlich-zeller-1966, kuznetsova-1995, pimenova-1979;
- cdmsv-poster-2008, bcdmv-computing-2006;
- kolomoitsev-lomako-2021, bialas-ciez-demarchi-suder-2026;
- the demarchi-2022 addendum.

brutman-1978 and guenttner-1980-1988 can also be reused. This topic does not write to that branch.
