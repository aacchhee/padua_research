# PD-T333 — A certified finite bracket for the optimal Padua degree-three obstruction radius

Final registration (2026-11-05): **PD-T333**; status **PROVED** unchanged. Canonical provisional/historical aliases: `PD-T?lanczos-frontier-codex-L5-02`; `PD-T?lanczos-frontier-codex-L5b`. See [complete map](../preparation/final-id-map.json). This is ID metadata only; original statement/proof and frozen input bytes retain their scopes.

ID kind: PD-T.
Aliases: PD-T?lanczos-frontier-codex-L5b; L5b; n3 G3 pilot; full-kernel positive-balance upper; pstar whole-ball Taylor lower; 1/512-to-1/2 bracket.
Split from: the finite-value task in L5/G3 for PD-T075(U2); U2 is not settled.
Split into: none.

## Statement

Let

    P_3={(cos(j*pi/3),cos(k*pi/4)):
                       0<=j<=3,0<=k<=4,j+k even}

be the ten degree-three Padua nodes, and let K_delta be the union of their closed Euclidean radius-delta balls in all of R². Define

    delta_obs(3)=sup{delta>=0: some nonzero real p in Pi_7
                              vanishes on P_3 and p>=0 on K_delta}.

Then

                         1/512 <= delta_obs(3) <= 1/2.       (1)

The upper bound quantifies over the entire real degree<=7 polynomial class. It is not an upper bound merely for the positivity radius of one selected polynomial. The endpoints are certified bounds, not an exact optimal value. This is only the n3 part of G3; no n4--8 bracket, monotone trend, full G3 verdict or all-degree U2 conclusion follows.

## Definitions

Pi_7 has all36 monomials x^a y^b with a+b<=7. The complete first-jet kernel is

    S1={p in Pi_7:p(z)=p_x(z)=p_y(z)=0 for every z in P_3}.

Its jet matrix J has30 rows. All exact certificate computations use F=Q(sqrt(2)) with the positive real embedding sqrt(2)>0. The full kernel over F extends to the full real kernel by the rank/minor argument of [L5a](l5-01-finite-optimal-radius-certificates.md); the real coefficient class in the statement is not narrowed to F.

The lower polynomial is the actual20-term rational pstar of PD-N020, recovered from its pinned historical coefficient log and supplied completely in [lower certificate](../evidence/g3-producer-n3-lower.json). The upper data are12 points z_i+h_i and12 positive F-valued weights in [upper certificate](../evidence/g3-producer-n3-upper.json), with each rational h_i satisfying ||h_i||²<=1/4. Six selected points lie outside [-1,1]²; they belong to the stated full node balls and are correctly included.

## Assumptions

Exact frozen parity family, degree7, all ten nodes, full real polynomial class and full R² Euclidean balls. Exact arithmetic, complete-kernel ranks, algebraic embedding/sign checks and independently executed verifier as below. No floating LP feasibility/tolerance, named-polynomial negative point, generator-completeness conjecture, sampled direction or historical printed radius is an acceptance premise.

## Status by part

Overall status: PROVED (finite computer-assisted statement, exact lower/upper certificates and actual distinct checker execution; required later Claude scientific/protocol audit pending).

| Mathematical part | Status | Evidence |
|---|---|---|
| Lower endpoint delta_obs(3)>=1/512 | PROVED, computer-assisted | Actual pstar,30 exact jet zeros, ten PD Hessians and ten complete finite Taylor inequalities |
| Upper endpoint delta_obs(3)<=1/2 | PROVED, computer-assisted | Complete6-dimensional kernel;12 positive weights; exact balance in all6 kernel coordinates; evaluation rank6; exact full-ball membership |

Candidate disposition: retained finite result of saved L5-01 and known Taylor lower route. No historical novelty/priority claim. Original PD-T075(U2) remains OPEN; supporting finite values do not make it PARTIAL.

## Depends on

[PD-T?lanczos-frontier-codex-L5-01](l5-01-finite-optimal-radius-certificates.md), the accepted analytic finite-certificate reduction, historical audited metadata/convention hash `6beeb3f07eaa7fd0e401f94257c3afa9902d556324dc7cb18bc234ebe2cdfde6` (before the dated audit-response metadata update). Its original proof input and empty-set convention were independently accepted; the present Padua feasible set is nonempty by the lower certificate. PD-T075 fixes the optimal-radius definition; PD-N020 supplies only the historical baseline polynomial, whose actual coefficients/jets are freshly checked here. No assumed equality between the PD-T065 generator image and S1 is used.

Trusted computational dependencies: Python3.12.14 exact integers/Fraction pairs for the producer; SymPy1.14.0 QQ(sqrt(2)) algebraic domain and DomainMatrix exact linear algebra for the independent checker; exact rational comparisons fixing the positive sqrt(2) embedding; standard JSON parsing, SHA256 and Git retrieval for input identity. The producer's NumPy2.3.5/SciPy1.17.0 HiGHS LP is a proposer only, excluded from mathematical acceptance. A fresh floating proposer need not reproduce the same weights or search trajectory to verify the fixed certificates.

## Checks and exact input identities

All essential certificate/checker files are present in the topic, normally under16KiB each. Larger raw matrices are unnecessary acceptance inputs because the distinct checker reconstructs them. Root owns their Git checkpoint and storage integration; this mathematics worker performed no Git mutation or new scientific execution.

| Artifact | Bytes / SHA256 |
|---|---|
| [Producer](../code/g3_producer.py) | `d5973f6302038e1ad2b6b5ccc7db3a133757e08817f8e3019c166cd43c5efc7b` |
| [Lower exact certificate](../evidence/g3-producer-n3-lower.json) | 2704 / `48ea29641bde627b69a069ffa01687089f6decc0258ab0afa516ca69863b7e3c` |
| [Upper exact certificate](../evidence/g3-producer-n3-upper.json) | 2136 / `5c0c70e976711b31d0eed6c91b1c422fd8247ec9805a630e669618b47b9ef2a3` |
| [Producer execution receipt](../evidence/g3-producer-n3-receipt.json) | 9506 / `985e7a1db060f28623cd5f47a120f6123562ad095d8e263f43dac7943420bb0a` |
| [Distinct independent checker](../code/g3_independent.py) | 10387 / `ec595ad0effc0df8c4a6e1a0ca95d0d2632bc00ea8eb2126fc3a25629fcfa2f4` |
| [Independent executed receipt](../evidence/g3-independent.json) | 6602 / `7da8b0ff63f3e7b30af9beeb40c74483e91b42114886ee6e23674a5c2a1c56c2` |

The baseline coefficient-log input is historical Git blob `c88017135d020db69ecf438794f0710dc5a09fda`,3963bytes, SHA256 `287e8dd0bdaa60d93d728045fcd47c5c75832813657f4849081fe4b1e0629e8b`. Both executions separately recover/check these bytes. The historical printed statuses/radius are not accepted as evidence; the actual20 coefficients are extracted and all mathematical conditions are recomputed. The manifest locator is in ideas-l5-continuation.md.

Actual producer execution from repository root:

```sh
timeout 660s python3 topics/padua-lanczos-frontier-20261105/code/g3_producer.py --out /tmp/padua-lanczos-frontier-g3/producer-n3
```

Producer input/rules head was12879b5666a93f2ca88d89c3deaa7a152f883cc3. Root released it only after the finite reduction's independent analytic acceptance. Observed elapsed171.489801831seconds, peakRSS75008KiB. Full J/kernel construction and identities were complete by0.357371511seconds. No stage cap fired. It tested the saved21 dyadic radii on each q2/4/8 rational-offset grid. q2 found no accepted upper; q4 accepted U=1; q8 accepted U=1 and1/2. The failed numerical proposals remain INCONCLUSIVE and prove no mathematical infeasibility. There were no bracket bisections, q16/new families or n4--8 runs. See [methods](../g3-methods.md) for pre-execution caps and complete outcomes.

Actual distinct checker execution, after a separately written prospective plan and independently recovered/copied/hash-pinned inputs:

```sh
timeout 600s python -B topics/padua-lanczos-frontier-20261105/code/g3_independent.py --lower /tmp/padua-lanczos-frontier-g3-independent/inputs/lower.json --upper /tmp/padua-lanczos-frontier-g3-independent/inputs/upper.json --baseline /tmp/padua-lanczos-frontier-g3-independent/inputs/pstar-source.json --out /tmp/padua-lanczos-frontier-g3-independent/check-n3 --receipt /tmp/padua-lanczos-frontier-g3-independent/receipt.json
```

The checker exited successfully, status `PASS independent exact n3 lower/full-kernel upper checks`, internal elapsed1.330798089seconds (module-import/startup excluded), Python3.12.14/SymPy1.14.0. The distinct worker read/imported no producer arithmetic/code. It independently regenerated nodes, all36 monomials, J, the complete kernel, jets/Hessians/Taylor terms and point evaluations. [Independent report](../independent-checks-g3-04.md) records execution and the bounded scope.

Nine malformed controls were actually rejected: changed baseline polynomial, oversized lower radius1, negative retained weight, positive but unbalanced weights, an off-ball point, rank-deficient point subset, invalid node index, invalid field encoding and a proper kernel subspace. The original certificates passed again afterward. These controls test the stated acceptance predicates; they do not prove a general implementation-correctness theorem.

For a fresh-directory recheck, recover the baseline blob with git cat-file into a new external scratch directory, supply the two small topic certificate files to the same checker with --lower/--upper, and choose a new --out directory because the checker requires it not to exist. The checker asserts baseline bytes/hash and recomputes every exact acceptance identity. No original developer matrices, LP search output or temporary kernel file is needed. This is a regeneration recipe, separate from the actual executed commands above. Temporary raw output/kernel retention is not guaranteed and no external archive delivery is claimed.

## Sources

No new primary literature or priority claim. Full source/novelty gate and saved candidate histories are in ideas-l5-continuation.md. The baseline polynomial is existing repository evidence; the new finite upper controls the whole kernel. No source theorem is silently imported from a literature digest.

## Proof or evidence

The exact verifier computes rank(J)=30 and a rank6 basis B with J B^T=0. Since Pi_7 has dimension36, B spans all of S1 over F and, by L5a, over R. No historical dimension prediction or generator-image assumption supplies this step.

For the lower certificate, the actual pstar is nonzero, rational and degree7. At all ten nodes it has exact zero value and first partials, and its2-by-2 Hessian H_i satisfies H_11>0 and det(H_i)>0. With mu_i=det(H_i)/trace(H_i), the checker independently computes every local Taylor coefficient and verifies exactly

    mu_i/2-sum_{k=3}^7 sum_{a+b=k}|t_iab|*(1/512)^(k-2)>=0.

These ten positive/nonnegative algebraic margins are recorded in the independent receipt. L5a therefore proves pstar>=0 on every closed radius1/512 node ball and yields the first inequality in(1).

For the upper certificate, all12 retained weights are strictly positive in the specified real embedding, all12 points satisfy their squared-distance bound<=1/4, the complete-kernel evaluation matrix A has rank6, and its six weighted balance coordinates vanish exactly. If any nonzero real p in Pi_7 vanished on the nodes and were nonnegative on K_(1/2), its node gradients would vanish and it would equal a real linear combination of the complete kernel basis. Every evaluation at the12 points would be nonnegative, while the positive balance forces them all to zero. Rank6 forces all coefficients to zero, a contradiction. L5a and radius monotonicity give the second inequality in(1). These are exact finite checks backed by a written reduction and a distinct executed implementation, not finite-sampling extrapolation.

## Scope

One finite, coarse certified bracket for the precise PD-T075 optimal radius at n3. No optimality/sharpness, other n, monotone trend, all-degree asymptotics, working-precision recurrence realization or reading(G) conclusion. A lower endpoint from one polynomial remains valid without being optimal; an upper endpoint from full-kernel positive spanning rules out all polynomials. The distinction from the named P_n radius is preserved. A single completed n3 bracket does not pass or dispose of the full original G3 gate.

## Open items

n4--8 certified brackets and the saved G3 trend/otherwise decision, under a new prospective bounded cost plan before scaling. Root owns storage/commit integration and later report/gate disposition. Required Claude scientific/protocol audit, including the original timing-deviation disposition, remains pending. PD-T075(U2) stays OPEN and no asymptotic attempt is authorized by this n3 record alone.

## History

2026-11-05: Codex mathematics developer `/root/l1_l2`, assigned gpt-6.1-sol xhigh; runtime metadata not independently exposed. Rules read atbb67c1ee830d468fa33007e15008d5574d00ccf4; concurrent integration head observed844e812f127d52cab789ff7fc740fd799d389034. This record was created only after root and the distinct checker reported actual PASS and the owner read both full implementations, exact certificates, receipts and finalized report. Producer `/root/g3_producer` and distinct checker `/root/g1_port` used the required medium allocation; their executions are attributed separately and are not this mathematics worker's reruns. No new scientific run, code edit, Git mutation, final ID or self-audit by this owner.

2026-11-05 audit-01 response, Codex statement/metadata worker; requested gpt-6.1-sol high; runtime variant/effort not independently exposed. Rules read at `7f50cae80f5372db7c278aef4ba4a0a05e1137ea`. Canonical ID is `PD-T?lanczos-frontier-codex-L5-02` (aliases old PD-T L5b, L5b); its supporting reduction is L5-01. The distinct finite statement, endpoint data and proofs are unchanged. The audit independently reran the committed checker under both SymPy ground-types backends (flint and python), with matching mathematical fields; this reports [audit-01/L5.md](../audit-01/L5.md), not a new execution here. The saved candidate draft first entered Git at `0574c47` before its prospective source gate was complete. Later completed reading does not cure or waive that deviation; acceptance remains AC's decision. The dated chronology and missing-read/gate checkpoints are in [gate-timing-response-01.md](../gate-timing-response-01.md). No novelty or priority claim is added.

## History addendum — 2026-11-05 (handoff10; A-P1)

This result descends from L5-01 full-kernel finite positive spanning, drafted before completion of the mandatory reading gate and first committed at `0574c47`. AC accepted the disclosed deviation on 2026-11-05. The deviation remains permanently disclosed, not waived and not cured. Completed-gate receipt: G5: `844e812`; these are publication SHAs, not worker input/rules SHAs. G5 was first preserved in ideas-l5-continuation blob `6b811daa2449644dcf81a5ca822f88e8e5f5cfa3`, not first at `b6bf1f6`. L5a/L5-01 shares `844e812` with that receipt; its reported gate-before-development order is not established by Git. Earlier pending-decision wording is historical and is superseded by this dated acceptance record. See [gate-timing-response-01.md](../gate-timing-response-01.md).
