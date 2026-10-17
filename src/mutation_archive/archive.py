"""In-memory archive service with deterministic validation and search."""
from __future__ import annotations
from dataclasses import dataclass, field
from .models import Variant
from .records import validate_variant

@dataclass
class MutationArchive:
    variants: dict[str, Variant] = field(default_factory=dict)

    def add(self, variant: Variant, *, replace: bool = False) -> None:
        errors = validate_variant(variant)
        if errors: raise ValueError("; ".join(errors))
        if variant.record_id in self.variants and not replace:
            raise KeyError(f"duplicate record_id: {variant.record_id}")
        self.variants[variant.record_id] = variant

    def get(self, record_id: str) -> Variant | None:
        return self.variants.get(record_id)

    def search(self, query: str) -> list[Variant]:
        q = query.casefold()
        return [v for v in self.variants.values() if q in " ".join(filter(None, [v.record_id, v.accession, v.gene_id, v.gene_symbol, v.scientific_name, v.variant_name if hasattr(v, 'variant_name') else None])).casefold()]

    def by_evidence(self, evidence: str) -> list[Variant]:
        return [v for v in self.variants.values() if v.evidence_status == evidence]

    def stats(self) -> dict[str, int]:
        result = {"total": len(self.variants)}
        for v in self.variants.values():
            result[f"molecule:{v.molecule_type}"] = result.get(f"molecule:{v.molecule_type}", 0) + 1
            result[f"evidence:{v.evidence_status}"] = result.get(f"evidence:{v.evidence_status}", 0) + 1
        return result
