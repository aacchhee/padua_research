# Supplementary independent check — S3 compact corner operator

Date: 2026-11-06. Separate Codex mathematical checker; requested
gpt-6-astra high, runtime model metadata not independently exposed.
Rules/source: `2143ad622fa98faf8fe7d5cb8ed2bb7e0062f861`.
Required Claude audit remains separate.

Initial complete integration reviewed: `theory/S3-corner-operator-limit.md`,
SHA-256 `1d604614365c2c61b606145b0de4d95456d641ecdcb6343970094bf464c3e9a1`.

**Mathematical verdict: no substantive gap found.** The finite-corner
tail, fixed compact signed operator, complete extremal convergence,
agreement of the two parities, and stated explicit comparison constants
follow from the written arguments. One routine clarification was
requested to make the zero-eigenvalue dimension argument explicitly
cover every m in the finite bound, rather than only sufficiently large m;
its final disposition is recorded below.

## Scope and dependencies

This check concerns mathematical validity and dependency direction.
It makes no novelty, priority or literature claim and accordingly uses
the workflow exception to a full ideas-registry review. No final S4 fits
were read. The approximate model decimals in the source are not verified
or used here.

The same independent checker previously reconstructed the full-grid
form reduction and the kernel lemma. The dependency identities are:

- S3-02, `theory/S3-full-form-log-model.md`, original audited SHA-256
  `3e1a9a0c8fc7c6878ebe2607d2a3ad491a5147ab1e2de51f2ce30e363ccc60d1`,
  with verified editorial update
  `8c991ebc077b8f27edaf9baf887c076db7737903f859d5a8de286734d53a2a77`;
  see [full-grid check](independent-checks-S3-model.md).
- S3-kernel, `theory/S3-corner-kernel-hard.md`, audited SHA-256
  `0200a23f0262418fe12cf1458bfbbc11bcb85018dce488a913fc58eae3bd326a`;
  see [kernel check](independent-checks-S3-kernel.md).
- PD-T379's accepted strictly signed carrier bounds, with the improved
  negative coefficient supplied by separately checked S3-01. The older
  PD-T379 bounds alone suffice for strict signs; neither carrier result
  is used to prove convergence or identify the fixed operator.

## Analytic reconstruction

1. **The uniform tail is an absolute form bound.** For D_jk>K,
   alpha_j beta_k>=D_jk/(m^2 M^2) implies
   p(node)^2<=m^2 M^2 alpha_j beta_k p(node)^2/K.
   The absolute L_m coefficient is <=4 epsilon_j eta_k/(m M R^2).
   Summing the nonnegative majorant and using the tensor CC bound gives
   16mM/(K R^2)<=120/K. This applies to any subset of the tail,
   in particular one corner and any finite shell. It is not an estimate
   that drops an uncontrolled cancellation from the signed form.
   For a selfadjoint finite-dimensional form its uniform absolute
   Rayleigh bound is precisely an operator-norm bound.

2. **Corner indexing and coefficient limits.** If m>=2K then every
   local index is <=K-1, strictly below half either mesh, so four patches
   are disjoint and all nodes with D_jk<=K appear exactly once.
   Reflection changes retained parity by m delta_x+M delta_y because
   subtraction and addition agree modulo two. Since 2R is even,
   reflection changes neither cosine. Consequently the two active
   corners use r+s even and coefficient -16e_r e_s(-1)^r; the other
   two use r+s odd and have limiting coefficient zero. On even m the
   active corners are (1,1),(-1,1), and on odd m they are (1,1),(1,-1).
   No axis interchange is needed to get the same limiting H-space and
   functions. There are exactly two copies of each parity subset of
   I_K, hence exactly N_K=2|I_K| retained nodes, including endpoints.

3. **Coefficient constants.** Multiplying the L_m nodal coefficient
   by m^4 gives q_m=2m^3/(M R^2), with no missing normalization factor.
   For even m, |q_m-8|=8/(m+1)<=16/m. For odd m>=5 its asserted
   bound reduces exactly to m^3-3m^2-m+2>=0, which is positive there.
   The x and y phase errors are respectively <=pi r/m and <=2pi s/m.
   Expand q_m times the actual cosine sum around 8 times the limiting
   sum: the former sum has modulus <=2. Thus the coefficient error is
   <=[32+8pi(r+2s)]/m<=[32+24pi K]/m. The calculation applies also
   when the limiting sum is zero and preserves endpoint halfweights.

4. **Scaled evaluation vectors and Gram convergence.** With
   v_z=m^(-2)K_(m-1)(.,z), one has <p,v_z>=m^(-2)p(z), so
   gamma_z|v_z><v_z| gives exactly the original L_m nodal term.
   The kernel lemma applies with angular coordinates pi r, pi s,
   mesh shifts 0,1 and endpoint signs. All coordinates are <=U.
   Its entrywise error C_U/m implies operator-norm error <=N_K C_U/m.
   The limit Gram matrix has four mutually orthogonal corner blocks,
   each the Gram matrix of the indicated functions in
   H=L2(D,ab da db). This identifies a fixed model, rather than a
   renamed finite Padua matrix. Inactive coefficients tend to zero;
   their nonzero Gram blocks do not generate spurious leading spectra.

5. **Signed finite-Gram transfer.** If V*V=G, the polar decomposition
   V=W G^(1/2) makes VCV* isometric on its nonzero spectral subspace
   to G^(1/2) C G^(1/2), with zeros appended. This is valid for every
   real symmetric C, including the signed diagonal here, and for singular
   G. The latter matrix vanishes on ker G, which handles possible
   linear dependencies among feature vectors. Continuous dependence
   of the positive matrix square root and the coefficients then gives
   convergence of all extrema after zero is included. Each active block
   has B_K's extremes; a direct sum duplicates these eigenvalues but
   does not multiply them by two. The inactive blocks only add zeros.

6. **Compactness has no circular premise.** Fix K'>K and use only
   the finite one-corner shell. The already proved absolute tail bound
   controls that finite-dimensional form for every large m. Its finite
   Gram limit identifies B_(K')-B_K and transfers the norm bound120/K.
   This step uses neither existence of B nor convergence of a Padua
   extremum. It proves the B_K sequence is norm-Cauchy, constructs its
   bounded selfadjoint limit B, and gives ||B-B_K||<=120/K. A norm limit
   of these finite-rank operators is compact; the diagonal subsequence
   argument supplied in the proof justifies this without a series
   rearrangement. The product truncation convention is therefore
   mathematically meaningful even without absolute summability of
   individual rank-one operator norms.

7. **Full spectrum and parity.** Variational extrema change by at most
   an operator-norm perturbation. Combining the finite-model transfer
   with the two truncation errors gives limsup|nu_sign(m)-c_sign|
   <=240/K. Both parity subsequences have the same finite-block extremes,
   so letting K increase proves all-integer convergence. S3-02 then
   transfers this to lambda_sign/log m. Only after this conclusion are
   the inherited negative and positive carriers used to show
   c_minus<0<c_plus. No fitted value or predicted sign is an input to
   the convergence proof. The constants are exact spectral values of
   the displayed fixed compact operator; no closed-form scalar or
   certified decimal evaluation follows.

8. **Explicit finite error.** The exact corner kernel sum is
   m(m+1)(m^2+m+1)/24. After division by m^4 it is <1/8 for m>=4;
   |P_l|<=1 bounds every finite Gram entry by this number. The limiting
   entries are <=integral_D ab=1/24. Hence both Gram norms are <=N_K/8.
   For positive matrices, the displayed square-root resolvent integral
   is valid also at zero eigenvalues. Two positive contractions have
   difference bounded in norm by one. The resolvent identity gives the
   alternative delta/t bound. Integrating min(t^(-1/2),delta t^(-3/2))
   on the two sides of delta yields (4/pi)sqrt(delta)<=2sqrt(delta).
   Telescoping the coefficient and square-root errors therefore gives
   N_K beta_K(m)/8+(64/sqrt(8))N_K sqrt(C_U/m), which is bounded by
   the stated E_K(m), since 64/sqrt(8)<24. Adding the two120/K tails
   and4300/log m proves the claimed modulus on its dimension-valid range.

## Routine clarification and disposition

The original §3 justified appended zero eigenvalues only for
"all sufficiently large m", while §5 claims the finite estimate for
every m>=max(4,2K). The required bound is immediate:
I_K is contained in {0,...,K-1}^2, hence
N_K<=2K^2< K(2K+1)<=m(m+1)/2=dim Pi_(m-1) for m>=2K.
Thus the statement's full range is valid. The developer agreed to
include this explicit dimension bound; it does not alter the theorem,
constants, dependencies, or limiting argument.

The developer added precisely this dimension clarification. The updated
theorem SHA-256 is
`94245edd52b601778d386d671a689b667abae9cbedd6481c9ab5a9112f883a83`.
The checker read the amended paragraph and reversed only that change
in memory, recovering the original frozen SHA-256 exactly. **Disposition:
clarification verified; no unresolved mathematical finding.** The complete
mathematical verdict applies to this updated file.

## Execution and residual limits

This is an independent analytic reconstruction. No numerical run is
claimed as verification of the operator limit, and no numerical premise
occurs in the proof. A separate finite-model replay is recorded below.
The source's coarse bounds permit successive
fixed-K then m limits and supply the stated explicit modulus; they do
not certify its model decimal predictions or a practical onset degree.
Whether an exact compact-operator characterization satisfies the
campaign's requested format for "determine their values" is a scope
decision for the coordinator and AC, distinct from mathematical validity.

## Separate measured finite-model replay

After the proof check, the coordinator requested an independent rerun of
the finite-model proxies. The checker read the complete producer and
executed, from `/workspace/sharp-work`:

```text
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-mz-sharp-constants-20261106/code/S3_corner_model.py --orders 128 192 --cuts 16 32 64 128 --output topics/padua-mz-sharp-constants-20261106/evidence/check-S3-corner-model.json
```

Producer SHA-256:
`dc4c5f0c4d935d065ea3409d234c2727890a3ddcb10cdaf59c397127bda03b20`.
Environment: Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0; deterministic,
no seed, both listed thread limits equal one. The producer constructs
the triangle Gram integral by b=(1-a)s with weight a(1-a)^2s, then
forms the symmetric signed matrix using Gram eigenvectors and square
roots. Its index set and coefficients agree with B_K. No numerical
nullspace was discarded in these runs: retained rank equals node count
at all four cuts and both orders.

Receipt: [check-S3-corner-model.json](evidence/check-S3-corner-model.json).
All sixteen extremal values reproduce the developer's receipt exactly
in this environment. The largest change between quadrature orders128
and192 is 2.55351295663786e-15. At K=128 and order192 the observed
values are -0.13358000211999999 and0.045598319570321344. These are
MEASURED finite-model proxies, not certified limiting constants.

The minimum Gram eigenvalue at K=128 differs materially between the
two orders, although the extremal signed values are stable; this replay
does not establish full Gram-matrix quadrature accuracy. The rigorous
infinite-operator tail bound there is still120/128=0.9375. The producer's
current preregistration-prose hash differs from its historical receipt
following documentation updates; the code hash and mathematical numeric
inputs match. This replay neither reaudits that chronology nor treats
the changed prose as a numerical input or proof premise.
