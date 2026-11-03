# Prospective exact row-sum repair after the coarse constants

This is a candidate retained during round5 diagnosis, not an executed round6. It stays in direction1's primitive analysis and is distinct from the unassigned generating-curve direction4.

The absolute regular-Hessian sums in round3 give unusably large constants. A potential distinct repair is to sum each first-coordinate row before bounding its derivatives. On the β=0 axis, write T=(u−v)/2,P=(u+v)/2,a=(1+cosα)/2. The quotient identities suggest

F=A_v cot T+B_v cot P,
A_v=(sinα−2a cot(v/2))/4,
B_v=(sinα+2a cot(v/2))/4,

away from endpoints/collisions, with the original finite polynomial retained there. A parity-restricted periodic row has n equally spaced first angles, so the complete cotangent sum should have the exact closed form n cot(nz). The numerator and denominator signs divide a row into a bounded number of intervals; only the corresponding signed partial cotangent sums remain.

Prospective decisive test: independently derive the exact row formula with all endpoint/removable cases, determine whether the partial sums can be bounded using their paired structure without the large absolute-Hessian constant, and test only a fixed predeclared small-degree grid for implementation correctness. If this simply replaces the existing n² sum by equally uncontrolled partial sums and produces no sharper uniform bound, stop this repair rather than increasing degrees. A finite exact formula alone does not establish an all-n gain estimate.

No row-sum numerical run or uniform bound has been performed in this note. A future round requires a separate positive gate and contract.
