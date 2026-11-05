// P6 speed pilot: phase instrumentation of unchanged scalar arithmetic.
// Separate scalar rational arithmetic; weighted formulas from P4-02.
#include <gmpxx.h>
#include <vector>
#include <string>
#include <iostream>
#include <stdexcept>
#include <chrono>
#include <fstream>
using Q=mpq_class; using V=std::vector<Q>;
Q rat(long a,long b){Q q(a,b); q.canonicalize();return q;}
Q rawdot(const V&a,const V&b){Q s=0;for(size_t i=0;i<a.size();++i)s+=a[i]*b[i];return s;}
V weights;
Q dot(const V&a,const V&b){Q s=0;for(size_t i=0;i<a.size();++i)s+=weights[i]*a[i]*b[i];return s;}
// Explicit integer cross products, including exact ties.
int cmp(const Q&a,const Q&b){mpz_class z=a.get_num()*b.get_den()-b.get_num()*a.get_den();return mpz_sgn(z.get_mpz_t());}
void require(bool b,const char*m){if(!b)throw std::runtime_error(m);}
struct Step{int axis,parent;V alpha;Q sigma;};
int main(int argc,char**argv){try{
 require(argc==5,"usage: executable input.txt maxdegree bj|mirror|alt|pivot family");
 std::string grid=argv[4],rule=argv[3];int degree=std::stoi(argv[2]);
 require(degree>=2&&degree<=20,"degree outside 2..20");
 require(rule=="bj"||rule=="mirror"||rule=="alt"||rule=="pivot","invalid rule");
 auto start=std::chrono::steady_clock::now();V x,y;Q weight=0;
 std::ifstream input(argv[1]);require(input.good(),"cannot open input");int M;input>>M;require(M>0&&M<=10000,"invalid point count");
 for(int i=0;i<M;++i){Q a,b,w;input>>a>>b>>w;require(input.good()&&w>0,"invalid input row");a.canonicalize();b.canonicalize();w.canonicalize();weight+=w;weights.push_back(w);x.push_back(a);y.push_back(b);}
 std::string extra;require(!(input>>extra),"extra input tokens");
 require(weight==1,"normalized weights required");
 int N=(degree+1)*(degree+2)/2;require(M>N,"M must exceed N");
 std::vector<V>B(1,V(M,1));V d(1,Q(1));std::vector<Step> steps(1);std::vector<int> ends(degree+1);std::vector<std::vector<int>> index(degree+1);index[0]={0};ends[0]=1;
 std::string choices;std::vector<std::pair<int,int>>ties;long gram=0;
 for(int t=1;t<=degree;++t){for(int j=0;j<=t;++j){
  std::vector<Step> cs;std::vector<V> residues;V norms;
  for(int a=0;a<2;++a){if((a==0&&j==t)||(a==1&&j==0))continue;
   int wanted=rule=="bj"?(j==0?0:1):rule=="mirror"?(j!=t?0:1):(2*j<t?0:1);
   if(rule!="pivot"&&a!=wanted)continue;
   int p=index[t-1][j-a];const V&coord=a?y:x;V z(M),alpha;
   for(int i=0;i<M;++i)z[i]=coord[i]*B[p][i];Q sigma=dot(z,z);require(sigma>0,"nonpositive source scale");
   for(size_t l=0;l<B.size();++l)alpha.push_back(dot(B[l],z)/d[l]);V r=z;
   for(size_t l=0;l<B.size();++l)if(alpha[l]!=0)for(int i=0;i<M;++i)r[i]-=alpha[l]*B[l][i];
   Q norm=dot(r,r);require(norm>0,"nonpositive pivot");cs.push_back({a,p,alpha,sigma});residues.push_back(std::move(r));norms.push_back(norm);
  }
  require(!cs.empty(),"missing parent");int pick=0;
  if(cs.size()==2){int c=cmp(norms[0]/cs[0].sigma,norms[1]/cs[1].sigma);if(c==0)ties.push_back({t,j});if(c<0)pick=1;}
  V r=residues[pick];for(size_t l=0;l<B.size();++l){require(dot(r,B[l])==0,"off-diagonal Gram failure");++gram;}
  index[t].push_back(B.size());B.push_back(std::move(r));d.push_back(norms[pick]);steps.push_back(cs[pick]);choices+=cs[pick].axis?'Y':'X';
 }
 ends[t]=B.size();std::cerr<<"basis "<<grid<<" "<<rule<<" "<<t<<"\n";
 }
 require((int)B.size()==N,"basis dimension mismatch");
 auto basis_end=std::chrono::steady_clock::now();
 std::cerr<<"phase_basis_seconds "<<std::chrono::duration<double>(basis_end-start).count()<<"\n";
 // At each prefix store sum_h v_hi and max_h v_hi; normal factor is h-independent.
 std::vector<V> totals(degree+1,V(M)),maxima(degree+1,V(M));
 for(int h=1;h<N;++h){std::vector<V>g(N);g[h]=V(M,1);V energy(M,1/d[h]);
  for(int k=h;k<N;++k){if(k>h){const Step&s=steps[k];g[k]=V(M);const V&coord=s.axis?y:x;
    if(s.parent>=h)for(int i=0;i<M;++i)g[k][i]=coord[i]*g[s.parent][i];
    for(int l=h;l<k;++l)if(s.alpha[l]!=0)for(int i=0;i<M;++i)g[k][i]-=s.alpha[l]*g[l][i];
    for(int i=0;i<M;++i)energy[i]+=g[k][i]*g[k][i]/d[k];}
   for(int s=2;s<=degree;++s)if(k+1==ends[s])for(int i=0;i<M;++i){Q v=steps[h].sigma*energy[i];totals[s][i]+=v;if(cmp(v,maxima[s][i])>0)maxima[s][i]=v;}
  }
  std::cerr<<"source "<<h<<"/"<<N-1<<"\n";
 }
 auto source_end=std::chrono::steady_clock::now();
 std::cerr<<"phase_source_seconds "<<std::chrono::duration<double>(source_end-basis_end).count()<<"\n";
 for(int s=2;s<=degree;++s){Q lo=0,hs=0,row=0,trace=0;int ns=ends[s];
  for(int i=0;i<M;++i){Q normal=1;for(int k=0;k<ns;++k)normal-=weights[i]*B[k][i]*B[k][i]/d[k];require(normal>=0&&normal<=1,"invalid projector diagonal");trace+=normal;
   Q a=normal*maxima[s][i];if(cmp(a,lo)>0)lo=a;hs+=normal*totals[s][i];if(cmp(totals[s][i],row)>0)row=totals[s][i];}
  require(trace==M-ns,"projector trace mismatch");Q upper=cmp(hs,row)<0?hs:row;require(lo>0&&cmp(lo,upper)<=0,"endpoint order failure");
  std::cout<<"{\"set\":\""<<grid<<"\",\"rule\":\""<<rule<<"\",\"degree\":"<<s<<",\"sources\":\"all\",\"source_count\":"<<ns-1<<",\"point_count\":"<<M<<",\"basis_count\":"<<ns<<",\"Knode_squared\":{\"exact\":\""<<lo<<"\"},\"KHS_squared\":{\"exact\":\""<<hs<<"\"},\"Urow_squared\":{\"exact\":\""<<row<<"\"},\"upper_squared\":{\"exact\":\""<<upper<<"\"},\"pivot_choices\":[";
  for(int k=0;k<ns-1;++k){if(k)std::cout<<",";std::cout<<"\""<<choices[k]<<"\"";}std::cout<<"],\"pivot_ties\":[";bool comma=false;for(auto p:ties)if(p.first<=s){if(comma)std::cout<<",";std::cout<<"["<<p.first<<","<<p.second<<"]";comma=true;}
  double seconds=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
  std::cout<<"],\"normal_trace_exact\":\""<<trace<<"\",\"exact_gram_pairs_checked\":"<<gram<<",\"elapsed_seconds\":"<<seconds<<"}"<<std::endl;
 }
 std::cerr<<"phase_finish_seconds "<<std::chrono::duration<double>(std::chrono::steady_clock::now()-source_end).count()<<"\n";
 return 0;
}catch(const std::exception&e){std::cerr<<e.what()<<"\n";return 2;}}
