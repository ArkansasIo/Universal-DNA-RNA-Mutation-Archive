# Mathematical Models for DNA/RNA Mutation Research

All models are idealizations. Pair each with assumptions, units, data provenance, diagnostics, and uncertainty estimates before interpreting biological observations.

## 1. Independent-site probability
For sequence length L and per-site event probability μ:
\[
E[M]=L\mu
\]
If sites are independent with identical probability:
\[
P(M\geq1)=1-(1-\mu)^L
\]
For small μ, this is approximately 1 − exp(−Lμ). If probabilities vary by site:
\[
P(M\geq1)=1-\prod_{i=1}^{L}(1-\mu_i)
\]

## 2. Poisson approximation
For rare approximately independent events K over exposure E:
\[
P(K=k)=\frac{(\lambda E)^k e^{-\lambda E}}{k!}
\]
λ is an event rate per unit exposure. Exposure may mean callable bases times generations, cell divisions, or another defined denominator. Do not mix incompatible units.

## 3. Binomial likelihood
For k mutated observations among n independent opportunities:
\[
\mathcal L(\mu\mid k,n)={n\choose k}\mu^k(1-\mu)^{n-k}
\]
The maximum-likelihood estimate is μ̂ = k/n for n>0. Independence and unbiased ascertainment are strong assumptions.

## 4. Time-varying mutation rate
If r(t) is an instantaneous expected event rate:
\[
M(T)=M(0)+\int_0^T r(t)\,dt,\quad \frac{dM}{dt}=r(t)
\]
If r(t)=a+bt, then M(T)=M(0)+aT+bT²/2. This models expected accumulation; individual genomes do not accumulate events smoothly.

## 5. Mutation–selection–reversion dynamics
A simplified model is:
\[
\frac{dp}{dt}=\mu(1-p)-\nu p+s p(1-p)
\]
μ is forward mutation, ν reverse mutation, and s a weak-selection approximation. Ploidy, dominance, drift, linkage, migration, and genotype-specific fitness may require another model.

## 6. Discrete selection recursion
For a haploid model with reference fitness 1 and alternate fitness 1+s:
\[
p'=\frac{p(1+s)}{1+ps}
\]
The denominator is mean fitness in this two-type model. This equation cannot predict a real trajectory without justified parameters and assumptions.

## 7. Hamming distance
For equal-length aligned sequences x and y:
\[
d_H(x,y)=\sum_{i=1}^{n}\mathbf{1}[x_i\ne y_i]
\]
The fraction differing is d_H/n. Indels and divergent sequences require alignment-aware methods.

## 8. Transition/transversion ratio
\[
R_{tv}=\frac{N_{transitions}}{N_{transversions}}
\]
Report denominators, callable sites, uncertainty, context composition, and sampling design.

## 9. Shannon entropy
For nucleotide frequencies p_A, p_C, p_G, p_T:
\[
H=-\sum_b p_b\log_2 p_b
\]
This summarizes sequence-composition diversity at a chosen level; it does not measure fitness, pathogenicity, or evolutionary progress.

## 10. Model comparison
Use predeclared criteria, held-out validation, likelihood-based measures where appropriate, and residual diagnostics. A better statistical fit is not proof of a causal mechanism.

## Wolfram|Alpha workflow
Suggested queries:
- integrate a+b*t from t=0 to T
- solve dp/dt = mu*(1-p)-nu*p+s*p*(1-p)
- simplify 1-(1-mu)^L
- plot 1-exp(-L*mu) for L=1000 to 1000000
- solve p2 = p*(1+s)/(1+p*s) for p

Archive the exact expression, parameter definitions, units, assumptions, date, and output. Symbolic correctness does not establish biological validity.
