# Local onset-512 certificates: preregistration

Recorded 2026-11-08 before any native call. Technical development requested as
Codex Sol medium; actual serving model/effort metadata are not exposed.
Rules/input HEAD: `b45e29fa1fe3dbfa2517ff8043e5d9c440870530`.
No novelty is claimed: this extends the frozen finite-check campaign only.

The exact population is every integer **320 through 510 inclusive**, 191 cases,
each a primary followed by a separate freshly compiled retained-proof verification.
Degree 320 is the actual first case and integration pilot, with no retry.
The remaining 190 cases use at most four workers on this sandbox's four-core
CPU quota and 16 GiB memory limit. No Syvert, SSH, or network compute is used.

The machine preregistration is outside Git at
`local-output/argmax-bridge-20261105/onset512-local-20261108/preregistration.json`,
SHA-256 `532e5af6af478d48546b4134635c296cd0aac5207de4df2955dda8b0fb7781a3`.
It lists all degrees, source/runtime file pins, Python identity, outputs and caps.
The runner's SHA-256 is
`459d0728a0cb264d241bc76d270209842fc2aa55c0fadd32e23f8e3b0523af9e`.
The unchanged engine FREEZE SHA-256 is
`0d9ce0a5dbb7fb37cf1a05f07040b72d046b61b8d36b6a5a8bf137eb7d9914eb`.

Per-pass engine CPU cap is 120 s; outer wall cap is 1050 s. Per-case wrapper CPU
soft/hard self-CPU limit is 260 s and address-space cap 2 GiB. The 260 s wrapper
limit does not aggregate its descendants; each pass's frozen engine enforces
its own 120 s aggregate CPU limit. All frozen scientific call/node/depth
limits remain unchanged. Each output and admission file is created exclusively.
The only allowed sequence is primary, full compact `validate_pass`, fresh,
full `validate_pass`, primary/fresh equality checks. Authenticated immutable
native artifacts may then be hardlinked by the existing compact storage routine.
All original paths/bytes, complete raw histories, logs, exits and accounting stay
locally retained outside Git. There is no retry, rescue, resume, substitution,
or extension outside the preregistered population. A failure stops new admissions;
already active cases finish and are recorded.

Observed `wait4` exits and resource usage are required for engine and wrapper
processes. SIGCHLD must be default; ECHILD cannot imply EXIT0. Subreapers,
parent-death signaling, signal handling and owned-descendant cleanup provide
the clean final quiescence record. PA1/PA2 are addressed by these local controls;
the frozen engine's internal stdlib waits remain as documented in audit-03 E-05.
This is a new clean epoch, with no recovery claim. The trusted compact validator
reads local files directly and does not execute any archive content.

Before preregistration, cheap exit-7, external-reap and ignored-SIGCHLD refusal
controls passed in `onset512-controls-20261108c`. Earlier controls directories
stopped in runtime preflight because the original cache lacked GMP headers/libs
and the MPFR shared-library target. Only absent runtime payloads were filled
from the already local compact release after checking byte hashes; no frozen
source was changed and no native call ran in those controls.

Commands, from repository root:

```
python3 -B topics/padua-argmax-bridge-20261105/code/local_onset512_campaign/runner.py pilot local-output/argmax-bridge-20261105/onset512-local-20261108
python3 -B topics/padua-argmax-bridge-20261105/code/local_onset512_campaign/runner.py remaining local-output/argmax-bridge-20261105/onset512-local-20261108
```

Computed success is pending independent mathematical review of the onset-512
gates, result review, and the next independent audit. It is not theorem adoption.
Full proofs must remain outside Git under the existing generated-output cap.
