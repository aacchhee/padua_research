// D07 actual physical lambda point prototype. Frozen C11 arithmetic included.
#include "../cheap_rows_C11/point.cpp"
#include <flint/acb_poly.h>
#include <cstring>
#include <cmath>
struct C7 {acb_t x;C7(){acb_init(x);}~C7(){acb_clear(x);}};
struct P7 {acb_poly_t x;P7(){acb_poly_init(x);}~P7(){acb_poly_clear(x);}};
struct Roots7 {acb_ptr x;long n;Roots7(long n):x(_acb_vec_init(n)),n(n){}~Roots7(){_acb_vec_clear(x,n);}};
using Poly7=std::vector<B>;
struct Count7 {long rows=0,eta=0,fallback=0,rootfail=0,signfail=0,direct=0,blocks=0,partials=0,roots=0,axis=0,node=0,corner=0,maxdirect=0;};
static B sc7(const Q&t,bool cosine){Q two=t*Q(2);if(fmpz_is_one(fmpq_denref(two.x))){long v=floorq(two-Q(4)*Q(floorq(two/Q(4))));long c[]={1,0,-1,0},s[]={0,1,0,-1};return B(cosine?c[v]:s[v]);}Q r=t-Q(2)*Q(floorq(t/Q(2)));return cosine?cosb(pi()*qb(r)):sinb(pi()*qb(r));}
static B g7(long n,const Q&u,const Q&v){B a=ratio((u+v)/Q(2),n+1),b=ratio((u-v)/Q(2),n+1),c=ratio((u+v)/Q(2),n),d=ratio((u-v)/Q(2),n);return a*b+c*d-sc7(Q(n)*u,true);}
static B four7(long n,long r,long j,const Q&xi,const Q&ze){B s;for(long sig:{-1L,1L})for(long tau:{-1L,1L})s=s+g7(n,xi+Q(sig*j)/Q(n),ze+Q(tau*r)/Q(n+1));if(!arb_is_finite(s.x))throw std::runtime_error("finite four-copy failure");return s;}
static B fullrow7(long n,long r,const Q&xi,const Q&ze,Count7&st){B s;for(long j=(1-r%2);j<=n;j+=2){s=s+absolute(four7(n,r,j,xi,ze))/B((j==0||j==n)?2:1);st.direct++;}return s;}
static Poly7 add7(Poly7 a,const Poly7&b){a.resize(std::max(a.size(),b.size()));for(size_t j=0;j<b.size();j++)a[j]=a[j]+b[j];return a;}
static Poly7 mul7(const Poly7&a,const Poly7&b){Poly7 p(a.size()+b.size()-1);for(size_t i=0;i<a.size();i++)for(size_t j=0;j<b.size();j++)p[i+j]=p[i+j]+a[i]*b[j];return p;}
static B eval7(const Poly7&p,const B&x){B a;for(long j=(long)p.size()-1;j>=0;j--)a=a*x+p[j];return a;}
static B absac7(const acb_t z){B a;acb_abs(a.x,z,P);return a;}
// Acb find_roots supplies candidates ONLY. Coverage is certified separately:
// d disjoint disks each satisfy |p1|r > |p0|+sum(j>=2)|pj|r^j.
// Rouche against p1*(z-center) gives one zero for EVERY coefficient member.
static std::vector<B> events7(const Poly7&p,long n,long delta,Count7&st){
 long d=(long)p.size()-1;while(d>=0&&arb_is_zero(p[d].x))d--;if(d<=0)return {};
 if(arb_contains_zero(p[d].x))throw std::runtime_error("uncertain polynomial degree");
 P7 poly;C7 c;for(long j=0;j<=d;j++){acb_set_arb(c.x,p[j].x);acb_poly_set_coeff_acb(poly.x,j,c.x);}
 Roots7 proposed(d),centers(d);acb_poly_find_roots(proposed.x,poly.x,nullptr,32,P);
 B radius=power(B(1)/B(2),60);std::vector<B> events;
 for(long i=0;i<d;i++){
  if(!acb_is_finite(proposed.x+i))throw std::runtime_error("nonfinite root candidate");acb_get_mid(centers.x+i,proposed.x+i);
  P7 shifted;acb_poly_taylor_shift(shifted.x,poly.x,centers.x+i,P);C7 coef;acb_poly_get_coeff_acb(coef.x,shifted.x,0);B rhs=absac7(coef.x);
  acb_poly_get_coeff_acb(coef.x,shifted.x,1);B lhs=absac7(coef.x)*radius;
  for(long j=2;j<=d;j++){acb_poly_get_coeff_acb(coef.x,shifted.x,j);rhs=rhs+absac7(coef.x)*power(radius,j);}
  if(!arb_gt(lhs.x,rhs.x))throw std::runtime_error("Rouche root coverage failed");
  for(long j=0;j<i;j++){C7 diff;acb_sub(diff.x,centers.x+i,centers.x+j,P);if(!arb_gt(absac7(diff.x).x,(B(2)*radius).x))throw std::runtime_error("root disks overlap");}
  B re,im;arb_set(re.x,acb_realref(centers.x+i));arb_set(im.x,acb_imagref(centers.x+i));arb_add_error(re.x,radius.x);arb_add_error(im.x,radius.x);
  if(!arb_contains_zero(im.x)||arb_lt(re.x,B(-1).x)||arb_gt(re.x,B(1).x))continue;
  // Clamp exact outward endpoints, then acos separately to avoid a rounded
  // union extending past [-1,1] before applying the endpoint function.
  arf_t lo,hi;arf_init(lo);arf_init(hi);arb_get_lbound_arf(lo,re.x,P);arb_get_ubound_arf(hi,re.x,P);
  if(arf_cmp_si(lo,-1)<0)arf_set_si(lo,-1);if(arf_cmp_si(hi,1)>0)arf_set_si(hi,1);
  B l,h,al,ah,t;arb_set_arf(l.x,lo);arb_set_arf(h.x,hi);arb_acos(al.x,l.x,P);arb_acos(ah.x,h.x,P);arb_union(t.x,al.x,ah.x,P);arf_clear(lo);arf_clear(hi);
  t=(B(n)*t/pi()-B(delta))/B(2);if(!arb_is_finite(t.x))throw std::runtime_error("root angle failure");events.push_back(t);
 }
 st.roots+=d;return events;
}
static void buffer7(const B&event,long count,std::set<long>&cuts,std::set<long>&direct){
 if(arb_lt(event.x,B(-2).x)||arb_gt(event.x,B(count+1).x))return;
 arf_t a,b;arf_init(a);arf_init(b);arb_get_lbound_arf(a,event.x,P);arb_get_ubound_arf(b,event.x,P);fmpz_t l,h;fmpz_init(l);fmpz_init(h);arf_get_fmpz(l,a,ARF_RND_FLOOR);arf_get_fmpz(h,b,ARF_RND_CEIL);long lo=fmpz_get_si(l)-1,hi=fmpz_get_si(h)+1;arf_clear(a);arf_clear(b);fmpz_clear(l);fmpz_clear(h);
 if(hi-lo>5)throw std::runtime_error("wide event buffer");for(long k=std::max(0L,lo);k<=std::min(count-1,hi);k++){direct.insert(k);cuts.insert(k);cuts.insert(k+1);}
}
static Q fold7(Q x){x=x-Q(2)*Q(floorq(x/Q(2)));return fmpq_cmp_si(x.x,1)>0?Q(2)-x:x;}
static B row7(long n,long r,const Q&xi,const Q&ze,Count7&st){
 long delta=1-r%2,count=(n-delta)/2+1,eps=r%2?1:-1;Q et[2]={ze+Q(r)/Q(n+1),ze-Q(r)/Q(n+1)};
 for(int tau=0;tau<2;tau++)if(fmpz_is_one(fmpq_denref(et[tau].x))){st.eta++;return fullrow7(n,r,xi,ze,st);}
 B a=sc7(xi,true),b=sc7(xi,false),A=sc7(Q(n)*xi,true),E=sc7(Q(n)*xi,false),y[2],k[2],coef[2][2];Poly7 den[2],ell[2],U,Wp;
 for(int t=0;t<2;t++){y[t]=sc7(et[t],true);B sineta=sc7(et[t],false);if(arb_contains_zero(sineta.x))throw std::runtime_error("unresolved eta sine");k[t]=B(eps)*A*(B(1)+y[t])-sc7(Q(n)*et[t],true)-sc7(Q(n+1)*et[t],true);
  den[t]={y[t]*y[t]-b*b,B(-2)*a*y[t],B(1)};ell[t]={B(-2)*(k[t]*y[t]+B(eps)*E*b*a),B(2)*(a*k[t]+B(eps)*E*b*y[t])};
  coef[t][0]=B(eps)*E/B(2)-k[t]/(B(2)*sineta);coef[t][1]=B(eps)*E/B(2)+k[t]/(B(2)*sineta);
 }
 if(fmpq_is_zero(ze.x)){U=ell[0];for(auto&v:U)v=v*B(2);Wp=den[0];st.axis++;}
 else if(fmpq_is_zero(xi.x)){U={B(-2)*(k[0]*y[1]+k[1]*y[0]),B(2)*(k[0]+k[1])};Wp={y[0]*y[1],B()-y[0]-y[1],B(1)};st.axis++;}
 else{U=add7(mul7(ell[0],den[1]),mul7(ell[1],den[0]));Wp=mul7(den[0],den[1]);}
 std::vector<B> events;try{events=events7(U,n,delta,st);}catch(...){st.rootfail++;throw;}
 for(int t=0;t<2;t++)for(long sign:{-1L,1L})events.push_back(qb((Q(n)*fold7(xi+Q(sign)*et[t])-Q(delta))/Q(2)));
 std::set<long>cuts{0,count},direct;
 for(const B&e:events)buffer7(e,count,cuts,direct);
 for(long j:{0L,n})if((j+r)%2){long idx=(j-delta)/2;direct.insert(idx);cuts.insert(idx);cuts.insert(idx+1);}
 if(direct.size()>40)throw std::runtime_error("direct buffer cap");st.maxdirect=std::max(st.maxdirect,(long)direct.size());B total;
 for(long idx:direct){long j=delta+2*idx;total=total+absolute(four7(n,r,j,xi,ze))/B((j==0||j==n)?2:1);st.direct++;}
 bool zero=true;for(const B&v:U)zero=zero&&arb_is_zero(v.x);
 std::vector<long> edges(cuts.begin(),cuts.end());
 for(size_t i=0;i+1<edges.size();i++){long lo=edges[i],hi=edges[i+1]-1;if(lo>hi||direct.count(lo))continue;
  for(const B&e:events)if(!arb_lt(e.x,B(lo).x)&&!arb_gt(e.x,B(hi).x))throw std::runtime_error("event not excluded from block");
  if(zero)continue;B cv=sc7(Q(delta+2*lo)/Q(n),true),nu=eval7(U,cv),de=eval7(Wp,cv);int sign=0;
  if((arb_is_positive(nu.x)&&arb_is_positive(de.x))||(arb_is_negative(nu.x)&&arb_is_negative(de.x)))sign=1;
  if((arb_is_positive(nu.x)&&arb_is_negative(de.x))||(arb_is_negative(nu.x)&&arb_is_positive(de.x)))sign=-1;
  if(!sign){st.signfail++;throw std::runtime_error("uncertified block sign");}
  B sum;for(int t=0;t<2;t++)for(long sig:{-1L,1L})for(int channel=0;channel<2;channel++){
   long j=delta+2*(sig>0?lo:hi);Q turn=(xi+Q(sig*j)/Q(n)+Q(channel?1:-1)*et[t])/Q(2),offset=Q(n)*turn;offset=offset-Q(n)*Q(floorq(offset/Q(n)));
   // partial() checks BOTH endpoint distances. Its whole ball, including
   // CP640/J16, harmonic and WD96 tails, is weighted without truncation.
   B part=partial(n,hi-lo+1,qb(offset));st.partials++;sum=sum+coef[t][channel]*part;
  }
  total=total+B(sign)*sum;st.blocks++;
 }
 return total;
}
static Q parse7(const char*s){if(!s||std::strlen(s)>512)throw std::runtime_error("rational input length");Q q;if(fmpq_set_str(q.x,s,10)||fmpz_is_zero(fmpq_denref(q.x)))throw std::runtime_error("rational parse");fmpq_canonicalise(q.x);if(fmpq_sgn(q.x)<0||fmpq_cmp_si(q.x,1)>0)throw std::runtime_error("inward turn domain");return q;}
static B lambda7(long n,const Q&xi,const Q&ze,Count7&st){if(n<2||n>2048)throw std::runtime_error("native degree range");Q j=Q(n)*xi,r=Q(n+1)*ze;
 if(fmpz_is_one(fmpq_denref(j.x))&&fmpz_is_one(fmpq_denref(r.x))&&(floorq(j)+floorq(r))%2){st.node=1;return B(1);}
 if(fmpq_is_zero(xi.x)&&fmpq_is_zero(ze.x)){Stats s;st.corner=1;return pointS(n,Q(),Q(),s);}
 B total;for(long r=0;r<=n+1;r++){st.rows++;B row;try{row=row7(n,r,xi,ze,st);}catch(...){st.fallback++;row=fullrow7(n,r,xi,ze,st);}total=total+row/B((r==0||r==n+1)?2:1);}
 B ans=total/(B(2)*B(n)*B(n+1));if(!arb_is_finite(ans.x)||arb_is_negative(ans.x))throw std::runtime_error("nonfinite lambda");return ans;
}
static void export7(const B&a,double*out){arf_t f;arf_init(f);arb_get_lbound_arf(f,a.x,P);out[0]=arf_get_d(f,ARF_RND_FLOOR);arb_get_ubound_arf(f,a.x,P);out[1]=arf_get_d(f,ARF_RND_CEIL);out[2]=mag_get_d(arb_radref(a.x));arf_clear(f);if(!std::isfinite(out[0])||!std::isfinite(out[1])||!std::isfinite(out[2]))throw std::runtime_error("binary64 export nonfinite");}
extern "C" int d07_point(long n,const char*xi,const char*ze,double*out,long*counts){try{Count7 st;B ans=lambda7(n,parse7(xi),parse7(ze),st);export7(ans,out);long values[]={st.rows,st.eta,st.fallback,st.rootfail,st.signfail,st.direct,st.blocks,st.partials,st.roots,st.axis,st.node,st.corner,st.maxdirect};for(int i=0;i<13;i++)counts[i]=values[i];return 0;}catch(...){for(int i=0;i<3;i++)out[i]=NAN;return 1;}}
