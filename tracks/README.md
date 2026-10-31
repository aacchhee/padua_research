# Scientific tracks

No scientific tracks have been selected. Create `tracks/<slug>/` when the campaign charter identifies a coherent research direction; do not infer the subject from the repository name.

Each track contains:

- `README.md`: question, assumptions, scope and links to its results.
- `theory/`: durable result files using [THEORY.md](../templates/THEORY.md), including scoped negative results.
- `NEGATIVE_RESULTS.md`: negative-result IDs, exact scope and evidence links.
- `AUDIT_LOG.md`: one row per independent audit verdict, with result ID, pinned commit, auditor, finding and evidence.
- Manuscript directories when needed.

Use global `PD-Tnnn` and `PD-Nnnn` IDs from [PROOF_STATUS.md](../PROOF_STATUS.md). Do not restart numbering for each track. Literature statements stay in the literature database; topic checks are evidence, not the sole home of results.
