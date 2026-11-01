"""Exact independent check of n=3 Padua cardinal factor and edge angle jets.
Audited SHA cadb35066160e466cb1704b9791ad6f374446422.
Uses the proposed polynomial's Kronecker nodal data and exact nonzero determinant,
not a replay of the developer's cardinal-inverse search.
"""
import pathlib,json,platform
import sympy as s
root=pathlib.Path(__file__).resolve().parents[1]
x,y=s.symbols('x y'); z=s.sqrt(2)/2
pts=[(s.Integer(1),s.Integer(1)),(s.Integer(1),s.Integer(0)),(s.Integer(1),s.Integer(-1)),
     (s.Rational(1,2),z),(s.Rational(1,2),-z),
     (s.Rational(-1,2),s.Integer(1)),(s.Rational(-1,2),s.Integer(0)),(s.Rational(-1,2),s.Integer(-1)),
     (s.Integer(-1),z),(s.Integer(-1),-z)]
idx=[(a,d-a) for d in range(4) for a in range(d,-1,-1)]
V=s.Matrix([[xx**a*yy**b for a,b in idx] for xx,yy in pts])
det=s.simplify(V.det())
poly=(x-1)*(2*x*x+x+2*y*y-2)/3
values=[s.simplify(poly.subs({x:xx,y:yy})) for xx,yy in pts]
assert values==[0,0,0,0,0,0,1,0,0,0]
assert det!=0
assert s.simplify(poly.subs(x,1))==0
# x=cos(theta), y=cos(phi): theta-normal first derivative has a sin(theta)
# factor; tangential derivatives have the exact x-1 factor.
assert s.simplify(s.diff(poly,y).subs(x,1))==0
assert s.simplify(s.diff(poly,y,2).subs(x,1))==0
out=dict(source_sha='cadb35066160e466cb1704b9791ad6f374446422',python=platform.python_version(),sympy=s.__version__,
         degree=int(s.Poly(poly,x,y).total_degree()),vandermonde_determinant=str(det),
         factor=str(s.factor(poly)),nodal_values=[str(v) for v in values],
         result='Exact cardinal identity and vanishing of angle value/first derivatives/tangential derivatives at theta=0 verified.',
         limitation='Does not enclose the background critical points or certify maxima counts.')
print(json.dumps(out,indent=2))
(root/'audit-02-support/proposal-edge-independent.json').write_text(json.dumps(out,indent=2)+'\n')
