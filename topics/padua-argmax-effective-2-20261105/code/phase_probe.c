/* Floating diagnostic only: no enclosure, finite-cover, or proof claim. */
#include <math.h>

static double sinc_stable(double x) {
    if (fabs(x) < 1e-4) {
        double z=x*x;
        return 1-z/6+z*z/120-z*z*z/5040;
    }
    return sin(x)/x;
}

static double ratio(int k, double x) {
    const double pi=acos(-1.0);
    long q=lround(x/pi);
    double r=x-q*pi;
    double sign=((q*(k-1))%2) ? -1.0 : 1.0;
    return sign*k*sinc_stable(k*r)/sinc_stable(r);
}

double phase_g(int n, double u, double v) {
    double s=(u+v)/2, t=(u-v)/2;
    return ratio(n+1,s)*ratio(n+1,t)+ratio(n,s)*ratio(n,t)-cos(n*u);
}

double phase_s(int n, double alpha, double beta) {
    int m=n+1;
    double sum=0, correction=0, pi=acos(-1.0);
    for(int j=0;j<2*n;j++) for(int r=1-(j%2);r<2*m;r+=2) {
        double value=fabs(phase_g(n,(j*pi+alpha)/n,(r*pi+beta)/m));
        double y=value-correction, next=sum+y;
        correction=(next-sum)-y; sum=next;
    }
    return sum/(2.0*n*m);
}

double phase_lambda(int n, double theta, double phi) {
    int m=n+1;
    double sum=0, correction=0, pi=acos(-1.0);
    for(int j=0;j<=n;j++) for(int k=j%2;k<=m;k+=2) {
        double tj=j*pi/n, pk=k*pi/m, four=0;
        for(int sx=-1;sx<=1;sx+=2) for(int sy=-1;sy<=1;sy+=2)
            four+=phase_g(n,theta+sx*tj,phi+sy*pk);
        double weight=((j==0||j==n)?0.5:1)*((k==0||k==m)?0.5:1);
        double y=weight*fabs(four)-correction, next=sum+y;
        correction=(next-sum)-y;sum=next;
    }
    return sum/(2.0*n*m);
}
