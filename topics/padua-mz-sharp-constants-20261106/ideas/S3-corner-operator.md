# IDEA-S3-03 — compact signed Bessel corner operator

Prospective registration,2026-11-06; no Bessel-model eigenvalues or final
S4 slope fits have been computed/read by S3. Complete preceding gate:
../novelty-gate-S3.md, including its prospective kernel refinement.

## Exact predeclared model and parity prediction

Let D={(a,b):a,b>=0,a+b<=1}, H=L2(D,ab da db), and

    J0(z)=sum_(r>=0) (-1)^r (z^2/4)^r/(r!)^2,
    psi_jk(a,b)=J0(pi j a)J0(pi k b),
    e_0=1/2, e_j=1 for j>=1.

For K>=1 define the finite-rank selfadjoint operator

    B_K=-16 sum_((1+j)(1+k)<=K, j+k even)
               e_j e_k (-1)^j |psi_jk><psi_jk|,

where |psi><psi|f=psi integral_D f psi ab da db. The predicted B is the
operator-norm limit of these B_K. Predicted signed logarithmic slopes:

    c_minus=inf spectrum(B),    c_plus=sup spectrum(B),
    lambda_minus(m,m-1)/log m -> c_minus<0,
    lambda_plus(m,m-1)/log m -> c_plus>0.

These exact constants and the **same values on even and odd m** are the
predeclared prediction. Even m has two active corners (1,1),(-1,1);
odd m has two active corners (1,1),(1,-1). Each active corner predicts
the identical B block. The other two corners predict a zero leading
block. Thus the full corner model is B direct-sum B, with zero allowed
in the remaining spectrum. This is an exact operator-value prediction;
no decimal slope is guessed before constructing that operator.

## Why this is falsifiable and what remains unproved at registration

The uniform finite-family L_m in S3-02 has tail norm at most120/K when
the retained nodes with endpoint-distance product>(K) are omitted. Its
fixed-corner scaled continuous reproducing kernel should converge to

    kappa((u,v),(u',v'))
       =integral_D ab J0(au)J0(au')J0(bv)J0(bv') da db.

At a shared corner kappa((0,0),(0,0))=1/24, fixing normalization.
Opposite-corner cross kernels should vanish by alternating sums.
Together these steps would control the full signed spectrum, with an
explicit tail error rather than fixed-index weights alone. A missing
tail bound, wrong sign/factor, nonzero cross-corner limit, or failure of
kernel convergence kills this formulation until repaired.

At registration the compact-operator construction and full spectral
transfer are **CONJECTURAL**; the full-form reduction S3-02 is proved
separately. Kernel-hard development is allocated by the coordinator to
a separate worker; it is a dependency, not an independent audit. This
record is preserved when the proof status is resolved in a theory file.

## Candidate disposition and numerical protocol

Retained implementation of the supplied corner-operator direction. No
historical novelty or priority claim. PD-T381 stays OPEN pending full
proof and independent review. The first numerical construction will
diagonalize finite B_K via its continuous Gram matrix, using a triangle
Gauss quadrature of increasing order; compare truncations before quoting
decimals. Such values remain MEASURED unless rigorous enclosures are
supplied. Parent publishes this exact prediction before final S4 fits.

Developer Codex S3, allocated gpt-6.1-sol xhigh; runtime metadata
unexposed. Input/rules2143ad622fa98faf8fe7d5cb8ed2bb7e0062f861.
