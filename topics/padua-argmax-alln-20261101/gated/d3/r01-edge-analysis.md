# Direction 3, round 1 — horizontal envelope and common-phase edge test

Date: 2026-11-02. Codex, assigned gpt-6.1-sol xhigh; runtime metadata not
independently exposed. Rules read at current administrative head
`3aebb299a4154dac822974b7245a9d243f21374e`; unchanged rule files have
the hashes recorded below (contract's rule reference
`aa1883f2fd9a837bb931ce804cb4b210c7475886`). The scientific campaign
base remains `7d308b10d946b607ae0690454f6c0103690775a4`.
Pre-execution contract: [direction3 round1](r01-contract.md).

## Gate and fixed scope

The full registry headings/aliases/summaries and obstruction/disposition
gate from direction1 round1 remains current: state/IDEAS.md has the same
SHA-256 `40ec132f73e55f82944ae497d2405f345a9f251b99702055a2c7baec7a4426df`.
Read the contract, the full horizontal supporting theorem, full fallback
records and pairing attempt, and the two-phase primitive statements/proofs.
Refreshed `edge`, `centreward`, `centerward`, `cell`, `common phase`,
`horizontal`, `primitive`, `reflection`, `translation`, `corrected mode`
across IDEAS, topic ideas/gate/attempts/theory and the literature INDEX.
Closest candidates are IDEA-305 and the retained original Claude03/E-C/E-P
variants. Existing O-R measured failures and exact O-Lt failure retain
their scopes; E-C's 76 measured comparisons remain finite support only.
No new mechanism, historical novelty claim or unread external theorem
transfer is introduced.

Rules-file hashes: AGENTS `c44a76f138fce01f02c06753b22fbc83fd5c1ee701785d49ba17cef5f8eee05b`;
WORKFLOW `a8927be27a1fe8166e5bcf59c7da8e70618ae0a5f17d56131724baffdad49353`;
CODEX `28ca2976171a34860e2bf8d24292af6b92bee34ce22ba1e497891b366533083b`.

## Common-phase identity and preregistered numerical execution

Let the physical first-edge index be j in {0,n}, m=n+1, and k,k' be
the eligible directed complementary centers in the contract. At the
common mesh phase u in [-1,1], s=pi*u. The exact vertical decomposition
on each complementary cell is

lambda_j(k+u)=S_n(0,s)-Delta_j(k,s).

The same phase uses the same corrected primitive at both centers;
therefore the finite common-phase difference is exactly

lambda_j(k'+u)-lambda_j(k+u)=Delta_j(k,s)-Delta_j(k',s).

Equivalently it is the finite endpoint-weighted sum of the differences
of absolute corrected two-copy kernels at the two ordinates. This
identity does not itself prove the sign. E-P asks its nonnegativity at
every phase, whereas E-C compares two whole-cell suprema and remains
logically separate if E-P fails.

Before executing the numerical command, fix n=7,12, all eligible directed
pairs (2 and 8), and exactly u in
{-1,-3/4,-1/2,-1/4,0,1/4,1/2,3/4,1}. Evaluate with the established
PD-T185 Edge evaluator and compare the same values with the original
coefficient-matrix evaluator. No optimizer, larger degree or additional
phase grid. Any reversal below -1e-6 is MEASURED only until an exact
algebraic/rational enclosure is established. All raw values from this
small command will be retained in this note or returned to the
orchestrator for its evidence files; no shared code/output path is
written by this math worker.

## Completed horizontal result

The full proof is preserved in
[theory16](../../theory/gated-codex-16-horizontal-compact-envelope.md).
For every real s the odd-board polynomial identity Fh(s)=-F(s,0)
gives Sh(s)=S(s,0), including all corrected-mode and collision values.
D1 global/local bounds therefore supply the missing horizontal phase
localization and vanishing gain. Combined with the previously proved
horizontal defect theorem, for any fixed nondegenerate closed interval
I subset(0,pi), each horizontal edge has envelope
Lambda_c-min_I g_h+o(1), uniformly over both edge signs and both degree
parities. The lower comparison chooses complementary centers **inside**
I within 2pi/n of a minimizing point, including boundary minima. The
upper maximizing point's nearest center may be outside I by pi/n;
compact uniform continuity handles that case. No numerical value for
g_h(pi/2), center-minimality, rate or threshold is inferred.

The explicit corner lower bound used in phase localization is PD-T157,
read in full (proof-attempts-2-codex-02-corner-explicit-leading.md).
PD-T159 is the bounded product comparison and is not the direct source
of that explicit inequality.

## Completed E-P screen

Actually executed the exact predeclared 90 sample comparisons: 2 pairs
at n7 and 8 at n12, nine common phases each, with the established Edge
evaluator. The same 180 point values were compared with the independent
coefficient-matrix evaluation path in maj.lam. The maximum absolute
validation discrepancy was 2.57571741713e-14. Arithmetic was Python/
NumPy float64, with no optimizer or fit. At cell endpoints u=+-1 the
compared points are Padua nodes, so the exact difference is zero; tiny
floating signs there are not reversals.

The following are the minimum differences over the seven **interior**
registered phases for each directed pair, not cell-supremum comparisons:

| n | edge j | k -> k' | minimizing sampled u | target-minus-source |
|---|---|---|---:|---:|
| 7 | 7 | 2 -> 4 | 0.75 | 0.0373243241370371 |
| 7 | 7 | 6 -> 4 | -0.75 | 0.0373243241370371 |
| 12 | 0 | 3 -> 5 | 0.75 | 0.0168875152116916 |
| 12 | 0 | 5 -> 7 | -0.5 | -0.0393766667442481 |
| 12 | 0 | 9 -> 7 | 0.5 | 0.0392592497173254 |
| 12 | 0 | 11 -> 9 | -0.75 | -0.0102372357340239 |
| 12 | 12 | 3 -> 5 | 0.75 | 0.0168875152116921 |
| 12 | 12 | 5 -> 7 | -0.5 | -0.039376666744249 |
| 12 | 12 | 9 -> 7 | 0.5 | 0.0392592497173254 |
| 12 | 12 | 11 -> 9 | -0.75 | -0.0102372357340226 |

All 18 n7 samples had no reversal below the registered threshold.
At n12 eight samples reversed: for each edge j=0,12, k5->7 at
u=-3/4,-1/2,-1/4 and k11->9 at u=-3/4. These observations are
MEASURED only. The selected strongest simple witness is n12,j0,k5->7,
u=-1/2: source angle9pi/26, target angle pi/2, source-minus-target
approximately .03937666674425. It lies in the original registered grid.
No new point search was needed.

The finite worker independently constructed outward polynomial point
bounds for this exact algebraic-angle witness as part of its registered
certificate. The scoped negative statement and complete finite proof
reduction are preserved in
[N02](../../theory/gated-codex-N02-pointwise-edge-translation-obstruction.md).
Its initial CONDITIONAL status was closed by the distinct actual
producer/checker execution and seventeen malformed-input controls; N02
now records the exact inequality as PROVED at its declared scope.
That certificate is shared with the separately owned whole-cell E-C
finite proof; it does not make the stronger E-P statement equivalent
to E-C.

Float-screen environment: Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0; deterministic phases, no randomness. Raw JSON 18695 bytes, SHA-256 `ef965f99e3cce84502baa2a297dcbc48340e6f3bbba050d316b9ebe1ede2c751`, temporary path `/tmp/padua-d3-ep-r01.json`. It is local exploratory output, not proposed as additional essential committed evidence. The finite worker's small exact certificate/screen preserves the same registered inputs.

Reproduction of this separate floating screen uses `tests_common.Edge`
and `maj.lam`, with source hashes recorded in the raw JSON, and these
fully specified loops: for n in (7,12), j in (0,n), eligible k in
range(2,n) with j+k odd; compare each eligible k+-2 that is strictly
closer to (n+1)/2; evaluate Edge.one at (k+u)*pi/(n+1) and
(k'+u)*pi/(n+1) for the nine rational phases above; validate both
against maj.lam at first angle j*pi/n. No independent rerun of this
floating screen is claimed by this math worker.

## Gate recommendation

**STOP direction3's current sequence after round1, subject to the
independent review.** The horizontal envelope is proved at its precise
non-effective scope. The exact E-P counterexample kills the fixed-phase
pointwise translation route once finite certification closes. Whole-cell
E-C remains distinct: the finite worker's exact degree7/12 comparisons
are retained at that finite scope, with no all-n inference.

A phase-dependent alignment or a direct comparison of whole-cell maxima
could still prove E-C, but no uniform analytic map, sign inequality or
other independently testable all-degree repair emerged in this bounded
round. Merely restating E-C, increasing the degrees, or collecting more
surviving samples would not supply the required next lemma. No round2
or later direction work was executed. The all-square PD-T099 target,
effective thresholds and the corner obligations remain OPEN, and required
Claude audit remains pending.

## Independent closure — direction3 round1

The Astra xhigh checker accepted the horizontal primitive/envelope proof
including both interval-boundary arguments. Its distinct actual producer
and checker execution verified ten whole-cell E-C comparisons with twenty
source leaves, all eight exact E-P reversal witnesses, and seventeen
malformed-input controls on the final frozen sources. The selected N02
witness is therefore PROVED; the earlier conditional checkpoint is
historical. Full review and compact execution receipt are in
[gated/checks/d3-r01.md](../checks/d3-r01.md). Required Claude audit remains
pending. The orchestrator accepted STOP after this one direction-3 round;
no round2 or later work was executed by this worker.
