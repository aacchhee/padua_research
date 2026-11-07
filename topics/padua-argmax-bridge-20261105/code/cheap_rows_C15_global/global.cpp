// C15 coherent global(A,p,q) vertices. C12/C11 dependencies stay unchanged.
#include "box.cpp"
struct Vertex15{B A,p,q;};
struct Stats15{Stats12 row;long vertices=0,successful=0;};
static void domain15(long n,const Q&al,const Q&ah,const Q&bl,const Q&bh){if(sizeof(long)<8||n<2||n>4096L||fmpq_sgn(al.x)<0||fmpq_sgn(bl.x)<0||fmpq_cmp(al.x,ah.x)>0||fmpq_cmp(bl.x,bh.x)>0||fmpq_cmp_si((ah+bh).x,1)>0)throw std::runtime_error("C15 whole rational triangle domain");}
static B centered15(const B&center,B&rho){
 B point;arb_set_arf(point.x,arb_midref(center.x));
 if(arb_gt(point.x,B(5).x))point=B(5);if(arb_lt(point.x,B(-5).x))point=B(-5);
 rho=up12(absolute(center-point));if(!arb_is_finite(point.x)||!arb_is_finite(rho.x))throw std::runtime_error("center calibration");return point;
}
static B global15(long n,const Q&al,const Q&ah,const Q&bl,const Q&bh,Stats15&st,B&freeze,B&cube,B&tail,B&rhoMax,long forceRow=-1,long forceVertex=-1){
 domain15(n,al,ah,bl,bh);if(fmpq_equal(al.x,ah.x)&&fmpq_equal(bl.x,bh.x)&&((!fmpq_cmp_si(al.x,1)&&fmpq_is_zero(bl.x))||(!fmpq_cmp_si(bl.x,1)&&fmpq_is_zero(al.x))))return B(1);
 B af=range12(qb12(al),qb12(ah)),bf=range12(qb12(bl),qb12(bh)),amid=qb12((al+ah)/Q(2)),bmid=qb12((bl+bh)/Q(2)),alpha=pi()*af,beta=pi()*bf,A=cos12(alpha)+cos12(beta),p=sin12(alpha),q=sin12(beta);
 auto av=endpoints12(A,0,2),pv=endpoints12(p,0,1),qv=endpoints12(q,0,1);std::vector<Vertex15>vertices;for(const B&a:av)for(const B&b:pv)for(const B&c:qv)vertices.push_back({a,b,c});st.vertices=vertices.size();if(vertices.empty()||vertices.size()>8)throw std::runtime_error("global vertex family");
 std::vector<B>acc(vertices.size()),epsMax(vertices.size());long m=n+1;B N=B(n)*B(m),rowcap=B(n)*N,common,widthBeta=up12(pi()*qb12(bh-bl));
 for(long r=0;r<2*m;r++){
  if(r==0||r==2*m-1||r==m-1||r==m){B actual;for(long k=0;k<n;k++){actual=actual+absolute(finite12(n,r,k,af,bf,st.row));st.row.retained++;}common=common+min12(actual,rowcap);continue;}
  st.row.ordinary++;
  try{
   long delta=(1-r)%2;if(delta<0)delta+=2;B v=pi()*(B(r)+bf)/B(m);std::set<long>cuts{0,n},actual;
   poleband12((B(n)*v-alpha-B(delta)*pi())/(B(2)*pi()),n,cuts,actual);poleband12((B(n)*(B(2)*pi()-v)-alpha-B(delta)*pi())/(B(2)*pi()),n,cuts,actual);directcut12(0,n,cuts,actual);directcut12(n-1,n,cuts,actual);
   if(actual.size()>8)throw std::runtime_error("actual collision buffer cap");st.row.maxD=std::max(st.row.maxD,(long)actual.size());B actualBuffered;
   for(long k:actual){actualBuffered=actualBuffered+absolute(finite12(n,r,k,af,bf,st.row));st.row.direct++;}
   if((long)actual.size()==n){common=common+min12(actualBuffered,rowcap);continue;}
   // Nothing is committed until EVERY shared vertex succeeds on this row.
   std::vector<B>staged(vertices.size()),epsilon(vertices.size()),rhoRow(vertices.size());B v0=pi()*(B(r)+bmid)/B(m),cos0=cos12(v0),sin0=sin12(v0);
   for(size_t j=0;j<vertices.size();j++){
    if(r==forceRow&&(long)j==forceVertex)throw std::runtime_error("diagnostic staged vertex failure");
    const Vertex15&z=vertices[j];B center=z.A*(B(1)+cos0)+z.q*sin0,ctilde=centered15(center,rhoRow[j]);
    B L=up12(z.A+z.q);epsilon[j]=up12(L*widthBeta/(B(2)*B(m))+rhoRow[j]);
    staged[j]=vertex12(n,r,af,bf,amid,bmid,ctilde,z.p,actual,cuts,st.row);
   }
   common=common+actualBuffered;for(size_t j=0;j<vertices.size();j++){acc[j]=acc[j]+staged[j];epsMax[j]=max12(epsMax[j],epsilon[j]);rhoMax=max12(rhoMax,rhoRow[j]);}st.successful++;
  }catch(const std::exception&){
   // This cap is for the ENTIRE ACTUAL row. Do not retain its buffered
   // terms or substitute an actual cap into any artificial vertex row.
   st.row.fallback++;common=common+rowcap;
  }
 }
 B H=B(1)+logb(B(n)),largest;for(size_t j=0;j<vertices.size();j++){B E=up12(B(2)/pi()*epsMax[j]*H*H);freeze=max12(freeze,E);largest=max12(largest,acc[j]/N+E);}
 B dA=av.back()-av.front(),dp=pv.back()-pv.front(),dq=qv.back()-qv.front();cube=(B(4)/(pi()*pi())*dA+B(2)/pi()*dp)*H*H+B(2)/pi()*dq*H;
 double budget[3];c06_budget(n,n,budget);tail=(point12(budget[0])+B(12)*point12(budget[1])+B(12)*point12(budget[2]))*(B(1)+B(5)*H)/B(n);
 B answer=min12(common/N+largest,B(2)*N);if(!arb_is_finite(answer.x))throw std::runtime_error("global upper nonfinite");return answer;
}
extern "C" int c15_global(long n,const char*al,const char*ah,const char*bl,const char*bh,double*out,long*counts){try{Stats15 st;B freeze,cube,tail,rho;B ans=global15(n,parse12(al),parse12(ah),parse12(bl),parse12(bh),st,freeze,cube,tail,rho);out[0]=upper12(ans);out[1]=upper12(freeze);out[2]=upper12(cube);out[3]=upper12(tail);out[4]=upper12(rho);long c[]={st.row.retained,st.row.direct,st.row.regular,st.row.blocks,st.row.fallback,st.row.ordinary,st.row.maxD,st.row.maxE,st.row.maxBlocks,st.row.ratioFallback,st.vertices,st.successful};for(int j=0;j<12;j++)counts[j]=c[j];return 0;}catch(...){return 1;}}

// Diagnostic only: force the same whole-row rollback before a selected vertex.
// It yields a valid coarse S upper, never a favorable numerical refinement.
extern "C" int c15_fault_probe(long n,const char*al,const char*ah,const char*bl,const char*bh,long row,long vertex,double*out,long*counts){try{if(n<2||n>4096||row<0||row>=2*(n+1)||vertex<0||vertex>=8)return 1;Stats15 st;B freeze,cube,tail,rho;B ans=global15(n,parse12(al),parse12(ah),parse12(bl),parse12(bh),st,freeze,cube,tail,rho,row,vertex);out[0]=upper12(ans);out[1]=upper12(freeze);out[2]=upper12(cube);out[3]=upper12(tail);out[4]=upper12(rho);counts[0]=st.row.fallback;counts[1]=st.vertices;return 0;}catch(...){return 1;}}
