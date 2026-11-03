# Proposed shared-record changes — not applied during WORK

The handoff restricts writes to this topic and its results file. Shared records
and merged theory bodies are untouched. These literal old→new rows are proposals,
subject to required Claude audit and later preparation. Replace descriptive
provisional paths by the actual assigned IDs at preparation, preserving all
original-to-split mappings and histories.

T1 PD-T180/184 changes will be proposed only after complete evidence exists.
PD-T181 (global degree-eight argmax) and PD-T099 are not changed here.

## PD-T098 — proposed PROOF_STATUS row

Old:

```text
| PD-T098 (PD-T?programme-ideas-claude-04) | Second-order expansion of the Padua Lebesgue function at the non-node corner (conjecture) | OPEN | finite evaluations MEASURED; pre-registered fit c ∈ [1.846095, 1.846161]; post-registration fit stability MEASURED; expansion OPEN; A1 exact finite identity split to PD-T101 (PROVED); expansion remains OPEN | OPEN target, not rejected; open targets A1–A3; A1 closed; A2 closed; full A3 remains OPEN | None; PD-T101 (exact identity only) | [record](topics/programme-ideas-20261031/theory/programme-ideas-claude-04-padua-corner-expansion.md) | [response-01](topics/programme-ideas-20261031/response-01.md); [Codex audit-01](topics/programme-ideas-20261031/audit-01.md); [Codex audit-02](topics/programme-ideas-20261031/audit-02.md) and [audit-03](topics/programme-ideas-20261031/audit-03.md): accepted at written scope; [integration audit-04](topics/programme-ideas-20261031/audit-04.md); [Claude audit-01](topics/padua-proof-attempts-20261101/audit-01.md); [response-01](topics/padua-proof-attempts-20261101/response-01.md); PR12 dated split: A2 is closed by PD-T156, PD-T157, PD-T158 with supportPD-T159; full A3 remains OPEN. |
```

New (after required audit and final-ID preparation):

```text
| PD-T098 (PD-T?programme-ideas-claude-04) | Second-order expansion of the Padua Lebesgue function at the non-node corner (conjecture) | OPEN | finite evaluations MEASURED; pre-registered fit c ∈ [1.846095, 1.846161]; post-registration fit stability MEASURED; expansion OPEN; A1 exact finite identity split to PD-T101 (PROVED); expansion remains OPEN | OPEN target, not rejected; open targets A1–A3; A1 closed; A2 closed; full A3 remains OPEN | None; PD-T101 (exact identity only) | [record](topics/programme-ideas-20261031/theory/programme-ideas-claude-04-padua-corner-expansion.md) | [response-01](topics/programme-ideas-20261031/response-01.md); [Codex audit-01](topics/programme-ideas-20261031/audit-01.md); [Codex audit-02](topics/programme-ideas-20261031/audit-02.md) and [audit-03](topics/programme-ideas-20261031/audit-03.md): accepted at written scope; [integration audit-04](topics/programme-ideas-20261031/audit-04.md); [Claude audit-01](topics/padua-proof-attempts-20261101/audit-01.md); [response-01](topics/padua-proof-attempts-20261101/response-01.md); PR12 dated split: A2 is closed by PD-T156, PD-T157, PD-T158 with supportPD-T159; full A3 remains OPEN. Follow-up constant term and parity independence proved separately in topics/padua-lebesgue-followups-20261103/theory/t4-03-corner-constant.md, with supporting t4-01/t4-02; the -1/N and sharp-remainder obligations remain OPEN. |
```

## PD-T211 — proposed PROOF_STATUS row

Old:

```text
| PD-T211 (PD-T?argmax-alln-codex-04) | Positive compact vertical-edge defect integral, uniform moving-phase limit and compact vertical envelope | PROVED | For each fixed compact interval inside(0,pi), gap>=delta²[1-cos(delta/2)]/(16pi²)+o(1); no effective rate | Retained supporting theorem; center-minimality remains OPEN/excluded | PD-T185, PD-T189, PD-T190, PD-T191; PD-T156/157 corner growth | [record](topics/padua-argmax-alln-20261101/theory/argmax-alln-codex-04-vertical-compact-defect.md) | Written analytic proof; [Claude audit-01](topics/padua-argmax-alln-20261101/audit-01.md) |
```

New (after required audit and final-ID preparation):

```text
| PD-T211 (PD-T?argmax-alln-codex-04) | Positive compact vertical-edge defect integral, uniform moving-phase limit and compact vertical envelope | PROVED | For each fixed compact interval inside(0,pi), gap>=delta²[1-cos(delta/2)]/(16pi²)+o(1); no effective rate | Retained supporting theorem; its excluded center-minimality obligation is proved separately in topics/padua-lebesgue-followups-20261103/theory/t2-01-edge-centre-minima.md; no effective rate added | PD-T185, PD-T189, PD-T190, PD-T191; PD-T156/157 corner growth | [record](topics/padua-argmax-alln-20261101/theory/argmax-alln-codex-04-vertical-compact-defect.md) | Written analytic proof; [Claude audit-01](topics/padua-argmax-alln-20261101/audit-01.md) |
```

## PD-T230 — proposed PROOF_STATUS row

Old:

```text
| PD-T230 (PD-T?argmax-alln-gated-codex-16) | Compact horizontal-edge envelope and positive gap, with exact primitive identity S_n^h(s)=S_n(s,0) | PROVED | Both parities/edges and fixed nondegenerate compact I inside(0,pi); Lambda_c-min_I g_h+o_I(1) | Retained supporting envelope; no center-minimality, effective remainder or endpoint comparison | PD-T212, PD-T216, PD-T217, PD-T157, PD-T185/101 | [record](topics/padua-argmax-alln-20261101/theory/gated-codex-16-horizontal-compact-envelope.md) | Written corrected-mode identification and phase argument; [Claude audit-01](topics/padua-argmax-alln-20261101/audit-01.md) |
```

New (after required audit and final-ID preparation):

```text
| PD-T230 (PD-T?argmax-alln-gated-codex-16) | Compact horizontal-edge envelope and positive gap, with exact primitive identity S_n^h(s)=S_n(s,0) | PROVED | Both parities/edges and fixed nondegenerate compact I inside(0,pi); Lambda_c-min_I g_h+o_I(1) | Retained supporting envelope; center-minimality and limiting endpoint comparison proved separately in follow-ups t2-01/t2-02; effective degree remainder remains excluded | PD-T212, PD-T216, PD-T217, PD-T157, PD-T185/101 | [record](topics/padua-argmax-alln-20261101/theory/gated-codex-16-horizontal-compact-envelope.md) | Written corrected-mode identification and phase argument; [Claude audit-01](topics/padua-argmax-alln-20261101/audit-01.md) |
```

## New records and index links to prepare after audit

- Centre-minima theorem: provisional `PD-T?lebesgue-followups-codex-t2-01`.
- Common endpoint expansion: provisional `PD-T?lebesgue-followups-codex-t2-02`.
- General-position geometric series: provisional `PD-T?lebesgue-followups-codex-t3-01`, currently under final verification.
- Parity-independent defect limit/series: provisional `PD-T?lebesgue-followups-codex-t4-01`.
- One-dimensional explicit remainder: provisional `PD-T?lebesgue-followups-codex-t4-02`.
- Corner constant: provisional `PD-T?lebesgue-followups-codex-t4-03`.

Allocate only from this topic's permanent reservation after a fresh union scan.
Add the topic's reservation link to the batch ledger and ID_CROSSWALK without
rewriting others' reservations. Register all retained/deferred candidate routes
from the gate files, including finite failed searches as measured evidence only.
Reuse LIT-388 for the inspected version/table; no new LIT assignment is needed
for this source. Copy only this topic's final results into its own RESULTS.md
section and append its scoped CURRENT/PAPER_MAP updates at preparation.
