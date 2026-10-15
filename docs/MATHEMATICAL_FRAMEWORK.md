# Mathematical framework

## Independent-site mutation model
For sequence length L and per-site probability mu:
- Expected events per replication: E[M] = L mu.
- Probability of at least one event: P(M >= 1) = 1 - (1 - mu)^L.
- For small mu: P(M >= 1) approximately 1 - exp(-L mu).

Assumptions: independent sites and equal event probability. Real mutation processes can depend on sequence context, strand, repair, replication machinery, and selection.

## Mutation accumulation over time
For rate r(t), expected accumulated events can be modeled as:
M(T) = M(0) + integral from 0 to T of r(t) dt.
For constant r: M(T) = M(0) + rT. Observed divergence is also shaped by drift, selection, recombination, recurrent mutation, and ancestral uncertainty.

## Haploid selection step
With reference fitness 1, alternate fitness 1+s, and alternate frequency p:
p' = p(1+s)/(1+ps).
This ignores mutation, migration, and genetic drift in the selection step.

## Simplified mutation-selection dynamics
dp/dt = mu(1-p) - nu*p + s*p*(1-p)
where mu is forward mutation and nu is reverse mutation. This is an approximation, not a universal law; dominance, ploidy, linkage, demography, and genotype-specific fitness may require other models.

## Sequence distance
For aligned equal-length sequences x and y:
d_H(x,y) = sum_i I(x_i != y_i).
The fraction of differing aligned sites is d_H/n. Use alignment-aware methods for indels and unequal lengths.

## Wolfram|Alpha queries
- `1 - (1 - 10^-9)^1000000`
- `solve dp/dt = s*p*(1-p)`
- `integrate r(t) from t=0 to T`
- `plot p*(1+s)/(1+p*s) for p=0.01 to 1`

Record exact query, parameter units, assumptions, tool access date, and results. Wolfram|Alpha is a mathematical tool, not a complete biological variant database.
