"""Native endpoint accumulation on the frozen checker's exact monomial table."""
if not __debug__:
    raise RuntimeError('T1 native checker backend refuses optimized Python')
from functools import lru_cache
import sys
from pathlib import Path
FROZEN=Path(__file__).resolve().parents[2]/'padua-proof-attempts-2-20261101'/'code'
sys.path.insert(0,str(FROZEN))
import a5_checker_n8_staged_cached as cached
from _t1_native import accumulate
check=cached.check

@lru_cache(maxsize=512)
def table_view(xlo,xhi,ylo,yhi,precision):
    # No powers/products are recomputed or changed; copy integer endpoints only.
    table=cached.monomials(xlo,xhi,ylo,yhi,precision)
    return tuple(tuple((z.lo,z.hi) for z in row) for row in table)

def evaluate(terms,box):
    xx,yy=box
    table=table_view(xx.lo,xx.hi,yy.lo,yy.hi,check.PRECISION)
    check.require(check.PRECISION==160 and check.UNIT==1<<160,'native checker precision changed')
    # Fresh snapshot each call: no coefficient-vector identity or mutation trust.
    converted=tuple((i,j,(c.lo,c.hi)) for i,j,c in terms)
    return check.Interval(*accumulate(converted,table,check.UNIT))
