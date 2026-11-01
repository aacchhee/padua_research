# PD-T?argmax-alln-codex-07 — Degree-eight Padua global maximum

ID kind: PD-T.
Aliases: n=8 global-max-only Bernstein certificate; P6 finite range.
Split from: PD-T099 / PD-T181, the still-open all-degree target and its degree-eight case.
Split into: none.

## Statement

For the even-checkerboard degree-eight Padua nodes of PD-T101,

\[
\max_{[-1,1]^2}\lambda_8=C,\qquad
\{(x,y):\lambda_8(x,y)=C\}=\{(-1,-1),(1,-1)\},
\]

where C is the exact non-node corner value of PD-T101. This statement
does not determine the number of local maxima.

## Definitions

Nodes (cos(jπ/8),cos(kπ/9)), 0≤j≤8,0≤k≤9,j+k even; the 45 unique
total-degree-eight cardinals L_B; λ₈=Σ_B|L_B|. The corner value C has
the following coordinates in the PD-T179 tensor basis
(1,b,b²,a,ab,ab²,a²,a²b,a²b²,a³,a³b,a³b²), where a=2cos(π/8),
b=2cos(π/9):

```
(7/9, -2/9, 4/9, -2, -5/9, 7/9, 4/9, 2/9, 0, 2/3, 2/9, -2/9).
```

## Assumptions

Exact algebraic cardinals and physical real embedding of PD-T179;
outward integer arithmetic at 160 bits. All predicates must replay;
the discovery summary alone is not accepted as proof.

## Status by part

Overall status: **PROVED** (written finite reduction, exact complete
certificate, developer and different-agent replay passed; required
Claude topic audit PENDING).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Stated degree-eight global argmax | PROVED | Complete 34-leaf cover, exact field reconstruction and both full replays passed |

Disposition: retained IDEA?argmax-alln-claude-05.

## Depends on

- PD-T179: exact degree-eight field/principal embedding and checked
  cardinals from the corrected kernel, with all 2025 nodal identities.
- PD-T?argmax-alln-codex-03: finite Bernstein certificate soundness.
- PD-T101: node convention and exact corner formula (the field run
  also computes its corner value directly from exact cardinals).

## Checks

Pinned input head: `328be35e55143013047ec03a70e9906e82b95353`.
The read-only field source SHA256 is
`764a7d7e50718c04f076ab3bbc86270adad1c47bc902d0b8d4eecf32ebbd2ec2`.
Frozen new sources:

| Source | SHA256 |
|---|---|
| finite_bernstein.py | a3133c6c22a365380f6c2ab14f6d31f60153d0df902b325cfcfbeeccc1bed74f |
| finite_bernstein_run.py | d03b0830b4e23261ee82ea5265b3f5123956a083b34418e6124ea9e4bbb352ac |
| finite_bernstein_check.py | 096e60475252ebeff871efd3b87eab8029fef0971c0f3b94bfd1ad83a71f6fa1 |

Executed from the repository root:

```
python -B topics/padua-argmax-alln-20261101/code/part3/finite_bernstein_run.py --seconds 75 --boxes 200000 --depth 48 --output topics/padua-argmax-alln-20261101/outputs/part3/finite_n8_pilot.json.gz
python -B topics/padua-argmax-alln-20261101/code/part3/finite_bernstein_check.py topics/padua-argmax-alln-20261101/outputs/part3/finite_n8_pilot.json.gz --output topics/padua-argmax-alln-20261101/outputs/part3/finite_n8_developer_check.json
```

Discovery: exit0, 67 visited / 33 splits, 32 bound leaves plus two
corner leaves, maximum depth6, zero pending. Setup47.970103s,
search0.364814s, total48.334941s. Complete certificate1397bytes,
SHA256 `92528fc9575407cfbb6c097a814327ebc8666a15fe736bc387044f6f6ff54f22`.
Developer replay: accepted=true, complete_partition=true, every bound
verified in41.207146s. A different Astra subagent actually replayed the
same raw certificate and accepted every bound and the complete partition
in45.721947s; receipt `../outputs/part3/finite_n8_independent_check.json`.
Its separate controls rejected five defects (missing leaf, wrong corner,
altered threshold, duplicate leaf and producer self-approval), while
accepting the authentic complete certificate. Receipt:
`../outputs/part3/independent_n8_controls.json`. All frozen source hashes
remained unchanged. The written mathematical/code review is in
`../independent-checks-part3.md`; it supplements the required Claude audit.

## Sources

No literature claim. Existing local exact-cardinal dependencies above.

## Proof or evidence

The certificate stores all 34 leaf paths and their verified predicates,
which form a complete binary midpoint partition of the closed square.
On 32 leaves, the sum of absolute cardinal Bernstein coefficients is
strictly below an outward lower bound for C at every coefficient.
On the two corner leaves, this strict bound holds at every coefficient
except its designated tensor vertex; that vertex is exactly the corner
value by definition. The exact field calculation proves both corner
values equal C. The finite correctness theorem then implies the stated
maximum and strict equality characterization. Both required full replay
receipts are recorded above. The artifact is a full-square upper
bound certificate; no enumeration of all local maxima is assumed.

## Scope

n=8 global maximum only. PD-T180/184 exact-count obligations stay OPEN.
The original all-degree PD-T099 target stays OPEN.

## Open items

Claude topic audit. All-degree PD-T099 and n=8 local-maxima counts remain
OPEN; this finite global-maximum result is substantive and remains split.

## History

2026-11-01, Codex gpt-6.1-sol xhigh: discovered and developer-replayed
the finite cover. Authorized after the T1–T5 first-pass outcomes;
the final T1 high-degree extension completed while this finite work ran.
