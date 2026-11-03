"""Optional exact CPython endpoint-sum backend, with frozen monomial reuse.

Build _t1_native from t1_native.c into a scratch directory on PYTHONPATH.
No installer or active scientific driver is changed by this module.
"""
if not __debug__:
    raise RuntimeError("T1 exact backend refuses optimized Python")
from functools import lru_cache
from _t1_native import accumulate

def evaluator(module, *, expected_unit=1 << 160):
    unit=module.S
    if type(unit) is not int or unit != expected_unit:
        raise ValueError("T1 native backend requires the explicitly expected scale")
    frozen_power=module.power; frozen_mul=module.mul
    @lru_cache(maxsize=512)
    def monomials(xlo,xhi,ylo,yhi):
        if any(type(v) is not int for v in (xlo,xhi,ylo,yhi)):
            raise ValueError("noninteger endpoints")
        xp=[frozen_power((xlo,xhi),i) for i in range(9)]
        yp=[frozen_power((ylo,yhi),j) for j in range(9)]
        return tuple(tuple(frozen_mul(a,b) for b in yp) for a in xp)
    def evaluate(terms,X,Y):
        if module.S != unit:
            raise ValueError("changed precision")
        return accumulate(terms,monomials(X[0],X[1],Y[0],Y[1]),unit)
    return evaluate,monomials
