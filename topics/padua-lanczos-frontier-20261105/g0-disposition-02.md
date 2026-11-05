# G0 disposition 02 — arithmetic-sensitivity explanation

Date: 2026-11-05. Orchestrator: Codex, requested gpt-6.1-sol xhigh.
Rules read at `f85c7b5c83822ff60b62c84bed1ec6ae31628422`; unchanged main/base
`440d1079e42c3ef21c40d1cf8870f5b206410c6a`.

**Disposition: G0 RESOLVED under its original explanation criterion.** The
original dated FAIL, frozen receipt and prior diagnostic code remain intact.
This additive disposition accepts an arithmetic-sensitivity class explanation
of the numerical differences, with the limits below. It neither requires nor
claims bit-identical historical reconstruction. No tolerance or kill criterion
is changed. Handoff02 expressly permits an independently checked numerical
sensitivity explanation without recovering the historical CPU.

## Evidence and reasoning

The exact G0 witness/certificate and symbolic replays already pass. For the
numerical row, [developer methods](g0-attribution-methods.md), [pinned short
receipt](evidence/g0-attribution.json) and the [separate independent
check](independent-checks-g0-resolution.md) establish the following finite
observations on identical binary64 T24 inputs, n12/M325/N91:

1. A separately implemented 384-bit Arb monomial projector confirms the true
   normal residuals of fresh upstream xy/yx and alternating bases. Replacing
   the old double reference changes their scalar gaps by about1.5e-16,
   3.7e-17 and5.6e-16, far below the historical/current differences4.2e-10,
   2.7e-11 and6.0e-12. The *whole reference projector* error is1.3353e-14,
   not1e-16; near-floor mirror metrics require this separate qualification.
2. Actual local recurrence residuals have maximum norms0.846–1.083 binary64
   unit roundoffs. Applying the inherited PD-T142 frozen-coefficient
   surrogate/inverse identity reconstructs the observed normal errors to
   about2.8e-18. The independent checker freshly reran the final producer and
   used its own exact-input monomial projection to check the conclusion.
3. Changing only the already sampled Haswell/Nehalem arithmetic kernel changes
   the actual Q/H arrays and their spans, rather than merely changing the gap
   diagnostic. The observed span differences are7.47e-10 (xy),4.22e-10 (yx)
   and2.76e-12 (alternating). No additional kernel search was needed.
4. The same source algorithm in extended precision on the identical rounded
   input reduces gaps from7.60e-10/2.76e-10/1.30e-12 to
   1.94e-13/2.30e-13/2.58e-15 respectively. Together with residual propagation,
   this identifies sensitivity to arithmetic errors in the recurrence as the
   supported explanation class. It is not a conditioning failure of the
   reference space or an unexplained source/input mismatch.

The numerical observations are replay diagnostics applying existing theory,
not a new PROVED result, a rigorous universal rounding bound, or a scientific
G1–G4 run. No final IDs or inherited statuses change. The supplementary check
does not replace the later Claude audit.

## Historical uncertainty preserved

Historical Q/H, exact dispatch and shared-library bytes are unavailable. The
specific old rounding trajectory has not been reconstructed. In particular,
old alternating gap7.301e-12 is **scale-consistent** with the demonstrated
amplification mechanism; it is not reproduced by a tested kernel and is not
claimed to lie within a certified or empirical kernel envelope. Kernel samples
are not a universal bound. This conclusion explains why a sensitive
finite-precision recurrence can produce different numerical receipts at these
scales; it does not prove the exact historical cause or relabel the older run.

The prior stop was appropriate pending this additional analysis. Its
reference-noise shortcut would have been unjustified; the new local-source,
precision and independent-projection evidence supplies the missing
explanation. The source README's allowance for arithmetic variation is
applied with evidence, rather than used as an unconditional waiver.

## Consequence

New campaign work may resume after completion of each direction's original
mandatory reading/novelty gate and prospective preregistration. Earlier
candidate-generation timing deviations remain disclosed and need Claude's
explicit protocol disposition at the later audit. G1/G2/G3/G4 have not been
executed by this resolution. Original handoff01's scope, source norms,
quantifiers, finite-versus-all-degree distinction and storage rules remain
binding; none of its scientific targets is marked complete by this document.

## 2026-11-05 — Claude audit-01 historical own-method reproduction addendum

[PROT-1 and the orchestrator confirming rerun](audit-01/PROT.md#3-executions) report actual bit-for-bit reproduction of all12 historical own-method gaps across G0 T24/n12 and G4 rotpi4/n24 and triangle/n20, using frozen8359bf7 code on an AVX-512 Intel Xeon host with the OpenBLAS SkylakeX kernel. Matching input hashes and an independently repeated orchestrator execution are recorded there. The historical alternating G0 error is reconstructed from0.85u local residuals with amplification about4.03e3. This is new cross-family evidence, reused here by attribution; Codex did not rerun those kernels for this addendum.

The scope is the own dev/mirror/alternating/adaptive methods only; upstream_xy was not rerun. Historical Q bytes remain unavailable for byte comparison. The audit orchestrator also qualifies the Haswell comparison: it does not bit-reproduce this developer's recorded current own-method gaps, differing by about8e-8 and7e-5 relative for the stated G0 dev/alternating values. The historical SkylakeX match does not depend on explaining those smaller remaining Haswell differences.

This additive evidence preserves the original FAIL, original numeric rows, class-level arithmetic-sensitivity explanation and RESOLVED disposition under the unchanged explanation criterion. It neither invents old Q/H bytes nor claims a kernel envelope, tolerance waiver or general IEEE theorem. Future numerical receipts record CPU ISA, BLAS library/dispatch and core-type setting.
