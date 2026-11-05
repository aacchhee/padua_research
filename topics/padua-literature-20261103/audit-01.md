# Audit 01 — Padua literature campaign, including pass 2

- Auditor/orchestrator: Codex, 2026-11-05. Requested configuration: `gpt-6-astra high`; serving model identity and effective effort are not independently exposed by this runtime. Four bounded Codex readers inherited that requested configuration.
- Rules read at `890f56ccde35431b70b43141c224b0b8817fea7f`: AGENTS.md, agents/WORKFLOW.md, agents/codex/CODEX.md. Role: independent auditor of Claude development.
- Scientific input: `a6302fb59f7b24242ca3b850fdd78c15753878b6`; publishing/handoff head: `890f56ccde35431b70b43141c224b0b8817fea7f`. Handoff 04 adds no scientific changes to that input.
- Original base: `440d1079e42c3ef21c40d1cf8870f5b206410c6a`. Refreshed main: `21dbfc90257b952d8923f6d01739d12aa8d6e0a1`, three commits ahead of that base. Audit stays pinned; merge reconciliation belongs to the response before further development/preparation.
- **Disposition: CHANGES REQUESTED; stage WORK.** Six findings below require a developer response. Mandatory primary-source checks remain incomplete. This is a completed bounded audit with findings and explicit coverage limits, not acceptance or readiness.

## Coverage and provenance

The Git shell could not connect to the configured proxy. GitHub connector reads supplied all 70 changed files and seven rule/context files at one pinned head; `check/audit-inputs.json` lists every fetched path and original Git blob identity. Exact UTF-8 bytes were verified against those identities. No papers or extracted third-party text are committed. Publication uses the GitHub connector with a checked parent and a fast-forward branch update.

Read the log, handoffs 01/04, report, four pack memos, inventory, DOWNLOADS, reservation, checks, and relevant records/addenda/proposed edits. The full 890-line `state/IDEAS.md` was read across the audit team in untruncated chunks: P1 reader lines 1–270 and 561–890; P3 reader 271–560. This is a complete team read, not a claim that the orchestrator personally read every line. Relevant INDEX/CORPUS entries, prior F6 locator qualification, and local PD-T057 / exact-section-versus-actual-run context were reviewed. Existing MZ obstruction scopes, classical downdating dispositions and provisional/final aliases were preserved. No new idea was generated, no final ID assigned, and no PD proof status changed.

Detailed source URLs, independent search queries, inspected portions and failed accesses are in [P1](audit-support/p1.md), [P2](audit-support/p2.md), [P3](audit-support/p3.md), and [P4/links](audit-support/p4-links.md). Those are audit notes, not inherited proof certificates. Nine P1 new records were sampled for reading-coverage honesty; Pimenova's unconfirmed constant and OCR-only qualifications remain explicit. No obvious unmarked long quotation was found in the sample. An exhaustive source-to-record word comparison was not possible for inaccessible papers; the blanket 15-word check is not certified.

## Findings requiring response

### F1 — P2: provide the corner lower-bound attribution bridge

Location: `topics/padua-literature-20261103/p1-comparison.md:37`, proposed wording at line 51, and copied report/results/PR statements.

The KL global theorem gives the corner upper estimate. Its checked lower-bound construction, arXiv v1 §4 (4.8), evaluates angular coordinates `(π/m,0)`, which map to the noncorner point `(cos(π/m),1)`. A lower bound near a corner does not itself give a lower bound at the corner. The comparison's “at or near” wording does not supply the needed transfer. Write the exact parity/symmetrisation argument from the cited equations if the matching corner leading term is to be attributed as implied, or restrict IMPLIES PART to the upper estimate and attribute the published coefficient to the global constant. Do not claim the leading term is newly discovered on this basis. This finding does not challenge PD-T156/157 or assert that a transfer is impossible. [KL primary PDF](https://arxiv.org/pdf/2009.07114).

### F2 — P2: restore Theorem 9's powered weight hypothesis

Location: `literature/records/mastroianni-russo-2000.md:20`.

The recorded assumption is `u/√(wφ) ∈ A_p`; the author-uploaded source, Theorem 9 (copy p. 18) and its dual-weight proof (copy p. 20), requires `(u/√(wφ))^p ∈ A_p`. Omitting the exponent weakens the stated theorem. For example, at p=2 with Chebyshev-first-kind w, `wφ=1`; `u=(1−x)^(3/4)` belongs to A2 whereas u² does not. Correct the transcription and any copies. The separate Theorem 11 endpoint specialization is not invalidated by this correction. [Author-uploaded primary PDF](https://www.researchgate.net/profile/Maria-Russo-8/publication/235443994_Weighted_Marcinkiewicz_inequalities_and_boundedness_of_the_Lagrange_operator/links/02e7e516597adb0052000000/Weighted-Marcinkiewicz-inequalities-and-boundedness-of-the-Lagrange-operator.pdf).

### F3 — P2: scope the absence of rates to the MZ constant

Location: the same record, lines 10/16, and unqualified “no rates” summaries in the P2 memo, report and proposed INDEX row.

The source does contain approximation-error rates in Theorems 14–17, as the record itself acknowledges at line 28. The paper-wide assertion that there is no rate-type estimate is false. Narrow it to the missing quantitative borderline decay estimate for the CC MZ minimum, while retaining the uniform-constant comparison and separately describing the Sobolev/Besov approximation rates. A search for the substring “log” cannot support the broader assertion. The bounded RELATED verdict survives this correction.

### F4 — P2: correct the dimension term in Möller's bound

Location: `topics/padua-literature-20261103/addenda/dunkl-xu-2014.addendum.md:14`.

The dimension term is `dim Π²_(n−1)`, not `dim Π_(2n−1)`. The latter materially overstates the number of cubature nodes. Xu's primary author-hosted Fields survey, equation (5.4), displays the bivariate superscript and the degree subscript separately. A one-node centered degree-one rule also contradicts the recorded version at n=1. Fix the transcription and any copied display; retain the correct commutator rank term and locator. This is a literature-record error, not a finding against a local PD proof. [Xu survey](https://pages.uoregon.edu/yuan/paper/fields.pdf).

### F5 — P2: narrow the bivariate-downdating absence claim

Location: `topics/padua-literature-20261103/p4-memo.md:39`, related opening inference at line 7.

The memo's assertion that nobody has bivariate OP downdating exceeds the inspected-source search. Existing IDEA-094/095 already classify stored-Q row-deletion and Q-free/R-factor downdating as classical background (`state/IDEAS.md:654–655`). Define the particular structured IEP/eigenvector extension that the proposed question would investigate, distinguish those classical routes, and state only what was absent from the inspected Leuven sources. No new IDEA should be registered in this literature topic.

### F6 — P2: reconcile the Laurie correction with the introduction/version

Location: `topics/padua-literature-20261103/addenda/faghih-et-al-2025.addendum.md:11`; propagated proposed changes at lines 117/187/320 and the assessment note.

The correction rejects the prior author-limited lack-of-awareness statement using §7. However, arXiv 2506.19796v2 explicitly states that lack of awareness in its introduction, while §7 proposes a continued-fraction extension. Those two statements coexist. Recheck the published introduction: retain the accurately attributed statement if present, or document the version difference. Neither author's unawareness nor a future-work proposal establishes universal nonexistence. The journal introduction was not independently accessible here. [Primary preprint](https://arxiv.org/html/2506.19796v2).

## Per-pack dispositions and unresolved source checks

| Pack | Corroborated within this audit | Disposition / remaining limits |
|---|---|---|
| P1 | 2008 poster calls vertex attainment conjectural; KL global theorem and v1 locators; bounded independent searches found no matching corner proof/exact formula/second-term theorem | F1 requires response. De Marchi 2022 p.23, Kuznetsova theorem page and Pimenova images were not independently reread. Search snippets do not replace those reads. No exhaustive novelty conclusion. |
| P2 | SVZ author preprint signed rule/exactness/Table 1; independent numerical rerun; Mastroianni Theorems 9–12 text and CC specialization; five A14 journal locators in author-hosted published PDF | F2/F3 require response. SVZ journal pp.417/421, the Mastroianni p.23 visual check, and mandatory Xu 1996 journal p.231 remain unchecked. |
| P3 | Zhu–Nakatsukasa v2 Remark5.1(5) and scope distinction; Xu author notes corroborate classical full-sequence Favard/commuting conditions; exact-section vs actual-run quantities remain distinct | F4 requires response. Greenbaum original p.51, Xu TAMS 342/343 theorem pages and Dunkl–Xu chapter theorem pages remain unchecked. Alternative primary notes do not verify those locators. |
| P4 | Four primary preprints corroborate core/reorthogonalized stability observations, three authors/RQ, future-work list, and FHV conversion hypotheses; proposals unregistered | F5/F6 require response. Journal pagination/version claims and all nine-source negative screens were not exhaustively repeated. |

The mandatory Xu check is especially significant: the accessible 16-page author preprint states Theorem 3.3 with `1<p≤∞`, while the proposed journal correction says `1<p<∞`. This is **unresolved version evidence**, not a demonstrated false journal correction. Inspect the actual journal p.231 before accepting the edit. Five A14 locators were checked against the published author-hosted JAT PDF (journal headers 15–25): Lemma1/Theorem1 p.19, degree2n−1 remark/Theorem2 p.20, Lemma2 p.22. That does not complete the A11–A14 or mandatory Xu review.

The Mastroianni Theorem 11 text supports the recorded node specialization and excluded A2 endpoint; the book-page mapping remains inferred. Screenshot calls returned textual image markers without visible image content to the reader, so no visual verification is claimed. Primary-source access gaps are not evidence that the developer's readings were false. Resolve them through inspectable sources or carry them explicitly into any later acceptance decision.

## Executed checks and reservation

Commands executed by the orchestrator in the pinned-file workspace:

```sh
python3 -I topics/padua-literature-20261103/check/svz_table1.py
python3 -I topics/padua-literature-20261103/check/audit_old_blocks.py --repo /workspace/padua_research --proposal topics/padua-literature-20261103/proposed-record-changes.md
```

Environment: Python3.12.14, NumPy2.3.5, Linux x86_64. SVZ input code blob `26cca392cccec5f8a422992b7e5a2f2b87a09f8c`; deterministic prescribed meshes, no RNG. The corrected sums are 4 within 2e−15; printed-denominator sums equal `4m/(m+2)` at m=5,10,…,40. Excess absolute sums: .0415,.00250,.000886,.000239,.000138,.0000568,.0000397,.0000201. Two negative weights occur at each sampled mesh. These agree with the author preprint Table1 at the printed precision. This is floating-point consistency evidence, not a computer proof or independent inspection of the journal's misprint. Short rerun output and code/check identities are retained in `check/audit-checks.json`.

The literal checker found **60 Old blocks, zero missing at base440d107**. Manual target inspection includes the repeated generic history/locator blocks and pass-2 edits. This verifies base substring applicability, not a full sequential application or a merged-current-main rehearsal. Some instructions are appends rather than Old/New blocks and are outside that mechanical count. No proposal was applied.

GitHub compare of base440d107 to scientific input returns 69 additions only: topic files, its results file and 24 new records. Publishing handoff04 brings the retrieved set to70. No shared registry, existing scientific file, `.github/`, or main branch was edited by the development input. This confirms the claimed scope and no-new-IDEA registration.

Fresh open PR population: 21/22/24; all returned closed PRs are merged, including19/20/23. `check/audit-reservations.json` pins four complete registry copies per current head and the applicable inherited/own ledgers. Qualified three-digit LIT references were scanned, excluding foreign four-digit BTTB aliases. Existing reservations remain disjoint: 466–473,474–481,**482–561 (this topic)**,562–573,574–581,582–593. No new reservation, inferred provisional offset or final assignment was made. Refresh again at preparation, including PR22's accepted same-source mappings, before allocating source IDs.

Ten DOI rechecks were attempted directly against Crossref; all endpoint opens failed. Fallback exact-DOI searches and publisher/author metadata agreed within the sample (detailed table in P4 notes), but two rely on indexed publisher excerpts. **Direct Crossref verification and provenance of every publisher link remain incomplete.** No guessed-link assurance is inferred from that fallback.

## Next step

Claude should answer F1–F6 individually in response-01.md, repair source records and propagated wording, reconcile current main without rewriting published history, and preserve every unchecked-source limitation. Material changes return to Codex audit; do not apply shared registry proposals or assign final IDs yet. Handoff05 carries the full instruction. Only AC merges.
