# Independent n=4 A5 certificate checker — executed verification receipt

Verification record, not a theory claim and not the required Claude audit.
Owner: Codex subagent `/root/a5_n4_checker`, inherited `gpt-6.1-sol` xhigh.
Rules read at `c26a6adf6ebf701368f5de73fc319b0e55cdfc13`:
`AGENTS.md`, `agents/WORKFLOW.md`, `agents/codex/CODEX.md`.
Scope: only new `code/a5_checker_n4*`, `outputs/a5_checker_n4*`, and this receipt.
No mutable Git operation; no n=3 source is imported or edited.

## Input and gate

Read AC's complete uploaded request, the n4 producer/checker schema, quartic
finite-reduction theory08, cubic theory05 only as a degree-specific predecessor,
and the programme source06. Sources supplied by the orchestrator are pinned to
programme `9bd14a6d2c4da69139a10107d8a787f2be0c5c9e` and part1 scientific head
`a09d910ae7d5526b1e216066421a0bee7fc20da4`; source06 supplies measured candidate
counts only. This checker reconstructs n4 directly and uses no part1 theorem.

Before mathematical work, scanned all `state/IDEAS.md` headings, identifiers,
aliases, summaries, and the complete campaign, seed, obstruction, lattice and
programme disposition tables. Searched `crease`, `quartic`, `Krawczyk`,
`sign.pattern`, `stationary`, `certificate`, `factor`, and `interval.Newton`
across the registry, programme and part1 records, theory, logs and literature
index. Read the full closest charter IDEA048 row, programme IDEA17 entry and
source06. Verdict: requested completion of registered A5, with a separate
certificate replay; no novelty/priority claim. The applicable source06
obstructions are tolerance coincidence, an escaped Newton iterate, incomplete
sign coverage, and unproved degenerate-point classification. The cheapest
decisive test is replay of a complete partition with every compatible sign
pattern and valid local witness, followed by independent execution. Quartic
singular Hessians and isolated-real common-factor zeros remain explicit;
cubic-only exclusions are not inherited.

The managed-cloud runtime skill was read and `environment_status` executed.
The environment was current, connected and enforced; no external credentials,
network operations or package changes were needed.

## Independent construction and trusted dependencies

`code/a5_checker_n4.py` does not import producer code. It explicitly constructs
the 15 parity-selected nodes from radicals and reconstructs total-degree
cardinals using exact field linear algebra. It verifies the inverse matrix,
all 225 cardinal node values, and `sum L_i=1`. Its interval implementation uses
integer endpoints at precision96, outward floor/ceiling on every multiplication,
and exact squared radical bracket checks. Natural polynomial evaluation and
the centered mean-value enclosure are intersected for cardinal sign coverage.

Trusted dependencies: CPython integer arithmetic and `fractions.Fraction`;
SymPy exact field, matrix, polynomial derivative, gcd and squarefree algebra.
There is no floating-point proof predicate. No producer subdivision, Newton
iteration, numerical root finder or root isolation is executed by the checker.

## Interior predicate justification

The supplied binary paths are replayed from the square, splitting the widest
side and x on ties. Prefix-freeness and exact Kraft mass1 verify the complete
finite leaf partition. For each leaf the checker independently computes forced
cardinal signs and requires exactly every compatible 15-bit mask, in order.
It checks every pattern rather than returning after a first root witness.

For a strict lambda maximum every active signed polynomial has a strict
maximum, by `P_s(w)<=lambda(w)<lambda(z)=P_s(z)`. The implemented exclusions are:

- An identically zero partial gives a constant line, contradicting strictness.
- A gradient component separated from zero excludes stationarity.
- Strictly positive Hxx or Hyy, or strictly negative Hessian determinant,
  excludes the negative-semidefinite Hessian necessary at a local maximum.
  A zero eigenvalue is never discarded by this predicate.
- For a common-gradient factor, the exact derivative gcd and quotients are
  reconstructed. A nonzero quotient forces every stationary point onto the
  factor. A nonzero derivative of its squarefree part gives a regular real
  curve; the signed polynomial is constant along it. Singular/isolated-real
  factor zeros fail this predicate.
- An exact stationary node has lambda1, a global minimum since `sum L_i=1`.
  A stationary exact regular cardinal zero is excluded by flipping that active
  sign and subtracting the two stationary gradient identities. An injectivity
  witness on a rational convex rectangle containing the entire leaf and exact
  point forces every possible stationary point in the leaf to be that point.
- A root witness verifies an exact outward Krawczyk inclusion strictly inside
  its rational box and `||I-C H||_infinity<1`. This is a contraction mapping
  existence/uniqueness proof for `z -> z-C grad P(z)`, with C invertible.
  Strict cardinal signs and a negative definite Hessian prove a smooth strict
  lambda maximum. A second contraction witness on U containing both the leaf
  and root box shows every stationary point in the leaf is that root. Distinct
  root records must have disjoint boxes, so repeated leaf references count once.

The injection argument uses the integral of the Hessian along the segment
between two alleged zeros in the convex rectangle. Their difference has norm
at most k times itself with k<1, forcing equality. This covers a supplied root
outside its referencing leaf without an escaped-Newton discard.

## Boundary coverage and predicates

For each of the four prescribed open edges, the checker reconstructs every
restricted cardinal and verifies it is not identically zero. It forms their
product and its squarefree part E. It independently verifies that E divides the
product of multiplicity-one factors from the cardinal factorizations. Thus
every actual crease zero is a regular zero of at least one restricted cardinal;
the all-active tangent derivative argument excludes a maximum there, including
crossings, exactly.

The checker computes the rational norm by explicitly multiplying the four
coefficient conjugates (`sqrt2` and `sqrt5` independently changing signs), rather
than calling the producer's `Poly.norm`. It removes repeated factors, builds
an exact rational Sturm chain by polynomial remainders, checks one root per
supplied interval (or exact rational singleton), strict pairwise disjointness,
and equality with the total all-real Sturm count. It never isolates roots.

The complete norm-root list subdivides every actual sign component. An actual
component between two actual E zeros contains a gap between consecutive
norm-root enclosures and hence a supplied rational sample; exterior components
are covered by exterior samples. Extra conjugate roots only add subdivisions.
Every sample sign is computed exactly, and the set of distinct masks and all
ordered per-mask records are checked. For each nonconstant signed edge
polynomial q, roots of q' shared with E are already excluded regular creases;
all roots of the remaining squarefree derivative norm receive a disposition.

An outside interval, nonzero selected-embedding derivative, inconsistent
cardinal sign or strictly positive q'' excludes an active edge maximum. For an
accepted root interval U, strict cardinal signs make lambda=q locally; q''<0
and opposite strict endpoint signs of q' prove exactly one tangent maximum by
the intermediate value theorem and monotonicity. Strict inward normal descent
then proves a relative strict maximum on the square. Strict inward ascent
excludes it. An actual candidate in its supplied norm interval lies in U, so
the unique stationary point in U covers it. Accepted U intervals on the same
edge are disjoint, and canonical global edge ids prevent double counts. Zero
normal derivatives and degenerate tangent cases have no accepted fallback.

All four corner records must occur in order. Node corners have exact value1
and cannot be strict maxima because lambda>=1. At each non-node corner the
checker derives exact zero-cardinal indices and enumerates every active sign
choice. Both inward partials must be strictly negative for each active
polynomial. Finiteness gives a uniform negative first-order bound on the
feasible corner cone; inactive patterns stay below by continuity. Thus each
accepted corner is a strict relative maximum. No tolerance is used.

## Optional global-value verification

The optional global file is bound to the exact count-certificate SHA256. The
checker bounds every714 occurrence of the interior `flat` predicate by its own
P evaluation, and checks the supplied uniform upper bound below4. It checks
all13 interior and12 edge value enclosures below4, proves every constant edge
restriction is exactly+1 or-1, and reconstructs the exact equal values of the
two non-node corners in the four-dimensional radical basis, with lower bound
above4.

The count exclusions other than `flat` also exclude non-strict maxima: gradient
and curvature necessities, regular-crease all-active derivatives, inconsistent
signs, inward ascent, and injectivity remain valid without strictness. The
actual n4 certificate uses only gradient/flat/hessian/root interior predicates;
optional regular-point/factor predicates are not needed for this global
argument. The explicit flat value bounds close the only non-strict gap.
Compactness supplies a global maximum; if it were outside the two non-node
corners, the coverage would either exclude it or bound its value below4.
The corners have the same exact value above4. Therefore they are precisely all
global maximizers; an unseen non-strict plateau above4 is also excluded.

## Executed checks

1. Independent exact construction and prefix controls were executed with
   `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/padua2-deps python -B` through
   `runpy.run_path` of the checker. Observed 15 nodes, 15 cardinals, all exact
   interpolation identities passing; partition `{0,10,11}` passed and incomplete
   partition `{0,10}` was recognized as incomplete. Construction took about
   4.71seconds. This is a checker developer execution, not the required
   different-agent producer/checker replay.
2. The first integration attempt used a symbolic signed-polynomial sum for
   every mask and was terminated before a result. The checker then changed to
   exact integer coefficient vectors derived from its independently rebuilt
   cardinals, retaining symbolic algebra only for optional exact-factor/point
   predicates. No producer implementation was imported.
3. The optimized integration replay of `/tmp/a5-n4-spatial-2.json.gz` completed
   in33.690737367seconds with Python3.12.14 and SymPy1.14.0. It verified the full
   2732-leaf prefix partition, every490672 supplied compatible-mask disposition
   (`gradient`489824, `flat`714, `hessian`82, `root`52), and13 disjoint Krawczyk
   root boxes. The actual certificate rows are counted, separately from the
   producer's accumulated search profiling counters. Certificate SHA256:
   `a60e352d5e55b60e24be0a6f58392e41876f6a5c98bbff79491e431bfc884537`;
   bytes1079278 (preliminary artifact over the per-file limit, retained in/tmp).
   Executed checker source hash:
   `077bac1c2748c078b6c9283cb63de2854780846c63c88ae251844be7b7dd91fd`.
   Command:
   `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/padua2-deps python -B code/a5_checker_n4.py /tmp/a5-n4-spatial-2.json.gz --allow-partial --output /tmp/a5_checker_n4_spatial-2.json`
   (topic directory as cwd; the actual execution used the absolute code path).
   Output remained `accepted=false`, `count_certified=false` because this
   preliminary certificate contains no boundary records. This is an executed
   independent checker implementation, not yet the different-agent full replay.
4. Separate boundary integration against `/tmp/a5-n4-boundary-1.json` completed
   in137.106196965seconds. It verified all4 edges,86 sample-derived patterns,
   842 derivative-norm root dispositions (`derivative`480, `minimum`100,
   `outside`172, `sign`78, `root`12),12 disjoint edge maxima,2 corner maxima and
   all8 active corner patterns. Input SHA256:
   `f1014f1e8518b58196feecfbdb1198bc73dfef6901ec8795e75ec4c8b9824a30`.
   Checker SHA256 at that execution:
   `844b6fb7d25ed6157a1821b96ed8c9ee3ad29705c2a93311dc6d8a689c775294`.
   Used `runpy.run_path` of the checker and `Verifier.boundaries` on the supplied
   JSON; output `/tmp/a5_checker_n4_boundary-1.json`. This was an actual separate
   boundary replay, not a root search.
5. Meaningful coverage/counterfeit controls first completed in8.58434775seconds
   on checker401a914f. The final reproducible harness
   `code/a5_checker_n4_controls.py` has SHA256
   `6ff60f6545f98fe09ead2a4749f399091e9de12615ae957cdbb502189ed64b61`.
   It was actually rerun in8.477368941seconds against final checker
   `1fe4f74ffe21447134e1c2f34e6364f3ca73929f207c7ebd8f3ea8977e53d143`;
   output `outputs/a5_checker_n4_controls.json`. Overlapping prefix, missing
   square leaf, missing compatible-mask row, singular preconditioner, false flat
   predicate, zero-Hessian exclusion, missing Sturm root and a false root
   interval were all rejected. A positive Sturm control verified
   `(t²-2)(t-1)` with two irrational-root intervals and the exact rational
   singleton1. Fourteen deterministic signed coefficient vectors exactly
   matched independently summed symbolic polynomials. No fake certificate
   artifact is retained. The final harness also rejected using a strict-only
   factor-curve predicate as a global plateau exclusion. Command from topic cwd:
   `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/padua2-deps python -B code/a5_checker_n4_controls.py outputs/a5_n4_certificate.json.gz --output outputs/a5_checker_n4_controls.json`.
   Each control executed the checker function, rather than matching output text.
6. The first full combined count/global replay completed in158.751383963seconds
   on checker401a914f: `accepted=true`,27=13+12+2, and exact global argmax
   `(−1,−1),(1,−1)`. Before final freeze an explicit optional-global guard was
   added: only the four actual interior disposition types are supported, and
   cut>1 is required. This rules out importing a generic strict-only factor
   exclusion into a non-strict global argument; no actual certificate row
   changed.
   The committed count artifact is64360bytes with
   SHA256 `14a69a131b3c20416fd5521bd971efdadd4e3741f70546d0fc5f0d9f25a2cf61`;
   global artifact SHA256
   `7bc43988a28848037f0b10b4e6c59cadb9dffa772e939175853e3769f7f6003a`.
7. Final frozen checker1fe4f74f was actually executed on the full count and
   global artifacts and completed with exit0 in159.835996067seconds. All
   partition/predicate/boundary/global checks passed. Observed27=13 interior+
   12 non-corner edge+2 corner maxima;2732 leaves;490672 interior pattern
   dispositions;86 edge patterns and842 norm-root dispositions;8 active corner
   cases. The checker proved the exact common value
   `(13+sqrt2+2sqrt5+sqrt10)/5` at `(−1,−1),(1,−1)`, strictly above4, while all
   25 interior/edge root-value enclosures and all714 flat-leaf occurrences were
   below4. Its independently obtained flat upper bound is
   `195815277203118945162885237407/79228162514264337593543950336`, two units of
   precision96 tighter than the supplied producer bound.

Exact final command executed from `/workspace`:

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/padua2-deps python -B /workspace/padua_research/topics/padua-proof-attempts-2-20261101/code/a5_checker_n4.py /workspace/padua_research/topics/padua-proof-attempts-2-20261101/outputs/a5_n4_certificate.json.gz --global-file /workspace/padua_research/topics/padua-proof-attempts-2-20261101/outputs/a5_n4_global.json --output /workspace/padua_research/topics/padua-proof-attempts-2-20261101/outputs/a5_checker_n4_developer.json
```

Final controls command actually used the same absolute paths:

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/padua2-deps python -B /workspace/padua_research/topics/padua-proof-attempts-2-20261101/code/a5_checker_n4_controls.py /workspace/padua_research/topics/padua-proof-attempts-2-20261101/outputs/a5_n4_certificate.json.gz --output /workspace/padua_research/topics/padua-proof-attempts-2-20261101/outputs/a5_checker_n4_controls.json
```

| Own final artifact | Bytes | SHA256 |
|---|---:|---|
| `code/a5_checker_n4.py` |44335| `1fe4f74ffe21447134e1c2f34e6364f3ca73929f207c7ebd8f3ea8977e53d143` |
| `code/a5_checker_n4_controls.py` |4210| `6ff60f6545f98fe09ead2a4749f399091e9de12615ae957cdbb502189ed64b61` |
| `outputs/a5_checker_n4_developer.json` |9353| `1d98031e4c14c5f1150782a0013ff52bfbc1a0e1c576664bba70b6215e46b1d6` |
| `outputs/a5_checker_n4_controls.json` |1945| `5e004ba200b8ecb008d8fb76537d0c9500f6ea1f2eb03232d44c62d53cd8fa8f` |

Both generated outputs are necessary small evidence receipts and are below
the1MB per-file limit. The full final certificate is a single legitimate gzip,
64360bytes, so no required evidence needs artifact splitting or cold storage.
Preliminary/tmp diagnostics are superseded and are not required proof evidence.

## Runs needed and current limits

Checker source, control harness and final count/global inputs are frozen. Own
integration and controls are complete. The output key `count_certified` denotes
this checker's mechanical acceptance; a repository PROVED-status upgrade still
requires the written reduction/classification plus a different agent's actual
producer+checker rerun, which the orchestrator is arranging. This receipt is
the checker implementer's actual execution, supplementing those obligations.

The default is fail-closed; `--allow-partial` permits incomplete witness
inspection with `accepted=false`, `count_certified=false`. Optional generic
regular-point/factor interior predicates were implemented but are unused by
this final n4 certificate; the global-value mode expressly rejects them.
No degree beyond4 is certified by this checker. Required Claude audit remains
PENDING. Different-agent replay should use a helper-owned output and regenerate
the global certificate against the actual rerun gzip SHA256: timing fields and
gzip headers may differ, so raw-byte equality is not the mathematical replay
criterion.
