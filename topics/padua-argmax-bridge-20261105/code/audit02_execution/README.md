# Local audit-02 operations candidate

UNEXECUTED; distinct review and root release required. This is a new local
operations source variant, not the released Syvert2 ZIP. See SPEC.md,
PREREGISTRATION.md and feasibility.md. Original pack and scientific engine
sources remain immutable. Source identity is CANDIDATE.sha256; rebuilds
must identify a new published source and new artifact hash.

The prospective local builder makes a short exclusive /workspace root using the
six pinned Debian packages already in Padua local-output. No download or
system-version fallback exists. The package remains self contained with
the unchanged engine's full relative source tree. The local launcher uses
inherited affinity directly, without beregning or a Syvert2 hostname gate.

Default two workers. Stop on first failure. No retry of a scientific
attempt. Resume only untouched never-started cases; a preflight-only failure
can create a new preflight epoch while retaining every prior record. Partial
return validation reports exact validated completed pairs, failed/interrupted
admissions, and never-started degrees; it never certifies the whole gap.

Hard kills keep nonquiescent state fail closed. Worker parent-death SIGTERM
requests cleanup, not an unconditional whole-tree kill guarantee. Collection
after reboot only accepts already strictly quiescent persisted runs and keeps
their original writer domain. No handwritten collection attestation is valid.

All raw proofs, builds and failures are retained off Git. Collection hashes
and compresses in bounded chunks, measures archive peak before writing, and
preserves raw data if space is insufficient. Short paths prevent avoidable
receipt growth; the strict 16384-byte cap remains unchanged. Never trim a
witness to fit a path, disk or Git limit.
