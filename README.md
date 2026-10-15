# Universal DNA & RNA Mutation Archive

A provenance-first research platform for cataloguing published DNA and RNA variants across organisms, with sequence validation, mathematical models, and reproducible import pipelines.

## Scope
The goal is a broad, continuously maintained catalogue—not a claim that this repository already contains every mutation ever discovered. No single public database covers every taxon, molecule, variant class, and publication. Coverage must be reported by source and version.

## Initial modules
- Python sequence validation and equal-length sequence comparison
- Mutation probability and simple selection models
- SQL schema for organisms, reference sequences, genes, variants, effects, experiments, publications, and provenance
- Data dictionary, research protocol, and import plan
- Clearly labelled synthetic test data (not biological claims)

## Public data sources to integrate
- NCBI GenBank / Variation / ClinVar / Taxonomy: https://www.ncbi.nlm.nih.gov/
- NCBI Virus: https://www.ncbi.nlm.nih.gov/labs/virus/
- Ensembl and Ensembl Genomes: https://www.ensembl.org/
- European Nucleotide Archive: https://www.ebi.ac.uk/ena
- European Variation Archive: https://www.ebi.ac.uk/eva/
- RNAcentral: https://rnacentral.org/
- Rfam: https://rfam.org/
- UniProt: https://www.uniprot.org/

Always retain source accession, reference version, coordinate convention, retrieval date, source release, license/terms, and evidence classification. Database presence alone is not proof of biological effect.

## Quick start
Python 3.10+; standard library only for the starter core.

```bash
python -m unittest discover -s tests
python -m mutation_archive.cli validate-sequence DNA ACGTN
python -m mutation_archive.cli compare DNA ACGT ACCT
```

Install as a package with `pip install -e .`.

## Mathematical models
See `docs/MATHEMATICAL_FRAMEWORK.md` for probability, mutation accumulation, sequence distance, selection, and model assumptions.

## Evidence vocabulary
- `observed`: reported in a sequence or variation dataset; not necessarily functionally validated
- `experimentally_supported`: effect measured experimentally
- `computational_prediction`: inferred by a model
- `clinical_interpretation`: source-specific clinical assertion
- `hypothesis`: not established
- `illustrative`: synthetic software test record
- `conflicting`: credible evidence disagrees

## Important limitations
Variant consequences depend on the organism, reference sequence, transcript, genetic background, and environment. Do not infer pathogenicity or adaptation from sequence difference alone. DNA variants, RNA-genome variants, RNA editing, and epigenetic changes are distinct record types and should not be conflated.

## Research documentation

- [Theory catalog](docs/THEORY_CATALOG.md)
- [Mathematical models: algebra, calculus, probability, and statistics](docs/MATHEMATICAL_MODELS.md)
- [Logic statements and true/false claim classifications](docs/LOGIC_AND_TRUTH_CLAIMS.md)
- [Hypotheses and mathematical proof obligations](docs/HYPOTHESES_AND_PROOF_OBLIGATIONS.md)
- [Comparative mutation dynamics thesis](docs/THESIS_MUTATION_DYNAMICS.md)
- [System design document](docs/SYSTEM_DESIGN_DOCUMENT.md)

## CRISPR, speculative research, and evolution
- [CRISPR research framework](docs/CRISPR_RESEARCH_FRAMEWORK.md)
- [Speculative hypotheses and research ideas](docs/SPECULATIVE_HYPOTHESES_AND_RESEARCH_IDEAS.md)
- [Applications to life and evolution](docs/LIFE_EVOLUTION_APPLICATIONS.md)
- [Why mutations exist and whether to engineer them](docs/WHY_MUTATIONS_EXIST_AND_WHETHER_TO_ENGINEER_THEM.md)
