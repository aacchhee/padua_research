# Bounded literature screen — sharp MZ campaign

Rules/input: `2143ad622fa98faf8fe7d5cb8ed2bb7e0062f861`; 2026-11-06. Codex literature support worker; model metadata unavailable in runtime. Scope: attribution/access checks for handoff 01, with one usable operator reference. No novelty claim or proposed new mechanism, so the novelty-candidate gate does not apply. No PD proof-status upgrade, exhaustive search claim, or third-party text/PDF deposited.

## Outcome for the campaign

The handoff's Hilbert-norm expansion remains **unverified against the cited original sources in this pass**. In particular, do not describe K1's pre-registered correction terms as a verified “Widom–Wilf form.” Retain the numerical ansatz as the handoff's chosen ansatz, pending primary verification. A source's big-O claim would in any event not supply an explicit computable error constant automatically.

The one fully read admissible source is [LIT?mz-sharp-codex-01](literature/basor-ehrhardt-1999.md). Its same-symbol and even-symbol hypotheses matter. It offers exact operator-norm constants, but does not identify the campaign endpoint operator or give its finite-N error. The source record contains the exact relevant statement/locators; no formula is imported as local proof.

## Classical references and access limits

| Source | Access/read actually achieved | Consequence |
|---|---|---|
| de Bruijn–Wilf, *On Hilbert's inequality in n dimensions*, Bull. AMS68(1962),70–73, [DOI](https://doi.org/10.1090/S0002-9904-1962-10726-5) | [TU/e publisher PDF](https://pure.tue.nl/ws/files/2444401/597527.pdf) retrieved by browser; extraction contains repository cover only. Article pp70–73 are scanned. Browser screenshot calls for all four pages returned textual `ImageDisplayed` placeholders without image payload; no article content could be visually read. Shell curl failed to connect to configured proxy. | Metadata verified from institutional primary record; expansion, hypotheses, theorem numbering and error constants **not verified**. No new LIT ID. |
| Widom–Wilf, *Small eigenvalues of large Hankel matrices*, Proc. AMS17(1966),338–344, [DOI](https://doi.org/10.1090/S0002-9939-1966-0189237-7) | [AMS PDF](https://www.ams.org/proc/1966-017-02/S0002-9939-1966-0189237-7/S0002-9939-1966-0189237-7.pdf) returned403; alternate journal path inaccessible. Author reprint index returned403. Existing INDEX row LIT-054 found; linked record absent from selected snapshot. | Original theorem unread; no new LIT ID and no original theorem asserted. There is a material attribution mismatch warning, described below. |
| Wilf, *Finite Sections of Some Classical Inequalities* (1970), [Springer DOI/journal page](https://link.springer.com/book/10.1007/978-3-642-86712-5) | Publisher overview and chapter listing read; book requires institutional access. Relevant chapter [Sections of Toeplitz and Hilbert Forms](https://link.springer.com/chapter/10.1007/978-3-642-86712-5_2), pp11–40, landing page only. | No chapter body read, no source theorem or constant verified, no LIT ID. |

### Specific conflation warning

A directly readable later primary paper, [Zhu–Chen–Emmart–Weems, arXiv1803.11324v1](https://arxiv.org/html/1803.11324v1), Introduction and opening §2 only, reports Widom–Wilf1966 as a smallest moment-Hankel eigenvalue asymptotic of the form A√N B⁻ᴺ for positive interval weights satisfying a Szegő condition. It distinguishes the Hilbert matrix as a special moment matrix and flags a factor correction to WW Lemma2. This is secondary attribution to WW, **not verification of WW's theorem**, and receives no LIT ID because the whole later paper was not read. Search also located a 1968 erratum; its content was not read.

Consequently the handoff appears to group a smallest-Hankel-eigenvalue source with a largest-Hilbert-eigenvalue/norm-deficit assertion. Those quantities cannot be interchanged. The original WW text and erratum must be obtained before deciding exactly what portions, if any, support the asserted norm expansion. No theorem-level accusation about the unread original is made here.

## Search/read provenance and remaining obligations

Read AGENTS.md, agents/WORKFLOW.md, agents/codex/CODEX.md, handoff01 and p2-comparison; searched INDEX for Hilbert/Widom/Wilf/Bruijn/Basor/Ehrhardt/Toeplitz before sources. The selected workspace is a nongit snapshot; source SHA comes from input-snapshot.json, not a fabricated local Git command. Only the coordinator controls Git.

Used discovered `search_service_web_run` browser tool for batched author/title queries, direct primary opens and PDF screenshot attempts. Source-readable coverage: Basor–Ehrhardt primary extracted text lines0–821 in overlapping windows covering the entire16-page paper; all proofs/references read. Its external references are discovery leads only: Böttcher–Silbermann1990 §§4.95–4.102, Power1979, Roch–Silbermann1988, Spitkovsky–Tashbaev1991 were not opened/read. Kac–Murdock–Szegő and Widom extreme-eigenvalue sources were not pursued in this bounded pass.

Remaining: readable de Bruijn–Wilf article images/OCR; WW1966 plus1968 erratum; Wilf1970 chapter body if its quantitative theorem is needed. Obtain via ordinary public source or owner-supplied authorized copy; no access-control bypass attempted. Until then, no exact classical theorem assumptions or effective asymptotic error constant can be certified by this report.
