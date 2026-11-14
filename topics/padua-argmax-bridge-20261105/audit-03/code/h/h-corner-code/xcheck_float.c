/* auditor driver: calls the repo float kernel phase_s(n,0,0) (included verbatim by #include) */
#include <stdio.h>
#include <stdlib.h>
#include "/home/user/padua_research/topics/padua-argmax-effective-2-20261105/code/phase_probe.c"
int main(int argc,char**argv){ for(int i=1;i<argc;i++){int n=atoi(argv[i]); printf("%d %.17g\n",n,phase_s(n,0,0));} return 0; }
