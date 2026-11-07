# Supplementary independent mathematical check — new T7/T9

Rules read at `120a19ee71baa8e7834b3b183798df2cf489c432` (2026-11-06).
Assigned checker: Codex, `gpt-6-astra` high; exact runtime metadata is not
independently exposed. This supplements the required substantive Claude
handoff; it is not that audit. Scope is the new T7/T9 mathematics and their
interactions only, without reopening accepted T1–T6 results.

**Review state: independent mathematical reconstruction and reruns complete
for the frozen files identified below; the coordinator confirmed this
as the final mathematical candidate.** The initial checks preceded the final proof files. The dated final
review below supersedes that preliminary state. Required substantive Claude
audit and broader workflow/readiness decisions remain separate.

## Gate and inputs

Read AGENTS, WORKFLOW, CODEX, handoff04, the complete 1,154-line
`state/IDEAS.md` including all obstruction/disposition tables (truncated
reads were completed by smaller contiguous reads), and relevant literature
INDEX rows/addenda. Search terms included finite subgroup, coset, Haar,
character, annihilator, phase, rank two, lattice packing, octahedron,
Fekete, Leja, lower set and hyperinterpolation. Searches covered the registry,
relevant lattice theory/candidate records, topic literature and theory.
Full shortlisted candidate records included C0 and C3; their relevant
PD-N032 and PD-T091 proofs were read. The T1 classification, restricted
obstruction and unrestricted OPEN target, T3 character/short-relation proofs,
T6 source coverage, and audit T1's exact witness/scope were read. These are
known-mechanism continuations; this check makes no priority or exhaustive
literature claim and does not inherit unverified source proofs.

## Independent reconstruction before final proofs

1. The finite-H Fourier coefficient dictionary follows by expanding all
   `2^d` signs, retaining multiplicities when indices vanish. Distinct
   characters of H form an invertible Fourier matrix. Duplicate cosine
   rows preserve rank. Phase coefficients must remain complex until the
   equality with a real evaluation matrix is used.
2. The compatible-relation annihilators from T3 use only that `u` annihilates
   H and `u.a` is an integral multiple of pi; cyclicity is irrelevant.
   An arbitrary phase does not satisfy this condition automatically.
3. `|H| <= 2^d |cos(a+H)|` gives finitely many bounded-order subgroups.
   The phase parameter is still continuous. Fold coincidences impose
   coordinate conditions `2a_j = -h_j-h'_j` on reversed coordinates and
   `h_j=h'_j` on unreversed ones. A finite fold partition is not a finite
   list of phases, and rank can vary inside a single fold stratum.
4. Abstract two-generator rank gives a primitive plane relation by choosing
   rational lifts of two generators and an integral perpendicular vector;
   it supplies no bound on its Chebyshev degree. The C5-squared example
   below specifically prevents an automatic degree-three exclusion.
5. At zero phase all signed terms in a Haar Chebyshev moment are positive
   integers. Hence total-degree-D exactness is equivalent to absence of a
   nonzero dual vector with l1 norm at most D. For shifted cosets the
   signed phase factors can cancel. Haar weights, non-Haar weights and
   unions must be kept distinct.
6. The claimed 18/19 lattice packing density is not proved or independently
   source-verified in this check. Any n>=110 obstruction using it must
   remain conditional on that named density statement. The elementary
   reduction uses min dual l1 length >=2n, disjoint interiors of radius-n
   cross-polytopes, determinant `|H|`, and the fold bound.
7. The proposed improved lower bound can retain the averaged kernel
   `K_n = sum_(|k|<=n) 2^-s(k) exp(i k.theta)` instead of paying T6's
   multiplier correction. Subgroup averaging onto nZ^3 leaves
   `1+sum_j cos(n theta_j)`. Its integral over the negative test box is
   `1/8-3/(4pi)`, yielding `3/4+3/(2pi)` for n>=1. For the proposed
   logarithmic test, the integer matrix with rows (-1,-1,-1),(-1,1,-1),
   (-1,-1,1) has determinant -4 and therefore preserves Haar measure
   as a surjective torus endomorphism. The carrier makes every frequency
   coordinate positive. The selected frequencies in the receipt have
   odd transformed coordinates and preserve total degree. Their weights
   are at least 1/8; the minimum-first slice contains at least one third
   of the symmetric reciprocal cube sum. Full final proof review remains
   necessary, including the sign-test normalization and real-norm passage.

These cautions were sent to the coordinator/workers while development was
in progress. No accepted claim was silently changed by the checker.

## Commands actually executed

From the repository root:

```text
python topics/padua-3d-20261106/code/independent_new_math.py --output topics/padua-3d-20261106/evidence/independent-new-math.json
```

Independent implementation imports no producer code. It uses Python 3.12.14 exact
integers/Fractions and SymPy 1.14.0; result-bearing tests raise explicitly.
The receipt pins its checker code and stays below 16 KiB. These finite
checks supplement hand proofs; they do not establish an unexecuted full
census or an all-degree numerical conclusion.

Observed PASS:

- H={(i,j,i+j)/4}: 16 angles, 10 nodes, absolute monomial determinant 256,
  no single-coordinate reflection invariance; four Haar weights 1/16 and
  six weights 1/8. Haar cubature is exact through degree two and the only
  nonzero degree-three Chebyshev moment is xyz=1/4. The degree-three
  moment system has rank 10 but augmented rank 11, excluding every real
  weight vector, including signed weights. The common cubic has continuous
  integral 1/2, independently explaining the contradiction.
- The two diagonal-C3 phases (1/12,1/12) and (1/12,1/4), in turn units,
  each have three nodes in the same collision-free coordinate stratum,
  but exact affine ranks 2 and 3. A generic fold pattern alone does not
  justify constant rank or sampling one representative.
- C5-squared graph `(i,j,2i+2j)/5` has no nonzero annihilator with q<=3;
  (1,1,2) is an annihilator with q=4. This does not establish minimal-node
  unisolvence or a family.
- Eight independent full-character/evaluation comparisons over F_1009,
  four explicitly defined groups and two phases each, agree entrywise
  with all zero-index multiplicities and give equal ranks. This is exact
  finite identity checking, not a claim that a deficient modular rank
  certifies deficient characteristic-zero rank.
- A shifted C2 orbit has first-kind Chebyshev moments (1,0,0,0) through
  degree three although its shortest nonzero dual vector has length two:
  the unshifted iff cannot be applied to phase-shifted cubature.
- Exact threshold polynomial values are -9809 at n109 and 2312 at n110;
  its forward difference is positive thereafter. Two-dimensional Padua
  n1..10 has the correct node count and only dual vectors (±2n,0) in the
  l1 ball of radius 2n, consistent with degree-(2n-1) exactness.
- Exact lower-bound subset and symmetry inequalities pass for n1..20.
  The claimed asymptotic coefficient is 1/(24pi^3), still a coarse bound;
  finite checks alone do not establish this limit.

## Final mathematical review — 2026-11-06

Worker-ready files were reviewed after their explicit freeze notifications.
The final scope is all seven `theory/t7-*.md` and seven `theory/t9-*.md`
files listed below, T7/T9 producer code and scientific receipts, and relevant
candidate/status prose. Working HEAD during this review was
`51c031a59bcd3a05e142e1c05dd19cbba1933bd7`; the file hashes identify the
then-uncommitted candidate exactly. No whole-batch audit is asserted.

**Mathematical verdict: supported within the stated scopes, with no unresolved
finding.** This covers the analytic PROVED statements, the isolated T7
computer-assisted rank result, the explicitly CONDITIONAL density corollary,
and the bounded MEASURED maxima. It does not constitute the required Claude
substantive audit or merge/readiness approval. The coordinator confirmed the frozen working-file candidate on2026-11-06
and will publish these same mathematical files; publication identity is
checked against the table below.

Three issues raised during review were corrected by the developers and the
corrections were checked:

- T7's symbolic-rank proof originally said N-column minors while N was an
  arbitrary requested node count. It now sets D=binom(n+d,d), independently
  of N, and tests D-column minors. The final existence reduction includes
  all positive-dimensional phase strata and is not an executed census.
- T9's open-items prose originally suggested that any packing bound δ<1
  discharged the exact n110 dependency. It now requires δ≤18/19 for that
  threshold and distinguishes other eventual thresholds. The f109 arithmetic
  typo was corrected to -9809. No unverified packing theorem is promoted.
- T9's result-bearing finite checks used asserts. They now raise explicitly,
  and the corrected producer was independently rerun. The proved analytic
  bounds do not depend on those finite checks.

The complete lower-bound proofs correctly keep real operator norms when
identifying the averaged kernel, then use complex characters only for scalar
Fourier identities. The determinant-minus-four torus map preserves Haar
measure, the square-wave phases agree, and the minimum-coordinate covering
has the correct inequality direction at ties. The leading constant is
1/(24pi^3), exactly 27 times the old explicit coefficient. The practical
bound is 3/4+3/(2pi)>1 for every n>=1. No sharpness is established.

The lower-set theorem is an elementary implication conditional on an actual
all-prefix bound, without claiming that its premise has been supplied for
the measured arrays. The extraction theorem uses the correct maximum-row-sum
norm of C inverse. Its proof does not infer a quantitative inverse bound
from invertibility. T5's inherited degree5/7/9 entries give node lower bounds
12/24/41 at section orders2/3/4; these are correctly compared to20/35/56
and do not exclude the respective minimal targets. No T5 theorem was reopened.

### Independent actual-node certificate for the cubic survivor

The checker constructs H from (7,7,4)/10 and (5,0,5)/10, adds
(1,2,4)/101, and represents every angle exactly by a residue modulo1010.
There are20 group elements and20 distinct coordinatewise cosine-folded
residue triples. This checks the count independently of the character
matrix. The direct Π3 Chebyshev evaluation matrix is20 by20.

The checker independently uses prime5051 and root32 of exact order1010.
It checks primality, `32^1010=1 mod5051`, and nonidentity at exponents
1010/2,1010/5,1010/101. Since5051 is odd and does not divide1010,
this root annihilates the cyclotomic polynomial Φ1010: the factorization
of t^1010-1 has disjoint roots modulo5051, and exact multiplicative
order selects this factor. Thus ζ1010↦32 defines a homomorphism
Z[ζ1010,1/2]→F5051. Direct cosine entries are
(ζ^t+ζ^(-t))/2, so nonzero determinant after reduction proves their
characteristic-zero determinant nonzero. Exact modular elimination gives
rank20. This proves actual-node Π3 unisolvence with the written finite
reduction and independently executed exact certificate; it is not a generic
axis argument or an inference from deficient modular rank.

The producer's distinct607/root122 order101 condition was independently
verified too. Its dictionary need not have a Fourier evaluation over F607;
the coefficient-ring homomorphism alone suffices to lift its nonzero minor.
The independent direct matrix hash is
`b28ebf3b89dc203575f98512d9f113a6a2e630f2870850fa1d96621d506c8ac9`.
The checker imports no producer code for this certificate. The finite trust
base is exact Python integers/modular arithmetic and SymPy primality; all
rank elimination in this checker is separately implemented.

The added cubature obstruction is also supported: u=(2,-2,0) is dual,
A-B=-4pi/101, and with U=T2(x),V=T2(y),c=cos(4pi/101), the quartic
U²+V²-2cUV-(1-c²) vanishes on every candidate node. Its product-arcsine
integral is c²>0 since0<4pi/101<pi/2. Hence no real weights reproduce
Π4 (and therefore not Π5), while Π3 unisolvence remains true. The
independent checker additionally verifies all20 nodal identities and the
nonzero integral specialization modulo5051. This is a scoped marker failure,
not a lower bound on Lebesgue growth or rejection of all shifted cosets.

### Consequential independent producer reruns

Actually executed after code freeze, without rewriting producer receipts:

```text
python topics/padua-3d-20261106/code/t7_cosets.py --output /tmp/padua-independent-t7-diagnostics.json
python /tmp/padua-independent-t9/code/t9_checks.py
```

The second command used an unchanged byte-for-byte copy of the producer
under a temporary `code/` directory with adjacent `evidence/`. T7 agrees in
every field except command destination and elapsed seconds; this includes
D0, all inherited control distributions, H39 witnesses, Padua ranks, the
full invariant T1 control, all new diagnostics, and the607 rank certificate.
The T9 exact receipt agrees in every field. In addition, this checker's
independent enumeration in transformed odd-frequency coordinates agrees
with all six producer rational square-wave sums at n1,2,4,8,16,32.
The harmonic crossing at n2420 remains MEASURED, as explicitly stated.

The complete T9 maxima suite was rerun with
`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1`, importing the frozen producer
via importlib and calling `main()`. Only `TOP` and the `numpy.save` output
path were redirected to `/tmp/padua-independent-t9`; all mathematical code,
node selection, source imports and optimization settings were unchanged.
All26 scientific rows, fits, guards, success counts and metadata match
exactly after removing elapsed seconds. No case was suppressed or unrun.
Maximum condition number was134.21473131424793 and maximum residual was
5.817981730063537e-13. Floating local refinement supplies only lower samples;
neither independent reproduction nor the descriptive power fits certify
suprema or an asymptotic growth law.

Rerun receipt identities (regenerate-only temporary artifacts):

| Rerun | SHA256 |
|---|---|
| T7 diagnostics | `21772ff266d233963f2af0a8895625a741bb706cb4a16360810a6452a65883c3` |
| T9 exact checks | `7ddaa69af559ca72f97e85e465ba1570827f2a2607ccebf0a88932e050d553bc` |
| T9 maxima | `d4edd843adae20da9eba918b08b2b5830ac377824b348dc8b39ff4122e295488` |

### Frozen candidate file identities

These prose hashes identify the reviewed snapshot only. The executable
checker pins no prose records.

| Topic-relative file | SHA256 |
|---|---|
| `theory/t7-finite-reduction.md` | `d6a5d3e7b42a9fe227ab4d028abdbf826ff6fa702b1e445dd6405657dbf1ddfa` |
| `theory/t7-general-character.md` | `0c08846457de178634fc3ed8162d4c04242b567f7b32de4257490646d26cc969` |
| `theory/t7-rank-two-survivor.md` | `abe1f2edec8ceec6d86179d9def270894197a0b0ca853b1cd87764e7a606d484` |
| `theory/t7-rank-two.md` | `80118e9035104dce9130778fa4ead9eb2cc4bab6439a444163eb4dd58c89fd36` |
| `theory/t7-short-relation.md` | `fa1b262c0bb9b7afa2779070b0eeb38aa88bc93cb385deef1fca774dd9b12db8` |
| `theory/t7-survivor-cubature.md` | `cb1f3273dc26832a771a416bdfce0fbfd4a95af7091d493b266fa1f79bdfc453` |
| `theory/t7-ten-point.md` | `eb4bbc0087ac667c467cba96518a4a6f3ed9ad3363d3cb538f00d0366b3e910b` |
| `theory/t9-averaged-projection-lower.md` | `ecca0ac29041c31c28a5665f2e316fd8d5e707bd71bf68ac3f814dea31183b93` |
| `theory/t9-haar-packing-reduction.md` | `4b6448828c5b15bf7fb5862865cc3e196c70a6c8277b5033f3a191136c67c9c5` |
| `theory/t9-lower-set-transfer.md` | `7a5b19313c31f1a638c3962efc1abcc291cdaa98f7b326b9a0dc7a806cdc97bc` |
| `theory/t9-measured-maxima.md` | `1ce57d5f997bff367bfc70cb2a79795dbb64d91c7b98e5ae3e54b5e73abc1833` |
| `theory/t9-packing-conditional.md` | `7f5eb856724efeca750b713d3a646ae150b47ab55bf761a093137c528607088f` |
| `theory/t9-projection-extraction.md` | `6179a82dd798dbbf4e4ec41025812031ba439750aca4bd47723cb2ac7c7736eb` |
| `theory/t9-squarewave-lower.md` | `6d441252f67c663973ca2603fed0c6dddd1dcd8652766b97bf98b744745d9671` |
| `code/t7_cosets.py` | `87c792762aafb210ce4cbe8417a8a61d43b13b5aadc952d5d2db43d120d617b5` |
| `code/t9_checks.py` | `3d85b0323dd62a9efe6c01023f0de8b74bf4483a315af984562b0717b1e22cf8` |
| `code/t9_maxima.py` | `b98fc5bae7502555a1ed903785d452140ac719f2ac8a478bfc8022c7b2d69a3e` |

Final independent code/evidence are `code/independent_new_math.py` and
`evidence/independent-new-math.json`; the receipt embeds the checker hash.
Their finite checks are reproducible by the command in the initial section.
The final survivor certificate uses the direct actual-node matrix, independently
of both T7 producer reductions and its prime. Source-density verification,
all-phase complete census, degree-uniform construction and certified global
Lebesgue bounds remain outside this supported scope.

### Frozen producer inputs and scientific receipts

| Repository-relative file | SHA256 |
|---|---|
| `topics/padua-3d-20261106/evidence/t2-generators.json` | `eec1bf41b736363ce951c26ed6d24c7f33d455f63fd65654b14e819807a1d953` |
| `topics/padua-3d-20261106/evidence/t2-n3-null-cover.json` | `ab78e752e646a880d305fc76c711808b7f8ac31e37546a25c5c05f623300eb2a` |
| `topics/padua-3d-20261106/evidence/t7-controls.json` | `a219129755d81798652bf67827570b6c8742638e46eba0d6433c744b1b435bcb` |
| `topics/padua-3d-20261106/evidence/t7-diagnostics.json` | `b8c1ff01a250733365ec467c1b61cc734b1790a2edbffefc7f39e2e4b1d1c3d8` |
| `topics/padua-3d-20261106/evidence/t9-checks.json` | `7ddaa69af559ca72f97e85e465ba1570827f2a2607ccebf0a88932e050d553bc` |
| `topics/padua-3d-20261106/evidence/t9-maxima.json` | `193286bedd88085486c87ab487ee7d919f821399eb61b60c1dd937dc6535d89f` |
| `tracks/lattice-unisolvence/code/c3_lebesgue.py` | `bf9cdb7c057f6ddf1793d99e6d338b1c1cfa37a274e5a6ac9689085f6bb3d66e` |
| `tracks/lattice-unisolvence/code/c3_rank.py` | `a95afbb764838662358dc70d2fd5a7eddf335d3ae48254d29b717fa015143332` |
| `topics/padua-3d-20261106/code/t4_stacks.py` | `0cd23793f436cd25328114e21dfda2c8c590cebbe7b88b985f7e478fc8c068b7` |
