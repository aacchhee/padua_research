# G0 numerical attribution diagnostics

Status: MEASURED verification record, not a theorem, new mechanism, target run,
or gate disposition. Developer: Codex, requested gpt-6.1-sol medium technical
work under rules `f85c7b5c83822ff60b62c84bed1ec6ae31628422`.
No novelty content is added, so the novelty gate is outside this bounded replay.
Only the topic-local script, this methods record and its compact receipt are owned
by this worker. No Git mutation was performed.

## Reproduction and scope

The pinned source snapshot is `8359bf7a047d9a212bd841224fb97a458cb7435e`,
using its original E6 helper, L2/L1 dependencies and polyrat commit
`6903d7af9995c9d88e661fb229626696e00fdfba`. The script asserts their byte
hashes. It constructs exactly the frozen T24 nodes by once-rounding rationals
`(i/12-1,j/12-1)`, `i+j<=24`, with unit weights, degree 12,
M=325 and N=91. Input hash is in the receipt. The two dispatched kernels are
Haswell and Nehalem, selected prospectively from the previous bounded probe;
no other kernels or parameter choices are searched here.

Executed from the repository root:

```sh
OPENBLAS_NUM_THREADS=1 OPENBLAS_CORETYPE=Haswell PYTHONPATH=/tmp/padua-lanczos-frontier-g0/deps python -B topics/padua-lanczos-frontier-20261105/code/g0_attribution.py --external /tmp/padua-lanczos-frontier-g0/polyrat --snapshot /tmp/padua-lanczos-frontier-g0/replay --output-dir /tmp/padua-lanczos-frontier-g0/attribution-pinned --receipt topics/padua-lanczos-frontier-20261105/evidence/g0-attribution.json
```

Reruns must use a new external output directory and their own receipt path.
The receipt records exact subprocess commands, runtime/library identities,
source hashes and hashes/bytes for external raw Q/H, references and propagated
residual artifacts. These `/tmp` outputs are temporary working storage;
archival/delivery remains pending the orchestrator's prescribed cold-storage
procedure. No large artifact or third-party source enters Git. The executed precision helper
was mpmath 1.3.0; dispatch inspection used threadpoolctl 3.6.0.

## Distinguishing reference error from recurrence error

Original NumPy CGS2 upstream xy/yx and L2 alt/mirror/adapt are executed unchanged.
The local dev equals upstream yx entrywise in the inherited replay; its numerical
attribution is therefore the yx row. Higher-precision controls rerun the same
functions with longdouble nodes, matrices and arithmetic on identical already
rounded binary64 inputs. The arithmetic precision changes; the selections and
algorithm do not. The x86 longdouble mantissa has 63 stored fraction bits.

An independent Dubiner reference is built with a longdouble three-term Jacobi
recurrence, then CGS2. A second reference evaluates Jacobi polynomials using
finite binomial sums at 50 decimal digits on the *identical binary64 nodes*,
rounds once to longdouble and applies the same reference CGS2. Spectral norms
are computed after longdouble projection and conversion of the small residual
matrix to binary64. These are numerical diagnostics, not interval enclosures.

The two reference projectors differ by `1.1172e-18`, their orthogonality defect
is `1.4410e-18`, and the column-normalized Dubiner condition number is 9.13376.
The full old E6 double reference departs from this reference by `1.3353e-14`.
That projector error must not be confused with the smaller *scalar gap
corrections for fixed Q* in the following table.

| Haswell method | Original E6 gap | Recomputed fixed-Q gap | Same algorithm in longdouble |
|---|---:|---:|---:|
| upstream xy | 7.5952754186e-10 | 7.5952769650e-10 | 1.9447e-13 |
| upstream yx = dev | 2.7558694937e-10 | 2.7558698676e-10 | 2.3013e-13 |
| alt | 1.3027152070e-12 | 1.3021561007e-12 | 2.5845e-15 |
| mirror | 1.4562450798e-14 | 1.2399859853e-14 | 3.9749e-18 |
| adapt | 7.6816304185e-14 | 7.6247861761e-14 | 4.8135e-17 |

For both worker kernels the legacy diagnostic is evaluated in the parent
Haswell process against the same Haswell-generated E6 reference. Thus the
Nehalem legacy scalar can differ at the reference-noise scale from the earlier
all-Nehalem E6 execution; that is deliberate fixed-diagnostic control.

Thus reference corrections explain neither the upstream xy historical/current
change `4.2044e-10`, the dev change `2.7467e-11`, nor the alt change
`5.9983e-12`. Mirror is sufficiently close to the old reference floor that its
relative gap differences need care. Higher precision reduces every measured
error, by factors about 3906, 1198, 504, 3120 and 1584 respectively. This is a
precision control for an inherited algorithm, not a new scientific comparison.

## Frozen recurrence and source propagation

Upstream directly returns Q, H and indices. For alt, original L2 returns Q and
parents but no H. Replaying the exact two CGS passes against each stored prefix
produces `c=s1+s2` and beta, and the reconstructed `r/beta` is asserted equal to
the original Q column **entrywise** in both precisions and kernels. No
least-squares coefficient fit or reference-based correction is used.

On frozen computed Q/H, the formed-column residual is recomputed in longdouble:

`f_k = A_k q_parent - Q_<k c_k - beta_k q_k`.

Its sign follows PD-T142. With zero initial error, the nodewise triangular
inverse solve is

`E_k = (A_k E_parent - E_<k c_k - f_k)/beta_k`.

Equivalently the frozen-coefficient polynomial surrogate V starts with exactly
the same constant Q column and satisfies this recurrence with zero residual;
`E=Q-V`. The script independently evaluates that surrogate at 50 decimal digits
with exact conversions of binary64 node/coefficient/start-vector values. It
saves the resulting E, alongside the longdouble F, in the external propagation
files. This is the same frozen triangular inverse applied to the *exact*
formed-column residual, evaluated without subtracting nearly cancelling
binary64 dot products. It does not perturb H or fit Q to the reference.
The non-unit-rounded q0 is constant, hence lies in the exact polynomial space;
its scalar normalization contributes no normal error.

Normal projection of E uses the well-conditioned reference. Comparing it to
normal projection of Q implements PD-T142's surrogate identity, without
claiming a rigorous computed upper bound for its K. Q is reorthonormalized in
longdouble for the separately reported span gaps; its orthogonality defects
are about 1e-15, and raw-Q normal norms agree at the displayed gap precision.

| Kernel/method | max local ||f_k|| | ||F||_F | measured normal error | 50-dps inverse reconstruction discrepancy |
|---|---:|---:|---:|---:|
| Haswell xy | 1.0113e-16 | 7.6132e-16 | 7.5953e-10 | 2.7372e-18 |
| Haswell yx | 1.1875e-16 | 7.6598e-16 | 2.7559e-10 | 2.7289e-18 |
| Haswell alt | 1.1356e-16 | 7.0055e-16 | 1.3022e-12 | 2.7278e-18 |
| Nehalem xy | 1.1764e-16 | 8.1344e-16 | 2.2543e-10 | 2.7256e-18 |
| Nehalem yx | 1.2017e-16 | 8.0984e-16 | 3.2401e-10 | 2.7517e-18 |
| Nehalem alt | 9.3890e-17 | 7.4014e-16 | 3.0241e-12 | 2.7506e-18 |

The maximum local residuals are 0.846–1.083 times binary64 unit roundoff.
Their normal responses divided by ||F||_F range about 2.77e5–9.98e5 for upstream
and 1.86e3–4.08e3 for alt. The longdouble inverse alone has normal reconstruction
errors as large as `2.76e-13`; the receipt retains these rather than hiding
that cancellation limitation. The independent 50-digit frozen solve removes
that ambiguity to the approximately `3e-18` reference/projection floor.

Changing only the dispatched kernel changes the computed spans by
`7.4668e-10` (xy), `4.2171e-10` (yx), and `2.7641e-12` (alt).
The actual Q and H bytes differ, with maximum H-entry changes `4.7911e-11`,
`2.5057e-11`, and `2.6453e-13`. These are observed recurrence changes, rather
than variation in a fixed-Q diagnostic. Alt's unprojected surrogate error is
`5.3851e-12`/`1.2414e-11` in the two kernels; its actual normal response remains
the smaller values in the table. A loose unprojected scale is not evidence
that the historical normal response has been reconstructed.

## Supported explanation and remaining limit

The current discrepancy class is supported by measured u-scale local rounding
sources, amplification by the inherited frozen recurrence that reconstructs
its true normal error, a controlled kernel-dependent change in Q/H and span,
and substantial error reduction with higher precision. The reference-noise
hypothesis is quantitatively inadequate for xy/yx/alt. The old frozen values
and current values have the scales expected from this arithmetic-sensitive
recurrence, but the historical Q/H, dispatch and library binary pins were not
preserved. In particular no tested kernel reproduces the old alt value
`7.3010e-12`; no claim about its exact historical residual realization is made.
These observations explain an arithmetic-sensitivity class without recovering
the old trajectory. They do not prove a universal error bound or equality of
historical/fresh runs, waive a tolerance, or issue a G0 PASS. The original dated
FAIL record and the orchestrator's separate G0 decision remain distinct.
