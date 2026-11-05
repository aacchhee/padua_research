# Same-source literature reconciliation — PR22 preparation

Date: 2026-11-05. Mechanical developer: Codex; dispatched gpt-6.1-sol medium;
backend metadata not exposed. Rules/input head: `4270d34abffdb83f33bbb811fb5b18e71809b14c`.
Read AGENTS.md, agents/WORKFLOW.md, agents/codex/CODEX.md and handoff05.
No novelty gate is required for this mechanical source-identity crosswalk: no
candidate, novelty claim, source theorem, status or reading scope is added.
No primary source was opened. Git operations were read-only. Only this file
and literature-map.json belong to this worker.

Pinned main: `21dbfc90257b952d8923f6d01739d12aa8d6e0a1`.
Pinned PR21: `890f56ccde35431b70b43141c224b0b8817fea7f`.
The JSON is a recommendation, not an allocation. Seven new IDs are recommended
(LIT-562–568), five aliases reuse existing IDs; LIT-569–573 remain reserved gaps
if the orchestrator accepts this map. All twelve local aliases are retained.

## PR21 allocation check

At the pinned PR21 head, topics/padua-literature-20261103/ALLOCATIONS.md says
**“No final IDs are assigned yet.”** Its range is LIT-482–561. The pinned
INDEX and ID_CROSSWALK contain no final assignments for its provisional
campaign statements. In particular provisional82 is not a numeric offset
from the reservation. No LIT-563 (or other inferred PR21 final ID) is invented.
The existing main IDs take precedence for already registered sources.

The essential source statements and bounded reading provenance are already
local in [literature.md](../literature.md) and
[source-recheck-01.md](../source-recheck-01.md); these do not require merging
PR21 to inspect. Pinned PR21 paths below document correspondence and historical
provenance only. PR22 can add its own coverage addendum/crosswalk against main
without copying or upgrading PR21's unmerged edits. Before PR21 later assigns
IDs it must preserve these existing same-source IDs and this crosswalk.

## All twelve aliases

`NN` below abbreviates `LIT?nn-mop-iep-codex-NN`. Locators are source-version
pages, not a claim that journal pagination was read. Each entry retains its
full original statement in literature.md; this receipt only reconciles identity.

| Alias | Source identity | Decision | Main/PR21 record correspondence |
|---|---|---|---|
| 01 | FHV 2015; arXiv:1406.0364v2 | LIT-420 | Main INDEX LIT-420, FHV half; CORPUS key filipuk-haneczok-vanassche-2015. PR21 literature/records/filipuk-haneczok-vanassche-2015.md provisional82; matching addenda/filipuk-haneczok-vanassche-2015.addendum.md. |
| 02 | Van Assche 2011; arXiv:1104.3778v1 | LIT-562 recommended, unassigned | Absent from both pinned INDEX/CORPUS and matching literature/campaign records; new source key vanassche-2011. |
| 03 | Aptekarev–Denisov–Yattselev 2020; arXiv:1806.10531v1 | LIT-420 | Main INDEX LIT-420, ADY half; CORPUS key aptekarev-denisov-yattselev-2020. PR21 FHV addendum explicitly leaves this half unverified; no campaign ADY record located. |
| 04 | Denisov–Yattselev tree spectral theory; arXiv:2008.08210 | LIT-563 recommended, unassigned | Absent from both pinned INDEX/CORPUS and matching literature/campaign records; new source key denisov-yattselev-2020. |
| 05 | Aptekarev–Denisov–Yattselev Angelesco asymptotics; arXiv:2004.04113v2 | LIT-564 recommended, unassigned | Absent from both pinned INDEX/CORPUS and matching literature/campaign records; new source key aptekarev-denisov-yattselev-2021. |
| 06 | Aptekarev–Derevyagin–Van Assche 2016; arXiv:1409.4053v2 | LIT-565 recommended, unassigned | Absent from both pinned INDEX/CORPUS and matching literature/campaign records; new source key aptekarev-derevyagin-vanassche-2016. |
| 07 | Aptekarev–Derevyagin–Van Assche 2015; arXiv:1410.1332v2 | LIT-566 recommended, unassigned | Absent from both pinned INDEX/CORPUS and matching literature/campaign records; new source key aptekarev-derevyagin-vanassche-2015. |
| 08 | Aptekarev–Derevyagin–Miki–Van Assche 2016; arXiv:1511.08098v3 | LIT-567 recommended, unassigned | Absent from both pinned INDEX/CORPUS and matching literature/campaign records; new source key aptekarev-derevyagin-miki-vanassche-2016. |
| 09 | Kozhan–Vaktnäs Christoffel transform; arXiv:2407.13946v2 | LIT-568 recommended, unassigned | Absent from both pinned INDEX/CORPUS and matching literature/campaign records; new source key kozhan-vaktnas-2026. |
| 10 | Van Barel–Van Buggenhout–Vandebril 2024; arXiv:2302.00355 | LIT-346 | Main INDEX LIT-346; CORPUS vanbarel-vanbuggenhout-vandebril-2023. PR21 literature/records/vanbarel-vanbuggenhout-vandebril-2023.md provisional75–77 and matching addendum. |
| 11 | Faghih et al. SINUM 2026; arXiv:2506.19796 | LIT-119; retain related LIT-347 | Main literature/records/faghih-et-al-2025.md LIT-119; INDEX LIT-347 also retained. PR21 topics/padua-literature-20261103/notes/faghih-sinum-2026-assessment.md explicitly names both IDs. |
| 12 | Faghih–Van Barel–Vandebril 2026; arXiv:2608.25758v1 | LIT-348; retain related LIT-117, LIT-118 | Main literature/records/faghih-vanbarel-vandebril-2026.md LIT-117/118; INDEX LIT-348 retained as canonical broad updating statement. PR21 topics/padua-literature-20261103/addenda/faghih-vanbarel-vandebril-2026.addendum.md provisional70–74 explicitly reuses all three. |

The two uses of LIT-420 identify the two sources already combined in that
accepted record; they do not equate the papers. Addenda must name which half
they cover. Existing per-statement IDs 117/118/348 and 119/347 are historical
accepted IDs: choosing a canonical lookup for this topic neither deletes nor
renumbers the others. The older secondary rows retain their original
provenance; this topic's bounded primary reading is credited separately.

## Bounded coverage preserved

The following is an index to the existing ledger, not new reading. Original
reader attribution remains in literature.md. Claude audit-01 could not reach
the primaries; developer-only primary checks are not retroactively independent
Claude verification. Acceptance in audit-02 does not expand source coverage.

- **01**: §§2.1–2.2 pp.4–12; §3.1 pp.14–17; §3.3 pp.19–21, (3.11)–(3.14); response recheck §3.1 Thm3.1 (3.3)–(3.10) pp.16–18 and §3.3 Thm3.3 (3.11)–(3.15) pp.20–21, full inductions. 01: Codex primary bounded reading and response recheck; earlier §2 coverage retained; Maple/code not executed.
- **02**: §2 Thm2.2 pp.7–8; §3 Thm3.1/(3.5) pp.8–10; recheck (3.1)–(3.5) pp.9–10 and normality/(2.12) pp.2–3,9. 02: Codex primary bounded reading; general-r proof, later examples and external Riemann–Hilbert dependencies remain unread.
- **03**: §§1.1–1.3 pp.1–5; §3.1 pp.8–10; selected §3.3; (1.17). 03: Codex primary bounded reading only; spectral identities and later asymptotics not fully checked; no response recheck.
- **04**: Abstract, contents, introduction pp.1–3 only. 04: reconnaissance only; Parts1–4 and publication metadata not checked.
- **05**: Abstract, contents, introduction pp.1–2 only. 05: reconnaissance only; theorem proofs and journal metadata unchecked; no theorem used as local dependency.
- **06**: Thm1.1/1.1′ pp.1–4; §4 pp.12–14 incl.Prop4.5/proof; §5 boundary problem/Prop5.1 statement pp.14–16. 06: Codex primary bounded reading; intervening framework, remaining algorithms and examples not fully read; no response recheck.
- **07**: Abstract and introductory operator formulation pp.1–2 only. 07: introductory report only; commutation/symmetrisation theorems and proofs unread; DOI not independently verified.
- **08**: pp.1–3 through Thm1.1/inverse discussion; selected determinants p.9; §3.1 pp.13–16; §3.2 Prop3.2/proof pp.16–17; selected r=2 equations pp.22–23. 08: Codex primary bounded reading; full continuous/discrete Lax proofs and examples incomplete; no response recheck.
- **09**: Initial §§2.4 pp.6–8, §3.2 Thms3.5–3.6 pp.15–16 and §3.8 Thm3.19 pp.24–25; response recheck §2.2 p.5, Def2.8 p.8, Lemma2.18(b)/proof p.11, Thm3.6/proof/Remarks3.7–3.8 pp.16–17. 09: Codex primary 19-Nov-2025 arXiv version; journal metadata checked separately; Thm3.19 not rechecked in response; factorization proof incomplete.
- **10**: Campaign-reported arXiv pp.11–12,18–19,21–25. 10: campaign-mediated report at d669363; no fresh primary check.
- **11**: Problems3.5/3.6 p.1197; algorithms §§4–5; §7 p.1213. 11: campaign assessment at d669363, Claude P4 selected primary coverage; no fresh primary/code check.
- **12**: Problem3.1/Lemma3.1 pp.7–10; scaling pp.10–11; experiments pp.20–22; conclusion p.24; developer response recheck Examples5.1–5.2 p.20. 12: campaign-mediated fulltext report at d669363; developer primary recheck p.20 validates inputs only, no algorithm/error reproduction.

In particular 03–08 and the KV Thm3.19 report are not upgraded by the response
recheck. For 10/11 the record remains campaign-mediated; 12 has only the
explicit developer p.20 input check beyond that campaign coverage. No source
algorithm, source error curve or stability result was reproduced here.

## Reproducible scope and receipts

Read-only commands used: git show at each full pin for INDEX.md, CORPUS.md,
ID_CROSSWALK.md; git ls-tree -r --name-only at PR21; inspect its ALLOCATIONS.md,
FHV record/addendum, OP record, SINUM assessment and MOP update addendum.
A Python scan of every Markdown/JSON file under literature/ and
 topics/padua-literature-20261103/ at pinned PR21 searched new-source arXiv
identities 1104.3778, 2008.08210, 2004.04113, 1409.4053, 1410.1332,
1511.08098 and 2407.13946 plus author/title terms (Kozhan, Vaktnäs, nearest
neighbor recurrence relations, discrete integrable systems, multidimensional
Toda and spectral theory of Jacobi). It returned no matching source record.
Main INDEX/CORPUS were separately searched with all twelve author/title and
arXiv identities. This is a repository dedup check, not an exhaustive
bibliographic search or a novelty assertion.

Git blob identities of principal pinned registry inputs:

| Pin | File | Blob |
|---|---|---|
| 21dbfc9 | literature/INDEX.md | `be38f1f3f19a3aa42cfaaee593a079e9d962349c` |
| 21dbfc9 | literature/CORPUS.md | `aeca8b272b50d70e9a6232e6bec878f1d06f82ba` |
| 21dbfc9 | ID_CROSSWALK.md | `0e01f3b27bc41cfe2ee06a6a03882fae939b3dbc` |
| 890f56c | literature/INDEX.md | `d4176c1e98a1088500782d8123516c48a9a3eeda` |
| 890f56c | literature/CORPUS.md | `aeca8b272b50d70e9a6232e6bec878f1d06f82ba` |
| 890f56c | ID_CROSSWALK.md | `00da995c936144cad3e1d80ec40bea224b2cfbb7` |

All recommendations remain conditional on the orchestrator's union reservation
receipt and final-ID allocation. No same-source ambiguity or collision was
found within these pins. If a fresher PR21 head has final assignments, reconcile
against those exact assignments before allocating any new source ID.
