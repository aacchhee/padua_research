import sys; sys.path.insert(0,'.')
from local_lemma import *
from fractions import Fraction as F
done=0
for N in range(5,9):
    for n in range(2,N-1):
        target=(n,1)
        for idx in range(N):
            x=[F(i*i+i,2)-F(3) for i in range(N)]
            w1=[F(1+(i*i)%3) for i in range(N)]
            w2=[F(1+(2*i+1)%4, 1+i%2) for i in range(N)]
            try: tv=tune(x,w1,w2,idx,target)
            except ZeroDivisionError: continue
            if tv<=0: continue
            w2[idx]=tv
            try:
                run(x,[w1,w2],f'N{N} t{target} w2[{idx}]={tv}',sum(target)-1,target); done+=1
            except AssertionError as e:
                print('ASSERT',N,target,idx,e)
            break
print('cases',done)
