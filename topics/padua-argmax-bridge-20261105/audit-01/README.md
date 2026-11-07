# Interim Claude audit-01: review records and auditor scripts

These are the authored review reports of the five scoped Claude subagent
reviews behind [../audit-01.md](../audit-01.md), together with the small
scripts and outputs they executed. They were copied unchanged from the
auditors' session scratch directory (`/tmp/claude-0/.../scratchpad/audit/`).
That directory is ephemeral, so absolute paths inside the reports and
scripts record where each ran; they do not point to durable storage.

- `*-review.md`: authored review reports (not generated output).
- `code/<review>/`: auditor scripts and small outputs (each <16 KiB).
  These are not candidate code, and the candidate does not depend on them.
- Not committed: the auditor-built binaries (kernel, FLINT libraries), the
  mpmath install and fresh replay working files. Their identities and
  outcomes are given in the reports.

Rerun recipes are in each report's commands section. `code/root/` holds
the orchestrator's exact scalar check and the far split-point floor
estimate used in audit-01-ideas.md.
