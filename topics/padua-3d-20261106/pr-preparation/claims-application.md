# Claim registry application

Rules/input: `c8691c5d4afcbb17506cb052ea48313c865eff35`. Published reservation: `512f63b02ce9b7436092729f53efcc883860a10a`. Authoritative mapping: [final-id-map.json](final-id-map.json).

Appended one topic section to `PROOF_STATUS.md`: 130 rows, 90 PD-T554–PD-T643 and 40 PD-N186–PD-N225. Canonical theory, code, evidence and historical reports are unchanged. Aliases and reciprocal split mapping are applied by the root crosswalk owner; canonical provisional wording remains intact.

Validation performed by the append/check script:

- 130 rows and 130 distinct final IDs; every mapping row applied once.
- No assigned ID already occurs in the pre-existing registry.
- Existing registry prefix is byte-identical: 287497 bytes, SHA-256 `97b44ce90c8215667ecd228408aa7036a041ae91da1994177fbc9787f985c59a`.
- Every new row has all eight schema cells, a canonical theory link and completed-audit scope links.
- No provisional PD identifier remains in the appended rows; explicit available dependencies use mapped final IDs.
- Status counts: {'PROVED': 74, 'PROVED with explicit LITERATURE dependency': 10, 'OPEN': 5, 'MEASURED': 40, 'CONDITIONAL': 1}.
- R08-minima overall keeps the full E4 label; its n1..3 PROVED/n4..16 E4 parts and separate packing-free n4..7 PD-T567 split remain explicit.
- Every OPEN target retains separate proved supports. PD-N failures/refutations retain named-mechanism scope. U2-C1 keeps its current retained hardware-dependent disposition.

No research, theorem change, status upgrade, new computation or Git mutation was performed.
