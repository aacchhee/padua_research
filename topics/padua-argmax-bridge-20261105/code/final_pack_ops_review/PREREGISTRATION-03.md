# Reviewer operational controls 03 — PROSPECTIVE / NOT RELEASED

Separate one-shot controls of the causal-state/FOPS-09 repair; 01 and 02 source,
fixtures, preregistrations and first failures remain unchanged. Root publishes
and internally releases the exact command below; no additional AC approval is
needed. No fixture imports or tests have run; only AST parsing occurred.

Source custody SHA256:
`b77b3c1da2eacb148ec49b4df369f203a4049dd3b8784115b2c9a5766d80360f`.
Root must record the published source SHA before execution.

| Fixture | SHA256 |
| --- | --- |
| review_controls_03.py | 587905c8560a184bb61a3a7e76fb5aed3272a0e3588c6c948064d70ec21f2e33 |
| fake_checker.py | f018c9db16812aeec6d067b08ab3d5744a9798845e5f883868715cdf16c88725 |
| fake_worker.py | b831316992c58fb607c0cd0147fc31aad1d1b36802a5e7dc4e85269db7d7770a |
| fixture.py | 8bbb46ffc79bcb398db5efde539bcf6ad8d4f6904c86d010c5f8937e705a96e0 |

Exact command from `/workspace/padua_research`:

```sh
python3 -I -S -B topics/padua-argmax-bridge-20261105/code/final_pack_ops_review/review_controls_03.py --source topics/padua-argmax-bridge-20261105/syvert2_pack --output local-output/argmax-bridge-20261105/final-ops-controls-03
```

Unchanged resource policy: fresh output only; 120-second harness alarm, 60 self
CPU seconds, 1 GiB harness address space, 128 MiB/10 CPU per fake case worker;
at most two simultaneous fake case workers and four total controlled processes
during fork controls. Inherited CPUs only, at least two required. File limit
16 MiB, aggregate output 64 MiB with root monitoring (not a quota), generation
reserve 48 MiB checked every forty synthetic degrees and final aggregate check.
Root preserves direct exit/stdout/stderr and allows at least 15 seconds for
SIGTERM cleanup before forced termination. First failure stops; no automatic
fix/rerun. All generated records and ZIPs remain off Git.

The harness substitutes fake case workers and the explicit NO_SCIENCE checker;
it never imports the actual scientific engine/checker, invokes native arithmetic,
compiler, real loader/extraction/builder or network. Synthetic records, interpreter
path, inherited affinity, actual boot metadata, absolute fresh paths and fixed
degree groups determine inputs; no random seed. Reduced scheduler plans and
mock preflight are confined to the fixture process; actual280 scope is used for
synthetic full-return validation. The actual collector's archive-space floor is
set to zero only for fixture collection, not a production capacity claim.

Retained controls include source/prose identity, shell syntax, synthetic full280
primary/fresh return and provenance/ZIP mutations, lock/resume, first failure,
timeout admission, owned double-fork cleanup, supervisor SIGTERM/SIGKILL and
quiescent collection, mock preflight refusal and isolated Python startup. The
second timeout worker remains 0.25 seconds with required non-timeout direct exit.

Additional causal-state controls run first:

- All-group guard refuses false/non-Boolean-true/ECHILD-false and wrong identity,
  source, plan or domain bindings for disjoint large admission, small resume
  and collection; missing/malformed summary and unknown group also refuse.
  A preflight assertion ensures a failed guard cannot silently reach admission.
- Real owned fake preflight orphan followed by exception or SIGTERM: verify false
  was persisted before spawning, no case entered, orphan killed/reaped, retained
  first failure and true only after ECHILD. A mocked cleanup failure leaves false
  and collection refuses. No numerical preflight runs.
- Missing/corrupt original resume provenance and changed current selected core
  set refuse before a case starts. Successful partial resume retains original
  domain and validates completed synthetic attempts.
- SIGKILL leaves an actual owned orphan and persisted false state. Collection
  refuses both before and after test-owned orphan cleanup; no manual quiescence
  reset occurs. SIGTERM cleanup/ECHILD permits collection with original domain.
- A Python audit hook rejects any attempted `/proc/*/environ` open in the harness
  and its forked supervisor. Owned `/proc/stat` cleanup remains allowed. The old
  removed scanner's direct permission tests are historical, not repeated or
  reported as passed by 03. Persisted domain identity tests remain applicable.

These checks do not establish real saved-proof schema compatibility; that is a
separately registered data-only check. They also do not establish scientific
correctness, production worker/native compatibility or Syvert2 portability.
The glibc>=2.38 requirement remains unresolved on Syvert2. Root executes and
reviewer later attributes evidence; no independent rerun is implied.
