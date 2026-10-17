# Universal DNA & RNA Mutation Archive

A provenance-first research platform for cataloguing published DNA and RNA variants across organisms. The project provides sequence validation, deterministic comparison, mathematical models, typed archive records, JSON/JSONL/FASTA I/O, a searchable in-memory archive, and SQL schemas for persistent storage.

> **Scientific scope:** this repository is an archival/research software system. A sequence difference is not, by itself, evidence of pathogenicity, adaptation, causality, or clinical significance. Synthetic records are explicitly labelled.

## Architecture

```text
src/mutation_archive/
  core.py        # sequence validation and mathematical utilities
  models.py      # Provenance and Variant domain models
  records.py     # validation and sequence hashing
  io.py          # JSON, JSONL, FASTA import/export
  archive.py     # in-memory archive/search service
  cli.py         # command-line interface
  __main__.py    # python -m mutation_archive

data/examples/  # synthetic test records only
sql/             # PostgreSQL reference schema + MySQL schema
 tests/           # unit tests
.github/workflows # continuous integration
```

## Quick start

Python 3.10+ and the standard library are sufficient for the core package.

```bash
python -m unittest discover -s tests -v
pip install -e .
mutation-archive validate-sequence DNA ACGTN
mutation-archive compare DNA ACGT ACCT
mutation-archive stats data/examples/variants.json
```

The package can also be invoked with:

```bash
python -m mutation_archive validate-sequence RNA ACGUN
```

## Data model

Every archived variant should retain, where available:

- source database and URL
- accession and version
- reference sequence/version
- coordinate system
- molecule type
- variant type
- source release
- retrieval timestamp
- transformation/provenance information
- evidence classification
- whether a record is synthetic/illustrative

Evidence vocabulary:

- `observed` — reported in a sequence or variation dataset
- `experimentally_supported` — effect measured experimentally
- `computational_prediction` — inferred by a model
- `clinical_interpretation` — source-specific clinical assertion
- `hypothesis` — not established
- `illustrative` — synthetic software test record
- `conflicting` — credible evidence disagrees

## SQL

`sql/schema.sql` contains the existing PostgreSQL-oriented reference schema. `sql/mysql_schema.sql` provides a MySQL/InnoDB implementation suitable for a production deployment after environment-specific review.

## Public sources planned for integration

- NCBI GenBank / Variation / ClinVar / Taxonomy
- NCBI Virus
- Ensembl / Ensembl Genomes
- European Nucleotide Archive
- European Variation Archive
- RNAcentral
- Rfam
- UniProt

Importers should preserve source accession, reference version, retrieval date, source release, license/terms, and evidence classification. Do not silently overwrite source records.

## Development principles

1. Preserve provenance before normalization.
2. Never manufacture biological conclusions from sequence differences.
3. Keep synthetic data separate from public biological observations.
4. Make transformations deterministic and testable.
5. Prefer source-versioned records over mutable interpretations.
6. Treat coordinate systems explicitly; never assume a database coordinate convention.
7. Keep clinical interpretation separate from raw observation.

## License

The repository's software implementation is intended to use the MIT License; confirm the final licensing terms before redistributing third-party datasets, which may have separate terms.
