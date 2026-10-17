"""Optional MySQL persistence adapter.

The core archive remains dependency-free. Install ``mysql-connector-python``
when MySQL persistence is required.
"""
from __future__ import annotations

from collections.abc import Iterable
from typing import Any

from .models import Provenance, Variant


class MySQLArchive:
    """Small repository adapter for the normalized MySQL schema."""

    def __init__(self, connection: Any):
        self.connection = connection

    @classmethod
    def connect(cls, **kwargs: Any) -> "MySQLArchive":
        try:
            import mysql.connector
        except ImportError as exc:
            raise RuntimeError(
                "MySQL support requires mysql-connector-python; install the optional dependency."
            ) from exc
        return cls(mysql.connector.connect(**kwargs))

    def close(self) -> None:
        self.connection.close()

    def insert_variant(self, variant: Variant) -> None:
        cursor = self.connection.cursor()
        try:
            if variant.provenance:
                cursor.execute(
                    """
                    INSERT INTO provenance
                      (source_database, source_url, retrieved_at, source_release,
                       source_record_version, license_or_terms, checksum_sha256,
                       transformation_steps_json)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    """,
                    (
                        variant.provenance.source_database,
                        variant.provenance.source_url,
                        variant.provenance.retrieved_at,
                        variant.provenance.source_release,
                        variant.provenance.source_record_version,
                        variant.provenance.license_or_terms,
                        variant.provenance.checksum_sha256,
                        __import__("json").dumps(variant.provenance.transformation_steps),
                    ),
                )
                provenance_id = cursor.lastrowid
            else:
                provenance_id = None

            cursor.execute(
                """
                INSERT INTO variants
                  (record_id, molecule_type, variant_type, variant_name,
                   coordinate_system, reference_allele, alternate_allele,
                   accession, start_pos, end_pos, organism_taxon_id,
                   scientific_name, gene_id, gene_symbol, evidence_status,
                   interpretation, provenance_id, illustrative, extra_json)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    variant.record_id,
                    variant.molecule_type,
                    variant.variant_type,
                    variant.variant_name,
                    variant.coordinate_system,
                    variant.reference_allele,
                    variant.alternate_allele,
                    variant.accession,
                    variant.start_pos,
                    variant.end_pos,
                    variant.organism_taxon_id,
                    variant.scientific_name,
                    variant.gene_id,
                    variant.gene_symbol,
                    variant.evidence_status,
                    variant.interpretation,
                    provenance_id,
                    variant.illustrative,
                    __import__("json").dumps(variant.extra),
                ),
            )
            self.connection.commit()
        except Exception:
            self.connection.rollback()
            raise
        finally:
            cursor.close()

    def insert_many(self, variants: Iterable[Variant]) -> int:
        count = 0
        for variant in variants:
            self.insert_variant(variant)
            count += 1
        return count
