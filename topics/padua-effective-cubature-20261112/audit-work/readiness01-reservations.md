# Readiness 01 — independent reservation refresh

Codex, `gpt-6-astra`, high, 2026-11-14. Rules read at
`b4e00bdaf2ea391489523c28a7f25f0f4fc24c49`; preparation candidate
`47892f13411132488a82e9dcd512d80dc543cd71`.

**Verdict: PASS within the pinned population below.** PR34's existing ranges
PD-T674–683, PD-N246–250, IDEA-756–765 and LIT-716–720 are uncontested.
No conflicting assignment, reservation, unknown retired reservation or
closed-unmerged PR was found. This is reservation readiness only; scientific
claims and registry wording are reviewed separately by the orchestrator.
No scientific computation was rerun. No Git state was mutated by this worker.

The scope has no novelty or mechanism assessment. Complete registry bytes were
scanned for identifiers and potentially foreign aliases; the scientific
content of every historical IDEA was not re-audited. All distinct allocation
ledgers were read, including their historical reservation and gap prose.

## Fresh remote population and complete head checklist

I independently called the GitHub connector's GET endpoints:

- `https://api.github.com/repos/aacchhee/padua_research/pulls?state=all&per_page=100&page=1`
- `https://api.github.com/repos/aacchhee/padua_research/branches/main`

The collection returned **34 PRs**, fewer than the page limit 100: open
**27, 34, 35**, all drafts; **31 closed, all merged**; **zero closed-unmerged**.
Closed merged PR numbers: 1–6, 8–26, 28–33. No PR7 was returned; the all-PR
collection, rather than the highest issue number, defines the population.
Consequently no additional closed-unmerged branch ledger required retrieval.

| Scope | Complete remote head | Ledger copies | Registry copies |
|---|---|---:|---:|
| main | `b5388c25a2a5ccb8d0faf816ab87023cf347bcd3` | 16 | 4 |
| PR27, `codex/padua-argmax-bridge-20261105` | `b918c1d5bedba60e8255d7d2b985dd6c70f4690a` | 17 | 4 |
| PR34, `claude/padua-effective-cubature-20261112` | `b4e00bdaf2ea391489523c28a7f25f0f4fc24c49` | 17 | 4 |
| PR35, `claude/padua-mz-paper-20261113` | `be28d3267bf6117878190b10f2d29840e524eac7` | 16 | 4 |

All four remote heads exactly match the local objects independently fetched
by the orchestrator. My subsequent work used read-only `git ls-tree`,
`git show`, `git rev-parse`, `git diff`, `git log`, and `git merge-base` on
these full SHAs; I performed no fetch, checkout, branch change or commit.

PR27 and PR35 have advanced since the preparation's reservation-time heads
`f4e8d8d313b1fec0cd4976de98524552fbdc94dd` and
`a0206a801e1d032175405db6ac7505e0691559fc`. Explicit old-to-current diffs show
**no change to any ALLOCATIONS.md or any of the four canonical registries**.
Both current peers' four registries are byte-identical to main. PR35 has no
own allocation ledger; its live PR body says it reserves no final-ID range.
PR27's unchanged own ledger retains T392–431/N146–161/IDEA490–529/LIT598–613.

## Complete source coverage

The scan consumed **82 full head/path copies**: **66 ledger copies** and
**16 registry copies**. Blob identities reduce these to **18 distinct ledger
versions** and **26 distinct versions overall**. Reuse of identical content
was based on exact Git blob identity, not filenames or presumed ancestry.

The same 16 ledgers occur on all four heads, with identical blobs:

- `topics/charter-unisolvence-20261031/ALLOCATIONS.md`
- `topics/nn-mop-conditioning-20261106/ALLOCATIONS.md`
- `topics/nn-mop-iep-20261103/ALLOCATIONS.md`
- `topics/nn-mop-stability-20261105/ALLOCATIONS.md`
- `topics/padua-3d-20261106/ALLOCATIONS.md`
- `topics/padua-argmax-alln-20261101/ALLOCATIONS.md`
- `topics/padua-argmax-effective-2-20261105/ALLOCATIONS.md`
- `topics/padua-argmax-effective-20261103/ALLOCATIONS.md`
- `topics/padua-batch-20261031/ALLOCATIONS.md`
- `topics/padua-lanczos-frontier-20261105/ALLOCATIONS.md`
- `topics/padua-lanczos-nonproduct-20261105/ALLOCATIONS.md`
- `topics/padua-lebesgue-followups-20261103/ALLOCATIONS.md`
- `topics/padua-literature-20261103/ALLOCATIONS.md`
- `topics/padua-mz-2d-frontier-20261105/ALLOCATIONS.md`
- `topics/padua-mz-cleanup-20261105/ALLOCATIONS.md`
- `topics/padua-mz-sharp-constants-20261106/ALLOCATIONS.md`

Additional ledgers:

- PR27 only: `topics/padua-argmax-bridge-20261105/ALLOCATIONS.md`, blob
  `02e33805a60dbf6dac3afe094791d40217a1c2d6`.
- PR34 only: `topics/padua-effective-cubature-20261112/ALLOCATIONS.md`, blob
  `fb962b0e42c101e67a4e5993dd03f4ed9380d537`.

The four canonical registries at **every** head were
`PROOF_STATUS.md`, `state/IDEAS.md`, `literature/INDEX.md`, `ID_CROSSWALK.md`.
The inventory retains every head/path/blob triple, byte count and namespace
maximum. Only the topic's own four registry versions differ from main.

## Union, ownership and priority

| Namespace | Highest foreign reserved/used ID, including permanent gaps | PR34 reservation | Assigned | Permanent unused |
|---|---:|---|---|---|
| PD-T | 673 | 674–683 | 674–679 | 680–683 |
| PD-N | 245 | 246–250 | 246 | 247–250 |
| IDEA | 755 | 756–765 | 756–762 | 763–765 |
| LIT | 715 | 716–720 | 716–717 | 718–720 |

The foreign maxima are attained by PR33's retained main ledger:
T554–673/N186–245/IDEA616–755/LIT636–715. All older ledgers, historical
reservations, unused headroom and imported blocks remain below those ends.
PR27's separate range is also below them. After PR34's reservation, union
maxima are **T683/N250/IDEA765/LIT720**. There are **zero foreign matches**
in any of PR34's four reserved intervals in the complete scanned ledgers
and registries.

The existing priority commit is
[`de39dabc7301b0de1463aaf2dab99365c4d7789e`](https://github.com/aacchhee/padua_research/commit/de39dabc7301b0de1463aaf2dab99365c4d7789e).
I verified that it is the sole addition commit for this topic's ledger, that
its original ledger contains the same four ranges, and that it is an ancestor
of preparation candidate `47892f13411132488a82e9dcd512d80dc543cd71`.
Its sole changed file is the new ledger (49 inserted lines). The live PR34
body links that full commit and records all reserved, assigned and unused
intervals. Thus the existing publication locator is preserved; no new
reservation, ownership transfer, renumbering or retrospective headroom is
being introduced. No competing reservation requires a priority adjudication.
The Git author/commit date was not used as a substitute for the PR-linked
publication identity.

### Qualified exclusions

The scanner includes qualified three-digit identifiers, abbreviated ledger
namespaces and omitted-prefix range endpoints; it also handles bare ranges
in namespace table cells. These exclusions were checked in context:

- Eight four-digit LIT aliases (1160, 1185, 1317, 1325, 1586, 1658, 1729,
  1750) refer to **bttb-research** records, not Padua reservations. Context
  appears in `literature/INDEX.md:225,233,238,239,271,339` and the related
  IDEAS/ledger disclosures. They are not truncated to three digits.
- The current topic ledger explicitly mentions `PD-T999` as a test fixture.
  Its original context is
  `topics/bivariate-lanczos-20261031/audit-05/check_integration_independent.py:298`,
  which writes a synthetic ID during a control.
- The same ledger explicitly mentions `PD-N303/N304` from unregistered audit
  prose, whose original context is
  `topics/padua-literature-20261103/audit-support/p3.md:15`.
  These are not canonical registry rows or reservations.

The two three-digit exclusions are applied only to those disclosure mentions
in PR34's own ledger. They are not blanket exclusions from arbitrary future
files. An initial conservative scanner run surfaced T999/N304;
after the contextual review, the scoped exclusion was added and the full
inventory rerun successfully. Historical “next unreserved” prose is not a
reservation and does not override the explicit permanent blocks.

## Executed commands and retained control

From `/workspace/padua_research`:

```
python3 -B topics/padua-effective-cubature-20261112/audit-work/readiness01_reservations.py
```

The audit-only source is 4,375 bytes, SHA-256
`35e71c6bc11c6b68283b28eafdd4088104fc481ebe39e77872f6039a15454a5a`.
It can run from any cwd and accepts `--output`. It reads the pinned Git objects
without mutating Git; it does **not** replace the fresh remote population
query or the semantic ledger review.

Other executed read-only commands include:

```
git for-each-ref --format='%(refname) %(objectname)' refs/remotes/origin refs/heads
git ls-tree -rl <each full head above>
git show <each head>:<each ledger or canonical registry>
git log --diff-filter=A --format=%H b4e00bdaf2ea391489523c28a7f25f0f4fc24c49 -- topics/padua-effective-cubature-20261112/ALLOCATIONS.md
git merge-base --is-ancestor de39dabc7301b0de1463aaf2dab99365c4d7789e 47892f13411132488a82e9dcd512d80dc543cd71
git show --format=fuller --stat de39dabc7301b0de1463aaf2dab99365c4d7789e
git diff --name-only f4e8d8d313b1fec0cd4976de98524552fbdc94dd b918c1d5bedba60e8255d7d2b985dd6c70f4690a -- ':(glob)**/ALLOCATIONS.md' PROOF_STATUS.md state/IDEAS.md literature/INDEX.md ID_CROSSWALK.md
git diff --name-only a0206a801e1d032175405db6ac7505e0691559fc be28d3267bf6117878190b10f2d29840e524eac7 -- ':(glob)**/ALLOCATIONS.md' PROOF_STATUS.md state/IDEAS.md literature/INDEX.md ID_CROSSWALK.md
```

Full off-repository inventory:
`/tmp/padua-readiness-reservations/inventory.json`, **28,734 bytes**, SHA-256
`8c42715d49cbb5f797420c9e3347bb89c90338c9791489fc4714033b4235dcb7`.
The compact API population is in `population.json` in the same directory;
no raw API payload or bulk registry copy is added to Git. Pinned Git sources
and the control reproduce the inventory if this temporary directory is lost.

## Remaining boundary

No missing head, unknown retired range or collision remains in the inspected
population. The orchestrator will repeat the live main/PR population query
and compare ledger/registry blob identities immediately before marking PR34
ready. Later readiness-only commits on PR34 do not change these reservation
facts if they leave the ledger and canonical ID registries unchanged. Repeat
the union review if main or another open PR's ledger/identifier content changes
before AC merges. Only AC merges.
