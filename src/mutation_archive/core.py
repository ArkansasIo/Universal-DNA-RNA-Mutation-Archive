"""Transparent starter utilities; not a clinical variant interpreter."""
from __future__ import annotations
import math

DNA_ALPHABET = set("ACGTN")
RNA_ALPHABET = set("ACGUN")

def validate_sequence(molecule: str, sequence: str) -> tuple[bool, str]:
    molecule = molecule.upper()
    seq = "".join(sequence.split()).upper()
    alphabet = DNA_ALPHABET if molecule == "DNA" else RNA_ALPHABET if molecule == "RNA" else None
    if alphabet is None:
        return False, "Molecule must be DNA or RNA."
    if not seq:
        return False, "Sequence is empty."
    invalid = sorted(set(seq) - alphabet)
    if invalid:
        return False, f"Invalid symbol(s) for {molecule}: {', '.join(invalid)}"
    return True, "Valid sequence alphabet."

def compare_equal_length(reference: str, alternate: str) -> dict:
    """Compare equal-length strings; positions are 1-based within supplied sequence."""
    ref, alt = reference.upper(), alternate.upper()
    if len(ref) != len(alt):
        raise ValueError("Sequences differ in length; use an alignment/indel-aware method.")
    changes = [
        {"position_1based": i + 1, "reference": a, "alternate": b}
        for i, (a, b) in enumerate(zip(ref, alt)) if a != b
    ]
    return {"reference_length": len(ref), "alternate_length": len(alt),
            "mismatch_count": len(changes), "mismatches": changes,
            "note": "Positions are relative to the supplied sequence, not genome coordinates."}

def probability_at_least_one(length: int, per_site_probability: float) -> float:
    """Independent equal-probability sites: P(M>=1)=1-(1-mu)^L."""
    if length < 0:
        raise ValueError("length must be >= 0")
    if not 0 <= per_site_probability <= 1:
        raise ValueError("per_site_probability must be in [0,1]")
    if length == 0 or per_site_probability == 0:
        return 0.0
    if per_site_probability == 1:
        return 1.0
    return -math.expm1(length * math.log1p(-per_site_probability))

def expected_events(length: int, per_site_probability: float, replications: int = 1) -> float:
    """Expected event count under a constant independent-site model."""
    if length < 0 or replications < 0:
        raise ValueError("length and replications must be >= 0")
    if not 0 <= per_site_probability <= 1:
        raise ValueError("per_site_probability must be in [0,1]")
    return length * per_site_probability * replications

def selection_step(p: float, s: float) -> float:
    """Haploid selection step; reference fitness=1, alternate fitness=1+s."""
    if not 0 <= p <= 1:
        raise ValueError("p must be in [0,1]")
    if 1 + p * s <= 0:
        raise ValueError("Mean fitness must be positive")
    return p * (1 + s) / (1 + p * s)
