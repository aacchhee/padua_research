# Literature coverage for the MZ papers (task 5; gate W3)

Purpose: for every `\cite` in each MZ paper, check that the citing sentence stays within the source's read coverage as recorded in its LIT record. Also check bibliographic data against the records, list relevant read sources that are not cited, and give AC links for unread items the text needs.

Checker: Claude Opus 5.5, high effort, independent literature check, 2026-11-13. Repository head `2e65795fc76710e821aa4a396e5ae0839a5aac80` (branch `claude/padua-mz-paper-20261113`). The manuscript working tree had uncommitted notation edits by another worker. The `\cite` line numbers below are identical at HEAD and in that working tree (checked). Read for this check:
- `tracks/mz-constants/paper/manuscript.tex` §1, §6 opening, §8;
- `refs.bib`;
- `literature/INDEX.md`, and records `mz-an-sommariva-vianello-2026`, `mz-an-wu-2022`, `mz-quadrature-aliasing-screen`, `mz-sloan-smith-1978-1980`, `mz-mean-convergence-screen`, `mz-prior-art-2026-additions`, `mastroianni-russo-2000`, `mz-classical-mz-screen`, `mz-mastroianni-milovanovic-2008`, `mz-widom-1966-screen`, `mz-don-gottlieb-1994`, `demarchi-kroo-2018`, `wu-aml-2026`, `guenttner-1980-1988`;
- `topics/mz-prior-art-20261101/translation.md` (T3–T6);
- `topics/padua-literature-20261103/p2-comparison.md`.

No source PDF was reopened. This is a check of the manuscript against the records only.

## MZ-CC

### Summary

- 35 citation occurrences (28 `\cite` commands; multi-key commands counted per key).
- **29 OK.** Two of them (L1292, L1329) need only process wording removed.
- **5 NEEDS-SOFTENING:** L213 (LIT-045), L239 (LIT-061), L278 and L1163 (LIT-051), L292 (LIT-049).
- **1 UNSUPPORTED:** L289 (LIT-298).
- **0 OVERREACH** among cited claims. One **uncited negative claim overreaches** against a read source: L300–302, "explicit fixed-ratio constants", against De Marchi–Kroó, LIT-490.

### A. Per-citation scope check

Coverage is quoted from the LIT record, not from the bib `coverage` field, where the two differ (see C).

| # | Line | Key | Claim attributed | Record coverage | Verdict |
|---|---|---|---|---|---|
| 1 | 86 | LIT-045 | ASV study weak MZ constants and examine CC numerically; they distinguish weak from strong constants; they report CC beyond half-exactness as not known theoretically | Published MCS 252: complete article keyword-screened, §§1–2, §3.1, §3.6 read; p. 738 "not known" (to their knowledge). arXiv v1 intro read | OK. Optional: add "to their knowledge" here as at L304 |
| 2 | 115 | LIT-046 | An–Wu's CC parameter m counts points | Cor. 4.1 read (arXiv v3 and published p. 1911): m-point CC | OK |
| 3 | 208 | LIT-055 | Thm 5.2 and (5.2)–(5.4) give the mode aliasing | §5, Thms 5.1–5.2, (5.2)–(5.4), pp. 73–80 read | OK |
| 4 | 209 | LIT-056 | coefficient-decay results give related quadrature context | intro theorem and §3 aliasing read | OK (process word "selected", see B) |
| 5 | 213 | LIT-045 | "ASV equation (7)" uses the factor 1+√(1+η) with an aliasing term; "(8)" separates the inverse-Gram least-squares construction | Eqs. (7)–(8) were read in **arXiv v1** (astra audit, 2026-10-31). Of the published version (the bib entry) only §§1–2 were read. That version adds Prop. 2.1 and Thm 2.1, and its equation numbering was not checked | **NEEDS-SOFTENING** (equation locators belong to arXiv v1, the bib cites the published version) |
| 6 | 232 | LIT-047 | controls Σ\|w\| (a C[−1,1] functional norm) | pp. 415–421 read, Thm 1 p. 419; Thm 3 located in the screen | OK |
| 7 | 234 | LIT-048 | heuristic error estimates and numerical tests; no theorem | complete text section- and keyword-screened; §4 "rather than rigorous error bounds"; no theorem/lemma/corollary | OK (the next sentence has process wording, see B) |
| 8 | 239 | LIT-061 | bounds interpolation from **uniform** data into weighted L^p | pp. 913–914 read: eq. (1), convergence in even powers for Chebyshev abscissae, measure dx/√(1−x²). Node convention and **function hypotheses are in the unread preceding note** (Feldheim, C. R. 203, 650–652) | **NEEDS-SOFTENING** |
| 9 | 239 | LIT-062 | same (uniform data → weighted L^p) | journal pp. 71–78 read; Thm 1 p. 75, continuous f, Gauss zeros | OK |
| 10 | 239 | LIT-063 | same; quasi-Lagrange theorem includes CC nodes | all theorems via text extraction (formulas partly garbled). Thm 1 p. 680: sup‖L_n(w,vf)u‖_p ≤ C‖f‖_∞. Thm 6 p. 695: quasi-Lagrange, w=(1−x²)^{1/2}, r=s=1 gives CC | OK. The CC specialization rests on parameter identification, not on garbled formulas. A page-image check of Thm 6 would firm it up (D) |
| 11 | 239 | LIT-065 | Lobatto theorem, uniform data → L²(w) | complete article incl. p. 379 | OK |
| 12 | 245 | LIT-064 | full-space converse inequalities need an exponent in an open range; CC/p=2 sits at the excluded endpoint | pp. 577–584 read: Thm 1.7, −1/p<σ<1−1/p. The endpoint statement is our translation T5 and is phrased as ours | OK |
| 13 | 248 | LIT-299 | iff-characterization at zeros of p_m((1−x²)^α) plus ±1, P∈Π_{m+1}; α=1/2 gives CC; necessity gives inf_N λ_−(N,N)=0 | pp. 163–167 read, Cor. 2.2 p. 167; proofs not audited (T6 conditional on the necessity part) | OK. Word fix: "This is classical" (L256) for a 2012 source → "This is known" |
| 14 | 258 | LIT-293 | converse inequalities at Gauss nodes, no endpoint terms; at U_{N−1} zeros the condition needs (1−x²)^{−1/2}∈L² | pp. 257–264 read, Thm 2.7 p. 263, (2.22) | OK |
| 15 | 258 | LIT-296 | converse inequalities at Gauss nodes | Part II pp. 77–87 (OCR), Thm 3.2 p. 82 | OK |
| 16 | 260 | LIT-294 | same-weight Jacobi nodes | arXiv v1 pp. 1–4, 13–17 read directly. Journal: p. 183 preview only. No locator is used in the text | OK |
| 17 | 265 | LIT-511 | Thm 11 covers CC nodes for even N on Π_N; A_2 hypothesis fails at the power-weight endpoint; no rate for the lower constant; forward theorem gives boundedness of the upper constant | §3 read, Thm 11 hypotheses from page images (copy p. 23); "log" search; negative scoped to "no quantitative borderline estimate" | OK |
| 18 | 269 | LIT-050 | boundedness of the upper constant | pp. 531–538 read, Thm 5 p. 534 | OK |
| 19 | 278 | LIT-051 | applies at CC only for n≤N/(πM), M unspecified; "for every admissible M≥2/π" inside half-exactness; "In its documented form it therefore adds nothing beyond exactness" | §4.2 and §7 read; p. 65 algebraic inequality with unspecified M. T4: "a non-trivial consequence would need an admissible M<2/π, and the source does not specify M" | **NEEDS-SOFTENING**. The "therefore" needs M≥2/π, which the source does not give, and "documented form" is process language |
| 20 | 284 | LIT-050 | at CC nodes, for each fixed l, every degree ≤lN; λ_+ ≤ C_l, unspecified | Thm 5 p. 534 (degree ≤ ln, constants independent of m, nodes, n, P), plus our T3 weight translation | OK |
| 21 | 289 | LIT-297 | relates product-integration convergence to mean convergence with uniform data | pp. 427–434 read; Thm 5 p. 432 | OK |
| 22 | 289 | LIT-298 | same | statements of Thms 1–3 read: convergence for continuous f and Σ\|w\|→∫\|k\| at **Jacobi zeros**, plus individual-weight limits. **No link to mean convergence is recorded** | **UNSUPPORTED** |
| 23 | 292 | LIT-049 | chapters 2, 4, 5 "concern uniform norms, Sobolev inputs or different matrix problems" | Chapters 2, 4, 5 indexed by headings and keyword-screened only. Ch. 4 is *Algebraic Interpolation in Uniform Norm*. Ch. 2 (weighted polynomial approximation) and ch. 5 (quadrature) are not uniform-norm material. Recorded negative: "no weighted ℓ²→L² Lagrange interpolation norm theorem in the screened chapters" | **NEEDS-SOFTENING** (the characterization fits ch. 4 only) |
| 24 | 293 | LIT-053 | Hankel asymptotics, a different matrix problem | all sections via extraction | OK |
| 25 | 293 | LIT-054 | same | whole note via extraction; erratum (Proc. AMS 19, 1968) unread | OK |
| 26 | 294 | LIT-058 | different matrix problem | journal pp. 1519–1525 read (OCR); same as ICASE 93-40 | OK |
| 27 | 296 | LIT-295 | Sobolev inputs | article page via extraction (paraphrase level) | OK |
| 28 | 297 | LIT-052 | records converse quadrature-sum theorems, at Gauss nodes and weights | §3 pp. 229–232 read; Thms 3.1–3.3 | OK |
| 29 | 303 | LIT-045 | the published version says CC beyond half-exactness is, to its authors' knowledge, not known theoretically | p. 738 read | OK. The **preceding uncited sentence** overreaches (see B, item 3) |
| 30 | 1163 | LIT-051 | "yields nothing beyond this in its documented form" | as #19 | **NEEDS-SOFTENING** (as #19) |
| 31 | 1292 | LIT-046 | "An–Wu's inspected arXiv version" assumes η<1; §4 η=3/4; Cor. 4.1 for n+2≤m≤2n+1, bound 3√V E_{m−1−n}(f) | arXiv v3 and published both read at Assumption 2.1, Thm 2.2, §4 opening and Cor. 4.1; they match | OK in content; remove "inspected arXiv version" (the published version was read) |
| 32 | 1322 | LIT-293 | analogous borderline mechanism in a converse MZ characterization | Thm 2.7 iff | OK |
| 33 | 1322 | LIT-294 | same | Thm 1(b) iff; log growth at p=M, eqs. (18)–(19) | OK |
| 34 | 1324 | LIT-299 | full-space subsequence version of λ_−(N,N)→0 | as #13 | OK |
| 35 | 1329 | LIT-046 | published Cor. 4.1 coincides with arXiv; m=513, n=511 in range; "No correction was found in a documented search; this is not proof of absence" | as #31; erratum/correction title search recorded | OK in content; process wording (B) |

#### Replacement sentences (minimal changes)

**Applied by the orchestrator, 2026-11-13:** #5 (resolved 2026-11-14: the published PDF, supplied by AC in Downloads\padua\papers as 1-s2.0-S0378475426004416-main.pdf and read by the orchestrator, has the factor 1+√(1+η) with an aliasing term as (7) and the inverse-Gram LS construction as (8), as in arXiv v1. The text now says "Equation (7) of [LIT-045]". The LIT-045 record should note this at PR preparation), #8, #13, #19, #22, #23, #30, #31, #35; B.1–B.6; the L4 pdfsubject; LIT-490 added and cited; bib fixes from C (LIT-294 doi and coverage, LIT-058 coverage, LIT-511 coverage, LIT-056 doi). Not applied: LIT-489 (Wu AML), which is optional and has no natural place in MZ-CC's text.

- **#5, L210–213.** Preferred fix: AC checks the published PDF ([doi:10.1016/j.matcom.2026.10.001](https://doi.org/10.1016/j.matcom.2026.10.001)). If the formulas are (7) and (8) there, keep the text. Otherwise replace with
  > In the arXiv version of \cite{LIT-045}, equation~(7) already uses the upper-MZ factor $1+\sqrt{1+\eta}$, together with an aliasing term, and equation~(8) separates the inverse-Gram least-squares construction.

  Also at L214, "is consequently known context" → "is therefore known".
- **#8, L237–240.** Replace the first sentence of the item with
  > The weighted mean-convergence results of Askey and Nevai, and Smith's Lobatto theorem \cite{LIT-062,LIT-063,LIT-065}, bound interpolation from \emph{uniform} data into weighted $L^p$, and Erd\H{o}s--Feldheim \cite{LIT-061} prove mean convergence at Chebyshev abscissae in the Chebyshev measure.

  The rest of the item stands.
- **#19, L277–282.** Replace the item with
  > The algebraic Marcinkiewicz inequality of Mastroianni--Totik \cite{LIT-051} applies at CC nodes only when $n\le N/(\pi M)$, where the sampling constant $M$ is asserted to exist but is not specified. Unless $M<2/\pi$, this window lies within the half-exactness range $n\le N/2$, where exactness already gives $\lambda_\pm(N,n)=1$. Since no such value of $M$ is given, the inequality adds nothing beyond exactness for the questions of Section~\ref{sec:ratio}.
- **#30, L1162–1165.** Replace with
  > For $n\le N/2$, exactness gives $\lambda_\pm(N,n)=1$; the classical algebraic Marcinkiewicz inequality of Mastroianni--Totik \cite{LIT-051} yields nothing beyond this, because its sampling constant is unspecified (Section~\ref{sec:context}).
- **#22, L289–290.** Replace with
  > The later Sloan--Smith paper \cite{LIT-297} relates product-integration convergence to mean convergence with uniform data; Smith and Sloan \cite{LIT-298} treat product integration at Jacobi zeros.
- **#23, L291–297.** Replace the first sentence with
  > Chapter~4 of the interpolation book of Mastroianni--Milovanovi\'c \cite{LIT-049} treats interpolation in the uniform norm, and Widom's and Widom--Wilf's Hankel asymptotics \cite{LIT-053,LIT-054}, the Chebyshev--Legendre method \cite{LIT-058} and recent Chebyshev--Lobatto interpolation estimates in the Legendre norm \cite{LIT-295} concern different matrix problems or Sobolev inputs.

  The sentence on Lubinsky's survey stands.
- **#31, L1288.** "An--Wu's inspected arXiv version assumes" → "An and Wu assume". Optionally add the locator `\cite[Thm.~2.2]{LIT-046}`.
- **#35, L1327–1330.** Replace with
  > Corollary~4.1 of the published version assumes $\eta=3/4$ for $m$-point CC with $n+2\le m\le2n+1$ \cite{LIT-046}, and $m=513$, $n=511$ lies in that range. We are not aware of a published correction.
- **#13, L256.** "This is classical, but" → "This is known, but".

### B. Remaining pre-PR #21 hedge and process language

In §1 (item i):
1. **L235–236:** "In the portions inspected we found no quadratic-form or nodal $\ell^2$ estimate in either paper." Replace with "Neither paper states a quadratic-form or nodal $\ell^2$ estimate." This is supported by the record verdicts. LIT-047: Thms 1–3 read or located; the only norm controlled is the C[−1,1] dual. LIT-048: the complete screen found no theorem at all.
2. **L281:** "In its documented form" (fixed by #19).
3. **L300–303:** "We found no statement of … our search was documented but not exhaustive."
   - Process language.
   - It also **overreaches**: "explicit fixed-ratio constants" is contradicted as written by De Marchi–Kroó (LIT-490, Lemma 1 pp. 72–73, proof read in full). That lemma gives explicit constants 2/3 and 2 at Chebyshev–Lobatto nodes cos(jπ/m), with Δx weights, for m ≥ 18pk+1. That is a fixed ratio, but for p=2 it lies inside half-exactness (record translation: n < m/36).
   - Replace with (adding a bib entry for LIT-490, see E):
     > To our knowledge, no published result states the logarithmic order of $\lambda_-(N,N-1)$, its limit constant, the limit of $\lambda_+(N,N-1)$, an all-$N$ upper constant below two, or explicit constants beyond half-exactness at a fixed degree ratio; explicit two-sided constants at Chebyshev--Lobatto nodes are known in a heavily oversampled regime \cite{LIT-490}, which for $p=2$ lies inside the half-exactness range.
   - Without the LIT-490 citation, at least insert "beyond half-exactness" after "explicit fixed-ratio constants".
4. **L209:** "selected coefficient-decay results" is mild. "selected" can go: "the coefficient-decay results of Xiang--Bornemann provide related quadrature context".
5. **L214:** "known context" is repository jargon (see #5).
6. **L256:** "This is classical", applied to a 2012 paper (#13).

Outside §1:
- **L1164:** "documented form" (#30).
- **L1288, L1327:** "inspected arXiv version/formulation" (#31, #35).
- **L1330:** "documented search; this is not proof of absence" (#35).
- **L4:** `pdfsubject={Audited development draft; historical priority screened, not cleared}`. This is process language in the PDF metadata. It is AC's choice; it must not survive to submission.

### C. Bibliographic data: refs.bib against the LIT records (item ii)

Authors, titles, journals, volumes, pages and years match the records for all 26 entries. The mismatches are:

| Key | Field | refs.bib | Record | Action |
|---|---|---|---|---|
| LIT-294 | doi | missing (only arXiv url) | DOI 10.1515/form.1994.6.183, "verified via Crossref (p2-links) and the publisher page (2026-11-03)" | add `doi = {10.1515/form.1994.6.183}` |
| LIT-294 | coverage | "arXiv version inspected via text extraction 2026-11-01; journal version not compared" | arXiv v1 pp. 1–4, 13–17 read directly 2026-11-03; journal only p. 183 preview (matches) | update |
| LIT-058 | coverage | "ICASE Report 93-40 version inspected …; journal version not compared" | journal pp. 1519–1525 read 2026-11-03 (AC-supplied, OCR), identical to ICASE 93-40 on the items used | update |
| LIT-511 | coverage | field absent | AC-supplied copy read 2026-11-05: §1 and §3 read, Thms 11–12 from page images; §2 and appendix proofs screened | add for consistency |
| LIT-056 | doi | missing (arXiv url only); the record also has no DOI | — | add `doi = {10.1137/120869845}` (SIAM epubs page found by web search 2026-11-13: [epubs.siam.org/doi/abs/10.1137/120869845](https://epubs.siam.org/doi/abs/10.1137/120869845); not yet recorded in the LIT record) |
| LIT-045 | author | "An, C." beside full given names for the coauthors | record: "C. An" | style only |
| LIT-052 | editor/series | absent | not recorded | optional; verify before adding |
| LIT-045…056 | INDEX coverage column | generic "selected text, abstract, metadata or UNVERIFIED … no blanket fulltext claim" | the per-record dated sections upgrade coverage (INDEX l. 87 says so) | not a bib error. The INDEX column is stale for these rows; whoever owns INDEX.md could refresh it |

The other entries match their records, with no mismatch: LIT-046 (its extra arXiv url is harmless), 047, 048, 049, 050, 051, 053, 054, 055, 061 (pp. 913–915; no DOI exists), 062, 063, 064, 065, 293, 295, 296, 297, 298 and 299.

### D. Unread items the text needs (item iv)

- **ASV published equation numbering** for (7)–(8) at L210–212 (#5). AC has the PDF. Link: [doi:10.1016/j.matcom.2026.10.001](https://doi.org/10.1016/j.matcom.2026.10.001).
- **Feldheim's preceding note**, C. R. Acad. Sci. Paris 203 (1936) 650–652. It is needed only if the text keeps attributing "uniform data" to Erdős–Feldheim (#8). The replacement above removes the need. The free expanded version is Feldheim, Bull. Soc. Math. France 65 (1937) 1–40: [doi:10.24033/bsmf.1260](https://doi.org/10.24033/bsmf.1260). Scan of Erdős–Feldheim: [renyi.hu/~p_erdos/1936-10.pdf](https://www.renyi.hu/~p_erdos/1936-10.pdf).
- **Nevai III, Theorem 6 (p. 695), page image.** Optional, to firm up "Nevai's quasi-Lagrange theorem includes the CC nodes", which is now read only at extraction level. Free PDF: [ams.org Nevai 1984](https://www.ams.org/journals/tran/1984-282-02/S0002-9947-1984-0732113-4/S0002-9947-1984-0732113-4.pdf); [doi:10.1090/S0002-9947-1984-0732113-4](https://doi.org/10.1090/S0002-9947-1984-0732113-4).
- **König–Nielsen journal body.** Not needed by the current text, which cites no locator, but the bib cites the journal. Link: [doi:10.1515/form.1994.6.183](https://doi.org/10.1515/form.1994.6.183).
- Still unread and **not needed** by the current text: Della Vecchia–Mastroianni–Vértesi 1995 (print only), Brutman 1997, and the Widom–Wilf erratum (Proc. AMS 19, 1968).

### E. Read sources in INDEX not cited that are directly relevant (item iii; at most 5)

1. **LIT-490, De Marchi–Kroó**, Acta Math. Hungar. 154 (2018) 69–89, [doi:10.1007/s10474-017-0769-4](https://doi.org/10.1007/s10474-017-0769-4). Read: pp. 69–75 in full, including the proof of Lemma 1. Lemma 1 gives explicit MZ constants at Chebyshev–Lobatto nodes, inside half-exactness for p=2. It is needed to keep L300–302 accurate, and it belongs next to Mastroianni–Totik (p2-comparison "Priority wording" (i)).
2. **LIT-489, Wu**, Appl. Math. Lett. 182 (2026) 110033, [doi:10.1016/j.aml.2026.110033](https://doi.org/10.1016/j.aml.2026.110033). Complete reading. It is an abstract consumer of the MZ defect η = max(1−λ_−, λ_+−1), with Galerkin stability needing η < α/β. Our Cor. 1.4(ii) supplies explicit η(θ), and Cor. 1.4(i) shows η_N → 1. Recommended by p2-comparison (ii). Fits §1 or §8.
3. **LIT-633, Basor–Ehrhardt 1999** (same-symbol Toeplitz-plus-Hankel norms). Sections 1–5 read; proofs not audited. Use only as a pointer in open problem 3 (L1436–1437, "Toeplitz-plus-Hankel or Wiener–Hopf type"), since the record says the CC identification "remains a separate obligation" (also review-plan-cc.md (f)).
4. **LIT-487, Günttner 1980/1988**, [doi:10.1137/0717043](https://doi.org/10.1137/0717043), [doi:10.1137/0725030](https://doi.org/10.1137/0725030). Theorem statements only. Uniform-norm Lebesgue constants (2/π) log n + c at Chebyshev extrema: a natural contrast to the (2√2/π²) log N ℓ²(w)→L² norm of Thm 1.2. Optional, and only at the statement scope.

LIT-427 (Sommariva–Vianello–Zanovello 2008) and LIT-488 (KLP 2018) are relevant to MZ-SP, not MZ-CC.

### F. Coverage table (bib `coverage` field / record), MZ-CC

| Key | Short reference | Record coverage (authoritative) | Scope check |
|---|---|---|---|
| LIT-045 | An–Sommariva–Vianello (2027) | arXiv v1 intro, eqs. (7)–(8), §§3.1–3.2; published: complete keyword screen, §§1–2, 3.1, 3.6 read | #1, #29 OK; #5 NEEDS-SOFTENING |
| LIT-046 | An–Wu (2022) | arXiv v3 and published: Assumption 2.1, Thm 2.2, §4 opening, Cor. 4.1; Padua/square screen | #2, #31, #35 OK (process wording in #31, #35) |
| LIT-047 | Sloan–Smith (1978) | pp. 415–421 read, 422–428 keyword-screened | #6 OK |
| LIT-048 | Sloan–Smith (1980) | complete section/keyword screen; no theorems | #7 OK |
| LIT-049 | Mastroianni–Milovanović (2008) | ch. 2, 4, 5 headings and keyword screen; ch. 1, 3 unscreened | #23 NEEDS-SOFTENING |
| LIT-050 | Lubinsky–Máté–Nevai (1987) | pp. 531–538 read; proofs not audited | #18, #20 OK |
| LIT-051 | Mastroianni–Totik (2000) | §4.2, §7 read; whole article keyword-indexed | #19, #30 NEEDS-SOFTENING |
| LIT-052 | Lubinsky (1998) | §3 read, p. 238 read, rest keyword-screened | #28 OK |
| LIT-053 | Widom (1966) | all sections via extraction | #24 OK |
| LIT-054 | Widom–Wilf (1966) | whole note via extraction; erratum unread | #25 OK |
| LIT-055 | Trefethen (2008) | pp. 73–80 selected (Thms 4.1, 5.1–5.2, (5.2)–(5.4)) | #3 OK |
| LIT-056 | Xiang–Bornemann (2012) | arXiv v3 intro theorem, §3 | #4 OK |
| LIT-058 | Don–Gottlieb (1994) | ICASE 93-40; journal pp. 1519–1525 read, rest screened | #26 OK |
| LIT-061 | Erdős–Feldheim (1936) | pp. 913–914; preceding note unread | #8 NEEDS-SOFTENING |
| LIT-062 | Askey (1972) | pp. 71–78 read, 79–85 keyword-screened | #9 OK |
| LIT-063 | Nevai (1984) + 1990 letter | all theorems via extraction; letter read | #10 OK |
| LIT-064 | Lubinsky (1999) | pp. 577–584 read, rest keyword-screened | #12 OK |
| LIT-065 | Smith (1986) | complete | #11 OK |
| LIT-293 | Mastroianni–Russo (1999) | pp. 257–264 read; rest keyword-screened | #14, #32 OK |
| LIT-294 | König–Nielsen (1994) | arXiv v1 pp. 1–4, 13–17; journal p. 183 only | #16, #33 OK |
| LIT-295 | Niu et al. (2021) | article page via extraction | #27 OK |
| LIT-296 | Xu (1994) | Part II pp. 77–87 (OCR); Part I keyword-screened | #15 OK |
| LIT-297 | Sloan–Smith (1982) | pp. 427–434 read | #21 OK |
| LIT-298 | Smith–Sloan (1980) | abstract, intro, statements of Thms 1–3 | #22 UNSUPPORTED |
| LIT-299 | Mastroianni–Milovanović–Notarangelo (2012) | pp. 163–167 read; proofs not audited | #13, #34 OK |
| LIT-511 | Mastroianni–Russo (2000) | AC copy: §1, §3 read (Thms 11–12 from page images); §2, appendix screened | #17 OK |

## MZ-SP

The per-citation scope check for MZ-SP was done by the internal exposition referee: [referee-sp-exposition.md](referee-sp-exposition.md), section on literature. It covered 12 citation occurrences of 9 keys: 10 OK, 2 NEEDS-SOFTENING (KLP18; ASV27) and 0 unsupported. Both softenings, and the addition of An–Wu 2022 (LIT-046) at its read scope, are applied ([response-internal-sp.md](response-internal-sp.md)). Bib keys in MZ-SP: BCDMVX06 (LIT-312), SVZ08 (LIT-427), Xu96 (LIT-314), CDMV07 (LIT-428), KLP18 (LIT-488), ASV27 (LIT-045), Wu26 (LIT-489), AW22 (LIT-046), MZ-CC. Unread and not cited (for AC, links in response-internal-sp.md): CDMV 2005, Sloan 1995, BDMVX 2007, CDMV 2008, Padua2DM, Erb 2016, An–Ran–Wu. Not resolver-checked: the DOIs of Xu96 and BCDMVX06.
