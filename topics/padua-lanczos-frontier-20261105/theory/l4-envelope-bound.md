# PD-T?lanczos-frontier-codex-L4-01 — certified full scalar-CGS2 factor-ten separation on rotQ24 at degree12

ID kind: PD-T.
Aliases: PD-T?lanczos-frontier-codex-L4a; L4a; full scalar envelope spectral upper; positive-vector envelope
certificate; same-sign full-output BJ readout.
Split from: the previously OPEN rotQ24 conjunct of PD-T140; candidate inputs are
`IDEA?lanczos-frontier-codex-L4-01` (old L4a upper) and
`IDEA?lanczos-frontier-codex-L4-02` (old L4b full-output lower), both
quantitative variants of IDEA-250. No inherited record is modified.
Split into: none. The separate `PD-N?lanczos-frontier-codex-L4-01` is split
from the fixed-old-lower candidate subroute, not from this positive theorem.

## Statement

The following strict finite inequality holds:

    K_inf,BJ > 10 min(K_inf,alt, K_inf,pivot)                    (T)

on the frozen rational rotQ24 grid at degree12, in the complete formal
relative-operation scalar-CGS2 model of PD-T138. More precisely, the
independently checked integer endpoints are

    K_inf,BJ^2 >= L = 2041704913997,
    K_inf,alt^2 <= B = 13462956266,
    L > 100B = 1346295626600.                                (F)

Thus the stronger named-alt comparison holds. The BJ lower uses exactly
the old target90 greedy node/operation-sign error vector, but reads its
complete output using the fixed rational monic combination in
`evidence/l4-readout-certificate.json`. The upper uses the complete
alternating scalar envelope. All local scalar vector-operation channels
and all90 source columns are retained. The following exact reduction
supplies the proof of the finite certificate.

For any fixed admissible selection under the hypotheses below, let

    S_ki = sum_(h=1)^k |g_kh(z_i)| rho_hi,
    C_ij = sum_(k=1)^90 S_ki S_kj/d_k.

For every strictly positive real vector v of length625, define

    w_k = sum_i S_ki v_i,
    z_i = sum_(k=1)^90 S_ki w_k/d_k,
    U(v) = max_i z_i/v_i.

Then the full scalar capacity satisfies

    K_inf^2 <= lambda_max(C) <= U(v).                         (1)

The old scalar upper is `trace(C)`, so one may also use

    K_inf^2 <= min(trace(C), U(v_1), ..., U(v_r))              (2)

for any finite collection of positive vectors. If S,d,v are rational,
every z_i, ratio and comparison in (1) is rational; no square root or
approximate eigenvalue is needed for acceptance. An integer or rational
outward bound B with `z_i <= B v_i` for all i also gives `K_inf^2 <= B`.

In particular, let G_R be the existing exact BJ squared lower witness of
PD-T141 on rotQ24. A newly checked alternating-envelope certificate

    100 B < G_R                                               (3)

is sufficient for (T), indeed for the stronger named-alt inequality
`K_inf,BJ > 10 K_inf,alt`. The existing certificate has
`G_R/trace(C_alt)=62.08553668985878... < 100`; that original
PD-T140 experiment remains INCONCLUSIVE. Failure of (3) for any or all
tested positive vectors supplies no kill of (T).

## Definitions

The625 grid points are the rotation
`((3x-4y)/5,(4x+3y)/5)` of `x=i/12-1,y=j/12-1`,
`0<=i,j<=24`, with uniform positive weights. Degree12 has91 columns,
indexed0,...,90 in the existing graded order. The constant starting vector
has no local source. The monic exact orthogonal columns b_k, their positive
squared norms d_k, the monic coefficients alpha_kl, and the frozen responses
g_kh are exactly those of PD-T136/138; `g_kh=0` when h>k.

For column h, selected coordinate A_h and parent p(h), the complete local
amplitude budget is

    rho_hi = |(A_h b_p(h))_i|
             + sum_(l=0)^(h-1) |alpha_hl b_l(i)|
             + sum_(l=1)^(h-1) |sum_(j=0)^l alpha_hj b_j(i)|
             + 3 |b_h(i)|.                                  (4)

These are the coordinate product, every first dense-matvec product and
left-to-right partial sum, both vector subtractions and final component
division of the specified graph. The second dense-matvec's local
product/addition amplitudes are zero at the exact baseline. Scalar dot and
norm errors lie in the first-order normal kernel by PD-T138; they are
included in the model and are not deleted by a source-subset assumption.

K_inf is the supremum of the spectral norm of the final first-order normal
derivative over the complete cube of independent formal scalar relative
parameters `|delta_o|<=1`. Let R be the exact orthogonal projector onto the
orthogonal complement of the degree12 polynomial evaluation space. All
matrix2-norms below are spectral norms. S has90 rows and625 columns;
C has625 rows and columns. A dummy zero source/response row0 may be stored
without affecting any formula.

## Assumptions

Positive exact weights; injectivity through degree12; exact q_0; exact
positive pivots; fixed admissible parents and coordinate choices under
perturbation; the exact scalar operation order and independent formal
relative perturbations of PD-T138; no overflow/underflow or data
perturbation. For the proposed comparator the fixed rule is alternating,
`X iff 2j<t`; the BJ lower uses the already frozen BJ rule. The rotated
product grid is injective at this degree because invertible linear change
of variables preserves degree and the25-by25 grid is injective for
polynomials of coordinate degree at most24. All S entries are nonnegative.

## Status by part

Overall status: PROVED, finite computer-assisted, in the stated formal
first-order scalar model. Separate Claude scientific/protocol audit pending.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Reduction (1)–(2), including all scalar sources | PROVED, analytic | Written finite-dimensional argument; independently reviewed |
| Fixed full-output lower (6)–(7) | PROVED, analytic | Exact norm/readout reduction; independently checked projection arithmetic |
| Comparator squared upper B in (F) | PROVED, finite computer-assisted | Distinct re-execution of the pinned S producer, all exact component inequalities and old-trace control |
| BJ squared lower L in (F) | PROVED, finite computer-assisted | Same frozen signs; distinct re-execution of the pinned V producer, exact Gram/projection/readout and fixed-vector check |
| Strict finite comparison (T), via (F) | PROVED, finite computer-assisted | Exact integer comparison L>100B |

Candidate disposition: sharper-certificate variant of IDEA250/PD-T138/140/141.
No new mechanism or historical priority is asserted. The separately
recorded PD-T140 experiment remains MEASURED/INCONCLUSIVE; its old
ratio62.0855... was a ratio of endpoints, not an upper on the true ratio.
This new certificate settles its previously OPEN rotQ24 mathematical
conjunct without rewriting that original experiment or chronology.

## Depends on

- PD-T136: exact monic recurrence, frozen source responses and final normal
  quotient.
- PD-T138: the complete specified scalar-operation model, amplitude table
  and first-order normal formula. Its l-infinity scalar domain is essential.
- PD-T141: the exact attained BJ node-sign lower witness G_R on the same
  rotQ24 degree12 graph; independently checked in the prior campaign.

PD-T137/139's aggregate Hilbert-source bounds motivate comparison only;
their upper endpoints are not used for this scalar theorem. Positive-matrix
majorization below is proved directly, with no external theorem premise.

## Checks

This reduction was written after G0 resolution and completed repository
reading gate. The separate medium-effort producer executed
`code/l4_envelope.py`, regenerating all90 comparator sources and reproducing
the old trace exactly. Its compact receipt is `evidence/l4-envelope.json`;
large exact arrays and every attempted vector remain outside Git with
hashes and the actual regeneration command. Producer source SHA-256 is
`0da27e69ddd3cff5ca23e3fcac764f53891ad164ffab20324540fd67d2faf901`.
The reported run used Python3.12.14, python-flint0.9.0, NumPy2.3.5, and
287.85 seconds. Floating power iterations only proposed vectors; all
z, ratios, ceil bounds and comparisons were exact rational operations.
This is the assigned code worker's execution, not this mathematics worker's.

All nine allowed vectors failed (3). Their conservative integer bounds B
were, in order,

    37165812233, 13529772583, 13463203624, 13462956266,
    13462964839, 13462964836, 13462964836, 13462964836,
    13462964836.

The best is proposal3 with B=13462956266; each failed candidate remains
in the receipt's external-artifact manifest. This is an INCONCLUSIVE
certificate search, preserving the original experiment's outcome. A
separate post hoc Rayleigh diagnostic of the fixed-old-lower subroute is
recorded in `l4-N01-fixed-lower-envelope-obstruction.md`; it never serves as
a kill of (T). The producer methods file contains the full command and
trust/retention limits.

The separately preregistered L4b producer `code/l4_full_witness.py`
(SHA-256 `9f56bf92aa5883aaf6895327044406b7fdccb57e3c26199391fcaf61d873d2cf`)
then regenerated the same frozen BJ error vector's full response. It
reproduced G_R by explicit projection of column90 exactly before any new
readout. The first preregistered quantization,10^6, gave
`floor Q(x)=2041704913997`; it stopped at that first pass, so the10^9 and
10^12 proposals were not run. Its actual217.2247-second execution is
recorded in `evidence/l4-full-witness.json`. No error-sign search occurred.

The accepted91-integer vector, with dummy coefficient0 equal to zero,
is retained in `evidence/l4-readout-certificate.json`, SHA-256
`1208f11acdc92a599645f68770621f77d44c8e87e0ef2c69cfdbbd12e43e046d`.
It is a fixed witness; future verification requires no floating singular
vector proposal. The full exact quotient and raw arrays remain manifested
external artifacts with regeneration commands.

The distinct supplementary reviewer executed both stable producers in new
directories, freshly regenerated the inherited BJ lower, and ran the
separately written `code/l4_independent.py`, SHA-256
`491be4db86f4a0c1ff369f4b51043d63944562d7ca522e60cd794ed4d70248ac`.
The checker imports no producer function. It compared every exact S and
V entry with the developer's separate runs, checked the complete source
schema, exact `B_basis^T B_basis=D`, the old trace and target90 control,
the saved rational upper quotients, and the accepted monic coefficients.
Its projection formula subtracts exact polynomial energies from total
energy, independently of the producer's explicit projected-vector norm.
It explicitly consumed the retained fixed-vector certificate and verified
`L<=Q(x)<L+1` and `L>100B` exactly. All13 actually executed malformed
controls were rejected. Distinct regeneration shares the approved producer
and rational library; the checker is a separately written implementation,
not a second derivation of the inherited graph. Future floating proposal
equality is not a mathematical premise: saved rational vectors are the
certificates, and exact regenerated S/V and inequalities are authoritative.

Final receipt: `evidence/l4-independent.json`, SHA-256
`7c3c89a0f52a6cfbab4b98e8b00185932adf18e2f310330a942ca2e45a2abb3b`,
verdict `INDEPENDENT_FINITE_FACTOR_TEN_PASSES`,68.45seconds. The complete actual commands,
source/evidence pins and external artifact identities are in these three
producer/checker receipts and
`independent-checks-l4.md`/`l4-producer-methods.md`. The mathematics worker
read the final numerical receipt, fixed vector and complete checker source,
including the bounded portability amendment, before accepting (F); no code
execution by this mathematics worker is claimed. The final verifier-only
portability amendment preserves the exact numerical result: saved rational
upper vectors and fixed lower coefficients are authoritative, while future
floating-proposal equality is diagnostic only.

## Sources

Closest complete repository records: IDEA246–253, especially IDEA250;
PD-T136–141. PR21(unmerged), pinned890f56c, P3 and its three addenda were
read as repository comparison records. Literature INDEX and stored
Barrio–Peña–Sauer, Krylov-sensitivity and V+A records were consulted with
their original coverage gaps retained. No original paper was newly read,
no literature premise is imported, and no publication-priority claim is made.
The completed reading ledger and the historical prospective-gate timing
deviation are in `ideas-l3-l4.md`; later reading does not cure that deviation.

## Proof or evidence

**1. Full scalar amplitudes to an entrywise envelope.** Fix an admissible
formal error vector delta. PD-T138 gives

    f_h(i) = sum_o m_hio delta_hio,
    V_k(i) = sum_(h<=k) g_kh(z_i) f_h(i),
    normal output = R [V_0,...,V_90] D^(-1/2).

The unperturbed column0 has zero derivative. Since every `|delta_hio|<=1`,
`|f_h(i)|<=rho_hi` with the complete rho in (4). Therefore

    |V_k(i)|/sqrt(d_k) <= S_ki/sqrt(d_k).                     (5)

Let E be the90-by625 transpose of the nonconstant unprojected normalized
response, `E_ki=V_k(i)/sqrt(d_k)`, and let
`A_ki=S_ki/sqrt(d_k)`. The transpose of the normal output is E R, because
R is symmetric. Orthogonal projection contracts spectral norm, so its norm
is at most `||E||_2`.

For any real vector x, (5) yields the entrywise inequality
`|E x| <= A |x|`. Taking Euclidean norms and then using the operator norm
of the nonnegative matrix A gives

    ||E x||_2 <= ||A |x|||_2 <= ||A||_2 ||x||_2.

Thus `||E||_2<=||A||_2`. This does not assume arbitrary entrywise signs of
E are jointly realizable; it is an upper bound valid for each response of
the original complete scalar cube. Since `A^T A=C`, its squared norm is
`lambda_max(C)`. Taking the supremum over delta proves the first inequality
in (1). C is rational, symmetric, positive semidefinite and entrywise
nonnegative even though A's displayed square-root normalization need not
be rational.

**2. A positive-vector certificate bounds the full spectral envelope.**
Let v>0 and `U=max_i(Cv)_i/v_i`. For any real x, nonnegativity and symmetry
of C, and `2|x_i x_j| <= (v_j/v_i)x_i^2+(v_i/v_j)x_j^2`, give

    x^T C x
      <= sum_(i,j) C_ij |x_i x_j|
      <= (1/2) sum_(i,j) C_ij[(v_j/v_i)x_i^2+(v_i/v_j)x_j^2]
       = sum_i ((Cv)_i/v_i) x_i^2
      <= U ||x||_2^2.

The identity in the middle uses `C_ij=C_ji`. The variational characterization
for a real symmetric matrix gives `lambda_max(C)<=U`. Equivalently this is
a weighted row-sum certificate, but the displayed proof requires no
irreducibility or strictly positive entry hypothesis on C. Positive v is
required at every index; zero rows of C cause no difficulty. Matrix
multiplication gives `Cv=S^T D^(-1)(Sv)`, exactly the stated w,z formulas.
For positive semidefinite C, `lambda_max(C)<=trace(C)`. Taking any finite
minimum proves (2). If the component inequalities use an outward B in
place of U, the same argument gives `lambda_max(C)<=B`.

**3. Finite comparison.** PD-T141's attained formal BJ error vector gives
`K_inf,BJ^2>=G_R>0`. For the alternating rule, (1) gives
`K_inf,alt^2<=B`. Therefore (3) implies

    K_inf,BJ^2 >= G_R > 100 B >= 100 K_inf,alt^2.

Taking nonnegative square roots yields the strict named-alt factor ten,
and hence (T), since the minimum comparator is no greater than the
alternating comparator. This implication uses one comparator upper only.
Conversely, a kill of (T) needs a BJ upper together with lowers on both
comparators, for example
`U_BJ^2<=100 min(L_alt^2,L_pivot^2)`. Neither failure of (3), nor the old
endpoint ratio below100, supplies those inequalities. Equality refutes the
strict target only when it occurs in a genuine upper/lower kill certificate.

**4. Stronger lower from the same frozen BJ error vector.** Keep exactly
the inherited target90 greedy node signs s_i and the local operation signs
`delta_hio=s_i sign(g_90,h(z_i)m_hio)`, with sign(0)=0. Define the full
signed monic response V by

    V_k(i)=s_i sum_(h<=k) g_kh(z_i) sign(g_90,h(z_i)) rho_hi.

These are a single admissible error vector in the original scalar cube.
Let x be any nonzero rational90-vector, `y=sum_k x_k V_k`, and set

    Q(x)=[||y||_2^2-sum_(l=0)^90 (b_l^T y)^2/d_l]
         /[sum_(k=1)^90 d_k x_k^2].                          (6)

The denominator is positive. Exact orthogonality gives the numerator
`||R y||_2^2`, which is nonnegative. The output-direction vector
`a=D^(1/2)x/sqrt(x^T D x)` has norm one, and the first-order normal matrix
for this fixed error vector sends it to `R y/sqrt(x^T D x)`. Consequently

    0 <= Q(x) <= K_inf,BJ^2.                                (7)

Every quantity in (6) is rational. For x=e90 it equals exactly the old
target-column lower G_R; that identity is a required producer/checker
control. Numerical singular vectors may propose x but are not evidence for
(7)'s numerical value. If any exact Q(x)>100B, the proof of part3 with
Q(x) in place of G_R proves (T). Failure of finitely many x leaves the
fixed witness's true full-output norm, and the target, undecided.

## Scope

The reduction is for the complete frozen first-order formal scalar graph,
not an aggregate residual map or a source subset. It may improve an upper
without computing the exact scalar capacity. Dropping R and taking absolute
values can lose sharpness, so no guarantee of a decisive certificate is
claimed. A numerical eigenvalue or a floating proposal vector alone cannot
establish (3); the decisive inequalities must be exact or outward rounded.

No unavoidable actual IEEE drift, activated rounding pattern, finite-u
radius, all-degree rate, smooth-fit consequence or perturbed-pivot rule is
covered. The original PD-T140 exploratory outcome and its chronology stay
unchanged even if a separate improved certificate later proves (T).

## Open items

The finite rotQ24 target is proved in the formal model; no further
certificate search is required for it. All nine failed fixed-old-lower
upper attempts and their scoped obstruction remain recorded. The required
later Claude scientific/protocol audit, including explicit disposition of
the historical reading-gate timing deviation, remains pending. Durable
large-artifact archival/delivery is the orchestrator's separate storage
obligation; the compact fixed integer vector and decisive receipts are
retained in the topic. Actual IEEE realization, finite-u radii and
all-degree comparisons remain outside this theorem. L3 is deferred this round.

## History

- 2026-11-05: Codex mathematics worker, configured gpt-6.1-sol xhigh.
  Written after root reported G0 RESOLVED at684849d and accepted the
  completed source-reading prerequisite. The earlier saved candidate
  preceded completion of its prospective reading gate; that historical
  timing deviation remains disclosed for Claude's explicit disposition.
  This initial record contains a proved finite reduction and an OPEN
  finite comparison target, with no new computation outcome.
- 2026-11-05: All nine original upper-test failures retained with exact
  integer bounds and producer receipt. Root then authorized the already
  saved L4b extension using the same frozen error vector; its specific
  three-proposal test was written before its producer run. Added the
  exact monic-combination lower reduction (6)–(7). Main target stays OPEN;
  separate independent computer checks and Claude audit are pending.
- 2026-11-05: The fixed-vector independent checker passed all finite
  premises and13 malformed controls. Main finite status changed OPEN→PROVED
  on the written reduction, exact producers, fixed integer witness and
  distinct independent regeneration/check. Initial title was
  "full scalar-CGS2 envelope reduction for the rotQ24 factor-ten target";
  changed to the finite certified separation now established. All earlier
  preparation/failure history and the original PD-T140 INCONCLUSIVE outcome
  are preserved. No actual-rounding or all-degree status is changed.

- 2026-11-05 audit-01 response, Codex statement/metadata worker; requested gpt-6.1-sol high; runtime variant/effort not independently exposed. Rules read at `7f50cae80f5372db7c278aef4ba4a0a05e1137ea`. Canonical provisional ID is now `PD-T?lanczos-frontier-codex-L4-01`; the old L4a result label remains an alias. IDEA L4-01 (old L4a) is **REJECTED: failed** only for its `100U<G_R` criterion with the fixed old lower; its valid upper is reused here. IDEA L4-02 (old L4b) is retained/successful. The negative record is a split of that failed candidate subroute. Auditor L4-1 accepted: regeneration means a distinct re-execution of the pinned producer, not an independently implemented producer; the separate checker and audit's CPython reconstruction are identified in [audit-01/L4.md](../audit-01/L4.md). Runtime is the receipt's 217.2247 seconds. Proofs, formulas and certificate bytes are unchanged. The saved candidate draft first entered Git at `0574c47` before its prospective source gate was complete. Later completed reading does not cure or waive that deviation; acceptance remains AC's decision. The dated chronology and missing-read/gate checkpoints are in [gate-timing-response-01.md](../gate-timing-response-01.md). No novelty or priority claim is added.
