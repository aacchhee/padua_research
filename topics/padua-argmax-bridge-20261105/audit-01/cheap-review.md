# Interim Claude audit — cheap-certifier claims (C03 replay, C12/C15 row boxes)

Auditor: Claude Opus 5.5, xhigh (independent subagent inside interim Claude audit).
Branch `codex/padua-argmax-bridge-20261105` at `02beaef2b22f8232286713dab0a1b7c95582ce13`
(rules AGENTS.md / agents/WORKFLOW.md read at this SHA). No repository file edited,
no state-changing git command (`git status` clean before/after). No producer, no
new degree, no rescue retry was launched. All builds/reruns under
`scratchpad/audit/cheap-run/`.

## Verdict

No BLOCKING or MAJOR finding in scope. The C03 mode0 PASS 364/364 on the
immutable n32 candidate is **independently reproduced** with a different
toolchain (g++ 13.3, FLINT 3.0.1, Python 3.13.18; original: g++ 14.2, FLINT
3.1.3, Python 3.12.14) and a driver of my own around the unchanged
`check_r8.check`. Acceptance predicates are the old strict ones, unweakened.
C12/C15 whole-box S uppers survived adversarial point fuzzing (0 violations).
Scope statements are honest. Five MINOR record/wording items and several NOTEs.

## Source identities (verified by sha256sum, execution)

| File | SHA256 (prefix) | Matches claim |
|---|---|---|
| cheap_C03/prototype.cpp | 9e357b25… | yes (also identical blob at e8fad16, an ancestor of HEAD) |
| cheap_C03/replay.py | 0e53a602… | yes (same at e8fad16) |
| cheap_C01/prototype.cpp | 178bbe5a… | yes |
| cheap_C02/replay.py | d3fc74db… | yes |
| phase_checker/check_r8.py / check_r6.py | 3c71ada8… / 437378a5… | equal to replay.py PINS |
| cheap_rows_C12_box/box.cpp | 91700bd4… | yes |
| cheap_rows_C15_global/global.cpp | 7f50e066… | yes |
| cheap_rows_C11/partial.cpp | bde1ce48… | yes (pinned by both builders) |
| evidence/c03-cheap-n32.json, c02-cheap-n32.json | e540444c…, 924e8ebb… | yes |
| candidate gz / plain | a01bc14b… / 97c33918… (21338 B) | yes |

## Executions performed (exact commands, CPU, exit codes)

Setup: `apt-get install -y libflint-dev` (FLINT 3.0.1; package install, not counted);
`pip install --target pylib mpmath` (1.4.1). Kernels built with
`g++ -std=c++17 -O3 -Wall -Wextra -fPIC -shared SRC -o LIB -lflint -lgmp` for
C03 prototype, C01 prototype, old `hybrid_kernel_v3.cpp`, and C15 `reference.cpp`
(includes global.cpp→box.cpp→partial.cpp, `-Ic15src`); ~7 CPU-s, all exit 0.

| # | Command (cwd cheap-run, PYTHONDONTWRITEBYTECODE=1) | CPU s | Exit | Result |
|---|---|---:|---:|---|
| E1 | `python3 driver.py lib_cheap_C03….so 0 out_…C03….json` | 33.7 | 0 | accepted, 364/364, 0 failed, 333 native calls |
| E2 | same with C01 prototype (=C02 kernel) | 25.9 | 0 | NOT accepted, 76 failed (48 far, 28 corner-orbit) |
| E3 | same with old hybrid_kernel_v3 | 131.4 | 0 | accepted, 364/364 |
| E4 | `ratio_fuzz.py lib_C03 {1,2,3} 1500` (variants 0,1,2) | ~36 | 0 | 191,904 mpmath(80 dps) samples, 0 violations |
| E5 | `box_fuzz.py lib_c15.so {1,2,3} 120` | 518.8 | 0 | 349 boxes, 3,839 512-bit reference points, 0 violations |
| E6 | `partial_fuzz4.py lib_c15.so` | ~1.3 (+~5 for flawed v1–v3) | 0 | 919 C11 `partial` point checks n≤4096, 0 violations |
| | **Total** | **≈760 (12.7 CPU-min)** | | within 30 CPU-min cap |

`driver.py` loads the kernel `.so`, sets `c03_variant(0)` when present, wraps
`phase_bounds` exactly like `check_r6.Kernel.bounds`, calls the unchanged
`check_r8.check(data, kernel)` with no leaf cap, and recomputes margins with
`Fraction`. E1–E3 ran concurrently on 3 of 4 cores.

E1 reproduces bit-for-bit every number I could compare: minimum strict margins
far 6793119230151/562949953421312 (2/0101011011), corner-orbit
1235104191095/140737488355328 (3/0000000111), max-exclusion
561502130767265/9007199254740992 (3/000000000); constants
[10.993594541100443, 10.993594541100444, π_lo, π_hi]; all 12 native counters
(9741780, 21585196, 17900, 0, 288, 0, 45, 999, 8439552, 655240, 0, 0). Comparison
counts reproduce exactly: C03 vs C01 S better 332/332, C better 304 / worse 28,
defect better 44 / worse 48 / equal 240; C03 vs v3 S worse 324, C worse 332,
defect worse 226; C01 vs v3 worse 332/332/270; constants identical across all
three kernels. E2 reproduces the C02 first failure 0/0101 with margin exactly
−133476523302491/281474976710656. Two different FLINT/compiler/Python stacks
giving identical outward bounds is strong evidence that the PASS does not depend
on the original build closure.

Could not test: the original 254-entry closure, raw `checker-report.json`,
`native-calls.jsonl` and `/tmp/c03-full-postcheck.json` (absent here:
`local-output/` does not exist; archive transfer pending). The author
`replay.py`/`controls.py` could not be run unchanged (they write into
repo-local `local-output/` and refuse because the receipt exists, and need the
pinned extracted FLINT 3.1.3 runtime).

## Item 1 — C03 mode0 replay

**Predicates (inspection, confirmed by E1–E3).** `check_r8.check`
(check_r8.py:76–127) is the same function the old accepted run used via
`check_r9.py` (check_r9.py:41–47 `acceptance.check(data,kernel,args.max_leaves)`).
Predicates are strict exact-Fraction comparisons: far `su<lc`; corner-orbit
`cu<lc and su-dl<lc`; max-exclusion `bootstrap_range(n,b) and su-dl<lc`;
outside `minabs+minabs>pu` (check_r8.py:102–111). Lc/π come from the kernel's
own (0,0) call and are cross-checked against candidate constants (lines 87–90);
Lc is bit-identical to v3. No weakened predicate, no leaf cap
(replay.py worker calls `acceptance.check(data, kernel)`), no monkeypatch.

**Lazy collector (inspection).** prototype.cpp:192 sets `C_upper=S_upper`,
defect 0 when `S_upper<Lc_lower`. Valid: the orbit sum
(1/8N)Σ|h(r,s)+h(−r,s)+h(r,−s)+h(−r,−s)| ≤ S by the triangle inequality because
each reflection permutes the odd-parity board indices (2n, 2m even). E1: 288
lazy leaves = 280 far + 8 corner-orbit.

**Ratio chart (inspection + E4).** C03 = C01 + `endpoint_chart`
(prototype.cpp:107–125); mode0 returns before the centered/ODE step (line 130),
and replay.py rejects any call with nonzero centered/ODE counters. I re-derived
theory C03 §1 (F′=F·[f(kr)−f(r)]/r with f=t·cot t; the kr=π case; π<kr≤4 via
cot y>1/√3, y≤4−π<π/3) and §2 folded-endpoint image; parity ε=−1 iff ell odd,
k even. Code guards match: residual from `lround(mid/π)` only proposes ell;
admission checks the ball and then the **extracted** dyadic endpoints
(`upper(u)≤1.5`, `upper(u·k)≤4`, line 115) with outward
`arb_get_abs_lbound/ubound_arf`; endpoint values come from non-recursive
`ratio_base`; derivative sign halves are oriented correctly for ε<0 and for
nonpositive residuals. Empty finite intersections throw (→ status 3 → checker
`Invalid`), never accepted. E4 found no enclosure violation for k∈[2,513],
turns −4..4, intervals across poles, at kr≈π, kr≈4, r≈1.5, and wide intervals.

**Identity closure (inspection only).** Wrapper pins 15 code/data inputs plus
itself against the published commit via `git cat-file`, snapshots the builder
with exactly two checked substitutions, checks the built source SHA, and
rechecks toolchain/header/dependency/linked/loaded groups before and after.
Gap: see MINOR-3 (Python stdlib not covered).

**3.08x comparison.** Old `total_subprocess_cpu_seconds` 139.405 (worker incl.
1.17 s build) vs new subprocess 45.229 (incl. 1.50 s build): same accounting
scope, ratio 3.082. Like-for-like on measure and predicate set. Single run each;
host identity/hardware is not recorded, so same-machine is not demonstrated
(NOTE-1). My same-host, concurrent measurement of checker-only CPU gives
131.37/33.64 = 3.91x, so 3.08x is not overstated for this candidate. Part of the
gain is from dropping v3's second (baseline) collect pass and its O(n) harmonic
ratios, which is a legitimate change.

## Item 2 — Row/point and whole-box components

**Domain guards (inspection + E5).** box.cpp `box12` and global.cpp `domain15`:
LP64 (`sizeof(long)<8` rejects), 2≤n≤4096, exact rationals with al,bl≥0,
al≤ah, bl≤bh, ah+bh≤1, so the rectangle lies wholly in the closed triangle;
straddling rectangles are rejected rather than clipped. Exact vertices (1,0),
(0,1) return S=1. Parsing rejects zero denominators.

**Collision removal before vertices (inspection).** Per ordinary row, both
denominator bands (d1,d2) must have literal width<1 (`narrow12`), are buffered
by ±1, plus seams 0,n−1; |D|≤8 and D is evaluated with the actual finite
primitive. Since the band [l,u] contains the real collision index, the buffer
puts floor/ceil of every collision in D, so every k∉D has real-index distance
>1 from both cot poles, which is what C14 (2) and the freeze bound require.
Cuts at k,k+1 for every direct k, and empty numerator bands still cut at ceil(l).

**Arbitrary-coefficient poles and signs (inspection).** For artificial (c,p)
the core decomposition F=C·cot((u−v)/2)+D·cot((u+v)/2), C=(p−c/sin v)/4,
D=(p+c/sin v)/4, follows from cos u−cos v=−2 sin x sin y (I re-derived it);
sin v≠0 checked. Wraps are accepted only after the whole y-ball satisfies y>0
and n−y−(q−1)>0; `partial` re-checks the same guard. The core sign is certified
at one point, valid because roots/collisions are cut over [a,b]×box; an
unresolved sign throws and the row falls back.

**Convexity and coherent max (inspection).** C12: per row, max over ≤4 (c,p)
vertices is valid by convexity at a common phase. C15: max over ≤8 shared (A,p,q)
vertices taken only after accumulating all rows (`largest=max_j(acc[j]/N+E_j)`,
global.cpp), valid because c_r is linear in (A,q) for fixed v_r. Freeze error
E=(2/π)·max_r ε·H² with H=1+log n≥H_n, ε=(A0+q0)·π(bh−bl)/(2m)+ρ with
A0,q0≥0 (A≥0 on the triangle), matching C14 (12).

**Forced rollback (inspection + E5 probes).** C15 stages all vertex values per
row; `common+=actualBuffered` and the `acc[j]` commits run only after every vertex
succeeds, and the commit loop cannot throw (all operands already passed
`up12`). On any exception the row adds the full n·N cap and nothing else.
E5: 89 `c15_fault_probe` calls; every probe at n≥7 charged ≥1 fallback and
returned upper ≥ n (=rowcap/N) and ≥ the unforced upper. 15 probes at n≤5 did
not trigger because D covers the whole row, so the vertex loop is never reached
(a test artifact, not a defect).

**Precision/radii (inspection + E5/E6).** Rationals→Arb via `arb_set_fmpq` at
160 bits; doubles→Arb exact; outputs rounded with directed ARF→double.
`partial` adds the J16 remainder `7q h⁴ mj/5760`, Bernoulli tail, w′ tail and an
input-radius moment charge; E6 found no containment failure for n≤4096, q≤n,
y near both pole guards. C12 `ratio12` uses library `arb_sinc`; this affects
only the fixed-work cost accounting (C01 §6 caveat), not validity.

**E5 adversarial results.** 349 rational boxes, n∈{2..32}, widths 0 to 1/64,
boxes on axes, on the hypotenuse and zero-width: C12 and C15 uppers ≥ reference
S at every one of 3,839 points (512-bit original cosine sum); no native
failures, no natural row fallbacks. Tightness: median excess over the sampled
max ≈0.005–0.008, maximum 2.66 on wide boxes; C15≤C12 on only 44% of boxes
(consistent with the disclosed "mixed" quality).

Not tested: n>32 whole boxes (reference limited to n≤32), the C12 relaxation and
C15 cube diagnostics as bounds, C02-row-cotangent/C09/C08 analytic constants
(read headers/statements only; not re-proved here), and the C10 controller
(not run, by scope).

## Item 3 — Scope honesty (inspection)

- No all-degree cost law: C03 record ("not a new-degree claim or evidence that
  every candidate or degree will meet this budget"), C02 record, gates.md:20
  ("no higher-degree box-count scaling theorem") and LOG.md:402 are scoped
  properly.
- Ω(n²w): C08-row-box-obstruction.md is scoped to "EVERY integer index swept by
  a moving numerator root" on β=0, α∈[3π/4,3π/4+w], n≥128; I re-checked
  1/8<g<3/4, |t_α|≥n/(8π)+1/(2π), 0<t<n/6 and the m/3−1 row count. It
  explicitly does not exclude relaxation (C09/C12 avoid it: fixed artificial
  (c,p) give root bands of width ≈w_α/(2π)).
- C10 producer controller: LOG.md:378 "prepared/not reviewed/unreleased";
  no execution evidence exists.
- Whole-box API: c12_box/c15_global return an S upper only; C09:12 and C14 state
  no corner-orbit/defect/derivative. Both review records repeat this.

## Findings

**MINOR-1** `independent-checks-C03-cheap-n32.md:144` — the exact-margin
postcheck behind the margin table and the "bit-identical constants" claim lives at
`/tmp/c03-full-postcheck.json`, and its script is not committed (no `postcheck`
under `code/`). Neither is durable or reproducible from the repo. Evidence:
grep. Mitigated by E1, which reproduces every number in the table. Fix: commit
the postcheck script or cite this independent rerun.

**MINOR-2** `independent-checks-C03-cheap-n32.md:1–12` — the execution record
does not name the executing agent, model or effort, which WORKFLOW requires
(serving metadata may stay unexposed, but the requested model should be named).

**MINOR-3** Wording `source_runtime_checks_complete` / "All 254 closure
entries" (C03 record :124–135; replay.py `project_modules`, `python_runtime`).
The closure hashes the Python executable and project modules only, not the
stdlib `fractions.py` that carries the exact strict acceptance arithmetic, nor
the json/gzip/ctypes extension modules. `loaded_closure` checks only the
kernel's linked libraries (build_snapshot_r9.py:82–94). Scope the
completeness claim. Mitigated by E1: a different Python (3.13.18) gives the same
outcome.

**MINOR-4** `gates.md:20` places "46.09 total CPU" next to "3.08x lower
subprocess cost". The ratio is correctly subprocess/subprocess, but readers
can compute 139.4/46.09=3.02. Name the measure on both numbers (as in the C03
record :89).

**MINOR-5** box.cpp `c12_box` / global.cpp `c15_global` return diagnostics
(relax, freeze, cube, tail, rho) in the same `out[]` as the S upper. Nothing in
the source says that out[1..] are non-additive diagnostics, and in C15 the
freeze term is already inside out[0]. A future integrator could double-count or
mistake them for bounds. Add a source comment or API note before integration.

**NOTE-1** The 3.08x is a single-run ratio, and the host identity of the two
runs is not recorded. My same-host checker-only ratio is 3.91x (concurrent load).
**NOTE-2** Mode0 uses only the endpoint chart. Variants 1 and 2 (centered Taylor,
ODE cap) passed my E4 enclosure fuzz but are not released and not full-replayed.
**NOTE-3** C12/C15 cover only the first-quadrant triangle. Use with the signed
C03 roots needs the separately proved symmetry reduction, and no integration
exists. **NOTE-4** C03 retains the O(n²) board per box and O(n³) profile loops
on 45 non-lazy leaves (C01 §6 says so). The "fixed-work" claim is
per-ratio-evaluation only. **NOTE-5** Raw artifacts and the 254-identity closure
are unverifiable until cold-storage transfer; the receipt pins them by hash.

## Genuine bottleneck (for idea generation)

The cheap kernel is sound but **loose exactly where margins are small**. Its
36 tightest far leaves (C03 margin <0.05) sit in the near-corner shell
|α|+|β|≈0.5–0.7 at width≈0.098. There the C03 margin is only 15–30% of v3's
(for example 0.0121 vs 0.0811), and the median far-margin ratio C03/v3 is 0.65.
The fixed n32 tree passes only because v3-level subdivision already exists.
At a new degree the cost will be dominated by how many producer leaves the
mean-value S enclosure needs in that shell, and by the corner-orbit/defect leaves
(the O(n³) profile). The O(1)-ratio saving does not touch either, and no
producer cost has been measured. The O(n) row/box S uppers do not help there yet.
They are S-only (no corner-orbit or defect), have median excess ~0.5% of S at
small n even on narrow boxes, and their selected n32 far uppers (11.40, 11.37)
exceed Lc=10.99.
