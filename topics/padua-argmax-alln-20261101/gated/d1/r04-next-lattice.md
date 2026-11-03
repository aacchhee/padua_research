# Round4 prospective repair at the first corner cells

During the adaptive-block diagnosis a more discrete next candidate arose: for n≥48 and odd-coset phases |α|+|β|≤1/64, every odd coset other than a physical non-node corner might have Δ≥1/4096. This is a candidate for a separately gated round5, not a completed claim. Its point is to replace an O(1/n) corner box by a small phase neighborhood of the actual non-node corner.

If the relevant angle is≥4π/n from the endpoints, round4's adaptive block should apply. Otherwise an interior mesh index is only one to four steps from an endpoint. Use a single parity-correct diagonal through middle mesh rows instead of requiring every row to contain an interval of prescribed width.

Prospective vertical near-top construction: s=m−K∈{1,2,3,4}; choose l∈[n/4,n/2], physical k=l+q and periodic first index j'=n−l, with q=1 for odd s and0 for even s. Odd-coset parity makes j'+k≡J. The selected numerator should be≥1/32 and denominator span<26/m; at least n/8 selected rows would give Qv≥1/3328. Near the bottom use j'=l and q=0 for odd s,1 for even s.

For the horizontal top construction the grids are reversed: choose l∈[m/4,m/2], periodic second index k'=m−l, physical first index j=l+q, with q=−1 for odd endpoint-distance index and0 for even. The tempting q=+1 odd choice fails the first-cell band inequality; it is retained as a rejected preliminary choice. Near the bottom use k'=l,q=0 for odd index and−1 for even. The fixed numerator1+cos v must be checked explicitly rather than importing the vertical expression.

Discriminating test: verify all four band inequalities, parity conditions, physical-index ranges and exact grid counts for every n≥48 and index distance1–4. Any missing parity case or false numerator margin kills the proposed constant/choice. The consequences would still have a non-effective degree threshold because the primitive phase-entry constants remain coarse/unquantified. No all-degree global theorem or new finite range is claimed.
