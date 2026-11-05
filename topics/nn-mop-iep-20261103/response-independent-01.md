# Supplementary independent check of response-01

Date: 2026-11-05 UTC. Checker: Codex supplementary agent, requested allocation
`gpt-6-astra`, high. Tool output does not independently attest backend model
or effort. This supplements, and does not replace, the required Claude
re-audit. No Git operation or developer-file edit was performed by this worker.

## Scope and provenance

Rules/input head supplied by the orchestrator:
`9ec2a54c5b6af56514feaf11c9fc329f19a88820`, branch
`codex/nn-mop-iep-20261103`. Read AGENTS.md, agents/WORKFLOW.md,
agents/codex/CODEX.md, handoff03 and audit-01. The response files were
uncommitted; hashes below identify the actual mathematical and code inputs.

Scope: reconstruct the complete F1 proofs; inspect and separately rerun the
C4 pilot; check its input convention, precision and metric; inspect F2 and
F4 wording. No new mechanism, novelty/priority claim, full novelty clearance,
or expanded impossibility claim is proposed. Under WORKFLOW's explicit
non-novelty audit exception, the full IDEAS registry was not reread. This
check does not reopen the accepted finite formulation or original counts.

| Reviewed input, relative to this topic unless stated | SHA-256 |
|---|---|
| `theory/interior-divisor-nonvanishing.md` | `1907b124c354d90acb9ed10bc94e4a0eb8410db380ad83d34c3502f8f2d51960` |
| `theory/marginal-reconstruction.md` | `27384beb097b9b6df5ff7240c4c7dd6bb371e8de375be0961b2e9fb5bbe50c24` |
| `source-recheck-01.md` | `c653c0af0484ca69ae1b792545a8ffe9536efb934acc2fefe4c05fa4f6e71c82` |
| `code/c4_float_baseline.py` | `9ce76ae88fb798f73127f75819bcdfb6c7bffb0d9cd092d70957164cb9b6a2e8` |
| `audit-01/claude_layer_recursion_check.py` | `13d59af82304a712d792c6e2f96c76f42ec732575dcfa3452a92295071c011b3` |
| `c4-baseline-01.md` | `e751f17a04abb07f11ce9206909ade8b80691ce5b85dd5abe56982b19fd34bf7` |
| `theory/c4-baseline-measurements.md` | `6cc2fb295b9dfbbf8e742afb55dec15d5790da7042ec7b669249b53cf44248a6` |
| `theory/fixed-site-dictionary-failure.md` | `d30194d11302864e5bfb8bafadee6b3f94cc133e70493912feff66f419e49b55` |
| `report.md` (F2 paragraphs inspected) | `a9e81050d48faf6817a04b3cf197cfdcb7761d4068c008f9e064d8a442856fd5` |
| `candidates.md` (C2 inspected) | `68da9746662a4ce20d204cf6904a257bf4a8a94c1353b8dbcf228c225a613b34` |
| `exact-runs.md` (F4 addendum) | `2fb02ca153f342654f4be7f731642a81e53eb399de34f10812f2aff984ffaccb` |
| `independent-check.md` (F4 addendum) | `f65cbbfdd5b7b479fe45a3bfe13e4052239660f6fdcf5e399a92a1f22eaabdf2` |

Rule-file SHA-256 values: AGENTS.md
`c44a76f138fce01f02c06753b22fbc83fd5c1ee701785d49ba17cef5f8eee05b`;
agents/WORKFLOW.md
`423e1bc005d61aaaec38a9d38660f48644618850590c53110b595898a41bde21`;
agents/codex/CODEX.md
`28ca2976171a34860e2bf8d24292af6b92bee34ce22ba1e497891b366533083b`.

The two baseline prose hashes include the parent's subsequent clarification
that no cold-storage transfer was performed. I inspected that clarification;
it does not change the code, measurements or interpretation reviewed here.

## F1: independent reconstruction

No substantive mathematical defect was found in the two full written proofs.
The conclusions below follow from reconstructing the algebra, not from
accepting Claude's checker output or the developer's source descriptions.

1. At degree s, the s orthogonality rows have rank s on polynomials of
   degree at most s because their first s columns form M_nu. Their kernel
   is one-dimensional and contains P_nu. Subtracting the monic successors
   therefore gives a multiple of P_nu; comparison of degree-s coefficients
   gives exactly d=b2-b1 with the displayed sign. If d=0, their common
   monic degree-(s+1) polynomial satisfies the union of the two successor
   conditions, all s+2 conditions at the opposite corner. Its coefficient
   vector contradicts invertibility there. This argument includes axis
   squares and s=0; for N=1 the asserted interior set is empty.
2. Expanding x(P_(nu+e1)-P_(nu+e2)) along directions 2 and 1 cancels
   the common opposite-corner polynomial. The two predecessor-difference
   substitutions give the positive lower terms in (E) and the coefficient
   d*b_(nu+e2,1)+S_(nu+e1)-S_(nu+e2) on P_nu. Expansion of d*xP_nu
   gives (F), so (A), (B1) and (B2) have the stated signs and indices.
3. The coefficient comparison uses an actually independent polynomial
   family. Its degrees are s+1, s and s-1. At mixed sites the two monic
   degree-(s-1) predecessors cannot be proportional unless equal; equality
   would satisfy the union of their conditions at nu and contradict
   normality. Thus both lower coefficients may be compared separately.
   On axes there is one predecessor; at the origin there is none. The
   written argument never infers matrix equality merely from action on a
   single polynomial vector.
4. For target layer t, mixed a's divide at degree t-2 and use numerators
   from degree t-1. Unknown b's divide at degree t-1 after every a on
   layer t is known. Each b1 with positive second index and each b2 with
   positive first index is assigned exactly once; the remaining b's and
   axis a's are marginal data. Hence there is no circular dependency.
   All recurrence bases have degree at most N-1 and opposite corners at
   most N. The largest divisor degree is N-2. Terminal d is not used
   even as a numerator. N=1 requires only the initial marginal entries,
   no division; N=2 uses only d_(0,0) for the new b's.
5. Genuine coefficients satisfy the identities and initial data, so the
   induction proves both correctness and determination by the marginals.
   It is not a converse assertion about arbitrary proposed Jacobi arrays.
   The common support polynomial solves each degree-N problem and
   normality selects it uniquely; terminal equality follows, including
   N=1. Rank through N support evaluations excludes normal degree N+1.

The withdrawal of the former active PD-N failure classification is
consistent with this reconstruction: the only proposed terminal division
would produce coefficients outside the domain. The separate substantive
interior lemma is a justified positive dependency. The terminal equality is
necessary and is not asserted to characterize all realizable arrays.

I read the full source-recheck note and its limited perfect-rectangle
comparison. The local rank argument for the common-support (N,N) matrix is
correct. I did not independently reopen the FHV, Van Assche or
Kozhan–Vaktnäs PDFs in this supplementary check: their primary locator
verification remains the mathematical developer's separately recorded
work, to be considered in Claude re-audit. No external theorem is needed
for the full local proof checked above.

## C4 implementation, source inputs and metric

I inspected the full executable and the exact mixed-moment checker it
imports. The recurrence uses node-valued monic Stieltjes marginals and the
same A/B formulas just reconstructed. Its floating branch uses Python floats
throughout arithmetic; calls to mpmath finite predicates do not increase
that arithmetic precision. Fractions define nodes and weights before their
separate conversion to float or mpf. The corrected Hahn empty product is a
Fraction, so factorial division does not inject an early binary64 value.

After inspecting the relevant literature/INDEX.md entries (including
LIT-347/348 and LIT-118), I independently opened the versioned primary
[arXiv:2608.25758v1 PDF](https://arxiv.org/pdf/2608.25758v1) using the
web service and checked printed p.20, Examples 5.1–5.2. Its N-node
convention and both parameter choices agree with the code and receipt.
The binomial weights use p1=0.4,p2=0.5; Hahn uses beta1=1,beta2=1.5,
gamma=1. The paper also notes these weight vectors change with N. This
verifies the pilot's source-family input claim, not the paper's algorithms
or numerical conclusions. No primary text was committed.

The affine coordinate z=2k/(N-1)-1 is used for both calculations; the
stated transformation a_z=(2/(N-1))^2*a_k and
b_z=2*b_k/(N-1)-1 is correct for monic recurrences. The executable's
metric is a maximum of four fieldwise relative sup norms, not a maximum
of componentwise relative errors. Structural zeros still contribute to
the numerator. Error subtraction, division and logarithms are evaluated
inside the enclosing 220-digit context, so this computation does not round
the reference to binary64 before comparing it. Epsilon is 2^-52 and is
correctly distinguished from unit roundoff. Negative reported correct
digits mean E>1; a completed finite run is not labelled accurate merely
because it avoided breakdown.

The 140/220-digit agreement is a convergence check using the same algorithm.
It alone cannot detect a shared algebraic bug or certify exact normality.
The N=4 checks instead solve the exact Fraction moment systems and match
polynomial coefficients, independently of the layer formulas. I inspected
that code's full-rank solves, exact residual assertions and equality of
the two directions' lower coefficients. Its use of exact normal equations
for coefficient matching does not incur floating conditioning error.
The receipt correctly states that this independent formulation covers only
the two N=4 inputs, not every larger reference case.

## Separate executions

Commands actually run from `/workspace/padua_research`, independently of
the developer's prior executions; both returned exit status 0:

```sh
python topics/nn-mop-iep-20261103/code/c4_float_baseline.py --family krawtchouk --sizes 4 8 12 16 24 32 --dps 140 220 > /tmp/nn-mop-response-check-krawtchouk.json
python topics/nn-mop-iep-20261103/code/c4_float_baseline.py --family hahn --sizes 4 8 12 16 24 32 --dps 140 220 > /tmp/nn-mop-response-check-hahn.json
```

Environment: Python 3.12.14 (Clang 22.1.3), mpmath 1.3.0,
Linux-6.18.57-x86_64-with-glibc2.41. Deterministic exact rational inputs;
no seed. The frozen executable and imported checker hashes are above;
each output records the exact rational-input hashes independently.

| Own local output | Bytes | SHA-256 |
|---|---:|---|
| `/tmp/nn-mop-response-check-krawtchouk.json` | 7064 | `53e6bc0e2de069bb3be0b4427aee78f63d9a3b880c4f7a6777ca659002bae834` |
| `/tmp/nn-mop-response-check-hahn.json` | 7094 | `fe8f91b3e29162f44891a05e2a393d627cb9cbe3586787f1eb4cc628e8e565e7` |

An actually executed Python JSON comparison found every complete `cases`
object equal to the corresponding developer final output, including input
identity, errors, digits, precision agreement, division diagnostics and
N=4 exact-check results. These are newly executed outputs, not copies.
Their raw hashes differ because elapsed times differ.

| N | Krawtchouk E | Hahn E | Maximum divisor degree |
|---:|---:|---:|---:|
| 4 | 1.0090076922134965e-13 | 1.3412313841971528e-12 | 2 |
| 8 | 1.8705702304571456e-9 | 2.614295169950109e-7 | 6 |
| 12 | 1.6124888672742654e-6 | 0.0024598366717086153 | 10 |
| 16 | 0.09666944831233441 | 70.31384815587052 | 14 |
| 24 | 72940.5982327841 | 310.52010170669297 | 22 |
| 32 | 5022.381465152575 | 677581.5807967706 | 30 |

All twelve cases completed and passed the 1e-60 reference-agreement
threshold. The worst reference disagreement was Hahn N32,
1.4113226016560325e-99. Both N4 exact checks passed. The observed large
errors and nonmonotonicity match the receipt. They establish only bounded
MEASURED behavior of this implementation; they do not isolate error
sources, compare C3, or prove general instability. Raw files remain local
and regenerable; no archival transfer is claimed by this checker.

## F2, F4 and disposition

The revised report, C2 and fixed-site record correctly state that Xu's
block conditions can couple neighboring degree levels. Same-site transfer
noncommutation refutes the literal dictionary only. Direct substitution
of the NN recurrence gives H1 P(x)=H2 P(x)=xP(x); both share one spectral
parameter. The comparison to two coordinate multiplications is correctly
qualified and does not assert impossibility of every alternate encoding.
No additional full-lattice experiment was executed here.

For F4, inspected output construction confirms that the old exact checker
emits `python`, and the independent small checker emits `python` and
`sympy`. Their added warnings correctly distinguish raw hashes from
payload comparison with those fields normalized. I did not rerun the
older checkers or independently repeat Claude's historical normalized-hash
calculation in this response. The C4 receipt separately identifies its
additional variable timing/platform/argv fields.

**Result:** no unresolved finding within this declared supplementary
scope. Required Claude re-audit remains pending. Parent integration,
later prose changes and final commit/PR state are outside this file's
approval; material mathematical or code changes require renewed review.
