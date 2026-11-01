# PD-T?argmax-alln-codex-08 — Padua global argmax for degrees nine through sixteen

ID kind: PD-T.
Aliases: P6 finite range; global-maximum-only certificates n=9,…,16.
Split from: PD-T099, its cases 9≤n≤16; the all-degree target remains OPEN.
Split into: none.

## Statement

For every integer n with 9≤n≤16, the even-checkerboard Padua Lebesgue
function of PD-T101 satisfies

\[
\max_{[-1,1]^2}\lambda_n=\Lambda_c(n),
\]

and equality holds only at its two non-node corners: (−1,−1),(1,−1)
for even n and (−1,−1),(−1,1) for odd n.

## Definitions

The nodes are (cos(jπ/n),cos(kπ/(n+1))) with 0≤j≤n,0≤k≤n+1 and
j+k even. The unique total-degree-n cardinals are L_B, and λₙ=Σ|L_B|.
Λ_c(n) is their common value at the two stated non-node corners. Each
certificate records a rational outward enclosure for that value and
the full midpoint prefix partition of the square.

## Assumptions

Exactly the specified checkerboard and corrected kernel of PD-T101.
All mathematical arithmetic is exact Fraction or outward-rounded
192-bit integer interval arithmetic. A failed strict comparison retains
the box; a cap/pending path prevents acceptance.

## Status by part

Overall status: **PROVED** (all eight complete exact covers accepted
by developer and different-agent replays; required Claude audit PENDING).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Stated global argmax for every 9≤n≤16 | PROVED | Eight complete finite covers, all predicates and prefix partitions replayed by both agents |

Disposition: retained IDEA?argmax-alln-claude-05; no novelty claim.

## Depends on

- PD-T101, proof §1: all-n corrected-kernel cardinal formula and
  unisolvence, derived there independently of cited literature.
- PD-T?argmax-alln-codex-03: exact enclosure and finite-certificate
  soundness, including the rational trigonometric constructor and
  equality of the two non-node corner values by node symmetry.

No asymptotic remainder, fitted threshold, monotonicity or local-maxima
count is assumed.

## Checks

Pinned input head: `328be35e55143013047ec03a70e9906e82b95353`.
Frozen source hashes:

| Source | SHA256 |
|---|---|
| finite_bernstein.py | a3133c6c22a365380f6c2ab14f6d31f60153d0df902b325cfcfbeeccc1bed74f |
| finite_general.py | b20b7f88ddfc0bbc92e68096063ef626664028c2a379c34d16dc9f84e17aa74a |
| finite_general_run.py | fe1647086b2db5c47d75e24d386cc6456782bb6ea36bc25acd39b75bd4752511 |
| finite_general_check.py | f9d33648eb05f9539f32c7d8f9003ed61410c7acfff9095bf7ea665989ac8281 |
| finite_n2_exact.py (constructor regression only) | a5f00e6039d6ec76660cac90fb5720e0d6721348ed34c9e62775e1125d3e87c2 |

The PD-T101 dependency file SHA256 is
`ea59aa077a4d021fc69354383f69340f21d17d87d3a28c6ecaaf302cc763612c`.

For each degree N the executed discovery command was:

```
python -B topics/padua-argmax-alln-20261101/code/part3/finite_general_run.py --n N --seconds 100 --output topics/padua-argmax-alln-20261101/outputs/part3/finite_nN_general.json.gz
```

For N=12 the actual output basename is `finite_n12_pilot.json.gz`.
The executed replay command replaces the producer by
`finite_general_check.py CERTIFICATE --output RECEIPT.json`.
Receipts are under `outputs/part3/finite_nN_general_developer_check.json`
(N=12: `finite_n12_developer_check.json`). Independent receipts are
tracked separately and do not overwrite these. All eight developer and
independent commands actually exited0 with accepted=true,
complete_partition=true and all_supplied_bounds_verified=true. The
independent receipts are `finite_nN_independent_check.json`, for each
N=9,…,16. The different Astra agent also read the complete constructor,
proof appendix and PD-T101 dependency, returning no blocking finding.

| n | Developer replay seconds | Independent replay seconds |
|---|---:|---:|
| 9 | 1.424382 | 1.266229 |
| 10 | 2.808632 | 3.484055 |
| 11 | 3.296149 | 5.165296 |
| 12 | 6.050755 | 6.278170 |
| 13 | 6.812330 | 15.432522 |
| 14 | 13.105442 | 22.886572 |
| 15 | 25.101784 | 28.970977 |
| 16 | 48.486231 | 44.681331 |

| n | Visited | Bound leaves | Corner leaves | Max depth | Discovery total seconds | Certificate bytes |
|---|---:|---:|---:|---:|---:|---:|
| 9 | 83 | 40 | 2 | 6 | 1.319723 | 2283 |
| 10 | 95 | 46 | 2 | 7 | 8.940463 | 2416 |
| 11 | 99 | 48 | 2 | 7 | 9.265453 | 2457 |
| 12 | 107 | 52 | 2 | 8 | 5.176281 | 2545 |
| 13 | 111 | 54 | 2 | 8 | 8.042605 | 2594 |
| 14 | 115 | 56 | 2 | 8 | 15.695044 | 2644 |
| 15 | 163 | 80 | 2 | 8 | 23.734180 | 3201 |
| 16 | 191 | 94 | 2 | 8 | 32.347048 | 3498 |

All eight have zero pending/unresolved paths. These are observed wall
times under concurrent CPU load, not isolated benchmarks or a scaling
theorem. Every certificate is far below the one-megabyte artifact limit.

| n | Certificate SHA256 |
|---|---|
| 9 | 5d3a17d91ab5931b88bb5084213d0c0c3f972f8e7e2f0fa09511efe85269f7a8 |
| 10 | 80f98ed868c82116bd1534c6b15b3f49d77c53b69e54bfc12d3ed8658c23a52c |
| 11 | 4d19c769d4ef8713c71feb4109f80a0b4f93643ca65d9e52d70753220e975073 |
| 12 | f44e2897e5b9432720293bf0a9243d6a6bada6a4e33642bc7924a2f65d635a8e |
| 13 | 730a22d7fde68c97b58791a77545bb449cd4249f3e181fd53fc705261b774d41 |
| 14 | 2b9cbed8288910fca1b0519cf8302ba1ecb1c4048976248a32ba6b2a45db48b9 |
| 15 | d528cf2768307a00d4b8751e514df9a6cd069e80a9487d7192dbb632a15c4ca1 |
| 16 | 8e51d6ae34852b34f828cff637b201277e668cf06389b613d64b7ecb1175f5c7 |

The developer's adversarial-control run on the actual n=8 general
certificate rejected 14 deliberate defects and accepted the complete
and genuinely partial positive cases, preserving all frozen source
hashes. It tests the same general checker used for n=9,…,16. A different
agent reran the same 14 controls, including both positive cases, and
accepted them; its receipt is
`../outputs/part3/independent_general_developer_controls.json`.
It also ran its own four-defect mutation harness on n=12, with receipt
`../outputs/part3/independent_general_controls.json`. All frozen source
hashes remained unchanged. The full independent account is in
`../independent-checks-part3.md`; Claude topic audit remains pending.

## Sources

Existing local proof PD-T101; no new literature or priority claim.

## Proof or evidence

For each listed n the exact corrected kernel yields enclosing cardinal
coefficients. Rational Machin and Taylor series enclose its trigonometric
nodes, and every subsequent conversion/subdivision rounds outward.
The complete prefix certificate covers the closed square. On every
bound leaf all coefficient absolute sums are strictly below a certified
lower bound for Λ_c(n). On the two corner leaves this strict inequality
holds at every coefficient other than the exact corner vertex.
The correctness theorem then gives strict inequality outside the two
designated corners; exact node reflection gives their common attained
value. The actual complete developer and different-agent replays
recorded above establish all per-degree finite premises under the
repository's computer-proof workflow. This proves the statement.

## Scope

Only the finite interval 9≤n≤16. No all-degree inference, no exact
count of local maxima, and no claim that n≥17 has been tested. Combined
with the separate n=2,n=8 results and merged n=3,…,7 results, these
cases give the continuous certified range 2≤n≤16. The required Claude
topic audit is pending.

## Open items

Claude topic audit. No further discovery beyond16 is authorized for this bounded
subtask. All-degree PD-T099, and quantitative P3–P6 assembly, remain OPEN.

## History

2026-11-01, Codex developer subagent; requested gpt-6.1-sol xhigh
(runtime model metadata not independently exposed). The orchestrator
authorized continuous extension through16 and then stopped discovery
to reserve time for complete evidence replay and documentation.
