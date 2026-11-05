# PD-T?lanczos-frontier-codex-L1a — All-degree aggregate span separation on a sheared U-grid

ID kind: PD-T.
Aliases: SH_n; triangular affine product-U family; final-degree normal source; BJ same-degree chain; mirror latent-coordinate elimination.
Split from: the explicit-family all-degree part of L1 / earlier E2; G1 on T24/rotQ24 remains a separate finite task.
Split into: none.

## Statement

For every integer n>=2, put m=n+2 and, for 1<=k<=m, define

    theta_k=k*pi/(m+1), s_k=cos(theta_k),
    v_k=2*sin(theta_k)^2/(m+1).

Give the M=m^2 distinct physical nodes

    (x_kl,y_kl)=(s_k,2*s_k+s_l)

the positive weights w_kl=v_k*v_l. Work in ordinary Euclidean coordinates after multiplying function values by sqrt(w_kl). Let S and T be the diagonal matrices with respective entries s_k and s_l, so the physical coordinate operators are X=S and Y=2S+T. Write N_d=(d+1)(d+2)/2 and order columns (r,j), r,j>=0, by increasing r+j and then increasing j.

For each of the two fixed parent rules below, start from q_00=(sqrt(w_kl))_kl. At every other column h, form

    a_h(epsilon)=A_h q_parent(h)(epsilon)+epsilon*f_h,

project a_h exactly against **all preceding perturbed columns**, and normalize the residual to unit norm with positive normalization. No parents or choices are revised. The rules are:

- BJ: X from (r-1,0) if j=0; Y from (r,j-1) if j>0.
- Mirror: X from (r-1,j) if r>0; Y from (0,j-1) if r=0.

Sources f_h are arbitrary vectors in R^M, not necessarily polynomial evaluation vectors. Let sigma_h=||A_h q_parent(h)(0)||_2 and use the rule's own source norm

    ||f||_src^2=sum_{h!=00} ||f_h||_2^2/sigma_h^2.

Let P_n be the orthogonal projector onto the exact weighted evaluations of Pi_n, let P_n(epsilon;f) project onto the computed first N_n columns, and define the first-order spectral-output capacity

    kappa_R(n)=sup_{||f||_src=1} lim_{epsilon->0+}
                 ||(I-P_n)P_n(epsilon;f)||_2/epsilon.

Then the exact recursion exists near zero for each fixed f, and

    kappa_BJ(n) >= sqrt(2*(4^(n+1)-1)/3) >= sqrt(2)*2^n,       (1)

    0 < kappa_mirror(n)
        <= 2*sqrt(6)*(n+1)^2*(N_n-1)
        <= 2*sqrt(6)*(n+1)^4.                                (2)

In particular

    kappa_BJ(n)/kappa_mirror(n)
        >= 2^n/[2*sqrt(3)*(n+1)^2*(N_n-1)],                  (3)

and the lower bound has exponential rate log(2) up to a polynomial factor. This is an all-degree **worst-case aggregate-source, first-order span-capacity** separation on this explicit n-dependent sample family. It is not a statement about deterministic IEEE errors, scalar-operation realizability, finite-epsilon uniformity, every reorthogonalization rule or closure defects.

## Definitions

U_0(z)=1, U_1(z)=2z, U_(a+1)(z)=2z U_a(z)-U_(a-1)(z) are the Chebyshev polynomials of the second kind; U_-1=0. A polynomial p is represented by the vector (sqrt(w_kl)*p(x_kl,y_kl))_kl. S_d denotes the represented Pi_d space. Coordinate multiplication is diagonal in these coordinates. All norms without subscripts in source/column formulas are Euclidean; matrix output norm is spectral unless Frobenius is explicitly written.

The admissible exact graded orthonormal column is

    q_rj=(sqrt(w_kl)*U_r(s_k)*U_j(s_l))_kl.

Thus the exact column normalization is distinguished from the monic-polynomial normalization b_rj=2^(-(r+j))*q_rj. A source budget is recomputed from the fixed exact base run for the named rule; the two rules are compared in the same relative-raw-product convention, not with falsely identical per-column scales.

## Assumptions

Exact real diagonal operators, exact all-prior orthogonal projection and exact normalization. Starting column unperturbed. Fixed finite n, fixed sources when taking epsilon to zero. Positive normalizations at the unperturbed run. The theorem uses every source position through degree n in the capacity domain, although its lower bound uses one source. No truncation, coefficient perturbation, input perturbation, random source law, floating arithmetic or finite-u activation hypothesis is imported.

## Status by part

Overall status: PROVED (complete written analytic proof below; supplementary independent Astra xhigh mathematical check accepted at the immutable input hash recorded below; required Claude scientific/protocol audit pending).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| All-degree statement (1)--(3) in the declared model | PROVED | Complete analytic proof below; supplementary independent reconstruction accepted in independent-checks-sh.md; required Claude audit pending |

Candidate disposition: retained saved variant IDEA?lanczos-frontier-codex-l1-02, with supplementary independent mathematical acceptance at the stated scope; required Claude audit remains pending. No historical novelty/priority claim. Original L1 includes the separately required G1 scan and is not relabeled completed by this analytic family alone.

## Depends on

No unproved scientific dependency. The normal-quotient argument is proved directly below, extending the uniform monic framework of PD-T136 to the weighted normalized convention rather than silently invoking that theorem outside its hypotheses. Context: PD-T033/038/039 (product/near-product hypotheses); PD-T035/036/041 (coupling, admissibility and raw-propagator predecessors). None of their measured or finite growth conclusions is used as a proof step. PD-T053 is not used and no span-to-closure converse is asserted.

## Checks

The developer performed analytic development only and executed no numerical, symbolic or exact-arithmetic experiment for this record. The distinct reviewer separately executed the supplemental checks described in the verification addendum below. There is no computer-assisted proof component: the all-degree result follows from the written analytic argument. The supplementary independent mathematical reconstruction is accepted; the later required Claude scientific/protocol audit remains pending. G1 implementation/independent execution belongs to the distinct assignment and supplies no premise of this proof.

### Verification metadata addendum — 2026-11-05

[Independent adversarial check](../independent-checks-sh.md), by distinct Codex `/root/sh_adversarial`, assigned gpt-6-astra xhigh (runtime-resolved metadata not independently exposed), **accepted the complete analytic proof with no unresolved mathematical finding** at immutable proof input SHA256 `9f59217da265a433470bb6030074acf76e63e4ffb0a6590add800666a64de90d`. The review pins integration head `79c3d6a211325eca6e8311b3ae03187c100a1d8a` and earlier unchanged-rules head `0e493be7f9883e00e6260cf6b081c607a230177f`. This addendum changes verification metadata only; the statement, definitions, assumptions, dependencies, sources, proof and scope remain byte-identical to the audited input sections. The immutable audited input hash is retained even though this metadata update changes the whole-file hash.

The input proof was pinned by its working-tree content hash, not by claiming its file existed in the review's integration commit. Immediately before this metadata edit, the developer recorded SHA256 `13325943c81b8f21760a2ed79f77ddf442bdf42609007aa108f4e4589bb7ac05` for the concatenated named mathematical sections above, separated by a newline; that same digest was verified after the edit. No scientific text changed.

The reviewer independently reconstructed DST normalization, physical non-productness, dimensions/injectivity, creator coefficients, monic/source scaling, the differentiated normal quotient, the complete normal BJ witness, all-source mirror cancellation/bound and quantifier/scope limits. It also wrote and actually executed a separate exact finite checker: full differentiated-projection versus frozen-response tests for both rules at n=2,3,4, covering 1,618 source coordinate directions in total, and all88 symbolic creator identities through degree8. [Code](../code/sh_independent.py) SHA256 `3d996f0f85f006350f5a29af72fd1cf26c25c8894b18db1cf451444f908230b8`; [receipt](../evidence/sh-independent.json) SHA256 `776b97a5e213c0125f49bac2355bc6f4e48dd628b4c21d31cf7a9adc2ec6cbbd`. These were the reviewer's executions, not the developer's reruns. Their finite agreement supplements the independent analytic reconstruction and is not a finite reduction of the all-degree theorem.

Acceptance covers only the declared all-degree first-order aggregate-source span capacity. It does not settle G1, full scalar/IEEE activation, closure defects, every-rule behavior, finite-epsilon uniformity, historical priority or original L1's remaining obligations. Required later Claude audit and the explicit original pre-gate timing-deviation disposition remain pending.

## Sources

No new primary literature consulted or theorem imported. The elementary sine identities and U-polynomial recurrence are proved/recalled explicitly below. Relevant predecessor and literature-record coverage, including primary-reading limitations and pinned unmerged PR21 material, is in ideas-l1-l2.md checkpoints4 and the handoff03 delta gate. Standard ingredients, prior numerical shear probes and affine-product structure are disclosed; no priority claim.

## Proof or evidence

### 1. Positive normalized weights, orthogonality and injectivity

All theta_k lie strictly between 0 and pi, so v_k>0. The finite geometric-series identity gives, for 1<=a<=m,

    sum_{k=1}^m cos(2*a*k*pi/(m+1))=-1.

Consequently sum_k sin(a*theta_k)^2=(m+1)/2. The sine vectors

    (sin(a*theta_k))_{k=1}^m,  1<=a<=m,

are mutually orthogonal: they are eigenvectors, with pairwise distinct eigenvalues 2*cos(a*pi/(m+1)), of the real symmetric m-by-m tridiagonal matrix with ones above/below the diagonal and zeros elsewhere. The eigenvector identity follows from sin((k-1)alpha)+sin((k+1)alpha)=2*cos(alpha)*sin(k*alpha) and the zero boundary values at k=0,m+1. Distinct-eigenvalue orthogonality follows by taking inner products of the two eigenvector equations. In particular sum_k v_k=1.

Induction in the U recurrence, or the sine addition identity, gives

    U_a(cos(theta))=sin((a+1)*theta)/sin(theta).

Hence for 0<=a,b<=m-1,

    sum_k v_k U_a(s_k)U_b(s_k)=delta_ab.                      (4)

Taking products proves orthonormality of the m^2 represented U_r(s)U_j(t), 0<=r,j<=m-1. In physical coordinates t=y-2x. The polynomial U_r(x)U_j(y-2x) has total degree d=r+j and top part

    2^d*x^r*(y-2x)^j.

In the fixed within-degree order it has leading monomial x^r*y^j, coefficient 2^d, and only earlier monomials otherwise: the top expansion has y exponents 0,...,j, and all remaining terms have smaller total degree. Therefore the first N_d such columns are triangular bases of Pi_d for d<=n+1. By (4) their represented evaluations are independent. This proves injectivity through n+1, identifies the exact graded orthonormal basis q_rj, and gives its monic gauge b_rj=2^-d q_rj with squared norm 4^-d.

The nodes are distinct since x recovers s_k and y-2x recovers s_l. For every d<=n,

    M-N_d >= (n+2)^2-N_n=(n+2)*(n+3)/2>0.                  (5)

The physical measure is not a product measure. Indeed S,T are independent under v_k*v_l, E S=E T=0 and E S^2=1/4 by (4) for U_1=2z. Thus

    Cov(X,Y)=Cov(S,2S+T)=1/2,

whereas a product measure on the physical coordinate pair would have zero covariance. Affine-product structure in the latent coordinates is explicit, not excluded.

### 2. Exact creator coefficients and source scales

Use q with a negative index to mean zero. Multiplication by S and T gives

    X q_rj=(q_(r+1,j)+q_(r-1,j))/2,

    Y q_rj=q_(r+1,j)+q_(r-1,j)
              +(q_(r,j+1)+q_(r,j-1))/2.                    (6)

We only apply (6) to parents of degree at most n-1; all displayed nonzero indices are <=n<m-1, so (4) applies and there is no grid-end alias or boundary modification. For either prescribed creator, the target has coefficient beta_h=1/2 and all other displayed columns precede it. For BJ's Y creator of (r,j), j>0, the same-degree column (r+1,j-1) precedes the target. For mirror's Y boundary creator (0,j), the same-degree column (1,j-1) likewise precedes it. The leading-monomial criterion is therefore satisfied, and exact all-prior projection yields exactly q_rj with positive normalization 1/2 for both rules.

For an arbitrary parent (a,b) of degree <=n-1, orthogonality in (6) yields

    ||X q_ab||^2=(1+1_(a>=1))/4,

    ||Y q_ab||^2=1+1_(a>=1)+(1+1_(b>=1))/4.                 (7)

In particular BJ's source scale at h=(n,0), whose parent is (n-1,0), is 1/sqrt(2) because n>=2. Mirror uses Y only on parents (0,b), so every mirror source satisfies

    0<sigma_h<=sqrt(3/2).                                  (8)

The exact monic raw-product source corresponding at first order to a normalized source f_h in degree d is tilde f_h=2^(-(d-1))*f_h. Its relative scale is ||A b_parent||=2^(-(d-1))*sigma_h, so its relative source budget is identical. Similarly the monic frozen response is 2^-d times the normalized response below; multiplying it by its Gram factor ||b_h||^-1=2^d gives the same normal output. This explains all gauge/source factors; the direct derivative proof next also avoids any reliance on a uniform-weight theorem.

### 3. Weighted normalized normal-quotient derivative

For either rule write its normalized exact relation as

    beta_h q_h=A_h q_p-sum_{l<h} c_hl q_l,  beta_h=1/2.

All perturbed columns and coefficients are smooth near zero for fixed f: projection denominators are nonzero and residual norms are positive at zero, so induction gives a neighborhood where projection and positive normalization are smooth. Differentiate the exact perturbed relation and write a dot for derivative at zero:

    beta_h dot q_h=A_h dot q_p-sum_l c_hl dot q_l+f_h
                      -sum_l dot c_hl q_l-dot beta_h q_h.   (9)

Define the frozen vector responses V_00=0 and

    beta_h V_h=A_h V_p-sum_l c_hl V_l+f_h.                 (10)

Subtracting (10) from (9) shows inductively that E_h=dot q_h-V_h belongs to S_(deg h): multiplication sends S_(deg p) into S_(deg h), every earlier E_l and q_l belongs to S_(deg h), and q_h does too. Thus, with R_n=I-P_n,

    R_n dot Q_n=R_n[V_h]_{deg h<=n}.                       (11)

Because the actual perturbed columns Q_n(epsilon) are exactly orthonormal, ||R_n P_n(epsilon)||_2=||R_n Q_n(epsilon)||_2. Taylor expansion, R_n Q_n(0)=0, and (11) give

    ||R_n P_n(epsilon;f)||_2
       =|epsilon|*||R_n[V_h]||_2+O(epsilon^2).              (12)

The remainder is only for fixed n,f. Therefore the capacity in the statement equals the supremum of ||R_n[V_h]||_2 over the unit source sphere. Coefficient and normalization derivatives disappear only from this normal quotient; they have not been asserted to vanish from other observables.

### 4. BJ lower bound with a genuinely normal source

Set e=q_(n+1,0). Section1 proves ||e||=1 and e orthogonal to S_n. Take only one nonzero source,

    f_(n,0)=e/sqrt(2).

By (7) its source norm is exactly one. Every frozen response before degree n is zero. At the first column (n,0), (10) gives V_(n,0)=2 f_(n,0). For each remaining degree-n column (r,j)=(n-j,j), j>=1, the creator relation (6) has only one other degree-n column, (r+1,j-1), with coefficient1. Its parent and all other terms have lower degree and zero response. Hence

    V_(n-j,j)=-2 V_(n-j+1,j-1)=2*(-2)^j*f_(n,0).           (13)

Every vector in (13) is a multiple of e, so R_n leaves it unchanged. The nonzero output columns are a rank-one matrix. Its spectral norm is the norm of its row of scalar coefficients:

    ||R_n[V_h]||_2^2
       =4*||f_(n,0)||^2*sum_{j=0}^n 4^j
       =2*(4^(n+1)-1)/3.

This proves (1). In particular this lower bound is not an inference from an unprojected inverse entry: the entire rank-one output is explicitly normal to S_n.

### 5. Mirror polynomial upper bound for all sources

Put V with a negative index equal to zero. Equations (6),(10) give, for r>=1,

    V_rj=2S V_(r-1,j)-V_(r-2,j)+2 f_rj,                   (14)

and for j>=1,

    V_0j=2Y V_(0,j-1)-2V_(1,j-1)-V_(0,j-2)+2 f_0j.       (15)

The r=1 case of (14) is V_(1,j-1)=2S V_(0,j-1)+2 f_(1,j-1). Substitution into (15), using Y-2S=T, yields

    V_0j=2T V_(0,j-1)-V_(0,j-2)+2 f_0j-4 f_(1,j-1).      (16)

Induction using the U recurrence solves (14),(16):

    V_0j=sum_{b=1}^j U_(j-b)(T)*(2 f_0b-4 f_(1,b-1)),     (17)

    V_rj=U_r(S)V_0j
               +2 sum_{a=1}^r U_(r-a)(S) f_aj.            (18)

For j=0 the first sum is empty and V_00=0. Every source appearing in (17),(18) has total degree no larger than r+j, so these formulas use only available columns. The final boundary f_(1,n-1) is available earlier in degree n; no future source has been introduced.

For z in [-1,1], |U_a(z)|<=a+1: writing z=cos(theta), the sine ratio is the sum e^(ia theta)+e^(i(a-2)theta)+...+e^(-ia theta), whose modulus is at most a+1; endpoint values follow by continuity. Therefore diagonal multiplication by U_a(S) or U_a(T) has norm at most a+1. For each fixed output (r,j), r+j<=n, every individual source coefficient operator in (17),(18) has norm at most

    C_n=4*(n+1)^2.                                        (19)

There is no hidden duplication that could invalidate (19): boundary sources are f_0b and f_(1,b-1) with b<=j; direct sources in (18) have second index exactly j. A source f_(1,c) occurs in a boundary term only if c<=j-1 and in a direct term only if c=j, so these cases are disjoint. Other source indices are already distinct. The bounds 2*(r+1)*(j-b+1), 4*(r+1)*(j-b+1), and 2*(r-a+1) are all bounded by (19).

Let H=N_n-1 and u_h=f_h/sigma_h, so sum_h||u_h||^2=1. Using (8),(19), the triangle inequality and Cauchy--Schwarz, for every output column,

    ||V_rj|| <= C_n*sqrt(3/2)*sum_h ||u_h||
               <= C_n*sqrt(3H/2).

There are H nonconstant output columns and the constant output is zero. Consequently

    ||R_n[V_h]||_2 <= ||[V_h]||_F
        <= C_n*sqrt(3/2)*H
        =2*sqrt(6)*(n+1)^2*(N_n-1).                        (20)

This proves the upper bound uniformly over the entire unit source sphere. Positivity of kappa_mirror follows by injecting a unit-budget source proportional to e at the last column (0,n): earlier V vanish and this last output is 2 sigma_(0,n) e, with positive scale. Finally H<= (n+1)^2, so the simpler upper in (2) holds. Dividing (1) by the positive upper bound gives (3). The logarithm of the denominator in (3) is O(log n), proving the stated exponential-rate separation. This finishes the proof.

## Scope

This exact, weighted aggregate-capacity family supplies an all-degree BJ exponential lower and mirror polynomial upper. It changes neither G1's frozen rational grids/criteria nor any source law or predicate in finite L2. The adversarial source depends on n and is a free aggregate vector; no one scalar operation or IEEE realization is asserted to produce it. Both algorithms use exact all-prior projection and have no loss of orthogonality; the observable is drift of their spaces. No degree-uniform nonlinear remainder or finite-epsilon activation estimate follows. A physical shear alone is not claimed as a new mechanism or a general classifier of non-product measures.

## Open items

- Supplementary independent mathematical reconstruction is complete and accepted at the immutable input hash in the verification addendum; any future mathematical change requires impact review.
- Required later Claude scientific/protocol audit, explicitly retaining the original pre-gate timing deviation.
- G1 exact scan and its independent execution remain required separately. Finite L2 W/R/F predicates, closure defects, actual IEEE activation, uniform finite-epsilon regime and any general family classification remain OPEN/outside this theorem.

## History

- 2026-11-05: Codex developer `/root/l1_l2`, assigned gpt-6.1-sol xhigh mathematics; runtime-resolved metadata not independently exposed. Rules/current head `0e493be7f9883e00e6260cf6b081c607a230177f`; main input supplied by root `21dbfc90257b952d8923f6d01739d12aa8d6e0a1`. Full earlier gate preserved and new registry delta read before renewed development. Saved SH_n family and contemplated equations retained unchanged; this record supplies their proposed complete hypothesis/normal-quotient proof. No experiment, Git mutation, final-ID allocation or self-audit.
- 2026-11-05: metadata-only verification addendum after root reported accepted distinct Astra xhigh check. Full independent report read, recovering an initially truncated tail in bounded lines90--end. Updated stale current pending-check wording; preserved immutable audited input hash and all mathematical sections. Required Claude audit and timing-deviation disposition remain pending. No new scientific computation or Git mutation by this developer.
