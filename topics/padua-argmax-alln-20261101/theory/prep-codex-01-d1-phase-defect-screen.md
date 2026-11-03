# PD-T232 (PD-T?argmax-alln-prep-codex-01) — Finite two-phase primitive and pairwise-defect screen

Final registration: **PD-T232**, 2026-11-03. The provisional identifier in the title remains an alias; mathematical statement and historical evidence are unchanged.

ID kind: PD-T.
Aliases: D1 round1 screen; full odd-board phase/defect samples.
Split from: the numerical claims in gated/d1/r01-screen.md (no original all-degree theorem is narrowed).
Split into: none.

## Statement

At n=16,32,64,128,256 the preregistered float64 screen evaluated, per degree,145global phase points,26near-zero points,117compact-coset points and48moving-strip points. Every registered finite kill flag was false. The largest normalized primitive remainder `(S-a*Lambda_c)/log(n+1)` decreases over the five degrees from1.5993457963 to1.4462486836. The compact minimum defect over all near phases decreases from1.8419070561 to1.7119286753. The finer h=1/n grid has a positive primitive excess at every tested degree, including0.0000176177240 at n256; this is a sampled value, not an enclosed supremum or an asymptotic assertion.

## Definitions

Use m=n+1 and full periodic odd mesh0<=j<2n,0<=r<2m,j+r odd. S=(2nm)^(-1)sum|G_n|,a=(cos(alpha)+cos(beta))/2,Delta=S-lambda, and the four-copy pairwise defects Qv,Qh are exactly those in [r01-screen](../gated/d1/r01-screen.md). Global phases are(i*pi/8,j*pi/8),|i|+|j|<=8. Each local diamond uses h=1/log(n+1)^2 or1/n with(i*h/2,j*h/2),|i|+|j|<=2. Compact macro coordinates lie in{pi/4,pi/2,3pi/4}² and round to nearest odd cosets with the recorded lexicographic rule; moving strips use widths k/n,k=1,2,4,8 on all four sides with three tangential ordinates.

## Assumptions

NumPy/SciPy float64, finite deterministic grids and no outward rounding; the screen uses no local optimizer or random sample. Validation at n2,3,4,8,16 compares independently expressed formulas but is not a rigorous error enclosure.

## Status by part

Overall status: **MEASURED**.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Finite phase, compact and strip observations | MEASURED | Fixed5-degree grids only |
| Finite kill flags all false | MEASURED | Planning rules only; no all-n consequence |

Candidate / claim disposition: none; this is a finite evidence record.

## Depends on

PD-T101 corrected-kernel conventions; the primitives and projected defects whose analytic claims are separate gated-codex-01/02/03 records. No measured screen is a premise of those analytic proofs.

## Checks

Original command: `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-argmax-alln-20261101/code/gated/d1_screen_r01.py <scratch>/d1_screen_r01.json`. Frozen producer SHA256`b8003e252d62147b19f1bc02116fe84434672c5cfdb91cd1cc835f9ba5d339e4`. The separately executed Astra xhigh [round1 check](../gated/checks/d1-r01.md) compares all20,997numeric and1,062other leaves exactly in that environment, excluding argv,timings and the disclosed completion-note hash change. Its [receipt](../outputs/gated/check_d1_r01_receipt.json),SHA256`0063d9e6db39d0f75fb4df792b4e4ac0e3d440ad8ae6875685da4d7becac391d`, records dependencies,versions and commands. This preparation only inspected those records; it did not rerun the screen.

## Sources

No external theorem, literature priority or new mechanism is claimed.
This is the durable rehoming required by audit-01 F11 and accepted
response-review-01, not a new scientific run.

## Proof or evidence

Claude [audit-01](../audit-01.md) accepted the numerical claims at their recorded finite scopes; its F11 requested these durable homes. Historical payloads are pinned at source `1cecd68ac0a64b01ed7b2d262b6263a955a7d4d7` in [cold-storage.json](../cold-storage.json); retrieval is byte-exact, and the active integrity manifest must never be overwritten. Raw860,021B payload SHA256`15c9d29a3d2b166ee54dc8a91fe7bff4c117cc85dc99184fa7bc7640a888e9ef`; archived gzip81,843B SHA256`8b57766f8e0251cc6bbd2b772888846ba475f0c01025e17cdf124a90d6c0fc1d`. At n256 the compact minimum Qv=.5511542427,Qh=.9968386231. Moving-strip minima Delta increase from.6218790475 to.8212807013; those strips do not exhaust a continuum. Formula-validation maximum absolute error is5.329070518200751e-15, and periodic-S/four-copy discrepancy across production samples is4.263256414560601e-13.

## Scope

Only these finite observations and planning flags. No uniform defect bound,phase-supremum estimate,limit law,effective threshold or all-degree argmax theorem follows.

## Open items

The relevant analytic theorems have their own accepted PROVED records. PD-T099 and its unknown finite bridge remain OPEN; no extra scan is requested by this rehoming.

## History

2026-11-03, Codex gpt-6.1-sol high (configured; serving metadata not
independently exposed), preparation input `cdb12257af24ea2542de707b9730f8278d69a168`.
Created from the already recorded finite observations and independent
checks cited above. No new measurement, criterion, bound or source output
was produced; no historical evidence was split or recommitted. This
record separates the measured claim from supporting PROVED theory and
from unresolved all-degree targets.
