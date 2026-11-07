# Recent-source refresh, 2026-11-07

Status: **LITERATURE — bounded primary reading and discovery ledger**. Codex assigned source-triage developer; actual runtime model/effort metadata not exposed. Rules/input SHA: `f937bf2339ebcd7e81d6992d31b9c169cae9e22e`. No mathematical candidate was generated, so the candidate-generation novelty gate is inapplicable. No theorem is imported as a locally verified proof; no priority or universal absence conclusion follows.

Inputs consulted: `AGENTS.md`, `agents/WORKFLOW.md`, `agents/codex/CODEX.md`, `literature/INDEX.md` (including its Padua/recent-source rows), existing De Marchi 2022 and Białas-Cież–De Marchi–Suder 2026 records, and `topics/padua-literature-20261103/p1-comparison.md`. This note owns no shared registry, log, or Git operation.

## Target and bounded outcome

The searched targets were a proof of exact global Padua maximisers at the two unoccupied corners for every degree, and a sharp two-dimensional Padua expansion through the linear-log coefficient, constant, `-1/(n+1/2)` correction, and `O(log n/n²)` remainder. Fingerprints included `b=(8/pi²)(gamma+log(8/pi))`, `1.846160310423926...`, and `kappa`. Searches used generic published-topic words and constants only.

The primary passages actually read below supply historical corner observation, current numerical local-maxima work, and a distinct Morrow–Patterson upper-bound theorem/open corner question. They supply no matching proof or fine Padua expansion in those passages. This is a conclusion about this reading, not certification that such a result is absent from the literature. The earlier P1 comparisons retain their separate documented scope; this pass does not silently upgrade them.

## Primary checks and exact coverage

### De Marchi 2022 (existing LIT-326/377)

[Journal PDF](https://dergipark.org.tr/en/download/article-file/2240064), accessed 2026-11-07. Read first-page bibliographic data, Padua properties around (2.10) on journal p.18, and §3.3 with Fig.7 caption on pp.22–23. The DOI printed on p.14 is `10.33205/cma.1070020`; publication date is 3 March 2022. Section3.3(2), p.23, observes maxima at corners unoccupied by Padua nodes, within the open-problems list. This confirms attribution of the location statement, not an all-degree proof. Formula(2.10) reports order `O(log² n)`, not the target fine expansion. Remaining paper, figure pixels, and cited proofs were not reread. The unrelated `kappa` in Definition3.1, p.20, parametrises Lissajous phases; it does not identify the target constant.

### Białas-Cież–De Marchi–Suder 2026 (existing LIT-388)

[arXiv metadata](https://arxiv.org/abs/2605.23299) lists only v1, submitted 22 May 2026, and no journal reference on this access date. [Full text](https://arxiv.org/html/2605.23299v1), §§3.1–3.3, Remark2, Tables3–4, figure captions and §4, read 2026-11-07. These sections define Padua/MP families, report numerical local-maxima counts, and discuss additional nearby maxima. Section4's bivariate open question concerns their number/geometry. No exact global Padua argmax theorem or fine Padua expansion appears in these read sections. Section2 proofs were not reread.

The [author-hosted draft](https://www.math.unipd.it/~demarchi/papers/draftMP_RM.pdf) is accessible (13 pages). Read §§3–4, printed pp.8–10, including tables and Remark2; its corresponding bivariate scope agrees with the above. No whole-file/version equivalence is asserted: author order and layout differ. Figure pixels were not inspected. The capitalised `DraftMP_RM.pdf` link from the publications page returned404; lowercase succeeds. [Author bibliography](https://www.math.unipd.it/~demarchi/publications.html), Submitted heading, lists the May2026 draft. That listing and arXiv metadata are bounded update checks, not proof that no journal version exists elsewhere.

### Beberok–Białas-Cież–De Marchi, MP paper (existing LIT-378 context)

[Version of record](https://link.springer.com/article/10.1007/s00365-025-09710-x), accessed 2026-11-07: bibliographic footer gives publication/version-of-record 14 May 2025, issue February2026, *Constructive Approximation*63,31–65. Read Theorem4 statement (§6), end of its proof, §§7–7.1 and relevant references. Theorem4 gives the MP upper bound `O(n²)`. Section7 reports numerical all-corner maxima, while §7.1 explicitly leaves proving that corner attainment open. These concern MP nodes, not Padua nodes; neither the growth order nor the numerical location statement transfers merely because the families are related. Proof estimates were not independently checked.

[arXiv2412.14595v1](https://arxiv.org/html/2412.14595v1), Theorem4 and §7.1, and [author revision](https://www.math.unipd.it/~demarchi/papers/draftMP-R1.pdf), Theorem4 printed p.16, were also inspected for the statements. Their numbering differs in other places; no complete version comparison was performed. Initial DOI-resolver opening failed500 through its redirect; the author's online-version link subsequently opened journal HTML successfully. Journal PDF was not read.

### New adjacent discovery: Beberok 2025 lower bound

[Institutional record](https://rpt.atar.edu.pl/info/article/UAST2be6d4fb65c04b6390fb1af209906842/), read 2026-11-07, identifies *A lower bound for the Lebesgue constant of the Morrow–Patterson points*, Tomasz Beberok, *Journal of Approximation Theory*311(2025), pp.1–7, DOI[10.1016/j.jat.2025.106191](https://doi.org/10.1016/j.jat.2025.106191). Its abstract's mathematical expressions are missing in the rendered record. DOI opening failed with tool inaccessibility. **Full text unread; lower-bound magnitude, hypotheses, and any exact corner statement unverified here.** This is a concrete follow-up acquisition lead for MP context, not a completed targeted priority audit or a Padua match.

## Author-page sweep

Read De Marchi's [research themes](https://www.math.unipd.it/~demarchi/research.html), recent/submitted bibliography rows, and Vianello's [Padua/Lissajous bibliography](https://www.math.unipd.it/~marcov/padua.html), its introductory description and complete short papers/codes list. The latter lists Padua/Lissajous papers through2017; this bounds that page only. The recent De Marchi rows point to the geometry draft and MP journal article inspected above. Author pages are discovery/status sources; their descriptions are not substitutes for paper proofs.

## Executed web-query ledger

All queries below were issued on2026-11-07 through the available `mcp__codex_apps__search_service_web_run` connector; search results/snippets were discovery only. Exact strings are retained so a later reader can repeat the search, subject to changing indexing. No external uploads, author contacts, raw downloads, source-code execution, or numerical experiments occurred.

| Query strings (each executed) | Discovery/reading disposition |
|---|---|
| `"2605.23299"`; `"On the Lebesgue constant of the Morrow" 2025`; `De Marchi 2022 Padua points survey Lebesgue corners` | Primary arXiv, survey PDF, author pages followed above. |
| `Padua "Lebesgue" "1.846160310423926"`; `Padua Lebesgue constant "gamma" "8" asymptotic expansion`; `Padua Lebesgue maxima corners proof 2025 2026` | Fine-constant query gave no usable target lead; broad expansion query rediscovered KL2021 and one-dimensional/Fourier contexts. Corner query produced substantial irrelevant football noise, so it cannot support a meaningful absence claim. |
| `"Padua" "Lebesgue" "corner" proof 2026`; `"Padua" "Lebesgue" "kappa"`; `"Padua" "Lebesgue" "1.846160"` | Survey/MP paper close matches followed; no target fine-coefficient primary passage identified. |
| `"Padua" "Lebesgue" "linear" "constant" asymptotic 2024 2025 2026`; `"Padua" "Lebesgue" "n+1/2"`; `"Geometric properties of the Lebesgue function" -site:scirate.com -site:researchgate.net -site:arxiv.org` | Geometry author draft followed. Extended interpolation2025 and histopolation2026 appeared as adjacent titles; full texts unread here and not cleared as priority matches. |
| `"Padua" "Lebesgue" "log" "constant term"`; `"Padua" "Lebesgue" "8/pi" gamma`; `"Padua" "Lebesgue" "-1" "asymptotic expansion"`; `"De Marchi" "Padua points and" "cited" 2026` | KL2021 and classical 1D summaries appeared. No new primary fine Padua expansion passage was identified/read. Citation wording was a discovery query, not a citation-index audit. |
| `"A lower bound for the Lebesgue constant of the Morrow-Patterson points"`; `"Padua" "Lebesgue" "log(n)/n"`; `"Padua" "Lebesgue" "1.846160310423926"` | Lower-bound institutional record followed; exact-constant repeat added no usable lead. |

## Limits and integration recommendation

This pass supports preserving the distinction between an observed/conjectured Padua corner location and a proved exact all-degree argmax, and between MP, 1D Chebyshev/Fourier, and 2D Padua asymptotics. A shared formula fragment such as `gamma+log(8/pi)` does not identify the operator or establish the target coefficient. No inference was made by squaring a 1D formula.

This was not a systematic cited-by audit: no complete MathSciNet, zbMATH, Scholar, OpenAlex or Crossref citation graph was obtained, and absence of a Cited-by string in the MP HTML is not a citation count. Current arXiv/author pages were checked as described. Unread adjacent results remain acquisition leads. No new LIT identifiers, priority wording, proof statuses, or global claims were assigned. Only this authored report is a repository artifact; no third-party full text is retained.
