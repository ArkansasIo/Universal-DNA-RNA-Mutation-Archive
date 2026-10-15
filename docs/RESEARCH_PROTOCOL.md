# Research protocol and evidence policy

## Evidence labels
- `observed`: reported in a sequence or variation dataset; not necessarily functionally validated.
- `experimentally_supported`: effect measured in an experiment.
- `clinical_interpretation`: source-specific clinical assertion with scope retained.
- `computational_prediction`: model-generated prediction, not direct proof.
- `hypothesis`: proposed but not established.
- `illustrative`: synthetic software test data only.
- `conflicting`: credible sources disagree.

## Minimum provenance
Store organism and taxon ID, molecule type, reference accession/version, coordinate convention, alleles, original record ID, source URL, source release, retrieval date, normalization method, evidence class, publication link, and license/terms.

## Quality controls
1. Validate sequence alphabet and lengths.
2. Verify reference allele against the exact reference version.
3. Normalize variants against the declared reference, retaining original representation.
4. Separate DNA variants, RNA-genome variants, RNA editing, and epigenetic changes.
5. Do not equate presence with causality, pathogenicity, or adaptation.
6. Track missingness, ascertainment bias, and conflicting evidence.
7. Publish coverage counts by source, taxon, molecule type, variant class, and evidence status.

## Thesis deliverables
Literature review; source coverage matrix; database/data dictionary; reproducible import pipeline; descriptive mutation spectra; statistical models with uncertainty and diagnostics; comparative analysis with confounders; limitations and reproducibility statement.
