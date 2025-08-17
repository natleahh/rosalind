"""Tests for dna."""
from pathlib import Path
from rosalind_problems.problems.dna import main
from rosalind_problems.utils import testing_utils

FIXTURES = Path("tests/test_problems/test_dna/fixtures")

def test_dna():
	"""TEST - main function of dna solved the sample problem."""
	sample_dataset, sample_solution = testing_utils.get_samples(FIXTURES)
	assert main.dna(sample_dataset) == sample_solution