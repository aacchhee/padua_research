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

<Split substantive PROVED claims into their own files/IDs by default so they keep PROVED. A proved part is substantive if another result depends on it, it would be reported on its own, or its proof is not a routine step of the main argument. Only minor routine proved steps may stay with a differently classified main statement; label them below and follow the main statement's status. The developer proposes this classification, the auditor checks it, and disputes go to AC. PARTIAL is reserved for PROVED + OPEN parts, subject to the splitting rule and minor-part exception; do not use it for CONDITIONAL or MEASURED parts. OPEN labels an unresolved statement and does not deny proved dependencies under their own IDs.>

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|

Candidate / claim disposition: <REJECTED, if applicable; separate from statement status>.
Rejection reason: <refuted | equivalent | abandoned; if applicable>.

## Negative-result scope (PD-N only)

Attempted mechanism: <exact mechanism or candidate, with its ID>.
Parameter range: <range and hypotheses covered by the negative statement>.
Rejection reason: <refuted | equivalent | abandoned>.

<The overall status above describes the negative statement's epistemic status, independently of the candidate's REJECTED disposition.>

<Under the current broad PD-N rule pending AC's L5 decision, a bookkeeping-only equivalent/abandoned record with no negative mathematical statement marks its statement/status fields "not applicable — administrative disposition only"; it does not assert a theorem.>

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
