# Protocol and pinned input inspection

Rules read at `cf89b140530d5838bdb208a8c28f3e7aa676ace3`: AGENTS.md,
agents/WORKFLOW.md, agents/codex/CODEX.md. Mechanical protocol worker;
requested model gpt-6.1-sol medium. Runtime identity is not independently
exposed. Root owns Git and every allocation decision. This worker writes
only this protocol directory and makes no new scientific claim.

## Permanent range scan

The GitHub connector refresh discovered that PR9 had merged while the scan
was running. Root fetched main at
`806cc7b4509fd93bae652f9545d32d95529f8281`. PR12 is the sole open draft,
at `12e9cf4539d0977773cad75fc74f93d1664cb429`; it explicitly carries no range.
The 12 returned PRs were individually checked: 11 are closed and merged,
none closed and unmerged. Branch pagination was exhausted at cursor null.
The PR search tool exposes a topn bound rather than a page cursor; the
complete all-state result contains 12 entries against topn100, and the
separate closed-unmerged query is empty. No further PR search page exists
in the connector schema. See [connector receipt](github-scan.json).

All bytes of the four final-ID registries, both ALLOCATIONS.md ledgers,
and every other tracked Markdown path matching allocation/reservation/ledger
were read at current main, PR12 and the retained PR9 source. Each source's
commit, blob, byte count and SHA256 are in [reservation-scan.json](reservation-scan.json).
The scan includes historical reservation prose and available preservation
notes; there is no closed-unmerged reservation requiring retirement.

The highest reserved-or-assigned IDs are PD-T105, PD-N043, IDEA-209,
LIT-426. The suggested fresh ranges, with 50% headroom over root's estimate,
are PD-T106–135 (30), PD-N044–061 (18), IDEA-210–245 (36), LIT-427–444 (18).
These are recommendations only. Root must publish the reservation in the
shared batch ledger and PR body. No final IDs are assigned by this scan.
Recheck reservations before assigning final IDs and before readiness.

Historical NEXT-unreserved boundaries are not reservations. LIT-1729 and
LIT-1750 in the four registries explicitly denote another repository's
records, not Padua namespace allocations. PD-T104–105 remain permanent
unused PR9 headroom; the latest assigned PD-T result is PD-T103.

## A1 and A2 source status

[input-manifest.json](input-manifest.json) pins 25 relevant source/evidence
objects by commit, repository path, Git blob, SHA256 and byte size.

A1 is PD-T101, PROVED with Claude audit-01 ACCEPTED and administrative
dispositions preserved. PR9 is merged into current main. Its scope is the
exact corner identity for every n>=1, all four corners and the stated even
checkerboard, with continuous singular limits. It supplies no global argmax
or asymptotic conclusion.

A2 records01–04 remain developer PROVED claims at the PR12 pin with the
required Claude audit PENDING. Their independently reported Codex hand
checks/reruns supplement that pending audit. The scope and dependency
qualification are recorded in the manifest. Their literal A1 audit-pending
labels are stale upstream text; this inspection does not edit that source.
No scientific run, independent rerun or scientific audit was performed by
this worker. Root and mathematical workers determine what can be used
under the campaign's source-status rules.
