/* Candidate outward first-order implementation; independent review pending. */
#include "c02_interval.h"
typedef struct { I f,a,b; I c; } J;
static I corrected_value(int n,I u,I v){
 I rs,ds,rt,dt,qs,es,qt,et;
 fixed_pair(n+1,scale(add(u,v),.5),&rs,&ds);fixed_pair(n+1,scale(sub(u,v),.5),&rt,&dt);
 fixed_pair(n,scale(add(u,v),.5),&qs,&es);fixed_pair(n,scale(sub(u,v),.5),&qt,&et);
 return sub(add(mul(rs,rt),mul(qs,qt)),trig(scale(u,n),1));
}
static J kernel(int n,I u,I v,I uc,I vc){
 I s=scale(add(u,v),.5),t=scale(sub(u,v),.5),rs,rt,qs,qt,rsp,rtp,qsp,qtp;
 fixed_pair(n+1,s,&rs,&rsp);fixed_pair(n+1,t,&rt,&rtp);fixed_pair(n,s,&qs,&qsp);fixed_pair(n,t,&qt,&qtp);
 I ds=add(mul(rsp,rt),mul(qsp,qt)),dt=add(mul(rs,rtp),mul(qs,qtp));J z;
 z.f=sub(add(mul(rs,rt),mul(qs,qt)),trig(scale(u,n),1));
 z.a=divide(add(scale(add(ds,dt),.5),scale(trig(scale(u,n),0),n)),iv(n,n));
 z.b=divide(scale(sub(ds,dt),.5),iv(n+1,n+1));z.c=corrected_value(n,uc,vc);return z;
}
static J jsum(J x,J y){J z={add(x.f,y.f),add(x.a,y.a),add(x.b,y.b),add(x.c,y.c)};return z;}
static I adabs(I f,I d){if(f.lo>0)return d;if(f.hi<0)return neg(d);return iv(-maxabs(d),maxabs(d));}
typedef struct {double c,natural;I a,b;} A;
static void accum(A *q,J h){q->c=up(q->c+maxabs(h.c));q->natural=up(q->natural+maxabs(h.f));q->a=add(q->a,adabs(h.f,h.a));q->b=add(q->b,adabs(h.f,h.b));}
static double upper(A q,double ra,double rb){return fmin(q.natural,up(up(q.c+up(maxabs(q.a)*ra))+up(maxabs(q.b)*rb)));}
int n3_box(int n,double al,double ah,double bl,double bh,double lc,double eps,int local,double *out){
 c02_fault=0;newbox();
 if(n<2||n>512||!valid(iv(al,ah))||!valid(iv(bl,bh))||!isfinite(lc)||!isfinite(eps)||eps<0||(local!=0&&local!=1))return 3;
 int m=n+1,nr=2*n,ns=2*m;double norm=2.0*n*m; I pi=pii();double ca=al+(ah-al)/2,cb=bl+(bh-bl)/2;double ra=fmax(up(ca-al),up(ah-ca)),rb=fmax(up(cb-bl),up(bh-cb));
 J *h=calloc((size_t)nr*ns,sizeof(J));if(!h)return 1;
 A sq={0,0,{0,0},{0,0}},cq=sq;
 for(int r=0;r<nr;r++)for(int s=1-r%2;s<ns;s+=2){I ur=scale(pi,r),vs=scale(pi,s);J z=kernel(n,divide(add(ur,iv(al,ah)),iv(n,n)),divide(add(vs,iv(bl,bh)),iv(m,m)),divide(add(ur,iv(ca,ca)),iv(n,n)),divide(add(vs,iv(cb,cb)),iv(m,m)));h[(size_t)r*ns+s]=z;accum(&sq,z);}
 double su=up(upper(sq,ra,rb)/norm),threshold=dn(lc-eps);
 out[0]=su;out[1]=su;out[2]=0;out[3]=0;out[4]=up(sq.natural/norm);out[5]=out[4];
 if(c02_fault||!isfinite(su)){free(h);return 2;}
 if(su<threshold){c02_stat[5]++;free(h);return 0;}
 for(int r=0;r<nr;r++)for(int s=1-r%2;s<ns;s+=2){int rr=(nr-r)%nr,ss=(ns-s)%ns;J z=jsum(jsum(h[(size_t)r*ns+s],h[(size_t)rr*ns+s]),jsum(h[(size_t)r*ns+ss],h[(size_t)rr*ns+ss]));accum(&cq,z);}
 double cu=up(upper(cq,ra,rb)/(4*norm));out[1]=cu;out[5]=up(cq.natural/(4*norm));
 if(!isfinite(cu)){free(h);return 2;}
 if(!local&&cu>=threshold){free(h);return 0;}
 if(n>=64&&full_half_radius(al,ah,bl,bh)){out[2]=1./2048;out[3]=1;c02_stat[6]++;free(h);return 0;}
 c02_stat[7]++;
 /* Reuse the rigorous mathematical pair-defect predicate; floating intervals
    here are only diagnostics. Take maximum with analytic constant. */
 double lowconstant=0;

 double *qh=calloc(n+1,sizeof(double)),*qv=calloc(m+1,sizeof(double));if(!qh||!qv){free(qh);free(qv);free(h);return 1;}
 for(int k=0;k<=m;k++){double v=0;for(int r=0;r<nr;r++)for(int s=1-r%2;s<ns;s+=2)v=dn(v+pairlower(h[(size_t)r*ns+s].f,h[(size_t)r*ns+(2*k-s+ns)%ns].f));qv[k]=dn(v/(2*norm));}
 for(int j=0;j<=n;j++){double v=0;for(int r=0;r<nr;r++)for(int s=1-r%2;s<ns;s+=2)v=dn(v+pairlower(h[(size_t)r*ns+s].f,h[(size_t)((2*j-r+nr)%nr)*ns+s].f));qh[j]=dn(v/(2*norm));}
 double low=HUGE_VAL;
 for(int j=0;j<=n;j++){I ja=add(scale(pi,j),iv(al,ah));if(ja.hi<0||ja.lo>up(n*pi.hi))continue;for(int k=1-j%2;k<=m;k+=2){I kb=add(scale(pi,k),iv(bl,bh));if(kb.hi<0||kb.lo>up(m*pi.hi))continue;if((j==0||j==n)&&(k==0||k==m))continue;low=fmin(low,fmax(qh[j],qv[k]));}}
 out[2]=fmax(0,fmax(lowconstant,low));out[3]=1;free(qh);free(qv);free(h);return !c02_fault&&isfinite(out[2])?0:2;
}
void n3_jet(int n,double al,double ah,double bl,double bh,double *out){c02_fault=0;if(n<2||n>512||!valid(iv(al,ah))||!valid(iv(bl,bh))){for(int i=0;i<6;i++)out[i]=NAN;return;}J z=kernel(n,iv(al,ah),iv(bl,bh),iv(al,ah),iv(bl,bh));out[0]=z.f.lo;out[1]=z.f.hi;out[2]=z.a.lo;out[3]=z.a.hi;out[4]=z.b.lo;out[5]=z.b.hi;}

void n3_constants(int n,double *out){c02_fault=0;if(n<2||n>512){for(int i=0;i<4;i++)out[i]=NAN;return;}I pi=pii();out[0]=pi.lo;out[1]=pi.hi;I total=iv(0,0);int m=n+1;for(int r=0;r<2*n;r++)for(int s=1-r%2;s<2*m;s+=2){I z=corrected_value(n,divide(scale(pi,r),iv(n,n)),divide(scale(pi,s),iv(m,m)));total=add(total,iv(minabs(z),maxabs(z)));}total=divide(total,iv(2.0*n*m,2.0*n*m));out[2]=total.lo;out[3]=total.hi;if(c02_fault){out[2]=out[3]=NAN;}}
int n3_geometry(int n,double al,double ah,double bl,double bh){if(n<2||n>512||!valid(iv(al,ah))||!valid(iv(bl,bh)))return 3;I pi=pii();double mina=(al<=0&&ah>=0)?0:fmin(fabs(al),fabs(ah)),minb=(bl<=0&&bh>=0)?0:fmin(fabs(bl),fabs(bh));if(dn(mina+minb)>pi.hi)return 1;double aa=fmax(fabs(al),fabs(ah)),bb=fmax(fabs(bl),fabs(bh));I x=trig(divide(iv(aa,aa),iv(2*n,2*n)),0),y=trig(divide(iv(bb,bb),iv(2*(n+1),2*(n+1))),0);I h=scale(add(mul(x,x),mul(y,y)),2);I N=iv((double)n*(n+1),(double)n*(n+1));I radius=divide(iv(1,1),scale(mul(mul(N,N),N),2));I r2=divide(iv(1,1),mul(iv(100000000000.,100000000000.),iv(n*n,n*n)));
return h.hi<=fmax(radius.lo,r2.lo)?2:0;}
const char *n3_mpfr_version(void){return mpfr_get_version();}

int c02_ratio(int k,int turn,double lo,double hi,double*out){
 c02_fault=0;if(turn< -4||turn>4||!valid(iv(lo,hi))||k<1||k>513)return 3;
 I r,d;fixed_pair(k,add(scale(pii(),turn),iv(lo,hi)),&r,&d);out[0]=r.lo;out[1]=r.hi;out[2]=d.lo;out[3]=d.hi;return c02_fault?2:0;
}
int c02_guard(int n,double al,double ah,double bl,double bh){return n>=64&&n<=512&&valid(iv(al,ah))&&valid(iv(bl,bh))&&full_half_radius(al,ah,bl,bh);}
int c02_stage_control(int which,double*out){c02_fault=0;I r=iv(1,1),d=iv(0,0),v=iv(1,1),g=iv(0,0);if(which==0)v=iv(NAN,NAN);else if(which==1)g=iv(NAN,NAN);else if(which==2)v=iv(2,2);else return 3;paired(&r,&d,v,g);out[0]=r.lo;out[1]=r.hi;out[2]=d.lo;out[3]=d.hi;return c02_fault?2:0;}
void c02_counts(double*out){for(int i=0;i<8;i++){out[i]=c02_stat[i];c02_stat[i]=0;}}
