# L6 actual n1 producer: prospective implementation and trace plan

Rules9825d184517db81d0aad8542fbd6639f2164b803; technical developer `/root/g3_n4`, assigned Codex gpt-6.1-sol medium, runtime metadata not independently exposed. Read accepted l6-02 contract (final metadata9d857e30), l6-01/N01 and PD-T057 exact section-map conditions. This continues saved L6-02 only. **No code execution/scientific result yet. Mandatory distinct source and exact trace-interpreter review precedes the one frozen run.** Root owns Git. Corrected data/model searches are not authorized.

## Literal implementation and interpreter

Implement only binary64 scalar Python host operations, one operator per primitive, no NumPy/BLAS/FMA. Inputs exactly ordered nodes(0,0),(1,0),(0,1), Xdiag(0,1,0), Ydiag(0,0,1). Startup sqrt(3), separate reciprocal, q0=(a,a,a). Basis(1,y,x), exact DOT row order0,1,2 and both CGS2 classical passes using the same saved v for every projection in a pass. Row subtraction uses saved coefficients/v, row accumulator begins+0; generation coefficients are sums of two pass coefficients. q1 fromYq0, q2 fromXq0; no fourth vector. FormXq1,Xq2,Yq1 with all3columns, store terminals. Hxfirstcolumn and j0 use generation coefficients, not fresh projection. Save Q and all14rawD scalars separately from completion.

Every primitive records sequential index, operation, input and output 16-hex-digit binary64 words, exact rational target (or sqrt radicand), and RN validity. Constants/stored vector states have all words, including signed zeros. Each add/sub/mul/div result is checked as exact Fraction target lying between rational midpoints of the actual result and its immediate binary64 neighbors; equality allowed only for an even low significand bit. For sqrt call actual math.sqrt, certify the exact radicand lies between the squares of nonnegative neighboring midpoints, with the same ties-even condition. Invalid rounding/nonfinite/invalid beta aborts. Subnormals and signed zeros are recorded; midpoint checks exclude silent flushing of a nonzero exact value unless it rounds correctly. This validates actual primitive results and does not assume a universal host-arithmetic theorem.

Raw trace JSON preserves all primitive words, exact rational targets, CGS passes/rows/returned coefficients and named stored vectors. A compact lossless zlib/base64 trace copy may be saved as essential evidence<16KiB. Distinct checker must reconstruct contract program flow and independently emulate RN, not import producer primitives.

## Exact completion and diagnostics

After freezing raw bytes, interpret as dyadic rationals. Compute prescribed C1 j2=(Hx*j0-h0*j0-h1*j1)/beta2 exactly; record Hy separately. Compute exact Q^TQ-I, detQ, all columns of Fx=XQ-QHx,Fy=YQ-QHy and omitted Fy e2. No extra host-rounded coefficient operation, symmetrization or repair.

Certified norm enclosures use only rational squares/integers: each vector Euclidean norm and matrix Frobenius upper bound is enclosed with outward dyadic sqrt bounds obtained by integer-square-root at192fraction bits. Matrix spectral lower bound is max column norm (or max entry); upper is Frobenius. With eta a rational Frobenius upper bound on Gram loss<1, eigenvalues of Q^TQ lie in[1-eta,1+eta], giving certified Q spectral/sigma_min bounds. Also detQ!=0 exactly certifies invertibility. Save columnwise and full residual bounds, omitted column, Gram and Q/sigma bounds. Test c64 budget using residual spectral upper<=64u*Qnorm lower for PASS; residual spectral lower>64u*Qnorm upper for FAIL; otherwise UNRESOLVED. Gram<=1/2 uses certified upper/lower analogously. Frobenius/spectral distinctions remain explicit.

Necessary exact consistency: both H matrices symmetric, beta1/beta2 positive, prescribed Hy(2,0)=0 and n1 echelon pattern, and commutator row/column0 zero. Exact asymmetry is already a necessary-condition FAIL and stops the raw exact-match branch as INCONSISTENT. If all full PD-T057 conditions pass, reconstruct all10moments by every word of length<=3, check word-content equality, mass1 and M1 positive leading minors, and verify section identities via the triangular monomial coefficient matrix [e0,Hy e0,Hx e0]. No matching/positive-model search follows; return gates. No corrected branch.

## Fixed cost and evidence

One frozen run only, external timeout60s/internal55s,512MiB address space. Raw `/tmp/padua-lanczos-frontier-l6-n1`; source/plan/contract hashes, actual command/runtime/platform and float settings frozen before run. Receipt, rawD/Q words, exact interpretation/norm/symmetry diagnostics and complete primitive trace saved; essential certificates/receipts normally<16KiB. Distinct reviewer source PASS must identify exact source/interpreter hash before launch; actual distinct trace/checker execution is required afterward. No general G, universal IEEE, Padua, changed precision/order or new mechanism claim.

## Pre-execution review, provenance and one actual run

Distinct reviewer `/root/reviewer`, requested gpt-6-astra high, inspected complete producer source and exact RN interpreter at SHA256 `d001e22e4ed8713721c6af429d5089d6c462afef60f9835e3802f79f03738be5`, and returned scoped source PASS conditional on persisting source/plan/contract/runtime/caps before the first primitive. This condition was fulfilled in a separate launcher action, before invocation: `/tmp/padua-lanczos-frontier-l6-n1/start-provenance.json` plus frozen copies. Pre-start plan4910bytes,SHA256 `46f9aca5340cd87d24ce1f76ea7a0c8f66b0b5bc9be86bd899c1bdcf292f34c7`; accepted contract13904bytes,SHA256 `9d857e30146be3e2f8963f20cf89a4441fa72b1b542a5dcb79245384198e3a35`. Actual Git head60126006dcc7c814680ed87d4fef8d9f9404a3d7. Python3.12.14 scalar binary64, float_info radix2/mant_dig53/rounds1. The reviewed producer was not changed. A catch-all INVALID_OR_CAP receipt would invalidate acceptance even with process exit0.

Actual command, run exactly once:

`timeout 60s python3 topics/padua-lanczos-frontier-20261105/code/l6_n1_producer.py --out /tmp/padua-lanczos-frontier-l6-n1/producer`

It exited0 with valid completed receipt,0.027141867seconds internal elapsed,13440KiB peakRSS. All367 primitive host results, including every actual math.sqrt, passed exact rational RN/midpoint/signed-zero checks;47named stored states are preserved. No cap/invalid beta/nonfinite/subnormal result occurred. Trace69921bytes,SHA256 `c3f9950dc198f17fde858d887bde0a4ebf61713c64145e5e4d44291c908eff5c`, has every primitive operand/output word and exact target. Lossless zlib/base64 essential trace is10383bytes. This is producer acceptance pending actual distinct trace reconstruction, not a universal IEEE implementation claim.

## Actual frozen diagnostics and stopping outcome

The saved raw14 D scalars and Q are interpreted exactly; prescribed C1 is recorded separately. Exact detQ is nonzero. Complete Fx/Fy include all3columns and the omitted Y column. Rational outward norm checks certify Gram loss<=1/2 and each complete residual<=64u||Q||. In fact the same rational enclosures give conservative explicit bounds Gram loss<=4u, ||Fx||<=u||Q||, ||Fy||<=2u||Q||. These use spectral lower/upper enclosures from column norms/Frobenius bounds and Gram-derived bounds for Q/sigma_min, not an ordinary floating SVD. All exact matrices and192-bit outward endpoints are saved.

Raw exact section data are **INCONSISTENT**. In zero-based indices, Hx01-Hx10=1/2^55, Hx02-Hx20=-1/2^54, Hx12-Hx21=1/2^54, and Hy01-Hy10=-1/2^54. An additional Hy12-Hy21 nonzero rational is saved. This necessary symmetry failure stops the exact raw match branch. The prescribed echelon/pivot gate passes; C1 gives an exactly zero commutator column0, while row0 is nonzero and the full interior condition fails. Symmetry alone already prevents any exact mass-one functional from having this interpreted pair as its orthonormal sections. No corrected data, reconstructed consistent moments, PD-T145-family match, optimizer or positive model was sought. The residual budget PASS does not supply missing consistency or imply any general reading-(G) conclusion.

Essential files, each<16KiB:

- `evidence/l6-n1-producer-receipt.json`:8101bytes,SHA256 `7c5ea62e8639a7bd0c5bb2743eb77697a0f99d56142cbca24d445d76e56b316f`.
- `evidence/l6-n1-exact-analysis.json`:6367bytes,SHA256 `d34f67ec26873e04914ccc640554330f842fe2ad8717b995a0f5b65365c19aeb`.
- `evidence/l6-n1-trace-packed.json`:10383bytes,SHA256 `81928b468a0b8a65483a438f2aec83e60c38993826b0bcac892932d06ca83b8e`.
- `evidence/l6-n1-start-provenance.json`:1886bytes,SHA256 `e6d1a410a9f0862a02b2dd9623f5159100689d3125b121772c835faec0819ef3`.

Raw output/frozen sources remain under `/tmp/padua-lanczos-frontier-l6-n1`. Distinct reviewer owns separate exact trace/checker execution/report; no independent PASS is claimed by this producer until that execution. Root owns Git/storage/shared integration. This one fixed n1 output supplies no Padua result, corrected-branch authorization, universal IEEE claim or resolution of PD-T056(G).
