# PD-T?argmax-effective-2-codex-01 — Exact common primitive and finite phase-cover reduction

ID kind: PD-T.
Aliases: A1 structural gate; endpoint-weighted reflection; common phase diamond; full versus projected defect.
Split from: none; explicit verification and certificate formulation of PD-T215/218/223, not a new primitive identity.
Split into: none. The unconstructed H1 certifier remains OPEN in `../attempts/H1.md`.

## Statement

For every integer n≥2 the identities (1)–(5) below hold at every physical angle point, including nodes, edges, corners and kernel collisions. In particular **λ=S_n−Δ is exact** when Δ is the full four-copy triangle defect. For projected defects only λ≤S_n−Q_v and λ≤S_n−Q_h follow. Endpoint weights cause no extra term.

For each fixed n, any finite collection of validated bounds meeting the cover and strictness predicates in §Finite reduction proves that λ≤Λ_c everywhere, with equality only at the two nonnode corners. This is a sufficient certificate theorem, not a claim that such a cover has been constructed or has a specified complexity.

## Definitions

Put m=n+1, N=nm, a_j=jπ/n, b_k=kπ/m. Physical nodes have 0≤j≤n, 0≤k≤m and j+k even. Let e_j and f_k be 1/2 at their two endpoints and 1 otherwise; w_jk=2e_jf_k/N. Let h_0=1 and h_a=2 for a>0, and

\[
 D_n(u,v)=\sum_{a+b\le n}h_a h_b\cos(au)\cos(bv),\qquad
 G_n(u,v)=D_n(u,v)-\cos(nu).
\]

Thus the exceptional coefficient of mode (n,0) in G is 1. These finite trigonometric polynomials, not quotients, define the functions at all arguments. For each physical node set g_ση=G_n(θ+σa_j,φ+ηb_k), σ,η∈{−1,1}, and define

\[
 M=\sum_{j+k\ {\rm even}}\frac{w_{jk}}4\sum_{\sigma,\eta}|g_{\sigma\eta}|,
 \quad
 \Delta=\sum_{j+k\ {\rm even}}\frac{w_{jk}}4
       \left(\sum_{\sigma,\eta}|g_{\sigma\eta}|-
                         \left|\sum_{\sigma,\eta}g_{\sigma\eta}\right|\right).
\]

The projected Q_v groups the four terms into the two fixed-σ pairs; Q_h uses fixed-η pairs, exactly as PD-T215. Let Γ⁻ be the odd board 0≤r<2n, 0≤s<2m, r+s odd, and

\[
 S_n(\alpha,\beta)=\frac1{2N}\sum_{(r,s)\in\Gamma^-}
 \left|G_n\left(\frac{r\pi+\alpha}{n},\frac{s\pi+\beta}{m}\right)\right|.
\]

It has 2N terms. This equals PD-T216's normalization N⁻¹Σ|F_rs| because |F_rs|=|G|/2. Write D={|α|+|β|≤π}. Physical odd centers are C={0≤J≤n,0≤K≤m,J+K odd}; their admissible domains are

\[
 D_{JK}=D\cap\{-J\pi\le\alpha\le(n-J)\pi,
                  -K\pi\le\beta\le(m-K)\pi\}.
\]

At boundary centers this imposes the appropriate inward phase signs. A phase point is attached only to centers for which it is physical.

## Assumptions

The corrected cardinal identity PD-T101, even-checkerboard nodes, and exact real arithmetic. For certificate acceptance every supplied enclosure must be exact or outward rounded and independently validated; floats alone are insufficient. No assumption about a maximizer, smooth sign pattern or asymptotic profile is used.

## Status by part

Overall status: **PROVED** by the analytic reduction below, pending supplementary check and required Claude audit. This is an inherited-identity verification plus a sufficient finite reduction; it does not upgrade any finite degree or PD-T099.

| Mathematical part | Status | Evidence / limitation |
|---|---|---|
| Common primitive, reflection multiplicities and full-defect equality | PROVED | Product-to-sum and exact periodic reindexing |
| Sufficiency of the stated finite-cover predicates | PROVED | Pointwise comparison and coverage |

Candidate disposition: retained quantitative/computational variant. No novelty claim.

## Depends on

PD-T101 for the cardinal coefficients; PD-T215/216/218/223 are the exact inherited identities reconstructed here. PD-T224 and PD-T251 can supply narrowly scoped predicates, but are **not** needed for the reduction theorem itself. PD-T099 remains OPEN.

## Proof or evidence

### Cardinal identity and defect

Using cos(aθ)cos(aa_j)=[cos(a(θ+a_j))+cos(a(θ−a_j))]/2 in both variables gives, coefficient by coefficient including (n,0),

\[
 L_{jk}(\cos\theta,\cos\phi)=\frac{w_{jk}}4\sum_{\sigma,\eta}g_{\sigma\eta},
 \qquad \lambda=M-\Delta.                                      \tag{1}
\]

All w_jk are positive. The triangle inequality proves Δ≥0. Grouping the sum first into the two vertical or horizontal pairs proves

\[
 \Delta\ge Q_v\ge0,\qquad \Delta\ge Q_h\ge0.                  \tag{2}
\]

Equality (1) does not claim equality in the triangle inequality. Δ records the complete loss. Substitution of Q for Δ changes equality to an upper bound.

### Endpoint reflection and translation

For every residue r modulo 2n,

\[
 \sum_{0\le j\le n,\ \sigma=\pm1:\ \sigma j\equiv r\ (2n)}e_j=1.
\]

Interior residues have one reflected preimage with weight 1. Residues 0 and n each have two coincident preimages, each with weight 1/2. The same statement holds for the m mesh. Reflection preserves parity because −j≡j (mod 2). Therefore, without any estimate,

\[
 M(\theta,\phi)=\frac1{2N}
 \sum_{\substack{0\le r<2n,\ 0\le s<2m\\r+s\ {\rm even}}}
       |G_n(\theta+r\pi/n,\phi+s\pi/m)|.                       \tag{3}
\]

If θ=(Jπ+α)/n, φ=(Kπ+β)/m and J+K is odd, translation by (J,K) is a bijection from the even periodic board to Γ⁻. Periodicity of the finite kernel then gives

\[
 M(\theta,\phi)=S_n(\alpha,\beta),\quad
 \lambda_n(\theta,\phi)=S_n(\alpha,\beta)-\Delta_{JK}(\alpha,\beta).
                                                                    \tag{4}
\]

S_n is independent of the chosen physical odd center, for fixed phases. The **defect is not**. Different admissible phase representations of the same physical point yield the same physical M by (3); no unique nearest-center selection is required.

### Coverage, collisions, zeros and corners

Choose a physical mesh rectangle containing (θ,φ); at a physical boundary use its adjacent interior rectangle. In normalized coordinates x,y∈[0,1], the distances to its two odd vertices are x+y and 2−x−y, or 1−x+y and 1+x−y. In either case their sum is 2, so one distance is at most 1. This proves that the maps from all D_JK cover [0,π]², including tied boundaries.

No denominator was introduced in (1)–(4). For implementation the divided difference of P_n=T_(n+1)+T_n gives

\[
 G_n(u,v)=\frac{P_n(\cos u)-P_n(\cos v)}{\cos u-\cos v}-\cos(nu)
\]

only when cos u≠cos v. At a collision replace the quotient by P'_n(cos u). In particular G_n(0,0)=2N, G_n(π,π)=2n(−1)^n, and G_n(0,π)=0. Zero terms remain inside absolute values; no differentiation through a sign change is assumed. The zero phase odd board can include the (π,π) collision, which must not be replaced by zero.

At each physical corner the four g_ση agree, by evenness and 2π-periodicity in each argument. Thus Δ=0 there. At a nonnode corner J+K odd, (4) gives

\[
 S_n(0,0)=\Lambda_c(n).                                      \tag{5}
\]

Node corners have λ=1 by cardinal interpolation. They are covered by boundary phases of odd-center charts; they are not additional zero-phase nonnode corners. At an edge only the copies in the endpoint coordinate coincide; the other pairing can retain positive defect.

### Finite reduction, with explicit acceptance predicates

Fix n and a rigorous lower bound L_c≤Λ_c(n). Partition the finite set C into any classes; classes may be singletons. For each class A cover every D_JK, (J,K)∈A, by finitely many closed phase boxes (or intersections of boxes with D_JK). Overlaps are allowed. A bound on the whole enclosing box is valid for its intersection, but the cover must not omit admissible boundary phases. Accept each class/box pair by one of:

1. **Far:** a validated U≥sup S_n on the relevant phase set has U<L_c.
2. **Defect:** a validated U≥sup S_n and d≤inf Δ_JK, uniform over all admissible members of A on that set, have U−d<L_c. A valid choice is d=max(0,d_v,d_h) where each d_v/d_h bounds its projected defect below. A sampled class minimum is not such a bound.
3. **Corner:** the class consists of actual nonnode corners and a validated direct comparison establishes λ_n≤Λ_c there, with strict inequality away from the corner itself. One possible certificate is Λ_c−λ_n≥c_x h_x+c_y h_y with c_x,c_y>0 and inward physical distances h_x,h_y≥0. No positive fixed numerical margin is required at the corner where equality is intended.

Every physical point belongs to an accepted class/box pair. Predicates 1 and 2 give strict comparison by (4). Predicate 3 gives the stated strictness except at the two actual nonnode corners; (5) gives equality there. Hence these predicates imply the full degree-n maximum and equality classification. This proof does not assume that the three regions have a fixed prescribed shape.

The existing Δ≥1/4096 is available only for n≥48, ρ≤1/64 and noncorner physical odd centers (PD-T224). It gives no bound on 1/64<ρ≤0.1. The existing physical n⁻⁶ corner radius (PD-T251) can be used within its exact domain, but does not supply H1's desired physical n⁻² corner box. Those are unresolved implementation obligations, not extra hypotheses silently accepted by this theorem.

### All-center projected-defect screen

At fixed phases define H_rs=G_n((rπ+α)/n,(sπ+β)/m) on Γ⁻. Periodic indices below are taken modulo 2n or 2m. With d(x,y)=|x|+|y|−|x+y|, exact reflection gives

\[
 Q_v^{(J,K)}=Q_v(K)=\frac1{4N}\sum_{\Gamma^-}d(H_{rs},H_{r,2K-s}),
 \quad
 Q_h^{(J,K)}=Q_h(J)=\frac1{4N}\sum_{\Gamma^-}d(H_{rs},H_{2J-r,s}).
\]

For example, first periodicizing the j mesh gives Q_v=(2N)⁻¹Σ_k f_k Σ_r d(H_(r,K+k),H_(r,K−k)), with the required parity. Periodicizing k counts each nonfixed pair twice; the endpoint/fixed pairs have d(x,x)=0. This yields the factor 1/(4N). Both index reflections preserve Γ⁻. **The phase β is unchanged** in H_(r,2K−s), and α is unchanged in the horizontal partner; only the integer lattice index is reflected.

Consequently an all-center lower screen at fixed phases needs the m+1 vertical profiles and n+1 horizontal profiles, followed by min over admissible noncorner centers of max(Q_v(K),Q_h(J)). Precomputing H costs O(n²) kernel calls; computing every profile directly costs O(n³) arithmetic operations. This is a pointwise algebraic algorithm, not a rigorous lower bound throughout a phase box. It cannot be replaced by a minimum over a few representative centers without a proof of that reduction.

### Implementable primitive enclosure, without a complexity claim

Put s=(u+v)/2, t=(u−v)/2 and R_k(z)=sin(kz)/sin z, continued as its finite trigonometric polynomial. Direct cosine subtraction gives

\[
 G_n(u,v)=R_{n+1}(s)R_{n+1}(t)+R_n(s)R_n(t)-\cos(nu).
\]

Away from zeros of sin z an outward sine quotient gives an enclosure. Near z=lπ, write z=lπ+q and use

\[
 R_k(l\pi+q)=(-1)^{(k-1)l}\,k\,\frac{\operatorname{sinc}(kq)}{\operatorname{sinc}(q)},
 \qquad \operatorname{sinc}(0)=1.
\]

On a neighborhood |q|<π this denominator is positive. Validated Taylor/range bounds for sinc then handle q=0 continuously. A box crossing several such charts must be split or bounded with the finite polynomial; pointwise substitution near a tiny denominator is insufficient. Each odd-board term can thus be enclosed before summing |G|/(2N). There are O(n²) terms, but accuracy-dependent arithmetic cost, refinement count, total coset-class cost and checker time remain unmeasured. This identity alone proves no O(n²) per-degree complexity.

## Checks

`python topics/padua-argmax-effective-2-20261105/code/structure_probe.py` checks n=3,4,5,6 by exact Fraction group algebra before absolute values. It compares direct cardinal evaluation with all four reflected kernels and compares the exact weighted argument multisets with the shifted odd periodic board. It also checks diagonal/opposite-angle collisions, both endpoint collision values and an exact zero. This supplementary finite check does not replace the analytic all-n proof. Run outcome is recorded in `../gates-structural.md`; independent rerun and Claude audit are separate.

## Sources

Internal dependencies above. The delegated novelty scan read the literature index before source comparisons. No external attribution, source transfer or historical novelty claim is made.

## Scope and open items

The inherited structural identity survives A1. The **cost gate remains unevaluated** until a complete corner predicate, classwise defect bounds, arithmetic margins and a genuine box cover are specified. A float point grid supplies none of the missing cover proof. No maximum certificate at n>32 or effective all-degree threshold follows from this record. PD-T099 remains OPEN.

## History

2026-11-05, Codex mathematical worker, AC-requested gpt-6-astra ultra; runtime model/effort not independently exposed. Input/rules ed21cc0bf205549936fccde90244a291bc6de324. Reconstructed the existing equality in response to the possible reflection-inequality concern. This is not a correction of PD-T215/223. Newly merged PD-T269 uses Δ_n for a **different signed mesh deformation** in Λ_c−L_n²; it is not the Δ of this record and supplies no H1 cancellation bound. No final IDs assigned.
