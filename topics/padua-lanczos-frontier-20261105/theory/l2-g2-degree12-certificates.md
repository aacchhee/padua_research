# PD-T?lanczos-frontier-codex-L2-02 — both saved degree12 W/R closure predicates pass on T24 and rotQ24

ID kind: PD-T.
Aliases: G2 finite smooth-rule closure certificates; full-law partial-trace lower.
Split from: the finite G2 obligations in attempts/L2.md.
Split into: none; all-degree targets and original PD-T055 remain separate.

## Statement

In exactly the saved R_smooth normalized aggregate model, with fixed BJ
parents, the following integer lower bounds hold:

| Frozen grid | Lower on C_12^2 | Lower on full-law E_12 |
|---|---:|---:|
| T24, M325 | 17525752205103 | 6457695691 |
| rotQ24, M625 | 6324995264 | 2606606 |

Consequently the unchanged predicates `C_12>=256` and `E_12>=16` are
true on each grid. These are lower certificates, not exact C/E values.
The full90-source domain and the full90*M independent-sign law are
unchanged. Only stage11/source6 is needed for these certificates.

## Definitions and assumptions

Exactly those of the saved W/R definitions in attempts/L2.md and
PD-T?lanczos-frontier-codex-L2-01, in
`l2-smooth-rule-closure-reduction.md`, SHA256
`44498c6230d0a59bbd0cfc4bc96600f0b401eb92ba9302b5c1d54cc569c8d5f9`.
Uniform positive weights, rational frozen points, exact starting vector,
smooth exact-base prior-subtraction rules, positive pivots and normalized
aggregate raw-product sources are essential. No actual IEEE law is used.

The W pulse is source h6=(3,0), stage11, with its Euclidean source/node
direction normalized by sigma_h. The selected nodes are T24 node22,
`(-1,5/6)`, and rotQ24 node1, `(2/15,-27/20)`. The R lower sums ell
over all325/all625 nodes at this same source/stage. Its denominators are
`90*M*||X||²=29250` and110250 respectively, with ||X||²1 and49/25.

## Status by part

Overall status: PROVED, finite computer-assisted. Required later Claude
scientific/protocol audit remains pending.

| Part | Status | Evidence |
|---|---|---|
| Both W predicates | PROVED | Exact pulse closure gains and independently applied two-projector derivatives |
| Both R predicates | PROVED | Exact nonnegative partial trace under the original full-law covariance |

No all-degree claim, full expectation value, spectral/expectation
interchange, finite-u radius or original working-precision PD-T055 result
is part of this theorem.

## Depends on

The complete analytic rule-class/closure reduction L2-01, including the
monic source conversion and both projector terms. The inherited exact
baseline builder is pinned to
`19ce7b774e5a6fa56108eebca3b2ef81f5237328e518d95225adf9f8835e060f`.
All source scales and coordinate expansions are verified exactly.

## Checks

Medium producer `code/g2_screen.py`, SHA256
`2e8c87db119b407a884bc089a5a7e69addfc674b94ebc499236a18307ca1c57d`,
executed separately on both grids, with receipts
`evidence/g2-triangle-screen.json` and `g2-rotated-screen.json`.
It verifies exact full Gram and X expansion, source scales, normal
diagonals and trace, and the formed-X omega sign identity. It directly
projects the winning pulse and matches its exact gain to ell. It tests
the prospective source order6,4,3,5 and stops after source6 passes.

The separately preregistered helper `code/g2_partial_r.py`, SHA256
`8b2b992f1c941fa3f49febe7d5b3e870582e78c8b6ac6189933262ee3932af5a`,
computes the partial lower from all-node exact ell values, with receipts
`evidence/g2-triangle-r-lower.json` and `g2-rotated-r-lower.json`.
It never changes the global denominator or calls this the full E_12.

Distinct independent `code/g2_independent.py`, SHA256
`e88536c7156256de09f907923d7a51437055b685f3ccbaee62fcff4b50589ca8`,
shares only the pinned exact baseline builder, not the producer response
or projector routines. Actual independent executions regenerated both
baselines and all selected-source responses; exact rational gains and
every all-node ell value agree with the developer outputs. Final receipts:

- `evidence/g2-independent-triangle.json`, SHA256
  `6c42af6af8b2e1bba5da5f92918a2d63f8be25b26e9fd2d9ff7fd43f0ce6215c`;
- `evidence/g2-independent-rotated.json`, SHA256
  `ba85d9e9b79c4d61dd96b4141a4675e952f83e57b96077c57f08a7708f5e7d12`.

The fixed compact certificate is `evidence/g2-fixed-certificate.json`,
SHA256 `6bec42971911fb3f86081a13042b6c7029290702c2536c128c0a6f1bf0b746cf`.
The independent checker accepts it from a fresh exact baseline without
opening original developer scratch files or reading original historical
receipt metadata. It rejects five malformed fixed fields per grid and
succeeds after removing nonessential top-level metadata; ignored nested
historical receipt fields remain in that particular removal control.
Its small-grid controls reject omitting either projector derivative or
reversing the next-projector sign. An exact45-source/node, two-stage
small-grid full trace equals43/135 after normalization. These are checks
of the finite reduction, not additional degree12 claims.

Actual commands, versions, elapsed times and artifact identities are in
the receipts, `g2-methods.md` and `independent-checks-l1-l2.md`. This
mathematics worker read the code, fixed certificate, final independent
receipts and relevant report before accepting the finite conclusion;
the executions belong to the distinct technical developer and reviewer.

## Sources

The saved W/R candidates, IDEA253–255, PD-T055/136/137/053 and PD-N062.
No new external source or historical-priority claim.

## Proof or evidence

By L2-01, every R_smooth rule has the same first-order closure map.
For each accepted pulse, the exact squared spectral gain is
`ell_(11,6,i)/||X||²`. The fixed integer lower L_W satisfies
`L_W<=ell/||X||²<L_W+1`; both L_W exceed65536. Therefore
`C_12²>=L_W>=256²`, proving W on each grid.

The exact full-law trace formula is a sum of nonnegative ell terms over
every stage, source and node. Consequently

    E_12 >= sum_i ell_(11,6,i)/(90*M*||X||²).

This is a lower under the full independent-sign covariance; no
one-source law replaces that covariance. The independent computation
checks `L_R<=this partial sum<L_R+1`, with L_R6457695691 and2606606,
each at least16. Hence the original R predicates hold. No uncomputed
cross term is discarded pointwise: cross terms vanish under the full
expectation in L2-01 before its nonnegative trace terms are bounded.

## Scope and open items

This discharges G2 for these saved formal W/R grid predicates. It does
not prove their SH_n all-degree growth statements, which require the
separate positive-weight extension and a new actual closure calculation.
Original literal PD-T055 and deterministic F remain OPEN. Preserve the
old zero-error quantifier warning and the campaign timing deviation for
Claude's later protocol disposition. Bulk arrays remain manifested and
regenerable outside Git; physical archival/delivery is root-owned.

## History

- 2026-11-05: Codex, configured gpt-6.1-sol xhigh. Written after actual
  independent W/R G2 passes on both grids and own reading of their code,
  fixed data and receipts. No threshold, source law or class changed.
  Only after root accepted those passes was further weighted/all-degree
  L2 development authorized. No all-degree proof is claimed in this file.
