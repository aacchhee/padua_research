import math
pi = math.pi
mx_m = mx_p = 0
for n in [7, 32, 51]:
    m = n+1
    for (x, y) in [(0.3, 0.7), (1.1, 0.2), (0.05, 2.9), (2.0, 1.0)]:
        for r in range(2*m):
            dl = (1-r) % 2; vr = (r*pi+y)/m; u0 = (dl*pi+x)/n
            tm = ((u0-vr)/2*n/pi) % 1; tp = ((u0+vr)/2*n/pi) % 1
            em = (0.5+(x-y+vr)/(2*pi)) % 1; ep = (0.5+(x+y-vr)/(2*pi)) % 1
            dm = abs(tm-em); dm = min(dm, 1-dm); dp = abs(tp-ep); dp = min(dp, 1-dp)
            mx_m = max(mx_m, dm); mx_p = max(mx_p, dp)
print('max |t_- - eta_-| mod 1 =', mx_m, '  max |t_+ - eta_+| mod 1 =', mx_p)
