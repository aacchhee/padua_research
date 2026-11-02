# Proposed shared-record changes — do not apply before audit/PR preparation

These literal blocks preserve handoff02's topic-only write scope. All new result labels remain provisional. Final-ID substitution and a fresh reservation union scan are later PR-preparation work. Required Claude audit PENDING.

## PROOF_STATUS.md — PD-T099 history/addendum

OLD:
```
| PD-T099 (PD-T?programme-ideas-claude-05) | Padua Lebesgue function attains its maximum at a non-node corner (conjecture) | OPEN | no counterexample at 75 tested degrees ≤ 200 (MEASURED); statement OPEN | OPEN target, not rejected; open target A4 | PD-T098 (definitions) | [record](topics/programme-ideas-20261031/theory/programme-ideas-claude-05-padua-corner-argmax.md) | [response-01](topics/programme-ideas-20261031/response-01.md); [Codex audit-01](topics/programme-ideas-20261031/audit-01.md); [Codex audit-02](topics/programme-ideas-20261031/audit-02.md) and [audit-03](topics/programme-ideas-20261031/audit-03.md): accepted at written scope; [integration audit-04](topics/programme-ideas-20261031/audit-04.md); PR12 dated split: Finite n3–7 globals PD-T162, PD-T166, PD-T169, PD-T174, PD-T177 and central-edge splits PD-T185, PD-T186, PD-T187, PD-T188, PD-T189, PD-T190, PD-T191, PD-T192 are PROVED; full-square all-n target remains OPEN. |
```

NEW:
```
| PD-T099 (PD-T?programme-ideas-claude-05) | Padua Lebesgue function attains its maximum at a non-node corner (conjecture) | OPEN | no counterexample at 75 tested degrees ≤ 200 (MEASURED); statement OPEN | OPEN target, not rejected; open target A4 | PD-T098 (definitions) | [record](topics/programme-ideas-20261031/theory/programme-ideas-claude-05-padua-corner-argmax.md) | [response-01](topics/programme-ideas-20261031/response-01.md); [Codex audit-01](topics/programme-ideas-20261031/audit-01.md); [Codex audit-02](topics/programme-ideas-20261031/audit-02.md) and [audit-03](topics/programme-ideas-20261031/audit-03.md): accepted at written scope; [integration audit-04](topics/programme-ideas-20261031/audit-04.md); PR12 dated split: Finite n3–7 globals PD-T162, PD-T166, PD-T169, PD-T174, PD-T177 and central-edge splits PD-T185, PD-T186, PD-T187, PD-T188, PD-T189, PD-T190, PD-T191, PD-T192 are PROVED; full-square all-n target remains OPEN. PR17 proposed additional splits: finite n2/8/9–16 (codex-02/07/08), compact vertical gap (codex-04), horizontal supporting defect and compact envelope (codex-05 and gated-codex-16), two-phase/localization lemmas (gated-codex-01–13), reflection-first local corner bound (gated-codex-14), eventual exact two-corner global argmax with non-effective threshold (gated-codex-15), finite E-C comparisons (gated-codex-17) and narrowly scoped primitive/E-P obstructions (gated-N01/N02). The unknown finite bridge keeps the original all-degree target OPEN; see topics/padua-argmax-alln-20261101/report.md. Apply only after accepted audit and final-ID substitution. |
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
Additional disjoint PD-T226–245(count20), first publication3aebb299a4154dac822974b7245a9d243f21374e, PR17,2026-11-02; union scan at main2b52b432fe59c9a50aef9deebe5152c5d6874465 and topicfdee6511195632dcf368865edef87b31be40f95c, onlyPR17open and no closed-unmerged PR. Original ranges unchanged.
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
PD-T099 retains its original all-degree wording and OPEN status. Separately register the finite2/8/9–16 and eventual exact argmax theorem, compact edge envelopes, local/phase/finite-defect dependencies and scoped obstructions in the current topic report. Preserve every original-to-split and provisional-to-final mapping. Import additional PD-T226–245 reservation unchanged; first publication3aebb299a4154dac822974b7245a9d243f21374e, PR17.
```

## RESULTS.md — append own topic section

OLD: empty suffix (no section for this topic).

NEW:
```
# padua-argmax-alln-20261101 — current results

Branch: `claude/padua-argmax-alln-20261101`; [draft PR17](https://github.com/aacchhee/padua_research/pull/17).
2026-11-02. Codex gpt-6.1-sol xhigh development; distinct Astra supplementary checks. Required Claude Opus5.5 xhigh audit **PENDING**. All IDs provisional; [permanent reservations](../topics/padua-argmax-alln-20261101/ALLOCATIONS.md).

- **PROVED, gated-codex-15:** for every sufficiently large degree, the global maximizers are exactly the two physical nonnode corners. The existential threshold N_* is non-effective. [Eventual theorem](../topics/padua-argmax-alln-20261101/theory/gated-codex-15-eventual-global-argmax.md).
- **PROVED, codex-02/03/07/08:** complete finite global argmax certification for every2<=n<=16, with exact/outward arithmetic and independent replay. No new degree>=17 global certificate was run.
- **PROVED, gated-codex-01–11:** two-phase primitive bounds, finite pairwise cancellation and uniform actual-corner phase localization. Exact primitive cusp has its own theorem06 and scoped negative N01; it does not refute lambda's corner argmax.
- **PROVED, gated-codex-12/13:** exact row identities and physical corner first variation/aggregate Taylor upper model. Sharper row partial-sum bounds and uniform slope/energy premises remain OPEN.
- **PROVED, gated-codex-14:** reflection-first local bound with237000rho²log(n+1) remainder; strict local descent on physical radius2^-17/n² under coarse sufficient logn>=10^7. [Local theorem](../topics/padua-argmax-alln-20261101/theory/gated-codex-14-reflection-first-corner-bound.md).
- **PROVED, codex-04/05 and gated-codex-16:** positive compact vertical and horizontal edge envelopes; horizontal primitive is exactly S(s,0). Neither center-minimality nor an effective remainder is claimed.
- **PROVED, gated-codex-17:** all ten whole-cell centreward E-C comparisons atn7,12, with20 complete Bernstein leaves and distinct producer/checker replay;17 malformed controls reject. All-n E-C remains OPEN.
- **PROVED, gated-codex-N02:** the stronger common-phase E-P translation fails atn12: lambda(1,cos(9pi/26))-lambda(1,0)>39/1000. E-C and other pairing maps are not refuted.
- Earlier exact tie-inclusive O-Lt obstruction (codex-N01), finite MEASURED T1–T4/pairing screens and six original-Claude-script replays retain their scopes. The T4 projection is inferred, not a rigorous threshold.

All-degree **PD-T099 remains OPEN**. Finite2–16 and eventualn>=N_* do not cover the unknown finite bridge17<=n<N_*. A complete proof needs an effective global threshold with matching coverage, or a direct comparison covering that range. General-beta series and defect center-minimality remain unresolved.

The authorized gated campaign completed sequentially with **6 / 2 / 1 rounds** in directions1 / 2 / 3; unused quota was not spent without a concrete viable next lemma. All failed variants and resumption conditions are retained in [campaign report](../topics/padua-argmax-alln-20261101/gated/REPORT.md), [candidate records](../topics/padua-argmax-alln-20261101/gated/CANDIDATES.md) and [round ledger](../topics/padua-argmax-alln-20261101/gated/ROUND_LEDGER.md).

Next: required Claude audit of part3 plus all gated development, then dispositions and final-ID/PR preparation. No final IDs assigned or shared scientific registries changed. [Topic report](../topics/padua-argmax-alln-20261101/report.md).
```

At preparation, refresh this block from the topic-owned results file, preserving every other section. Likewise append only this topic's audited rows to IDEAS, PROOF_STATUS and topic/frontier indexes, with dispositions for each retained or failed precise formulation. No scientific registry has changed in this session.
