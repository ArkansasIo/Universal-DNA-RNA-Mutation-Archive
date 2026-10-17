"""Typed domain records for the mutation archive.

These models describe archival observations; they do not determine clinical or
biological significance.
"""
from __future__ import annotations
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from typing import Any, Literal

Molecule = Literal["DNA", "RNA"]
Evidence = Literal[
    "observed", "experimentally_supported", "computational_prediction",
    "clinical_interpretation", "hypothesis", "illustrative", "conflicting"
]

@dataclass(slots=True)
class Provenance:
    source_database: str
    source_url: str
    retrieved_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    source_release: str | None = None
    source_record_version: str | None = None
    license_or_terms: str | None = None
    checksum_sha256: str | None = None
    transformation_steps: list[str] = field(default_factory=list)

@dataclass(slots=True)
class Variant:
    record_id: str
    molecule_type: Molecule
    variant_type: str
    coordinate_system: str
    reference_allele: str | None = None
    alternate_allele: str | None = None
    accession: str | None = None
    start_pos: int | None = None
    end_pos: int | None = None
    organism_taxon_id: str | None = None
    scientific_name: str | None = None
    gene_id: str | None = None
    gene_symbol: str | None = None
    evidence_status: Evidence = "observed"
    interpretation: str | None = None
    provenance: Provenance | None = None
    illustrative: bool = False
    extra: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Variant":
        value = dict(data)
        p = value.get("provenance")
        value["provenance"] = Provenance(**p) if isinstance(p, dict) else None
        return cls(**value)
