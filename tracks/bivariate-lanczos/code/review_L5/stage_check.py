# brute-force check: in the sequence (j,i), i=1..M-1, j=0..i-1, any rotation m later than k with stage(m)<=stage(k) is disjoint from k
for M in (5, 12, 30):
    seq=[(j,i) for i in range(1,M) for j in range(i)]
    bad=0
    for a,(j,i) in enumerate(seq):
        for (j2,i2) in seq[a+1:]:
            if j2+i2<=j+i and len({j,i}&{j2,i2})>0: bad+=1
    print(M, "violations", bad, "stages", len({j+i for j,i in seq}))
