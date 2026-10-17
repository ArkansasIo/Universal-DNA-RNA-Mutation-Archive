CREATE DATABASE IF NOT EXISTS mutation_archive CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE mutation_archive;

CREATE TABLE organisms (
  organism_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  taxon_id VARCHAR(128) NOT NULL,
  scientific_name VARCHAR(512) NOT NULL,
  common_name VARCHAR(512),
  taxonomic_rank VARCHAR(64),
  taxonomy_source VARCHAR(255) NOT NULL,
  UNIQUE KEY uq_organism_taxon_source (taxon_id, taxonomy_source)
) ENGINE=InnoDB;

CREATE TABLE reference_sequences (
  reference_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  organism_id BIGINT UNSIGNED,
  accession VARCHAR(255) NOT NULL,
  accession_version VARCHAR(64),
  molecule_type ENUM('DNA','RNA','protein') NOT NULL,
  sequence_length BIGINT UNSIGNED,
  assembly_name VARCHAR(255),
  release_label VARCHAR(255),
  source_database VARCHAR(255) NOT NULL,
  source_url TEXT NOT NULL,
  retrieved_at DATETIME(6) NOT NULL,
  checksum_sha256 CHAR(64),
  UNIQUE KEY uq_reference (accession, accession_version, source_database),
  CONSTRAINT fk_reference_organism FOREIGN KEY (organism_id) REFERENCES organisms(organism_id)
) ENGINE=InnoDB;

CREATE TABLE genes (
  gene_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  organism_id BIGINT UNSIGNED,
  stable_id VARCHAR(255), symbol VARCHAR(255), name TEXT,
  reference_id BIGINT UNSIGNED, start_pos BIGINT UNSIGNED, end_pos BIGINT UNSIGNED,
  strand TINYINT, annotation_source VARCHAR(255), annotation_version VARCHAR(255),
  INDEX idx_gene_stable_id (stable_id),
  FOREIGN KEY (organism_id) REFERENCES organisms(organism_id),
  FOREIGN KEY (reference_id) REFERENCES reference_sequences(reference_id),
  CHECK (strand IN (-1,1) OR strand IS NULL)
) ENGINE=InnoDB;

CREATE TABLE variants (
  variant_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  organism_id BIGINT UNSIGNED, reference_id BIGINT UNSIGNED NOT NULL,
  record_id VARCHAR(255) NOT NULL, variant_name VARCHAR(512),
  variant_type VARCHAR(64) NOT NULL, coordinate_system VARCHAR(128) NOT NULL,
  start_pos BIGINT UNSIGNED, end_pos BIGINT UNSIGNED,
  reference_allele TEXT, alternate_allele TEXT, sequence_accession VARCHAR(255),
  normalization_method VARCHAR(255), evidence_status VARCHAR(64) NOT NULL,
  interpretation TEXT, source_database VARCHAR(255) NOT NULL, source_url TEXT NOT NULL,
  source_record_version VARCHAR(255), retrieved_at DATETIME(6) NOT NULL,
  is_illustrative BOOLEAN NOT NULL DEFAULT FALSE,
  UNIQUE KEY uq_variant_source (source_database, record_id, source_record_version),
  INDEX idx_variant_record (record_id), INDEX idx_variant_type (variant_type), INDEX idx_variant_source (source_database),
  FOREIGN KEY (organism_id) REFERENCES organisms(organism_id),
  FOREIGN KEY (reference_id) REFERENCES reference_sequences(reference_id)
) ENGINE=InnoDB;

CREATE TABLE provenance (
  provenance_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  entity_type VARCHAR(128) NOT NULL, entity_key VARCHAR(255) NOT NULL,
  source_database VARCHAR(255) NOT NULL, source_url TEXT NOT NULL,
  retrieved_at DATETIME(6) NOT NULL, release_label VARCHAR(255),
  checksum_sha256 CHAR(64), transformation_steps JSON, license_or_terms TEXT,
  INDEX idx_provenance_entity (entity_type, entity_key)
) ENGINE=InnoDB;
