# Permanent reservation — effective Padua argmax phase 2

Owner: `codex/padua-argmax-effective-2-20261105`. Date: 2026-11-05.
Reservation only; no final-ID assignments. The topic-local ledger follows
handoff01's write scope. Shared-ledger/crosswalk import is deferred to PR
preparation via literal proposed changes. The fresh-range procedure supersedes
historical owner-only prose; every earlier reservation and unused gap remains
permanent, including phase1's T253–265/N087–091/IDEA349–355/LIT471–473.

| Namespace | Reserved range | Count | Estimated need / headroom |
|---|---|---:|---:|
| PD-T | PD-T364–PD-T375 | 12 | 8 / 4 |
| PD-N | PD-N132–PD-N137 | 6 | 4 / 2 |
| IDEA | IDEA-454–IDEA-465 | 12 | 8 / 4 |
| LIT | LIT-594–LIT-597 | 4 | 2 / 2 |

[Complete review](allocation-review.md), [file-identity receipt](allocation-scan.json).
Forty complete ledger/registry reads across main and every open foreign PR;
11 distinct complete ledger versions. Union maxima before this reservation:
T363/N131/IDEA453/LIT593. All 21 returned closed PRs are merged; no missing
closed-unmerged reservation was found. Foreign bttb aliases are excluded with
explicit context review. No overlapping range or accepted-ID renumbering.

Immediately before publication, both the connector's open-PR query and
`git ls-remote` confirmed these unchanged heads:

- main: `21dbfc90257b952d8923f6d01739d12aa8d6e0a1`;
- PR21: `890f56ccde35431b70b43141c224b0b8817fea7f`;
- PR22: `1de5891ee622e826d7553819152aa261b02faaa9`;
- PR24: `79c3d6a211325eca6e8311b3ae03187c100a1d8a`.

Publication priority is the first pushed commit introducing this file, to be
linked in the draft PR body. Recheck the complete union before assignment,
additional reservations or readiness. Unused IDs remain permanent gaps.
