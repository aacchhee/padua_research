# PD-T?programme-ideas-claude-06 — Candidate counts of local maxima of the Padua Lebesgue function, n = 3…8 (MEASURED; not certified)

Final ID: **PD-T100** (allocated 2026-11-01 under AC's authorisation; the provisional ID above and in the text is retained as provenance — see ID_CROSSWALK.md).

ID kind: PD-T.
Aliases: T3 counts; "certified maxima" (withdrawn wording); 15, 27, 25, 41, 50, 62; proposed correction to Białas-Cież–De Marchi–Suder arXiv 2605.23299 Table 3; proposal-1 Paper B data.
Split from: `checks/decisive-gen4-2.md` T3 and Verdict at `614709d` ("complete certification", "settles", "corrects the published table").
Split into: none.

## Statement

For the Padua points Pad_n (as in `PD-T?programme-ideas-claude-04`) and the Lebesgue function λ_n on the closed square, the developer's quadtree search with local certificates found the following local maxima, with zero undecided boxes:

| n | interior | edge (non-corner) | corner | total | arXiv 2605.23299 Table 3 (int / total) |
|---|---|---|---|---|---|
| 3 | 7 | 6 | 2 | 15 | 7 / 15 |
| 4 | 13 | 12 | 2 | 27 | 13 / 27 |
| 5 | 14 | 9 | 2 | 25 | 14 / 25 |
| 6 | 25 | 14 | 2 | 41 | 23 / 39 |
| 7 | 33 | 15 | 2 | 50 | 27 / 42 |
| 8 | 44 | 16 | 2 | 62 | 38 / 56 |

These are **MEASURED candidate counts**. They are *proposed* corrections to the published table at n = 6, 7, 8, pending certification. Each listed point is numerically a strict local maximum (independent check below); the completeness of the list (no maxima missed) and the strictness/uniqueness inside degenerate neighbourhoods are **not** certified.

## Definitions

Local maximum: point of the closed square at which λ_n is a strict local maximum relative to the square. Crease: zero curve of a cardinal function L_B, across which λ_n = Σ|L_B| is not differentiable.

## Assumptions

IEEE double arithmetic in the search; tolerances as recorded in `t3_certify.py`.

## Status by part

Overall status: MEASURED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| listed points are numerical strict local maxima | MEASURED | developer ring tests and valley depths (`t3_validate.py/.out`); independent audit check with a separately constructed product-Chebyshev Vandermonde inverse: all 220 listed points agree in λ to ≤ 7.994e-15 and gradient norm to ≤ 2.881e-14 and pass 64-direction ring tests at radius 1e-5 (`audit-support/proposal-independent.py/.json`) |
| totals reproduced by rerunning the developer certifier | MEASURED | `audit-support/proposal-rerun.py/.json` (same totals; an execution of developer code, not an independent proof) |
| completeness of the list (exact counts) | OPEN | not certified: see Scope |
| smallest recorded certificate margin | MEASURED | 4.34e-7 (pattern constancy, n = 6; `t3_certify.out` row n = 6); earlier summaries said 1.5e-6, which is the n = 8 value |

## Depends on

The existing numerical candidate-count claim retains MEASURED status. Supporting local theorem: PD-T103 (`../../padua-proof-attempts-20261101/theory/proof-attempts-codex-03-degenerate-maxima.md`) proves exact identities, critical-point enclosures and rigorous local Hessian bounds for the two degree-3 exact representatives reconstructed from the recorded `degenerate_max` decisions. It does not prove search completeness or upgrade any count.

## Checks

`checks/code/decisive/gen4-2/t3_certify.py`, `t3_degenerate.py`, `t3_validate.py` with `t3_certify.out/.log`, `t3_maxima.json`, `t3_validate.out` (frozen at `614709d`). Audit replays and counterchecks: `audit-support/proposal-rerun.*`, `proposal-independent.*`, `proposal-degenerate-counterexample.*`.

**Runs needed (certification):** a proved finite reduction of the counting problem; rigorous versions of the (D) corner and (E) edge-node certificates in `t3_degenerate.py`; rigorous root enclosures/exclusions replacing the per-pattern Newton steps over every discarded region; complete sign-pattern box-discard arguments without the early return; exact treatment near regular crease crossings; rigorous arithmetic throughout and an independent checker. The separate `degenerate_max` local obligations have replacement certificates in PD-T103 for the two degree-3 exact representatives, with Z={L_(2,2)}, background critical points at (theta,phi)=(0,acos(±1/sqrt(3))), rational angle enclosures of width 1e-18 and uniform Hessian margin greater than 3.5 on angle l1 discs of radius 0.0021. These discs rigorously contain the recorded radius-0.002 decision neighborhoods. The stored floating iterates themselves are not exact zeros. A fresh trace of every call for n=3,…,8 found two calls at n=3 and none at n=4,…,8; this trace remains MEASURED execution evidence. Obligation (2) is discharged for the `degenerate_max` path only; the (D) corner and (E) edge-node handlers remain explicit certification work. No maxima count is certified.

## Sources

Białas-Cież–De Marchi–Suder, arXiv 2605.23299v1, §3.3 Table 3, Remark 2, §4 (numerical observations and the open counting question; primary excerpt checked by the audit). Białas-Cież–Kenne–Sommariva–Vianello, ETNA 60 (2024) (certified Lebesgue-constant brackets; coverage as recorded in `checks/adversarial-gen4-2.md`). Closest registry entry: charter IDEA-048 ("Geometry of Lebesgue function, ≥ n(n−1)/2 interior maxima", deferred contextual; `state/IDEAS.md`).

## Proof or evidence

Finite computation; the certificate logic has the following gaps, identified by Codex audit-01 A1 and accepted by the developer:
1. `degenerate_max` (lines 187–207) turns small cardinal values/gradients plus a negative background Hessian into "exactly one strict maximum in a small ball"; the local model 2 − x² − y² + ε|x| (two maxima for every ε > 0) passes the same test at ε = 1e-12 (`audit-support/proposal-degenerate-counterexample.py`; not a Padua counterexample). The n = 3 run uses this path twice.
2. `last_resort` returns after the first accepted sign-pattern maximum (line 249) without excluding other surviving patterns in the box.
3. A pattern is discarded when an unconstrained Newton iterate leaves the box (lines 233–234), while the injectivity bound is checked only on the box.
4. Near-coincidence of a critical point with a regular crease crossing (to 1e-10) is treated as exact coincidence (lines 241, 253–257).
Interval arithmetic alone would not repair 1–4; they are logical gaps.

## Scope

The six counts are what this search found. They are not certified, and no correction should be communicated to the authors of arXiv 2605.23299 on the basis of this record. The disagreement with the published table at n = 6, 7, 8 is MEASURED evidence that one of the two lists is incomplete or that the definitions differ; it does not establish which.

## Open items

Precise targets: `../OPEN_TARGETS.md` A5-partial (degenerate identities; the n = 3 cardinal function L_(2,2) = (x − 1)(2x² + x + 2y² − 2)/3 is now exact, `checks/code/response-02/padua_n3_edge_identity.py`) and A5 (the five certification obligations).

Certification (Runs needed above). The code is Padua-specific (`LebDense` uses Padua kernel weights; the degenerate-point handlers use the Padua square/corner/node geometry); extension to other node families is planned, not implemented.

## History

- 2026-11-01, decisive agent (claude-fable-5-1, xhigh): counts produced and described as "complete certification", "settles the factual dispute", "corrects the published table".
- 2026-11-01, Codex audit-01 A1, A9.4: certification not established; margin and generality corrections.
- 2026-11-01, response-01 (claude-opus-5-5, effort not exposed): counts kept as MEASURED candidate counts; certification moved to Runs needed; certification/correction wording struck in the sources (originals kept).

- 2026-11-01, Codex PR #9 finalization (gpt-6.1-sol medium), Claude audit-01 ACCEPTED: PD-T103 supplies supporting exact local replacement certificates for degenerate_max only. Historical completeness/strictness caveats describe the search and remain in force globally; counts remain MEASURED. Corner/edge-node handlers and the other four A5 obligations remain OPEN.
