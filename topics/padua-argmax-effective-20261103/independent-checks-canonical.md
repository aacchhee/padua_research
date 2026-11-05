# Supplementary checker canonicalization impact check

Rules/input: `8a1f394739293953e1566fd24a0a193cc78ff26f`.
Codex, configured gpt-6-astra high; supplementary independent check,
**not Claude audit**. 2026-11-03. Status: **bounded corrective check
complete; corrected n=32 accepted, n=40 capped and unverified**.

## Finding and exact correction

The earlier native checker constructed transform terms with
`mpq_class(num,den)` and immediately added them. That constructor does
not canonicalize; GMP rational arithmetic requires canonical operands.
The checker developer found the issue after the original review boundary.
Matching previous outputs is insufficient to waive this precondition.

Historical native observations are retained with their actual source,
`ae4f20b69c5e676a5d2fefa55c903c8b3efd87a5807a5c5617ca21390a1cab3d`,
but **do not supply corrected-native acceptance**. The old independent
summary stays byte-for-byte unchanged, SHA-256
`01df7fd5e61793e49a13eb216ba1a0a4402d6b799f87b94682677058459feeaf`.
Its separately executed Python reference G0 results remain valid.

Corrected source:
`b0c871e7711219edfe3ce01480d8d1de3503a20d9b59f82b63a00eff248bc6e0`.
It adds `ratio(Z a,Z b)`, calls `q.canonicalize()` before returning,
and uses that helper for every transform term before `+=`.
Independently reversed exactly those two text changes in memory: the
result hashes to the historical source above. No other production
kernel change is hidden in this correction.

The matrix starts with canonical zero rationals; each new term is now
canonical before addition, so the GMP operation preconditions hold
inductively. Inspected every remaining direct two-argument rational
constructor: both are `1/2^224`, hence canonical. Existing `frac()` also
canonicalizes before its result is used. The correction preserves the
mathematical finite sum and outward interval proof.

## Independent exact transform differential

Executed `code/independent/weight_differential.py`. It snapshots the
corrected source, leaves its **actual production weight construction
unchanged**, and inserts only a print/exit block immediately afterward.
It does not copy a replacement implementation of that construction.

For every n=2,...,40, compared every resulting w[k][i] against a separately
computed standard-library Fraction/binomial expression. No reference or
producer arithmetic module was imported. All **23816 weights agree
exactly**, every denominator is positive, and every numerator/denominator
pair has gcd 1. This validates the actual corrected construction against
the Python formula; it is a finite regression, not a substitute for the
general canonical-operand argument above.

Essential receipt:
[canonical-weight-differential.json](evidence/canonical-weight-differential.json),
8477 bytes, SHA-256
`8d102246ae2b5e1796628c7cff59b0d6914bbcfecc8e402b86e688b58394d88a`.
It pins production source, instrumented source, executable, build command
and per-degree printed-weight hashes. The supplementary run took 1.654 s.

## Fresh corrected complete-certificate replay

Independently rebuilt using
`g++ -O3 -std=c++17 .../kernel.cpp -lgmpxx -lgmp`.
Corrected binary SHA-256:
`f17fed2e69a98c952d1ad5e72de03c08b2ceb07970c49fc0db1b35396fe3e605`.
The strict Python parser source is unchanged:
`b6c7320db2f7cfebf27fe33aa38ffdd45ff719870e3d23e15f845b6e8026eb2e`.

Executed in two independent processes:

```text
python topics/padua-argmax-effective-20261103/code/independent/canonical_replay.py 32
python topics/padua-argmax-effective-20261103/code/independent/canonical_replay.py 40
```

Each inherits a 600-second CPU cap and a 6-GiB address-space cap. The
orchestrator explicitly authorized up to four concurrent heavy kernels
within 16 GiB overall: this worker's two plus one each for the checker
and gates workers. Their corrected overlap replays are separate evidence.
The initial resource-wrapper launch found `/usr/bin/time` unavailable
before either scientific replay began; the runner uses standard-library
`resource.getrusage(RUSAGE_CHILDREN)` instead. No acceptance is inferred
from the initial launch.

Fresh corrected **n=32 accepted**: 282 leaves (280 bound, 2 corner),
281 splits. Canonical input SHA-256
`e17a8712fb257a219436e44e977eaa6a1e0287ba6a64a86c78e34009f984c609`;
fresh receipt `canonical-check-n32.json`, SHA-256
`d8150b457171ce7fa1b15a4507efd82f57c212644f397baba704d0aace7f43a9`.
Measured wall time 217.731 s, user CPU 217.009 s, system CPU 0.621 s,
maximum child RSS 1522816 KiB. This reproduces every supplied exact leaf
bound with the corrected arithmetic; historical acceptance is not used
as a substitute.

Corrected **n=40 reached the authorized CPU cap** and terminated with
SIGXCPU. There is no successful checker receipt and no proof acceptance
for this degree. The canonical producer input remains
`267725558e4c8c0626ec798d1a80bc44acc37da65909484398e14025f56d8b13`.
Measured aggregate child usage: 594.718 s user CPU, 10.636 s system CPU,
605.562 s wall time, maximum RSS 3900672 KiB. The inherited native CPU
limit was 600 s; aggregate waited-driver usage also includes termination
and driver overhead. The failure record is `canonical-check-n40-run.json`,
SHA-256 `5e17eb7a747d81e7019bcd91edfd222d5ddae3723279414c529743e292cba375`;
resource receipt SHA-256
`610882b6ce0f73a30ee335e768d9ee52893b0684d66650e578c35293d71f9196`.
This is a bounded computation outcome, not a mathematical rejection or
counterexample. A future full corrected replay is still needed at n=40.

The final versioned compact summary is
`/workspace/padua-work/independent/independent-summary-canonical.json`,
8995 bytes, SHA-256
`5bb29c15077b4e0a8246b8b949cb50d4ae10ad2ceab20539dca035c866259401`.
Its identical repository copy is [evidence/independent-summary.json](evidence/independent-summary.json).
It explicitly separates historical non-supporting native observations,
unaffected reference G0 and reference controls, corrected n=32 acceptance,
and the unverified capped n=40 run. No historical receipt was rewritten.

The canonical-operand implementation finding is resolved by the exact
source correction, contract inspection and finite regression. Fresh
degree-specific acceptance extends only as far as actual completed
replays; this worker supplies corrected n=32. Other workers' corrected
overlap receipts are documented separately. Required Claude audit remains
pending independently of this corrective verification.
