"""Tests for gc."""
from pathlib import Path
from rosalind_problems.problems.gc import main
from rosalind_problems.utils import testing_utils

FIXTURES = Path("tests/test_problems/test_gc/fixtures")

def test_gc():
	"""TEST - main function of gc solved the sample problem."""
	sample_dataset, sample_solution = testing_utils.get_samples(FIXTURES)
	assert main.gc(sample_dataset) == sample_solution