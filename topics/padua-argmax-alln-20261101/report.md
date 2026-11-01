# Part 3 report — all-degree Padua argmax

2026-11-01 · Codex gpt-6.1-sol xhigh · rules/input `328be35e55143013047ec03a70e9906e82b95353`.
[Draft PR17](https://github.com/aacchhee/padua_research/pull/17). Required Claude audit **PENDING**.
The all-degree PD-T099 target remains **OPEN**.

## Results

The certified finite range is now **every n=2,…,16**. Each new degree has exact or outward-rounded arithmetic, a written finite reduction, small committed evidence and a different agent's successful replay. The vertical-edge envelope has a positive gap on every compact interval away from the endpoints. The horizontal defect has a proved compact positive limit, while the horizontal primitive bounds remain unresolved. Scientific IDs remain provisional.

## Pre-registered tests

| Test | Verdict | Scope and limits |
|---|---|---|
| T1 edges | Intended noncorner version retained through sampled n400 | All four edges. Literal all-cell criterion includes zero corner gap and trivially fails. Positive integral evaluated; requested general-β series not derived. Smallest sampled noncorner gap for n≥100: .550440482023 at n399. |
| T2 interior profile | KILL under recorded cell convention | 32/81 positions change>.05 from64 to128; maximum .382304500506. This does not refute a strict interior upper bound. |
| T3 corner profile | Measured KILL of degree-independent raw angular profile | n16/64/256; no second sampled nearzero point. No divergence theorem. |
| T4 effectivity | Literal existing-proof projection killed; improved architecture inconclusive | Inferred constants project≈1.33×10^14 for a localization step. Central-only fits are much smaller. Neither is an all-square threshold. |
| T5 n2 | PASS | Exact rational proof and independent replay. |

Original criteria and separate dated interpretations: [tests](attempts/T1-T5.md), [MEASURED record01](theory/argmax-alln-codex-01-measured-tests.md).
Independent numerical execution covers fullT2–T4 and T1 at n12 on all four edges; full-rangeT1 has developer execution plus source review.

## P0–P6

| Obligation | Status | Durable record / remaining gap |
|---|---|---|
| P0 n2 | PROVED | [02](theory/argmax-alln-codex-02-degree-two-global-argmax.md): maximum3 only at(±1,−1). |
| P1 compact vertical edges | PROVED in the allowed positive-gap form | [04](theory/argmax-alln-codex-04-vertical-compact-defect.md): max=Λc−min_I g_v+o(1), min_I g_v≥δ²[1−cos(δ/2)]/(16π²)>0. |
| P2 horizontal envelope | OPEN | [05](theory/argmax-alln-codex-05-horizontal-compact-defect.md) proves supporting decomposition/defect; global phase localization and local primitive gain still needed. |
| P3 corners | OPEN | Uniform local comparison and transitions; raw angular profile form fails its planning test. |
| P4 interior | OPEN | Two-phase majorant and four-copy defect estimates; raw gap-profile stability test fails. |
| P5 strips | OPEN | Uniform bridge across moving distances to edges; fixed-strip measurements are insufficient. |
| P6 effective threshold | OPEN | Finite2–16 closed; rigorous n0 and17≤n<n0 remain. |

P3–P5 and the fallback are detailed in [their attempt](attempts/P3-P5-and-pairing.md). Proved supporting lemmas do not make the unresolved targets PARTIAL. Center-minimality of g_v remains OPEN; the vertical theorem uses a positive compact minimum instead.

## Finite certificate evidence

[Correctness theorem03](theory/argmax-alln-codex-03-finite-certificate-correctness.md) uses positive tensor Bernstein weights. Bound leaves put all coefficient absolute sums below the corner lower bound. Corner leaves allow equality only at their exact corner vertex; every other coefficient sum is strictly smaller. The checker verifies the full closed-box binary prefix cover.

| Degrees | Construction | Complete leaves / observed cost |
|---|---|---|
| n2 | Explicit rational cardinals; four quadrant bounds | Standard-library Fraction proof/checker |
| n8 | Accepted exact principal algebraic field |34leaves,depth6; discovery48.33s, independent replay45.72s |
| n9–16 | PD-T101 corrected cardinal formula; rational Machin/Taylor cosine enclosures;192-bit outward integers |42,48,50,54,56,58,82,96leaves; depth≤8; independent replays all accepted |

[Degree8 theorem07](theory/argmax-alln-codex-07-degree-eight-global-argmax.md),
[degree9–16 theorem08](theory/argmax-alln-codex-08-degree-nine-through-sixteen-global-argmax.md),
[finite attempt and exact commands](attempts/P0-finite.md),
[independent checks](independent-checks-part3.md).

n12 discovery took5.18s, below IDEA-05's10×n7 baseline threshold (~35234s), so this finite tool is retained in the tested scope. Runtime is a measurement, with no bound for larger degrees. Corrupted-certificate controls reject missing/duplicated leaves, wrong corners, forged bounds/thresholds, altered sources and other malformed inputs. The producer/checker share arithmetic; independent execution and code/proof review are separate from an independently implemented arithmetic kernel.

Together with inherited accepted n3–7, these results give2≤n≤16. PD-T181's n8 OPEN row is superseded only by a proposed local split until audited PR preparation updates the shared registry.

## Fallback and limits

[Measured record06](theory/argmax-alln-codex-06-measured-pairing.md) retains finite geometric screens. [Scoped obstructionN01](theory/argmax-alln-codex-N01-pairing-order-obstruction.md) proves a precisely specified tie-inclusive order fails on the accepted n4 list; [independent check](independent-checks-pairing.md). The ambiguous IDEA-03 suggestion and every possible pairing method are not refuted. [Candidate history](ideas-codex-fallback.md) preserves each formulation and its test.

No counterexample to PD-T099 was found. No planning-test failure is promoted to a general nonconvergence theorem. No unread one-dimensional literature result is transferred into a P3 proof; that reading remains necessary before such a transfer.

## Evidence and next review

[Pinned input paths/blobs](input-snapshot.json), [Claude replay](independent-checks-claude-records.md), [manifest](evidence-manifest.json).
[Codex audit of the original Claude observations](independent-checks-claude-observations-audit.md) accepts the replay-covered MEASURED claims with C-01 corrected: the strip runs cover separate one-cell-thick offset bands, not cumulative wider adjacent strips. Targeted optimizer-location checks confirm all six central-box runs ended inside the box. Standalone maj.py whole-square scans remain outside independent execution.
All essential new finite evidence is small and committed; no Windows/cold-storage access is required for these claims. Trusted dependencies include Python integers/Fraction, SymPy for n8's algebraic field and the explicitly cited accepted PD-T101/179.

Scope stays inside this topic and its own results file. [Shared-row/ledger proposals](proposed-record-changes.md) wait for audited PR preparation. No final IDs assigned.
The GitHub connector uses Andrey Chesnokov's account noreply email and exposes no author-email override; the requested gmail email could not be selected. Published history is preserved.

Next is Claude Opus5.5 xhigh audit, followed by dispositions and PR preparation. Supplementary Astra checks do not replace the required Claude audit.
