# System Design Document: Universal Mutation Archive

## 1. Purpose
Build a versioned, source-attributed archive for public DNA and RNA variant records, analysis methods, mathematical models, and evidence. The platform must represent uncertainty and coverage gaps rather than claiming exhaustive knowledge.

## 2. Functional requirements
- Import public records using documented source interfaces.
- Preserve original records and accession/version identifiers.
- Normalize variants relative to a declared reference and coordinate system.
- Separate observed variants, RNA editing, recombination, predictions, and synthetic examples.
- Link variants to organisms, genes, transcripts, proteins, experiments, and publications.
- Validate sequence alphabets and reference alleles.
- Provide source/taxon/type coverage reports.
- Track source release, retrieval date, transformations, and license terms.
- Export reproducible CSV/JSON/SQL subsets.
- Support mathematical analysis with assumptions and parameter units.

## 3. Non-functional requirements
Reproducibility, traceability, data integrity, resumable bulk ingestion, interoperability, secure credentials, respect for source terms, and transparent uncertainty.

## 4. Logical architecture
1. Source adapters: NCBI, Ensembl, EVA, ENA, RNAcentral, Rfam, and future providers.
2. Raw landing zone: immutable snapshots where terms permit.
3. Parser/validator: schema checks, alphabet checks, reference verification, coordinate conventions.
4. Normalization layer: canonical variant representation while retaining original representation.
5. Relational database: organisms, references, genes, variants, effects, experiments, publications, provenance.
6. Analysis layer: mutation spectra, statistical models, sequence comparisons, uncertainty estimates.
7. Reporting layer: coverage, rejected records, freshness, and evidence summaries.
8. Optional API/UI: query by organism, accession, variant type, source, or evidence status.

## 5. Ingestion lifecycle
DISCOVERED → DOWNLOADED → PARSED → VALIDATED → NORMALIZED → LINKED → PUBLISHED.
A record may instead enter REJECTED or QUARANTINED with a machine-readable reason. Never silently discard data.

## 6. Core validation rules
- Source ID is unique within source/version.
- Reference accession and version are explicit.
- Coordinate convention is required.
- Reference allele matches the selected reference where applicable.
- DNA and RNA alphabets are validated separately.
- Missing values remain missing; do not invent names.
- Predicted effects carry method and version.
- Clinical assertions retain source and review status.
- Synthetic test records are excluded from scientific counts.

## 7. Proposed API routes (not yet implemented)
- GET /organisms/{taxon_id}
- GET /references/{accession_version}
- GET /variants?taxon_id=&type=&source=&evidence=
- GET /variants/{source}/{record_id}
- GET /coverage?source=&taxon_group=&molecule_type=
- GET /models/{model_id}
- GET /provenance/{entity_type}/{entity_key}

## 8. Testing strategy
Unit tests for sequence validation and equations; integration tests with fixed fixtures; importer contract tests; reference-allele verification; regression tests on versioned datasets; and manual review of stratified samples.

## 9. Operational metrics
Records discovered/imported/rejected; validation failure rate; duplicate rate; source freshness; fraction with reference versions; evidence coverage; and counts by taxon, molecule, and variant class.

## 10. Risks and mitigations
- Incomplete coverage: publish source-specific coverage reports.
- Incorrect normalization: retain originals and reference versions.
- False causal claims: separate annotation from evidence.
- Licensing conflicts: record terms and constrain exports.
- Data drift: version snapshots and algorithms.
- Overgeneralization: stratify by organism and genome system.
