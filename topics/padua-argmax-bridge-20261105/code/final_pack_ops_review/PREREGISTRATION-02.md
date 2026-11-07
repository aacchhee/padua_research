# Reviewer operational controls 02 — PROSPECTIVE / NOT RELEASED

Separate prospective run after FOPS-07 source repair. Run 01 remains preserved
at its original source/fixture identities and failed outcome; it is not rerun.
Root alone publishes and internally releases this command under existing AC
authorization. Reviewer has performed static reading and AST parsing only.

## Exact sources

Operational candidate custody SHA256:
`6d32521c6856a615ff49a52d6f0184d4ea6dabf041108f25233cf00c1d5fbe7a`.
Root must record its published source SHA before executing. Reused helpers
remain exactly those of 01; the new harness is a separate file:

| File | SHA256 |
| --- | --- |
| fake_checker.py | f018c9db16812aeec6d067b08ab3d5744a9798845e5f883868715cdf16c88725 |
| fake_worker.py | b831316992c58fb607c0cd0147fc31aad1d1b36802a5e7dc4e85269db7d7770a |
| fixture.py | 8bbb46ffc79bcb398db5efde539bcf6ad8d4f6904c86d010c5f8937e705a96e0 |
| review_controls_02.py | c7942287c3684fa49dd8cfe31b7109babf7020a1481a709822bf030140f93c45 |

These are all fixture input sources. They generate deterministic synthetic
NO_SCIENCE evidence using declared degree groups, absolute output paths,
interpreter identity, inherited CPU set and real boot/process metadata; no
random input. Operational code is copied into fresh synthetic packages, the
job worker replaced by the bounded fake worker, and scientific checker path
replaced by the explicit stub. No scientific engine/checker, compiler, native
code, arithmetic asset, real certificate or network is imported/executed.

## Exact command and unchanged resource policy

Run once from `/workspace/padua_research` after publication/release:

```sh
python3 -I -S -B topics/padua-argmax-bridge-20261105/code/final_pack_ops_review/review_controls_02.py --source topics/padua-argmax-bridge-20261105/syvert2_pack --output local-output/argmax-bridge-20261105/final-ops-controls-02
```

An existing output directory refuses. Preserve direct EXIT, stdout/stderr and
the first failure; no fix/rerun under this registration. Same caps as 01:
120-second harness alarm, self CPU 60 seconds, 1 GiB harness address space;
128 MiB/10 CPU per fake case worker; at most two simultaneous fake case workers,
four total controlled processes during the fork controls; inherited affinity
only, requiring at least two CPUs. Per-file limit 16 MiB; total output cap
64 MiB, fixture-generation reserve check at 48 MiB every forty degrees and final
aggregate check. Root must independently monitor aggregate bytes and stop the
owned control tree at the cap; this is not a filesystem quota. Allow at least
15 seconds for SIGTERM-triggered owned-descendant cleanup before forced kill,
and report forced cleanup as incomplete. All output remains off Git.

Actual production CPU/memory/group/plan policies are unchanged. Fixture-only
scheduler plans use two/three cases, with a 0.3-second fake timeout and the
unchanged ten-second TERM/KILL escalation. The second timeout worker sleeps
0.25 seconds and must exit without its own timeout. The actual quiescent
collector is additionally exercised with its archive free-space floor replaced
by zero **in the fixture process only**; this tests domain/custody behavior,
not available production capacity. No aggregate cap is relaxed.

## Coverage

Retain the enumerated six-group synthetic controls and omissions in
`PREREGISTRATION.md`: source/prose identity and shell syntax, full280 synthetic
primary/fresh return validation, corrupt provenance/EXIT/linkage/ZIP refusal,
partial resume, first failure and timeout admission, real owned setsid/orphan
cleanup and supervisor signals, mock preflight incompatibility and safe Python
startup. As in 01, arithmetic checking is stubbed and real loader/asset/build
compatibility remains untested. The new shared plan validator is deliberately
given the same reduced fixture plan as the scheduler; full-return testing uses
the actual 280-case plan.

Additional FOPS-07 controls:

- Exercise the real scanner with a synthetic `/proc` view: strictly pre-floor
  process with unreadable environment is skipped without environment access;
  equal/post-floor environment denial and unreadable candidate birth metadata
  propagate `PermissionError`; birth-tick change while excluding an old PID
  refuses. Restore all scanner bindings afterward.
- Under a real campaign lock, verify original domain retention; missing floor
  with existing run, wrong token/floor/instance, boot mismatch, and a replacement
  earlier floor with recomputed token all refuse. Existing run binding must catch
  valid-token replacement even when the proposed floor is not in the future.
  Restore original bytes after every mutation.
- Actual partial resume must preserve exact original domain bytes. Separate
  instances must reject each other's domain.
- For signal controls the parent establishes the original domain under lock
  before forking the operational supervisor. Child admission and later parent
  collection both retain this earliest floor. This deliberately exercises the
  earlier registered supervisor case without confusing an older collector's
  birth with a newly created child floor.
- After supervisor SIGKILL, the real orphan marker check must specifically
  report an owned package writer; collection also refuses. After orphan cleanup,
  interrupted output without quiescence still refuses. After SIGTERM/ECHILD,
  actual collection must preserve identical domain in `COLLECTION.json` and
  archived `outputs/writer-domain.json`.

## Interpretation

Only enumerated checks that actually complete may be reported. A first failure
stops the suite, preserves evidence and returns to focused diagnosis. Passing
controls do not establish mathematical correctness, independent scientific
review, production job-worker/native compatibility or Syvert2 portability.
The known pinned GMP glibc>=2.38 requirement remains unresolved on Syvert2.
Root executes; reviewer later inspects and attributes the results, without
claiming an independent rerun it did not perform.
