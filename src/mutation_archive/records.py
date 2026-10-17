"""Validation and normalization helpers for archive records."""
from __future__ import annotations
import hashlib
import json
from .core import validate_sequence
from .models import Variant

VALID_VARIANT_TYPES = {"SNV", "MNV", "insertion", "deletion", "indel", "substitution", "RNA_editing", "other"}
VALID_EVIDENCE = {"observed", "experimentally_supported", "computational_prediction", "clinical_interpretation", "hypothesis", "illustrative", "conflicting"}

def sequence_sha256(sequence: str) -> str:
    normalized = "".join(sequence.split()).upper().encode("ascii")
    return hashlib.sha256(normalized).hexdigest()

def validate_variant(record: Variant) -> list[str]:
    errors: list[str] = []
    if not record.record_id.strip(): errors.append("record_id is required")
    if record.molecule_type not in {"DNA", "RNA"}: errors.append("molecule_type must be DNA or RNA")
    if record.variant_type not in VALID_VARIANT_TYPES: errors.append(f"unsupported variant_type: {record.variant_type}")
    if record.evidence_status not in VALID_EVIDENCE: errors.append("invalid evidence_status")
    if record.start_pos is not None and record.start_pos < 1: errors.append("start_pos must be >= 1")
    if record.end_pos is not None and record.end_pos < 1: errors.append("end_pos must be >= 1")
    if record.start_pos is not None and record.end_pos is not None and record.end_pos < record.start_pos:
        errors.append("end_pos must be >= start_pos")
    if record.evidence_status == "illustrative" and not record.illustrative:
        errors.append("illustrative evidence must set illustrative=true")
    return errors

def validate_sequence_record(molecule: str, sequence: str) -> dict:
    ok, message = validate_sequence(molecule, sequence)
    normalized = "".join(sequence.split()).upper()
    return {"valid": ok, "message": message, "length": len(normalized), "sha256": sequence_sha256(normalized) if ok else None}

def dumps_variant(record: Variant) -> str:
    return json.dumps(record.to_dict(), sort_keys=True, indent=2)
