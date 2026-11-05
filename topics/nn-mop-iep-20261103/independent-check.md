# Supplementary independent mathematical and code check

Date: 2026-11-05 UTC. Agent: Codex supplementary checker. Model and effort:
`gpt-6-astra`, high, as explicitly allocated for this subagent; shell/tool output
does not independently attest the backend identity. This is **not the required
Claude audit**, does not approve PR readiness, and does not change claim status.

## Scope and provenance

Rules/source head supplied by the orchestrator:
`320fe07f5231ac7e72a4da45e64a38e5ff381b4a`, branch
`codex/nn-mop-iep-20261103`. Read `AGENTS.md`, `agents/WORKFLOW.md`,
`agents/codex/CODEX.md`, and `handoffs/01-work.md` before the mathematical check.
No Git operation was performed by this subagent. The claim/code files below
were uncommitted development files; their hashes, not the base commit alone,
identify the reviewed input.

Scope: elementary normal moment systems, their finite-support boundary, the
displayed transfer matrices, and executed finite checks. No new candidate,
novelty clearance, priority claim, full literature comparison, or general
nonexistence assertion is made. For this narrow non-novelty scope the complete
IDEAS registry was not reread; the orchestrator's separate gate must discharge
the topic-wide novelty obligation. In particular, the reference to FHV
Theorem 3.3 and its applicability to a proposed algorithm need the literature
gate and Claude audit; this check verifies the explicitly stated division rule.

Input SHA-256 values, all paths relative to the repository unless noted:

| Input | SHA-256 |
| --- | --- |
| `AGENTS.md` | `c44a76f138fce01f02c06753b22fbc83fd5c1ee701785d49ba17cef5f8eee05b` |
| `agents/WORKFLOW.md` | `423e1bc005d61aaaec38a9d38660f48644618850590c53110b595898a41bde21` |
| `agents/codex/CODEX.md` | `28ca2976171a34860e2bf8d24292af6b92bee34ce22ba1e497891b366533083b` |
| topic `handoffs/01-work.md` | `821ad49a6d568394ab867dd826996998535fc0ebd0bda763c4883e6fbfccc5f7` |
| topic `theory/finite-moment-formulation.md` | `55ef34e0fc3ae426e9828ca6d129dd2eadb8563dd98e775f1cab9f1bfdfa3413` |
| topic `theory/terminal-division-obstruction.md` | `8551df5752505a5bf4b933b2b4bc59bf76a07224cf27120275f95a45552b17e2` |
| topic `code/exact_nn_mop.py` | `64f1100a41f76abfca777ae0096c2a1710f20dc6b434bff7605940deaeb3bc53` |
| topic `exact-runs.md` | `39878e9ee116416f7954ffa89ca7db0e10c78a693859eb46096287ef50da008a` |

## Mathematical assessment and finding

No substantive gap was found in the two elementary proofs under the stated
normality assumptions. The following points were reconstructed independently.

1. A unique monic degree-k solution is equivalent to invertibility of the
   k-by-k coefficient system; a singular consistent linear system cannot have
   a unique solution. Invertibility at the successor rules out vanishing h at
   its predecessor. This justifies every denominator used through degree N-1.
2. For n,m positive, the lowered constraints have rank k-2 by normality at
   (n-1,m-1). Their degree-at-most-k-1 solution space has dimension two. The two
   monic predecessors are independent: equality would give a nonzero
   degree-k-1 polynomial satisfying all conditions at (n,m), contradicting its
   normality. The residual and h-ratio argument therefore determines the same
   lower coefficients in either direction. Axes have a single predecessor;
   degree zero is treated separately and correctly.
3. At degree N the common node polynomial F solves all conditions. A normal
   terminal system uniquely selects F, although distinct terminal moment
   matrices can all be invertible. Both degree-N successors consequently have
   the same subleading coefficient, forcing terminal d=0. For degree N+1,
   F supplies a nonzero kernel vector for every square moment matrix. These
   conclusions are compatible: uniqueness of a fixed monic degree-N problem
   does not imply independence of the degree-N polynomials at different indices.
4. Inside the specified normal square, d=0 would equate the two successors and
   put their lower-degree common polynomial in the kernel at the opposite
   corner. The normality contradiction proves the interior d assertion.
   N=1 is permitted and the independent calculation below checks its boundary.
5. The algebraic relation being tested is the shifted equality
   `L2(nu+e1) L1(nu) = L1(nu+e2) L2(nu)`; it is not the fixed-site equality
   `L2(nu) L1(nu) = L1(nu) L2(nu)`. Equality of their action on one polynomial
   column alone would not prove the matrix identity. Both checkers compare
   every entry of the matrix identity itself. The explicit counterexample
   below disproves identifying these particular fixed-site matrices with a
   commuting pair. It does not exclude different operator encodings, including
   shifted operators on sections, and does not prove a general obstruction to
   nearest-neighbour inverse problems.

**Finding S1 (minor, documentation):** the original `exact-runs.md` says the
two predecessors can be linearly dependent at low-degree sites; the source has
a matching comment near the h ratios. Under the tested normality assumptions
and n,m>0 they are independent, including at (1,1), as point 2 proves. On an
axis only one predecessor exists. Remove that rationale while retaining the
h-ratio formulas. Reported promptly to the orchestrator; the orchestrator
accepted the correction. No developer file was changed by this checker.
Subsequent comment-only revisions need a new hash/impact receipt, not a claim
that the original hash was rerun after revision.

## Independent execution of the development checker

Command actually run from `/workspace/padua_research`:

```sh
python topics/nn-mop-iep-20261103/code/exact_nn_mop.py > /tmp/nn-mop-independent-rerun.json
```

Observed exit status 0; `all_passed: true`. Source SHA-256 was
`64f1100a41f76abfca777ae0096c2a1710f20dc6b434bff7605940deaeb3bc53`.
Environment: Python 3.12.14; Python standard library `fractions.Fraction`.
No randomness or tolerance. Inputs: all 14 deterministic cases specified by
the code and original `exact-runs.md`, both families at N=2,...,8.

Output `/tmp/nn-mop-independent-rerun.json`: 12,801 bytes; SHA-256
`e0fe11743c96bcd188a4d6a421a155421488469dcc317d2c6783e86425c20219`.
This separately executed output happens to be byte-identical to the recorded
developer output; it was generated anew, not copied from that output.

Observed totals: 238 interior and 84 terminal normality checks; 1,316 scalar
orthogonality checks; 476 recurrences; 238 successor differences; 224 transfer
actions; 70 shifted flatness squares; 112 nonzero fixed-site commutators at
x=0; 168 nonterminal nonzero d and 70 terminal zero d values; 84 terminal
products; 476 terminal support evaluations; 168 terminal zero h values;
98 singular degree-N+1 matrices; 14 proportional-weight singular examples.
All agree with the original receipt. These are finite observations, not a
general computer-assisted proof.

## Separate small calculation

New independent source: `code/independent_nn_mop.py`, SHA-256
`69b373434958fd3e8f9df4e579e393d3fb4c209f76c15133cd04bbf04b0a3a5b`.
It imports no development-checker function. It constructs each monic
polynomial with determinants/Cramer's rule, then obtains recurrence
coefficients from polynomial coefficient matching, avoiding the original
elimination routine and h-ratio implementation. SymPy independently performs
the exact arithmetic and polynomial-matrix expansion. This is an independent
implementation check, not algorithmic novelty.

Command actually run from the repository root:

```sh
python topics/nn-mop-iep-20261103/code/independent_nn_mop.py > /tmp/nn-mop-independent-small.json
```

Environment: Python 3.12.14, SymPy 1.14.0. Observed exit status 0 and
`all_passed: true`. Deterministic integer inputs, exact rational outputs:

- N=1: node 7, weights (2) and (5). All 3 indices through degree 1 normal;
  2 recurrences pass; terminal polynomial x-7 and terminal d=0.
- N=4: nodes (-2,0,1,3), weights (1,2,3,5) and (2,3,5,11).
  All 15 indices through degree 4 normal; 20 recurrences pass. Terminal
  determinants, in n=0,...,4 order, are
  `(10692000, -102600, 7920, -20520, 972000)`, all nonzero. Every terminal
  polynomial is `x^4-2*x^3-5*x^2+6*x`. All degree-3 d values vanish; lower
  d values do not. Every degree-5 matrix annihilates the coefficient vector
  of the displayed terminal polynomial and is singular.

At nu=(1,1) for the N=4 input the independently recovered matrices are

```text
L1 = [[x+6622/3097,  -10269/361, 10989/361],
      [1,            0,         0],
      [1,            0,         5379/3002]]
L2 = [[x+13772/6327, -10269/361, 10989/361],
      [1,            20979/11362,0],
      [1,            0,         0]].
```

The shifted product difference is identically the zero polynomial matrix.
The (1,2) entry of `[L1(0),L2(0)]` is
`-7804807927/151762234`, hence nonzero at the very same eligible square.

Output `/tmp/nn-mop-independent-small.json`: 2,271 bytes; SHA-256
`9790542877736255d0b56d3b2285ff0d5334a4f3504587ffc0be6a96dbaee430`.
The two raw JSON outputs remain local and regenerable; no archival upload or
cold-storage retrieval is claimed. This source and short receipt are the
retained artifacts.

## Remaining limits

Response-01 provenance addendum (F4, not a change to the original independent
review): the emitted JSON contains `python` and, in the small checker, `sympy`
version fields. Raw output SHA-256 is environment-dependent. Across
environments compare after removing or normalising those version fields only;
retain code/input hashes and mathematical values. Claude audit-01 R2 obtained
the recorded hash after normalising its Python version. This does not claim
that its raw output bytes were identical before normalisation.

This check supplies no performance/stability benchmark, complete inverse
characterization of coefficient arrays, exhaustive counterexample search,
or literature novelty decision. The small checker adds a SymPy trusted
dependency; the complete rerun uses only the standard library. Neither finite
check replaces the written general proofs. The required Claude Opus 5.5 xhigh
audit remains pending, and later material edits require renewed review.
