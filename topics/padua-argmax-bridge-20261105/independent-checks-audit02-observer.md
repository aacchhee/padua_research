# Independent observer source and actual local artifact review

2026-11-07. **ACCEPT within the exact scope below. Real known-case integration
has not executed and remains subject to root release.** No unresolved MAJOR
or BLOCKING finding. This supplements, and does not replace, the Claude audit.

Reviewer requested/API-accepted Codex `gpt-6-astra` medium; actual serving
metadata unexposed. Rules were read at
`4a5de2012bad94601c713b2ff5517f2e3fb80af2`; read-only diff confirms those
AGENTS/WORKFLOW/CODEX rules unchanged at current inspection head
`0a14af36b581e2c8ed7771144a9daafdded05ed4`. No novelty or mathematical content;
the full-IDEAS technical-review exception applies. Root alone controls Git.

## Exact observer source

Read `code/audit02_observer/observe.py`, SPEC.md and PREREGISTRATION.md in full.
Source SHA256 verified independently:
`137b48c16a730e362e03dac37751ab00600b3d3cac1b29f006fbe5643ec93544`.
No observer execution or import was performed. Acceptance concerns this exact
source and the fixed command `/bin/bash /workspace/p02/run_rehearsal --workers 2`.

- Before children, it resets/refuses nondefault inherited SIGCHLD; validates
  every manifest byte, supplied manifest identity, source custody, engine
  freeze, rehearsal[41,511], and absent outputs. Linux pidfd APIs and inherited
  CPU soft/hard limits of at least260 (or unlimited) are required. It never
  imposes a lower inherited CPU limit.
- It becomes a subreaper before a single fork/exec. Direct `wait4` raw statuses
  and decoded exits are retained; ECHILD without an observed root status is
  failure. Completion needs root exit0, ECHILD, no ancestry-owned descendants
  and no recorded failure. No CPython subprocess ECHILD-to-zero path exists.
- Normal wall/signal shutdown gives owned descendants TERM, then KILL after15s,
  with bounded reap. Unexpected errors retain their failure and attempt bounded
  cleanup. Pidfds plus fresh ancestry/birth checks avoid ordinary PID-reuse
  signalling errors. It does not signal by process name or inspect environments.
- Hard observer death/power loss cannot promise cleanup or a final observation;
  missing complete evidence never permits retry. The script preserves output
  files and never narrows/restarts the plan.
- It records input/source identities, raw wait status, waited CPU, maximum
  reported wait4 RSS, wall duration, resource/space context, signals and cleanup
  outcome. Maximum wait4 RSS is expressly not concurrent aggregate RSS.
  Logical tree bytes may count aliases, as disclosed.

**Measurement limit:** `waited_cpu_seconds` sums child wait reports; the
observer's own CPU is not recorded in that field (nor separately measured by
this script). Do not label it total CPU including observer supervision.
Metadata traversal and hashing costs remain observer overhead. This does not
change the frozen per-engine120CPU cap or planned480CPU engine envelope.

The observer is execution evidence, not a scientific checker. Its accepted
code does not itself establish proof validity or prove actual two-worker
computation overlap; those require inspecting the returned known-case records.

## Actual artifact independently inspected, data only

The local build already existed before this review. A standalone Python
stdlib read-only inspection (JSON, SHA256, ZIP, `git show`) exited0; it imported
no candidate module and launched no compiler, loader, native oracle or engine.
Tool output chunk c8e968 records all assertions passing.

| Object | Independently checked identity/scope |
|---|---|
| Build source | `ffe4d42ba176d56db2e77c228bce28eda0872298` |
| `/workspace/p02.zip` | 25,085,718B; SHA256 `b41794138898198a391caa17a2b0a114e456ed690b994b41df8a5fbedc5bd2ba` |
| `/workspace/p02/runtime_manifest.json` | 52,438B; SHA256 `583435701282d0f22aa8d2d9429e735ed8c125b9cf285c3f6ac57983157c2eb4` |
| Local operations | 19 rows match accepted v3 manifest SHA256 `836dcbf098ecb391b740fa884e594e260b74705e88d26339dcc5cba9bbbf673f` |
| Scientific freeze | SHA256 `0d9ce0a5dbb7fb37cf1a05f07040b72d046b61b8d36b6a5a8bf137eb7d9914eb`; all13 code/data rows match |

Every one of240 runtime-manifest entries matched size/hash and was not a
symlink. All33 source paths equaled their bytes obtained with `git show` at
the build source SHA. All19 active top-level operations/launcher copies matched
accepted source hashes. The six bundled package archives matched their pinned
size/hash records, whose original constants were read during source review.
All asset provenance entries equal their manifest rows. The active library
directory has9 aliases, all FLINT/GMP/MPFR; no producer libc/loader is active.

All247 ZIP entries had unique safe names under `p02/`, and every ZIP payload
equaled its local unpacked file. The six top-level launchers have archive mode
100755; other entries have100644. ZIP and unpacked identity checks therefore
cover the actual artifact, unlike the earlier missing-ZIP limitation.

Plan data equals small[41,42,63,64,159,160,511], the273 residual degrees
43–62/65–158/161–319, their exact280 union, and rehearsal[41,511]. The package
outputs directory was absent at inspection: no local scientific admission
had occurred. The original Syvert2 archive was not rewritten or substituted.

## Remaining execution obligations

Root publishes the accepted observer and records its full source SHA, the
operations source above, manifest hash and fresh observer-output path before
release. The only prospective scientific work is four engine invocations:
primary/fresh41 and primary/fresh511, once each, two workers. No residual case
or campaign is authorized by this review.

Require directly observed observer exit0 and complete raw observation, then
genuine trusted data validation of both pairs, exact completed subset[41,511],
comparison of proof fields with accepted known certificates, actual affinity/
overlap evidence, pinned compiler/native loaded closure and storage/accounting
records. A data review is not an independently executed numerical rerun.

Native correctness, target Syvert2 behavior, four-worker scale, physical reboot,
full residual success/runtime/disk and cold-storage transfer remain outside
this acceptance. The previous12 synthetic-control passes and preserved initial
fixture failure remain in independent-checks-audit02-execution.md.
