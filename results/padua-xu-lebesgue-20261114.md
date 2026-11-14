# padua-xu-lebesgue-20261114: Xu-points Lebesgue conjecture and Morrow–Patterson Lebesgue function

Only the topic orchestrator writes this file. Branch `claude/padua-xu-lebesgue-20261114`, draft [PR #36](https://github.com/aacchhee/padua_research/pull/36). Provisional IDs `PD-T?padua-xu-lebesgue-20261114-claude-NN`; final IDs are assigned at PR preparation. Every PROVED claim below is **developer PROVED**: an independent Opus subagent check has confirmed it, but the formal Opus 5.5 xhigh audit is still pending.

## X1: Xu points (BCDMV 2006, Conjecture (17))

- **-01** Tensor lift: Xu interpolation is symmetrized tensor trigonometric interpolation in u = (θ₁+θ₂)/2, v = (θ₁−θ₂)/2. PROVED. [record](../topics/padua-xu-lebesgue-20261114/theory/X1-01-tensor-lift.md)
- **-02** 1-D lemma: ω_n ≤ L_n, with equality exactly at the midpoints, where L_n = (1/n)Σ cot((2k−1)π/(4n)) is the Lebesgue constant of the n zeros of T_n. Classical facts re-proved. PROVED.
- **-03** Vertex value λ^Xu_n(v) = L_n² at every non-node vertex, with all signs explicit. PROVED.
- **-04** **Exact Lebesgue constant Λ^Xu_n = L_n² for every n ≥ 1**, via the pointwise bound λ_n ≤ ω_n(u)ω_n(v). PROVED.
- **-05** **Argmax = the non-node vertices for every n ≥ 2**: all four vertices for even n, and (1,−1), (−1,1) for odd n. No finite certificates are needed. PROVED.
- **-06** Two-sided n⁻⁴ enclosure of L_n, sharpening PD-T270. PROVED.
- **-07** Expansion Λ^Xu_n = (4/π²)log²n + b log n + c + R_n, with b = (8/π²)(γ+log(8/π)), c = (4/π²)(γ+log(8/π))², and 0 < R_n < (log n + 1.55)/(18n²) for n ≥ 1. Verdict on Conj. (17), reading "≲" asymptotically: the ratio → 1, and the maximum sits exactly at the four vertices for every even n ≥ 2. The literal inequality fails at every n. PROVED.
- **-08** Edge-centre deficit L_n² − λ_n(0,1) → ≈ 0.8913. MEASURED.
- Novelty: no prior statement of -04/-05 was found in the documented search. Method precedents: BdMV 2006 (non-sharp product bound), Li–Sun–Xu 2009 (lattice derivation), Xu JAT 2012 §6.2. Coverage limits are in `literature-xu-mp.md` §5.

## X2: Morrow–Patterson points (n even)

- Literature: Λ_MP ≥ c n² is published (Beberok, JAT 311 (2025) 106191); BBDM 2026 proves O(n²).
- **-21** Corner kernel (re-derives Beberok's eq. (2)). PROVED.
- **-22** λ_n(±1,−1) = n+1. PROVED.
- **-23** Exact closed form and sign band at (±1,1). PROVED.
- **-24** λ_n(±1,1) > n+1. PROVED.
- **-25** λ_n(1,1) = c*(n+5/2)² − (n+1) + O(log²n), with explicit two-sided bounds. c* = 0.51695365336… is an explicit sinc-type integral or Si-series, with a certified enclosure. PROVED; computer-assisted parts: evidence/mp-x2-corner-arb.json.
- **-26** Λ_n > c* n² for every even n ≥ 2, strengthening Beberok's existential constant. PROVED.
- **-N29** λ(x,y) ≠ λ(−x,−y), and Λ_n is not attained at (±1,−1), for every even n ≥ 2. This answers both BBDM §7.1 open problems negatively. PROVED negative.
- **-N30** No vertex value equals (n+1)(n+2)/2 (BBDM's reported corner value). PROVED negative.
- **-27** Remainder of -25. MEASURED.
- **-28** Argmax = {(±1,1)}. OPEN (G1-MP screen n ≤ 60 supports it, gap ≈ 40%).
- **-31** First variation at (±1,1), closed form. PROVED.
- **-32** (±1,1) are strict local maxima for every even n ≤ 3000. PROVED, computer-assisted; independent rerun pending.
- **-33** Far-field localization: every maximizer lies within angle ≤ 21.5 log²(n+2)/n of the vertex lines, for every n. PROVED.
- **-34** Translation formula. PROVED tool.
- **-N35** Zero shift not maximal. MEASURED.
- G0/G1 screens and C-MP certificates: `topics/padua-xu-lebesgue-20261114/gates.md` (verdicts).

## Next step

Decision for AC: more X2 rounds (P1 tail; W1–W3 for the argmax and the sharp constant), or the audit now.
