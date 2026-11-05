# Bounded audit: P4 and DOI sample

Auditor: Codex subagent `/root/audit_p4_links`; requested model/effort gpt-6-astra high, inherited from parent (runtime does not independently expose a model identifier). Date: 2026-11-05. Snapshot: `890f56ccde35431b70b43141c224b0b8817fea7f`; mathematical/source outputs input `a6302fb59f7b24242ca3b850fdd78c15753878b6`. No Git operations or development edits performed.

Read AGENTS.md, CODEX.md, relevant WORKFLOW text, handoff04, p4-memo, P4 assessment/addenda and Van Barel/FHV records, P4 proposed changes and BibTeX. Read INDEX rows LIT-346–348,118,119,420 and relevant IDEAS rows (IDEA-090,094,095,097,098,100,117 plus aliases). Root and other agents handle the complete IDEAS read. No novelty generation performed.

## Findings requiring response

1. **P2: scope the bivariate-downdating absence claim.** `topics/padua-literature-20261103/p4-memo.md:39` says nobody has downdating for bivariate OPs. The source searches establish only that the inspected recent Leuven papers do not treat it. Moreover, the existing registry's IDEA-094 (state/IDEAS.md:654) treats stored-Q bivariate downdating by QR row deletion as settled background, while IDEA-095 (:655) identifies Q-free bivariate downdating with classical R-factor downdating. This statement can mislead the proposed joint project's scope. Restrict it to the particular structured IEP/eigenvector extension actually absent from the inspected corpus, and explicitly distinguish the existing classical routes. Similarly qualify p4-memo.md:7's inference that the field is open on their side. No claim of a newly discovered external counterexample is made.

2. **P2: reconcile the Laurie correction with the introduction, including source version.** `addenda/faghih-et-al-2025.addendum.md:11` rejects the previous author-limited statement that the authors know no extension, based on section 7 alone. However [arXiv 2506.19796v2](https://arxiv.org/html/2506.19796v2), introduction (HTML line81), explicitly reports the authors' lack of awareness of a MOP extension. Section7 (lines2191–2192) also proposes a continued-fraction extension; these statements coexist. The correction propagates into `proposed-record-changes.md:117,187,320` and the assessment's correction paragraph. The journal PDF could not be reread (web-tool access failure); therefore this finding does not assert the published text is identical. Recheck journal section1, preserve the properly attributed author-limited statement if still present, or document the version difference. Do not infer universal nonexistence from author unawareness.

## P4 primary-source checks actually completed

- [2506.19796v2](https://arxiv.org/html/2506.19796v2), sections1,6.2,7: the source reports the reorthogonalized/core stability distinction, investigated at finite N, and discusses the listed future directions. Corroborates the substance of the LIT-347/119 stability correction; no general backward-stability theorem inferred. Journal pagination and algorithm locators not independently confirmed.
- [2302.00355v1](https://arxiv.org/html/2302.00355v1), title/authors and section3.2: confirms exactly three authors, excluding Faghih, and the RQ/QR weight-condition distinction. Corroborates LIT-346. Journal full text not accessed (ScienceDirect403).
- [2608.25758v1](https://arxiv.org/html/2608.25758v1), introduction, section5.1 and section6: confirms the finite experiment's scaling/update comparison and the future-work list, including stability analysis. Corroborates LIT-118. No general conditioning theorem inferred.
- [1406.0364v2](https://arxiv.org/html/1406.0364v2), abstract, Maple procedures, section3.3 and Theorem3.3: confirms two conversion problems and the distinct-nearest-neighbour-coefficient hypothesis. Searches for stable, error, accuracy returned no matches. Corroborates the FHV half of LIT-420; ADY half not reread. Journal bibliographic metadata and abstract agree; journal theorem pagination not independently read.
- P4 memo labels all three joint questions as unregistered later-topic proposals; changed-file list supplied by root includes no state/IDEAS modification. This satisfies the no-new-IDEA scope, subject to the wording finding above.

## DOI sample: ten attempted Crossref rechecks

All ten exact `https://api.crossref.org/works/<DOI>` opens failed with the web tool's inaccessible/Internal Error response. This is an access limitation, not evidence against the DOIs and not a completed Crossref verification. Used exact DOI searches and primary publisher/author-hosted metadata as a narrower fallback:

| DOI | Independent fallback actually seen | Outcome |
|---|---|---|
| 10.1137/25M1770965 | SIAM abstract page, authors and journal issue metadata | agrees with title, five authors, 64(4),1190–1216,2026 |
| 10.1016/j.apnum.2023.07.009 | ScienceDirect indexed metadata; arXiv title/authors | agrees with title and three-author attribution; publisher page open403 |
| 10.1007/s11075-025-02149-y | Springer article page | agrees with title, four authors,100,1837–1865,2025 |
| 10.1002/nla.70017 | Wiley indexed publisher metadata | agrees with title,32,e70017,2025; direct publisher and institutional opens failed |
| 10.1007/s00211-023-01379-3 | Springer article page | agrees with title,N.Van Buggenhout,155,415–443,2023 |
| 10.1016/j.cam.2024.116109 | ScienceDirect indexed publisher metadata and CNR-hosted journal PDF first-page search excerpt | agrees with title,451,116109,2024; direct publisher open403 |
| 10.1007/s11075-024-01785-0 | Springer article page | agrees with three authors,title,100,621–643,2025; online2024 distinguished |
| 10.1007/s11075-024-01767-2 | Springer article page | agrees with W.Van Assche,title,100,599–620,2025; online2024 distinguished |
| 10.1007/s11075-015-9959-8 | Springer article page | agrees with three authors,title,70,519–543,2015 |
| 10.1007/s11075-023-01600-2 | Springer article page | agrees with four authors,title,95,1079–1102,2024; online2023 distinguished |

Publisher URL patterns used for Springer above were https://link.springer.com/article/<DOI>; SIAM https://epubs.siam.org/doi/abs/10.1137/25M1770965; Wiley https://onlinelibrary.wiley.com/doi/10.1002/nla.70017. ScienceDirect source URLs were https://www.sciencedirect.com/science/article/abs/pii/S0168927423001927 and https://www.sciencedirect.com/science/article/pii/S0377042724003583. CNR excerpt: https://iris.cnr.it/retrieve/e61925e0-5dda-4495-acca-e5cf50ecb2e5/JCAM_2024_TNWP.pdf .

Queries actually run: each of the ten DOI strings above, individually quoted in web search (batched in groups of four or two). Primary-source opens and find terms are listed above. No captcha bypass, alternate network route, or code download performed. No computational rerun in this bounded task. No DOI mismatch found within this sample, but handoff04's direct-Crossref and all-links provenance requirements remain uncompleted.

## Disposition and limits

P4 requires response to the two scoped findings. Core stability, authorship/RQ, future-work and FHV conversion corrections are corroborated in accessible primary preprints. This is not a clean audit of all P4 material: journal full-text locators, every negative keyword claim, every quotation length, publisher-link Crossref provenance, and all DOI metadata were not exhaustively checked. Findings concern literature wording; they do not change a PD theorem status.
