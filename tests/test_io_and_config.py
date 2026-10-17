import json
from pathlib import Path

from mutation_archive.config import Settings
from mutation_archive.io import read_fasta, read_variants_json, write_variants_json
from mutation_archive.models import Variant


def test_json_round_trip(tmp_path: Path):
    path = tmp_path / "variants.json"
    source = Variant(
        record_id="T1",
        molecule_type="DNA",
        variant_type="SNV",
        coordinate_system="sequence-relative-1based",
        reference_allele="A",
        alternate_allele="G",
        evidence_status="illustrative",
        illustrative=True,
    )
    write_variants_json(path, [source])
    loaded = read_variants_json(path)
    assert loaded[0].record_id == "T1"
    assert loaded[0].alternate_allele == "G"


def test_fasta_reader(tmp_path: Path):
    path = tmp_path / "sample.fa"
    path.write_text(">seq1 description\nACGT\nAC\n>seq2\nNN\n", encoding="utf-8")
    assert read_fasta(path) == [("seq1 description", "ACGTAC"), ("seq2", "NN")]


def test_example_json_is_valid():
    path = Path("data/examples/variants.json")
    payload = json.loads(path.read_text(encoding="utf-8"))
    assert payload["variants"][0]["illustrative"] is True


def test_default_settings_are_safe():
    settings = Settings()
    assert settings.host == "127.0.0.1"
    assert settings.mysql_password is None
