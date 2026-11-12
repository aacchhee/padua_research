# D1 supplemental adversarial reconstruction — 2026-11-12

Reviewer: Codex supplemental agent, assigned gpt-6-astra xhigh; additional
provider metadata is not independently exposed. Rules read at
`4ab7e93ee19d60c5cfbf3626a23e43fd871a38ef`; AGENTS, WORKFLOW, CODEX and
handoffs 19/18. No developer-file edits or Git operations. This is
**supplemental mathematical review, not formal Claude acceptance**.

## Current verdict

**PASS for the R1–R4 material at the hashes below, with general doubling
explicitly OPEN.** I independently
reconstructed each finite, compactness, intensity, completeness and
quantifier step. No unresolved mathematical gap was identified. The
appropriate consequence label is **PROVED with explicit LITERATURE
dependency**, using the independently primary-checked Greenfeld–Lev
Theorem 1.1. This is an audit conclusion at the stated scope, not a
historical-priority claim, an effective constant, or approval of later
material changes.

The R4 coverage update below verifies the exact inverse-polynomial
weight corollary, consistency controls and the conditional H1/H2 route.
It does not establish H1/H2 from doubling. The R1–R3 Chebyshev proof
bytes remained unchanged on this second read.

## Input identity

The R3 proof was present by observed branch head
`9cf64efbe16b9ba356c20f1d987ba1f60034cfb3`. Because the coordinator
and developer were active concurrently, exact read-version hashes identify
the audited prose:

| Topic-relative file | SHA256 |
|---|---|
| final-d1/finite-frame.md | 6e02595b600085b5b8d55412d66ba93087dfb55d4798059bfbf548d955fb9254 |
| final-d1/stationary-limit.md | 11c6c719078aad03878905aee28f52d22aba0f92d782d677af66cd7d99df23f5 |
| final-d1/complete-law.md | 6db3f5dc823a1cd37aa22418793222b0bcd22f776ee595317b44202235b17ece |
| final-d1/spectral-obstruction.md | 33206f2d2196420b5af5adb9310963bc22f6ec7bdc8eaf8381d25334a861d33c |
| code/fd1_controls.py | e5bf2b9266a8128585c460c42324827b3380b1c3443a9e38ed9cffd457292d1c |

Also read the D1 protocol, gate, rounds and sources, frontier S2/S4,
the complete T9 Haar/phase/packing and unshifted negative predecessors,
and the relevant D5 source coverage. The resulting comparison is below.

## Adversarial reconstruction

### Finite identities and reflection

The polynomial Gram identity follows from exactness on products of two
degree-(n-1) basis elements. B*B=I makes BB* a projection, so its
diagonal entries lie in [0,1], its trace is D and its squared row sum
equals its diagonal. These prove every stated defect identity without
requiring unisolvence on Pi_n.

Every boundary sign orbit has constant stabilizer size. Averaging all
2^d signs with repetitions is therefore averaging its distinct atoms
with equal weights. Its character average is the tensor Chebyshev
polynomial of total degree |k|_1. Distinct cube nodes cannot share a
reflected orbit. This verifies the character exactness, positivity and
M<=2^d N bound, including endpoints and repeated coordinate values.

The torus frequency set A_n has size m_n=(2^d/d!)n^d+O(n^(d-1)).
Differences of two frequencies have l1 norm at most 2n-2, giving the
exact complex Gram identity. Its rank gives M>=m_n. Thus N/D->1,
with D=binom(n+d-1,d), forces M/m_n->1 by squeeze. There is no
unstated assumption that most original nodes are interior; this squeeze
already handles the potentially smaller boundary orbits.

### Removal, separation and compactness

Set a_n=(M-m_n)/m_n>=0 and epsilon_n=sqrt(a_n)+1/n. The number of
discarded atoms is at most a_n m_n/epsilon_n=o(m_n), even when a_n=0.
Consequently g_n/m_n->1. The projection-row bound after dividing by
q_j=m_n v_j>0 is exactly

    |D_n(t_j-t_l)/m_n|^2 <= eta_j/q_l
                              <= epsilon_n/(1-epsilon_n).

The denominator is positive after discarding a finite prefix. No
uncontrolled minimum over the discarded weights occurs.

The union of cubes k/n+[0,1/n)^d differs from the unit l1 ball only
within an O(1/n) boundary shell. Uniform continuity of the exponential
for bounded u proves the normalized Riemann-sum kernel limit on every
compact set. The frequency radius n-1 rather than n affects only that
shell. Since the limiting kernel equals one at zero, near-orthogonality
gives one positive separation constant for the rescaled retained sets.
The factor n/(2pi) in the spatial rescaling exactly matches the
exp(2pi i xi.u) Fourier convention.

I checked the empty-limit and collision cases in the compactness
argument. Truncated distance functions are bounded and 1-Lipschitz;
their locally uniform subsequential limit is the truncated distance to
its zero set, including the all-one function for the empty set. If a
limiting distance is below one, nearest points remain in a compact set
and supply a zero. Separation prevents collisions, while packing gives
uniform bounds on counts in every fixed compact set. Those bounds also
make continuous compactly supported counting functionals continuous
under the resulting vague convergence.

Random translation uniformly over one period cell makes each P_n
exactly stationary. Weak compactness of probability measures on the
compact configuration space gives one limiting law. Translation is a
continuous map for every fixed translation, so invariance passes using
that same subsequence; no uncountable intersection or translation-specific
subsequence is being used.

### Exact intensity survives the limit

The period-cell integral of a compactly supported test is exactly

    E_(P_n) sum f(lambda) = (g_n/n^d) integral f.

Compact-window counts are uniformly bounded, not merely bounded in
expectation. Thus the counting functional is a legitimate bounded
continuous test for weak convergence. Its expectation converges to
|O| integral f. This explicitly prevents the usual loss-of-intensity
counterexample in which clusters of growing multiplicity disappear
from almost every local window. Those clusters are excluded by the
uniform separation already proved.

For the orthogonality functional H_f, the finite pair sum is continuous:
the product counting measure converges on a compact support, and its
diagonal is subtracted separately. Uniform local counts bound the number
of terms. The kernel convergence and the row estimate force H_f->0
uniformly in translation. Nonnegativity then gives zero expectation
only if H_f=0 almost surely. Countably many cutoffs equal to one on
expanding balls give all pairwise orthogonality on one event of full
probability.

**NOTE (optional clarity, not a gap):** two periodic copies of the same
retained torus atom are at distance at least n. They cannot both occur
in a fixed cutoff support once n exceeds its diameter. Hence every
pair used in the limiting H_f estimate is either absent or covered by
the off-diagonal estimate for distinct original atoms. This routine
eventual observation is implicit in the written proof and was sent to
the coordinator for possible clarification. **Resolved editorially in
R4:** reconstruction.md now states it explicitly; no proof correction
was required.

### Completeness, including the tail issue

The decisive extra fact is exact **mean counting measure**, not merely
critical asymptotic density of a deterministic realization. With
F=hat(1_O)/|O|, Plancherel gives integral |F|^2=1/|O|. Equality of
locally finite mean measures extends the C_c identity to nonnegative
Borel tests. Monotone convergence/Tonelli can therefore be applied to
|F(y-lambda)|^2 without first assuming a far-field bound. It yields
E S_Lambda(y)=1 for every fixed y.

Bessel's inequality for normalized exponentials gives S_Lambda(y)<=1
almost surely, so equality holds almost surely for each rational y.
Taking the countable intersection of those events is valid. Equality
in Bessel implies each rational-frequency normalized exponential is
in the closed span of the selected exponentials. If g is perpendicular
to that span, its zero extension is in L1 by finite volume; continuity
and uniqueness of its Fourier transform then give g=0. This proves
completeness on one event of probability one, not just completeness
with a y-dependent exceptional set.

I challenged this with the standard 'remove one point from a spectrum'
example: it preserves a deterministic density but loses the required
homogeneous mean measure. There is no stationary probability distribution
for a single finite hole spread uniformly over all of R^d. The example
therefore does not contradict the lemma. Empty configurations likewise
cannot receive positive probability under all of its hypotheses, as
Bessel saturation rules that out.

### Source application and universal quantifiers

The octahedron O is bounded, full-dimensional and convex. Its positive
coordinate facet is a triangle. Central symmetry would pair its vertices
without fixed vertices, impossible for three vertices. After completeness
has been proved, Greenfeld–Lev's facet condition applies in exactly the
same Fourier and Lebesgue normalization.

Negating the eventual assertion gives, for each r, a degree n_r>=r
and a positive rule with N_r<(1+1/r)D_r. The elementary dimension bound
supplies N_r>=D_r. Hence n_r->infinity and N_r/D_r->1, even without
monotonicity of the sequence. The three local lemmas then produce a
spectrum for O and a contradiction. This establishes a uniform
existential gamma>0 and n0 over **all** such positive rules; it is
stronger than merely excluding one preselected sequence.

Finally binom(n+3,3)/binom(n+2,3)=1+3/n. Thus eventual positive
Padua-cardinality cubature is excluded. There is no numerical value of
gamma, no explicit finite forbidden degree, no 1/4 leading coefficient,
and no conclusion about interpolation without positive cubature.

## Primary-source checks actually performed

The web PDF reader exposes primary text and page counts, not downloaded
PDF bytes. No PDF checksum is fabricated. Source proofs were not
independently reconstructed and remain LITERATURE.

| Source | Actual independent coverage | Use |
|---|---|---|
| [Greenfeld–Lev 1602.08854v2](https://arxiv.org/pdf/1602.08854v2), 39 pages | Definition (1.1), introduction, Theorems 1.1/1.2, printed pp.1–3 | Load-bearing facet condition; exact completeness and normalization checked |
| [Lev–Matolcsi 1904.12262v4](https://arxiv.org/pdf/1904.12262v4), 29 pages | Definition, Theorem 1.1, introductory facet/tiling conditions, printed pp.1–3 | Corroboration only; no additional dependency needed |
| [Antezana–Marzo–Ortega-Cerda 2101.08064v1](https://arxiv.org/pdf/2101.08064v1), 17 pages | Introduction; Proposition 12, Theorems 13/14 and their displayed proof/remark, printed pp.14–16 | Close prior kernel-blow-up/orthogonality obstruction; direct sphere analogy is only the source's remark |
| [Kolountzakis 1606.02452v1](https://arxiv.org/pdf/1606.02452), 14 pages | Definitions, Theorem 1, Lemmas 1–3 and final proof of Theorem 1, printed pp.4–7,9 | Close compactness/density-to-tiling precedent; not directly imported for approximate finite orthogonality |
| [Marzo math/0611503v1](https://arxiv.org/pdf/math/0611503v1), 25 pages | Introduction, sphere/MZ/interpolation definitions, Theorems 1.6/1.7, printed pp.1–4 | R4 consistency check: the nonexistence theorem expressly omits p=2; no L2 sphere excess follows |
| [Kuperberg math/0405366v2](https://arxiv.org/pdf/math/0405366v2), 15 pages | Introduction; Proposition 3.1/Theorem 3.2 p.5; Theorem 6.1 statement p.11, Corollary 6.2 statement/discussion pp.12–13, Scholium 6.5 and its sketch p.14; section 7 Fourier-cubature paragraph p.14 | R4 prior-art comparison only; lattice packing, uniform-simplex/polytope local density, and periodic weighted Fourier-cubature density minimization |

The AMO result concerns exact orthogonal reproducing-kernel bases on a
ball. The currently read statement does not establish D1's arbitrary
almost-critical redundant positive-frame extension on the cube. The
Kolountzakis statement assumes exact packings of a fixed function, which
the finite D1 configurations do not directly provide. They are substantive
predecessors; no claim that either general principle is new is justified.

## Consistency and exact controls

In dimension two, O is the diamond A[-1/2,1/2]^2 for
A=[[1,1],[1,-1]]. It has the explicit lattice spectrum
A^(-T) Z^2={((p+q)/2,(p-q)/2):p,q in Z}, with intensity 2=|O|.
Thus the local-limit/completeness chain permits the Padua control;
the nonspectrality conclusion fails precisely where it should. Finite
D3 existence is also compatible with a non-effective eventual theorem.

Actually executed separately from both development and root reruns:

```sh
python -B topics/padua-3d-20261106/code/fd1_controls.py --output topics/padua-3d-20261106/evidence/fdc-d1-controls.json
```

CPython 3.12.14, SymPy 1.14.0, optimization zero, seed none; elapsed
0.48733 seconds measured. All seven exact rows equal the developer's
rows, including node-defect hashes: three parity-lattice cases, one
cyclic q19 case and three 2-D Padua cases. The independently written
receipt SHA256 is
`dae51951071a74afa8ef452fcf138e6080d9281cd30e0cf4f7dee4bcea79d74e`
(3261 bytes). These finite controls check indexing and normalization;
the asymptotic proof is analytic and does not infer a limit from them.

## R4 coverage update — 2026-11-12

| Topic-relative file | SHA256 |
|---|---|
| final-d1/reconstruction.md | adb6b469a4f7391080f5e904a0d6555957564bd2e58ba5cef5cf96e6bd79ea1a |
| final-d1/weight-corollary.md | d99b58750a8e10de4431a275bccce995cf0b325f77c2be664d8be79c6bcddc51 |
| final-d1/general-weight-open.md | e1c8162f5051c777ecf55fbab5f933126d40a7741f67b0c4773e002343d6a6e6 |
| final-d1/README.md | 76abdecaf1fefae6409ace454098ae9108a57d98fd12e944bbaa815460bff811 |
| final-d1/ideas.md | c0e39d7e0262321f3dec7429f6fee4a8845424d37cd149563e2735ac9bd09a74 |
| final-d1/sources.md | 30cf32869a14e6adc6010a7db0ebb35d65adbca9e1d08a589110d09d780ba6a2 |

All six were read completely. README/ideas were checked as status and
provenance pointers, not as additional proof bodies. The source table
above distinguishes my own primary coverage from the developer's.
The reconstruction/source hashes include the subsequently added
Kuperberg section 7 coverage note, which was reread separately.

### Exact measure change and doubling

For fixed p>0 on the closed cube, v_i=p(x_i)w_i/c is positive and
integrates q against mu whenever deg(pq)<=2n-1. If k=2s or 2s+1,
r=n-ceil(k/2) gives respectively 2r-1=2n-1-k or 2r-1=2n-2-k.
Thus both parities satisfy the degree budget. For sufficiently large n,
q=1 is included, so normalization is automatic. The original positive
Chebyshev theorem applies to exactly the same node set. Since the loss
n-r is fixed, the binomial ratio tends to one and eventually absorbs
half the positive excess. No assumption of a uniform degree bound
over a varying sequence of p's is being made.

The arcsine interval estimate is valid uniformly up to both endpoints:
its density is boundedly comparable to (1-|t|)^(-1/2), and integration
on an interval gives the stated r/sqrt(1-|x|+r) expression up to
absolute constants. Large radii saturate the total mass. Coordinate
box products preserve doubling; the box inclusions for a Euclidean
ball and a finite number of box doublings give the asserted ball
version. Compactness supplies finite positive min p and max p, so
bounded density comparison preserves it. D1-05 is therefore a valid
routine source-dependent consequence, with ineffective constants.

### General doubling: conditional proof checked, hypotheses remain open

The arbitrary-measure projection identity alone does not imply an
exact Haar Fourier frame. The document identifies this failure and
does not use the unavailable identity. Under the expressly unproved
H1/H2, good original nodes number (1+o(1))D; removing o(n^3) bulk
exceptions preserves that count. Their eight reflected orbits are
distinct and interior, hence give 8(1+o(1))D atoms per n-period cell.

For completeness of this conditional reconstruction, a bounded-distance
pair in the reflected periodic lift must eventually belong to the same
reflection sector in every coordinate: different sectors are separated
by at least a constant times n*rho_n, including across the period seam.
For pairs from distinct original nodes, reflect the local displacement
back to the original sector and apply H2 with one displacement zero.
The octahedral F is invariant under coordinate sign changes. Thus the
projection estimate transfers to F, both near zero (uniform separation)
and on every bounded window (limiting orthogonality). Copies of a single
original node cannot form a close pair because n*rho_n diverges.
The stationary-law and Bessel arguments then apply with intensity
8/6=|O|. This verifies the conditional implication; it does not verify
bulk count or uniform moving-center kernel convergence for a doubling
weight. D1-06 remains **OPEN**, with no numerical evidence changing
that status.

The assumption checks are also correct. A point mass has a degenerate
polynomial form and only addresses support-centered doubling. For the
displayed curve the first coordinate gives a bi-Lipschitz lower bound,
and bounded derivatives give the upper bound. Uniform interval measure
therefore pushes to a measure doubling on that curve. A nonzero
polynomial restricts to a nontrivial exponential polynomial: j+sqrt(2)k
are distinct for distinct integer pairs (j,k), and the coefficients
are polynomials in t. Analytic continuation followed by removing the
largest exponent proves independence. Positive definiteness therefore
does not imply full support. Neither example is represented as a
counterexample to the full-cube, positive-density target.

### All-degree Padua and source consistency

Writing g=(1/2,n/[2(n+1)]), the proposed lift lattice is generated by
e1 and g. It contains nZ^2 since 2(n+1)g-(n+1)e1=(0,n), and e1 is
obtained from 2(n+1)g-(n,n). Its covolume is n/[2(n+1)], so its
n-period cell contains 2n(n+1) points, exactly the cyclic group's
order. These inclusions and counts establish equality with the full
lift. The limiting basis e1,(1/2,1/2) generates the displayed diamond
spectrum. The polynomial and Fourier defect counts agree with the
seven exact controls; no additional numerical run was necessary.

The independently read Marzo statements do not rule out the p=2
sphere setting. The AMO ball theorem and kernel limit have their stated
ball/weight hypotheses; the cube proof supplies neither a sphere nor
an arbitrary-domain extension. Kuperberg's stated local-density results
concern uniform simplex/polytope measures and do not state this
Chebyshev fixed-relative-excess theorem. His section 7 additionally
poses density minimization for periodic weighted Fourier cubature and
asks about nonlattice improvements; this is a substantive predecessor
for the limit framing and was reported to the developer/coordinator.
No claim of novelty for continuous Fourier cubature, kernel blow-up,
or compactness is justified by this audit. These extra comparisons
introduce no load-bearing theorem beyond GL1.1.

## Novelty scope and remaining review

Read the complete current `state/IDEAS.md`, 1154 lines including all
historical/superseding disposition and obstruction tables, SHA256
`d7ec3aa6cf36f72e8057bcb90d8ac6eae8bf285a5b17f12526b26472ff4bddef`.
The INDEX hash is
`1f6f2acea05a6c65e11ba54646a6db46dbd5b947bb058f233d11bc542401ae61`.
INDEX coverage here is targeted rows/source links and a mechanism search,
not a claim to have read every unrelated source or its full proof.
Search terms included spectral/Fuglede, critical density, orthogonal
exponentials, stationary/local limit, Christoffel defect, octahedron,
positive cubature, Li–Sun–Xu, sphere and designs.

Closest repository comparisons include IDEA-029/120 and their original
minimal-cubature seed; IDEA-207's known commuting-extension theory;
the T9 Haar/phase/packing reduction and strictly-positive unshifted
negative record; the MZ Gram/leverage and signed-rule obstructions;
and the exact inherited S2/S4 C1 sketch. Full linked T9 proof bodies
were read. Full Li–Sun–Xu, Degani–Schiff–Tannor, Collowald–Hubert and
Xu–Pitman source records were read with their own coverage limitations;
reading those records does not constitute fresh primary reading.

The correct distinction is the extension from subgroup-support
restrictions to arbitrary positive cubature nodes through a fully
proved stationary limit. It is an assigned continuation of C1, not a
newly proposed mechanism. The newly completed asymptotic assertion may
be significant, but this bounded audit establishes no historical
priority or exhaustive literature absence. Sphere/disk and general
doubling claims cannot be imported from the cube proof. The R4 records
preserve those scope limits. The required formal Claude acceptance
remains a separate step and is not supplied by this supplemental audit.
