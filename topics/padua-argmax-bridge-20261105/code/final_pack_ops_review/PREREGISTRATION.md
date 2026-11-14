# Reviewer operational controls 01 — PROSPECTIVE / NOT RELEASED

Reviewer `/root/final_pack_ops_review`; root alone grants the internal execution
release under AC's existing audit-then-run authorization. No new AC permission
is requested. No fixture imports/tests have run; four Python files were parsed
with the standard-library AST parser only. Preserve the first outcome, including
fixture failures. Do not edit and rerun under this registration.

## Exact source and fixtures

Operational Python code is the source-accepted repaired candidate identified by
custody SHA256 `b231408769469a5928ee8998036ef2421f4c3af6dd647126b33cc06487985965`.
The later README-only portability clarification changes custody to
`a9e30423e3d33670817753cdc979fcf1a9c5c287b635c8197b37d6faf2803cfd`; no
operational code, plan, pins or caps changed. Root must publish those bytes and
record the source commit before release. Fixture identities in this directory:

| File | SHA256 |
| --- | --- |
| fake_checker.py | f018c9db16812aeec6d067b08ab3d5744a9798845e5f883868715cdf16c88725 |
| fake_worker.py | b831316992c58fb607c0cd0147fc31aad1d1b36802a5e7dc4e85269db7d7770a |
| fixture.py | 8bbb46ffc79bcb398db5efde539bcf6ad8d4f6904c86d010c5f8937e705a96e0 |
| review_controls.py | 13e423b3bb9d6776c7af0da6855f75d0cb59da70858d2b4e179c19f7b35b254e |

The harness copies operational Python into fresh off-Git synthetic package
directories. It replaces `job_worker.py` with the bounded fake worker and the
scientific checker path with `fake_checker.py`. No scientific engine, native
source, actual certificate, arithmetic package or oracle is copied/imported/
executed. No compiler, extraction, setup, package installation or network call
is allowed. The stub always labels its input `NO_SCIENCE`; it proves nothing.
Synthetic native binaries/TUs are plain text, never loaded. All inputs arise
deterministically from these fixture bytes, the declared degree groups, current
interpreter identity, inherited CPU set, absolute fresh output root and fixed
timeout values. There is no random seed or external input corpus.

## Planned command and caps

Run once from `/workspace/padua_research`, after root release:

```sh
python3 -I -S -B topics/padua-argmax-bridge-20261105/code/final_pack_ops_review/review_controls.py --source topics/padua-argmax-bridge-20261105/syvert2_pack --output local-output/argmax-bridge-20261105/final-ops-controls-01
```

Fresh output only; an existing directory refuses execution. Capture command,
direct return code and stdout/stderr in the root execution receipt. One harness
process, at most two simultaneous fake case workers; the orphan control can
briefly create three descendants during its double fork. The signal control
uses one child supervisor and one fake case worker. At most four processes
including the harness exist in these controlled trees; unrelated processes are
not targeted. CPU affinity is inherited; the scheduler fixture needs at least
two inherited CPUs and refuses otherwise.

Harness RLIMIT_AS 1 GiB and self RLIMIT_CPU 60 seconds; fake case worker
RLIMIT_AS 128 MiB and RLIMIT_CPU 10 seconds. Harness alarm 120 seconds total;
scheduled fake case timeout is 0.3 seconds in the timeout test, followed by the
unchanged ten-second operational TERM/KILL escalation. Other fake waits are at
most 25 seconds and are killed/awaited by ownership-scoped cleanup. No production
cap is modified: timeout values change only in the imported fixture process.
Per-file RLIMIT_FSIZE 16 MiB. Total generated output cap 64 MiB, generation
reserve checked every forty synthetic degrees at 48 MiB and final size checked
before success. Root execution must additionally monitor aggregate output and
stop the owned control tree if 64 MiB is reached; this is an output cap, not a
claim that RLIMIT_FSIZE imposes a filesystem quota. Retain all output on failure.
SIGTERM/SIGINT and the alarm raise into the harness's final owned-descendant
cleanup. Root should allow at least fifteen seconds for that cleanup before
external forced termination; capture any forced termination as incomplete.

## Coverage and explicit omissions

1. Five Bash launchers receive `bash -n`; check exact 7/273/280 scope, unchanged
   runtime acceptance after a prose-only change, and changed frozen code refusal.
2. Actual server lock collision, partial never-started resume, changed-worker
   refusal, preservation of completed attempts, and corrupt wrapper-EXIT refusal.
   Synthetic pass records exercise the same `validate_attempt` used by resume.
3. Actual scheduler first-failure and timeout admission stop with two fake workers,
   pending third case, TERM resistance, bounded KILL and ECHILD. Separate real
   setsid/double-fork processes exercise marker refusal and subreaper cleanup.
   The timeout fixture's second worker sleeps 0.25 seconds, and its direct exit
   must show no timeout; this checks that a newly freed slot is not refilled
   after observing the first worker's timeout. A scheduling failure of this
   fixture requirement is retained as first failure, not retried.
4. SIGTERM and SIGKILL of an actual fixture supervisor while a fake writer is
   live; collection must refuse, including orphan writers after SIGKILL and
   absent persisted quiescence after cleanup. Every test-owned child is awaited.
5. Actual data-only return validator over all 280 synthetic primary/fresh pairs;
   real semantic checks with an explicitly fake arithmetic checker. Remove TU
   from both ZIP and custody index, remove wrapper EXIT0, alter raw linkage,
   started identity, failure and primary-copy linkage, and reject traversal,
   duplicate ZIP members and wrong released manifest. No scientific validity or
   numerical correctness is tested. Other proposed negative variants remain
   covered only to the extent listed here; do not report unimplemented variants
   as executed controls.
6. Git-free synthetic package; real preflight refusal of wrong host, missing
   system tool and missing offline prerequisites. Incompatible-loader refusal
   uses a mock subprocess result: no real loader/library compatibility claim.
   Harmless `sitecustomize` marker verifies `-E -S -B`/`-I -S -B` suppression.

An actual archive builder, six-package extraction, real offline dependency
compatibility, Syvert2 startup, production job worker, scientific proof checker
and final return review remain separate. Root reports actual pinned GMP requires
glibc >=2.38; Syvert2's version remains unknown. The mock preflight does not
resolve that portability limitation. Success means only the enumerated
operational controls passed on this host under these explicit substitutions.

## Results destination

All raw generated trees/ZIPs remain below the declared off-Git output root.
`receipt.json` records first failure/events, wall and self/waited-child CPU.
The report may retain a short authored outcome with exact hashes/observed exit;
no generated fixture corpus enters Git. No automatic rerun follows failure.
