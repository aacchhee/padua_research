"""T4 measured phase constants, local gain, central-envelope rate and projections.

No fitted constant is a rigorous all-n bound. The projection model is stated
in the output; it cannot decide effectivity of the still unquantified full
assembly. Global and local phase windows are exactly those in PD-T189/190.
"""
import json, sys, time
import numpy as np
from scipy.optimize import minimize_scalar, brentq
from scipy.integrate import quad
from tests_common import Edge, Primitive, Eval, validate


def maxgrid(f, a, b, count=65):
    q = np.linspace(a, b, count); vals = np.array([f(s) for s in q])
    # Retain all grid values and refine all grid local maxima.
    candidates = [(float(vals[i]), float(q[i])) for i in (0, len(q)-1)]
    for i in range(1, len(q)-1):
        if vals[i] >= vals[i-1] and vals[i] >= vals[i+1]:
            rr = minimize_scalar(lambda x: -f(x), bounds=(q[i-1], q[i+1]), method='bounded', options={'xatol': 1e-10})
            candidates.append((-float(rr.fun), float(rr.x)))
    candidates.append((float(vals.max()),float(q[vals.argmax()])))
    return max(candidates)


if __name__ == '__main__':
    start=time.monotonic()
    g, gerr = quad(lambda x: 8/np.pi**2 * (np.arcsinh(x)+x/(1+np.sqrt(1+x*x))) * np.arctanh(x),0,1,epsabs=1e-11)
    out={'status':'MEASURED','arithmetic':'float64','validation':validate(), 'g_quadrature':g,'g_quad_error_estimate':gerr,'rows':[]}
    for n in (8,12,15,16,24,31,32,48,60,63,64,96,127,128,192,255,256,399,400):
        p,e=Primitive(n),Edge(n)
        assert abs(p.lc-e.lc)<1e-8
        glob=maxgrid(lambda s:(p.one(s)-np.cos(s/2)**2*p.lc)/np.log(n+1),0,np.pi)
        local=maxgrid(lambda s:p.one(s)-p.lc,0,np.pi/6)
        local_C=maxgrid(lambda s:(p.one(s)-np.cos(s/2)**2*p.lc)/(s*s*np.log(n+1)+s),1e-6,np.pi/6,33)
        # Search the EXACT definition of R_cen, both vertical edges.
        cen=max((maxgrid(lambda t:e.one(edge,t),np.pi/2-np.pi/(n+1),np.pi/2+np.pi/(n+1),33)+(edge,)) for edge in ('v+','v-'))
        gap=p.lc-cen[0]
        out['rows'].append({'n':n,'corner':p.lc,'global_phase_C_estimate':glob[0],'global_phase_argmax_s':glob[1],
                            'local_excess':local[0],'local_argmax_s':local[1],
                            'local_log_squared_coefficient':local[0]*np.log(n)**2,
                            'local_C_estimate':local_C[0],
                            'window_boundary_excess':p.one(np.pi/6)-p.lc,
                            'central_gap':gap,'central_gap_minus_g':gap-g,
                            'central_rate_n':n*(gap-g),'central_rate_n_over_log':n*(gap-g)/np.log(n),
                            'central_argmax_angle':cen[1],'central_edge':cen[2]})
        print(json.dumps(out['rows'][-1]),flush=True)
    # Optimistic model: all unknown assembly errors share the measured central
    # absolute-error rate C/n. Alternative applies log(n)/n. Full gap budget g/2.
    for law in ('C/n','C*log(n)/n'):
        if law=='C/n': c=max(abs(r['central_rate_n']) for r in out['rows'] if r['n']>=32)
        else: c=max(abs(r['central_rate_n_over_log']) for r in out['rows'] if r['n']>=32)
        threshold=next(n for n in range(32,1000000) if c*(1 if law=='C/n' else np.log(n))/n < g/2)
        out.setdefault('optimistic_projections',[]).append({'law':law,'C_inferred':c,'error_budget':g/2,'n0_projected':threshold,
          'rigorous':False,'scope':'central-envelope error only; no bound for unknown P1-P5 assembly errors'})
    c=max(r['global_phase_C_estimate'] for r in out['rows'] if r['n']>=32)
    a=np.sin(np.pi/12)**2
    # Existing localization proof plus the PROVED but crude A2 lower bound.
    # c is inferred from finite data, hence the threshold remains a projection.
    z=brentq(lambda z:a*(4/np.pi**2*z*z-54)-c*np.log(np.exp(z)+1)-g,1,100)
    out['literal_proof_projection']={'C_global_inferred':c,'local_window':float(np.pi/6),
      'corner_lower_bound':'(4/pi^2)*log(n)^2-54','log_n0':z,'n0_projected':float(np.exp(z)),
      'rigorous':False,'criterion_n0_exceeds_60':bool(np.exp(z)>60),
      'scope':'sufficient threshold to enter PD-T190 local window via PD-T189 uniform C; unknown defect and global assembly errors omitted'}
    out['seconds']=time.monotonic()-start
    with open(sys.argv[1],'w') as f:json.dump(out,f,indent=2)
    print(json.dumps({'projections':out['optimistic_projections'],'seconds':out['seconds']},indent=2))
