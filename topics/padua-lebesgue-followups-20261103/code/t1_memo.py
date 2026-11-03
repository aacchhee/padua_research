"""Bit-identical integer interval evaluation with bounded monomial reuse.

Cache only frozen power/multiply results, then perform the same ordered sum of
outward per-term coefficient products. No field/interval/acceptance precision
changes. A factory binds the exact scale and power implementation of its module.
"""
if not __debug__:
    raise RuntimeError('T1 refuses optimized Python: t1_memo.py')
from functools import lru_cache

def evaluator(module):
    unit=module.S; frozen_power=module.power; frozen_mul=module.mul
    @lru_cache(maxsize=512)
    def monomials(xlo,xhi,ylo,yhi):
        assert all(type(v)is int for v in(xlo,xhi,ylo,yhi))
        xp=[frozen_power((xlo,xhi),i)for i in range(9)]
        yp=[frozen_power((ylo,yhi),j)for j in range(9)]
        return tuple(tuple(frozen_mul(a,b)for b in yp)for a in xp)
    def evaluate(terms,X,Y):
        assert module.S==unit
        table=monomials(X[0],X[1],Y[0],Y[1]);lo=hi=0
        for i,j,c in terms:
            m=table[i][j]
            values=(c[0]*m[0],c[0]*m[1],c[1]*m[0],c[1]*m[1])
            lo+=min(values)//unit;hi+=-((-max(values))//unit)
        return lo,hi
    return evaluate,monomials
