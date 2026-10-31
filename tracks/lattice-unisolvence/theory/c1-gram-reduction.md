# PD-T?lattice-c1-codex-04 — Antipodal-transversal Gram reduction and explicit character moments

ID kind: PD-T. Aliases: quarter-character cross block; strict-contraction reduction.
Split from: none. Split into: unresolved family theorem PD-T?lattice-c1-codex-05; measured block diagnostics PD-T?lattice-c1-codex-06.

## Statement

Use Chebyshev–Lobatto axes `x_i=cos(pi*i/n)`, `y_j=cos(pi*j/(n+1))`, with either (A) odd n>=1, phasep=0, or (B) even n>=2, phasep=1. Select the adjacent mod4 union `i+j-p mod4 in{0,1}`. Let N=binom(n+2,2). Normalize the tensor Chebyshev total-degree basis to be orthonormal on the **full** product Lobatto grid with the product trapezoidal probability weights W. Partition this basis into even and odd total degrees. Then the selected-node Gram matrix is

`G = (1/2)*[[I_e,A],[A^T,I_o]]`,

where A is given explicitly by the one-axis finite moments below, and `||A||_2<=1`. The selected N nodes are unisolvent exactly when `sigma=||A||_2<1`. Equivalently `det(I_o-A^T*A)>0`; moreover

`det(V)^2 * product_(selected s) W_s = 2^(-N)*det(I_o-A^T*A)`.

If sigma<1, their Lebesgue function satisfies

`Lambda(z)<=||phi(z)||_2/sqrt(1-sigma)<=2*sqrt(N)/sqrt(1-sigma)`, for z in[-1,1]^2.

This is a proved structural reduction, **not a proof that sigma<1 for every degree**, nor a polylogarithmic stability bound. Even a uniform strict gap in this elementary bound would leave an O(n) factor; a useful logarithmic estimate needs additional kernel structure.

## Definitions and assumptions

All arithmetic here is over R or C. On a lengthM+1 Lobatto axis, `nu_j=c_j/M`, c0=cM=1/2, otherc=1. Let h_M(a)=1 if a=0 or a=M, and1/2 otherwise, for0<=a<=M. Put `psi_a^(M)(cos theta)=cos(a*theta)/sqrt(h_M(a))`. The full product basis is `phi_(a,b)(x,y)=psi_a^(n)(x)*psi_b^(n+1)(y)`, a+b<=n. The matrix V evaluates this basis on the selected nodes; W_s=nu_i^(n)*nu_j^(n+1). e/o are its numbers of even/odd total-degree modes.

Define the complex axis moments

`Z_M(a,c)=sum_(j=0)^M nu_j * i^j * psi_a^(M)(cos(pi*j/M))*psi_c^(M)(cos(pi*j/M))`.

Then, for an even mode(a,b) and odd mode(c,d),

`A_((a,b),(c,d))=Re[(1-i)*i^(-p)*Z_n(a,c)*Z_(n+1)(b,d)]`.

Explicit scalar formulas: let `S_M(r)=(1+r)*(1-r^M)/(2*(1-r))` if r!=1, and S_M(1)=M. Define

`C_M(t)=(S_M(i*exp(i*pi*t/M))+S_M(i*exp(-i*pi*t/M)))/(2*M)`.

Then `Z_M(a,c)=(C_M(a-c)+C_M(a+c))/(2*sqrt(h_M(a)*h_M(c)))`. At resonance use the stated r=1 branch, not division by zero. These are finite identities, with no convergence issue.

## Status by part

Overall status PROVED (developer complete algebraic/trigonometric proof; independent Astra reconstruction pending). This statement stops at an equivalent finite cross-block criterion and a conditional bound with the explicit assumption sigma<1. The universal strictness/polylogarithmic target is a **separate OPEN statement**, not an unproved conjunct here.

## Depends on

Elementary cosine sums, positive Gram matrices, Cauchy–Schwarz and Schur complements; count PD-T?lattice-c1-codex-02 for the square selected matrix. No charter/literature theorem inherited.

## Proof

The weighted cosine sum `sum_j nu_j*cos(k*pi*j/M)` is0for0<k<2M and1at k0or2M. This follows by summing geometric progressions and taking real parts (or pairing j with M-j). Combining it with cosu*cosv=(cos(u-v)+cos(u+v))/2 proves one-axis orthogonality with norms h_M(a), including endpoints. Therefore the full tensor matrix U satisfies U^T*W*U=I on the total-degree subset.

For integer r the real number `g_p(r)=Re[(1-i)*i^(r-p)]` is+1exactly when r-p mod4 is0or1, and-1otherwise. Thus `G=U^T*W*diag((1+g)/2)*U=(I+H)/2`, where `H=U^T*W*diag(g)*U`. H is real symmetric. Its norm is<=1because W^(1/2)U has orthonormal columns and diag(g) is an orthogonal sign matrix.

Central inversion of the full grid sends sum residue r to2n+1-r and preserves W. In caseA, 2n+1≡3mod4; phase0is sent to phase2, its complement. In caseB, 2n+1≡1mod4for every even n; phase1is sent to phase3, its complement. Hence g changes sign. A basis mode changes sign by(-1)^(a+b). Every H entry between modes of the same total-degree parity is therefore its negative, so is0over R. H has the off-diagonal block form `[[0,A],[A^T,0]]`; its defining sum factors by axes to give the displayed A formula. Its norm is exactly ||A||_2.

The Gram is positive semidefinite. Its eigenvalues are(1±singularvalue(A))/2, with any remaining unpaired eigenvalues1/2. Since selected cardinality is N and weights are positive, G is positive definite exactly when V is invertible. With ||A||<=1this is equivalent to sigma<1. The block Schur complement gives detG=2^(-N)*det(I_o-A^T*A). Also detG=det(V)^2*productW_s, proving the identity.

For sigma<1, the cardinal vector satisfies `ell_s(z)=W_s*phi(s)^T*G^(-1)*phi(z)`. Its absolute sum is at most

`sqrt(sum_s W_s)*sqrt(phi(z)^T*G^(-1)*phi(z))`

by weighted Cauchy–Schwarz and V^T W V=G. Because the constant basis mode is even, its diagonal G entry is1/2, so sum_s W_s=1/2. The smallest Gram eigenvalue is(1-sigma)/2. This proves the first Lebesgue bound. Every normalized tensor mode has absolute value<=2on the square, so ||phi(z)||_2<=2sqrtN, giving the second.

Finally, `S_M(r)=(1+r^M)/2+sum_(j=1)^(M-1)r^j`; summing the finite series gives its stated rational form, with S_M(1)=M directly. The cosine and cosine-product identities yield C_M and Z_M. This completes all asserted identities.

## Checks and attempted continuation

Round10code c1_gram.py independently forms direct restricted Grams at small degrees and compares cross blocks, and verifies the finite moment formulas numerically including resonances. Those are supplementary to the written proof. Explicit moments contain factors `(1+r)/(1-r)` and exact parity zeros when r^M=1, suggesting a trigonometric Cauchy/Hilbert structure. No valid uniform strict-contraction or localized inverse estimate was obtained; resemblance alone is not a theorem identification. The elementary Cauchy–Schwarz route loses sqrtN even if the gap were uniform, so it does not close the desired polylogarithmic result.

## Sources, scope and open items

Literature comparison/candidate screen and follow-up reports identify related Fourier non-aliasing, lower-space Lissajous and known parity families, with stated fulltext gaps. No exact matching family is claimed absent from all literature; no novelty claim. Property(a)periodic yes; property(b)complete all-degree mixed cross-block criterion in these Chebyshev cases, plus arbitrary-field row-moment criterion elsewhere; property(c)polylogarithmic growth remains OPEN. Next exact analytic obligation: prove sigma_n<1for all stated degrees and obtain an inverse/kernel estimate whose interpolation L1norm avoids the sqrtN loss. Further numerical agreement cannot supply that proof.

## History

2026-10-31, Codex assigned gpt-6.1-sol xhigh, rules/source e949ef06895acd5463cdf8df7e0e5f795218f70f; rounds8–9frozen before derivation. Initially caseBwas restricted to n≡2mod4. Root-authorized rounds11–12proved the missing phase1count at n≡0mod4and confirmed the same antipodal argument for every even n, broadening caseBexplicitly. No theorem of universal unisolvence or logarithmic stability has been inferred.
