# D1 round 1 prospective protocol

Preregistered 2026-11-12 at input `04ef28b6139ad15b8cfc31f865c7bb9ba0d56d9b`, before D1 mathematical development or computation. Parent publication/go is required before execution. The gate is [gate.md](gate.md).

## Target and assumptions

For normalized product Chebyshev measure on [-1,1]^3, seek constants c>0 and n0 such that every positive cubature exact on Pi_(2n-1), n>=n0, has N>=(1+c)n^3/6. Distinct support points; zero weights omitted. General doubling weights are a separate unproved extension.

## Round 1: exact finite bridge and controls

Write from first principles the polynomial projection identity delta_i=1-w_i K_(n-1)(x_i,x_i)>=0 and sum delta_i=N-dim Pi_(n-1). Unfold every cube rule by coordinate sign reflections to an exact torus rule. State precisely the number of lifted atoms, positive masses, l1 frequency set A_n, Gram projection, torus defects and the nearcritical count squeeze. Check support collisions and boundary stabilizers explicitly. No conclusion from non-tiling alone.

Cheapest decisive tests: reconstruct algebra; use exact rational/cyclotomic arithmetic on a small topic lattice witness and 2-D Padua. If the lift fails exact Fourier moments or critical count, stop that route with its precise gap. Finite verification will be a control only; mathematical identities need written proofs. Planned code `../code/fd1_controls.py`, evidence `../evidence/fd1-controls.json`; deterministic, no random seed. Limit: one small process, <30 seconds intended, no numerical optimization or large matrices. Independent rerun is requested from root after publication of code/input identities.

## Subsequent rounds, each separately preregistered before execution

2. Prove a local compactness lemma: choose high-leverage lifted nodes, establish uniform scaled separation and exponential orthogonality of a local limit. Explicitly track how many nodes are discarded.
3. Prove or identify the gap in critical-density retention and completeness. Tail control, choice of window/translation and passage from finite identities to an infinite basis must have quantifiers. A limiting orthogonal set alone does not close this round.
4. Adversarial reconstruction, mandatory 2-D/sphere/disk consistency, exact source/application check; attempt repairs to the remaining limit obligation. If it remains open after this round, STOP with OPEN target/CONDITIONAL implication and explicit missing lemma. Do not consume rounds 5/6 merely because available.

Rounds 5/6 are ceiling headroom only if the limit step closes by round 4 and a genuinely necessary verification remains. They are not authorized automatically. Total ceiling six; strict stop after four without closure. No 'programme exhausted' claim while a listed step is untried.

## Acceptance/status

Split substantive locally proved lemmas into their own theory homes, preserving the OPEN original target. A complete consequence of checked primary theorems uses exactly **PROVED with explicit LITERATURE dependency** under handoff19; any remaining application premise uses CONDITIONAL. External novelty is bounded by stated source coverage. Evidence records include source/code/input hashes, exact commands, interpreter/library versions and elapsed times; measured checks never become universal proofs.

