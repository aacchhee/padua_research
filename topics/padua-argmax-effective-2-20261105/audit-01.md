# Claude audit-01 — effective Padua argmax, phase 2 (handoff 02)

## Decision

**The mathematics is ACCEPTED at every stated scope, with no status change.
Two MAJOR record findings (F1, F2: missing closest predecessors and an
unqualified "strengthens" claim) and ten MINOR findings must be answered
before PR preparation. Stage moves to WORK for a Codex response
(handoff 03).**

- **PROVED, accepted as stated:** T03 (boundary cotangent profile,
  error <= 7/(12N^2), midpoint S_n=L_N), N01 (leading-factor-only profile
  rejected, scoped), T04 (full noncorner defect >= 1/8192 for n>=48,
  rho<=1/10), T05 (W_n <= 10^10 n^4 Lambda_c), T06
  (Lambda_n <= 110[1+log(n+1)]^2 <= 27500 Lambda_c) and T07 (strict
  descent with loss n^2 Lambda_c H/16 for 0<H<=10^-11/n^2, both nonnode
  corners, every n>=2).
- **T01 (phase structure):** every identity and the finite sufficiency
  reduction are correct. Most of it re-verifies PD-T215/216/218/223/225/228.
  The registration decision is F4.
- **T02:** correct arithmetic, properly CONDITIONAL on a hypothetical C. My
  recommendation is not to register it (F5).
- **MEASURED, accepted as MEASURED:** the phase probe, the projection probe
  and the capped floating box pilot. The pilot is INCOMPLETE at every
  degree. It is neither an A1 pass nor an A1 kill.
- **Original target:** PD-T099 stays **OPEN**. The certified global range is
  still exactly 2–32 and no n>32 is certified. N_* is non-effective and the
  bridge 33<=n<N_* is open. There is no explicit full-diamond N1. The
  local/boundary results are supporting results, not a PARTIAL
  decomposition.
- **Severity:** no blocking finding and no mathematical error. F1–F2 are
  MAJOR (record/attribution, not proof). F3–F12 are MINOR. E1–E8 are
  editorial.

## Identity, rules and audited candidate

- **Auditor:** Claude, configured `claude-opus-5-5`, effort xhigh, as
  handoff 02 requested (mathematical audit of a novel mechanism). Role:
  audit orchestrator and auditor, distinct from every Codex developer
  (gpt-6-astra ultra), technical worker (gpt-6.1-sol medium) and the
  supplementary reviewer (gpt-6-astra high). The runtime exposes no
  separate serving-model receipt. I edited no developer file.
- **Independent subagent checks:** six Claude Opus 5.5 xhigh subagents.
  Each was read-only on the repository and briefed with the claims, not my
  conclusions. Each read `independent-math-checks.md` only after its own
  reconstruction. Their scopes were T01+T02, T03+N01, T04, T05, T06+T07, and
  novelty/registry/protocol. The last of these read the complete
  955-line `state/IDEAS.md`, including every obstruction and disposition
  table. Their scripts and outputs are local only (see Runs).
- **Rules:** `AGENTS.md`, `agents/WORKFLOW.md` and
  `agents/claude/CLAUDE_ROLES.md` were read at branch head
  `368b4c90ddc2f96124c15a512a7c7aa8a15f24b3`.
- **Audited input:** `352daad8c164617331c34ae81a7ce7331f501bb9`.
  - `git diff --stat 352daad 368b4c9` touches only handoffs 01 (status line)
    and 02.
  - `git diff 7d394fd 368b4c9` touches no theory, code or evidence file.
  - So every audited scientific byte equals the enclosing source `7d394fd`.
- **Main:** refetched at `aff30e8` (PR #22 merged after base `21dbfc9`). It
  touches only NN-MOP files and append-only registry rows, plus the IDEA-117
  row; no rule, template, tool or dependency of this topic changes. It
  merged cleanly into the topic as `3707a5f`, without rewriting history.
  - Both "Old:" anchors in `proposed-record-changes.md` still occur verbatim
    on main.
- **Open PRs (live 2026-11-05):** draft #21 `0b5fb2d`, #24 `02a465b`, #25
  (this topic) `368b4c9`, #26 `902360d`.
- **Audited hashes** (sha256; all equal the pins in
  `independent-math-checks.md`). All 41 rows of `evidence-manifest.json`
  match both the current bytes and `7d394fd`.

| File | sha256 |
|---|---|
| theory/phase-structure.md | `130820b34725a58e3dfd78602917d4eb77eb45d9476cae62532aa2579c42cbe4` |
| theory/localization-diagnosis.md | `43bf9eedc2931fdc5fa146fbcba92c615fac6fff39650fd21a80d86ab7a513c9` |
| theory/profile-boundary-cotangent.md | `8ccc83649464a568a12acaf03e265719b58dc4274b345b4a3a9be61eec652a3e` |
| theory/profile-leading-only-obstruction.md | `2545c5047d0c0cc743953b2141ff3766b9f919566e4fbf8b69aa2b9a02c9575e` |
| theory/defect-radius-extension.md | `a56fedfb1897c7bdbd1d761d7016e2bd0a016ccc7264440d05aa35a0d5d60a0d` |
| theory/corner-weighted-energy.md | `445f2c46907992b5c3d7173850205d4de8981bd9edebbf0413f0f4062e72bdf5` |
| theory/corner-global-norm-ratio.md | `2e9c0590ceb6032f0796a3383579751f241c13914918676418e85cd9a2c8dc59` |
| theory/corner-n2-local-radius.md | `280cfe73bc4ca82485a5f8df58ebbb864fd471a91403ac1b7849cdb4065bb5ad` |
| code/independent_math.py | `8481576a5fa766f2686208ab1ecc126f54e70970d2f9c89d38e3e12019ab5c8d` |
| evidence/independent-math.json | `3b2dba6591adde80ffade9bfd34920b462e467cea438a4d0acd2a86711088655` |

## Read coverage

- **Novelty scope applies.** The checkpoint contains candidates and negative
  claims, so the complete `state/IDEAS.md` was read (by the novelty
  subagent, in chunks), including every obstruction/disposition table. The
  aff30e8 delta to it is NN-MOP only.
- **Full shortlisted predecessors:**
  - IDEA-305, 316–335 (FINAL_CANDIDATES and gated/CANDIDATES), 336–348
    (phase-1 idea bodies), 320 (original body) and 326;
  - `gate-t4.md` (the IDEA-358 wrapper) and PD-T270;
  - PD-N079, PD-T227, PD-T215, PD-T216, PD-T222, PD-T224, PD-T250, PD-T251;
  - PD-T101 conventions and the PD-T157 statement.
- **Read in part:** PD-T218, T223, T225, T226, T228 (§1 and its statement),
  PD-N085 (statement and scope), and the PD-T232/233/247 statements.
- **Literature:** `literature/INDEX.md` headers and targeted searches
  (Padua, Lebesgue function/constant, cotangent, Euler–Maclaurin,
  Chebyshev–Lobatto, Bos, Caliari, De Marchi, Vianello, Xu), and the LIT-312
  record. No external fulltext was read.
- **Topic files read in full:** LOG, report, gates, gates-structural, plan,
  both novelty gates, ideas/*, attempts/*, all eight theory files, box-pilot,
  ALLOCATIONS, allocation-review, proposed-record-changes, COLD_STORAGE and
  both handoffs.
- **Read in part:** projection-probe and phase-probe headers.
- **Not re-audited:** the proof bodies of PD-T157, PD-T222 and PD-T228 beyond
  §1, and PD-N080–086 beyond their registry rows. These are accepted
  dependencies; T04's use of PD-T222 and T05/T06's use of PD-T157 were
  checked at the point of use.

## Independent mathematical reconstruction

- **T01.**
  - Reconstructed: the four-copy identity λ=M−Δ; Δ ≥ Q_v, Q_h; and the
    endpoint multiplicities (residues 0 and n get two coincident half-weight
    preimages, so there is no boundary correction).
  - Reconstructed: the chart identity λ=S_n−Δ_JK with the correct domains
    D_JK, and the cover lemma (the L1 distances to a cell's two odd vertices
    sum to 2). The collision values, divided-difference and sinc charts, and
    the 1/(8N) full-orbit formula (orbit sizes 4/2/1, 4e_jf_k/(8N)=w/4) also
    check.
  - The reduction is complete. The classes partition the centres, the D_JK
    cover the closed square including edges, nodes and both nonnode corners,
    and Far and Defect give strict inequality.
  - At a nonnode corner, S=Λ_c and Δ=0, so only the Corner predicate can
    accept it. The equality set is therefore exactly the two corners. This is
    a sufficiency theorem only; it builds no certificate.
- **T02.** The arithmetic is right; I also checked it by hand: the leading
  log n is Cπ⁴/(2ρ²), e.g. 279,291 at C=1.4, ρ=1/64. The geometric minimum
  of 1−a over ρ ≥ r is 1−cos(r/2). No certified C and no practical threshold
  is asserted.
- **T03.**
  - Reconstructed: on α=πt, β=π(1−t) the numerator gives
    (−1)^j G = sin πt·cot((u+v)/2).
  - Reconstructed: the CRT map (j,r) ↦ mj+nr mod 2N has kernel
    {(0,0),(n,m)}, so it is onto. Because n+m is odd, each fibre holds
    exactly one odd-board element, for either parity of n.
  - Reconstructed: the vertices have S=1; evenness covers all four edges;
    collisions are isolated at t=k/(2n+1) and removable.
  - The remainder is at most (1/(2π)+π²/24)/N² ≈ 0.5704/N², below
    7/12 ≈ 0.5833/N², for every N ≥ 1.
  - C(t) = −ψ(t) − ψ(1−t). The midpoint value is PD-T270 eq. (2) at degree N.
- **N01.** It needs only that b_n is phase-independent. a≡0 on the
  boundary, while S_n(π/2,π/2) = L_N ≥ A_N − 1/(4N²) grows like
  (4/π) log n. Its scope (lines 44–47, 69–70) does not refute H2, PD-T216 or
  IDEA-337.
- **T04.**
  - All eight line selections were re-derived: displacements, parities,
    index ranges with f_k=e_j=1, and bands. They are identical to PD-T224's.
  - The case split is exhaustive. K interior with s ≤ 4 uses own lines;
    s ≥ 5 uses PD-T222(V) (needs (5π−1/10)/m > 4π/n and ρ < 1/8). An
    endpoint K forces J interior, with the horizontal analogue.
  - Exact constants: √2 < 17/12; cos²(π/8) < 41/48 < (37/40)²; numerator
    floor (399/400)(3/40) − 1/20 = 397/16000 > 1/64; 1/6656 > 1/8192.
  - The range inequalities hold from n ≥ 38.25.
  - It uses the full defect via Δ ≥ Q. No sample is a premise.
- **T05.**
  - W matches PD-T227 part 4 exactly. The zero cardinals Z={(j,0): j>0
    even} are excluded from W. Their linear part enters A_n, B_n exactly, and
    their Taylor remainders are inside PD-T227 (6)–(7), which T07 applies
    directly. So no term is missing.
  - Re-derived: the gradient ratios; the diagonal cancellation K_n =
    −2m³/[n(2n+1)²] with the error constants (|q_x| ≤ 29.55m²,
    |q_y| < 31m²); the off-diagonal geometry L ≤ D+1 (tight at k=m) and
    (7)–(9) (22500, 61 and 2·10⁶ n⁴); the multiplicities ≤ 2 and ≤ 4; the
    sums; the removable (0,0) term (< n⁴); and the logarithmic absorption
    H ≤ 11Λ_c for all n ≥ 2.
  - Total: 4,301,010,007 n⁴ Λ_c ≤ 10¹⁰ n⁴ Λ_c.
- **T06.**
  - The four-reflection kernel pairing and the 2-branch lift are exhaustive.
    The 18-per-bin overcount is safe: the measured maximum is 4.
  - Σ B_l ≤ 2m H_m, and m/n ≤ 3/2.
  - The ratio uses Λ_c ≥ 2 for log n ≤ 20 and PD-T157 for log n ≥ 20. The
    worst value of H²/max(2, (4/π²)x² − 54) is about 81.3, against the
    required ≤ 250. No argmax assumption is used.
- **T07.**
  - PD-T227 (3) needs no sign preservation: AM-GM gives
    |l+g·h| ≤ |l| + sign(l)g·h + (g·h)²/(2|l|) pointwise.
  - The remainder comes from exact finite Taylor expansion with
    Σ_B|∂^r_x ∂^s_y L_B(c)| ≤ n^{2r+2s} Λ_n, using tensor Lobatto, a sign
    choice and T_n^{(r)}(1) ≤ n^{2r}.
  - Exact rational check at z = 10⁻¹¹: (10¹⁰+90000)z/2 = 0.05000045 < 1/16,
    and e^z − 1 − z ≤ 3z²/2.
  - The inward quadrant covers every direction into the square. PD-N085 is
    respected.

No reconstruction found a gap. The numerical falsification runs below
found no violation of any final or intermediate bound.

## Findings

**F1 — MAJOR (novelty/attribution), T06.** `corner-global-norm-ratio.md`
(lines 31–46) records no closest prior and says "no external theorem".
- The H2/H3 gate search terms (`novelty-gate-H2-H3.md` lines 12–15) omit
  Lebesgue constant, log² and global norm, and its table has no T06 row.
- Repository records of the known result:
  - LIT-312 (Bos et al. 2006, Theorem 3: Padua Lebesgue constant
    ≤ C log² n, constant unspecified; record
    `literature/lattice-unisolvence/records/padua-2006.md`);
  - `topics/padua-proof-attempts-2-20261101/attempts/T-A2.md`;
  - LIT-379 ((4/π²)log² n + O(log n));
  - the eventual non-explicit ratio from PD-T216 + PD-T157
    (`gated-codex-13` line 168).
- Meanwhile `report.md` "For the paper" lists "global-norm bounds" as an
  addition.
- **Required:**
  - add these predecessors to T06, the gate and the IDEA record;
  - restate T06 as an explicit-constant re-derivation of a known
    O(log² n) theorem;
  - qualify the report's paper sentence;
  - make no "first explicit constant" claim unless an inspectable source
    check supports it. The Bos et al. fulltext is a pending reference.
- The mathematics is unaffected.

**F2 — MAJOR (attribution/scope), T07.**
- **Missing predecessors.** `corner-n2-local-radius.md` lines 96–99, the
  report headline, `ideas/H2-H3.md` and the gate do not cite the closest
  existing n⁻² result. That result is PD-T228's 2⁻¹⁷/n² radius
  (`gated-codex-14` lines 26 and 212), which requires log n ≥ 10⁷. They also
  do not cite PD-T227's §Scope implication (8) ⇒ κ = min(1, a/(b+eK))
  (`gated-codex-13` lines 156–168), of which T07 is a direct instantiation
  (a=1/8, b=10¹⁰, K=3·10⁴).
- **Unqualified "strengthens".** "Strengthens the radius scale beyond
  PD-T251's n⁻⁶" (line 98, also LOG) is true only for n ≥ 473. For
  2 ≤ n ≤ 472, 1/(2N³) > 10⁻¹¹/n²: at n=2 they are 2.3·10⁻³ against
  2.5·10⁻¹².
- **Required:**
  - state the separation: every n ≥ 2 with an explicit constant, against
    eventual only;
  - present the usable all-degree radius as max(1/(2N³), 10⁻¹¹/n²);
  - cite PD-T227 (8) and PD-T228 in the record, the report and the
    proposed CURRENT/PAPER_MAP text.
- `report.md` already notes that the old radius can be larger at moderate
  degrees; the theory file and the LOG must match it.

**F3 — MINOR (gate interpretation for AC).** The A0 rule in
`handoffs/01-work.md` reopens R1 as a main line "if that value is ≤ 10⁴".
- The sharpened geometric variant gives log n of 7076–8592 at ρ=1/16, which
  meets the letter.
- The value the criterion names (PD-T216 + PD-T225 as inherited) is
  17456–21197 at ρ=1/16 and about 2.8–3.4·10⁵ at 1/64, which does not.
- The developer's refusal to reopen is mathematically sound. exp(7076) is
  unreachable, no global C is proved, and the corner comparison at that
  radius is missing.
- But it is not a dated criterion interpretation, as the handoff rule
  requires.
- **Required:** a dated entry in `gates.md`. My reading: the criterion
  addresses the inherited coarse route, so it is not met. The sharpened
  variant is a separate geometric refinement that does not reopen R1. AC
  may decide otherwise; preserve this for AC.

**F4 — MINOR (classification), T01.**
- Identities (1)–(5), the cover lemma, collisions and charts restate
  PD-T215/216/218/223/225/226/228 and PD-T101. The 1/(8N) orbit formula
  generalizes PD-T228 eq. (3) from corner centres to all odd centres by
  routine reindexing; the supplementary review's "new" is overstated.
- Only the finite phase-chart sufficiency reduction is a new statement
  (precedent: PD-T210).
- **Required:**
  - relabel the identity parts as verification of the cited records, not new
    PROVED dependencies;
  - cite PD-T225, PD-T228 eq. (3) and PD-T210;
  - at preparation, register either one narrow PD-T for the sufficiency
    reduction (with the orbit/profile formulas as labelled routine lemmas),
    or defer it until an H1 checker cites it. I recommend the narrow
    registration, because IDEA H1 already names it.
- Remove the stale "pending supplementary check" (line 55).

**F5 — MINOR, T02.**
- Recommendation: do not register. Keep it as gate-A0 evidence, linked from
  R1's deferred disposition.
- `localization-diagnosis.md` line 73 says noncorner defect control stops at
  r ≤ 1/64. It must cite T04 (ρ ≤ 1/10), which now covers r=1/16; the
  conclusion is unchanged.
- Cite the provenance of the hypothetical C range: the handoff A0 gate and
  the measured PD-T247/252.

**F6 — MINOR (measured records).** The phase-probe, projection-probe and
box-pilot measurements are used in `gates.md` but have no registered
MEASURED home and are absent from `proposed-record-changes.md`. Phase 1
registered its equivalents (PD-T247/252).
- The measured predecessors PD-T232/247 (phase/defect screens) and PD-T233
  (energy screen) are cited nowhere in the topic. T05 should cite PD-T233.
- **Required:** propose one scoped MEASURED record (or an explicit reason
  for none), and add these citations.

**F7 — MINOR (candidate dispositions).** Nothing is lost, but:
- `ideas/H1.md` line 15 omits the box-pilot outcome that
  `proposed-record-changes.md` promises;
- the signed-polynomial Markov shortcut is "under analysis"
  (`novelty-gate-H2-H3.md` line 38) and "no rejection"
  (`ideas/H2-H3.md` line 56), with no disposition. It is effectively
  PD-T227 (6)–(7): record it as equivalent or deferred;
- the cell-integral envelope norm route (`ideas/H2-H3.md` line 62) needs a
  `deferred` disposition with a resume condition;
- the T04 sub-variant has no provisional IDEA label;
- the full-diamond profile with a phase-dependent logarithm lives only
  inside IDEA03's text;
- the H1 gate row for IDEA-320 (`novelty-gate-H1.md` line 22) compares only
  PD-T210's implementation. Original IDEA-320 already had S-discard and
  three regions. State the separation as phase-diamond reuse plus classwise
  defect bounds; the verdict is unchanged.

**F8 — MINOR (protocol disclosure completeness).** Add to the handoff/log
protocol list:
- At published checkpoint `d98613e`, T01/T02/T04 linked to
  `novelty-gate-H1.md`, `attempts/H1.md` and `gates-structural.md`, which
  were first committed at `50bcbb4`. The prospective H1 gate is
  self-attested only.
- The H1 parent delegated its full registry read (`novelty-gate-H1.md`
  line 8).
- `LOG.md` has no entry recording the gates' scope, terms and timing.

**F9 — MINOR (second corner), T05/T07.** Both transfer to the second
nonnode corner by "the node-preserving reflection of PD-T251". PD-T251 only
asserts this "exactly as in PD-T228"; it does not prove it.
- The claim is true; numerically, Λ_c, A, B and W agree at both corners to
  about 10⁻⁴³ for n ≤ 40.
- **Required:** a one-line invariance argument (the x-reflection for even n
  and the y-reflection for odd n permute nodes and weights) or a precise
  citation, and a status row.

**F10 — MINOR, N01 lines 67–68.** "The obstruction requires a nonzero
phase-dependent logarithmic correction on the diamond boundary" does not
follow from N01's midpoint argument: a phase-independent c_n would fix the
midpoint. It holds only via T03: a≡0 on the boundary while S=1 at the
vertices and S=L_N at the midpoints. Cite T03 (2) or mark it as a remark.

**F11 — MINOR (reproducibility).**
- Handoff 02's command for `independent_math.py` omits its required
  `--output` argument; it exits with status 2. The working form is in
  `independent-math-checks.md` line 206.
- `projection_probe.py` and `box_pilot.py` import `phase_probe` from their
  own directory, so they cannot run under `python -I`.
- `structure_probe.py`'s "direct cardinal" path is the PD-T101 kernel
  expansion at phases (±π/4, ±π/4). It does not exercise the orbit formula,
  the Q formulas, the cover lemma or the sinc chart. `gates-structural.md`
  line 41 should state that scope.

**F12 — MINOR (storage durability).** The 40 pending-local outputs
(118,964,704 bytes) live under `local-output/argmax-effective-2-20261105/`
in the Codex sandbox. They do not exist in this cloud session, so no one
can deliver or retrieve them from here.
- The analytic proofs do not depend on them. Every receipt-level
  mathematical field regenerated identically in my reruns (below), but the
  original timing bytes and n=256 CPU-capped frontiers are not
  reproducible.
- **Required:** Codex states whether its sandbox still holds the bytes. If
  not, `COLD_STORAGE.md` must say "not retained; regenerable except
  timing", rather than "pending delivery".

**Editorial.**
- E1: stale "pending" wording at T06 lines 28–29 and T07 lines 33–35. T07
  must also say its status rests on T05/T06 as accepted here.
- E2: symbol clashes — N (node count in PD-T101), H (1+log m in T05/T06,
  but h_x+h_y in T07), and L_n (PD-T220 versus PD-T159/270).
- E3: T03 "Depends on" should list PD-T159 (the csc definition of L_M) and
  PD-T270 eq. (2) (the cot form).
- E4: T06 should define D_n, cite PD-T227 (not PD-T185) for the interior
  four-reflection formula, and cite PD-T251 §1 for Λ_c ≥ 2.
- E5: T04 lines 28 and 171 say the "numerator floor" is sharpened, but it
  drops from 223/4096 to 397/16000; what improves is the baseline
  (1/16 → 3/40). Same at `ideas/H1.md` line 23.
- E6: T04 also needs: a definition of ρ := |α|+|β| (line 49); α²+β² ≤ ρ²
  (line 52); a forward reference for "opposite in sign" (line 70); and the
  m/4 − 1 ≥ m/8 step (line 109).
- E7: T05 small unstated steps — the sinc² range, R_E ≥ sinc² s,
  1 − R_d² ≤ 2(1 − R_d), H_m ≤ H, and the absorption of 3904 n⁴. Line 43
  also uses Λ_c ≥ 1 at (14).
- E8: the optional handoff-01 task 5 (degree-40 cross-check) is not
  recorded as not attempted. `box_pilot.c` line 51 uses 1/8192 instead of
  max(1/8192, profile), which is valid but weakens acceptance near
  n ≈ 48–64. Sampled S − Λ_c ≈ 8.0·10⁻⁵ there is about 65% of 1/8192.

## Disposition of the handoff's protocol items

- **H3 child gate timing:** accepted as disclosed (`attempts/H3.md`
  lines 55–66). After the full read, T05's only relevant predecessors are
  IDEA-330/PD-T227, IDEA-345/PD-N084, IDEA-347/PD-N085, IDEA-348/PD-T251 and
  the measured PD-T233. The child read all of them except PD-T233, which is
  not a theorem. No verdict changes.
- **IDEA-358 wrapper read late:** accepted as disclosed. Its subject (corner
  signed deformation) differs from T03's boundary phase cancellation, and
  the load-bearing PD-T270 was read beforehand. No verdict changes.
- The coverage gaps that actually matter are F1 and F2, in the lead's scan
  for T06/T07, and F8. These are not the disclosed timing items. No
  retrospective full prospective compliance is granted; the disclosures
  stand as written.
- **Merge `ed21cc0` without typed prefix or trailers:** accepted as
  disclosed. Merging main is required, and the commit must not be
  rewritten. This audit's merge `3707a5f` carries the prefix and trailers.
- **Candidates:** every considered candidate is retained (F7 asks only for
  explicit dispositions). No historical novelty or new literature transfer
  is claimed. N01 and the capped pilot stay within scope. PD-N079, PD-N084,
  PD-N085 and PD-N086 are not contradicted.
- **Model allocation:** gpt-6-astra ultra for the mathematics follows AC's
  explicit 2026-11-03 instruction (handoff 01) and is justified in the LOG.
  Parent serving metadata is disclosed as unexposed.

## Reservation check

- **Reservation:** T364–375 / N132–137 / IDEA454–465 / LIT594–597, first
  published at `ce17564`, unchanged since.
- **Main `aff30e8` and every open PR head listed above:** no use or
  overlapping reservation of these ranges in PROOF_STATUS, IDEAS, INDEX,
  ID_CROSSWALK or any ledger.
  - PR22, now merged, assigned T286–290, N100, IDEA376–379 and LIT562–568,
    all below these ranges.
  - PR26's ledger explicitly records this reservation and reserves above it
    (IDEA466–489).
- **Required before any assignment or readiness:** the full union recheck.

## Runs executed by this audit

All runs used Python 3.13.18, NumPy 2.5.3, mpmath 1.4.1, gcc/g++ 13.3.0 and
GMP 6.3.0, on Linux 6.18.44 with an Intel Xeon at 2.80 GHz. They ran in a
detached scratch worktree at `368b4c9`. The probe-overwritten receipts were
copied out and the worktree restored; no committed receipt was changed.
Raw outputs are local only, in the session scratchpad, and are not
archived.

### Repository commands

1. `python3 -I code/structure_probe.py`: exit 0, 25 s. 3544 cardinal and 172
   weighted-multiset checks, n=3–6, all accepted. Matches
   `gates-structural.md`.
2. `python3 -I code/a0.py`: exit 0. Every row equals the `gates.md` figures,
   e.g. 279291.75 / 339139.90 at 1/64 and 7075.53 / 8591.62 (sharp) at 1/16.
3. `OPENBLAS_NUM_THREADS=1 python3 -I code/independent_math.py --output
   <scratch>/independent-math.json`: exit 0, 9.8 s. All mathematical fields
   equal the committed receipt; only input_head, environment and elapsed
   time differ.
   - The handoff form without `--output` exits 2 (F11).
4. `python3 -I code/replay.py --work local-output/.../audit-replay --summary
   local-output/.../audit-replay-summary.json`: exit 0, 270 s.
   - The n17 (106 leaves) and n24 (154 leaves) regenerated and committed
     certificates are accepted by all four checker runs.
   - `mathematical_fields_equal`, `frontier_and_bounds_equal` and the
     previous math/receipt hash matches are all true. The mathematical
     sha256 values are `0257c171…` and `c352f9a2…`.
   - The regenerated certificate bytes differ only through excluded timing
     fields.
5. `OPENBLAS_NUM_THREADS=1 python3 code/phase_probe.py` (40 s),
   `projection_probe.py` (20 s) and `box_pilot.py` (174 s): exit 0. The
   last two need no `-I` (F11).
   - Phase- and projection-probe receipts: no scientific field differs (only
     compiler, timing and raw byte counts).
   - Box pilot: n17/32/64/128 are identical (2000 visited; unresolved
     880/902/774/802).
   - At n=256 the 60-CPU-second cap stopped at 543 visited with 213
     unresolved, against the developer's 802/308. This is the expected
     hardware dependence of a CPU-time cap, and the cover is incomplete
     either way.
6. `git diff --check 21dbfc9 368b4c9`: clean. Tracked topic files over
   16 KiB: only the hand-written `handoffs/01-work.md` (17,466 B, not
   generated output). `tools/cold_storage.py plan`: 0 bytes to relocate.

### Subagent falsification runs

These are high-precision floating point. They confirm only, and are not
proofs.

- **T01:**
  - Independent Vandermonde-inverse cardinals at 50 digits, n=2–8, two
    seeds: |λ − (S−Δ)| and |λ − orbit| ≤ 1.5e−49.
  - Exact Fraction multisets, the cover grid and δ_AB in Q(ζ_{2N}) for
    every node pair: 0 failures.
  - Mutation controls (dropped half-weights, even centres, exceptional
    coefficient 2) are all detected.
- **T03:** 2122 evaluations at 40 digits for n=2–60, including 538 collision
  points, vertices and midpoints, plus a float sweep of 4001 t per n.
  - Formula against the direct sum: ≤ 6.8e−36.
  - max N²|S − P_N| = 0.043633, against 7/12. The midpoint identity holds to
    5e−39.
- **T04:** about 1.19M samples over every admissible noncorner centre,
  n=48/49/50/64/97, with ρ ≤ 0.1, plus edge and fine-grid runs to n=200.
  - Zero violations. min Δ is about 0.549–0.563 (×8192 ≈ 4500), at
    edge-midpoint centres at ρ=0.1.
  - The own-line classes have min Δ ≥ 1.634.
- **T05:** 50-digit cardinals and gradients from the PD-T101 kernel,
  n=2–40, asserting every identity and intermediate bound; float64 to
  n=6000.
  - W/(n⁴Λ_c) ∈ [0.2945, 0.3831] for n ≤ 40, 0.385 at n=6000.
  - Every intermediate ratio is < 1; the tightest chord bound is at 0.9997.
- **T06/T07:** 60-digit descent test, n=2–25, both corners, 12 directions,
  four radii up to 10⁻¹¹/n².
  - No violation; the worst normalized margin is 0.1319.
  - The bound first fails only at n²H ≈ 6–8.
  - 110H²/Λ_c ≤ 205 for n ≤ 40, and the bin count ≤ 4.
  - No affine sign change occurs at T07's radius below n ≈ 3.5·10¹¹. That
    mechanism therefore rests on the analytic AM-GM argument, checked above,
    and on a stress test of PD-T227 (3) at n²H up to 1, with up to 37 sign
    flips.

## Remaining uncertainty

- The all-n claims rest on analytic reconstruction. The numerics are not
  interval-certified, and none could exercise T07's sign-change mechanism at
  its stated radius.
- The inherited PD-T157, PD-T222 and PD-T228 bodies were not re-audited.
- No external fulltext was read. Whether Bos et al. 2006 or later work
  states explicit constants matching T06, or the boundary/generating-curve
  identity behind T03 (cf. LIT-312), is unknown.
- Prospective gate timing is reconstructable only from commits and
  self-attestation.

## Required response (handoff 03)

Codex answers F1–F12 and E1–E8 in `response-01.md`, each with a fix, an
evidence-based rejection, or an explicit unresolved item. No requested
change alters a statement, proof step or constant: they are attribution,
scope wording, records, dispositions and reproducibility. A Claude response
check of the record changes therefore suffices before PR preparation,
unless the response changes a statement, proof or status; that would need a
mathematical re-audit. The remaining H1/H2 research stays OPEN and is not
part of the response.
