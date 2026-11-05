# Audit 01 — padua-mz-cleanup-20261105 — independent Claude audit of the cleanup candidate

## Verdict

**No correctness finding.** The mathematics, the computer-assisted reduction and the measured scopes of C1–C3
are accepted at their stated scope. No status needs to change.

The audit does record **findings, none blocking and none major**: 12 minor and 14 editorial. They concern record
completeness, wording, provenance and the shared-record proposals. Under `agents/WORKFLOW.md`, findings set **WORK**.
Codex answers each finding in `response-01.md` (handoff 03). If no claim, proof, code or evidence changes
materially, the documented resolutions may proceed to PR preparation without a fresh audit. A material change
returns to AUDIT.

## Identity and scope

- **Auditor:** Claude, configured `claude-opus-5-5` (Opus 5.5). AC requested xhigh effort; the runtime does not expose
  the effort actually used. Role: independent auditor and topic orchestrator for handoff 02. The developer was
  Codex, gpt-6.1-sol xhigh, so the auditor is a different agent.
- **Rules** read at `902360d26edabc348d1a2b687f3ea44bb33f28e9`: AGENTS.md, agents/WORKFLOW.md,
  agents/claude/CLAUDE_ROLES.md and templates/HANDOFF.md. They are unchanged since ad503cb.
- **Candidate:** `10898ad99882248e5e6f9d76641624146af97454`. Head 902360d differs from it only in `handoffs/`.
- **Main/base:** `aff30e8ad5542c94fab642ae024dc9aab4fa7ad7`, an ancestor of the head (merged in ef9723b).
- **Shared files untouched:** `git diff aff30e8 HEAD` is empty for PROOF_STATUS.md, state/, RESULTS.md,
  ID_CROSSWALK.md, literature/, PAPER_MAP.md, agents/, templates/, AGENTS.md and .github/. The only change outside
  the topic directory and the manuscript is a pure append to the M7 record.
- **Theory files audited** (sha256 prefixes):

| File | sha256 prefix |
|---|---|
| finite-indefiniteness.md | 8cfc0d55 |
| finite-measurements.md | 46e716ca |
| growth-carrier-bounds.md | 0e72d427 |
| odd-carriers.md | 49067244 |
| odd-weight-asymptotic.md | 7e5ae874 |

- **Code audited** (sha256 prefixes). Every hash equals the one pinned in the developer's receipts:

| File | sha256 prefix |
|---|---|
| rigorous_witness.py | 11f7cabc |
| independent_witness.py | 60c1e6db |
| g1_minimum.py | 247bf4fa |
| g1_spectral.py | f246b7a4 |
| independent_odd_check.py | 2590f394 |

- **Orchestration.** I audited C1 directly. Four Claude Opus 5.5 subagents ran independent supplementary
  reconstructions, with no Git authority:
  - C2 mathematics (xhigh);
  - C3 mathematics (xhigh);
  - novelty and idea discipline (high);
  - manuscript, measurements and inventories (high).

  I spot-checked their key claims against the files: README:124, manuscript.tex:1544–1595, the CURRENT.md:42 line,
  the proposed-record-changes header, PROOF_STATUS:385, IDEAS:938, and the C3 constants recomputed with my own
  script. Their scripts and outputs are committed under `audit-support/sub-*/`. None of these checks replaces
  the developer's response.
- **Novelty coverage.** The novelty subagent read all of `state/IDEAS.md`, lines 1–974, in sequential chunks. That
  includes every obstruction and disposition table. It also read the full closest records IDEA-384–397 in
  `ideas-f12/f3/f4`. IDEA-210–227 were read as registry rows plus the PD-N044–053 table, not their d1–d7 bodies.
  The candidate makes no new literature or priority claim.
- **Sandbox.** All runs were in this session's container. Total compute was well under one CPU hour, no external
  machine was used, and nothing was written to AC's computer or cold storage.

## C1 — computer-assisted finite indefiniteness: accepted

### Reduction, re-derived

- **Definition.** Under the frozen definitions, λ_-(m,n) is the minimum over Π_n of Q_m(p²)/∫∫p² dxdy, because G
  is written in a dxdy-orthonormal product-Legendre basis. So an explicit p with N>0 and Q_m(p²)<0 gives λ_-<0.
  With Q_m(1)=4 the form is indefinite.
- **Trial quotients.** The tabulated rationals bound the trial quotient of each stated witness, not an eigenvalue.
  The records say so.
- **Producer.** I re-derived each bound:
  - |p−p̂| ≤ L_C(2ε+ε²), from |P_a| ≤ 1 and the per-entry predicate |P_a − A/S| < 1/S;
  - |K−K̂| ≤ L_D(2ε+ε²) + E_D(1+ε)²;
  - the energy error δ_K B0 + 2δ_p √((A0+δ_K B0) L_D) + δ_p² L_D. It follows from
    Kp² − K̂p̂² = (K−K̂)p̂² + 2Kp̂(p−p̂) + K(p−p̂)², with Cauchy–Schwarz, Σρ=1 (checked exactly) and |K| ≤ L_D.

  I also checked:
  - the scale exponents S⁹, S⁶ and S³;
  - the ρ multiplicities;
  - the halving at D_{m,0};
  - that the ball recurrence uses unrounded balls, so precision loss can only reject a run;
  - that the sign test uses certain Arb comparisons and raises an error on a straddle.
- **Alternate checker.** I re-derived:
  - the two-product forward bound (L+uL)(1+δ)²(1+γ)² − L. It is monotone in |a|,|b| ≤ 1, and the nested-product
    bound is ((1+γ)²−1)|A||C||B|ᵀ;
  - the scale and kernel weight error;
  - the final γ_{N+3} sum bound;
  - the cross terms 2E_pΣ|ŵp̂|, E_p²Σ|ŵ| and E_w.

  Its half-angle kernel (t_0=2, t_a=−4/(4a²−1), and −4/(1−m²) at (m/2,0) for even m) equals the producer's D with
  the exceptional halving. Its standard IEEE γ_k dot-product model is an explicit extra trust assumption.
- **Weight convention, independent of the developer's code.** `audit-support/code/kernel_vs_moments.py` solves the
  defining moment system Vᵀw = (h_a h_b), a+b ≤ m, at 80 digits. For m=1..13 (both parities) it matches
  ρ_jk K(x_j,y_k), with the T_m coefficient halved, to ≤3e-81 (`evidence/claude-kernel-vs-moments.txt`). The C2
  subagent separately confirmed this to 9e-72 for odd m ≤ 21 in 256-bit balls, and showed the halving is required
  at even m (error 0.027 without it at m=4).

### Actual executions

**Environment.** Python 3.13.18, python-flint 0.9.0, NumPy 2.5.4 and SciPy 1.18.1 under
`PYTHONPATH=/tmp/claude-0/deps`, with `OPENBLAS_NUM_THREADS=1`. These versions differ from the developer's
(3.12.14 / 2.3.5 / 1.17.0). The developer's `/tmp/mz-cleanup` artifacts are absent from this container. **No
original large witness, norm file or package is claimed retrieved or byte-checked.**

**Commands** (from the repository root; SP is this session's scratchpad):

```sh
PYTHONPATH=/tmp/claude-0/deps OPENBLAS_NUM_THREADS=1 python3 topics/padua-mz-cleanup-20261105/code/g1_minimum.py --m 60 400 1101 1240 1600 --output $SP/audit/minimum.json --vector-dir $SP/audit/vectors
PYTHONPATH=/tmp/claude-0/deps OPENBLAS_NUM_THREADS=1 python3 topics/padua-mz-cleanup-20261105/code/rigorous_witness.py --m $m --vector $SP/audit/vectors/m$m-n$((m-1))-min.npy --scratch $SP/audit/cert-m$m --output $SP/audit/producer-m$m.json
PYTHONPATH=/tmp/claude-0/deps OPENBLAS_NUM_THREADS=1 python3 topics/padua-mz-cleanup-20261105/code/independent_witness.py --witness $SP/audit/cert-m$m/witness.json.gz --output $SP/audit/independent-m$m.json
python3 audit-support/code/third_path.py $SP/audit/cert-m$m/witness.json.gz $SP/audit/cert-m$m/exact-norm.txt
python3 audit-support/code/bracket_check.py <receipt dir> <receipt dir> <producer prefix> <independent prefix>
```

**Proposals.**
- The m60 vector reproduces the developer's sha `62838be1…`.
- The m400, m1101, m1240 and m1600 vectors differ from the developer's. In particular m1600 is `90a8c0cd…`, not
  PR23's `a23cb0e6…`.
- The minima agree with the developer's within 3e-11.

**Certificates.** These are new, separately regenerated certificates for different dyadic witnesses:

| m | producer energy enclosure | alternate q_center ± error | sign | witness sha256 (gzip) | producer s |
|---|---|---|---|---|---|
| 60 | [0.1885934804891 ± 2.58e-14] | 0.18859348048909605 ± 1.33e-13 | + | 662491797ba699dc… | 0.1 |
| 400 | [0.102818906 ± 3.62e-10] | 0.10281890623374051 ± 3.01e-10 | + | ff6d451f1def8b2c… | 4.9 |
| 1101 | [−0.0350668 ± 4.18e-8] | −0.03506683433961681 ± 5.78e-8 | − | 56007f1e11dbaa2e… | 43.8 |
| 1240 | [−2.71e-5 ± 6.00e-8] | −2.7148059718220147e-5 ± 8.19e-8 | − | 84fad274f80ddb19… | 52.0 |
| 1600 | [−0.0234144 ± 4.95e-8] | −0.02341441659322953 ± 1.74e-7 | − | 69cbcf9713635158… | 107.3 |

The sign was the same on both paths at every m. Every run enclosed weight sum 4 and had a positive exact norm.
The receipts are `audit-support/evidence/claude-{producer,independent}-m*.json`. The large witness and norm files
remain in session scratch only. They are regenerable from the commands above with these library versions, and
will be lost with this container. They are not delivered anywhere and no delivery is claimed.

**Brackets.** `bracket_check.py` rebuilds every interval outward with Fractions and divides by the norm enclosure.
- In the developer's **committed** receipts at 1101, 1240 and 1600, both the producer interval and the alternate
  checker's q_center ± q_absolute_error lie strictly inside the stated rational brackets
  (`claude-brackets-committed.txt`).
- The alternate checker's default printed `q_enclosure` does not imply the bracket at 1240 or 1600. This is the
  caveat the developer already disclosed.
- My regenerated certificates fall inside the same three brackets (`claude-brackets-regenerated.txt`). The
  theorem's content is therefore reproduced here with different witnesses.

**Third path (MEASURED only).** `third_path.py` was written from `definitions.md` alone, with no topic code and no
FLINT.
- The float64 kernel weights satisfy every moment equation a+b ≤ m to ≤1.2e-13 at m1101, 1240 and 1600.
- The float Q_m(p²) agrees with both rigorous centers to ≤5e-12.
- The exact norm, recomputed with `fractions.Fraction`, equals the producer's `exact-norm.txt` exactly at every m.

**Extra float probes** (`g1_minimum.py --m 1238 1239`):
- m1238 gives +1.2076189966751e-4, which reproduces the developer's positive value to 7e-12.
- m1239 gives −0.045942496436. This odd degree lies outside the developer's grid; the result is auditor-only
  MEASURED and adds no claim.
- Together with the five regenerated minima above, this reruns 6 of the 23 developer rows: m60, 400, 1101, 1240,
  1600 and 1238. The other 17 were not rerun.

**Residual trust.**
- The producer trusts FLINT/Arb; the alternate path trusts FLINT/Arb plus the IEEE/BLAS γ model.
- The convention is checked exactly only for m ≤ 13 (≤ 21 by the subagent), and in float at the three large m.
- The developer's specific witness identities depend on the pending delivery of the 159,265,962-byte package.

### C1 findings

- **F1 (minor, provenance).** The witness identities are SHA-256 hashes of the gzip containers
  (`theory/finite-indefiniteness.md:28-35`, the receipts and `cold-storage.json`).
  - Here the m60 vector reproduced exactly, and so did the exact-norm file (`04e78a32…`).
  - The container hash was nevertheless `662491…` instead of `9a1bb58c…`. Container bytes depend on the
    Python/zlib build.
  - Fix: also record the SHA-256 of the decompressed canonical JSON payload in future receipts, the theory record
    and the storage manifest, and say the container hash is environment-specific. The existing identities stay
    valid for the staged files.
- **F2 (minor, wording).** `finite-indefiniteness.md` says the independent interval "lies inside the conservative
  rational bracket". That holds only for q_center ± q_absolute_error, not for the printed `q_enclosure`. Fix: state
  this reconstruction in the theory record.
- **F3 (editorial).** The proof paragraph is written for m1600 only ("Pi_1599", "near −0.0234144"). Fix: make it
  generic. The same applies to "regenerable" at line ~104: byte-identical regeneration is not guaranteed across
  platforms, which COLD_STORAGE.md already states correctly.

## C2 — odd-m weights and carriers: accepted

This is the subagent's independent reconstruction. Scripts and outputs are in `audit-support/sub-c2/`.

**Reconstructed by hand.**
- The odd kernel. h_m = 0, so the exceptional term vanishes at every node regardless of axis; no axis swap is used.
- The majorant (2). Each term in (6) holds, so the constant 8192 is valid.
- The fixed-index limit −16 e_j e_k (−1)^j. This includes the phases 2Rθ_j and 2Rφ_k, the thin-strip and
  middle-region split, and the order of limits (R→∞, then δ→0).
- The y-mesh carriers. Checked:
  - the identity sin(Mt/2) sin(rt) and exact parity selection on M=m+1;
  - the constant coefficients;
  - the degree conditions 2r<M, 2s<m and 4r<M;
  - the energies b/3, a/3 and a/6;
  - dominated convergence over the whole signed sum and the direction of the Rayleigh inequality;
  - the combination of even and odd subsequences into "all integers";
  - the fixed-θ degree budget, including the +1/2 overhead at odd m;
  - the edge 2⌊θm⌋ ≤ m, where G = I.
- Neither record relies on corner negativity alone or on an axis-swapped cardinal formula; both say so explicitly.

**Computations.**
- Ball moment solves at odd m = 3..21 match the formula to 9e-72.
- The majorant ratio, over every odd m from 5 to 601, is at most 182, against 8192.
- Fixed-node slopes at m = 10⁵..10⁶ match the predictions to about 1e-3. Examples: (0,0) gives −4.0002;
  (1,1) gives +16.002.
- Carrier energy slopes at m = 10⁶..10⁷ match the predictions to about 1e-5.
- ‖G−I‖ ≤ 4e-14 at n = ⌊m/2⌋.
- A replay of `independent_odd_check.py` passes, with 176 exact cases. mpmath here is 1.4.1.

**Findings.**
- **F4 (minor).** `odd-carriers.md:147-152`. Dominated convergence for p⁺ also needs sin²(rkπ/M) → sin²(akπ)
  pointwise. Fix: add the clause.
- **F5 (editorial).** `odd-carriers.md:44,193-196`. The record lacks the PD-N105–107 caveat "existence only, not
  feasible finite witnesses". By extrapolation only, the p⁻ carrier with a=b=0.2 still has Q = +2.686 at
  m = 10⁷+1. Fix: add the same sentence as the even records.
- **F6 (editorial).** `odd-carriers.md:59-62` bundles the odd packet theorem with the all-integer synthesis. Both
  parts are PROVED and separately labelled, and the synthesis is routine, so status aggregation is not at risk.
  The developer may optionally split them to mirror PD-N105/106 versus PD-N107.
- **F7 (editorial).** `novelty-gate-math.md:53`. The alias "coordinate-swapped odd-grid packet" can be misread as
  the forbidden axis swap. Fix: rename it "y-carrier odd-grid packet".

## C3 — normalized one-sided bounds: accepted

This is the subagent's independent reconstruction (`audit-support/sub-c3/`). I also recomputed the constants with
`audit-support/code/c3_constants.py`.

**Checked.**
- The denominator is the continuous L²(dxdy) norm, factorized into carrier and non-carrier parts, with limits
  A J_∓(a) at O(m⁰) and dominated by u·min(1, π⁴/u⁴).
- The cosine-transform identity: u g(u) = 2(3 − 4cos u + cos 2u)/u³, the moment cancellations, two integrations by
  parts, and the Frullani step, giving C(q) = Σ c_t t² log|t|.
- The energy coefficients −16ab/9 and 8ab/9.
- The boundary supremum. For every admissible packet the limsup/liminf bound holds; taking the infimum over b
  gives exactly −c₋ and +c₊. The supremum is approached, not attained, and no inadmissible packet is used.

**Constants**, to 20 digits:
- c₋ = 0.02962182359685996308;
- c₊ = 0.01277888643955839765.

Direct Gauss–Legendre quadrature agrees to about 3e-9 without using the transform. Finite normalized packet
slopes at m = 1600..3200 approach their limits monotonically (MEASURED). The record claims no sharpness, no
existence of a limit and no opposite bound, and the auditors found no text implying more.

Within the same family, a = 1/4 and a = 1/8 are not the optimal parameters. The optima are a ≈ 0.25686, giving
0.0296434, and a ≈ 0.12530, giving 0.0127790. The record's non-optimality disclaimer is accurate, and the stated
constants remain valid bounds.

**Findings.**
- **F8 (minor).** `report.md:78-79` displays "≤ −0.02962182360..." and "≥ 0.01277888644...". These are rounded up,
  and the ellipsis reads as a truncated expansion, which would state slightly stronger bounds than proved. The
  same strings appear in `results/padua-mz-cleanup-20261105.md` and the PR body as "≈", which is fine. Fix: use
  "≈", the truncations 0.0296218235… and 0.0127788864…, or the exact formulas.
- **F9 (editorial).** `growth-carrier-bounds.md:82-83` and `attempts/C3.md:27-28` print double-precision values
  that are wrong after about 13–14 digits because of cancellation. For example, J₊(1/8) = 0.78400536769110933… and
  c₊ = 0.012778886439558398…. Fix: cite high-precision values or state the precision.
- **F10 (editorial).** `attempts/C3.md:29-30` says the independent check is "requested, not yet claimed
  completed". That is stale. Fix: update it.
- **F11 (minor, preparation).** The OPEN sharp target ("Split from: C3's sharp-growth target") has no registered
  durable home. The split rules require it to stay registered with its true status and an ID_CROSSWALK mapping.
  Fix at preparation: register an OPEN record for the existence and value of lim λ_±(m,m−1)/log m, with
  "Split into: -04", or name the existing registered home. The analogous "Split from:" wording in the odd records
  (`odd-weight-asymptotic.md:5`, `odd-carriers.md:5`) describes extensions of accepted PD-T295 and PD-N105–107.
  "Extends:" is more accurate there and avoids implying crosswalk splits.

## Measured rows and K2: accepted as MEASURED

- There are 23 rows with no duplicates: 4 replay, 11 coarse, 5 fine and 3 growth.
- Every even degree 1230–1240 is present. All six odd probes are negative.
- The OLS fits, recomputed from the committed rows and the PD-T300 source (sha 82ada412…), give
  −0.09153004304730 and −0.09212159619974. The distances from −1/9, 0.019581 and 0.018990, match exactly.
- The K0 and K1 receipts match their claims.
- The 1240 statement is scoped to "this campaign". "No limit", "no first crossing" and the odd-crossing limitation
  appear consistently.
- The preregistration commit 6508e4e precedes the scan commit. Git cannot verify the relative order of the runs
  themselves; the claim rests on the developer's record.
- My own reruns (6 of the 23 rows) are listed under C1.

## Manuscript (C4): accepted at translation scope

**Build.** The subagent installed TeX Live 2023 with apt. pdflatex → bibtex → pdflatex → pdflatex gives
**25 A4 pages**:
- no warnings, no overfull or underfull boxes, no undefined references and no `??`;
- bibtex gives no warnings;
- the source sha256 `d0da06ad…c04f` matches manuscript-changes.md;
- `refs.bib` is unchanged and no `\cite` is added;
- there are no provisional IDs, and PR21 appears only as "not used";
- no PDF is tracked, and the preserved PDFs (outside Git) are untouched by the branch.

The PDF hash differs from the developer's because of the TeX version and timestamps.

**Fidelity to the records.**
- Trial quotients and eigenvalue brackets are kept distinct.
- The denominator is the continuous norm.
- The 1240 claim is scoped to this campaign.
- The IEEE/BLAS model is named.
- The constants are defined by integrals, with no sharpness claimed.
- MEASURED fits and windows do not appear as theorems.

**Findings.**
- **F12 (minor).** `tracks/mz-constants/paper/README.md:124` says the build "includes the committed finite
  certificates". Only the small receipts are committed; the witnesses and norms are staged with delivery pending.
  Fix: say so, with a matching note near `manuscript.tex:1606`.
- **F13 (editorial).** `manuscript.tex:1548`, and the existing table at 1528, head the Padua table columns λ₋/λ₊.
  Section 1 defines λ±(N,n) for Clenshaw–Curtis. Fix: use `\lamin`/`\lamax` of G^Pa.
- **F14 (editorial).** The trust statement near `manuscript.tex:1593` names Arb but not FLINT exact
  integer/rational arithmetic. Fix: name it.
- **F15 (editorial).** `manuscript-changes.md:81`. The intermediate 24-page source hash 6d28fe… belongs to a version
  that was never committed. Fix: label it scratch-only.
- **F16 (editorial).** Spaces are missing before numbers in README:113–124, the M7 record and many topic files
  ("is25", "page22"). Fix the files touched in response.

## Inventories, storage and allocations (C5): accepted

- `evidence_manifest.py` (read-only) verifies 54 small-file identities and all witness source hashes.
- Every committed JSON is under 16 KiB. The branch adds about 78 KB of generated JSON.
- `tools/cold_storage.py verify` accepts.
- The witness and norm hashes and sizes in cold-storage.json match the receipts.
- Delivery is consistently PENDING. The package bytes could not be checked because `/tmp/mz-cleanup` is absent here.
- No reserved ID is used. A live check of the ledgers at the PR21, PR24 and PR25 heads found nothing above
  T375/N137/IDEA465/LIT597, consistent with the reservation T376–391/N138–145/IDEA466–489 (first publication
  ee49035). Preparation must still recheck it.
- All three literal "old" blocks occur verbatim, exactly once, at both aff30e8 and HEAD.

**Findings.**
- **F17 (minor).** `proposed-record-changes.md:72`. The CURRENT.md old block includes the file-level line at
  `state/CURRENT.md:42` ("Updated: 2026-11-01. Owner: AC … charter … preserved below"), but the new block omits
  it. Applying the change would delete AC's owner and charter pointer. Fix: keep the line.
- **F18 (minor).** `proposed-record-changes.md:25`. The new PAPER_MAP row lists "PD-T295–299", but the manuscript
  omits PD-T296 and the row omits the cleanup records. Fix: "PD-T295, PD-T297–299", plus the final cleanup IDs at
  preparation.
- **F19 (minor, preparation).** `proposed-record-changes.md` contains no registration blocks for the five PD-T
  records or the three IDEA candidates. It also has no dated qualifiers for rows the cleanup makes stale:
  - `state/IDEAS.md:938` ("m1600 float hit stays MEASURED and uncertified");
  - `state/IDEAS.md:947`;
  - `PROOF_STATUS.md:385` (PD-T295, "no odd-m weight classification");
  - `PROOF_STATUS.md:390` (PD-T300, "m1600 … uncertified");
  - `PROOF_STATUS.md:394` (PD-N107, "no odd-m classification").

  Registry application belongs to preparation, so this does not block. The preparation step must cover these
  exact rows without rewriting their historical scope.
- **F20 (editorial).** `ALLOCATIONS.md:24` says "SHA is recorded in the draft PR". Fix: write "First publication:
  ee49035…" as other ledgers do.

## Novelty and candidate discipline: accepted, with record gaps

- The verdict "variant" for all three gated candidates is correct. None duplicates an existing IDEA, since odd m
  is explicitly OPEN in PD-T295 and PD-N105–107.
- No PD-N is proposed and REJECTED is never used.
- No priority or literature claim is made.
- The gate states its own timing qualification honestly.

**Findings.**
- **F21 (minor).** Considered routes without candidate records:
  - the handoff's sharp-localization route for matching bounds (`handoffs/01-work.md:76`,
    `attempts/C3.md:32-38`). Record it as deferred, with PD-N048 as the obstruction and a resume condition;
  - the handoff's "slope ≈ −1/9, same branch as PD-N105" interpretation. It is mis-normalized per `gates.md:13-17`
    and should get an IDEA disposition (cf. IDEA-253);
  - the literal T_(m/2)(x) odd carrier and the naive axis swap (`attempts/C2.md:19-21`). These can be aliases or
    sub-bullets of codex-03;
  - the C1 dyadic outward-enclosure certifier. Compare it with IDEA-058 and PD-T298/299; IDEA-343/344 set the
    precedent for registering such implementation variants.
- **F22 (minor).** `novelty-gate-math.md:37-87`. The records omit template fields:
  - applicable obstructions: none listed for codex-02, and PD-N048 missing for codex-04;
  - test discriminability, disposition reason and the provisional PD-T mapping;
  - closest entries IDEA-388 and IDEA-394 for the carriers, and IDEA-385/PD-T294 and IDEA-071/PD-T020 for
    codex-04;
  - a record that IDEA-395–397 were read, as handoff 01 requires.

  No verdict changes.
- **F23 (minor).** `novelty-gate-math.md:25-26`. Several logged search terms return zero hits (`growth.constant`,
  `spectral.*log`, `parity.carrier`). Synonyms that do hit were not used: carrier, normaliz, mass,
  leading.*constant. Fix: rerun with them and log the result.
- **F24 (editorial).** The gate reports 955 IDEAS lines, which is pre-merge. The gate file should note that the
  19 NN-MOP lines main later added are unrelated, and point to independent-checks-math.md:197-199.
- **F25 (editorial).** `report.md` and the results file do not point to the three IDEA candidates.

## Other

- **F26 (editorial).** `odd-weight-asymptotic.md:131-133` (optional). At odd m the nodes and weights are invariant
  under k → m+1−k, which follows from uniqueness and is confirmed numerically for m ≤ 21. So the corner (1,−1)
  limit follows immediately. The current cautious wording is correct.

## Remaining uncertainty

- The large artifact bytes of the developer's packages (159,265,962 B and 44,618,351 B) were not retrieved or
  checked. Their delivery remains PENDING.
- 17 of the 23 float rows were not rerun.
- PD-T295, PD-T101 and PD-T111 were used as accepted dependencies and not re-audited.
- The C2 and C3 proof checks are subagent reconstructions plus my spot checks, not a second line-by-line pass by
  me.
- The runtime effort of each model is not exposed.
- Readiness concerns this scope only and authorizes no merge. Only AC merges.
