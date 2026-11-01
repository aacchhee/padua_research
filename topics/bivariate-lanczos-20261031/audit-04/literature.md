# Audit 04 — literature integration

Rules a2dd845. Independent, focused Codex audit of PR10's literature integration; **changes required for one canonical-source identity error**. Accepted-main content and the 227 topic statement mappings are preserved. The new reading reports remain literature evidence, not inherited proofs.

Auditor: `/root/audit_l3_framework`, configured by the coordinator as `gpt-6-astra`, xhigh; model/effort are the supplied launch configuration, not independently observable runtime telemetry. Date: 2026-11-01. No developer files or Git state were changed. No external search, source retrieval, theorem rerun, or external message was performed.

## Pinned comparison and scope

| Role | Commit |
|---|---|
| Reviewed HEAD | `a2dd845b8a231e1b00733e1361e2a9ad3bad222f` |
| Accepted topic baseline | `cf01449fc96233c9074ce25efcb056535414aa1d` |
| Accepted main | `9739a0c56b7a3976422ce60a8441bfbbfd6554df` |
| Main merge | `1167c33e71e2b0677e569f5fbae7ed97160fa8e9` |
| Before consolidation | `9a77f2b10d42bb43aea01cacfcea86469c87c5dc` |
| Consolidation | `ae36ec013630c939fb1b2c1cdddb2cf12cc80cf0` |
| Final allocation | `896afd6c6befee3bc05f74d178cab9400baab31a` |

Read current AGENTS, WORKFLOW, CODEX (including the new local-working-track paragraph), the complete current INDEX and IDEAS, all three frozen prior-art reviews, the consolidation search log, relevant CORPUS rows, all 49 added statement blocks and their coverage, affected source metadata/history, and the developer integration checker. The prior-art reviews are byte-identical to the accepted topic baseline. This is a consolidation/attribution audit; it does not re-establish historical priority, verify primary papers, or reopen accepted mathematical proofs. Root and the registry auditor own scientific summaries, non-LIT allocations and dependency graphs.

## A4-L1 — duplicate canonical record for the same truncated-normal-form paper

**Priority: medium; changes required.** `literature/records/telen-mourrain-vanbarel-2018.md:23` calls the accepted `mourrain-telen-vanbarel` record “a different, earlier Step 0 item.” Both records' line 3 names exactly `https://arxiv.org/abs/1803.07974`; the descriptions identify the same truncated-normal-form polynomial-system paper. Different author ordering and reading dates do not make different sources. `literature/records/README.md:3` requires one file per source.

The duplicate is carried into `literature/CORPUS.md:29` and `:151`, and into the separate source keys for `literature/INDEX.md:29` (accepted LIT-023) and `:327` (new LIT-259 / provisional 416). The 29-new-record count is a correct file-change count, but includes this existing source. This splits the earlier secondary account and the later WebFetch reading instead of maintaining one source's provenance.

**Fix:** retain the accepted canonical `mourrain-telen-vanbarel` record and its LIT-023 statement; append LIT-259 with its provisional alias, distinct reading coverage, reader and date. Reconcile the bibliographic header conservatively, remove the false different-source assertion, and update CORPUS/INDEX and any source-key references to the canonical record. Preserve both statement IDs and their contents; no ID renumbering is needed. An explicit legacy-key alias or redirect may preserve discoverability without keeping a second independent source record. Root's combined report names this finding A4-M4.

## E1 — optional provenance wording correction

`literature/records/barrio-pena-sauer-2010.md:36` says the L1 reviewer “read the source through WebFetch digests.” The frozen L1 review says it did not read the paper, and the new history paragraph at `:42` correctly records metadata-only access followed by the orchestrator's reading of AC's copy. Remove or specialize the generic sentence at line 36. The statement-level page coverage and the accurate history remain intact, so this is an editorial correction, not a new mathematical or primary-reading objection.

## Preservation and mapping results

The independent checker is [check_literature.py](literature/check_literature.py); full receipts are [checks.json](literature/checks.json), [run.log](literature/run.log) and [input-manifest.json](literature/input-manifest.json). It uses read-only Git plumbing at the pins above and compares the inspected worktree bytes with HEAD.

| Check actually executed | Result |
|---|---|
| Consolidation file changes | 29 added records, 15 modified records |
| Shared main/topic sources | 14 actual sources, excluding README |
| Shared source preservation | 13 complete main records occur literally as contiguous text in HEAD; DST retains every original nonblank line as a line or a prefix extended with explicit new provenance, and all original statement headings |
| All accepted-main record files | All nonblank lines preserved, allowing additive line extensions; 53 files including README checked |
| Accepted-main INDEX | Every nonblank main line retained literally |
| Accepted-main CORPUS | Every existing source-row field preserved within its corresponding field; added topic coverage does not overwrite main's reading history |
| Accepted topic statements | 178 headings retained under final aliases; every existing verification, statement, hypotheses, locator and reading-evidence field is unchanged |
| Final topic references | All 227 aliases map bijectively to LIT-066–292 and to the correct record key and path in INDEX; no disagreement |
| New source statements | 49, provisional 401–449 / final LIT-244–292; each INDEX statement plus hypotheses and locator exactly equals its record fields |
| Verification labels | All 49 newly consolidated statements explicitly say UNVERIFIED; no conversion into inherited proof status |
| Inspected input/worktree consistency | No input differs from pinned HEAD; all three frozen prior-art reviews unchanged from baseline |
| Source identity | One duplicate exact arXiv identifier among root canonical records: 1803.07974, as A4-L1 |

These checks go beyond numeric ID uniqueness: they compare source keys, record targets, statement fields, hypotheses, locators and accepted provenance. The duplicate-source check intentionally exposes the remaining semantic defect even though both IDs and links are syntactically valid.

## Comparison with the frozen reviews

All 49 additions were compared with the corresponding L1/L2/L3 review passages. Their core factual paraphrases and reported locators faithfully preserve those reviews, within the limitations below. Grouping the complete comparison by source role:

| Final statements | Frozen-review content retained |
|---|---|
| 244–250 | L1 stacked triangle recurrence, Xu's nonunique left inverse, unread Dunkl–Xu pointer, enlarged-matrix two-directional Arnoldi, Meurant's qualitative observation; L2's later Austin reading supersedes L1's unread pointer; Waldron remains abstract-only |
| 251–259 | L2 univariate fitted-value rounding result, confluent selection rule, Stewart residual/backward comparison, Paige augmented Krylov result, unread conditioning references and metadata-only DGRS background, SVD border bases, TNF residual/backward checks; no commutator-based accuracy result is invented |
| 260–266 | L3 moment-cone duality and derivative/interiority ingredients, Blekherman's round double zeros, infinite Favard and cubature/count statements, Lasserre criterion; exact hypotheses or numbering not extracted remain explicitly unresolved |
| 267–275 | L3 minimal-matrix-convex/dilation framework, secondary DDSS citation, abstract-only Putinar, metadata-only Bayer–Teichmann, secondary Greenbaum–Strakoš, partly garbled Meurant–Strakoš digest, one-dimensional super-resolution, abstract/title-only DGIM/CSS |
| 276–282 | L1's Zaccaron measurements and table reconciliation, Liu–Narayan's all-relations predecessor, Hokanson's informal non-Krylov statement and L2's unverified selection mapping, FOX's coefficient-space algorithm; no new equivalence or stability proof inferred |
| 283–288 | Zhu–Nakatsukasa's fit/orthogonality scope and unseen Appendix B, univariate BNT caveat, Sinha's partially read injection formula, Jia–Li's one-operator semiorthogonality assumptions and measured cost comparison |
| 289–292 | Chen's reported model, unresolved Greenbaum-width conflict, DST compatibility/block-tridiagonal reading, and explicitly unresolved Xu paper/numbering conflict |

The three updates without new statements are appropriately limited: Simon records a second digest of already recorded equations and costs; Šimonová–Tichý records the second §1 reading; BPS records the later AC-copy reading and still-unread pages (subject to E1). Existing stronger primary-page coverage is not replaced by the digest-only limitations of later reviewers. The consolidation log expressly says the consolidator did not reread papers. Its ten metadata calls are logged as bibliographic checks rather than mathematical verification; unsuccessful lookups, ambiguous Kuznetsov DOIs, PSS identity uncertainty, missing titles, and author initials from memory remain disclosed.

The important old conflicts remain visible instead of being silently settled: Zhu's Remark 3 wording/version, Liu–Narayan equation numbering, Xu's Favard location, and the competing accounts of Greenbaum's interval width. Zaccaron's two numbers are reconciled only to the extent of the reviewer's reported table reading; the record still requires a verbatim table check and does not assume the square's node set is a product grid.

## Audit-01 P2 disposition and limits

The central deferred obligation in `audit-01/protocol.md:31`–33 is substantially fulfilled: previously missing Di Dio–Schmüdgen, Blekherman, Zhang–Su–Li and the other recommended source statements now have canonical-index entries with digest/abstract/metadata limitations, rather than being promoted to mathematical dependencies. Full closure of canonicalization requires A4-L1.

A bounded inventory limit remains: the frozen L3 review `:38` reports a WebFetch of Schmüdgen's *Ten Lectures*, arXiv:2008.12698 (only Lectures 1–5 returned; Lecture 3 Theorem 3.5), and `:79` uses it as the one-dimensional analogue. Current LIT-261 records that analogue inside the Di Dio–Schmüdgen entry, but CORPUS has no separate *Ten Lectures* source record. This audit records that remaining inventory limit rather than treating it as a newly verified theorem or a separate blocker. Unread leads such as KPR, Stetter, Braconier–Langlois–Rioual and Reichel remain named pending leads, not attested source facts; no additional literature search is required by this audit.

The report verifies faithful consolidation of review evidence, not the truth of every digest formula. In particular, unresolved hypotheses, theorem numbers, rank/count wording and source identity qualifications still require primary inspection before publication-level reliance. No global priority conclusion follows from the reviewed searches.

## Commands, hashes and reproducibility

From `/workspace/padua_research`, the final independent execution was:

```text
python topics/bivariate-lanczos-20261031/audit-04/literature/check_literature.py > topics/bivariate-lanczos-20261031/audit-04/literature/run.log
```

Exit 0 means the checker completed and wrote its result, including the duplicate-source finding; it is not a claim of a clean literature registry. During checker development, whitespace around Markdown cells and plain-text record paths were handled before the final execution; intermediate parser diagnostics were not source findings.

Additional read-only comparisons executed included `git diff --name-status` and `git show --stat` across the consolidation parent/commit, `git ls-tree -r --name-only` at main/baseline/HEAD, and `git diff 9739a0c56b7a3976422ce60a8441bfbbfd6554df a2dd845b8a231e1b00733e1361e2a9ad3bad222f -- literature/records/degani-schiff-tannor-2005.md`. Source identity was independently checked using each record's metadata URL, not a title-only similarity test.

| Artifact/input | SHA-256 |
|---|---|
| `literature/check_literature.py` | `7168c1f2ad48538ae18869feccfbf6d56a76ede66f624682fe5d2a4af7a89136` |
| `literature/checks.json` | `b586e684832bd03b7e983488055e83e1e89a50ba45e0a214aa0dffe20fb8c635` |
| `literature/input-manifest.json` | `2aa088848fbbba9145fa732bf13941038cc8f3a4cdfd0193b21bdd1bc917cf3d` |
| `literature/run.log` | `55a82ba5692b136470ea38682582bcba2bece78461426cf7821190f53827ab30` |
| Repository `literature/INDEX.md` | `f7af5cea1ded7afafc9383531949078499223479700453359b86bf839c5928e2` |
| Repository `literature/CORPUS.md` | `37937a48e89cfee4e9b47f9799252792f2850f1ca1f681f08fd268b8bbd4a878` |
| Repository `state/IDEAS.md` | `8a9c3f5e5cedb9211218b884eabce7fdefbbf1f2bd3bab32d3abd082f3998839` |

The input manifest supplies exact sizes and hashes for all inspected canonical records, rules, registry inputs and frozen reviews. Evidence files total under 100 kB and each is below 1 MB. Root owns the repository-wide output budget and Git/protocol work. Next: the developer should correct A4-L1 (and preferably E1), after which a focused canonical-source/index check is sufficient; no unaffected mathematical reruns are requested.
