# Direction 3, round 1: finite edge-cell certificate

Registered before new execution, 2026-11-02. Codex assigned gpt-6.1-sol
xhigh, runtime metadata not independently exposed. Rules unchanged from
`aa1883f2fd9a837bb931ce804cb4b210c7475886`; current supplied checkpoint
`3aebb299a4154dac822974b7245a9d243f21374e`, scientific base
`7d308b10d946b607ae0690454f6c0103690775a4`.
Read `gated/d3/r01-contract.md`, the exact E-C/E-P definitions in
`attempts/P3-P5-and-pairing.md`, existing pairing code/output, the outward
constructor and Bernstein arithmetic. This implements those already
retained candidates, with no new novelty/literature claim. The prior
O-R/O-Lt obstructions and measured E-C results are unchanged.

## Registered scope and bounded test

Only n=7,12. At vertical-edge index j=0 or n, eligible integer centers
satisfy 2<=k<=n-1 and j+k odd. Enumerate every k'=k+-2 still eligible
with |2k'-(n+1)|<|2k-(n+1)|: expected counts 2 at n=7 and 8 at n=12.
The source is the whole closed angular cell
`phi*pi^(-1)*(n+1) in [k-1,k+1]`. A strict upper bound on its supremum
below a lower bound at the target center phi=k'*pi/(n+1) proves the
desired strict E-C comparison. No floating optimizer supplies a bound.
Stop and retain an unresolved certificate if target-center bounds or
subdivision fail within 4096 leaves/depth24 per pair or about180CPU seconds.
No new degrees or global finite certificate scan is authorized.

Separately evaluate E-P at all ten directed pairs and exactly the nine
registered common phases u=-1,-3/4,-1/2,-1/4,0,1/4,1/2,3/4,1.
A float target-minus-source below -1e-6 is MEASURED; if one occurs,
seek a rigorous witness at the same rational-angle pair using outward
polynomials. Check every witnessed difference by integer intervals.
Surviving samples do not prove E-P, and an E-P failure does not refute E-C.

## Finite reduction and certificate to be checked

Use the existing corrected-cardinal constructor `finite_general.construct`
at 192-bit outward integer precision S=2^192. Its rational Machin/Taylor
cosine intervals enclose all coefficients of every cardinal polynomial;
the exceptional coefficient C_(n,0)=1 is retained. Restrict x to the exact
edge value +1 for j=0 and -1 for j=n, producing degree<=n univariate cardinals P_B(y).
Let ylo be the lower cosine enclosure at (k+1)*pi/(n+1), and yhi the upper
enclosure at (k-1)*pi/(n+1). The closed source cell is contained in the
dyadic physical interval [ylo/S,yhi/S], because cosine is decreasing on
[0,pi]. An upper bound on that entire enlarged interval is sufficient.

For any rational physical interval [a,b], express each cardinal in degree-n
Bernstein form for y=a+(b-a)z, 0<=z<=1, using the exact rational weights

`y^i -> sum_(h<=min(i,r)) binom(i,h)*a^(i-h)*(b-a)^h*binom(r,h)/binom(n,h)`

at Bernstein index r. Apply outward integer linear combinations to the
coefficient intervals. Every exact cardinal coefficient is enclosed. With
nonnegative Bernstein basis and its partition of unity,

`sum_B |P_B(y)| <= max_r sum_B max(|lower_Br|,|upper_Br|)/S`.

This bound remains valid through outward de Casteljau bisection. A complete
prefix-free binary leaf partition therefore bounds the entire source
closed interval, including all cardinal sign changes and endpoints.

At the target center, evaluate each univariate polynomial with outward
Horner arithmetic on the rigorous cosine interval. The sum of interval
absolute-value lower bounds is <=lambda at the actual target point.
The actual center belongs to its target cell. Hence strictly positive
`target_lower - source_upper` at every source leaf proves
`sup_source lambda < lambda(target center) <= sup_target lambda`.

The compact certificate records exactly the expected directed pairs,
dyadic source endpoint bounds, target center interval/lower bound and each
leaf path/upper bound. The checker reconstructs all polynomial intervals,
endpoints, centers and Bernstein coefficients from pinned sources, rejects
uncovered/duplicate/overlapping leaves and forged bounds, and checks all
strict comparisons by integers. Mathematical status stays OPEN until
complete evidence, checker, arithmetic controls and a distinct actual
replay are present. Any proven finite statement will have its separate
durable theorem17 record and retain its n=7,12 scope.

## Planned commands

`python topics/padua-argmax-alln-20261101/code/gated/d3_edge_generate.py --output topics/padua-argmax-alln-20261101/outputs/gated/d3_edge_certificate.json --ep-output topics/padua-argmax-alln-20261101/outputs/gated/d3_ep_screen.json > topics/padua-argmax-alln-20261101/outputs/gated/d3_edge_generate.out`

`python topics/padua-argmax-alln-20261101/code/gated/d3_edge_check.py topics/padua-argmax-alln-20261101/outputs/gated/d3_edge_certificate.json --output topics/padua-argmax-alln-20261101/outputs/gated/d3_edge_check.json --controls > topics/padua-argmax-alln-20261101/outputs/gated/d3_edge_check.out`

The producer's own replay is development validation; a distinct checker
agent must actually rerun before a computer-assisted PROVED claim.
Required Claude audit remains pending.

## Completed finite computation

The final frozen producer command was the planned command above with
`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1` prefixed, from
`/workspace/padua-argmax-alln`. It completed in 4.749713391 CPU seconds
(4.749876563 wall seconds). Python 3.12.14 exact integers/Fraction provide
all certificate arithmetic; NumPy 2.3.5 / SciPy 1.17.0 are used only by the
separate MEASURED E-P evaluator. No optimizer, randomness, degree beyond
7/12 or global finite certificate search was used.

Every one of the ten directed E-C comparisons succeeded, using exactly
the two leaf paths `0` and `1` for each source. Those halves bisect the
enlarged **physical y interval**; they are not an angular half-cell claim.
There are no pending leaves. The table shows approximate decimal
renderings of the exact outward bounds; acceptance uses integer scaled
bounds in the certificate, not these decimal values.

| n | edge j | k -> k' | whole source upper | target-center lower | strict margin lower |
|---:|---:|---:|---:|---:|---:|
| 7 | 7 | 2 -> 4 | 4.7844467434 | 5.0721322218 | .2876854784 |
| 7 | 7 | 6 -> 4 | 4.7844467434 | 5.0721322218 | .2876854784 |
| 12 | 0 and 12 | 3 -> 5 | 6.4928199256 | 6.7450762694 | .2522563438 |
| 12 | 0 and 12 | 5 -> 7 | 6.8022965470 | 6.8104017598 | .0081052129 |
| 12 | 0 and 12 | 9 -> 7 | 6.6913585451 | 6.8104017598 | .1190432147 |
| 12 | 0 and 12 | 11 -> 9 | 6.2213178212 | 6.6099891474 | .3886713262 |

The actual edge convention in both proof and executable is x=+1 at j=0,
x=-1 at j=n, including even n=12. An initial drafting typo `(-1)^j`
was corrected before any execution. Both edges at n=12 were independently
constructed/evaluated by the code; no floating symmetry assumption is used.

The 90 separately registered E-P float samples have eight reversals below
-1e-6, all at n=12 and each certified afterward with outward polynomial
bounds. For each of j=0 and j=12, they are k=5->7 at phases
-3/4,-1/2,-1/4 and k=11->9 at phase -3/4. The designated exact witness is
j=0,k=5->7,u=-1/2: source phi=9pi/26 and target phi=pi/2. At scale S=2^192,
its source-value lower numerator minus target-value upper numerator is

`247171343154114144115533517377438935359423611891579067211 > 0`,

whose quotient by S is approximately .0393766667442563. Thus that pointwise
translation reverses, while the whole-cell E-C comparisons above remain
strictly valid. The scoped negative mathematical record belongs to the
parallel worker's `gated-codex-N02` file; no negative claim about E-C or
the all-degree corner target follows.

The developer checker accepted the final certificate and rejected all
17 malformed controls: missing/wrong pair, nonedge index, missing/duplicate
leaf, invalid path, forged source upper/target lower, changed source
interval, target sample outside its registered center, changed source
hash, false complete flag, producer self-approval, missing designated
E-P witness, duplicate witness, nonpositive reversal and unregistered
phase. The final checker mandates the designated E-P witness, not merely
an arbitrary optional list. Earlier development-only certificate versions
were regenerated after this targeted robustness change; only the final
frozen hashes below support the completed result. No degree grid or
mathematical comparison changed during that strengthening.

## Frozen source and evidence identity

| Source | SHA-256 |
|---|---|
| `code/gated/d3_edge_common.py` | `fd3b278f167999def5a8f43ddd83da258e5ce2452a76082d9256dcde93d01b92` |
| `code/gated/d3_edge_generate.py` | `b0c2b98851dd8721bc876686fd388c62085938ff24d97308a132a7f14e9e3145` |
| `code/gated/d3_edge_check.py` | `5f43f69a427c415542848f8ae9e337c69b3a5b8f822e78db38e095a0a2c9a358` |
| `code/part3/finite_general.py` | `b20b7f88ddfc0bbc92e68096063ef626664028c2a379c34d16dc9f84e17aa74a` |
| `code/part3/finite_bernstein.py` | `a3133c6c22a365380f6c2ab14f6d31f60153d0df902b325cfcfbeeccc1bed74f` |
| `code/part3/finite_n2_exact.py` | `a5f00e6039d6ec76660cac90fb5720e0d6721348ed34c9e62775e1125d3e87c2` |

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| `outputs/gated/d3_edge_certificate.json` | 13561 | `0d660fc70e9db06624d6f8bd82371602c9f6d540b01124824e264624de0385b7` |
| `outputs/gated/d3_ep_screen.json` | 24993 | `3215523e1a768ce7e81c76283ac18bf476f8162bdcd84e579a7b93388707d14c` |
| `outputs/gated/d3_edge_generate.out` | 1916 | `56dd95b333d6ceedb49434b9625bca50bcfde23f3d8fb57af0574c88665de314` |

Developer replay receipt and distinct-agent final execution are recorded
below. The certificate preserves the pre-execution note
hash; appending this completion record deliberately changes the note's
current hash. Mathematical sources and final certificate remain frozen.
All small artifacts are local working evidence until the orchestrator's
commit/storage disposition; no cold-storage destination is invented.

## Scope and next obligation

The finite proof is of strict E-C for these ten whole cells, not exact
algebraic values of their suprema or an all-degree ordering. E-P's fixed
two-step translation fails in the stated finite scope. Any future all-n
E-C route needs a new analytic comparison that handles the maximizing
phases or maps source points to target points differently; additional
surviving sample degrees alone would not supply it. This worker has not
executed a later round or direction, changed Git/shared files, or supplied
an all-degree certificate. Independent execution has now completed and the
separate finite theorem17 is PROVED in its stated scope; the required
Claude audit remains PENDING.

Final round disposition supplied by the orchestrator: **STOP direction 3
after round 1**. The finite E-C result and the E-P obstruction are retained,
but no viable all-degree phase-alignment repair is currently specified.
The all-degree E-C target remains OPEN; no further scan or round is needed
to implement this disposition.

## Completed development and independent replay

The final developer checker command above (with the same thread-limit
environment prefix) accepted the certificate in 6.095775444 CPU seconds
and rejected all seventeen malformed controls. Its receipt
`outputs/gated/d3_edge_check.json` is 9696 bytes, SHA-256
`7fd1ca1b8c94ea1f1f2e699de1b9aa2a70f4e749d7fcf1dc34291bb376fe2f05`;
stdout `outputs/gated/d3_edge_check.out` is 8086 bytes, SHA-256
`7ed591e7d4b55da00f13172398d49146bda88f3a146cd4df3981c6d68fe15a0f`.

The distinct gpt-6-astra xhigh checker actually reran both final producer
and checker: all ten E-C pairs/twenty leaves/eight E-P witnesses/seventeen
controls passed and mathematical rows matched exactly apart from timings.
Its receipt `outputs/gated/check_d3_r01_receipt.json` is 10932 bytes,
SHA-256 `d77ee6d68926d3b19eaf663a6837a5fbcc9d9115fec0db36f26076cd37bf539b`.
Coverage, comparisons and review are recorded in `gated/checks/d3-r01.md`.
The separate finite theorem is
`theory/gated-codex-17-finite-edge-cell-comparison.md`; the exact E-P
counterexample is independently retained by the mathematical worker in
the separate N02 record. Required Claude audit remains PENDING.
