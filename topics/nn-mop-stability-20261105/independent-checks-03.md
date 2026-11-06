# Supplementary independent checks 03 — published finite Hahn theorem

2026-11-05. Requested allocation: gpt-6-astra high; serving model identity
and effective effort are not independently exposed. Rules/source
`823cf6a4ef7c01b4ef3d2a6fec3e9f19d4b4f6f1`, original main/base
`b4d292eea5eed373002506d5e16a3761bd7ae10e`. The coordinator authorized this
separate review of the newly published finite theorem and compact-receipt
checker. Reports01/02 remain frozen. This supplements, and does not replace,
the mandatory Claude audit or coordinator publication decision. No developer
file was edited by this checker.

## Scope and finding

Read all 189 lines of `theory/conditioning-hahn-normality-finite.md` in two
bounded chunks, including every one of its 61 essential evidence rows and
all source identities. Read the entire new
`code/conditioning_verify_normality.py`. The generic converse statement and
proof were reviewed in report02; its only new Open-items paragraph links the
completed finite theorem and retains the mandatory-audit qualification.

No substantive mathematical gap found in this finite application. With
gamma=1, the displayed second Pochhammer factor equals M-k+1=N-k, matching
the frozen rational input generator. Positivity concerns the weights;
the nodes are distinct rational numbers on [-1,1]. The finite result uses
only interior differences through degree N-2 and the previously checked
noncircular induction, establishing normality through degree N. The count
per size is N(N-1)/2, totaling 43,676 for N=4,...,64. The open-neighborhood
derivative conclusion follows from finitely many nonzero determinants.
There is no all-N Hahn theorem or numerical stability bound here.

One wording defect was sent to the developer: the initial proof phrase
"weights and distinct nodes are strictly positive/rational" could incorrectly
assert positivity of the nodes. The developer changed it to distinguish
positive rational weights from distinct rational nodes. I checked the
corrected text and reran the entire checker. The table and arithmetic did
not change. This was a developer correction, not a silent reviewer edit.

## Executed verification

From `/workspace/scratch/nn-mop-stability-20261105`, both commands exited 0:

```sh
python3 topics/nn-mop-stability-20261105/code/conditioning_verify_normality.py > /tmp/nn-mop-independent-finite-receipt.json
python3 topics/nn-mop-stability-20261105/code/conditioning_verify_normality.py > /tmp/nn-mop-independent-finite-receipt-final.json
```

The first checks the initial theorem hash, the second the corrected final
theorem. Each recomputed all 61 exact cases and matched every count,
input hash and coefficient-payload hash, with 43,676 nonzero d values.
The checker verifies complete ordered coverage N=4,...,64 before the loop.
It imports the same frozen producer, so this is a separate execution and
receipt validation, not a new independent implementation of all61 cases.
Report01's direct-moment construction separately checked the scalar graph
at small sizes; report02 separately ran and compared all61 producer cases.

I additionally executed a Python check parsing the final Markdown table
using string splitting rather than the new checker's regex. It asserted
ordered N=4,...,64 coverage, each count N(N-1)/2, and equality of every input
and coefficient digest with my prior independently generated
`/tmp/nn-mop-independent-hahn-normality.json`. All 61 rows matched. That
prior receipt's SHA-256 is
`aa880df02ce17f664aad81412a78d2c8e7f743534774973ed3c5996b39cf8d69`.
Current on-disk producer, graph, baseline and checker hashes were separately
read and compared with the theorem's pins; all matched. Hash strings alone
are not used as a substitute for the exact recomputation.

Environment: Python3.12.14, Linux6.18.57-x86_64/glibc2.41; Fraction scalar
arithmetic. Imported graph environment remains mpmath1.3.0, NumPy2.3.5,
SciPy1.17.0 as in report02; none supplies floating arithmetic to these exact
certificates. No randomness, external paper reading or external package
experiment was added. Raw receipts remain regenerable local /tmp files.

## Frozen identities

| Source | SHA-256 |
|---|---|
| finite theorem, initial 15226 bytes | `eb0936a1f4b9acc32f7640a6a7ce9120d36eebbc249beeb34a18743c24e2cb77` |
| finite theorem, final 15246 bytes | `eadbb94053a564a4706dfe0e107cd8644f1fef540dd6b7055fbc58430c567352` |
| generic converse, administrative update | `6692f54ea21b77eb744775e21d3827b4e21b45ca13e0ad4c1659be1b52967eac` |
| conditioning_verify_normality.py | `f9403f537c67a64cadaedd376d430e960b21ab6b806be2092df824a8ba61e9db` |
| conditioning_exact_normality.py | `7aa4115143a51bd3abcea50abd4ea7b8de9a7507bea711ca7e19ab662a2be24a` |
| conditioning.py | `11c4b49be8541697e74d383b908db47b42480e11c60f92c35821340eacea929c` |
| predecessor c4_float_baseline.py | `9ce76ae88fb798f73127f75819bcdfb6c7bffb0d9cd092d70957164cb9b6a2e8` |

Both output receipts are 323 bytes and report PASS, sizes61,
exact_interior_checks43676, and their exact checker/producer/theorem hashes.

| /tmp/nn-mop-independent- output | SHA-256 |
|---|---|
| finite-receipt.json | `6f301d573551343d6fb10c79aaf7791745004eac1e987c8db358886815c08fd3` |
| finite-receipt-final.json | `8020ed792e2821359a17a1b08fb018b2e34aed16f6800588bee8783acfea6db0` |

The finite exact claim is supported in precisely the stated size/parameter
scope. This report does not independently clear novelty or historical
priority, and the mandatory Claude audit remains outstanding.
