# C02 directed-MPFR cheap producer backend

Rules/source head4b728b04216a5490910780bc609a82b853058426. Developer Codex requested gpt-6.1-sol medium; serving metadata unexposed. Parent authorized distinct MPFR backend and bounded controls only. No candidate tree/full producer/new degree.

Reuse the old producer's binary64 interval endpoints, one-ulp outward arithmetic,128-bit directed MPFR transcendental endpoint evaluations and existing J/A board accumulation conventions. Preserve old source/header byte-identically. New header/source live only in `code/cheap_C02_mpfr/`. Fixed J32 Taylor formulas are independently implemented in C from the accepted C01 mathematical specification; no Arb implementation code is copied. Rational coefficients and remainder divisions use MPFR directed factorial/reciprocal arithmetic before outward binary64 conversion. Literal residual guards1.5 and4, exact integer turn parity, checked k<=513 and n<=512, finite global caps and paired refinement staging are mandatory. Nonfinite inputs rejected before k1 exact shortcut.

Remove old derivative's k-term harmonic fallback. A new paired ratio evaluates value+derivative together using at most four scalar trig interval calls. Both value and center board evaluations use the new pair. Each of2n(n+1) board entries evaluates four ratio pairs at its box and four at its center, plus two box sin/cos correction calls and one center cosine: at most35 scalar trig calls per entry,70n(n+1) per box. Corner constants use four ratio pairs plus one correction:34n(n+1) more calls per constant call. Each trig interval uses at most four directed MPFR endpoint evaluations plus a fixed seven-extrema check. Fixed Taylor calls use33/32-coefficient polynomials, no k loop. Preparation cost is fixed. To make the endpoint evaluator's hidden work explicit, remove the old open-addressed trig cache from the new header and call directed MPFR directly; old cached header unchanged. This is a transparent prototype choice, not a speed claim.

Lazy collection: after quadratic S accumulation, strict S_upper<downward(lc-eps) returns C_upper=S_upper and defect0. Otherwise compute orbit. Integer n>=64 plus directed-MPFR exact-dyadic endpoint-radius test<=.5 permits the reviewed all-noncorner floor1/2048; no caller boolean or true-corner descent inference. Outside that guard retain old pairlower projected scans (2n(n+1)(2n+3) pair visits). Final leaf predicates remain external and unchanged.

Prospective controls before experiments: freeze source and runner; invalid n/k/nonfinite/R1; positive/negative exact turns, exact/crossed poles, numerator zeros, broad fallback, J32 remainder/rational values; direct high-precision point samples for ratio value/derivative; same two saved n32 former failures; narrow same synthetic64/128 boxes plus full half-radius synthetic boxes; exact analytic guard equality and +1ULP rejection. Capture first failure and source snapshot, preprocessed TU, every included header, compiler/tools and runtime closure, actual loaded mappings, inputs, own/childCPU, status and commands. Total diagnosticCPU<=180 including build, own worker cap150; stop before another box if cumulative exceeds120CPU. Only MEASURED cost labels. No consequential run before distinct review and new parent release.

## First build failure preserved

Frozen first producer3c5240cc..., headerf0dc0341..., builder3f06d018..., controls e1fa88dc... failed before any mathematical assertion or box. The helper name `remainder` collided with libm, and explicit `libmpfr.so.6` was erroneously passed while compiler input language remained `-x cpp-output`; GCC parsed ELF bytes as C, producing pathological diagnostics. Compilation was stopped. First receipt records own5.859769+child105.348520CPU, wall109.046907, statusFAIL/assertions0. First files and preprocessed source remain local. This is a build failure, not a mathematical/timing result.

Fix: namespace helper `c02_remainder`, reset language with `-x none` before the library, compiler max5errors,20s per build-tool command timeout and bounded error text in future failures. Freeze changed files before rerun. New worker cap60CPU and prospective stop before a new box at40CPU; correct build should cost only a small amount, but the previous111.208289CPU counts against180. No full producer/candidate run occurred.

## Corrected frozen controls outcome

Source producer unchanged3c5240cc991162fd0b859a7de81a9f37d7d44107ebe8ec315899c0761f0feb04, corrected headere9841471f2372cc93dd6d97b79332c0501514008623f1ffa4a24c913ecf5d6df, builderdb75e288ac58c95156c54cf2a7245158c9adac56269eab33d81c60bb085f06b7 and runner6263be7b675d45111c26d8c9e49556c10fecc202e6f00ec5ffaab2dfbaa17561 were frozen before rerun.

Corrected command `python topics/padua-argmax-bridge-20261105/code/cheap_C02_mpfr/controls_v2.py` completes exit0,635finite controls/assertions, own25.707637+child.588394CPU, wall26.309877. Ratio controls sample the independent85-digit finite harmonic formula; they are control evidence, not a proof premise. Exact-half-radius and +1ULP/out-of-range guard controls, invalid inputs, R1, signed turns, broad fallback and paired nonfinite/finite-disjoint staging pass. Full source/preprocessed/header/toolchain/link/runtime/actual-loaded-map hashes are stable.

Selected-case tightness gate FAIL1of2, preserved: n32 root0/path111111011 returns S_upper11.423706806619034, defect_lower.4136264866783589, Lc_lower10.993594541096453, so S−defect<Lc is false. The second saved root2/path010101010 remains strict. No old harmonic fallback or candidate refinement was used to hide this weakness. This backend is not yet an adopted replacement producer for the saved full candidate.

| diagnostic | box CPU s | branch | strict S−defect comparison |
|---|---:|---|---|
|saved n32 first|.423771|projected scan|false|
|saved n32 second|.451808|projected scan|true|
|n64 same narrow synthetic|1.699192|lazy S|true|
|n64 full[0,.25]²|1.814119|analytic floor1/2048|false|
|n128 same narrow synthetic|7.559111|lazy S|true|
|n128 full[0,.25]²|7.687640|analytic floor1/2048|false|

The per-box ratio count is exactly16n(n+1), scalar trig count<=70n(n+1), with four directed MPFR endpoint calls per observed scalar trig call. No degree-growing harmonic sum occurs in the new value/derivative paths; projected scans still grow cubically outside skipped cases. Corner constants separately cost four ratio pairs per board entry. No unchanged-old-MPFR comparator was run; comparison to earlier Arb timings would mix different arithmetic/backends. No practical million-degree or full-cover cost claim.

Metered first-failure plus corrected-run subtotal137.504320CPU. The unusually large first diagnostic's JSON/terminal serialization happened after its ownCPU field was sampled, so that extra cost is unmetered; do not present the subtotal as exact whole executionCPU. The first failure receipt is711295590bytes of repeated compiler diagnostics, stays ignored local, and is hash-pinned in the small evidence. No further experiment is scheduled under this cap. Essential record `evidence/c02-mpfr-bounded.json` preserves both failure and changed-source outcome with source/runtime/input closure pointers. Physical archive transfer pending. Distinct source review remains required before any consequential use, and no full producer, candidate tree or new degree ran.
