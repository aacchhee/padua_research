# Audit 01 — Claude cross-agent acceptance audit of `codex/charter-unisolvence-20261031`

- Auditor: Claude, independent auditor role (developer was Codex). Model `claude-opus-5-5` (Opus 5.5). AC requested xhigh; the session does not expose its runtime effort setting, so xhigh is the requested, not an observed, value. Reason for this depth: mathematical audit with an all-characteristic repair mechanism and a negative result, the xhigh row of `agents/claude/CLAUDE_ROLES.md`.
- Date: 2026-10-31.
- Audited commit: `eb7bdcdf3a587dd49ea9d692b1d27c7af053fe64` (branch head when this audit started). Base/rules `d36722823441dc40c6e19d69a174459348dd309c`. I read `AGENTS.md`, `agents/WORKFLOW.md` and `agents/claude/CLAUDE_ROLES.md` at the audited head. None of the three changed between base and head.
- Hashes: all 82 entries of `audit-targets.json` matched their SHA-256 values at the audited head (0 missing, 0 mismatched).
- Subagents: none. All reconstruction, code and reruns below were done by this auditor. This audit made no Git push. A local commit adding only this report, `claude-audit/` and a LOG entry is prepared for AC (see delivery note at the end).

## Reading coverage and novelty scope

Read in full: `state/IDEAS.md` (all 51 entries, the historical seed table, the contextual table, the prior-art corrections and the obstruction table), `state/CURRENT.md`, `PROOF_STATUS.md`, `PAPER_MAP.md`, `tracks/unisolvence/{README,AUDIT_LOG,NEGATIVE_RESULTS}.md`, all 13 canonical theory files under `tracks/unisolvence/theory/`, `literature/U1-COMPARISON.md`, the `cao-ghimire-wang-2022` record, `topics/charter-unisolvence-20261031/{AUDIT_HANDOFF,LOG,ALLOCATIONS,report,integration-impact}.md`, `directions/U1/candidates.md`, and the U0 replay wrapper. Partly read: `COLD_STORAGE.md` (header and manifest rows), `independent/u1/report.md` (scope and conclusions), `literature/INDEX.md` (rows used for attribution).

Novelty scope: this branch claims no novelty. I checked whether the mechanism classification is conservative enough and whether every candidate survives with a disposition. I did not run a publication-level novelty search.

External sources I opened myself:
- De Marchi–Usevich, arXiv:1311.6455 (HTML). Proposition 1 and the §4 corollary factor the Padua-like Vandermonde into axis-only univariate Vandermonde factors for distinct node sets. §4.1 says "For simplicity, we consider n even (the case n odd is similar)." This matches U1-COMPARISON.md and supports the "reformulation/corollary" classification. I did not read the paper end to end.
- Cao–Ghimire–Wang, PAMS 150 (2022), journal PDF. p. 2161: "Coupling Theorem 3.1 and (3.22) proves [7, Conjecture 3]". The uniqueness result is Theorem 4.2 on p. 2162. Nodes are real and strictly decreasing (p. 2153). This confirms the HS Conjecture 3 correction and its locators in `LIT-033`. In the arXiv version (2107.06380) the uniqueness theorem is numbered 4.1, so the records' choice to cite the journal version is right.

## Independent reconstruction of each claim

For each proof I rebuilt the argument myself before relying on any checker output.

**PD-T001 (char ≠ 2, PROVED).** Write ε_{ij} = (-1)^{i+j}.
- The two parity sums G_0 and G_1 add up to the full alternation product sum, and their difference is the ordinary barycentric product sum. The ordinary sum kills x^a y^b unless a ≥ m and b ≥ m+1, which forces a+b ≥ 2m+1. So G_0 = G_1 = G/2 on Π_m × Π_m, and this is the only place 2 is inverted.
- Tensor Gram determinant: the norm of degree a occurs m−a+1 times. Each Δ_r for r = 1..m comes from +(m−r+2) at a = r−1 and −(m−r+1) at a = r, so its exponent is 1. Δ_{m+1} has exponent 1. The same holds for Y. This gives ∏_{r=1}^{m+1} Δ_r(X)Δ_r(Y).
- Generic-moment polynomial argument: correct.
- Δ_L(H) = 1 because ∏ω′ = (−1)^{L(L−1)/2} Vand² and ∏(−1)^i = (−1)^{L(L−1)/2}.
- The cutoff 1..L−1 on both axes, with Δ_{m+1}(X) automatically 1, gives exactly the stated iff.
- No gaps found.

**PD-N001 (PROVED negative; IDEA-001 REJECTED: refuted).**
- I recomputed both F4 determinants by hand. In columns (1,x,y): S_0 = {(0,0),(0,a),(1,1)} has determinant −a = a, and S_1 = {(0,1),(1,0),(1,a)} has determinant a. In characteristic 2, Δ_1(X) = Σ1/ω′ = 0.
- The argument that every m = 1 board is unisolvent over any field with |K| ≥ 3 is correct. So is the scope statement: only necessity fails. Original sufficiency is vacuous in characteristic 2 because Δ_1(Y) = 0 whenever |Y| ≥ 2, and it is true elsewhere by PD-T001.
- The m = 2 example over F8 = F2[a]/(a³+a+1) is unisolvent for both parities in my own field implementation. My exp/log tables happen to use the other primitive cubic, x³+x²+1, so the checker tests the example for **each** of the three roots of a³+a+1 inside its F8. All three pass, and the F8, m = 2 exhaustive run below contains these labellings in any case.
- The negative statement is scoped correctly: no family-wide rejection, and the corrected criterion is untouched.

**PD-T002 (all characteristics, PROVED).**
- Complementary minors: in the I and J Cauchy–Binet summands the sign exponents add to L(L−1)/2 + L(L−1)/2 = L(L−1), which is even. So Δ_{L−r} = Δ_r holds as an identity in ℤ[nodes, 1/differences]. The developer's bookkeeping, L(L−1)/2 + Σi − r(r−1), is also even, so it agrees.
- Δ_r = 2^r H_r for r ≤ ⌊L/2⌋, because the entries have degree ≤ 2r−2 ≤ L−2.
- Products: for L = 2k I get 2^{k²} A ∏_{r<k} H_r², and for L = 2k+1 I get 2^{k(k+1)} ∏_{r≤k} H_r². The terminal odd-axis minor is H_k = (−1)^k Vand(odd)² ∏_{odd} 1/ω′ ≠ 0, since B_even = −B_odd up to degree 2k−2.
- The power of 2 matches N in both cases. For m = 2a: a(a+1) + (a+1)² = (a+1)(2a+1). For m = 2a+1: (a+1)² + (a+1)(a+2) = (a+1)(2a+3).
- Every factor in (2) lies in the localized ring R. The char-0 equality therefore holds in R and specializes to any field where the within-axis differences are nonzero. Cross-axis coincidences are harmless because no cross-axis denominator ever appears.
- The ranges ⌊(L−2)/2⌋ are exactly what is left after dropping A_E and the odd-axis H_k. No gaps found.

**PD-T003 (PROVED).**
- Because V^T W V = D/2 with D diagonal and invertible, V^{-1} = 2D^{-1}V^T W, so 2VD^{-1}V^T W = I. Its z-th column is ℓ_z.
- The norm hypotheses are exactly the PD-T001 criterion: Δ_1..Δ_m on X (Δ_{m+1}(X) = 1) and Δ_1..Δ_{m+1} on Y.
- The cubature statement needs no quasi-definiteness. Its scope (a discrete product functional, char ≠ 2) is stated correctly.

**PD-T004 (PROVED).**
- The endpoint-halved sum is half the full cyclic sum, so A_m(r) = [2m | r].
- Since ρ^m = −1, (−1)^j T_r(c_j) = T_{r+m}(c_j).
- Expanding the checkerboard indicator gives the two-term moment formula. For a+b ≤ 2n+1 the only surviving moments are (0,0), (2n,0) and (n,n+1). This includes n = 1, where (1,2) and (2,0) survive.
- In the Gram matrix only (0,0) and (2n,0) are reachable at total index ≤ 2n. Hence D_{(n,0)} = 1, and the diagonal entries are c_a c_b otherwise.
- Distinctness, the cardinality count and the basis change are correct.

**PD-T005 (PROVED).**
- Frobenius fixes c exactly when ρ^q ∈ {ρ, ρ^{−1}}. Index-one nodes occur on both axes, since j = k = 1 is an even pair.
- The intrinsic (u,v) description gives independence from the choice of root.
- I recomputed the CRT table: 2n+1 ≡ 1 (mod 2n) and ≡ −1 (mod 2n+2); 2n²−1 ≡ −1 (mod 2n) and ≡ 1 (mod 2n+2). The n = 1 collapse is correct.
- The bound q ≥ 2n+1 holds, and at equality the characteristic is good.

**PD-T006 (PROVED).**
- det D = 2^{1−n(n+1)}.
- Boundary count: there are exactly two even corners, (0,0) and whichever of (0,n+1), (n,0) is even. The 2n+3 incidences give 2n+1 distinct boundary nodes. I checked both parities of n.
- This gives det W = 2^{N−2n−3}[n(n+1)]^{−N} and det V² = 2^{4+n−n²−N}[n(n+1)]^N.
- The Dickson basis change contributes 2^{−n(n+1)}. The final exponent is (n²+3n+6)/2. Hand check at n = 1: the determinant is −16, its square is 256 = 2^5·2^3.
- The integral-reduction corollary follows because the identity holds among algebraic integers.

**PD-T007 (PROVED).**
- Split and nonsplit trace images, X ∪ Y = F_q and X ∩ Y = {±1}, are correct.
- 2(x+1) = (u+1)²/u. For v in the norm-one group U, (v+1)^{q−1} = v^{−1}, which gives χ(2(y+1)) = v^{(q+1)/2}.
- At v = −1 the endpoint sign is −χ(−1). The count (q+1)(q+3)/8 is correct.

**PD-T008 (PROVED).**
- The diagonal Gram matrix gives the weighted dual, and dimensions add up.
- The lower bound comes from the multiplication map P_{n−k} → C supported on supp(f). It is correct, and as the file notes it is generic to any unisolvent set.

**PD-T012 (PROVED).**
- Bound 1: through any point of PG(2,7) there are only 8 lines, so there is no 10-arc.
- Bound 2: assume d ≥ 5. Then every 6 columns are independent, so the dual is a [10,4,7] MDS code. Shortening it gives a [9,3,7] code, i.e. a 9-arc. That arc has no tangent lines, so an external point forces |A| to be even, which is a contradiction.
- Both proofs are elementary and complete for linear codes. They are correctly separated from the MEASURED attainment results.

**PD-T009 / PD-T010 (MEASURED)** and **PD-T011 (OPEN).** The status labels are correct. No finite run is treated as a proof. PD-T011's two OPEN parts are both OPEN, so keeping them in one file does not violate the split rule. Every substantive PROVED claim has its own ID, and no weakest-part relabelling occurs.

**Status classification:** I agree with all 13 epistemic statuses and with every disposition in `PROOF_STATUS.md` and `state/IDEAS.md`. Ten records are PROVED (nine PD-T and one PD-N), two are MEASURED and one is OPEN. The "reformulation/direct corollary" classification of the U1 mechanism is suitably conservative given De Marchi–Usevich 2014. All source candidates and failed routes survive with dispositions: the superseded kernel route, the aborted rational expansion, U1d consolidated into U1c, and the deferred U2/U3 items.

## Commands I executed

Run from the repository root at `eb7bdcd` with Python 3.13.18, NumPy 2.3.5, SymPy 1.14.0 and mpmath (the SymPy dependency). The developer recorded Python 3.12.14, so my reruns are cross-version replays. Outputs went to my session scratch directory. The small JSON outputs are committed under `claude-audit/outputs/`.

1. Developer and Astra checkers, all exit code 0:
   - `python3 topics/charter-unisolvence-20261031/directions/U1/exact_checker.py --samples 20 --output …/u1-fields.json` returned `all_assertions: PASS` (3.1 s). Output sha256 `d9b9aa4c…86205f`.
   - `python3 …/directions/U1/exact_checker.py --symbolic --output …/u1-symbolic.json` returned `PASS` (2.1 s). Output sha256 `89b60021…26d5678`.
   - `python3 …/independent/u1/check_u1.py` returned `PASS axis pairs 9336 checkerboards 18672` (5.6 s).
   - `python3 -I …/directions/U0/verify_exact.py` passed and reproduced all eight PD-T010 distances and message counts (1.1 s).
   - `python3 …/independent/u0/exact_check.py` returned `ALL INDEPENDENT EXACT CHECKS PASSED` (1.5 s).
2. Source replay: I copied the committed `input-code/ff_padua/*.py` to a fresh off-repo directory and ran `python3 -I …/directions/U0/replay_source.py SRC OUT`. All six children exited 0 with their markers present (44 s).
   - Five of the six child logs are **byte-identical** to the developer's cold-storage hashes in `COLD_STORAGE.md`: `padua_ff.log edd514e2…`, `quadratic_padua.log 3dbc20f0…`, `discriminant_real.log e5921882…`, `hs_ff.log 0e07fc5f…`, `padua_codes.log a8b2da53…`.
   - `fast_transform.log` differs only because it contains timings.
   - The PD-T009 counts check out: 76 `padua_ff` cases all OK; the (3,13) rationality pattern `[True,False,True,False,True]`; 46 transform comparisons plus 9 benchmark round trips; 13 quadratic primes; maximum log-determinant discrepancy 4.3e-16.
3. Input provenance, checked against **AC's own local copy**: I staged `C:\Users\andreyac\Downloads\padua\padua_unisolvence_inputs.zip` from AC's machine. Its SHA-256 is `0ea3f395…cb20d1f`, which equals the LOG value, and all 17/17 internal SHA256SUMS match. All nine `input-code/` files are byte-identical both to `IDENTITY.json` and to the corresponding members of AC's ZIP.
4. My own checkers, written from the theorem statements before I read any developer checker code. They import nothing from the developer or the source. They use their own exact GF(p^k) arithmetic, with exp/log tables over primitive polynomials found by search.
   - `python3 -I topics/charter-unisolvence-20261031/claude-audit/check_checkerboard.py OUT` returned **ALL PASS on 1,566,000 boards** (2 min). Checker sha256 `67f0e797…af420ec`; output `outputs/checkerboard.json` sha256 `2d23b292…f065b`. Coverage:
     - Exhaustive over **all** labelled axis pairs, including cross-axis coincidences: F2, F3, F4 at m = 0; F4, F3, F5 at m = 1; F4, F5, F7, **F8** at m = 2 (F8 alone gives 1,128,960 boards); F5 at m = 3.
     - Seeded samples (seed 20261031) over F9, F8, F16, F25, F7, F11, F13, F32 and F27 for m ≤ 6.
     - Asserted on every board: PD-T002 identity (2) and its iff; PD-T001 identity (1) and its iff when char ≠ 2; Δ_{L−r} = Δ_r; Δ_L = 1; A_E = H_k(E) ≠ 0; the terminal odd-axis H_k ≠ 0; and that both parities agree.
     - PD-T003 cardinality ℓ_z(z′) = δ was checked exactly on 8,784 boards in odd characteristic.
     - Zero failures of "original sufficiency" were seen. The exhaustive runs include 311,904 singular boards (320,996 including the samples), so both directions of each iff were exercised.
   - `python3 -I topics/charter-unisolvence-20261031/claude-audit/check_padua.py OUT` returned **ALL PASS** (43 s). Checker sha256 `1bb4ebf5…7e4cc` with `gf.py` `ca0d134a…f14e4`; output `outputs/padua.json` sha256 `2e7ba470…c146`. It works inside F_{q²} for 18 odd prime powers q from 3 to 49, including 9, 25, 27 and 49:
     - **PD-T005** rationality iff on 81 (q,n) cases (60 rational, 21 not), and the residue table on every rational case.
     - **PD-T004** moment identity on 71 cases and the full Gram identity on 67 cases with n ≤ 8.
     - **PD-T006** squared Dickson determinant over F_q on 67 cases.
     - **PD-T006** bad-prime reduction: 17 (p,n) cases with p ∈ {2,3,5,7} and p | 2n(n+1), reducing a primitive lcm-root to a primitive p′-part root. All 17 matrices are singular, as stated.
     - **PD-T006** in characteristic 0 for n = 1..10 with mpmath at 120 digits: relative error below 2e-118.
     - **PD-T007** character description equals the canonical set for all 18 values q = 2n+1 ∈ {3,…,49}.
     - **PD-T008** weighted dual orthogonality and rank for every k on 12 (q,n) cases, including q = 9, 25.
     - Exact minimum distances by full projective enumeration. These reproduce **all eight PD-T010 rows** (7/4, 17/13, 23/18, 39/33) with an implementation built differently from the developer's: roots in F_{q²} rather than a character construction, in the monomial basis. They add new measured rows for q = 5, 9, 11, 13 and q = 25 at k ≤ 1.
     - PG(2,7) maximal arc size is 8 by exhaustive search after fixing a frame. This supports, but is not needed for, PD-T012.

## Findings

No Critical or Major findings. I found no mathematical error, missing hypothesis, quantifier defect, status misclassification or attribution overreach.

**A1 — Minor, protocol, a readiness condition.** A multi-PR batch now exists but this branch does not record it.
- Where: `topics/charter-unisolvence-20261031/ALLOCATIONS.md` says "No batch integration or squash rehearsal is applicable (one PR only)", and `ID_CROSSWALK.md` links only the standalone ledger.
- What changed: `topics/padua-batch-20261031/ALLOCATIONS.md` exists at `claude/programme-ideas-20261031@8f500db`. It lists this branch as the first block (PD-T001–012, PD-N001, LIT-001–041, IDEA-001–051) and proposes integrating it first.
- Why it matters: `codex/mz-constants-20261031@33bf9e6` and `claude/bivariate-lanczos-20261031@2d8c3ab` both modify `state/IDEAS.md` from the same base, so a textual conflict is certain. Those branches use only provisional IDs today, so there is **no ID collision**.
- Required response: link the batch ledger from `ID_CROSSWALK.md` and this topic's LOG and PR. Replace the stale "one PR only" sentence with the integration order recorded in the batch ledger. State whether the sequential squash rehearsal is deferred to the later members, which is acceptable if this PR integrates first.
- Caveat: I could not query the GitHub PR list, because API access for this repository is not enabled in my session.

**A2 — Minor, editorial.** Several canonical theory files still describe hand-offs that have since been completed.
- `code-structure.md` (PD-T008), Scope: "…`PD-T012`, in `independent/u0/code-optimality-bounds.md`; integrating and accepting that bound is the orchestrator's handoff." That path is no longer canonical.
- `code-distances.md` (PD-T010), Checks: "Integration of its report/hashes is the orchestrator's audit step… The complete bound proof is handed off for a separate durable result."
- `measurements.md` (PD-T009), Scope: "its exact report and hashes must be integrated before acceptance."
- `open-targets.md` (PD-T011): "…bound is handed separately to the orchestrator."
- `code-optimality-bounds.md` (PD-T012) header: "The provisional result ID is assigned here at the orchestrator’s explicit request."

These are non-mathematical. Please point them to the integrated records (PD-T012 and AUDIT_LOG), and list the replacements in `integration-impact.json` as was done for the earlier editorial changes. This is not a material change and does not require re-audit.

**A3 — Minor, evidence archival, an open item for AC.**
- AC's chosen destination `C:\Users\andreyac\Downloads\padua\cold_storage\charter-unisolvence-20261031\` did **not exist** when I listed `Downloads\padua` at 2026-10-31 20:56 UTC.
- The handoff ZIP (`fdcc1ce2…`, 210015 bytes) and the full outputs exist only under the developer's cloud `/workspace/padua-cold/`, which I cannot reach and which may be ephemeral.
- `COLD_STORAGE.md` correctly labels Windows delivery as pending, so this is not a misstatement.
- Mitigation: reruns 1, 2 and 4 show the evidence regenerates from committed code. Five source logs reproduce byte-for-byte, and no proof depends on the cold bytes.
- Required response: the developer delivers the ZIP to AC (or AC retrieves it), runs `verify_cold_storage.py` on the Windows copy, and records the receipt. My own audit outputs and checker are placed in that destination under `claude-audit-01/` together with a manifest.

**A4 — Informational.**
- My reruns used Python 3.13.18 rather than the developer's 3.12.14. All results agreed, with byte-identical deterministic logs.
- The developer's U1 exact checker reports `original_iff_mismatches` for characteristic-2 sample fields. That is the expected PD-N001 phenomenon, not a failure.

## MEASURED side observations (not registered; for possible U3 follow-up)

These are finite exhaustive counts. They are not claims.
- Fraction of singular labelled boards: F5 m=2: 4800/14400 = 1/3. F7 m=2: 70560/352800 = 1/5. F8 m=2: 225792/1128960 = 1/5. F5 m=3: 9600/28800 = 1/3. F4 m=2: all 1152 boards are singular.
- The F4 case is simple. Y must then be all of F4, so ω′_Y ≡ 1 and H_1(Y) = 1+1 = 0. More generally, when Y = F_q, H_1(Y) = −⌈q/2⌉ in F_q.
- These are concrete data for IDEA-016 (exact counts of unisolvent labellings). IDEA-016 remains deferred, and I do not propose a formula.
- For q ≠ 2n+1 the measured distances also exceed the PD-T008 lower bound, for example (q,n,k) = (7,2,1), (11,2,1) and (13,2,1) all give d = 4 against a bound of 3.

## Verdict and stage

- **Mathematics: ACCEPTED** for the stated scope. All 13 epistemic statuses, the PD-N001 negative scope, the REJECTED: refuted disposition of IDEA-001, the split structure, and the conservative mechanism and attribution classification are confirmed.
- **Protocol: three Minor findings** (A1–A3). Under the workflow, any findings set **Stage WORK**.
- The developer answers in `response-01.md` without editing this report.
- A1 and A2 are editorial or registry-link fixes that change no claim, proof, code or evidence. A3 is a delivery step. If the responses stay within that scope, they may proceed to PR without a fresh audit ("unchanged claim with a documented resolution"). Any change to statements, proofs, checkers or statuses returns to AUDIT.
- This readiness assessment covers the stated scope only. It does not authorize a merge; only AC merges.

## Residual uncertainty

- **Publication-level overlap.** The exact barycentric-Hankel all-characteristic statement may already be in print. The Floater 2017 journal text and full Camargo–De Marchi 2015 remain unread. This audit relies on the branch making no novelty claim; it does not establish novelty.
- **Finite checks support but do not prove.** My finite checks support the proofs but are not proofs. The universal claims rest on the hand-verified arguments above.
- **Stale GitHub view.** My view of GitHub state is limited to branch heads fetched at about 21:00 UTC. I had no PR API access.
- **Python version.** I did not rerun under Python 3.12.14 itself.

Next: `Codex (gpt-6.1-sol medium): Continue codex/charter-unisolvence-20261031 — answer audit-01 in response-01.md (A1 batch-ledger link and integration order, A2 stale hand-off prose, A3 cold-storage delivery receipt), then prepare the PR.`
