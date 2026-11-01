# P3–P5 and IDEA-03 pairing: scoped followup

Rules/input source: `328be35e55143013047ec03a70e9906e82b95353` (read-only source snapshot; no local `.git`). Codex mathematical developer, parent-assigned model gpt-6.1-sol xhigh; actual runtime metadata not independently exposed. 2026-11-01. Status: WORK; no all-degree proof.

## Before running: operationalizations of IDEA-03

The original wording, retained without amendment, is: **“Do the cell-wise local maxima decrease monotonically along rhombus directions away from the non-node corners?”** Its kill criterion is **“kill if any certified n ≤ 7 list violates the ordering in a way no pairing could respect (to be made precise when the lists are read).”** Neither the cells, direction, pairing map nor corner-selection rule was specified. The later plan's centreward edge comparison is a different claim. We keep them separate.

Use mesh coordinates q=(nθ/π,(n+1)φ/π), Q=[0,n]×[0,n+1]. The antinode centers A are integer (j,k) with j+k odd. Define diamond cells D_a={q∈Q: |q1−j|+|q2−k|≤1}. They tile Q up to boundaries. Rhombus neighbor steps are e∈{(1,1),(1,−1),(−1,1),(−1,−1)}. The non-node corners C are the corners of Q with odd index sum.

**O-R (one precise original-direction reading).** Let M_a=sup_{D_a} λ_n. If c∈C is the unique closest corner to both a and b=a+e in Euclidean mesh distance and |b−c|>|a−c|, ask M_b≤M_a. The exact domain and metric matter; this is an operationalization, not a claim that the ambiguous original necessarily meant it. A numerical violation kills pursuit of this universal formulation as a measured screen. A certified kill requires a lower bound for M_b and an upper bound for M_a on the entire diamond, including its artificial boundaries. A complete list of local maxima of λ on Q alone does not provide that upper bound.

**O-L (certified-list screen).** For each D_a, group only strict interior local maxima from the certified list and take their greatest value V_a; leave an empty group undefined. Test V_b≤V_a on the same directed neighbor graph. This is a necessary empirical screen for a proposed pairing of those selected cellwise local maxima, not equivalent to O-R. Coordinate assignment must be certified. Fractional coordinate midpoint assignment alone remains MEASURED. Any exact O-L witness refutes only O-L, not every possible rhombus partition or pairing map.

**E-C (amended centreward edge comparison).** On each vertical edge with complementary integer center k (j+k odd), let E_k=sup_{[k−1,k+1]∩[0,n+1]}λ_n. Exclude cells meeting either endpoint. If |k'−(n+1)/2|<|k−(n+1)/2| and k'=k±2, ask E_k≤E_k'. This is the centreward version suggested by the later edge profile, with a two-mesh translation preserving parity. It does not assert original O-R.

**E-P (strong pointwise version).** Replace the edge-cell suprema by λ_n(j,t)≤λ_n(j,t±2), for every mesh t in the source edge cell and the sign directed toward the centre. This is stronger than E-C. A single exact algebraic-angle violation refutes E-P only; an optimized-cell violation is needed against E-C.

Pre-run kill thresholds for float64 screens: a reported reversed difference >10^−6 is a measured violation; smaller differences are unresolved. Use the established kernel evaluator, validate against the coefficient-matrix evaluator, retain positions and optimizer limitations. Test n=4 certified inputs first, then degrees ≤50 as budget permits. Do not rewrite original pre-registration after observing results.

## Gate and source access

This follows existing IDEA?argmax-alln-claude-03, not a new mechanism or novelty claim. Read rules, role, topic plan v2/history, ideas/gate/handoff02; registry headings/aliases and obstruction/disposition rows; IDEA-048/206/303–305 and their part2 route records. The closest comparison is IDEA-305's phase/gain/defect assembly; an exact pairing would remove its effective-asymptotic remainder obligation. Existing majorant failure remains applicable: S alone may exceed Λ_c. The candidate distinction is an exact comparison of λ or a defect-compensated inequality, and disappears for a chosen ordering if that ordering fails. No claim of exhaustive originality.

The literature INDEX was inspected. The original Brutman 1978, Günttner, Brutman 1997 and trigonometric midpoint-maximality sources were not accessed in this bounded followup. No 1-D technique is transferred or attributed as established. P3 technique development that depends on them remains deferred until primary reading with locators.

### Added after initial O-L grouping, before tie-inclusive comparison

The n=4 certified-list grouping leaves zero eligible O-L comparisons under the **unique** closest-corner convention: the interior neighbors land on the corner Voronoi tie line. Thus O-L is untested there. Define **O-Lt** separately by replacing “unique closest corner” by “c is a closest corner to both a and b,” allowing ties. Keep every other rule unchanged. This tests the natural extension to the cut locus; a failure does not refute tie-excluding O-L or O-R. Its pre-run exact kill is max(lower value in b)>max(upper value in a), with certified rational coordinate assignment and inherited strict-max certificates.

## P3–P5: precise obligations retained after T2/T3/T4

The parent reports T2's raw O(1) interior-profile convergence kill (32/81 gaps change by >0.05 from n64 to128), T3's raw scaled-angle profile growth, and T4's literal-bound projection n0≈1.33×10^14. These kill those tested formulations. They do not disprove positive gaps, corner dominance or an exact comparison. The following is a conditional reduction, not an all-n proof or an unrun experiment.

Fix δ∈(0,π/4). Write angle-square Qθ=[0,π]^2 and let d1=min(θ,π−θ), d2=min(φ,π−φ). Use the closed cover:

- Corner regions Cδ={d1≤δ,d2≤δ} (four squares).
- Interior Iδ={d1≥δ,d2≥δ}.
- Vertical strips Vδ={d1≤δ,d2≥δ}; horizontal strips Hδ={d2≤δ,d1≥δ}.

There is no omitted transition region; overlaps only help. In the reflected-lattice identity let S be the primitive shifted-lattice absolute sum and Δ=S−λ_n≥0. Reindexing by lattice reflections shows the averaged four-copy majorant equals this same S. This finite reindexing and the triangle inequality provide no upper bound Λ_c by themselves.

**P3 obligation.** Produce explicit N3,δ and, for each corner c, a nonnegative function h_n,c on its square with h_n,c(q)>0 except at a non-node corner q=c, such that

    Δ_n(q) − [S_n(q)−Λ_c(n)] ≥ h_n,c(q),   n≥N3.

For node corners strict positivity is required everywhere in that square. A local physical-coordinate certificate and an annular estimate can split this into two tasks: choose explicit r_n≤δ; prove the inequality on |q−c|≤r_n, and prove a positive lower bound on r_n≤|q−c|≤√2δ. One must track r_n and cover every n≥N3; fixed-n Hessian or cusp data without a uniform radius are insufficient. T3 shows the raw scaled-angle O(1) limit cannot be the announced certificate.

A finite-n caution about the expected cusp: every cardinal L_B is a polynomial in physical x,y. The reverse triangle inequality gives |λ_n(x,y)−λ_n(c)|≤K_n(|x−c_x|+|y−c_y|) locally. As x=cosθ, near a corner this is O_n(|θ−θ_c|²+|φ−φ_c|²). Thus λ itself has no nonzero first-order angular cusp at a fixed n. S and Δ may each have angular cusps which cancel in S−Δ. Uniform n-scaling is a separate question. This elementary observation is not a strict-maximum proof, and does not replace a P3 sign estimate.

**P4 obligation after T2.** A limit for the raw gap at every fixed sampled phase is unnecessary. It suffices to find a phase neighborhood U_n of the odd coset in one primitive lattice cell, explicit N4 and d>0 such that, uniformly over Iδ:

    outside U_n: S_n≤Λ_c−d;
    inside U_n:  S_n≤Λ_c+ε_n and Δ_n≥2d, with ε_n≤d.

Then λ_n≤Λ_c−d on Iδ. The phase-localization inequality outside U_n and the defect lower bound inside U_n are OPEN; PD-T189/190/191 establish their edge analogues only. An n-dependent or growing defect is allowed. This escapes T2's rejected n-independent raw profile but is an implementation variant of IDEA-305, without a novelty claim. A numerical positive minimum does not certify uniformity over position or phase.

**P5 obligation.** For Vδ and Hδ, either establish the same two-part phase/defect inequalities with a strip-specific d>0, or construct an explicit map F_n from each strip to its adjacent edge with λ_n(q)≤λ_n(F_n(q)) and preserve strictness/equality information. F_n must be defined for every point, not merely for sampled maxima. If using the phase route, constants must be uniform down to distance 0 from that edge; if using matched asymptotics, specify an integer K and split 0≤n·distance≤K and K≤n·distance≤nδ, with error bounds uniform in the growing intermediate parameter. A compact-in-β limit alone leaves precisely this gap. Corner ends of the strips are already in Cδ. Neither the current edge E-C measurement nor strip sampling constructs F_n.

**Conditional assembly.** If these P3/P4/P5 inequalities and P1/P2 edge estimates hold with explicit thresholds, their finite cover proves corner dominance above the largest threshold. P0 and certificates for every remaining degree below it are still required. Without thresholds they do not discharge P6. The n8 global target remains OPEN. No convergence rate or finite-certifier capability is inferred from these logical implications.

## Concrete next work

1. The independent rational n4 O-Lt grouping/value check and separate reconstruction now PASS. Publish its narrowly scoped negative record with code/evidence, then obtain the required Claude audit; never relabel all IDEA03 as refuted.
2. Retain E-C as an edge-only candidate. Its next exact task is to compare **whole edge-cell suprema** at n7 and one higher degree, accounting for multiple extrema/sign cells. Then seek a common-phase inequality; if that stronger inequality fails, retain E-C separately.
3. For P3, first inspect original 1-D endpoint/midpoint arguments, recording precise source access and locators; then derive n-uniform physical-coordinate sign/radius bounds. For P4/P5, test the defect lower bound and primitive majorant excess on phase neighborhoods, rather than another raw O(1) profile.


## Executed outcomes

O-R's whole-diamond float screen reports6/10,16/42,60/130 reversals at n4,7,12. Interior-center reversals exist at n7, so failure is not confined to comparing physical-edge centers. Diamond optimization at n24/50 was not run. No exact M_a comparison is claimed. [Record06](../theory/argmax-alln-codex-06-measured-pairing.md) gives method and limitations.

E-C's amended centreward edge screen has no reversal in76 comparisons at n7,12,24,50; n4 has no eligible comparison. This is finite measured support only.

Tie-excluding O-L at n4 has zero comparisons. Separately formulated O-Lt has an exact inherited-certificate witness from a=(3,2) to b=(2,1), corner(4,5), with V_b−V_a>.06322. Developer rational checker, independent rerun and separate rational reconstruction PASS. The [scoped negative record](../theory/argmax-alln-codex-N01-pairing-order-obstruction.md) retains all hypotheses and input identities; required Claude audit remains pending. Original IDEA03 and PD-T099 remain OPEN.
