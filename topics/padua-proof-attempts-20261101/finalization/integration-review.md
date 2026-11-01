# PR9 mechanical integration review

- Reviewer: Codex independent subagent `reservation_inventory`; requested gpt-6.1-sol medium; resolved runtime model/effort metadata unexposed.
- Date: 2026-11-01. Rules read at `2c192c7575a5688d84a5869072c5918d7405ef03`.
- Reviewed working tree based at `020dcddd36fa1e3254cbf288701d5ab02d27c580`, against main `cf89b140530d5838bdb208a8c28f3e7aa676ace3` and published PR9 `93da3be26dbddf9ec2446af578fe8015bb4eeada`.
- Scope: mechanical application, preservation, status consistency and registry integrity. No mathematics reaudit or new novelty assessment; the accepted Claude audit remains the scientific authority.

## Result

PASS after the orchestrator corrected the dependency-column precision issue below. No unresolved actionable finding remains in this review scope.

## Finding and verified disposition

The first integration draft put source targets PD-T098/PD-T100 in new PD-T101/PD-T103 Depends-on cells, creating apparent reverse dependencies, and put complementary PD-N042 in PD-T102's dependency cell. The orchestrator moved source/complement provenance into Disposition and supplied the actual elementary/optional dependencies. Independently reread the three corrected rows: they match the durable records and do not inherit an OPEN/MEASURED target as a proof. This was a registry-description correction, not a proof change.

## Executed verification

- Parsed all twelve reviewed Old/New proposal blocks, translated the three new result aliases and the existing PD-N042 alias through the ID mapping, and compared each entry with applied-replacements.json. All twelve entries match exactly. Every old block was unique in the sequential base reconstruction; every installed new block occurs once.
- Reconstructed all five changed source files from main plus the twelve replacements. OPEN_TARGETS.md matches that reconstruction exactly; each of the four theory files adds only its dated finalization History item. The three original Known/Done/Route paragraphs remain verbatim at the beginning of their appended updates.
- Compared every existing primary proof ID/claim/title/status against main: all 143 identities, titles and statuses preserved. Exactly PD-T101, PD-T102 and PD-T103 were added, all PROVED. No duplicate primary proof ID among the resulting 146 rows.
- IDEA primary-column occurrence sequence is unchanged (231 inherited mentions, 209 unique IDs). All 426 literature primary IDs and their sequence are unchanged. Literature INDEX/CORPUS content is outside this integration diff.
- Compared the first four columns of all 845 inherited crosswalk table rows: every existing ID mapping, origin and durable path is preserved. The three source audit/comparison cells append provenance; three new provisional-to-final result rows and the original-to-split statement are present.
- The complete preexisting shared-ledger body remains verbatim; the standalone charter ledger is byte-identical. Published PR9 reservation PD-T101–105 is preserved with 101–103 assigned and 104–105 unused permanent headroom. PD-N/IDEA/LIT have no new range. PR12 advance was separately checked in reservation-recheck.json.
- All seven added/changed PROOF_STATUS table rows have eight cells, and all seven added/changed ID_CROSSWALK rows have five cells.
- Checked 2,433 Markdown local path targets across the seven global registry/state/index files, the five changed source files, all three proof records and the proposal record: zero missing paths. This checks path existence, not remote URLs or Markdown heading anchors.
- All 22 protected developer-code/output/auditor-support/audit-report files are byte-identical to published PR9. In each of the three result records, every byte from Statement through Scope is unchanged, including definitions, assumptions, status tables, dependencies, checks, sources and full proof. Changes are final-ID/provenance metadata plus B5's obsolete source/ID-deferral sentence under Open items.
- Main cf89b14 is an ancestor of the current HEAD (git merge-base --is-ancestor exit 0). git diff --check passes. No Git mutations were performed by the reviewer.

## F5 checklist coverage

All nine checklist rows are represented: IDEA-197 generic complement; IDEA-206 A1/local A5 links; the PD-N042 IDEA comparison; PD-T098 A1 split/dependency/audit; PD-T100 restricted local support and remaining certification; PD-N042 preserved counterexample; three new PROOF_STATUS rows; three existing source crosswalk audit/comparison updates; three new crosswalk rows plus explicit PD-T098→PD-T101 split mapping. PD-T098/PD-T099 remain OPEN, PD-T100 remains MEASURED, PD-N042 remains PROVED and its universal rejection is retained. A1/B5 close at their exact scopes; A2/A3/A4 and remaining A5 work remain unresolved.

## Limits

This is a working-tree mechanical review of the bytes identified below. The orchestrator owns the fresh remote readiness scan, batch rehearsal, finalization log/PR metadata and publication. No new scientific rerun was needed or claimed by this review.

## Reviewed content identities

| Path | SHA-256 |
|---|---|
| `ID_CROSSWALK.md` | `a65c2e715cbb6fd01f75ae7de900ccf85509e81c34ed0354bd21c2e2289d8229` |
| `PROOF_STATUS.md` | `a916cda87c9f7ad1950f62e32d254f5c276d386b63f5e84a32cb08a3298f8b0f` |
| `state/IDEAS.md` | `de45820ecb33f8694b0ed4a13177fc2d91094729dc2f164e3d26034fada4d4a0` |
| `PAPER_MAP.md` | `bca6b29bbd5c0e6b357cb9904dfe0df682f4c80518829a823e9fac28b3b2e701` |
| `state/CURRENT.md` | `bfa11a51cd5e03d614756638818674644a830dbd92372ce98e719ed9f7972afc` |
| `topics/padua-batch-20261031/ALLOCATIONS.md` | `26918056d06e8fed622e07e512c062fb8bfce9762e211ffe5bf78aedd0225d36` |
| `topics/programme-ideas-20261031/OPEN_TARGETS.md` | `c181d688edc8927b23e273f2a5f6542e950652b9bd892e5a96c89d2e3e199157` |
| `topics/programme-ideas-20261031/theory/programme-ideas-claude-04-padua-corner-expansion.md` | `3cedf9b5f79f7b2ca24ce5b4b5e71327a90bf8951be780b54d021132c12bd30b` |
| `topics/programme-ideas-20261031/theory/programme-ideas-claude-06-padua-lebesgue-maxima-counts.md` | `cf96d30ce806aee7915fa47593b22a5b6873e5110b54be8e83b7ab2301cdb355` |
| `topics/programme-ideas-20261031/theory/programme-ideas-claude-N04-pattern-commutant-not-three-dimensional.md` | `c3f1a222d295ade530a5b682b4d76ad4fe02b2a6c1791391f979ca6ff0ffab01` |
| `topics/programme-ideas-20261031/theory/programme-ideas-claude-01-finite-favard-pattern-pairs.md` | `9e25301b14086106d623c5d5e44cc2a751eea17d5f58b6c412b75a3ebfdf89aa` |
| `topics/padua-proof-attempts-20261101/theory/proof-attempts-codex-01-padua-corner.md` | `ea59aa077a4d021fc69354383f69340f21d17d87d3a28c6ecaaf302cc763612c` |
| `topics/padua-proof-attempts-20261101/theory/proof-attempts-codex-02-generic-commutant.md` | `3a167aa4b81edeb12452a3da01de67ae64f10290f628a0b680762e43852350a7` |
| `topics/padua-proof-attempts-20261101/theory/proof-attempts-codex-03-degenerate-maxima.md` | `e46beb621139cf531c855ad2574430045193a740685605e4556cb5c6960e6067` |
| `topics/padua-proof-attempts-20261101/proposed-record-changes.md` | `c58ae82187d450051a931b70550e387c7e0b9be72c9769debab0238f65471fe3` |
| `topics/padua-proof-attempts-20261101/finalization/id-map.json` | `ea982701c0936ada133335d0e2721b39c93c45148df3ac9f53bacb1f768d6b66` |
| `topics/padua-proof-attempts-20261101/finalization/applied-replacements.json` | `69e89d38f1a514418ed20c1cc25c20ef99356647bec07f1065a2bf07259c263b` |
