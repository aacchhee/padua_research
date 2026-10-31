# Identifier crosswalk

No mappings or reservations exist. Final IDs are repository-local. Preserve the provisional ID, source branch and pinned commit as provenance. Use provisional patterns `PD-T?<topic>-<agent>-<n>`, `PD-N?<topic>-<agent>-<n>`, `IDEA?<topic>-<agent>-<n>` and `LIT?<topic>-<agent>-<n>`.

Once reservations exist, link the single authoritative `topics/<batch-slug>/ALLOCATIONS.md` ledger here and from every member PR/log. A standalone topic uses `topics/<topic-slug>/ALLOCATIONS.md`. Each ledger has one allocation owner who reconciles current main and all active reservations before allocating; concurrent PRs do not allocate independently. No allocation ledger is needed yet because no IDs are reserved.

| Provisional ID | Final ID | Source branch / commit | Canonical file | Allocating PR / batch |
|---|---|---|---|---|

## Original-to-split result mappings

Record one row per split, retaining the original target's true status and canonical home. The original and split theory files also name `Split from:` / `Split into:`; substantive proved results keep PROVED under their exact statements. Narrowing or rewording is recorded in History, not hidden by a split.

| Original target ID / file | Split result ID / file | Relation / exact scope | Source commit | Reason / history |
|---|---|---|---|---|
