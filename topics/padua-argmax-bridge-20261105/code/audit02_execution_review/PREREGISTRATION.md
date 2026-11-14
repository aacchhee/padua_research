# Independent synthetic operational controls — preregistered, unexecuted

Reviewer: requested/API-accepted Codex gpt-6-astra medium; serving metadata
unexposed. Rules input 4a5de2012bad94601c713b2ff5517f2e3fb80af2.
No mathematical/novelty content. Root alone publishes and releases execution.

Exact candidate manifest SHA256:
`836dcbf098ecb391b740fa884e594e260b74705e88d26339dcc5cba9bbbf673f`.
Harness `controls.py` SHA256:
`7c1bb8d43c81f539dbfe74cd359b84dcb7af71ee5a8ef893188cc1351df135d5`.
The harness verifies all 19 candidate rows before its first case. No candidate
imports, fixture execution, compiler or native call occurred while preparing
this record. A Python text-edit command modified harness text only.

## Command and budget

After publication and root release, from repository root:

```
python3 -I -S -B topics/padua-argmax-bridge-20261105/code/audit02_execution_review/controls.py --source topics/padua-argmax-bridge-20261105/code/audit02_execution --output /workspace/p02c
```

Output must be absent. Never retry that output or overwrite a failed receipt.
Fixed order is status7, ignored, echild, hup, quit, parentdeath, reboot,
preflight, deleted, partial, zipbounds, pin. Each subprocess has 10/12-second
CPU soft/hard limits and a 20-second wall limit; 12 cases give at most144
self CPU seconds and240 wall seconds, within the180/300 preregistered envelope
with small observer overhead. All ordinary/fake subprocess workloads are
exit, sleep or bounded metadata work; no compiler or numerical oracle exists
in the fixture. The observer is a subreaper, kills/reaps only its descendants
on timeout, including separate sessions, and treats surviving processes as
failure. Stop at the first failed case. Root observes outer EXIT status and
retains all receipt/stdout/stderr and fixture files. Large fixtures remain off
Git; a short result record may be committed under the repository size policy.

## What each fixture tests

| Case | Fixed test and acceptance |
|---|---|
| status7 | Real child exits7; strict wait returns7, repeat poll stays7. |
| ignored | Set SIGCHLD ignored before Popen; refuse before child, normalize DFL, emit original-disposition stderr record. |
| echild | Reap real exit7 child outside its Popen; subsequent poll raises ChildProcessError with returncode still None. |
| hup/quit | Actual server dispatcher, fake worker plus stubborn sleeping descendant. Deliver signal after descendant exists; require strict quiescence and no surviving fake descendant. |
| parentdeath | Actual worker under a disposable supervisor, fake sleeping engine. Kill supervisor; require worker/engine termination via worker PDEATHSIG cleanup; independent observer reaps. |
| reboot | Actual collector on a stopped quiescent fixture. Simulate changed boot reader; require preserved original domain and new collection boot. Set state false, require collection refusal. This is not a real reboot experiment. |
| preflight | Actual dispatcher with failing synthetic inspect, then successful synthetic inspect. Require no first admission, second preflight epoch, preserved old failure, and only subsequent fake attempts. |
| deleted | Run terminal fake failures, remove their directories retaining ledger; resume must refuse the missing-admission gate without rerun. |
| partial | Real archive/manifest/history/ledger/partition path with one sentinel-completed and one failed attempt. Explicitly replace validate_attempt with an independent sentinel only to test routing; require completed=[41], failed=[511], never_started=[], complete280=false. Replacement validator rejection must propagate, never demote completed to failed. |
| zipbounds | Oversized central-directory member must refuse before read; actual tiny ZIP with inventory-size mismatch refuses. |
| pin | Actual preflight against four synthetic required asset files with wrong hashes; assert the arithmetic-byte gate refuses before the loader function can be called. Host prerequisites remain real. |

## Fixture substitutions and limits

Each isolated case copies candidate source. Except parentdeath, the worker
is replaced by the literal FAKE_WORKER source in the harness. The parentdeath
case retains the real candidate worker and replaces only its scientific
engine with the literal sleep script. Every fixture supplies an inert checker
module and a synthetic manifest over the actual fixture files. Dispatcher
preflight is replaced except in the pin case. These substitutions are not
claimed to be a released artifact or scientific proof validation.

The partial test establishes routing/coverage/error propagation, not genuine
validate_pass closure; the separately preregistered actual41/511 rehearsal
must test that. Controls do not demonstrate full Syvert2 behavior, NFS lock
semantics, a physical reboot, arbitrary hostile history rewriting, or native
engine correctness. No residual degree is evaluated; the degree names in
fixtures are identifiers only. Actual known-case integration remains a
separate release after these checks.
