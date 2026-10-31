# Result status registry

No results are registered.

Use repository-global IDs `PD-T001`, `PD-T002`, ... for positive or unresolved result statements and `PD-N001`, `PD-N002`, ... for scoped negative results. IDs are unique across tracks. Provisional IDs include a topic slug and agent, for example `PD-T?charter-codex-01`. Allocate final IDs at PR preparation after checking main and pending reservations. Record the mapping in [ID_CROSSWALK.md](ID_CROSSWALK.md); never renumber merged results.

Every mathematical result, including a distinct measured claim, has a [theory file](templates/THEORY.md) when produced and a row here at PR preparation. Published statements use `LIT-nnn` in the literature database and do not inherit a research proof status.

Split substantive proved results into their own files/IDs so they keep PROVED. Keep an original unresolved target registered with its true status and dependencies on the split results; record the split in [ID_CROSSWALK.md](ID_CROSSWALK.md). Minor routine steps do not contribute to aggregation. PARTIAL requires explicitly identified parts of the target's statement, some PROVED under split-off IDs and the remainder OPEN; supporting lemmas alone leave the unresolved target OPEN.

REJECTED is a separate disposition, not a proof status. A refuted registered claim must show `REJECTED: refuted (see PD-Nnnn)` with a link to its refuting result in the disposition column. Check this column before relying on any row: a rejected claim is not a usable dependency even if its earlier epistemic status remains as history. PD-N is reserved for scoped refuted/failed mechanisms; its status describes the negative statement. Equivalent or abandoned candidates stay as IDEA dispositions and do not create administrative PD-N rows.

| ID | Statement and scope | Status | Status by mathematical part | Disposition / reason | Depends on | Theory file | Evidence / audit |
|---|---|---|---|---|---|---|---|
