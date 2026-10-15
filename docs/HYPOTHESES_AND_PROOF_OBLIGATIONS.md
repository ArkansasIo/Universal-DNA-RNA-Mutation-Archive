# Hypotheses, Predictions, and Proof Obligations

## H1 — Repair impairment changes mutation spectrum
Hypothesis: reducing activity of a specified repair pathway changes mutation rate and/or spectrum in a defined organism.

Design: compare matched repair-proficient and repair-impaired backgrounds; include independent replicates, sequencing controls, callable-site masks, and validated variant calling.

Potential confounders: growth rate, viability selection, sequencing artifacts, secondary mutations, coverage, and cell-cycle effects.

## H2 — Sequence context affects mutation probability
Hypothesis: local sequence contexts have different mutation rates after controlling for coverage and technical error.

Analysis: model counts with exposure offsets and context features; validate on held-out samples. A well-powered equivalence result may reject a predeclared practically meaningful difference in the studied system.

## H3 — Mutation rate and life history covary
Hypothesis: mutation rates vary with generation time, cell division, reproductive biology, repair, or effective population size across selected taxa.

Analysis: comparative phylogenetic regression with uncertainty in rate estimates and explicit covariates. Correlation alone does not establish mechanism.

## H4 — RNA and DNA genome variant spectra differ
Hypothesis: spectra differ among defined groups after controlling for genome region, replication strategy, selection, sampling interval, and sequencing technology. Do not assume molecule type is the only explanatory variable.

## H5 — Prediction models generalize
Hypothesis: a specified computational model predicts experimentally measured effects better than a baseline on a held-out dataset.

Metrics: calibration, error distribution, uncertainty, and performance by organism group. The model fails its hypothesis if it misses the predeclared benchmark or does not outperform baseline within uncertainty.

## H6 — Somatic burden varies by tissue and age
Hypothesis: measured somatic mutation burden varies across tissues and age groups in a specified organism.

Account for cell division, cell composition, clonal expansion, sequencing depth, and error suppression. This is not a universal age curve.

## Mathematical proof A
For L independent sites with equal event probability μ, probability of no event is (1−μ)^L.

Proof: each site has probability 1−μ of no event. Independence means the joint probability of no event at all L sites is the product (1−μ)^L. Therefore:
\[
P(M\geq1)=1-P(M=0)=1-(1-\mu)^L.
\]
This is a mathematical proof conditional on independence and equal probabilities, not proof that biological sites satisfy these assumptions.

## Mathematical proof B
For site-specific probabilities μ_i and independent sites:
\[
P(M\geq1)=1-\prod_{i=1}^{L}(1-\mu_i).
\]
Proof: multiply the no-event probability for each site, then take the complement.

## Mathematical proof C
For a haploid two-type population with fitness 1 and 1+s and alternate frequency p, post-selection frequency is p' = p(1+s)/(1+ps).

Proof: the alternate type's weighted contribution is p(1+s). Mean fitness is (1-p)·1+p(1+s)=1+ps. Dividing the alternate weighted contribution by mean fitness yields the stated recursion.

## Biological proof distinction
These proofs establish algebraic consequences of premises. They do not prove an empirical hypothesis about a particular organism. Empirical claims require reproducible observations, controls, appropriate statistical inference, and independent corroboration when feasible.
