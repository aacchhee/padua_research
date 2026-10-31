# Lattice-unisolvence campaign plan

Stage AUDIT. Root is the orchestrator/developer; runtime model/effort metadata is not exposed. Assigned mathematical developers use gpt-6.1-sol xhigh, literature gpt-6.1-sol high, adversarial reconstruction gpt-6-astra xhigh. No ultra assignment.

## Authority and pinned starting state

User request is retained at `REQUEST.md`. Original required base eb7bdcdf3a587dd49ea9d692b1d27c7af053fe64. Rules first read at d36722823441dc40c6e19d69a174459348dd309c and re-read unchanged at e949ef06895acd5463cdf8df7e0e5f795218f70f. The latter merges charter audit head 3bd9d4e8e7817eaf0abd5b7a750ea77eb8101342 without rewriting the base. Main observed d367228. Charter audit accepts its mathematics, with protocol findings; this campaign rechecks any used dependency. Never push the base branch.

## Step 0, before exploration

Baseline: ../../literature/lattice-unisolvence/baseline.md. Initially all user-supplied source statements are UNVERIFIED against fulltext; predecessor source checking continues independently. AC explicitly permits exploration after this sourced baseline, before full duplicate screening. Each candidate must have prior-art comparison and independent Astra reconstruction before acceptance. No publication novelty claim is planned.

## Frozen first questions (before launch)

At most C0 and C3 run as substantive directions simultaneously.

- C0: On finite product grids with consecutive index lengths, which single congruence / character fibers or coset unions have exactly binomial(n+d,d) nodes for d=2,3, in an explicitly bounded catalogue, and does a 3D family exist for infinitely many n? First test: exact integer counts, then density/periodic-polynomial reasoning. Freeze enumeration bounds in C0 before execution; catalogue completeness is only within those bounds.
- C3: For every cardinality-admissible C0 pattern in the frozen small catalogue, what is the exact rank for total degree n<=6 at seeded distinct random axes over multiple primes? First test is rank, before Lebesgue calculations. A finite failure stays MEASURED unless a written annihilating polynomial proves a scoped obstruction. An explicit exact nonzero determinant is a proof only for that specialization; generic statements remain MEASURED absent a symbolic identity or written probabilistic reduction.

C1 (2D higher characters), C2 (known 2D comparisons), C4 (consequences) are queued, not concurrent substantive directions. Literature C2 comparisons may proceed as baseline work. Activate a new mathematical direction only after closing one of C0/C3. Preserve deferred and failed candidates.

## Round policy

Up to ten conceptual rounds per direction, extension to twenty only with written reason. Automatically continue concrete surviving openings. Record every question, test, correction, outcome and continuation/stop reason in the direction folder and round ledger. No arbitrary time stop of a live proof opening.

## Round ledger

| Direction / round | Frozen question / command scope | Outcome | Next |
|---|---|---|---|
| C0 / rounds1–2 | bounded count catalogue; density/infinite-family count | CLOSED:5061trials,451count survivors, direct proofs | retained rows and C3 handoff |
| C3 / rounds1–5 | exact rank; covers/projections; axis rectangles; Lobatto; isolated n2 | CLOSED:142survivor reps,213certificates, isolated axis factorization; broad target OPEN | Claude audit / precise future structural step |
| C1 / rounds1–12 | adjacent mod4phases; row/Gram reductions; stability; all-degree phase completion | CLOSED at justified extended budget; universal contraction/log² OPEN | Claude audit / prove strictness or kernel bound |

## Evidence and completion

Exact checkers and small essential outputs may be committed within repository limits. Large output and third-party fulltext stay outside Git. AC cold destination: C:\\Users\\andreyac\\Downloads\\padua\\cold_storage\\lattice-unisolvence-20261031\\; cloud staging is temporary and Windows receipt remains pending until verified. Each preserved pattern reports (a) periodicity, (b) axis factorization/structural criterion, (c) Lebesgue growth, even when unknown. Prepare report, theory, audit handoff, shared batch reconciliation and draft PR targeting charter branch; only AC merges, after charter PR #2. Final Stage AUDIT, Next Claude (Opus 5.5 xhigh).

## Ownership

- literature agent (Sol high): literature/lattice-unisolvence/ and topic literature-summary.md.
- counting agent (Sol xhigh): direction C0, code/c0_*.py and theory/c0-*.md.
- rank3d agent (Sol xhigh): direction C3, code/c3_*.py and theory/c3-*.md.
- root: Git, shared ledger/registries, topic plan/log/progress/report/handoff, integration and verification.
- separate Astra xhigh reconstruction: assigned disjoint independent/ folder after mathematical checkpoint; no developer acceptance before that check.

## C0 closure and C1 activation

C0 closed after two conceptual rounds: finite catalogue + elementary density/infinite-six count and short-axis obstruction complete in its declared scope. No unresolved counting proof opening remains there; all omitted classes retained deferred. C3 structural/stability work continues. C1 is activated as the second substantive direction, with question frozen in directions/C1/launch.md before any run; developer ownership transfers from C0 to C1. Literature baseline and candidate-specific predecessor screen are already recorded. At no point are C0,C1,C3 substantively active together.

## Scientific continuation checkpoints

C3 closes its five-round route after exact layer/projection certificates, rectangle nonseparability tests, Lobatto sampling and a direct isolated n2 axis-factorization proof. Its naive fixed-coefficient continuation is already deficient or count-invalid at the next tested degrees, and the broad target remains OPEN. C1's initial symmetry obstruction is not used to erase its stable odd-degree or shifted-phase subsequences; those openings automatically continue through bounded higher-degree tests and analytic reductions, up to the ten-round budget. Every extension is frozen in the direction records before execution.

## Justified C1 extension, frozen before execution

After ten actual C1 rounds, a concrete omitted counting opening remains: phase1 (`i+j mod4 in{1,2}`) may fill the n≡0mod4 degrees excluded by the original phase0 count. The complete4-block/remainder count at n4 and the antipodal complement test are cheap decisive checks. Root therefore authorizes a justified extension to **at most12 C1 rounds**, within AC's maximum20: round11 count/symmetry and finite Chebyshev tests for this missing subsequence; round12 consolidate a single all-degree phase schedule if valid and identify its exact remaining proof obligation. This does not authorize new blind searches or a polylog claim. If the resulting target still needs the same unresolved contraction/inverse inequality and no new proof route is found, stop with that target OPEN rather than extending for more samples.
