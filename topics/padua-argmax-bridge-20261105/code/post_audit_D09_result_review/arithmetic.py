"""Independent exact dyadic endpoint and squared-coordinate loss arithmetic."""
import math
from fractions import Fraction as Q

def endpoints(values):
    if len(values)!=3 or not all(math.isfinite(x) for x in values):
        raise ValueError('three finite binary64 outputs required')
    low,high,radius=values
    if low>high or radius<0:raise ValueError('invalid enclosure')
    return dict(lower=str(Q.from_float(low)),upper=str(Q.from_float(high)),
        radius=str(Q.from_float(radius)),binary64_hex=[x.hex() for x in values])

def check_endpoint_record(row):
    reconstructed=endpoints([float.fromhex(x) for x in row['binary64_hex']])
    if row!=reconstructed:raise ValueError('rational/hex endpoint disagreement')
    return reconstructed

def loss_test(n,a,b,corner,vertices):
    """Use exact normalized slope; pi is bounded, never approximated."""
    if n!=512 or len(vertices)!=3 or a<=0 or b<=0:raise ValueError('fixed case contract')
    check_endpoint_record(corner)
    for row in vertices:check_endpoint_record(row)
    u,v=a*a/2,b*b/2
    k=Q(n,n+1);pi_up=Q(22,7);norm=Q(34)
    losses=[Q(corner['lower'])-Q(row['upper']) for row in vertices]
    slopes=[losses[0]/u,losses[1]/v,losses[2]/(u+v)]
    threshold=norm*pi_up**4*max(u,k**4*v)/6
    gap=min(slopes)-threshold
    return dict(u_prime=str(u),v_prime=str(v),kappa=str(k),losses=list(map(str,losses)),
        q=str(min(slopes)),M=str(norm),pi_upper=str(pi_up),threshold=str(threshold),
        gap=str(gap),passes=gap>0,epsilon_lower=str(gap/pi_up**2) if gap>0 else None)

def covers_half_diamond(a,b):
    return min(a,b)*Q(157,50)>Q(1,2)
