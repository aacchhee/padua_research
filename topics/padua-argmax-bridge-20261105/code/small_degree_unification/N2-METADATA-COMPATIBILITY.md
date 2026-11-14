# Degree2 initial-seed reporting compatibility

2026-11-07, source-only diagnosis and prospective repair. The first
independent replay at2 stopped with actual exit1 and
`ValueError: metadata x_cosine_seed`. No replay of3–16 ran in that attempt.
The failed raw witness remains unchanged at `certificates/n2.json.gz`;
the failed execution outputs remain at
`/tmp/padua-consolidation-small-review-1hhnptij/`. See the canonical
[consolidation audit](../../paper/consolidation-audit.md) for that execution.
This record does not relabel that attempt as accepted or hide a retry.

The producer reports its initial Taylor cosine seed `[-1,1]` at degree2.
Its actual x-axis midpoint is already replaced by the exact identity
cos(pi/2)=0. The independently implemented C++ checker also replaces its
midpoint by exact zero, but reported the *postreplacement* x-axis entry
`[0,0]` under the initial-seed metadata name. Its strict Python driver
correctly rejects the different metadata, before checking the leaves.
No false native acceptance or differing cardinal coefficients is asserted.

The new `metadata_kernel.cpp` changes only the reported initial x seed.
It recomputes the same independent Machin/Taylor initial seed, using the
existing C++ rational functions, and reports that initial interval.
`metadata-patch.json` records the two exact literal replacements against
the frozen baseline, both source hashes and exactly one occurrence of
each preimage. All cardinal, Bernstein, subdivision, threshold, tree and
leaf code remains byte-identical. Neither the original kernel nor any
certificate is rewritten. The unchanged strict Python checker still
checks every metadata field and predicate.

For every n>=3, axis(n) only overwrites entries0,n and, when n is even,
n/2. None of those indices is1. Thus the original x[1] is exactly the
initial seed and the new reported metadata is identical. For n=2 only,
the index n/2=1 is overwritten, explaining the failure and the correction.
The y-axis has degree n+1>=3, so its reported first seed was already
correct. In particular, for every existing degree17–40 the exact checker
output is unchanged, and the accepted old witnesses/replays remain usable.
The native mathematical arithmetic is unchanged at every degree2–40.

The new `check.py` is only an invocation/receipt wrapper. It imports the
unchanged strict driver, passes its actual certificate bytes through the
unchanged loader/check functions without alteration, and records the
effective variant kernel and baseline identities separately. This avoids
the baseline driver's main routine attributing the new binary to its
adjacent old kernel. The wrapper adds no mathematical acceptance rule.

Root authorized preparing this narrow correction after the actual failure.
Before **any** native execution of the variant, the independent auditor
must inspect the exact literal patch, hashes and all-input equivalence
argument. After source acceptance and root release, first run one fresh
degree2 pilot using a fresh compile/destination. Only if that accepts may
the fixed list3–16 run under the same source identity and recipe. Preserve
the original failure and new identities. Reviewer resource caps/exclusive
output paths are prospective in the audit; there is no cap, precision,
degree, certificate or predicate rescue. No large-degree native replay is
needed for a two-literal metadata reporting correction.

The common checker compile command is now:

```
g++ -O3 -std=c++17 topics/padua-argmax-bridge-20261105/code/small_degree_unification/metadata_kernel.cpp -lgmpxx -lgmp -o WORK/kernel
```

For each degree the same strict checker wrapper is:

```
python -E -S -B topics/padua-argmax-bridge-20261105/code/small_degree_unification/check.py CERTIFICATE --binary WORK/kernel --output WORK/nN-check.json
```

At this source-record creation, the new kernel has not been compiled and
no new native execution or acceptance is claimed.

Completion addendum: the distinct auditor accepted the source patch and
all frozen identities before execution, then freshly compiled the variant
and accepted the2 pilot and every fixed3–16 replay, all with actual exit0.
No source, witness or cap changed. The original failed attempt remains
preserved. The independent whole sequence used19.153825 child CPU seconds;
[checker-summary.json](checker-summary.json) records the actual results and
identities, and the linked canonical audit records the execution.
