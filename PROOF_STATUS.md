# Result status registry

No results are registered.

Use repository-global IDs `PD-T001`, `PD-T002`, ... for positive or unresolved result statements and `PD-N001`, `PD-N002`, ... for scoped negative results. IDs are unique across tracks. Provisional IDs include a topic slug and agent, for example `PD-T?charter-codex-01`. Allocate final IDs at PR preparation after checking main and pending reservations. Record the mapping in [ID_CROSSWALK.md](ID_CROSSWALK.md); never renumber merged results.

Every mathematical result, including a distinct measured claim, has a [theory file](templates/THEORY.md) when produced and a row here at PR preparation. Published statements use `LIT-nnn` in the literature database and do not inherit a research proof status.

Split substantive proved results into their own files/IDs so they keep PROVED. Keep an original unresolved target registered with its true status and dependencies on the split results; record the split in [ID_CROSSWALK.md](ID_CROSSWALK.md). REJECTED is a separate candidate disposition, not a proof status; a `PD-N` statement has its own epistemic status. Administrative records asserting no mathematical statement carry `not applicable` rather than an invented proof status.

| ID | Statement and scope | Status | Status by mathematical part | Depends on | Theory file | Evidence / audit |
|---|---|---|---|---|---|---|
