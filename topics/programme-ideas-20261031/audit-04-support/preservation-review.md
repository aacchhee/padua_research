# PR #6 integration preservation review

- Rules/source read: `37820a528c863e5cfe2dc2f1f8879b4fd40cf210` (`AGENTS.md`, `agents/WORKFLOW.md`, `agents/codex/CODEX.md`). Baseline: `f4e213390f66a8c9f0c6bd65131b97b78db873c8`; refreshed main supplied by orchestrator: `21e620ba8b5f0e0706f3a8c6613517df04d9d469`.
- Independent supplementary Codex reviewer under the parent audit; inherited model/effort, resolved runtime metadata not separately exposed. Root alone owns Git mutations. This reviewer writes only new `audit-04-support/preservation-*` files.
- Scope: accepted-record preservation and historical evidence provenance. No accepted mathematics, novelty, or literature comparison is reassessed. The full novelty gate is omitted because this review proposes no ideas and assesses no novelty claims. No full mathematical tests were executed.
- Executed: `python topics/programme-ideas-20261031/audit-04-support/preservation-check.py > topics/programme-ideas-20261031/audit-04-support/preservation-check.json` from repository root. Uses pinned Git objects and read-only `git show`, `ls-tree`, `diff`, `rev-parse`. Result: **PASS**, zero unexplained preservation differences within scope.

## Canonical records

At allocation `6954664fc0906b7e5c8ff0f1804b077bd3b5861f`, each of the **21 lattice PD files**, **11 programme PD files**, and **33 IDEA records** receives exactly the documented Final ID/provenance paragraph. Removing only that exact paragraph restores the allocation parent's entire original file bytes. The source head retains these allocation outputs unchanged. Thus the allocation changes no prior statement, assumption, proof, limitation, disposition, or status in these canonical records. The receipt identifies every file, ID, and before/after blob/SHA-256.

Against accepted audit baseline `f4e2133`, the sole additional canonical PD/IDEA text edit is the disclosed PD-T01(d) gauge sentence: the stabiliser is exactly `{±I}` because `e₁` is cyclic, replacing the prior finite-stabiliser explanation. This is the disclosed `c93c912` preparation clarification recorded in `pr-prep.md`; the precise diff is included in the receipt. It is not attributed to allocation and is not a new mathematical audit here. The separate OPEN_TARGETS and decisive-record N1/N2 prose corrections are outside this preservation subtask and remain part of the parent review.

## Protected records, code, rules, and inherited main

All **197 protected baseline files** are byte-identical at source: programme `audit-01.md`, `audit-02.md`, `audit-03.md`, all three prior audit-support directories, every `checks/code/` file, `AGENTS.md`, and `agents/`. The receipt lists the full protected path set. This confirms preservation since `f4e2133`, without implying these files have always matched main.

Relative to current main, rules differ only in `agents/WORKFLOW.md` and `agents/claude/CLAUDE_ROLES.md`: the disclosed Fable 5.1 ideas-campaign allocation and corresponding Claude role paragraphs. `AGENTS.md` and the Codex role are unchanged. No new rule amendment occurs after `f4e2133`.

The apparent large post-baseline Lanczos changes are inherited main content: **485 paths** under `topics/bivariate-lanczos-20261031/` and **219 paths** under `tracks/bivariate-lanczos/` differ from the earlier programme baseline, while both complete subtrees are byte-identical between current main and source. They are not topic mutations introduced by this integration.

## Main merge and CORPUS reconciliation

At main merge `3e0100f1a339c3f63dcb638785917400089a31a6`, all original main lines, including multiplicities and order, survive in each of `ID_CROSSWALK.md`, `PROOF_STATUS.md`, `literature/CORPUS.md`, `literature/INDEX.md`, and `state/IDEAS.md`. Their merge diff from main has additions only. This validates the five-registry preservation claim before the later documented allocation/deduplication transformations.

Comparing CORPUS with the merge's topic parent separately, **49 branch rows** disappear: exactly **15 old citation rows replaced by main's versions** and **34 provisional duplicate rows whose keys main now registers**. Every removed key has its replacement row on main. No nonempty branch non-row line disappears. The receipt gives all 49 old/replacement rows. The 15 old keys are:

`harris-simanek-2021`, `bos-dmv-xu-2007`, `caliari-dmv-2008`, `sommariva-vianello-2015`, `xu-siam-1994`, `xu-pitman-1994`, `degani-schiff-tannor-2005`, `huhtanen-larsen-bit-2002`, `bartels-jezioranski-1985`, `sauer-2007`, `mourrain-2017`, `humet-2019`, `egk-1991`, `mourrain-telen-vanbarel`, `vanbarel-chesnokov-2010`.

This establishes preservation and provenance of the rewrite, not independent validation of the replacement bibliographic assertions.

## Historical lattice checkers

`check-response-01.py`, `response-review/check_response.py`, their selected historical JSON receipts, and the response-review report remain byte-identical to `f4e2133`. Their pinned old main/topic revisions and the snapshot's `head=ad40c38ffbd28a80500f6ee10dd35bc778ac4c5b` identify historical executions. `pr-prep.md:104` explicitly states these checkers will not pass at the current head and remain historical receipts. No current passing execution is claimed here, and these scripts were not rerun against a knowingly incompatible current schema.

Precision note: “assert the earlier Unallocated state” in `pr-prep.md` is an informal description. Neither script contains a literal `Unallocated` assertion. The first validates provisional-ID row unions, 13 provisional IDEA summaries, fixed old-main preservation, and pre-allocation theory prefixes; the second reports equivalent provisional-row/status expectations. In particular the latter prints diagnostic JSON rather than enforcing an overall passing exit code. The historical limitation is correctly disclosed; a future wrapper must inspect diagnostics rather than treat process exit 0 as current validation.

## Outcome and limits

No blocking or unexplained preservation difference found. The recorded allocation transformation is metadata-only for the canonical records. Historical accepted proofs, status scopes, code, and audit receipts are preserved. This report does not validate global ID uniqueness, literature claim equivalence, links, source retrieval, batch rehearsal, PR metadata, or live merge readiness; those belong to the parent integration audit and its other checks.
