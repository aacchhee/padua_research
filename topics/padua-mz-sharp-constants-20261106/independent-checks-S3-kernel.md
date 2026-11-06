# Supplementary independent check — S3 Legendre corner kernel

Date: 2026-11-06. Separate Codex supplementary mathematical checker;
requested gpt-6-astra high, runtime model metadata not independently
exposed. Rules/source: `2143ad622fa98faf8fe7d5cb8ed2bb7e0062f861`.
Required Claude audit remains separate.

Reviewed full file: `theory/S3-corner-kernel-hard.md`, SHA-256
`0200a23f0262418fe12cf1458bfbbc11bcb85018dce488a913fc58eae3bd326a`.
The hash was checked against the actual file after reconstruction.

**Verdict: no unresolved mathematical finding in the frozen kernel
lemma.** The estimate is uniform for every m>=1 and all four angular
coordinates in a stated bounded cube, includes the m+1 mesh shifts,
and covers every distinct reflected-corner pair. This check does not
approve a later infinite-operator or spectral-limit theorem.

## Scope and dependencies

This is a mathematical-validity audit, without novelty, priority or
literature claims; the workflow exception to full ideas-registry review
therefore applies. The kernel proof is self-contained from Rodrigues'
formula and elementary integrals. Prior accepted Padua weight results
and the S3 form reduction are applications, not premises of this
kernel lemma. No measured fit, spectral limit, Mehler--Heine theorem,
or externally quoted Bessel asymptotic is used.

## Independent reconstruction

1. **Normalization and integral representations.** Integrating the
   Rodrigues formula by parts k times gives orthogonality and the
   displayed norm 2/(2k+1); the leading-coefficient argument is valid
   also for k=0. Tensor products with k+l<=m-1 therefore give the
   correct unnormalized-dxdy kernel weights (k+1/2)(l+1/2).
   The explicit coefficient formula agrees with the binomial expansion
   of (1-2xz+z^2)^(-1/2). Averaging a geometric series is justified
   for sufficiently small |z|, and its even moments give the claimed
   square root with the branch taking value one at z=0. Coefficient
   comparison yields the Legendre integral. Changing the sign of sin(t)
   leaves the average unchanged, so the representation holds for all
   real t. Averaging the exponential series similarly gives exactly
   the stated J0 power series. Both integrands have modulus at most
   one on their real domains; differentiation gives |J0'|<=1.

2. **Legendre/Bessel error, including zero degree.** Centering the
   two-point variable X at its mean c cancels its linear Taylor term.
   The integral remainder for exp(iy) has absolute value <=y^2/2,
   yielding the variance factor 1-c^2. Factoring the kth-power
   difference costs at most k because both bases have modulus <=1.
   Averaging 1-cos(phi)^2 contributes exactly 1/2, hence kt^2/4.
   At k=0 the error is zero. No estimate involving division by k or
   a positive lower degree fraction occurs. The argument shift costs
   ku eta/[m(m+eta)], which with k<=m gives precisely the bound
   (u^2/4+eta u)/m. This covers both m and m+1 meshes.

3. **Weighted triangular sum.** Reflection contributes exactly
   (-1)^(epsilon k+delta l) by Legendre parity. Four-factor telescoping
   gives A/m, with no missing factor from real versus complex values.
   On k+l<=m-1 the normalized two weight factors have sum <=1, so
   their product is <=1/4. There are m(m+1)/2<=m^2 terms, including
   m=1. Also the weight replacement error satisfies the slightly
   stronger inequality
   (a+b)/(2m)+1/(4m^2)<=1/(2m)-1/(4m^2)<=1/(2m).
   Thus the total normalized product/weight error is bounded by
   (A/4+1/2)/m, regardless of alternating signs and including zero
   coordinate-degree rows.

4. **Triangle quadrature and boundary.** Every point of the unit
   triangle belongs, up to boundaries of measure zero, to an included
   lower-left grid cell. Exactly m boundary cells contain an exterior
   half-triangle, each of area 1/(2m^2). Hence the excess area is
   exactly 1/(2m), not an unaccounted full boundary strip. On the full
   square the derivative bounds 1+u+u' and 1+v+v' hold by product
   differentiation and |J0|,|J0'|<=1. The coordinate displacement
   within a cell is <=1/m; the union's area is <=1. Its quadrature
   error is therefore <=(2+S)/m. Adding excess area gives
   (5/2+S)/m. Combining with the previous step gives exactly
   (3+S+A/4)/m for equal corners.

5. **Different corners.** If the x endpoints differ, pair successive
   k-values within each fixed-l row. Each complete pair is bounded by
   (1+u+u')/m; at most one terminal term of modulus <=1 is left.
   The deliberately loose count of at most m pairs bounds each row
   by 2+u+u'. There are exactly m rows. Multiplication by an
   alternating row sign does not change this estimate, so reflection
   in both coordinates is covered directly. When only y differs,
   pair within columns instead. The resulting bound plus the product
   replacement error is no larger than the stated C/m. This proves
   decoupling without an assumption about oscillatory cancellation
   beyond the explicitly paired differences.

6. **Constants and origin.** On [0,U]^4, S<=4U and
   A<=U^2+4U for arbitrary allowed shifts, giving
   C_U=3+5U+U^2/4. For Padua's two y-shifts and zero x-shifts,
   A<=U^2+2U, giving 3+(9/2)U+U^2/4. The triangle integral of ab
   is 1/24, confirming the normalization. Neither corner multiplicity
   nor checkerboard density is built into this kernel: those belong
   to the subsequent signed-form construction and must be checked
   there separately.

## Execution and limitations

The independent check above is analytic. No numerical execution,
spectral fit, or finite arithmetic test is claimed or needed as a proof
premise; the tool execution read the frozen file and checked its hash.
The bound grows quadratically with the coordinate cutoff U. It supplies
finite-coordinate Gram convergence and reflected-corner decoupling,
not uniform control of all unbounded indices. A later operator theorem
still needs an independent uniform tail bound, a justified signed
finite-Gram passage, and a spectral perturbation argument.
