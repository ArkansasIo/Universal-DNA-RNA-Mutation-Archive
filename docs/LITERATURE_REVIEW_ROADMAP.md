# Literature Review Roadmap: Evolution, Biology, Mathematics, and Engineering

## Purpose
This roadmap defines a reproducible process for building a literature library across evolutionary biology, genetics, molecular biology, mathematics, bioinformatics, genetic engineering, and non-genetic approaches to studying biological change. It is not a claim that every paper in these fields has already been read. The literature is too large and continually expanding; the archive should use transparent search strategies, prioritized source collections, and documented coverage.

## Core terminology
- **Evolutionary biology:** the broad study of heritable change in populations and the diversification and history of life.
- **Population genetics:** mathematical and empirical study of genetic variation and allele-frequency change in populations.
- **Molecular evolution:** evolution of DNA, RNA, proteins, and molecular mechanisms.
- **Phylogenetics:** inference and analysis of evolutionary relationships.
- **Evolutionary developmental biology (evo-devo):** how development and its genetic regulation evolve.
- **Comparative biology / comparative genomics:** comparison across organisms, including anatomy, physiology, genes, genomes, and traits.
- **Experimental evolution:** direct study of evolutionary change across generations under defined conditions.
- **Paleobiology / paleontology:** study of ancient life, including fossils and long-term evolutionary patterns.
- **Systems biology:** study of interacting molecular, cellular, and organismal systems.
- **Bioinformatics / computational biology:** computational analysis and modeling of biological data.
- **Synthetic biology / genetic engineering:** deliberate design or modification of biological systems, including genome editing.
- **Non-genetic approaches:** comparative observation, field studies, fossils, microscopy, physiology, developmental studies, ecological monitoring, mathematical models, and other approaches that do not require deliberate genome editing.

## Scope and boundaries
Include bacteria, archaea, viruses, protists, fungi, plants, and animals. Distinguish viruses from cellular life where relevant. Separate naturally occurring mutation, recombination, horizontal gene transfer, RNA editing, epigenetic changes, engineered edits, and measurement/sequencing errors. Do not assume all mechanisms apply to all taxa.

## Literature collection strategy
1. **Foundational textbooks and consensus reports:** use these to establish terminology, established mechanisms, and conceptual structure.
2. **Systematic reviews and meta-analyses:** use these to map the current state of evidence and disagreements.
3. **Primary research papers:** use these for methods, data, effect estimates, and reproducibility checks.
4. **Public data resources:** record database version, accession, reference sequence/genome, organism/taxon, license, and retrieval date.
5. **Preprints and speculative proposals:** include only with explicit labels distinguishing non-peer-reviewed or unvalidated claims.
6. **Conflicting and null results:** actively search for them; do not collect only positive findings.

## Starting authoritative resources
- National Academies, Evolution resources: https://www.nationalacademies.org/evolution-resources
- National Academies Press, *Teaching About Evolution and the Nature of Science*: https://www.nationalacademies.org/read/5787
- NCBI Bookshelf, *How Genomes Evolve*: https://www.ncbi.nlm.nih.gov/books/NBK26836/
- NCBI Bookshelf, *Evolution and Diversity*: https://www.ncbi.nlm.nih.gov/books/NBK217815/
- Stanford Encyclopedia of Philosophy, *Population Genetics*: https://plato.stanford.edu/entries/population-genetics/
- NCBI Bookshelf, *Genetics*: https://www.ncbi.nlm.nih.gov/books/NBK518809/
- NCBI PubMed: https://pubmed.ncbi.nlm.nih.gov/
- NCBI GenBank: https://www.ncbi.nlm.nih.gov/genbank/
- NCBI Gene: https://www.ncbi.nlm.nih.gov/gene/
- NCBI Genome: https://www.ncbi.nlm.nih.gov/datasets/genome/
- European Nucleotide Archive: https://www.ebi.ac.uk/ena
- Ensembl: https://www.ensembl.org/
- UniProt: https://www.uniprot.org/
- Tree of Life Web Project (historical reference; verify status of individual content): http://tolweb.org/tree/

## Search plan by discipline
Create a separate search log for each discipline with query, database, date, filters, inclusion/exclusion criteria, number screened, number included, and reviewer notes.

1. Evolutionary biology and natural selection.
2. Population genetics and quantitative genetics.
3. Molecular evolution, mutation, repair, and recombination.
4. Phylogenetics, phylogenomics, and ancestral reconstruction.
5. Evo-devo, morphology, anatomy, and comparative physiology.
6. Paleontology, fossils, and historical biogeography.
7. Ecology, conservation, and population dynamics.
8. Microbial evolution, horizontal gene transfer, and antimicrobial resistance.
9. Viral evolution and RNA-genome variation.
10. Epigenetics, gene regulation, transcriptomics, and proteomics.
11. CRISPR systems, genome editing, gene regulation, diagnostics, and editing outcomes.
12. Non-genetic experimental approaches and observational evidence.
13. Mathematical biology: probability, statistics, differential equations, dynamical systems, information theory, graph theory, and optimization.
14. Bioinformatics, reproducible pipelines, databases, and data standards.
15. Synthetic biology, biotechnology, biosafety, ethics, governance, and societal impacts.

## Evidence labels
- **Established mechanism:** supported by multiple independent lines of evidence and broad scientific consensus.
- **Replicated empirical result:** directly observed in studies and replicated in relevant settings.
- **Context-dependent result:** supported only under specified organisms, conditions, or measurement methods.
- **Model prediction:** computational or mathematical result requiring empirical validation.
- **Hypothesis:** testable proposal with defined supporting and falsifying outcomes.
- **Speculation:** idea not yet operationalized into a testable, sufficiently constrained claim.
- **Conflicting evidence:** credible findings disagree or are sensitive to assumptions.
- **Unresolved:** evidence is currently insufficient to choose among explanations.

Do not use “proven” to mean absolute certainty. Mathematical derivations can prove implications of assumptions; empirical biology is assessed through evidence, replication, uncertainty, and the ability of explanations to survive serious attempts at falsification.

## Literature record schema
Each record should include:
- stable identifier (DOI, PMID, accession, ISBN, or persistent URL);
- full citation, authors, year, title, journal/publisher, and document type;
- peer-review status and version;
- organisms/taxa, biological scale, and research domain;
- research question, hypothesis, methods, sample/data source, and controls;
- key findings with effect sizes and uncertainty where available;
- limitations, confounders, alternative explanations, and null findings;
- code/data availability and reproducibility notes;
- evidence label, curator notes, and last-reviewed date;
- links to related archive records and equations.

## Mathematical review requirements
For every equation, document variable definitions, units, assumptions, parameter provenance, valid domain, boundary conditions, uncertainty, and empirical validation. Check dimensional consistency. Separate deterministic identities, stochastic models, statistical estimates, fitted models, and illustrative equations. Never present a model output as observed biological fact.

## Deliverables
- Search protocol and reproducible search logs.
- Annotated bibliography grouped by discipline.
- Evidence map separating consensus, open questions, and speculative ideas.
- Equation catalogue with assumptions and units.
- Data-source register and ingestion provenance.
- Reproducible analysis notebooks or scripts.
- Periodic update reports listing newly indexed papers and changed conclusions.

## Initial orientation
Evolutionary biology is the broad term for studying evolution. Population genetics, molecular evolution, phylogenetics, evo-devo, comparative biology, and experimental evolution are important subfields. Evolution occurs at the population/lineage level across generations; an individual organism can develop, acclimate, learn, or change physiologically during its lifetime, but those changes are not automatically biological evolution.
