/* Native exact GMP construction of the frozen PD-T106/107 pencil.
 * Compile: cc -O3 -std=c11 cert_pencil.c -lgmp -o /tmp/cert_pencil
 * Every mpq value is explicitly canonical before arithmetic or inspection.
 * Output files are regenerable scratch, never proof inputs accepted unchecked.
 */
#include <stdio.h>
#include <gmp.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

static void die(const char *s) { fprintf(stderr,"%s\n",s); exit(2); }
static int fold(int k,int n) { k%=2*n; return k<n?k:2*n-k; }
static void h(mpq_t z,int k) {
    if(k%2) mpq_set_ui(z,0,1);
    else if(k==0) mpq_set_ui(z,2,1);
    else mpq_set_si(z,-2,(unsigned long)k*k-1);
    mpq_canonicalize(z);
}
static void product(mpq_t z,int r,int s) {
    mpq_t a,b; mpq_inits(a,b,NULL); h(a,r); h(b,s); mpq_mul(z,a,b);
    mpq_clears(a,b,NULL);
}
static void entry(mpq_t H,mpq_t Q,int m,int a,int b,int c,int d) {
    int rr[2]={a+c,abs(a-c)},ss[2]={b+d,abs(b-d)};
    mpq_t v; mpq_init(v); mpq_set_ui(H,0,1); mpq_set_ui(Q,0,1);
    for(int i=0;i<2;i++) for(int j=0;j<2;j++) {
        int r=rr[i],s=ss[j],A=fold(r,m),B=fold(s,m+1);
        product(v,r,s); mpq_add(H,H,v);
        if(A+B<=m) product(v,A,B); else product(v,m-A,m+1-B);
        mpq_add(Q,Q,v);
    }
    mpq_div_2exp(H,H,2); mpq_div_2exp(Q,Q,2); mpq_clear(v);
}
int main(int argc,char **argv) {
    if(argc!=3) die("usage: cert_pencil m output-prefix");
    int m=atoi(argv[1]); if(m<2||m>500) die("m outside supported 2..500");
    int N=m*(m+1)/2,*a=calloc(N,sizeof(int)),*b=calloc(N,sizeof(int));
    int *p=calloc(N,sizeof(int)),*local=calloc(N,sizeof(int)),n[2]={0,0};
    int k=0; for(int t=0;t<m;t++) for(int x=t;x>=0;x--) {
        a[k]=x;b[k]=t-x;p[k]=(m%2?b[k]:a[k])%2;local[k]=n[p[k]]++;k++;
    }
    mpq_t *H[2],*Q[2];
    for(int z=0;z<2;z++) {
        size_t len=(size_t)n[z]*n[z]; H[z]=calloc(len,sizeof(mpq_t));Q[z]=calloc(len,sizeof(mpq_t));
        if(!H[z]||!Q[z]) die("allocation failed");
        for(size_t u=0;u<len;u++) {mpq_init(H[z][u]);mpq_init(Q[z][u]);}
    }
    mpq_t h0,q0; mpq_inits(h0,q0,NULL); size_t offblock=0;
    for(int i=0;i<N;i++) for(int j=i;j<N;j++) {
        entry(h0,q0,m,a[i],b[i],a[j],b[j]);
        if(p[i]!=p[j]) {
            if(mpq_sgn(h0)||mpq_sgn(q0)) die("offblock nonzero");
            offblock++;continue;
        }
        int z=p[i]; size_t u=(size_t)local[i]*n[z]+local[j],v=(size_t)local[j]*n[z]+local[i];
        mpq_set(H[z][u],h0);mpq_set(Q[z][u],q0);
        mpq_set(H[z][v],h0);mpq_set(Q[z][v],q0);
    }
    char name[4096]; if(strlen(argv[2])>4000) die("prefix too long");
    snprintf(name,sizeof(name),"%s.exact",argv[2]);FILE *ex=fopen(name,"w");
    snprintf(name,sizeof(name),"%s.float",argv[2]);FILE *fl=fopen(name,"wb");
    if(!ex||!fl) die("cannot create output");
    fprintf(ex,"%d %d %d %zu\n",m,n[0],n[1],offblock);
    mpz_t den,tmp;mpz_inits(den,tmp,NULL);
    for(int z=0;z<2;z++) {
        size_t len=(size_t)n[z]*n[z];mpz_set_ui(den,1);
        for(size_t u=0;u<len;u++) {
            mpz_lcm(den,den,mpq_denref(H[z][u]));mpz_lcm(den,den,mpq_denref(Q[z][u]));
        }
        if(mpz_sgn(den)<=0) die("nonpositive denominator");
        gmp_fprintf(ex,"%Zd\n",den);
        for(int which=0;which<2;which++) {
            mpq_t *M=which?Q[z]:H[z];
            for(size_t u=0;u<len;u++) {
                if(!mpz_divisible_p(den,mpq_denref(M[u]))) die("nondividing denominator");
                mpz_divexact(tmp,den,mpq_denref(M[u]));mpz_mul(tmp,tmp,mpq_numref(M[u]));
                gmp_fprintf(ex,"%Zd\n",tmp);double d0=mpq_get_d(M[u]);
                if(fwrite(&d0,sizeof(d0),1,fl)!=1) die("float write failed");
            }
        }
        for(size_t u=0;u<len;u++){mpq_clear(H[z][u]);mpq_clear(Q[z][u]);}free(H[z]);free(Q[z]);
    }
    if(fclose(ex)||fclose(fl)) die("close failed");
    fprintf(stderr,"GMP %s; m=%d; dimensions=%d,%d; checked_offblock=%zu\n",gmp_version,m,n[0],n[1],offblock);
    mpz_clears(den,tmp,NULL);mpq_clears(h0,q0,NULL);free(a);free(b);free(p);free(local);return 0;
}
