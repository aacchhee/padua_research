/* Outward PD-T227 corner-energy producer, not an independent checker.
 * Build example is in attempts/N3-corner.md. No binary64 arithmetic enters
 * any endpoint or acceptance predicate. MPFR -> exact GMP rational output.
 * Formula O(n^2), memory O(n), at the canonical physical corner (-1,-1).
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <time.h>
#include <gmp.h>
#include <mpfr.h>

typedef struct { mpfr_t lo, hi; } iv;
static mpfr_prec_t precision;
static void init(iv *x) { mpfr_init2(x->lo,precision); mpfr_init2(x->hi,precision); }
static void clear(iv *x) { mpfr_clear(x->lo); mpfr_clear(x->hi); }
static void copy(iv *r,const iv *a) { mpfr_set(r->lo,a->lo,MPFR_RNDD); mpfr_set(r->hi,a->hi,MPFR_RNDU); }
static void rational(iv *r,long a,unsigned long b) {
  mpq_t q; mpq_init(q); mpq_set_si(q,a,b); mpq_canonicalize(q);
  mpfr_set_q(r->lo,q,MPFR_RNDD); mpfr_set_q(r->hi,q,MPFR_RNDU); mpq_clear(q);
}
/* Each operation supports aliasing by filling a temporary before copying. */
static void add(iv *r,const iv *a,const iv *b) {
  iv t; init(&t); mpfr_add(t.lo,a->lo,b->lo,MPFR_RNDD);
  mpfr_add(t.hi,a->hi,b->hi,MPFR_RNDU); copy(r,&t); clear(&t);
}
static void sub(iv *r,const iv *a,const iv *b) {
  iv t; init(&t); mpfr_sub(t.lo,a->lo,b->hi,MPFR_RNDD);
  mpfr_sub(t.hi,a->hi,b->lo,MPFR_RNDU); copy(r,&t); clear(&t);
}
static void mul(iv *r,const iv *a,const iv *b) {
  iv t; mpfr_t p; init(&t); mpfr_init2(p,precision);
  mpfr_mul(t.lo,a->lo,b->lo,MPFR_RNDD);
  mpfr_mul(p,a->lo,b->hi,MPFR_RNDD); if(mpfr_less_p(p,t.lo)) mpfr_set(t.lo,p,MPFR_RNDD);
  mpfr_mul(p,a->hi,b->lo,MPFR_RNDD); if(mpfr_less_p(p,t.lo)) mpfr_set(t.lo,p,MPFR_RNDD);
  mpfr_mul(p,a->hi,b->hi,MPFR_RNDD); if(mpfr_less_p(p,t.lo)) mpfr_set(t.lo,p,MPFR_RNDD);
  mpfr_mul(t.hi,a->lo,b->lo,MPFR_RNDU);
  mpfr_mul(p,a->lo,b->hi,MPFR_RNDU); if(mpfr_greater_p(p,t.hi)) mpfr_set(t.hi,p,MPFR_RNDU);
  mpfr_mul(p,a->hi,b->lo,MPFR_RNDU); if(mpfr_greater_p(p,t.hi)) mpfr_set(t.hi,p,MPFR_RNDU);
  mpfr_mul(p,a->hi,b->hi,MPFR_RNDU); if(mpfr_greater_p(p,t.hi)) mpfr_set(t.hi,p,MPFR_RNDU);
  copy(r,&t); mpfr_clear(p); clear(&t);
}
static void divide(iv *r,const iv *a,const iv *b) {
  if(mpfr_sgn(b->lo)<=0 && mpfr_sgn(b->hi)>=0) {
    fprintf(stderr,"division by interval containing zero\n"); exit(2);
  }
  iv t; init(&t); mpfr_ui_div(t.lo,1,b->hi,MPFR_RNDD);
  mpfr_ui_div(t.hi,1,b->lo,MPFR_RNDU); mul(r,a,&t); clear(&t);
}
static void square(iv *r,const iv *a) {
  iv t; init(&t);
  if(mpfr_sgn(a->lo)>=0) { mpfr_sqr(t.lo,a->lo,MPFR_RNDD); mpfr_sqr(t.hi,a->hi,MPFR_RNDU); }
  else if(mpfr_sgn(a->hi)<=0) { mpfr_sqr(t.lo,a->hi,MPFR_RNDD); mpfr_sqr(t.hi,a->lo,MPFR_RNDU); }
  else {
    mpfr_set_zero(t.lo,0); mpfr_sqr(t.hi,a->lo,MPFR_RNDU);
    mpfr_t p; mpfr_init2(p,precision); mpfr_sqr(p,a->hi,MPFR_RNDU);
    if(mpfr_greater_p(p,t.hi)) mpfr_set(t.hi,p,MPFR_RNDU);
    mpfr_clear(p);
  }
  copy(r,&t); clear(&t);
}
static void absolute(iv *r,const iv *a) {
  if(mpfr_sgn(a->lo)>=0) { copy(r,a); return; }
  if(mpfr_sgn(a->hi)<=0) {
    iv t; init(&t); mpfr_neg(t.lo,a->hi,MPFR_RNDD);
    mpfr_neg(t.hi,a->lo,MPFR_RNDU); copy(r,&t); clear(&t); return;
  }
  fprintf(stderr,"absolute value requires separated sign\n"); exit(2);
}
static void scale(iv *r,const iv *a,long p,unsigned long q) {
  iv t; init(&t); rational(&t,p,q); mul(r,a,&t); clear(&t);
}
static void cosine_node(iv *r,unsigned j,unsigned n,const iv *pi) {
  if(j==0) { rational(r,1,1); return; }
  if(j==n) { rational(r,-1,1); return; }
  if(2*j==n) { rational(r,0,1); return; }
  iv t; init(&t); scale(&t,pi,j,n);
  /* Interior angle interval lies strictly in (0,pi); cos decreases there. */
  if(mpfr_sgn(t.lo)<=0 || mpfr_cmp(t.hi,pi->lo)>=0) {
    fprintf(stderr,"cosine monotonicity guard failed\n"); exit(2);
  }
  mpfr_cos(r->lo,t.hi,MPFR_RNDD); mpfr_cos(r->hi,t.lo,MPFR_RNDU); clear(&t);
}
static void printq(const char *name,const mpq_t q,int comma) {
  printf("  \"%s\": \"",name); mpq_out_str(stdout,10,q);
  printf("\"%s\n",comma?",":"");
}
int main(int argc,char **argv) {
  if(argc<2 || argc>4) { fprintf(stderr,"usage: %s n [precision=256] [term-output.csv]\n",argv[0]); return 2; }
  unsigned long ni=strtoul(argv[1],NULL,10);
  precision=argc>=3?(mpfr_prec_t)strtoul(argv[2],NULL,10):256;
  if(ni<2 || ni>10000 || precision<128 || precision>16384) return 2;
  unsigned n=(unsigned)ni,m=n+1;
  FILE *terms=NULL;
  if(argc==4) { terms=fopen(argv[3],"w"); if(!terms) return 2;
    fputs("j,k,value_lo,value_hi,qx_lo,qx_hi,qy_lo,qy_hi,energy_lo,energy_hi\n",terms); }
  clock_t start=clock();
  iv pi,one,a,b,C,d,ad,d2,ab,t0,t1,t2,t3,qx,qy,V,energy,Lsum,Wsum;
  iv *vars[]={&pi,&one,&a,&b,&C,&d,&ad,&d2,&ab,&t0,&t1,&t2,&t3,&qx,&qy,&V,&energy,&Lsum,&Wsum};
  for(unsigned i=0;i<sizeof(vars)/sizeof(*vars);i++) init(vars[i]);
  mpfr_const_pi(pi.lo,MPFR_RNDD); mpfr_const_pi(pi.hi,MPFR_RNDU); rational(&one,1,1);
  rational(&Lsum,0,1); rational(&Wsum,0,1);
  iv *xs=calloc(n+1,sizeof(iv)),*ys=calloc(m+1,sizeof(iv));
  if(!xs || !ys) return 2;
  for(unsigned j=0;j<=n;j++) { init(&xs[j]); cosine_node(&xs[j],j,n,&pi); }
  for(unsigned k=0;k<=m;k++) { init(&ys[k]); cosine_node(&ys[k],k,m,&pi); }
  unsigned nonzero=0,zero=0;
  for(unsigned j=0;j<=n;j++) for(unsigned k=j%2;k<=m;k+=2) {
    if(k==0 && j>0) { zero++; continue; } /* exact zero mask, never divide */
    nonzero++;
    if(j==0 && k==0) {
      /* Explicit removable case. q=L'/L, so parity signs cancel. */
      rational(&V,1,m); rational(&qx,-(2L*n*n+1),6);
      rational(&qy,-(long)m*(2L*n+1),6);
    } else {
      copy(&a,&xs[j]); copy(&b,&ys[k]); sub(&C,&one,&b); sub(&d,&b,&a);
      if(mpfr_sgn(C.lo)<=0) { fprintf(stderr,"nonpositive C\n"); return 2; }
      int expected=((long)m*j-(long)n*k)>0?1:-1;
      if((expected>0 && mpfr_sgn(d.lo)<=0) || (expected<0 && mpfr_sgn(d.hi)>=0)) {
        fprintf(stderr,"denominator sign guard failed at %u,%u\n",j,k); return 2;
      }
      absolute(&ad,&d); divide(&V,&C,&ad);
      /* 2w = 4 epsilon_j eta_k/[n(n+1)]. */
      unsigned weight_den=n*m*(j==0||j==n?2:1)*(k==0||k==m?2:1);
      scale(&V,&V,4,weight_den);
      square(&d2,&d); mul(&ab,&a,&b); sub(&ab,&ab,&one);
      mul(&t0,&C,&d); divide(&t0,&ab,&t0); scale(&t0,&t0,n,1);
      /* qx=-n^2/2+n(ab-1)/(Cd)-a/d+2(1-a^2)/d^2. */
      rational(&qx,-(long)n*n,2); add(&qx,&qx,&t0);
      divide(&t1,&a,&d); sub(&qx,&qx,&t1);
      square(&t1,&a); sub(&t1,&one,&t1); divide(&t1,&t1,&d2);
      scale(&t1,&t1,2,1); add(&qx,&qx,&t1);
      /* qy=-m^2/2+n(ab-1)/(Cd)+(1+2b)/d+2(1-b^2)/d^2. */
      rational(&qy,-(long)m*m,2); add(&qy,&qy,&t0);
      scale(&t1,&b,2,1); add(&t1,&one,&t1); divide(&t1,&t1,&d); add(&qy,&qy,&t1);
      square(&t1,&b); sub(&t1,&one,&t1); divide(&t1,&t1,&d2);
      scale(&t1,&t1,2,1); add(&qy,&qy,&t1);
    }
    square(&t1,&qx); square(&t2,&qy); add(&energy,&t1,&t2); mul(&energy,&energy,&V);
    add(&Lsum,&Lsum,&V); add(&Wsum,&Wsum,&energy);
    if(terms) {
      fprintf(terms,"%u,%u",j,k);
      iv *out[]={&V,&qx,&qy,&energy};
      mpq_t q; mpq_init(q);
      for(unsigned t=0;t<4;t++) {
        fputc(',',terms); mpfr_get_q(q,out[t]->lo); mpq_out_str(terms,10,q);
        fputc(',',terms); mpfr_get_q(q,out[t]->hi); mpq_out_str(terms,10,q);
      }
      fputc('\n',terms); mpq_clear(q);
    }
  }
  if(terms) fclose(terms);
  mpq_t ell,ell_hi,E,Elo,u,n4,bup,Kup,kappa,H,q,phase_r,phase_sq;
  mpq_inits(ell,ell_hi,E,Elo,u,n4,bup,Kup,kappa,H,q,phase_r,phase_sq,NULL);
  mpfr_get_q(ell,Lsum.lo); mpfr_get_q(ell_hi,Lsum.hi);
  mpfr_get_q(E,Wsum.hi); mpfr_get_q(Elo,Wsum.lo);
  unsigned c=0,pow2=1; while(pow2<m) {pow2*=2;c++;}
  mpq_set_ui(u,110UL*(1+c)*(1+c),1);
  mpq_set_ui(n4,(unsigned long)n*n*n*n,1);
  mpq_mul(q,n4,ell); mpq_div(bup,E,q); mpq_div(Kup,u,ell);
  mpq_set_ui(q,3,1); mpq_mul(q,q,Kup); mpq_add(q,q,bup);
  mpq_set_ui(kappa,1,8); mpq_div(kappa,kappa,q);
  if(mpq_cmp_ui(kappa,1,1)>0) mpq_set_ui(kappa,1,1);
  mpq_set_ui(q,(unsigned long)n*n,1); mpq_div(H,kappa,q);
  /* A 40-bit dyadic symmetric scaled-phase radius, rounded down exactly. */
  mpq_set_ui(q,2UL*m*m,(unsigned long)m*m+(unsigned long)n*n);
  mpq_mul(phase_sq,kappa,q);
  mpz_t radicand,root,den; mpz_inits(radicand,root,den,NULL);
  mpz_mul_2exp(radicand,mpq_numref(phase_sq),80);
  mpz_fdiv_q(radicand,radicand,mpq_denref(phase_sq)); mpz_sqrt(root,radicand);
  mpz_set_ui(den,1); mpz_mul_2exp(den,den,40);
  mpq_set_num(phase_r,root); mpq_set_den(phase_r,den); mpq_canonicalize(phase_r);
  printf("{\n  \"schema\": \"n3-corner-energy-v1\",\n  \"degree\": %u,\n  \"precision_bits\": %ld,\n",n,(long)precision);
  printf("  \"nonzero_cardinals\": %u,\n  \"zero_cardinals_omitted\": %u,\n",nonzero,zero);
  printf("  \"mpfr_version\": \"%s\",\n  \"gmp_version\": \"%s\",\n",mpfr_get_version(),gmp_version);
  printq("corner_lower",ell,1); printq("corner_upper",ell_hi,1);
  printq("energy_lower",Elo,1); printq("energy_upper",E,1);
  printq("global_norm_upper",u,1); printq("normalized_energy_upper",bup,1);
  printq("global_corner_ratio_upper",Kup,1); printq("kappa",kappa,1);
  printq("physical_H_radius",H,1); printq("symmetric_scaled_phase_radius",phase_r,1);
  printf("  \"cpu_seconds_diagnostic\": %.6f\n}\n",(double)(clock()-start)/CLOCKS_PER_SEC);
  for(unsigned j=0;j<=n;j++) clear(&xs[j]);
  for(unsigned k=0;k<=m;k++) clear(&ys[k]);
  free(xs);free(ys);for(unsigned i=0;i<sizeof(vars)/sizeof(*vars);i++) clear(vars[i]);
  mpq_clears(ell,ell_hi,E,Elo,u,n4,bup,Kup,kappa,H,q,phase_r,phase_sq,NULL);
  mpz_clears(radicand,root,den,NULL); return 0;
}
