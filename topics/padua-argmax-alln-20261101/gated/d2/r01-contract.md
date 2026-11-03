# Direction2 round1 — physical-coordinate corner derivatives

Direction1 is CLOSED after6 of at most7 rounds. Its independently checked localization confines large-degree global maximizers to vanishing phases of actual non-node corners. Both quantitative repairs stopped on stated bottlenecks; no new uniform primitive bound justifies round7. Required Claude audit remains pending.

## Target registered before execution

Work at canonical physical corner c=(-1,-1), a non-node corner for every n. The other non-node corner is obtained by x reflection for even n and y reflection for odd n.
Classify exactly which cardinal values vanish at c. The candidate is k=0,j even>0; (j,k)=(0,0) is a nonzero polynomial removable value.
Compute the inward one-sided directional derivative of λ along positive physical x and y, retaining |gradient| contributions from zero cardinals.

For a direction v=(s,t)≥0, the first variation is
D_vλ(c)=Σ_(L_B(c)≠0)sign(L_B(c))∇L_B(c)·v
+Σ_(L_B(c)=0)|∇L_B(c)·v|.
This function is convex and homogeneous in v, so strict negative axis derivatives would imply strict negative first variation in every inward direction. A uniform corner-radius theorem requires more than fixed-n negativity.

## Decisive finite test and validation

Before running, use degrees2,3,4,5,8,12,16,24,32,48,64,96,128 (modest-degree screen).
Evaluate exact endpoint Chebyshev derivatives and the corrected coefficient kernel; use the structural zero mask rather than a floating zero test.
Validate n2 against the explicit rational cardinals and inward slopes−7/3,−14/3.
Use exact/outward constructor checks at a few cheap degrees as needed.
Record signs, magnitudes, normalization by n²Λc or corresponding y scale, and directional checks at ratios0,1/4,1/2,3/4,1.
All float64 results MEASURED; any positive derivative needs an exact witness before a refutation.

## Gate

GO requires a validated exact structural reduction and a plausible quantitative derivative/radius lemma with a next discriminating calculation. A wrong zero mask/kernel convention blocks the screen until repaired. A nonnegative axis derivative kills the strict-linear formulation in that degree; retain possible higher-order cases separately rather than reject the corner target. If only empirical negativity remains with no analytical mechanism, stop that approach.
No transferred 1-D literature theorem is used: this round derives directly from the accepted corrected cardinal kernel. Source-reading prerequisites apply before any later external technique transfer.
No direction3 work until direction2 closes; at most7 rounds here. No new finite global certification beyond16 is authorized by this diagnostic.
