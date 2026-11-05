/* Finite floating diagnostics. Profiles are not outward-rounded bounds. */
#include <math.h>
#include <stdlib.h>

double phase_g(int n, double u, double v);

int projection_profiles(int n, double alpha, double beta,
                        double *qh, double *qv, double *sout) {
    int m=n+1, nr=2*n, ns=2*m;
    double *h=calloc((size_t)nr*ns,sizeof(double));
    if (!h) return 1;
    double pi=acos(-1.0), sum=0;
    for(int r=0;r<nr;r++) for(int s=1-(r%2);s<ns;s+=2) {
        double value=phase_g(n,(r*pi+alpha)/n,(s*pi+beta)/m);
        h[(size_t)r*ns+s]=value;sum+=fabs(value);
    }
    *sout=sum/(2.0*n*m);
    for(int k=0;k<=m;k++) {
        double value=0;
        for(int r=0;r<nr;r++) for(int s=1-(r%2);s<ns;s+=2) {
            int reflected=(2*k-s+ns)%ns;
            double a=h[(size_t)r*ns+s], b=h[(size_t)r*ns+reflected];
            value+=fabs(a)+fabs(b)-fabs(a+b);
        }
        qv[k]=value/(4.0*n*m);
    }
    for(int j=0;j<=n;j++) {
        double value=0;
        for(int r=0;r<nr;r++) {
            int reflected=(2*j-r+nr)%nr;
            for(int s=1-(r%2);s<ns;s+=2) {
                double a=h[(size_t)r*ns+s],b=h[(size_t)reflected*ns+s];
                value+=fabs(a)+fabs(b)-fabs(a+b);
            }
        }
        qh[j]=value/(4.0*n*m);
    }
    free(h);return 0;
}
