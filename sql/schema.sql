-- PostgreSQL-oriented schema; adapt JSONB and identity types for MySQL.
CREATE TABLE organisms (
  organism_id BIGSERIAL PRIMARY KEY,
  taxon_id TEXT NOT NULL,
  scientific_name TEXT NOT NULL,
  common_name TEXT,
  taxonomic_rank TEXT,
  taxonomy_source TEXT NOT NULL,
  UNIQUE (taxon_id, taxonomy_source)
);

CREATE TABLE reference_sequences (
  reference_id BIGSERIAL PRIMARY KEY,
  organism_id BIGINT REFERENCES organisms(organism_id),
  accession TEXT NOT NULL,
  accession_version TEXT,
  molecule_type TEXT NOT NULL CHECK (molecule_type IN ('DNA','RNA','protein')),
  sequence_length BIGINT,
  assembly_name TEXT,
  release_label TEXT,
  source_database TEXT NOT NULL,
  source_url TEXT NOT NULL,
  retrieved_at TIMESTAMPTZ NOT NULL,
  checksum_sha256 TEXT,
  UNIQUE (accession, accession_version, source_database)
);

CREATE TABLE genes (
  gene_id BIGSERIAL PRIMARY KEY,
  organism_id BIGINT REFERENCES organisms(organism_id),
  stable_id TEXT,
  symbol TEXT,
  name TEXT,
  reference_id BIGINT REFERENCES reference_sequences(reference_id),
  start_pos BIGINT,
  end_pos BIGINT,
  strand SMALLINT CHECK (strand IN (-1,1)),
  annotation_source TEXT,
  annotation_version TEXT
);

CREATE TABLE variants (
  variant_id BIGSERIAL PRIMARY KEY,
  organism_id BIGINT REFERENCES organisms(organism_id),
  reference_id BIGINT NOT NULL REFERENCES reference_sequences(reference_id),
  record_id TEXT NOT NULL,
  variant_name TEXT,
  variant_type TEXT NOT NULL,
  coordinate_system TEXT NOT NULL,
  start_pos BIGINT,
  end_pos BIGINT,
  reference_allele TEXT,
  alternate_allele TEXT,
  sequence_accession TEXT,
  normalization_method TEXT,
  evidence_status TEXT NOT NULL,
  interpretation TEXT,
  source_database TEXT NOT NULL,
  source_url TEXT NOT NULL,
  source_record_version TEXT,
  retrieved_at TIMESTAMPTZ NOT NULL,
  is_illustrative BOOLEAN NOT NULL DEFAULT FALSE,
  UNIQUE (source_database, record_id, source_record_version)
);

CREATE TABLE variant_effects (
  effect_id BIGSERIAL PRIMARY KEY,
  variant_id BIGINT NOT NULL REFERENCES variants(variant_id),
  gene_id BIGINT REFERENCES genes(gene_id),
  consequence_term TEXT,
  transcript_accession TEXT,
  protein_accession TEXT,
  evidence_kind TEXT NOT NULL,
  method_name TEXT,
  method_version TEXT,
  evidence_summary TEXT,
  confidence_score DOUBLE PRECISION,
  score_scale TEXT,
  source_url TEXT
);

CREATE TABLE experiments (
  experiment_id BIGSERIAL PRIMARY KEY,
  title TEXT NOT NULL,
  method TEXT NOT NULL,
  hypothesis TEXT,
  controls TEXT,
  replicate_count INTEGER,
  conditions JSONB,
  results_summary TEXT,
  dataset_url TEXT
);

CREATE TABLE publications (
  publication_id BIGSERIAL PRIMARY KEY,
  doi TEXT UNIQUE,
  pmid TEXT,
  title TEXT NOT NULL,
  authors TEXT,
  publication_year INTEGER,
  journal TEXT,
  url TEXT,
  evidence_type TEXT
);

CREATE TABLE provenance (
  provenance_id BIGSERIAL PRIMARY KEY,
  entity_type TEXT NOT NULL,
  entity_key TEXT NOT NULL,
  source_database TEXT NOT NULL,
  source_url TEXT NOT NULL,
  retrieved_at TIMESTAMPTZ NOT NULL,
  release_label TEXT,
  checksum_sha256 TEXT,
  transformation_steps JSONB,
  license_or_terms TEXT
);

CREATE INDEX idx_variants_record_id ON variants(record_id);
CREATE INDEX idx_variants_type ON variants(variant_type);
CREATE INDEX idx_variants_source ON variants(source_database);
CREATE INDEX idx_genes_stable_id ON genes(stable_id);
