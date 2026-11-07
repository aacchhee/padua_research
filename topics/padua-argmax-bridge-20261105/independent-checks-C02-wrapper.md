# C02 replay-wrapper source review

2026-11-06, Codex coordinator, requested Astra high; serving metadata
unexposed. Reviewer of the wrapper is distinct from its author and from
the Sol prototype author. This is orchestration/provenance source review,
not a new mathematical acceptance or the required Claude audit.

Reviewed entire frozen code/cheap_C02/replay.py, SHA256
d3fc74dbf4f211fc3fce0f24b7fc6b90a1250a2ef6ee5b8112c58712582f98fa,
against the published prototype and unchanged check_r8.check contract.
The explicit Kernel does not patch acceptance, bounds or candidate leaves.
Its build adaptation changes only source/output paths; native source SHA
178bbe5a... is checked. Imported code/data and publication blobs are
pinned; no prose is a runtime dependency. Snapshot candidate gzip/plain
identities, complete364-leaf scope, no leaf cap and no output reuse hold.

The source rechecks compiler/header/TU/binary/linked and actual loaded
closure, transitive project Python imports, runtime, candidate and wrapper
before/after. Calls and first failed leaf are retained even on rejection.
No numerical failure triggers a source change, tree refinement or retry.
Worker RLIMIT178/179 and aggregate supervisor/group watch176 leave margin
under180totalCPU, including compiler helpers and supervisor. Interrupt
cleanup kills the process group. Success additionally requires complete
364/364,0failed/0pending,exit0 and unchanged provenance.

NOTE: the adapted builder retains its legacy variant label; the actual
prototype identity/source-origin and executed builder snapshot establish
the backend. This metadata label does not select numerical acceptance.
Syntax inspected with ast.parse; no full native or candidate execution by
this review. **ACCEPTED for the one prospective known-n32 replay** after
publication and explicit coordinator release. Selected-source controls
and mathematical review are in independent-checks-C01-prototype.md.
