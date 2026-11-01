# Independent B1 top-form and leakage check

Codex `/root/a5_checker`, assigned gpt-6.1-sol xhigh for mathematics;
runtime-resolved serving metadata is unexposed. Rules read at
`d8b878b348a94575e7753e5a756d969d41d5bca8`. Root started B1 at
2026-11-01 16:35:09 UTC, with hard ceiling18:35:09 UTC. This worker owns only
this new file. No A4/B3/A5 reopening, Git, handoff or shared-file mutation is
authorized. This is supplementary independent mathematics, not Claude audit.

## Actual reading and refreshed relaxed gate

Read the full user request, AGENTS, WORKFLOW and Codex role; the results-only
rule update does not change mathematics or override the user's topic-only
write restriction. Read B1 input preparation, the complete part1 T-B1 optional
attempt, OPEN_TARGETS B1 and its finite-sampling/general-position hypotheses,
the full decisive-gen1-3 and adversarial-gen1-3 records, the complete current
IDEA192 candidate and PD-N040 negative, window_exact.py, and orf2d.py's space,
pole-class, inner-product and generation/projection definitions. The historical
"EXACT blocks" diagnostic uses floating QR/SVD; it is not an exact rank proof.
Pdiag and Mpt source coverage are kept distinct. The failed real-division
closure argument in part1 is retained, not silently reused as a proof.

Before generation, freshly scanned the entire783-line state/IDEAS.md in
bounded chunks: all headings, IDs, aliases, summaries, every obstruction and
disposition table, including historical/current Lanczos rows, programme rows
and new MZ rows. Truncated aggregate displays were re-read in bounded chunks.
Searched top form/top-form, lower block, one linear pole, rational window,
windowed rational, project two/constrain one, gauge/skew, Ldiag/Pdiag/Ppt/Pbhh
across state, programme candidate/theory, part1, Lanczos theory and literature
INDEX. Closest full shortlist: IDEA192 and its linked PD-N040/source records;
IDEA035/051 and Lanczos fixed-start/top-form records are contextual neighbours,
not inherited rational-window identities. All obstruction tables were read.
The source's skew-rank and generation assertions remain conditional; candidate
space generation alone cannot identify the constrained projected remainder.
No novelty, priority, primary-source completeness or numerical proof claim is
made. This is completion of the registered B1 step, not a new programme.

## Registered bounded candidate before mathematical development

Candidate B1-C1: describe the lower leakage of the projected candidate via a
linear functional on the degree-(t-2) binary forms, then prove detection by
W_(t-2) for real parallel Ldiag poles (normalization and class to be coordinated
with the lead before assuming it). Closest entry: the registered top-form/gauge
sketch in adversarial-gen1-3(ii)(1), plus part1's explicit next step.
Verdict: continuation/variant of that registered mechanism, no novelty claim.

Separation from the incomplete sketch: an actual injectivity statement for the
LOWER LEAKAGE after projecting, retaining arbitrary positive determining
samples, rather than generic generation/skew ranks. Cheapest decisive test is
an exact symbolic factorization of every old-block inner product through one
top-form functional. Kill: a term depending on a lower numerator component
that cannot be represented by that functional, or a nonzero functional whose
restriction to W_(t-2) vanishes without killing its older-block image. If a
rank witness is needed, it must specify whether it varies nodes/weights or
only poles and prove a proper exceptional set for the claimed quantifiers.

No mathematical computation is preregistered or executed here. Any future
script requires separately assigned prefix, frozen scope and actual
different-agent rerun. Current approach is purely analytic.

## Analytic detection: the actual projected lower leakage

Write ell=ell_(t+1), d=t-2. Work over real sampled vectors with
<f,g>=sum_i w_i f(z_i)g(z_i), w_i>0. Evaluation on V_(T+1) is injective,
all pole values are nonzero, and2<=t<=T. The real poles considered below
have ell/ell_d of one strict sign on the nodes when d>=1. In particular this
holds for exterior parallel lines on the same side of the support.

Let K_d=Pi_(d-1)/pi_d, with K_0={0}. If f in K_d, then f,xf,yf and ell*f
all lie in V_d. For c=(a+b+xv+yw)/ell in C_t, where a in W_(t-1) and
b,v,w in W_t, it follows that <ell*c,f>=0. If
r=c-P_(W_t)c-P_(W_(t-1))c, self-adjointness of multiplication by ell gives

    <ell*r,f>=0 for every f in K_d.                         (B1)

Indeed the subtracted terms pair with ell*f in V_d, and both projected
blocks are orthogonal to V_d. By linearity this holds for every r in R_t.
Consequently there is a unique functional nu_r on the homogeneous binary
forms H_d such that

    <ell*r,p/pi_d>=nu_r(top_d p), p in Pi_d.                (B2)

This is an exact top-form description of the ell-weighted low pairings. It
does not assume the adversary's gauge rank or a top-numerator isomorphism.

For the ACTUAL unweighted lower pairings, let E_d(p/pi_d) be the restriction
of p to the new affine pole line ell=0. Its values are univariate polynomials
of degree at most d on that line, equivalently homogeneous binary forms of
degree d after ordinary homogenization. The restriction map is onto and its
kernel is ell*K_d, by polynomial division by a nonconstant affine linear
factor. Identity(B1) says that <r,q> vanishes on this kernel. Therefore a
unique functional gamma_r on that(d+1)-dimensional polynomial/form space
satisfies

    <r,q>=gamma_r(E_d q), q in V_d.                       (B2a)

In the parallel coordinates ell_j=x+y-c_j, take x as a coordinate on the
new line y=c_(t+1)-x. If f=p_s/pi_s lies in W_s,0<=s<=d, its unique common
numerator in V_d gives the explicit lower-block formula

    <r,f>=gamma_r( [product_(j=s+1)^d(c_(t+1)-c_j)]
                              p_s(x,c_(t+1)-x) ).         (B2b)

An empty product is1. Coincident factors cause no singularity in this
formula. No sample relation is assumed: uniqueness of each numerator
follows from determining evaluation. These are all lower leakage
coefficients, parametrized by just d+1=t-1 numbers.

Restriction E_d is an isomorphism on W_d in the exterior class. Indeed,
if q in W_d has numerator ell*P, put g=P/pi_(d-1) in V_(d-1), so
q=(ell/ell_d)g. Then0=<q,g>=sum_i w_i(ell/ell_d)(z_i)g(z_i)^2 forces
g=0. Injectivity and equal dimension d+1 give bijectivity. Thus testing
<r,W_d>=0 sets the ENTIRE gamma_r to zero, including its values controlling
every older block. This is a second direct proof of detection. For d=0,
restriction on constants is the identity and the conclusion is immediate.

To prove detection, impose r perpendicular W_d. Since R_t lies in V_(t+1)
and is perpendicular W_t+W_(t-1), the orthogonal block decomposition gives
r=h+u with h in W_(t+1) and u in V_(d-1). For d=0 the latter is zero,
which already proves detection. For d>=1, h also satisfies(B1), because
ell*f lies in V_d and h is orthogonal to V_t. Hence ell*u is perpendicular
K_d. But u/ell_d lies in K_d: if u=p/pi_(d-1), its numerator there is p
of degree at most d-1. Testing with that vector yields

    0=<ell*u,u/ell_d>=sum_i w_i (ell/ell_d)(z_i) u(z_i)^2.

The ratio has one strict sign, so u=0 as a sampled vector. Thus

    {r in R_t:r perpendicular W_(t-2)} subset W_(t+1).     (B3)

This proves detection for all admissible t and all such exterior real pole
tuples, independently of candidate-space generation. It does not yet prove
the reverse inclusion. No dimension count has been used to assume it.

The other independent worker separately obtained the equivalent direct
description: lower pairings of r factor through restriction of the numerator
of q in V_d to the NEW affine pole line. Its kernel is ell*K_d. Restriction
on W_d is bijective by the same sign-ratio positivity. That is a separate
reconstruction of detection; it is not a computational rerun.

## Structural pole-only rank witness: coalescence and projective coordinates

The following supplies the missing generation modulo the two projected
blocks, without assuming unprojected W_(t+1) subset C_t or the source's skew
form ranks. Fix ANY finite real node set and positive weights with evaluation
injective on Pi_(T+1), T>=3. Put u=x+y and choose c_* nonzero and larger than
max_i u(z_i). Let L=u-c_*. At the coalescent tuple ell_s=L for every
1<=s<=T+1, define sampled projective coordinates

    X=x/L, Y=y/L, a=1/L=(X+Y-1)/c_*.

No node meets L=0. At EVERY degree s<=T+1,

    V_s=Pi_s(X,Y).                                        (B4)

Forwards: p(x,y)/L^s is a polynomial of degree at most s in X,Y, replacing
x/L by X,y/L by Y and each remaining factor1/L by the affine a. Conversely
X^iY^j=x^iy^j L^(s-i-j)/L^s belongs to V_s for i+j<=s. This also proves
that the transformed nodes are Pi_(T+1)-determining. The positive inner
product is unchanged. The blocks W_s are now ordinary total-degree
orthogonal polynomial blocks in X,Y.

The exact polynomial three-term block property follows directly from
self-adjointness and degree: multiplying W_s by any affine function gives
components only in W_(s-1),W_s,W_(s+1). No floating recurrence is involved.
The coalescent candidate space is

    C_t=span{a W_(t-1),a W_t,X W_t,Y W_t}.

Projecting off W_(t-1),W_t therefore leaves vectors in
W_(t+1)+W_(t-2). The forward components of XW_t and YW_t span W_(t+1):
the top-form map of an ordinary polynomial block is bijective, and
X H_t+Y H_t=H_(t+1). Subtracting degree-at-most-t terms does not change that
surjectivity. Thus these candidates independently supply ALL W_(t+1).

The projected a W_(t-1) is exactly its backward component in W_d. That
backward map is onto W_d, because its adjoint is the forward map

    W_d -> W_(d+1), f -> P_(W_(d+1))(a f).

This map is injective: a has nonconstant linear part(X+Y)/c_*, f nonzero
has degree d, and top_(d+1)(af)=((X+Y)/c_*) top_d f is nonzero. If the
projection vanished, af would be represented in Pi_d on the determining
transformed nodes, contradicting degree and injectivity through d+1.
Adjointness in a positive finite-dimensional inner product proves the
backward surjectivity. This also covers d=0.

We have proved, at this SAME admissible coalescent tuple for every2<=t<=T,

    R_t=W_(t+1) direct-sum W_(t-2),
    dim R_t=2t+1.                                        (B5)

Coalescence is used as an exact structural rank witness. It is not claimed
to be a distinct-pole general-position tuple. Because the relevant rank
minor is nonzero there, it will also be nonzero for nearby distinct tuples;
the next subsection makes the pole-only algebraic quantifiers precise.

## Proper algebraic exception in POLES, with node data fixed arbitrarily

Fix the preceding node set, positive weights and T>=3. Choose an exterior
parallel Ldiag class ell_s=x+y-c_s with independent real parameters
c=(c_1,...,c_(T+1)) in the open region c_s>U, where
U=max(0,max_i(x_i+y_i)). Multiplying individual factors by nonzero constants
does not change any V_s,W_s,C_t or R_t, so this is the normalized source
parallel-line class. On nodes in[-1,1]^2, the usual outward source class
c_s>2 is a subregion of the same argument. A fixed taper formula is NOT
substituted for these independent offset parameters.

Let D=diag(w_i). Use evaluated total-degree monomial matrices E_s(c), whose
entries are monomials divided by pi_s. They have full column rank throughout
the admissible domain: multiplying rows by pi_s reduces to the fixed
Pi_s-determining evaluation matrix. Thus

    P_(V_s)=E_s(E_s^T D E_s)^(-1)E_s^T D,
    Q_s=P_(W_s)=P_(V_s)-P_(V_(s-1))                       (B6)

have entries rational in the pole parameters. E_-1 and P_(V_-1) mean zero.
The columns of Q_s span W_s, so the following rational matrix has column
space EXACTLY R_t, with no basis selection or radical normalizations:

    G_t=(I-Q_t-Q_(t-1)) diag(ell_(t+1))^(-1)
                 [Q_(t-1), Q_t, diag(x)Q_t, diag(y)Q_t].  (B7)

Choose a polynomial common denominator q_t for its entries that is nonzero
on the exterior domain: the node pole values and the positive Gram
determinants in(B6) suffice after clearing their own denominators. Put
A_t=q_t G_t and define F_t as the sum of squares of ALL(2t+1)-minors of A_t.
This is an explicit finite polynomial definition, not a computed numerical
rank threshold. At the coalescent tuple c_s=c_*>U, choose c_*>0. Statement(B5)
proves F_t(c_*,...,c_*)>0. Consequently

    F=product_(t=2)^T F_t

is a nonzero polynomial in the pole parameters for THIS arbitrary fixed
sample and weights. The exception Z={F=0} is proper algebraic. Its defining
coefficients may depend on the fixed sample/weights; it is not asserted to
be a single data-independent polynomial simultaneously valid for all data.

For c outside Z in the exterior domain, dim R_t>=2t+1 for all2<=t<=T.
Restriction of the inner-product constraint to W_(t-2), which has dimension
t-1, imposes at most t-1 independent equations. Its kernel in R_t therefore
has dimension at least t+2. By(B3) this kernel is contained in W_(t+1), whose
dimension is exactly t+2. Hence

    W_(t+1)={r in R_t:r perpendicular W_(t-2)}             (B8)

for EVERY2<=t<=T simultaneously. The same reasoning also gives
dim R_t<=2t+1 in the exterior domain, so the generic rank is exactly2t+1
and the constraint rank exactly t-1. These dimensions are consequences,
not premises imported from the old measurements.

If distinct offsets or any specified ordering are required, add the
collision factor product_(i<j)(c_i-c_j) to F. This product remains a nonzero
polynomial: F is nonzero at coalescence, each collision factor is a nonzero
polynomial, and the polynomial ring is an integral domain. Its complement
meets EVERY nonempty open ordered exterior region. Equivalently one can
perturb the coalescent witness slightly into any strict order while retaining
F nonzero. Thus the genericity is in the actual pole parameters for every
fixed admissible sample, not merely in joint node-weight-pole data.

This is a structural all-admissible-data proof of properness, and requires
no exact computational witness or independent execution. It does not assert
(B8) on the remaining algebraic exception or for arbitrary nonparallel or
complex/conjugate-pair lines. No claim of full rank on a fixed one-parameter
tapered curve follows just from nonvanishing in the independent offsets.

## Independent coordination and current scope

The other independent analytic worker reconstructed the coalescent argument
in full and reported no blocker, including both forward generation and the
backward-adjoint surjectivity. The lead and parent received the derivation
before any status promotion. The proof never relies on the adversary's
unproved skew-rank assertion, unprojected generation, a floating rank witness,
or a perturbation of the nodes/weights. It covers any finite T>=3 allowed by
M>=dim Pi_(T+1) and injective evaluation, including t>=3 where lower-block
leakage detection has nontrivial content. The t=2 case is retained as a
boundary case, not presented as completion by itself.

Current bounded result: the requested identity is analytically established
for the stated exterior parallel pole class outside the explicitly defined
proper algebraic exception for each arbitrary fixed admissible sample.
The literal original all-pole-class target remains OPEN beyond that class;
finite-precision stability of a recurrence is a separate question, and
PD-N040's tested implementation failure is unchanged. Claude audit PENDING.

No mathematical code, rank calculation or numerical fit was executed.

## Candidate dispositions retained

- B1-C1, registered leakage/detection continuation: **retained**, with(B1–B3)
  supplying the promised top-form functional and structural positivity
  detection. This is the source-prescribed next step, with no novelty claim.
- B1-C1a, trying to deduce generation from surjectivity onto the newest
  quotient alone: **abandoned as insufficient**. A subspace can surject onto
  W_(t+1) while being a graph over it with lower leakage; surjectivity alone
  would not put pure W_(t+1) into R_t. No target refutation follows.
- B1-C1b, full generic rank from the source's gauge/skew statement or a joint
  data witness: **not used**. Those premises would leave the required
  fixed-node/pole-parameter quantifier unresolved.
- B1-C1c, the coalescent-pole/projective structural witness: **retained**.
  It proves the rank separately for every arbitrary fixed admissible sample
  and supplies the pole-only nonzero polynomial required by the target.
  Difference from the incomplete source sketch is the rank of the PROJECTED
  candidate space, not generation of an unprojected numerator window. The
  cheapest kill check was the exact forward/backward decomposition after
  coalescence; a missing backward-adjoint surjectivity would have killed the
  witness. Both maps were proved above and separately reconstructed.

No rejected mathematical mechanism with a new negative claim was established,
so this worker requests no PD-N allocation. The pre-existing closure obstacle
and finite-precision implementation failure keep their original scopes.

## Parent-requested bounded corollary for the actual fixed taper

Parent proposed this corollary after reading(B1–B8); independently
reconstructed here before lead adoption. It is a continuation of the same
registered pole class, using only an elementary real-exponential zero bound,
not a genericity inference from an arbitrary analytic curve. Additional
Rolle/exponential-polynomial/Chebyshev-system keyword search found no closer
registered B1 mechanism; no novelty or external theorem attribution is made.

Fix m=T+1>=4, fix either the source's far-first or near-first ordering, and
write d_j=sqrt(m)-sqrt(j), j=1,...,m. In normalized coordinates the actual
Ldiag taper is

    c_j(sigma)=2+sqrt(2)*exp(-sigma*d_j), sigma>0,

up to that fixed permutation. The source library asserts an even final n
for all classes, though this real Ldiag formula is well-defined for every
m; to retain that literal implementation convention one may take m even,
equivalently T odd. The mathematical formula and proof require only m>=4.
The fixed final m is chosen once; every degree uses its prefix, as in the
source, rather than silently retapering at each intermediate degree.

Use the rank polynomial F from(B7–B8), WITHOUT multiplying by the collision
factor. At sigma=0 all c_j equal2+sqrt(2)>2, so the coalescent proof gives

    f(sigma)=F(c_1(sigma),...,c_m(sigma)), f(0)>0.          (B9)

Because F is a polynomial, f is a finite linear combination of real
exponentials. After combining all equal exponents and deleting zero
coefficients it has L>=1 nonzero terms with distinct real exponents. It
has at most L-1 distinct real zeros. Proof by induction: for L=1 there are
none. Otherwise factor the smallest exponential. The derivative of the
remaining constant-plus-exponentials has L-1 distinct nonzero terms, hence
at most L-2 zeros by induction. If the original had L distinct zeros,
Rolle would give at least L-1 derivative zeros, a contradiction. The same
argument rules out infinitely many zeros by selecting any L of them.

Thus Z_sigma={sigma>0:f(sigma)=0} is FINITE. For every sigma>0 outside that
set, all simultaneous conclusions(B8) hold. The offsets are automatically
distinct for sigma>0, because the d_j are distinct; their prescribed order
does not change. The source nearest-distance parameter is

    epsilon_min=exp(-sigma*(sqrt(m)-1)),

a bijection(0,infinity)->(0,1), so its exceptional set is finite as well.
This is stronger than a merely nowhere-dense analytic exception. A finite
set of real parameter values is proper real-algebraic: its points are the
zeros of the product of linear factors over that set, with real
coefficients (the empty set can use polynomial1). No claim that those
coefficients or exceptional values are rational/algebraic numbers is made.
Their finite description by(B9) is exact; no zeros have been numerically
located.

This proof certifies the generic fixed-taper family, for every arbitrary
fixed admissible node set and positive weights. It does NOT certify any
particular taper parameter in the stored floating tests. It also does not
assert that every polynomial nonzero on the ambient offset space would be
nonzero on an arbitrary analytic parameter curve: nonvanishing here comes
from the shared coalescent point and finiteness from real exponential
structure. No computation was performed or needed.

## Actual independent full-file inspections

The complete durable90,91 and92 were independently read after they were
written; no mathematical finding was identified. This is a full-file read,
not an assumption that previously exchanged derivations match the final
proof. In particular the following were reconstructed:

- Record90's literal homogeneous next-pole top form
  tau_(a,k)(p)=sum_(d=0)^k(s/a)^(k-d)p_d has kernel(s-a)Pi_(k-1) and is
  onto H_k. Its projective interpretation is exact: with X=x/(s-a),
  Y=y/(s-a), the homogeneous degree-k part of p(x,y)/(s-a)^k is exactly
  tau_(a,k)(p)(X,Y). Thus this is an actual top form, not a relabeling of
  the original-at-infinity numerator truncation. The latter source gauge
  ranks are explicitly not assumed. Positive new/old pole ratio proves
  the detector isomorphism, and the paired projection map proves the
  universal rank upper bound without assuming reverse inclusion.
- Record91's exact projective coordinate flag equivalence, forward
  W_(t+1) generation and backward-adjoint surjectivity, including t=2,
  give rank2t+1 for EACH fixed admissible dataset at every coalescent
  c>2. Its explicit denominator construction h_j,B_j,g_j,G was checked:
  B_j is polynomial and full rank; g_j is strictly positive; at most two
  projector factors and one evaluated diagonal inverse occur in M_t,
  so q_t=G² product_i ell_(t+1)(z_i) clears every entry. Sum-of-squared
  maximal minors and the separately appended collision factor give a
  proper pole-only exception. A coalescent witness need not itself avoid
  the collision factor. All strict ordering chambers meet the rank-open
  neighbourhood. No generic-node premise is hidden there.
- Record92 uses rank2t+1 and at most t-1 constraint equations, then the
  exact detector, to prove BOTH inclusions. Its data/pole quantifier
  order, finiteT>=3, all required degrees, source normalization,
  unrestricted-class limitation and numerical-stability separation were
  checked. It does not silently promote the broad source B1 statement.

The other worker's full independent-checks-b1-topform.md was also read.
Its homogenized all-lower-block formula includes the required H^(k-j)
factor, and its original-at-infinity Top_j isomorphism is proved by the
strictly negative ell_j sum of squares. Its direct pole-line and homogeneous
form descriptions agree with(B2a–B2b) and90. The coalescent witness is
attributed to the primary checker and separately reconstructed. No blocker
was found. Earlier lead wording implying separately originated ideas was
flagged for a provenance-only change to "independently reconstructed";
the proof and its validity were unaffected.

The complete durable93 was then independently read after it was written;
no finding was identified. Checked its literal even-m implementation
restriction, T=m-1>=3 and fixed-length prefixes; separate substitutions
for both far/near orders; grouping equal real exponential rates before the
Rolle induction; nonzero coalescent P_0 WITHOUT the collision factor;
automatic distinctness for sigma>0; finite union for the two orders; the
epsilon_min bijection and real-coefficient algebraic-set meaning. The
theorem does not certify a stored individual taper parameter or silently
extend the source library's even-degree coverage. Its mathematical formula
would be well-defined at other lengths, but93's exact statement retains
the literal source restriction. No mathematical run is pending.

All four durable files90–93 have therefore received actual full-file
independent inspection, in addition to the exchanged analytic derivations.
Final whole-file pins will be recorded after the lead's status/provenance
metadata synchronization. Required Claude audit remains PENDING.

## Stop and final verdict

Root stopped B1 mathematics at2026-11-01 16:57:37 UTC, at the completed
one-class done criterion, well before the original18:35:09 ceiling. All
mathematical derivations and full90–93 inspections above were completed
before that stop. Only this administrative consolidation, status-wording
read and final content hashing followed. No mathematical computation,
counterexample search or additional proof development was performed after
stop. No mathematical script or source module was executed anywhere in this
worker's B1 task, so there is no missing independent computational rerun.

Final independent verdict: no unresolved mathematical finding in the four
written class results90–93. The top-form functional describes every lower
pairing; W_(t-2) detects every leakage direction for ALL outward offsets;
the structural coalescent witness proves generic pole-only rank for every
fixed admissible sampled measure; rank and detection prove exact extraction
simultaneously through any finite admissibleT>=3. The literal even-count
source taper has at most finitely many exceptional positive parameters,
simultaneously for near/far orders. This covers a meaningful t>=3 range.

This verdict does not certify any individual stored floating taper parameter,
classify the exceptional offsets, prove floating-recurrence stability, extend
the source implementation to odd pole counts, close the other real/complex
pole classes, or supply an unlimited-degree result on fixed finite nodes.
The original broader B1 target remains OPEN beyond these exact statements.
This is supplementary independent reconstruction, not the required Claude
audit; the latter remains PENDING. Root owns all integration, status and
handoff/Git work. This worker made no such writes.

Administrative coordination correction: early messages intended for the B1
lead used the old `/root/a5_n4_checker` alias. Root received every substantive
derivation and inspection confirmation directly. The live lead was then
identified as `/root/a5_n4` and received the consolidated full-read/stop and
provenance notice. No read, execution or receipt acknowledgement is inferred
from delivery to the old alias; the written final proofs were inspected
directly and match the mathematics recorded above.

## Final frozen inspection bindings

Lead then promoted90–93 to PROVED at their exact class scopes by metadata
edits, retaining Part2 Claude audit PENDING. Final status/inspection and
reconstruction-provenance wording was read; the91 History now says the
coalescent proof was independently reconstructed, without claiming separately
originated ideas. The lead's administrative before/after guard reports that
every Proof body is byte-identical. The final whole-file identities below
were independently hashed by this worker after the metadata synchronization.
This hashing is content identification only, not mathematical computation.

| File under theory/ | Bytes | SHA-256 |
|---|---:|---|
| `proof-attempts-2-codex-90-pole-topform-detection.md` |9520|`fc18d4e83e23607783d3968c387b5dd0b5101faa82c92f2a44365d1ee396f972`|
| `proof-attempts-2-codex-91-pole-only-generic-rank.md` |10381|`732c5bd93aa751514fc61fed5322e4062e96e4090cad0ad82588a847a2484eb9`|
| `proof-attempts-2-codex-92-generic-ldiag-constrained-window.md` |6705|`8261bd243e633c2d9532c17aadb3137820dfbd7f66583d28010152a9ecf59229`|
| `proof-attempts-2-codex-93-source-ldiag-taper.md` |6698|`563fae640d26f49d88cc773aa339f3fc472abceed7d61def120d42337ff2c614`|

Read the entire `outputs/b1_status_metadata.json`:2847 bytes, SHA256
`05005e5fe5f3ead035e97741c5102155bf60906a8167bde8c52742ac8892da4a`.
It records the actual stop time, old/new whole-file hashes, equal old/new
Proof-body hashes, metadata-only scope and no mathematical computation.
This is the lead's administrative guard, not an independent mathematical
execution. Current files match its final whole-file bindings. Any later
scientific edit requires renewed inspection; no unseen proof change is
silently covered by this receipt.

This receipt is ready for root's final checkpoint and frozen once its own
content hash is reported. No continuation of B1 mathematics is requested.
