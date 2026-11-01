# P0 and finite global-maximum certification

Rules/source pin: `328be35e55143013047ec03a70e9906e82b95353`.
Developer: Codex, gpt-6.1-sol xhigh for mathematics. P0 is prespecified test T5.

## P0 exact result

**PROVED:** degree two has global maximum 3 only at (−1,−1),(1,−1).
Full proof: [degree-two record](../theory/argmax-alln-codex-02-degree-two-global-argmax.md).
Exact standalone checker: [finite_n2_exact.py](../code/part3/finite_n2_exact.py).
Actual output: [finite_n2_exact.json](../outputs/part3/finite_n2_exact.json).
It reconstructs rational cardinals from the node Vandermonde and verifies
the four-quadrant tensor Bernstein majorants and equality locations.
All essential exact coefficients appear in the small JSON evidence.
The orchestrator reports that the different-agent rerun and independent
proof/code inspection passed; its JSON is byte-identical. Claude topic
audit remains pending.

## Gate and candidate continuity

This is the prescribed IDEA?argmax-alln-claude-05 implementation, a weaker
target than IDEA-290…302: only exclude values above the corner and prove
strictness, with no count of stationary points. Closest full records read:
the topic's plan/ideas/gate, IDEA-206 registry entry, the full IDEA-290…305
preparation entries, and the part-2 degree-eight attempt. Registry headings,
aliases, summaries, applicable obstruction/disposition tables and mechanism
terms were screened; output truncations were not treated as full reads.
No priority claim or separate new mechanism is proposed.

Relevant inherited obstructions are all-stratum coverage, exact sign
decisions, corner-neighbourhood strictness and the difference between an
interrupted cap and a complete certificate. Floating agreement is not a
proof. P0 avoids sign enumeration entirely through positive Bernstein
weights; this is an implementation of the prescribed global upper-bound
strategy, not a claim to a new mathematical mechanism.

## Attempts retained

1. A single degree-(2,2) Bernstein expansion on the whole square was
insufficient: 12 of the 64 signed polynomials 3−ΣσᵢLᵢ had a negative
coefficient (small exploratory SymPy calculation). This does not refute
the target or Bernstein certification; it only fails that coarse box.
2. Splitting at x=y=0 makes every absolute-coefficient sum at most 3;
the only coefficient equal to 3 in a lower quadrant is its non-node
corner. This gives the successful exact analytic proof and checker.

## Larger-degree execution protocol

Prepare the interval/upper-bound machinery while T1–T5 are in progress.
Do not launch the n=8 mathematical search until the orchestrator confirms
that all five tests are done. First costly pilots are capped at about
120 seconds each. Every cap must preserve actual visited/discarded/
unresolved box counts and elapsed time. If n=8 succeeds, extend while
cost allows; no n=12 timing extrapolation counts as a completed run.

The original IDEA-05 kill criterion stays unchanged: kill as the P6 tool
if full n=12 certification costs more than ten times part 2's n=7 full
certificate. Discovery/replay times are now measured below; completion
of the independent n=12 receipt is required before calling the new
package certified. A pilot failure does not itself reject the method.

## Actual finite executions and practical feasibility

After explicit orchestrator authorization following the T1–T5 first-pass
outcomes, the n=8 field-based pilot completed in48.334941s: 67 visited,
34 leaves (32 bound, two corner), maximum depth6, zero pending. Developer
replay accepted every predicate and the full partition in41.207146s.
The full certificate is1397bytes. The field/producer/checker trio remains
frozen. Result record: [degree eight](../theory/argmax-alln-codex-07-degree-eight-global-argmax.md).

A separate general constructor uses the already proved PD-T101 exact
cardinal formula with rational Machin/Taylor trigonometric enclosures,
then the same interval Bernstein bounds. Its proof is in correctness
record03; it does not modify or invalidate the original n=8 sources.
The n=12 pilot completed in5.176281s, with107visited/54leaves, maximum
depth8, zero pending. Its developer full replay accepted in6.050755s.
All degrees9,…,16 then produced complete covers (42–96leaves), with
total discovery times1.32–32.35s under concurrent load. Discovery stopped
at16 by orchestrator instruction, reserving time for complete replays
and documentation. No n≥17 run was launched. See the [finite-range
record](../theory/argmax-alln-codex-08-degree-nine-through-sixteen-global-argmax.md)
for per-degree times, exact commands, complete artifacts and hashes.

Part2's actual n=7 producer timing, recorded in its T-A5-n7 attempt,
is2852.822651s interior plus670.587425s boundary, totaling3523.410076s;
ten times this already exceeds35234s. The new complete n=12 discovery
plus developer replay costs11.227036s; the different-agent full n=12
replay subsequently accepted in6.278170s. IDEA-05's specified timing
kill is therefore **NOT TRIGGERED** on these
observed executions. This is a practical finite test under different
implementations and concurrent-load conditions, not a complexity theorem
or an isolated hardware benchmark. It does not revive the killed
asymptotic-profile or effectivity claims.

Developer general-checker controls on the actual complete n=8 general
certificate rejected14deliberate corruptions, accepted a complete
positive, and verified a genuinely partial positive without accepting
it as a global theorem. No pending box was silently discarded in any
successful run, and no unsuccessful larger-degree cap occurred. The
different agent independently accepted all complete n=8,…,16 certificates
and reran all14general controls. The finite range is now **PROVED for
2≤n≤16**, combining the new results with merged n=3,…,7. Required
Claude topic audit is pending.

## Runs needed

- Claude topic audit of P0, the soundness theorem and finite certificates.
- All-degree PD-T099/P3–P6 remain open beyond the finite range; do not
  infer a general comparison or effective threshold from this finite work.
