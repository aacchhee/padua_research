# Exact defining-system sanity checks

Status: **MEASURED**. These are finite, exact-arithmetic sanity checks of the
defining moment systems and standard nearest-neighbour recurrences. They are
neither a general proof nor a performance/stability comparison or a new method.
The orchestrator handles the topic's novelty gate; this code generates no new
mechanism. Independent rerun and external audit are separate obligations.

## Completed developer run

- Date: 2026-11-05 (UTC).
- Source/rule commit read before work:
  `320fe07f5231ac7e72a4da45e64a38e5ff381b4a`.
- Code: `code/exact_nn_mop.py`, newly developed from that source tree.
- Code SHA-256:
  `64f1100a41f76abfca777ae0096c2a1710f20dc6b434bff7605940deaeb3bc53`.
- Command, from repository root:
  `python topics/nn-mop-iep-20261103/code/exact_nn_mop.py > /tmp/nn-mop-exact-developer.json`
- Observed exit status: 0; JSON reports `all_passed: true`.
- Output: `/tmp/nn-mop-exact-developer.json`, 12,801 bytes; SHA-256
  `e0fe11743c96bcd188a4d6a421a155421488469dcc317d2c6783e86425c20219`.
  This local regenerable output is not committed. This receipt and the checker
  suffice to regenerate it; no cold-storage location is claimed.
- Environment: Python `3.12.14 (main, Aug 25 2026, 14:00:49)
  [Clang 22.1.3]`; exact `fractions.Fraction` arithmetic and other Python standard
  library modules only. No SymPy dependency. No random seed: inputs deterministic.
- Agent: Codex developer subagent. The runtime does not expose an independently
  verifiable model/effort identifier in its tool outputs; no such metadata is
  inferred from a requested allocation.

A same-developer CLI subset check also ran successfully (exit 0):
`python topics/nn-mop-iep-20261103/code/exact_nn_mop.py --min-n 8 --max-n 8 > /tmp/nn-mop-exact-n8.json`.
It rechecks only the two N=8 cases and is not independent evidence. Output size:
2,553 bytes; SHA-256:
`ca6cb7b01bf0c90cb206e72dbace86e8091f5455f07dfd7b0b100a1628d82b3e`.

## Inputs and exact equations

For each integer N=2,...,8, both families use N distinct rational common nodes
and two strictly positive rational weight vectors. Index k ranges from 0 to N-1.

1. Generic deterministic test: `x_k=(k^2+k+1)/(k+2)`,
   `w1_k=(2/3)^k`, `w2_k=(3/5)^k`.
2. Binomial/Krawtchouk-type test: `x_k=k`,
   `w1_k=binom(N-1,k)(1/3)^k(2/3)^(N-1-k)`,
   `w2_k=binom(N-1,k)(2/3)^k(1/3)^(N-1-k)`.

JSON records an input SHA-256 for every case: SHA-256 of the UTF-8 bytes of
`json.dumps({'nodes': list(map(str,nodes)), 'weights':
[list(map(str,ws)) for ws in weights]}, sort_keys=True)`.
The formulas and code hash freeze all inputs without external files.

Write `mu_j(s)=sum_k wj_k x_k^s`, with j=1,2. For alpha=(n,m),
D=n+m, assemble the D-by-D matrix whose rows are
`(mu_j(k+i))_(i=0,...,D-1)`, for `(j,k)=(1,0),...,(1,n-1),
(2,0),...,(2,m-1)`. Exact Gaussian elimination computes its determinant and solves
the right-hand side `-mu_j(k+D)` for the lower coefficients of the monic P_alpha.
The empty determinant at (0,0) equals 1. The code separately checks every defining
orthogonality equation, rather than relying solely on the solve.

For D<=N-1, let `h1(n,m)=sum w1_k x_k^n P_nm(x_k)` and
`h2(n,m)=sum w2_k x_k^m P_nm(x_k)`. The code uses

```
a(n,m) = h1(n,m)/h1(n-1,m) if n>0, else 0
c(n,m) = h2(n,m)/h2(n,m-1) if m>0, else 0
b_j(n,m) = [x^(D-1)]P_nm - [x^D]P_(alpha+e_j)
```

The first subleading coefficient of P_00 is defined as zero. These ratios fix a
and c in the canonical moment convention. Under normality at an interior
index, the two predecessor polynomials are independent, including (1,1);
there is only one predecessor on an axis. All divisions are exact, with a nonzero denominator
required by successful execution. Missing predecessor terms are omitted on axes.
Both full polynomial identities are checked coefficient by coefficient:

```
x P_alpha = P_(alpha+e_j) + b_j P_alpha
            + a P_(alpha-e1) + c P_(alpha-e2), j=1,2.
P_(alpha+e1)-P_(alpha+e2) = d(alpha) P_alpha, d=b2-b1.
```

## Transfer compatibility and the fixed-site distinction

For n,m>=1, use the polynomial column
`Y_alpha=(P_alpha,P_(alpha-e1),P_(alpha-e2))^T`. The two transfer matrices are

```
L1(alpha;x) = [[x-b1, -a, -c],
               [1,     0,  0],
               [1,     0,  d(alpha-e2)]]
L2(alpha;x) = [[x-b2, -a, -c],
               [1, -d(alpha-e1), 0],
               [1,     0,  0]].
```

All entries a,c,b1,b2 in the first rows are at alpha. The checker verifies
`Y_(alpha+e_j)=Lj(alpha;x)Y_alpha` as polynomial identities wherever D<=N-1.
It then multiplies polynomial matrices and checks all nine entries of

```
L2(alpha+e1;x) L1(alpha;x) = L1(alpha+e2;x) L2(alpha;x)
```

for n,m>=1 and D<=N-2. These restrictions ensure all required successors have
degree <=N. Axis sites are excluded because this three-component state includes
an absent predecessor; N=2,3 have no such squares.

The fixed-site commutator `[L1(alpha;0),L2(alpha;0)]` is also computed. It is
nonzero at all 112 tested interior sites, despite shifted compatibility at all
70 eligible squares. For example, generic N=3, n=m=1 gives entry (1,2)
`34034175/3251718184`. This is a counterexample to equating this particular
fixed-site pair's commutation with its shifted flatness; it does not address all
possible alternative encodings.

## Observed counts and boundaries

Counts include both families and all seven N values.

| Check | Passed checks |
| --- | ---: |
| Nonzero moment determinant, n+m<=N-1 | 238 |
| Nonzero moment determinant, n+m=N | 84 |
| Defining scalar orthogonality equations, n+m<=N | 1,316 |
| Nearest-neighbour polynomial recurrence, both directions | 476 |
| Successor-difference polynomial identity | 238 |
| Three-component transfer action, both directions | 224 |
| Shifted polynomial-matrix flatness squares | 70 |
| Fixed-site commutator nonzero at x=0 | 112 |
| d!=0 at n+m<=N-2 | 168 |
| d=0 at n+m=N-1 | 70 |
| Degree-N polynomial equals common node product | 84 |
| Degree-N polynomial vanishes at an individual support node | 476 |
| h1 or h2 vanishes at terminal degree N | 168 |
| Singular moment determinant at n+m=N+1 | 98 |
| Positive proportional-weight singularity at (1,1) | 14 |

For either family separately, N=2,...,8 has respectively 3,6,10,15,21,28,36
interior normality checks; 3,4,5,6,7,8,9 terminal normality checks; and
0,0,1,3,6,10,15 flatness squares. Each square check compares nine polynomial
entries; it is counted once, not nine times.

All tested degree-N moment matrices are nonsingular, but their monic solutions
coincide with `prod_k(x-x_k)`. The h values then vanish, all tested degree-(N+1)
moment matrices are singular, and d=0 already at degree N-1 because both
successors coincide. In particular formulas dividing by d cannot be applied
naively at that final layer. No beyond-support NN recurrence is asserted or
tested. Nonsingularity at the terminal layer does not make the finite measure
pair perfect at every degree.

For the proportional example the code replaces w2 by `2*w1`. Its (1,1) rows
are proportional and determinant zero in every case, although all weights are
positive. The monic equations are consistent, e.g. `x^2-mu1(2)/mu1(0)` is one
solution. Thus singularity here concerns uniqueness/normality, not absence of
every monic solution. This counterexample is a separate modified input, not a
failure of either primary family's tests.

## Limits and runs needed

The labels “generic” and “binomial” name these explicit finite test inputs;
they imply no genericity theorem. Positivity alone is not taken as a normality
assumption. Matrix identity checks are stronger than merely evaluating the
action on one polynomial state, and both are recorded separately. This receipt
does not certify a general finite reduction or a computer-assisted proof.

- Supplementary independent rerun: separate agent and output/receipt; not counted
  as completed here.
- No floating-point experiment or C3/C4 performance comparison was run by this
  subagent. Any such experiment requires its own defined algorithms and receipt.

## Supplementary review correction

Astra identified an inaccurate comment about dependent predecessors. The
comment and its explanation above were corrected; all executable code is
unchanged. The original developer-run hash above identifies the original bytes.
The independent rerun receipt is [independent-check.md](independent-check.md);
it is additional evidence, not the required Claude audit.

Final comment-corrected rerun (orchestrator), executed from the repository:
`python topics/nn-mop-iep-20261103/code/exact_nn_mop.py > /tmp/nn-mop-final-exact.json`.
Exit 0; every count above reproduced. Code SHA-256
`8e420d166f82b3ec7730357a31dcbd684bf8694e3499f5803556a097e745cc7c`;
output SHA-256 `92e41630aa81a6e9071c2a1a325b353a968f6b15104142206e79ccbb8e2f44f6`.
JSON differs from the developer output only in its embedded code hash.
