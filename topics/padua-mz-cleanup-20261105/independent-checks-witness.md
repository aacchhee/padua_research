# Independent finite-witness check

Rules/input head: `ad503cb0603fc017444b0aa732240981eefa4d24`.
Independent worker: Codex, inherited user-requested `gpt-6.1-sol xhigh`.
This is a separately executed supplementary arithmetic check of C1, not
the required later Claude audit. No eigenvalue computation is an
acceptance premise. No new mathematical mechanism or novelty claim is
proposed: the existing signed-node formula and a prescribed rational
polynomial are verified. The idea-generation gate is not applicable.

## Different arithmetic path

The producer uses exact fixed-point integer tensor matrix products. This
checker independently builds Arb-certified **binary64** node tables,
uses floating BLAS tensor products, and encloses their errors analytically.
It imports no producer code and reads only the chosen rational polynomial
artifact. Shared trusted components are Python, NumPy/BLAS, FLINT/Arb,
the frozen signed quadrature convention, and ordinary Legendre and cosine
identities. It is not an independent proof of the cardinal formula.

For exact unnormalized Legendre coefficients `c_ab=C_ab/2^bits`, the
checker requires `a+b<=n<m`, integer numerators and a nonzero polynomial.
Its two node tables approximate `P_a(cos(j*pi/m))` and
`P_b(cos(k*pi/(m+1)))`, each entry with absolute error below
`delta=2^-48`. Arb uses `2n+192` bits for the Legendre recurrence to absorb
interval wrapping; every resulting binary64 entry is checked against its
enclosing ball. On `[-1,1]`, `|P_a|<=1`: the Laplace integral represents
it as the average of `(x+i sqrt(1-x²) cos(phi))^a`, whose modulus is at
most one. Thus the true tables have entry bound one.

Put `u=2^-53`, `gamma_k=ku/(1-ku)` and `L=sum|c_ab|`. Integer-to-double
conversion followed by exact power-of-two scaling has coefficient
absolute error sum at most `u L`. If each dot product of length `k`
satisfies the standard binary64 gamma bound, the two matrix products
therefore give a **uniform nodal polynomial error** at most

`E_p=(L+u L)(1+delta)^2(1+gamma_(n+1))^2-L`,

plus the explicitly included absolute underflow budget. This follows by
bounding the two absolute dot products entrywise, expanding the input
table errors, and summing `|c_ab|`; it avoids an unsupported inference
from an eigensolver residual.

The weight computation independently assembles the **even-frequency**
triangle `D_ab=t_a t_b` for `a+b<=floor(m/2)`, with `t_0=2` and
`t_a=-4/(4a²-1)`. If m is even, subtract `2h_m` at `(m/2,0)`, where
`h_m=2/(1-m²)`. This is exactly the integrated cardinal formula

`w_jk = 2 epsilon_j eta_k/[m(m+1)] * [sum D_ab cos(2a theta_j) cos(2b phi_k)]`.

Each cosine entry is independently enclosed using Arb's cosine, then
converted with the same checked `delta` bound. Coefficient rounding is
bounded by summing its actual Arb enclosures, rather than assuming
rational coefficients are exactly representable as doubles. The same
two-dot-product argument gives the kernel error from `||D||_1`, its
rounding-error sum, `delta` and `gamma_(floor(m/2)+1)`. The code separately
accounts for rounding the rational prefactor and multiplying it into
the kernel. Endpoint halving is exact in binary64 (subject to the
included underflow allowance); checkerboard deletion is exact. These
steps yield one uniform absolute weight error `E_w`.

For floating nodal values `p_hat` and weights `w_hat`, the checker adds

`2 E_p sum|w_hat p_hat| + E_p² sum|w_hat|`

`+ E_w [sum p_hat² + 2 E_p sum|p_hat| + N E_p²]`

to a gamma enclosure of the floating sum `sum w_hat p_hat²`. All
nonnegative sums and scalar product rounding factors are bounded
outward with Arb. The signed sum uses the absolute term sum. Finite
values are required; a straddling final interval raises an exception.
Absolute underflow allowances of order `2^-1000` times operation-count
and coefficient factors exceed the binary64 minimum subnormal budget.

Finally, if any `c_ab!=0`, orthogonality gives the explicit positive
norm summand `4 c_ab²/[(2a+1)(2b+1)]`. Thus an accepted negative Q enclosure
proves that the rational polynomial has negative signed sampled energy
and positive continuous norm. The constant polynomial has Q=4>0, so
the Gram form is indefinite, not merely nonpositive.

### Arithmetic trust boundary

Arb intervals are outward-rounded. The alternate checker additionally
assumes round-to-nearest binary64 operations and that each CPU BLAS
dot product satisfies the conventional gamma bound; fused multiply-add
is permitted and cannot worsen that bound. NumPy reports OpenBLAS
0.3.30 (scipy-openblas, Haswell/dynamic x86_64 architecture, ILP64).
One BLAS/OMP thread was set. This is a stated arithmetic implementation
assumption, not a formal verification of OpenBLAS machine code. The
producer's accepted integer check supplies a separate path with no such
BLAS error-model dependence.

## Executions actually completed

Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0, python-flint 0.9.0. From the
repository root, each execution used:

```sh
PYTHONPATH=/tmp/mz-cleanup-deps OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-mz-cleanup-20261105/code/independent_witness.py --witness /tmp/mz-cleanup/cert-mM/witness.json.gz --output /tmp/mz-cleanup/independent-mM.json
```

Here M was separately substituted by 60, 400, 1101, 1240 and 1600. Source SHA-256:
`60c1e6db62fbd1c422fae2fa29476afad2796aa503a1225d7f507745fa08361f`.

| m | Independently evaluated Q center | Absolute error upper bound | Seconds | Result |
|---|---:|---:|---:|---|
| 60 | 0.18859348048909605 | 1.334e-12 | 0.029 | Strictly positive; consistent with accepted m60 bracket |
| 400 | 0.10281890623374046 | 3.010e-9 | 1.889 | Strictly positive; relative width <5.854e-8, independently passing K1 |
| 1101 | -0.03506683433961493 | 5.785e-8 | 19.762 | Strictly negative odd-m finite witness |
| 1240 | -0.000027148059718313734 | 8.191e-8 | 26.274 | Strictly negative finite witness |
| 1600 | -0.02341441659322948 | 1.743e-7 | 37.654 | Strictly negative finite witness |

The m400 run took less than ten minutes and width/|Q| is below 1e-6.
The larger m1600 run need only establish strict negativity, which it does.
These are energy enclosures of the chosen rational polynomials, not
certified extremal eigenvalue brackets or positivity of a whole Gram form.

Witness SHA-256 values, respectively:

- m60: `9a1bb58cce8d8179840a024f045e8bbb32aafe9ad58d7545af4ec74278d566e9`;
- m400: `b433ab66e1d7e971629c58b4c56839a013bf1bfb64e021ccac09b84bd1bb094d`;
- m1101: `22913a3271c0cd826ff062a1f880c3539ef937b0141820dab381b53181662813`;
- m1240: `1a9faac5677ac4dde63749a6acac38d95ee88a5082445e6ba6b59cc297d35e4e`;
- m1600: `16d89f2c8600364aac3962c4164f0e0875c4fa866fc61269fd6f849e8f1fdad6`.

Receipt SHA-256 values:

- m60: `b2fe5d352c0d32f51713fe1bac62c87c3ddcaebe0541420f6c700165581a7d68`;
- m400: `1926664c0f45c92b75bf58570df396914220559b402afbb0b626e6369b99a2b9`;
- m1101: `7b0b36fa7c3f6ef1603fe98345f4355c31c6b06671234d86c1ec8664d4ea8a74`;
- m1240: `0b4f58ba0c209fecb4ba4300f9c1fec90e321253aad753fde03aa44297c42b5f`;
- m1600: `6b28a7514b41537bb027ae2301188e21f86b6ef0c9cd6e9c106592f8edce6912`.

Two separately executed malformed-input controls exited 1 before any
acceptance receipt: an above-cutoff coefficient at `(a,b)=(1,1)` for
`n=1` rejected with `polynomial exceeds the total-degree cutoff`, and
the zero polynomial rejected with `zero polynomial`. Those scratch
inputs are `/tmp/mz-cleanup/independent-invalid-{wrong-degree,zero}.json.gz`.

Small receipts remain in `/tmp/mz-cleanup/independent-mM.json` for the
orchestrator to inventory and commit. Bulk rational witnesses are
regenerable artifacts, and Padua cold-storage delivery is pending.
