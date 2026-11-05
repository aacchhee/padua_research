# Preregistered capped floating box pilot

Rules read at `2fb2f7502bb8d1b46c0fe1089588c46a06df258d`; code developer
gpt-6.1-sol medium. Before execution: n=17,32,64,128,256; cap **2000 visited
boxes or 60 process-CPU seconds per degree**, stopping at whichever comes first.
Use four closed quadrants partitioning [-pi,pi]^2, longest-side bisection,
breadth-first order, and discard only rectangles strictly outside the closed
phase diamond. Bound every intersecting rectangle on its entire rectangle.
This avoids relying on unverified phase symmetries. Boundary overlaps are benign.

The protocol is the dated final section of `attempts/H1.md`, supplied by the
structure-gates worker. Use eps=1e-10*(1+Lambda_c), a diagnostic budget with no
error-control claim. First test S_upper<Lambda_c-eps. Otherwise require both
corner and noncorner predicates. The corner test adds four reflected interval
terms before absolute value and uses the orbit normalization 1/(8N), or the
universal physical H3 radius 1e-11/n². No measured-energy radius enlargement is
used. Noncorner: radius<=.1 and n>=48 permits the supplied analytic 1/8192 defect;
otherwise use opposite-sign pair interval lower profiles over all possibly
admissible noncorner centers. Unknowns remain unknown.

Intervals use ordinary double arithmetic, not directed rounding. Removable
sin(kx)/sin(x) values use the supplied sinc chart. If a safe chart cannot be
formed, use [-k,k]. Every unresolved rectangle remains in the frontier at a
cap. No complete cover or A1/A2/A5 pass is inferred from a partial tree. This
tests one enclosure and refinement policy, not the original box-growth kill
criterion or an exact-arithmetic time projection.

## Enclosure and acceptance implementation

The C evaluator forms interval H values on the odd periodic torus. Away from
zeros it uses sin(kX)/sin(X), intersected with [-k,k]. Near a removable value
l*pi, it uses `(-1)^((k-1)l) k*sinc(kq)/sinc(q)`, q=X-l*pi. The denominator
chart is restricted to [-pi/2,pi/2]; otherwise the fallback is [-k,k]. For
sinc ranges inside [-pi,pi], monotonicity of sinc(|x|) gives endpoint bounds;
outside that range an interval quotient is used if zero is excluded, with
[-1,1] otherwise. Taylor evaluation supplies sinc(0) continuously. The
implementation adds a small pole-detection tolerance to select the stable
chart; this is not an outward arithmetic guarantee.
An empty or nonfinite clipped R interval falls back to [-k,k]. Every computed
H interval must be finite and ordered; invalid/nonfinite or negative predicate
values stop execution before any leaf can be accepted.

S_upper sums absolute upper bounds. Corner_upper adds the four orbit H
intervals first, then takes absolute upper bounds and divides by 8N. A
noncorner projected pair contributes zero unless its two interval signs are
strictly opposite; then it contributes twice the smaller minimum absolute
value. Summing and dividing by 4N gives each Q-profile diagnostic lower value.
The minimum of max(Qh,Qv) includes every odd noncorner center that could be
physically admissible anywhere on the rectangle. Including centers that might
not occur on its diamond intersection is conservative. Profiles are skipped
when the corner predicate already fails, since their value cannot accept that
box. Within the analytic radius the supplied constant may replace profiles.

The universal H3 check uses
`2 sin²(maxabs(alpha)/(2n))+2 sin²(maxabs(beta)/(2(n+1))) <= 1e-11/n²`,
avoiding subtraction cancellation in 1-cos. It never uses sampled derivative
energy or an enlarged hypothetical radius. A box meeting both the diamond and
its complement is bounded on its whole rectangle. The surviving frontier and
accepted leaves therefore describe a genuine attempted rectangle cover,
with the entire unprocessed frontier retained when a cap is reached.

## Validation before the cover run

The independent cosine-polynomial primitive and direct weighted-reflection
lambda path in `phase_probe.py` were used before the box loop at n=3,4,5,6,17.
There were 412 finite comparisons: primitive point intervals and width 1e-5
intervals near (0,0), (pi,pi), (pi,0), (0,pi), and a nonspecial point; plus
complete point-box S/corner/projected-defect checks on admissible centers at
zero and signed nonzero phases. The largest absolute containment/predicate
violation was 1.14e-13, within the diagnostic threshold
1e-10*(1+abs(reference)). This establishes only the tested finite checks. It
does not certify enclosure validity between the validation points or control
all floating errors. No separate-agent interval checker or corruption test is
claimed. The C warning/syntax check emitted no diagnostics.

## Completed capped attempt

Executed the preregistered campaign, then repeated it once after the root's
review requested explicit invalid/nonfinite guards and the empty-intersection
fallback. No parameters or caps changed. The following receipt and table are
the final guarded source run, including validation and all degrees:

```sh
OPENBLAS_NUM_THREADS=1 python topics/padua-argmax-effective-2-20261105/code/box_pilot.py
```

| n | Visited | Far accepted | Corner-orbit + defect accepted | Outside | Unresolved frontier | CPU (s) | Stop |
|---|---:|---:|---:|---:|---:|---:|---|
|17|2,000|363|155|44|880|0.7418|box cap|
|32|2,000|374|145|32|902|2.4390|box cap|
|64|2,000|421|162|32|774|9.1407|box cap|
|128|2,000|395|178|28|802|38.3841|box cap|
|256|802|195|26|28|308|60.0311|CPU cap|

**No degree completed its floating cover.** The remaining processed boxes
were split, generating the frontier shown. All accepted corner/defect leaves
used the direct orbit interval comparison; none used the universal H3 leaf
rule. The largest-side widths of pending boxes were .04909–.09817 at n17/32,
approximately .04909 at n64/128, and .09817–.19635 at n256. The minimum
visited largest-side width was .09817 at n17/32, .04909 at n64/128, and
.19635 at n256. Thus this breadth-first cap does not reach the tiny universal
corner neighborhood. It neither tests nor refutes the efficacy of a targeted
corner-first refinement or an independently justified larger corner radius.

Wall times were 0.7419, 2.4394, 9.1421, 38.3891 and 60.0367 seconds. A cap is
checked between box evaluations, so the CPU-limited degree overshoots 60 by
one final box evaluation. Profile bounds were computed for 227,197,234,222,81
boxes, respectively. Other boxes either passed the far predicate, failed the
corner predicate, or could use the analytic small-radius alternative.

The [7,048-byte receipt](evidence/box-pilot.json) pins source and mathematical-input
SHA-256 hashes, commands, versions, validation, caps, counts, widths and timing.
It also pins the per-box trace, complete unresolved frontier and finite
validation output under
`local-output/argmax-effective-2-20261105/phase-probe/`. Those raw outputs stay
outside Git and are reproducible; archival transfer to AC's Padua cold storage
is pending. Every recorded source, mathematical input and raw identity was
verified after execution.
The final run fired no invalid/nonfinite guard. All 8,802 complete trace rows
were separately parsed after execution to check finite nonnegative predicate
values and to reconcile their count with the receipt's visited boxes.

The measured outcome is an **incomplete cover within the declared caps** for
this natural-interval and breadth-first variant. Partial accepted leaves do
not provide complete-cover box counts. The handoff's log²-growth pass and
linear-growth kill criteria therefore remain unevaluated, as does its
ten-minute exact-arithmetic projection. Neither a complete floating cover,
an exact certificate, new finite proved degree, nor an A1/A2/A5 pass is claimed.
