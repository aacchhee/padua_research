# Actual Syvert compact return —2026-11-07

All **273 previously missing degrees** and all seven controls passed.
Together with the accepted finite base and analytic tail n>=320, this
closes the all-degree mathematical gap: [G01](theory/G01-all-degrees.md)
proves exactly the two parity-correct nonnode corner maximizers for every
integer n>=2, with its explicit computer-assisted dependencies and limits.
The final substantive Claude audit remains required before PR readiness.

## Returned artifact and coverage

The actual archive is `syvert2-padua-compact-20261107T091106.535376Z.tar.gz`,
36,045,486B, SHA256
`b00fd57f85ce6d96a6c1fa01e2307abd815088bb8fcb28b1587657ef142b109a`.
It was supplied as two transport parts because the executor limits single
file downloads to32MiB. Concatenation aa then ab restores these exact
bytes. Actual off-Git path:
`local-output/argmax-bridge-20261105/actual-return-20261107/return.tar.gz`.
The user-supplied parts are retained in the chat attachments; their file
IDs are `file_00000000a26881f495a7c96369104fe1` (aa) and
`file_000000002ab08246b4e6947dffc9e660` (ab). No archive code was executed.

Production source: `996fedcad4ba79a28e45a3fe3678adc12f1e5358`.
Trusted separately released package:
`local-output/argmax-bridge-20261105/compact-release-aea62883/padua30`.
Manifest SHA256:
`5b89fa66e742952497f99a49110a965ada2828b1861917268d3074af0eb22a16`.
The unchanged scientific FREEZE and exact package regeneration/delivery
commands are recorded in [delivery](compact-delivery.md) and
[README](compact_pack/README.md).

Both developer and distinct reviewer actually executed:

```sh
python3 -I -S -B topics/padua-argmax-bridge-20261105/compact_pack/verify_compact.py \
  local-output/argmax-bridge-20261105/actual-return-20261107/return.tar.gz \
  --package local-output/argmax-bridge-20261105/compact-release-aea62883/padua30 \
  --manifest-sha 5b89fa66e742952497f99a49110a965ada2828b1861917268d3074af0eb22a16
```

Both PASS:280pairs, exactly41..319 plus511, all560 rational proofs checked.
There are no never-started or unfinished cases. All account/exit/source
links pass, final server state is quiescent/ECHILD with no cleanup/failure.
The returned4323-payload inventory and sampled complete closures pass.
All unsampled full histories were validated by the released collector on
Syvert; they were not transferred or independently inspected in full here.

## Random sample and independent native replays

Eligible population is precisely the273 completed residual degrees.
Persisted seed:
`7c79b8e401d9a32f8233f8371c441cd28d82dedd60e46e7c73d211ab099d01d2`.
`random.Random(bytes.fromhex(seed)).sample(sorted_eligible,2)` reproduces
the ordered draw **199,238**. Both complete histories passed local checking.

[Preregistration](evidence/compact-return/preregistration.json) was saved and
independently read before either native call. The exact executed
[runner](code/compact_return_replay/run_two.py) is copied without changes;
it belongs beside the preregistration/primary inputs in the original local
output layout. It is a provenance copy, not a rerun command for an already
occupied output directory. The underlying reproducible operation, using
fresh exclusive output paths and the pinned offline arithmetic library
path recorded in preregistration, is:

```sh
python3 -E -S -B TRUSTED_PACKAGE/topics/padua-argmax-bridge-20261105/code/final_hybrid_engine/engine.py \
  --mode verify --n N --output NEW_OUTPUT --run-once --certificate PRIMARY
```

Exactly two fresh verify-mode calls executed; no new primary/discovery,
substitute sample, retry or precision/cap rescue.

| Degree | Observed exit | CPU through summary | Fresh S / actual calls | Nodes / leaves |
|---|---|---|---|---|
|199|0|10.162178s|45 / 3|51 / 26|
|238|0|11.856834s|45 / 3|51 / 26|

Both final accounts are complete, first_failure=null, ECHILD=true and
cleanup empty. Original engine120CPU/pass and scientific stage/native
caps remain enforced. The outer-wrapper resource difference is disclosed
once in [LOG](LOG.md#completed-native-checks-and-canonical-resource-scope-disclosure);
these are not server-memory-limit measurements. CPU through summary is
not exact CPU through final return. Both samples are below256, so prior
511 checks and mathematical/source acceptance support the analytic-corner
branch rather than these two new replays.

Distinct [technical review](independent-checks-compact-return.md) executed
full fresh-pass validation and rehashed301distinct source/build/native/
runtime/closure identities. The retained tree, bounds, norm, floor,
corner/far predicates and exact rational verification fields match the
returned primaries. [Mathematical scope review](independent-checks-compact-return-math.md)
accepts the all-degree assembly and its trust/retention boundary.

## Observed production cost and retention

The280 primary pass CPU checkpoints range10.441..23.217s, median16.979s;
fresh passes10.098..22.497s, median16.015s. Their checkpoint sum is
9295.048013CPU seconds. The broader supervisor waited-descendant measure
is10496.346196s, about2.92CPU-hours, with12.181273s supervisor self CPU;
these are different scopes, not interchangeable exact final totals.
No actual peak-memory measurement is present. See the complete small
[statistics](evidence/compact-return/statistics.json).

The whole compact return and new raw/native histories remain offGit.
Small sampled primary/fresh certificates, accounts, observed exits,
preregistration, summary and result record are committed under
`evidence/compact-return/`. All-essential unsampled proofs remain in the
compact return. Unsampled full histories stay on Syvert, as explicitly
authorized by AC; no complete cold retention is claimed. External durable
delivery/retrieval of this new artifact remains unverified. Regeneration
uses the released source/pins/worklist/commands; historical timings/paths
need not match. [Cold-storage record](cold-storage.json) records custody.

These supplemental reviews do not replace the final Claude audit, waive
existing chronology findings, assign final IDs or authorize a merge.
