# FLINT exact checker implementation pilot — 2026-11-05

Technical developer: Codex, requested gpt-6.1-sol medium; serving metadata is
not independently exposed. Rules read at dbe5c811e0b22498382c8b3a6f2b0f2d9eb66bfc.
Only the assigned FLINT checker, notes and compact receipts are changed.

## Prospective scope and arithmetic path

This is an existing finite implementation variant, with no new theorem,
mechanism, priority, family admission or endpoint model. Read P4-02's weighted
normal quotient and check_scans_review.py's independently reconstructed
triangular inverse identity. Every original node and source h=1,...,N_s-1
is retained at every completed prefix. No symmetry reduction is used.

Before implementation, agreed the exporter schema with n0_replay: all exact
points, unweighted polynomial-value B columns, norms d, selected alpha,
source squared scales, parents/axes, grading, choices/ties. The exporter
owns its code separately. Exported numbers are **untrusted inputs** to this
checker, not accepted because their source hashes match a native source.

The new checker first independently parses normalized positive distinct input
points and compares all exported triples. It checks full B^T W B=diag(d)
(in its row-column orientation), exact constant start and positive pivots.
It forms raw creators anew in FLINT, derives all candidate projection
coefficients by matrix multiplication, and verifies their residual vectors
are exactly the exported B columns. Every selected alpha and source scale
is compared. For adaptive pivot, both admissible candidates are constructed;
their checked residual norms give exact d/sigma score comparisons, with X
winning ties. Fixed rules, parents, grading and all choice/tie metadata are
checked. Thus creator induction supplies the prescribed monic basis and
Gram identity supplies orthogonality; the basis export is not an arithmetic
shortcut requiring trust in the native recurrence.

Only after validation, at each original node i the checker constructs
unit lower-triangular A_i with row k entries alpha_kl and subtraction of
a_k(z_i) in parent column, and computes G_i=A_i^(-1) using fmpq_mat.inv.
It additionally checks A_i G_i=I at every node. These are the same scalar
response coefficients from the existing quotient identity, obtained through
FLINT's matrix inverse rather than the producer's vector recurrence.
All h>=1 and k>=h feed each complete prefix's squared energy. No extra
node weight is inserted in v_hi; weights appear in Gram/scales/normal.
Normal diagonals, traces, positive/order endpoints are checked exactly.

References are compared across **all** JSON scientific fields, omitting
only elapsed_seconds and exact_gram_pairs_checked (the latter records a
different implementation's count; the new Gram checks every matrix entry).
A developer execution does not constitute distinct-agent approval.

## Dependency and execution boundary

Read cloud runtime skill and networking reference, queried runtime status,
and read /etc/codex/network-policy.json before network activity. Runtime
reported current enforced package-manager policy allowing pypi.org and
files.pythonhosted.org, VPN false and no required credentials. No secrets
or global configuration were read or changed. Actual install, with
additional network permission, was:

```sh
python -m pip install --no-cache-dir --no-deps --only-binary=:all: --index-url https://pypi.org/simple --target /tmp/padua-lanczos-nonproduct-20261105/deps python-flint==0.9.0
```

Installed wheel name reported by pip:
python_flint-0.9.0-cp310-abi3-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.
Runtime package reports python-flint0.9.0, FLINT3.6.0. Checker enforces one
FLINT thread and the pinned Python package version; these remain trusted
library dependencies. The wheel bytes were not retained separately.

Prospective pilots: original D36x9 and admitted D65x9, degrees4/6/8 where
cheap, at most60seconds per case, one extra serial CPU process. First
successful case must verify all basis obligations before inversion.
Existing original scalar3600 jobs continue unchanged. No degree16 launch
or result acceptance until the coordinator reviews pilot speed and obtains
a focused distinct review of this new result-bearing implementation.

## Completed runs

The individual evidence/flint-check-*.json receipts pin input, export,
exporter source/binary, checker code, comparison files, command and output.
Raw exports, arrays and logs remain under /tmp. Pilot summary and final
assessment will be appended after the bounded runs; nothing unexecuted is
reported as completed.

## Bounded block variant preregistration and first result

After the generic path's degree6 cost and alt8 timeout, the coordinator
authorized **one** additional implementation variant, at most ten minutes
of coding/pilots: disjoint `flint_disk_block_check.py`, BJ6 then alt8, each
with60s cap. No original checker edit, symmetry/source reduction or degree16
run was authorized. The copy differs only in inverse algorithm, method/status
labels and phase timers. All exported basis checks, node A*G=I checks,
source loops and endpoints are retained.

For A=[[L,0],[C,R]] with unit lower-triangular diagonal blocks, recurse on L,R
and use inverse [[L^-1,0],[-R^-1 C L^-1,R^-1]]. Multiplying A by this candidate
gives upper blocks I,0 and lower blocks C L^-1-C L^-1,I. Thus it is the exact
inverse, with recursion ending at [1]. This is elementary block algebra for
the same matrices, not a new representation, normalization or finite reduction.
Five tiny unit-lower rational matrices of sizes1,2,3,5,8 matched FLINT's generic
inverse exactly before node pilots.

Actual BJ6 block pilot: all scientific fields against both accepted native
paths PASS, all324 inverse-product guards PASS. Checker3.460s; basis0.236s,
inverse0.832s, inverse validation1.030s, energy accumulation1.163s.
These separate counters cover the complete original node set. A generic
BJ6 inverse pilot took17.178s, so the block algorithm improves that generic
implementation substantially; it does not establish a gain over original
scalar BJ6 (~1.067s in the earlier speed assessment). Alt8 is still pending
at this addendum. No degree16 check is claimed.


## Final bounded disposition

| Family/rule/cap | Algorithm | Checker seconds | Exact comparison |
| --- | --- | ---: | --- |
| D36x9 alt4 | generic inverse | .473 | PASS all fields vs producer and scalar |
| D65x9 alt4 | generic inverse | .313 | PASS all fields vs producer and scalar8 prefix |
| D36x9 BJ6 | generic inverse | 17.178 | PASS all fields vs both degree8 prefixes |
| D36x9 pivot6 | generic inverse | 35.644 | PASS all fields vs both degree8 prefixes |
| D36x9 alt8 | generic inverse | timeout60 | INCOMPLETE; no endpoint result/comparison |
| D36x9 BJ6 | block inverse | 3.460 | PASS all fields vs both degree8 prefixes |
| D36x9 alt8 | block inverse | timeout60 | INCOMPLETE; no endpoint result/comparison |

The generic queue stopped after alt8 timed out; generic D36pivot8 and
D65alt8/pivot8 were **not run** by this developer. The two degree4 cases
were rerun after direct-prefix reference support was added; the table and
current receipts describe those pinned runs, not overwritten initial runs.
The separate scan_check worker reported its own generic degree8 attempts;
these are not counted as developer executions here.

The bounded block attempt is finished: it substantially improves the generic
inverse at BJ6 but remains slower than the original scalar implementation.
For comparison, accepted p6-benchmark8-D36x9.json records scalar alt8 at
11.204s, whereas the new block check did not complete alt8 within60s.
Actual timings differ in concurrent load, so this is a cost-screen decision,
not a controlled estimate of a precise speed ratio. No material speed gain
over the existing checker is demonstrated. The successful BJ6 phase profile
shows inverse/product verification/energy all contribute materially; the
incomplete alt8 log contains no final phase totals and none are inferred.

Do not use either FLINT path as a faster replacement or launch degree16 on
the present evidence. Keep both as bounded, unsuccessful performance
variants with successful small exact validation cases. No degree16 FLINT
run occurred; no disk16 independent-verification or family conclusion is
promoted. Original scalar3600 followups remain unchanged.

Reproduction: the individual successful receipts contain full checker argv,
all code/input/export/binary/reference identities, coverage and timings.
flint-check-pilots.json retains each actual additional exporter argv/output
identity and the generic timeout; flint-check-block-pilots.json retains the
actual block commands, phase counts, successful receipt identity and timeout.
Export generation for the original degree4 cases is in the separately owned
p6-basis-export-pilot.json. Each process in these queues was serial with a
60-second subprocess timeout. No raw arrays or unexecuted commands are
represented as committed completed evidence. No archival delivery is claimed.

Distinct review: scan_check reported a static review finding no blocker in
both inverse identities or retained checks, and independently owns its
replays/negative controls. This note does not convert that message into a
completed cross-family audit or claim an unperformed independent endpoint
rerun of the block path. Coordinator owns the final review disposition.
