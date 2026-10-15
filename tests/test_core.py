import unittest
from mutation_archive.core import (
    validate_sequence, compare_equal_length, probability_at_least_one,
    expected_events, selection_step
)

class CoreTests(unittest.TestCase):
    def test_dna_valid(self):
        self.assertTrue(validate_sequence("DNA", "ACGTN")[0])
    def test_rna_rejects_t(self):
        self.assertFalse(validate_sequence("RNA", "ACT")[0])
    def test_mismatch(self):
        result = compare_equal_length("ACGT", "ACCT")
        self.assertEqual(result["mismatch_count"], 1)
        self.assertEqual(result["mismatches"][0]["position_1based"], 3)
    def test_probability(self):
        self.assertEqual(probability_at_least_one(0, 0.1), 0.0)
        self.assertGreater(probability_at_least_one(100, 0.01), 0.0)
    def test_expected_events(self):
        self.assertAlmostEqual(expected_events(1000, 1e-4, 2), 0.2)
    def test_selection(self):
        self.assertGreater(selection_step(0.2, 0.1), 0.2)

if __name__ == "__main__":
    unittest.main()
