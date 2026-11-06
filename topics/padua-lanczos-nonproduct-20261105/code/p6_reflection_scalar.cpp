// P6 scalar-rational adaptation of predecessor g1_independent.cpp.
// NEW 2026-11-05 sign-reflection method variant, p6-reflection-methods.md.
// Original scalar arithmetic and all full-node basis/endpoint guards retained.
// Source responses only: squared values reused on verified independent-sign orbits.
// Experiments require coordinator approval of the separately written proof.
#include <gmpxx.h>
#include <vector>
#include <string>
#include <iostream>
#include <stdexcept>
#include <chrono>
#include <fstream>
#include <map>
#include <set>
#include <array>
#include <algorithm>
using Q=mpq_class; using V=std::vector<Q>;
Q rat(long a,long b){Q q(a,b); q.canonicalize();return q;}
Q rawdot(const V&a,const V&b){Q s=0;for(size_t i=0;i<a.size();++i)s+=a[i]*b[i];return s;}
V weights;
Q dot(const V&a,const V&b){Q s=0;for(size_t i=0;i<a.size();++i)s+=weights[i]*a[i]*b[i];return s;}
// Explicit integer cross products, including exact ties.
int cmp(const Q&a,const Q&b){mpz_class z=a.get_num()*b.get_den()-b.get_num()*a.get_den();return mpz_sgn(z.get_mpz_t());}
void require(bool b,const char*m){if(!b)throw std::runtime_error(m);}
struct Step{int axis,parent;V alpha;Q sigma;};
struct Reflections{
 std::vector<int> rx,ry,representatives,orbit;
 std::array<long,5> histogram{};
};
Q absq(const Q&q){Q v=q;if(v<0)v=-v;return v;}
Reflections reflectionOrbits(const V&x,const V&y,const V&w){
 require(x.size()==y.size()&&x.size()==w.size(),"reflection input dimensions");
 int M=x.size();Reflections R;R.rx.resize(M);R.ry.resize(M);R.orbit.resize(M,-1);
 std::map<std::pair<Q,Q>,int> nodes;
 for(int i=0;i<M;++i)require(nodes.emplace(std::make_pair(x[i],y[i]),i).second,"duplicate node");
 for(int i=0;i<M;++i){
  auto a=nodes.find({-x[i],y[i]}),b=nodes.find({x[i],-y[i]});
  require(a!=nodes.end()&&b!=nodes.end(),"missing exact reflected node");
  R.rx[i]=a->second;R.ry[i]=b->second;
  require(w[i]==w[R.rx[i]]&&w[i]==w[R.ry[i]],"unequal exact reflected weights");
 }
 std::set<int> imageX(R.rx.begin(),R.rx.end()),imageY(R.ry.begin(),R.ry.end());
 require((int)imageX.size()==M&&(int)imageY.size()==M,"reflection not bijective");
 for(int i=0;i<M;++i)require(R.rx[R.rx[i]]==i&&R.ry[R.ry[i]]==i&&R.rx[R.ry[i]]==R.ry[R.rx[i]],"reflection involution/commutation");
 std::map<std::pair<Q,Q>,std::set<int>> classes;
 for(int i=0;i<M;++i)classes[{absq(x[i]),absq(y[i])}].insert(i);
 int assigned=0;
 for(const auto&item:classes){
  const auto&members=item.second;int representative=*members.begin();
  std::set<int> generated={representative,R.rx[representative],R.ry[representative],R.rx[R.ry[representative]]};
  require(generated==members,"absolute-key class is not the exact reflection orbit");
  require(members.size()==1||members.size()==2||members.size()==4,"invalid reflection orbit size");
  int orbit=R.representatives.size();R.representatives.push_back(representative);++R.histogram[members.size()];
  for(int i:members){require(R.orbit[i]==-1,"duplicate orbit membership");R.orbit[i]=orbit;++assigned;}
 }
 require(assigned==M&&std::all_of(R.orbit.begin(),R.orbit.end(),[](int a){return a>=0;}),"incomplete orbit partition");
 return R;
}
void checkParity(const V&b,const Reflections&R,int r,int j){
 int sx=(r%2)?-1:1,sy=(j%2)?-1:1;
 require(b.size()==R.rx.size(),"basis parity dimensions");
 for(size_t i=0;i<b.size();++i){require(b[R.rx[i]]==sx*b[i],"basis X-reflection parity failure");require(b[R.ry[i]]==sy*b[i],"basis Y-reflection parity failure");}
}
void guardSelfTest(){
 V x={1,1,-1,-1},y={1,-1,1,-1},w(4,rat(1,4));
 Reflections R=reflectionOrbits(x,y,w);checkParity(x,R,1,0);
 require(R.representatives.size()==1&&R.histogram[4]==1,"selftest orbit dimensions");
 int rejected=0;
 auto reject=[&](auto f){try{f();}catch(const std::exception&){++rejected;return;}throw std::runtime_error("malformed reflection control accepted");};
 reject([&](){V bad=x;bad[0]=2;reflectionOrbits(bad,y,w);});
 reject([&](){V bad=w;bad[0]+=rat(1,8);bad[1]-=rat(1,8);reflectionOrbits(x,y,bad);});
 reject([&](){V bad=x;bad[0]+=1;checkParity(bad,R,1,0);});
 require(rejected==3,"selftest rejected count");
 std::cout<<"{\"status\":\"PASS reflection guard controls\",\"malformed_controls_rejected\":3}\n";
}
int main(int argc,char**argv){try{
 if(argc==2&&std::string(argv[1])=="--guard-self-test"){guardSelfTest();return 0;}
 require(argc==5,"usage: executable input.txt maxdegree bj|mirror|alt|pivot family");
 std::string grid=argv[4],rule=argv[3];int degree=std::stoi(argv[2]);
 require(degree>=2&&degree<=20,"degree outside 2..20");
 require(rule=="bj"||rule=="mirror"||rule=="alt"||rule=="pivot","invalid rule");
 auto start=std::chrono::steady_clock::now();V x,y;Q weight=0;
 std::ifstream input(argv[1]);require(input.good(),"cannot open input");int M;input>>M;require(M>0&&M<=10000,"invalid point count");
 for(int i=0;i<M;++i){Q a,b,w;input>>a>>b>>w;require(input.good()&&w>0,"invalid input row");a.canonicalize();b.canonicalize();w.canonicalize();weight+=w;weights.push_back(w);x.push_back(a);y.push_back(b);}
 std::string extra;require(!(input>>extra),"extra input tokens");
 require(weight==1,"normalized weights required");
 Reflections reflection=reflectionOrbits(x,y,weights);int R=reflection.representatives.size();
 std::cerr<<"reflection_orbits {\"nodes\":"<<M<<",\"representatives\":"<<R<<",\"size1\":"<<reflection.histogram[1]<<",\"size2\":"<<reflection.histogram[2]<<",\"size4\":"<<reflection.histogram[4]<<"}\n";
 std::vector<std::pair<int,int>>exponents(1,{0,0});checkParity(V(M,1),reflection,0,0);
 long parityChecks=2L*M,parentChecks=0,alphaSlots=0,alphaZeroChecks=0,expandedSnapshots=0;
 int N=(degree+1)*(degree+2)/2;require(M>N,"M must exceed N");
 std::vector<V>B(1,V(M,1));V d(1,Q(1));std::vector<Step> steps(1);std::vector<int> ends(degree+1);std::vector<std::vector<int>> index(degree+1);index[0]={0};ends[0]=1;
 std::string choices;std::vector<std::pair<int,int>>ties;long gram=0;
 for(int t=1;t<=degree;++t){for(int j=0;j<=t;++j){
  std::vector<Step> cs;std::vector<V> residues;V norms;
  for(int a=0;a<2;++a){if((a==0&&j==t)||(a==1&&j==0))continue;
   int wanted=rule=="bj"?(j==0?0:1):rule=="mirror"?(j!=t?0:1):(2*j<t?0:1);
   if(rule!="pivot"&&a!=wanted)continue;
   int p=index[t-1][j-a];
   require(exponents[p].first==t-j-(a==0)&&exponents[p].second==j-(a==1),"parent exponent/axis relation");++parentChecks;
   const V&coord=a?y:x;V z(M),alpha;
   for(int i=0;i<M;++i)z[i]=coord[i]*B[p][i];Q sigma=dot(z,z);require(sigma>0,"nonpositive source scale");
   for(size_t l=0;l<B.size();++l)alpha.push_back(dot(B[l],z)/d[l]);
   for(size_t l=0;l<alpha.size();++l){++alphaSlots;if((exponents[l].first%2)!=(t-j)%2||(exponents[l].second%2)!=j%2){require(alpha[l]==0,"nonzero cross-parity projection coefficient");++alphaZeroChecks;}}
   V r=z;
   for(size_t l=0;l<B.size();++l)if(alpha[l]!=0)for(int i=0;i<M;++i)r[i]-=alpha[l]*B[l][i];
   Q norm=dot(r,r);require(norm>0,"nonpositive pivot");cs.push_back({a,p,alpha,sigma});residues.push_back(std::move(r));norms.push_back(norm);
  }
  require(!cs.empty(),"missing parent");int pick=0;
  if(cs.size()==2){int c=cmp(norms[0]/cs[0].sigma,norms[1]/cs[1].sigma);if(c==0)ties.push_back({t,j});if(c<0)pick=1;}
  V r=residues[pick];checkParity(r,reflection,t-j,j);parityChecks+=2L*M;
  require(dot(r,r)==norms[pick],"diagonal Gram failure");for(size_t l=0;l<B.size();++l){require(dot(r,B[l])==0,"off-diagonal Gram failure");++gram;}
  index[t].push_back(B.size());exponents.push_back({t-j,j});B.push_back(std::move(r));d.push_back(norms[pick]);steps.push_back(cs[pick]);choices+=cs[pick].axis?'Y':'X';
 }
 ends[t]=B.size();std::cerr<<"basis "<<grid<<" "<<rule<<" "<<t<<"\n";
 }
 require((int)B.size()==N,"basis dimension mismatch");
 auto basisEnd=std::chrono::steady_clock::now();
 std::cerr<<"phase_basis_seconds "<<std::chrono::duration<double>(basisEnd-start).count()<<"\n";
 // At each prefix store sum_h v_hi and max_h v_hi; normal factor is h-independent.
 std::vector<V> totals(degree+1,V(M)),maxima(degree+1,V(M));
 for(int h=1;h<N;++h){std::vector<V>g(N);g[h]=V(R,1);V energy(R,1/d[h]);
  for(int k=h;k<N;++k){if(k>h){const Step&s=steps[k];g[k]=V(R);const V&coord=s.axis?y:x;
    if(s.parent>=h)for(int i=0;i<R;++i)g[k][i]=coord[reflection.representatives[i]]*g[s.parent][i];
    for(int l=h;l<k;++l)if(s.alpha[l]!=0)for(int i=0;i<R;++i)g[k][i]-=s.alpha[l]*g[l][i];
    for(int i=0;i<R;++i)energy[i]+=g[k][i]*g[k][i]/d[k];}
   for(int s=2;s<=degree;++s)if(k+1==ends[s]){
    V snapshot(R);for(int q=0;q<R;++q)snapshot[q]=steps[h].sigma*energy[q];
    // Expand to every original node BEFORE the unchanged totals/maxima updates.
    for(int i=0;i<M;++i){const Q&v=snapshot[reflection.orbit[i]];totals[s][i]+=v;if(cmp(v,maxima[s][i])>0)maxima[s][i]=v;++expandedSnapshots;}
   }
  }
  std::cerr<<"source "<<h<<"/"<<N-1<<"\n";
 }
 auto sourceEnd=std::chrono::steady_clock::now();
 std::cerr<<"phase_source_seconds "<<std::chrono::duration<double>(sourceEnd-basisEnd).count()<<"\n";
 long expectedSnapshots=0;for(int s=2;s<=degree;++s)expectedSnapshots+=(ends[s]-1)*M;
 require(expandedSnapshots==expectedSnapshots,"full-node/source snapshot coverage failure");
 std::cerr<<"reflection_guards {\"basis_parity_scalar_checks\":"<<parityChecks<<",\"parent_exponent_checks\":"<<parentChecks<<",\"alpha_slots_checked\":"<<alphaSlots<<",\"cross_parity_zeros_checked\":"<<alphaZeroChecks<<",\"source_positions\":"<<N-1<<",\"expanded_node_source_snapshots\":"<<expandedSnapshots<<",\"expected_expanded_node_source_snapshots\":"<<expectedSnapshots<<"}\n";
 for(int s=2;s<=degree;++s){Q lo=0,hs=0,row=0,trace=0;int ns=ends[s];
  for(int i=0;i<M;++i){Q normal=1;for(int k=0;k<ns;++k)normal-=weights[i]*B[k][i]*B[k][i]/d[k];require(normal>=0&&normal<=1,"invalid projector diagonal");trace+=normal;
   Q a=normal*maxima[s][i];if(cmp(a,lo)>0)lo=a;hs+=normal*totals[s][i];if(cmp(totals[s][i],row)>0)row=totals[s][i];}
  require(trace==M-ns,"projector trace mismatch");Q upper=cmp(hs,row)<0?hs:row;require(lo>0&&cmp(lo,upper)<=0,"endpoint order failure");
  std::cout<<"{\"set\":\""<<grid<<"\",\"rule\":\""<<rule<<"\",\"degree\":"<<s<<",\"sources\":\"all\",\"source_count\":"<<ns-1<<",\"point_count\":"<<M<<",\"basis_count\":"<<ns<<",\"Knode_squared\":{\"exact\":\""<<lo<<"\"},\"KHS_squared\":{\"exact\":\""<<hs<<"\"},\"Urow_squared\":{\"exact\":\""<<row<<"\"},\"upper_squared\":{\"exact\":\""<<upper<<"\"},\"pivot_choices\":[";
  for(int k=0;k<ns-1;++k){if(k)std::cout<<",";std::cout<<"\""<<choices[k]<<"\"";}std::cout<<"],\"pivot_ties\":[";bool comma=false;for(auto p:ties)if(p.first<=s){if(comma)std::cout<<",";std::cout<<"["<<p.first<<","<<p.second<<"]";comma=true;}
  double seconds=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
  std::cout<<"],\"normal_trace_exact\":\""<<trace<<"\",\"exact_gram_pairs_checked\":"<<gram<<",\"elapsed_seconds\":"<<seconds<<"}"<<std::endl;
 }
 std::cerr<<"phase_finish_seconds "<<std::chrono::duration<double>(std::chrono::steady_clock::now()-sourceEnd).count()<<"\n";
 return 0;
}catch(const std::exception&e){std::cerr<<e.what()<<"\n";return 2;}}
