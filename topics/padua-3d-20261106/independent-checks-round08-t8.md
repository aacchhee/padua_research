# T8 round08 independent supplemental checks

2026-11-06. Codex supplemental checker, assigned gpt-6.1-sol xhigh;
runtime model metadata is not separately exposed. Rules/input head:
`9042e1c42964150f30fdbe8563c12ba6c6a8692a`. The orchestrator published
the T8 gate and prospective protocol at
`69694f3a69ee139ac6b2d6d567c48e549575a8a5` before the new-family runs.
No Git operation or shared-registry edit was performed by this worker.
This record supplements the required focused Claude re-audit; it does not
replace it or approve the developer's material changes.

Scope: independently reconstruct the already proposed half-shift class,
rerun its selected witnesses and controls, and assess the existing nine
M=N certificates. This work generates no candidate mechanism and claims
no novelty or priority. Accordingly it uses the published T8 gate and
the existing cosine/finite-character and sign-trace routes without a new
ideas campaign. Read: repository rules and role, handoff08, audit03 T8 and
its exact-check code, the r06 certificate/fold/witness records, the r08
protocol, producer code/data and half-shift obstruction proof. The full
IDEAS registry was not reread for this bounded verification scope.

## Frozen code/data and commands actually executed

The independent checker imports no project mathematics:
[t8_r08_check.py](code/t8_r08_check.py), SHA256
`040b5393e24e851840d75b997f43bc69376e114793c92fa7e90aedf00f793d6f`.
The final receipts were generated with this exact checker. Earlier
development runs were superseded after enforcing distinct primes and
matching the frozen QR mode order; they are not the reported final runs.

From the repository root, prefix each command below with
`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python`:

```text
topics/padua-3d-20261106/code/t8_r08_check.py --old-witnesses topics/padua-3d-20261106/evidence/t8-r06-witnesses.json --output topics/padua-3d-20261106/evidence/t8-r08-check-old.json
topics/padua-3d-20261106/code/t8_r08_check.py --structure --census-n3 --quality --output topics/padua-3d-20261106/evidence/t8-r08-check-census.json
topics/padua-3d-20261106/code/t8_r08_check.py --halfshift topics/padua-3d-20261106/evidence/t8-r08-halfshift.json --quality --output topics/padua-3d-20261106/evidence/t8-r08-check-selected.json
topics/padua-3d-20261106/code/t8_r08_check.py --halfshift topics/padua-3d-20261106/evidence/t8-r08-halfshift-corrected.json --quality --output topics/padua-3d-20261106/evidence/t8-r08-check-corrected.json
```

All four reported commands exited 0. The first three ran concurrently, taking
respectively 4.082, 4.050 and 0.770 seconds. The fourth, after the dated tie
repair below, took 0.523 seconds. Environment: Python 3.12.14, NumPy 2.3.5,
SciPy 1.17.0, both recorded thread controls set to 1; no random sampling in
the checker. No network, container or external service was needed.

| Receipt | Bytes | SHA256 |
| --- | ---: | --- |
| [Old witnesses](evidence/t8-r08-check-old.json) | 5041 | `ddb9ecf0f7211bf49b81f9f0e748065ed1fbc37be6d33b169482ac0e9ebfdf02` |
| [Counts, exact n3 census and quality](evidence/t8-r08-check-census.json) | 13775 | `21c8632e3056aa60e7de7a07af5868acd1d71817cafcf350c5244fe69b9faa11` |
| [Selected witnesses and controls](evidence/t8-r08-check-selected.json) | 5968 | `1d2cfb28054ee7d943734b224bcc056885ede08f406b3ab319e9cdf3ec0899fb` |
| [Corrected selection and controls](evidence/t8-r08-check-corrected.json) | 6132 | `b57b36d38b2a2d045c2f427bb69025e762f629247553069fb729821ee9a21fa4` |

Every receipt is below 16 KiB. Input code/data hashes, exact parameters,
primes, roots, ranks and matrix/node hashes are inside the receipts; no
prose is pinned by the checker. The selected run verifies the producer's
three executable dependency hashes before using its data. Producer receipt
SHA256 is `87561592b48fcdcf062568b2e5a0a5586108e33d66c6f1518d24744f2d6c755b`;
producer source SHA256 is
`5435a6128dfdd44d0ebeed3f3a02bcb68856352b1b9aa2386a98ba098061058c`.
The old-witness input receipt hash is recorded in its independent receipt.

The complete 741-row independent n3 rank catalogue is regenerate-only raw
data at the unique scratch path recorded by the census receipt, 40977 bytes,
SHA256 `17c3a76e92a057f368676436b5a5671b838abde35c22cd3e901a8014773c676f`.
It was not archived or committed; the command deterministically regenerates
its scientific rows. The compact durable receipts contain the full positive
witness parameters and the complete exact-rank histogram.

## Independent exact arithmetic

Cosine nodes are reconstructed from integer angles modulo their common
denominator L, using the sorted triples of min(v,L-v). Cosine injectivity
on [0,pi] makes this an exact node-equality test. Each positive witness is
evaluated in the monomial basis, rather than the producer's product
Chebyshev basis, at two distinct fresh splitting primes above 1.7e9.
The checker uses its own deterministic Miller--Rabin test, trial-factor
root-order test and elimination; it imports neither SymPy nor producer
arithmetic. Each root has exact order L, and each prime is 1 modulo L.
Scalar Python integer powers/products construct the monomial matrix.
Elimination uses exact int64 values with p<1.9e9, so every product is below
p^2<2^63 and each subtract-product fits signed int64. Determinant
accumulators and inverses use Python integers. NumPy integer arithmetic,
Python, and the stated deterministic primality criterion are trusted.

The existing cyclotomic specialization proof applies: sending zeta_L to
the checked root defines a homomorphism on Z[zeta_L,1/2]. A nonzero
modular determinant implies a nonzero real evaluation determinant. The
change between monomials and product Chebyshev polynomials is invertible
at odd primes and in characteristic zero. No deficient modular rank is
used by itself as an upper bound.

## Count, parity and even-degree rank

Independently derived before seeing producer output: write M=2N and
theta_k=pi(2k+1)/M. Since z_1=1, equal first-coordinate cosines force
l=k or l=M-1-k modulo M. The second case agrees in every coordinate and
is free because M is even. Hence exactly N nodes occur for every b,c.

Translation by N induces R(x)_j=(-1)^(z_j)x_j. A folded node is fixed
precisely when 2k=N-1 modulo 2N. This has no solution for even N and two
parameter solutions belonging to one folded node for odd N. The node
trace is therefore f=N mod2. If t is the number of odd z_j, the polynomial
trace is D_t(n)=sum_(|alpha|<=n)(-1)^(alpha_1+...+alpha_t). Its generating
function is (1-s)^(-(4-t))(1+s)^(-t). For n=2m the three traces are
((m+1)^2,m+1,(m+1)^2), and for n=2m+1 they are
((m+1)(m+2),0,-(m+1)(m+2)). Sign-equivariance gives the exact upper bound
N-|D_t-f|/2. Thus every even n>=2 is excluded; odd-degree full rank
requires exactly two odd coordinates. This agrees with the developer's
complete hand proof in [the obstruction record](theory/t8-r08-halfshift-obstruction.md).

The checker independently enumerates polynomial traces for every n1..40,
checks N parity there, and directly folds three explicit generators at
each requested degree. These finite controls support the implementation;
the all-degree conclusion uses the proof above.

| n | N | Node fixed count | D1,D2,D3 | Best rank ceiling |
| --- | ---: | ---: | --- | ---: |
| 3 | 20 | 0 | 6,0,-6 | 20 |
| 4 | 35 | 1 | 9,3,9 | 34 |
| 5 | 56 | 0 | 12,0,-12 | 56 |
| 6 | 84 | 0 | 16,4,16 | 82 |
| 7 | 120 | 0 | 20,0,-20 | 120 |
| 8 | 165 | 1 | 25,5,25 | 163 |

## Complete exact n3 rank check

This checker independently evaluates every 1<=b<c<40, all 741 pairs.
For an exact characteristic-zero upper bound as well as a modular lower
bound, form an integer matrix C whose columns expand eight times each
product cosine in the basis cos(r*theta), 0<=r<N. The product-to-sum
identity gives eight signed frequencies. Reduce them modulo 2M, reflect
to [0,M], use cos((M-r)theta)=-cos(r*theta), and discard cos(N*theta)=0.

At the first N parameter angles, the matrix B of these basis cosines is
the DCT matrix, with B^T B=diag(N,N/2,...,N/2), hence invertible. Therefore
V=B*C/8 and rank(V)=rank_Q(C). The checker computes rank(C) using exact
integer row operations, dividing rows only by their integer gcd. These
operations preserve rational rank. Separately, it builds the actual-node
monomial matrix at two fresh primes for every pair. Both modular ranks
equal the exact rational rank in all 741 cases.

| Exact rank | Number of generators |
| ---: | ---: |
| 4 | 3 |
| 7 | 21 |
| 9 | 35 |
| 10 | 82 |
| 12 | 52 |
| 13 | 8 |
| 14 | 40 |
| 15 | 132 |
| 16 | 64 |
| 17 | 188 |
| 18 | 48 |
| 19 | 60 |
| 20 | 8 |

The eight survivors are (1,4,11), (1,4,29), (1,6,15), (1,6,25),
(1,11,36), (1,15,34), (1,25,34), (1,29,36). They all have exactly
20 nodes. A separate checked-division Bareiss determinant gives
|det C|=562949953421312=2^49 for all eight. Since B and the column
normalization depend only on n, all eight tie in exact absolute
orthonormal determinant. The original producer's machine scores selected
(1,6,25) by roundoff-scale differences; this is not a unique exact
determinant maximizer. The original selected generator and its receipt
are preserved as execution history. The dated correction below implements
the mathematical objective's exact ties and existing lexicographic rule.

## Original selections and independently measured quality

The n3/n5/n7 selections have exactly 20/56/120 nodes and full rank at
both independent primes. All eight n3 survivors were also measured
independently: four have Lambda21=9.78879826896222 and four have
Lambda21=17.24928814826148. These reproduce the producer's two clusters.

The independent quality route explicitly inverts a differently ordered
Chebyshev matrix and evaluates cardinals in 21 axis slices. It rebuilds
the Leja set and QR controls. The frozen QR construction needs the
producer's graded-total-degree basis order: floating pivot ties can change
under a basis permutation, even though interpolation on a fixed set is
basis independent. All final comparisons use that frozen QR ordering.

| n | Selected z | Independent Lambda21 | Leja21 | Frozen QR21 |
| --- | --- | ---: | ---: | ---: |
| 3 | (1,6,25) | 17.24928814826147 | 13.17471981994816 | 8.32067061468994 |
| 5 | (1,10,49) | 70.37294484036501 | 26.33661533788493 | 13.85750218511736 |
| 7 | (1,17,212) | 136.69039970499560 | 49.81258782308562 | 26.93507231925501 |

Selected condition numbers are 13.20, 31.77 and 54.57. Independent
inverse residual infinity norms are below 7.7e-14. The largest absolute
difference from a producer selected Lambda or control is 1.14e-13.
Maximizer coordinates may differ among symmetry-related tied mesh nodes.
All quality values remain **MEASURED** lower samples, not certified suprema.

The n5/n7 QR losses exclude promising status under the frozen D2 rule.
Only n7 is an eligible n>=6 odd-degree quality row, and it loses to Leja.
The two-consecutive-loss kill cannot fire within n3..8; excluded even
degrees are not quality losses. Three measured degrees also do not meet
the six-row growth-fit requirement. The producer's full numeric scans
at n5/n7 were inspected, not independently replayed here; this checker
certifies their final selections, not completeness of a numerical census
or global quality optimality.

### Dated exact-tie repair and its independent rerun

2026-11-06: after the original survivor qualities and the exact determinant
tie were known, the orchestrator requested correction of n3 selection to
the preregistered mathematical determinant objective with lexicographic
ties. This is an explicit post-run implementation repair, not a newly
prospective discovery or an undisclosed quality selector. The canonical
producer account is in [the attempt](attempts/T8-round08.md).

The new correction executable
[t8_r08_tie_correction.py](code/t8_r08_tie_correction.py), SHA256
`dd4f744aca52e09a6b15b0506ed9acce1f76a13fac9c99619b926cdb862167a8`,
computes exact C determinants on every one of the 380 trace-permitted
n3 pairs. The other 361 pairs are analytically excluded. It recovers
the same eight equal nonzero determinants, so exact determinant ties
select (1,4,11) lexicographically. This agrees with the independent
full 741-pair exact-rank/Bareiss check above. n5/n7 selection is unchanged.

The corrected producer receipt SHA256 is
`6612b8148225a2ee849e59c44c7686b12303825a4296a11ed6150243e1a70af9`.
The fourth actual command independently verifies all four producer executable
dependencies, rebuilds all three corrected selections and controls, and
certifies every selection at two distinct fresh primes. It gives:

| n | Corrected selected z | Independent Lambda21 | Condition2 |
| --- | --- | ---: | ---: |
| 3 | (1,4,11) | 9.78879826896222 | 7.64258666116916 |
| 5 | (1,10,49) | 70.37294484036501 | 31.76920495724978 |
| 7 | (1,17,212) | 136.69039970499560 | 54.57101285271123 |

The largest corrected Lambda/control difference from the producer remains
1.14e-13. Corrected n3 beats Leja and loses to frozen QR, but is below
the QR-loss gate's n>=4 threshold. The n5/n7 and D2 conclusions above
therefore remain unchanged. Both the correction and the new finite cubic
classification are material changes for the focused Claude re-audit.

## Old nine finite M=N witnesses: status assessment

The old nine explicit rational witnesses at n=1,3,4,5,7,8,9,11,12 were
all independently rebuilt and certified at two distinct primes above
1.7e9. They have exactly N nodes and full rank N, up to N=455 at n12.
The reduction and prior Claude audit already exist; this is another
executed independent rerun, not merely review of their outputs.

| Computer-assisted proof condition | Check |
| --- | --- |
| Explicit finite statement and rational inputs | The nine listed n,z,phase witnesses in the old receipt/theory. |
| Proved reduction to finite exact tests | [r06 certificate reduction](theory/t8-r06-certification.md), reconstructed above. |
| Exact arithmetic and validated prime/root | Producer checker and this independent monomial checker, with explicit integer bounds. |
| Committed checker and small evidence | Existing r06 code/receipts are committed; these supplemental files are ready for orchestrator publication. |
| Actually executed independent rerun | Prior Claude audit03 plus the new final old-witness command above, all nine passing. |

A separate finite-existence statement for exactly these nine degrees can
therefore be proposed as **computer-assisted PROVED**, once the proposed
record and supplemental artifacts are committed. This upgrades neither
quality nor the full mixed measurement document, and proves no all-degree
construction. The producer's optional separate record/status change is
**material** and must be explicitly included in focused Claude re-audit.
No remaining numerical or finite-certificate obligation was found within
this nine-witness scope. The broad minimal-polylog target remains OPEN.
