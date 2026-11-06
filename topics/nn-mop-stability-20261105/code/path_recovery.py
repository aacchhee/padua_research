"""High precision fixed alternating-path spectral diagnostic; not NN backward error.

Locally derived from the NN and successor-difference identities (PD-T289).
Starting with e1, nu_k=(ceil(k/2),floor(k/2)). Multiplication is
x Pk=P{k+1}+b Pk+S P{k-1}+g P{k-2}, where g=-a1*d at even k,
and g=a2*d at odd k, and d is at nu_{k-2}. This forms H by columns.
The normalized functionals on this path are l1=(1,0,...), and
l2=(1,d_0,0,...). The latter d_0 is an extra NN anchor: one step-line
alone cannot distinguish mu2 from mu2+c*mu1. Eigenprojections of H give
weights. No nearest-compatible full-array optimization is done here.
"""
import mpmath as mp


def recover(c, N, x, weights, dps=100):
    with mp.workdps(dps):
        H=mp.matrix(N)
        for k in range(N):
            nu=((k+1)//2,k//2)
            r={key:mp.mpf(val) for key,val in c[nu].items()}
            H[k,k]=r['b1' if k%2==0 else 'b2']
            if k+1<N: H[k+1,k]=1
            if k: H[k-1,k]=r['a1']+r['a2']
            if k>=2:
                old=c[((k-1)//2,(k-2)//2)]
                d=mp.mpf(old['b2'])-mp.mpf(old['b1'])
                H[k-2,k]=(-r['a1'] if k%2==0 else r['a2'])*d
        eig,V=mp.eig(H)
        Vi=V**-1
        order=sorted(range(N),key=lambda i:(float(mp.re(eig[i])),float(mp.im(eig[i]))))
        d0=mp.mpf(c[0,0]['b2'])-mp.mpf(c[0,0]['b1'])
        ws=[[V[0,i]*Vi[i,0] for i in order],
            [(V[0,i]+d0*V[1,i])*Vi[i,0] for i in order]]
        xx=[eig[i] for i in order]
        truth=[[mp.mpf(t)/sum(row) for t in row] for row in weights]
        weight_componentwise=max(abs(a-b)/b for row,rr in zip(ws,truth) for a,b in zip(row,rr))
        node_error=max(abs(a-b) for a,b in zip(xx,x))/max(abs(a) for a in x)
        weight_error=max(max(abs(a-b) for a,b in zip(row,rr))/max(abs(a) for a in rr)
                         for row,rr in zip(ws,truth))
        return dict(normalized_weight_componentwise_relative=float(weight_componentwise),
                    mixed_input_diagnostic=float(max(node_error,weight_componentwise)),
                    node_relative_sup=float(node_error),normalized_weight_relative_sup=float(weight_error),
                    diagnostic_max=float(max(node_error,weight_error)),
                    max_node_imag=float(max(abs(mp.im(a)) for a in xx)),
                    min_real_weight=float(min(mp.re(a) for row in ws for a in row)),
                    max_weight_imag=float(max(abs(mp.im(a)) for row in ws for a in row)),
                    mass_residual=float(max(abs(sum(row)-1) for row in ws)),
                    dps=dps,scope='alternating path plus d0 anchor; not full NN backward error')
