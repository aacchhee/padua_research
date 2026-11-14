import sys
sys.path.insert(0, sys.argv[1])
import check_correspondence as c
from pathlib import Path
p=c.current_sources(c.ORIGINAL); q=c.current_sources(c.HERE)
labs,cl,di=c.compare_pair(p,q)
L=c.aux_numbers(Path(sys.argv[2])); R=c.aux_numbers(Path(sys.argv[3]))
bad=[k for k in labs if k not in L or k not in R or L[k]!=R[k]]
print(len(labs), 'labels; mismatches:', bad)
print('companion-only aux labels:', len(set(R)-set(L)), 'paper-only:', len(set(L)-set(R)))
