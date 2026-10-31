# <provisional or final result ID> — <title>

ID kind: <PD-T | PD-N>.
Aliases: <all names and close variants>.
Split from: <original ID and exact claim, or none>.
Split into: <new IDs and exact claims, or none; record the mapping in ID_CROSSWALK.md or PROOF_STATUS.md>.

## Statement

<Exact statement and quantifiers, including the mathematical/computational model.>

## Definitions

<Terms, objects and conventions used in the statement.>

## Assumptions

<Explicit hypotheses and parameter ranges.>

## Status by part

Overall status: <PROVED | PARTIAL | CONDITIONAL | MEASURED | OPEN>.

<Split substantive PROVED claims into their own files/IDs by default so they retain PROVED. A proved part is substantive if another result depends on it, it would be reported on its own, or its proof is not a routine step of the main argument. The original target references split-off proved parts without duplicating their proofs. Minor routine proved steps may stay with the main statement, but are excluded from status aggregation and never turn an OPEN main statement into PARTIAL. PARTIAL applies only when the target's own statement decomposes into explicitly identified conjuncts, cases or parameter ranges, some PROVED under split-off IDs and the remainder OPEN, with no other epistemic status. Proved supporting lemmas alone leave the target OPEN. The developer proposes the substantive/minor classification, the auditor checks it, and disputes go to AC.>

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|

Candidate / claim disposition: <REJECTED, if applicable; separate from statement status>.
Rejection reason: <refuted (negation established within stated scope) | failed (mechanism/candidate shown not to achieve its aim under stated hypotheses and range; never for a theorem whose proof attempt failed) | equivalent | abandoned; if applicable; equivalence or abandonment is an IDEA disposition>.

## Negative-result scope (PD-N only)

Attempted mechanism: <exact mechanism or candidate, with its ID>.
Parameter range: <range and hypotheses covered by the negative statement>.

<A PD-N requires a genuine negative mathematical statement with scoped failure/refutation evidence for a mechanism. Its overall status describes that statement's epistemic status, independently of the candidate's REJECTED disposition. Failed observations support MEASURED evidence within the exact tested scope, not a proof. Equivalence and abandonment belong in IDEA dispositions and do not alone warrant a PD-N.>

## Depends on

<Result IDs and exact hypotheses used; external published statements by LIT ID.>

## Checks

<Producer/checker/helper paths, frozen commands, commit SHA, file list, actual outputs and independent replay. List unrun commands as Runs needed.>

## Sources

<LIT IDs with page/theorem locators; explicitly label unread or unverified sources.>

## Proof or evidence

<Written proof, or measured evidence with its limits. A computer proof needs exact arithmetic, a proved reduction, committed code and committed essential evidence or a cold-storage manifest plus checker result.>

## Scope

<What the claim establishes; for a negative result, exactly which mechanism and hypotheses fail.>

## Open items

<Unresolved statements, dependencies, required computations and decisions; next unresolved step. Preserve any original combined target with its true status and a dependency on the split-off result.>

## History

<Date, agent/model/effort, commit and change. For splits or scope changes, preserve the original wording, changed wording and reason; do not hide an unresolved original target by narrowing its statement.>
