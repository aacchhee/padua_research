# Handoff 29: answer audit-03, move the analytic onset to 512, remove PD-T271, revise both manuscripts

- Status: done in f4c6229871a494b1b859d3140e81e9eb48b6b56a
- Previous handoff: 28-claude-audit-both-manuscripts.md
- Next agent / model / effort: Codex, gpt-6-astra high coordinator. Development: Sol medium for technical work and certificate runs, Sol xhigh for ordinary mathematics. A distinct Astra high/xhigh agent does supplementary mathematical checks. Astra ultra only with a recorded written justification.
- Role: orchestrator and developer
- Branch: codex/padua-argmax-bridge-20261105
- Input head SHA: `863e6d645cdca620fc91eb5d0f35997e06bd1b78` (audit-03 outputs, MINOR fixes at `2bb805c`); this handoff is the following handoff-only commit
- Main / base: `f70a260e5b5f9a01209dc8a05faabdcf8db1feeb`
- Stage: WORK (MAJOR findings are open; the substantive audit is [audit-03](../audit-03.md))
- Written by / date: Claude. Orchestrator `claude-sonnet-5-5`; audit work by thirteen Claude Opus 5.5 subagents instructed at xhigh (see audit-03.md for the disclosure). · 2026-11-08

## Authority and AC decisions

Pushes to this working branch stay authorized. Do not push main, merge,
force-push, change tags, `.github` or settings, submit or contact anyone
externally, or mark PR 27 ready. Only AC merges. Nothing in audit-03 waives any
finding or grants readiness.

AC decided during the audit (recorded once in the [LOG](../LOG.md) entry of
2026-11-08 and [audit-03.md](../audit-03.md)):
1. **Move the analytic onset from 320 to 512.** Certify degrees 320..510 with
   the frozen engine. AC asked whether about 1 CPU-hour can run in a sandbox:
   yes. The projection is 191 degrees x 2 passes x about 8–12 s, worst case
   about 2.4 CPU-hours. Run it **in your own environment with the pinned
   runtime** (the audit sandbox cannot obtain the pinned Debian packages), or on
   Syvert if AC prefers a second location. Syvert is not required.
2. **PD-T271 is to be removed** by an elementary rational enclosure.
3. **One master notation register** for both texts (delivered).

Not yet decided by AC: the disposition of the chronology findings P1–P4;
whether paper-wide renames re-baseline `check_correspondence.py` or use the
rename-aware check (recommended, implemented and self-tested in the register);
whether to authorize the independent second-arithmetic recheck of all 560
certificates (idea I25) or a local native replay of the 276 unsampled degrees
(about 4.4k CPU-s); data deposit and DOI; funding and AI-disclosure wording.
Put these in front of AC in your reply; do not decide them yourself and do not
waive P1–P4.

## Read first

1. AGENTS.md, agents/WORKFLOW.md and agents/codex/CODEX.md at the current
   head; record the full SHA.
2. This handoff, then [audit-03.md](../audit-03.md) and
   [audit-03-manuscripts.md](../audit-03-manuscripts.md).
3. [s-streamline.md](../audit-03/s-streamline.md) (the architecture and its
   numbers), [n-notation.md](../audit-03/n-notation.md) (notation register),
   and the review reports in [audit-03/](../audit-03/) for exact locations.
4. The LOG entry dated 2026-11-08.

## Task A: onset 512 (the main analytic and computational step)

Design and numbers are in s-streamline.md sections 2.3, 3 and 4. Summary:

- **Relative gate.** The radius-one relative estimate gives
  S_n − Lambda_c <= P_n(rho) = C_4 + g + f rho − e rho^2 on rho <= 1. With the
  uniform floor 1/20 (which the tail floors already give from n = 295) the
  noncorner near region closes at 512 with margin 0.0092, and P_512(1/2) =
  −0.143, so no floors are needed on [1/2, 1].
- **Absolute gate.** G(n, rho_1) = Theta (1 − cos(rho_1/2)) − (t_0 + 2K_D)
  sin(rho_1/2) − t_0^2 cos(rho_1/2)/(2 Theta) − C̄_E − ē with Theta = T + j.
  It gives the far region at rho_1 = pi/2 (G(192, pi/2) = 0.0990 > 3/100, the
  certificates' analytic far leaf unchanged) and the outer region at
  rho_1 = 1 (G(512, 1) = 0.534). First closing degrees (base checks only):
  near gate 457, outer gate 365, far gate 189.
- **What drops:** the near column of the relative estimate, the
  radius-dependent tail floors, the annulus and its seams 3/5, 21/40, pi/4,
  the outer-geometry block, the separate far-192 derivation, the
  phase-dependent allowance statements. **What stays:** the radius-one
  relative estimate (corner-256 needs it), the scalar maximum with cusp, the
  cancellation lemma, the general central-root bound, the one-sided origin
  bound, the 3H/n correlation saving.

Steps:
1. Preregister and write the two gates and the uniform-floor lemma with their
   monotone steps in n (the audit lists them: P_n's maximum and P_n(1/2)
   decrease for real n >= 512; G(n, rho_1) increases under the tangent
   condition; F_h(n, 1/2) increases; one exact Fraction evaluation of each gate
   at its base). The gate values in s-streamline.md are Arb enclosures at base
   degrees only; the all-n steps are unwritten. They look routine but are
   unproved: treat as proof obligations, not facts.
2. Independent mathematical review of the new gates before the computation is
   treated as final.
3. Certificates for 320..510 (primary plus fresh) with the frozen hybrid engine
   (guard 41..4095, floor tiers already cover n < 512, corner-256 and far-192
   branches apply). Follow the compact-pack protocol and the preregistration
   discipline used for the 280 pairs: exact source, pins, caps, observed exits,
   no retry or rescue. Honour audit-03 PA1–PA4 dispositions in the code you
   use. Projected evidence is about 25 MB.
4. **Kill / fallback.** If a new gate fails its exact enclosure at 512, choose
   the smallest N0 >= 512 at which both gates close with positive margin
   (1024 costs about 4 CPU-hours and 90 MB) and record the failure; do not
   quietly change a constant.
5. The independent Claude replay of a random subset of the new degrees comes
   in the next audit; build the compact return so it can be retrieved by AC
   (see the size note below).

## Task B: remove PD-T271

The chain consumes only kappa > 9/10 (giving j > 23/250) and C_* < 1.8516
(giving C_infinity < 9/4); `kappa < 23/25` and the H0 upper bound have no
consumer and are to be deleted. The paper's own kappa series (uc:kappa-series)
cut at K = 3, with exact rational brackets for pi, gamma, log 2, log pi and
zeta(3), zeta(5), zeta(7), zeta(9), gives 0.91720 < kappa < 0.92151 and
C_* < 1.84802 (audit idea I26 with K = 6: kappa in (0.919677, 0.919784),
C_* in (1.846102, 1.846328); the G reviewer confirmed the consequences in exact
rationals without Arb). Commit the checker and a receipt. Then remove every
"trusted computational input to the location proof" phrase (introduction lines
103–104; Section 4 lines 555–558; G01 lines 75–77). Do **not** drop PD-T271 from the
shared records until the enclosure lemma has had a distinct review. The analytic
tail and the E12/E15 branches then have no computational dependency.

## Task C: record findings

Answer in `response-03.md`, one disposition per finding (change, decision or
reasoned dispute):
- **MAJOR (record structure): G-1** name the evaluator theorems (D23/C02/C06/N5
  for S vertex bounds, D06/C11 for actual lambda points) as premises in G01 and
  paper Section 5, or re-validate every retained key by direct finite sums;
  **F-01** split F03 sections 1–3 into a PROVED supporting record, keep the
  target OPEN, repoint H01/H04/H05/H06/H-sharp, correct "F01–F10 are not
  premises".
- **MINOR:** H-C02, H-C03 (the swapped majorant coefficients at H04:129; math
  content, so a reviewed correction), G-2 to G-5, E-01 and E-02 (verifier
  shadowing and missing checks; code, so a re-review), E-10 (cold-storage.json
  size and custody), F-03, plus the NOTEs you judge worth acting on (E-03 flag
  `--expect-plan`, E-05 wording).
- **Done by the auditor** (dated addenda, commit `2bb805c`): H-C01, X-17, E-07,
  G-6. The developer may dispute these; disputes go to AC.

## Task D: manuscripts (one coordinated pass)

Source of truth: [audit-03-manuscripts.md](../audit-03-manuscripts.md). Do this
together with Task A so the changed sections are written once. Preserve the
frozen manuscript versions (old PDFs and the freeze commits stay as they are;
build new versions into new output directories and record new identities).

1. **Notation first.** Use the register. Companion-only renames are cheap and
   keep `check_correspondence.py` passing. Paper-wide renames fail that script even
   when both texts are renamed identically (it requires the paper to be
   byte-identical to frozen commit c6e195f); that needs AC's decision. Until AC
   answers, do the companion-only renames and the section notation tables, and
   prepare the paper-wide rename map and the rename-aware check.
2. **Restructure** Section 4 and Section 5 for onset 512 per Task A:
   near and wide as one polynomial, far-192 and outer as one gate (prove far-192
   in Section 5 where only the certificates use it), one master comparison
   theorem, a shared kernel and row calculus (reflection, cotangent row
   identity, cotangent sums, psi toolkit, one quadrature lemma) so that Section
   3.1 comes from the phase-zero rows. Number the regional results and add the
   roadmap table and phase-diamond figure (P-04). Estimated 43 pages.
3. **Make the same fixes in both texts:** the Section 5.3 trust boundary and a
   formal computer-assisted proposition (P-08, C3-01, G-1, G-4, G-5); the wrong
   reason in the outer-geometry step (P-09, C3-03; the correct two-case argument
   is in E13 lines 67–74); the corner-formula derivation (C1-01); the row
   identity clause (C2B-M1); the M_infinity link (C2A-01, paper line 298);
   the endpoint identity needing the sum over sigma (C3-07) and the E_c(h,0)
   < 1/4 source (C3-08).
4. **Abstract, introduction, attribution and references:** state
   "computer-assisted" plainly (P-02); give b, c, kappa values and the earlier
   numerical fits (P-06, P-07, X-06); add Kuznetsova 1995 and Pimenova 1979
   (X-05) and the reference formatting fixes (X-01..X-04, X-08); update the
   checker's frozen-bib baseline in the same commit.
5. **Declarations:** the data/code statement must say what is deposited and
   where (P-01); the AI disclosure must include Claude Sonnet 5.5, which
   orchestrated audit-02 and audit-03 (P-13); keep funding and ORCID items for
   AC. Remove audit-history phrases (P-11).
6. **Companion pedagogy:** the four readers' MAJOR and MINOR lists (C1, C2A, C2B,
   C3 reports), then merge the duplicated compressed-plus-expanded sentences,
   add the ledger tables, the n = 320 (now 512) worked column, a tiny worked n = 2
   certificate and the proposed figures.
7. **Reviews.** After the changes: a focused re-check by a distinct agent, fresh
   builds and the correspondence check. Notify Claude for the next substantive audit,
   which must cover the changed analytic part (the onset-512 gates, the
   PD-T271 replacement and the new certificates), not wording.

## Frozen, and boundaries

- E01–E15 theory, the finite theorems and certificates for 2..319 and 511, the
  hybrid engine freeze (any engine change needs a new freeze and review), the
  compact return, all PD-N scopes, and the post-audit round counts.
- Preserve P1–P4, all audit-01..03 findings and their dispositions. No
  retrospective waiver and no backdating.
- No new degree by old technology beyond 320..510, no producer rescue, no
  Syvert pack other than the agreed one.

## Size, retention and publication

- Evidence index: 396 entries, 32,414 B (reviewed exception). Conservative
  generated bound after audit-03: 9,873,956 B against AC's 10,000,000 B cap,
  **headroom 126,044 B**. The certificates for 320..510 are about 382 proofs of
  up to about 6.4 KB each, so they cannot be committed in full: keep them in the
  compact return outside Git (as for the first 280 pairs) and commit only a small
  sample, the statistics and the preregistration. Ask AC for a cold-storage
  transfer or a cap exception if you want more in Git. Do not split evidence to
  evade the cap.
- Custody: `cold-storage.json` is over the 16 KiB per-file limit with no recorded
  exception (E-10) and the delivered-entries list is empty for the compact
  return. Put this before AC for a decision.
- Update LOG, report, results and the PR 27 sections. Final IDs and registry
  application stay deferred; refresh the live reservation union before any
  assignment. PR 27 stays a draft.
- At the session boundary commit outputs first. Then, in a separate commit, close
  this handoff as `done in <sha>` and add the next numbered handoff. Exactly one
  handoff stays open.

## Dated addendum — AC decisions of 2026-11-08 (recorded once in the LOG entry of the same date)

AC answered the five open items one by one. These supersede the "not yet
decided" list above. Handoff 29 stays the open handoff.

1. **P1–P4: accepted as recorded.** AC's disposition: process findings with no
   mathematical impact, kept permanently in the history, no remedial work. The
   records are unchanged (no waiver wording, no backdating, no deletion). P4's
   annular component also drops out of the paper with the onset-512 plan. Link
   AC's disposition from response-03 and at registry application; do not
   rewrite the original findings.
2. **Correspondence check: rename-aware now, re-baseline at the end.** Use the
   rename-aware mode (`audit-03/code/n/notation_scan.py --baseline-rev ...
   --rename-map ...`) to show the notation pass is rename-only, then freeze a new
   paper and companion baseline commit after the onset-512 restructuring and
   update `companion-paper/check_correspondence.py` to it in the same reviewed
   commit.
3. **Trust gap: both.** (a) The local native replay of the 276 unsampled archive
   primaries is done by Claude as auditor, in the audit sandbox with a non-pinned
   Ubuntu runtime (result in the LOG entry and `audit-03.md` addendum). (b) You
   build the independent second-arithmetic checker (idea I25, prototypes
   `audit-03/code/i/` `indep_S.py` and `rig_S.py`, at most 400 lines, written from
   the paper only): first on degrees 41, 199, 238, 511 with corruption controls
   (cap 60 CPU-min), then preregister the full run over all 560 certificates and
   the new 320..510 certificates. It also re-validates the vertex keys by direct
   finite sums, which would let G-1 be closed by removing the evaluator theorems
   from the trusted base instead of listing them.
4. **Data deposit: Zenodo with a DOI, created by AC.** Prepare the manifest,
   README, the data-availability sentence and the list of files (compact returns
   including the new 320..510 return, frozen engine and checker source, runtime
   manifest and package pins, preregistrations, `verify_compact.py` and the
   verification commands). AC reserves the DOI and publishes after the final
   certificates exist. Until then keep a clearly marked placeholder in the
   Declarations.
5. **AI-involvement text: AC will re-edit it later. Do not change the AI
   declaration** (the Declarations paragraph on generative AI) in this pass. The
   funding statement ("no specific grant") still needs AC's confirmation that it
   is accurate for this project; leave it as is and ask. Do not alter ORCID or
   author-contribution text.
