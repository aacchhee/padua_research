# PD-T?padua-3d-20261106-codex-D1-02 — a stationary orthogonal local limit at critical intensity

ID kind: PD-T. Aliases: D1-LIMIT; random translation of high-leverage nodes.
Split from: supporting local-limit obligation of frontier C1.
Split into: none. Completeness is a separate obligation, not asserted here.

## Statement and definitions

Fix d>=1. Let n_r->infinity and, for every r, let a positive rule on T^d be exact on characters with |k|_1<=2n_r-2. Suppose its number M_r of distinct atoms satisfies M_r/m_(n_r)->1, where A_n={k in Z^d:|k|_1<=n-1} and m_n=|A_n|. Then there is a probability law P on locally finite, uniformly separated subsets Lambda of R^d such that:

1. P is invariant under every translation of R^d.
2. For every nonnegative f in C_c(R^d),

       E_P sum_(lambda in Lambda) f(lambda) = |O| integral f,

   where O={u in R^d:|u|_1<=1} and |O|=2^d/d!.
3. For P-almost every Lambda, the exponentials exp(2pi i lambda.u), lambda in Lambda, are pairwise orthogonal in Lebesgue L2(O).

All separations are Euclidean, and a single positive separation constant works for the whole law. Empty configurations are allowed in its ambient compact space. This does not assume every individual realization has a prescribed Beurling density.

## Assumptions, status and dependencies

Overall status: **PROVED** (local analytic supporting lemma). Depends on D1-01's torus frame identities. Standard background used explicitly: Arzela–Ascoli/diagonal compactness, representation of positive unit functionals on a compact metric space by probability measures, basic weak convergence, and Fubini for nonnegative finite sums. No source-specific cubature, universality or point-process theorem is imported.

Root supplied the stationary-translation lead before R2; the inherited S2/S4 sketch supplied the local spectral-limit question. Kolountzakis's compactness precedent is recorded in sources.md; no novelty is claimed for the compactness principle.

## Proof

Suppress r, and write q_j=m_n v_j and eta_j=1-q_j for the lifted masses. Set

    a_n=(M-m_n)/m_n ->0,
    epsilon_n=sqrt(a_n)+1/n ->0,
    G_n={j:eta_j<=epsilon_n}.

Only a subsequence of n values is present; every limit below is along it. At most (M-m_n)/epsilon_n=o(m_n) indices are discarded, since sum eta_j=M-m_n. Consequently g_n=|G_n| satisfies g_n/m_n->1 and g_n/n^d->|O|. Every retained q_j>=1-epsilon_n. For different retained atoms, the individual off-diagonal term in the frame row identity is bounded by q_j eta_j. Cancelling q_j gives

    |D_n(t_j-t_l)/m_n|^2 <= eta_j/q_l
                                  <= epsilon_n/(1-epsilon_n).       (1)

The estimates apply once epsilon_n<1; discarding a finite prefix has no effect.

### Uniform kernel limit

Define

    F_n(u)=m_n^(-1) sum_(k in A_n) exp(2pi i (k/n).u),
    F(u)=|O|^(-1) integral_O exp(2pi i xi.u) dxi.

Then F_n->F uniformly on every compact set. Here is the Riemann-sum justification including the boundary. Let C_n be the union of half-open cubes k/n+[0,1/n)^d for k in A_n. Its volume is m_n/n^d. The symmetric difference C_n triangle O lies in a shell ||xi|_1-1|<=C_d/n, whose volume tends to zero. On each such cube and for |u|<=R, the exponential differs from its value at k/n by at most 2pi R sqrt(d)/n. Integrating over C_n and using m_n/n^d->|O| proves the asserted uniform limit. No decay estimate for F away from zero is used.

### Separation of the full periodic configurations

Since F(0)=1 and F is continuous, choose b>0 so |F(u)|>=3/4 on |u|<=b. For sufficiently large n, |F_n(u)|>=1/2 on this ball, whereas the upper bound in (1) has square root <1/2. Define the periodic set

    L_n={n t_j/(2pi)+n z : j in G_n, z in Z^d}.

It is b-separated. Indeed two distinct points from different retained atoms at distance <=b would violate (1), since F_n of their difference is exactly D_n(t_j-t_l)/m_n (integer periods give exp(2pi i k.z)=1). Two copies of the same atom have distance at least n>b. Thus all L_n, after a finite prefix, lie in the same separated-configuration space. This step rules out both unbounded local multiplicities and collisions in the limit.

### Compact configuration space and limiting law

Let X_b be the space of counting measures of b-separated closed subsets of R^d, including the empty set, with the vague topology. For every R, disjoint balls of radius b/2 imply a uniform bound C_(R,b,d) on the number of points in B_R. This space is compact metrizable. One concrete compactness argument is as follows. For each configuration form h(x)=min(1,dist(x,Lambda)), assigning h=1 to the empty set. These functions are bounded and 1-Lipschitz. Arzela–Ascoli and a diagonal subsequence give local uniform convergence to h. Its zero set Lambda is b-separated. A zero is approximated by configuration points, and every convergent bounded sequence of such points is a zero. If h(x)<1, nearest points stay in a bounded ball, so this zero set has the expected truncated distance function. The uniform local count bound then shows convergence of sums of every compactly supported continuous test function. Hence the associated counting measures converge vaguely. A countable dense collection of C_c tests metrizes the topology on this locally bounded space. This proves sequential compactness and metrizability, hence compactness.

Let U_n be uniform on [0,n)^d and let P_n be the law of L_n+U_n in X_b. It is translation invariant for each n, because adding any fixed vector to U_n modulo nZ^d preserves uniform measure and L_n is nZ^d-periodic. The map from U_n to a counting measure is continuous in the vague topology, so the law is well defined.

Probability measures on compact metric X_b have a weakly convergent subsequence. For completeness, this can be obtained by diagonal convergence of integrals over a countable sup-norm-dense subspace of C(X_b); the limiting positive unit functional extends to C(X_b) and its representing probability measure is P. Translation by a fixed s is continuous on X_b. Passing the equality of integrals of H and H composed with that translation for every H in C(X_b) shows P is translation invariant. This holds for each s in R^d, without selecting any s-dependent subsequence.

### Retaining the exact intensity

For f in C_c, the functional Lambda -> sum f(lambda) is continuous and uniformly bounded on X_b by the local count bound. Directly, by partitioning R^d into period cells,

    E_(P_n) sum f(lambda)
      = (1/n^d) sum_(j in G_n) sum_(z in Z^d)
                       integral_[0,n)^d f(n t_j/(2pi)+n z+u) du
      = (g_n/n^d) integral_R^d f.

Weak convergence therefore gives the assertion in (2). In particular no intensity is lost in taking local limits: bounded compact-window counts are the needed uniform integrability. Taking a deterministic local subsequence alone would not justify this equality.

### Orthogonality almost surely

For a nonnegative compactly supported continuous cutoff f, define the finite sum

    H_f(Lambda)=sum_(lambda!=lambda')
          f(lambda) f(lambda') |F(lambda-lambda')|^2.

It is continuous and bounded on X_b. This follows from vague convergence, uniform local counts and continuity of F; the excluded diagonal can also be subtracted as sum f(lambda)^2 since F(0)=1. On every L_n+U_n, pair differences in the support of f belong to one fixed compact set. The uniform kernel limit and (1) therefore show H_f->0 uniformly over all translations U_n. Thus E_P H_f=0, and nonnegativity gives H_f=0 almost surely. Choose countably many cutoffs f_R>=1 on B_R, R positive integers. Outside a single null set all H_(f_R) vanish, so F(lambda-lambda')=0 for every distinct pair of points. This is exactly the orthogonality condition in L2(O), proving (3). QED.

## What remains and what was avoided

No far-field sum was passed through a limit. No deterministic 'orthogonal plus critical Beurling density implies complete' assertion was used. Neither completeness nor spectrality is a conclusion of this record; those require the separate Bessel/mean-intensity argument. It remains to show that at least one realization is complete, apply the checked spectral obstruction, and run the consistency/quantifier reconstruction. General doubling weights remain outside this torus lemma. [Superseded 2026-11-12 (audit-05): completed in D1-03/D1-04 and the R4 [reconstruction](reconstruction.md); current status in the [D1 README](README.md); this line is retained as round history.]

## Checks and history

Analytic R2 only, no computation. R2 protocol published/pushed at `db8c3cc` before root GO and this proof. Codex, assigned gpt-6.1-sol xhigh, 2026-11-12. The original D1 target is still recorded as OPEN pending completeness and the final source-dependent application. [Superseded 2026-11-12 (audit-05): completed in D1-03/D1-04 and the R4 [reconstruction](reconstruction.md); current status in the [D1 README](README.md); this line is retained as round history.]
