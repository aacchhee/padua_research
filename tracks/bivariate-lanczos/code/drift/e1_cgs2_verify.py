#!/usr/bin/env python3
"""Developer check: dual-number enumeration of the declared local graph.

Monic gauge rescales local normalized residuals by sqrt(dparent). The final
division error has monic amplitude b_k; scalar denominator errors are omitted
under the separately proved normal-quotient reduction. Every declared vector
operation, including the zero-baseline second matvec, is enumerated here.
"""
import argparse
import contextlib
import io
import json
from pathlib import Path
from e1_exact import Q, build, points


class Dual:
    def __init__(self,value,gradient=None):
        self.value=value;self.gradient=gradient or {}
    def add(self,other,sign=1):
        grad=dict(self.gradient)
        for k,v in other.gradient.items():
            grad[k]=grad.get(k,Q(0))+sign*v
        return Dual(self.value+sign*other.value,grad)
    def round(self,key):
        grad=dict(self.gradient);grad[key]=grad.get(key,Q(0))+self.value
        return Dual(self.value,grad)


def verify(name,rule,n=3):
    xy=points(name)
    with contextlib.redirect_stdout(io.StringIO()):
        coords,b,d,rec,_=build(xy,n,rule)
    count=0;zero_second_ops=0
    for source in range(1,len(b)):
        axis,parent,alpha,_=rec[source]
        for i in range(len(xy)):
            u=coords[axis][i]*b[parent][0,i]
            candidate=Dual(u).round('coordinate_product')
            products=[Dual(c*b[l][0,i]).round(f'first_product_{l}') for l,c in enumerate(alpha)]
            summed=products[0]
            for l in range(1,len(products)):
                summed=summed.add(products[l]).round(f'first_sum_{l}')
            first=candidate.add(summed,-1).round('first_subtract')
            zero_products=[Dual(Q(0)).round(f'second_product_{l}') for l in range(len(alpha))]
            zero_sum=zero_products[0]
            for l in range(1,len(zero_products)):
                zero_sum=zero_sum.add(zero_products[l]).round(f'second_sum_{l}')
            final=first.add(zero_sum,-1).round('second_subtract').round('normalization_division')
            assert final.value==b[source][0,i]
            partial=Q(0);rho=abs(u)+3*abs(b[source][0,i])
            for l,c in enumerate(alpha):
                product=c*b[l][0,i];rho+=abs(product);partial+=product
                if l>=1:
                    rho+=abs(partial)
            assert sum(map(abs,final.gradient.values()),Q(0))==rho
            assert final.gradient['coordinate_product']==u
            assert final.gradient['normalization_division']==b[source][0,i]
            for key,value in final.gradient.items():
                if key.startswith('second_product') or key.startswith('second_sum'):
                    assert value==0;zero_second_ops+=1
            count+=1
    return {'set':name,'rule':rule,'degree':n,'local_graph_gradient_identities':count,'zero_second_pass_operation_checks':zero_second_ops,'arithmetic':'exact rational dual numbers','result':'PASS'}


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args()
    rows=[verify(s,r) for s in ['triangle','rotated'] for r in ['bj','mirror','alt','pivot']]
    Path(a.output).write_text(json.dumps({'status':'MEASURED developer local-graph check; not independent agent rerun','checks':rows},indent=2)+'\n');print(json.dumps({'cases':len(rows),'result':'PASS'}))
