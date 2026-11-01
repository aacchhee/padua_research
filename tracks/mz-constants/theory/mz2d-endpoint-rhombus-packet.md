# PD-N?mz2d-codex-22 — A bounded rotated harmonic-packet test does not improve the endpoint witness

ID kind: PD-N.
Aliases: symmetrized sum-difference U packet; rhombus harmonic product.
Split from: IDEA?mz2d-codex-23, one explicitly specified packet only.
Split into: none.

## Statement

For m=8,16,32,64,128, the packet defined below has measured signed Padua
Rayleigh quotient, respectively,

\[
 .881698207223,quad .888410221049,quad .904919467088,
 \quad .923866185781,quad .941961054455.                    \tag{1}
\]

It fails the bounded screening aim of producing a quotient tending
downward or improving the known coordinate harmonic witness in these
tests. The claim is only the recorded finite observation and resulting
stopping disposition. No all-m limit or impossibility theorem is claimed.

## Definitions and assumptions

Write the exact PD-T018 witness in cosine coefficients
`p_m(cos t)=sum_r a_r cos(rt)`; only frequencies r of parity m-1 occur.
For x=cos(theta), y=cos(phi), define

\[
 F_m(x,y)=p_m\bigl(\cos((\theta+\phi)/2)\bigr)
          p_m\bigl(\cos((\theta-\phi)/2)\bigr).             \tag{2}
\]

This is an actual real algebraic polynomial in `Pi_(m-1)`.
Indeed its Cartesian Chebyshev coefficient matrix is given exactly by
adding, for each ordered pair r,s with nonzero a_r,a_s,

\[
 C_{(r+s)/2,\,|r-s|/2}\mathrel{+}=a_ra_s/2,\qquad
 C_{|r-s|/2,\,(r+s)/2}\mathrel{+}=a_ra_s/2.                 \tag{3}
\]

The indices are integers of nonnegative total degree `max(r,s)<=m-1`.
To verify (3), apply cosine product-to-sum in (2), then pair the
ordered summands (r,s) and (s,r); their sine products cancel. The r=s
and zero-frequency cases are included by the two additions, including
when both locations coincide. Thus degree and separate angular-evenness
were checked before interpreting any quotient.

## Status and disposition

Overall status: **MEASURED**. Polynomial admissibility above is a routine
exact check of this measured candidate, not a separate all-m spectral
result. IDEA?mz2d-codex-23 is **REJECTED: failed** for the stated packet's
bounded improvement screen at precisely the five m values in (1).

## Negative-result scope

Attempted mechanism: multiply the same critical harmonic packet in the
two rotated angles, using its same-parity Fourier support to retain the
total-degree cutoff. Scope: (2), these five construction degrees, float64
computation. It excludes no different coefficients, symmetrization,
asymptotic argument, or signed rhombus witness.

## Depends on

PD-T018 witness definition. The accepted PD-T101 rhombus change of
variables motivated the support test but no A2 claim is assumed. Actual
signed weights are assembled by `mz2d_spectra.padua_weights`, whose
normalization is separately fixed by D1/definitions.

## Checks and reproducibility

Executed 2026-11-01 from `/workspace/padua_research`, Python3.12.14,
NumPy2.3.5, SciPy1.17.0, deterministic with no random seed. The command
was an inline `python` script with these complete mathematical operations:

1. For each listed m, set `M=(m-1)//2`; initialize the U coefficient
   vector u by `u[m-1-2k]+=1/k` and
   `u[m-1]-=(1-2k/m)/k`, k=1,...,M.
2. Convert U to Chebyshev cosine coefficients by
   `a[r]=2*sum(u[r::2])` and divide `a[0]` by two.
3. Assemble C by (3), asserting zero coefficients above total degree m-1.
4. Evaluate `Vx @ C @ Vy.T` at the actual Padua coordinate grids and
   sum `w*values**2` using `padua_weights(m)`.
5. Evaluate the same C on an m-point Gauss-Legendre grid in each
   coordinate and sum the positive tensor Gauss weights times F squared.
   In exact arithmetic that quadrature integrates this polynomial square
   exactly; in this execution its nodes, weights and sums are float64.
6. Divide the signed sample sum by that continuous-norm measurement.

| m | signed sample sum | continuous squared norm | quotient |
|---:|---:|---:|---:|
|8|37.99260435038215|43.090259273680786|0.8816982072230825|
|16|262.69051753434|295.68605955955746|0.888410221048749|
|32|1225.7344908664259|1354.5232868194691|0.9049194670876055|
|64|4615.460778800926|4995.810919196065|0.9238661857810373|
|128|15153.286796665727|16086.9568067588|0.9419610544549483|

The original command exited zero; the exact operation list above makes
the run reconstructible without a generated binary artifact. There is
no independent execution receipt yet and no rigorous enclosure claim.
The producer's source SHA256 is recorded in the D3 direction file.

## Sources, scope and open items

Complete gate and predecessor comparison: D3 direction/candidate files.
No rate, exact eigenvalue, global rhombus obstruction or historical
novelty claim follows from the five quotients. A genuinely different
packet would need a fresh gate/separation test. This bounded candidate
is stopped; PD-T028 positivity and endpoint order remain OPEN.

## History

2026-11-01, Codex D3 developer, requested gpt-6.1-sol xhigh; rules
`806cc7b4509fd93bae652f9545d32d95529f8281`. Third bounded round after
D1 PASS. Failed candidate retained rather than silently discarded.
