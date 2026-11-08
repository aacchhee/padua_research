# PD-T?padua-3d-20261106-codex-T9-r06-02 — phase and weight boundaries for short dual vectors

Aliases: T9-R06-PB; T9-R06-TH02. This file contains the positive-weight lemma (header ID), phase-uniform annihilator PD-T?padua-3d-20261106-codex-T9-r06-03, tetrahedron formula PD-T?padua-3d-20261106-codex-T9-r06-04, and counterexample PD-N?padua-3d-20261106-codex-T9-r06-01 (phase-blind short-dual inference). All IDs are provisional local namespaces.

Status: **PROVED local statements**. Scope: finite cosine images of torus cosets, and explicitly stated cubature or interpolation conditions. This is a variant of the old character and short-relation tools, with no novelty claim.

## A phase destroys the unshifted dual criterion in every degree

For q>=2, let H_q={2pi j/q:0<=j<q} and a=pi/(2q). The q distinct numbers cos(a+H_q) are precisely the q zeros of T_q. For each integer 1<=m<=2q-1, the Haar average of cos(m(a+theta)) is zero: it vanishes by the character average unless q divides m; the only remaining m=q has cos(qa)=0. Thus this is the positive q-point Gauss–Chebyshev rule of degree 2q-1, although the shortest dual vector has length q.

Taking three tensor factors gives H=H_q^3 and phase (a,a,a). Its q^3 distinct cosine points are exact on Pi_(2q-1), while the shortest nonzero vector of L=q Z^3 still has length q. In particular the assertion 'exactness on Pi_(2n-1) implies dual minimum >=2n' is false for translated Haar cosine rules, for every n=q>=2. This counterexample concerns that criterion; for q>=3, q^3 exceeds the total-degree cardinality, whereas q=2 has8<10. For every q>=2, T_q(x1) is a nonzero degree-q polynomial vanishing on these nodes, so the set is not Pi_q-unisolvent. The example therefore does not establish a translated Padua-type interpolation rule.

## A phase-uniform annihilator

Let k be a nonzero vector of L, r=||k||_1, s=|supp k|, and m=2^(s-1). For one representative of each pair of sign vectors epsilon and -epsilon on supp k, put

```
F(theta) = product_epsilon [cos(sum_j epsilon_j k_j theta_j)-cos(k.a)].
```

Changing the sign of any theta coordinate permutes these factors (cosine identifies the overall sign). Thus F is invariant under independent coordinate reflections. Its Laurent Fourier frequencies have l1 norm at most mr. The invariant Laurent polynomials have the tensor Chebyshev basis, so F(theta)=p(cos theta) for a real polynomial p of total degree at most mr. Every factor is a nonzero analytic function, hence their product is not identically zero. For theta in a+H the all-plus factor vanishes. Therefore p is nonzero and vanishes at every point of cos(a+H).

It follows that:

* if mr<=n, cos(a+H) is not Pi_n-unisolvent;
* if 2mr<=D, **no weights at all** supported on cos(a+H) can produce a Chebyshev-product integral rule exact on Pi_D. Indeed p^2 vanishes on the support, but its integral is positive.

For a=0 one can take F=product_epsilon(1-cos(sum epsilon_j k_j theta_j)), which is nonnegative and nonzero. In that unshifted case exactness on Pi_D with any weights is impossible already when mr<=D. These general annihilator conclusions include non-Haar weights. The sharper strictly positive unshifted argument below recovers the Haar threshold in dimension three and hence the same sharp packing constant. The phase-uniform argument alone does not recover that constant.

## Strictly positive unshifted weights obey the Haar short-dual condition

Let a rule exact on Pi_D use strictly positive weights on the full X=cos H. Suppose nonzero k in L has r=||k||_1<=D. There are three support cases.

If k has three nonzero coordinates, reorder the coordinates so their magnitudes are a>=b>=c>0 and put u=T_a(x1),v=T_b(x2),w=T_c(x3). Signed k causes no change because cos is even. On cos H the relation k.theta=0 implies the elementary cosine Gram identity

```
1-u^2-v^2-w^2+2uvw=0.
```

Therefore F=1-v^2-w^2+2uvw=u^2>=0 on X. Its degree is at most max(2b,2c,a+b+c)=r, since 2b<=a+b+c. Its product-Chebyshev integral is 1-1/2-1/2+0=0. But F(1,1,1)=1, so the strictly positive mass at the identity gives Q(F)>0, a contradiction. A two-coordinate relation gives T_a(x_i)T_b(x_j)=cos^2(a theta_i)>=0 on H, again with zero integral and identity value1 in degree a+b=r. A one-coordinate relation gives T_r(x_j)=1 on X, contradicting its zero integral and exactness of the constant.

Thus **every nonzero dual vector has norm>D**. The proof only requires nonnegative weights overall and a strictly positive identity mass; strict positivity at every node is a convenient sufficient hypothesis. If zero masses allow removal of the identity, this argument alone does not exclude a rule. The complete-support hypothesis must be retained. Combined with the imported octahedron theorem this proves the n>=110 density obstruction for arbitrary strictly positive unshifted weights in `t9-r06-packing-source.md`.

The degree3 LP (187 groups) and degree5 unbalanced-relation LP (111 eligible groups after241 analytic exclusions) found no escape. These are bounded MEASURED controls only; the all-degree proof above is independent of those searches. The degree5 follow-up was preregistered before its run; the final simpler nonnegative witness sharpened its initial balanced-relation motivation.

## Identical dual minimum can coexist with arbitrarily poor interpolation

Let H consist of the four torus points whose coordinates are 0 or pi and whose number of pi coordinates is even. Its dual is L={k in Z^3:k1=k2=k3 mod 2}, with shortest l1 length 2. For 0<t<=1 choose phase a=(arccos t,0,0). The cosine image is

```
X_t={(t epsilon1,epsilon2,epsilon3): epsilon_j in {+1,-1}, epsilon1 epsilon2 epsilon3=1}.
```

These four points are Pi_1-unisolvent, and their cardinal polynomials are

```
l_epsilon(x,y,z)=(1+epsilon1 x/t+epsilon2 y+epsilon3 z)/4.
```

Their Lebesgue function is convex in each coordinate, hence its maximum on the cube occurs at a vertex. Setting b=1/t>=1 and evaluating the two vertex sign classes gives

```
Lambda(X_t)=max(b,(b+3)/2).
```

Thus Lambda(X_1)=2 while Lambda(X_t) tends to infinity as t tends to zero, with the entire dual lattice unchanged. Shortest-dual length alone does not control the conditioning or Lebesgue constant of a phased cosine set. This fixed-degree example is not an asymptotic lower bound for a selected sequence of phases.

## Two-dimensional control

For the standard two-dimensional Padua torus representation, the cyclic order is 2n(n+1) and generator (n,n+1). Reducing its dual congruence modulo n and n+1 gives the exact dual lattice {((n+1)a,nb):a+b even}, whose shortest l1 length is2n, attained at(0,2n). An odd pair has norm at least2n+1; a nonzero even coordinate costs at least2n. Thus **every** dual vector has mr>=r>=2n>n and 2mr>=4n>2n-1. Neither rank/exactness obstruction falsely triggers on Padua. The mixed vector(n+1,-n) has length2n+1 and annihilator degree2(2n+1). Closed-form values through16 are tabulated (not enumerated) in `evidence/t9-r06-exact.json`; the inequalities prove compatibility for all n.

Dated correction 2026-11-06 (response03): the old blanket q^3>N
claim had the exceptional q=2 case wrong. The non-unisolvence argument
above supplies the correct scope; phase-blind short-dual inference is
still refuted exactly as before. The tabulation wording also applies
audit03 companion T9-F7. This is disclosed for focused material re-audit. The replaced sentence (9042e1c, line 11) read: "This counterexample concerns that criterion; q^3 exceeds the minimal total-degree cardinality and does not refute the unshifted packing theorem's cardinality conclusion for the larger translated class." Its final clause was removed with it; the packing theorem's own scope is in [t9-r06-packing-source.md](t9-r06-packing-source.md).

## Canonical claim homes and template fields — 2026-11-06 response03

ID kind: PD-T. Split from: none. Split into: the independently named
annihilator, tetrahedron and phase-counterexample subsections now have
standalone homes below; the positive identity-mass witness keeps this ID.
Definitions: Pi_D, full cosine support and dual L are defined in the
statement above. Assumptions: zero phase and nonnegative weights with
positive identity mass for the witness; other subsections have their own
stated assumptions. Status by part: the witness is local PROVED, the LP
controls are MEASURED, and all broader lower-bound/construction targets
are OPEN. Depends on the elementary cosine identity; the packing theorem
is a separate explicitly imported consequence, not a proof input here.

Canonical homes: [annihilator](r08-t9-phase-annihilator.md),
[tetrahedron](r08-t9-tetrahedron-formula.md),
[phase counterexample](r08-negative-t9-phase-dual.md). Those records
carry exact statements, proofs, D3 and remaining obligations. This older
combined text is retained for history and does not allocate duplicate IDs.
Open: a class-specific all-degree coset Lebesgue lower bound; resume with
a defined class/cardinal-kernel argument, not a rank-only annihilator.
History: audit03 accepted the local proofs; response03 adds canonical
homes and fixes the exceptional q2 cardinality sentence.
