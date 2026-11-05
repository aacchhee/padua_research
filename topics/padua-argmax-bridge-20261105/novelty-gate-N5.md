# N5 exact novelty gate — partial cotangent blocks

2026-11-05. Assigned developer: Codex, gpt-6.1-sol xhigh (assignment;
runtime model/effort are not independently exposed). Rules read at
`98d6c00d8a474cf97602c9cfdea631a837191ac0`. No Git or shared registry edit.

## Coverage

Read AGENTS, WORKFLOW, CODEX, bridge handoff01, plan, gates and the
input novelty baseline. Scanned all 1015 lines of `state/IDEAS.md` in
bounded chunks and explicit identifier/alias/summary views; read the
obstruction/disposition tables, including unrelated tracks. Registry SHA256:
`948c30b35cdb3ffacefe398acfb35439fc7e69f8be33fd94bc605b052b8d03c6`.
Large combined terminal reads truncated; missing ranges were subsequently
read in bounded views rather than treating a truncated result as a full read.

Search scope: Markdown under `state`, `tracks`, `topics`, `literature`,
excluding this new bridge topic for search counts. Case-insensitive groups:

| Terms / synonyms | Matching files / lines |
|---|---:|
| cotangent, cosecant, Ehlich, Zeller, Brutman, G[u/ue/ü]nttner, local maxima, ordering, centreward/centerward | 287 / 678 |
| partial...cot / cot...partial, pole subtraction/extraction, regularization, Euler–Maclaurin, midpoint, Peano, shifted harmonic | 130 / 298 |

Counts inventory the search, not a claim that every matching proof was read.
Relevant full reads: original alln ideas and fallback records; canonical
IDEA318/324/325; gated candidates including IDEA329; effective comparison-r3
(IDEA339/340); phase2 H2/H3 records (IDEA455/456/459/460/461).
Full mathematical reads: T185, T186, T189–191, T211, T226, T231,
T248/249, N080, T269 (including its local cotangent partial fraction),
T270 and T365. The whole-cell proof and the negative result were read,
not inferred from registry rows alone. T192's conclusion is context;
no part of its proof is imported into N5.

Read the literature INDEX warning and relevant rows/addenda LIT466/470/487,
then the complete Ehlich–Zeller, Brutman and Günttner source records.
These records report another reader's coverage; they are not this worker's
reading of those papers. The sources have no local PDFs (parent's checked
input); this worker transfers no external proof. Links and limits are in
`literature-N5.md`.

## Exact surviving problem and exclusions

E-C fixes n, m=n+1, physical j in {0,n}, eligible complementary centers
2<=k<=m-2 with j+k odd, and compares the suprema over closed intervals
[k-1,k+1] under a parity-preserving step 2 toward m/2. The maximizing
phases are independent. N080 proves only E-P's equal-phase reversal at
n12,k5->7,u=-1/2, by more than 39/1000. It does not reject E-C.
T231's ten comparisons and T249's three spots are finite exact theorems;
T248's 1536 comparisons are measured. None supplies an all-degree order.

T226 already gives signed row sums, exact cotangent coefficients, full
negative sign intervals and endpoint values on beta=0, |alpha|<=2/5.
Restating them or evaluating more rows fails its continuation gate.
T270 regularizes one fixed full half-interval with an O(n^-2) remainder.
T365 gives an O([n(n+1)]^-2) boundary profile using paired full sums.
Neither controls arbitrary contiguous truncated cotangent blocks with
uniformity as their first/last sample approaches either pole.

## Verdict and separation test

The scoped candidate is a **quantitative variant with difference** of
IDEA329/T226 and IDEA358/T270, supporting the existing N1/N5 continuation.
No historical originality claim. The proposed distinction is an explicit
fourth-order error for **every offset and every contiguous sub-block**,
after retaining the two nearest endpoint poles exactly. A remainder whose
constant depends on pole distance, or one that after coefficient weighting
cannot improve the previous O(log n/n^2) scale, erases the useful distinction.
The cheapest test is an elementary derivative bound and corrected-midpoint
kernel calculation, followed by nonproof high-precision checks near both
poles. Full T226 row/sign/collision assembly belongs to N1 by coordination.

The 1D interface was discussed with N1 while this written gate was being
finalized, after the relevant full predecessor reads. This is an informed
continuation, not a claim of a blind preregistration. Candidate records are
written before any new numerical experiment. No E-P rerun is authorized or
needed. All-degree E-C and PD-T099 remain OPEN.
