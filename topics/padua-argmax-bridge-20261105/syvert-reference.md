# Syvert reference inspection (2026-11-06)

Authored reference report, not an executed campaign or a Padua launch approval.
Padua rules read at `ca8d52aa2a48c941473846ab884cccb25f1bdb9f` (`AGENTS.md`,
`agents/WORKFLOW.md`, `agents/codex/CODEX.md`). Technical inspection only;
no new mechanism, mathematical claim, novelty claim or ID allocation, so the
novelty gate does not apply. Requested allocation: Sol medium; runtime model
metadata is unexposed. Only the orchestrator mutates Git.

## Exact source and scope

Read-only GitHub connector inspection of `aacchhee/bttb-research`, pinned main
`5ed62a8d6be1dd98f462bbd97c8428ea2fcc6f54` (branch endpoint inspected on
2026-11-06; merge PR149). All links below use that immutable source. No clone,
remote mutation, dependency installation, reference execution or bulk source
copy into Padua was performed. Root recursive-tree fetch was too large; bounded
directory/tree browsing and exact file fetches sufficed. Connector code searches
returned no matches even for known `syvert2`, so absence from search is not evidence
of absence.

The actual A/B/C packs are
[`topics/banded-halfstrip-production/abc_syvert/`](https://github.com/aacchhee/bttb-research/tree/5ed62a8d6be1dd98f462bbd97c8428ea2fcc6f54/topics/banded-halfstrip-production/abc_syvert),
not the unrelated pySuperDC stepABC numerical records. Inspected full files:
`README.md`, `run`, `plans.py`, `build_pack.py`, `server.py`, `ordered_runner.py`.
The directory also contains `worker.py`, `calibrate.py`, `calibration_review.py`,
`test_plans.py`, listing helper, and the other launchers. This inspection did not
independently audit the reference worker's numerical algorithms.

## Actual A/B/C shape

| Aspect | Evidence from the inspected source |
| --- | --- |
| Delivery | One fresh directory per campaign, one prebuilt ZIP; never unpack over an old campaign or reuse its output. Producer runs locally, AC receives the complete committed numerical closure. |
| Launch interface | `run`, `run_small`, `run_large`, `finished_cases`, `collect_data`; `chmod +x` once, then `./run`. Small means n<=32 and R<=4, large is its complement; these are separate output directories. |
| Queue/cores | `run` invokes `beregning python3 -I server.py run`, supports an executable or shell function, and tries `module load beregning` if needed. `beregning` owns allocation. Supervisor uses inherited affinity only; one inherited core is leased for an entire comparison block. No idle-core scan, host-global queue, cross-campaign lock or aggregate CPU kill deadline. |
| Profiles | A on syvert2: 40 workers, 2 GiB worker address-space cap; B on syvert0: 16 / 3 GiB; C on syvert1: 10 / 4 GiB. Current supervisor soft cap 8 GiB. These are virtual-address limits, not physical RSS forecasts. Older delivered originals used 1 GiB supervisor cap and needed a separately recorded recovery overlay. |
| Work ordering | Longest estimated block first; fresh process for each observation. A mirrors arm order (forward then reverse); B/C use listed order once. Do not infer replication or order balancing for B/C. |
| Configuration | `plans.py` gives candidates and hardware profiles. Reviewed `calibration.json` freezes admitted cells, omissions and estimates. Positive completed anchors and phase-counter checks are required. Empty calibration intentionally refuses launch. Estimate scope, location and extrapolation remain explicit. |
| Guard | Planning gates check total estimated work and queue tail against the profile; per-case runaway guard is twice the largest expected job, rounded up. Guard is protection, not a planned timeout result or CPU measurement. |
| Package identity | `runtime_manifest.json`: campaign/profile, numerical commit, hardware profile, SHA256 map of packaged files. `server.py` rechecks all listed file bytes. A/B/C builder copies working-tree closure and records the supplied commit; unlike later F builder, it does not itself prove every copied byte belongs to that commit. A Padua builder should add that check. |
| Output tree | `outputs/<campaign>[/jobs/<block>/<index>/...]`; `run.json` freezes identity, manifest, blocks, settings, inherited affinity and selected CPUs. `campaign-status.json`, `summary.json`, `disagreements.json`; per-observation `status.json` / `result.json`. Writes use shared atomic helpers; output-directory lock prevents duplicate local supervisors. |
| Resume/failure | `./run --resume` requires identical manifest/blocks/profile/guard identity. Completed terminal outcomes remain untouched. Stale running observations become `interrupted`; retrying those requires `--resume --retry-interrupted`. Resume executes missing positions in original order and records qualification of interrupted comparison order. Supervisor exceptions and unfinished blocks persist in summary. Same-input successful output-hash disagreement raises an error. |
| Collection | `finished_cases` reports running/finished/pending/outcomes and rows. `collect_data` includes matching full/small/large outputs, manifest and listing helper; refuses source/campaign mismatch. Return ZIP name uses actual hostname, campaign and UTC. Live collection is a snapshot of atomic files, not a transaction across jobs. |
| Measurement discipline | Worker timing/memory conventions and numerical qualifications are in the README; exact checks for ordinary arms are outside public solver timing. Finite measurements do not establish asymptotics. Censored and refused outcomes remain visible. |

Useful source identities: A/B/C README blob
`bda340e5936386bf89c8ee63916d2948962cfce3`; launcher `run`
`cae658e3114f9f429f2771a514ed2543a70597cd`; plan
`6147b2f99adc3ce114ca785a825b90dea4fe9daa`; builder
`ead31402cc9945074ba05564a3782784d8f74d77`; server
`2644049bf5f9fa3712570728e61dc90cf57a7b9e`; ordered runner
`3cff8817267350023a2825cd25e75fe4e813af52`.

## Syvert2 facts and later useful examples

The later inspected
[`syvert_F/README.md`](https://github.com/aacchhee/bttb-research/blob/5ed62a8d6be1dd98f462bbd97c8428ea2fcc6f54/topics/paper-f-plan-audit/syvert_F/README.md)
states earlier-record host assumptions: **48 physical cores, 128 GB RAM,
CPython >=3.10, `beregning` available**. These are attributed reference facts,
not a live inventory. It packages pinned wheels offline, checks import/route/core/
RAM/limit prerequisites before workers, and keeps the same five A/B/C launchers.
Its builder blob-checks copied repository files against the explicit source SHA,
uses LF executable launchers and deterministic ZIP metadata, and rejects missing
pinned wheel bytes. Inspected `pins.py` supplies python-flint abi3 plus NumPy
CPython-specific wheel hashes. These dependencies belong to that campaign;
Padua must select its own required closure.

The newer inspected
[`paper-f-dense-lu-syvert-20261031/README.md`](https://github.com/aacchhee/bttb-research/blob/5ed62a8d6be1dd98f462bbd97c8428ea2fcc6f54/topics/paper-f-dense-lu-syvert-20261031/README.md)
uses **20 workers and 120 GiB budget on syvert2**, frozen measured-memory
reservations and a different `probe/run/analyze/finished_cases/collect_data/audit`
interface. Twenty is that campaign's worker choice, not a hardware core count.
Its final-v2 text explicitly removes startup memory calibration; its older
`PLANNING.md` still describes that gate. Do not import the obsolete gate or its
LU-specific reservations into Padua. Reference-specific source-audit acceptance
does not approve a new Padua pack.

## Possible eventual Padua shape and remaining unknowns

AC clarified on 2026-11-06 that packing is deferred until the end, only if the
remaining gap requires it; the mathematical work may close that gap first.
This inventory prepares no pack skeleton, files, scripts or jobs and does not
authorize starting packaging now. The following is a reference shape only.

A matching Padua pack can preserve the familiar fresh ZIP, `beregning` launcher,
five-command interface, committed source closure, immutable SHA256 runtime
manifest, inherited-core block scheduling, explicit frozen job plan, per-job
terminal records, strict identity resume, progress listing, and hostname/UTC return
ZIP. Add an independent data-only return checker and producer checker, following
the later F example rather than trusting the producer's declared commit string.
Only small authored summaries/receipts belong in Git; ZIPs, wheels and raw returns
need the Padua-specific storage destination authorized by AC.

Still to determine from Padua work: decisive jobs and exact inputs; arithmetic
backend and dependency/wheel closure; calibrated per-job time and memory; useful
worker count within inherited allocation; guard and failure meanings; outputs and
independent checker; audit and delivered ZIP identity. No reference file supplies
these Padua decisions. Live Syvert2 Python/OS/CPU-affinity facts and availability
of `beregning` remain unchecked. No Syvert2 run, performance claim or completed
Padua pack is claimed by this report.
