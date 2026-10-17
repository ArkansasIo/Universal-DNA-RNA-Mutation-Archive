"""In-memory archive service with deterministic validation and search."""
from __future__ import annotations

from dataclasses import dataclass, field

from .models import Variant
from .records import validate_variant


@dataclass
class MutationArchive:
    """Validated in-memory collection of mutation records."""

    variants: dict[str, Variant] = field(default_factory=dict)

    def add(self, variant: Variant, *, replace: bool = False) -> None:
        errors = validate_variant(variant)
        if errors:
            raise ValueError("; ".join(errors))
        if variant.record_id in self.variants and not replace:
            raise KeyError(f"duplicate record_id: {variant.record_id}")
        self.variants[variant.record_id] = variant

    def add_many(self, variants: list[Variant], *, replace: bool = False) -> int:
        """Add a batch and return the number of records accepted."""
        for variant in variants:
            self.add(variant, replace=replace)
        return len(variants)

    def get(self, record_id: str) -> Variant | None:
        return self.variants.get(record_id)

    def search(self, query: str) -> list[Variant]:
        q = query.strip().casefold()
        if not q:
            return list(self.variants.values())
        fields = (
            "record_id",
            "variant_name",
            "accession",
            "gene_id",
            "gene_symbol",
            "scientific_name",
            "interpretation",
        )
        matches: list[Variant] = []
        for variant in self.variants.values():
            haystack = " ".join(
                str(getattr(variant, name) or "") for name in fields
            ).casefold()
            if q in haystack:
                matches.append(variant)
        return matches

    def by_evidence(self, evidence: str) -> list[Variant]:
        return [
            variant
            for variant in self.variants.values()
            if variant.evidence_status == evidence
        ]

    def by_molecule(self, molecule_type: str) -> list[Variant]:
        molecule = molecule_type.upper()
        return [
            variant
            for variant in self.variants.values()
            if variant.molecule_type == molecule
        ]

    def stats(self) -> dict[str, int]:
        result = {"total": len(self.variants)}
        for variant in self.variants.values():
            molecule_key = f"molecule:{variant.molecule_type}"
            evidence_key = f"evidence:{variant.evidence_status}"
            result[molecule_key] = result.get(molecule_key, 0) + 1
            result[evidence_key] = result.get(evidence_key, 0) + 1
        return result
