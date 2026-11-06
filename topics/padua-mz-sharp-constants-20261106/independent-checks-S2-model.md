# Supplementary S2 endpoint-model checks

2026-11-06. Codex supplementary checker, requested gpt-6-astra high;
actual runtime metadata unexposed. Rules/source input:
`2143ad622fa98faf8fe7d5cb8ed2bb7e0062f861`.
Scope: mathematical validity of the fixed-J lemma and closed-form
matrix, plus actual independent finite numerical replay. No novelty,
priority or full sharp-limit approval. Full novelty/Claude audit remains
separate; this check proposes no new mechanism.

**PASS in this scope.** One MINOR DCT normalization display in the
prediction record was returned to the developer and fixed. It did not
change the cancelling trial, operator prediction or numerical code.
No unresolved BLOCKING, MAJOR or MINOR finding remains.

## Frozen records and execution

Read the complete [prediction](theory/S2-endpoint-model.md),
[fixed-J theorem](theory/S2-fixed-trial-limit.md), producer and developer
receipt. The PD-T013 cardinal/weight definitions and S2 uniform5/3
theorem were already read/reconstructed in this session.

- Fixed-J theorem audited SHA-256:
  `e11070a2876f3ea87857f00ab471a55713ccdfba13aa5af77e11ef38a6db91c1`.
- Corrected prediction SHA-256:
  `aa1117239e7060d816664a712319a7e17f74ca385860f95de29f77eedff9ff89`.
- Frozen producer code/S2_model.py SHA-256:
  `4c2ad09ad14bfe180243d0e57b8987ec2688bc61bd5e379e141d73aa0cb5723a`.
- Developer evidence/S2-model.json SHA-256:
  `84af25b7c251d0dd200d348d4798383e04741ee818c6af0725e4378ba4b41961`.

The model prediction was registered at513f3bd before its Galerkin run.
After verifying the producer hash, independently executed from
`/workspace/sharp-work`:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python topics/padua-mz-sharp-constants-20261106/code/S2_model.py --sizes 32 64 128 256 512 --quad-periods 2000 --output topics/padua-mz-sharp-constants-20261106/evidence/check-S2-model-replay.json
```

The process exited0. Python3.12.14, NumPy2.3.5, SciPy1.17.0; no random
seed is used. The [independent receipt](evidence/check-S2-model-replay.json)
records timestamp, command, platform, versions and producer identity.
Its SHA-256 is
`15598ff686fa183f63b1448e1d07eb15854bf7ac8446ff41c4158cfe51c9c858`,
4441 bytes. Every Galerkin eigenvalue and the complete quadrature
result list exactly match the developer output. This is an actual
separate execution using the same inspected implementation.

| J | Largest measured generalized eigenvalue |
|---:|---:|
| 32 | 1.004420045396333 |
| 64 | 1.0044298834885106 |
| 128 | 1.0044362411630081 |
| 256 | 1.004436493737461 |
| 512 | 1.0044369188646673 |

Maximum reported generalized relative residual:1.780e-15. All six
direct quadrature comparisons at indices1,2,3 pass their recorded
diagnostic threshold. The largest absolute discrepancy is2.530e-12.
The remote tail estimate follows from |f_j(t)|<=(8/3)a_j²/t³:
integrating its product against t gives16a_i²a_j²/(9T⁴), exactly
as implemented. Adaptive quadrature's reported finite-interval error
is not rigorous interval arithmetic; these numerical observations
are **MEASURED**, not certified eigenvalue enclosures.

## Independent reconstruction of the closed-form Gram

The stable near-pole formula for f_j follows by t=a_j+z and
sin(a_j+z)=(−1)^j sin z. The direct quadrature evaluates the canonical
integral t f_i f_j, independently of the special-function matrix entries.
The following algebra also checks those entries for all integer indices,
not only the six quadrature examples.

For a a positive integer multiple of pi, put
d(a)=gamma+log(2a)−Ci(2a) and

    I(a)=integral_0^infinity sin²(t)/[t(t²−a²)]dt.

Using t/(t²−a²)=(1/(t−a)+1/(t+a))/2 and translating sin² by a
shows that the difference of its logarithmically divergent integrals
equals −integral_0^a sin²(v)/v dv. Therefore
I(a)=−d(a)/(2a²). The difference is taken with common finite cutoffs
before passing to infinity, so no separate divergent value is assigned.
Partial fractions now give, for i!=j,

    C_ij=4(−1)^(i+j)a_i²a_j²[I(a_i)−I(a_j)]/(a_i²−a_j²),

which is precisely the implemented off-diagonal formula.

For the diagonal, the decomposition

    1/[t(t²−a²)²]
      =(1/a⁴)[1/t−t/(t²−a²)]+(1/a²)t/(t²−a²)²

and integration by parts give

    integral_0^infinity t sin²(t)/(t²−a²)²dt
      =(1/2)integral_0^infinity sin(2t)/(t²−a²)dt
      =Si(2a)/(2a).

Translation in the two linear-denominator integrals proves the last
identity. Boundary terms vanish at0, infinity and the removable
interior pole. Thus C_jj=2[d(a_j)+a_j Si(2a_j)], as implemented.
The discrete form diag(omega)+4ss^T follows directly from the prescribed
samples f_j(0)=−2s_j and f_j(a_k)=delta_jk.

## Fixed-J analytic theorem

### Degree and exact ratio

The correct top coefficient is (1/N)sum c_k(−1)^k v_k, with endpoint
halfweights. The prediction's earlier2/N display was wrong by a common
factor; cancellation was still valid. The developer corrected it and
uses1/N in the theorem. The two prescribed nonzero samples cancel,
and the J trial polynomials are independent by their interior samples.

Subtracting the endpoint cardinal from the jth cardinal and applying
cosine differences yields exactly the displayed sinc ratio R_(N,j).
The formula gives R(0)=R(a_j)=1 by continuity. On t<=N with N>=2A,
the three denominator sinc factors are at least0.9. The numerator
and denominator factor deficits sum to at most
t²/(4N²)+a_j²/(6N²). Dividing by0.9³ is smaller than
(t²+a_j²)/N², proving the local error with its stated constant.
The numerator is nonnegative and bounded by1.

On the full range0<=t<=pi N, the denominator arguments lie in the
specified intervals and give the global bound
R<=3pi³/(8sqrt2)<9. The transformed mass element is exactly
t sinc(t/N)dt. Combining R<=2 and the local errors gives the factor4
in equation(9), with room for the Jacobian error.

### Continuous error constants

The cosine-integral representation gives |f_j|<=4 everywhere, while
its rational form gives |f_j|<=3a_j²/t³ for t>=2A. Splitting there
reproduces both equation(10) constants:

    integral t|f_i f_j| <=32A²+9/64,
    integral t³|f_i f_j|<=64A⁴+9A²/8.

Substitution in the factor4 local error gives
[512A⁴+(45/8)A²]/N². The actual and limiting tails together cost
82 times the limiting absolute tail, bounded by(369/2)A⁴/N⁴.
Since N>=2A, the latter is at most(369/8)A²/N². These constants
are indeed below1000(1+A⁴)/N² for A>=pi. Multiplication by J
is a valid operator-norm bound for a J-by-J entrywise error matrix.

### Both parity weight errors

For F_j(x)=(1−cos(bx))/(2x²), b=2pi j, the integral representation
implies F_j<=b²/4 and |F_j'|<=b³/12. The exact difference of a
summand from F_j(k/N)/N is

    N[1−cos(bk/N)]/[2k²(4k²−1)]
      <=b²/[4N(4k²−1)].

Its total is at most b²/(8N). For odd N, the right-rectangle sum
and missing half interval give the stated remaining error. For even
N, the endpoint correction is a half trapezoid term; its replacement
cost is at most2/[N(N²−1)]. The constant N²/(N²−1) adds
1/(N²−1). These extra even-parity terms fit within2/N. The missing
lower half endpoint and the Lipschitz trapezoid estimate give the
same displayed bound. Integration by parts yields
g_j=cos(pi j)+pi j Si(pi j). Doubling and taking the maximum j<=J
is well within the stated coarse20(1+8A³)/N estimate. The endpoint
rank-one error has norm at most4J/(N²−1), proving equation(2).

### Model boundedness, Rayleigh error and lower limits

C is positive definite because a zero continuous mass forces the
finite continuous combination to vanish everywhere, and its interior
samples recover all coefficients. The integral expression gives
omega_j>=2. Passing the checked uniform5/3 CC bound to each fixed-J
form limit gives D<=5C/3. The sample map therefore extends boundedly
to the completion and its squared norm is exactly the supremum of
finite-dimensional generalized maxima, bounded above by5/3.

For a unit coefficient vector, writing the difference of the two
Rayleigh quotients with common denominator and using D/C<=5/3 gives
[d+(5/3)e]/(m_J−e) whenever e<m_J. Taking suprema proves equation(3).
Each finite trial subspace lies inside Pi_(N−1); taking N to infinity
at fixed J, along either parity, then the supremum over J proves the
two lower-limit statements. It does not give a full upper limsup.

The lower assertion Lambda_edge>=1 also checks. At a=pi j and
t=a+v, the local mass divided by a has integrand

    [4a³/((a+v)(2a+v)²)]*(sin v/v)².

On |v|<=a/2 the bracket is bounded and tends to1 pointwise.
The complementary low-t mass is O(log a), the high-t mass is O(1),
and both vanish after division by a. Dominated convergence therefore
gives C_jj/a→pi. The same elementary Dirichlet integral gives
omega_j/a→pi; the endpoint4/a vanishes. Single-trial ratios tend1.

## Exact limits of approval

The theorem proves explicit fixed-J errors, boundedness of the model,
1<=Lambda_edge<=5/3, and both-parity lower limits for the actual upper
spectrum. It does not identify Lambda_edge numerically or bound the
full spectral limsup. The finite J512 value differs from the K3 fitted
intercepts by about5.34e-8; this is a measured proxy comparison only.
No certified infinite Galerkin tail is present. Neither the finite
stability nor the fixed-J theorem proves convergence of the full CC
upper spectrum or extremal parity equality.
