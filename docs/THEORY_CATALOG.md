# Mutation Theory Catalog: Established Mechanisms and Open Explanations

## Purpose
This document separates established molecular mechanisms from explanatory theories and unresolved hypotheses. A scientific theory is an evidence-supported explanatory framework, not a guess. Claim status can vary by organism and context.

## 1. Replication error and proofreading
DNA polymerases can incorporate incorrect nucleotides; proofreading and mismatch repair reduce the probability that errors become stable sequence changes.

A simplified residual error model is:
\[
\mu_{residual}=e(1-q)
\]
where e is the raw mismatch probability and q is the fraction corrected. This assumes one correction stage and constant effectiveness; real repair is more complex.

Prediction: impairing a relevant proofreading or repair pathway may increase particular mutation classes. The effect depends on pathway and organism.

## 2. DNA damage and repair
A lesion is not automatically a mutation: it may be repaired, bypassed, or converted into a stable sequence change during replication.

A conceptual bookkeeping equation is:
\[
D_{t+1}=D_t+I_t-R_t-C_t
\]
where D is unrepaired lesion burden, I is lesion input, R is repair, and C represents other explicitly defined removal processes. This is accounting logic, not a universal kinetic law.

## 3. Mutation–selection balance
For a deleterious allele under a simplified haploid model, a common rare-allele approximation is:
\[
\hat q\approx\frac{\mu}{s}
\]
where μ is forward mutation rate and s is the selection coefficient. Assumptions include weak mutation, effective selection, and negligible reverse mutation, drift, and linkage. Diploid and recessive models differ.

## 4. Neutral theory and genetic drift
Neutral or nearly neutral variants can change frequency through random sampling in finite populations. Under a simple neutral diploid model, θ = 4Nₑμ is a common equilibrium approximation under an infinite-sites model. Real populations may violate equilibrium, neutrality, random mating, or infinite-sites assumptions.

## 5. Drift-barrier hypothesis
Hypothesis: selection can favor improved replication fidelity, but random genetic drift may limit the fixation of small-effect improvements, especially in lineages with small effective population sizes.

Status: influential, evidence-supported hypothesis—not a universal law for every lineage. Compare it with mechanistic and life-history explanations.

## 6. Mutation-rate variation
Rates can vary across species, loci, sequence contexts, cell types, and life stages. Potential factors include replication machinery, repair, generation time, chromatin, recombination, and exposure history.

Testable prediction: after controlling for technical error and ascertainment, mutation spectra may show repeatable associations with mechanistic variables.

## 7. Germline and somatic mutation
Germline mutations may be inherited. Somatic mutations arise in non-germline cell lineages and generally are not transmitted to offspring, although germline mosaicism and differing reproductive biology complicate simple rules. Somatic mutations can affect development, tissue function, ageing, and cancer.

## 8. RNA genome variation and RNA editing
RNA viruses can accumulate sequence changes through replication and selection. RNA editing changes RNA after transcription in particular systems and should be recorded separately from genomic mutation. RNA viruses differ substantially in replication fidelity and proofreading; it is not defensible to claim all RNA viruses mutate faster than all DNA viruses.

## 9. Evolutionary consequences
Mutation introduces heritable variation; selection, drift, migration, recombination, and demography shape its fate. A variant can be beneficial in one environment and neutral or harmful in another.

Relative selection coefficient:
\[
s=\frac{w_{alt}-w_{ref}}{w_{ref}}
\]
Fitness values must be measured in a specified environment and assay.

## 10. Research guardrails
- Do not infer function from sequence difference alone.
- Do not treat computational prediction as experimental validation.
- Do not equate database submission with consensus truth.
- Preserve reference sequence versions and coordinate conventions.
- Distinguish mutation, recombination, gene conversion, RNA editing, epigenetic modification, and sequencing error.
- Report uncertainty and alternative explanations.

## References
- Lynch et al. (2016), “Genetic drift, selection and the evolution of the mutation rate,” Nature Reviews Genetics. https://doi.org/10.1038/nrg.2016.104
- Brown, Genomes, “Mutation, Repair and Recombination,” NCBI Bookshelf. https://www.ncbi.nlm.nih.gov/books/NBK21114/
- Beichman, Zhu & Harris (2024), “The Evolutionary Interplay of Somatic and Germline Mutation Rates.” https://pubmed.ncbi.nlm.nih.gov/38669515/
- Barrick & Lenski (2013), “Genome dynamics during experimental evolution.” https://www.nature.com/articles/nrg3564
