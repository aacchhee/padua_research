# A5: greedy-Leja orderings at 400 dps; report gap structure (near-ties) and compare to code's permutation(n,'L') at 100 dps / 1e-80
import mpmath as mp, sys
sys.path.insert(0,'topics/padua-3d-20261106/code')
def greedy(n,dps,tol):
    with mp.workdps(dps):
        h=[mp.cos(mp.pi*j/n) for j in range(n+1)]
        order,rem=[0],list(range(1,n+1)); minsep=mp.inf; maxtie=mp.mpf(0)
        while rem:
            v={j:mp.fprod(abs(h[j]-h[i]) for i in order) for j in rem}
            best=max(v.values())
            ties=[j for j in rem if abs(v[j]-best)<=tol*best]
            for j in rem:
                rel=abs(v[j]-best)/best
                if j in ties: maxtie=max(maxtie,rel)
                else: minsep=min(minsep,rel)
            w=min(ties); order.append(w); rem.remove(w)
        return order, minsep, maxtie
import importlib.util
spec=importlib.util.spec_from_file_location('t4','topics/padua-3d-20261106/code/t4_stacks.py')
t4=importlib.util.module_from_spec(spec); spec.loader.exec_module(t4)
worst_sep=1; worst_tie=0
for n in range(1,41):
    o,s,t=greedy(n,400,mp.mpf('1e-300'))
    code=t4.permutation(n,'L')
    worst_sep=min(worst_sep,s); worst_tie=max(worst_tie,t)
    if n<=12 or o!=code: print(n,o==code, o if n<=8 else '', 'min non-tie rel gap %s  max tie rel diff %s'%(mp.nstr(s,3),mp.nstr(t,3)))
print('n<=40: smallest relative gap to a non-tie competitor',mp.nstr(worst_sep,3),' largest relative diff among ties',mp.nstr(worst_tie,3))
