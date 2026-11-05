# Rigorous fixed-point witness producer

Developer: Codex, gpt-6.1-sol xhigh (inherited requested model/effort).
This is an implementation of the already fixed Padua weight formula, not a
new mathematical mechanism. It adds no novelty claim. The source conventions
are [the definitions](../padua-mz-2d-20261101/definitions.md) and the kernel
formula of PD-T106. Independent acceptance and the required Claude audit are
separate from this producer.

## Exact polynomial and its continuous norm

The source floating eigenvector is a proposal only. Its entries in the
orthonormal Legendre basis are converted to coefficients in the unnormalized
basis and rounded to integers C_ab at denominator S=2^q. The resulting exact
polynomial is

    p(x,y) = sum_(a+b<=n) C_ab P_a(x) P_b(y) / S.

The accepted object is this dyadic polynomial; no eigensolver assertion enters
the sign predicate. Its coefficients outside the total-degree triangle are
checked to be exactly zero. Its continuous squared norm is computed exactly
with FLINT rational arithmetic:

    N = sum_(a+b<=n) 4 C_ab^2 / [S^2 (2a+1)(2b+1)].

The producer rejects zero witnesses and requires N>0. It saves the exact
rational N and the exact integer coefficient array, with SHA-256 identities.
The coefficients are serialized as deterministic gzip JSON, including m, n,
q and the full row-major square array. Large witness artifacts remain outside
Git and must be manifested for cold-storage delivery. Their absence from Git
is not a claim of completed archival delivery.

## Node tables and exact tensor products

At each rational angle j/m or k/(m+1), Arb evaluates `cos_pi` with outward
rounding. The three-term Legendre recurrence, or the Chebyshev recurrence,
is evaluated entirely in balls. Precision defaults to 2m+q+160 bits to
compensate for interval wrapping. Every individual returned table entry is
rounded to an integer, and the rigorous predicate

    |P_a(x_j) - A_ja/S| < 1/S

(or its Chebyshev equivalent) must pass. Thus the recurrence's wrapping or
loss of precision can only reject a run. A higher precision changes table
centers but never relaxes their accepted error. It does not assume floating
trigonometric accuracy or a stable floating recurrence.

FLINT integer matrix multiplication evaluates

    U = A C B^T,       p_hat_jk = U_jk / S^3.

There is no floating matrix arithmetic, overflow, or approximate dot product
in acceptance. Put eps=1/S and L_C=sum|C_ab|/S. Since |P_a(x)|<=1 on [-1,1],

    |p-p_hat| <= delta_p = L_C (2 eps + eps^2)

at every grid point.

## Exact weight formula and its error

Write c_0=1 and c_a=2 for a>0. The exact kernel coefficient array is

    D_ab = c_a c_b h_a h_b  for a+b<=m,
    D_m,0 is halved,
    h_a=2/(1-a^2) for even a, h_a=0 for odd a.

The halving is the exceptional T_m kernel coefficient from PD-T106. The
kernel K is the tensor Chebyshev polynomial with these exact rational
coefficients. The exact signed Lebesgue weight is

    w_jk = rho_jk K(x_j,y_k),
    rho_jk = 2 e_j e_k / [m(m+1)]  on j+k even,
    e_j = 1/2 at coordinate endpoints and 1 otherwise.

The producer verifies exactly that sum rho_jk=1. It rounds each D_ab to a
dyadic coefficient and computes their total absolute rounding error E_D
exactly. Let L_D=sum|D_ab|. With certified Chebyshev table errors eps and
integer tensor product V, K_hat=V/S^3, the global rigorous error is

    |K-K_hat| <= delta_K
       = L_D(2 eps+eps^2) + E_D(1+eps)^2.

The separate zeroth-moment check requires the rigorous weight-sum enclosure
to contain four. The exactness theorem supplies Q_m(1)=4 independently;
this check detects implementation or convention errors.

## Rigorous contraction and sign predicate

The following finite sums over retained nodes are exact rationals, formed
from integer accumulators with endpoint multiplicities 1 or 2:

    q0 = sum rho K_hat p_hat^2,
    A0 = sum rho |K_hat| p_hat^2,
    B0 = sum rho p_hat^2.

Because |T_a|<=1 and sum rho=1, sum rho |K|<=L_D. Therefore weighted
Cauchy--Schwarz gives the rigorous energy error

    |Q_m(p^2)-q0| <= delta_K B0
       + 2 delta_p sqrt[(A0+delta_K B0)L_D]
       + delta_p^2 L_D.

The rational terms are exact; Arb encloses the square root and final
interval outward. Acceptance requires this enclosure to be strictly
positive or strictly negative. A straddling enclosure raises an exception
without emitting an accepted receipt. A strictly negative interval and
N>0 prove a negative Rayleigh direction in Pi_n. Together with the exact
positive direction Q_m(1)=4 this proves indefiniteness, rather than merely
failure of strict positive definiteness. The trusted arithmetic dependencies
are FLINT exact integers/rationals and Arb ball arithmetic, plus Python's
integer indexing/serialization. NumPy supplies proposals only.

## Commands and actual producer runs

From the repository root, with python-flint in the scratch dependency path:

```sh
PYTHONPATH=/tmp/mz-cleanup-deps OPENBLAS_NUM_THREADS=1 python topics/padua-mz-cleanup-20261105/code/rigorous_witness.py --m 400 --vector /tmp/mz-cleanup/vectors/m400-n399-min.npy --scratch /tmp/mz-cleanup/cert-m400 --output /tmp/mz-cleanup/cert-m400.json
```

All final producer receipts use source SHA-256
`11f7cabcfb3c431a26224eb0d8df49db5d7de65c4685f979a9037d835a1cd498`.
The final receipt files are `/tmp/mz-cleanup/cert-m<m>.json`; exact rational
norms and compressed coefficient witnesses are under
`/tmp/mz-cleanup/cert-m<m>/`. Their final committed locations are indexed by
the topic's evidence manifest. Every final receipt encloses weight sum four
and has an exactly positive computed rational norm.

| m | n | Rigorous energy enclosure (Arb printed enclosure) | Wall seconds | Peak RSS KiB |
|---:|---:|---|---:|---:|
|60|59|`[0.1885934804891 +/- 2.58e-14]`|0.0550|37,956|
|400|399|`[0.102818906 +/- 3.62e-10]`|3.3750|88,344|
|1101|1100|`[-0.0350668 +/- 4.18e-8]`|40.2902|410,356|
|1240|1239|`[-2.71e-5 +/- 6.00e-8]`|49.7728|505,780|
|1600|1599|`[-0.0234144 +/- 4.95e-8]`|94.8996|821,528|

The m60 result is strictly inside the accepted PD-T298 interval. K1 at m400
passes both criteria: 3.375 s is below ten minutes and the rigorously
computed relative width is below 2.54e-9, hence below 1e-6. All three larger
polynomials have strictly negative energy. The m1101 run separately checks
the odd-degree kernel convention, where h_m=0 makes the exceptional term
zero. The m1600 regenerated source eigenvector has SHA-256
`a23cb0e6e241993e5458474c64f153c965e8dc5047c2f1dfe08c7bc293e0a338`,
exactly matching the original PR23 vector identity.

Two initial engineering runs at m60 and m400, and an initial m1600 run,
preceded the addition of saved exact-norm files and the explicit zeroth
moment check. They are superseded by the final-source runs above; their
old receipts are not accepted provenance. The final-source runs were made
without editing the producer source while a run was active. In particular,
the final m1600 receipt replaces an engineering receipt whose end-of-run
source hash could otherwise have described a newer source than the one
loaded by that process.

Separate checker receipts use the alternate BLAS forward-error path, not
these fixed-point integer tensor contractions. Their exact coverage and
results are recorded in the independent checking report. Producer acceptance
is not self-audit: the required Claude audit remains a separate workflow
stage. Bulk witness delivery to AC's Padua cold storage is documented by
the orchestrator; a scratch path is not an archival delivery claim.
