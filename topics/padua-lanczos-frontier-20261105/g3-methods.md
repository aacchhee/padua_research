# G3 n3 producer: prospective methods and cost caps

Rules/input head: `12879b5666a93f2ca88d89c3deaa7a152f883cc3`. Assigned technical developer: Codex gpt-6.1-sol medium (runtime effort metadata not independently exposed). No new mechanism or novelty claim: implement accepted L5a finite reduction and existing Taylor lower check only. Source review/recovery is read-only. **Scientific execution authorized and started after root reported Astrahigh acceptance of L5a at c684b6bb. Endpoint verification and independent checker remain pending.** Root owns Git/shared records. Independent implementation/execution is a separate obligation.

## Frozen scope and inputs

Only n=3, D=7, all 36 monomials, all ten nodes `(cos(j*pi/3),cos(k*pi/4))`, j+k even. Coordinates are encoded exactly in Q(sqrt2), with sqrt2 the positive real root. Balls include all R². Baseline polynomial: the twenty rational coefficients recovered from Git blob `c88017135d020db69ecf438794f0710dc5a09fda`, 3963 bytes, SHA256 `287e8dd0bdaa60d93d728045fcd47c5c75832813657f4849081fe4b1e0629e8b`. The producer must recover/hash these bytes itself; old printed radius is unused.

## Arithmetic and exact acceptance

Use Python Fraction pairs a+b sqrt2. Sign compares a² against 2b² when a,b have opposite signs; this chooses the positive embedding without floating root ordering. Exact Gaussian elimination builds the entire 30-by-36 first-jet matrix and its complete nullspace. Recheck JB=0, rank B=36-rank J. Expected ranks in historical source are predictions only.

For each U=2^-j, j0..20, candidate offsets are U(a/q,b/q), a²+b²<=q², q=2,4,8 in order. Remove zero evaluation rows and duplicate exact points with a retained explicit list. Select d independent evaluation rows exactly. Floating scipy HiGHS proposes nonnegative weights balancing the evaluation rows, with each selected row's weight at least one. A basic solution has small support; reconstruct by rationalizing free weights and solving pivot weights over the exact field. Retain positive weights only and accept only after exact A^T lambda=0, rank A=d, and every distance and sign check. Failures are INCONCLUSIVE, including float solver infeasibility.

The implementation loops U from largest to smallest for each grid; every accepted upper is retained and the smallest reported. No q16 or extra families, no all-degree inference, no n4--8 execution. The saved eight extra bracket bisections remain permitted but are omitted from this bounded pilot unless root requests a cost refinement.

For the lower endpoint, expand the actual pstar by the binomial formula at each node. Verify nonzero degree<=7, exact value and first derivatives zero, Hessian hxx>0 and det>0. Set mu=det/trace; sum absolute exact coefficients per degree. Accept the largest saved dyadic L such that sum(S_k L^(k-2))<=mu/2 at every node. This controls whole balls by L5a. A failed polynomial/grid yields no lower claim.

## Per-stage caps, fixed before execution

- Source hash/parse and arithmetic sanity: 10 seconds, 64 MiB additional storage.
- Full first-jet rank/kernel and identities: 120 seconds CPU/wall budget, 512 MiB process memory.
- Local Taylor lower, all21 dyadics: 60 seconds.
- Each q grid: 150 seconds wall, at most21 LP calls, each solver time limit5 seconds; exact row count <=10(2q+1)^2, exact reconstruction at most three denominator scales (10^6,10^9,10^12). No more than12 retained certificate points preferred; larger small support is allowed only within16KiB evidence limit.
- Entire invocation: 660 seconds external timeout; process address-space cap2GiB. Stop exhausted stages with explicit INCONCLUSIVE/CAP records. Raw output under `/tmp/padua-lanczos-frontier-g3`; committed exact source certificates and receipt normally <16KiB each. No unchecked or truncated certificate is accepted.

A failed stage preserves reason/timing; no automatic unbounded retry. A subsequent larger search or n4--8 requires a new dated cost plan and root acceptance based on observed pilot cost.

## Planned commands (NOT RUN)

`timeout 660s python3 topics/padua-lanczos-frontier-20261105/code/g3_producer.py --out /tmp/padua-lanczos-frontier-g3/producer-n3`

Actual command, source hashes, versions, elapsed time, selected exact data and verifier results will be recorded only after execution. Independent port must regenerate ranks/jets/signs/distances/dependence, not import this producer's arithmetic or trust its summaries. G3 remains NOT RUN until that execution; a single n3 bracket will not pass the full original G3 criterion. U2 remains OPEN.

## Authorized pilot execution

Root released n3 only after independent acceptance of the reduction. Started original documented invocation at source SHA256 `d5973f6302038e1ad2b6b5ccc7db3a133757e08817f8e3019c166cd43c5efc7b`, head `12879b5666a93f2ca88d89c3deaa7a152f883cc3`. Pre-start methods SHA256 `c8bdbd3cacecb4478712c8a4b71ff1fcb1ed2fba6f653d0391c6b3661f61d032`. Frozen source and pre-start record: `/tmp/padua-lanczos-frontier-g3/producer-n3/{producer-frozen.py,start-provenance.json}`. Original caps apply. Execution/endpoint outcome will be appended after completion; no current bracket acceptance claim.

## Completed n3 pilot (independent validation pending)

The documented command exited0. Actual source remains SHA256 `d5973f6302038e1ad2b6b5ccc7db3a133757e08817f8e3019c166cd43c5efc7b`; Python3.12.14, NumPy2.3.5 and SciPy1.17.0. Elapsed171.489801831seconds, peakRSS75008KiB. Full first-jet matrix rank30, complete kernel dimension6 and basis rank6; construction plus exact identities completed by0.357371511seconds. Individual lower/grid timings were not instrumented; no separate timing is inferred. All21radii on each q2/4/8 grid completed within their caps, with no partial/capped stage.

Producer exact acceptance supplied lower `L=1/512` from the actual20coefficient pstar and upper `U=1/2` from12retained q8 points with strictly positive exact weights and full rank6. These are candidate finite endpoints pending distinct checker execution, not yet a completed computer-assisted PROVED statement. The lower bound checks all Taylor coefficients at all ten nodes and entire balls in R². The upper bound excludes the full first-jet kernel, rather than bounding the named pstar's positivity radius.

Preserved proposer outcomes: q2 all21INCONCLUSIVE; q4 U=1exact accepted,20INCONCLUSIVE; q8 U=1and1/2exact accepted,19INCONCLUSIVE. q4 j15andj20 returned numerical LPstatus4; all other failed LPs returned status2. These solver outcomes do not establish infeasibility or any negative mathematical claim. No bisections, extra families or n4--8 run occurred. This single coarse n3 bracket does not pass the original full G3 trend criterion; U2 remains OPEN.

Durable essential evidence (all <16KiB):

- `evidence/g3-producer-n3-lower.json`,2704bytes,SHA256 `48ea29641bde627b69a069ffa01687089f6decc0258ab0afa516ca69863b7e3c`.
- `evidence/g3-producer-n3-upper.json`,2136bytes,SHA256 `5c0c70e976711b31d0eed6c91b1c422fd8247ec9805a630e669618b47b9ef2a3`.
- `evidence/g3-producer-n3-receipt.json`,9506bytes,SHA256 `985e7a1db060f28623cd5f47a120f6123562ad095d8e263f43dac7943420bb0a`; includes all63proposal records, input/code pins, environment and observed costs.

Raw frozen source, stdout, start provenance and inventory remain under `/tmp/padua-lanczos-frontier-g3/producer-n3/`; archival manifests are root-owned. Distinct checker `/root/g1_port` received final source data and hashes and owns its separate implementation/execution/report. No independent PASS is claimed by this producer. Next obligation: exact independent reconstruction of kernel/field/points/weights and lower polynomial/Taylor checks, then root disposition and a separately accepted cost refinement before any scaling.
