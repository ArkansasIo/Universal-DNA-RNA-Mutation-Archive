import unittest
from mutation_archive.archive import MutationArchive
from mutation_archive.models import Variant, Provenance
from mutation_archive.records import sequence_sha256, validate_variant

class ArchiveTests(unittest.TestCase):
    def make_variant(self):
        return Variant(
            record_id="TEST-001", molecule_type="DNA", variant_type="SNV",
            coordinate_system="sequence-relative-1based", start_pos=3, end_pos=3,
            reference_allele="G", alternate_allele="A", accession="TESTSEQ.1",
            scientific_name="Synthetic test organism", evidence_status="illustrative",
            illustrative=True, provenance=Provenance("synthetic-test", "https://example.invalid/test"))

    def test_validate(self):
        self.assertEqual(validate_variant(self.make_variant()), [])

    def test_archive_add_and_stats(self):
        archive = MutationArchive(); archive.add(self.make_variant())
        self.assertEqual(archive.stats()["total"], 1)
        self.assertEqual(len(archive.by_evidence("illustrative")), 1)

    def test_duplicate_rejected(self):
        archive = MutationArchive(); archive.add(self.make_variant())
        with self.assertRaises(KeyError): archive.add(self.make_variant())

    def test_hash(self):
        self.assertEqual(len(sequence_sha256("ACGT")), 64)

if __name__ == "__main__": unittest.main()
