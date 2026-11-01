"""Independent exact re-audit of the retained upper bound and parity obstruction.

Source cadb35066160e466cb1704b9791ad6f374446422. No source files are modified.
Run from repository root with python -I <this path>; results print as JSON.
"""
import json
import platform
import sympy as s

def check(nodes, weights, k, parity=False):
    mons=[(a,d-a) for d in range(k+1) for a in range(d+1)]
    V=s.Matrix([[x**a*y**b for a,b in mons] for x,y in nodes])
    W=s.diag(*weights)
    G=V.T*W*V
    assert G.det()!=0
    Gi=G.inv()
    P=V*Gi*V.T*W
    assert P*P==P and P.T*W==W*P
    rows=[]
    for i,(xB,yB) in enumerate(nodes):
        v=V[i,:].T
        KBB=(v.T*Gi*v)[0]
        K=V*Gi*v
        sat=s.factor(weights[i]*KBB)
        assert sat>0 and sat<=1
        def residual(axis,centre):
            r=P*s.diag(*[q[axis]-centre for q in nodes])*K
            return s.factor((r.T*W*r)[0]/KBB)
        rx2=residual(0,xB); ry2=residual(1,yB)
        assert rx2<=4*(1-sat) and ry2<=4*(1-sat)
        if (xB,yB)==(0,0):
            if parity:
                assert rx2==0 and ry2==0
            rows.append({'node':[str(xB),str(yB)],'s':str(sat),
                         'residual_x_squared':str(rx2),'residual_y_squared':str(ry2)})
    return {'node_count':len(nodes),'degree':k,'Pi_dimension':len(mons),
            'all_nodes_upper_bound_exact':True,'central_rows':rows}

R=s.Rational
grid=[-1,-R(1,2),0,R(1,2),1]
nodes=[(a,b) for a in grid for b in grid]
out={'source_sha':'cadb35066160e466cb1704b9791ad6f374446422',
     'auditor':'Codex independent supplementary agent; requested gpt-6-astra xhigh; runtime metadata unexposed',
     'environment':{'python':platform.python_version(),'sympy':s.__version__},
     'equal_grid_k2':check(nodes,[R(1,len(nodes))]*len(nodes),2,True)}

# Only central symmetry is imposed. Pair directions are non-product and not
# invariant under separate x/y sign changes; masses are positive and unequal.
directions=[(1,0),(0,1),(R(1,2),R(1,3)),(R(1,4),-R(2,3))]
nodes=[(0,0)]
mass=[s.Integer(1)]
for (a,b),w in zip(directions,[2,3,5,7]):
    nodes.extend([(a,b),(-a,-b)]);mass.extend([s.Integer(w)]*2)
total=sum(mass);weights=[w/total for w in mass]
out['central_only_unequal_weights']=check(nodes,weights,2,True)

# A symmetry centre can already be saturated. This distinguishes the universally
# valid cancellation claim from the overbroad slogan "converse fails at every centre".
nodes=[(0,0),(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)]
out['saturated_central_case']=check(nodes,[R(1,7)]*7,2,True)
assert out['saturated_central_case']['central_rows'][0]['s']=='1'

# An asymmetric non-product positive measure, checked at every node. This checks
# normalization of the bound beyond the symmetric examples used for the negative.
nodes=[(0,0),(1,0),(0,1),(-1,0),(0,-1),(R(1,2),R(1,3)),(-R(1,3),R(1,4))]
weights=[R(i,28) for i in range(1,8)]
out['asymmetric_bound']=check(nodes,weights,2)
print(json.dumps(out,indent=2))
