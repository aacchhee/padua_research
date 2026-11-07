# Post-audit D01 — P4 fully charged corner-envelope test

Rules/input `4cf68980fa0538b53e2aea7174ed6e5782a34908`;
2026-11-06, Codex mathematics worker, parent-assigned Sol xhigh;
serving metadata unexposed. Code/evidence belongs to the separate
D01 technical worker. Root alone controls Git and shared records.

## Frozen target and mathematical meaning

This implements already gated Claude P4/I04 as a quantitative C07/C13
variant. See [the idea](../ideas/D01-corner.md) for exact novelty-gate
coverage and the [pre-execution SPEC](../code/post_audit_D01_corner/SPEC.md)
for definitions. The measured object is

    K0_C07=C_f+C_rem+C_sine+C_strip-log(n+1)/3,

with the unchanged C07 reciprocal A1/A2/A3 sums on exactly R, the
complete harmless-term bound C07(13), its normalized sine reciprocal
envelope, and every enlarged-strip index including the weighted(n,m)
endpoint. The theory record derives all four normalization/charge terms.
This quantity is not a measured cardinal Hessian or the optimal
actual-function bracket constant.

The preregistered tests were primary<=4 at1000; weaker alternative<=7.8
at10000; kill>=0.1L^2-L/3 at20000, L=log(n+1). All four prescribed
degrees and their odd companions were fixed before execution. No degree
certificates, phase/lambda samples, new model or correction were used.

## MEASURED finite-sum results

Every interval below is a **MEASURED truncation envelope**: its omitted
positive tails have explicit analytic upper bounds, while floating
arithmetic has no directed-rounding error enclosure.

| n | A1 lower | A2 lower | A3 lower | K0_C07 lower | K0_C07 upper |
|---:|---:|---:|---:|---:|---:|
|1000|18.8025197935|4.3419253013|4.9501942195|9.0601209827|9.0628362189|
|1001|18.8177955917|4.3419278929|4.9502040367|9.0620206684|9.0647370649|
|10000|22.9549572577|4.3442625853|4.9550053964|8.9562144828|8.9603560177|
|10001|22.9564860053|4.3442626113|4.9550054949|8.9564054372|8.9605469970|
|20000|24.1965454230|4.3443926774|4.9552729432|8.9279566899|8.9322314755|
|20001|24.1973098142|4.3443926839|4.9552729679|8.9280521978|8.9323269907|
|100000|27.0760872248|4.3444967725|4.9554870039|8.8634874786|8.8678937599|
|100001|27.0762401046|4.3444967728|4.9554870049|8.8635065854|8.8679128671|

The small [receipt](../evidence/d01-corner.json) contains every sum's
explicit tail upper bound, B20/C20, G2 and all four budget charges.
For example, at1000 C_f is6.87495924–6.87497634, C_rem is0.00318051,
C_sine is1.68629809–1.68899623, and C_strip is2.79860140.
Subtracting log1001/3 yields the reported K interval. This exhibits why
the result cannot be called a bare sum constant or Hessian estimate.

**Decisions:** primary FAIL; weaker alternative FAIL; kill FIRES,
since the n=20000 threshold is6.5068264192, below its lower endpoint.
All three decisions concern the fixed envelope. They neither refute an
optimal actual-corner inequality nor close any argmax/degree interval.
No failed primary was relabeled as success and no rescue run followed.

## Finite reduction, controls and cost

The mathematical worker derived and supplied exact odd-diagonal ranges
before launch. The code enumerates only |j-r|<=127, then intersects
two valid positive-tail upper bounds: denominator minima on each omitted
finite diagonal, and spacing-two integral bounds. Full B20/C20 grouping
uses exact integer counts by odd S in O(n). At100000 the loop visits
12,741,999 terms and covers4,987,358,001 further terms by positive tails.
Naive full O(n^2) evaluation was not attempted.

The code worker actually ran one controller invocation, compiling once,
with the command and provenance in its
[run record](../code/post_audit_D01_corner/run-record.md). Full direct
j,r loops at1000/1001 lay within the independently enumerated diagonal
tail brackets. Full n17 and independent Fraction n17 agreed in all six
reported sums/counts after the recorded conversion to double. These
are measured regression controls, not independently validated rounding
or actual-function proofs. Both parities have their own reported data;
the physical other-corner reflection keeps the same mesh convention.

Measured controller CPU2.511748s; complete shell tree2.524s; postrun
source/header provenance0.120s; total shell-observed2.644s<300s.
The initial missing-/usr/bin/time wrapper and its source-preserving
substitution are disclosed once in the technical run record; no numeric
first failure, retuning or rescued mathematical input occurred.

Source/spec SHA256:

* measure.cpp: ab5b8154dac29336caf50ab822bbcc8b27659a4ef32102920125d669679c8891
* run.py: 6b25fc4735f0c5f9299e6e6b13da3140ca323213baf4706d3c715296e9e3b454
* SPEC.md: 5db165cee96f1011fcac0a92286632177f44d7502e9d41a6d3d08539e48c5000

The receipt pins the61,263-byte local manifest and the preregistration;
large raw/provenance files stay off Git pending authorized cold storage.
The developer controls are not the later independent consequential
rerun. No independent audit acceptance is claimed.

## Separate exact primary obstruction

After observing the diagnostic, a two-index elementary argument proved
the frozen envelope's primary failure without numerical premises:

    K0_C07(1000)>1289/300>4.

The complete [PD-N?argmax-bridge-codex-D01-corner proof](../theory/D01-corner-budget.md)
uses (0,1),(1,0), pi^2<10 and the positive exp7 series through degree11.
A standard-library Fraction scalar check actually returned
sum_(k=0)^11 7^k/k!=2959911103/2851200>1001; this supplementary arithmetic
check is not a finite premise of the written analytic proof. This is a
new scoped negative statement about the frozen allocation only. The
measured n=20000 kill remains MEASURED.

## Stop boundary and remaining obligations

This bounded D01 implementation is complete and stopped. No new
fixed-K lemma, actual-function bracket at1000, corner onset, smaller-n
reuse of C07/C13, or old-degree certification is claimed. The enlarged
strip endpoint weights and normalization were derived, not sampled.

If a later separately authorized candidate changes the majorant, it
must prove its new uniform derivative/sine/collision estimates, retain
the exact four-copy normalization and all zero-cardinal/endpoint terms,
and recheck every degree-sensitive bound. In particular a proof must
not reuse the old1-120/n small-j estimate at1000, round the positive
corner deformation d(n), or assume the old million/half-million domains
extend automatically. None of these new obligations is discharged by
the present measurements. More precision on the same envelope cannot
remove its exact primary obstruction.
