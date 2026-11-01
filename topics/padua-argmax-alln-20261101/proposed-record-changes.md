# Proposed shared-record changes — do not apply before audit/PR preparation

These literal blocks preserve handoff02's topic-only write scope. All new result labels remain provisional. Final-ID substitution and a fresh reservation union scan are later PR-preparation work. Required Claude audit PENDING.

## PROOF_STATUS.md — PD-T099 history/addendum

OLD:
```
| PD-T099 (PD-T?programme-ideas-claude-05) | Padua Lebesgue function attains its maximum at a non-node corner (conjecture) | OPEN | no counterexample at 75 tested degrees ≤ 200 (MEASURED); statement OPEN | OPEN target, not rejected; open target A4 | PD-T098 (definitions) | [record](topics/programme-ideas-20261031/theory/programme-ideas-claude-05-padua-corner-argmax.md) | [response-01](topics/programme-ideas-20261031/response-01.md); [Codex audit-01](topics/programme-ideas-20261031/audit-01.md); [Codex audit-02](topics/programme-ideas-20261031/audit-02.md) and [audit-03](topics/programme-ideas-20261031/audit-03.md): accepted at written scope; [integration audit-04](topics/programme-ideas-20261031/audit-04.md); PR12 dated split: Finite n3–7 globals PD-T162, PD-T166, PD-T169, PD-T174, PD-T177 and central-edge splits PD-T185, PD-T186, PD-T187, PD-T188, PD-T189, PD-T190, PD-T191, PD-T192 are PROVED; full-square all-n target remains OPEN. |
```

NEW:
```
| PD-T099 (PD-T?programme-ideas-claude-05) | Padua Lebesgue function attains its maximum at a non-node corner (conjecture) | OPEN | no counterexample at 75 tested degrees ≤ 200 (MEASURED); statement OPEN | OPEN target, not rejected; open target A4 | PD-T098 (definitions) | [record](topics/programme-ideas-20261031/theory/programme-ideas-claude-05-padua-corner-argmax.md) | [response-01](topics/programme-ideas-20261031/response-01.md); [Codex audit-01](topics/programme-ideas-20261031/audit-01.md); [Codex audit-02](topics/programme-ideas-20261031/audit-02.md) and [audit-03](topics/programme-ideas-20261031/audit-03.md): accepted at written scope; [integration audit-04](topics/programme-ideas-20261031/audit-04.md); PR12 dated split: Finite n3–7 globals PD-T162, PD-T166, PD-T169, PD-T174, PD-T177 and central-edge splits PD-T185, PD-T186, PD-T187, PD-T188, PD-T189, PD-T190, PD-T191, PD-T192 are PROVED; full-square all-n target remains OPEN. PR17 proposed additional splits: n2 (PD-T?argmax-alln-codex-02), n8 (codex-07), n9–16 (codex-08), compact vertical gap (codex-04) and horizontal supporting defect (codex-05); see topics/padua-argmax-alln-20261101/report.md. Apply only after accepted audit and final-ID substitution. |
```

## PROOF_STATUS.md — PD-T181 supersession

OLD:
```
| PD-T181 (PD-T?proof-attempts-2-codex-62) | Degree-eight global corner maximum | OPEN | Target retained OPEN; supporting results do not discharge completeness/global obligations | OPEN, not rejected; deadline failures are not passes | Exact dependencies and assumptions in the linked record; accepted earlier results retain their IDs | [record](topics/padua-proof-attempts-2-20261101/theory/proof-attempts-2-codex-62-degree-eight-global-argmax.md) | [Claude audit-01](topics/padua-proof-attempts-2-20261101/audit-01.md); [response-01](topics/padua-proof-attempts-2-20261101/response-01.md) |
```

NEW:
```
| PD-T181 (PD-T?proof-attempts-2-codex-62) | Degree-eight global corner maximum | PROVED | Complete exact/outward Bernstein square cover and distinct-agent replay, PR17 scoped theorem07 | Retained; previous OPEN state superseded by the new proof, with original history preserved | PD-T101, PD-T179 and PD-T?argmax-alln-codex-03; substitute audited final IDs at preparation | [new proof](topics/padua-argmax-alln-20261101/theory/argmax-alln-codex-07-degree-eight-global-argmax.md); [original history](topics/padua-proof-attempts-2-20261101/theory/proof-attempts-2-codex-62-degree-eight-global-argmax.md) | PR17 required Claude audit PENDING: apply this proposal only after acceptance; supplementary checks in topics/padua-argmax-alln-20261101/independent-checks-part3.md |
```

Preserve the old theory statement/history and link its proved split rather than overwrite history. After audit, replace the explicit pending-audit cell with the actual accepted record before applying this row.

## topics/padua-batch-20261031/ALLOCATIONS.md — append unchanged reservation

OLD: empty suffix.

NEW:
```
## Padua argmax all-degree part 3 — reservation import

Owner branch: `claude/padua-argmax-alln-20261101`. First publication:
`405febab68fbe1d998bf894c2d21dfe23d689f96`, PR17, 2026-11-01.
Import unchanged from [topic ledger](../padua-argmax-alln-20261101/ALLOCATIONS.md).
PD-T206–225(count20), PD-N078–083(count6), IDEA-316–335(count20), LIT-460–465(count6).
Unused IDs remain permanent gaps. No re-reservation or accepted-ID renumbering.
Heads checked before original publication: main2b52b432fe59c9a50aef9deebe5152c5d6874465,
topic328be35e55143013047ec03a70e9906e82b95353; all15prior PRs merged.
[Scan](../padua-argmax-alln-20261101/allocation-scan.json). Refresh union before assignment.
```

## ID_CROSSWALK.md — append reservation/split pointer

OLD: empty suffix.

NEW:
```
## Padua argmax all-degree part 3
Reservation: topics/padua-argmax-alln-20261101/ALLOCATIONS.md; first publication405febab68fbe1d998bf894c2d21dfe23d689f96, PR17.
No final IDs assigned at audit handoff. After final-ID assignment preserve mappings for all Claude/Codex provisional claims.
PD-T099 splits into the finite degree2/8/9–16 and compact vertical claims listed in the topic report; full all-degree target stays OPEN.
```

## RESULTS.md — append own topic section

OLD: empty suffix (no section for this topic).

NEW:
```
# padua-argmax-alln-20261101 — part 3 results

Branch: `claude/padua-argmax-alln-20261101`; [draft PR17](https://github.com/aacchhee/padua_research/pull/17).
2026-11-01. Codex gpt-6.1-sol xhigh. Required Claude audit PENDING.
IDs remain provisional; [reservation](../topics/padua-argmax-alln-20261101/ALLOCATIONS.md).

- **PROVED, codex-02:** n2 maximum3, only at(±1,−1); rational proof and independent exact replay.
- **PROVED, codex-03:** tensor Bernstein certificate correctness, strict corner leaves and outward integer arithmetic.
- **PROVED, codex-07/08:** global argmax only at the two non-node corners for n8 and every n9–16. All new certificates independently replayed. With inherited n3–7, the certified finite range is **2≤n≤16**.
- **PROVED, codex-04:** positive compact vertical-edge envelope gap, with continuous positive integral and explicit positive lower bound.
- **PROVED, codex-05:** horizontal decomposition and compact positive defect limit. The P2 envelope remains OPEN.
- **MEASURED, codex-01:** four-edge scans at selected degrees through400 retain the intended noncorner profile; raw interior/corner profile tests fail their planning criteria. Literal localization effectivity projection≈1.33×10^14 is inferred, not rigorous.
- **PROVED, codex-N01:** a precise tie-inclusive finite pairing order fails at n4. This rejects only that formulation; the broader pairing suggestion remains unresolved. The separate geometric screens in codex-06 are MEASURED.
- Claude observations01/02 remain MEASURED; all six prescribed independent replays match exactly.

All record IDs have prefix `PD-T?argmax-alln-`, except N01 with `PD-N?`.
[Report](../topics/padua-argmax-alln-20261101/report.md) links every proof, attempt and independent check.

PD-T099 remains **OPEN**. P0 and a positive-gap compact form of P1 are closed. P2 primitive bounds, P3 corner neighborhoods, P4 interior, P5 strips and P6 effective threshold remain OPEN. The general-β alternating series and center-minimality proof remain unfinished.

Next: Claude Opus5.5 xhigh audit, then dispositions/PR preparation. No final IDs or shared scientific registries changed.
```

At preparation, refresh this block from the topic-owned results file, preserving every other section. Likewise append only this topic's audited rows to IDEAS, PROOF_STATUS and topic/frontier indexes, with dispositions for each retained or failed precise formulation. No scientific registry has changed in this session.
