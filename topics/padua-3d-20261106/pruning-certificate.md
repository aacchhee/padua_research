# Exact parity-subset certificate: proof reduction and schema

2026-11-07. Codex mathematical worker, configured gpt-6.1-sol xhigh;
provider runtime metadata unexposed. Rules reread in this session; original
rules/input `6d894d50efd8167c5b10f3d5b0da4d8cf214b681`, unchanged-rule
continuation input `ccab7af1ac38a6e8ec83b5d254a9260f0d57ea64`.
Root alone owns Git, shared records, artifact publication and counters.
This worker owns this new file only for this task.

Document kind: **verification proof reduction / proposed schema**. No new
construction or global theorem is proposed. The exact implication below
is PROVED standard algebra, specializing the existing
[T8 certificate reduction](theory/t8-r06-certification.md). Application
to a particular exported pruning payload remains **OPEN / not executed
here** until its exact checker and independent execution are recorded.
No new PD-T/PD-N or final ID is allocated. This known verification route
was gated in [next questions](pruning-next-questions.md); no new source
paper or inherited external theorem is used.

P3's root-reported finite quality survivor motivates delivery, without
becoming a premise of this proof. P4 is a separately registered degree16
transfer, not certified by this note. Checking an already counted support
and exporting its exact IDs is proof/artifact verification, **0 additional
research rounds**; it adds no new scientific measurement or counter.

## Exact object and canonical decoder

Let n>=1 and let m=(m1,m2,m3) be positive integer orders. This campaign's
artifacts use precisely m=(n,n+1,n+1). Define the complete list I_m by:

```
for i1 = 0,...,m1:
    for i2 = 0,...,m2:
        for i3 = 0,...,m3:
            retain (i1,i2,i3) iff i1%2 == i2%2 == i3%2
```

An **ID is the zero-based offset in this filtered list**, not a flattened
offset in the full tensor box. The third index varies fastest. This
matches the inspected `parity_nodes` implementation in code/u1_usable.py;
the checker must implement the integer decoder independently of that
producer. An ordered retained-ID list J must contain distinct integers
in [0,len(I_m)); require it strictly increasing for this schema. Each ID
decodes to i(j) and defines the mathematical point

`x(j)=(cos(pi*i1/m1), cos(pi*i2/m2), cos(pi*i3/m3))`.

All coordinates lie in [-1,1]. Cosine is strictly decreasing on [0,pi],
so different decoded triples give different exact real points. Thus valid
unique IDs prove distinctness without floating comparison tolerances.
The full count is `prod(floor(mj/2)+1)+prod(ceil(mj/2))`, by its two
disjoint parity classes. A decoder must verify this against its enumeration.

Write K=len(J), N=binom(n+3,3) and require K>=N. The exact point set is
the ordered list above; its definition needs no temporary NPZ or optimizer
history. For campaign payloads, additionally validate the expected n,
orders, K and selected construction-state identity against the published
scientific record, so a different valid subset is not substituted.

## Cyclotomic denominator and modular coordinates

Compute `L=lcm(2*m1,2*m2,2*m3)` using integers. The relevant cases are:

| n | orders | full count | N | L and factorization | angular exponent multipliers |
|---:|---|---:|---:|---|---|
|12|12,13,13|637|455|lcm(24,26,26)=312=2^3*3*13|13,12,12|
|16|16,17,17|1377|969|lcm(32,34,34)=544=2^5*17|17,16,16|

These LCMs follow from the displayed prime factorizations: 24=2^3*3,
26=2*13, 32=2^5, 34=2*17. The checker must recompute the LCM rather
than trust the payload's L. For each decoded coordinate put

`e(j,t)=L*i(j,t)/(2*mt)`, an exactly divisible integer.

With zeta=exp(2*pi*i/L), the exact coordinate is
`(zeta^e+zeta^(-e))/2`. It belongs to R=Z[zeta,1/2].

Choose an **odd verified prime** p with `(p-1)%L=0`, and a nonzero
rho in F_p of exact multiplicative order L. Verify

`rho^L=1`, and `rho^(L/q)!=1` for every distinct prime divisor q of L.

For n12 these divisors are 2,3,13; for n16 they are 2,17. This verifies
order L because every proper divisor omits some prime factor. Finding rho
by a primitive-root routine is not a substitute for these checks. A base
g raised to (p-1)/L is sufficient only if its resulting order is checked.
Use exact modular powers, not floating trigonometry. The modular point is

`x_p(j,t)=(rho^e + rho^(-e))*inverse(2) mod p`,

where `rho^(-e)=pow(rho,(-e)%L,p)` and inverse(2) exists since p is odd.
Integer primality must be proved by an exact trusted method recorded with
its limits; complete trial division through isqrt(p) suffices for small p.
An unqualified probable-prime result is not this schema's proof premise.

## Columns, minor and proof

Use all exponent triples alpha=(a,b,c)>=0 with |alpha|<=n. The producer's
declared order may be its existing degree order:

`[(a,b,d-a-b) for d in 0..n for a in 0..d for b in 0..d-a]`.

Check count N, uniqueness and completeness. For the rank certificate use
the **unscaled** columns `T_a(x1)*T_b(x2)*T_c(x3)`. Evaluate T by
`T_0=1, T_1=x, T_(r+1)=2*x*T_r-T_(r-1)` over F_p. These polynomials
have integer coefficients; their products form a real basis of Pi_n,
since the transformation from total-degree monomials is triangular with
nonzero diagonal. The continuous orthonormal columns used in measured
OLS multiply them by nonzero factors `2^(number of positive indices/2)`;
that real column scaling preserves rank. **Do not introduce sqrt(2) into
the finite-field evaluator or assume it lies in R.**

Let E be the exact K-by-N unscaled evaluation matrix. Select N distinct
retained IDs, specifying their order, and form the square row minor D.
The certificate condition is `det(D_p)!=0` in F_p, where D_p is evaluated
at the modular coordinates above. Selecting this minor by exact modular
pivoting is verification of the existing set, not a new construction.
For an unambiguous determinant receipt, rebuild that specified N-by-N
minor and compute its determinant; do not call a product of unspecified
rectangular-elimination pivots a determinant of E.

**Proof of the implication.** Since p=1 mod L, p does not divide L.
The polynomial t^L-1 has no repeated roots over F_p. Its factorization
`product_(d|L) Phi_d(t)` and rho's exact order imply Phi_L(rho)=0:
a root of Phi_d for d<L would satisfy rho^d=1. Hence substitution
`zeta -> rho` defines a ring homomorphism `R -> F_p`, extending integer
reduction and sending 1/2 to inverse(2). All coordinates and entries of
D belong to R, and polynomial evaluation/recurrence commute with it.
Determinants commute with ring homomorphisms, so

`image(det(D))=det(D_p)!=0`.

Therefore det(D) is nonzero in R and in its given complex embedding.
Its entries are real, so this is a nonzero real determinant. E has rank
N. Evaluation on these K points is injective on Pi_n, proving that the
set is Pi_n-determining. For K=N this is unisolvence/interpolation; for
K>N arbitrary K data need not be exactly interpolable, but ordinary LS
has a unique coefficient minimizer. Positive fixed row weights preserve
rank, without supplying a noise or conditioning theorem.

One nonzero modular minor suffices mathematically. A zero minor or deficient
modular rank is **inconclusive**, not a characteristic-zero singularity
certificate: that prime can annihilate a nonzero algebraic determinant.
No inverse implication or lower bound on |det(D)| is asserted.

## Proposed compact payload and verification receipt

The implementation may choose filenames; it must freeze/version the
schema before export and reject unknown versions. Essential geometry:

```
schema: pdpr-parity-subset-v1
n: integer
orders: [m1,m2,m3]
indexing: parity-filtered-lex-zero-based-v1
retained_ids: strictly increasing integer list J
count: K
dimension: N
geometry: exact-cos-pi-index-over-order
construction: protocol/source/receipt identity and selected state
```

Reject booleans, nonintegers, duplicate/out-of-range IDs, unexpected orders,
count/dimension mismatches and K<N. Derive geometry and counts from n,
orders and IDs; metadata is checked, not trusted. Small plain JSON IDs
should fit the storage limit; verify actual bytes. Do not split a logical
object merely to bypass the limit. No coordinate matrix or factorization
need be stored: these can be regenerated from the exact definition.

The exact verification receipt records:

- payload path, byte count, SHA256 and complete canonical decoded IDs;
  the IDs may be referenced from that essential payload without duplication;
- expected construction-state identity, n/orders/K/N/full count, computed
  L and its checked prime factors;
- p, exact primality method, rho and every order-test residue;
- basis label and complete exponent-order definition, N-column check;
- N distinct minor-row IDs/order, their membership in J, rank N, determinant
  residue in [1,p), pivot/swap conventions and exact elimination algorithm;
- source/input identities, actual command, UTC start/end, versions, arithmetic
  model/overflow bounds, CPU/wall cost and explicit failures/unrun checks;
- a separate payload-to-measurement linkage status, and independent-check
  receipt identity when actually executed. No prose-acceptance hash pin.

If a row-list codec is used, it must be lossless and versioned with exact
length/range/distinctness checks. A deterministic row-selection algorithm
may instead reconstruct the minor, provided the checker verifies the
specified ordered minor and records its identity. Stored hashes alone do
not replace actually computing the nonzero determinant. No full matrix
or elimination transcript is required for an independent replay.

## Integer arithmetic and overflow contract

Python unbounded integers with reduction after each operation need no
fixed-width overflow assumption. A NumPy implementation must explicitly
use signed int64 residues in [0,p) and, for the following simple contract,
enforce `p<2^30` before allocating/operating. Then:

- two residue products are <(p-1)^2; the Chebyshev expression
  `2*x*T_r-T_(r-1)` has magnitude <2*(p-1)^2+(p-1)<2^63;
- modular coordinate addition followed by multiplication by inverse(2)
  is also <2*p^2; row normalization and outer-product elimination use
  single residue products and differences with magnitude <p^2+p;
- reduce after EACH pairwise product: a three-coordinate basis product
  must be `((u*v)%p)*w%p`, not an unreduced triple product;
- never use an unbounded-length int64 dot/matrix product without a proved
  accumulator bound or intermediate reduction. `N*p^2` can overflow even
  when each product fits. Floating BLAS elimination is not exact arithmetic;
- convert scalar determinant/power/inverse/exponent/LCM arithmetic to
  Python integers as needed; reduce pivot products after each step.

The checker must record the actual bound and staged operations it uses;
changing p/dtype/operations invalidates this generic contract until checked.
No silent NumPy wraparound, float-to-int rounding or probabilistic pivot
test is admissible. An independently written NumPy checker can be exact
under its own verified bounds; importing the producer's math routine is
not independent implementation.

## Independent criterion and linkage to measured quality

A distinct checker decodes the essential IDs independently, reconstructs
the exact integer triples, verifies counts/domain/distinctness, and chooses
a **different verified compatible prime** with its own exact-order root.
It evaluates the complete **monomial** basis (preferably a different
explicit exponent order) and finds/verifies a nonzero N-minor of its own.
It need not reuse the producer's minor. Zero at a new prime is inconclusive;
any bounded prime retry policy and every attempt must be recorded.
The acceptance criterion is matching payload identity/geometry and two
independently executed full-rank checks, not equal determinant residues
across different fields or bases. Record independent source/command/output
and trusted library limits before claiming a computer-assisted finite proof.

For usable delivery, separately check that exported IDs exactly equal the
retained canonical IDs at the claimed scientific checkpoint. Link the
original measured node-array byte identity and order. If a frozen floating
decoder is offered, compare its regenerated binary64 coordinates with the
measured array and report actual byte equality/differences, versions and
cosine-evaluation expression. Reproducing floats does not make them equal
to ideal cosines. Cross-platform last-bit differences require honest
reporting, not an assumed exact coordinate identity.

This certificate proves rank of the **ideal algebraic cosine set**.
It proves neither rank of a separately interpreted dyadic set nor a
certified perturbation transfer to those rounded nodes. Measured rounded
quality, amplification, covariance, error and cost remain MEASURED under
their recorded operator/noise assumptions. There is no certified norm,
determinant lower bound, stability margin or all-degree construction.
The old [455-node U2 witness](theory/u2-degree12-unisolvence.md) instead
proves rank of its stored binary64 values interpreted as exact dyadic
rationals. That witness, its payload and its claim remain unchanged.

## Runs needed and history

Root's technical worker next implements/freezes the decoder, payload
export/linkage and exact producer/independent checkers, then records their
actual outputs for any chosen quality survivor. No prime, root, payload,
minor, rank computation or new quality run was executed by this worker.
Only repository reading and writing this proof/schema occurred here.
The general correctness implication is proved above; no selected finite
artifact is promoted to PROVED by this unexecuted plan.

2026-11-07: standard certificate route specified after gated P3 quality
evidence; prerequisite source proofs/old dyadic witness and canonical
integer enumeration inspected. No new paper reading, priority claim,
research-round allocation, source-code mutation or Git operation.
