# Protocol check 01 — PR22 preparation (handoff 06)

- Checker: Claude, `claude-opus-5-5`; the in-session effort level is not exposed. Role: independent protocol checker of Codex's PR preparation. I authored Claude audit-01/02 but none of the preparation files.
- **Model disclosure.** AC's prompt named Claude Sonnet 5.5 high. This session runs on Opus 5.5 and cannot switch models. Handoff 06 and agents/claude/CLAUDE_ROLES.md allow Opus 5.5 high for a protocol audit, so I used it rather than delegating the check.
- Date: 2026-11-05 (UTC).
- Rules read at branch head `1de5891ee622e826d7553819152aa261b02faaa9`. AGENTS.md, agents/WORKFLOW.md and agents/claude/CLAUDE_ROLES.md are byte-identical to the audit-02 rules.
- Checked preparation output: `7881e1cf771a70cad94b835c0580c2e3d4f94ece`. `1de5891` changes only handoff 05's status and adds handoff 06.
- Audited science pin (audit-02): `5b36f8f8ac5b3c9a426d22a9375155a2b4d86e1b`.
- Live main: `21dbfc90257b952d8923f6d01739d12aa8d6e0a1`, an ancestor of the head.
- **Result: PASS.** No mechanical or protocol finding. PR22 is ready for AC's merge decision.

## What was checked

1. **E1, E2 and X1.** `git diff 5b36f8f HEAD` on the topic files shows exactly the approved edits.
   - E1: terminal max |d| "reaches 33.86 (Krawtchouk N32) and 71.15 (Hahn N24); it is not monotone".
   - E2: the results file distinguishes the marginal-only route from the shift-family plus boundary-data route, and says "no C3 comparison".
   - X1: the addenda in c4-baseline-01.md and PD-T290 attribute the exact references at N=8, 12, 16, 24 to audit-02 R4; N4 is the developer's own check, and N32 still rests on precision convergence.
   - All other changes to accepted files are final-ID headers, provisional aliases, process-status lines and link targets. Proof sections and executable bytes are unchanged; this is also asserted by the checker.
2. **Final-ID map** (preparation/final-id-map.json; ID_CROSSWALK rows present):

   | Final ID | Former provisional ID | Status |
   | --- | --- | --- |
   | PD-T286 | T?…01 | PROVED |
   | PD-T287 | T?…02 | MEASURED |
   | PD-T288 | T?…03 | PROVED |
   | PD-T289 | T?…04 | PROVED |
   | PD-T290 | T?…05 | MEASURED |
   | PD-N100 | N?…02 | MEASURED; IDEA-377 REJECTED: refuted |
   | IDEA-376–379 | C1–C4 | — |
   | LIT-562–568 | seven new sources | — |

   - PD-N?…01 is recorded as "withdrawn, no final ID", with its splits pointing to PD-T288/289. Its original text remains verbatim in the historical redirect.
   - Unused T291–293, N101–103, IDEA380–383 and LIT569–573 remain permanent gaps. All assignments come from the reservation first published at `a0abe8b`.
3. **IDEA-117.** The registry row records AC's 2026-11-03 resume, the audited outcome, and C3 (IDEA-378) as deferred. It is the only changed pre-existing line in `state/IDEAS.md`, as handoff 01 authorised. Every other shared file starts with the exact bytes of main `21dbfc9` and only appends this topic's sections.
4. **Literature deduplication.**
   - Reused rows (same sources; I checked them against main's INDEX):
     - LIT-420, the compound FHV + ADY record, used for both of those sources;
     - LIT-346 (Van Barel–Van Buggenhout–Vandebril);
     - LIT-119, with related LIT-347 (SINUM);
     - LIT-348, with related LIT-117/118 (arXiv 2608.25758).
   - The seven new sources (Van Assche 2011, Denisov–Yattselev 2008.08210, ADY 2004.04113, ADV 2016/2015, the Toda paper, Kozhan–Vaktnäs) are absent from main's INDEX. A `git grep` of PR21 at `890f56c` for their arXiv numbers and author names returns nothing, so they cannot duplicate a PR21 record.
   - The new rows do not relabel developer-verified locators as Claude-verified.
5. **Registry and frontier wording.** PROOF_STATUS, IDEAS, INDEX, CORPUS, CROSSWALK, CURRENT, PAPER_MAP, RESULTS and the batch ledger are additive and topic-only.
   - RESULTS.md ends with an exact copy of the topic results file, with links converted; the checker asserts this.
   - The CURRENT and PAPER_MAP text keeps stable coupled updating, error-source decomposition and C3 open or deferred. It does not present preparation as research.
6. **Live reservation refresh** (GitHub API, all states, at check time):
   - open PRs: 21 (`890f56c`), 22, and 24 (`79c3d6a`), identical to preparation/reservation-refresh.json;
   - every closed PR returned is merged (#7 does not appear in the PR listing);
   - main is unchanged at `21dbfc9`.
   - `git grep` of main, PR21 and PR24 finds no registry row or ledger that uses any ID in T286–293, N100–103, IDEA376–383 or LIT562–573.

## Commands executed

```sh
python3 topics/nn-mop-iep-20261103/preparation/check_registration.py   # exit 0, passed true, 10 assignments, 12 literature aliases, 7 new, withdrawn negative no final ID
git diff --check origin/main HEAD                                       # clean
```

Squash rehearsal, replayed at the current head `1de5891` in a disposable detached worktree that was then removed. No branch or remote was changed.
- main + squash(PR22): tree `b43cffdd476e2bb2d228a053b1f9b8396eb9a65a`, identical to the PR head tree.
- Then PR24 (`79c3d6a`): squash exit 0, no conflicts.
- Then, separately, PR21 (`890f56c`): squash exit 0, no conflicts.
- After each second merge, this topic's rows survive in PROOF_STATUS, IDEAS, INDEX, CROSSWALK and RESULTS.

This supersedes the frozen rehearsal at `fcb3a6a` only for currency. The later commits add topic-only files.

## Limitations

- No new science, run or primary reading was done in this step. Primary locators remain developer-verified only (audit-01 N1, audit-02 coverage).
- The optional supplementary Astra integration check did not execute (capacity error, honestly recorded in integration-check.md).
- The rehearsal does not set a merge order for PR21 or PR24. If main moves before AC merges, replay it.
