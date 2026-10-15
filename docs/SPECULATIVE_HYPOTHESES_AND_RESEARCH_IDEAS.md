# Speculative Hypotheses and Research Ideas

## How to read this document
The ideas below are proposals for investigation, not claims that the effects exist. They should remain labelled `hypothesis` until evidence is obtained. A research idea is useful when it can be operationalized, tested against alternatives, and potentially rejected.

## H1. Context-aware variant effect models
**Idea:** Variant-effect predictions may improve when models jointly represent sequence context, gene regulation, cell type, evolutionary conservation, and environmental conditions.

**Test:** Compare a context-aware model with simpler baselines on a held-out, independently curated dataset. Report calibration, uncertainty, performance by taxon, and failure cases.

**Alternative explanation:** Apparent gains may arise from data leakage, class imbalance, or overrepresentation of a few well-studied organisms.

## H2. Repair-pathway signatures across the tree of life
**Idea:** Some mutation-spectrum patterns may act as signatures of specific repair or replication mechanisms across related taxa.

**Test:** Compare published mutation-accumulation and genomic datasets while accounting for sequence context, phylogeny, generation time, and technical error.

**Falsifier:** Signatures fail to replicate in independent data or are explained by confounding variables.

## H3. CRISPR outcome predictability
**Idea:** Models that incorporate cell state, genomic context, and repair-pathway information may predict editing outcomes more reliably than sequence-only models.

**Test:** Evaluate on independent published datasets, with organism- and assay-stratified results.

**Alternative explanation:** The model may learn study-specific technical artifacts instead of general biological rules.

## H4. Evolutionary constraints on editability
**Idea:** Evolutionary conservation and network context may help identify which classes of genetic changes are more likely to have broad pleiotropic effects.

**Test:** Compare conservation and network predictions with independent functional evidence. Conservation is not itself proof of essentiality or harmfulness.

## H5. Environmental dependence of variant effects
**Idea:** Some variants have effects that change direction or magnitude across environments.

**Test:** Use published genotype-by-environment data and interaction models. Predefine environmental contrasts and report uncertainty.

## H6. Biological redundancy and compensation
**Idea:** Redundant genes and compensatory pathways may buffer some mutations, while network bottlenecks may amplify others.

**Test:** Integrate functional genomics and systems-biology datasets. Predictions must be distinguished from experimentally demonstrated compensation.

## H7. Reporting-quality hypothesis
**Idea:** More complete reporting of reference versions, controls, detection limits, and negative results is associated with better reproducibility.

**Test:** Create a preregistered reporting rubric, assess a representative publication sample, and measure agreement between reviewers.

## H8. Comparative natural CRISPR diversity
**Idea:** Natural diversity in CRISPR-associated systems may reveal evolutionary relationships between mobile genetic elements and host defense.

**Test:** Use public genomes, validated annotations, phylogenetic analysis, and documented uncertainty. Sequence similarity alone cannot establish the direction of evolutionary transfer.

## H9. Variant archive coverage bias
**Idea:** Public variant records are disproportionately concentrated in model organisms, humans, and medically or economically important species.

**Test:** Compare database record counts with taxonomic diversity and genome availability. Counts should not be interpreted as true mutation prevalence.

## H10. Multiscale prediction
**Idea:** A model combining molecular, cellular, organismal, and ecological data may predict some long-term outcomes better than a single-scale model.

**Test:** Compare models with ablation studies, external validation, uncertainty calibration, and explicit causal assumptions.

## Standard hypothesis template
- Claim:
- Scope and organism:
- Independent variable:
- Outcome variable:
- Baseline or null:
- Minimum effect of interest:
- Data source and inclusion criteria:
- Confounders:
- Analysis plan:
- Expected result if supported:
- Result that would weaken or falsify it:
- Replication plan:
- Ethics and biosafety review:
- Evidence status and last review date:

## Rule
Do not use “proven” for a new hypothesis before evidence exists. Keep speculative ideas in a separate table from established mechanisms and measured findings.
