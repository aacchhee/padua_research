# IDEA?padua-argmax-bridge-phase-checker-r5 — Bounded response to R4-1

Aliases: dependency-aware sine square; finite-refinement fallback;
explicit experimental-kernel selection.

Rules/input: `3888dd37c362a0689943f33e6b7e44c1dd1c3050`.
Date: 2026-11-06. Assigned developer: Codex Sol medium; serving metadata
not independently exposed. **Status: OPEN, preregistered bounded response.**

The published round4 source, controls, failed five-leaf gate and independent
R4-1 finding remain frozen at3888dd3. Original finite-cosine source remains
236116452dc7aae66e39cbf8800fe847cffe931ac0ce8a9682397313de7c43a6;
failed hybrid remains9a976e77d861c291468d6bfa4d2104c6c42ace953781ce1c5ff1a43073505d7d.
This is an implementation bug response within the same inherited
IDEA-344/454 gate, with no new certificate predicate, novelty or literature
claim. New-main summary differences and the complete relevant predecessor
records were already inspected for round4; no new mechanism is generated.
The source response is independently reviewable, not self-approval.

## Concrete finding and proposed response

At k1, turn-2, offsets[.125,.375], the round4 ratio API returned success0
with NaN derivative bounds even though R1'=0. A generic ball multiplication
of sin(Z) by itself can contain0 although sin(Z) excludes0. Dividing by
that overestimated ball can become indeterminate, and an unchecked Arb
intersection can carry indeterminacy into successful diagnostic outputs.
Round4's separately guarded phase-bounds API did not establish any false
certificate acceptance. See `../independent-checks-phase-round4.md`, R4-1.

Create a separate `hybrid_kernel_v2.cpp`. Use Arb's dependency-aware
`arb_sqr` for the sine denominator square, test finiteness and exclusion
of0 before division, and stage both quotient candidates before committing
any refinement. If a quotient candidate or its intersection is
indeterminate/nonfinite, retain the valid globally clipped finite-harmonic
baseline. Before every optional intersection, check finite inputs. A
nonempty finite intersection must produce a finite enclosure to be used.
An **empty intersection of finite purportedly valid enclosures is still an
error**, not permission to silently drop a contradiction. Success of every
diagnostic API requires finite output endpoints. Preserve all existing
strict comparison, midpoint/radius, profile, orbit and geometry semantics.

Keep the stable bare builder/CLI default on the original baseline kernel.
Select experimental round4/round5 sources explicitly from a fixed whitelist,
never from a candidate-supplied path. Record the selected variant and exact
source/build closure in each receipt. Existing immutable-input and fresh
unique-build provenance remains required.

## Unchanged target and ordered bounded gate

The exact original n17 compact candidate remains1288leaves/0pending,
plain SHA64f7befd86658c8d9f29b05c1cb5a0162e611b726b161e737610547bed218c4b.
No producer tree, local patch, leaf kind or strict threshold changes.
The original candidate's28local leaves already passed; no larger patch
is needed to decide these five fixed predicates.

1. Run the exact R4-1 reproducer and wide/narrow k1 cases about integer*pi,
   including crossings, plus the relevant prior ratio/primitive,
   intersection, input/build provenance and uneven-endpoint controls.
   Explicitly exercise nonfinite refinement fallback and finite disjoint
   intersection rejection. Return-code0 must never accompany nonfinite
   diagnostic endpoints. Any contrary result stops the response.
2. Rerun precisely the same five original strict leaf predicates:
   far0/01010; corner-orbit-plus-defect0/1100111,0/11011111,
   3/0011000,0/1111111111101111. All five must pass. A remaining failure
   stops this bounded variant, with exact inequalities recorded; no
   internal subdivision, changed tree, second formula or automatic next
   iteration is included.
3. Freeze source and bounded evidence for a distinct focused review.
   Only after all five pass **and** that review accepts the material
   change may one full original-tree replay run. Its unchanged pass
   condition is1288/1288leaves checked, zero failures/pending, acceptedtrue
   within120checker CPU seconds; compiler child CPU separately reported.
   No whole replay is authorized if the bounded gate fails. No new-degree
   or n128 whole-cover job is included.

This gate distinguishes a correct finite-output bug response from actual
repair of the original enclosure failures. Fixing R4-1 alone is insufficient
progress for complete phase-certificate acceptance. Any remaining broad
corner or defect failure must be retained. A failed response rejects only
this specified bounded variant, not every phase certifier or PD-T099.

## Actual results

No round5 code or arithmetic run preceded this preregistration. Results,
source hashes and the precise resulting disposition will be appended after
the bounded execution. Original round4 records and source paths are not
edited; no new PD-N/final ID is requested.

## Executed bounded response and focused review

After the3888dd3 publication and parent authorization, the separate
hybrid_kernel_v2.cpp fixed the R4-1 path with dependency-aware arb_sqr,
finite guards, staged optional refinements and a finite-output success
contract. Both frozen original kernels remain unchanged. The bare builder
and CLI now select the stable baseline; experimental kernels require
explicit fixed-whitelist selection and are identified in build manifests.

The75ratio controls,4triangular primitive/value-gradient controls,
explicit nonfinite-candidate fallback cases, finite contradiction rejection,
uneven-endpoint control and relevant input/build checks all pass. Exact
R4-1 input returns[1,1,0,0,1,1,0,0] with success and safe finite fallback.
All five original strict leaf predicates pass. The bounded evidence is
`../evidence/phase-checker-round5-bounded.json`, SHA-256
6eb2371ba9a80d688db329e6930374751afc7c407a7891b1a978dc545a608df1.

A distinct reviewer actually rebuilt and exercised the frozen v2 source.
Its focused review **ACCEPTED the response and CLOSED R4-1** before the
whole replay. See `../independent-checks-phase-round5.md` and
`../evidence/phase-round5-review.json` (receipt SHA-256
617ca089876b4854b44755baeb0a4ce3571b4201379c766b523da8bea19302cd).
That source review did not itself replay the complete candidate.

Frozen computational source identities:

- hybrid_kernel_v2.cpp:
  17fea91d4fa02e4183823e5d70b44705e96da7acfd26b04a0f3ed1cac443d9a2;
- build_snapshot.py:
  19a5a7c2296768853b94672b9b5dc4cf16c9ae87c37abbcde073ffaf89246bfb;
- check.py:
  88dde644a77a286e547679b0547c4d35814a4dda7373575208246882d9a26820.

## ONE actual whole original-tree replay — PASS

Only after focused review acceptance did the parent authorize and this
developer execute one whole original1288-leaf replay, with **no leaf cap,
no tree edit, no internal rescue and no repeat run**. The actual checker
argv was:

    python topics/padua-argmax-bridge-20261105/code/phase_checker/check.py local-output/argmax-bridge-20261105/N3/outward-full-n17-r3/n17-phase-compact.json --kernel round5 --output local-output/argmax-bridge-20261105/phase-checker/round5/full-n17/raw-replay.json

A pinned runpy launcher supplied those exact argv values and an OS checker
CPU limit of120seconds (hard limit121). The short receipt includes the
launcher's exact source bytes, digest, process argv and exit status so the
CPU instrumentation is reproducible. Candidate bytes were read once by the
checker and their digest matched the exact original
64f7befd86658c8d9f29b05c1cb5a0162e611b726b161e737610547bed218c4b.
The checker rebuilt its own library in a unique directory, recording source,
preprocessed translation unit, binary, compiler, headers and actual loaded
dependency closure. Reviewed sources also matched after execution.

**Actual result:** accepted=true, complete=true,1288/1288leaves checked,
zero failed leaves, zero pending regions, process exit0. Checker-process CPU
was109.449514seconds, below the120-second gate. Separately measured
compiler/build-helper child CPU was1.287483seconds; this quantity includes
all waited build helpers, not only the final compiler invocation. Wall time
was131.282938206seconds and is not the registered CPU budget.

The exact1288leaves comprise32outside,524far,704corner-orbit-plus-defect,
and28inherited-local leaves. Every original predicate passed. The old
failed whole-replay receipt at021ded297... was verified unchanged; the
round4 failure and R4-1 finding are not overwritten.

The new small receipt is `../evidence/phase-checker-full-n17-round5.json`.
The465506-byte raw result is local:
`local-output/argmax-bridge-20261105/phase-checker/round5/full-n17/raw-replay.json`,
SHA-256 dd09354bdbb2f6a7196f486c64a4c971ca56b1fa9e0b127a4b46ea4fcc5c6b08.
Its full build manifest is pinned by the small receipt. Bulk archival remains
with the coordinator's established Padua cold-storage workflow.

Disposition: **the registered round5 complete n17 overlap repair gate
PASSES**. This is a completed independent arithmetic replay of an inherited
finite degree. No new higher degree, universal growth law, n128 whole-cover
run or all-degree conclusion follows. Required Claude audit and any next
finite-degree jobs remain separately scoped; no additional run is started.
