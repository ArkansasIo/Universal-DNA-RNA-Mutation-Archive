"""JSON, JSONL and FASTA import/export utilities using the standard library."""
from __future__ import annotations
import json
from pathlib import Path
from collections.abc import Iterable
from .models import Variant

def read_variants_json(path: str | Path) -> list[Variant]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if isinstance(data, dict): data = data.get("variants", [data])
    return [Variant.from_dict(item) for item in data]

def write_variants_json(path: str | Path, variants: Iterable[Variant]) -> None:
    payload = {"schema_version": "1.0", "variants": [v.to_dict() for v in variants]}
    Path(path).write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")

def read_variants_jsonl(path: str | Path) -> list[Variant]:
    result = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if line.strip(): result.append(Variant.from_dict(json.loads(line)))
    return result

def write_variants_jsonl(path: str | Path, variants: Iterable[Variant]) -> None:
    with Path(path).open("w", encoding="utf-8") as handle:
        for variant in variants:
            handle.write(json.dumps(variant.to_dict(), sort_keys=True) + "\n")

def read_fasta(path: str | Path) -> list[tuple[str, str]]:
    records: list[tuple[str, str]] = []
    header = None
    chunks: list[str] = []
    for raw in Path(path).read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line: continue
        if line.startswith(">"):
            if header is not None: records.append((header, "".join(chunks)))
            header, chunks = line[1:].strip(), []
        elif header is not None:
            chunks.append(line)
        else:
            raise ValueError("FASTA sequence encountered before header")
    if header is not None: records.append((header, "".join(chunks)))
    return records
