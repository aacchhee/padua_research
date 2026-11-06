# C09 — coefficient-vertex row attempt

Rules 4b728b0; 2026-11-06. Root seeded convexity escape only after C08
artifacts were complete and frozen. New C09 records only; no C08/C06/C07
source, review, receipt, Git or shared file changes.

Prospective gate: [ideas/C09-row-convexity.md](../ideas/C09-row-convexity.md).
The fresh search and complete new shortlist preceded the candidate proof.
The proposed specialization needs four (c,p) vertices, not eight generic
coefficients, and excludes all possible denominator collisions FIRST.

No code/test/board/cover has run. First analytic obligation is sound
convex relaxation with the correlated denominator kept fixed at each
actual phase, followed by a whole-box vertex enclosure. Point bounds
are not assumed to enclose any phase box.

## Live gate refresh and first freeze

After the original preregistration, root announced the live PR28 registry
merge. All40 new lines and three changed rows were read in full before
the proof was written; the current registry hash is
`68bf789c82967944421e6fc54f8164dbdb91d1096fa10694008261fbd54f9e9d`.
The prior complete read and original preregistration hash are preserved
in the idea record. The NN-MOP additions cause no mechanism change.

Frozen proof: `theory/C09-row-convexity.md`,17,527 bytes, SHA-256
`ba07f3c0b613b999d342414e38950b7f6433fb038896f8985bd072e784fbd052`.
Idea/gate SHA-256:
`cb0f3ff4f9c19ec890be2185514f370fb8569e72a55c274c6be9f6f1cc792aab`.
Developer status PROVED analytic contract; independent review PENDING.
No arithmetic diagnostic, implementation, board, fit or cover was run;
computational CPU charged is zero.

The coefficient-vertex escape survives the first analytic collision test
only after possible collision terms are retained under their actual finite
primitive. The proof supplies an exact n3 removable-collision example where
an expanded rectangle's artificial vertex would otherwise have a pole.
One-grid-unit collision buffers cost at most8 actual points/ordinary row
and give both remaining cotangent channels pole clearance at least1.

Four(c,p) vertices suffice. Their roots are fixed in angular u, so only
the alpha/(2pi) grid shift moves each index root. Literal outward band
width<1 guards give at most3 regular vertex direct samples and12 blocks
per channel. Relaxed vertex terms require their own rational/cotangent
coefficients, and their complete signed core sum replaces the unavailable
original signed-row identity. Dropping a failed vertex is forbidden.

Main quantitative result: the exact-real convex majorant exceeds S by at
most `(2/pi)*Delta_* H_n^2`, with Delta_* the largest row coefficient
rectangle width sum. Exact coefficient ranges satisfy
Delta_*<=3*w_alpha+4*w_beta. This bounds coefficient relaxation only;
whole-box interval dependency and arithmetic errors remain additional.
The proof derives the separate all-row artificial-vertex tail charge;
it does not reuse C02's special correlated coefficient weight estimate.

O(n) scalar work is proved for the guarded upper path plus finite coarse
row fallback. Constants can be expensive, C06 rational bit costs remain,
and useful tightness/speed have not been measured. The result gives S
uppers only; point equality, gradients, corner orbit and defects remain
separate. Root and the C06/C07 code owner received the frozen proof with
explicit independent-review/no-release notice. Frozen C08 files unchanged.
