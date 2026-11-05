/* Exact fixed-point interval producer. All scientific arithmetic uses GMP. */
#include <stdio.h>
#include <gmp.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
typedef struct {
    mpz_t l,h;
}
I;
static int n,m,K,T;
static mpz_t S;
static mpq_t *W;
static mpz_t *C;
static I *X,*Y;
static double limit;
static long maxboxes, visited, splits, bound_count, corner_count;
static int maxdepth, depthlimit, limited;
static clock_t search_start;
static I *right_tables[101];
static I *alloc_i(size_t count) {
    I *p=calloc(count,sizeof(I));
    if(!p) {
        perror("allocation");
        exit(2);
    }
    for(size_t i=0;i<count;i++) {
        mpz_init(p[i].l);
        mpz_init(p[i].h);
    }
    return p;
}
static void free_i(I*p,size_t count) {
    for(size_t i=0;i<count;i++) {
        mpz_clear(p[i].l);
        mpz_clear(p[i].h);
    }
    free(p);
}
static void seti(I*a,I*b) {
    mpz_set(a->l,b->l);
    mpz_set(a->h,b->h);
}
static void mul(I*out,I*a,I*b) {
    mpz_t p,lo,hi;
    mpz_inits(p,lo,hi,NULL);
    mpz_mul(lo,a->l,b->l);
    mpz_set(hi,lo);
    mpz_mul(p,a->l,b->h);
    if(mpz_cmp(p,lo)<0)mpz_set(lo,p);
    if(mpz_cmp(p,hi)>0)mpz_set(hi,p);
    mpz_mul(p,a->h,b->l);
    if(mpz_cmp(p,lo)<0)mpz_set(lo,p);
    if(mpz_cmp(p,hi)>0)mpz_set(hi,p);
    mpz_mul(p,a->h,b->h);
    if(mpz_cmp(p,lo)<0)mpz_set(lo,p);
    if(mpz_cmp(p,hi)>0)mpz_set(hi,p);
    mpz_fdiv_q_2exp(out->l,lo,192);
    mpz_cdiv_q_2exp(out->h,hi,192);
    mpz_clears(p,lo,hi,NULL);
}
static I *mode(I*v,int len,int j,int p) {
    int r=j*p%(2*len);
    return v+(r<len?r:2*len-r);
}
static void add_scaled(I*out,I*a,mpz_t z) {
    if(mpz_sgn(z)>=0) {
        mpz_addmul(out->l,a->l,z);
        mpz_addmul(out->h,a->h,z);
    }
    else {
        mpz_addmul(out->l,a->h,z);
        mpz_addmul(out->h,a->l,z);
    }
}
static void combine(I*out,I*in,int stride,int target) {
    mpq_t lo,hi,q;
    mpq_inits(lo,hi,q,NULL);
    for(int a=0;a<m;a++) {
        mpq_ptr w=W[a*m+target];
        if(!mpq_sgn(w))continue;
        I*v=in+a*stride;
        mpq_set_z(q,mpq_sgn(w)>0?v->l:v->h);
        mpq_mul(q,q,w);
        mpq_add(lo,lo,q);
        mpq_set_z(q,mpq_sgn(w)>0?v->h:v->l);
        mpq_mul(q,q,w);
        mpq_add(hi,hi,q);
    }
    mpz_fdiv_q(out->l,mpq_numref(lo),mpq_denref(lo));
    mpz_cdiv_q(out->h,mpq_numref(hi),mpq_denref(hi));
    mpq_clears(lo,hi,q,NULL);
}
static I *construct(mpz_t threshold) {
    I*all=alloc_i((size_t)K*T), *p=alloc_i(T),*tmp=alloc_i(T),*product=alloc_i(2);
    mpz_t z,cl,ch,low[2],high[2],a,b;
    mpz_inits(z,cl,ch,low[0],low[1],high[0],high[1],a,b,NULL);
    int card=0;
    for(int j=0;j<=n;j++)for(int k=0;k<=n+1;k++) {
        if((j+k)%2)continue;
        for(int t=0;t<T;t++) {
            mpz_set_ui(p[t].l,0);
            mpz_set_ui(p[t].h,0);
        }
        for(int u=0;u<=n;u++)for(int v=0;v<=n-u;v++) {
            int h=(u?2:1)*(v?2:1);
            if(u==n&&v==0)h=1;
            int den=n*(n+1)*(j==0||j==n?2:1)*(k==0||k==n+1?2:1);
            mpz_mul_ui(z,S,2*h);
            mpz_fdiv_q_ui(product[1].l,z,den);
            mpz_cdiv_q_ui(product[1].h,z,den);
            mul(product,mode(X,n,j,u),mode(Y,n+1,k,v));
            mul(product,product,product+1);
            for(int a0=0;a0<=u;a0++)if(mpz_sgn(C[u*m+a0]))for(int b0=0;b0<=v;b0++)if(mpz_sgn(C[v*m+b0])) {
                mpz_mul(z,C[u*m+a0],C[v*m+b0]);
                add_scaled(p+a0*m+b0,product,z);
            }
        }
        for(int c=0;c<2;c++) {
            mpz_set_ui(cl,0);
            mpz_set_ui(ch,0);
            for(int a0=0;a0<m;a0++)for(int b0=0;b0<m;b0++) {
                int sign= ((a0+b0)%2?-1:1);
                if(c==1)sign= n%2?(a0%2?-1:1):(b0%2?-1:1);
                if(sign>0) {
                    mpz_add(cl,cl,p[a0*m+b0].l);
                    mpz_add(ch,ch,p[a0*m+b0].h);
                }
                else {
                    mpz_sub(cl,cl,p[a0*m+b0].h);
                    mpz_sub(ch,ch,p[a0*m+b0].l);
                }
            }
            mpz_abs(a,cl);
            mpz_abs(b,ch);
            if(mpz_sgn(cl)*mpz_sgn(ch)>0)mpz_add(low[c],low[c],mpz_cmp(a,b)<0?a:b);
            mpz_add(high[c],high[c],mpz_cmp(a,b)>0?a:b);
        }
        for(int b0=0;b0<m;b0++) {
            for(int a0=0;a0<m;a0++) {
                combine(tmp+a0*m+b0,p+b0,m,a0);
            }
        }
        for(int a0=0;a0<m;a0++) {
            for(int b0=0;b0<m;b0++) {
                combine(all+card*T+a0*m+b0,tmp+a0*m,1,b0);
            }
        }
        card++;
    }
    mpz_set(threshold,mpz_cmp(low[0],low[1])>0?low[0]:low[1]);
    gmp_printf("THRESHOLD %Zd %Zd\n",threshold,mpz_cmp(high[0],high[1])<0?high[0]:high[1]);
    free_i(p,T);
    free_i(tmp,T);
    free_i(product,2);
    mpz_clears(z,cl,ch,low[0],low[1],high[0],high[1],a,b,NULL);
    return all;
}
static void divide(I*src,I*l,I*r,int axis) {
    I*line=alloc_i(m);
    for(int c=0;c<K;c++)for(int fixed=0;fixed<m;fixed++) {
        for(int t=0;t<m;t++)seti(line+t,src+c*T+(axis?fixed*m+t:t*m+fixed));
        for(int level=0;level<m;level++) {
            int il=axis?fixed*m+level:level*m+fixed,ir=axis?fixed*m+n-level:(n-level)*m+fixed;
            seti(l+c*T+il,line);
            seti(r+c*T+ir,line+n-level);
            for(int t=0;t<n-level;t++) {
                mpz_add(line[t].l,line[t].l,line[t+1].l);
                mpz_fdiv_q_2exp(line[t].l,line[t].l,1);
                mpz_add(line[t].h,line[t].h,line[t+1].h);
                mpz_cdiv_q_2exp(line[t].h,line[t].h,1);
            }
        }
    }
    free_i(line,m);
}
/* Corner membership is propagated combinatorially from the root. */ static void dfs(I*data,char*path,int d,int mask,mpz_t threshold) {
    if(limited||visited>=maxboxes||(double)(clock()-search_start)/CLOCKS_PER_SEC>=limit) {
        limited=1;
        printf("PENDING %s\n",d?path:"-");
        return;
    }
    visited++;
    if(d>maxdepth)maxdepth=d;
    mpz_t mx,a,b,other;
    mpz_inits(mx,a,b,other,NULL);
    mpz_t*bounds=malloc(T*sizeof(mpz_t));
    for(int t=0;t<T;t++) {
        mpz_init(bounds[t]);
        for(int c=0;c<K;c++) {
            I*v=data+c*T+t;
            mpz_abs(a,v->l);
            mpz_abs(b,v->h);
            mpz_add(bounds[t],bounds[t],mpz_cmp(a,b)>0?a:b);
        }
        if(mpz_cmp(bounds[t],mx)>0)mpz_set(mx,bounds[t]);
    }
    int kind=0,which=-1;
    if(mpz_cmp(mx,threshold)<0)kind=1;
    else for(int c=0;c<2;c++)if(mask&(1<<c)) {
        int index=c==0?0:(n%2?n:n*m);
        mpz_set_ui(other,0);
        for(int t=0;t<T;t++)if(t!=index&&mpz_cmp(bounds[t],other)>0)mpz_set(other,bounds[t]);
        if(mpz_cmp(other,threshold)<0) {
            kind=2;
            which=c;
            break;
        }
    }
    for(int t=0;t<T;t++) {
        mpz_clear(bounds[t]);
    }
    free(bounds);
    if(kind==1) {
        gmp_printf("BOUND %s %Zd\n",d?path:"-",mx);
        bound_count++;
    }
    else if(kind==2) {
        gmp_printf("CORNER %s %d %Zd\n",d?path:"-",which,other);
        corner_count++;
    }
    else if(d>=depthlimit) {
        limited=1;
        printf("PENDING %s\n",d?path:"-");
    }
    else {
        if(!right_tables[d])right_tables[d]=alloc_i((size_t)K*T);
        I *r=right_tables[d];
        /* Every complete source line is copied before writing its left half. */
        divide(data,data,r,d%2);
        splits++;
        int lm=mask,rm=mask;
        /* c0 always low/low; c1 is low/high (odd), high/low (even). */rm&=~1;
        int high=(n%2?d%2==1:d%2==0);
        if(high)lm&=~2;
        else rm&=~2;
        path[d]='0';
        path[d+1]=0;
        dfs(data,path,d+1,lm,threshold);
        path[d]='1';
        dfs(r,path,d+1,rm,threshold);
        path[d]=0;
    }
    mpz_clears(mx,a,b,other,NULL);
}
int main(int argc,char**argv) {
    if(argc!=5)return 2;
    limit=atof(argv[1]);
    maxboxes=atol(argv[2]);
    depthlimit=atoi(argv[3]);
    FILE*f=fopen(argv[4],"r");
    if(!f)return 2;
    if(fscanf(f,"%d",&n)!=1||n<2||n>100)return 2;
    m=n+1;
    T=m*m;
    K=m*(n+2)/2;
    mpz_init_set_ui(S,1);
    mpz_mul_2exp(S,S,192);
    X=alloc_i(m);
    Y=alloc_i(m+1);
    for(int j=0;j<m;j++)gmp_fscanf(f,"%Zd %Zd",X[j].l,X[j].h);
    for(int j=0;j<=m;j++)gmp_fscanf(f,"%Zd %Zd",Y[j].l,Y[j].h);
    C=malloc(T*sizeof(mpz_t));
    W=malloc(T*sizeof(mpq_t));
    for(int t=0;t<T;t++) {
        mpz_init(C[t]);
        gmp_fscanf(f,"%Zd",C[t]);
    }
    for(int t=0;t<T;t++) {
        mpq_init(W[t]);
        gmp_fscanf(f,"%Qd",W[t]);
        mpq_canonicalize(W[t]);
    }
    fclose(f);
    mpz_t threshold;
    mpz_init(threshold);
    clock_t start=clock();
    I*data=construct(threshold);
    const char*dump=getenv("PADUA_DUMP_INITIAL");
    if(dump) {
        FILE*out=fopen(dump,"w");
        if(!out)return 2;
        for(size_t t=0;t<(size_t)K*T;t++)gmp_fprintf(out,"%Zd %Zd\n",data[t].l,data[t].h);
        fclose(out);
    }
    printf("SETUP_SECONDS %.9f\n",(double)(clock()-start)/CLOCKS_PER_SEC);
    fflush(stdout);
    search_start=clock();
    char path[102]= {
        0
    }
    ;
    dfs(data,path,0,3,threshold);
    printf("STATS %ld %ld %ld %ld %d %d %.9f\n",visited,splits,bound_count,corner_count,maxdepth,limited,(double)(clock()-search_start)/CLOCKS_PER_SEC);
    free_i(data,(size_t)K*T);
    for(int d=0;d<101;d++)if(right_tables[d])free_i(right_tables[d],(size_t)K*T);
    return 0;
}
