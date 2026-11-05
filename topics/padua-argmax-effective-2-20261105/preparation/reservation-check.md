# PR25 preparation reservation union — 2026-11-05

**PASS.** The existing T364–375 / N132–137 / IDEA454–465 /
LIT594–597 reservation remains uncontested. No new range, assignment or
accepted-ID renumbering is performed by this check.

Worker: Codex, gpt-6.1-sol medium. Rules read at
`5821c3f130ec0b1e33ad1d01620b67620e1f0be1`: AGENTS, WORKFLOW and CODEX;
also handoff 05 and response-check-01. This mechanical inventory introduces
no mathematical mechanism or scientific claim, so the scientific novelty
gate is not applicable. No scientific runs were executed.

## Population and pinned inputs

The orchestrator supplied the live all-state connector population in
[pr-population.json](pr-population.json): 25 returned PRs, three open
(PR21/24/25), 22 closed and merged, none closed-unmerged. This worker did
not independently query the network. Merged PR26 is included through current
main. Current remote PR25 is `22e8540cf90278dad2eba3eb51f129ca10a9dd9e`;
the scan uses its local integration with current main:

| Input | Complete SHA |
|---|---|
| main | `330fab835f43e5ba5b24e320c2d7e9647e6cbd60` |
| PR21 | `3ed6c94246f21353350f82712b6628b39db6f65a` |
| PR24 | `3a179f68ecbed20dc7e15862da842ed6116aa375` |
| own integration | `5821c3f130ec0b1e33ad1d01620b67620e1f0be1` |

Executed `python topics/padua-argmax-effective-2-20261105/preparation/scan_allocations.py`.
The script reads every complete `*/ALLOCATIONS.md`, plus complete
PROOF_STATUS, state/IDEAS, literature/INDEX and ID_CROSSWALK, at every pin:
49 complete file reads, comprising 33 ledger copies and 16 registry copies;
12 distinct ledger blobs and 19 distinct blobs overall. The compact
[receipt](reservation-scan.json) identifies every file copy by head, path,
Git blob, SHA256 and byte count. Raw convenience inventory stays outside Git
at `/tmp/argmax-prep-allocation/full-inventory.json`; the script regenerates it.

Complete unique ledger prose was reviewed, including the long shared batch
ledger history and its earlier foreign-branch copy, publication priority,
superseded owner instructions, imported reservations, and permanent gaps.
The parser includes qualified namespace tokens, omitted-prefix upper bounds
such as T364–375 and table ranges such as `PD-T | 266–285`. Bare T/N aliases
are interpreted only in ledgers: registry EX-T852/EX-T516 are foreign source
aliases and N512 is a numerical parameter. Four-digit BTTB LIT aliases are
not Padua IDs. Historical next-free boundaries confer no reservation.
No additional unreconstructed retired range was found in the ledgers; the
supplied population has no closed-unmerged PR needing separate recovery.

## Union and ownership

| Namespace | Highest used or permanently reserved | Own unchanged reservation |
|---|---:|---|
| PD-T | 391 | 364–375 (12) |
| PD-N | 145 | 132–137 (6) |
| IDEA | 489 | 454–465 (12) |
| LIT | 597 | 594–597 (4) |

PR21 reserves LIT482–561 only. PR24 reserves T324–363, N116–131,
IDEA414–453 and LIT582–593. Merged PR26 reserves T376–391, N138–145,
IDEA466–489 and no LIT; its main ledger explicitly acknowledges PR25's
unchanged reservation. PR25 priority is first publication
`ce17564ea1c185fea0be109b8ebb38efe25bceec`; original and current reservation
rows match. Repeated mentions/imports acknowledge their original owners,
rather than reserving overlapping blocks. Every proposed own ID is absent
from the three scientific registries at all four pins.

Eligible proposed mapping only: T01→T364, T03→T365, T04→T366, T05→T367,
T06→T368, T07→T369, T08→T370; N01→N132; IDEA01–08→IDEA454–461.
T02 remains unregistered and no LIT is assigned. If the orchestrator applies
that mapping, own permanent unused gaps are **T371–375, N133–137,
IDEA462–465, LIT594–597**. This scan assigns none of them.

## Preserved permanent unused ranges

The complete historical reservations remain binding, including unused IDs.
Explicitly recorded gaps from completed topics, carried forward unchanged:

| Topic / PR | PD-T gaps | PD-N gaps | IDEA gaps | LIT gaps |
|---|---|---|---|---|
| PR9 | 104–105 | — | — | — |
| PR14 | 118–135 | 054–061 | 228–245 | 429–444 |
| PR15 | 147–155 | 064–071 | 268–285 | 445–459 |
| PR12 | 198–205 | 074–077 | 312–315 | — |
| PR17 | 236–245 | — | — | 460–465 |
| PR19 | 253–265 | 087–091 | 349–355 | 471–473 |
| PR20 | 272–285 | 092–099 | 359–375 | 474–481 |
| PR22 | 291–293 | 101–103 | 380–383 | 569–573 |
| PR23 | 301–323 | 108–115 | 398–413 | 574–581 |
| PR26 | 382–391 | 138–145 | 472–489 | — |

Unassigned open-topic reservations PR21/24 remain wholly unavailable to
other owners. Their eventual unused portions are also permanent gaps.
No accepted identifier or earlier reservation is renumbered or recycled.

The orchestrator must refresh the live population and heads again immediately
before assignment/readiness; PASS applies to the pins above only.
