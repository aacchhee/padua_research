# NN MOP conditioning and numerical stability

Stage: PR preparation; [audit-01](audit-01.md) and [audit-02](audit-02.md) accepted the scientific scope/response. [G5 audit](audit-g5-01.md) accepts the finite reproduction with its explicit paper-data verification limitation. Final-ID/registry preparation is subject to distinct Claude readiness review. Current rules/source`414e781567078560b7e233aace3661abb88e37ab`; main/base`f654e32daff27b6846849311092f6daebbbf235b` is already an ancestor. Original campaign inputs remain pinned in input-snapshot.json. [Draft PR28](https://github.com/aacchhee/padua_research/pull/28).

## What the campaign establishes

The nearest-neighbour inverse problem is intrinsically very sensitive on the tested classical families. The local derivative and its exact induced norm are explicit. A mass-preserving signed weight perturbation proves an all-N Krawtchouk lower bound with asymptotic base at least `5+2sqrt(6)` (approximately 9.898979); a separate rational-height argument gives a much coarser explicit upper bound. These are local first-order conditioning results, rather than an error analysis of a floating algorithm. The sharp rate and a useful matching upper bound remain OPEN.

The frozen C4 baseline replays exactly. Computing accurate marginal Jacobi data does not satisfy the prescribed stage-isolation gate: excess error persists in the layer reconstruction. Two whole-triangle mixed-system designs often improve forward accuracy substantially. Neither has a general weak- or backward-stability theorem.

Strict joint-data backward error requires the entire reported array to equal the exact NN map of one positive common-support input. A compact exact dyadic certificate proves that one highly accurate raw N=4 LU output has no such inverse. A separate local geometry theorem makes nearby compatible projection well posed in a frozen positive-definite coefficient norm. Its practical metric has two components: an array correction and a common-input perturbation. Numerical projection measures these separately; it is not a silent redefinition of the original backward criterion.

## Objects, norms and proof status

There are N common distinct nodes and two positive weights, with the full mixed triangle normal through degree N. All monic coefficients are in `z=2k/(N−1)−1` on coefficient degrees at most N−1. The output error E is the largest of four relative field sup errors, exactly as in PD-T290. Structural zeros stay in the numerator. The primary input condition uses independent absolute node perturbations at scale one and componentwise relative weight perturbations. Individual mass scalings are null directions. A fixed-mass parity direction supplies the lower bound even under that stricter constraint.

The exact derivative formula is a weighted Jacobian row sum. The implementation evaluates all 3N columns and also extracts the alternating monic four-term step-line map, with its own field scales. This is not automatically the scaled Hessenberg metric used in LIT-347. Fully componentwise output conditioning is infinite when a coefficient is exactly zero with nonzero sensitivity; it is not estimated by dividing by a floating near-zero.

Written analytic proofs labelled PROVED were supported within audit-01’s declared scope; the localized response proof corrections were accepted in audit-02. Floating tables, optimization results and precision agreement are MEASURED. The analytic derivative algorithm is proved; numerical evaluations are not outward enclosures. Separate exact Fraction checks independently verify small Jacobians, finite identities and normality certificates. No fitted growth rate is promoted to a theorem.

## D1: conditioning

[Local derivative and norms](theory/conditioning-local.md), [coarse explicit upper bound](theory/conditioning-krawtchouk-bound.md), [exponential lower bound](theory/conditioning-lower-krawtchouk.md), [normality certificate reduction](theory/conditioning-normality-certificate.md), and [run receipt](attempts/D1.md) carry the precise statements and limitations.

The initial eight-size grid is N=4,8,12,16,24,32,48,64. At N=4 the NN mixed conditions are 165.04 (Krawtchouk) and 1573.916 (Hahn); at N=64 they are approximately 1.216e61 and 9.595e66. The 180/260-digit calculations agree very closely, but that agreement is not certification. All four expanded runs now cover every integer N=4–64 at180/260 dps, with all six NN/step-line input-model comparisons passing1e-60. Worst relative precision disagreements are1.764e-115 and1.285e-93. The complete61-row table appears once in attempts/D1.md. The separate [finite Hahn theorem](theory/conditioning-hahn-normality-finite.md) certifies all 61 full triangles by exact rational arithmetic, a noncircular reduction and committed essential receipt.

Independent direct-moment differentiation equals the C4 automatic derivative over Fraction for N=3,4,6 in both families, covering 4,416 entries. The exact N=4 Krawtchouk maximizing row has condition 4126/25. The lower-bound witness has separate exact terminal checks through N=8; its all-N conclusion comes from the written proof.

The measure-proximity sweep was registered before execution. A separate [analytic proximity theorem](theory/conditioning-lower-proximity.md) now proves that, for each fixed N>=4, `kappa*d_min` diverges as `p2` decreases to `p1=2/5`. Thus the proposed O(1/d_min) law fails in this precise family/metric; this conclusion follows from an exact weight witness, not a fitted sweep. A disjoint-support Angelesco experiment is outside this full-triangle domain: strict positive common weights cannot be disjoint, and allowing zero weights makes a marginal axis singular once its degree exceeds its support size.

The explicit stronger bound, with M=N−1, is

    kappa_N >= 5/(2M^2) * [(5+2sqrt(6))^(M−1)+(5−2sqrt(6))^(M−1)].

At N=64 it is approximately 3.3563e58, versus the measured1.2158e61. It gives a worst-case first-order capacity, not an assertion that every floating computation loses that many digits. A matching sharp upper rate remains OPEN.

## D2: the C4 error source

[D2 receipt](attempts/D2.md) records all twelve exact baseline replays, stable full-reorthogonalized Lanczos marginals, exact-input and rounded-input oracle marginals, and fixed-path spectral diagnostics. The original 140/220-digit reference convergence remains explicit.

For the finite G1 criterion, C4 exceeds `10 kappa u` at Krawtchouk N=8/N=16 and Hahn N=8/N=12/N=16, where `u=2^-53`. At larger N, `kappa u` can exceed one and the first-order comparison loses practical resolution. This is not an all-input theorem that the algorithm is or is not weakly stable.

G2 has nonvacuous failing cases at Hahn N=8/N=16: the stable-marginal C4 ratios E/(kappa u) are approximately 182.39 and 220.68. Oracle-rounded marginals also leave large reconstruction errors. Thus the handoff's criterion does not clear the layer recursion.

An alternating path alone loses information about the second functional; the diagnostic includes the additional `d_0` anchor. Even that diagnostic cannot see the whole NN array. An independently executed off-path perturbation leaves it unchanged while violating the mandatory terminal equality. Some large runs also recover complex nodes or negative weights. All such limitations are retained.

## D3 and D5: native solves and full-array backward geometry

[D3](attempts/D3.md) implements two designs: mixed solves in an orthogonal coefficient basis, and node-space constraint QR. LU/QR/SVD variants and failed large-N behavior are retained. These are known defining-system reformulations, without a historical novelty claim.

Binary64 values below are platform-dependent as specified in [native measurements](theory/native-measurements.md) and [projection measurements](theory/backward-projection-measurements.md). At N=8, the orthogonal-basis LU errors are about 3.096e-12 (Krawtchouk) and 4.238e-10 (Hahn), improving C4 by 2.78 and 2.79 decimal digits in regimes with `kappa u < 1e-4`. This satisfies the forward-accuracy threshold. It does not establish strict joint backward stability. At N=16 A-LU and B avoid the prescribed two-family kill; A-QR/SVD are separate variants with gains0.97/1.21 in the cited limiting case, not a blanket two-digit improvement. Some larger cases still lose all accuracy.

[D5](attempts/D5.md) proves that normalized masses and ordered nodes make the actual NN image an analytic embedded manifold of dimension 3N−2. Both complete marginal axes provide a smooth spectral left inverse. A frozen positive-definite coefficient norm has a unique nearest compatible point locally, with the stated pseudoinverse derivative. This concerns the actual common-data image, not an arbitrary flatness variety.

The [dyadic obstruction](theory/backward-dyadic-obstruction.md) has a standalone integer checker and an independent replay. Its necessary compatibility residual is nonzero, so strict backward error is infinite for the displayed raw output. Feasible common-data correction pairs and the [numerical nearest-fit follow-up](theory/backward-projection-measurements.md) are distinct measurements. For N=4 LU, the fitted input perturbations are approximately 0.98u/1.58u (Krawtchouk/Hahn) and the full coefficient corrections1.93u/3.06u. At N=8, the LU input changes exceed1000u and corrections exceed5000u, so the proposed100u mixed target fails in these fits. No optimization convergence test certifies the exact global minimizer, and no finite success yields a uniform stability theorem.

## D4: transforms and continuation

[D4](attempts/D4.md) gives finite common-Christoffel transport in O(N^2) arithmetic and a closed finite Toda flow, including the terminal boundary. Both require an available starting array and a normality interval. Exact rational checks and a separate independent reconstruction support the implementations; the proofs do not infer their general statements from those samples.

Positive common modifications do not automatically preserve mixed normality. The explicit three-node pair `(11,1,1),(13,2,1)` on `(0,1,2)` is initially normal, but multiplying by `x+1` makes the transformed means equal and the `(1,1)` determinant zero. A positive exponential path has an explicit finite normality crossing too. Common multipliers also preserve the weight ratio, restricting which targets can be reached.

The particular predivide-C4-restore solver is killed by G4 at N=16: E is about .223 versus .0967 for Krawtchouk, and 79.8 versus 70.3 for Hahn. Restoration from accurate starting coefficients is much better, but that does not solve initialization. The Toda pilot likewise uses oracle-quality initialization. Independent-weight transport with a useful starting representation remains OPEN.

## D6 and D7

[D6](attempts/D6.md) proves a positive graph encoding: put `y_l=w2_l/w1_l` and graph mass `w1_l`. The two MOP test families become `x^k` and `y x^k`. This elementary identity does not identify the whole NN triangle with standard total-degree bivariate orthogonal sections. Exact standard-grade and two-sheet obstructions are scoped to those literal dictionaries. A faithful recurrence dictionary and stable transfer to Padua remain OPEN. [Gate chronology and AC decision](LOG.md#2026-11-06-ac-decisions).

[D7](attempts/D7.md): **G5 reproduction gate PASS (one configuration, Octave 8.4, to the decade); large-N variation measured; topic-metric comparison not yet run**. The source is AC's pinned archive, now available in both executors. [Development receipt](g5-run/README.md), [independent audit](audit-g5-01.md). Codex independently reran all52 paper family/size cases using Octave9.4; the selected case also passes. Full tables vary with platform. The auditor's direct arXiv paper-table/hash verification remains unresolved (CONNECT403); paper comparisons are attributed to Claude's source-bundle record. No MATLAB/Advanpix, fieldwise NN comparison, all-platform agreement or stable solver is claimed. No Leuven contact.

## Gates, reproducibility and next step

[gates.md](gates.md) preserves all original criteria and dates the backward-metric interpretation. G0 passes; the finite G1 threshold and G2 fail; G3 has finite measurements and a separate proved obstruction to the proposed inverse-divisor rate; G4 has forward gains and explicit adverse strict-backward evidence; G5 clears its single-configuration reproduction gate; the topic-metric comparison remains unrun.

The [input inventory](input-snapshot.json) pins fetched repository files. Code and small essential evidence are committed. Regenerable raw data stay in local working storage, with commands/hashes in direction receipts; no cold-storage delivery is claimed. The connector-author exception was explicitly authorized by AC. Source imports were restored byte-for-byte after correcting a materialization-only final newline.

The full grid, figure receipts and three supplementary reports were reviewed by audit-01. Response checks pass the61-size exact normality verifier and12-case committed projection reference (six exact N4 gradients); corrupted identities fail normally/under-O as documented. Original temporary projection witnesses are unavailable; the new113,095-byte fixed-configuration reference is explicitly a response rerun, with platform-dependent measurements and no historical-byte recovery claim. [Evidence](evidence/README.md), [response checks](response-01/checks.json). Response01 was accepted in audit-02. Preparation applies final IDs and registries by reviewed diff after reservation refresh; [handoff07](handoffs/07-readiness.md) passes the prepared output to Claude Opus5.5high for readiness. Direct paper-data verification remains explicitly unresolved in the Codex G5 audit. Only AC merges. All unfinished scientific targets and unrun topic-metric comparison remain explicit rather than being labelled PARTIAL on the strength of supporting results.

## G2 convention and margin (audit-01 MINOR15)

G2's HahnN8 antecedent is narrow: E/(kappa*u)=100.6929, or2.003 excess
digits, only about0.7% above100. With epsilon=2^-52 instead of the
pre-registered u=2^-53, no baseline case would trigger that antecedent.
The convention in plan.md is retained; no run/threshold was re-selected.
