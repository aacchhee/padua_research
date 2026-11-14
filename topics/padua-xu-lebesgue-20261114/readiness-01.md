# Readiness 01 — Xu and Morrow–Patterson Lebesgue functions

2026-11-14. Independent auditor: **Codex, gpt-6-astra, high**. This agent did not develop the work and made no Git mutation. The approved model substitution is recorded in [LOG](LOG.md), entry “2026-11-14 — handoff 04 started (Codex orchestrator)”.

- Rules and open-handoff head: `b361e675e5e77c2b8829f2af8a08d17469229c34`.
- Preparation candidate: `0e97396c3e16df5e83451544e1cbfae044c403a4`.
- Response candidate: `80a744eec779ac0e279443850453d44e7573c8da`.
- Main/base: `99a9b1d161e41a80c4fd425b63022c681fbe8779`.

## Verdict

**READY for AC review and merge decision**, with the orchestrator's one-line map wording correction reviewed below included in publication. No unresolved BLOCKING, MAJOR or MINOR readiness finding remains. The final PR readiness/head lines and handoff completion are publication actions for the orchestrator. Only AC merges.

This is the bounded response/registry/reservation readiness check requested by [handoff 04](handoffs/04-readiness.md). It does not repeat the substantive audit. The accepted 23 claim statuses, result-bearing code and evidence are unchanged. No material scientific divergence beyond the accepted audit scope was found.

## Coverage and response diff

Read AGENTS.md, agents/WORKFLOW.md, agents/codex/CODEX.md and the handoff's referenced agents/claude/CLAUDE_ROLES.md at the input head; the full topic LOG, audit-01 and response-01; handoffs 03–04; the allocation ledger and PR34 readiness format. Reviewed both requested diffs, including all changed theory text, result summaries, gates, literature records, registry rows, headers and the final-ID map:

```
git diff 8fdd0392bf53e076b0ebef7ca4eec1a2549e7076 80a744eec779ac0e279443850453d44e7573c8da
git diff 80a744eec779ac0e279443850453d44e7573c8da 0e97396c3e16df5e83451544e1cbfae044c403a4
git diff 0e97396c3e16df5e83451544e1cbfae044c403a4 b361e675e5e77c2b8829f2af8a08d17469229c34
```

The last interval changes only LOG and handoffs. The readiness scope adds no novelty claim or candidate; it checks faithful application of already audited material. Accordingly, I read the new IDEAS section and relevant cited context, and mechanically scanned the complete registry for reservations, rather than repeating a full conceptual novelty audit or full human read of unrelated IDEAS entries.

All A-m1–A-m9 and n1–n9 have dispositions in response-01. The retrospective gate is explicitly retrospective; the X2-33 summaries now distinguish the all-even-n sine bound from the non-trivial n ≥ 1030 bound; stale rerun/process text is corrected or superseded by dated notes; the P1 plan remains a plan and PD-T705 remains OPEN. The float cancellation and timing-field substitution are disclosed, with references to the existing evidence. Beberok's number remains a qualified transcription, not a newly verified source fact. The optional PD-N253 upgrade was not taken. No Statement section, claim quantifier, constant, status, dependency direction, result-bearing code or evidence was changed by the response. Corrections of summaries restore the accepted canonical statements.

**Cyclotomic check (PD-T700 / X2-23 addendum §2).** I checked the new explanatory proof mathematically. Bézout gives the compositum Q(ζ_l), and primewise exponents give φ(a)φ(b)=φ(l)φ(d). Restriction injects Gal(KL/Q) into the compatible-pair group, whose order is φ(a)φ(b)/[K∩L:Q]; hence [K∩L:Q]≤φ(d). Inclusion Q(ζ_d)⊆K∩L supplies the reverse degree inequality. For a=2M, b=2M+2, d=2, the intersection is Q. The remaining non-vanishing argument is unchanged: the positive algebraic integers in (0,4) must be 1, 2 or 3, and the possible ratios greater than 1 force nonintegral M. The explicit standard inputs are cyclotomic irreducibility/degree and elementary Galois theory. Thus the unverified Washington proposition locator is no longer needed. This is the requested expansion of the already accepted textbook fact, with no replacement fact, proof route or dependency; its mathematical verification is included here, not deferred to another audit. The already accepted registration choice retains substantive part (f) inside PD-T700 and records its consumers PD-T706/709 and the PD-T705 remark.

## Registry, map and literature checks

The six shared registries and literature record changes are additive; existing rows and other topics are preserved. All 23 theory bodies are byte-identical across the registration interval from their first section heading onward: only the header IDs/aliases change. The global statuses match audit-01 §6: **19 PROVED** (17 PD-T and two PD-N), **three MEASURED**, **one OPEN**. PD-N251/252 reject the external BBDM assertions; IDEA-772 remains a retained successful candidate. PD-N253 remains a scoped MEASURED mechanism failure.

Programmatic checks of the final map, canonical rows, aliases and paths found **48 unique assignments**: 20 PD-T, three PD-N, 14 IDEA and 11 LIT, all within their reservations. Each has one canonical registry row and a consistent crosswalk entry; the 23 theory headers retain their provisional aliases. Permanent gaps are unchanged. The new Markdown tables have the required 8/3/4/7 columns in PROOF_STATUS/IDEAS/CROSSWALK/INDEX, with escaped mathematical pipes. All **239 relative-link occurrences added in the registration diff** resolve to existing files (file targets checked; remote URLs and fragment anchors were not fetched or tested).

The literature records preserve the stated coverage distinction: journal text, selected sections/page images, model-mediated digests, abstract-only, or the orchestrator's unverified transcription. I did not fetch or re-read the primary papers in this readiness check. LIT-721/722 are different statements from one Beberok record, and LIT-723/724 different statements from one BdMV record. Li–Sun–Xu extends LIT-307/010/650, without a duplicate new ID. Existing Xu, BCDMV, KL, Dencker–Erb and related entries receive dated addenda. The BCDMV Table 7 p. 320 correction is attributed to the developer's page check, not claimed as my verification. The documented-search and unread-source limits remain in force.

**Resolved MINOR R-m1.** In `pr-preparation/final-id-map.json`, IDEA-773's disposition originally said “PARTIAL progress”. The orchestrator changed it to “partial progress without a PARTIAL status”, preserving the following PROVED corner / OPEN argmax-and-limit distinction. I reviewed the one-line working-tree diff. This aligns wording with the existing IDEAS row; it changes no status, claim or ID. The auditor edited no developer record.

## Reservation refresh

The live GitHub all-PR collection (`pulls?state=all&per_page=100`) returned **35 PRs**, below the 100-item limit: open PR27/35/36, 32 merged, and **no closed-unmerged PR**. Main and every open head were inspected, drafts included; `git ls-remote` independently confirmed the following heads again at the end of the checks.

| Scope | Checked head |
| --- | --- |
| main | `99a9b1d161e41a80c4fd425b63022c681fbe8779` |
| PR27, draft | `fd82e593cd73019601fb00dea9844db09f8601c0` |
| PR35, open | `a045b8e9b2b4d92813a9b8e2832b2f8254e7397e` |
| PR36, draft input | `b361e675e5e77c2b8829f2af8a08d17469229c34` |

A read-only Python inventory using `git ls-tree`, `git show` and `git rev-parse` consumed every ALLOCATIONS.md and all four canonical identifier sources (PROOF_STATUS, IDEAS, literature INDEX, CROSSWALK) at these heads: **87 complete copies**, comprising **71 ledgers and 16 registries**, deduplicated to **20 ledger blobs / 31 blobs overall**. It scans range upper ends and historical/retired prose as well as assigned IDs; source-copy identities were retained in scratch `/tmp/readiness36-inventory.json`. I inspected reservation tables, retirement context and exceptional mentions. The first raw pass exposed PR35's additional fixture mention; after context inspection it was excluded on the same basis as the existing PR34/PR36 notes. Exclusions are limited to the documented PD-T999 test-fixture mention, PD-N303/N304 unregistered prose mentions, and eight four-digit bttb-research LIT aliases (foreign identifiers). None overlaps this topic's ranges. No unknown retired reservation was found.

| Namespace | Highest foreign reserved/used | PR36 reservation | Assigned | Permanent unused |
| --- | ---: | --- | --- | --- |
| PD-T | 689 | 690–719 | 690–709 | 710–719 |
| PD-N | 250 | 251–257 | 251–253 | 254–257 |
| IDEA | 765 | 766–795 | 766–779 | 780–795 |
| LIT | 720 | 721–745 | 721–731 | 732–745 |

The complete union maxima are **T719/N257/IDEA795/LIT745**; no foreign source overlaps PR36's intervals. The first ledger-addition commit is `91a0116eb9e83afe86a25c70d68684f364b316c5`, an ancestor of the input head, linked by the live PR body. No range was added, shifted or enlarged. The [ledger refresh](ALLOCATIONS.md) records the same snapshot. This is one PR's readiness, not a requested multi-PR squash integration rehearsal; no Git integration or merge was performed. Refresh again if main or another open PR's reservation/identifier sources change before AC merges.

## PR body, executed checks and limits

Read the live PR36 body twice, including the orchestrator's in-session metadata corrections. It contains WORK, the supplied audit-01 §8.1 AUDIT paragraph, response dispositions, PR, the reservation publication and ledger links, full base/input head, corrected PD-T708 scope, approved readiness auditor identity and AC decisions (merge, X2 continuation, manuscripts). The draft/in-progress text was accurate when read. On publication, replace it with this verdict and the actual final head; the orchestrator owns that operation.

Executed: the diffs above; map/row/status/header/path/table/link checks; the complete reservation inventory; live all-PR query and PR-body reads; final `git ls-remote`; `git diff --check 8fdd039 b361e675` and working-tree `git diff --check` (PASS). The code/evidence-only diff from 8fdd039 to b361e675 is empty. An initial naive status-cell split misread escaped pipes; the corrected escaped-pipe-aware check passes all 23 rows.

**No scientific rerun was executed or needed here.** The earlier audit's reruns and separate code path remain its evidence, not mine. Residual limits remain: trusted Arb/python-flint arithmetic; finite local-maximality only through n=3000; global MP argmax and sharp-limit target OPEN; qualified Beberok transcription; incomplete literature coverage; and the existing license decision for AC. The readiness verdict does not expand any claim or erase these limitations.
