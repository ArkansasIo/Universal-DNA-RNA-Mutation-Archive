# CRISPR Research Framework: Mutation, Repair, Evolution, and Evidence

## 1. Purpose and scope
This document extends the Universal DNA & RNA Mutation Archive to CRISPR-associated research. It is a conceptual and computational research framework, not a laboratory editing protocol. It covers established CRISPR mechanisms, hypotheses that can be evaluated using published data, evolutionary applications, risk analysis, and evidence standards.

CRISPR systems are diverse. In bacteria and archaea, CRISPR-associated systems can provide adaptive defense against mobile genetic elements. Researchers have adapted some CRISPR-associated proteins for genome editing, gene regulation, diagnostics, and other applications. Different systems have different mechanisms and limitations; “CRISPR” is not one uniform tool.

## 2. Questions for the archive
1. Which CRISPR system, organism, target type, and application are described by each record?
2. What is directly observed, what is predicted, and what is only proposed?
3. How are on-target changes, unintended changes, mosaic outcomes, delivery effects, and measurement limits reported?
4. How do outcomes differ by species, cell type, genomic context, and repair pathway?
5. What evidence supports a claimed phenotype or evolutionary consequence?
6. What are the ecological, ethical, welfare, equity, and governance implications?

## 3. CRISPR record model
Each CRISPR-related record should capture:
- system name and components as reported by the source;
- organism, strain or cell type, taxon identifier, and reference genome version;
- target locus and coordinate convention where applicable;
- intended edit class and observed edit class separately;
- detection/validation method, assay limitations, and controls;
- on-target outcomes and unintended outcomes reported by the study;
- phenotype, conditions, sample size, replicates, and uncertainty;
- publication, data accession, version, date retrieved, and license;
- evidence label: established mechanism, experimentally observed, computational prediction, hypothesis, or conflicting evidence;
- biosafety and ethical review context when relevant.

Do not infer that a design succeeded from a predicted target score. Do not equate a reported edit with a demonstrated organism-level benefit.

## 4. Established concepts
### 4.1 Target recognition and specificity
CRISPR-associated nucleic-acid recognition depends on the particular system, target context, and recognition rules. Specificity is empirical, not absolute: related sequences, chromatin or molecular context, delivery, and assay sensitivity can influence observed outcomes.

### 4.2 Cellular repair and outcome
For genome-editing applications that create a DNA break, cellular repair can produce multiple outcomes. Outcomes may include the intended change, small insertions/deletions, larger rearrangements, no detectable edit, or mosaic mixtures. Some CRISPR systems do not work by making a conventional double-strand DNA break, so the outcome model must be system-specific.

### 4.3 Intended edit versus biological phenotype
A sequence change does not guarantee a predictable phenotype. Gene networks, regulatory context, pleiotropy, genetic background, development, environment, and compensatory pathways can alter outcomes.

### 4.4 Natural CRISPR and laboratory CRISPR are different contexts
Natural CRISPR-associated immune systems evolved in microbial contexts. Engineered applications repurpose components under different constraints. Evidence from one context should not be automatically generalized to another.

## 5. Mathematical framework
These are high-level analysis models, not design instructions for editing a particular organism.

### 5.1 Observed outcome proportions
If n independently assessed samples produce k samples with a defined outcome:
\[
\hat p = \frac{k}{n}
\]
Report a confidence interval, sample-selection process, detection threshold, and whether samples are independent. The estimate is only for the defined assay and population.

### 5.2 Specificity as a measured rate
For a defined study, let O be validated unintended events and E be the number of adequately assessed candidate sites or samples. A descriptive rate may be:
\[
\hat r = \frac{O}{E}
\]
The denominator must be explicitly defined. Different assays detect different classes of outcomes, so rates from different studies may not be comparable.

### 5.3 Expected utility under uncertainty
For a proposed application with possible outcomes i:
\[
EU = \sum_i P(O_i\mid D)\,U(O_i)
\]
where D is available evidence and U is an explicitly defined utility or harm measure. This is a decision framework, not a claim that ethical values can be reduced to one universally agreed number.

### 5.4 Benefit–risk comparison
A simple decision table can compare expected benefit, unintended outcomes, reversibility, distribution of risk, ecological persistence, and availability of alternatives. Do not collapse rare catastrophic risks or unequal burdens into an unexamined average.

### 5.5 Model uncertainty
If an outcome model predicts probability p with uncertainty, report calibration and validation performance, not just a single score. A prediction is not proof that an edit will have the same effect in another organism or environment.

## 6. Testable research hypotheses
- H1: Published on-target outcome distributions vary by CRISPR system, cell type, genomic context, and repair state.
- H2: Predicted specificity scores are imperfectly calibrated across organism groups and assay types.
- H3: The relationship between an intended edit and phenotype depends on genetic background and environmental conditions.
- H4: Unintended outcomes are undercounted when studies use assays that cannot detect large or low-frequency changes.
- H5: Natural CRISPR-system diversity contains functional variation that cannot be inferred from a single model organism.
- H6: Reporting completeness is associated with the reproducibility of CRISPR outcome claims.

These are research hypotheses, not established conclusions. A useful study predefines outcomes, controls, effect sizes, exclusions, statistical methods, and falsification criteria.

## 7. Limitations and governance
- CRISPR methods differ in mechanism and application; avoid universal claims.
- Public datasets are subject to publication and ascertainment bias.
- Negative results may reflect assay limits rather than absence of an event.
- Organism-level effects may be pleiotropic and context-dependent.
- Heritable, ecological, agricultural, medical, and microbial applications have different risk profiles.
- Research should follow applicable biosafety, ethics, animal-welfare, clinical, environmental, and access-control requirements.
- This document intentionally does not provide step-by-step wet-lab editing procedures, target-specific designs, or operational parameters.

## 8. Selected starting resources
- Broad Institute CRISPR resources: https://www.broadinstitute.org/what-broad-crispr
- Addgene CRISPR educational resources: https://www.addgene.org/crispr/
- NCBI PubMed literature search: https://pubmed.ncbi.nlm.nih.gov/?term=CRISPR+genome+editing+specificity+review
- National Academies, Human Genome Editing: Science, Ethics, and Governance: https://nap.nationalacademies.org/catalog/24623/human-genome-editing-science-ethics-and-governance
- WHO, Human genome editing: https://www.who.int/health-topics/human-genome-editing
