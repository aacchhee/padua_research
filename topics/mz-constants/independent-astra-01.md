# Independent adversarial reconstruction and audit 01

Rules SHA: `d36722823441dc40c6e19d69a174459348dd309c`.
Date: 2026-10-31. Auditor: separate Codex agent, assigned model
`gpt-6-astra`, effort `xhigh`. Scope: independent reconstruction and adversarial
audit of M1/M2, with foundational CC/Padua implications and candidate-gate review.
This is not a third substantive development direction and does not replace the
required Claude handoff, which remains **PENDING**.

Current status: **SCIENTIFIC AUDIT AND FINAL ALLOCATION / MANUSCRIPT IMPACT REVIEW
COMPLETE**, within the scopes and hashes recorded below and in the accompanying
auditor input manifest. The chronological initial checkpoints are retained;
the final addendum supersedes their pending allocation/manuscript wording.
No novelty or final publication-readiness acceptance is given. Required Claude
cross-provider audit remains **PENDING**.
Only this report and `tracks/mz-constants/evidence/astra-*` are auditor-owned.
No Git operations or developer-file edits are performed.

## Read scope and prior-art limits

Read in full: `AGENTS.md`, `agents/WORKFLOW.md`, `agents/codex/CODEX.md`, the
complete initial 25-line `state/IDEAS.md`, `literature/INDEX.md`,
`topics/mz-constants/plan.md`, `topics/mz-constants/literature-search.md`,
`literature/records/mz-input-reports.md`, and the theory/evidence templates.
The initial registry and published-statement index were empty; that supplies no
external novelty evidence. Searched ideas, tracks, topics, and literature for
Hankel, positivity, marginal, eta, U, cardinal, Lagrange, and logarithmic terms.
Read the supplied Hankel, Padua marginal, CC/Padua checking, and B2/B2b scripts as
untrusted proposed mechanisms. No supplied claim is adopted as proof.

The M0 literature worker's source reports identify ASV, An–Wu, Sloan–Smith,
Mastroianni–Milovanović, and general weighted MZ/interpolation literature as
relevant. I have not independently read those primary full texts at this initial
checkpoint. Their report is reading evidence, not a proved novelty verdict.
The final seeded ideas registry must be reread in full before closing this audit.

## Independent mathematical reconstruction

Let N≥2, x_j=cos(jπ/N), and let Q_N be the interpolatory quadrature for dx on
[-1,1] at these N+1 nodes. Write I_k=∫T_k dx: I_k=0 for odd k and
I_k=2/(1−k²) for even k. For p=Σ_(i=0)^n a_iT_i, n≤N−1, define
T_ij=(I_|i−j|+I_(i+j))/2 and Q_ij=Q_N(T_iT_j). These matrices represent
the continuous and discrete squared norms in Chebyshev coefficient coordinates.

**Hankel identity.** For 0≤s≤2N, nodewise cosine aliasing gives
Q_N(T_s)=I_s for s≤N and I_(2N−s) for s>N. Product-to-sum therefore gives
2(T−Q)=D with D_ij=0 for i+j≤N and
D_ij=I_(i+j)−I_(2N−i−j) otherwise. Active odd entries vanish. Active even
entries are positive in the restricted degree range because 2≤2N−i−j<i+j.
The identity requires no numerical evidence.

**Entrywise positivity is not positive semidefiniteness.** For every N≥5 set
i=floor(N/2), j=i+2≤N−1. Then D_ii=0 and D_ij>0, so this principal 2×2
minor has determinant −D_ij²<0. Since D has positive diagonal entries, it is
indefinite. At N=2 D=0; N=3 and N=4 give rank-one positive semidefinite D.
This kills only a proposed PSD-defect argument, not the upper-spectrum target.

**Upper-spectrum sign argument, reconstructed from the developer's proposal.**
Set A=2T−Q=T+D/2. For i≠j of opposite parity, A_ij=0. For same parity
and i+j≤N, A_ij=T_ij<0. In the active case put d=|i−j|≥2,
s=i+j, r=2N−s. Then
A_ij=−1/(d²−1)−2/(s²−1)+1/(r²−1)<0,
since r−d=2(N−max(i,j))≥2. Hence for every real a and v=|a|,
aᵀAa≥vᵀAv=vᵀTv+vᵀDv/2>0 for a≠0. The last strict inequality uses
continuous polynomial norm positivity and entrywise D≥0 only. Thus the strict
upper threshold survives independent analytic reconstruction. A pinned proof and
prior-art disposition are still needed for final acceptance.

**Positivity and eta.** Once positivity of CC weights is separately established,
the sampled norm is positive definite on Π_n for n≤N, because a nonzero such
polynomial cannot vanish at N+1 distinct nodes. For the continuous-orthonormal
Gram matrix G, eta=||I−G||_2=max(1−lambda_min,lambda_max−1), since the constant
polynomial has Rayleigh quotient one. Consequently eta<1 is equivalent to
lambda_max<2 in this range. Signed Padua weights do not inherit this positivity
argument. If n≥N+1, the nodal polynomial gives a zero sampled norm.

**U witness, with parity accounted for.** U_(N−1)(cosθ)=sin(Nθ)/sinθ is zero
at every interior node and equals ±N at the endpoints. Its exact continuous norm
is 2Σ_(k=1)^N1/(2k−1): after x=cosθ, consecutive N values differ by
∫_0^π sin((2N−1)θ)dθ=2/(2N−1), starting with norm²=2 at N=1.
The endpoint CC weights are 1/N² for odd N and 1/(N²−1) for even N, so
Q_N(U_(N−1)²)=2 for odd N and 2N²/(N²−1) for even N. Its quotient is
O(1/log N), forcing lambda_min→0 for any degree range containing U_(N−1).
It does not establish a matching O(log^−2 N) quotient.

**Full-degree obstruction.** T_N² equals one at every CC node, while
∫T_N²=1−1/(4N²−1). Its discrete/continuous quotient is
2(4N²−1)/(4N²−2)>2 for every N≥1. Thus the upper threshold cannot extend
to Π_N. This is compatible with strict positivity of the full-degree Gram matrix.

**Padua marginal and its limit.** For any interpolatory Lebesgue Padua rule exact
on total degree≤m whose x coordinates are cos(jπ/m), grouped x weights A_j obey
ΣA_jr(x_j)=2∫r for every r∈Π_m. Uniqueness of interpolatory weights gives
A_j=2w_j^CC. This proof permits signed individual Padua weights. The embedding
p(x)↦p(x)/√2 into two-dimensional L² is isometric and preserves the discrete
form, so the CC Gram matrix is a compression of the Padua matrix. Therefore
lambda_min(Padua)≤lambda_min(CC), lambda_max(Padua)≥lambda_max(CC), and
eta(Padua)≥eta(CC), for the same degree n≤m. The factor two is essential.

**Major implication gap in imported F7.** A vanishing upper bound on lambda_min
alone yields liminf eta≥1; it does not yield eta→1. For example, diagonal Gram
matrices with eigenvalues epsilon_N,1,3 and epsilon_N→0 satisfy the same lower
spectral behavior while eta=2. The CC strict upper bound, once proved, supplies
the missing limsup bound for CC. Marginal domination transfers no such upper
bound to Padua. A Padua eta→1 statement remains unsupported by the marginal
argument alone. At full degree n=m, T_m already gives eta(Padua)>1.

## M2 threats and revised mechanism

1. The imported alternating normalized-node vector
   y_j=(−1)^j/sqrt(max(min(j,N−j),1)) is a full-degree nodal vector. For
   degree≤N−1 it must satisfy Σ_j(−1)^jy_j/(c_j sqrt(w_j))=0, where c_j=2
   at endpoints and 1 otherwise. The proposed vector violates this constraint.
   A full-space large quotient cannot establish the desired restricted-space
   upper bound on lambda_min.
2. A naive argument combining the Lebesgue constant with
   ∫|ell_j|≤C log(N)w_j fails at endpoints: ∫|ell_0| has order 1/N but
   w_0 has order 1/N². This does not reject a weighted cellwise Schur argument.
3. The developer's revised witness is
   p_N=Σ_(m=1)^M[U_(N−1−2m)−(1−2m/N)U_(N−1)]/m,
   M=floor((N−1)/2). Independently checked: degree≤N−1, both endpoints
   vanish, and interior values are −(−1)^j B_M(θ_j)/sinθ_j, with
   B_M(θ)=Σ sin(2mθ)/m. In the continuum,
   p_N(cosθ)=[sin(Nθ)C_M(θ)−cos(Nθ)B_M(θ)]/sinθ, where
   C_M=Σ(cos(2mθ)−1)/m+2M/N. Uniform boundedness of B_M and
   C_M≤−(1/2)log N+O(1) on [N^−1/2,1/4] suggest Q=O(log N) and
   norm²≥c log³N. The quantified proof, small-N treatment, and literature
   comparison remain under audit; this checkpoint does not certify them.

## Candidate dispositions at the initial checkpoint

| Candidate | Scoped prior-art threat | Adversarial disposition |
|---|---|---|
| M0 literature baseline | Primary versions, historical norm-equivalent results, errata | IN PROGRESS; source-reading coverage needs final review |
| M1 sharp upper spectrum | Exact CC/Lebesgue norm inequalities in CC product integration/MZ sources | Analytic sign argument survives; novelty and pinned audit PENDING |
| M2 endpoint log-squared behavior | Lobatto l²-to-L² interpolation norms and weighted endpoint MZ theorems | Revised lower/upper arguments pending pinned quantified proofs |
| M3 fixed ratio | General weighted MZ plus exact upper-constant requirements | DEFERRED; no accepted theorem claimed |
| M4 Padua | Existing marginal/interpolatory exactness facts and Padua spectrum studies | Foundational marginal reconstructed; endpoint eta limit remains OPEN |
| M5 other rules | Rule/measure-specific classical MZ theory | DEFERRED; no proof accepted |
| M6 fast/certified computation | Hierarchical matrix theory, fixed-tolerance rank measurements | MEASURED only where actually rerun; no fast/certified theorem accepted |
| M7 manuscript | Requires accepted M1/M3 plus M2 or an explicitly scoped part | Gate NOT MET; no manuscript acceptance |

## Executed checks and pending handoff

The auditor wrote and separately executed
`tracks/mz-constants/evidence/astra-independent-check.py`, importing no developer
or supplied calculation. It reconstructs quadrature as integration of polynomial
remainders modulo (x²−1)U_(N−1). Exact Python rational arithmetic verifies the
alias identity, nonnegative D entries, nonpositive offdiagonal entries of A,
positive rational elimination pivots for A, indefinite minors, U norm/parity,
and full-degree T_N obstruction for N=2,...,20. Floating checks separately test
Padua marginal normalization at m=2,...,10 and full versus constrained cardinal
spectra at N=16,32,64,128. These checks are supplementary finite evidence, not a
computer proof of any all-N assertion.

Executed command:
```
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python tracks/mz-constants/evidence/astra-independent-check.py > tracks/mz-constants/evidence/astra-independent-check.json
```
Exit code: 0. No seed; all inputs deterministic. Python/NumPy versions and script
hash are in the output. Final artifact manifest will pin bytes and hashes.

The separately launched developer-runner replay uses the root-pinned runner
SHA-256 `fe88a16d2ac08df96dc5e18a224ac1b0d46d5cec4310cc86fff0f7fda1aa44ac`:
```
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python tracks/mz-constants/code/reproduce.py --suite all --max-N 1280 --output /tmp/mz-audit-reproduction.json > /tmp/mz-astra-reproduction-stdout.txt
```
At this checkpoint its completion and comparison are PENDING. The import emits
a divide-by-zero warning from `np.where` evaluating both branches at k=1; the
selected odd-moment result is zero, but output finiteness must still be checked.

Runs needed: finish replay and compare invariant results; receive final file
hashes for theory/ideas/literature/evidence; reread them; audit all changed proofs
and constants; record finding dispositions; retain the Claude handoff as PENDING.

## Subsequent independent source verification

The complete seeded 160-line `state/IDEAS.md` was read, including every M0–M7
entry and both tables. The final M0 search record and all ten `mz-*.md` literature
records were read. Their scope is appropriately bounded: inaccessible historical
texts remain FULLTEXT UNVERIFIED and there is no comprehensive novelty clearance.

On 2026-10-31 I separately opened these primary sources through the web connector:

- [ASV arXiv v1](https://arxiv.org/html/2601.04708v1): introduction, equations
  (7)–(10), and §3.1. The CC claim there is a finite numerical observation.
  Equation (7) already uses an upper-MZ hyperinterpolation factor with an aliasing
  term; equation (8) distinguishes least squares by inversion of the Gram matrix.
  The standard upper-Gram operator argument is therefore not treated as a novel
  mechanism. The new CC bound, if accepted, is a distinct input to that argument.
- [An–Wu arXiv v3](https://arxiv.org/html/2202.13691v3): definitions in the
  introduction and §4.1/Corollary 4.1. The corollary explicitly retains its
  theorem's conditions with eta=3/4. A failing eta hypothesis does not refute
  the conditional implication. Published-version comparison remains unverified.
- [Trefethen 2008](https://www.math.stonybrook.edu/~bishop/classes/math401.F09/Trefethen-Quad.pdf):
  abstract and Theorem 5.2 with formulas (5.2)–(5.4), printed page 78. This is
  direct prior art for the exact folded CC modes. The inspected statement does
  not supply the campaign's Z-matrix quadratic-form argument or sharp threshold.
  This is selected-text verification, not a complete paper or historical audit.

The actual connector commands were three URL `open` requests, followed by `find`
for `Corollary 4.1`, `Theorem 5.2`, and `3.1 The interval`. No third-party full text
was saved into the repository. The cloud-runtime skill and networking reference
were read, current enforced restricted policy was inspected, and no policy bypass
or configuration change was attempted.

## Completed numerical replay and M1 checkpoint

The all-suite reproduction replay completed with exit code 0. Its separate output
is `tracks/mz-constants/evidence/astra-reproduction.json`, SHA-256
`1511bfeb982f3e12b904acf151d9a586e6a65ee776dc464a12789a955ead4976`.
The comparison file `astra-replay-comparison.json` records identical runner and
source hashes, 637 numeric values compared, maximum absolute difference zero,
and no differences after removing only elapsed `[Ns]` fragments from source
stdout. The developer output hash is
`b85b06fa9b3317d6ce84f9d354626b74edad4e8f9885341ecad39166d4fd6d40`.
Its raw runner metadata still says the developer runner itself did not perform
an independent replay; this audit record supplies the separate-agent provenance.
The warning did not produce nonfinite recorded outputs.

The independent rational reconstruction passed all 19 N values, 2 through 20.
Its independently assembled Padua marginal maximum residual was
2.01574867908505e−15 for m=2,...,10. The normalized alternating-node trial's
relative constraint violation was between .9807 and .9828 at N=16,32,64,128;
this measurement illustrates an obstruction already established algebraically.

The M1 developer supplied stable hashes, which were checked before executing:

| Artifact | Audited SHA-256 |
|---|---|
| `code/m1_exact_check.py` | `7a9b32260a90684e16fcd023e031fd3b91d5ea21ecce2ff351bbc034d68552e3` |
| `theory/m1-cc-foundation.md` | `77e58ff93b916d169c6013ebf5085dc55d406ebdce277a09385efdce5804abf3` |
| `theory/m1-coefficient-floor.md` | `60d780befe615321e3a249550c32e7e1e644b258b45933afd24fbfce0ca42893` |
| `theory/m1-upper-bound.md` | `ef798918a10befc52fb72c64443942b87a97d59bc1b85424db88f09099122514` |
| `theory/m1-full-degree-obstruction.md` | `628e0f0a10df9e9f6f253d6d31f3a689f84eb9dcefe59847e6dc26c34744efd6` |

Paths in that table are relative to `tracks/mz-constants/`. Also read both M1
negative-result files and complete direction IDEAS/RUNS files. The weighted
continuous-mass floor was reconstructed, including its half-weight constant
coefficient and the i=0 telescoping factor. It yields the quantitative
2−2/(πN) upper bound as written. The N=5 unweighted row-dominance failure has
exact margin −2/35 and is correctly scoped as a failed sufficient criterion.

Executed separately, exit 0:
```
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python tracks/mz-constants/code/m1_exact_check.py --max-n 40 --float 2 3 4 5 6 10 20 40 80 160 320 > tracks/mz-constants/evidence/astra-m1-replay.txt
```
Exact N=2,...,40 checks all passed. Floating values agree with the developer
record to displayed numerical precision; final digits can differ by BLAS thread
configuration. This is an actual replay, supplementary to the analytic audit.

## Additional implication checks

For positive weights summing to V and continuous-orthonormal evaluation matrix
Phi, hyperinterpolation has coefficient vector PhiᵀWf. Writing
A=W^(1/2)Phi gives norm bound sqrt(lambda_max(G))sqrt(Q(f²)), hence
||L_nf||_(L²)≤sqrt(V lambda_max(G))||f||_infinity. There is no G inverse in
this operator. If the rule is exact through d≥n, reproduction holds on degree
r=min(n,d−n); the resulting error bound is
sqrt(V)(1+sqrt(lambda_max(G)))E_r(f). The minimum in r is necessary when d>2n.
This is a corrected applicability consequence, not by itself the fixed-ratio M3
theorem and not a new general hyperinterpolation mechanism.

At the endpoint n=N−1, accepted M1/M2 estimates would imply eta_N→1 and
kappa_2(G_N) of order log²N, since 1≤lambda_max<2 and lambda_min has order
log^−2N. They do **not** establish 1−eta_N of order log^−2N: exactly
1−eta_N=min(lambda_min,2−lambda_max), and the currently proved upper-spectrum
gap may be only of order 1/N. Eventual dominance of the lower-spectrum branch
and the sharp limiting upper constant near 1.004437 remain OPEN.

## M2 pinned proof audit and replay

The final developer pin was checked against disk before rerunning. Full proofs,
all seven candidate entries, the round log and the sharp-limit OPEN file were
read. Audited hashes under `tracks/mz-constants/`:

| Artifact | Audited SHA-256 |
|---|---|
| `code/m2_endpoint.py` | `71f516a44e4d1e46731b0e596b36ba8796577f823c11a267efaf6b71746142c0` |
| `theory/m2-cardinal-lower.md` | `76da1cbc0c88867eaf837f2ae2a9d3bc2112d376af4effaba5b5af18f3259f45` |
| `theory/m2-parity-upper.md` | `6513c1d598fd8adb4cc33e40fc9f7f31502c3981e7bed8a70fb66115e815605c` |
| `theory/m2-u-witness.md` | `4413095f8d9bb0c86426fc7fba17f9d6e6824b00393af5ec93dea8f14625b024` |
| `theory/m2-eta-counterexample.md` | `0814bf8bad091de72398051fb0e67674f6a59cc1cc62bb830225dda0e6ebd1dc` |
| `theory/m2-l1-obstruction.md` | `47c6a3339168d7fb5d67ed03b49f8cc196e572c0fbe2175a0fb1f59e9a87e285` |
| `theory/m2-parity-obstruction.md` | `0beac81ecf6c6db5f82bc5be8e48d56e0babb44b15263f4dcb647f55f0e1682b` |
| `theory/m2-sharp-constant-open.md` | `9d6c7a2c674c351c04f0fec7325fcdd2dbbc676aefd47997a69e36e1701e606c` |

Direction files under `topics/mz-constants/directions/M2/`:
`candidates.md` has hash
`f5bb1210b058616ccaccc702c6f3f6074e935831bc8232150cc6c7ff7ff39dcc`,
and `LOG.md` has hash
`b2e2dfd3963406a803cbca3a3216338e68ddb87eb59fd9df2516edd4e99cdd28`.

Independent reconstruction checked each of the following potential failure points:

- The CC cosine-series tail and the N=2 parity case give the stated interior
  weight bounds and the all-node floor w_k≥(1+min(k,N−k))/N².
- The cardinal estimate is min(π,1/|t−k|), including continuous nodal limits;
  the relaxed kernel and angular cell mass use correct factors. The asymmetric
  weighted row and column Schur bounds multiply to the claimed K_N. Endpoints
  are included; this proof genuinely works on Π_N.
- The harmonic witness has degree≤N−1 and vanishes at both endpoints. The
  geometric partial-sum bound gives the finite harmonic tail ≤1; no convergence
  assumption about an infinite sine series is hidden in the proof. Both uniform
  sine bound and logarithmic cosine upper bound hold as stated.
- On [N^−1/2,1/4], the integration-by-parts error is at most N^−1/2. The
  subtraction 25 log N is absorbed for log N≥128; the constant polynomial handles
  the entire remaining finite range without numerical enumeration. Thus the
  explicit 128000/(log N)² upper bound is proved with loose but valid constants.
- The U norm, N=512 eta counterexample, endpoint cardinal absolute integral
  exactly 1/N, and nonzero top coefficient of positive-amplitude alternating
  nodal data are independently correct. Their negative scopes do not reject
  either main theorem or the source's correctly labeled full-space computation.

No mathematical finding remains open for these six proved statements. Their
analytic validity is **ACCEPTED WITHIN THIS INDEPENDENT AUDIT'S SCOPE**; this is
neither a novelty acceptance nor the required Claude audit. The leading-constant
target correctly remains OPEN, with a deferred candidate and no invented result.

Executed separately, exit 0:
```
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python tracks/mz-constants/code/m2_endpoint.py --exact 512 --measure 8 16 32 64 128 256 512 1024 > tracks/mz-constants/evidence/astra-m2-replay.jsonl
```
The replay is byte-identical to the developer output, SHA-256
`df076812f88c19e8e6a71b58ac1eb46cacb506541cccd09a92441fd9356ae6a8`.
`astra-m2-comparison.json` records 74 numeric values compared, maximum difference
zero and no mismatches. The rational N=512 quotient is below 1/4 exactly.
All floating witness measurements remain MEASURED; the universal proofs do not
depend on them.

The M2 historical comparison remains high risk and unresolved. Equivalent
weighted Lobatto interpolation norm results would remove order-law novelty even
if this explicit witness or proof differs. The scoped literature check has been
performed and the limitation is retained, rather than treating missing full texts
as evidence of a new result.

## M3 pinned proof audit and replay

Final stable hashes under `tracks/mz-constants/`:

| Artifact | Audited SHA-256 |
|---|---|
| `code/m3_exact_check.py` | `246bd4b95226182b0231730d7ad6ae6d7716623d31b28193c0e44d932825d2dd` |
| `theory/m3-upper-ratio.md` | `95139656c243842cb4a23807e7b63123b7e560420af2408356b40774fe4fcda7` |
| `theory/m3-lower-ratio.md` | `2f99dac17bf276a5741ccf034fe353b6bd44a7555ee1a5192caa04281b795503` |
| `theory/m3-uniform-eta.md` | `7dc112e74bbf992383b43e8f92f26c94aca27d745b7ce8c165738be55bcab44c` |
| `theory/m3-hyperinterpolation.md` | `4d19ba82d096aa316c4801887740dd0ad537c6a0293eeed6075128c92e2a81d2` |

The complete M3 candidate file has hash
`e7f019c7e50458db05302e1b023b7ef3b13b239523734e6e2c8e31a8fb7fa1b5`;
the RUNS file has hash
`102d80a21a72b191cc3d20cc7c02728d77f2e928d14e555502712e6dc29e90c5`.
Both are under `topics/mz-constants/directions/M3/` and were read in full.

For the upper bound, independently checked
(d²−1)/(r²−1)≤d²/r²≤(2n/N−1)² on every active offdiagonal pair. This
gives the same valid sign replacement with a positive coefficient rho when
2n>N. The exactness case 2n≤N is correctly separated.

For the lower bound, checked the filter's coefficient at the cutoff |k|=n,
degree N−1, n=0 convention and exclusion of every nonzero 2N alias. The
inverse-square kernel bound and the one-Lipschitz regularized sine weight give
the transformed exponent −3/2. Each half-open distance shell contains at most
two nodes. The row bound is C_0(1+2/π)/epsilon and the column integral is
2C_0/(epsilon N), with ordinary circle measure. The mirrored weighted nodal sum
is at most 3NQ_N and the full-circle integral is at least twice the Lebesgue
norm squared. These factors give exactly
C_*=12(1+π)^4(1+2/π), and lower bound (1−n/N)²/C_*.

The uniform-eta synthesis and the direct hyperinterpolation argument both follow
with their stated quantifiers. The latter's restriction k≤min(n,N−n) correctly
enforces polynomial reproduction, and signed rules are expressly excluded.
The final citation-only update correctly identifies the generic upper-Gram
mechanism as known context. No mathematical finding remains open in these four
proofs. Their analytic validity is **ACCEPTED WITHIN THIS AUDIT'S SCOPE**, with
classical prior-art/novelty uncertainty and Claude review still pending.

Executed separately at the checked code hash, exit 0:
```
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python tracks/mz-constants/code/m3_exact_check.py --max-n 25 --measure 20 40 80 160 > tracks/mz-constants/evidence/astra-m3-replay.txt
```
All 324 integer pairs passed the finite rational checks. The 120 numbers in the
printed floating-result rows matched the developer record exactly at its printed
precision. Replay hash:
`b4d40043ff747f83ed12a1b6e9d625913bde3f8835e662f057cdf012ee19ce08`.
Comparison details are in `astra-m3-comparison.json`. The all-N kernel and norm
bounds are analytic proofs, not extrapolations from those checks.

## Padua foundation, preserved open targets, and findings

The separate Padua theorem `m2-padua-marginal.md`, hash
`df4e67df2b3bcf0929375d6d2216d3ea04490a309b93dab356810120e70a0f90`,
was read and independently reconstructed. Its support/exactness hypotheses,
factor two, signed-weight-safe compression and only-liminf consequence are all
correct. No additional numerical run is needed for this algebraic proof; the
separate earlier independent marginal measurements remain finite evidence.

A minor protocol finding was returned to its developer: the new candidate record
incorrectly described the now-seeded registry as empty. The developer reread the
complete registry and corrected the record to cite M4 seed05 and M2 seed03 while
preserving the initial-empty chronology. The corrected
`directions/M2/padua-foundation-record.md` has hash
`42ec2b845673b4da29e1ddeba61ff9d5bb16150d0ab7cced4a7043d17ae84ca6`;
I reread and verified it. Finding resolved; the theorem was unchanged.

The M1 negative-result role label was also corrected by its developer from
independent adversarial developer to auditor; only provenance wording changed.
Final `m1-failed-psd.md` hash:
`71fe71fe4ad49b059538897b1e2d77688bae132b00e683ac09db2360b8a7534d`.
This change needs no mathematical rerun.

The two newly preserved open targets were read at these hashes:

- `open-upper-limit.md`:
  `e4e404c0bc48299c2828adcec4d2ff26b180e5828cccc0f64f6917b9dbdbbdc9`.
  The limit, exact value and uniform endpoint upper gap correctly remain OPEN.
- `open-padua-target.md`:
  `2ca00c885d5e181555381137fbb4d3e17d3e34220a4a28445bf90ee1a5dcd2bd`.
  The two-dimensional positivity/upper threshold, matching endpoint order and
  eta convergence correctly remain OPEN; the marginal is supporting information.

The full seeded registry was read again at audit closure, SHA-256
`8faa713969b420b0fd1136e87af0086715a01435df52a8e17322a6cc5fdac912`.
This is the preallocation seed state; integration must reconcile its historical
active/deferred labels with the completed audited direction records.

| Finding or adversarial threat | Severity/scope | Final disposition |
|---|---|---|
| Entrywise positive defect falsely promoted to PSD | Mathematical; hypothetical route, not attributed to source | Refuted and retained as scoped PD-N; surviving proof avoids it |
| Plain row diagonal dominance | Mathematical; sufficient criterion only | Exact N=5 failure retained; target survives |
| Full-space alternating vector transferred to degree N−1 | Mathematical applicability | Rejected direct transfer; admissible harmonic witness independently verified |
| Cardinal absolute-L1 columns bounded by log times CC weights | Mathematical mechanism | Exact endpoint obstruction retained; weighted-cell proof escapes it |
| Imported vanishing lambda_min treated as eta convergence | Major implication gap in source reasoning | CC limit now has M1 upper control; Padua retains only liminf and OPEN limit |
| Inverse-MZ factor described as true hyperinterpolation stability | Major operator-definition threat | Direct upper-Gram proof and known-source context recorded; no false growth claim |
| Log-squared lambda_min order promoted to a rate for 1−eta | Mathematical implication threat | Explicitly excluded in final theorem/open-target wording |
| New Padua candidate described current registry as empty | Minor provenance | Developer corrected; auditor verified new hash |
| Independent auditor mislabeled as developer | Minor provenance | Developer corrected; proof unchanged |
| Historical interpolation/MZ fulltexts inaccessible | Novelty limitation | Unresolved and retained; blocks novelty clearance, not the self-contained proofs |

## Final preallocation dispositions and acceptance boundary

| Direction/candidates | Mathematical or evidentiary disposition | Prior-art/novelty disposition |
|---|---|---|
| M0 baseline, seed01 | Bounded source-reading record accepted as such; selected primary comparisons independently checked | No exhaustive clearance; named missing fulltexts retained |
| M1 seed02; local13–14 | Exact foundation, strict/quantitative upper theorem and mass floor analytically accepted | Known aliasing predecessor; precise sharp-ratio novelty unresolved |
| M1 local11–12 | Scoped PSD refutation and row-dominance mechanism failure accepted | Elementary local kill tests; no novelty claimed |
| M1 local15 | Full-degree T_N obstruction accepted | Equivalent supplied reconstruction, no novelty claimed |
| M2 seed03; local21–22 | Explicit two-sided log-squared endpoint order accepted | High historical interpolation prior-art risk; novelty unresolved |
| M2 local23–26 | U identity, exact eta counterexample and both scoped mechanism failures accepted | Reconstructed/elementary statements; no new-priority claim |
| M2 local27 | Sharp endpoint leading constant remains OPEN/deferred | No novelty verdict or invented acceptance |
| M3 seed04; local31–32 and34 | Fixed-ratio upper/lower estimates and eta synthesis accepted | Classical filtered reconstruction/MZ overlap unresolved |
| M3 local33 | Hyperinterpolation application accepted for positive weights and stated reproduction degree | Generic upper-Gram mechanism is known context; CC application separately scoped |
| M4 seed05; local28 | Exact Padua marginal/compression accepted | Equivalent supplied mechanism; full 2D target deferred/OPEN |
| M5 seed06 | Deferred, not accepted as a theorem | Rule-specific primary comparison still needed |
| M6 seed07; finite record41 | Bounded reproduced observations accepted as MEASURED | No certified all-N or fast-rank theorem accepted; proof route deferred |
| M7 seed08 | M1+M2+M3 mathematical prerequisite satisfied for drafting | Manuscript not reviewed in this checkpoint; novelty and Claude handoff pending |

The complete local candidate files, including failed, equivalent and deferred
entries, were checked; there is no unrecorded mathematical acceptance in this
report. No developer proof was silently edited by the auditor. No private theorem
was imported and no third-party full text was committed by this auditor.

The auditor input/evidence manifest `tracks/mz-constants/evidence/astra-manifest.json`
pins the inspected working-tree bytes and executed outputs. All generated audit
files are below the repository per-file limit and are necessary small verification
evidence. No external cold-storage transfer is claimed. They are locally
retrievable at the recorded repository paths and regenerable with the commands
above; external archival and its retention policy remain the orchestrator/AC's
pending arrangement.

**Remaining boundary:** required cross-provider Claude handoff is **PENDING**.
Final ID allocation, registry integration and any manuscript are outside this
preallocation pin until a later impact review is appended. No merge, publication,
exhaustive novelty, sharp limiting constant, Padua convergence or certified
large-N computation is approved by this audit.

## Final allocation and registry impact review

This addendum closes the allocation/manuscript boundary of the preceding
checkpoint. The scientific preallocation checkpoint supplied by the orchestrator
is `2dc9264333cdf8372947448f4b9bdd3bb577d0e1`. The auditor performed no Git
operation. The exact final-ID map was read and checked at SHA-256
`0175b632f6d82f8053ff91f25893a92b688c005d1b00ef25f3e8e031c2f9d39e`.
It maps 65 complete provisional tokens into PD-T013–028, PD-N002–006,
LIT-042–060 and IDEA-052–076. The preceding mathematical dispositions apply
to those final identifiers via that map; no status is upgraded by renumbering.
The batch ledger preserves the existing charter reservation ranges. This audit
does not certify acknowledgements from another chat or unpublished reservations.

The independent allocation check reverses the complete final-ID tokens in all
37 files listed by `allocation-impact.json`, removes exactly the identical
administrative review banner from each of the 21 theory files, and restores
only the three documented file-specific dependency shorthand expansions
(`m3-uniform-eta.md`, `m3-hyperinterpolation.md`, and
`m2-sharp-constant-open.md`). After that normalization, **all 21 theory files**
and 35 of the 37 files match their recorded preallocation SHA-256 bytes exactly.
This includes both retained OPEN targets; no mathematical statement or proof
changed. The two expected exceptions were separately read and reviewed:
the fully expanded ideas registry, and the ASV selected-reading paragraph
attributing equations (7)–(8) and distinguishing hyperinterpolation from
inverse-Gram least squares. The latter agrees with the auditor's own primary
inspection already recorded above. `astra-allocation-check.json` retains the
per-file hashes and normalization outcome. A final check found no file changed
since that evidence was produced.

The complete final `state/IDEAS.md` was read, including all 25 entries and the
historical/current disposition distinction. The final crosswalk, proof-status
registry, literature index and batch ledger were checked. All 65 crosswalk
pairs resolve to their canonical files, all 21 result rows have the scoped
PROVED / MEASURED / OPEN status, all 19 literature rows are present, and all
25 IDEA headings resolve. The final README, negative-result index, audit log,
and historical CURRENT-snapshot qualifiers were also inspected for claim-scope
consistency. Minor stale index wording was returned to the orchestrator and
corrected without changing any proof. These checks do not author or accept
the charter PR's scientific content.

**Manifest provenance correction.** The first 55-input manifest snapshot was
collected while allocation was occurring. Its original label, “preallocation
working-tree file hashes,” was too broad: some bytes already contain final IDs.
Those 55 original identity records are preserved as a historical mixed-time
snapshot in the refreshed manifest, not relabeled as if they all came from the
scientific checkpoint. The explicit developer pins and independent reconstruction
entries in this report remain the actual preallocation proof pins. The final
manifest separately records current reviewed inputs and the allocation impact
chain. Code and executed numerical outputs did not change; no repeated numerical
run was needed for token substitutions, administrative banners or source-coverage
wording.

## Pinned manuscript translation and claim-scope review

The manuscript was read in full (922 TeX source lines), together with its complete
bibliography, README and M7 readiness record. Its full proofs were compared with
the independently reconstructed M1/M2/M3 and Padua statements, including all
constants and endpoint/range conditions. Stable writing inputs are:

| File | SHA-256 |
|---|---|
| `tracks/mz-constants/paper/manuscript.tex` | `072ae4e52c2cea78f2ec13f6e48a3d9529234af6c99d7b747a40c44c31f08c7c` |
| `tracks/mz-constants/paper/refs.bib` | `f2f4eb04dec45003a107deac7c91b2f0d4737e2707289d359fd3d0194aeb9bf8` |
| `tracks/mz-constants/paper/README.md` | `f433fc6f10b3e0da3bdfec1da80e6e5a177b0967cf6802ec7e1b8217de2512d7` |
| `topics/mz-constants/directions/M7/manuscript-record.md` | `68b15a5ed49e5c06bfdb3b5d6367a9ff5ac458de1cbe55736010aa0cf61d048b` |

No mathematical gap or unproved upgrade was found. In particular:

- CC exactness is correctly parity-sensitive: d_N=N for odd N and N+1 for
  even N. Symmetry supplies the extra odd degree in the even case, and the
  first aliased even mode disproves the next degree. Node index N, point count
  N+1, test degree n and exactness degree d_N remain distinct.
- The endpoint conclusion is lambda_min asymptotic order log-squared inverse,
  eta tending to one, and condition number of logarithmic squared order.
  The proof uses 1≤lambda_max<2. It expressly does not infer that
  1−eta has log-squared inverse order or that the minimum-eigenvalue side is
  eventually binding. The guaranteed upper-bound gap remains insufficient.
- The fixed-ratio constants and filtered-Fejer normalizations agree with the
  audited proofs. Hyperinterpolation uses the upper Gram bound directly,
  with no inverse Gram matrix. The stated reproduction range
  k≤min(n,d_N−n) correctly retains the CC parity improvement.
- The exact N=512, n=511 counterexample defeats an unconditional eta≤3/4
  applicability claim while preserving An–Wu's explicitly conditional theorem.
- Padua conclusions are only compression, extreme-eigenvalue domination,
  the finite eta counterexample and liminf eta≥1. Signed weights are allowed;
  positivity, a two-dimensional upper bound and convergence are not inferred.
- The measured decimal near 1.004437, sharp endpoint constant and genuine
  two-dimensional targets stay OPEN. Historical interpolation/MZ fulltext gaps,
  known generic upper-Gram context, Claude PENDING and non-submission readiness
  remain visible. There is no first-proof claim or implied exhaustive exclusion.

Two clarity findings were returned to the manuscript developer, who applied
them before the final pin: the parity obstruction now says “strictly alternating
nodal values with positive amplitudes,” and the gap discussion says “the
guaranteed gap in our upper bounds.” The auditor did not edit developer files.

The retained auditor script was actually executed from the repository root:

```sh
python tracks/mz-constants/evidence/astra-final-check.py
```

It checks final registry/crosswalk consistency and independently parses both
manuscript tables against `astra-reproduction.json`, the auditor's earlier
actual separate spectral replay. All **10 rows and 30 floating entries** pass;
maximum rounding discrepancy is `4.673308962033218e-10`, below `5.1e-10`.
Padua degrees and negative-weight counts match. All 12 citation keys match the
bibliography exactly, all manuscript PD/LIT identifiers belong to the final
allocation, and no provisional token occurs. Final exit status was zero.
Two preliminary checker failures were parser assumptions, corrected locally:
the manuscript uses `citep` and the registry uses third-level IDEA headings.
Neither was a manuscript or mathematical defect. Durable outputs are
`astra-registry-check.json` and `astra-manuscript-check.json`.

This last check is a transcription/impact check, not an additional spectral run.
The auditor did not compile TeX or visually inspect the PDF; the manuscript
developer's compilation and the orchestrator's independent build are separate
evidence. The independently executed earlier numerical checks remain finite,
uncertified floating observations where applicable, not proofs of all-N claims.

**Final disposition:** M7's pinned development manuscript is accepted as a
faithful mathematical synthesis within this audit's scope. M0–M6 dispositions
remain exactly as in the preceding table, translated through the final-ID map.
The new writing does not accept deferred mechanisms, settle OPEN constants or
upgrade novelty. Required Claude cross-provider audit remains **PENDING**;
historical duplicate comparison remains **unresolved**. No merge, submission,
publication, authorship decision or external archival is approved by this
independent audit.
