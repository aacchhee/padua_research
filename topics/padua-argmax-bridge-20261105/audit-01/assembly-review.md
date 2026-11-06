# Interim Claude audit: C13 global assembly/cover (Scope A) and native finite range 2–40 (Scope B)

Auditor: Claude Opus 5.5, xhigh effort, independent subagent in the interim Claude audit.
Audited: branch `codex/padua-argmax-bridge-20261105` at `02beaef2b22f8232286713dab0a1b7c95582ce13`
(worktree clean, HEAD verified). Rules read at that SHA: AGENTS.md, agents/WORKFLOW.md
(roles, status, computation and evidence sections; computer-proof rule WORKFLOW.md:109).
No state-changing git command was run and no repository file was edited.
No novelty content is in scope (assembly and finite replay only), so the full IDEAS.md read was skipped.

Labels used below: **[D]** my own derivation, **[E]** my own execution, **[I]** inspection only.

## Files read in full or in the relevant parts

- `$T/theory/C13-onset-budget.md` (full, 135 lines), sha256 bc975d53…ea0
- `topics/padua-argmax-effective-2-20261105/theory/phase-structure.md` (PD-T364, full, 250 lines)
- The statement, domain and closing sections of `C13-near-comparison.md`, `C13-corner-comparison.md`,
  `C13-corner-value-lower.md` and `C13-far-comparison.md`. I read the corner comparison §5 in full and
  near comparison (17)–(18) in full. I did not re-derive the near/far representation and
  comparison analytic estimates; that is outside the assembly scope.
- The `C02-defect-dense-band.md` statement; `independent-checks-C13-onset.md` lines 1–30 and 290–446;
  `attempts/C13-onset.md` lines 76–120.
- `$T/theory/native-finite-range.md` (full), `$T/independent-checks-native-37-40.md` (full),
  `$T/theory/phase-checker-reduction.md` (header/status), PD-T210 record lines 1–150,
  and the native checker `README.md`, `check.py` and `kernel.cpp` (full).
- `$T/code/check_native_37_40.py` (inspected for its guards) and PROOF_STATUS rows PD-T099/210/246/364.

All nine C13 hashes listed in `independent-checks-C13-onset.md:375-385` match the current files [E].

## Scope A: global assembly and cover

### (i) Definitions [D]
PD-T364 defines m=n+1, N=nm, a_j=jπ/n, b_k=kπ/m and nodes j+k even. The weights are w=2e_jf_k/N,
which gives 1/(2N) at vertices, 1/N on edges and 2/N inside. D_n=Σ_{a+b≤n}h_ah_b cos(au)cos(bv) with h_0=1 and h_a=2,
and G_n=D_n−cos(nu). The product-to-sum step gives L_jk(cosθ,cosφ)=w_jk[Σ h_ah_b T_a(x)T_a(x_j)T_b(y)T_b(y_k) − T_n(x)T_n(x_j)].
This is the standard Padua cardinal w_ξ[K_n(ξ,x) − T̂_n(ξ_1)T̂_n(x_1)/2], so the (n,0) mode has coefficient 2−1=1, which is the
"exceptional highest x mode". The phases θ=(Jπ+α)/n and φ=(Kπ+β)/m make S_n(α,β)=(2N)⁻¹Σ_{Γ⁻}|G_n(...)| with 2N terms.
Every quantity is a trigonometric polynomial, so collisions need no special definition.
[E] A float sanity check (`scripts/cover_sanity.py`, MEASURED only, n=2..8) gives a cardinal-property error ≤2.1e-15 at all nodes.
The Λ_c values (3, 3.776142375, 4.409725436 at n=2,3,4) agree with the GMP kernel's outward threshold to 9 digits.
The kernel's constructor was written separately, so the two cardinal constructions agree.

### (ii) Closed physical cover with odd centre and ρ≤π [D]
Put X=nθ/π∈[0,n] and Y=mφ/π∈[0,m]. Take the rectangle [j,j+1]×[k,k+1] with j=min(⌊X⌋,n−1) and k=min(⌊Y⌋,m−1).
This always exists because n≥1 and m≥2, and the clamp handles θ=π or φ=π. Exactly one diagonal pair of vertices has odd J+K:
{(j,k),(j+1,k+1)} if j+k is odd, otherwise {(j+1,k),(j,k+1)}. With x=X−j and y=Y−k in [0,1], the L1 distances are x+y and 2−x−y,
or 1−x+y and 1+x−y. Each pair sums to 2, so the minimum is ≤1. Since α=π(X−J) and β=π(Y−K), ρ=π·(normalized L1) ≤ π.
Both vertices satisfy 0≤J≤n and 0≤K≤m, and the point's own θ,φ lie in [0,π]. The chart is therefore automatically physical, i.e. in D_JK.
This also holds on the square boundary, on edge rectangles (j=0 or n−1, k=0 or m−1), and for θ or φ in {0,π}.
Ties x+y=1 give two charts with ρ=π, and both are valid. (θ,φ)↦(cosθ,cosφ) is a bijection [0,π]²→[-1,1]².
**The claim is correct.** [E] For every sampled point (random, all four edges, all mesh points, diagonals and a tie point; n=2..8)
the rectangle chart was among the physical odd charts and had normalized distance ≤1.

### (iii) Corner centres and inward phases [D]
Odd centres with both coordinates at an endpoint: (n,m) always has parity 2n+1, which is odd. (0,m) has parity n+1 and is odd iff n is even.
(n,0) has parity n and is odd iff n is odd. (0,0) is a node. At (n,m), θ=π+α/n≤π forces α≤0 and φ=π+β/m≤π forces β≤0.
At (0,m) the constraints force α≥0 and β≤0; at (n,0) they force α≤0 and β≥0. These are the only physical constraints, so every
physical phase at a corner centre is inward. With A=|α| and B=|β|, the ρ≤1/2 physical set is exactly {A,B≥0, A+B≤1/2}.
That is the patch of `C13-corner-comparison.md:11-17`, and its image (−cos(A/n), −cos(B/(n+1))) is stated correctly at :16.
At (0,m) the physical point is (cos(A/n), −cos(B/m)), which is the x-reflection of the (n,m) patch; for odd n it is the y-reflection.
**Correct.** [E] For 200 random phases per corner centre, n=2..8, "physical" was equivalent to "inward".
Every other odd centre has an interior coordinate, so it is in the near-noncorner class of `C13-near-comparison.md:16-20`.
C02 supplies Q_v>1/16 if 0<K<m and Q_h>1/16 if 0<J<n (`C02-defect-dense-band.md:24-28`), so one applicable projection always exists.

### (iv) Nodes, the ρ=1/2 boundary and collisions [D]
A node is an even lattice point, so its distance to any odd lattice point is an integer ≥1. Its ρ is therefore exactly π for every odd chart.
Nodes, including node corners, never enter a near or corner chart; the far case covers them, and they have λ=1<Λ_c in any case.
[E] min ρ over all odd centres was π at every node, n=2..8. The far statement (3) is closed at ρ=1/2 and ρ=π (`C13-far-comparison.md:10-13`).
Near (2)/(4) is closed at ρ≤1/2 (`C13-near-comparison.md:10-25`), and the corner patch is closed (A+B≤1/2). Points with ρ exactly 1/2 are
covered twice and both bounds hold. Collisions do not arise as a separate case because every function is a polynomial.
**Correct.**

### (v) λ=S−Δ, Δ≥0 at every chart [D]
In PD-T364 (1)–(4), Δ is defined from the physical point (θ,φ) alone, and M(θ,φ)=S_n(α,β) for any odd translation (J,K).
This uses the even-board bijection and 2π-periodicity and needs no physicality or nearest-centre condition. Therefore λ=S_n(α,β)−Δ with Δ≥0 (triangle inequality,
positive weights) at every chart representation, including nodes, edges and collisions. Hence λ≤S_n everywhere.
Since S_n is center-independent and (3) covers every real phase pair in the closed annulus 1/2≤ρ≤π, any point whose chosen chart has ρ≥1/2 has λ<Λ_c−1/2000.
**Correct.** [E] |λ−(S−Δ)|≤8.9e-15 and Δ≥0 at every physical odd chart with ρ≤π (all charts, not only the chosen one) at all sample points.

### (vi) Circularity [I]+[D]
The dependency chain is: global ← (3),(4),(5) and PD-T364. (3) depends on the far representation and corner-value lower. (4) depends on the near representation, C02, C04, C05 and N1-16/17.
(5) depends on corner-value baseline (19), C05 and C07. Λ_c is the defined value λ_n(−1,−1)=S_n(0,0) (PD-T364 (5)). None of these statements uses the global
maximum, a localization of the maximizer, or an energy premise. This agrees with the focused review's acyclicity check at `independent-checks-C13-onset.md:395-404`.
[D] The corner (5) arithmetic checks out exactly with Fraction (exit 0):
- p(131/10)=10987/64000>1/6;
- the inequality 1−a = sin²(A/2)+sin²(B/2) ≥ (95/96)²r2/4 holds, and (95/96)²/4 − 47/192 = 1/36864 > 0;
- in near (18), 2/1000+1/10000+11270/500000+3000/500000 = 383/12500, and 1/16−383/12500 > 1/32.

### (vii) Equality set and reflection [D]
x↦−x maps node (j,k)→(n−j,k) and changes parity by n−2j, so the node set is preserved iff n is even. y↦−y changes parity by m−2k, so it is preserved iff n is odd.
The polynomial space and interpolation commute with that reflection, so λ is symmetric and the two odd-corner values are equal.
The equality set is {(−1,−1),(1,−1)} for even n and {(−1,−1),(−1,1)} for odd n, matching `C13-onset-budget.md:19-22`.
[E] Over n=2..8 the corner values put exactly the parity-correct pair at Λ_c, and the reflection asymmetry was ≤4.4e-15.
**Assembly verdict: the global proof in `C13-onset-budget.md:84-102` is valid given (3), (4), (5) and PD-T364. I found no gap.**

## Scope B: finite range 2–40

### Reduction [I]+[D]
The proved reduction is **PD-T210** (`topics/padua-argmax-alln-20261101/theory/argmax-alln-codex-03-finite-certificate-correctness.md:12-27,97-141`,
registered PROVED at PROOF_STATUS.md:313), not `phase-checker-reduction.md`. That file is OPEN and phase-route only (`phase-checker-reduction.md:8-11`),
and native-finite-range.md does not cite it. I checked PD-T210's proof myself. The Bernstein weights are ≥0 with partition of unity; a bound leaf gives a strict inequality.
On a corner leaf, the true vertex coefficient of each cardinal equals L_l(e), so its absolute sum is C exactly whatever the enclosure width. The other coefficients are <C₋≤C,
and the vertex weight equals 1 only at e. Replacing sums by upper enclosures and C by C₋ preserves strictness. **Sound.** 2–32 is inherited from registered PD-T209/162/166/169/174/177/181/214/246.

### Checker acceptance predicates (kernel.cpp, check.py) [I]+[D]
- Constructor (kernel.cpp:41-43):
  - Machin π bracket and alternating cosine Taylor bracket. Valid because |x|≤π/2, so the term ratio is <1.
  - The cos(π/n) seed is oriented correctly (cos is decreasing).
  - Interval Chebyshev recurrence, then exact overrides v[0]=1, v[n]=−1 and v[n/2]=0.
  - mode(): r=jp mod 2n, folded by min(r,2n−r). Weights 2e_jf_k/N; h=1 exactly at (p,q)=(n,0); exact integer T-coefficients.
- Bernstein transform (kernel.cpp:42,45): w[k][i]=Σ_r C(i,r)C(k,r)2^r(−1)^{i−r}/C(n,r) is the exact power-to-Bernstein matrix on [−1,1].
  `linear()` picks endpoints by sign of the weight and rounds outward, with canonicalised rationals.
- De Casteljau midpoint split with floor/ceil averaging (kernel.cpp:30); the first child is the lower half and the axes alternate x,y.
  Flag clearing (kernel.cpp:39) tracks correctly whether a box still touches x=±1 or y=±1.
- Bound leaf: max_i Σ_l absmax(c_l,i) < low (kernel.cpp:34). Corner leaf: the box contains the vertex (flags), and every index except the vertex index
  ((0|n)·(n+1)+(0|n)) has a sum < low (kernel.cpp:36). These are exactly PD-T210's two predicates.
- Threshold: low = max of the two corner lower enclosures (kernel.cpp:44,46). This is valid only because the two corner values are equal (PD-T210 appendix, reflection).
  `high` serves only as a sanity check (S<low≤high).
- Partition: check.py:84-93 requires a prefix-free frontier with |F|=|A|+1, which forces a full binary tree. The native walk also throws on an uncovered child
  (kernel.cpp:39) and on duplicate or overlapping paths. check.py:105-125 then requires exact metadata equality, every leaf row equal to the reconstructed verdict,
  a frontier fully reached, producer accepted=false, no pending paths and both parity-correct corners covered. Pending paths always give accepted=false.
- [E] Controls on the scratch-built kernel at n=2,3,4: a root-only frontier gives a null verdict, as it must. Uniform depth 4 and 8 give 2 corner leaves, at exactly the parity-correct corners,
  plus all-bound leaves. An incomplete frontier is rejected ("uncovered partition", exit 1), and so is a duplicate path (exit 1).
- **I found no soundness defect in the acceptance predicates.** Trusted base, as stated at native-finite-range.md:98-99: compiler, GMP, Python json/gzip, hardware.

### Workflow computer-proof requirements (WORKFLOW.md:109) [I]
| Requirement | Status |
|---|---|
| Proved reduction | Met: PD-T210 PROVED and registered. |
| Exact arithmetic | Met: GMP integers and rationals; no floats in verdicts. |
| Committed checker | Met: `topics/padua-argmax-effective-20261103/code/native_checker/`; hashes b6c7320d… (driver) and b0c871e7… (kernel) match the record. |
| Committed evidence | Met: certificates n33–n40 (8–10 KB each) and receipts. |
| Independent rerun | Met by the distinct Codex checker executions, plus the Claude rerun below. |

The required Claude audit is still pending, and this report is interim.

### Independent rerun [E]
**n37 ACCEPTED.** I replayed the committed certificate from the committed checker, using a kernel binary I compiled myself under a fresh scratch path.

- Certificate: `topics/padua-argmax-bridge-20261105/evidence/n37.json.gz`, sha256 425fb779…efae, which matches native-finite-range.md:64.
- Build: `g++ -O3 -std=c++17 …/native_checker/kernel.cpp -lgmpxx -lgmp -o assembly-run/kernel`, exit 0.
  Binary sha256 e596d431…c9d7. It differs from the recorded f17fed2e… because the toolchain differs.
- Replay command, from the repository root:
  `python3 topics/padua-argmax-effective-20261103/code/native_checker/check.py topics/padua-argmax-bridge-20261105/evidence/n37.json.gz --binary assembly-run/kernel --output assembly-run/replay-n37.json`.
  It was wrapped by `assembly-run/run.sh`, which measures RUSAGE_CHILDREN.
- Result: exit 0, `accepted: true`, `complete_partition: true`, `all_supplied_bounds_verified: true`, counts bound 316 / corner 2 / splits 317.
  The counts match `independent-n37.json` and native-finite-range.md:34. checker_sha256 b6c7320d… and kernel_sha256 b0c871e7… also match.
- Cost: CPU 815.53 s user + 18.07 s sys = 833.59 s (recorded run: 897.8 s); wall 840.7 s.
- n40 (about 1367 CPU s) was not run because it would exceed the 30 CPU-minute cap together with n37. No producer was launched and no new degree was run.
- Outputs: `assembly-run/replay-n37.json`, `n37-wrapper.json` and `n37-wrapper.err` under the scratchpad audit directory.

## Findings

**No BLOCKING or MAJOR findings.**

- **A-1 MINOR (stale status).** All seven C13 records still say the focused F1/F2 check is pending:
  - `C13-onset-budget.md:33-35`, `:50`, `:122-123`;
  - `C13-near-representation.md:26`, `C13-near-comparison.md:34`, `C13-corner-value-lower.md:28`, `C13-corner-comparison.md:30`,
    `C13-far-representation.md:32`, `C13-far-comparison.md:25`.

  `independent-checks-C13-onset.md:361-367` records it as ACCEPTED, with all nine hashes matching [E].
  The prose files are hash-pinned by that review, so the fix must be a dated addendum (or a pin update or companion note), per WORKFLOW.md:187.
  The text "Formal Claude audit remains separate" stays correct.
- **A-2 MINOR (provenance).** The frozen original proof (483 lines, sha256 6cc04de4…) and the split-extraction script exist only as `/tmp` paths on another machine.
  They are cited at `C13-onset-budget.md:107-110` and `attempts/C13-onset.md:80-87,114-118`. Neither path exists here.
  The original was never committed: only commit 99c6b6f touches the file, and it already holds the 135-line split version [E].
  It is also not in COLD_STORAGE.md. The mathematics survives in full in the split files, so no claim depends on the snapshot.
  However, the focused review's byte-preservation verification cannot be repeated from the repository or cold storage.
  Recommendation: record the snapshot in cold storage with its hash, or state the limitation once in the log.
- **A-3 NOTE (wording).** At `C13-onset-budget.md:90`, "includes every center parity and edge" is loose, since every centre is odd. It means both degree parities and the edge centres.
  At `:92`, "Odd endpoint centers" should read "odd corner centres (both coordinates at endpoints)". Single-endpoint edge centres are noncorner and are handled by (4).
- **A-4 NOTE (clarity).** `C13-onset-budget.md:86-88` and PD-T364:134 could state explicitly that both odd vertices of any rectangle satisfy 0≤J≤n and 0≤K≤m,
  so the chart phase is automatically physical. I verified this in (ii); it is not a gap.
- **B-1 NOTE.** The finite reduction for 33–40 is PD-T210, not phase-checker-reduction.md (OPEN, not a dependency). The record cites PD-T210 correctly (native-finite-range.md:41-42).
- **B-2 NOTE.** native-finite-range.md:76-79 lists portable commands only for n33 and n34. The commands for 35–40 are in the separate independent records.
  At :89-92 the 33–36 shell exit statuses were lost and acceptance rests on the persisted receipts; this is disclosed honestly.
  The rerun recorded above covers n37 only.

## Commands, CPU and exit codes [E]
All runs were under `/tmp/claude-0/-home-user-padua-research/8833296e-cd9e-51d7-9205-e1ddfbc5960f/scratchpad/audit/`. Each command ran from the path its `cd` shows.

| Command | What it did | CPU | Exit |
|---|---|---|---|
| `apt-get install -y libgmp-dev` | libgmp-dev was already installed | negligible | 0 |
| `cd /home/user/padua_research; g++ -O3 -std=c++17 topics/padua-argmax-effective-20261103/code/native_checker/kernel.cpp -lgmpxx -lgmp -o assembly-run/kernel` | Built the kernel | 1.58 s | 0 |
| `cd /tmp/claude-0/-home-user-padua-research/8833296e-cd9e-51d7-9205-e1ddfbc5960f/scratchpad/audit; python3 -I scripts/cover_sanity.py > assembly-run/cover_sanity.out` | Float sanity check of the cover and identity | 7.2 s | 0 |
| Inline Fraction check of the p(L), sin² and near-sum constants | Exact arithmetic of the assembly constants | <0.1 s | 0 |
| Inline kernel predicate and negative controls, n=2,3,4 | Small-degree predicate controls | about 1 s | 0 |
| `cd /home/user/padua_research; python3 topics/padua-argmax-effective-20261103/code/native_checker/check.py topics/padua-argmax-bridge-20261105/evidence/n37.json.gz --binary assembly-run/kernel --output assembly-run/replay-n37.json`, run through `assembly-run/run.sh` | n37 replay | 833.59 s | 0 |

Total CPU was about 843 s, roughly 14 CPU-minutes, within the 30-minute cap.

The first sanity-script attempt exited 1 because my own tie-point test point was non-physical for n=2. I fixed it and reran; this was not a finding.

Toolchain: Python 3.13.18, g++ 13.3.0 (Ubuntu), libgmp 6.3.0+dfsg-2ubuntu6.1, numpy 2.5.3.
These differ from the recorded Debian toolchain, which adds toolchain diversity.
