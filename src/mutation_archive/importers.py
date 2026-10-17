"""Safe local import pipelines.

Network retrieval is intentionally not embedded here. External adapters should
fetch data separately, preserve the exact source payload/version, then hand
normalized records to these functions.
"""
from __future__ import annotations
import csv
from pathlib import Path
from .models import Variant, Provenance
from .archive import MutationArchive

def import_csv(path: str | Path, archive: MutationArchive, *, source_database: str, source_url: str) -> int:
    count = 0
    with Path(path).open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            provenance = Provenance(source_database=source_database, source_url=source_url)
            variant = Variant(
                record_id=row["record_id"], molecule_type=row["molecule_type"],
                variant_type=row["variant_type"], coordinate_system=row.get("coordinate_system", "unspecified"),
                reference_allele=row.get("reference_allele") or None,
                alternate_allele=row.get("alternate_allele") or None,
                accession=row.get("accession") or None,
                start_pos=int(row["start_pos"]) if row.get("start_pos") else None,
                end_pos=int(row["end_pos"]) if row.get("end_pos") else None,
                organism_taxon_id=row.get("organism_taxon_id") or None,
                scientific_name=row.get("scientific_name") or None,
                gene_id=row.get("gene_id") or None,
                gene_symbol=row.get("gene_symbol") or None,
                evidence_status=row.get("evidence_status", "observed"),
                interpretation=row.get("interpretation") or None,
                provenance=provenance,
                illustrative=row.get("illustrative", "false").lower() in {"1", "true", "yes"},
            )
            archive.add(variant); count += 1
    return count
