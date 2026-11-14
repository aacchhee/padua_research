import sys,re
src=open(sys.argv[1]).read()
L=src.split('\n')
def R(a,b): return L[a-1:b]          # 1-based inclusive
def must_replace(t,old,new):
    assert t.count(old)==1,(old[:60],t.count(old)); return t.replace(old,new)

# ---------------- MZ-CC ----------------
cc=R(1,953)+R(1497,1524)+R(1620,1653)
cc='\n'.join(cc)
cc=must_replace(cc,"pdftitle={Marcinkiewicz--Zygmund constants of Clenshaw--Curtis and Padua rules beyond half-exactness}",
                "pdftitle={Marcinkiewicz--Zygmund constants of Clenshaw--Curtis rules beyond half-exactness}")
cc=must_replace(cc,"\\title{Marcinkiewicz--Zygmund constants of Clenshaw--Curtis\\texorpdfstring{\\\\}{ }and Padua rules beyond half-exactness}",
                "\\title{Marcinkiewicz--Zygmund constants of Clenshaw--Curtis\\texorpdfstring{\\\\}{ }rules beyond half-exactness}")
cc=must_replace(cc,"""of An and Wu. For signed Lebesgue Padua rules, we prove the exact
factor-two Clenshaw--Curtis marginal and its spectral compression consequence;
the actual signed Gram form has divergent negative and positive extrema
as the construction degree tends to infinity, at every fixed degree ratio
above one half.
Explicit parity carriers and logarithmic boundary-weight asymptotics prove
this sharp half-exactness threshold. Nevertheless the direct signed
coefficient hyperinterpolant has a uniform $C\\to L^2$ norm below thirty.
Analytic proofs are included. For CC,""","""of An and Wu.
Analytic proofs are included. For CC,""")
cc=must_replace(cc,"""test shows below. For the signed Padua rule the picture is different: Section~\\ref{sec:padua}
proves divergence of both spectral extrema along all construction degrees
above half-exactness, alongside a uniform bound for its direct coefficient
operator. These results""","""test shows below. These results""")
cc=must_replace(cc,"% Companion MEASURED record: PD-T380; topics/padua-mz-cleanup-20261105/theory/finite-measurements.md (campaign rows not reproduced here).\nTables~\\ref{tab:cc}--\\ref{tab:padua} reproduce","Table~\\ref{tab:cc} reproduces")
cc=must_replace(cc,"""claim here. Third, for the signed Padua rule, Theorem~\\ref{thm:padua-carriers}
refutes the universal positivity and upper-threshold conjectures and the
proposed positive endpoint orders and convergence of the defect to one.
% OPEN sharp-growth target: PD-T381; topics/padua-mz-cleanup-20261105/theory/sharp-growth-open.md
The sharp growth constants and effective onset estimates remain separate
quantitative questions. The present odd-degree extension completes the
qualitative parity classification; Proposition~\\ref{prop:padua-growth}
gives only one-sided normalized logarithmic bounds. The analytic carriers
give no explicit onset. Proposition~\\ref{prop:padua-finite-negative}
supplies a separate finite certificate, without claiming the first crossing.
Sharp direct-operator
norms and endpoint fixed-function convergence also remain separate.
These mathematical""","""claim here.
These mathematical""")
cc=must_replace(cc,"proofs of the central CC and Padua statements","proofs of the central CC statements")
cc=must_replace(cc,"""\\section{Finite observations and unresolved sharpenings}\\label{sec:numerics}

""","""% Signed Padua material (old Section 6 and the Padua parts of old Section 7) moved to ../paper-sp/ (MZ-SP); see topics/padua-mz-paper-20261113/split-map.md.
\\section{Finite observations and unresolved sharpenings}\\label{sec:numerics}

""")
open(sys.argv[2],'w').write(cc+('\n' if not cc.endswith('\n') else ''))

# ---------------- MZ-SP ----------------
pre='\n'.join(R(1,26))
pre=pre.replace("pdftitle={Marcinkiewicz--Zygmund constants of Clenshaw--Curtis and Padua rules beyond half-exactness}",
                "pdftitle={Marcinkiewicz--Zygmund constants of signed Padua rules beyond half-exactness}")
head=r"""\title{Marcinkiewicz--Zygmund constants of signed Padua rules\texorpdfstring{\\}{ }beyond half-exactness}
\author{Research development draft\thanks{Authorship and submission venue to be decided by AC. This document is not for submission.}}
\date{13 November 2026}
\begin{document}
\maketitle
\begin{center}\small
\textbf{Development status.} Post-split baseline of the signed Padua part
(old Section~6 and the Padua parts of old Section~7) of the single MZ
development draft of 5 November 2026; split by AC's decision of
13 November 2026. The companion Clenshaw--Curtis paper is cited as
\citep{MZ-CC}. No statement or proof below was changed by the split.
\end{center}

\begin{abstract}
For signed Lebesgue Padua rules, we prove the exact
factor-two Clenshaw--Curtis marginal and its spectral compression consequence;
the actual signed Gram form has divergent negative and positive extrema
as the construction degree tends to infinity, at every fixed degree ratio
above one half.
Explicit parity carriers and logarithmic boundary-weight asymptotics prove
this sharp half-exactness threshold. Nevertheless the direct signed
coefficient hyperinterpolant has a uniform $C\to L^2$ norm below thirty.
Analytic proofs are included.
\end{abstract}

% Split glue (MZ-SP baseline): the CC conventions and the three CC inputs
% used below, recapped from MZ-CC; see split-map.md.
\section{Conventions and Clenshaw--Curtis inputs}\label{sec:cc-recap}
"""
recap=R(82,95)+R(108,129)
recap='\n'.join(recap)
recap+=r"""

Write $\theta_j=j\pi/N$ and let $S_N(\theta)$ denote the bracket in the
explicit weight formula
\[
 w_j=\frac{2\gamma_j}{N}S_N(\theta_j),\qquad
 S_N(\theta)=1-\sum_{r=1}^{\lfloor(N-1)/2\rfloor}
      \frac{2\cos(2r\theta)}{4r^2-1}
 -\boldsymbol1_{2\mid N}\frac{\cos(N\theta)}{N^2-1},
\]
with $\gamma_0=\gamma_N=1/2$ and $\gamma_j=1$ otherwise.
The following facts are proved in \citep{MZ-CC}.

\begin{lemma}[CC weight comparison; \citealp{MZ-CC}]\label{lem:weight-comparison}
For $0\le\theta\le\pi$,
$|S_N(\theta)-(\pi/2)\sin\theta|\le1/N$ for odd $N$ and
$\le N/(N^2-1)$ for even $N$. Consequently, for $1\le j\le N-1$,
\[
 \frac{\sin\theta_j}{N}\le w_j\le\frac{5\sin\theta_j}{N}.
\]
\end{lemma}

\begin{proposition}[CC spectral inputs; \citealp{MZ-CC}]\label{prop:counterexample}
For $0\le n<N$, $\lambda_+(N,n)\le2-4/N+4/N^2<2$.
Moreover $\lambda_-(N,N-1)\to0$ as $N\to\infty$, and
$\lambda_-(512,511)<1/4$, so $\norm{I-G_{512,511}}_2>3/4$.
\end{proposition}

"""
body='\n'.join(R(954,1496))
body=body.replace(r"\section{Signed Padua rules beyond half-exactness}\label{sec:padua}",
                  r"\section{Signed Padua rules beyond half-exactness}\label{sec:padua}")
fin=r"""\section{Finite observations and unresolved sharpenings}\label{sec:numerics}

% Companion MEASURED record: PD-T380; topics/padua-mz-cleanup-20261105/theory/finite-measurements.md (campaign rows not reproduced here).
Table~\ref{tab:padua} reproduces bounded float64 observations
(\id{PD-T026}), not asymptotic proofs. The producer runs with Python,
NumPy, and SciPy and pins its code and supplied input hashes in the evidence
manifest. An independent Astra agent separately reran the bounded suite.
The analytic theorems above do not use these observations as proof.

"""
fin+='\n'.join(R(1525,1619))
fin+=r"""
Several sharper questions remain separate from the proved comparisons.
For the signed Padua rule, Theorem~\ref{thm:padua-carriers}
refutes the universal positivity and upper-threshold conjectures and the
proposed positive endpoint orders and convergence of the defect to one.
% OPEN sharp-growth target: PD-T381; topics/padua-mz-cleanup-20261105/theory/sharp-growth-open.md
The sharp growth constants and effective onset estimates remain separate
quantitative questions. The present odd-degree extension completes the
qualitative parity classification; Proposition~\ref{prop:padua-growth}
gives only one-sided normalized logarithmic bounds. The analytic carriers
give no explicit onset. Proposition~\ref{prop:padua-finite-negative}
supplies a separate finite certificate, without claiming the first crossing.
Sharp direct-operator
norms and endpoint fixed-function convergence also remain separate.

\paragraph{Reproducibility and claim identification.}
The accompanying README gives exact compilation and numerical commands,
artifact hashes, and links to the theory and evidence. The final
\id{PD-T}/\id{PD-N} identifiers in theorem headings refer to the durable
repository claims. These identifiers do not confer publication or audit
readiness. Analytic proofs of the central signed Padua statements have
been included here; no private manuscript is a mathematical dependency.

\bibliographystyle{plainnat}
\bibliography{refs}
\end{document}
"""
sp=pre+'\n'+head+recap+body+'\n'+fin
open(sys.argv[3],'w').write(sp)
