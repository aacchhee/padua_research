# Supplementary independent mathematical checks 01

Rules/input: `8a1f394739293953e1566fd24a0a193cc78ff26f`.
Codex, configured gpt-6-astra high; runtime internals are not independently exposed.
2026-11-03. Narrow analytic reconstruction, not novelty/priority audit and
**not the required Claude audit**. All acceptances below are within their
explicit scopes and inherited dependencies.

## Exact degree-four sign obstruction (supplementary analytic review)

Independently reconstructed the n=4 PD-T101 kernel using standard-library
`Fraction` arithmetic and the recurrence T0=1,T1=x,Tj=2xT(j-1)-T(j-2),
without loading the comparison worker's polynomial output. The (0,0)
node is (1,1), its weight is 1/40, and the exceptional (4,0) mode has
coefficient one. At y=0 the cardinal's power coefficients are exactly
`[1/10,-1/5,-3/10,1/5,1/5]`. Thus

```text
L00(x,0) = (x²-1)(2x²+2x-1)/10,
L00(1/3,0) = 4/405 > 0,
L00(3/8,0) = -11/4096 < 0.
```

Read and checked the complete theorem
`theory/argmax-effective-codex-04-coarse-cell-sign-obstruction.md`.
For its specified D(2,3), y=0 gives qy=5/2. The exact inequality
3/8<sin(pi/8) is equivalent to sqrt(2)<23/16, proved by
512<529 after squaring positive sides. Consequently 3/2<qx<2 for
both witnesses and |qx-2|+|qy-3|<1 strictly. A fixed sign times two
nonnegative finite factors cannot take these opposite signs.

**Finding: the stated fixed-sign individual-cardinal obstruction is
correct.** It refutes only the explicitly quantified G7-F representation.
It does not establish nonexistence in an unspecified envelope class,
kill the whole IDEA-319 route, or bear on the all-degree argmax claim.
The complete analytic evidence is displayed here and in the theorem;
the scratch diagnostic is `n4-cardinal-exact.json`. No bulk artifact
is required to reconstruct this elementary proof. Claude audit remains
pending independently of this supplementary acceptance.

## Exact corner spectrum and all-degree slopes: supplementary acceptance

Independently reviewed the full analytic proofs in
`theory/argmax-effective-codex-06-corner-active-spectrum.md` (06a) and
`theory/argmax-effective-codex-06-uniform-slopes-local-radius.md` (06b),
including their new normalized y-slope extension. **Accepted at their
stated scope**, subject to inherited PD-T101/227, not a new audit of those
entire predecessor topics. No finite numerical reconstruction is used as
a premise of this acceptance.

Reconstructed the reflected odd-board signs from the original indices:
the exceptions at r=m are exactly the zero cardinals and the original
00 cardinal. Summing each parity cosine row gives the stated H_j(b),
including the half endpoint. With A=n-a, the removed j=n endpoint adds
epsilon/2 to the outer transform; A=n contributes the additional
-epsilon*n/2 term, and A=0 gives 1/2 before multiplication by 2/N.
These reproduce the full coefficient formula, including C_0b and C_n0.
Positivity uses a*pi/n+b*pi/(n+1)<pi; sine concavity proves the diagonal
bound. The row-pair interpolation and column-average arguments correctly
retain the endpoint exception for even n. As an exact n=2 boundary
check, the rows are C_00=-1/6,C_01=C_02=2/3;
C_10=1/3,C_11=4/3; C_20=1/6. They sum to Lambda_c=3 and give
A_2=-7/3, B_2=-14/3.

For the strengthened y slope, independently reconstructed the reduced
odd-grid endpoint cardinal when n is even:
`[1+2 sum_(b=1)^(n/2) (-1)^b cos(b eta)]/m`.
Its coefficient differences give
`D_b-D_(m-b)=4(-1)^(b+1)/m`, with the plus sign as written.
The asymmetry contributes
`(2/m) sum_(b=1)^n (-1)^(b+1)b^2=-n`.
Combining D_0=1-2/m yields
`-B_n>=m^2(Lambda_c-1)/4-(n-1)/2`; odd n has no correction.
The lower bound Lambda_c>=2 then proves both
`A_n,B_n<=-n^2 Lambda_c/8`. For even n the y-bound surplus after
subtraction is at least 3/4, so the endpoint degrees cause no gap.

For the explicit radius, independently checked the kernel coefficient
sum 2N and the nonzero-cardinal bound |l_B|>=2w_B/m^2, including 00.
The gradient estimate 2w_B*N*n^2 and H<=1/(2N^3) preserve the signs of
the **affine** values l_B+g_B.h. They do not assume true cardinal sign
stability. The summed higher derivatives are at most
2N*n^(2r+2s); the resulting Taylor remainder is at most
e*N*n^4*H^2<=n^2*H/6. Combining it with both slopes at most -n^2/3
proves the stated strict decrease on this physical radius.

The normalized slope premise formerly open in PD-T227 is closed by this
argument. The weighted-energy premise, the fixed rho<=1/64 neighborhood,
effective global localization and the all-degree maximum remain open.
The radius is of order n^-6, not n^-2. Minor wording findings were sent
to development: remove an abandoned n=2 estimate saying 1/3 exceeds
1/m, and express the inward derivative as d[cos(a xi)]/dx=-a^2 rather
than the literal derivative of T_a(-cos xi). Neither affects the
reconstructed formulas. Both wording findings are resolved in the final source hashes below.

## R5 algebra review

Read `attempts/r1-r2-r5.md`, SHA-256
`f268f9b663ce278a5768448c9a6dae1d0ca6618e2dd475d804accabcb24b7ea3`.
The stated equivalence is correct: at a fixed Bernstein index,
`max_(epsilon in {+-1}^M) sum_l epsilon_l c_li = sum_l |c_li|`.
Both universal quantifiers are finite, so requiring the coefficientwise
test for every sign vector at every index is exactly the existing
absolute-coefficient test, including its strict version. This confirms
only the specified full-sign-family test's **equivalent** disposition;
it does not reject other positivity representations or the entire R5
route. No new negative theorem follows from this reformulation.

## Reviewed final source identities

- 06 corner-active spectrum: `76468d2ea6005f16a9430ed4acd41234a86bec9f96960e953a3523e7a32b5658`.
- 06 normalized slopes and local radius: `c545111c04cf4526c18e6b6020f8c26915cbe25df83f63e6fe579b415d4732f9`.
- 04 coarse-cell sign obstruction: `335288d1ae05aacf779e23940dfc802c7fc47f1c9efc1a0e4c481f0816738365`.

Hashes identify reviewed mathematical content before administrative IDs or
review-status edits; any substantive subsequent change needs impact review.

## Two scoped R6 negative statements

Independently checked `theory/argmax-effective-codex-06-negative-spectrum.md`,
hash `458d0d79486a1ab2dce45fcf123bcbdb23595df3f72eb7d426ce0c6ec7642925`.
Substitution n=3,b=1 into the proven a=0 coefficient formula gives
`[2/(1+sqrt(2)/2)-3]/6=(1-2sqrt(2))/6<0` exactly. This refutes the
specified nonnegative nonconstant spectrum, with mixed/aggregated
positivity explicitly retained. **Accepted at this scope.**

Independently checked `theory/argmax-effective-codex-06-affine-sign-obstruction.md`,
final hash `ccda306823572d126c4e712f9fdca0f9bec037d350dfb74c73c636690b319e48`.
For the admissible (3,1) cardinal, n²C→pi²/2, n²d→4pi² and
n²(ab-1)→-5pi². Dividing the PD-T227 gradient/value formula by n³,
its n*(ab-1)/(Cd) term tends to -5/(2pi²) and the other three terms
vanish. Hence 1+kappa*q_n/n²→-infinity for fixed positive kappa.
The stated eventual affine sign reversal and radius asymptotic follow.
**Accepted at this scope:** a failure of uniform termwise affine sign
preservation, not a proof about the sign of the true cardinal including
its Taylor remainder. The development text now explicitly says the
radius bound is for sufficiently large n. No counterexample to actual
local maximality or to aggregate/weighted-energy methods is asserted.

## Administrative review labels

The mathematical worker subsequently made review-status/link
updates, with current hashes: spectrum
`8e6fa98c4ed820c575a6e2053e620272a364caa35bf0d91b7e7129dd19b5f6ed`,
slopes/radius `83499891b742f44c5b78283f16e94a023765f72188ef8cdddb366008d7c11201`,
negative spectrum `60502d05eb9397a946bace8dd1720072faa1624db19c4dc9c74cb294110a294a`,
affine obstruction `7e7f0963879cc1b72977166a407d8038c9e23adaf1891db3d9f61a5f64c9e33a`.
Independently inspected these exact substitutions and reversed only the
declared status/checks prose in memory. The reconstructed bytes hash
exactly to all four previously reviewed versions above; the executed
receipt is `math-admin-impact.json`. Thus the mathematical content is
unchanged and **acceptance extends to these current hashes**. This does
not represent a Claude audit.

## Three exact edge spots: reduction inspection only

Read the complete `theory/argmax-effective-codex-03-exact-edge-spots.md`.
Its enlarged physical source interval, exact affine power-to-Bernstein
conversion, complete 2/2/3-leaf covers and target-center lower bounds
correctly imply the three stated strict whole-cell comparisons. Each
chosen target center is in the specified centerward cell. Independently
executed integer comparisons on the displayed margins: multiplying by
20,40,100 respectively exceeds 2^192 in every case. No all-degree or
cell-maximizer-location conclusion follows. This was a proof/reduction
inspection and tiny integer check; **this worker did not rerun the edge
checker**. The separate comparison mathematics worker's actual replay
and controls provide that independent execution, as the theorem states.
